# Problem: spread 14 points in the unit square (Heilbronn triangle)

Place 14 points in the unit square `[0,1] x [0,1]`.

**Objective**
- Maximize the **minimum triangle area** over all triples of the 14 points.
- For a configuration, the score is `min` over every triple `(i, j, k)` of the
  area of triangle `(p_i, p_j, p_k)`. Larger is better.

**Constraints**
- All 14 points lie inside the unit square.

**Decision variables**: the 14 point coordinates `(x_i, y_i) in [0,1]^2`.

You start from a random configuration (no warm start, no known/optimal layout).
The objective is **non-smooth** — a minimum over many `C(14,3)` triangle areas —
so plain gradient descent stalls; improve it with general-purpose optimization
you write yourself (e.g. simulated annealing, basin-hopping, multistart, pattern
search).
