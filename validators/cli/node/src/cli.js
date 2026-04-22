#!/usr/bin/env node
// universal-spawn CLI (Node).
//
// Subcommands:
//   validate [path]   Validate manifest at path (default: ./universal-spawn.yaml).
//   init [--type t]   Write a starter manifest.
//   migrate [path]    Lift legacy v1.0.0 spawn.yaml → v1.0 universal-spawn.yaml.

import { Command } from "commander";
import { existsSync, writeFileSync, readFileSync } from "node:fs";
import { resolve } from "node:path";
import YAML from "yaml";
import { validateFile, validate } from "./validator.js";

const VERSION = "1.0.0";

const DEFAULT_FILES = [
  "universal-spawn.yaml",
  "universal-spawn.yml",
  "universal-spawn.json",
  "spawn.yaml",
  "spawn.yml",
  "spawn.json",
];

const STARTERS = {
  minimal: {
    version: "1.0",
    name: "Your Project",
    description:
      "Replace this with a one-paragraph description of what your project does.",
    type: "web-app",
    platforms: { vercel: {} },
    metadata: {
      license: "MIT",
      author: { name: "Your Name", handle: "yourhandle" },
      source: { type: "git", url: "https://github.com/yourhandle/your-project" },
    },
  },
  "ai-agent": {
    version: "1.0",
    name: "Your AI Agent",
    description:
      "Replace with a one-paragraph description of what this AI agent does.",
    type: "ai-agent",
    platforms: {
      claude: {
        skill_type: "subagent",
        model: "claude-sonnet-4-6",
        surface: ["claude-api"],
      },
    },
    safety: {
      min_permissions: ["network:outbound:api.anthropic.com"],
      safe_for_auto_spawn: false,
    },
    env_vars_required: [
      {
        name: "ANTHROPIC_API_KEY",
        description: "Anthropic API key.",
        secret: true,
      },
    ],
    metadata: {
      license: "Apache-2.0",
      author: { name: "Your Name", handle: "yourhandle" },
      source: { type: "git", url: "https://github.com/yourhandle/your-agent" },
    },
  },
};

function detectDefaultPath() {
  for (const c of DEFAULT_FILES) {
    if (existsSync(c)) return c;
  }
  return null;
}

function cmdValidate(pathArg, opts) {
  const path = pathArg || detectDefaultPath();
  if (!path) {
    console.error(
      `no manifest path given and no default manifest found ` +
        `(looked for: ${DEFAULT_FILES.join(", ")})`
    );
    process.exit(2);
  }
  const result = validateFile(path, {
    platformSchemasDir: opts.platformSchemasDir || null,
    strict: opts.strict || false,
  });
  for (const e of result.errors) console.log(`error  ${e}`);
  for (const w of result.warnings) console.log(`warn   ${w}`);
  if (result.platformsChecked.length > 0) {
    console.log(
      `info   checked platform extensions: ${result.platformsChecked.sort().join(", ")}`
    );
  }
  if (result.ok) {
    console.log(`ok     ${path}`);
    process.exit(0);
  }
  console.log(
    `fail   ${path}: ${result.errors.length} error(s), ${result.warnings.length} warning(s)`
  );
  process.exit(1);
}

function cmdInit(opts) {
  const starter = STARTERS[opts.type];
  if (!starter) {
    console.error(
      `unknown starter '${opts.type}'. Choose from: ${Object.keys(STARTERS).sort().join(", ")}`
    );
    process.exit(2);
  }
  const out = resolve(opts.out);
  if (existsSync(out) && !opts.force) {
    console.error(`refusing to overwrite ${out} (pass --force).`);
    process.exit(2);
  }
  writeFileSync(out, YAML.stringify(starter));
  console.log(`wrote   ${out} (type=${opts.type})`);
  process.exit(0);
}

function cmdMigrate(pathArg, opts) {
  const src = pathArg || detectDefaultPath();
  if (!src) {
    console.error("no source manifest given and no default found.");
    process.exit(2);
  }
  const legacy = YAML.parse(readFileSync(src, "utf8"));
  if (typeof legacy !== "object" || legacy === null) {
    console.error(`${src}: not a YAML/JSON object.`);
    process.exit(2);
  }

  const lifted = { version: "1.0" };
  for (const k of ["name", "description", "summary"]) {
    if (legacy[k] !== undefined) lifted[k] = legacy[k];
  }
  lifted.type = legacy.kind || "web-app";

  const metadata = {};
  for (const k of ["id", "license", "author", "source"]) {
    if (legacy[k] !== undefined) metadata[k] = legacy[k];
  }
  if (Object.keys(metadata).length > 0) lifted.metadata = metadata;

  for (const k of ["platforms", "env_vars_required", "deployment", "visuals", "safety"]) {
    if (legacy[k] !== undefined) lifted[k] = legacy[k];
  }

  const safety = (lifted.safety && typeof lifted.safety === "object") ? lifted.safety : {};
  for (const k of [
    "min_permissions",
    "rate_limit_qps",
    "cost_limit_usd_daily",
    "safe_for_auto_spawn",
    "data_residency",
  ]) {
    if (legacy[k] !== undefined && safety[k] === undefined) safety[k] = legacy[k];
  }
  if (Object.keys(safety).length > 0) lifted.safety = safety;

  if (lifted.platforms === undefined && lifted.deployment === undefined) {
    lifted.platforms = {};
  }

  const out = resolve(opts.out || "universal-spawn.yaml");
  if (existsSync(out) && !opts.force) {
    console.error(`refusing to overwrite ${out} (pass --force).`);
    process.exit(2);
  }
  writeFileSync(out, YAML.stringify(lifted));
  console.log(`wrote   ${out} (lifted from ${src})`);
  process.exit(0);
}

const program = new Command();
program
  .name("universal-spawn")
  .description("Validate, init, and migrate universal-spawn manifests.")
  .version(VERSION);

program
  .command("validate [path]")
  .description("Validate a manifest.")
  .option("--strict", "Treat warnings as failures.", false)
  .option(
    "--platform-schemas-dir <dir>",
    "Directory with <id>-spawn.schema.json files for platform-extension validation."
  )
  .action(cmdValidate);

program
  .command("init")
  .description("Write a starter manifest.")
  .option("--type <type>", "Starter id.", "minimal")
  .option("--out <path>", "Output path.", "universal-spawn.yaml")
  .option("--force", "Overwrite an existing file.", false)
  .action(cmdInit);

program
  .command("migrate [path]")
  .description("Lift a legacy v1.0.0 spawn manifest to v1.0.")
  .option("--out <path>", "Output path.", null)
  .option("--force", "Overwrite an existing file.", false)
  .action(cmdMigrate);

program.parseAsync(process.argv);
