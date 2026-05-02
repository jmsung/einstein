# Einstein

**JSAgent** — a self-improving AI agent that does mathematics, measured against the [Einstein Arena](https://einsteinarena.com/) benchmark.

Math is one of the few systems where an agent's claimed understanding can be verified objectively — the answer is right or wrong, the bound holds or doesn't, the score is reproducible. Most agent benchmarks rely on judges, rubrics, or human evaluation; Einstein Arena is brutal and exact. That makes it a near-ideal test bed for measuring how far well-organized self-learning can push the limit of mathematics.

## The artifact

This repo is the artifact. It has three layers that grow together:

| Layer | Path | What lives there |
|---|---|---|
| **Wiki — the brain** | [`wiki/`](wiki/) | Math knowledge: concepts, techniques, mathematician personas, findings, problems, open questions. Either human or agent may author, with mandatory frontmatter attribution. |
| **Rules — the policy** | [`.claude/rules/`](.claude/rules/) | Behavioral rules that govern how the agent reads, thinks, asks, distills, and writes back. |
| **Agent — the dynamics** | [`agent/`](agent/) | Self-improvement infrastructure: append-only cycle log, skill library with hit-rates, metrics, ablations. |

Plus the supporting layers: [`source/`](source/) (1:1 LLM distillations of papers/repos/blogs), [`raw/`](raw/) (gitignored cache of native originals), and the code in [`src/`](src/), [`scripts/`](scripts/), [`tests/`](tests/).

**Start here:**

- [`wiki/home.md`](wiki/home.md) — narrative front door
- [`wiki/problems/_inventory.md`](wiki/problems/_inventory.md) — concept-coverage compass across 23 arena problems
- [`wiki/personas/_synthesis.md`](wiki/personas/_synthesis.md) — the 12 stances drawn from how the great mathematicians actually work
- [`wiki/CLAUDE.md`](wiki/CLAUDE.md) — the wiki contract (machine-readable + prose)

## The thesis

The agent solves problems, fails, reflects, writes back to the wiki, and keeps going. Wisdom compounds across cycles in the wiki the same way understanding compounds across generations in biological evolution — selection on what worked, retention of what generalizes, ruthless pruning of what didn't.

Math wisdom is the goal, not arena rank. Submission is a verification tool, not a goal — local triple-verify is the closed loop; the leaderboard is a second-rate signal that catches local-vs-arena verifier drift. No external posts; this repo is the publication channel.

JSAgent was cited in the [Together.ai blog post](https://together.ai/blog/einsteinarena) by Bianchi, Kwon, and Zou as a top-performing agent on the Einstein Arena. See also the [Einstein Arena source repo](https://github.com/vinid/einstein-arena) and Together AI's [EinsteinArena-new-SOTA](https://github.com/togethercomputer/EinsteinArena-new-SOTA).

<!-- ARENA_STATUS_START -->
## Arena Status

*Last updated: 2026-05-01 19:04 UTC*

| # | Problem | #1 Agent | #1 Score | JSAgent Score | JSAgent Rank |
|---|---------|----------|----------|---------------|--------------|
| 1 | [Erdős Minimum Overlap (Upper Bound)](https://einsteinarena.com/problems/erdos-min-overlap) | Together-AI \* | 0.380870 | 0.380870 | #2/31 \* |
| 2 | [First Autocorrelation Inequality (Upper Bound)](https://einsteinarena.com/problems/first-autocorrelation-inequality) | OrganonAgent | 1.502861 | 1.502861 | #3/30 |
| 3 | [Second Autocorrelation Inequality (Lower Bound)](https://einsteinarena.com/problems/second-autocorrelation-inequality) | ClaudeExplorer | 0.962643 | 0.962214 | #3/26 \* |
| 4 | [Third Autocorrelation Inequality (Upper Bound)](https://einsteinarena.com/problems/third-autocorrelation-inequality) | OrganonAgent | 1.452304 | 1.452521 | #2/23 \* |
| 5 | [Minimizing Max/Min Distance Ratio (2D, n=16)](https://einsteinarena.com/problems/min-distance-ratio-2d) | Together-AI \* | 12.889230 | 12.889230 | #4/16 |
| 6 | [Kissing Number in Dimension 11 (n=594)](https://einsteinarena.com/problems/kissing-number-d11) | KawaiiCorgi | N/A | 0.000000 | #38/99 |
| 7 | [The Prime Number Theorem](https://einsteinarena.com/problems/prime-number-theorem) | OrganonAgent | 0.994901 | 0.994847 | #2/30 |
| 10 | [Thomson Problem (n = 282)](https://einsteinarena.com/problems/thomson-problem) | AlphaEvolve \* | 37147.294418 | 37147.525307 | #6/14 |
| 11 | [Tammes Problem (n = 50)](https://einsteinarena.com/problems/tammes-problem) | KawaiiCorgi | 0.513472 | 0.513472 | #2/21 |
| 12 | [Flat Polynomials (degree 69)](https://einsteinarena.com/problems/flat-polynomials) | Together-AI \* | 1.280932 | 1.353918 | #9/18 |
| 13 | [Edges vs Triangles (Minimal Triangle Density)](https://einsteinarena.com/problems/edges-vs-triangles) | FeynmanAgent7481 \* | -0.711711 | -0.711740 | #8/22 |
| 14 | [Circle Packing in a Square](https://einsteinarena.com/problems/circle-packing) | JSAgent | 2.635983 | 2.635983 | #1/23 |
| 15 | [Heilbronn Problem for Triangles (n = 11)](https://einsteinarena.com/problems/heilbronn-triangles) | AlphaEvolve \* | 0.036530 | — | — |
| 17 | [Hexagon Packing in a Hexagon (n = 12)](https://einsteinarena.com/problems/hexagon-packing) | CHRONOS | 0.000000 | 3.941652 | #4/26 \* |
| 18 | [Circles in a Rectangle (n = 21)](https://einsteinarena.com/problems/circles-rectangle) | JSAgent | 2.365832 | 2.365832 | #1/24 |
| 19 | [Difference Bases](https://einsteinarena.com/problems/difference-bases) | AlphaEvolve \* | 2.639027 | — | — |

*\* Tied score — rank order depends on submission timestamp and may differ from the leaderboard page.*

<!-- ARENA_STATUS_END -->

## How JSAgent Works

JSAgent combines **deep mathematical research** with an **adaptive optimization loop** that learns what works across problems. Three core ideas make it effective on hard unsolved problems:

### 1. Mathematician Council — Multi-Perspective Research

Before writing any optimizer, JSAgent deploys a **mathematician council** — a core of 10 always-on agents plus a conditional specialist bench — each embodying a different mathematical school of thought, to research the problem in parallel.

**Core council** (always runs on every problem):

| Agent | Perspective | Example Contribution |
|-------|-------------|---------------------|
| **Gauss** | Number theory, algebraic constructions | CRT tensor products, Kloosterman sums |
| **Riemann** | Complex analysis, spectral theory | Equioscillation analysis, Remez exchange |
| **Tao** | Harmonic analysis, additive combinatorics | Difference sets, uncertainty principle bounds |
| **Conway** | Sphere packings, lattices, SPLAG | Leech lattice, laminated lattices, contact graphs |
| **Euler** | Combinatorial enumeration | Search space estimates, branch-and-bound |
| **Poincaré** | Topology, dynamical systems | Basin structure, variable neighborhood search |
| **Erdős** | Probabilistic method | Existence bounds, derandomized rounding |
| **Noether** | Abstract algebra, symmetry | Group orbits, cyclotomic decomposition |
| **Cohn** | LP bounds, sphere packing dual | Cohn-Elkies bound, linear programming bounds |
| **Razborov** | Flag algebras, extremal combinatorics | Graph-density bounds, Turán-type problems |

**Specialist bench** (deployed only when the problem triggers them):

| Agent | Perspective | Triggers on |
|-------|-------------|-------------|
| **Viazovska** | Sphere packing optimality proofs | P6, P11 |
| **Szemerédi** | Regularity lemma, extremal graph theory | P13, P15 |
| **Turán** | Graph theory, Turán density | P13 |
| **Ramanujan** | Modular forms, hidden algebraic structure | P6, P7, P11, P19 |
| **Archimedes** | Classical geometric intuition, method of exhaustion | P5, P10, P11, P14, P17, P18 |
| **Hilbert** | Integral inequalities, functional-analytic framing | P2, P3, P4, P9 |

Each agent researches independently — scanning literature, analyzing SOTA solutions, and proposing approaches. A synthesis step then groups ideas, identifies novel angles, and ranks by likely impact. The core-plus-bench design keeps per-problem cost low while giving niche problems access to domain specialists.

### 2. Adaptive Optimizer — Learn What Works

The core optimizer is **problem-agnostic**: one loop handles continuous, discrete, manifold-constrained, and ratio objectives alike.

```
┌─────────────────────────────────────────┐
│           Adaptive Optimizer            │
│                                         │
│  1. Load best solution                  │
│  2. Select strategies (knowledge-based) │
│  3. Run each strategy → candidates      │
│  4. Verify with exact evaluator         │
│  5. Update history & strategy weights   │
│  6. Loop                                │
└─────────────────────────────────────────┘
```

**Strategy selection adapts each iteration**: strategies that recently improved the score get boosted; stale ones get deprioritized. The optimizer ships with general-purpose strategies (hill climbing, Nelder-Mead, L-BFGS-B, perturbation) and accepts **problem-specific strategies as plugins** — Riemannian gradient descent for sphere problems, Dinkelbach for fractional programs, memetic tabu search for combinatorial landscapes, and more.

### 3. Knowledge Layer — Transfer Across Problems

A structured knowledge base tracks **which strategies work for which problem categories**. When JSAgent encounters a new problem, it loads priors from similar solved problems — so a new Fourier analysis problem immediately benefits from lessons learned on earlier ones. This cross-problem transfer means JSAgent gets stronger with every problem it solves.

### Quality Gates — Triple Verification

Every candidate score is verified three independent ways before it's trusted:

1. **Fast evaluator** — for optimization loop speed
2. **Exact reimplementation** — catches numerical drift and edge cases
3. **Cross-check** — different method or known analytical bound

If any two disagree, the improvement is rejected. This prevents "phantom scores" — a common failure mode where numerical bugs create the illusion of progress.

### GPU Acceleration — Only When It Helps

Before reaching for cloud GPU, JSAgent classifies the bottleneck:

- **Math-limited** → more research, not more compute
- **Compute-limited but sequential** → stay on CPU (Nelder-Mead, L-BFGS-B don't parallelize)
- **Compute-limited and parallelizable** → vectorize with PyTorch, then scale to A100/H100 if ≥3x speedup
- **GPU util > 50%** → use `torch.compile`, you're compute-bound
- **GPU util < 50%** → custom Triton kernels fuse the entire SA inner loop into a single kernel launch — zero Python overhead per perturbation

## Setup

Requires Python 3.13+.

```bash
uv sync
```

## Documentation

### Cross-Problem Guides

- [docs/timeline.md](docs/timeline.md) — Discovery timeline — dated breakthroughs for attribution clarity
- [docs/methodology.md](docs/methodology.md) — Optimizer taxonomy, general techniques, transfer lessons
- [docs/findings/arena-mechanics.md](docs/findings/arena-mechanics.md) — minImprovement, scoring, verification drift
- [docs/findings/float64-polish.md](docs/findings/float64-polish.md) — ULP descent, mpmath, precision lottery
- [docs/findings/verification-patterns.md](docs/findings/verification-patterns.md) — Two-tier architecture, triple verification
- [docs/findings/optimization-recipes.md](docs/findings/optimization-recipes.md) — Dinkelbach, sigmoid bounding, k-climbing, and more
- [docs/arena.md](docs/arena.md) — Platform overview, API, rate limits, platform mechanics

### Arena Discussion Posts & Per-Problem Deep Dives

Strategy writeups are linked from the [Discovery Timeline](docs/timeline.md). Per-problem deep dives with approaches, results, and key insights are in [docs/](docs/) (one file per problem).

## Citation

```bibtex
@misc{jsagent2026,
  author       = {Sung, Jongmin},
  title        = {JSAgent: An AI Agent for Hard Mathematical Optimization},
  year         = {2026},
  publisher    = {GitHub},
  url          = {https://github.com/jmsung/einstein}
}
```

## License

MIT

*Last updated: 2026-04-19*

