---
type: question
author: agent
drafted: 2026-06-12
status: open
asked_by: gap-detector
related_pages: [findings/dead-end-newton-max-strict-tol-lockout-p14.md, findings/p14-manifest-wired-slsqp-polish.md]
gap_type: type-2-missing-connection
similarity: 0.64
---

# Connection gap: `findings/dead-end-newton-max-strict-tol-lockout-p14.md` ↔ `findings/p14-manifest-wired-slsqp-polish.md`

## Question

qmd reports semantic similarity 0.64 between these two pages, but there is no explicit citation in either direction. What is the missing connection?

## Why it matters

Per `knowledge/wiki/findings/finding-the-fertile-gaps.md`: pages with high semantic similarity but no explicit link likely share an underlying concept that hasn't been articulated. Either:

1. The connection is real and a bridge page should be authored, OR
2. The similarity is superficial (qmd false-positive) and we should note that.

## Next step

Read both pages. If a structural connection exists, file as `knowledge/wiki/findings/<bridge-slug>.md`. If not, close this question with `status: superseded` and a one-line explanation.

## Suggested sources

*Auto-suggested by `docs/tools/gap_search.py` — arxiv query: `(all:"Connection gap `findings dead-end-newton-max-strict-tol-lockout-p14.md` ↔ `findings") AND (cat:math.NT OR cat:math.CO OR cat:math.OC OR cat:math.MG OR cat:math.PR OR cat:math.CA OR cat:math.NA)`*

Review and `/wiki-ingest <arxiv-url>` any that look relevant. If none fit, close the question with `status: superseded` and a one-line explanation.

*(no results; broaden the search terms or query the web)*
