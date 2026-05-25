"""Tests for src/einstein/auto_submit.py — the 6-gate decision chain."""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO / "src"))

from einstein import arena_submit, auto_submit  # noqa: E402


UTC = dt.timezone.utc


# ---------------- fixtures ----------------


def _now() -> dt.datetime:
    return dt.datetime(2026, 5, 24, 4, 0, 0, tzinfo=UTC)


def _passing_tv() -> dict:
    return {"fast": 2.6359, "exact": 2.6359, "cross": 2.6359, "passed": True}


def _ok_submission(*, http_status: int = 200, arena_id: int = 9999) -> arena_submit.SubmissionResult:
    return arena_submit.SubmissionResult(
        ok=True, problem_id=14, http_status=http_status,
        arena_response={"id": arena_id, "rank": 1, "score": 2.64},
    )


# ---------------- gate 1: kill switch ----------------


def test_kill_switch_blocks_submission(monkeypatch: pytest.MonkeyPatch,
                                        tmp_path: Path) -> None:
    monkeypatch.setenv("EINSTEIN_AUTO_SUBMIT", "0")
    audit = tmp_path / "audit.md"
    submitter = MagicMock()

    r = auto_submit.try_submit(
        14, {"vectors": []}, score=2.64,
        triple_verify=_passing_tv(),
        audit_log=audit,
        submitter=submitter,
        clock=_now,
    )
    assert r.submitted is False
    assert r.rejected_at_gate == "kill-switch"
    submitter.assert_not_called()
    assert "kill-switch" in audit.read_text()
    assert "rejected" in audit.read_text()


# ---------------- gate 2: triple-verify ----------------


def test_triple_verify_failed_blocks(tmp_path: Path) -> None:
    audit = tmp_path / "audit.md"
    submitter = MagicMock()
    r = auto_submit.try_submit(
        14, {"vectors": []}, score=2.64,
        triple_verify={"fast": 2.64, "exact": 2.65, "passed": False},
        audit_log=audit,
        submitter=submitter,
        clock=_now,
    )
    assert r.submitted is False
    assert r.rejected_at_gate == "triple-verify-failed"
    submitter.assert_not_called()


def test_no_triple_verify_blocks(tmp_path: Path) -> None:
    audit = tmp_path / "audit.md"
    r = auto_submit.try_submit(
        14, {"vectors": []}, score=2.64,
        triple_verify=None,
        audit_log=audit,
        submitter=MagicMock(),
        clock=_now,
    )
    assert r.submitted is False
    assert r.rejected_at_gate == "triple-verify-failed"


# ---------------- gate 3: daily cap ----------------


def test_daily_cap_blocks_after_N_submits(tmp_path: Path) -> None:
    audit = tmp_path / "audit.md"
    # Pre-populate with 5 submitted rows today
    audit.parent.mkdir(parents=True, exist_ok=True)
    audit.write_text("# audit\n\n" + auto_submit.AUDIT_LOG_HEADER + "".join(
        f"| 2026-05-24T0{i}:00:00Z | {10 + i} | 1.0 | submitted | ok | 200 | id{i} |\n"
        for i in range(5)
    ))
    submitter = MagicMock()
    r = auto_submit.try_submit(
        14, {"vectors": []}, score=2.64,
        triple_verify=_passing_tv(),
        audit_log=audit,
        daily_cap=5,
        arena_top1_score=2.6,
        submitter=submitter,
        clock=_now,
    )
    assert r.submitted is False
    assert r.rejected_at_gate == "daily-cap"
    submitter.assert_not_called()


# ---------------- gate 4: throttle ----------------


def test_throttle_blocks_same_problem_within_60min(tmp_path: Path) -> None:
    audit = tmp_path / "audit.md"
    audit.parent.mkdir(parents=True, exist_ok=True)
    # P14 submitted 30 min ago — under the 60min throttle
    audit.write_text("# audit\n\n" + auto_submit.AUDIT_LOG_HEADER +
                     "| 2026-05-24T03:30:00Z | 14 | 2.63 | submitted | ok | 200 | abc |\n")
    submitter = MagicMock()
    r = auto_submit.try_submit(
        14, {"vectors": []}, score=2.64,
        triple_verify=_passing_tv(),
        audit_log=audit,
        arena_top1_score=2.6,
        submitter=submitter,
        clock=_now,
    )
    assert r.submitted is False
    assert r.rejected_at_gate == "throttle"
    submitter.assert_not_called()


def test_throttle_passes_for_different_problem(tmp_path: Path) -> None:
    """Throttle is per-problem; P22 submission doesn't block P14."""
    audit = tmp_path / "audit.md"
    audit.parent.mkdir(parents=True, exist_ok=True)
    audit.write_text("# audit\n\n" + auto_submit.AUDIT_LOG_HEADER +
                     "| 2026-05-24T03:30:00Z | 22 | 2.00 | submitted | ok | 200 | xy |\n")
    submitter = MagicMock(return_value=_ok_submission())
    r = auto_submit.try_submit(
        14, {"vectors": []}, score=2.64,
        triple_verify=_passing_tv(),
        audit_log=audit,
        arena_top1_score=2.6,
        submitter=submitter,
        clock=_now,
    )
    assert r.submitted is True
    submitter.assert_called_once()


# ---------------- gate 5: arena #1 SOTA improvement ----------------


def test_score_below_arena_top1_blocks(tmp_path: Path) -> None:
    audit = tmp_path / "audit.md"
    submitter = MagicMock()
    # Our score 2.5 < arena #1 = 2.6 (maximize, so 2.5 does NOT beat 2.6)
    r = auto_submit.try_submit(
        14, {"vectors": []}, score=2.5,
        triple_verify=_passing_tv(),
        audit_log=audit,
        arena_top1_score=2.6,
        submitter=submitter,
        clock=_now,
    )
    assert r.submitted is False
    assert r.rejected_at_gate == "no-improvement"
    submitter.assert_not_called()


def test_score_below_min_improvement_blocks(tmp_path: Path) -> None:
    """Beating arena #1 by less than min_improvement = no submit."""
    audit = tmp_path / "audit.md"
    submitter = MagicMock()
    r = auto_submit.try_submit(
        14, {"vectors": []}, score=2.60000000000001,  # ~1e-14 over arena #1
        triple_verify=_passing_tv(),
        audit_log=audit,
        arena_top1_score=2.6,
        min_improvement=1e-8,
        submitter=submitter,
        clock=_now,
    )
    assert r.submitted is False
    assert r.rejected_at_gate == "no-improvement"


def test_minimize_problem_uses_lower_score_as_improvement(tmp_path: Path) -> None:
    """For min-target problems, lower beats higher."""
    audit = tmp_path / "audit.md"
    submitter = MagicMock(return_value=arena_submit.SubmissionResult(
        ok=True, problem_id=5, http_status=200, arena_response={"id": 1}))
    r = auto_submit.try_submit(
        5, {"points": []}, score=12.8,  # lower than arena #1 = 12.9
        triple_verify=_passing_tv(),
        audit_log=audit,
        arena_top1_score=12.9,
        minimize=True,
        submitter=submitter,
        clock=_now,
    )
    assert r.submitted is True
    submitter.assert_called_once()


def test_leaderboard_fetch_failure_blocks(tmp_path: Path) -> None:
    audit = tmp_path / "audit.md"
    submitter = MagicMock()
    r = auto_submit.try_submit(
        14, {"vectors": []}, score=2.64,
        triple_verify=_passing_tv(),
        audit_log=audit,
        leaderboard_fetcher=lambda pid: None,  # simulate network failure
        submitter=submitter,
        clock=_now,
    )
    assert r.submitted is False
    assert r.rejected_at_gate == "leaderboard-unavailable"
    submitter.assert_not_called()


# ---------------- gate 6: POST + audit ----------------


def test_all_gates_pass_submits_and_records(tmp_path: Path) -> None:
    audit = tmp_path / "audit.md"
    submitter = MagicMock(return_value=_ok_submission())
    r = auto_submit.try_submit(
        14, {"vectors": []}, score=2.64,
        triple_verify=_passing_tv(),
        audit_log=audit,
        arena_top1_score=2.6,
        submitter=submitter,
        clock=_now,
    )
    assert r.submitted is True
    assert r.rejected_at_gate is None
    submitter.assert_called_once()
    call = submitter.call_args
    assert call.args[0] == 14
    assert call.kwargs["expected_score"] == 2.64
    # Audit log records the submission with HTTP status + arena id
    text = audit.read_text()
    assert "submitted" in text
    assert "9999" in text  # arena_id from _ok_submission
    assert "200" in text


def test_post_failure_records_as_rejected(tmp_path: Path) -> None:
    """If submit_solution returns ok=False (HTTP 4xx), audit row is 'rejected'."""
    audit = tmp_path / "audit.md"
    submitter = MagicMock(return_value=arena_submit.SubmissionResult(
        ok=False, problem_id=14, http_status=429,
        arena_response={"error": "rate limited"},
        error="HTTP 429",
    ))
    r = auto_submit.try_submit(
        14, {"vectors": []}, score=2.64,
        triple_verify=_passing_tv(),
        audit_log=audit,
        arena_top1_score=2.6,
        submitter=submitter,
        clock=_now,
    )
    assert r.submitted is False
    assert r.rejected_at_gate == "post-failed"
    assert "429" in audit.read_text()


def test_dry_run_passes_all_gates_without_posting(tmp_path: Path) -> None:
    audit = tmp_path / "audit.md"
    submitter = MagicMock()
    r = auto_submit.try_submit(
        14, {"vectors": []}, score=2.64,
        triple_verify=_passing_tv(),
        audit_log=audit,
        arena_top1_score=2.6,
        dry_run=True,
        submitter=submitter,
        clock=_now,
    )
    assert r.submitted is False
    assert r.rejected_at_gate == "dry-run"
    submitter.assert_not_called()
    # Audit row still appended for the dry-run decision
    assert "dry-run" in audit.read_text()


def test_audit_log_header_created_on_first_write(tmp_path: Path) -> None:
    audit = tmp_path / "new" / "audit.md"
    auto_submit.try_submit(
        14, {"vectors": []}, score=2.64,
        triple_verify=_passing_tv(),
        audit_log=audit,
        arena_top1_score=2.6,
        submitter=MagicMock(return_value=_ok_submission()),
        clock=_now,
    )
    text = audit.read_text()
    assert "# auto-submit audit log" in text
    assert "| timestamp_utc | problem_id" in text
