# Record-campaign input set (Goal 0 audit)

**Drafted:** 2026-06-02 · **Author:** agent · **Branch:** `js/feat/autonomous-record-campaign`

The autonomous record campaign (the 24/7 full-stack loop) does **not** attack
all 23 problems. This page is the audited **input set** — the problems the
launchd-driven `autonomous_loop.py` should spend cycles on. Goals 1–4 of this
branch operate over exactly this set.

## Inclusion criteria

A problem is in the campaign input set iff **all three** hold:

- **(a) Manifest wired** — has a dispatch entry in
  `src/einstein/optimizer_manifest.yaml` (the loop can produce a real,
  triple-verified score, not `dispatch: no-manifest-entry`).
- **(b) Headroom** — `rank-current ≥ #2` (a record is still available to take)
  **OR** at least one `status: open` question in `docs/wiki/questions/`.
- **(c) Not closed** — not `retired`, and not operator-excluded via
  `in_active_queue: false`.

Manifest-wired ids (source: `optimizer_manifest.yaml`):
`{2, 4, 5, 11, 14, 15, 16, 18, 19, 22}`.

## Audit table

| P | name | status | rank≥#2? | open Q? | in queue? | verdict |
|---|---|---|---|---|---|---|
| 5  | min-distance-ratio    | rank-4-frozen | ✅ | — | ✅ | **IN** |
| 11 | tammes-n50            | rank-2-frozen | ✅ | ✅ (1) | ✅ | **IN** |
| 14 | circle-packing-square | rank-2-frozen | ✅ | ✅ (3) | ✅ | **IN** |
| 15 | heilbronn-triangles   | frozen (not #1) | ✅ | — | ✅ | **IN** |
| 19 | difference-bases      | shelved | ✅ | ✅ (3) | ✅ | **IN — flagged** |
| 2  | first-autocorrelation | conquered (#1) | ❌ | ❌ (all answered) | ✅ | OUT — we hold #1 |
| 4  | third-autocorrelation | conquered (#1) | ❌ | ❌ | ✅ | OUT — we hold #1 |
| 18 | circles-rectangle     | conquered (#1) | ❌ | ❌ | ✅ | OUT — we hold #1 |
| 16 | (anomalous frontmatter) | — | — | — | ❌ | OUT — not in active queue |
| 22 | kissing-d12           | rank-3 | ✅ | ❌ | ❌ | OUT — `in_active_queue: false` |

`open Q?` counts only `status: open` questions (answered questions don't create
headroom). P2 has three question files but all are answered.

## Campaign input set

```
P5  min-distance-ratio       (rank-4-frozen)
P11 tammes-n50               (rank-2-frozen, 1 open Q)
P14 circle-packing-square    (rank-2-frozen, 3 open Q)
P15 heilbronn-triangles      (frozen)
P19 difference-bases         (shelved, 3 open Q — see flag)
```

Five problems. `--max-problems 3` per 30-min invocation (Goal 1) means the loop
visits the highest-priority 3 of these per tick; tier/score ordering inside
`autonomous_loop.py` decides which.

## Judgment calls (review at merge)

1. **P19 is `shelved`.** The loop's `is_active()` only filters `retired`, so
   shelved problems remain in the queue, and P19's three open questions satisfy
   criterion (b). But `shelved` is a human signal of deprioritization. Included
   here because the open questions are live research seeds; flag for operator to
   override via `in_active_queue: false` if P19 should stay parked.
2. **Strict vs. loose "manifest wired".** This audit uses the **strict** reading
   — an entry in `optimizer_manifest.yaml`. Several rank-≥#2 problems in the
   active queue (P1 erdos-overlap, P10 thomson-n282, P12 flat-polynomials) have
   real headroom but **no manifest entry**, so they're excluded by (a). If the
   campaign should also attack those, the fix is to wire their manifest entries
   first (a separate sprint), not to loosen this criterion.
3. **Conquered ≠ done forever.** P2/P4/P18 are excluded only because we hold #1
   with no open question. A new open question on any of them re-admits it.
