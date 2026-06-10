"""Tests for docs/tools/scheduler_health.py — Phase 3 Goal 4 health monitor.

The monitor reads the unattended loop's ledgers (scheduler runs, telemetry,
budget, sentinel) and returns healthy/unhealthy + reasons, exit-code-coded
so cron can alert on it.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import scheduler_health as sh  # noqa: E402

TODAY = "2026-06-09"
NOW = "2026-06-09T12:00:00Z"


def _runs(tmp_path: Path, lines: list[str]) -> Path:
    p = tmp_path / "scheduler-runs.log"
    p.write_text("\n".join(lines) + ("\n" if lines else ""))
    return p


def _tele(tmp_path: Path, records: list[dict]) -> Path:
    p = tmp_path / "telemetry.jsonl"
    p.write_text("\n".join(json.dumps(r) for r in records) + ("\n" if records else ""))
    return p


def _tele_rec(path_taken: str = "llm", parse_ok: bool = True, cost: float = 0.5) -> dict:
    return {
        "problem_id": 12,
        "attempt_index": 1,
        "path_taken": path_taken,
        "llm_error_kind": "" if path_taken == "llm" else "parse-error",
        "parse_ok": parse_ok,
        "wall_clock_s": 60.0,
        "input_tokens": 10,
        "output_tokens": 2000,
        "token_source": "exact",
        "cost_usd": cost,
        "ts": f"{TODAY}T01:00:00+00:00",
    }


# ---------------- individual checks ----------------


def test_check_last_run_age_fresh_ok(tmp_path: Path) -> None:
    runs = _runs(tmp_path, [f"{TODAY}T10:00:00Z exit=0 dur=100.0s"])
    issues = sh.check_runs(runs, now_iso=NOW, max_age_hours=6, max_consecutive_failures=3)
    assert issues == []


def test_check_stale_last_run_flagged(tmp_path: Path) -> None:
    runs = _runs(tmp_path, ["2026-06-08T10:00:00Z exit=0 dur=100.0s"])
    issues = sh.check_runs(runs, now_iso=NOW, max_age_hours=6, max_consecutive_failures=3)
    assert any("stale" in i for i in issues)


def test_check_missing_ledger_flagged(tmp_path: Path) -> None:
    issues = sh.check_runs(
        tmp_path / "nope.log", now_iso=NOW, max_age_hours=6, max_consecutive_failures=3
    )
    assert any("no scheduler runs" in i for i in issues)


def test_check_consecutive_failures_flagged(tmp_path: Path) -> None:
    runs = _runs(
        tmp_path,
        [
            f"{TODAY}T08:00:00Z exit=0 dur=100.0s",
            f"{TODAY}T09:00:00Z exit=1 dur=100.0s",
            f"{TODAY}T10:00:00Z exit=timeout dur=7200.0s",
            f"{TODAY}T11:00:00Z exit=1 dur=100.0s",
        ],
    )
    issues = sh.check_runs(runs, now_iso=NOW, max_age_hours=6, max_consecutive_failures=3)
    assert any("consecutive" in i for i in issues)


def test_check_exit75_lock_skips_not_failures(tmp_path: Path) -> None:
    # EX_TEMPFAIL (lock held) is benign — cron retries; must not trip the alert.
    runs = _runs(
        tmp_path,
        [f"{TODAY}T0{i}:00:00Z exit=75 dur=0.1s" for i in range(6, 9)]
        + [f"{TODAY}T11:00:00Z exit=75 dur=0.1s"],
    )
    issues = sh.check_runs(runs, now_iso=NOW, max_age_hours=6, max_consecutive_failures=3)
    assert issues == []


def test_check_telemetry_fallback_rate_breach(tmp_path: Path) -> None:
    tele = _tele(tmp_path, [_tele_rec("fallback")] * 3 + [_tele_rec("llm")] * 7)
    issues = sh.check_telemetry(tele, window=50, max_fallback_rate=0.2, max_cost_usd=5.0)
    assert any("fallback" in i for i in issues)


def test_check_telemetry_healthy(tmp_path: Path) -> None:
    tele = _tele(tmp_path, [_tele_rec("llm")] * 10)
    assert sh.check_telemetry(tele, window=50, max_fallback_rate=0.2, max_cost_usd=5.0) == []


def test_check_telemetry_cost_breach(tmp_path: Path) -> None:
    tele = _tele(tmp_path, [_tele_rec("llm", cost=6.5)])
    issues = sh.check_telemetry(tele, window=50, max_fallback_rate=0.2, max_cost_usd=5.0)
    assert any("cost" in i for i in issues)


def test_check_telemetry_missing_is_informational_not_alert(tmp_path: Path) -> None:
    # No telemetry yet (fresh deploy) — not an alert condition.
    assert (
        sh.check_telemetry(
            tmp_path / "nope.jsonl", window=50, max_fallback_rate=0.2, max_cost_usd=5.0
        )
        == []
    )


def test_check_sentinel_present_flagged(tmp_path: Path) -> None:
    sentinel = tmp_path / ".inner-agent-disabled"
    sentinel.write_text("tripped 2026-06-09")
    issues = sh.check_sentinel(sentinel)
    assert any("sentinel" in i for i in issues)
    assert sh.check_sentinel(tmp_path / "absent") == []


# ---------------- report / main ----------------


def test_main_healthy_exit_zero(tmp_path: Path, capsys) -> None:
    runs = _runs(tmp_path, [f"{TODAY}T10:00:00Z exit=0 dur=100.0s"])
    tele = _tele(tmp_path, [_tele_rec("llm")] * 5)
    rc = sh.main(
        [
            "--runs-ledger",
            str(runs),
            "--telemetry",
            str(tele),
            "--sentinel",
            str(tmp_path / "absent"),
        ],
        now_iso=NOW,
    )
    assert rc == 0
    out = capsys.readouterr().out
    assert "HEALTHY" in out


def test_main_unhealthy_exit_one_lists_reasons(tmp_path: Path, capsys) -> None:
    runs = _runs(tmp_path, ["2026-06-07T10:00:00Z exit=1 dur=1.0s"])
    sentinel = tmp_path / ".inner-agent-disabled"
    sentinel.write_text("x")
    rc = sh.main(
        [
            "--runs-ledger",
            str(runs),
            "--telemetry",
            str(tmp_path / "none.jsonl"),
            "--sentinel",
            str(sentinel),
        ],
        now_iso=NOW,
    )
    assert rc == 1
    out = capsys.readouterr().out
    assert "UNHEALTHY" in out
    assert "sentinel" in out and "stale" in out
