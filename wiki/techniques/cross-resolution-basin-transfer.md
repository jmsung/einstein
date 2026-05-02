---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P3]
compute_profile: [local-cpu]
cost_estimate: "minutes — one downsample + Dinkelbach refinement"
hit_rate: "TBD"
---

# Cross-Resolution Basin Transfer

## TL;DR

When the target resolution `n` has a proven exhausted basin AND a higher-resolution solution exists (or is cheap to find), **average-pool the high-resolution solution to target `n` and refine** — it lands in a structurally distinct basin from the known target-n local maximum. Resolution is non-monotonic in optimization. P3 (Second Autocorrelation) used this for a 1.6M → 100k jump from 0.96199 to 0.96221 (rank #1).

## When to apply

- Discretized-function problem with a fixed target resolution `n` whose basin is exhausted (multistart at `n` returns the same local optimum).
- A higher-resolution version of the problem is feasible to solve (solver scales, OR you can warm-start at `kn` from the existing SOTA).
- The problem has structural features (block positions, peak shapes) that survive downsampling.
- Refinement at target `n` (Dinkelbach / smooth-max L-BFGS) is cheap.

## Procedure

1. **Solve at high resolution `kn`** (or warm-start from a high-resolution SOTA if available).
2. **Average-pool to target `n`**: `f_n = average_pool(f_kn, kernel=k)` (or sum-pool then renormalize — both give identical C under scale invariance).
3. **Confirm landing in a different basin**: compute `C(f_n)` and compare to the known target-n local max. If equal, the downsample landed in the same basin (rare but possible).
4. **Refine at target `n`** with the standard Dinkelbach + β-cascade pipeline. The refinement polishes within the transferred basin instead of searching from scratch.
5. **Triple verification**: convolution-based score with `np.convolve` + `scipy.fftconvolve` + manual loop.

```python
# Sketch: P3 cross-resolution transplant
v_high = solve_at_n(1_600_000)               # high resolution
v_target = average_pool(v_high, kernel=16)   # 1.6M → 100k
C_target = score(v_target)                   # compare to known 100k local max
v_target = dinkelbach_refine(v_target)       # polish within transferred basin
```

## Pitfalls

- **Naive interpolation does NOT transfer basins** the same way. Average-pool / sum-pool of high-res structures preserve dominant low-frequency features; bilinear interpolation can wash them out.
- **The reverse direction is multi-scale upsampling** (Jaech & Joseph 2025, P2): start small → 4× interpolate → refine. Different mechanism: explores combinatorially-cheaper small-n basins. Both work; pick based on which direction's compute is cheaper.
- **Target-n basin may be globally optimal** for some problems — non-monotonicity is a property, not a guarantee. Always test on a known case first.
- **High-res solve cost**: 1.6M-point Dinkelbach is expensive; only worth it if you have a cheap entry to high-res (warm-start from a published high-n SOTA, or amortize across multiple problems).
- **Block boundary artifacts**: average-pool at the wrong kernel size introduces spurious frequency content. Match the kernel to the structural period of the high-res solution.

## Compute profile

Local CPU. Downsample is O(n_high). Refinement at n=100k via Dinkelbach + β-cascade: ~5 min (FFT-conv).

## References

- `wiki/findings/optimizer-recipes.md` ("Cross-Resolution Basin Transfer" + "Multi-Scale Upsampling").
- `wiki/findings/equioscillation-escape.md` (#51 contrast: larger-n escape = upsample with perturbation; this = downsample for basin transfer).
- knowledge.yaml pattern `cross-resolution-basin-transfer`.
- `mb/wiki/problem-3-second-autocorrelation/strategy.md` (1.6M → 100k transplant + C(90,3) algebra).
- Jaech & Joseph 2025 autoconvolution paper (multi-scale upsampling, the dual direction).
