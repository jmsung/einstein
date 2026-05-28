"""Tests for the Thompson skill sampler (Goal 1).

Covers: posterior shape, determinism under fixed seed, per-category masking,
empty-history / no-arm fallback, and that an overwhelmingly better arm wins
across seeds (the bandit actually exploits).
"""

from __future__ import annotations

import random
from types import SimpleNamespace

import pytest

from einstein.bandit.thompson import (
    Arm,
    ThompsonSampler,
    arm_from_row,
    sample_arms,
)


def _row(technique, category, tried, top3):
    return SimpleNamespace(technique=technique, category=category, tried=tried, top3=top3)


# A small two-category library: kissing + autocorrelation.
ROWS = [
    _row("parallel-tempering-sa.md", "kissing / Coulomb", 5, 3),
    _row("micro-perturbation-multiscale.md", "kissing", 1, 1),
    _row("larger-n-cascade.md", "autocorrelation", 4, 4),
    _row("remez-equioscillation-diagnostic.md", "autocorrelation", 2, 0),
]


# ---------------- posterior shape ----------------


def test_arm_from_row_beta_shape():
    arm = arm_from_row(_row("t.md", "kissing", tried=5, top3=3))
    assert arm.alpha == 4.0  # top3 + 1
    assert arm.beta == 3.0  # (tried - top3) + 1
    # posterior mean == Laplace-smoothed hit-rate (top3+1)/(tried+2)
    assert arm.mean == pytest.approx(4 / 7)


def test_arm_from_row_unseen_is_uniform_prior():
    arm = arm_from_row(_row("never-tried.md", "kissing", tried=0, top3=0))
    assert (arm.alpha, arm.beta) == (1.0, 1.0)  # Beta(1,1) == Uniform(0,1)
    assert arm.mean == pytest.approx(0.5)


def test_arm_from_row_guards_malformed_top3_gt_tried():
    # top3 > tried can't happen in a healthy library, but must never produce
    # an improper Beta (beta < 1).
    arm = arm_from_row(_row("bad.md", "kissing", tried=1, top3=3))
    assert arm.beta >= 1.0


# ---------------- determinism ----------------


def test_pick_deterministic_under_fixed_seed():
    s = ThompsonSampler(rows=ROWS)
    a = s.pick("kissing", rng=random.Random(42))
    b = s.pick("kissing", rng=random.Random(42))
    assert a is not None and b is not None
    assert (a.technique, a.alpha, a.beta, a.theta) == (b.technique, b.alpha, b.beta, b.theta)


def test_different_seeds_can_differ_but_stay_in_category():
    s = ThompsonSampler(rows=ROWS)
    picks = {s.pick("kissing", rng=random.Random(seed)).technique for seed in range(50)}
    # every pick is a kissing technique, never an autocorrelation arm
    assert picks <= {"parallel-tempering-sa.md", "micro-perturbation-multiscale.md"}


# ---------------- masking ----------------


def test_per_category_masking_excludes_off_category_arms():
    s = ThompsonSampler(rows=ROWS)
    kissing = {a.technique for a in s.arms_for("kissing")}
    assert kissing == {"parallel-tempering-sa.md", "micro-perturbation-multiscale.md"}
    autocorr = {a.technique for a in s.arms_for("autocorrelation")}
    assert "larger-n-cascade.md" in autocorr
    assert "parallel-tempering-sa.md" not in autocorr


def test_avoid_set_drops_techniques():
    s = ThompsonSampler(rows=ROWS)
    arms = s.arms_for("kissing", avoid={"parallel-tempering-sa.md"})
    assert {a.technique for a in arms} == {"micro-perturbation-multiscale.md"}


# ---------------- empty-history / no-arm fallback ----------------


def test_no_matching_category_returns_none():
    s = ThompsonSampler(rows=ROWS)
    assert s.pick("sphere-packing", rng=random.Random(0)) is None


def test_empty_arm_set_sample_returns_none():
    assert sample_arms([], rng=random.Random(0)) is None


def test_avoid_everything_returns_none():
    s = ThompsonSampler(rows=ROWS)
    avoid = {"parallel-tempering-sa.md", "micro-perturbation-multiscale.md"}
    assert s.pick("kissing", rng=random.Random(0), avoid=avoid) is None


# ---------------- the bandit exploits ----------------


def test_overwhelming_arm_wins_across_seeds():
    # 100/100 vs 0/100 — the strong arm should win for (almost) every seed.
    arms = [
        Arm("strong.md", alpha=101.0, beta=1.0),
        Arm("weak.md", alpha=1.0, beta=101.0),
    ]
    wins = sum(sample_arms(arms, rng=random.Random(s)).technique == "strong.md" for s in range(50))
    assert wins == 50


def test_pick_result_note_format():
    arms = [Arm("foo.md", alpha=4.0, beta=2.0)]
    res = sample_arms(arms, rng=random.Random(1))
    assert res.prior_str == "Beta(4,2)"
    note = res.note()
    assert note.startswith("technique=foo.md prior=Beta(4,2) sampled_θ=")
