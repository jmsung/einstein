---
type: question
author: agent
drafted: 2026-05-28
asked_by: agent-recursive-meta
status: open
related_problems: []
related_concepts: []
cites:
  - ../findings/recursive-meta-design.md
---

# What's the simplest safe `meta_self_edit` we'd expect to see in practice?

## The question

Given the gate chain on `js/feat/recursive-meta` (≥10 cycles, mandatory shadow
A/B with `p < 0.1`, never auto-merge, snapshot-based revert), what does the
*smallest* `meta_self_edit` look like that would actually clear all gates and
land in `mb/meta-self-edit-queue/`?

## Why it matters

Hypothesis: a diff that adds a *read-only* column to `diagnose.py`'s report
(e.g. mean wall-clock per cycle, or count of distinct techniques tried per
problem) is the floor — read-only, easily reverted, low blast radius, would
plausibly let the proposer surface meta-layer signals it currently can't.

If dogfood (G6) produces *only* higher-risk candidates — gate-strictness
tweaks, proposal-type whitelist edits, audit-log column changes — that's
diagnostic evidence the thresholds in `recursive-meta-design.md` aren't tight
enough at the *proposer* (the proposer is generating high-risk candidates
because it isn't surfacing the easy ones).

If dogfood produces *no* candidates at all, the thresholds are too tight at
either the proposer or the gate; the dead-end finding goes to
`findings/dead-end-recursive-meta-thresholds-too-tight.md`.

## How we'd recognize an answer

A merged `mb/meta-self-edit-queue/<>` entry with:

- a diff that touches `scripts/meta_loop.py` only,
- evidence ≥10 cycles,
- shadow A/B verdict `a_wins=TRUE` with `p < 0.1`,
- a human review note classifying it as "read-only / diagnostic-only" vs
  "behavior-changing".

The shape of the first such entry IS the answer.

## See also

- [`findings/recursive-meta-design.md`](../findings/recursive-meta-design.md)
- [`findings/meta-loop-first-run.md`](../findings/meta-loop-first-run.md) — the
  parallel "first-run" question on the non-recursive meta-loop, still pending
  its own first-run distillation.

## Suggested sources

*Auto-suggested by `docs/tools/gap_search.py` — arxiv query: `(all:"What's the simplest safe `meta_self_edit` we'd") AND (cat:math.NT OR cat:math.CO OR cat:math.OC OR cat:math.MG OR cat:math.PR OR cat:math.CA OR cat:math.NA)`*

Review and `/wiki-ingest <arxiv-url>` any that look relevant. If none fit, close the question with `status: superseded` and a one-line explanation.

*(no results; broaden the search terms or query the web)*
