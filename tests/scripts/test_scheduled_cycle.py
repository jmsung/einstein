"""Tests for scripts/scheduled_cycle.py — Phase 3 Goal 2 cron entry point.

The wrapper adds the scheduler-level guards the loop itself doesn't have
(runs/day cap, hard wall-clock timeout, run ledger); everything else
(sentinel, kill switches, token budget, skip-if-recent, lockfile) stays in
autonomous_loop's precheck. No live cron until Goal 5's verdict.
"""

from __future__ import annotations

import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "scripts"))

import scheduled_cycle as sc  # noqa: E402

TODAY = "2026-06-09"


# ---------------- build_command ----------------


def test_build_command_default_shape() -> None:
    cmd = sc.build_command(skip_if_recent_min=45)
    joined = " ".join(cmd)
    assert "autonomous_loop.py" in joined
    assert "--one-problem" in cmd
    assert "--by-priority" in cmd
    assert "--skip-if-recent" in cmd
    assert "45" in cmd
    assert "--skip-gates" not in cmd  # Goal-0 lesson: precheck IS the LLM enabler


def test_build_command_dry_run_appends_flag() -> None:
    cmd = sc.build_command(skip_if_recent_min=45, dry_run=True)
    assert "--dry-run" in cmd


# ---------------- runs/day cap ----------------


def _ledger(tmp_path: Path, lines: list[str]) -> Path:
    p = tmp_path / "scheduler-runs.log"
    p.write_text("\n".join(lines) + ("\n" if lines else ""))
    return p


def test_runs_today_counts_only_today(tmp_path: Path) -> None:
    led = _ledger(
        tmp_path,
        [
            "2026-06-08T22:00:00Z exit=0 dur=120s",
            f"{TODAY}T01:00:00Z exit=0 dur=100s",
            f"{TODAY}T05:00:00Z exit=75 dur=1s",
        ],
    )
    assert sc.runs_today(led, today=TODAY) == 2


def test_runs_today_missing_ledger_is_zero(tmp_path: Path) -> None:
    assert sc.runs_today(tmp_path / "nope.log", today=TODAY) == 0


def test_should_run_respects_daily_cap(tmp_path: Path) -> None:
    led = _ledger(tmp_path, [f"{TODAY}T0{i}:00:00Z exit=0 dur=1s" for i in range(3)])
    assert sc.should_run(led, max_runs_per_day=3, today=TODAY) is False
    assert sc.should_run(led, max_runs_per_day=4, today=TODAY) is True


def test_record_run_appends_one_line(tmp_path: Path) -> None:
    led = tmp_path / "scheduler-runs.log"
    sc.record_run(led, exit_code=0, duration_s=12.3, ts=f"{TODAY}T01:00:00Z")
    sc.record_run(led, exit_code=75, duration_s=0.4, ts=f"{TODAY}T02:00:00Z")
    lines = led.read_text().splitlines()
    assert len(lines) == 2
    assert "exit=0" in lines[0] and "exit=75" in lines[1]


# ---------------- main (guards short-circuit before the subprocess) ----------------


def test_main_skips_at_daily_cap_without_running(tmp_path: Path) -> None:
    led = _ledger(tmp_path, [f"{TODAY}T0{i}:00:00Z exit=0 dur=1s" for i in range(5)])
    calls: list[list[str]] = []
    rc = sc.main(
        [
            "--ledger",
            str(led),
            "--max-runs-per-day",
            "5",
        ],
        runner=lambda cmd, timeout: calls.append(cmd) or 0,
        today=TODAY,
        now_iso=f"{TODAY}T06:00:00Z",
    )
    assert rc == 0  # cap-skip is a clean exit (cron-friendly), not an error
    assert calls == []
    # The skip itself is NOT ledger-recorded — only real runs count.
    assert sc.runs_today(led, today=TODAY) == 5


def test_main_runs_and_records_under_cap(tmp_path: Path) -> None:
    led = _ledger(tmp_path, [])
    calls: list[list[str]] = []
    rc = sc.main(
        ["--ledger", str(led), "--max-runs-per-day", "5"],
        runner=lambda cmd, timeout: calls.append(cmd) or 0,
        today=TODAY,
        now_iso=f"{TODAY}T06:00:00Z",
    )
    assert rc == 0
    assert len(calls) == 1
    assert "--one-problem" in calls[0] and "--by-priority" in calls[0]
    assert sc.runs_today(led, today=TODAY) == 1


def test_main_propagates_loop_exit_code(tmp_path: Path) -> None:
    led = _ledger(tmp_path, [])
    rc = sc.main(
        ["--ledger", str(led)],
        runner=lambda cmd, timeout: 75,  # lock held → EX_TEMPFAIL passthrough
        today=TODAY,
        now_iso=f"{TODAY}T06:00:00Z",
    )
    assert rc == 75
    assert "exit=75" in (led.read_text())


def test_main_timeout_records_and_returns_nonzero(tmp_path: Path) -> None:
    import subprocess

    led = _ledger(tmp_path, [])

    def hang(cmd: list[str], timeout: int) -> int:
        raise subprocess.TimeoutExpired(cmd=cmd, timeout=timeout)

    rc = sc.main(
        ["--ledger", str(led), "--timeout-s", "7200"],
        runner=hang,
        today=TODAY,
        now_iso=f"{TODAY}T06:00:00Z",
    )
    assert rc != 0
    assert "exit=timeout" in led.read_text()


def test_main_dry_run_skips_ledger(tmp_path: Path) -> None:
    led = _ledger(tmp_path, [])
    calls: list[list[str]] = []
    rc = sc.main(
        ["--ledger", str(led), "--dry-run"],
        runner=lambda cmd, timeout: calls.append(cmd) or 0,
        today=TODAY,
        now_iso=f"{TODAY}T06:00:00Z",
    )
    assert rc == 0
    assert len(calls) == 1 and "--dry-run" in calls[0]
    assert led.read_text() == ""  # dry runs don't consume the daily cap


def test_main_timeout_passed_to_runner(tmp_path: Path) -> None:
    led = _ledger(tmp_path, [])
    seen: list[int] = []

    def spy(cmd: list[str], timeout: int) -> int:
        seen.append(timeout)
        return 0

    sc.main(
        ["--ledger", str(led), "--timeout-s", "1234"],
        runner=spy,
        today=TODAY,
        now_iso=f"{TODAY}T06:00:00Z",
    )
    assert seen == [1234]
