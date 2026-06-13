"""Tests for src/einstein/meta_loop/ablation.py — Goal 6 3-arm ablation harness.

Covers the test-plan obligations: arms isolated (A/B/C knowledge access); B
firewall verified (no leaderboard/repo/solution leak); N-seed run matrix;
distributional comparison.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import ablation as ab  # noqa: E402
from einstein.meta_loop.trajectory import TrajectoryPoint  # noqa: E402

# ---------------- arm isolation ----------------


def test_arms_are_isolated():
    assert ab.arms_isolated() is True
    a = ab.ARM_CONFIGS[ab.Arm.CURATED_WIKI]
    b = ab.ARM_CONFIGS[ab.Arm.WEB_SEARCH]
    c = ab.ARM_CONFIGS[ab.Arm.MODEL_ONLY]
    assert (a.allow_wiki, a.allow_web) == (True, False)
    assert (b.allow_wiki, b.allow_web) == (False, True)
    assert (c.allow_wiki, c.allow_web) == (False, False)


# ---------------- firewall ----------------


@pytest.mark.parametrize("url", ab.ANSWER_KEY_PROBES)
def test_firewall_blocks_every_answer_key_probe(url):
    assert ab.is_firewalled(url) is True


def test_firewall_verified_helper():
    assert ab.firewall_verified(list(ab.ANSWER_KEY_PROBES)) is True


@pytest.mark.parametrize(
    "url",
    [
        "https://arxiv.org/abs/1902.05438",
        "https://en.wikipedia.org/wiki/Sidon_set",
        "https://mathoverflow.net/questions/12345",
    ],
)
def test_firewall_allows_general_references(url):
    assert ab.is_firewalled(url) is False


def test_assert_allowed_raises_on_answer_key():
    with pytest.raises(ab.FirewallViolation):
        ab.assert_allowed("https://einsteinarena.com/leaderboard")
    # general reference passes silently
    ab.assert_allowed("https://arxiv.org/abs/2026.00001")


def test_firewall_blocks_arena_subdomain():
    assert ab.is_firewalled("https://www.einsteinarena.com/problems/x") is True


def test_firewall_blocks_local_solution_path():
    assert ab.is_firewalled("/home/u/einstein/mb/problems/4/solutions/best.json") is True


# ---------------- run matrix ----------------


def test_build_run_matrix_is_full_cross_product():
    matrix = ab.build_run_matrix([4, 19], [1, 2, 3])
    assert len(matrix) == 2 * 3 * 3  # problems × arms × seeds
    # every (problem, arm, seed) combination present exactly once
    keys = {(r.problem_id, r.arm, r.seed) for r in matrix}
    assert len(keys) == len(matrix)
    # ordered problem → arm → seed
    assert matrix[0].label == "P4-A-curated_wiki-seed1"


# ---------------- measurement ----------------


def test_climb_rate_minimize_positive_when_improving():
    traj = [TrajectoryPoint(1, 2.0), TrajectoryPoint(3, 1.6)]
    assert ab.climb_rate(traj, minimize=True) == pytest.approx(0.2)  # (2.0-1.6)/2


def test_climb_rate_maximize():
    traj = [TrajectoryPoint(1, 0.5), TrajectoryPoint(5, 0.7)]
    assert ab.climb_rate(traj, minimize=False) == pytest.approx(0.05)  # (0.7-0.5)/4


def test_climb_rate_flat_and_short_are_zero():
    assert ab.climb_rate([TrajectoryPoint(1, 1.0)], minimize=True) == 0.0
    assert ab.climb_rate([TrajectoryPoint(1, 1.0), TrajectoryPoint(2, 1.0)], minimize=True) == 0.0


def test_cycles_to_fraction_of_floor_minimize():
    # start 2.0, floor 1.0; 50% gap closed at score ≤ 1.5
    traj = [TrajectoryPoint(1, 1.9), TrajectoryPoint(2, 1.6), TrajectoryPoint(3, 1.4)]
    cyc = ab.cycles_to_fraction_of_floor(traj, start=2.0, floor=1.0, fraction=0.5, minimize=True)
    assert cyc == 3  # first cycle reaching ≤ 1.5


def test_cycles_to_fraction_none_when_not_reached():
    traj = [TrajectoryPoint(1, 1.9), TrajectoryPoint(2, 1.85)]
    assert (
        ab.cycles_to_fraction_of_floor(traj, start=2.0, floor=1.0, fraction=0.5, minimize=True)
        is None
    )


def test_dead_ends_avoided():
    known = {"sdp-lift.md", "cold-seed.md", "different-k.md"}
    attempted = {"cold-seed.md", "warm-pruning.md"}
    assert ab.dead_ends_avoided(attempted, known) == 2  # sdp-lift + different-k avoided


# ---------------- distributional comparison ----------------


def test_summarize_arm_stats():
    s = ab.summarize_arm(ab.Arm.CURATED_WIKI, [0.2, 0.4, 0.3])
    assert s.n_seeds == 3
    assert s.mean_climb_rate == pytest.approx(0.3)
    assert s.median_climb_rate == pytest.approx(0.3)


def test_summarize_arm_empty_safe():
    s = ab.summarize_arm(ab.Arm.MODEL_ONLY, [])
    assert s.n_seeds == 0 and s.mean_climb_rate == 0.0


def test_rank_arms_orders_by_mean_climb_rate():
    ranked = ab.rank_arms(
        {
            ab.Arm.CURATED_WIKI: [0.4, 0.5],
            ab.Arm.WEB_SEARCH: [0.2, 0.3],
            ab.Arm.MODEL_ONLY: [0.0, 0.1],
        }
    )
    assert [s.arm for s in ranked] == [ab.Arm.CURATED_WIKI, ab.Arm.WEB_SEARCH, ab.Arm.MODEL_ONLY]
