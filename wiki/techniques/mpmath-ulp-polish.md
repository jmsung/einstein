---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P6, P11, P15, P16]
compute_profile: [local-cpu]
cost_estimate: "minutes (per polish run)"
hit_rate: "TBD"
---

# mpmath ULP-Step Coordinate Descent

## TL;DR

At the float64 floor of constraint-heavy problems, smooth surrogates die (their kernel noise floor sits around 1e-12 while the residual loss is ~1e-13). The actual workhorse is **discrete ±1/±2 ulp single-coordinate descent** in float64, with mpmath at dps≥50 used only to evaluate proposed moves. Pair with a float64 active-pair screen for a 10× speedup over uniform mpmath.

## When to apply

- Problem score depends on a smooth quadratic distance / constraint structure.
- Smooth optimizers (SLSQP, L-BFGS, smooth-max β-cascade) have saturated; further gains require precision below their kernel noise.
- An mpmath verifier is available (P6 post-2026-04-09; Tammes; min-distance-ratio) to evaluate candidate moves without numerical drift.
- Goal: drive the score from `~2e-13` to `~1e-13` (P6 reproduction: 1.97e-13 → 1.59e-13 in ~15 min CPU).

## Procedure

1. **Choose dps from condition number**: `dps ≈ log10(cond) + buffer`. For P6 d=11 n=594, dps=50 is sufficient; for k-climbed Laguerre matrices (cond ~9e37), dps=30 minimum.
2. **Float64 active-pair screen** (the 10× speedup):
   ```python
   # P6 sketch — only ~17k of 176k pairs survive
   d2 = pairwise_dist2_float64(v)
   active = d2 < 4 + 1e-10
   ```
3. **For each coordinate `v[i][k]`, in sequential row order**:
   - Compute candidates at `+1, +2, −1, −2` ulps of the current float64 value.
   - For each candidate, recompute only the row-i pair set (~593 pairs at d=11) in mpmath at dps=50.
   - Accept any strict improvement; otherwise restore.
4. **Alternate 1-coord and 2-coord sweeps**: a 2-coord intra-row variant (perturb two coords of the same vector to rotate it slightly in a 2D subspace) finds moves the 1-coord sweep misses; alternating compounds.
5. **Stop when a full sweep produces zero improvements**.

```python
import struct, mpmath
mpmath.mp.dps = 50

def ulp_neighbors(x, k):                       # ±1 and ±2 ulps
    bits = struct.unpack('<q', struct.pack('<d', x))[0]
    return [struct.unpack('<d', struct.pack('<q', bits + s))[0]
            for s in (-2, -1, 1, 2)]
```

## Pitfalls

- **dps too low → silent inf scores** (lesson #65): k=15 Uncertainty optimizer reported "improvements" while `fast_evaluate` returned inf because the leading coefficients underflowed. Always re-run a known-good smaller-k solution at the new dps and confirm bit-identical scores.
- **Skip the float64 screen** → uniform mpmath polish is 10–100× too slow; you lose `minImprovement = 0` polish races.
- **Smooth surrogates at the floor** are dead — they have a noise floor (kernel-set) larger than the residual loss. Don't retune β; it cannot help below its own noise.
- **2-coord cross-row** is more expensive (~2 × 593 pairs touched) and rarely productive without alternating with 1-coord.
- **No mpmath verifier?** This pattern is unsafe. Evaluate the float64 candidate with arena verifier + scipy-spatial cross-check; without three-way agreement the "improvement" is likely numerical noise.
- **Ulp encoding**: use bit-level integer arithmetic on float64 representation, not multiplicative scaling. `x * (1 + 1e-16)` is not 1 ulp.

## Compute profile

Local CPU. Sequential per-coordinate descent — GPU sits idle. mpmath is CPU-only. Productive for ~15–60 minutes; diminishing returns past that. P6 reproduction: 15 min for ~0.4e-13 of improvement.

## References

- `wiki/findings/float64-polish.md` (lessons #65, #74, #75 — dps scaling, screen-then-evaluate, ulp coord descent).
- `wiki/findings/optimizer-recipes.md` — mpmath polish patterns.
- knowledge.yaml strategies: `mpmath_polish_with_float64_screen`, `ulp_coord_descent_mpmath_verify`.
- `wiki/techniques/slsqp-active-pair-polish.md` (the smoother-but-shallower polish that this technique succeeds).
- `mb/tracking/problem-6-kissing-number/strategy.md`.
