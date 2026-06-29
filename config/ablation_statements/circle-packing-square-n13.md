# Problem: pack 13 equal circles in the unit square

Place 13 circles of a common radius r inside the unit square `[0,1] x [0,1]`.

**Constraints**
- Every circle lies fully inside the square: for each center `(cx_i, cy_i)`,
  `r <= cx_i <= 1 - r` and `r <= cy_i <= 1 - r`.
- Circles do not overlap: `|| c_i - c_j || >= 2r` for all `i < j`.

**Objective**
- Maximize the common radius `r` (equivalently, choose the 13 centers so the
  achievable radius is as large as possible).
- For a given configuration of centers, the achievable radius is
  `r = min( 0.5 * min_{i<j} || c_i - c_j ||,  min_i min(cx_i, 1-cx_i, cy_i, 1-cy_i) )`.

**Decision variables**: the 13 center coordinates `(cx_i, cy_i) in [0,1]^2`.

You start from a random configuration (no warm start, no known/leaderboard
configuration). Improve the radius using general-purpose optimization.
