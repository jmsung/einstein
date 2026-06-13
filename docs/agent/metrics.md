# Metrics — running scoreboard

Recomputed weekly (Friday) by hand or by `/agent-reflect` (TBD).

## Headline metrics

| Metric | Value (as of) | Target |
|---|---|---|
| Cycles completed | 0 (post-refactor; bootstrap = cycle 0) | grow over time |
| Median time-to-top-3 (over Tier-S/A) | n/a | should decrease over cycles |
| Wiki hit rate (cycle cites at least one prior wiki page) | n/a | > 80% |
| Cross-problem transfer (concepts cited by 2+ problems' tracking) | n/a (baseline) | grow |
| Author mix (agent / human / hybrid) | a:79 / h:1 / hyb:0 (bootstrap-only) | balanced over time |
| Wiki page count | 132 (concepts:30, techniques:27, personas:23, findings:25, problems:23, questions:4) | grow with cycles |
| Source corpus | 44 distillations, 24 raw PDFs | grow with ingest |
| Failure findings filed | 0 (none from new cycles yet) | proportional to attempts |

## Honesty checks

These four catch the failure modes called out in `agent/README.md`:

1. **Memorization vs improvement** — measure: cross-problem transfer count. If <2x cycles count, agent is memorizing.
2. **Human laundering** — measure: agent-authored / total wiki pages. If ~0%, agent isn't contributing.
3. **Compute-time effect** — measure: score-improvement-per-GPU-hour over cycles. Should improve as the wiki helps short-circuit dead ends.
4. **Cherry-picking** — measure: cycle-log entries / total actual cycle count. Should be 1:1 — every cycle, even failures, is logged.

## Ablation queue (run monthly)

| Date | Question | Method | Notes |
|---|---|---|---|
| 2026-06-XX (planned) | Cold-wiki vs warm-wiki | Solve a held-out problem twice — once with empty `wiki/`, once with full | The honest test |
| 2026-07-XX (planned) | Persona ablation | Disable individual personas, measure cycle outcome | Which personas earn their dispatch? |

## Recent cycles

(Empty — first cycle starts post-merge.)

<!-- compounding:start -->
## Compounding metrics (auto — Phase 4)

_Computed by `docs/tools/compounding_metrics.py`. The signal of a loop that compounds, not just runs._

| Metric | Value | Reading |
|---|---|---|
| Records achieved | 0 | problems that reached a record |
| Median time-to-record | n/a cycles | ↓ over time = compounding |
| Technique hit-rate (top3/tried) | 26% | ↑ = picks getting better |
| Cite-reuse rate | 84% (51/61) | ↑ = cycles standing on prior cites |
| % cycles recall-preceded-win | n/a (needs instrumentation) | honest gap — not faked |

<!-- compounding:end -->

## Objective trajectory & classifier (js/feat/evolve-and-measure, Goal 1)

The metric that says *direction*, not just *ran*. Computed by
`einstein.meta_loop.trajectory` from the cycle-log; surfaced in the dashboard's
per-problem "signal" column (badge + running-best sparkline).

Per problem, a **best-verified-score-vs-cycle** curve plus a classification:

| Class | Meaning | What it implies |
|---|---|---|
| **improving** | running-best moved the right way within the recent window | the loop is climbing here — leave it |
| **solved-at-floor** | a `certificate:` (dual bound / BnB negative lemma / PD-Hessian) proves the floor | flat is *solved*, not stuck — don't spend |
| **stuck** | open headroom vs arena #1, no certificate, no recent gain | the only class the evolve engine runs on |
| **unknown** | no headroom data + no certificate + flat | honest gap — not labeled either way |

Branch aggregates (from `trajectory.aggregate`): **#rank-1**,
**records/100-cycles**, **headroom-closed rate** = solved-at-floor / (solved +
stuck) — of the problems where the floor question is *decided*, the fraction
closed.

Why a `certificate:` frontmatter field and not the `status:` string: this
branch exists to stop conflating *frozen-by-policy* with *proven-at-floor*. A
problem is `solved-at-floor` only when a real proof is named.
