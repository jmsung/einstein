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
| 13 | Second Autocorrelation Inequality | **#1** | C=0.96221 — cross-resolution structure transplant |
| 14 | Tammes Problem (n=50) | - | |
| 15 | The Prime Number Theorem | - | |
| 16 | Third Autocorrelation Inequality | - | |
| 17 | Thomson Problem (n=282) | - | |
| 18 | Uncertainty Principle | In progress | Hillclimb optimizer with fast numerical evaluator |

## License

MIT
