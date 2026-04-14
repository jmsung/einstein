# Problem 15 — Heilbronn Triangles (n = 11)

**Status**: No submission (basin is frozen — float64 ceiling confirmed)

## Problem

Place 11 points in a unit-area equilateral triangle

    A = (0, 0),  B = (1, 0),  C = (1/2, √3/2)

to maximize the normalized minimum triangle area

    score = min_{i < j < k} area(p_i, p_j, p_k) / (√3 / 4).

## Background

The Heilbronn triangle problem asks for point configurations that maximize the minimum area of any triangle formed by three of the points. For n = 11 in an equilateral triangle, the SOTA is held by four agents with bit-identical configurations matching the AlphaEvolve published construction.

## Arena Details

- **API ID**: 15
- **Direction**: maximize
- **Solution format**: `{"points": [[x, y] × 11]}`
- **Scoring**: normalized minimum triangle area
- **minImprovement**: 1e-8

## Results

- **Arena SOTA**: 0.036529889880030156 — held by four agents (CHRONOS, AlphaEvolve, Euclid, EinsteinAgent6391) with bit-identical configurations.
- **JSAgent status**: did not submit. Our parity tests reproduce the arena SOTA bit-exactly. A 60-digit mpmath polish confirms the true-math ceiling is only +6.25 × 10⁻¹⁷ above the float64 score — well below the 1 × 10⁻⁸ submission gate.

## Approach

### Entry Gate Analysis (3-Check Test)

Before investing compute, we apply a systematic entry gate:

1. **Tie-multiplicity check**: 4 agents are bit-tied at the top score. Matching SOTA yields zero points (ties resolved by submission time).
2. **Paper-copy detection**: Hash SOTA against AlphaEvolve published construction — bit-identical match confirms this is the published result, already polished by the authors.
3. **mpmath-ceiling check**: 60-digit mpmath Newton polish on the reduced KKT system confirms the true-math gap is +6.25 × 10⁻¹⁷ — orders of magnitude below the 1 × 10⁻⁸ gate.

All three checks indicate this problem is frozen. No optimization can reach a submittable improvement.

### Exhaustive Basin Search

Despite the entry gate, we ran an exhaustive search to characterize the landscape:
- ~18,800 multistart, CMA-ES, and basin-hopping trials
- 12 initialization strategies + 8 hop types
- No distinct basin matching or exceeding the leaderboard top was found

### Structural Analysis

The SOTA construction has:
- **D1 reflection symmetry** about the median through vertex (1, 0)
- **Six boundary-edge incidences** (two per side, no corners)
- **17 minimum-area triangles** tied to floating-point equality — consistent with a rigid KKT local maximum
- **Over-determined KKT**: 17 active constraints > 8 DOF (22 coords − 4 gauge − 10 boundary), confirming full rigidity

### What Worked

- **Entry gate analysis** — correctly identified this as frozen before wasting compute
- **Parity tests** — reproduce arena SOTA bit-exactly, validating our evaluator
- **mpmath Newton polish** — confirms the float64 ceiling quantitatively

### What Didn't Work

- **18,800 multistart trials** — zero new basins found (confirms single-basin)
- **Basin-hopping with 8 move types** — perturbation, teleport, swap all fail to escape

## Key Insights

- **Entry gate saves time**: The 3-check test (tie-multiplicity, paper-copy, mpmath-ceiling) correctly identifies frozen problems before expensive optimization. Apply this to every problem.
- **Over-determined KKT = rigid**: When active constraints exceed degrees of freedom, the basin is mathematically rigid. No local or global search can improve the score within that basin.
- **17 active triangles = deep freeze**: The equioscillation of 17 near-minimal triangles creates a stress network that absorbs any perturbation.
- **mpmath quantifies the ceiling**: High-precision arithmetic gives an exact answer to "how much room is there?" rather than hoping for improvement.

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

# Verify parity
uv run python -m pytest tests/heilbronn_triangles/ -v

# Confirm the float64 ceiling via mpmath Newton
uv run python scripts/heilbronn_triangles/mpmath_polish.py
```

## References

- Georgiev, Gómez-Serrano, Tao, Wagner. *Mathematical exploration and discovery at scale.* arXiv:2511.02864 (2025). §6.48, construction B.9.
- Goldberg, M. *Maximizing the smallest triangle made by N points in a square.* Math. Mag. 45 (1972), 135–144.
- Comellas, F., Yebra, J. L. A. *New lower bounds for Heilbronn numbers.* Electron. J. Combin. 9 (2002), R6.
- Friedman, E. *Heilbronn in triangles.* https://erich-friedman.github.io/packing/heiltri/
- Cohen, A., Pohoata, C., Zakharov, D. *A new upper bound for the Heilbronn triangle problem.* arXiv:2305.18253 (2023).

## Infrastructure

- `src/einstein/heilbronn_triangles/evaluator.py` — arena-matching evaluator (strict containment tolerance 1 × 10⁻¹¹)
- `scripts/heilbronn_triangles/mpmath_polish.py` — 60-digit Newton polish on reduced active-triple system
- `scripts/heilbronn_triangles/multistart_search.py` — 12 init strategies, SLSQP on 165-triple epigraph
- `scripts/heilbronn_triangles/cma_search.py` — CMA-ES on softmin surrogate + SLSQP polish
- `scripts/heilbronn_triangles/basin_hop.py` — basin hopping with 8 perturbation / teleport / swap moves
- `tests/heilbronn_triangles/test_parity.py` — parity tests against downloaded leaderboard solutions

*Last updated: 2026-04-13*
