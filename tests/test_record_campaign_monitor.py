"""Tests for scripts/record_campaign_monitor.py — the record-campaign monitor.

Each alert detector is a pure function over parsed log text, so the tests feed
crafted fixtures and assert on the returned Alert list. The notify side effect
is exercised via a mock runner.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[1]
_MOD_PATH = _REPO / "scripts" / "record_campaign_monitor.py"
_spec = importlib.util.spec_from_file_location("record_campaign_monitor", _MOD_PATH)
mon = importlib.util.module_from_spec(_spec)
sys.modules["record_campaign_monitor"] = mon  # dataclass introspection needs this
_spec.loader.exec_module(mon)


# ---------------- auto-submit parsing ----------------

AUTO_SUBMIT_FIXTURE = """# auto-submit audit log

| timestamp_utc | problem_id | score | decision | reason | http_status | arena_id |
|---|---|---|---|---|---|---|
| 2026-06-02T01:00:00Z | 14 | 2.62 | rejected | triple-verify-failed: triple_verify['passed'] not True (numbers: {'note': 'triple-verify not yet wired'}) | — | — |
| 2026-06-02T02:00:00Z | 5 | 12.9 | submitted | ok | 200 | abc |
| 2026-06-01T02:00:00Z | 5 | 12.9 | submitted | ok | 200 | old |
"""


def test_parse_auto_submit_rows():
    rows = mon.parse_auto_submit_rows(AUTO_SUBMIT_FIXTURE)
    assert len(rows) == 3
    assert rows[0]["problem_id"] == "14"
    assert rows[1]["decision"] == "submitted"
    assert rows[1]["timestamp_utc"].startswith("2026-06-02")


# ---------------- triple-verify mismatch ----------------


def test_triple_verify_not_yet_wired_is_not_an_alert():
    rows = mon.parse_auto_submit_rows(AUTO_SUBMIT_FIXTURE)
    alerts = mon.check_triple_verify(rows, sentinel_present=False)
    assert alerts == []


def test_triple_verify_genuine_mismatch_alerts():
    text = (
        "| timestamp_utc | problem_id | score | decision | reason | http_status | arena_id |\n"
        "|---|---|---|---|---|---|---|\n"
        "| 2026-06-02T03:00:00Z | 11 | 0.51 | rejected | "
        "triple-verify-failed: evaluators disagree (fast=0.51, exact=0.49) | — | — |\n"
    )
    rows = mon.parse_auto_submit_rows(text)
    alerts = mon.check_triple_verify(rows, sentinel_present=False)
    assert len(alerts) == 1
    assert alerts[0].kind == "triple-verify"
    assert alerts[0].severity == "critical"


def test_synthetic_test_row_is_not_an_alert():
    text = (
        "| timestamp_utc | problem_id | score | decision | reason | http_status | arena_id |\n"
        "|---|---|---|---|---|---|---|\n"
        "| 2026-06-02T03:00:00Z | 14 | 2.62 | rejected | "
        "triple-verify-failed: triple_verify['passed'] not True "
        "(numbers: {'note': 'synthetic gate-2 test'}) | — | — |\n"
    )
    rows = mon.parse_auto_submit_rows(text)
    assert mon.check_triple_verify(rows, sentinel_present=False) == []


def test_sentinel_present_always_alerts():
    alerts = mon.check_triple_verify([], sentinel_present=True)
    assert len(alerts) == 1
    assert alerts[0].kind == "triple-verify"


# ---------------- dispatch failures ----------------

# Production-shaped: 12 columns (trailing `cites_src`), dispatch failures marked
# in NOTES (not outcome=="blocked"), and one row with embedded `|` in notes.
CYCLE_FIXTURE = """## Cycles

| # | problem | start → end | hours | compute | wiki cites | findings+ | concepts+ | author mix | outcome | notes | cites_src |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | P5-min-distance-ratio | none | 0 | none-strategy-only | 0 | 0 | 0 | a:1/h:0/hyb:0 | fanout-no-completion | autonomous_loop inner_attempt — dispatch-failed: optimizer exited with code 1 | 0 |
| 2 | P5-min-distance-ratio | none | 0 | none-strategy-only | 0 | 0 | 0 | a:1/h:0/hyb:0 | scaffold-no-attempt | autonomous_loop — category=packing; dispatch: no-manifest-entry | 0 |
| 3 | P5-min-distance-ratio | none | 0 | none-strategy-only | 0 | 0 | 0 | a:1/h:0/hyb:0 | fanout-no-completion | dispatch-failed: optimizer exited with code 1 | 0 |
| 4 | P5-min-distance-ratio | none | 0 | none-strategy-only | 0 | 0 | 0 | a:1/h:0/hyb:0 | fanout-no-completion | dispatch-failed: code 1 | 0 |
| 5 | P5-min-distance-ratio | none | 0 | none-strategy-only | 0 | 0 | 0 | a:1/h:0/hyb:0 | fanout-no-completion | dispatch-failed: code 1 | 0 |
| 6 | P11-tammes-n50 | 0.5 → 0.5 | 0 | local-cpu+llm | 0 | 0 | 0 | a:1/h:0/hyb:0 | converged | reproduced; gap arena#1 (\\|R\\|,\\|A\\|) ~5e-15 | 0 |
"""


def test_parse_cycle_outcomes_left_anchored_on_12_col():
    # outcome must come from column 9, NOT cells[-2] (which is cites_src/notes
    # on a 12-column production row) — this is the bug code-review caught.
    outcomes = mon.parse_cycle_outcomes(CYCLE_FIXTURE)
    p, outcome, notes = outcomes[0]
    assert p == "P5-min-distance-ratio"
    assert outcome == "fanout-no-completion"
    assert "dispatch-failed" in notes
    # last row: 12 cols + embedded pipes in notes; outcome still parses cleanly.
    assert outcomes[-1][:2] == ("P11-tammes-n50", "converged")
    assert len(outcomes) == 6


def test_dispatch_failures_five_in_a_row_alerts():
    # 5 consecutive P5 cycles with dispatch-failure NOTES markers (outcome is
    # fanout-no-completion / scaffold-no-attempt, never "blocked").
    outcomes = mon.parse_cycle_outcomes(CYCLE_FIXTURE)
    alerts = mon.check_dispatch_failures(outcomes, threshold=5)
    assert len(alerts) == 1
    assert alerts[0].kind == "dispatch-failures"
    assert "P5" in alerts[0].message


def test_dispatch_failures_below_threshold_quiet():
    outcomes = mon.parse_cycle_outcomes(CYCLE_FIXTURE)
    assert mon.check_dispatch_failures(outcomes, threshold=6) == []


def test_converged_is_not_a_dispatch_failure():
    # A healthy `converged` cycle (the dominant production outcome) must NOT
    # count as a dispatch failure — else the detector fires on normal operation.
    assert mon._is_dispatch_failure("converged", "reproduced; gap ~5e-15") is False
    assert mon._is_dispatch_failure("no-change", "auto-submit-rejected@kill-switch") is False
    assert mon._is_dispatch_failure("fanout-no-completion", "dispatch-failed: code 1") is True
    assert mon._is_dispatch_failure("blocked", "anything") is True


def test_dispatch_failures_run_broken_by_other_problem():
    text = (
        "| # | problem | s | h | c | wc | f | co | am | outcome | notes |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|\n"
        "| 1 | P5 x | a | 1 | x | 0 | 0 | 0 | a:1 | fanout-no-completion | dispatch-failed: e |\n"
        "| 2 | P5 x | a | 1 | x | 0 | 0 | 0 | a:1 | fanout-no-completion | dispatch-failed: e |\n"
        "| 3 | P11 y | a | 1 | x | 0 | 0 | 0 | a:1 | fanout-no-completion | dispatch-failed: e |\n"
        "| 4 | P5 x | a | 1 | x | 0 | 0 | 0 | a:1 | fanout-no-completion | dispatch-failed: e |\n"
    )
    outcomes = mon.parse_cycle_outcomes(text)
    # P5 has 2 then 1 consecutive (interrupted by P11) — never 3 in a row.
    assert mon.check_dispatch_failures(outcomes, threshold=3) == []


# ---------------- auto-submit rate ----------------


def test_auto_submit_rate_over_cap_alerts():
    rows = mon.parse_auto_submit_rows(AUTO_SUBMIT_FIXTURE)
    # one submitted row today (2026-06-02); cap=0 forces the alert.
    alerts = mon.check_auto_submit_rate(rows, today="2026-06-02", cap=0)
    assert len(alerts) == 1
    assert alerts[0].kind == "auto-submit-rate"


def test_auto_submit_rate_within_cap_quiet():
    rows = mon.parse_auto_submit_rows(AUTO_SUBMIT_FIXTURE)
    alerts = mon.check_auto_submit_rate(rows, today="2026-06-02", cap=5)
    assert alerts == []


def test_auto_submit_rate_counts_only_today_and_submitted():
    rows = mon.parse_auto_submit_rows(AUTO_SUBMIT_FIXTURE)
    # 2 submitted rows total but only 1 is today; rejected rows never count.
    n = mon.count_submitted_today(rows, today="2026-06-02")
    assert n == 1


# ---------------- orchestration + notify ----------------


def test_run_checks_aggregates(tmp_path):
    alerts = mon.run_checks(
        auto_submit_text=AUTO_SUBMIT_FIXTURE,
        cycle_text=CYCLE_FIXTURE,
        sentinel_present=True,
        today="2026-06-02",
        cap=0,
        dispatch_threshold=5,
    )
    kinds = {a.kind for a in alerts}
    assert kinds == {"triple-verify", "dispatch-failures", "auto-submit-rate"}


def test_fire_alerts_invokes_runner():
    calls = []

    def fake_runner(*a, **k):
        class R:
            returncode = 0

        calls.append((a, k))
        return R()

    alert = mon.Alert(kind="triple-verify", severity="critical", message="boom", detail={})
    mon.fire_alerts([alert], runner=fake_runner)
    assert len(calls) == 1
