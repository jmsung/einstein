---
type: finding
author: agent
drafted: 2026-06-10
question_origin: problem-4
status: answered
related_problems: [2, 3, 4]
related_concepts:
  - autocorrelation-inequality
  - n-agent-tie-not-global-min
related_findings:
  - p2-warm-self-pruning-beats-record.md
  - p4-basin-is-discrete-sign-topology.md
  - p4-fragmentation-not-fraction-shared-envelope.md
cites:
  - ../findings/p2-warm-self-pruning-beats-record.md
  - ../findings/p4-basin-is-discrete-sign-topology.md
  - ../findings/p4-fragmentation-not-fraction-shared-envelope.md
  - ../questions/2026-06-10-p4-shrink-regrow-geometric-decay.md
  - scripts/third_autocorrelation/self_pruning_search.py
  - scripts/third_autocorrelation/regrow_reopt.py
  - scripts/third_autocorrelation/transplant_signs.py
---

# Dead end: shrink–regrow self-pruning converges to its own fixed point on P4, 7.7e-5 above the leader

## What we tried

P2's record operator (warm data-driven self-pruning) ported to the signed P4
objective with f = mask·w (sign-free re-opt inside the surviving support), plus a
full-support *regrow* phase (refill pruned cells with tiny noise, re-opt) — the
shrink–regrow cycle. Six cycles from our verified basin (1.4525211550469), then a
wall-hit council (Tao/Hilbert/Cohn/Hadamard) with three falsifiable arms:
energy-norm prune selection (e_i = w_i²·p_{2i}), mid-domain run-splitting prune,
and leader-sign transplant onto our magnitudes. Strong cascade throughout
(max_iter 2000, β → 1e13); every checkpoint triple-verified.

## What worked (and is NOT the dead end)

- **Shrink–regrow is the first operator that crosses P4 sign-topology classes by
  continuous descent** — it partially overturns the 06-06 verdict ("descent is
  trapped in its starting sign class"). neg_runs grew 823 → 2758 with monotone
  score descent: 1.4525211550 → **1.4523808925** (−1.40e-4, our new P4 best,
  triple-verified to 4e-16).
- The weak-cascade artifact: at max_iter 1000 / β ≤ 1e12 pruning looks
  monotone-UP; the same schedule with max_iter 2000 / β → 1e13 is monotone-DOWN.
  Verify the cascade is strong enough before judging an operator.
- Fine prune steps (~0.4%/level) beat coarse (~1%/level) at matched support.

## Why it failed (the obstruction)

Per-cycle gains decay geometrically (−1.9e-5, −1.2e-5, −9.1e-6, −6.8e-6, −2.6e-6)
toward a fixed point ≈ 1.452381, 7.7e-5 above the leader (1.4523043331832). The
council's three competing explanations were all falsified by experiment:

1. **Not prune-selection blindness (Hilbert/Cohn):** energy-norm selection
   (curvature-weighted, 37% different kill set) stayed exactly on the decay
   envelope (−2.3e-6).
2. **Not starved run-nucleation (Tao):** forcing mid-domain run-splitting injected
   fragmentation fast (2696 → 3642 runs) but *worsened* C monotonically (+2.4e-4)
   — injected runs are damage, not the leader's organized structure.
3. **Not a sign-field deficit at all (Hadamard):** transplanting the leader's
   complete 4705-run sign field onto our magnitudes lands at 1.4539 after free
   re-opt — worse than both basins.

The surviving explanation: **new fragmentation is only worth its cost when the
sign field and the magnitude field co-evolve through descent.** The operator's
bottleneck is the rate at which re-optimization can *organize* newly injected
structure — intrinsic to the cycle, not to any selection rule. The leader's basin
is a jointly co-adapted (sign, magnitude) structure; no fiat injection of either
half reproduces it.

## What this rules out

- All prune-selection-rule variants of shrink–regrow on P4 (|w|, energy-norm,
  run-splitting, and by two independent falsifications the LP-dual-guided class).
- Sign-field synthesis/extrapolation and any transplant of topology between
  basins (extends `p4-basin-is-discrete-sign-topology`: incompressible AND
  jointly co-adapted with magnitudes).
- More plain cycles: each costs ~90 min and the envelope predicts <1e-6/cycle now.

## What might still work

- **P3 transfer (the prescribed next probe).** P3 (second autocorrelation,
  f ≥ 0) is the *closer* P2 twin — same nonnegativity, same dead-cell Hessian
  fingerprint (verified n=80), compact-support leaders. Port notes from this
  campaign: (a) use the v² parameterization as in P2, not the signed kernel;
  (b) **strong cascade first** — the weak-cascade artifact here would have
  falsely killed the operator at calibration; (c) fine steps ~0.4%/level;
  (d) add the regrow phase (refill with *positive* noise) — it bought an extra
  −5e-6 to −3e-5 per cycle on P4 and has no P2/P3 precedent; (e) budget cycles
  geometrically — if per-cycle gains decay faster than ×0.75, the fixed point is
  short and the honest move is to bank the improvement. Resolution interaction:
  P3's record may be n-limited (resolution-is-the-lever) — run the cycle at the
  arena n-cap from the start.
- **On P4 itself:** only a genuinely different co-evolution channel — e.g.
  joint (sign, magnitude) continuation methods (homotopy in run count along the
  descent path), or the long-deferred signed-f dual certificate to decide whether
  1.4523 has headroom at all. Both are research items, not optimizer runs.

## Status

Honest-zero for the record claim (gap 7.7e-5 ≫ 0, and P4's minImprovement gate is
1e-4 anyway). The −1.40e-4 improvement and the operator are banked:
`solution-js-feat-p4-warm-pruning-transfer-1.4523808924693.json`.
