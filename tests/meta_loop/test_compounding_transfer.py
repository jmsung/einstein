"""Tests for the cross-family frozen-KB injection path (pre-reg §0b transfer design)."""

from einstein.meta_loop import compounding_ablation as ca
from einstein.meta_loop.trajectory import TrajectoryPoint


def _mock_solve_fn(*, warm_bonus: float = 0.5):
    """A no-LLM solve_fn: warm cells (lessons present) close more of the gap than cold.
    Lets us test the transfer orchestration deterministically."""

    def solve_fn(problem, cfg, seed, spec):
        read = len(spec.accumulated_lessons)
        final = problem.reference_optimum if read else (0.5 * problem.reference_optimum)
        return ca.SolveResult(
            trajectory=[TrajectoryPoint(cycle_id=0, best_score=final)],
            score_coldinit=0.0,
            score_final=final,
            lesson_text=f"lesson for {problem.problem_id} (read={read})",
            attempted_techniques={"slsqp"},
            wall_clock_s=1.0,
        )

    return solve_fn


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


def test_run_transfer_experiment_pairs_cold_and_warm_transfer(tmp_path):
    a = _fam("heilbronn_triangle", ["heil-0", "heil-1"])
    b = _fam("tammes_sphere", ["tam-0"])
    out = ca.run_transfer_experiment(
        a,
        b,
        seeds=[1, 2],
        solve_fn=_mock_solve_fn(),
        results_dir=tmp_path,
        replicates=1,
    )
    recs = out["records"]
    # 2 seeds × 1 B-problem × {cold, warm_transfer} = 4 records
    assert len(recs) == 4
    assert out["family_a"] == "heilbronn_triangle" and out["family_b"] == "tammes_sphere"
    cold = [r for r in recs if r.arm == "cold"]
    warm = [r for r in recs if r.arm == "warm_transfer"]
    assert len(cold) == 2 and len(warm) == 2
    # The one variable: warm-transfer read KB_A lessons; cold read none.
    assert all(r.lessons_read == 0 for r in cold)
    assert all(r.lessons_read == len(a) for r in warm)  # KB_A has one lesson per A problem
    # Warm-transfer closes more gap than cold (the mock's manipulation).
    assert all(r.gap_closed == 0.5 for r in cold)
    assert all(r.gap_closed == 1.0 for r in warm)
    # KB_A hash is recorded and stable per seed.
    assert set(out["kb_a_hashes"]) == {1, 2}
    assert all(r.kb_a_hash == out["kb_a_hashes"][r.seed] for r in recs)


def test_is_solved_separates_bimodal_outcomes():
    assert ca.is_solved(1.0) and ca.is_solved(0.97)
    assert not ca.is_solved(0.0) and not ca.is_solved(0.49)


def test_solve_rate_screen_keeps_intermediate_rate(tmp_path):
    # Mock: "mid" solves on even seeds only (rate 0.5); "easy" always; "hard" never.
    def solve_fn(problem, cfg, seed, spec):
        solved = {"mid": seed % 2 == 0, "easy": True, "hard": False}[problem.family]
        final = problem.reference_optimum if solved else 0.0
        return ca.SolveResult(
            trajectory=[TrajectoryPoint(0, final)],
            score_coldinit=0.0,
            score_final=final,
            lesson_text=None,
            wall_clock_s=10.0,
        )

    problems = _fam("mid", ["m0"]) + _fam("easy", ["e0"]) + _fam("hard", ["h0"])
    out = ca.solve_rate_screen(
        problems, solve_fn, seeds=[1, 2, 3, 4], results_dir=tmp_path, band=(0.2, 0.8)
    )
    rate = {r.problem_id: r.solve_rate for r in out["results"]}
    assert rate["m0"] == 0.5 and rate["e0"] == 1.0 and rate["h0"] == 0.0
    assert out["eligible"] == {"m0": True, "e0": False, "h0": False}  # only mid has headroom


def test_transfer_solve_rates_computes_warm_minus_cold_delta():
    def rec(fb, arm, gap):
        return ca.TransferRecord(
            family_a="heilbronn_triangle",
            family_b=fb,
            problem_id="p",
            arm=arm,
            seed=1,
            score_coldinit=0.0,
            score_final=gap,
            gap_closed=gap,
            gap_closed_reps=(gap,),
            lessons_read=0,
            kb_a_hash="h",
            wall_clock_s=1.0,
        )

    records = [
        rec("tammes_sphere", "cold", 1.0),
        rec("tammes_sphere", "cold", 0.0),
        rec("tammes_sphere", "warm_transfer", 1.0),
        rec("tammes_sphere", "warm_transfer", 1.0),
        rec("autocorrelation_seq", "cold", 0.0),
        rec("autocorrelation_seq", "warm_transfer", 0.0),
    ]
    out = ca.transfer_solve_rates(records)
    assert out["tammes_sphere"]["cold_solve_rate"] == 0.5
    assert out["tammes_sphere"]["warm_solve_rate"] == 1.0
    assert out["tammes_sphere"]["delta"] == 0.5
    assert out["autocorrelation_seq"]["delta"] == 0.0


def test_headroom_probe_flags_in_band_families(tmp_path):
    def solve_fn(problem, cfg, seed, spec):
        # easy family closes ~0.95 of the gap; medium ~0.5; hard ~0.05
        frac = {"easy": 0.95, "medium": 0.5, "hard": 0.05}[problem.family]
        return ca.SolveResult(
            trajectory=[TrajectoryPoint(0, frac)],
            score_coldinit=0.0,
            score_final=frac * problem.reference_optimum,
            lesson_text=None,
        )

    problems = (
        _fam("easy", ["e0", "e1"]) + _fam("medium", ["m0", "m1"]) + _fam("hard", ["h0", "h1"])
    )
    out = ca.headroom_probe(problems, solve_fn, seeds=[1], results_dir=tmp_path, band=(0.2, 0.8))
    assert out["eligible"] == {"easy": False, "medium": True, "hard": False}
    medium_rows = [r for r in out["results"] if r.family == "medium"]
    assert all(r.in_band for r in medium_rows)


def _problem() -> ca.Problem:
    return ca.Problem(
        problem_id="autocorr-32",
        n=32,
        sequence_index=0,
        reference_optimum=1.0,
        statement="maximize ...",
        family="autocorrelation_seq",
    )


def test_load_problems_supports_per_problem_family_and_inline_statement(tmp_path):
    cfg = tmp_path / "transfer.yaml"
    cfg.parent.mkdir(parents=True, exist_ok=True)
    cfg.write_text(
        "family: heilbronn_triangle\n"
        "minimize: false\n"
        "problems:\n"
        "  - id: a0\n    n: 7\n    sequence_index: 0\n    reference_optimum: 1.0\n"
        "    statement: build KB here\n"
        "  - id: b0\n    family: tammes_sphere\n    n: 12\n    sequence_index: 1\n"
        "    reference_optimum: 1.05\n    statement: transfer target\n"
    )
    probs = ca.load_problems(cfg)
    assert [p.family for p in probs] == ["heilbronn_triangle", "tammes_sphere"]
    assert probs[1].statement == "transfer target"


def test_load_frozen_kb_reads_prior_run(tmp_path):
    kb = ca.RunKB(tmp_path / "kb-a")
    kb.write_lesson("heilbronn-7", "lesson one: SLSQP on active pairs")
    kb.write_lesson("heilbronn-8", "lesson two: anneal then polish")
    frozen = ca.load_frozen_kb(tmp_path / "kb-a")
    assert frozen == ("lesson one: SLSQP on active pairs", "lesson two: anneal then polish")


def test_warm_transfer_arm_carries_frozen_kb_with_empty_run_kb(tmp_path):
    """A pure transfer cell: the warm arm's knowledge IS exactly KB_A."""
    frozen = ("A-lesson: shrink-regrow operator", "A-lesson: avoid cold restarts")
    run_kb = ca.RunKB(tmp_path / "kb-b")  # empty — this is the first B problem
    spec = ca.build_session_spec(
        _problem(), ca.Arm.WARM, seed=1, run_kb=run_kb, frozen_kb_lessons=frozen
    )
    assert spec.accumulated_lessons == frozen


def test_frozen_kb_prepends_within_run_lessons(tmp_path):
    frozen = ("A-lesson",)
    run_kb = ca.RunKB(tmp_path / "kb-b")
    run_kb.write_lesson("b-0", "B-lesson")
    spec = ca.build_session_spec(
        _problem(), ca.Arm.WARM, seed=1, run_kb=run_kb, frozen_kb_lessons=frozen
    )
    assert spec.accumulated_lessons == ("A-lesson", "B-lesson")


def test_cold_arm_ignores_frozen_kb(tmp_path):
    """Cold never reads any KB — frozen or not — preserving the one-variable invariant."""
    spec = ca.build_session_spec(
        _problem(),
        ca.Arm.COLD,
        seed=1,
        run_kb=ca.RunKB(tmp_path / "kb"),
        frozen_kb_lessons=("A-lesson",),
    )
    assert spec.accumulated_lessons == ()


def test_within_family_path_unchanged_when_frozen_none(tmp_path):
    run_kb = ca.RunKB(tmp_path / "kb")
    run_kb.write_lesson("p-0", "within-lesson")
    spec = ca.build_session_spec(_problem(), ca.Arm.WARM, seed=1, run_kb=run_kb)
    assert spec.accumulated_lessons == ("within-lesson",)


def test_frozen_plus_within_respects_char_cap(tmp_path):
    frozen = ("x" * 30,)
    run_kb = ca.RunKB(tmp_path / "kb")
    run_kb.write_lesson("p-0", "y" * 30)
    # cap fits only the first (frozen) lesson; the second whole lesson is dropped
    spec = ca.build_session_spec(
        _problem(),
        ca.Arm.WARM,
        seed=1,
        run_kb=run_kb,
        max_lesson_chars=40,
        frozen_kb_lessons=frozen,
    )
    assert spec.accumulated_lessons == frozen
