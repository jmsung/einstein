---
type: question
author: agent
drafted: 2026-05-02
status: answered
asked_by: human
related_problems: []
answered_at: 2026-05-02
---

# Goal-12 smoke test: does the new self-improvement loop produce wiki entries without manual hand-holding?

## Question

Goal 12 of the wiki refactor is the first cycle smoke test. Pick a Tier-S problem (chose P19 Difference Bases — has the Kronecker concept already authored, has a 7-way tie wall to dent, and is small enough to validate the loop without burning Modal hours). Dispatch a mini council. Verify the loop produces `wiki/questions/` entries with proper frontmatter and cross-links, ready for a follow-up cycle to actually run the research.

## Answer

**Yes, with friction observations below.** Three council questions filed:

1. `2026-05-02-p19-kronecker-w4-existence.md` — Gauss persona; tactical (enumerate 5-mark Sidon rulers).
2. `2026-05-02-p19-structural-cap-conjecture.md` — Cohn persona; structural (LP/SDP dual certificate).
3. `2026-05-02-p19-finite-field-construction.md` — Ramanujan persona; algebraic (Singer / Bose-Chowla / Paley / LPS).

Each question has frontmatter `author: agent`, `asked_by: <persona>`, `related_problems`, `related_concepts`, `status: open`. Body has Question + Why-it-matters + Hypotheses + Next-step + References.

## Friction observations (for Goal 13 refinement)

1. **Council dispatch needs a cleaner trigger** — manually wrote 3 questions in the persona voices; need a `/council-dispatch <problem>` shortcut that auto-spawns parallel research subagents seeded with each persona page, problem statement, and SOTA. Currently dispatch is hand-orchestrated.
2. **Question-finding link is implicit** — no automatic mechanism to detect when a question gets answered (need lifecycle: open → research-active → answered with `answer_finding:` populated). Currently a wiki-lint follow-up.
3. **No `cycle-log.md`** — Goal 13 should add `cb/agent/cycle-log.md` to track agent-authored questions/findings/concepts per cycle (the self-improvement metric).
4. **Compute-router not yet implemented** — `tools/compute_router.py` is referenced in `wiki/techniques/compute-router.md` but is TBD. Goal 13 builds it.
5. **Skill ergonomics** — `/wiki-query` works (qmd is wired), but the chain `gap-detect → file-question → research → distill-finding → cite-back` is multi-step manual. Goal 13 sketches `/agent-reflect` to formalize the cycle close.
6. **Sanitization for public wiki** worked but was a manual pass — Goal 13 may want a `tools/lint-public.py` that grep-rejects competitor names + private params + Modal billing on cb/ pre-commit (low priority since the partition already enforces it).

## Verdict

The architecture is sound. The friction is in the *ergonomics of running the loop*, not in the loop's design. Goal 13 addresses each friction point.
