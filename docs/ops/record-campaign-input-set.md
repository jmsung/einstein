# Record-campaign input set (Goal 0 audit)

**Drafted:** 2026-06-02 · **Author:** agent · **Branch:** `js/feat/autonomous-record-campaign`

---

## 2026-06-04 re-audit (Phase 6 — `js/feat/headroom-target-set`, Goal 6)

The Phase-4 input set below (5 converged problems) yielded **0 records** — the
engine was sound, the input set was the bottleneck. Phase 6 fixed both sides of
the criterion:

- **Manifest now wired for the headroom targets.** `optimizer_manifest.yaml` ids
  are now `{1, 2, 3, 4, 5, 10, 11, 12, 14, 15, 16, 18, 19, 22}` — Phase 6 added
  **P1, P3, P10, P12** (P2/P4 already had entries). Every new entry landed with a
  `verify_seed` SPEC + a triple-verify registration (registry-coverage CI gate).
  → **Judgment call #2 below is resolved** (P1/P10/P12 are no longer
  manifest-excluded).
- **Triple-verify is now real.** Phase 5 (PR #116) replaced the hardcoded
  `passed=False` with `triple_verify.run_payload` (`autonomous_loop.py:859`), so
  gate 2 can pass — the auto-submit gate-flip is no longer a structural no-op.

**New input set (11 problems)** — `in_active_queue: true` ∩ manifest-wired ∩
(rank ≥ #2 OR open question OR tied-SOTA-we-keep):

| P | name | standing (2026-06-03 audit) | seed |
|---|---|---|---|
| 1  | erdos-overlap        | #2 tied-SOTA (gap ~0)        | 0.38087031048 (ours) |
| 2  | first-autocorrelation| #3, gap −1.84e-7 (tight)     | existing |
| 3  | second-autocorrelation| #3, gap +4.30e-4           | 0.96227 (100k, ours) |
| 4  | third-autocorrelation| #2, gap −2.17e-4            | existing |
| 5  | min-distance-ratio   | #4 frozen                    | Cantrell (22,8) |
| 10 | thomson-n282         | #6, gap +0.231               | Wales global-min (ties #1) |
| 11 | tammes-n50           | #3 float64-tied              | Hardin-Sloane |
| 12 | flat-polynomials     | #9, gap +0.073               | arena-SOTA (grid-drift caveat) |
| 14 | circle-packing-square| #1 we lead                   | ours |
| 15 | heilbronn-triangles  | tied-SOTA                    | AlphaEvolve §6.48 |
| 19 | difference-bases     | 7-way SOTA tie               | Kronecker |

**Honest expectation: still 0 submissions from a *Phase-6* campaign.**
`verify_seed` only re-scores a fixed seed — it cannot beat a record. The seeds
above tie #1 (P10/P12/P15/P19), sit sub-`minImprovement` below #1 (P1), or sit
behind #1 (P2/P3/P4 — new-basin gaps). A submittable Δ requires running the
real optimizers, which is **Phase 7** (`js/feat/strategy-attempts-headroom`).

### Next campaign trigger condition

> **Re-run the live campaign (consider `AUTO_SUBMIT=1`) only after Phase 7 lands
> a strategy attempt that produces a triple-verified candidate beating arena #1
> by ≥ `minImprovement` on a headroom target.** Until then a live run is safe
> (gates hold) but pointless (no record is reachable by re-scoring seeds).

### Seed-visibility rule (decided 2026-06-04)

Seeds live in **public cb** by default (matches the 8 pre-existing seeds +
`verify_seed`'s self-contained design; einstein has no secret-methodology
layer). **Exception:** a seed that represents a *novel record not yet submitted*
stays **private (mb-only)** until its record is submitted, to avoid publishing
an unsubmitted record. None of the current seeds qualify (all are public-domain,
tied, or sub-SOTA).

---

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
