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
- **goal 7** — techniques pass: shred mb/wiki/knowledge.yaml (56KB) into wiki/techniques/ (27 files); cross-problem-lessons-gpu.md → wiki/techniques/gpu-decision-framework.md.
- **goal 7.5** — sanitization + mission reframe: removed alpha_omega context from findings (per resolved competition); rewrote mb/wiki/* citations to post-refactor paths; rewrote home.md with "math is the verifiable system, agent is the subject, wiki is the artifact, biological-evolution-like compounding" framing.
- **goal 8** — concepts pass: 30 wiki/concepts/*.md durable mental models, mined from problem-N-*/strategy.md and findings; bidirectional cross-links with techniques/ and findings/ deferred to lint.
- **goal 9** — tracking move: 23 problem-N-* dirs migrated from mb/wiki/ to mb/tracking/; 22 problem index pages authored in cb/wiki/problems/ (P8/P20 don't exist; 17/18 splits); mb/.claude/CLAUDE.md rewritten.
- **goal 10** — delete mb/wiki/: removed entirely after verifying all content migrated. Private historicals preserved as mb/branch-summaries-historical.md and mb/log-historical.md. Rollback tag: `mb:pre-refactor`.
- **goal 11** — qmd collections wired: `einstein-wiki` (136 docs over wiki/) and `einstein-wiki-source` (45 docs over source/) registered; embeddings generated (414 chunks). Sample query "Cohn-Elkies LP bound" returns wiki/personas/cohn.md (93%) + wiki/concepts/lp-duality.md (92%).
- **2026-05-02 lint pass (post P19 cycles 1-4)** — 145 pages total. Resolved 3 concept↔finding name collisions (basin-rigidity, float64-ceiling, k-climbing): findings now point at concepts via `synthesized_into:` frontmatter + header note. Index staleness caught: 11 docs from this branch were unindexed; refreshed via `tools/refresh_qmd.sh` (now part of cycle-discipline). Orphans: 7 problem index pages (by design — entry points) + 2 newest dead-end findings (will gain incoming). 0 broken cites detected. `cycle-discipline.md` updated: REFUSE to start cycle without qmd query; REFUSE to end cycle without `tools/refresh_qmd.sh`.
