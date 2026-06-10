"""Tests for docs/tools/inner_agent_gates.py (Goal 7.5)."""

from __future__ import annotations

import datetime as dt
import socket
import subprocess
import sys
import urllib.error
from pathlib import Path
from unittest.mock import MagicMock, patch

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import inner_agent_gates as iag  # noqa: E402

# ---------------- kill switch ----------------


def test_kill_switch_set_when_env_is_0():
    assert iag.is_kill_switch_set({"EINSTEIN_INNER_AGENT": "0"})


def test_kill_switch_unset_by_default():
    assert not iag.is_kill_switch_set({})
    assert not iag.is_kill_switch_set({"EINSTEIN_INNER_AGENT": "1"})
    assert not iag.is_kill_switch_set({"EINSTEIN_INNER_AGENT": ""})


# ---------------- sentinel ----------------


def test_sentinel_absent(tmp_path: Path):
    assert not iag.is_sentinel_present(tmp_path / "missing")


def test_sentinel_present(tmp_path: Path):
    s = tmp_path / ".inner-agent-disabled"
    s.write_text("disabled due to qmd lint failure on cycle 47\n")
    assert iag.is_sentinel_present(s)


def test_write_sentinel_creates_file_with_reason(tmp_path: Path):
    s = tmp_path / "mb" / ".inner-agent-disabled"
    result = iag.write_sentinel(s, reason="wiki_lint exit 2", cycle_id=47)
    assert result == s
    assert s.is_file()
    body = s.read_text()
    assert "reason: wiki_lint exit 2" in body
    assert "cycle_id=47" in body
    assert "Remove this file" in body
    # Idempotent — rewriting works
    iag.write_sentinel(s, reason="newer reason")
    assert "newer reason" in s.read_text()


def test_write_sentinel_omits_cycle_id_when_unspecified(tmp_path: Path):
    s = tmp_path / "mb" / ".inner-agent-disabled"
    iag.write_sentinel(s, reason="no cycle context")
    assert "cycle_id=" not in s.read_text()


def test_clear_sentinel_removes_existing(tmp_path: Path):
    s = tmp_path / ".inner-agent-disabled"
    s.write_text("disabled\n")
    assert iag.clear_sentinel(s) is True
    assert not s.exists()


def test_clear_sentinel_idempotent_on_missing(tmp_path: Path):
    assert iag.clear_sentinel(tmp_path / "missing") is False


# ---------------- CLI ----------------


def test_cli_write_sentinel(tmp_path: Path, capsys):
    s = tmp_path / "mb" / ".inner-agent-disabled"
    rc = iag._cli(
        [
            "write-sentinel",
            str(s),
            "--reason",
            "wiki_lint exit 2",
            "--cycle-id",
            "47",
        ]
    )
    assert rc == 0
    out = capsys.readouterr().out.strip()
    assert out == str(s)
    body = s.read_text()
    assert "wiki_lint exit 2" in body
    assert "cycle_id=47" in body


def test_cli_clear_sentinel_removes(tmp_path: Path, capsys):
    s = tmp_path / ".inner-agent-disabled"
    s.write_text("x\n")
    rc = iag._cli(["clear-sentinel", str(s)])
    assert rc == 0
    assert "removed" in capsys.readouterr().out
    assert not s.exists()


def test_cli_clear_sentinel_missing_exits_1(tmp_path: Path, capsys):
    rc = iag._cli(["clear-sentinel", str(tmp_path / "no-such")])
    assert rc == 1
    assert "not-present" in capsys.readouterr().out


def test_cli_budget_prints_today_row(tmp_path: Path, capsys):
    budget = tmp_path / "budget.md"
    iag.record_token_usage(
        budget,
        input_tokens=100,
        output_tokens=20,
        today=dt.date(2026, 5, 24),
    )
    rc = iag._cli(["budget", str(budget)])
    assert rc == 0
    out = capsys.readouterr().out
    # today (real today) is likely different from 2026-05-24, so we won't
    # assert on the date; just on the schema.
    assert "date=" in out
    assert "input=" in out
    assert "total=" in out
    assert "cycles=" in out


# ---------------- reachability ----------------


def test_is_reachable_returns_true_on_success():
    fake_resp = MagicMock()
    fake_resp.__enter__ = lambda self: self
    fake_resp.__exit__ = lambda *_a: False
    with patch.object(iag.urllib.request, "urlopen", return_value=fake_resp):
        assert iag.is_reachable("https://arxiv.org/")


def test_is_reachable_returns_true_on_http_error():
    """4xx/5xx still means the host is reachable."""
    err = urllib.error.HTTPError(
        url="https://x",
        code=503,
        msg="Service Unavailable",
        hdrs=None,
        fp=None,
    )
    with patch.object(iag.urllib.request, "urlopen", side_effect=err):
        assert iag.is_reachable("https://x")


def test_is_reachable_returns_false_on_timeout():
    with patch.object(iag.urllib.request, "urlopen", side_effect=TimeoutError):
        assert not iag.is_reachable("https://x")


def test_is_reachable_returns_false_on_network_error():
    with patch.object(
        iag.urllib.request, "urlopen", side_effect=urllib.error.URLError("connection refused")
    ):
        assert not iag.is_reachable("https://x")


def test_is_reachable_returns_false_on_dns_error():
    with patch.object(
        iag.urllib.request, "urlopen", side_effect=socket.gaierror("nodename nor servname")
    ):
        assert not iag.is_reachable("https://x")


# ---------------- thermal ----------------


def test_thermal_ok_when_no_speed_limit_line():
    fake = MagicMock(stdout="Note: No thermal warning level recorded\n", stderr="")
    with patch.object(iag.subprocess, "run", return_value=fake):
        ok, detail = iag.is_thermal_ok()
    assert ok
    assert "no thermal pressure" in detail


def test_thermal_ok_when_speed_limit_is_100():
    fake = MagicMock(stdout="CPU_Speed_Limit = 100\n", stderr="")
    with patch.object(iag.subprocess, "run", return_value=fake):
        ok, detail = iag.is_thermal_ok()
    assert ok
    assert "CPU_Speed_Limit=100" in detail


def test_thermal_not_ok_when_throttled():
    fake = MagicMock(stdout="CPU_Speed_Limit = 70\n", stderr="")
    with patch.object(iag.subprocess, "run", return_value=fake):
        ok, detail = iag.is_thermal_ok()
    assert not ok
    assert "throttled" in detail
    assert "CPU_Speed_Limit=70" in detail


def test_thermal_ok_when_pmset_missing():
    """Non-macOS or pmset not installed — don't block the loop."""
    with patch.object(iag.subprocess, "run", side_effect=FileNotFoundError("pmset")):
        ok, detail = iag.is_thermal_ok()
    assert ok
    assert "unavailable" in detail


def test_thermal_ok_when_pmset_times_out():
    timeout_err = subprocess.TimeoutExpired(cmd="pmset", timeout=3)
    with patch.object(iag.subprocess, "run", side_effect=timeout_err):
        ok, _ = iag.is_thermal_ok()
    assert ok


# ---------------- budget ledger ----------------


def test_read_today_total_returns_zero_when_file_missing(tmp_path: Path):
    row = iag.read_today_total(tmp_path / "missing.md")
    assert row.input == 0
    assert row.output == 0
    assert row.cycles == 0


def test_record_token_usage_creates_file_with_header(tmp_path: Path):
    path = tmp_path / "budget.md"
    today = dt.date(2026, 5, 24)
    row = iag.record_token_usage(
        path,
        input_tokens=100,
        output_tokens=20,
        today=today,
    )
    assert row.input == 100
    assert row.output == 20
    assert row.total == 120
    assert row.cycles == 1
    text = path.read_text()
    assert "Inner-agent daily budget" in text
    assert "| 2026-05-24 | 100 | 20 | 120 | 1 |" in text


def test_record_token_usage_accumulates_within_a_day(tmp_path: Path):
    path = tmp_path / "budget.md"
    today = dt.date(2026, 5, 24)
    iag.record_token_usage(path, input_tokens=100, output_tokens=20, today=today)
    row = iag.record_token_usage(
        path,
        input_tokens=50,
        output_tokens=10,
        today=today,
    )
    assert row.input == 150
    assert row.output == 30
    assert row.cycles == 2


def test_record_token_usage_separates_days(tmp_path: Path):
    path = tmp_path / "budget.md"
    iag.record_token_usage(
        path,
        input_tokens=100,
        output_tokens=20,
        today=dt.date(2026, 5, 23),
    )
    iag.record_token_usage(
        path,
        input_tokens=50,
        output_tokens=10,
        today=dt.date(2026, 5, 24),
    )
    text = path.read_text()
    assert "| 2026-05-23 | 100 | 20 | 120 | 1 |" in text
    assert "| 2026-05-24 | 50 | 10 | 60 | 1 |" in text


def test_is_under_budget_true_when_under_cap(tmp_path: Path):
    path = tmp_path / "budget.md"
    iag.record_token_usage(
        path,
        input_tokens=100,
        output_tokens=20,
        today=dt.date(2026, 5, 24),
    )
    ok, detail = iag.is_under_budget(
        path,
        daily_cap=1000,
        today=dt.date(2026, 5, 24),
    )
    assert ok
    assert "today=120 cap=1000" in detail


def test_is_under_budget_false_when_over_cap(tmp_path: Path):
    path = tmp_path / "budget.md"
    iag.record_token_usage(
        path,
        input_tokens=900,
        output_tokens=200,
        today=dt.date(2026, 5, 24),
    )
    ok, _ = iag.is_under_budget(
        path,
        daily_cap=1000,
        today=dt.date(2026, 5, 24),
    )
    assert not ok


def test_is_under_budget_true_when_no_file_yet(tmp_path: Path):
    ok, detail = iag.is_under_budget(tmp_path / "missing.md", daily_cap=1000)
    assert ok
    assert "today=0" in detail


# ---------------- precheck composition ----------------


def _make_paths(tmp_path: Path) -> dict:
    return {
        "budget_path": tmp_path / "budget.md",
        "sentinel_path": tmp_path / ".inner-agent-disabled",
    }


def test_precheck_budget_gate_flips_across_repeated_cycles(tmp_path: Path):
    """Phase 2 Goal 3: simulate repeated cycles accumulating tokens; precheck
    proceeds under the cap and flips to skip once the daily total crosses it."""
    paths = _make_paths(tmp_path)
    cap = 1000
    today = dt.date(2026, 6, 9)
    # 4 cycles of 200 tokens each = 800 < cap → all proceed.
    for _ in range(4):
        iag.record_token_usage(
            paths["budget_path"], input_tokens=150, output_tokens=50, today=today
        )
        decision = iag.precheck(
            env={},
            daily_cap=cap,
            skip_reachability=True,
            skip_thermal=True,
            today=today,
            **paths,
        )
        assert decision.action == "proceed"
    # 5th cycle pushes total to 1000 (== cap) → next precheck skips (not < cap).
    iag.record_token_usage(paths["budget_path"], input_tokens=150, output_tokens=50, today=today)
    decision = iag.precheck(
        env={},
        daily_cap=cap,
        skip_reachability=True,
        skip_thermal=True,
        today=today,
        **paths,
    )
    assert decision.action == "skip"
    assert "daily token budget hit" in decision.reason


def test_precheck_proceed_happy_path(tmp_path: Path):
    decision = iag.precheck(
        env={},
        skip_reachability=True,
        skip_thermal=True,
        **_make_paths(tmp_path),
    )
    assert decision.action == "proceed"
    assert decision.llm_enabled is True


def test_precheck_kill_switch_proceeds_with_mechanical_mode(tmp_path: Path):
    decision = iag.precheck(
        env={"EINSTEIN_INNER_AGENT": "0"},
        skip_reachability=True,
        skip_thermal=True,
        **_make_paths(tmp_path),
    )
    assert decision.action == "proceed"
    assert decision.llm_enabled is False
    assert "mechanical path only" in decision.reason


def test_precheck_sentinel_skips_both_modes(tmp_path: Path):
    paths = _make_paths(tmp_path)
    paths["sentinel_path"].write_text("disabled\n")
    decision = iag.precheck(
        env={},
        skip_reachability=True,
        skip_thermal=True,
        **paths,
    )
    assert decision.action == "skip"
    assert decision.llm_enabled is False
    assert "sentinel" in decision.reason


def test_precheck_budget_skips_when_over_cap(tmp_path: Path):
    paths = _make_paths(tmp_path)
    iag.record_token_usage(
        paths["budget_path"],
        input_tokens=9999,
        output_tokens=2,
        today=dt.date(2026, 5, 24),
    )
    decision = iag.precheck(
        env={},
        daily_cap=100,
        today=dt.date(2026, 5, 24),
        skip_reachability=True,
        skip_thermal=True,
        **paths,
    )
    assert decision.action == "skip"
    assert "daily token budget" in decision.reason


def test_precheck_unreachable_skips(tmp_path: Path):
    paths = _make_paths(tmp_path)
    with patch.object(iag, "is_reachable", return_value=False):
        decision = iag.precheck(
            env={},
            reachability_urls=("https://arxiv.org/",),
            skip_thermal=True,
            **paths,
        )
    assert decision.action == "skip"
    assert "unreachable" in decision.reason


def test_precheck_thermal_throttled_skips(tmp_path: Path):
    paths = _make_paths(tmp_path)
    with patch.object(iag, "is_thermal_ok", return_value=(False, "CPU=70")):
        decision = iag.precheck(
            env={},
            skip_reachability=True,
            **paths,
        )
    assert decision.action == "skip"
    assert "thermal" in decision.reason


def test_precheck_kill_switch_skips_llm_mode_checks(tmp_path: Path):
    """When kill switch is on, budget/reach/thermal don't matter — they
    apply only to LLM cycles. precheck must not invoke them."""
    paths = _make_paths(tmp_path)
    iag.record_token_usage(
        paths["budget_path"],
        input_tokens=10**8,
        output_tokens=10**8,
        today=dt.date(2026, 5, 24),
    )  # way over any cap
    # If precheck called is_reachable, the unpatched one would try the network
    # and likely succeed; if it called is_thermal_ok, would run real pmset. We
    # patch both to fail noisily so the test would error if precheck reached
    # them despite the kill switch.
    with (
        patch.object(iag, "is_reachable", side_effect=AssertionError("should not be called")),
        patch.object(iag, "is_thermal_ok", side_effect=AssertionError("should not be called")),
    ):
        decision = iag.precheck(
            env={"EINSTEIN_INNER_AGENT": "0"},
            today=dt.date(2026, 5, 24),
            **paths,
        )
    assert decision.action == "proceed"
    assert decision.llm_enabled is False


def test_precheck_sentinel_takes_priority_over_kill_switch(tmp_path: Path):
    """Both set — sentinel wins because it's the regression-detect signal
    that should block even mechanical-mode work."""
    paths = _make_paths(tmp_path)
    paths["sentinel_path"].write_text("disabled\n")
    decision = iag.precheck(
        env={"EINSTEIN_INNER_AGENT": "0"},
        skip_reachability=True,
        skip_thermal=True,
        **paths,
    )
    assert decision.action == "skip"
    assert "sentinel" in decision.reason
