---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P2, P3, P4]
compute_profile: [local-cpu]
cost_estimate: "minutes to ~1 hour CPU"
hit_rate: "TBD"
---

# Larger-n Cascade for Equioscillation Escape

## TL;DR

For discretized-function problems where 3+ top agents converge to byte-identical SOTA at fixed `n` with high active-constraint count (Chebyshev equioscillation fingerprint), block-repeat upsample to `kn`, add tiny Gaussian noise, and re-optimize with smooth-max L-BFGS at progressively higher β. The "frozen at theoretical bound" label is usually a discretization bound, not the continuous bound — larger n unlocks fresh DOF.

## When to apply

- Discretized-function problem (autocorrelation, Erdős overlap, flat polynomials with variable n).
- 3+ leaderboard agents share byte-identical SOTA at the same n.
- Active-constraint count at SOTA ≥ n/2 (count conv positions where the max is attained within 1e-12).
- Problem allows variable n up to a generous arena cap (P4: 100k; P2: 100k).
- Solutions are downloadable (warm-start required — naive upsample alone gains nothing).

## Procedure

1. **Diagnostic (15 minutes)**:
   - Download SOTA via `/api/solutions/best`.
   - Count active conv positions. If ≥ n/2, equioscillation-locked at this n.
2. **Block-repeat upsample**: `v_kn = np.repeat(v_n, k)`. Score is preserved EXACTLY at this point.
3. **Add tiny noise**: `v_kn += sigma_noise * randn(kn)` with `sigma_noise ≈ 1e-6 · σ(v)`. This is the unlock — without perturbation the piecewise-constant constraint is preserved and L-BFGS finds nothing.
4. **β-cascade**: run L-BFGS on a smooth surrogate (e.g. LSE_β for max objective) at β stepwise: `1e4 → 3e4 → 1e5 → 3e5 → 1e6 → ... → 1e10`. Each step runs to convergence at that β.
5. **n-cascade**: starting at 2×–4× SOTA n, double per stage until arena cap or continuous limit. Each stage warm-starts from the previous (block-repeated + re-perturbed). Gains halve per stage (continuous-limit convergence).
6. **Triple verification**: `np.convolve` + `scipy.fftconvolve` + manual loop. Max disagreement ≤ 1 ulp.

```python
# Sketch (P4 n=400 → 100k cascade)
for n in [1600, 3200, 6400, 12800, 25600, 51200, 100000]:
    v = np.repeat(v_prev, n // n_prev)
    v += 1e-6 * v.std() * np.random.randn(n)
    for beta in [1e4, 3e4, 1e5, 3e5, 1e6, 3e6, 1e8, 1e10]:
        v = lbfgs_smooth_max(v, beta)
    v_prev, n_prev = v, n
```

## Pitfalls

- **Upsample alone gains nothing**: block-repeat preserves piecewise-constant structure exactly. The unlock is the noise + L-BFGS combination.
- **β too high too early**: jumping to β=1e10 immediately commits to the nearest local optimum of the smooth surrogate. The cascade is essential.
- **n too large**: P2 sweet spot is n=90000 (3× block-repeat); larger gives shallower minima. Test the n curve before committing.
- **Parameterization may peak-lock** (P2 with `f = exp(v)` peak-locked at delta~5.25e-8 across all n). Larger-n alone doesn't break peak-locking — change parameterization to `f = v²` first (lesson #93). See `gap-space-parameterization.md` for related ordering trick.
- **Doesn't apply to fixed-geometry problems**: P15 Heilbronn n=11 is over-determined — adding n means adding points in a fixed region, KKT trap stays. The DoF-vs-active-constraint ratio is the discriminator.
- **Solutions must be downloadable**: cold-start at large n drifts to inferior basins. Always warm-start.

## Compute profile

Local CPU. FFT conv via `torch.fft.rfft/irfft` makes n=100k tractable on CPU in ~5 min. P4 cascade total: ~1 hr CPU for 1.52e-3 delta. GPU offers no benefit — sequential L-BFGS dominates.

## References

- `wiki/findings/equioscillation-escape.md` (lessons #51, #52, #94 — cascade recipe, "frozen" label test, parameterization companion).
- `wiki/findings/optimizer-recipes.md` (#93 v² parameterization escape).
- knowledge.yaml strategy `larger_n_escape_cascade` and pattern `larger-n-escape-for-equioscillation-basins`.
- `mb/tracking/problem-4-third-autocorrelation/strategy.md`, `mb/tracking/problem-2-first-autocorrelation/strategy.md`.
