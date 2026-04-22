// universal-spawn — Node validator test suite (vitest).
import { describe, expect, it } from "vitest";
import { mkdtempSync, writeFileSync, mkdirSync, copyFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import YAML from "yaml";

import {
  loadMasterSchema,
  validate,
  validateFile,
} from "../src/validator.js";

const REPO = resolve(import.meta.dirname, "..", "..", "..", "..");

function goodManifest() {
  return {
    version: "1.0",
    name: "Sample",
    description: "A sample manifest used by the validator test suite.",
    type: "web-app",
    platforms: { vercel: { framework: "nextjs" } },
    metadata: {
      license: "MIT",
      author: { name: "Tester", handle: "tester" },
      source: { type: "git", url: "https://example.com/r.git" },
    },
  };
}

describe("master schema", () => {
  it("loads", () => {
    const s = loadMasterSchema();
    expect(s.title).toBeTruthy();
    expect(s.$id).toBeTruthy();
  });
});

describe("validate", () => {
  it("accepts a minimal valid manifest", () => {
    const r = validate(goodManifest());
    expect(r.ok).toBe(true);
    expect(r.errors).toEqual([]);
  });

  it("rejects a missing required field", () => {
    const m = goodManifest();
    delete m.name;
    const r = validate(m);
    expect(r.ok).toBe(false);
    expect(r.errors.length).toBeGreaterThan(0);
  });

  it("rejects a wrong version string", () => {
    const m = goodManifest();
    m.version = "0.1";
    const r = validate(m);
    expect(r.ok).toBe(false);
  });

  it("rejects an unknown type", () => {
    const m = goodManifest();
    m.type = "definitely-not-a-real-type";
    const r = validate(m);
    expect(r.ok).toBe(false);
  });

  it("warns on safe_for_auto_spawn=true with no env_vars_required", () => {
    const m = goodManifest();
    m.safety = { safe_for_auto_spawn: true };
    const r = validate(m);
    expect(r.ok).toBe(true);
    expect(r.warnings.length).toBeGreaterThan(0);
  });

  it("strict mode promotes warnings to failures", () => {
    const m = goodManifest();
    m.safety = { safe_for_auto_spawn: true };
    const r = validate(m, { strict: true });
    expect(r.ok).toBe(false);
  });

  it("rejects a non-object root", () => {
    const r = validate("not-an-object");
    // when called with a string, validator tries to read it as a file and returns an error
    expect(r.ok).toBe(false);
  });
});

describe("validateFile", () => {
  it("validates a YAML manifest from disk", () => {
    const dir = mkdtempSync(join(tmpdir(), "us-"));
    const p = join(dir, "u.yaml");
    writeFileSync(p, YAML.stringify(goodManifest()));
    const r = validateFile(p);
    expect(r.ok).toBe(true);
  });

  it("validates a JSON manifest from disk", () => {
    const dir = mkdtempSync(join(tmpdir(), "us-"));
    const p = join(dir, "u.json");
    writeFileSync(p, JSON.stringify(goodManifest()));
    const r = validateFile(p);
    expect(r.ok).toBe(true);
  });

  it("validates a real platform extension (grok) when discovered", () => {
    const dir = mkdtempSync(join(tmpdir(), "us-"));
    const schemasDir = join(dir, "schemas");
    mkdirSync(schemasDir, { recursive: true });
    const src = join(REPO, "platforms", "ai", "grok", "grok-spawn.schema.json");
    try {
      copyFileSync(src, join(schemasDir, "grok-spawn.schema.json"));
    } catch {
      return; // skip when not present
    }
    const grok = {
      version: "1.0",
      name: "Grok Tester",
      description: "Used to exercise the grok platform schema.",
      type: "ai-agent",
      platforms: { grok: { model: "grok-4-fast", surface: ["grok-api"] } },
      metadata: {
        license: "Apache-2.0",
        author: { name: "Tester", handle: "tester" },
        source: { type: "git", url: "https://example.com/r.git" },
      },
    };
    const p = join(dir, "u.yaml");
    writeFileSync(p, YAML.stringify(grok));
    const r = validateFile(p, { platformSchemasDir: schemasDir });
    expect(r.ok).toBe(true);
    expect(r.platformsChecked).toContain("grok");
  });

  it("rejects a manifest that fails a platform extension", () => {
    const dir = mkdtempSync(join(tmpdir(), "us-"));
    const schemasDir = join(dir, "schemas");
    mkdirSync(schemasDir, { recursive: true });
    const src = join(REPO, "platforms", "ai", "grok", "grok-spawn.schema.json");
    try {
      copyFileSync(src, join(schemasDir, "grok-spawn.schema.json"));
    } catch {
      return;
    }
    const bad = {
      version: "1.0",
      name: "Grok Tester",
      description: "Missing required surface[].",
      type: "ai-agent",
      platforms: { grok: { model: "grok-4-fast" } },
      metadata: {
        license: "Apache-2.0",
        author: { name: "Tester", handle: "tester" },
        source: { type: "git", url: "https://example.com/r.git" },
      },
    };
    const p = join(dir, "u.yaml");
    writeFileSync(p, YAML.stringify(bad));
    const r = validateFile(p, { platformSchemasDir: schemasDir });
    expect(r.ok).toBe(false);
    expect(r.errors.some((e) => e.includes("grok"))).toBe(true);
  });

  it("requires platforms or deployment", () => {
    const m = goodManifest();
    delete m.platforms;
    const r = validate(m);
    expect(r.ok).toBe(false);
  });

  it("accepts deployment with targets in lieu of platforms", () => {
    const m = goodManifest();
    delete m.platforms;
    m.deployment = { targets: ["vercel"] };
    const r = validate(m);
    expect(r.ok).toBe(true);
  });
});
