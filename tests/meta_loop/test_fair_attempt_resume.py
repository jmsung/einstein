"""Tests for the fair-attempt guard + transfer-runner resume (offline/rate-limit safety).

`fair_attempt` decides whether a SolveResult is a genuine budgeted attempt worth
RECORDING, or an infra/offline fast-fail that should be RETRIED on resume (not recorded
as a bogus gap=0 cell). The transfer runner is also made resumable + guarded so an
overnight WiFi drop / 429 storm never poisons the data and never re-solves a done cell.
"""

from __future__ import annotations

import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import compounding_ablation as ca  # noqa: E402
from einstein.meta_loop.trajectory import TrajectoryPoint  # noqa: E402


def _res(*, ok=True, error_kind="", wall=120.0, lesson="lesson"):
    return ca.SolveResult(
        trajectory=[TrajectoryPoint(0, 0.0)],
        score_coldinit=0.0,
        score_final=0.0,
        lesson_text=lesson,
        wall_clock_s=wall,
        ok=ok,
        error_kind=error_kind,
    )


# ---------------- fair_attempt: all five branches ----------------


def test_fair_attempt_unavailable_is_unfair():
    # auth/quota/429/overload — always transient, retry on resume
    assert ca.fair_attempt(_res(ok=False, error_kind="unavailable", wall=2.0)) is False
    # even a "slow" unavailable is still transient
    assert ca.fair_attempt(_res(ok=False, error_kind="unavailable", wall=9999.0)) is False


def test_fair_attempt_timeout_is_fair():
    # a real timeout ran the full budget — a VALID budgeted result
    assert ca.fair_attempt(_res(ok=False, error_kind="timeout", wall=600.0)) is True


def test_fair_attempt_ok_is_fair():
    assert ca.fair_attempt(_res(ok=True, error_kind="", wall=42.0)) is True


def test_fair_attempt_nonok_fast_is_unfair():
    # non-ok that returned quickly (< fast_fail_s) looks like an infra fast-fail
    assert ca.fair_attempt(_res(ok=False, error_kind="non-zero", wall=2.0)) is False


def test_fair_attempt_nonok_slow_is_fair():
    # non-ok that ran a long time is treated as a genuine (if failed) attempt
    assert ca.fair_attempt(_res(ok=False, error_kind="non-zero", wall=120.0)) is True


# ---------------- transfer guard: a transient cell is NOT recorded ----------------


def _fam(family, ids):
    return [
        ca.Problem(
            problem_id=pid,
            n=8,
            sequence_index=i,
            reference_optimum=1.0,
            statement="maximize",
            family=family,
        )
        for i, pid in enumerate(ids)
    ]


def test_transfer_skips_transient_cell(tmp_path):
    """A fast-fail (ok=False, non-zero, wall<60) B-cell must not appear in records;
    a normal cell must. The guard fires on the COLD arm of the B-problem here."""

    def solve_fn(problem, cfg, seed, spec):
        # A-phase (heilbronn) and the warm B-arm solve cleanly; the cold B-arm fast-fails.
        if problem.family == "tammes_sphere" and len(spec.accumulated_lessons) == 0:
            return _res(ok=False, error_kind="non-zero", wall=2.0)  # transient cold cell
        return _res(ok=True, error_kind="", wall=120.0)

    a = _fam("heilbronn_triangle", ["heil-0"])
    b = _fam("tammes_sphere", ["tam-0"])
    out = ca.run_transfer_experiment(a, b, seeds=[1], solve_fn=solve_fn, results_dir=tmp_path)
    recs = out["records"]
    # cold cell was transient → dropped; only the warm_transfer cell is recorded.
    assert out["n_skipped_transient"] == 1
    assert [r.arm for r in recs] == ["warm_transfer"]
    assert all(r.fair for r in recs)


# ---------------- transfer resume: done cells are not re-solved ----------------


class _Counter:
    def __init__(self):
        self.calls: list[tuple[str, str, int]] = []

    def fn(self, problem, cfg, seed, spec):
        arm = "warm_transfer" if spec.accumulated_lessons else "cold"
        self.calls.append((problem.problem_id, arm, seed))
        return _res(ok=True, error_kind="", wall=120.0)


def test_warm_a_phase_transient_not_persisted(tmp_path):
    """A transient WARM failure must NOT freeze a junk lesson into the KB and must not be
    recorded — else a frozen KB_A (or the compounding warm arm) is permanently poisoned,
    and A-resume skips the junk cell forever. The A-phase analogue of the B-cell guard.
    On resume the cell retries and persists the real lesson."""
    probs = _fam("heilbronn_triangle", ["heil-0", "heil-1"])
    kb = ca.RunKB(tmp_path / "kb-a")

    # First pass: heil-1 fast-fails (offline-like); heil-0 solves cleanly.
    def flaky(problem, cfg, seed, spec):
        if problem.problem_id == "heil-1":
            return _res(ok=False, error_kind="non-zero", wall=2.0, lesson="JUNK")
        return _res(ok=True, error_kind="", wall=120.0, lesson="real-0")

    recs = ca.run_arm_sequence(ca.Arm.WARM, 1, probs, flaky, kb)
    ids = {r.problem_id for r in recs}
    assert "heil-1" not in ids  # transient cell not recorded
    assert set(kb.lesson_problem_ids()) == {"heil-0"}  # NO junk lesson frozen for heil-1

    # Resume: skip the recorded (good) problem; heil-1 retries and now succeeds.
    def healthy(problem, cfg, seed, spec):
        return _res(ok=True, error_kind="", wall=120.0, lesson=f"real-{problem.problem_id}")

    recs2 = ca.run_arm_sequence(ca.Arm.WARM, 1, probs, healthy, kb, skip_done=ids)
    assert {r.problem_id for r in recs2} == {"heil-1"}
    assert set(kb.lesson_problem_ids()) == {"heil-0", "heil-1"}


def test_transfer_resume_skips_done_cells(tmp_path):
    a = _fam("heilbronn_triangle", ["heil-0", "heil-1"])
    b = _fam("tammes_sphere", ["tam-0"])

    c1 = _Counter()
    out1 = ca.run_transfer_experiment(a, b, seeds=[1], solve_fn=c1.fn, results_dir=tmp_path)
    recs1 = out1["records"]
    assert len(recs1) == 2  # cold + warm_transfer for the single B problem
    # A-phase: heil-0, heil-1 each solved once; B-phase: tam-0 cold + warm.
    b_calls_run1 = [c for c in c1.calls if c[0] == "tam-0"]
    assert len(b_calls_run1) == 2

    # Build skip_done from the run-1 B records and re-run on the SAME results_dir.
    skip_done = {(r.problem_id, r.arm, r.seed) for r in recs1}
    c2 = _Counter()
    out2 = ca.run_transfer_experiment(
        a, b, seeds=[1], solve_fn=c2.fn, results_dir=tmp_path, skip_done=skip_done
    )
    # No B-cell re-solved (both done); no A-problem re-solved (lessons persist on disk).
    assert [c for c in c2.calls if c[0] == "tam-0"] == []
    assert [c for c in c2.calls if c[0] in {"heil-0", "heil-1"}] == []
    assert out2["records"] == []
    # KB_A hash is stable across the resume (same persisted lessons).
    assert out2["kb_a_hashes"] == out1["kb_a_hashes"]
