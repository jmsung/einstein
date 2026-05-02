---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P13]
compute_profile: [local-cpu]
cost_estimate: "seconds per snap; minutes with snap-polish-BH chain"
hit_rate: "TBD"
---

# Boundary-Snap for Interpolation Kinks

## TL;DR

For piecewise-linear / slope-N interpolation of an envelope with first-order discontinuities at known points (Turán scallops, sphere-packing contact-graph hinges), **snap the nearest sample point to each kink and re-polish**. The interpolation residual at kinks is the dominant overshoot; smooth optimizers avoid the boundary because the gradient is discontinuous there, but the actual optimum requires a sample on the boundary.

## When to apply

- Score = slope-N (linear, quadratic, cubic) interpolation of an envelope.
- Envelope has first-order discontinuities at known points `x_kink` (Turán: `x = 1 − 1/k` for `k=2..n`; sphere packings: contact-graph switch points).
- Diagnostic: residual `(interp − envelope)` shows spikes at `x_kink` locations and is flat elsewhere.
- A smooth bounded optimizer (e.g. `bounded-lbfgs-per-region-sigmoid`) is already in place for the polish stage.

## Procedure

1. **Enumerate known kink locations** from problem structure (e.g. `x_kink = [1 − 1/k for k in 3..n]`).
2. **For each kink, find the nearest sample point** and snap it exactly: `x_i ← x_kink`.
3. **Re-polish neighboring points** with bounded L-BFGS (per-region sigmoid). The freshly-snapped point has zero gradient at the kink; neighbors take up the residual.
4. **Iterate snap → polish → BH → snap** until stable; converges in 2–3 rounds (P13: each round yields ~+1.24e-8).

```python
# Sketch
kinks = [1 - 1/k for k in range(3, n+1)]
for round in range(3):
    for x_kink in kinks:
        i = np.argmin(np.abs(x - x_kink))
        x[i] = x_kink                              # exact snap
    x = bounded_lbfgs_polish(x)                    # per-region sigmoid
    x = basin_hop(x, n_hops=10)                    # explore neighbors
```

## Pitfalls

- **Smooth optimizers avoid the boundary**: gradient at `x_kink` is discontinuous, so gradient-based methods stay strictly inside the region. The actual optimum REQUIRES a sample on the boundary — that's why pure smooth polish fails on these problems.
- **Snap without re-polish overshoots elsewhere**: snapping disturbs neighbors; without a polish pass, you trade kink-residual for neighbor-residual.
- **All kinks must be enumerated**: missing one leaves a residual spike that no smooth optimizer can find.
- **Hit rate per round is small** (P13: 1.24e-8); allocate enough rounds to compound. Single snap-polish often gives 50% of the available improvement; the rest needs the chain.
- **Doesn't apply to smooth envelopes**: if the score function is smooth at all `x_kink`, snap gives nothing — verify the kink hypothesis first by inspecting residual spikes.

## Compute profile

Local CPU. Each snap → bounded-L-BFGS polish → BH cycle is ~30s for n=500. Three rounds = ~2 min total.

## References

- `wiki/findings/optimizer-recipes.md` (#71 — boundary-snap for slope-N interpolation kinks).
- knowledge.yaml pattern `boundary-snap-for-interpolation-kinks`.
- `wiki/techniques/bounded-lbfgs-per-region-sigmoid.md` (the companion polish technique).
- `mb/tracking/problem-13-edges-triangles/strategy.md` (snap-BH chain → −0.71170918806610).
