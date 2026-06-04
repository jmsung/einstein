---
type: question
author: agent
asked_by: riemann
drafted: 2026-06-04
status: open
related_problems: [2]
---

# P2 headroom — Riemann: is OrganonAgent's 1.5028609074 basin a distinct equioscillation fixed point, or our basin polished?

1. **Does OrganonAgent's 1.5028609074 solution equioscillate with the same active-peak count and the same 69-cluster spatial support as our 1.5028610916 basin, or a structurally different one?**
   Why it matters: our v² basin is a Chebyshev minimax fixed point with ~5794 near-peaks within 0.999×max and a single strict argmax at index 28879. If OrganonAgent's active set (peaks within 1e-10 of max) overlaps ours cell-for-cell, the −1.84e-7 gap is *polish within one basin* (reachable by ULP refinement). If the active peak positions differ, it is a *different basin* and polish is futile. A good answer is a side-by-side table: #peaks within {1e-12, 1e-10, 1e-8} of max, argmax location(s), and the L2/support-overlap distance between the two configurations after common-grid resampling. **Requires downloading OrganonAgent's solution values via the arena API.**

2. **Is the −1.84e-7 gap consistent with the float64-floor of our equioscillation basin, or below it?**
   Why it matters: the experiment log measured our basin's polish floor at ~1e-9 below SOTA (polish-lottery rate decaying 4e-12/s → 1.5e-13/s). If OrganonAgent sits 1.84e-7 below us — two orders of magnitude past our measured polish floor — that is strong evidence the gap is *not* within-basin polish but a genuinely lower equioscillation fixed point. A good answer reconciles the measured polish floor against the observed competitor gap and states a falsifiable claim: "same basin" (gap ≤ floor) vs "different basin" (gap ≫ floor).

3. **Does the autoconvolution of OrganonAgent's solution admit a cleaner equilibrium-measure / potential-theoretic characterization (e.g. an arcsine-type density on the support) than ours?**
   Why it matters: if the better basin corresponds to a recognizable equilibrium measure, the optimal support is predictable analytically rather than found by L-BFGS lottery — which would let us *construct* the seed instead of re-discovering it. A good answer either exhibits the measure or rules out the potential-theoretic frame for this asymmetric (sym_err 0.87) optimum.
