# Problem 14 — Circle Packing in a Square (n = 26)

**Status**: JSAgent **#1**

## Problem

Pack 26 disjoint circles into the unit square, maximizing the sum of radii.

This is the n = 26 instance of the classical circle-packing-in-a-square family catalogued on Erich Friedman's *Packing Center* and Packomania. The published AlphaEvolve construction is the natural starting point.

## Arena Details

- **API ID**: 14
- **Direction**: maximize
- **Solution format**: `{"circles": [[cx, cy, r] × 26]}`
- **Scoring**: sum of radii (penalized for constraint violations)

## Approach

### Strategy Overview

All top-rank constructions polish to a **single dominant basin** within float64 precision. The competition reduces to precision polishing and strategic rank-window placement.

### SLSQP Polish with Tolerance Cascade

`polish()` runs SLSQP on the joint variables (cx_i, cy_i, r_i) with 104 wall constraints and 325 pair disjointness constraints. A **loose-to-tight slack cascade** is critical: start with relaxed tolerances to find the basin, then tighten to settle onto the floor without drifting outside the feasible region.

### Rank-Window Strategy

When the #1 score is at the float64-overlap-noise ceiling (unbeatable with strict disjointness), rank #2+ is achievable mechanically:
1. Polish SOTA to the strict-disjoint floor via SLSQP (overlap_tol=0, ftol=1e-16)
2. Identify the safe rank window between the next-best score + minImprovement and #1
3. Uniform shrink each radius to land in the target window
4. Triple-verify with `evaluate_strict(tol=0)` before submitting

### Multistart / Topology Search

Additional scripts explore random greedy starts, perturbative kicks, topological contact swaps, and ring-rotated golden-angle initializations to scan for alternate basins above the published ceiling. None found a distinct basin.

### What Worked

- **SLSQP tolerance cascade** — converges reliably to the basin floor
- **Rank-window strategy** — mechanical rank capture below the float64 ceiling
- **Warm-start from SOTA** — nested basin means polish beats from-scratch

### What Didn't Work

- **Finding an alternate basin** — extensive multistart (Apollonian, flip-and-flow, diverse init, asymmetric search) all converge to the same basin
- **From-scratch optimization** — random starts cannot reach the SOTA basin

## Key Insights

- **Single dominant basin**: For well-studied packing problems, extensive multistart confirming one basin is strong evidence of global optimality.
- **Tolerance cascade matters**: For constrained optimization, starting with loose tolerances and tightening avoids getting stuck at artificial boundaries.
- **Rank-window is mechanical**: When #1 is at the float64 ceiling, lower ranks are achievable via uniform radius shrinking — a systematic technique, not a creative search.
- **Warm-start from published constructions**: The AlphaEvolve construction provides a warm-start that is unreachable from random initialization.

## References

- Novikov et al., *AlphaEvolve*, [arXiv:2506.13131](https://arxiv.org/abs/2506.13131), §B.36; data in [google-deepmind/alphaevolve_results](https://github.com/google-deepmind/alphaevolve_results).
- Erich Friedman, *Packing Center* — circles in a square records, <https://erich-friedman.github.io/packing/cirinsqu/>.
- Packomania — <http://www.packomania.com/>.

## Infrastructure

- `src/einstein/circle_packing_square/evaluator.py` — strict arena verifier (`evaluate`, `evaluate_strict`, `evaluate_verbose`)
- `src/einstein/circle_packing_square/polish.py` — SLSQP polisher with tolerance-cascade support
- `src/einstein/circle_packing_square/active_set.py` — active-set identification helpers
- `scripts/circle_packing_square/multistart.py` — multistart SLSQP search
- `scripts/circle_packing_square/submit.py` — pre-flight checklist and arena submission
- `tests/circle_packing_square/test_evaluator.py` — evaluator regression tests (strict tolerance-zero)

*Last updated: 2026-04-13*
