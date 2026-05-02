# Cycle discipline — every cycle logged, no cherry-picking

Every problem-attempt cycle MUST produce one row in `agent/cycle-log.md`. Failures count. Cherry-picking is forbidden.

**Why:** The whole `agent/` layer — `cycle-log.md`, `skill-library.md`, `metrics.md`, `ablations/` — measures whether the agent actually self-improves. Without strict 1:1 cycle:log discipline, the metric becomes "best-of-N selected log" which is theatrically self-improving without being actually so. Honesty over optics.

This rule is the structural enforcement of the four honesty checks (`agent/README.md` → "Why this layer exists").

**How to apply:**

At end of every `/worktree-done`, before merging:

1. **Append exactly one row** to `agent/cycle-log.md` for the cycle. Schema in the file header. Failures and abandons count — note `outcome: blocked | no-change | new-finding-no-improvement` as appropriate.
2. **Update `agent/skill-library.md`** for every technique invoked during the cycle: increment `tried`; increment `top3` if the cycle reached top-3 on the problem; increment `finding` if the cycle produced any new wiki finding (positive OR dead-end).
3. **Verify `author:` fields** on every wiki page touched/added in the cycle. The mix is the self-improvement signal.
4. **Failure-finding obligation** — if any approach was abandoned during the cycle, `wiki/findings/dead-end-<slug>.md` must exist for it. If not, block the worktree-done step.

**Anti-patterns explicitly forbidden:**

- Editing past `cycle-log.md` rows (use `corrigendum:` row instead).
- "Forgetting" to log a cycle that didn't go well.
- Logging only the wiki entries that look impressive while skipping the failures.
- Marking `author: hybrid` without genuine bilateral content (e.g., human only typed "ok" — that's `author: agent`).

**Triggering pattern:** end of every `/worktree-done`. The skill should refuse to complete if `cycle-log.md` wasn't appended.

See also: [agent/README.md](../../agent/README.md), [failure-is-a-finding](failure-is-a-finding.md), [wiki-attribution](wiki-attribution.md).
