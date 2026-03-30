# Einstein

My solutions for [Einstein Arena](https://einsteinarena.com/) — a competitive platform where AI agents tackle unsolved math and science optimization problems.

Agents register, develop solutions locally using provided verifiers, and submit via REST API. See [docs/arena.md](docs/arena.md) for details on how the platform works.

## Setup

Requires Python 3.13+.

```bash
uv sync
```

## Progress

| # | Problem | Status | Notes |
|---|---------|--------|-------|
| 1 | Circle Packing in a Square | - | |
| 2 | Circles in a Rectangle (n=21) | - | |
| 3 | Difference Bases | - | |
| 4 | Edges vs Triangles | - | |
| 5 | Erdos Minimum Overlap | - | |
| 6 | First Autocorrelation Inequality | - | |
| 7 | Flat Polynomials (degree 69) | - | |
| 8 | Heilbronn Problem for Convex Regions (n=14) | - | |
| 9 | Heilbronn Problem for Triangles (n=11) | - | |
| 10 | Hexagon Packing in a Hexagon (n=12) | - | |
| 11 | Kissing Number in Dimension 11 (n=594) | - | |
| 12 | Minimizing Max/Min Distance Ratio (2D, n=16) | - | |
| 13 | Second Autocorrelation Inequality | - | |
| 14 | Tammes Problem (n=50) | - | |
| 15 | The Prime Number Theorem | - | |
| 16 | Third Autocorrelation Inequality | - | |
| 17 | Thomson Problem (n=282) | - | |
| 18 | Uncertainty Principle | **#1** | S=0.31835 — beats REDACTED SOTA (0.31885) |

## Problem 18: Uncertainty Principle

**Score: 0.31835263** (verified exact) — **#1 on leaderboard**, beating REDACTED's 0.31885459.

Approach:
- **Laguerre double roots** (k=13) following Cohn & Goncalves (2017)
- **Numba-JIT fast evaluator** with 20k-point grid scan + exponential far-out sign-change detection to x=100,000
- **Exact SymPy verification** as quality gate — rejects results with hidden far sign changes
- **RALPH-style adaptive optimization loop** — 8 strategies (CMA-ES, hillclimb, Nelder-Mead, L-BFGS-B, basin-hopping, pairwise, perturbation, differential evolution) compete each iteration; top 3 + 2 random selected adaptively based on recorded performance history

Key insight: most optimizer "improvements" produce parasitic sign changes at x >> max(roots) that the standard grid scan misses. The two-tier verification pipeline (fast numerical + exact SymPy) is critical for correctness.

## License

MIT
