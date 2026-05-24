"""Tests for docs/tools/claude_headless.py (Goal 7.2 — shared `claude -p` wrapper)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import claude_headless as ch  # noqa: E402

# ---------------- happy path + CLI flags ----------------


def test_run_builds_minimal_cmd_for_text_output():
    fake = MagicMock(returncode=0, stdout="hello\n", stderr="")
    with patch.object(ch.subprocess, "run", return_value=fake) as mock_run:
        result = ch.run("PROMPT", model="claude-opus-4-7[1m]")

    assert result.ok
    assert result.stdout == "hello\n"
    assert result.error_kind == ""

    cmd = mock_run.call_args[0][0]
    assert cmd[0] == "claude"
    assert cmd[1] == "-p"
    assert "--model" in cmd and "claude-opus-4-7[1m]" in cmd
    assert cmd[-1] == "PROMPT"  # prompt is the last positional arg
    # No optional flags absent inputs
    assert "--output-format" not in cmd
    assert "--allowedTools" not in cmd
    assert "--json-schema" not in cmd
    assert "--max-budget-usd" not in cmd
    assert "--permission-mode" not in cmd


def test_run_threads_optional_flags():
    fake = MagicMock(returncode=0, stdout='{"ok": true}', stderr="")
    schema = '{"type":"object"}'
    with patch.object(ch.subprocess, "run", return_value=fake) as mock_run:
        ch.run(
            "PROMPT",
            allowed_tools=["Read", "Grep", "Bash(qmd:*)", "Task"],
            output_format="json",
            json_schema=schema,
            max_budget_usd=0.50,
            permission_mode="acceptEdits",
            fallback_model="claude-sonnet-4-6",
            system_prompt="be terse",
            append_system_prompt="cite paths",
            add_dirs=[Path("/tmp/a"), Path("/tmp/b")],
            extra_args=["--debug", "api"],
            timeout_seconds=600,
        )

    cmd = mock_run.call_args[0][0]
    # tool allow-list passed as space-separated args (not comma-joined)
    i = cmd.index("--allowedTools")
    assert cmd[i + 1 : i + 5] == ["Read", "Grep", "Bash(qmd:*)", "Task"]
    assert "--output-format" in cmd and "json" in cmd
    assert "--json-schema" in cmd and schema in cmd
    assert "--max-budget-usd" in cmd and "0.5" in cmd
    assert "--permission-mode" in cmd and "acceptEdits" in cmd
    assert "--fallback-model" in cmd and "claude-sonnet-4-6" in cmd
    assert "--system-prompt" in cmd and "be terse" in cmd
    assert "--append-system-prompt" in cmd and "cite paths" in cmd
    assert "--add-dir" in cmd and "/tmp/a" in cmd and "/tmp/b" in cmd
    assert "--debug" in cmd and "api" in cmd
    # subprocess.run timeout matches what we passed
    assert mock_run.call_args.kwargs["timeout"] == 600


# ---------------- failure classifications ----------------


def test_run_classifies_session_limit_as_unavailable_even_on_exit_0():
    """Claude CLI sometimes prints the quota message to stdout w/ exit 0."""
    fake = MagicMock(
        returncode=0,
        stdout="You've hit your session limit · resets 5:20pm\n/usage-credits\n",
        stderr="",
    )
    with patch.object(ch.subprocess, "run", return_value=fake):
        result = ch.run("PROMPT")
    assert not result.ok
    assert result.error_kind == "unavailable"
    assert "auth, quota" in result.error_message


def test_run_classifies_429_overload_as_unavailable():
    fake = MagicMock(
        returncode=1,
        stdout="",
        stderr="API error: 429 — service overloaded, retry later",
    )
    with patch.object(ch.subprocess, "run", return_value=fake):
        result = ch.run("PROMPT")
    assert not result.ok
    assert result.error_kind == "unavailable"


def test_run_classifies_auth_failure_as_unavailable():
    fake = MagicMock(returncode=1, stdout="Not logged in. Please run /login.", stderr="")
    with patch.object(ch.subprocess, "run", return_value=fake):
        result = ch.run("PROMPT")
    assert not result.ok
    assert result.error_kind == "unavailable"


def test_run_classifies_timeout():
    """subprocess.TimeoutExpired → HeadlessResult(error_kind='timeout')."""

    def boom(*args, **kwargs):
        raise subprocess.TimeoutExpired(
            cmd=args[0],
            timeout=30,
            output=b"partial output",
            stderr=b"",
        )

    with patch.object(ch.subprocess, "run", side_effect=boom):
        result = ch.run("PROMPT", timeout_seconds=30)
    assert not result.ok
    assert result.error_kind == "timeout"
    assert "30s" in result.error_message
    assert result.stdout == "partial output"


def test_run_classifies_nonzero_exit_as_non_zero():
    fake = MagicMock(returncode=2, stdout="", stderr="invalid flag --foo")
    with patch.object(ch.subprocess, "run", return_value=fake):
        result = ch.run("PROMPT")
    assert not result.ok
    assert result.error_kind == "non-zero"
    assert "invalid flag" in result.error_message
    assert result.returncode == 2


def test_run_nonzero_exit_truncates_long_stderr_in_message():
    long_stderr = "x" * 2000
    fake = MagicMock(returncode=1, stdout="", stderr=long_stderr)
    with patch.object(ch.subprocess, "run", return_value=fake):
        result = ch.run("PROMPT")
    # Message keeps only the tail
    assert len(result.error_message) < 700
    # But full stderr is preserved on the result for diagnostics
    assert len(result.stderr) == 2000


# ---------------- helpers ----------------


def test_is_unavailable_matches_known_patterns():
    assert ch._is_unavailable("You've hit your session limit")
    assert ch._is_unavailable("API error: 401")
    assert ch._is_unavailable("API error: 429")
    assert ch._is_unavailable("Overloaded right now")
    assert ch._is_unavailable("usage-credits limit")
    assert not ch._is_unavailable("everything is fine")
    assert not ch._is_unavailable("")
    assert not ch._is_unavailable(None)


def test_decode_handles_bytes_str_and_none():
    assert ch._decode(b"abc") == "abc"
    assert ch._decode("abc") == "abc"
    assert ch._decode(None) == ""


def test_headless_result_raise_for_error():
    ok = ch.HeadlessResult(ok=True, stdout="x")
    ok.raise_for_error()  # no-op on ok

    bad = ch.HeadlessResult(ok=False, error_kind="non-zero", error_message="boom")
    with pytest.raises(ch.ClaudeHeadlessError, match="boom"):
        bad.raise_for_error()


# ---------------- env + cwd ----------------


def test_run_passes_env_and_cwd(tmp_path: Path):
    fake = MagicMock(returncode=0, stdout="", stderr="")
    with patch.object(ch.subprocess, "run", return_value=fake) as mock_run:
        ch.run("PROMPT", env={"FOO": "1"}, cwd=tmp_path)
    kwargs = mock_run.call_args.kwargs
    assert kwargs["env"]["FOO"] == "1"
    # Inherits PATH from os.environ
    assert "PATH" in kwargs["env"]
    assert kwargs["cwd"] == tmp_path


# ---------------- claude_bin override ----------------


def test_run_uses_custom_claude_bin():
    fake = MagicMock(returncode=0, stdout="", stderr="")
    with patch.object(ch.subprocess, "run", return_value=fake) as mock_run:
        ch.run("PROMPT", claude_bin="/opt/custom/claude")
    cmd = mock_run.call_args[0][0]
    assert cmd[0] == "/opt/custom/claude"
