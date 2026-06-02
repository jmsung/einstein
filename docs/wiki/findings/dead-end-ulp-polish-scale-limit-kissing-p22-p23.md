---
type: finding
author: agent
drafted: 2026-06-01
question_origin: problem-22
status: answered
related_concepts: [float64-ceiling, provable-floor-and-frozen-problems]
related_problems: [22, 23, 6]
cites:
  - src/einstein/ulp_polish.py
  - src/einstein/p22_kissing_d12/evaluator.py
  - src/einstein/p23_kissing_d16/evaluator.py
---

# Dead end: dual-gate ULP polish does not scale to the kissing problems (P22 d=12, P23 d=16)

## What we tried

Phase 2a targeted P22 (kissing d=12, n=841) and P23 (kissing d=16, n=4321) for the
generic dual-gate ULP polish, "polish off the rank-3 squeeze solutions." Both
already ship an `overlap_loss_mpmath` exact evaluator, so they looked like clean
fits.

## Why it failed — three independent obstructions

1. **No in-repo seed.** Neither problem has `scripts/<problem>/seeds/best.json`;
   the only solutions live in the private `mb/` tree (the CHRONOS score-2 config
   and a near-floor "squeeze" variant for each). The polish/dispatch contract
   requires a deterministic in-repo seed (same discipline as `verify_seed`), so
   there is nothing to wire against without a seed-backfill commit.

2. **O(n²) mpmath per coordinate is intractable.** The merit is a sum of
   pair overlaps over all pairs: 353,220 pairs for P22, **9,333,360** for P23.
   The engine evaluates the exact (mpmath) merit once per coordinate key
   (n keys) plus once per float64-passing candidate. A single sweep is
   ~n·(pairs) ≈ 3e8 mpmath ops for P22 and ~4e10 for P23 — orders of magnitude
   beyond a practical polish budget. The P14/P5/P11 fits work because n ≤ 50
   keeps the pair count ≤ 1225; the kissing dimensions break that assumption.
   (A per-coordinate active-pair screen would help, but the contact structure in
   d=12/16 is far denser than the planar packings, so the screen does not reduce
   the order.)

3. **Tied-SOTA floor → non-auto.** Both sit at the score-2 floor pattern (P23
   κ(16)=4320 is the known exact maximum; the score-2 config is tied SOTA). Per
   the submission policy, "tied SOTA with floor configuration" is explicitly a
   human-approval case, not auto-submit — so even a successful sub-ulp squeeze
   would not be auto-submittable.

## What this rules out

The dual-gate ULP polish is a **small-n** technique (n·n_pairs must fit a polish
budget; empirically n ≤ ~50 with full mpmath). It does not generalize to the
high-n sphere-code problems regardless of seed availability. The "the body
generalizes verbatim to the whole float64-ceiling family" optimism in the
dual-gate finding holds for the *planar / small sphere-code* members
(P5/P11/P14) but not the kissing members.

## What might still work

- For P22/P23, the right tool is the existing `overlap_loss_mpmath` evaluator
  applied to **active (near-contact) pairs only**, driven by a contact-graph
  first-order step (the P22 link-tangent + squeeze recipe in
  `scripts/p22_kissing_d12/`), not a brute coordinate sweep.
- A seed-backfill (commit the mb best solutions to `scripts/<problem>/seeds/`)
  would at least enable `verify_seed` dispatch for both — orthogonal to the
  polish question.

## See also

- [mpmath-ulp-polish-dual-gate-p14](mpmath-ulp-polish-dual-gate-p14.md)
- [provable-floor-and-frozen-problems](../concepts/provable-floor-and-frozen-problems.md)
