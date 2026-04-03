# Problem 17: Hexagon Packing in a Hexagon (n = 12)

## Problem

Pack 12 disjoint unit regular hexagons (side length 1) inside a larger regular hexagon, minimizing the outer hexagon's side length. Each inner hexagon may be freely rotated.

## Background

Packing regular polygons inside a container is a classical computational geometry problem. For hexagons in hexagons, the 6-fold symmetry allows rich contact structures. The optimal packing for n=12 unit hexagons is expected to have many nearly-touching pairs forming a rigid "frozen" contact graph.

## Key References

- Packing problems survey — combinatorial and computational geometry literature
- Separating Axis Theorem — standard convex polygon overlap detection

## Arena Details

- **API ID**: 17
- **Direction**: minimize
- **Solution format**: `{"hexagons": [[cx, cy, angle_deg] × 12], "outer_side_length": float, "outer_center": [x, y], "outer_angle_deg": float}`
- **Scoring**: `outer_side_length + penalty × violations` (overlap + containment)
- **minImprovement**: 0.0001

## Approach

Continuous optimization on 12 × (x, y, angle) + outer container parameters. Warm-start from SOTA solutions available via API.

*Last updated: 2026-04-02*
