# Cycle log — append-only

Every problem-attempt cycle gets one row. Failures count. Cherry-picking is forbidden by `.claude/rules/cycle-discipline.md`.

## Schema

| Column | Notes |
|---|---|
| `cycle_id` | sequential integer |
| `problem` | P{id}-{slug} |
| `start_score` | best score we held entering the cycle (or `none` for first attempt) |
| `end_score` | best score after the cycle |
| `hours` | wall-clock spent on the cycle (rough; cap at 100h) |
| `compute` | local-cpu / local-mps / modal / mixed |
| `wiki_citations` | # of wiki/ pages we cited during the cycle |
| `findings_added` | # of new wiki/findings/ pages produced |
| `concepts_added` | # of new wiki/concepts/ pages produced |
| `author_mix` | agent/human/hybrid counts |
| `outcome` | conquered / improved / no-change / new-finding-no-improvement / blocked |
| `notes` | one-line gloss |

## Cycles

| # | problem | start → end score | hours | compute | wiki cites | findings+ | concepts+ | author mix | outcome | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | refactor | (n/a)              | ~10  | local-cpu | (n/a) | 25 migrated + 27 techniques + 30 concepts + 22 personas + 22 problem indices | (rebuild) | a:79/h:1/hyb:0 | bootstrap | `js/refactor/wiki-bootstrap` — wiki rebuilt as public artifact in cb/. mb shrunk to tracking. Goals 0-13. |

## Cycle 1 onward

Starts when the first new problem is attempted post-merge. Cycle 1 will be a Tier-S problem from `wiki/problems/_inventory.md`; the bootstrap friction log identified P19 (Difference Bases) as the natural first target — questions already filed.

*This file is append-only. Edits to past rows require a separate `corrigendum:` row referencing the original `cycle_id`.*
