"""Tests for docs/tools/notify_milestone.py (Goal 7.8c)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import notify_milestone as nm  # noqa: E402

# ---------------- escape + cmd building ----------------


def test_escape_quotes_and_backslashes():
    assert nm._escape_for_applescript('say "hi"') == 'say \\"hi\\"'
    assert nm._escape_for_applescript(r"path\with\slash") == r"path\\with\\slash"


def test_escape_collapses_newlines():
    assert nm._escape_for_applescript("line1\nline2\rline3") == "line1 line2 line3"


def test_build_osascript_cmd_no_subtitle():
    cmd = nm.build_osascript_cmd(title="t", message="m")
    assert cmd[0] == "osascript"
    assert cmd[1] == "-e"
    body = cmd[2]
    assert 'display notification "m"' in body
    assert 'with title "t"' in body
    assert "subtitle" not in body


def test_build_osascript_cmd_with_subtitle():
    cmd = nm.build_osascript_cmd(title="t", message="m", subtitle="s")
    body = cmd[2]
    assert 'subtitle "s"' in body


def test_build_osascript_cmd_escapes_special_chars():
    cmd = nm.build_osascript_cmd(title='quote " test', message="line\nbreak")
    body = cmd[2]
    assert '\\"' in body
    assert "\n" not in body
    assert "line break" in body


# ---------------- notify behavior ----------------


def test_notify_happy_path_returns_true():
    fake_runner_calls: list = []

    def fake_runner(cmd, **kw):
        fake_runner_calls.append((cmd, kw))
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    ok = nm.notify(
        title="Hello",
        message="World",
        subtitle="sub",
        runner=fake_runner,
    )
    assert ok is True
    assert len(fake_runner_calls) == 1
    cmd, kw = fake_runner_calls[0]
    assert cmd[0] == "osascript"
    assert kw["timeout"] == nm.DEFAULT_TIMEOUT_S


def test_notify_returns_false_on_non_zero_exit():
    def bad_runner(cmd, **kw):
        return SimpleNamespace(returncode=1, stdout="", stderr="boom")

    assert nm.notify(title="t", message="m", runner=bad_runner) is False


def test_notify_returns_false_on_timeout():
    def slow_runner(cmd, **kw):
        raise subprocess.TimeoutExpired(cmd=cmd, timeout=kw.get("timeout"))

    assert nm.notify(title="t", message="m", runner=slow_runner) is False


def test_notify_returns_false_on_missing_binary():
    def missing(cmd, **kw):
        raise FileNotFoundError("osascript")

    assert nm.notify(title="t", message="m", runner=missing) is False


def test_notify_no_op_on_non_macos():
    """No runner passed + non-Darwin → returns False without raising."""
    with patch.object(nm.platform, "system", return_value="Linux"):
        assert nm.notify(title="t", message="m") is False


def test_notify_arena_record_calls_notify_with_expected_strings():
    calls: list = []

    def spy_runner(cmd, **kw):
        calls.append(cmd)
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    nm.notify_arena_record(problem_id=14, score=2.6359830849175, runner=spy_runner)
    assert len(calls) == 1
    body = calls[0][2]
    assert "P14" in body
    assert "submission accepted" in body
    # Score is rendered via :.10g — first ~9 sig figs round-trip exactly
    assert "2.635983085" in body
    assert "autonomous loop" in body


def test_is_supported_reflects_platform():
    with patch.object(nm.platform, "system", return_value="Darwin"):
        assert nm.is_supported() is True
    with patch.object(nm.platform, "system", return_value="Linux"):
        assert nm.is_supported() is False
