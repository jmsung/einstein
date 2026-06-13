"""Tests for src/einstein/meta_loop/trajectory.py — Goal 1.

The trajectory metric turns the cycle-log into a per-problem
best-verified-score-vs-cycle curve and classifies each problem as
improving / solved-at-floor / stuck / unknown. This is the closed-loop
signal that says *better/worse*, not just *ran*.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import trajectory as tj  # noqa: E402
from einstein.meta_loop.diagnose import CycleRow  # noqa: E402


def _row(cid: int, problem: str, score_field: str, outcome: str = "no-change") -> CycleRow:
    return CycleRow(
        cycle_id=cid,
        problem=problem,
        score_field=score_field,
        hours="0",
        compute="local-cpu",
        wiki_citations="0",
        findings_added="0",
        concepts_added="0",
        author_mix="a:1/h:0/hyb:0",
        outcome=outcome,
        notes="",
    )


# ---------------- parse_score ----------------


@pytest.mark.parametrize(
    "field,expected",
    [
        ("2.6 → 2.7", (2.6, 2.7)),
        ("2.6390274695 → 2.6390274695", (2.6390274695, 2.6390274695)),
        ("0.380870310586 (no Δ)", (0.380870310586, 0.380870310586)),
        ("1.5028616283498 (no Δ)", (1.5028616283498, 1.5028616283498)),
        ("none (no Δ)", (None, None)),
        ("(n/a)", (None, None)),
        ("(HIDDEN)", (None, None)),
        ("(HIDDEN) → (HIDDEN)", (None, None)),
        ("37147.5253 → 37147.5253", (37147.5253, 37147.5253)),
        ("1e-13 → 2e-13", (1e-13, 2e-13)),
    ],
)
def test_parse_score(field, expected):
    assert tj.parse_score(field) == expected


# ---------------- problem_id_of ----------------


@pytest.mark.parametrize(
    "label,expected",
    [
        ("P19 difference-bases", 19),
        ("P19-difference-bases", 19),
        ("P1-erdos-overlap", 1),
        ("P16-heilbronn-convex", 16),
        ("refactor", None),
        ("P10 Thomson ablation audit", 10),
    ],
)
def test_problem_id_of(label, expected):
    assert tj.problem_id_of(label) == expected


# ---------------- problem_trajectory ----------------


def test_trajectory_running_best_minimize():
    """For a minimize problem, running-best is the lowest end-score so far."""
    rows = [
        _row(1, "P2-first-autocorrelation", "1.6 → 1.55"),
        _row(2, "P19-difference-bases", "2.6 → 2.6"),  # different problem ignored
        _row(3, "P2-first-autocorrelation", "1.55 → 1.60"),  # worse end, best holds
        _row(4, "P2-first-autocorrelation", "1.60 → 1.50"),  # new best
    ]
    traj = tj.problem_trajectory(rows, problem_id=2, minimize=True)
    assert [(p.cycle_id, p.best_score) for p in traj] == [
        (1, 1.55),
        (3, 1.55),
        (4, 1.50),
    ]


def test_trajectory_running_best_maximize():
    rows = [
        _row(1, "P11-tammes", "0.51 → 0.52"),
        _row(2, "P11-tammes", "0.52 → 0.50"),  # worse, best holds
        _row(3, "P11-tammes", "0.50 → 0.55"),  # new best
    ]
    traj = tj.problem_trajectory(rows, problem_id=11, minimize=False)
    assert [p.best_score for p in traj] == [0.52, 0.52, 0.55]


def test_trajectory_skips_unparseable_scores():
    rows = [
        _row(1, "P1-erdos", "(n/a)"),
        _row(2, "P1-erdos", "0.38 → 0.38"),
        _row(3, "P1-erdos", "(HIDDEN)"),
    ]
    traj = tj.problem_trajectory(rows, problem_id=1, minimize=True)
    assert [(p.cycle_id, p.best_score) for p in traj] == [(2, 0.38)]


# ---------------- classify ----------------


def test_classify_solved_at_floor_when_certificate_present():
    """A certificate beats every other signal — even with apparent headroom."""
    traj = [tj.TrajectoryPoint(1, 2.639), tj.TrajectoryPoint(2, 2.639)]
    c = tj.classify(traj, headroom=0.0, certificate="bnb-negative-lemma")
    assert c is tj.Classification.SOLVED_AT_FLOOR


def test_classify_improving_when_recent_strict_gain():
    traj = [
        tj.TrajectoryPoint(1, 1.60),
        tj.TrajectoryPoint(2, 1.55),
        tj.TrajectoryPoint(3, 1.50),
    ]
    c = tj.classify(traj, headroom=0.01, certificate=None, minimize=True)
    assert c is tj.Classification.IMPROVING


def test_classify_stuck_when_flat_with_open_headroom():
    traj = [tj.TrajectoryPoint(i, 1.50) for i in range(1, 6)]
    c = tj.classify(traj, headroom=0.02, certificate=None, minimize=True)
    assert c is tj.Classification.STUCK


def test_classify_unknown_when_no_headroom_no_cert_flat():
    """Flat, no certificate, no known headroom → we honestly don't know."""
    traj = [tj.TrajectoryPoint(i, 1.50) for i in range(1, 6)]
    c = tj.classify(traj, headroom=None, certificate=None, minimize=True)
    assert c is tj.Classification.UNKNOWN


def test_classify_unknown_when_empty():
    assert tj.classify([], headroom=0.1, certificate=None) is tj.Classification.UNKNOWN


def test_classify_improving_respects_window():
    """An old gain outside the window does not count as improving."""
    traj = [
        tj.TrajectoryPoint(1, 1.60),
        tj.TrajectoryPoint(2, 1.50),  # the gain
        tj.TrajectoryPoint(3, 1.50),
        tj.TrajectoryPoint(4, 1.50),
        tj.TrajectoryPoint(5, 1.50),
    ]
    assert tj.classify(traj, headroom=0.02, certificate=None, minimize=True, window=3) is (
        tj.Classification.STUCK
    )


# ---------------- certificate_of ----------------


def test_certificate_of_reads_field():
    assert tj.certificate_of({"certificate": "dual-cert"}) == "dual-cert"


@pytest.mark.parametrize("val", ["none", "None", "", "  ", "false", "no"])
def test_certificate_of_treats_falsy_as_none(val):
    assert tj.certificate_of({"certificate": val}) is None


def test_certificate_of_missing_is_none():
    assert tj.certificate_of({}) is None


# ---------------- aggregate ----------------


def test_aggregate_counts_and_rates():
    classifications = [
        tj.ProblemClassification(2, "P2", tj.Classification.SOLVED_AT_FLOOR, [], 0.0, "cert"),
        tj.ProblemClassification(19, "P19", tj.Classification.SOLVED_AT_FLOOR, [], 0.0, "lemma"),
        tj.ProblemClassification(1, "P1", tj.Classification.STUCK, [], 0.02, None),
        tj.ProblemClassification(11, "P11", tj.Classification.IMPROVING, [], 0.01, None),
        tj.ProblemClassification(7, "P7", tj.Classification.UNKNOWN, [], None, None),
    ]
    rows = [
        _row(1, "P2", "1.6 → 1.5", outcome="improved"),
        _row(2, "P2", "1.5 → 1.5", outcome="no-change"),
        _row(3, "P11", "0.5 → 0.55", outcome="conquered"),
        _row(4, "P1", "0.4 → 0.4", outcome="no-change"),
    ]
    agg = tj.aggregate(classifications, rows, rank1_ids={11})

    assert agg.num_rank_1 == 1
    assert agg.num_solved_at_floor == 2
    assert agg.num_stuck == 1
    assert agg.num_improving == 1
    # 2 improvement-outcome cycles ("improved", "conquered") over 4 cycles → 50/100
    assert agg.records_per_100_cycles == pytest.approx(50.0)
    # solved / (solved + stuck) = 2 / 3
    assert agg.headroom_closed_rate == pytest.approx(2 / 3)


def test_aggregate_zero_cycles_safe():
    agg = tj.aggregate([], [], rank1_ids=set())
    assert agg.records_per_100_cycles == 0.0
    assert agg.headroom_closed_rate == 0.0


# ---------------- build_classifications ----------------


def test_build_classifications_end_to_end():
    rows = [
        _row(1, "P19-difference-bases", "2.639 → 2.639"),
        _row(2, "P2-first-autocorrelation", "1.60 → 1.55"),
        _row(3, "P2-first-autocorrelation", "1.55 → 1.50"),
        _row(4, "P1-erdos-overlap", "0.38 → 0.38"),
    ]
    specs = [
        tj.ProblemSpec(19, "P19", {"certificate": "bnb-negative-lemma"}),
        tj.ProblemSpec(2, "P2", {}),
        tj.ProblemSpec(1, "P1", {"certificate": "none"}),
    ]
    headrooms = {19: 0.0, 2: 0.01, 1: 0.05}
    out = {pc.problem_id: pc for pc in tj.build_classifications(rows, specs, headrooms)}

    assert out[19].classification is tj.Classification.SOLVED_AT_FLOOR
    assert out[2].classification is tj.Classification.IMPROVING
    assert out[1].classification is tj.Classification.STUCK  # flat + open headroom
    assert out[2].certificate is None


def test_build_classifications_skips_unknown_direction():
    """A problem id absent from PROBLEM_MINIMIZE (and with no override) is
    skipped rather than guessed."""
    rows = [_row(1, "P99-fake", "1.0 → 1.0")]
    specs = [tj.ProblemSpec(99, "P99", {})]
    assert tj.build_classifications(rows, specs, {99: 0.1}) == []
