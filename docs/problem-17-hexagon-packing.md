# Problem 17: Hexagon Packing in a Hexagon (n = 12)

**Status**: JSAgent #2

## Problem

Pack 12 disjoint unit regular hexagons (side length 1) inside a larger regular hexagon, minimizing the outer hexagon's side length. Each inner hexagon may be freely rotated.

## Background

Packing regular polygons inside a container is a classical computational geometry problem. For hexagons in hexagons, the 6-fold symmetry allows rich contact structures. The optimal packing for n = 12 is expected to have many nearly-touching pairs forming a rigid "frozen" contact graph.

## Arena Details

- **API ID**: 17
- **Direction**: minimize
- **Solution format**: `{"hexagons": [[cx, cy, angle_deg] × 12], "outer_side_length": float, "outer_center": [x, y], "outer_angle_deg": float}`
- **Scoring**: `outer_side_length + penalty × violations` (overlap + containment)
- **minImprovement**: 0.0001

## Approach

### Strategy Overview

All top-10 agents converge to the same basin. The problem is a warm-start → polish pipeline with no novel technique required beyond standard continuous optimization.

### Warm-Start + Polish

1. Download top solutions via `/api/solutions/best?problem_id=17`
2. Continuous optimization on 12 × (x, y, angle) + outer container parameters
3. SLSQP-style constrained optimization with overlap and containment penalties

### What Worked

- **Warm-start from API** — immediate access to the SOTA basin
- **Standard constrained optimization** — converges to the shared basin floor

### What Didn't Work

- **Finding a different basin** — all top-10 agents share the same configuration
- **Symmetry exploitation** — 6-fold symmetry doesn't help escape the single basin

## Key Insights

- **Single-basin convergence**: When all top-10 agents share the same solution structure, the problem is effectively solved at the float64 level.
- **Not every problem needs novel techniques**: For some problems, warm-start + standard polish is sufficient. Recognize this early and allocate effort elsewhere.

## References

- Packing problems survey — combinatorial and computational geometry literature
- Separating Axis Theorem — standard convex polygon overlap detection

## Infrastructure

- `src/einstein/hexagon/evaluator.py` — arena-matching evaluator (SAT-based overlap detection)
- `scripts/hexagon/` — optimization scripts
- `tests/hexagon/` — evaluator parity tests

*Last updated: 2026-04-13*
