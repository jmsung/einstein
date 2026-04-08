# Problem 4: Third Autocorrelation Inequality (Upper Bound)

**Status**: JSAgent holds rank #1

## Problem

For $f \colon [-1/4, 1/4] \to \mathbb{R}$ (possibly signed), define the
autoconvolution $f \star f$. The third autocorrelation constant is

$$
C(f) = \frac{\left|\max_{t}\,(f \star f)(t)\right|}{\left(\int f\right)^2}.
$$

The arena task is to find $f$ minimizing $C(f)$. Unlike the first autocorrelation
inequality, $f$ is allowed to take negative values, which permits destructive
interference in the autoconvolution and lower constants. This is variant (b) of
Problem 6.4 in the AlphaEvolve paper.

## Approach

- Downloaded the top entries on the leaderboard via the public
  `/api/solutions/best` endpoint to use as warm-starts.
- Built a verifier that matches the arena's scoring formula byte-for-byte
  (`abs(np.convolve(f,f).max() * dx) / (np.sum(f) * dx)**2`).
- Optimized a smooth-max relaxation of $C(f)$ with an L-BFGS beta cascade,
  warm-starting from a finer discretization of the downloaded construction.
- Verified the final score with three independent implementations
  (`np.convolve`, `scipy.signal.fftconvolve`, and a direct $O(n^2)$ loop) to
  rule out numerical artifacts before submitting.

## Infrastructure

- `src/einstein/third_autocorrelation/evaluator.py` — exact arena-matching evaluator
- `scripts/third_autocorrelation/optimize_torch.py` — smooth-max L-BFGS optimizer (direct conv)
- `scripts/third_autocorrelation/optimize_fft.py` — same optimizer with FFT-based convolution for larger $n$
- `scripts/third_autocorrelation/submit.py` — pre-flight check, triple verification, and blocking leaderboard poll

## Results

JSAgent achieved $C \approx 1.45252$ on the arena leaderboard, improving over
the previous best cluster at $\approx 1.45404$. This is below the
upper bound $C'_{6.4} \leq 1.4557$ reported for this variant in the
AlphaEvolve paper.

## References

- Tao et al., *Mathematical exploration and discovery at scale*
  ([arXiv:2511.02864](https://arxiv.org/abs/2511.02864)), Problem 6.4 (variant b).
- de Dios Pont & Madrid, *On classical inequalities for autocorrelations and
  autoconvolutions* ([arXiv:2106.13873](https://arxiv.org/abs/2106.13873)).
- Matolcsi & Vinuesa (2009) — improved bounds on autocorrelation inequalities
  ([arXiv:0907.1379](https://arxiv.org/abs/0907.1379)).

*Last updated: 2026-04-08*
