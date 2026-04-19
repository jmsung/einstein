# Problem 18: Uncertainty Principle

**Status**: JSAgent **#1**

## Problem

Minimize S = largest_sign_change / (2π) of a Laguerre polynomial combination.

Given a set of "double roots" z₁, ..., zₖ (positive reals ≤ 300), construct a specific Laguerre polynomial combination g(x) with α = −1/2 and find its largest sign-changing root. Lower S is better.

## Arena Details

- **API ID**: 9
- **Direction**: minimize
- **Solution format**: `{"laguerre_double_roots": [z1, z2, ..., zk]}`
- **Scoring**: largest sign change / (2π)

## Approach

### Strategy Overview

The breakthrough came from **k-climbing** (adding degrees of freedom when stuck) combined with a **two-tier verification** system that catches the deceptive landscape. A **gap-space parameterization** of the ordered roots improves optimizer conditioning.

### Two-Tier Verification (Critical)

The landscape is extremely deceptive — optimizers routinely report fake improvements that don't survive exact verification.

- **Fast evaluator** (mpmath + numpy): Drives the optimization loop at high speed. Sufficient for screening candidates.
- **Exact symbolic verifier** (sympy): Quality gate before any score is trusted. Catches numerical artifacts, especially far-field sign changes.
- **Hybrid evaluator** (sympy polynomial construction + numpy root-finding): 8x faster than full sympy while maintaining exact polynomial coefficients. The key speedup is using sympy only for the polynomial construction (where precision matters) and numpy for root-finding.

**Never collapse the tiers**: exact-only cripples search speed; fast-only lets false positives through.

### k-Climbing (Adding Dimensions When Stuck)

When optimization at k double roots plateaus, try k+1:
- **k = 13 → 14**: Gave a significant improvement (above the minImprovement gate). The extra degree of freedom opened a new region of the solution landscape.
- **k = 14 → 15**: Gave ~4.57 × 10⁻⁶ improvement — 40x below the minImprovement gate. Diminishing returns hit hard.

**Gate-feasibility ratio**: Track (improvement from k→k+1) / minImprovement. When this ratio drops below ~0.1, further k-climbing is unproductive. The ratio collapsed from 1.8 (k=13→14) to 0.046 (k=14→15).

### Gap-Space Parameterization

For ordered roots z₁ < z₂ < ... < zₖ, optimize the gaps g_i = z_{i+1} − z_i instead of absolute positions. This:
- Enforces ordering without explicit constraints
- Reduces condition number
- Lets optimizers explore relative structure (spacing) rather than absolute positions

CMA-ES and Nelder-Mead in gap-space with smooth penalty terms handle the soft constraints naturally.

### Far-Field Sign Change Detection

Hidden sign changes far from the root cluster (x >> 300) can invalidate apparently good solutions. The exact verifier scans well beyond the dense grid to catch these. This is where the fast evaluator most commonly produces false positives.

### What Worked

- **k-climbing** (k = 13 → 14) — opened a new region with significant improvement
- **Two-tier verification** — catches deceptive landscape; prevents phantom scores
- **Gap-space CMA-ES** — good conditioning for ordered-root optimization
- **Hybrid verifier** — 8x faster than full sympy, enabling more iterations

### What Didn't Work

- **k = 15 climbing** — improvement below minImprovement gate (diminishing returns)
- **Trusting the fast evaluator alone** — false positives from far-field sign changes
- **Direct position optimization** — poor conditioning for ordered variables; gap-space is much better

## Key Insights

- **k-climbing has diminishing returns**: Each additional degree of freedom gives less improvement. Track the gate-feasibility ratio and pivot when it drops below 0.1.
- **Deceptive landscapes demand exact verification**: When the fast evaluator reports improvement, don't trust it until the exact verifier confirms. Far-field sign changes are the most common source of false positives.
- **Gap-space is a general technique for ordered variables**: For any optimization over ordered real variables (roots, breakpoints, knots), optimizing gaps instead of positions improves conditioning and enforces ordering for free.
- **Laguerre polynomial conditioning**: At k = 15, the condition number of the polynomial evaluation reaches ~10³⁸, requiring mpmath dps ≥ 40. Rule of thumb: dps ≥ log₁₀(condition_number) + safety buffer.

## References

- Problem 9 in the arena (API ID 9)
- Laguerre polynomial combination with α = −1/2
- arXiv:2511.02864 — Mathematical exploration and discovery at scale

## Infrastructure

- `src/einstein/uncertainty/verifier.py` — exact symbolic verifier (sympy)
- `src/einstein/uncertainty/fast.py` — fast numerical evaluator (mpmath + numpy)
- `src/einstein/uncertainty/hybrid.py` — hybrid evaluator (sympy polynomial + numpy root-finding)
- `scripts/uncertainty/optimize_loop.py` — adaptive optimization loop
- `scripts/uncertainty/exact_hillclimb.py` — exact hill-climbing optimizer
- `scripts/uncertainty/k_climb_optimizer.py` — k-climb optimizer (add dimensions when stuck)
- `scripts/uncertainty/k14_polish.py` — hybrid-verified hillclimb on k = 14 solutions
- `scripts/uncertainty/k15_climb.py` — k = 15 parallel multi-start climb
- `scripts/uncertainty/k15_parallel_cma.py` — k = 15 parallel CMA-ES with smooth penalty
- `scripts/uncertainty/submit.py` — arena submission script

*Last updated: 2026-04-13*
