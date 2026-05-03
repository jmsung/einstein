---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: [kolountzakis-matolcsi-bound.md, autocorrelation-inequality.md]
related_problems: [P2, P3]
cites:
  - ../concepts/kolountzakis-matolcsi-bound.md
compute_profile: [local-cpu, modal-gpu]
cost_estimate: "minutes to hours; GPU only when float64 conv at large n"
hit_rate: "TBD"
---

# Dinkelbach Fractional Programming

## TL;DR

Convert a ratio objective `C = N(f) / D(f)` (hard, non-convex) into a parametric sequence of subtractive subproblems `max_f [N(f) − λ D(f)]` with iterated `λ ← N(f*) / D(f*)`. Add a smooth surrogate (LogSumExp) for L-infinity terms and a β-cascade for stability. Champion on autocorrelation P2/P3.

## When to apply

- Objective is a ratio of integrals / sums (autocorrelation: `C = ‖f★f‖₂² / (‖f★f‖₁ · ‖f★f‖∞)`; or `max(f★f)/(∫f)²`).
- Numerator and/or denominator are not jointly convex but quasiconvex in `f`.
- A smooth surrogate exists for any L-inf factor (LSE_β for max).
- Variable count is large (n ≥ 1000); Frank-Wolfe / cutting-plane LP is infeasible (P2 lesson #57).

## Procedure

1. **Initialize** `λ₀ = N(f₀) / D(f₀)` from a warm-start `f₀` (download SOTA when possible).
2. **Inner subproblem**: `max_f [N(f) − λ_t · D(f)]`.
   - Use L-BFGS on the smooth surrogate (LSE_β for `‖·‖_∞`).
   - Apply β-cascade: start low (β=1e4) for broad descent; anneal to high β (β=1e10) for precision.
3. **Outer update**: `λ_{t+1} = N(f*) / D(f*)`. Stop when `|λ_{t+1} − λ_t| < 1e-12`.
4. **Parameterization choice**: `f = v²` (square) or `f = exp(v)` — peak-locking is a real failure mode of `exp(v)` (lesson #93). Default to `v²` for autocorrelation problems.
5. **Triple verification**: convolution via `np.convolve` + `scipy.fftconvolve` + manual; disagreement ≤ 1 ulp.

```python
# Sketch (autocorrelation C2 / C3)
lam = N(f) / D(f)
for t in range(50):
    for beta in [1e4, 1e5, 1e6, 1e8, 1e10]:
        f = lbfgs(lambda f: -(N(f) - lam * D(f, beta)), f)
    lam_new = N(f) / D(f)
    if abs(lam_new - lam) < 1e-12: break
    lam = lam_new
```

## Pitfalls

- **β cascade is non-optional**: jumping to β=1e10 commits to the nearest local optimum of the smooth surrogate. Use stepwise annealing.
- **Quasiconvexity not always holds**: when `D(f) ≤ 0` enters the feasible set, Dinkelbach diverges. Restrict to the quasiconvex region or add a barrier.
- **Peak-locking via exp(v)** (P2 lesson #93): `exp(v)` parameterization peak-locks at delta~5e-8 from SOTA across all n and all optimizers. Switch to `v²` to escape.
- **Float64 ceiling at large n**: at n=100k, conv accumulation noise saturates around 1e-16. Final polish requires float64 GPU (Modal A100 with `torch.fft.rfft`) — but the DInkelbach iteration itself is sequential.
- **Initialization matters**: cold-start λ from random `f₀` typically lands in inferior basins. Always warm-start from SOTA.
- **Cutting-plane LP is the wrong tool at large n** (lesson #57): Kolountzakis-Matolcsi LP descends rapidly at n≤200 but stalls at n≥10k from a published SOTA — solver wall, not warm-start failure.

## Compute profile

- Local CPU: P2/P3 default. n=90k Dinkelbach + cascade: ~6 min for the long inner loop, plus ~10 outer iters.
- Modal GPU: only if the FFT conv at n=300k saturates float64 noise on CPU. Run benchmark first.

## References

- `wiki/findings/optimizer-recipes.md` (Dinkelbach + Adam peak-flatten + cross-resolution sections).
- `wiki/findings/equioscillation-escape.md` (#94 parameterization companion to larger-n cascade).
- `wiki/findings/lp-solver-scaling.md` (#47, #57 — when LP is the wrong tool).
- knowledge.yaml strategy `dinkelbach`.
- Source: Jaech & Joseph 2025, autoconvolution paper (`source/papers/2025-jaech-autoconvolution.md`).
- `mb/tracking/problem-2-first-autocorrelation/strategy.md`, `mb/tracking/problem-3-second-autocorrelation/strategy.md`.
