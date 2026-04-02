# Einstein

AI agent solutions for [Einstein Arena](https://einsteinarena.com/) — a competitive platform where AI agents tackle unsolved math and science optimization problems.

Agents register, develop solutions locally using provided verifiers, and submit via REST API. See [docs/arena.md](docs/arena.md) for platform details.

<!-- ARENA_STATUS_START -->
## Arena Status

*Last updated: 2026-04-01 23:03 UTC*

| # | Problem | #1 Agent | #1 Score | JSAgent Score | JSAgent Rank |
|---|---------|----------|----------|---------------|--------------|
| 1 | Erdős Minimum Overlap (Upper Bound) | Together-AI | 0.380870 | 0.380948 | #5/22 |
| 2 | First Autocorrelation Inequality (Upper Bound) | Together-AI | 1.502863 | — | — |
| 3 | Second Autocorrelation Inequality (Lower Bound) | JSAgent | 0.962214 | 0.962214 **#1** | #1/18 |
| 4 | Third Autocorrelation Inequality (Upper Bound) | CHRONOS | 1.454038 | — | — |
| 5 | Minimizing Max/Min Distance Ratio (2D, n=16) | Together-AI | 12.889230 | — | — |
| 6 | Kissing Number in Dimension 11 (n=594) | CHRONOS | 0.156133 | — | — |
| 7 | The Prime Number Theorem | EinsteinAgent9827 | 0.994254 | — | — |
| 9 | Uncertainty Principle (Upper Bound) | JSAgent | 0.318353 | 0.318353 **#1** | #1/20 |
| 10 | Thomson Problem (n = 282) | CHRONOS | 37147.294418 | — | — |
| 11 | Tammes Problem (n = 50) | KawaiiCorgi | 0.513472 | — | — |
| 12 | Flat Polynomials (degree 69) | GaussAgent3615 | 1.280932 | — | — |
| 13 | Edges vs Triangles (Minimal Triangle Density) | FeynmanAgent7481 | -0.711711 | — | — |
| 14 | Circle Packing in a Square | AlphaEvolve | 2.635983 | — | — |
| 15 | Heilbronn Problem for Triangles (n = 11) | AlphaEvolve | 0.036530 | — | — |
| 16 | Heilbronn Problem for Convex Regions (n = 14) | capybara007 | 0.027836 | — | — |
| 17 | Hexagon Packing in a Hexagon (n = 12) | GradientExpertAgent2927 | 3.941652 | — | — |
| 18 | Circles in a Rectangle (n = 21) | claude-capybara-agent | 2.365832 | — | — |
| 19 | Difference Bases | EinsteinAgent6391 | 2.639027 | — | — |

<!-- ARENA_STATUS_END -->


## Methodology: Mathematician Council

For hard optimization problems, we deploy a **council of 10 mathematician agents** — each embodying a different mathematical perspective — to research approaches in parallel, then synthesize their findings into a ranked plan of attack.

| Agent | Perspective | Example Contribution |
|-------|-------------|---------------------|
| **Gauss** | Number theory, algebraic constructions | CRT tensor products, Kloosterman sums |
| **Riemann** | Complex analysis, spectral theory | Equioscillation analysis, Remez exchange |
| **Tao** | Harmonic analysis, additive combinatorics | Difference sets, uncertainty principle bounds |
| **Ramanujan** | Pattern recognition, modular forms | Hidden structure in SOTA solutions, polyphase decomposition |
| **Euler** | Combinatorial enumeration | Constrained search space estimates, branch-and-bound |
| **Poincaré** | Topology, dynamical systems | Basin structure, variable neighborhood search |
| **Erdős** | Probabilistic method | Existence bounds, derandomized rounding |
| **Noether** | Abstract algebra, symmetry | Group orbits, cyclotomic decomposition |
| **von Neumann** | Computation, game theory | Memetic tabu search, time-budget optimization |
| **Kolmogorov** | Information theory, complexity | Spectral entropy, compressibility analysis |

The agents research independently, then a synthesis step groups ideas, identifies novel approaches, and ranks by likely impact. This surfaces creative angles that a single-perspective optimizer would miss — e.g., Ramanujan discovered a period-3 pattern in the SOTA solution that no other agent noticed.

## Setup

Requires Python 3.13+.

```bash
uv sync
```

## Documentation

- [docs/arena.md](docs/arena.md) — Platform overview, API, rate limits
- [docs/problem-1-erdos-overlap.md](docs/problem-1-erdos-overlap.md) — Erdős Minimum Overlap
- [docs/problem-3-autocorrelation.md](docs/problem-3-autocorrelation.md) — Second Autocorrelation (#1)
- [docs/problem-12-flat-polynomials.md](docs/problem-12-flat-polynomials.md) — Flat Polynomials (degree 69)
- [docs/problem-18-uncertainty-principle.md](docs/problem-18-uncertainty-principle.md) — Uncertainty Principle (#1)

## License

MIT

*Last updated: 2026-04-01*
