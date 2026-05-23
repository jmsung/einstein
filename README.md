# Einstein

**JSAgent** — a self-improving AI agent that does mathematics, measured against the [Einstein Arena](https://einsteinarena.com/) benchmark.

Math is one of the few systems where an agent's claimed understanding can be verified objectively — the answer is right or wrong, the bound holds or doesn't, the score is reproducible. Most agent benchmarks rely on judges, rubrics, or human evaluation; Einstein Arena is brutal and exact. That makes it a near-ideal test bed for measuring how far well-organized self-learning can push the limit of mathematics.

## The artifact

This repo is the artifact. Three layers grow together:

| Layer | Path | What lives there |
|---|---|---|
| **Wiki — the brain** | [`docs/wiki/`](docs/wiki/) | Math knowledge: concepts, techniques, mathematician personas, findings, problems, open questions. Either human or agent may author, with mandatory frontmatter attribution. |
| **Rules — the policy** | [`.claude/rules/`](.claude/rules/) | Behavioral rules that govern how the agent reads, thinks, asks, distills, and writes back. |
| **Agent — the dynamics** | [`docs/agent/`](docs/agent/) | Self-improvement infrastructure: append-only cycle log, skill library with hit-rates, metrics, ablations, finding→concept promotion log. |

Supporting layers: [`docs/source/`](docs/source/) (1:1 LLM distillations of papers/repos/blogs), `docs/raw/` (gitignored local cache of native originals; regenerable from each `source/` page's `source_url`), [`docs/tools/`](docs/tools/) (wiki gap-detector + qmd reindex), and the code in [`src/`](src/), [`scripts/`](scripts/), [`tests/`](tests/).

**Start here:**

- [`docs/wiki/home.md`](docs/wiki/home.md) — narrative front door
- [`docs/wiki/problems/_inventory.md`](docs/wiki/problems/_inventory.md) — concept-coverage compass across 23 arena problems
- [`docs/wiki/personas/_synthesis.md`](docs/wiki/personas/_synthesis.md) — the 12 stances drawn from how the great mathematicians actually work
- [`docs/wiki/CLAUDE.md`](docs/wiki/CLAUDE.md) — the wiki contract (machine-readable + prose)
- [`docs/wiki/timeline.md`](docs/wiki/timeline.md) — dated discovery breakthroughs

## The thesis

The agent solves problems, fails, reflects, writes back to the wiki, and keeps going. Wisdom compounds across cycles in the wiki the same way understanding compounds across generations in biological evolution — selection on what worked, retention of what generalizes, ruthless pruning of what didn't.

Math wisdom is the goal, not arena rank. Submission is a verification tool — local triple-verify is the closed loop; the leaderboard is a second-rate signal that catches local-vs-arena verifier drift. The wiki *is* the publication channel.

JSAgent was cited in the [Together.ai blog post](https://together.ai/blog/einsteinarena) by Bianchi, Kwon, and Zou as a top-performing agent on the Einstein Arena. See also the [Einstein Arena source repo](https://github.com/vinid/einstein-arena) and Together AI's [EinsteinArena-new-SOTA](https://github.com/togethercomputer/EinsteinArena-new-SOTA).

<!-- ARENA_STATUS_START -->
## Arena Status

*Last updated: 2026-05-22 19:27 UTC*

| # | Problem | #1 Agent | #1 Score | JSAgent Score | JSAgent Rank |
|---|---------|----------|----------|---------------|--------------|
| 1 | [Erdős Minimum Overlap (Upper Bound)](https://einsteinarena.com/problems/erdos-min-overlap) | Together-AI \* | 0.380870 | 0.380870 | #2/31 \* |
| 2 | [First Autocorrelation Inequality (Upper Bound)](https://einsteinarena.com/problems/first-autocorrelation-inequality) | OrganonAgent | 1.502861 | 1.502861 | #3/30 |
| 3 | [Second Autocorrelation Inequality (Lower Bound)](https://einsteinarena.com/problems/second-autocorrelation-inequality) | ClaudeExplorer | 0.962643 | 0.962214 | #3/27 \* |
| 4 | [Third Autocorrelation Inequality (Upper Bound)](https://einsteinarena.com/problems/third-autocorrelation-inequality) | OrganonAgent | 1.452304 | 1.452521 | #2/23 \* |
| 5 | [Minimizing Max/Min Distance Ratio (2D, n=16)](https://einsteinarena.com/problems/min-distance-ratio-2d) | Together-AI \* | 12.889230 | 12.889230 | #4/16 |
| 6 | [Kissing Number in Dimension 11 (n=594)](https://einsteinarena.com/problems/kissing-number-d11) | KawaiiCorgi | N/A | 0.000000 | #38/99 |
| 7 | [The Prime Number Theorem](https://einsteinarena.com/problems/prime-number-theorem) | OrganonAgent | 0.994901 | 0.994847 | #2/30 |
| 9 | [Uncertainty Principle (Upper Bound)](https://einsteinarena.com/problems/uncertainty-principle) | JSAgent \* | 0.318169 | 0.318169 | #1/39 \* |
| 10 | [Thomson Problem (n = 282)](https://einsteinarena.com/problems/thomson-problem) | AlphaEvolve \* | 37147.294418 | 37147.525307 | #6/14 |
| 11 | [Tammes Problem (n = 50)](https://einsteinarena.com/problems/tammes-problem) | KawaiiCorgi | 0.513472 | 0.513472 | #2/21 |
| 12 | [Flat Polynomials (degree 69)](https://einsteinarena.com/problems/flat-polynomials) | Together-AI \* | 1.280932 | 1.353918 | #9/20 |
| 13 | [Edges vs Triangles (Minimal Triangle Density)](https://einsteinarena.com/problems/edges-vs-triangles) | FeynmanAgent7481 \* | -0.711711 | -0.711740 | #8/22 |
| 14 | [Circle Packing in a Square](https://einsteinarena.com/problems/circle-packing) | JSAgent | 2.635983 | 2.635983 | #1/23 |
| 15 | [Heilbronn Problem for Triangles (n = 11)](https://einsteinarena.com/problems/heilbronn-triangles) | AlphaEvolve \* | 0.036530 | — | — |
| 18 | [Circles in a Rectangle (n = 21)](https://einsteinarena.com/problems/circles-rectangle) | JSAgent | 2.365832 | 2.365832 | #1/24 |
| 19 | [Difference Bases](https://einsteinarena.com/problems/difference-bases) | AlphaEvolve \* | 2.639027 | — | — |
| 22 | [Kissing Number in Dimension 12 (n=841)](https://einsteinarena.com/problems/kissing-number-d12) | CHRONOS | 2.000000 | 2.001403 | #3/10 |

*\* Tied score — rank order depends on submission timestamp and may differ from the leaderboard page.*

<!-- ARENA_STATUS_END -->

## How JSAgent works

Four ideas, in order of when they fire on a new problem.

### 1. Mathematician council — multi-perspective research

Before writing any optimizer, JSAgent dispatches a **council of mathematician personas** in parallel — a core of 10 always-on personas plus a triggered specialist bench — each embodying a different mathematical school of thought.

| Tier | Personas | When |
|---|---|---|
| Core (always) | Gauss, Riemann, Tao, Conway, Euler, Poincaré, Erdős, Noether, Cohn, Razborov | every problem |
| Specialist bench | Viazovska, Szemerédi, Turán, Ramanujan, Archimedes, Hilbert | triggered per problem domain |
| Meta-coaches | Polya, Hadamard, Grothendieck, Atiyah, Wiles | when stuck on protocol, not math |

Each persona writes **questions, not solutions** (see [`.claude/rules/council-dispatch.md`](.claude/rules/council-dispatch.md)). Questions land in [`docs/wiki/questions/`](docs/wiki/questions/) for the gap-detect step. Full persona index: [`docs/wiki/personas/_synthesis.md`](docs/wiki/personas/_synthesis.md).

### 2. Adaptive optimizer — problem-agnostic loop

One loop handles continuous, discrete, manifold-constrained, and ratio objectives. Strategies that recently improved get boosted; stale ones get deprioritized. Ships with general-purpose strategies (hill-climb, Nelder-Mead, L-BFGS-B, perturbation) and accepts **problem-specific plugins**: Riemannian gradient descent for sphere problems, Dinkelbach for fractional programs, memetic tabu search for combinatorial landscapes, parallel-tempering SA for fractal hinge-loss landscapes, and more. Full taxonomy: [`docs/wiki/techniques/`](docs/wiki/techniques/).

### 3. Self-improving loop — wisdom compounds across cycles

Each problem-attempt cycle goes:

```
understand → wiki-first lookup → council dispatch → gap-detect → research
           → distill (cite source) → specialize (n=2,3,4) → execute → look back
           → failure-as-finding → cycle-log append → promote
```

The honesty signals live in [`docs/agent/`](docs/agent/):

- **`cycle-log.md`** — append-only row per cycle (failures count; cherry-picking forbidden)
- **`skill-library.md`** — technique hit-rates per problem category
- **`metrics.md`** — time-to-top-3, transfer count, score-per-GPU-hour, agent/human authorship mix
- **`promotion-log.md`** — finding→concept graduations (human-gated)
- **`ablations/`** — controlled experiments (cold-wiki vs warm-wiki, persona ablation)

Every dead-end becomes a `docs/wiki/findings/dead-end-<slug>.md` with the *why*. Tomorrow's breakthrough sits on yesterday's articulated obstruction.

### 4. Triple verification — every score, three ways

Every candidate score must agree under three independent evaluations: a fast evaluator (drives the loop), an exact reimplementation (catches numerical drift), and a cross-check (analytical bound or different method). If any two disagree, the score is fake — debug before proceeding. This is the closed loop; submission to the arena is the second-rate signal that catches local↔arena verifier drift. See [`.claude/rules/triple-verify.md`](.claude/rules/triple-verify.md).

## Compute routing

Two first-class environments, picked per workload before launch:

- **Local M5 Max (128GB)** — mpmath polish, sequential CPU optimizers (L-BFGS / NM / SLSQP), small basin-hopping, MPS float32 batch ops, large multistart with multiprocess.
- **Modal A100/H100** — sustained float64 GPU parallel (parallel tempering, CMA-ES large-pop float64), large LP/SDP that's RAM-bound.

Decision matrix in [`docs/wiki/techniques/compute-router.md`](docs/wiki/techniques/compute-router.md); pre-launch audit rule in [`.claude/rules/compute-router.md`](.claude/rules/compute-router.md).

## Setup

Requires Python 3.13+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync                                # install all deps
uv run python -m pytest tests/ -v      # run all tests
uv run python scripts/<problem>/...    # run a per-problem entry point
modal run scripts/<problem>/modal_*.py # GPU runs (needs Modal account)
```

## Layout

```
cb/                            # public artifact (this repo)
├── docs/
│   ├── wiki/                  # math knowledge: concepts/, techniques/, findings/,
│   │                          # personas/, problems/, questions/, home.md, timeline.md
│   ├── source/                # 1:1 LLM distillations of papers/blog/repos
│   ├── raw/                   # gitignored — native originals (PDFs)
│   ├── agent/                 # self-improvement infra
│   └── tools/                 # wiki_graph.py + refresh_qmd.sh
├── src/einstein/              # per-problem subpackages + shared modules
├── scripts/                   # entry points (per-problem + cross-cutting)
├── tests/                     # per-problem pytest
└── .claude/rules/             # behavioral rules (always-loaded)
```

## Documentation

- [`docs/wiki/timeline.md`](docs/wiki/timeline.md) — dated breakthroughs
- [`docs/wiki/concepts/arena-platform.md`](docs/wiki/concepts/arena-platform.md) — platform overview, API, rate limits
- [`docs/wiki/findings/`](docs/wiki/findings/) — cross-problem findings (arena mechanics, float64 polish, verification patterns, optimizer recipes, …)
- [`docs/wiki/techniques/`](docs/wiki/techniques/) — optimizer taxonomy + reusable methods
- [`docs/wiki/problems/`](docs/wiki/problems/) — per-problem deep dives (one file per arena problem)

Search the wiki with [qmd](https://github.com/tobi/qmd):

```bash
qmd query "<question>" -c einstein-wiki -n 5            # synthesis layer
qmd query "<question>" -c einstein-wiki-source -n 5     # distilled summaries
```

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

*Last updated: 2026-05-22*
