---
type: queue
author: hybrid
drafted: 2026-05-28
cites: [docs/wiki/problems/_inventory.md]
---

# Active problem queue

JSAgent's current attempt set. **This page is a curated view; the source of truth is the per-problem frontmatter flag `in_active_queue: true|false` (default: true).** Edit a problem page to change the queue; do not edit this list alone.

## How it gates the agent

| System | Reads the flag? | Mechanism |
|---|---|---|
| `scripts/autonomous_loop.py` | ✅ direct | `is_active()` checks `extra.get("in_active_queue")`; sorted, dispatched by `build_queue()`. Skipped if `false`, `no`, `0`, `off`. |
| `scripts/meta_loop.py` | inherited | reads `docs/agent/cycle-log.md` + `skill-library.md`; only sees problems that the autonomous loop ran. No standalone queue. |
| `scripts/research_synthesis.py` | inherited | takes `--problem-id` from the orchestrator (autonomous_loop); not invoked standalone in cycles. |
| `scripts/research_synthesis_shadow.py` | inherited | forks worktrees + runs autonomous_loop cycles per arm. Honors the flag in each arm. |

`retired` `status` still skips (5 dead pages). The flag is independent of `status` — P6 keeps `status: conquered`, P22 keeps `status: rank-3`; only the queue flag is `false`.

## Queue (15 problems)

| ID | Title | Inventory status | Inventory tier |
|---|---|---|---|
| P1 | Erdős Minimum Overlap | #2, frozen | C |
| P2 | First Autocorrelation | #3, displaced (gap −1.84e-7) | S |
| P3 | Second Autocorrelation | #3, displaced (gap +4.30e-4) | S |
| P4 | Third Autocorrelation | #2, displaced (gap −2.17e-4) | S |
| P5 | Min Distance Ratio | #4, frozen | B |
| P7 | Prime Number Theorem | #1, conquered | A |
| P9 | Uncertainty Principle | #1 local, hidden | A |
| P10 | Thomson Problem n=282 | #5, frozen | B |
| P11 | Tammes Problem n=50 | #2, basin-locked | B |
| P12 | Flat Polynomials | #8, local opt | B |
| P13 | Edges vs Triangles | #1 local, blocked | S |
| P14 | Circle Packing in Square | #2, basin-locked | B |
| P15 | Heilbronn Triangles | frozen, tied | C |
| P17b | Circles in Rectangle (arena ID 18) | #1, sole | A |
| P19 | Difference Bases | 7-way tie, shelved | S |

## Excluded (6 problems)

| ID | Title | How excluded | Reason |
|---|---|---|---|
| P6 | Kissing Number d=11 | `in_active_queue: false` | terminal-min (score 0.0 = theoretical minimum; κ(11)≥594 proven) |
| P16 | Heilbronn Convex | `status: retired` (filename `retired-16-*`) | already retired 2026-05-23 |
| P17a | Hexagon Packing | `status: retired` (filename `retired-17-*`) | already retired |
| P21 | Lean Sum Formula | `status: retired` (filename `retired-21-*`) | already retired |
| P22 | Kissing Number d=12 | `in_active_queue: false` | arena-unavailable (human review 2026-05-28); rank-1 also structurally infeasible |
| P23 | Kissing Number d=16 | `status: retired` (filename `retired-23-*`) | already retired (κ(16)=4320 proven, Levenshtein 1979) |

## Changing the queue

To **remove** a problem from the queue, edit its frontmatter:
```yaml
in_active_queue: false
queue_exclusion_reason: <short tag — terminal-min, arena-unavailable, etc.>
queue_excluded_at: YYYY-MM-DD
```

To **re-add**, delete the flag or set `in_active_queue: true`. Then update this page's tables to reflect the change.

## Provenance

- Source: [`_inventory.md`](_inventory.md) (2026-05-02).
- Curation: human decision on 2026-05-28 — excluded P6 (terminal-min) + P22 (arena-unavailable). P16/P17a/P21/P23 were already retired.
- Inventory ranks/scores may have drifted since 2026-05-02; cross-check via `check_submission.check_leaderboard(problem_id)` before launching a cycle.

See also: [`autonomous_loop.is_active`](../../../scripts/autonomous_loop.py), [`test_is_active_in_active_queue_flag`](../../../tests/scripts/test_autonomous_loop.py).
