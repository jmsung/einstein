# Problem 4: Third Autocorrelation Inequality (Upper Bound)

**Status**: JSAgent **#1** — C ≤ 1.4525211550469 (n = 100,000)

## Problem

For f: [-1/4, 1/4] → ℝ (possibly signed), define the autoconvolution (f ⋆ f)(t) = ∫ f(t-x)f(x) dx. The third autocorrelation constant is:

C(f) = |max_t (f ⋆ f)(t)| / (∫f)²

Minimize C(f). Unlike the second autocorrelation (Problem 3), f can take negative values, enabling destructive interference in the autoconvolution. This is variant (b) of Problem 6.4 in Tao et al. (arXiv:2511.02864).

**Prior bounds**: C ≤ 1.45810 (literature, Ref 290) → C ≤ 1.4557 (AlphaEvolve) → **C ≤ 1.4525 (JSAgent)**

## Arena Details

- **API ID**: 4
- **Direction**: minimize
- **Solution format**: `{"values": [floats]}` — discretized f on [-1/4, 1/4] with dx = 0.5/n
- **Scoring**: `abs(np.convolve(f, f, mode='full').max() * dx) / (f.sum() * dx)**2`
- **minImprovement**: 1e-4
- **Note**: C is scale-invariant (f → c·f gives the same C for any c ≠ 0)

## Strategy & Insights

### The Key Observation: Equioscillation Traps

Before our work, multiple agents on the leaderboard were stuck in the same basin, with three byte-identical at C = 1.4540379299619. This looked like a theoretical bound — but it wasn't.

What actually happened: at n = 400 (the discretization everyone used), the optimal solution develops an equioscillation pattern — many autoconvolution positions simultaneously achieve the maximum to float64 precision, creating a saturated active set. The basin becomes fully rigid: no local perturbation can improve the objective without raising another constraint.

**Lesson**: A byte-identical tie across multiple independent agents is evidence of a discretization-level basin floor, not necessarily the continuous optimum. Always test whether going to larger n breaks the tie.

### The Breakthrough: Larger-n Escape via Block-Repeat

The escape exploits a simple algebraic fact: **block-repeat preserves the score exactly**. If you take an n = 400 solution and repeat each value 4 times to get n = 1600, the autoconvolution and integral scale identically, so C is unchanged. This means upsampling alone does nothing.

But block-repeat + tiny noise + re-optimization unlocks everything:

1. **Block-repeat**: v → np.repeat(v, k) from n = 400 to n = 1600
2. **Perturb**: Add Gaussian noise (σ ≈ 1e-6 · std(v)) to break the piecewise-constant constraint
3. **Optimize**: L-BFGS with smooth-max surrogate at n = 1600

The noise breaks the exact equioscillation pattern. At the larger n, L-BFGS has 1200 new degrees of freedom (the within-block variations) that were invisible at n = 400. These allow finer adjustments that reduce the autoconvolution peak without proportionally affecting the integral.

**Critical detail**: Linear or cubic interpolation (instead of block-repeat) strictly *worsens* the score — it blurs the piecewise-constant structure. Block-repeat is the correct upsampling because it preserves the original solution exactly.

### Resolution Cascade: Monotonic Improvement

We cascaded through progressively larger n, warm-starting each stage from the previous:

| n | C (exact) | Δ vs n=400 SOTA | CPU time |
|---|-----------|-----------------|----------|
| 400 | 1.4540379299619 | — (baseline) | — |
| 1,600 | 1.4535655501386 | 4.72 × 10⁻⁴ | ~1 min |
| 3,200 | 1.4530065851775 | 1.03 × 10⁻³ | ~5 min |
| 6,400 | 1.4527526158024 | 1.29 × 10⁻³ | ~18 min |
| 12,800 | 1.4526228187693 | 1.42 × 10⁻³ | ~8 min |
| 25,600 | 1.4525676100372 | 1.47 × 10⁻³ | ~9 min |
| 51,200 | 1.4525315813911 | 1.51 × 10⁻³ | ~5 min |
| **100,000** | **1.4525211550469** | **1.52 × 10⁻³** | ~5 min |

The gains diminish at each stage — characteristic of convergence toward a continuous limit. The total improvement (1.52 × 10⁻³) is 15× the minImprovement gate.

### Smooth-Max Surrogate: LogSumExp + Beta Cascade

The max in C(f) is non-differentiable, so L-BFGS needs a smooth proxy. We use:

C_smooth(f) = LSE_β(conv(f,f) · dx) / (Σf · dx)²

where LSE_β(v) = (1/β) · log Σ exp(β · v_i). As β → ∞, LSE → true max.

A **beta cascade** is essential — ramping β through stages rather than starting high:

- **Low β (1e4–1e5)**: Wide gradient support across many autoconvolution positions. L-BFGS explores broadly to find the right neighborhood.
- **Medium β (1e6–1e7)**: Gradient concentrates on the top ~10 positions. Fine-tuning.
- **High β (1e8–1e10)**: Near-exact max. Precision polishing at n = 100,000.

Starting directly at high β traps the optimizer — the gradient is too spiky for L-BFGS line search to make progress.

**Schedule**: β ∈ {1e4, 3e4, 1e5, 3e5, 1e6, 3e6, 1e7, 3e7} for n ≤ 51,200; extend to {…, 1e8, 3e8, 1e9, 1e10} at n = 100,000. Run 1,500–2,000 L-BFGS iterations per β stage with strong-Wolfe line search.

### FFT Convolution: Making Large n Tractable

At n = 100,000, direct convolution is O(n²) ≈ 10¹⁰ — impractical. We use `torch.fft.rfft/irfft` for O(n log n) autoconvolution. This makes each L-BFGS closure ~5ms at n = 100,000, and a full beta cascade runs in ~5 minutes on CPU (float64).

### Verification: Triple-Check Every Score

All scores are verified with three independent implementations before trusting:

1. `np.convolve(f, f, mode='full')` — arena's exact formula
2. `scipy.signal.fftconvolve(f, f)` — independent FFT implementation
3. O(n²) manual loop (for small n only)

Maximum inter-method disagreement: 4.44 × 10⁻¹⁶ (≈ 1 ULP of float64). If any two methods disagree by more than this, the score is not trusted.

### What Didn't Work

- **Direct optimization at fixed n = 400** — equioscillation lock makes this a dead end
- **Random restarts at any fixed resolution** — all roads lead to the same equioscillation pattern
- **Small perturbations of the equioscillated solution** — the stress network absorbs them elastically
- **Cold starts at large n (n ≥ 1,600)** — never find the basin neighborhood without warm-start
- **Linear/cubic interpolation for upsampling** — blurs structure, strictly worsens score
- **Jumping to high β directly** — gradient too spiky for L-BFGS; must cascade from low β

### Generalizable Lessons

1. **Block-repeat + noise is a general escape technique** for any discretized-function optimization where equioscillation traps form at fixed resolution. We expect it to work on Problems 1, 2, and 3 as well.
2. **Beta cascade is essential for any LogSumExp surrogate** — the anneal schedule matters more than the optimizer choice.
3. **"Frozen at theoretical bound" labels deserve skepticism** — a multi-agent tie at the same score is often a shared discretization basin, not a fundamental limit.
4. **Resolution is a free parameter** — the arena accepts any n. Don't assume the default discretization is optimal.

## Results

| Bound | Source | Value |
|-------|--------|-------|
| Literature (Ref 290) | de Dios Pont & Madrid | C ≤ 1.45810 |
| AlphaEvolve | Tao et al. | C ≤ 1.4557 |
| **JSAgent** | **This work** | **C ≤ 1.4525211550469** |

## Reproduction Recipe

```bash
# 1. Download arena SOTA as warm-start
curl "https://einsteinarena.com/api/solutions/best?problem_id=4&limit=1" > sota.json

# 2. Cascade through resolutions (each stage warm-starts from previous)
uv run python scripts/third_autocorrelation/optimize_torch.py \
    --n 1600 --start sota.json \
    --beta-cascade 1e4,3e4,1e5,3e5,1e6,3e6,1e7,3e7 --iters 1000

# 3. Switch to FFT optimizer at larger n
uv run python scripts/third_autocorrelation/optimize_fft.py \
    --n 3200 --start <prev_output> \
    --beta-cascade 1e4,3e4,1e5,3e5,1e6,3e6,1e7,3e7 --iters 1500

# 4. Continue cascade: n ∈ {6400, 12800, 25600, 51200, 100000}
# Each stage: block-repeat from previous, add 1e-6 noise, re-optimize
uv run python scripts/third_autocorrelation/optimize_fft.py \
    --n 100000 --start <prev_output> \
    --beta-cascade 1e4,3e4,1e5,3e5,1e6,3e6,1e7,3e7,1e8,3e8,1e9,1e10 \
    --iters 2000
```

Total wall time: ~50 minutes on CPU, entirely in float64.

## References

- Tao et al., *Mathematical exploration and discovery at scale* ([arXiv:2511.02864](https://arxiv.org/abs/2511.02864)), Problem 6.4 (variant b).
- de Dios Pont & Madrid, *On classical inequalities for autocorrelations and autoconvolutions* ([arXiv:2106.13873](https://arxiv.org/abs/2106.13873)).
- Matolcsi & Vinuesa (2009), *Improved bounds on autocorrelation inequalities* ([arXiv:0907.1379](https://arxiv.org/abs/0907.1379)).

## Infrastructure

- `src/einstein/third_autocorrelation/evaluator.py` — exact arena-matching evaluator
- `src/einstein/third_autocorrelation/optimizer.py` — shared surrogate / autograd helpers
- `scripts/third_autocorrelation/optimize_torch.py` — direct-conv optimizer (n ≤ 1600)
- `scripts/third_autocorrelation/optimize_fft.py` — FFT-conv optimizer (n ≥ 3200)
- `scripts/third_autocorrelation/submit.py` — pre-flight check, triple verification, and blocking leaderboard poll

*Last updated: 2026-04-13*
