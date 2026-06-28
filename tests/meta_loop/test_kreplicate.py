"""k-replicate variance reduction in run_arm_sequence (compounding_ablation).

Each cell is solved `replicates` times with independent cold-inits and the
per-replicate gap_closed values are averaged (mean-of-gaps). Exactly one lesson
(the first replicate's) is persisted, so Warm's one-lesson-per-problem KB
invariant — and the §9 manipulation check — are unchanged. replicates=1 must
reproduce the legacy single-solve behavior.
"""

import statistics
from dataclasses import dataclass
from pathlib import Path

from einstein.meta_loop import compounding_ablation as ca


@dataclass
class _TP:  # duck-typed TrajectoryPoint (cycle_id, best_score)
    cycle_id: int
    best_score: float


def _problems():
    return [
        ca.Problem(problem_id="p-a", n=11, sequence_index=0, reference_optimum=1.0, statement="s"),
        ca.Problem(problem_id="p-b", n=12, sequence_index=1, reference_optimum=1.0, statement="s"),
    ]


def _solve_fn(problem, cfg, seed, spec):
    # gap_closed = (final - 0) / (1 - 0) = final; vary it with the replicate index
    # so the three replicates yield gaps 0.1, 0.2, 0.3.
    final = 0.1 * (spec.replicate + 1)
    return ca.SolveResult(
        trajectory=[_TP(0, 0.0), _TP(1, final)],
        score_coldinit=0.0,
        score_final=final,
        lesson_text=f"lesson {problem.problem_id} rep{spec.replicate}",
        attempted_techniques={"slsqp"},
        wall_clock_s=1.0,
    )


def test_replicates_average_gap_and_preserve_kb_invariant(tmp_path):
    kb = ca.RunKB(tmp_path / "warm-kb")
    recs = ca.run_arm_sequence(
        ca.Arm.WARM, 0, _problems(), _solve_fn, kb,
        order=ca.cyclic_order(_problems(), 0), replicates=3,
    )
    for r in recs:
        assert r.gap_closed == 0.2  # mean of 0.1, 0.2, 0.3
        assert r.replicates == 3
        assert r.gap_closed_reps == (0.1, 0.2, 0.3)
        assert r.gap_closed_std == statistics.stdev([0.1, 0.2, 0.3])
        assert r.wall_clock_s == 3.0  # summed across replicates (total cell compute)
    # one lesson per problem, and it is the FIRST replicate's (banked-count intact)
    assert kb.lesson_count() == 2
    for p in sorted((tmp_path / "warm-kb").glob("lesson-*.md")):
        assert "rep0" in p.read_text()


def test_replicates_one_reproduces_legacy(tmp_path):
    kb = ca.RunKB(tmp_path / "warm-kb")
    recs = ca.run_arm_sequence(
        ca.Arm.WARM, 0, _problems(), _solve_fn, kb,
        order=ca.cyclic_order(_problems(), 0), replicates=1,
    )
    for r in recs:
        assert r.gap_closed == 0.1  # rep0 only
        assert r.replicates == 1
        assert r.gap_closed_std == 0.0
        assert r.gap_closed_reps == (0.1,)


def test_to_dict_carries_replicate_fields(tmp_path):
    kb = ca.RunKB(tmp_path / "warm-kb")
    recs = ca.run_arm_sequence(
        ca.Arm.WARM, 0, _problems(), _solve_fn, kb,
        order=ca.cyclic_order(_problems(), 0), replicates=2,
    )
    d = recs[0].to_dict()
    assert d["replicates"] == 2
    assert d["gap_closed_reps"] == [0.1, 0.2]
    assert "gap_closed_std" in d


def test_default_replicates_is_legacy(tmp_path):
    # omitting `replicates` must behave exactly like replicates=1
    kb = ca.RunKB(tmp_path / "warm-kb")
    recs = ca.run_arm_sequence(
        ca.Arm.WARM, 0, _problems(), _solve_fn, kb,
        order=ca.cyclic_order(_problems(), 0),
    )
    assert all(r.replicates == 1 and r.gap_closed == 0.1 for r in recs)
