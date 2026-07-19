---
type: question
author: agent
drafted: 2026-05-25
status: open
asked_by: agent
related_problems: []
related_findings:
  - research-synthesis-design
cites:
  - ../../domains/ai-agents/source/2026-lin-agentic-harness-engineering-ahe.md
  - ../../domains/ai-agents/source/2026-ning-code-as-agent-harness.md
---

# What structural signal would surface a regression before commit in a self-evolving harness?

## Question

AHE ([`domains/ai-agents/source/2026-lin-agentic-harness-engineering-ahe.md`](../../domains/ai-agents/source/2026-lin-agentic-harness-engineering-ahe.md))
reports a sharp asymmetry in self-attribution by a strong evolve agent: **fixes
are foreseeable, regressions are not**. Across ten iterations:

- Predicted-fix precision and recall both swing high across rounds.
- Predicted-regression cumulative precision = 11.6%, recall = 11.1%.
- 40 regressions occurred unforeseen vs 5 foreseen.

The Code-as-Agent-Harness survey
([`domains/ai-agents/source/2026-ning-code-as-agent-harness.md`](../../domains/ai-agents/source/2026-ning-code-as-agent-harness.md))
names "regression-free self-evolving harnesses" as an explicit open problem.

Concretely: an outer-loop agent edits a file-mounted harness component
(prompt, tool, middleware, skill, sub-agent, memory) and writes a manifest
including `predicted_regressions: [...]`. The current state of the art has
the agent miss ~9 out of 10 actual regressions. **What structural signal,
visible at edit-write time and cheap to compute, would surface a likely
regression before the commit lands?**

## Why it matters

Both directions of the einstein autonomous loop will hit this:

- When the agent edits `.claude/rules/` or `cb/scripts/` as part of the
  meta-loop branch's self-improvement, the regression-foresight failure mode
  is exactly what could silently degrade the cycle without anyone noticing.
- The triple-verify axiom is currently the project's only line of defense:
  catch regressions in the score after the fact. That's slow and binary.
  A pre-commit structural signal would be a meaningful upgrade.

## What might count as an answer

- A diffable invariant set (e.g., "every rule that defines an axiom must still
  appear in cycle-discipline.md's checks list after the edit").
- A regression-test harness over a frozen golden-set of past cycles (replay
  N=20 prior cycles against the new harness, compare scores element-wise).
- A learned predictor trained on a corpus of past commit → cycle-score deltas
  (most expensive; least likely to be honest).
- An admission that the answer is "you can't beat 11.1% recall without an
  external evaluator," in which case the design implication is to invest in
  the external evaluator (golden-set replay) rather than in better
  predicted-regression prompts.

## Status

Open. Surfaced by the literature synthesis in
[`../findings/research-synthesis-design.md`](../findings/research-synthesis-design.md);
not in scope for `js/feat/research-synthesis` (which focuses on the
upstream/synthesis side of the loop). Candidate for `js/feat/meta-loop` G4 or
a follow-on branch.

## Suggested sources

Not yet enriched by `gap_search.py`. Re-run the tool after this question is
in qmd's index.
