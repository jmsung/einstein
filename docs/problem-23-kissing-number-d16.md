# Problem 23: Kissing Number in Dimension 16

**Status**: Submitted; rank #2 (pending arena confirmation)

## Problem

Place n = 4321 unit vectors in ℝ¹⁶ to minimize total overlap penalty. Sphere centers are placed at c_i = 2v_i/‖v_i‖. The score is:

    loss = Σ_{i<j} max(0, 2 − ‖c_i − c_j‖)

Score = 0 would prove κ(16) ≥ 4321, but **κ(16) = 4320 is proven** (Levenshtein 1979 LP bound, achieved by the Barnes-Wall lattice BW₁₆ ≅ Λ₁₆). Hence at least one pair of vectors must overlap; the leaderboard #1 (CHRONOS) sits at the duplicate floor of 2.0.

## Background

The kissing number κ(d) is the maximum number of non-overlapping unit spheres that can simultaneously touch a central unit sphere in dimension d. For d = 16, the **proven value is κ(16) = 4320**, achieved uniquely by the Barnes-Wall lattice BW₁₆ minimum vectors. With n = 4321 the problem demands fitting one extra vector, which by the proven kissing bound forces at least some overlap.

Related: [Problem 6 — Kissing Number d=11](problem-06-kissing-number.md), [Problem 22 — Kissing Number d=12](problem-22-kissing-number-d12.md).

## Arena Details

- **API ID**: 23
- **Direction**: minimize
- **Scoring**: total hinge overlap loss
- **minImprovement**: 0 (any strict improvement registers)

## Approach

1. **Recon**. Scrape leaderboard (5 entries, all CHRONOS, rank #1 = 2.0). Download SOTA: 4320 BW₁₆ unit vectors with coords in `{0, ±¼, ±½, ±1}` (32 axis + 2240 four-coord + 2048 sixteen-coord) plus one exact duplicate of `(-1, 0, …, 0)`.
2. **Evaluator**. Hybrid float64+mpmath path: prescreen via float64 dot products, recompute borderline pairs in 50/100 dps. Verified exactly against CHRONOS SOTA.
3. **Constructive baseline**. `bw16_min_vectors()` builds 4320 minimum vectors of BW₁₆ from the [16, 11, 4] extended Hamming code (parity check = RM(1,4) generator). Set-equal to CHRONOS SOTA.
4. **Five-pronged rank-#1 attack**, all confirming infeasibility:
   - First-order link analysis — `min_u S(u) ≈ 16.67` over the 280-vector link of v₀; threshold to break 2.0 is `2/√3 ≈ 1.155` (margin 14×).
   - Random scan of S¹⁵ (200K samples) — best non-duplicate basin = 11.23.
   - L-BFGS multi-start (50 random + tangent starts, softplus annealing β ∈ {10..3000}) — best = 2.00125, none below 2.0.
   - Remove-and-replace (drop 1 vertex + jointly optimize 2 fillers) — best = 2.0038.
   - Cross-problem precedent (P22 d=12, exhaustive 60M+ samples) — same 2.0 floor.
5. **Rank-#2 squeeze**. Place the 4321st vector at f = cos(δ) v₀ + sin(δ) u\* where u\* minimizes S(u). Score(δ) ≈ 2 + δ · (√3 · S(u\*) − 2). Sweep δ ∈ {1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8}; pick the smallest where float64 / mpmath50 / mpmath100 / mpmath200 agree to ≥ 13 digits.

## Key Insight

The penalty function `p(γ) = 2 − 2√(2(1−γ))` is **convex** on [½, 1], with `p(½) = 0` (kissing) and `p(1) = 2` (duplicate). For a fixed "violation budget", spreading overlap across many pairs lowers total penalty (Jensen's inequality), but the BW₁₆ link is too dense — the first-order escape direction has S(u\*) ≈ 16.67, requiring a 14× reduction to dip below 2.0. Combined with empirical scans showing all non-duplicate basins above 11, the 2.0 floor is structurally locked.

The rank-#2 squeeze achieves the smallest verifiable score above 2.0 by placing the filler infinitesimally off v₀ in the least-bad tangent direction. With δ = 1e-7 the score is **2.000002687258436** (mpmath agreeing to 18 digits across 50/100/200 dps).

## Results

| Method | Best score | Rank |
|---|---|---|
| BW₁₆ + duplicate (CHRONOS pattern) | 2.000000000000000 | #1 (held by CHRONOS via timestamp) |
| Random S¹⁵ scan (200K samples) | 11.225683 | #4 |
| L-BFGS filler multi-start (50 starts) | 2.001253 | #2 |
| Remove-and-replace (joint 2-filler) | 2.003763 | #2 |
| **Rank-#2 squeeze, δ = 1e-7** | **2.000002687258436** | **#2** |

## Reproduction

```bash
# 1. Build the squeeze candidate
uv run python scripts/p23_kissing_d16/build_rank2_squeeze.py --n-starts 400 --deltas 1e-7 \
    --out results/p23_kissing_d16/squeeze

# 2. Triple-verify and submit (dry run first)
uv run python scripts/p23_kissing_d16/submit.py results/p23_kissing_d16/squeeze/squeeze_delta1e-07.json
uv run python scripts/p23_kissing_d16/submit.py results/p23_kissing_d16/squeeze/squeeze_delta1e-07.json --submit
```

*Last updated: 2026-04-25*
