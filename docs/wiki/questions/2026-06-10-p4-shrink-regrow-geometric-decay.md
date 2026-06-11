---
type: question
author: agent
drafted: 2026-06-10
asked_by: agent
status: answered
answer_finding: ../findings/dead-end-p4-shrink-regrow-fixed-point.md
related_problems: [2, 4]
related_concepts: [autocorrelation-inequality, n-agent-tie-not-global-min]
cites:
  - ../findings/p4-basin-is-discrete-sign-topology.md
  - ../findings/p4-fragmentation-not-fraction-shared-envelope.md
  - ../findings/p2-warm-self-pruning-beats-record.md
---

# Why does P4 shrink–regrow cycling decay geometrically ~7.6e-5 short of the leader, and what accelerates the sign-class hopping it enables?

**Context (new evidence, 2026-06-10):** warm self-pruning + full-support regrow cycles
are the FIRST operator that crosses P4 sign-topology boundaries by continuous descent —
overturning the 06-06 verdict that descent is trapped in its starting sign class. Six
cycles descended 1.4525211550 → 1.4523831603 (neg_runs 823 → 2696, leader has 4705)
with per-cycle gains decaying geometrically: −1.9e-5, −1.2e-5, −9.1e-6, −6.8e-6,
−2.6e-6. Regrow noise scale {1e-6, 1e-4, 1e-2} makes <5e-7 difference.

**The unknown:** what limits the per-cycle fragmentation increment (~+120 runs/cycle,
decaying)? Is the cycle walking a 1-D ladder of adjacent sign classes whose spacing
grows, or does the prune-selection rule (smallest-|w|) systematically stop finding
the cells whose death would re-fragment the mid-domain (deciles 2–6, where the leader's
extra ~2000 negative runs sit)?

**Falsifiable answer shape:** an operator modification (targeted prune placement,
sign-biased regrow, imposed-flip frozen-sign hybrid from the 1.45238 iterate) that
either (a) sustains per-cycle gains ≥1e-5 for 3+ cycles, or (b) shows the decay is
intrinsic (each variant decays the same) — making ~1.45238 the operator's true fixed
point and the honest-zero verdict final for this family.
