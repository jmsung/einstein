---
type: finding
author: agent
drafted: 2026-06-08
question_origin: problem-2
status: answered
related_problems: [2, 3, 4]
related_concepts:
  - autocorrelation-inequality
  - parameterization-induced-rank-deficiency
  - compact-support
related_findings:
  - dead-end-p2-compact-support-basin-floor.md
  - dead-end-p2-cold-seed-fixed-window.md
  - p2-peak-locking-hessian-mechanism.md
  - p2-record-gate-no-cheap-certificate.md
cites:
  - ../findings/dead-end-p2-cold-seed-fixed-window.md
  - ../findings/dead-end-p2-compact-support-basin-floor.md
  - ../findings/p2-peak-locking-hessian-mechanism.md
  - scripts/first_autocorrelation/self_pruning_search.py
  - src/einstein/first_autocorrelation/optimizer.py
  - src/einstein/first_autocorrelation/evaluator.py
---

# Breakthrough: warm self-pruning beats the P2 2-agent-tied floor (1.5028609 → 1.5028506)

## The result

Warm self-pruning support-shrinking found a P2 configuration scoring
**C = 1.5028506180034** at n=90000, support 74489 — beating the arena #1
(OrganonAgent / CHRONOS, **1.5028609073611**, tied to 1e-13) by **+1.03e-5**, four
orders of magnitude past the 1e-8 record gate. Submitted as arena_id 2335.

This **overturns the standing prior** that the 2-agent tie was the global minimum
(see `dead-end-p2-compact-support-basin-floor`). It was a sharp *local* basin, not
the floor. The branch's stated EV was honest-zero; the result was a record.

## What worked (the mechanism)

The path was the one `dead-end-p2-cold-seed-fixed-window` left open — *warm* self-
pruning, reconciling the two prior dead-ends:

1. **Start warm, full-support.** Seed from our near-converged full-support basin
   (`solutions-v2/best_1.502862793_n90000.json`, C=1.5028628). Cold seeds can't
   reach the competitive region (cold-seed dead-end: +0.022); warm starts are
   already at +1.9e-6.
2. **Prune smallest-|v|, optimizer's choice.** Zero the smallest-magnitude *active*
   cells on a support-shrinking schedule (89910 → 74489). The key difference from
   the failed Goal-1 search: the optimizer chooses *which* cells die (data-driven),
   NOT a pre-imposed contiguous window. A fixed window was strictly worse (+0.336);
   data-driven pruning monotonically *improved* C.
3. **Re-optimize v² L-BFGS, let peak-locking set in.** `f = mask·v²` makes the
   pruned cells exact-zero gradient fixed points; the surviving cells re-converge
   with the full β-cascade (`p2-peak-locking-hessian-mechanism`).

The trace is monotone-down in C as support shrinks — the signature of a genuinely
better basin, not a discretization spike:

| support | C | vs arena #1 |
|---:|---:|---:|
| 89910 | 1.5028613889 | +4.8e-7 |
| 86589 | 1.5028593719 | **−1.5e-6 (crosses below)** |
| 83391 | 1.5028568053 | −4.1e-6 |
| 80312 | 1.5028538278 | −7.1e-6 |
| 77346 | 1.5028515229 | −9.4e-6 |
| 74489 | **1.5028506180** | **−1.03e-5** |

## Why it's real (verification, not just the in-loop evaluator)

The 2-agent-tie prior is strong, so a 1e-5 improvement demanded scrutiny against the
P9/P14/P17 evaluator-drift pattern. Four independent checks, all pass:

1. **Evaluator = verbatim arena code.** `evaluator.verify_and_compute` is the arena
   verifier byte-for-byte (`np.convolve` direct, dx=0.5/n). Not a surrogate.
2. **Calibrated exactly on the leader.** Scoring OrganonAgent's own #1 solution with
   our evaluator reproduces **1.5028609073611** (the published arena value) to the
   digit; organon-polished matches its published score to 1e-13. No drift.
3. **Robust to thresholding (not filler-gaming).** Clipping all cells below
   1e-7·max — dropping support 74489 → 56638 — moves C by only +2e-7; it still beats
   arena #1. The record is carried by real structure, not near-zero spike cells.
4. **No proven bound violated.** The certificate ceiling is ≤1.28
   (`p2-record-gate-no-cheap-certificate`); a better empirical construction at
   1.50285 contradicts no theory.

Structure is non-pathological: fragmented multi-run support (1099 runs) and
spikiness (max/mean ≈ 179) comparable to organon's (6334 runs, ≈ 95).

## What this generalizes to (look-back)

- **The 2-agent / N-agent tie is evidence of a sharp basin, not a proof of global
  optimality.** A tie to 1e-13 means independent searches *converge* there — often
  because they share a parameterization that can only reach that basin. It does not
  rule out a better basin reachable by a *different search operator*.
- **Data-driven self-pruning > pre-imposed support masks** for compact-support
  problems. Let the optimizer choose which cells to zero; don't impose the geometry.
- **Warm + actively-shrinking** beats both pure polish (can't change support) and
  cold search (can't reach competitive scores). The viable corridor is the
  intersection.
- **Candidate transfer**: P3 (second-autocorrelation) and P4 (third-autocorrelation)
  are the same family with the same compact-support leaders. Warm self-pruning from
  our full-support basins there is the obvious next probe.

## Status

Submitted arena_id 2335 (2026-06-08, gated auto-submit path, human-confirmed).
Server-side verification pending at write time; live-board confirmation to follow.
Solution backed up: `mb/problems/2-first-autocorrelation/solutions/solution-selfprune-1.502850618003.json`.
