"""Tests for scripts/scheduled_cycle.py — Phase 3 Goal 2 cron entry point.

The wrapper adds the scheduler-level guards the loop itself doesn't have
(runs/day cap, hard wall-clock timeout, run ledger); everything else
(sentinel, kill switches, token budget, skip-if-recent, lockfile) stays in
autonomous_loop's precheck. No live cron until Goal 5's verdict.
"""

from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "scripts"))

import scheduled_cycle as sc  # noqa: E402

TODAY = "2026-06-09"


@pytest.fixture(autouse=True)
def _isolate_real_paths(tmp_path, monkeypatch):
    """Keep every main() test off the real cooldown/telemetry files.

    main()'s post-run cooldown logic reads --telemetry and writes/clears
    --cooldown-file, both defaulting to real mb/logs/ paths. Redirect the
    module defaults to tmp so the suite never deletes a live cooldown.
    """
    monkeypatch.setattr(sc, "DEFAULT_COOLDOWN_FILE", tmp_path / "cooldown.txt")
    monkeypatch.setattr(sc, "DEFAULT_TELEMETRY", tmp_path / "telemetry.jsonl")


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


# ---------------- rate-limit cooldown gate ----------------


def _telemetry_writer(path: Path, *, error_kind: str, n: int):
    """A fake runner that appends n far-future telemetry rows, then succeeds."""

    def run(cmd: list[str], timeout: int) -> int:
        with path.open("a") as f:
            for i in range(n):
                f.write(
                    json.dumps(
                        {
                            "ts": "2099-01-01T00:00:00+00:00",  # ≥ run start always
                            "problem_id": 3,
                            "attempt_index": i + 1,
                            "path_taken": "fallback" if error_kind else "llm",
                            "llm_error_kind": error_kind,
                        }
                    )
                    + "\n"
                )
        return 0

    return run


def test_count_unavailable_since_filters_kind_and_time(tmp_path):
    tel = tmp_path / "t.jsonl"
    tel.write_text(
        json.dumps({"ts": "2026-06-11T05:00:00+00:00", "llm_error_kind": "unavailable"})
        + "\n"
        + json.dumps({"ts": "2026-06-11T07:00:00+00:00", "llm_error_kind": "unavailable"})
        + "\n"
        + json.dumps({"ts": "2026-06-11T07:30:00+00:00", "llm_error_kind": "parse-error"})
        + "\n"
    )
    since = dt.datetime(2026, 6, 11, 6, tzinfo=dt.timezone.utc)
    assert sc.count_unavailable_since(tel, since) == 1  # only the 07:00 unavailable row


def test_in_cooldown_expired_returns_none(tmp_path):
    cd = tmp_path / "cd.txt"
    cd.write_text("2020-01-01T00:00:00+00:00\n")
    now = dt.datetime(2026, 6, 11, tzinfo=dt.timezone.utc)
    assert sc.in_cooldown(cd, now=now) is None


def test_main_skips_when_in_cooldown(tmp_path):
    led = _ledger(tmp_path, [])
    cd = tmp_path / "cd.txt"
    cd.write_text("2099-01-01T00:00:00+00:00\n")  # far-future deadline
    calls: list[list[str]] = []
    rc = sc.main(
        ["--ledger", str(led), "--cooldown-file", str(cd)],
        runner=lambda cmd, timeout: calls.append(cmd) or 0,
        today=TODAY,
        now_iso=f"{TODAY}T06:00:00Z",
    )
    assert rc == 0 and calls == []  # skipped cleanly, loop never invoked
    assert led.read_text() == ""  # not counted as a run


def test_main_trips_cooldown_on_unavailable_run(tmp_path):
    led = _ledger(tmp_path, [])
    cd = tmp_path / "cd.txt"
    tel = tmp_path / "t.jsonl"
    rc = sc.main(
        [
            "--ledger",
            str(led),
            "--cooldown-file",
            str(cd),
            "--telemetry",
            str(tel),
            "--cooldown-after",
            "2",
            "--cooldown-hours",
            "5",
        ],
        runner=_telemetry_writer(tel, error_kind="unavailable", n=2),
        today=TODAY,
        now_iso=f"{TODAY}T06:00:00Z",
    )
    assert rc == 0
    assert cd.exists()  # cooldown tripped
    assert sc.read_cooldown_until(cd) > dt.datetime.now(dt.timezone.utc)  # future deadline


def test_main_clears_cooldown_on_clean_run(tmp_path):
    led = _ledger(tmp_path, [])
    cd = tmp_path / "cd.txt"
    cd.write_text("2020-01-01T00:00:00+00:00\n")  # stale/expired → not skipped
    tel = tmp_path / "t.jsonl"
    sc.main(
        [
            "--ledger",
            str(led),
            "--cooldown-file",
            str(cd),
            "--telemetry",
            str(tel),
            "--cooldown-after",
            "2",
        ],
        runner=_telemetry_writer(tel, error_kind="", n=1),  # clean llm cycle
        today=TODAY,
        now_iso=f"{TODAY}T06:00:00Z",
    )
    assert not cd.exists()  # clean run clears the stale cooldown
