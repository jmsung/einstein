# Promotion log

Append-only record of finding→concept promotions. A finding becomes a concept when it's cited 3+ times across other wiki pages OR invoked across 3+ distinct problems. Promotion is **human-gated** (per `knowledge/wiki/CLAUDE.md` line 41).

Why this log exists: without a trail, "promotion happened" is unverifiable, and the wiki silently leaks high-leverage findings that should have graduated. The cycle-log measures cycle-level work; this log measures wisdom compounding.

## Schema

| Date | Source finding | New concept | Cite count at promotion | Rationale | Approver |
|------|---------------|-------------|-------------------------|-----------|----------|

## Entries

*(No promotions yet. First row to be added at the next cycle-end where `docs/agent/skill-library.md` shows a finding with `tried ≥ 3` AND citations across ≥3 problems.)*

## How to add a row

1. At cycle-end, scan `docs/agent/skill-library.md` for findings with high `tried`/`finding`/`top3` counts.
2. Cross-reference: how many distinct problems cite the finding? Use `qmd query "<finding>" -c einstein-wiki`.
3. If ≥3 distinct problems → eligible.
4. Human reviews: read the finding, read the proposed concept page draft.
5. Append a row here. Author the concept page. Update the finding's frontmatter with `promoted_to: <concept-path>`.

## Anti-patterns

- Promoting agent-drafted findings without human review.
- Promoting findings cited by only the same agent thread (echo chamber — not real cross-problem use).
- Editing past rows (use a new row with `corrigendum:` if a prior promotion needs revision).
