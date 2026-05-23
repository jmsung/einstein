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
