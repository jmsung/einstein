---
type: harness
author: agent
drafted: 2026-06-12
status: live
cites: [docs/agent/metrics.md, docs/agent/cycle-log.md]
---

# The self-improving harness — system description

This page is the system section: what JSAgent *is*, as a machine. The
[home page](home.md) frames the experiment (arena = gym, math = verifiable
system, agent = subject, wiki = artifact); this page describes the loop that
turns those into a measurable claim.

The honest thesis of this harness is **not** "we beat records" — the benchmark
is largely saturated and several problems sit at certified floors. It is: *we
built a self-improving, knowledge-based agentic loop and rigorously measured
whether it improves* — including a methodology to tell **compounding** from a
**random walk**, and an honest ablation of whether a curated knowledge base
beats web search. Contribution = rigor + methodology + (likely) negative
result, not the engine (AlphaEvolve / FunSearch already published that shape).

## The loop

```
understand → wiki-first → council dispatch → gap-detect → research → distill
   → specialize → execute → triple-verify → look-back → failure-log → commit
```

Each cycle is one row in [`docs/agent/cycle-log.md`](../agent/cycle-log.md)
(append-only, failures included — cherry-picking is forbidden by
`cycle-discipline`). The pieces:

1. **Council of personas** — a parallel panel of mathematician personas, each
   writing the *questions* a stuck expert would ask (not solutions). Questions
   seed the gap-detect loop.
2. **Adaptive optimizer + Thompson bandit** — one loop over continuous /
   discrete / manifold / ratio objectives; a bandit boosts recently-winning
   techniques and deprioritizes stale ones. Best-of-K *fanout* runs K attempts
   per visit (`einstein.parallel.fanout`).
3. **Knowledge base (the wiki)** — every cycle writes back: dead-ends become
   *findings* (with the articulated *why*), recurring findings get promoted
   (human-gated) to *concepts*. The next cycle queries it first. This is the
   only layer that survives across sessions/contexts/models.
4. **Triple-verify** — every score is checked three ways (fast evaluator,
   exact reimplementation, analytical/different-method cross-check). Two that
   disagree ⇒ the score is fake. This is the closed loop; arena submission is
   only a fourth, slower check.

## The measurement layer (js/feat/evolve-and-measure)

The loop above ran 380+ cycles with 0 new records and no way to tell
*plateaued-because-solved* (at a certified floor) from *plateaued-because-stuck*
(open headroom). This layer makes the difference legible:

- **Objective-trajectory metric + classifier**
  (`einstein.meta_loop.trajectory`). Per problem, a *best-verified-score-vs-
  cycle* curve from the cycle-log; each problem is classified:
  - **improving** — running-best moved the right way recently;
  - **solved-at-floor** — a `certificate:` (dual bound / BnB negative lemma /
    PD-Hessian) proves the floor — a flat score here is *solved*, not stuck;
  - **stuck** — open headroom vs arena #1, no certificate, no recent gain;
  - **unknown** — not enough signal to decide honestly.
  Gating on an explicit certificate (not status strings) is the point: it stops
  conflating *frozen-by-policy* with *proven-at-floor*. Aggregates: #rank-1,
  records/100-cycles, headroom-closed rate.
- **Dashboard signal column** — the per-problem table shows the classifier
  badge + a sparkline of the running-best curve, so direction is a glance.
- **Per-cycle solution artifacts** (`einstein.meta_loop.solution_artifact`) —
  each cycle persists the actual solution/params it produced (`cycle-<id>.json`),
  linked from the dashboard log viewer so a plateau is *inspectable*.
- **AlphaEvolve engine** (`einstein.meta_loop.evolve`) — champion → mutate-K →
  triple-verify → promote best **iff strictly better** → repeat. The champion
  is monotone; it moves only on a triple-verified strict gain. **Gated to
  `stuck` problems only** — running it on a solved-at-floor problem would burn
  LLM spend chasing a proven floor.
- **3-arm ablation** (planned, Goal 6) — A = curated wiki, B = web search
  (firewalled from the leaderboard / this repo / solution dumps), C = model-only.
  Cold-start, N seeds, measured locally by climb-rate, dead-ends-avoided, and
  cycles-to-X%-of-floor. It varies *reasoning support*, not *answer access* —
  this is the publishable experiment.

## Reading the result honestly

The four honesty checks (`docs/agent/README.md`) are structural, not
aspirational: 1:1 cycle:log discipline (no cherry-picking), agent/human author
mix (no human laundering), score-per-compute over cycles (compute-effect
control), and cross-problem transfer (memorization control). The trajectory
classifier adds the fifth: a plateau now carries a *reason*, so "the loop
stopped improving" can be read as *solved* or *stuck* rather than left
ambiguous. See [`docs/agent/metrics.md`](../agent/metrics.md) for the live
scoreboard.
