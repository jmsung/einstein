---
type: finding
author: agent
drafted: 2026-05-02
status: answered
related_problems: [P3]
related_concepts: [autocorrelation-inequality.md, parameterization-selection.md]
related_findings: [optimizer-recipes.md, dead-end-p3-jaech-cascade-extended.md]
cites:
  - ../../mb/tracking/problem-3-autocorrelation/strategy.md
  - ../../source/papers/2026-rechnitzer-autoconvolution-digits.md
  - ../../source/papers/2025-jaech-autoconvolution.md
---

# P3 closed-form baseline: where simple constructions fall vs. the empirical ceiling and the trivial bound

## Question

How does the arena's empirical ceiling for P3 (Second Autocorrelation Inequality, $S(f) = \|f*f\|_2^2 / (\|f*f\|_1 \cdot \|f*f\|_\infty)$) compare against (a) closed-form non-negative densities and (b) the Cauchy–Schwarz trivial upper bound? The Rechnitzer 2026 paper's 128-digit value computes a *different* quantity ($\inf \|f*f\|_2^2$ for unit-mass $f$ ≈ 0.5746...), so it does not bound the arena's quantity. Without a published rigorous upper bound, we want at least an empirical landscape view of where 0.96272 sits.

## Method

Computed $S(f)$ at $n = 50\,000$ via the existing `einstein.autocorrelation.fast.fast_evaluate` for ~25 closed-form non-negative $f$ on $[-1/2, 1/2]$ scaled to unit mass. All computations finish in <2s on local CPU.

## Result

| Construction | $S(f)$ |
|---|---|
| `cos²(πx)` bump (smoothest unimodal) | **0.722** |
| Triangular tent | 0.719 |
| Uniform on $[-1/2, 1/2]$ | 0.667 |
| Rechnitzer minimizer $(1-4x^2)^{-1/2}$ | 0.574 |
| Two blocks at $\pm 3/8$, width $1/4$ | 0.500 |
| Beatty $K=32$ blocks | 0.500 |
| 16 equal blocks (gap ratio 0.3) | 0.521 |
| 64+ equal blocks (uniform spacing) | 0.444 |
| Exponentially-spaced blocks (varied) | 0.41–0.43 |

**Best closed-form $S$**: 0.722 (cos² bump). **Arena empirical ceiling**: 0.96272. **Trivial Cauchy–Schwarz upper bound**: 1.0.

## Interpretation

Three regimes separate cleanly:

1. **Smooth unimodal closed-forms** (uniform, triangular, cos², half-cosine): plateau at 0.67–0.72. These are the "natural" probability densities; their autoconvolutions are bell-shaped with $\|f*f\|_\infty$ moderate and $\|f*f\|_2^2$ moderate.
2. **Naive multi-block constructions** (equal-width, equal-height blocks, uniform or non-uniform spacing): consistently *worse* than unimodal, in the 0.44–0.52 range. Block structure by itself does not help — quite the opposite. The autoconvolution of a multi-block sum has many small peaks of varying height, none of which dominate cleanly, so $\|f*f\|_\infty / \|f*f\|_2^2$ is large.
3. **Tuned high-resolution arena solutions**: 0.96272. Reached only by the cross-resolution-transplant pipeline starting from ClaudeExplorer's 1.6M solution. The block heights, widths, and positions are *individually tuned* via Dinkelbach + L-BFGS to flatten $f*f$ globally.

The +0.24 jump from "best closed-form" 0.722 to "empirical ceiling" 0.96272 is therefore *all* tuned-block-heights wisdom from the arena's optimization campaign — there is no closed-form construction within reach of 0.96 by inspection.

The remaining 0.04 gap from 0.96272 to the trivial bound 1.0 is the "non-flatness tax" — even the best $f*f$ is not perfectly flat. *Empirical evidence (without proof) that the arena leaders are near the math ceiling*: every method tried plateaus at 0.96272 across $n \in \{100\text{k}, 400\text{k}, 800\text{k}, 1.6\text{M}\}$, with the same construction byte-similarity at the ceiling for all 11 leaderboard agents (per leaderboard inspection).

## What this answers

- The literature does *not* provide a rigorous upper bound on the arena P3 quantity (Rechnitzer 2026's 128-digit value is for $\inf \|f*f\|_2^2$, not for the arena's ratio).
- Closed-form constructions cap at 0.722 — the arena leaders' 0.24 of additional headroom comes entirely from optimization, not from a clever ansatz.
- The arena leaders are 0.04 below the trivial Cauchy–Schwarz bound 1.0 — suggestive but not proof of being near the math ceiling.

## What this does not answer

- The actual math ceiling. It lies in $(0.96272, 1.0]$, but the upper end of the interval is not known.
- Whether the arena leaders' specific 1.6M solution is the unique global maximizer or one of many basins (analogous to the P11 / P12 uniqueness questions).
- Whether a tighter rigorous upper bound is achievable by adapting Rechnitzer-style methodology (White's Fourier reformulation + truncated quadratically-constrained LP + interval arithmetic) to the arena's specific $L^2/(L^1 \cdot L^\infty)$ ratio.

## Path to a rigorous upper bound (sketch for future work)

The H3-cap path adapts Rechnitzer 2026 §2-3:

1. White-style Fourier reformulation: extend $f$ to $F$ on $(-1, 1)$, expand $\hat{F}(k)$ on integers. Compute $\|f*f\|_2^2 = \|F*F\|_2^2$ as a sum of $|\hat{F}(k)|^4$ terms (Rechnitzer eq. 8).
2. Sup-norm constraint: replace $\|f*f\|_\infty \leq C$ by an SOS (sum-of-squares) certificate that the trigonometric polynomial $C - (F*F)(x)$ is non-negative on $[-1, 1]$. This is a Toeplitz / Hankel positivity SDP. Cohn–Elkies-style.
3. Non-negativity constraint on $f$: similar Toeplitz-positivity SDP on $\hat{f}$.
4. Truncate the Fourier expansion to $|k| \leq T$, solve the resulting moment SDP via MOSEK or HiGHS at high precision (mpmath at 200–1024 dps).
5. Interval-arithmetic certification of the final upper bound.

Estimated implementation effort: 1–3 days of careful Fourier analysis + SDP coding + debugging. Worth doing if the user wants a published-quality wisdom artifact closing the H3 path on P3.

## Operational implication

JSAgent at rank #3 with 0.962214 is locked by the arena proximity-guard against the SOTA cluster (0.962643). Strategy.md verdict "Move on, this problem is solved to its practical limit" stands. The closed-form baseline diagnostic adds *quantitative* support to that verdict: 0.96272 is closer to the trivial UB than to any closed-form construction, so further empirical optimization is unlikely to yield > 1e-4 improvement.

The wisdom artifact for "ultimate limit" on P3 is now: *the empirical 0.96272 is closer to the Cauchy–Schwarz UB (gap 0.04) than to any tractable closed-form (gap 0.24). The arena leaders' tuning extracts all available headroom from the 1.6M-resolution basin. The math ceiling is not pinned.*
