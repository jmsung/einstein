---
type: question
author: agent
drafted: 2026-06-12
status: open
asked_by: gap-detector
related_pages: [concepts/uncertainty-principle.md, findings/tool-autosynthesis-design.md]
gap_type: type-2-missing-connection
similarity: 0.80
---

# Connection gap: `concepts/uncertainty-principle.md` ↔ `findings/tool-autosynthesis-design.md`

## Question

qmd reports semantic similarity 0.80 between these two pages, but there is no explicit citation in either direction. What is the missing connection?

## Why it matters

Per `docs/wiki/findings/finding-the-fertile-gaps.md`: pages with high semantic similarity but no explicit link likely share an underlying concept that hasn't been articulated. Either:

1. The connection is real and a bridge page should be authored, OR
2. The similarity is superficial (qmd false-positive) and we should note that.

## Next step

Read both pages. If a structural connection exists, file as `docs/wiki/findings/<bridge-slug>.md`. If not, close this question with `status: superseded` and a one-line explanation.

## Suggested sources

*Auto-suggested by `docs/tools/gap_search.py` — arxiv query: `(all:"Connection gap `concepts uncertainty-principle.md` ↔ `findings") AND (cat:math.NT OR cat:math.CO OR cat:math.OC OR cat:math.MG OR cat:math.PR OR cat:math.CA OR cat:math.NA)`*

Review and `/wiki-ingest <arxiv-url>` any that look relevant. If none fit, close the question with `status: superseded` and a one-line explanation.

*(no results; broaden the search terms or query the web)*
