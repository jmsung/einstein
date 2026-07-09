---
type: finding
author: agent
drafted: 2026-06-02
question_origin: problem-3
status: answered
related_concepts: [basin-rigidity, float64-ceiling]
cites:
  - knowledge/wiki/findings/dead-end-p2-autonomous-loop-blocked-by-seed-backfill.md
  - knowledge/wiki/questions/2026-06-01-seed-backfill-gap-p3-p10-p12.md
  - knowledge/wiki/findings/verify-seed-dispatch-pattern.md
  - knowledge/wiki/problems/3-autocorrelation.md
  - src/einstein/optimizer_manifest.yaml
  - docs/agent/cycle-log.md
---

# Dead end: autonomous-loop cycles on P3 are no-op until seed-backfill lands

## What we tried

Five consecutive autonomous-loop cycles on P3 (cycle-log rows 60, 61, 67, 68,
and this one) attempted to make progress on
`problem-3-second-autocorrelation` after its 2026-04-10 conquering
(cross-resolution-basin-transfer from a public 1.6M solution, average-pool to
n=100000, Dinkelbach refinement on Modal A100, arena #1 at C=0.962214 — since
slipped to rank-3-frozen-by-proximity-guard). Each cycle:

1. Drew a bandit recommendation (`larger-n-cascade`,
   `cross-resolution-basin-transfer`, `remez-equioscillation-diagnostic`,
   `dinkelbach-fractional-programming`).
2. Overrode with an LLM-picked strategy when the bandit's choice was a known
   dead-end (cycle 61: avoided `larger-n-cascade.md` per
   [dead-end-p3-jaech-cascade-extended](dead-end-p3-jaech-cascade-extended.md);
   cycle 68: picked `construction-driven-init-n1.6M-sidon-beatty`).
3. Reached the dispatch step, found `optimizer_manifest.yaml` has **no entry
   for problem 3**, and logged `agent=no-manifest-entry`.

Same wall, fifth time in a row.

## Why it failed

Identical to the P2 case
([dead-end-p2-autonomous-loop-blocked-by-seed-backfill](dead-end-p2-autonomous-loop-blocked-by-seed-backfill.md)) — that
finding is the canonical statement and applies verbatim:

1. **Manifest gap, not basin gap.** P3's conquering recipe (cross-resolution
   transplant 1.6M → 100k + Dinkelbach refinement, see
   `mb/problems/3-autocorrelation/experiment-log.md` Wave 1) requires the
   1.6M source artifact AND a result-file emitter wrapper. Neither exists in
   the manifest. `mb/problems/3-autocorrelation/solutions/solution-best.json`
   is a bare submission record (no `values` array), so `verify_seed` cannot
   even be wired the way P2/P4/P5/P11/P15/P16/P18/P19 are.
2. **No dispatchable bandit pick.** The bandit's candidates
   (`larger-n-cascade`, `cross-resolution-basin-transfer`,
   `remez-equioscillation-diagnostic`, `dinkelbach-fractional-programming`)
   are real techniques with wiki pages, but `optimizer_dispatch` only invokes
   scripts listed under `optimizers:` per problem. P3 has no `optimizers:`
   block at all.
3. **Attempt-2/3 anti-repeat is irrelevant.** Attempt-1 already cannot pick a
   dispatchable strategy, so the anti-repeat rule has nothing to enforce — every
   attempt in every visit collapses to the same `no-manifest-entry` log.

## What this rules out

- **Spending more autonomous-loop cycle slots on P3 before the seed-backfill
  branch lands.** The fifth blocked cycle in a row confirms the pattern is
  deterministic, not stochastic. Each cycle costs LLM tokens + cycle-log row
  + skill-library increments with hit_rate 0.00 for whichever technique was
  "tried" — actively poisons the bandit's posterior for techniques that
  weren't actually evaluated.
- **The bandit/LLM strategy-picker as a remediation.** No prompt engineering
  inside the inner-attempt loop can produce a dispatchable strategy when the
  outer manifest is empty for this problem_id. The fix has to live in
  `optimizer_manifest.yaml` + `mb/problems/3-autocorrelation/solutions/`,
  not in the picker.

## What might still work

Strict infrastructure path, mirroring the P2 remediation steps:

1. **Backfill the n=100000 seed.** Re-run the Wave-1 recipe from
   `mb/problems/3-autocorrelation/experiment-log.md`: download the public
   ClaudeExplorer 1.6M solution → average-pool to n=100000 → Dinkelbach
   refinement with the documented beta cascade → triple-verify against
   the audited arena evaluator → save the full `values` array to
   `mb/problems/3-autocorrelation/solutions/solution-best.json` (currently
   a bare submission record) → drop a seed under
   `scripts/second_autocorrelation/seeds/best.json[.gz]`. Axiom-A3 hygiene
   anyway — the conquering solution is currently one disk-failure from loss.
2. **Wire `verify_seed` for P3.** Once (1) lands, add a P3 block to
   `src/einstein/optimizer_manifest.yaml` modeled on P2/P4/P5: `default:
   verify_seed`, `script: scripts/verify_seed.py`, `cli_args: ["--problem-id",
   "3"]`. Also extend `SPECS`/`EXPECTED` in `scripts/verify_seed.py`. This
   gives the loop a real triple-verified dispatch — the n=100k float64
   ceiling — even if no novel Δ is reachable.
3. **Optionally add a non-verify_seed P3 entry.** Wrap the Wave-1 transplant
   recipe (or the cleaner Wave-19 1.6M-upsample variant scoring 0.96270) as
   `scripts/second_autocorrelation/transplant_and_refine.py` with a long
   timeout (30–60 min). This is the only path to give attempt-2/3 a real
   second option per the cycle-discipline anti-repeat rule. Without it, even
   post-backfill the loop converges to `skip-execution-converged-await-...`
   on attempt-2 (the P2 pattern after manifest-coverage-sprint Goal-6).
4. **Skip P3 in the autonomous-loop manifest until (1)+(2) land.** A
   per-problem `manifest_block_until: 2026-06-15` (or top-level
   `autonomous_loop_skip: [3, 10, 12]`) would stop the bleed. See
   cycle-log rows 60, 61, 67, 68 for the cost so far.

The math on P3 is settled in two senses: arena #1 was held briefly at
0.962214 in 2026-04-10 then conceded to ClaudeExplorer at n=400k; the
**unbridgeable 2.4e-5 gap to the current SOTA-of-SOTA target** is documented
across 22 experiments in
`mb/problems/3-autocorrelation/experiment-log.md` (Campaigns 1–3, ~$115 GPU,
~12h CPU). This dead end is purely about the loop's *machinery*, not the
problem.

## Cross-pollination

This is the second instance (after
[dead-end-p2-autonomous-loop-blocked-by-seed-backfill](dead-end-p2-autonomous-loop-blocked-by-seed-backfill.md))
of the same loop-machinery dead-end. P10 (thomson-n282, no solution file at
all) and P12 (flat-polynomials, no in-repo construction reproduces the 1.3539
stochastic-search result) are the next two queued instances per the
[seed-backfill question](../questions/2026-06-01-seed-backfill-gap-p3-p10-p12.md).
At ≥4 wasted cycles per blocked problem (the current P3 number), the
expected cost of *not* doing the backfill across {P3, P10, P12} is
≥12 more bandit-poisoning no-op cycles. The right intervention is a single
infrastructure branch covering all three, not per-problem retries inside the
autonomous loop.
