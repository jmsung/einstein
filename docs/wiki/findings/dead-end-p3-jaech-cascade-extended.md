---
type: finding
author: agent
drafted: 2026-05-02
status: answered
related_problems: [P3]
related_concepts: [autocorrelation-inequality.md, parameterization-selection.md]
related_findings: [optimizer-recipes.md]
cites:
  - ../../mb/tracking/problem-3-autocorrelation/strategy.md
  - ../../source/papers/2025-jaech-autoconvolution.md
---

# Dead end: extending Jaech's Adam + upsampling cascade past n=50k does not break the from-scratch ceiling on P3

## What we tried

`scripts/autocorrelation/test_jaech_cascade_extended.py` — modified Jaech & Joseph 2025 pipeline (Adam + Gaussian-noise-annealed exploration + elitist respawn + linear-interp upsampling), continuing the cascade past the existing 50k cap all the way to n=400000. The hypothesis: the existing `adam_peak_flatten.py` script caps at n=50k and tops out at C ≈ 0.908 (per strategy.md). If the 0.908 ceiling were a *cascade-length artifact*, extending the cascade to match the leader's submission resolution (n=400k) might unlock a different basin.

Cascade: random init at n=768 → exploration (4000 iters, B=128) → exploitation (4000 iters) → upsample 3072 → 12288 → 49152 → 196608 → 400000, with single-trajectory Adam refinement at each scale. MPS-accelerated on local M5 Max. Total wall-clock: 17 seconds.

## Result

| Stage  | n        | C          |
|--------|----------|------------|
| Start  | 704      | 0.897989   |
| 4×     | 3072     | 0.897730   |
| 16×    | 12265    | 0.898315   |
| 64×    | 49120    | 0.899649   |
| 256×   | 196573   | 0.900994   |
| 521×   | 400000   | 0.901404   |

The cascade does progress monotonically with `n`, but tops at ~0.901 — *below* the published 0.908 from-scratch ceiling and orders of magnitude below the warmstart-SOTA-400k result of 0.96264 (the basin reached by transplanting ClaudeExplorer's 1.6M solution). The extra resolution between 50k and 400k contributes only +0.002 to the score, well within the from-scratch noise floor.

## Why it failed (the obstruction)

The from-scratch basin and the SOTA basin are *disjoint* in the configuration space — they cannot be smoothly connected by Adam steps regardless of resolution. ClaudeExplorer's 1.6M solution lies in a structurally distinct basin (sparse-block region, 274k truly active points spanning ≥36% of the array) that random initialization simply does not reach. Adam — even with noise-annealed exploration — descends into the *nearest* local maximum, which for random uniform init is the 0.91 basin. Upsampling preserves basin identity (linear interpolation is continuous), so the 0.91 basin at small n maps to a 0.91 basin at large n.

This corroborates the strategy.md observation that "100k and 1.6M solutions live in DIFFERENT structural basins" (originally formulated for the cross-resolution transplant). The same statement applies to "from-random and from-transplant solutions live in different structural basins."

## What this rules out

- **Path (1) of the "ultimate limit" agenda** is closed: extending the upsampling cascade does not by itself find a higher basin from random init. The 0.91 from-scratch ceiling is *structural*, not an artifact of the existing 50k cap.
- By inference (and per `mb/tracking/problem-3-autocorrelation/strategy.md` Campaign 3 dead-ends): the 0.96272 result requires the cross-resolution transplant from a public high-resolution source. The transplant has been thoroughly explored via every threshold, every interpolation method, every refinement variant. It tops at 0.96272.

## What might still work (the residue)

Two paths remain genuinely untried:

1. **Brute-force GPU multistart at n ≥ 1.6M with construction-driven init** — random init only finds the 0.91 basin, but the SOTA basin is reachable from ClaudeExplorer's specific construction. If a *different* construction-driven init (Sidon-set-derived, Beatty sequence, modular character density, supersingular elliptic curve sampling) lands in a *different* high-score basin, that's a new result. Cost: ~$50-100 GPU spend, ~10% success probability.

2. **LP/SDP dual certificate** — the Cohn–Elkies-style upper bound applied to the autoconvolution objective. Rechnitzer 2026 (arXiv:2602.07292) computed 128 verified digits of the constant via interval arithmetic; that value is the true math ceiling. If the rigorous upper bound exceeds 0.9627433 (current arena gate threshold), there's room above. If it's below, the gap is fundamental. Reading Rechnitzer's actual numerical value is a 30-min literature task and is the next cheapest move.

The extended-cascade result rules out only the cheapest path. It does not establish the absolute math ceiling.

## What this means operationally

JSAgent at rank #3 with score 0.962214 is locked by the proximity-guard against the SOTA cluster (#1 ClaudeExplorer 0.962643, #2 CHRONOS 0.962641). Our local best 0.96272 is 7.6e-5 above SOTA but below the minImprovement gate (1e-4). Further compute on Adam-style or transplant-style methods is the lesson #70 anti-pattern.

The next move should be either: (a) read Rechnitzer 2026 for the rigorous upper bound (cheap, definitive on whether the gap is fundamental); (b) pivot to P17 or P19; or (c) accept the freeze and document the proximity-guard pattern as a new wisdom artifact.
