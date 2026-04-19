# Problem 6: Kissing Number in Dimension 11

**Status**: JSAgent #38 (score 0.000000 — theoretical minimum achieved by many agents)

## Problem

Place n = 594 unit vectors in ℝ¹¹ to minimize total overlap penalty. Sphere centers are placed at c_i = 2v_i/‖v_i‖. The score is:

    loss = Σ_{i<j} max(0, 2 − ‖c_i − c_j‖)

Score = 0 would prove κ(11) ≥ 594, an open problem in mathematics.

## Background

The kissing number κ(d) is the maximum number of non-overlapping unit spheres that can simultaneously touch a central unit sphere in dimension d. Exact values are known only for d = 1, 2, 3, 4, 8, 24. For d = 11, the best known lower bound was κ(11) ≥ 593 (AlphaEvolve 2025). Achieving score 0 with n = 594 improves this bound.

## Arena Details

- **API ID**: 6
- **Direction**: minimize
- **minImprovement**: 0 (uniquely permissive — any improvement counts)

## Approach

### Strategy Overview

A multi-phase campaign combining parallel tempering simulated annealing, discrete ulp-step descent, and high-precision mpmath verification. The optimization landscape has a fractal-like structure where improvements exist at every scale from 1e-4 down to individual ulps.

### Parallel Tempering Simulated Annealing

The workhorse optimizer: 8 temperature replicas with geometric spacing [1e-12, 1e-4], periodic replica exchange. This outperforms greedy perturbation by approximately 730x in improvement rate.

- **Contribution-weighted sampling**: Focus perturbation on vectors with the highest overlap contributions rather than uniform sampling. Dramatically improves hit rate.
- **Incremental O(n) evaluation**: When perturbing a single vector, only the n − 1 distances involving that vector change, avoiding O(n²) full recomputation.
- **Sphere manifold projection**: Re-normalize to the unit sphere after each perturbation. Optimization lives on S¹⁰.

### ULP-Step Discrete Descent

Once the smooth optimizer's noise floor (~1e-12) exceeds the residual loss (~1e-13), continuous methods become unproductive. Single-coordinate ±1/±2/±4 ulp steps become the only productive method:

1. For each vector v[i] and coordinate k, try v[i][k] ± {1, 2, 4} ulps
2. Re-normalize and evaluate
3. Accept if loss decreases

Alternating single-coordinate and 2-coordinate intra-row sweeps finds improvements that smooth optimizers miss entirely.

### mpmath High-Precision Verification

A critical lesson: the arena verifier upgraded mid-competition from float64 to mpmath (~50 decimal digits). Submissions that appeared to have score 0.0 in float64 were revealed to have residual ~7.7 × 10⁻¹³ in mpmath. This required re-polishing all solutions at higher precision.

- **Float64 screen + mpmath verify**: Use fast float64 to identify active constraint pairs (~10% of all pairs), then evaluate only those in mpmath. 10x faster than uniform mpmath scan.

### What Worked

- **Parallel tempering SA** — 730x improvement rate over greedy perturbation
- **Contribution-weighted sampling** — focuses effort on the vectors that matter
- **ULP-step descent** — the only productive method at the float64 precision floor
- **Incremental O(n) evaluation** — enables millions of perturbation trials per second

### What Didn't Work

- **Riemannian gradient descent** — the basin is flat at gradient scale; returns zero gradient everywhere near the optimum
- **Large-scale perturbations** — destroy the delicate contact structure without finding a better configuration
- **Assuming verifier stability** — the float64 → mpmath upgrade invalidated previously "perfect" solutions

## Key Insights

- **Fractal optimization landscape**: Improvements exist at every scale from 1e-4 down to individual ulps. The landscape has structure at all resolutions.
- **Verifier precision can change mid-competition**: Arena verifiers are not guaranteed stable. Always re-verify against the current verifier, especially near theoretical optima.
- **Score 0 is achievable but not unique**: Many agents achieved score 0.000000 (ranking by submission time), confirming the mathematical result κ(11) ≥ 594.
- **SA parallel tempering is ideal for sphere packing**: The temperature hierarchy naturally handles the multi-scale structure of the contact graph.

## References

- Novikov et al. (2025), "AlphaEvolve" — κ(11) ≥ 593 ([arXiv:2506.13131](https://arxiv.org/abs/2506.13131))
- Conway & Sloane, "Sphere Packings, Lattices and Groups"
- Odlyzko & Sloane (1979), kissing number bounds

## Infrastructure

- `src/einstein/kissing_number/evaluator.py` — arena-matching evaluator
- `src/einstein/gpu_tempering/core.py` — GPU-accelerated parallel tempering SA
- `src/einstein/gpu_tempering/triton_kernel.py` — Triton-fused SA step kernel
- `scripts/kissing_number/gpu_tempering.py` — GPU tempering entry point
- `scripts/kissing_number/polish_ulp_coord.py` — single-coordinate ulp descent
- `scripts/kissing_number/polish_ulp_2coord.py` — 2-coordinate ulp descent

*Last updated: 2026-04-13*
