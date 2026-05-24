"""Tests for src/einstein/optimizer_dispatch.py."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO / "src"))

from einstein import optimizer_dispatch as od  # noqa: E402


# ---------------- fixtures ----------------


def _write_manifest(tmp_path: Path, entries: dict) -> Path:
    """Write a minimal manifest. Accepts {pid: {slug, default, optimizers}}."""
    import yaml
    p = tmp_path / "manifest.yaml"
    p.write_text(yaml.safe_dump(entries))
    return p


def _example_entry(script_rel: str = "scripts/fake/opt.py",
                   result_rel: str = "results/fake/r.json") -> dict:
    return {
        "slug": "fake",
        "default": "opt",
        "optimizers": {
            "opt": {
                "script": script_rel,
                "cli_args": [],
                "timeout_seconds": 30,
                "result_file": result_rel,
                "result_parser": "json_score_payload",
            }
        },
    }


# ---------------- behavior ----------------


def test_no_manifest_entry_returns_clear_error(tmp_path: Path) -> None:
    manifest = _write_manifest(tmp_path, {99: _example_entry()})
    r = od.dispatch(problem_id=14, manifest_path=manifest)
    assert r.ok is False
    assert "no manifest entry" in (r.error or "")
    assert r.problem_id == 14


def test_dry_run_resolves_optimizer_without_executing(tmp_path: Path) -> None:
    manifest = _write_manifest(tmp_path, {14: _example_entry()})
    r = od.dispatch(problem_id=14, manifest_path=manifest, dry_run=True)
    assert r.ok is False
    assert r.error == "dry-run"
    assert r.optimizer == "opt"


def test_missing_script_is_caught_before_subprocess(tmp_path: Path) -> None:
    # script path is relative; cwd=tmp_path so script won't exist
    manifest = _write_manifest(tmp_path, {14: _example_entry()})
    r = od.dispatch(problem_id=14, manifest_path=manifest, cwd=tmp_path)
    assert r.ok is False
    assert "script missing" in (r.error or "")


def test_successful_dispatch_parses_score_and_payload(tmp_path: Path) -> None:
    # Lay out a fake script + result file relative to tmp_path
    (tmp_path / "scripts" / "fake").mkdir(parents=True)
    (tmp_path / "scripts" / "fake" / "opt.py").write_text("# stub")
    (tmp_path / "results" / "fake").mkdir(parents=True)
    (tmp_path / "results" / "fake" / "r.json").write_text(
        json.dumps({"score": 1.2345, "payload": {"vectors": [[1, 0], [0, 1]]}})
    )
    manifest = _write_manifest(tmp_path, {14: _example_entry()})

    # Mock subprocess.run to return success without actually running anything
    def fake_runner(cmd, *, cwd, capture_output, text, timeout):
        return MagicMock(returncode=0, stdout="ok\n", stderr="")

    r = od.dispatch(problem_id=14, manifest_path=manifest, cwd=tmp_path,
                    subprocess_runner=fake_runner)
    assert r.ok is True
    assert r.score == pytest.approx(1.2345)
    assert r.payload == {"vectors": [[1, 0], [0, 1]]}
    assert r.optimizer == "opt"
    assert r.exit_code == 0


def test_subprocess_timeout_returns_clean_error(tmp_path: Path) -> None:
    (tmp_path / "scripts" / "fake").mkdir(parents=True)
    (tmp_path / "scripts" / "fake" / "opt.py").write_text("# stub")
    manifest = _write_manifest(tmp_path, {14: _example_entry()})

    def fake_runner(cmd, *, cwd, capture_output, text, timeout):
        raise subprocess.TimeoutExpired(cmd, timeout)

    r = od.dispatch(problem_id=14, manifest_path=manifest, cwd=tmp_path,
                    subprocess_runner=fake_runner)
    assert r.ok is False
    assert "timeout" in (r.error or "").lower()
    assert r.optimizer == "opt"


def test_nonzero_exit_includes_stderr_tail(tmp_path: Path) -> None:
    (tmp_path / "scripts" / "fake").mkdir(parents=True)
    (tmp_path / "scripts" / "fake" / "opt.py").write_text("# stub")
    manifest = _write_manifest(tmp_path, {14: _example_entry()})

    def fake_runner(cmd, *, cwd, capture_output, text, timeout):
        return MagicMock(returncode=42, stdout="warming up\n",
                         stderr="ValueError: bad input\n")

    r = od.dispatch(problem_id=14, manifest_path=manifest, cwd=tmp_path,
                    subprocess_runner=fake_runner)
    assert r.ok is False
    assert r.exit_code == 42
    assert "ValueError" in r.stderr_tail
    assert "exited with code 42" in (r.error or "")


def test_missing_result_file_reports_parse_error(tmp_path: Path) -> None:
    (tmp_path / "scripts" / "fake").mkdir(parents=True)
    (tmp_path / "scripts" / "fake" / "opt.py").write_text("# stub")
    # Do NOT create the result file
    manifest = _write_manifest(tmp_path, {14: _example_entry()})

    def fake_runner(cmd, *, cwd, capture_output, text, timeout):
        return MagicMock(returncode=0, stdout="", stderr="")

    r = od.dispatch(problem_id=14, manifest_path=manifest, cwd=tmp_path,
                    subprocess_runner=fake_runner)
    assert r.ok is False
    assert "result_file missing" in (r.error or "")


def test_malformed_result_json_reports_parse_error(tmp_path: Path) -> None:
    (tmp_path / "scripts" / "fake").mkdir(parents=True)
    (tmp_path / "scripts" / "fake" / "opt.py").write_text("# stub")
    (tmp_path / "results" / "fake").mkdir(parents=True)
    (tmp_path / "results" / "fake" / "r.json").write_text("{not valid json")
    manifest = _write_manifest(tmp_path, {14: _example_entry()})

    def fake_runner(cmd, *, cwd, capture_output, text, timeout):
        return MagicMock(returncode=0, stdout="", stderr="")

    r = od.dispatch(problem_id=14, manifest_path=manifest, cwd=tmp_path,
                    subprocess_runner=fake_runner)
    assert r.ok is False
    assert "parse" in (r.error or "").lower()


def test_strategy_picks_optimizer_by_name(tmp_path: Path) -> None:
    """When strategy matches an optimizer key, use it instead of default."""
    entry = _example_entry()
    entry["optimizers"]["alt"] = {
        "script": "scripts/fake/alt.py",
        "cli_args": [],
        "timeout_seconds": 30,
        "result_file": "results/fake/alt.json",
        "result_parser": "json_score_payload",
    }
    (tmp_path / "scripts" / "fake").mkdir(parents=True)
    (tmp_path / "scripts" / "fake" / "alt.py").write_text("# stub")
    (tmp_path / "results" / "fake").mkdir(parents=True)
    (tmp_path / "results" / "fake" / "alt.json").write_text(
        json.dumps({"score": 9.9, "payload": {"tag": "alt"}})
    )
    manifest = _write_manifest(tmp_path, {14: entry})

    def fake_runner(cmd, *, cwd, capture_output, text, timeout):
        # Verify the script being invoked is the alt one
        assert any("alt.py" in arg for arg in cmd)
        return MagicMock(returncode=0, stdout="", stderr="")

    r = od.dispatch(problem_id=14, strategy="alt", manifest_path=manifest,
                    cwd=tmp_path, subprocess_runner=fake_runner)
    assert r.ok is True
    assert r.optimizer == "alt"
    assert r.payload == {"tag": "alt"}
