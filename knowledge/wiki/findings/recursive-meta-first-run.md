---
type: finding
author: agent
drafted: 2026-05-28
question_origin: branch-js-feat-recursive-meta
status: pending-first-run
related_concepts: []
related_techniques: []
related_personas: []
cites:
  - recursive-meta-design.md
  - meta-loop-design-from-literature.md
  - meta-loop-swap-surface.md
  - ../../domains/ai-agents/source/2026-zhang-hyperagents.md
  - ../../domains/ai-agents/source/2025-zhang-darwin-godel-machine-open-ended.md
---

# Recursive meta-loop first run — scaffold + synthetic dogfood

## Status: pending the first real overnight run

This page mirrors the scaffold pattern established by
[`meta-loop-first-run.md`](meta-loop-first-run.md). G0–G5 of
`js/feat/recursive-meta` shipped the *machinery* for `meta_self_edit`;
this page documents the **synthetic dogfood** that exercises every code
path end-to-end, and reserves space for the **real first-run** results
the operator will fill in after `scripts/meta_loop.py` accumulates ≥10
cycles of audit-log data.

The honesty check (per [`cycle-discipline.md`](../../../.claude/rules/cycle-discipline.md)
and [`self-improvement-loop.md`](../../../.claude/rules/self-improvement-loop.md)):
no real cycles have run yet — the audit log is empty. The G6 commit
therefore lands two artifacts:

1. The synthetic dogfood evidence below (runs the whole pipeline against
   a hand-crafted ledger; documents the gate-chain works as designed).
2. A `status: pending-first-run` page the operator updates after the
   first real overnight run.

## Synthetic dogfood — pipeline works end-to-end (2026-05-28)

Driver: `/tmp/dogfood_recursive_meta.py` (not committed — a transcripted
demonstration of the production code paths).

Setup: a synthetic `meta-proposals.md` audit log with 11 rows — 4
rejected at `evidence-threshold` for `rule_edit` (the recurring pattern),
7 accepted. This is the minimum shape that should trigger the proposer.

Pipeline:

| step | result |
|---|---|
| `count_audit_rows` | 11 ≥ floor=10 ✓ |
| `detect_recurring_gate_rejection` | `{type: rule_edit, gate: evidence-threshold, count: 4}` ✓ |
| `propose_meta_self_edit` emits | 1 candidate, tagged `proposer_id=recursive-meta-v0`, `target=scripts/meta_loop.py` |
| `Proposal._validate` | passes (schema accepts `meta_self_edit` for `scripts/meta_loop.py`) |
| `evaluate_meta_self_edit_post_shadow` with `arm_a=10 findings, arm_b=0` | decision=**QUEUED** at p=0.001 |
| `mb/meta-self-edit-queue/<ts>-<sha>.md` | written ✓ |
| `mb/meta-loop-snapshots/<ts>-<sha>.py` | written ✓; SHA matches `snapshot_source` |
| `list_queue` | surfaces 1 entry ✓ |
| `apply_queue_entry` | tested in `test_recursive_meta_queue.py` (not run in dogfood — would mutate `scripts/meta_loop.py`) |

What this confirms:

- **Floor + pattern detection both required.** A ledger with 11 rows but
  no recurring pattern returns `[]` from the proposer (per
  `test_proposer_returns_empty_when_floor_met_but_no_pattern`). The
  proposer doesn't emit just because the floor is met.
- **Schema scope-whitelist holds.** Hand-crafted attempts to set
  `target_path` to `src/einstein/...` or `tests/...` are rejected
  (per `test_meta_self_edit_rejects_*`).
- **Post-shadow gate is binomial-statistical, not just directional.**
  A `findings_delta=0.3` shadow with `findings_a=5, findings_b=2`
  passes `a_wins` but FAILS the gate at `p=0.62 >= 0.1` floor
  (per `test_gate_b_rejects_directional_but_high_p`). Only strong
  signals queue.
- **Never auto-merge.** The decision is `QUEUED`, not `ACCEPTED`. No
  diff is applied without a human running `meta_loop queue --apply`.
- **Snapshot precedes queue.** `evaluate_meta_self_edit_post_shadow`
  writes the snapshot BEFORE the queue entry; a snapshot-write failure
  rejects the gate without leaving a queue entry orphaned
  (per `test_gate_a_rejects_below_cycles_floor` and the order in
  `_record` calls).

## What the real first run will measure

When the operator enables `meta_self_edit` in a live meta-loop run and
≥10 cycles of audit data accumulate, this page should be updated with:

### 1. Did `recursive-meta-v0` emit any candidates?

| date | row | proposer_id | type | gate decision | shadow verdict | queued? | applied? |
|---|---|---|---|---|---|---|---|
| (pending) | … | … | meta_self_edit | … | … | y/n | y/n |

Hypothesis from [`recursive-meta-design.md`](recursive-meta-design.md):
the first emitted candidate is likely a *read-only diagnostic addition*
(the simplest-safe edit per the open question
[`questions/2026-05-28-recursive-meta-simplest-safe-edit.md`](../questions/2026-05-28-recursive-meta-simplest-safe-edit.md)).
If the first candidate is instead a *gate-strictness tweak* or
*audit-log column change*, the design finding's hypothesis is wrong —
flag it.

### 2. Did the shadow A/B verdict align with the binomial gate?

If `a_wins=True` but `p >= 0.1` rejected the candidate, the
`META_SELF_EDIT_SHADOW_P_FLOOR=0.1` is doing real work. If every
`a_wins=True` candidate also passed `p < 0.1`, the binomial gate is
redundant — note for future calibration.

### 3. DGM-node-114 adversarial check

Did any candidate trip the `not_worse_on_dead_ends` guard? Did any
*pass* the guard but look suspicious on human review (high findings,
zero dead-ends)? The latter is the partial gap documented in
[`questions/2026-05-28-recursive-meta-dgm-node-114-guard.md`](../questions/2026-05-28-recursive-meta-dgm-node-114-guard.md).

### 4. Cross-check vs. design predictions

| design prediction | actual |
|---|---|
| First candidate is read-only diagnostic | (pending) |
| Shadow p-value threshold catches false positives | (pending) |
| ≥10 cycles is enough — not too tight | (pending) |
| Never auto-merge → all candidates queued for human review | (pending — should be 100%) |
| `mb/meta-loop-snapshots/` accumulates one entry per queued candidate | (pending) |

If the cycle-log over the first 30 days shows zero queued candidates,
the right finding is
`knowledge/wiki/findings/dead-end-recursive-meta-thresholds-too-tight.md` —
file it and open a follow-on question on which threshold to relax
(more likely `RECURRING_REJECTION_MIN=3` than `META_SELF_EDIT_CYCLE_FLOOR=10`).

## What this branch shipped

- **G0**: design finding ([this branch](recursive-meta-design.md)) + 2
  open questions
- **G1**: `META_SELF_EDIT` proposal type + scope whitelist
  (`scripts/meta_loop.py` only) + 5 schema tests
- **G2**: `src/einstein/meta_loop/recursive_meta.py` proposer with
  ≥10-row floor + recurring-rejection detection + 13 tests
- **G3**: `evaluate_meta_self_edit_post_shadow` gate chain (cycles ≥ 10,
  shadow stat with binomial p<0.1, queued not applied, snapshot before
  queue) + new `GateDecision.QUEUED` value + 13 tests
- **G4**: `MetaArmMetrics` + `parse_meta_arm_metrics` + `ShadowMetaDelta`
  for per-arm meta-layer signal collection; 10 tests including 2
  DGM-node-114 adversarial cases
- **G5**: `src/einstein/meta_loop/queue.py` (parse + list + apply) +
  `meta_loop queue --list` / `meta_loop queue --apply <id>` CLI + 13
  tests
- **G6** (this page): synthetic dogfood + scaffold for the real first run

Total: 5 new modules / extensions, ~1300 lines of code + tests, 64 new
tests on top of the 111 existing meta_loop tests.

## See also

- [recursive-meta-design](recursive-meta-design.md) — the literature
  rationale; this page is its empirical counterpart.
- [meta-loop-first-run](meta-loop-first-run.md) — the parallel
  pending-first-run finding for the non-recursive meta-loop. Both
  pages should be updated together after the first real overnight run.
- [meta-loop-swap-surface](meta-loop-swap-surface.md) —
  `recursive-meta-v0` is the third concrete `proposer_id` after
  `metaharness-llm-v1` (LLM) and `thompson-bandit-v0` (skill bandit);
  the swap surface earned its keep.
- Branch: `js/feat/recursive-meta` — `mb/active/js-feat-recursive-meta.md`
- Code surface:
  [`src/einstein/meta_loop/recursive_meta.py`](../../../src/einstein/meta_loop/recursive_meta.py),
  [`src/einstein/meta_loop/queue.py`](../../../src/einstein/meta_loop/queue.py),
  [`src/einstein/meta_loop/meta_gate.py`](../../../src/einstein/meta_loop/meta_gate.py)
  (`evaluate_meta_self_edit_post_shadow`),
  [`src/einstein/meta_loop/shadow.py`](../../../src/einstein/meta_loop/shadow.py)
  (`MetaArmMetrics`),
  [`scripts/meta_loop.py`](../../../scripts/meta_loop.py)
  (`queue` subcommand).
