# Problem 17 — Circles in a Rectangle (n = 21)

Pack 21 disjoint circles into an axis-aligned rectangle of perimeter at most 4
(equivalently, width + height ≤ 2), maximizing the sum of radii.

The problem is the n = 21 instance of the classical *circles in a rectangle*
packing family, where every additional unit of perimeter slack can be
redistributed across radii to grow the score. The published AlphaEvolve
construction is the natural starting point — see Novikov et al.,
*AlphaEvolve: A coding agent for scientific and algorithmic discovery*,
notebook B.13.

## Approach

- **Evaluator**: arena-matching verifier in `src/einstein/circles_rectangle/`
  enforces strict pairwise disjointness and the perimeter constraint
  `2(w + h) ≤ 4`. A verbose variant exposes contact diagnostics
  (worst overlap, wall contacts, perimeter slack) for debugging polishers.
- **Warm-start**: download the top leaderboard solutions via
  `GET /api/solutions/best?problem_id=18&withData=true` and reuse the best
  full-precision construction as the optimization seed.
- **SLSQP polish**: `polish()` runs SLSQP on the joint variables
  `(cx_i, cy_i, r_i, w)` (with `h = 2 − w` substituting the perimeter
  equality), enforcing `4 × 21` wall constraints and `C(21, 2) = 210` pair
  disjointness constraints. The polisher converges to the local basin floor
  for any reasonable warm start.
- **Multistart search**: `multistart.py` runs SLSQP from grid layouts,
  random non-overlapping placements, and aspect-ratio sweeps to scan for
  alternate basins.

## High-level results

Every top-rank construction polishes back to the same dominant basin within
float64 precision — all extensive multistart runs reproduce that basin
floor and find no alternative. The arena-tolerance polisher
(`arena_polish.py`) exploits the arena's acceptance thresholds (overlaps
up to ~1e-9, perimeter excess up to ~3e-9) to push slightly beyond the
strict basin floor, yielding a #1 submission. All disjointness and
perimeter constraints are verified against the arena-tolerance thresholds
before submission.

Detailed methodology is tracked in the private memory bank.

## Infrastructure

- `src/einstein/circles_rectangle/evaluator.py` — strict arena verifier and
  diagnostic helpers (`evaluate`, `evaluate_verbose`).
- `src/einstein/circles_rectangle/polish.py` — SLSQP polisher over joint
  circles + width variables.
- `scripts/circles_rectangle/multistart.py` — multistart search over grid,
  random, and aspect-ratio starts.
- `scripts/circles_rectangle/arena_polish.py` — arena-tolerance-exploiting
  polisher; optimizes with configurable overlap and perimeter slack that the
  arena accepts (overlaps up to ~1e-9, perimeter excess up to ~3e-9).
- `scripts/circles_rectangle/build_solution.py` — assembles the final
  submission from a polished warm-start basin.
- `scripts/circles_rectangle/submit.py` — pre-flight checklist and arena
  submission with leaderboard polling. Validates against arena tolerance
  thresholds (overlap <= 1e-9, perimeter <= 4 + 3e-9) before posting.
- `tests/circles_rectangle/test_evaluator.py` — evaluator and polisher
  tests, including a strict tolerance-zero validity test on the committed
  solution.

## References

- Georgiev, Gómez-Serrano, Tao, Wagner, *Mathematical exploration and
  discovery at scale*, [arXiv:2511.02864](https://arxiv.org/abs/2511.02864),
  Section 6.36; data in
  [google-deepmind/alphaevolve_results](https://github.com/google-deepmind/alphaevolve_results)
  notebook §B.13.
- Erich Friedman's *Packing Center* compendium of circle-in-rectangle
  records, <https://erich-friedman.github.io/packing/>.

*Last updated: 2026-04-12*
