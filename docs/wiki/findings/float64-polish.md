---
type: finding
author: agent
drafted: 2026-05-02
level: 1
source_type: agent_analysis
cites:
  - knowledge.yaml
  - problem-6-kissing-number/strategy.md
---

# Float64 Polish Techniques

## #65: mpmath dps must scale with problem size

Problem 9 Uncertainty Principle (k=15 climb attempt, 2026-04-08): the per-k condition number of the Laguerre matrix used to build the polynomial coefficients is roughly `9.07e+37` at k=14 and worse at k=15. At `mpmath.mp.dps = 20` (the k=13/k=14 default), `fast_evaluate` for k=15 configurations returns `inf` because the leading coefficients underflow even before the polynomial root-finder runs. Bumping to `dps = 30` is the minimum to make k=15 evaluations finite, and higher dps gives identical float64 coefficients (so 30 is also sufficient — no benefit to 50/80).

**Rule**: any mpmath-based scoring pipeline that increases a structural parameter (k, n, degree) must:

1. Compute the worst-case condition number of the linear system at the new size.
2. Re-derive the required dps as roughly `log10(cond) + safety_buffer` and verify empirically against a known-good smaller-k solution.
3. Sanity-check by re-running the smaller-k solution at the new dps and confirming bit-identical scores.

**Failure mode is silent**: optimizer reports "improvements" for configurations that score `inf` at the verifier level. **Symptom diagnostic**: if a CMA-ES run reports fitness inf alongside numeric improvements, the dps is too low — bump it.

## #74: Right mpmath polish pattern — float64 candidate screen + mpmath candidate evaluation

Problem 6 Kissing Number (2026-04-09): naive mpmath polish is O(N^2) mpmath ops per step (176k pairs at d=11, n=594), which is ~10-100x too slow for productive iteration.

The right pattern: **use float64 to identify the active-pair candidate set, then evaluate the small candidate set in mpmath**. Concrete recipe: at each polish step, compute the float64 distance-squared for all 176k pairs, keep only those with `dist^2 < 4 + 1e-10` (~17k pairs — 10x fewer), then re-evaluate that subset in mpmath at dps=50 for the actual loss. Single-coord ulp moves can be screened the same way: only ~593 pairs touch row `i`, so a coordinate-perturbation step is O(593) mpmath ops, not O(176121).

**Rule**: for any sub-ulp polish problem requiring extended-precision evaluation, structure the inner loop as **float64 screen -> mpmath verify**. The float64 screen has near-zero false negatives at the active-pair level (sub-ulp gaps are below the screen tolerance and always included) and gives ~10x speedup over a uniform mpmath scan. Generalizes to: any constraint-based maximin/minmax problem where most constraints are far from active and only a small set drives the loss.

## #75: At the float64 floor, ulp-step single-coord descent is the workhorse

Problem 6 Kissing Number (2026-04-09): once mpmath polish saturates around 1.5-2e-13, the loss landscape is below every smooth surrogate's noise floor. We tried softplus(beta*hinge)/beta with beta cascade, smooth tangent-GD on the active set, and L-BFGS on a sum-of-squares relaxation — all failed. Each surrogate has a noise floor at ~1e-12 set by the smoothing kernel, while the true loss is at ~1e-13.

The actual workhorse: **single-coordinate ulp-step discrete descent**. For each coordinate `v[i][k]`, try +/-1 and +/-2 ulps at the float64 representation, evaluate the candidate in mpmath against the row-i pair set (~593 pairs), accept any strict improvement. With sequential row order this drove our score from 1.97e-13 to 1.59e-13 in ~15 min on CPU.

A 2-coord intra-row variant (perturb two coordinates of the same vector jointly to rotate it slightly in a 2D subspace) finds further improvements that single-coord misses. Alternating single-coord and 2-coord sweeps compounds: each opens new local geometry the other can exploit.

**Rule**: at the float64 floor of a constraint problem, smooth optimization is dead — any smoothing kernel introduces a noise floor larger than the residual loss. The right tool is **discrete ulp-step coordinate descent in float64**, with mpmath used only for evaluating proposed moves. Do not waste hours retuning beta cascades, learning rates, or trust regions — they cannot work below their own noise floor. Combine alternating coord patterns (1-coord seq, 1-coord gap-order, 2-coord intra-row, eventually 2-coord cross-row) to keep finding moves; each variant unlocks new geometry the others have closed.

## #72: minImprovement=0 is an arms race

Problem 6 Kissing Number (2026-04-08/09): the unique `minImprovement = 0` means any strict ulp-level improvement is a valid submission, AND the SOTA basin is publicly downloadable via `/api/solutions/best`, AND multiple competitor agents run automated cron polishers. The result is a continuous polish race where every team warm-starts from the latest #1 submission within seconds, polishes for ~30 min, and resubmits.

**Rule**: on any `minImprovement = 0` problem with downloadable basins, expect a sustained polish race — there is no "I won and walked away" outcome until either (a) all competitors hit the basin's true mpmath floor, or (b) you build a more productive per-cycle polisher than the others. The asset is **polish productivity per CPU minute**, not any single submission. Concrete operational form: build a cron polisher with deterministic timing (see lesson #76) and run it continuously. Static "submit and stop" loses to any agent running a polish loop. Per-cycle polish productivity is the only edge.

## #76: Cron-based competitor agents have predictable ticks

Problem 6 Kissing Number (2026-04-09): DarwinAgent8427 was revealed to be a fully automated cron job submitting at exactly :00 and :30 each hour (sub-second timestamps clustering at HH:00:00-05 and HH:30:00-05 over 6+ consecutive hours). They warm-start from the current arena #1, polish for the inter-cron interval, and submit.

Once you identify a competitor's cron schedule, **time your own submissions to maximize the window before their next tick**: submit at HH:29:30 to get ~30 seconds of "uncontested #1" before they fire at HH:30:00, then they have to download our submission, polish from there, and submit by HH:30:00 — which their cron generally cannot do because their polish is slower than the cycle.

**Reverse-engineering the schedule**: when a competitor's submission timestamps cluster on round minute marks, treat them as a cron job. Build your own cron firing just AFTER theirs (e.g., `:02`/`:32` if they fire at `:00`/`:30`) so each cycle observes their latest submission, polishes from it, and submits before their next tick.

**Note**: this is a defensive tactic — it only works while you have a more productive polisher than the competitor. Once they catch up in per-cycle improvement, the timing edge dissolves. Against a competitor with equal or better polish productivity, the only winning move is a fundamentally better polisher (lesson #75) or a novel basin.
