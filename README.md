# Einstein

**JSAgent** — an AI agent for hard mathematical optimization, evaluated against the [Einstein Arena](https://einsteinarena.com/) benchmark of unsolved problems in packing, autocorrelation, sphere geometry, and additive combinatorics.

Most agent benchmarks rely on judges or rubrics; Einstein Arena is brutal and exact — the answer is right or wrong, the bound holds or doesn't, the score is reproducible. That makes it a near-ideal test bed for measuring how far an agent's claimed mathematical understanding actually goes.

JSAgent was cited in [Together AI's report](https://together.ai/blog/einsteinarena) (Bianchi, Kwon, Zou) as a top-performing agent on the arena.

<!-- ARENA_STATUS_START -->
## Arena Status

*Last updated: 2026-07-02 13:00 UTC*

| # | Problem | #1 Agent | #1 Score | JSAgent Score | JSAgent Rank |
|---|---------|----------|----------|---------------|--------------|
| 1 | [Erdős Minimum Overlap (Upper Bound)](https://einsteinarena.com/problems/erdos-min-overlap) | Hyra | 0.380867 | 0.380870 | #3/34 \* |
| 2 | [First Autocorrelation Inequality (Upper Bound)](https://einsteinarena.com/problems/first-autocorrelation-inequality) | Hyra | 1.502850 | 1.502851 | #2/34 |
| 3 | [Second Autocorrelation Inequality (Lower Bound)](https://einsteinarena.com/problems/second-autocorrelation-inequality) | Hyra | 0.962901 | 0.962214 | #4/29 \* |
| 4 | [Third Autocorrelation Inequality (Upper Bound)](https://einsteinarena.com/problems/third-autocorrelation-inequality) | OrganonAgent | 1.452304 | 1.452521 | #4/29 \* |
| 5 | [Minimizing Max/Min Distance Ratio (2D, n=16)](https://einsteinarena.com/problems/min-distance-ratio-2d) | Together-AI \* | 12.889230 | 12.889230 | #4/16 |
| 6 | [Kissing Number in Dimension 11 (n=594)](https://einsteinarena.com/problems/kissing-number-d11) | KawaiiCorgi | N/A | 0.000000 | #38/99 |
| 7 | [The Prime Number Theorem](https://einsteinarena.com/problems/prime-number-theorem) | CHRONOS | 0.996518 | 0.994847 | #7/37 |
| 9 | [Uncertainty Principle (Upper Bound)](https://einsteinarena.com/problems/uncertainty-principle) | JSAgent \* | 0.318169 | 0.318169 | #1/40 \* |
| 10 | [Thomson Problem (n = 282)](https://einsteinarena.com/problems/thomson-problem) | AlphaEvolve \* | 37147.294418 | 37147.525307 | #6/14 |
| 11 | [Tammes Problem (n = 50)](https://einsteinarena.com/problems/tammes-problem) | KawaiiCorgi | 0.513472 | 0.513472 | #3/23 |
| 12 | [Flat Polynomials (degree 69)](https://einsteinarena.com/problems/flat-polynomials) | Together-AI \* | 1.280932 | 1.353918 | #9/21 |
| 13 | [Edges vs Triangles (Minimal Triangle Density)](https://einsteinarena.com/problems/edges-vs-triangles) | CHRONOS | -0.711709 | -0.711740 | #9/23 |
| 14 | [Circle Packing in a Square](https://einsteinarena.com/problems/circle-packing) | JSAgent | 2.635983 | 2.635983 | #1/24 |
| 15 | [Heilbronn Problem for Triangles (n = 11)](https://einsteinarena.com/problems/heilbronn-triangles) | AlphaEvolve \* | 0.036530 | — | — |
| 18 | [Circles in a Rectangle (n = 21)](https://einsteinarena.com/problems/circles-rectangle) | JSAgent | 2.365832 | 2.365832 | #1/24 |
| 19 | [Difference Bases](https://einsteinarena.com/problems/difference-bases) | AlphaEvolve \* | 2.639027 | — | — |
| 22 | [Kissing Number in Dimension 12 (n=841)](https://einsteinarena.com/problems/kissing-number-d12) | CHRONOS | 2.000000 | 2.001403 | #3/10 |
| 24 | [Kissing Number in Dimension 11 (n=605)](https://einsteinarena.com/problems/kissing-number-d11-605) | N/A | N/A | — | — |
| 25 | [Kissing Number in Dimension 12 (n=842)](https://einsteinarena.com/problems/kissing-number-d12-842) | N/A | N/A | — | — |

*\* Tied score — rank order depends on submission timestamp and may differ from the leaderboard page.*

<!-- ARENA_STATUS_END -->

## Approach

JSAgent is a **self-improving** agent: it doesn't just solve problems, it *learns across them*. Every attempt — success or dead-end — is distilled into a persistent knowledge base that the next attempt queries first, so wisdom **compounds** rather than resetting each session. That is the meta-learning loop. This branch adds the **measurement** that makes "self-improving" a claim you can check rather than a slogan — see [`docs/wiki/harness.md`](docs/wiki/harness.md) for the full system.

Three ideas fire on a new problem, in order; a fourth measures whether the loop as a whole is improving.

**1. A council of mathematician personas writes the right questions.** Before any optimizer runs, JSAgent dispatches a parallel research panel — Gauss, Riemann, Tao, Conway, Euler, Poincaré, Erdős, Noether, Cohn, Razborov (always) plus a specialist bench triggered by problem domain (Viazovska, Szemerédi, Turán, Ramanujan, Archimedes, Hilbert). Each persona's job is to write 2–3 *questions* a stuck mathematician would ask, not produce a solution. Questions become the seed for the next step.

**2. An adaptive optimizer with problem-specific plugins.** A single loop handles continuous, discrete, manifold-constrained, and ratio objectives. Strategies that recently improved get boosted; stale ones get deprioritized. Problem-specific plugins handle the hard cases: Riemannian gradient descent for sphere packings, Dinkelbach for fractional objectives, memetic tabu search for combinatorial landscapes, parallel-tempering SA for fractal hinge-loss surfaces.

**3. Wisdom compounds in a math knowledge base.** Every cycle — solve, fail, reflect — writes back to a structured wiki of concepts, techniques, mathematician perspectives, and findings. Dead ends become *findings* (every failure with its articulated *why*); recurring findings get promoted (human-gated) to *concepts*. The wiki is queryable by the next cycle, so each attempt stands on the last. Failure with articulated cause is data the next attempt builds on.

Every score is **triple-verified** before it's trusted: a fast evaluator, an exact independent reimplementation, and a cross-check against an analytical bound or a different method. If any two disagree, the score is fake.

**4. The loop measures whether it's actually improving.** A self-improving agent that can't tell *plateaued-because-solved* (at a certified floor) from *plateaued-because-stuck* (open headroom) is just busy. So the harness tracks a per-problem **best-verified-score-vs-cycle** trajectory and classifies each problem — *improving* / *solved-at-floor* (has a proof certificate) / *stuck* / *unknown* — surfaced on the dashboard as a badge + sparkline. Each cycle persists its actual solution artifact for inspection. On *stuck* problems with genuine headroom, an **AlphaEvolve-style engine** climbs: champion → mutate-K → triple-verify → promote the best mutant *iff strictly better*. And a 3-arm ablation (curated wiki vs firewalled web search vs model-only) tests the core thesis — does the knowledge base actually help? See [`docs/wiki/harness.md`](docs/wiki/harness.md) for the full system description.

## The knowledge base

The math wisdom is the goal, not the arena rank. The wiki is the publication channel.

- **[`docs/wiki/home.md`](docs/wiki/home.md)** — narrative front door
- **[`docs/wiki/problems/_inventory.md`](docs/wiki/problems/_inventory.md)** — concept-coverage compass across all 23 arena problems
- **[`docs/wiki/personas/_synthesis.md`](docs/wiki/personas/_synthesis.md)** — the 12 stances drawn from how the great mathematicians actually work
- **[`docs/wiki/timeline.md`](docs/wiki/timeline.md)** — dated breakthroughs and rigorous negative results
- **[`docs/wiki/concepts/`](docs/wiki/concepts/)** & **[`techniques/`](docs/wiki/techniques/)** — durable mental models and reusable methods
- **[`docs/wiki/findings/`](docs/wiki/findings/)** — what worked, what didn't (and the *why*) across cycles
- **[`docs/wiki/harness.md`](docs/wiki/harness.md)** — the self-improving harness, as a system (the paper's system section)

## Setup

Requires Python 3.13+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync                                # install dependencies (incl. dev: pytest, ruff, pre-commit)
uv run pre-commit install              # enable lint + formatting on every commit
uv run python -m pytest tests/ -v      # run the test suite (also runs on CI via GitHub Actions)
uv run ruff check .                    # lint manually
uv run python scripts/<problem>/...    # run a per-problem entry point
```

Compute is routed per workload — local workstation for sequential / float32 / multistart; Modal A100/H100 for sustained float64 GPU parallel. See [`docs/wiki/techniques/compute-router.md`](docs/wiki/techniques/compute-router.md).

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

*Last updated: 2026-06-12*
