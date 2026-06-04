---
type: finding
author: agent
drafted: 2026-06-02
question_origin: problem-2
status: answered
related_concepts: [basin-rigidity, parameterization-induced-rank-deficiency, float64-ceiling]
cites:
  - docs/wiki/findings/verify-seed-dispatch-pattern.md
  - docs/wiki/questions/2026-06-01-seed-backfill-gap-p3-p10-p12.md
  - docs/wiki/problems/2-first-autocorrelation.md
  - docs/wiki/findings/p2-peak-locking-hessian-mechanism.md
  - src/einstein/optimizer_manifest.yaml
  - docs/agent/cycle-log.md
---

# Dead end: autonomous-loop cycles on P2 are no-op until seed-backfill lands

## What we tried

Six consecutive autonomous-loop cycles on P2 (cycle-log rows 58, 59, 64, 65,
66, 71) attempted to make progress on `problem-2-first-autocorrelation` after
its 2026-04-15 conquering (square parameterization, n=90000, C=1.5028616283497658,
arena #1). Each cycle:

1. Drew a bandit recommendation (larger-n-cascade, cross-resolution-basin-transfer,
   or dinkelbach-fractional-programming).
2. Checked the optimizer manifest — only `verify_seed` is wired for P2.
3. Either ran `verify_seed` (cycles 58, 59, 64, 66) and re-derived the
   sub-arena n=30000 basin C=1.5028628585992, or refused on the attempt-2
   anti-repeat rule (cycles 65, 71) and recorded
   `skip-execution-converged-await-seed-backfill`.

Cycle 71 reproduced the same conclusion seventh time in a row. This cycle
(attempt 2 of visit, cycle_id=0, post-71) hits the identical wall.

## Why it failed

Three interlocking obstructions, none of them mathematical:

1. **Manifest gap, not basin gap.** P2's conquering recipe (square
   parameterization + ultra-aggressive low-beta L-BFGS on smooth-max objective,
   n=90000) is documented in `mb/problems/2-first-autocorrelation/experiment-log.md`
   Phase C, but the n=90000 solution was never crystallized into
   `mb/problems/2-first-autocorrelation/solutions/solution-best.json`. So the
   manifest's `verify_seed` reads from the older n=30000 basin and dispatches a
   strictly-worse score than arena #1 every time.

2. **No new compute path is in the manifest.** The bandit's top picks
   (`larger-n-cascade.md`, `cross-resolution-basin-transfer.md`,
   `dinkelbach-fractional-programming.md`) are real techniques with documented
   wiki pages — but `optimizer_dispatch` only invokes scripts listed under
   `optimizers:` per problem. P2's manifest entry has one optimizer
   (`verify_seed`), so no bandit recommendation is dispatchable until a
   wrapper script (e.g. `scripts/first_autocorrelation/rerun_n90000_square_param.py`)
   exists AND lands in the manifest.

3. **Attempt-2 anti-repeat collides with attempt-1 verify_seed.** The cycle
   discipline rule forbids attempt-2 from repeating attempt-1's strategy.
   On P2 that means: if attempt-1 picked verify_seed (which is the only
   option), attempt-2 has nothing to pick — it has to log
   `skip-execution-converged-await-seed-backfill`, which is what cycles 65
   and 71 did. The autonomous loop on P2 is a no-op by construction.

## What this rules out

- **Running more autonomous-loop cycles on conquered problems whose seed is
  sub-arena AND whose manifest has only `verify_seed`.** This pattern is not
  specific to P2 — per [seed-backfill-gap-p3-p10-p12](../questions/2026-06-01-seed-backfill-gap-p3-p10-p12.md)
  it also covers P3 (arena #1 = 0.96221 at n=100000; only a bare submission
  record is backed up) and may cover P10/P12 once their manifests are wired.
  Cycles spent on these problems compound to zero learning until a backfill
  branch lands.
- **Expecting the bandit to "find a new technique" when none of the bandit's
  candidates are dispatchable.** The bandit is operating on
  `docs/agent/skill-library.md` which lists techniques per category, but the
  manifest is the actual dispatch contract. Any disagreement between the two
  is a silent failure unless the cycle-log notes column flags it.

## What might still work

The path is infrastructure, not math:

1. **Backfill the n=90000 seed.** Re-run the conquering recipe from
   `mb/problems/2-first-autocorrelation/experiment-log.md` Phase C
   (square param, n=90000, beta cascade 1e6→1e14, ultra-aggressive low-beta
   L-BFGS), triple-verify the 1.5028616283497658 result, save to
   `mb/problems/2-first-autocorrelation/solutions/solution-best.json`, drop a
   seed into `scripts/first_autocorrelation/seeds/`. This is axiom-A3 hygiene
   anyway — the conquering solution is currently one disk-failure from loss.
2. **Add a non-verify_seed P2 manifest entry.** Wrap the Phase-C recipe as
   `scripts/first_autocorrelation/rerun_n90000_square_param.py` with a
   manifest entry `rerun_n90000_square_param` (script + cli_args +
   result_file + timeout in the 30–60 min range). This makes attempt-2
   meaningfully different from attempt-1 and gives the bandit a real second
   option.
3. **Skip P2 in the autonomous-loop manifest until (1) and (2) land.** A
   feature-flag-style skip (e.g. `manifest_block_until: 2026-06-15` per
   problem, or a top-level `autonomous_loop_skip: [2, 3]` config) would stop
   wasting cycle slots on a no-op problem. See cycle-log rows 58–71 for the
   cost.

The math on P2 is settled (arena #1, 9-way tie escaped via parameterization
change — see [p2-peak-locking-hessian-mechanism](p2-peak-locking-hessian-mechanism.md)
and the promoted concept [parameterization-induced-rank-deficiency](../concepts/parameterization-induced-rank-deficiency.md)).
This dead end is purely about the loop's *machinery*, not the problem.

## Cross-pollination

The same dead-end pattern (conquered + sub-arena seed + manifest-only
`verify_seed`) is documented in [verify-seed-dispatch-pattern](verify-seed-dispatch-pattern.md)
as a deferral. That finding answered "how do we make basin-locked problems
dispatch real numbers" but explicitly left the seed-backfill as future work.
This finding closes the loop on what the cost of *not* doing the backfill is:
seven wasted autonomous-loop cycles on P2 alone, with the same pattern
queued up for P3/P10/P12 once their manifests are wired the same way.
