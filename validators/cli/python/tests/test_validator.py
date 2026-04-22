"""universal-spawn validator tests."""
from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from universal_spawn import (
    ValidationResult,
    load_master_schema,
    load_platform_schema,
    validate,
    validate_file,
)
from universal_spawn.cli import main as cli_main


REPO = Path(__file__).resolve().parents[4]


def _good_manifest() -> dict:
    return {
        "version": "1.0",
        "name": "Sample",
        "description": "A sample manifest used by the validator test suite.",
        "type": "web-app",
        "platforms": {"vercel": {"framework": "nextjs"}},
        "metadata": {
            "license": "MIT",
            "author": {"name": "Tester", "handle": "tester"},
            "source": {"type": "git", "url": "https://example.com/r.git"},
        },
    }


# 1
def test_master_schema_loads():
    schema = load_master_schema()
    assert schema["title"]
    assert "$id" in schema


# 2
def test_valid_minimal_manifest_passes():
    res = validate(_good_manifest())
    assert res.ok, res.errors
    assert res.errors == []


# 3
def test_missing_required_field_fails():
    bad = _good_manifest()
    del bad["name"]
    res = validate(bad)
    assert not res.ok
    assert any("name" in e or "<root>" in e for e in res.errors)


# 4
def test_wrong_version_string_fails():
    bad = _good_manifest()
    bad["version"] = "0.1"
    res = validate(bad)
    assert not res.ok
    assert any("version" in e for e in res.errors)


# 5
def test_unknown_type_fails():
    bad = _good_manifest()
    bad["type"] = "definitely-not-a-real-type"
    res = validate(bad)
    assert not res.ok


# 6
def test_validate_file_yaml(tmp_path: Path):
    p = tmp_path / "u.yaml"
    p.write_text(yaml.safe_dump(_good_manifest()))
    res = validate_file(p)
    assert res.ok, res.errors


# 7
def test_validate_file_json(tmp_path: Path):
    p = tmp_path / "u.json"
    p.write_text(json.dumps(_good_manifest()))
    res = validate_file(p)
    assert res.ok, res.errors


# 8
def test_warns_safe_auto_spawn_without_secrets():
    m = _good_manifest()
    m["safety"] = {"safe_for_auto_spawn": True}
    res = validate(m)
    assert res.ok
    assert res.warnings, "expected at least one warning about auto-spawn + no env"


# 9
def test_strict_mode_promotes_warnings_to_failures():
    m = _good_manifest()
    m["safety"] = {"safe_for_auto_spawn": True}
    res = validate(m, strict=True)
    assert not res.ok
    assert res.warnings


# 10
def test_platform_schema_validation_via_dir(tmp_path: Path):
    """Loads a real platform schema from the repo and validates an
    extension-specific manifest against it."""
    grok_schema_dir = tmp_path / "schemas"
    grok_schema_dir.mkdir()
    src = REPO / "platforms" / "ai" / "grok" / "grok-spawn.schema.json"
    if not src.is_file():
        pytest.skip("ai/grok schema not present in this checkout")
    (grok_schema_dir / "grok-spawn.schema.json").write_text(src.read_text())

    grok_manifest = {
        "version": "1.0",
        "name": "Grok Tester",
        "description": "A manifest used to exercise the grok platform schema.",
        "type": "ai-agent",
        "platforms": {"grok": {"model": "grok-4-fast", "surface": ["grok-api"]}},
        "metadata": {
            "license": "Apache-2.0",
            "author": {"name": "Tester", "handle": "tester"},
            "source": {"type": "git", "url": "https://example.com/r.git"},
        },
    }
    p = tmp_path / "u.yaml"
    p.write_text(yaml.safe_dump(grok_manifest))
    res = validate_file(p, platform_schemas_dir=grok_schema_dir)
    assert res.ok, res.errors
    assert "grok" in res.platforms_checked


# 11
def test_platform_schema_extension_failure(tmp_path: Path):
    """A manifest declaring `platforms.grok` with a missing required field
    must fail under platform-schema validation."""
    src = REPO / "platforms" / "ai" / "grok" / "grok-spawn.schema.json"
    if not src.is_file():
        pytest.skip("ai/grok schema not present in this checkout")
    grok_schema_dir = tmp_path / "schemas"
    grok_schema_dir.mkdir()
    (grok_schema_dir / "grok-spawn.schema.json").write_text(src.read_text())

    bad = {
        "version": "1.0",
        "name": "Grok Tester",
        "description": "Missing required surface[].",
        "type": "ai-agent",
        "platforms": {"grok": {"model": "grok-4-fast"}},  # surface missing
        "metadata": {
            "license": "Apache-2.0",
            "author": {"name": "Tester", "handle": "tester"},
            "source": {"type": "git", "url": "https://example.com/r.git"},
        },
    }
    p = tmp_path / "u.yaml"
    p.write_text(yaml.safe_dump(bad))
    res = validate_file(p, platform_schemas_dir=grok_schema_dir)
    assert not res.ok
    assert any("grok" in e for e in res.errors)


# 12
def test_cli_validate_returns_zero_on_good(tmp_path: Path, monkeypatch):
    p = tmp_path / "universal-spawn.yaml"
    p.write_text(yaml.safe_dump(_good_manifest()))
    monkeypatch.chdir(tmp_path)
    rc = cli_main(["validate"])
    assert rc == 0


# 13
def test_cli_validate_returns_one_on_bad(tmp_path: Path, monkeypatch):
    bad = _good_manifest()
    del bad["description"]
    p = tmp_path / "universal-spawn.yaml"
    p.write_text(yaml.safe_dump(bad))
    monkeypatch.chdir(tmp_path)
    rc = cli_main(["validate"])
    assert rc == 1


# 14
def test_cli_init_writes_starter(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    rc = cli_main(["init", "--type", "minimal"])
    assert rc == 0
    out = tmp_path / "universal-spawn.yaml"
    assert out.is_file()
    doc = yaml.safe_load(out.read_text())
    assert doc["version"] == "1.0"
    res = validate(doc)
    assert res.ok, res.errors


# 15
def test_cli_migrate_lifts_legacy(tmp_path: Path, monkeypatch):
    legacy = {
        "spawn_version": "1.0.0",
        "id": "com.example.thing",
        "name": "Thing",
        "kind": "ai-agent",
        "description": "A legacy v1.0.0 manifest used as the migration source.",
        "license": "Apache-2.0",
        "author": {"name": "Tester", "handle": "tester"},
        "source": {"type": "git", "url": "https://example.com/r.git"},
        "min_permissions": ["network:outbound:api.anthropic.com"],
        "rate_limit_qps": 3,
        "safe_for_auto_spawn": False,
    }
    src = tmp_path / "spawn.yaml"
    src.write_text(yaml.safe_dump(legacy))
    monkeypatch.chdir(tmp_path)
    rc = cli_main(["migrate", str(src), "--out", "universal-spawn.yaml"])
    assert rc == 0
    out = tmp_path / "universal-spawn.yaml"
    new = yaml.safe_load(out.read_text())
    assert new["version"] == "1.0"
    assert new["type"] == "ai-agent"
    assert new["metadata"]["id"] == "com.example.thing"
    res = validate(new)
    assert res.ok, res.errors
