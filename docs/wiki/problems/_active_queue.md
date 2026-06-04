---
type: queue
author: hybrid
drafted: 2026-05-28
updated: 2026-06-04
cites: [docs/wiki/problems/_inventory.md, mb/logs/leaderboard-audit-2026-06.md]
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

## Queue (11 problems) — refreshed 2026-06-04 (Phase 6)

Verified live against `autonomous_loop.py --queue-only`. Phase 6
(`headroom-target-set`) re-enabled 6 problems (P1/P2/P3/P4/P10/P12), all now
wired in `optimizer_manifest.yaml` + `verify_seed` SPECS + triple-verify.

| ID | Title | Standing (2026-06-03 audit) | Tier | Phase-6 change |
|---|---|---|---|---|
| P1 | Erdős Minimum Overlap | #2, tied-SOTA (gap ~0) | C | **re-enabled + wired** (seed 0.38087031048) |
| P2 | First Autocorrelation | #3, displaced (gap −1.84e-7) | S | **re-enabled** (was Phase-4 scope-out) |
| P3 | Second Autocorrelation | #3, displaced (gap +4.30e-4) | S | **re-enabled + wired** (seed 0.96227, 100k) |
| P4 | Third Autocorrelation | #2, displaced (gap −2.17e-4) | S | **re-enabled** (was Phase-4 scope-out) |
| P5 | Min Distance Ratio | #4, frozen (gap +2.5e-10) | B | (Phase-4 five) |
| P10 | Thomson Problem n=282 | #6, behind (gap +0.231) | B | **re-enabled + wired** (Wales global-min seed, ties #1) |
| P11 | Tammes Problem n=50 | #3, float64-tied | B | (Phase-4 five) |
| P12 | Flat Polynomials | #9, behind (gap +0.073) | B | **re-enabled + wired** (arena-SOTA seed; grid-drift caveat) |
| P14 | Circle Packing in Square | #1, we lead | B | (Phase-4 five) |
| P15 | Heilbronn Triangles | tied SOTA (not on board) | C | (Phase-4 five) |
| P19 | Difference Bases | 7-way SOTA tie (not on board) | S | (Phase-4 five) |

## Excluded / parked (in_active_queue: false or retired)

| ID | Title | How excluded | Reason |
|---|---|---|---|
| P6 | Kissing Number d=11 | `in_active_queue: false` | terminal-min (score 0.0 = theoretical minimum; κ(11)≥594 proven) |
| P7 | Prime Number Theorem | `in_active_queue: false` | NEW headroom found 2026-06-03 (gap −5.35e-5, rank #2) — deferred to Phase 7, not wired ([question](../questions/2026-06-03-headroom-p7-p13-not-in-plan.md)) |
| P9 | Uncertainty Principle | `in_active_queue: false` | we lead (#1 local) — no work needed |
| P13 | Edges vs Triangles | `in_active_queue: false` | NEW headroom found 2026-06-03 (gap −2.88e-5, rank #8) — deferred to Phase 7, not wired |
| P18 | Circles in Rectangle (arena ID 18) | `in_active_queue: false` | we lead (#1) — frozen, no submittable Δ |
| P22 | Kissing Number d=12 | `in_active_queue: false` | arena-unavailable (human review 2026-05-28); rank-1 also structurally infeasible |
| P16 | Heilbronn Convex | `status: retired` (filename `retired-16-*`) | already retired 2026-05-23 |
| P17a | Hexagon Packing | `status: retired` (filename `retired-17-*`) | already retired |
| P21 | Lean Sum Formula | `status: retired` (filename `retired-21-*`) | already retired |
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
- **2026-06-04 (Phase 6, `headroom-target-set` Goal 5):** queue re-scoped 5 → 11. Re-enabled P1/P2/P3/P4/P10/P12 (all newly wired with manifest + verify_seed + triple-verify). The prior "15 problems" list was stale/aspirational — P7/P9/P13/P18 were `in_active_queue: false` and are corrected here. Standings from the [2026-06-03 leaderboard audit](../../../../mb/logs/leaderboard-audit-2026-06.md).
- Ranks/scores drift; cross-check via `check_submission.check_leaderboard(problem_id)` before launching a cycle.

See also: [`autonomous_loop.is_active`](../../../scripts/autonomous_loop.py), [`test_is_active_in_active_queue_flag`](../../../tests/scripts/test_autonomous_loop.py).
