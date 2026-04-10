"""Tests for Difference Bases (Problem 19) evaluator."""

from __future__ import annotations

from einstein.difference_bases.evaluator import (
    coverage,
    evaluate,
    score_set,
    verify_and_compute,
)


def test_trivial_consecutive_set() -> None:
    """{0,1,2,3,4} covers diffs {1,2,3,4}, k=5, v=4, score=25/4."""
    score, k, v = score_set([0, 1, 2, 3, 4])
    assert k == 5
    assert v == 4
    assert score == 25 / 4


def test_zero_added_automatically() -> None:
    """Per problem spec: 0 must be present and is auto-added if missing."""
    a, _, _ = score_set([1, 3, 7])
    b, _, _ = score_set([0, 1, 3, 7])
    assert a == b


def test_dedup_and_sort() -> None:
    """Input is deduplicated and sorted before scoring."""
    a, _, _ = score_set([3, 1, 1, 0, 7, 3])
    b, _, _ = score_set([0, 1, 3, 7])
    assert a == b


def test_coverage_simple() -> None:
    """B={0,1,3} → diffs={1,2,3}, v=3."""
    assert coverage([0, 1, 3]) == 3


def test_coverage_gap_breaks_at_first_missing() -> None:
    """B={0,1,2,5} → diffs={1,2,3,5,4}, missing nothing up to 5? Actually:
    differences: 1-0=1, 2-0=2, 5-0=5, 2-1=1, 5-1=4, 5-2=3 → {1,2,3,4,5}, v=5."""
    assert coverage([0, 1, 2, 5]) == 5


def test_coverage_breaks_at_4() -> None:
    """B={0,1,2,7}: diffs={1,2,7,6,5} → {1,2,5,6,7} — missing 3, v=2."""
    assert coverage([0, 1, 2, 7]) == 2


def test_evaluate_dict_form() -> None:
    """evaluate({"set": [...]}) returns the score."""
    assert evaluate({"set": [0, 1, 2, 3, 4]}) == 25 / 4


def test_verify_and_compute_alias() -> None:
    """verify_and_compute mirrors arena verifier signature: returns score float."""
    assert verify_and_compute([0, 1, 2, 3, 4]) == 25 / 4


def test_score_invariant_to_input_order() -> None:
    """score_set is order-independent (set semantics)."""
    base = [0, 5, 11, 13, 17, 23]
    s1, _, _ = score_set(base)
    s2, _, _ = score_set(list(reversed(base)))
    s3, _, _ = score_set(base + base)  # duplicates allowed in input
    assert s1 == s2 == s3
