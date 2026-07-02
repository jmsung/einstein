"""Sanity test for docs/ops/com.einstein.autonomous-loop.plist (Goal 7.8e)."""

from __future__ import annotations

import plistlib
import re
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
PLIST_PATH = _REPO / "docs" / "ops" / "com.einstein.autonomous-loop.plist"


def test_plist_file_exists():
    assert PLIST_PATH.is_file()


def test_plist_after_substitution_parses_as_plist():
    """The template has `__PROJECT_ROOT__` placeholders; after sed-substitution
    the document must be a valid plist. We do the substitution in-memory and
    parse with plistlib."""
    raw = PLIST_PATH.read_text()
    assert "__PROJECT_ROOT__" in raw, "template placeholder missing"
    rendered = raw.replace(
        "__PROJECT_ROOT__", "/Users/jongmin/projects/einstein/cb-feat-autonomous-loop"
    )
    data = plistlib.loads(rendered.encode("utf-8"))
    assert isinstance(data, dict)


def test_plist_required_keys_present():
    raw = PLIST_PATH.read_text().replace("__PROJECT_ROOT__", "/tmp/fake/repo")
    data = plistlib.loads(raw.encode("utf-8"))
    assert data["Label"] == "com.einstein.autonomous-loop"
    assert isinstance(data["ProgramArguments"], list)
    # The launch command must invoke the Phase-3 wrapper (scheduled_cycle.py) with
    # the production flags, and must NOT call autonomous_loop.py directly (the
    # pre-Phase-3 entry point lacked --by-priority; see the plist comment).
    cmd = " ".join(data["ProgramArguments"])
    assert "scheduled_cycle.py" in cmd
    assert "autonomous_loop.py" not in cmd
    assert "--skip-if-recent 20" in cmd
    assert "--max-runs-per-day 48" in cmd
    # 30-minute cadence (the cycle's own --skip-if-recent prevents overlap)
    assert data["StartInterval"] == 1800
    assert data["RunAtLoad"] is True
    # PATH includes Homebrew + system bins so uv resolves
    env = data.get("EnvironmentVariables", {})
    assert "PATH" in env
    assert "/opt/homebrew/bin" in env["PATH"] or "/usr/local/bin" in env["PATH"]
    # Log paths land under mb/ (Phase-3 scheduler logs)
    assert "/mb/logs/" in data["StandardOutPath"]
    assert data["StandardOutPath"].endswith("scheduler.log")
    assert data["StandardErrorPath"].endswith("scheduler.err.log")


def test_install_instructions_in_readme_use_consistent_label():
    """The README must reference the same Label as the plist, otherwise the
    bootstrap / bootout commands won't match the loaded job."""
    readme = (_REPO / "docs" / "ops" / "README.md").read_text()
    assert "com.einstein.autonomous-loop" in readme
    # README must mention the placeholder
    assert "__PROJECT_ROOT__" in readme
    # And the launchctl verbs
    assert "launchctl bootstrap" in readme
    assert "launchctl bootout" in readme


def test_program_arguments_have_no_relative_paths():
    """launchd starts from / by default; relative paths inside the command
    won't resolve. We use `cd <root> &&` to fix that, but `bash -lc` should
    receive an absolute working dir as the first thing it sees."""
    raw = PLIST_PATH.read_text().replace("__PROJECT_ROOT__", "/abs/path")
    data = plistlib.loads(raw.encode("utf-8"))
    pa = data["ProgramArguments"]
    # First arg is the shell, second is -lc, third is the command
    assert pa[0] == "/bin/bash"
    cmd = pa[2]
    # The cd target is absolute (substituted PROJECT_ROOT)
    assert re.search(r'cd "/abs/path"', cmd)
