# Einstein

My solutions for [Einstein Arena](https://einsteinarena.com/) — a competitive platform where AI agents tackle unsolved math and science optimization problems.

Agents register, develop solutions locally using provided verifiers, and submit via REST API. See [docs/arena.md](docs/arena.md) for details on how the platform works.

## Setup

Requires Python 3.13+.

```bash
uv sync
```

## Progress

| API ID | Problem | Dir | SOTA | Status |
|--------|---------|-----|------|--------|
| 1 | Erdős Minimum Overlap | min | 0.380870 | — |
| 2 | First Autocorrelation Inequality | min | 1.502863 | — |
| 3 | Second Autocorrelation Inequality | max | 0.961986 | — |
| 4 | Third Autocorrelation Inequality | min | 1.454038 | — |
| 5 | Min Distance Ratio (2D, n=16) | min | 12.88923 | — |
| 6 | Kissing Number (d=11, n=594) | min | 0.156133 | — |
| 7 | Prime Number Theorem | max | 0.994254 | — |
| 9 | Uncertainty Principle | min | 0.318353 | **#1** (JSAgent) |
| 10 | Thomson Problem (n=282) | min | 37147.29 | — |
| 11 | Tammes Problem (n=50) | max | 0.513472 | — |
| 12 | Flat Polynomials (deg 69) | min | 1.280932 | — |
| 13 | Edges vs Triangles | max | −0.71171 | — |
| 14 | Circle Packing in Square | max | 2.635983 | — |
| 15 | Heilbronn Triangles (n=11) | max | 0.036530 | — |
| 16 | Heilbronn Convex (n=14) | max | 0.027836 | — |
| 17 | Hexagon Packing (n=12) | min | 3.941652 | — |
| 18 | Circles in Rectangle (n=21) | max | 2.365832 | — |
| 19 | Difference Bases | min | 2.639027 | — |

See [docs/evaluation.md](docs/evaluation.md) for full analysis with scoring functions, constraints, and feasibility assessment.

## Problem 9: Uncertainty Principle

**Score: 0.31835263** (verified exact) — **#1 on leaderboard**, beating REDACTED's 0.31885459.

Approach:
- **Laguerre double roots** (k=13) following Cohn & Goncalves (2017)
- **Numba-JIT fast evaluator** with 20k-point grid scan + exponential far-out sign-change detection to x=100,000
- **Exact SymPy verification** as quality gate — rejects results with hidden far sign changes
- **RALPH-style adaptive optimization loop** — 8 strategies (CMA-ES, hillclimb, Nelder-Mead, L-BFGS-B, basin-hopping, pairwise, perturbation, differential evolution) compete each iteration; top 3 + 2 random selected adaptively based on recorded performance history

Key insight: most optimizer "improvements" produce parasitic sign changes at x >> max(roots) that the standard grid scan misses. The two-tier verification pipeline (fast numerical + exact SymPy) is critical for correctness.

## License

MIT
