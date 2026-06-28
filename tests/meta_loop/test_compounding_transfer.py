"""Tests for the cross-family frozen-KB injection path (pre-reg §0b transfer design)."""

from einstein.meta_loop import compounding_ablation as ca


def _problem() -> ca.Problem:
    return ca.Problem(
        problem_id="autocorr-32",
        n=32,
        sequence_index=0,
        reference_optimum=1.0,
        statement="maximize ...",
        family="autocorrelation_seq",
    )


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
