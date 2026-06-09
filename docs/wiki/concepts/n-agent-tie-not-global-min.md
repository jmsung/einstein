---
type: concept
author: agent
drafted: 2026-06-08
related_problems: [2, 3, 4, 22, 23]
related_concepts:
  - parameterization-induced-rank-deficiency
  - basin-rigidity
related_findings:
  - p2-warm-self-pruning-beats-record.md
  - dead-end-p2-compact-support-basin-floor.md
cites:
  - ../findings/p2-warm-self-pruning-beats-record.md
  - ../findings/dead-end-p2-compact-support-basin-floor.md
---

# An N-agent tie is a sharp shared basin, not a proof of global optimality

## The claim

When several *independent* agents/solutions converge to the same score to many
digits (a "tie to 1e-13"), the correct inference is **"this is a sharp, attractive
local basin that the common search methods all fall into"** — NOT "this is the
global optimum." The two are easily confused and the confusion is expensive: it
closes problems as "honest-zero / floor confirmed" while a better basin sits
unexplored.

## Why a tie is weaker evidence than it looks

Independent searchers are rarely independent in the way that matters. They tend to
share:

- **The same parameterization** (e.g. everyone uses `f = exp(v)` → full support; or
  everyone warm-starts from the same public seed).
- **The same search operator** (gradient polish, basin-hopping, CMA-ES) with the
  same blind spots.
- **The same discretization and initialization folklore.**

Given shared machinery, convergence to the same point is *expected* — it measures
the **strength of one basin's attractor**, not the **absence of other basins**. A
tie to 1e-13 says the basin is sharp and that polishing within it is exhausted; it
says nothing about basins reachable only by a *different operator*.

## The P2 case (the falsification)

On P2 (first-autocorrelation), OrganonAgent and CHRONOS tied at
**C = 1.5028609073611** to 1e-13, both at a compact-support configuration
(74489/90000 nonzero). The wiki recorded this as "almost certainly the global
minimum" and set the branch EV to honest-zero
([dead-end-p2-compact-support-basin-floor](../findings/dead-end-p2-compact-support-basin-floor.md)).

A search operator no competitor had tried — **warm data-driven self-pruning** (start
full-support, let the optimizer zero the smallest cells under `f=v²`, shrink support)
— reached **C = 1.5028506180**, beating the "global min" by 1.03e-5 (four orders past
the record gate), arena-verified
([p2-warm-self-pruning-beats-record](../findings/p2-warm-self-pruning-beats-record.md)).
The tie was a sharp local basin. The prior was wrong.

## How to apply (the diagnostic)

Before declaring "this is the floor / honest-zero" on a record attempt where the SOTA
is an N-agent tie, ask the falsifying question:

1. **What do the tied solutions share?** Same parameterization? Same support
   structure? Same warm-start lineage? If yes, the tie is intra-method, not
   cross-method.
2. **Is there a search operator no one in the tie has tried?** A different
   parameterization (`exp(v)` → `v²`), a different topology move (support shrink,
   symmetry break), a different starting regime (warm vs cold). If yes, **the floor
   is unproven** — the untried operator is the next attempt, not the dead-end.
3. **Only when a genuine *proof* exists** (a dual certificate, an LP/SDP bound that
   matches the value) is "this is the floor" warranted. An empirical tie is never a
   proof — see [p2-record-gate-no-cheap-certificate](../findings/p2-record-gate-no-cheap-certificate.md):
   the proven ceiling for P2 is ≤1.28, far below the arena value, so nothing
   *forced* 1.5028609 to be optimal.

## What this rules out

- Treating leaderboard consensus as a stopping criterion. Consensus among
  same-method searchers is not optimality.
- Closing a problem as honest-zero while an untried operator is on the table — that
  is the [wall-hit](../../.claude/rules/wall-hit-escalation.md) anti-pattern wearing
  a respectable disguise ("the floor is confirmed").

## See also

- [parameterization-induced-rank-deficiency](parameterization-induced-rank-deficiency.md) — why one operator (`v²`) reaches basins another (`exp(v)`) structurally cannot.
- Technique: [warm-self-pruning-compact-support](../techniques/warm-self-pruning-compact-support.md) — the operator that broke the P2 tie.
