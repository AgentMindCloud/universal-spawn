// universal-spawn validator core (Node).
//
// Public API:
//   validate(doc, opts) → { ok, errors[], warnings[], platformsChecked[] }
//   validateFile(path, opts)
//   loadMasterSchema()
//   loadPlatformSchema(path)

import { readFileSync, readdirSync, existsSync } from "node:fs";
import { dirname, extname, resolve, basename } from "node:path";
import { fileURLToPath } from "node:url";
import Ajv from "ajv/dist/ajv.js";
import addFormats from "ajv-formats";
import YAML from "yaml";

const __dirname = dirname(fileURLToPath(import.meta.url));
const BUNDLED = resolve(__dirname, "..", "v1.0.schema.json");

export const MASTER_ID =
  "https://universal-spawn.dev/spec/v1.0/universal-spawn.schema.json";

export function loadMasterSchema(path = BUNDLED) {
  return JSON.parse(readFileSync(path, "utf8"));
}

export function loadPlatformSchema(path) {
  return JSON.parse(readFileSync(path, "utf8"));
}

function _newAjv(masterSchema) {
  const ajv = new Ajv({
    allErrors: true,
    strict: false,
    schemas: [masterSchema],
  });
  addFormats(ajv);
  return ajv;
}

function _formatError(err) {
  const path = err.instancePath ? err.instancePath.replace(/^\//, "") : "<root>";
  return `${path || "<root>"}: ${err.message}`;
}

function _loadDoc(source) {
  if (typeof source === "object" && source !== null && !Buffer.isBuffer(source)) {
    return source;
  }
  const path = String(source);
  const text = readFileSync(path, "utf8");
  const ext = extname(path).toLowerCase();
  if (ext === ".json") return JSON.parse(text);
  // YAML covers .yaml, .yml, and is a JSON superset.
  return YAML.parse(text);
}

export function validate(source, opts = {}) {
  const {
    masterSchema = loadMasterSchema(),
    platformSchemas = null,
    strict = false,
  } = opts;

  let doc;
  try {
    doc = _loadDoc(source);
  } catch (e) {
    return { ok: false, errors: [`<root>: ${e.message}`], warnings: [], platformsChecked: [] };
  }
  if (typeof doc !== "object" || doc === null || Array.isArray(doc)) {
    return { ok: false, errors: ["<root>: manifest must be an object"], warnings: [], platformsChecked: [] };
  }

  const ajv = _newAjv(masterSchema);
  const validateMaster = ajv.compile(masterSchema);
  const errors = [];
  if (!validateMaster(doc)) {
    for (const e of validateMaster.errors || []) errors.push(_formatError(e));
  }

  const warnings = [];
  const platformsChecked = [];
  const declaredPlatforms = (doc.platforms && typeof doc.platforms === "object") ? doc.platforms : {};

  if (platformSchemas) {
    for (const [pid, extSchema] of Object.entries(platformSchemas)) {
      if (!(pid in declaredPlatforms)) continue;
      const ajvExt = _newAjv(masterSchema);
      const v = ajvExt.compile(extSchema);
      if (!v(doc)) {
        for (const e of v.errors || []) errors.push(`platforms.${pid}/${_formatError(e)}`);
      }
      platformsChecked.push(pid);
    }
  }

  // Lightweight semantic check → warning.
  if (
    doc.safety &&
    doc.safety.safe_for_auto_spawn === true &&
    !(Array.isArray(doc.env_vars_required) && doc.env_vars_required.length > 0)
  ) {
    warnings.push(
      "safety.safe_for_auto_spawn=true with no env_vars_required: " +
        "double-check this manifest does not need any secrets."
    );
  }

  let ok = errors.length === 0;
  if (strict && warnings.length > 0) ok = false;
  return { ok, errors, warnings, platformsChecked };
}

export function validateFile(path, opts = {}) {
  const { platformSchemasDir = null, ...rest } = opts;
  let platformSchemas = null;
  if (platformSchemasDir) {
    platformSchemas = {};
    // Find every *-spawn.schema.json under the dir (recursive).
    const stack = [platformSchemasDir];
    while (stack.length) {
      const dir = stack.pop();
      for (const ent of readdirSync(dir, { withFileTypes: true })) {
        const full = resolve(dir, ent.name);
        if (ent.isDirectory()) stack.push(full);
        else if (ent.isFile() && ent.name.endsWith("-spawn.schema.json")) {
          const id = basename(ent.name).replace(/-spawn\.schema\.json$/, "");
          platformSchemas[id] = loadPlatformSchema(full);
        }
      }
    }
  }
  return validate(path, { ...rest, platformSchemas });
}
