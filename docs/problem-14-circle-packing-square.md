# Problem 14 — Circle Packing in a Square (n = 26)

Pack 26 disjoint circles into the unit square, maximizing the sum of radii.

This is the n = 26 instance of the classical circle-packing-in-a-square
family catalogued for decades on Erich Friedman's *Packing Center* and in
Packomania. The published AlphaEvolve construction is the natural starting
point — see Novikov et al., *AlphaEvolve: A coding agent for scientific
and algorithmic discovery*, notebook §B.36.

## Approach

- **Evaluator**: arena-matching verifier in `src/einstein/circle_packing_square/`
  enforces that every circle lies inside `[0, 1]^2` and that all
  `C(26, 2) = 325` pairwise distances satisfy `‖c_i − c_j‖ ≥ r_i + r_j`.
  A strict tolerance-zero mode is provided for submission gating; a
  verbose variant exposes contact graph and worst-overlap diagnostics.
- **Warm-start**: download the top leaderboard solutions via
  `GET /api/solutions/best?problem_id=14` and reuse the best
  full-precision construction as the optimization seed.
- **SLSQP polish**: `polish()` runs SLSQP on the joint variables
  `(cx_i, cy_i, r_i)` with 104 wall constraints and 325 pair disjointness
  constraints, using a loose-to-tight slack cascade to settle onto the
  basin floor without drifting outside the strict feasible region.
- **Multistart / topology search**: additional scripts explore
  random greedy starts, perturbative kicks, topological contact swaps,
  and ring-rotated golden-angle initialisations to scan for an alternate
  basin above the published ceiling.

## High-level results

All top-rank constructions polish to a common dominant basin within
float64 precision. JSAgent's submission lands in the rank-2 window while
staying strictly below the leaderboard #1, with all disjointness and wall
constraints verified at the strict (tolerance-zero) evaluator.

Detailed methodology is tracked in the private memory bank.

## Infrastructure

- `src/einstein/circle_packing_square/evaluator.py` — strict arena
  verifier and diagnostic helpers (`evaluate`, `evaluate_strict`,
  `evaluate_verbose`).
- `src/einstein/circle_packing_square/polish.py` — SLSQP polisher over
  joint circle variables with tolerance-cascade support.
- `src/einstein/circle_packing_square/active_set.py` — active-set
  identification helpers used by the polisher.
- `scripts/circle_packing_square/multistart.py` — multistart SLSQP
  search over random and perturbative starts.
- `scripts/circle_packing_square/submit.py` — pre-flight checklist and
  arena submission with leaderboard polling.
- `tests/circle_packing_square/test_evaluator.py` — evaluator regression
  tests including a strict tolerance-zero validity test on the committed
  solution.

## References

- Novikov et al., *AlphaEvolve: A coding agent for scientific and
  algorithmic discovery*, [arXiv:2506.13131](https://arxiv.org/abs/2506.13131),
  §B.36; data in
  [google-deepmind/alphaevolve_results](https://github.com/google-deepmind/alphaevolve_results).
- Erich Friedman, *Packing Center* — circles in a square records,
  <https://erich-friedman.github.io/packing/cirinsqu/>.
- Packomania, *Packings of n congruent and non-congruent circles in a
  unit square*, <http://www.packomania.com/>.

*Last updated: 2026-04-09*
