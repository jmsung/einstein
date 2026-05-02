---
type: log
author: human
drafted: 2026-05-02
---

# Wiki ops log

Append-only record of wiki ingests, promotions, lints, and structural changes.

## 2026-05-02

- **bootstrap** — wiki/ rebuilt from scratch under cb/. Migration from mb/wiki/ underway via `js/refactor/wiki-bootstrap` branch. Snapshot tags: `cb:pre-wiki`, `mb:pre-refactor`. See `mb/tracking/active/js-refactor-wiki-bootstrap.md` for design context.
- **inventory** — `wiki/problems/_inventory.md` authored as project compass (23 problems × concepts × coverage × tier). Author: agent (Explore subagent), human-confirmed.
- **goal 2** — bootstrap: cb/CLAUDE.md, wiki/CLAUDE.md, scaffolds for concepts/techniques/personas/findings/problems/questions, .claude/CLAUDE.md, raw/+source/ subdirs.
- **goal 3** — 10 behavioral rules + slim 4-axiom file in `.claude/rules/`.
- **goal 4** — personas pass: 22 files (16 council + 5 new + _synthesis). Source: mb/wiki/mathematician-council.md.
- **goal 5** — findings pass: 25 files migrated from mb/wiki/findings/ + arena-scoring.md (renamed from arena-scoring-investigation). Frontmatter updated with type/author/drafted; cites still reference old paths (rewritten in Goal 6).
- **goal 6** — references pass: 44 .md files from mb/wiki/reference/ split by provenance into source/{papers/(38), repos/(2), blog/(4)}. 24 PDFs copied to raw/papers/ (gitignored). Cites in findings/ and source/ rewritten from `reference/<x>` → `../source/<provenance>/<x>` paths.
