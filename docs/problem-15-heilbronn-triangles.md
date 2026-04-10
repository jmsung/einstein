# Problem 15 — Heilbronn Triangles (n = 11)

Place 11 points in a unit-area equilateral triangle

    A = (0, 0),  B = (1, 0),  C = (1/2, √3/2)

to maximize the normalized minimum triangle area

    score = min_{i < j < k} area(p_i, p_j, p_k) / (√3 / 4).

This repository contains the arena-matching evaluator, a high-precision mpmath
polish utility, and several multistart / basin-hopping search baselines for
the Heilbronn triangle problem at n = 11.

## Results

- **Arena SOTA (2026-04-08)**: 0.036529889880030156 — held by four agents
  (CHRONOS, AlphaEvolve, Euclid, EinsteinAgent6391) with bit-identical (or
  1-ulp-equivalent) configurations.
- **JSAgent status**: did not submit. Our parity tests reproduce the arena
  SOTA bit-exactly; a 60-digit mpmath polish of the basin confirms the true-
  math ceiling is only +6.25 × 10⁻¹⁷ above the claimed float64 score, well
  below the problem's 1 × 10⁻⁸ submission gate. Across ~18 800 multistart,
  CMA-ES, and basin-hopping trials (12 init strategies + 8 hop types) we did
  not find a distinct basin that matched, let alone exceeded, the leaderboard
  top.

The current best construction is the one published in the AlphaEvolve
results repository (`alphaevolve_results/mathematical_results.ipynb`,
section B.9, cell 100) and in §6.48 of
Georgiev–Gómez-Serrano–Tao–Wagner, *Mathematical exploration and discovery at
scale* (arXiv:2511.02864). That construction has D1 reflection symmetry about
the median through the vertex (1, 0), six boundary-edge incidences (two per
side, no corners), and seventeen minimum-area triangles tied to floating-point
equality — consistent with a rigid KKT local maximum.

## Layout

- `src/einstein/heilbronn_triangles/evaluator.py` — arena-matching evaluator.
  Strict containment tolerance is empirically 1 × 10⁻¹¹; verified against the
  top-15 downloaded solutions.
- `scripts/heilbronn_triangles/mpmath_polish.py` — 60-digit Newton polish on
  the reduced active-triple system. Used to confirm the basin's floating-point
  ceiling.
- `scripts/heilbronn_triangles/multistart_search.py` — 12 init strategies,
  direct SLSQP polish on the full 165-triple epigraph.
- `scripts/heilbronn_triangles/cma_search.py` — CMA-ES on a softmin surrogate
  followed by SLSQP polish.
- `scripts/heilbronn_triangles/basin_hop.py` — basin hopping from the
  AlphaEvolve construction using eight perturbation / teleport / swap moves.
- `tests/heilbronn_triangles/test_parity.py` — parity tests against the
  downloaded leaderboard solutions.

## Reproducing the SOTA

```bash
# Download the public leaderboard
uv run python -c "
import json, urllib.request
data = json.loads(urllib.request.urlopen(
    'https://einsteinarena.com/api/solutions/best?problem_id=15&limit=5'
).read())
print(json.dumps(data[0]['data'], indent=2))
"

# Verify parity (all 15 downloaded solutions reproduce to bit)
uv run python -m pytest tests/heilbronn_triangles/ -v

# Confirm the float64 ceiling via mpmath Newton
uv run python scripts/heilbronn_triangles/mpmath_polish.py
```

## References

- Georgiev, Gómez-Serrano, Tao, Wagner. *Mathematical exploration and discovery
  at scale.* arXiv:2511.02864 (2025). §6.48, Figure 26, construction B.9.
- Goldberg, M. *Maximizing the smallest triangle made by N points in a square.*
  Math. Mag. 45 (1972), 135–144. (Unit-square variant; not directly applicable
  to the equilateral-triangle arena problem.)
- Comellas, F., Yebra, J. L. A. *New lower bounds for Heilbronn numbers.*
  Electron. J. Combin. 9 (2002), R6. (Unit square, n ≤ 12.)
- Friedman, E. *Heilbronn in triangles.*
  https://erich-friedman.github.io/packing/heiltri/ (Cantrell 2006 n = 11
  construction, pre-AlphaEvolve record.)
- Cohen, A., Pohoata, C., Zakharov, D. *A new upper bound for the Heilbronn
  triangle problem.* arXiv:2305.18253 (2023).

*Last updated: 2026-04-09*
