# Cycle discipline — every cycle logged, no cherry-picking

Every problem-attempt cycle MUST produce one row in `agent/cycle-log.md`. Failures count. Cherry-picking is forbidden.

**Why:** The whole `agent/` layer — `cycle-log.md`, `skill-library.md`, `metrics.md`, `ablations/` — measures whether the agent actually self-improves. Without strict 1:1 cycle:log discipline, the metric becomes "best-of-N selected log" which is theatrically self-improving without being actually so. Honesty over optics.

This rule is the structural enforcement of the four honesty checks (`agent/README.md` → "Why this layer exists").

**How to apply:**

### At cycle START (per `wiki-first-lookup` rule, made REFUSING):

0. **REFUSE to start the cycle without at least one `qmd query`** against `einstein-wiki` (and optionally `einstein-wiki-source`). The agent's first tool call after reading the problem statement must be `qmd query "<question>" -c einstein-wiki -n 5`. No exceptions. The rationale: the failure mode is "I think I remember the prior strategy, so I skip the wiki" — that's exactly what produces drift and re-derivation. Even if you have the strategy.md loaded in context, the qmd query may surface findings/concepts/personas that strategy.md doesn't reach. Treat the qmd query as a *correctness check on memory*, not a search-because-stuck.

### During the cycle:

1. **Author with attribution** — every new wiki page gets `author: agent | human | hybrid` frontmatter (per `wiki-attribution.md`).
2. **File failure findings** — every abandoned approach immediately gets a `wiki/findings/dead-end-<slug>.md` (per `failure-is-a-finding.md`).

### At cycle END (per `/worktree-done` or `/agent-reflect`):

3. **Run `tools/refresh_qmd.sh`** before any merge. The qmd index does NOT auto-detect new files; without refresh, the NEXT cycle can't query this cycle's findings — silently breaks the wiki-first discipline. Refusal: don't mark cycle complete if qmd is stale.
4. **Append exactly one row** to `agent/cycle-log.md` for the cycle. Schema in the file header. Failures and abandons count — note `outcome: blocked | no-change | new-finding-no-improvement` as appropriate.
5. **Update `agent/skill-library.md`** for every technique invoked during the cycle: increment `tried`; increment `top3` if the cycle reached top-3 on the problem; increment `finding` if the cycle produced any new wiki finding (positive OR dead-end).
6. **Verify `author:` fields** on every wiki page touched/added in the cycle. The mix is the self-improvement signal.
7. **Failure-finding obligation** — if any approach was abandoned during the cycle, `wiki/findings/dead-end-<slug>.md` must exist for it. If not, block the worktree-done step.

**Anti-patterns explicitly forbidden:**

- Editing past `cycle-log.md` rows (use `corrigendum:` row instead).
- "Forgetting" to log a cycle that didn't go well.
- Logging only the wiki entries that look impressive while skipping the failures.
- Marking `author: hybrid` without genuine bilateral content (e.g., human only typed "ok" — that's `author: agent`).
- **Skipping the cycle-start qmd query** because "I already have strategy.md loaded." This was the dominant violation in the first session post-refactor (cycles 2-4 of P19 skipped qmd; cycle 1 used it). The query is mandatory regardless of context state.
- Ending a cycle without running `tools/refresh_qmd.sh` — produces silent stale-index drift.

**Triggering pattern:** end of every `/worktree-done`. The skill should refuse to complete if `cycle-log.md` wasn't appended.

See also: [agent/README.md](../../agent/README.md), [failure-is-a-finding](failure-is-a-finding.md), [wiki-attribution](wiki-attribution.md).
