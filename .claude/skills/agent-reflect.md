---
description: Run the close-of-cycle reflection. After a problem cycle ends, distill what worked / failed / generalized into wiki entries, append a row to agent/cycle-log.md, update agent/skill-library.md citation counts. Enforces .claude/rules/cycle-discipline.md.
---

# /agent-reflect — close-of-cycle reflection

Run at the end of every problem cycle (typically inside `/worktree-done` distill). Produces:

1. One row appended to `agent/cycle-log.md`
2. Updated `agent/skill-library.md` citation counts
3. Any new `wiki/findings/` (positive or dead-end) authored
4. Any new `wiki/concepts/` (if a finding is invoked across 3+ problems)
5. Wiki questions closed (status: open → answered, with `answer_finding:`)

## Procedure

1. **Identify the cycle**: branch name, problem ID, start/end scores, hours, compute used.

2. **Structured reflection** — answer in writing (in the branch tracking file):
   - **What worked?** which technique(s) + why
   - **What failed?** which technique(s) + WHY (the obstruction)
   - **What would I try differently?** the next-step delta
   - **What wiki page would have made this faster?** (gap-detect signal — file as a question)
   - **What wiki page should NOW exist?** (post-hoc finding/concept proposal)

3. **Author wiki entries**:
   - For each "what failed + why" answer → `wiki/findings/dead-end-<slug>.md` (per failure-is-a-finding rule)
   - For each generalizable insight → `wiki/findings/<slug>.md` or, if cited 3+ times, `wiki/concepts/<slug>.md`
   - For each unanswered question → `wiki/questions/<YYYY-MM-DD>-<slug>.md` (status: open)

4. **Update tracking**:
   - Append cycle row to `agent/cycle-log.md` (per cycle-discipline rule)
   - Increment `tried` / `top3` / `finding` counts in `agent/skill-library.md`

5. **Close any in-flight questions** that this cycle answered:
   - Set frontmatter `status: answered`, `answered_at: <date>`, `answer_finding: <path>`

6. **Honesty checks** before completing:
   - Every `author:` field on new pages is set correctly
   - Every abandoned approach has a dead-end finding
   - The cycle row reflects reality, including failures

## Output

Print:
- Cycle log row (so user can verify)
- List of wiki entries authored
- List of skill-library updates
- List of questions closed
- Honesty-check summary

## Refusal

This skill REFUSES to mark complete if:
- Any abandoned approach lacks a dead-end finding (failure-is-a-finding violation)
- The cycle log row is missing
- Any agent-authored wiki page lacks `author: agent` frontmatter

These refusals are by design — they enforce `cycle-discipline.md`.

## Status

Stub authored 2026-05-02 — Goal 13. Promote to a real skill once the loop has run on 1-2 actual problems and the pattern stabilizes.
