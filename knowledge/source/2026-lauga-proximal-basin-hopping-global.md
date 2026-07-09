---
type: source
kind: paper
title: Proximal basin hopping: global optimization with guarantees
authors: Guillaume Lauga, Cesare Molinari, Samuel Vaiter
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2605.18364v1
source_local: ../raw/2026-lauga-proximal-basin-hopping-global.pdf
ingested_for_concept: basin-hopping-multistart.md
cites: 
---

# Proximal basin hopping: global optimization with guarantees

**Authors:** Guillaume Lauga, Cesare Molinari, Samuel Vaiter  ·  **Year:** 2026  ·  **Source:** http://arxiv.org/abs/2605.18364v1

## One-line
A hybrid global optimizer combining proximal operators with basin hopping that provably converges to the global minimizer with high probability using finitely many samples.

## Key claim
Proximal Basin Hopping (PBH) — built around the operator $S^\gamma_f(x) := \mathrm{prox}_{\gamma T_f \circ f}(x) \approx T_f(\mathrm{prox}_{\gamma(f \circ T_f)}(x))$ — converges to the unique global minimizer $x^*$ under coercivity, polynomial growth ($C_1\|z\|^\alpha - C_2 \le f(z) \le C_3(1+\|z\|)^\beta$), and a value-gap assumption ($f_{\min} + \mu < f(M)$ for all non-global local minimizers $M$), even with finite sample size $N$ and inexact local solvers — and outperforms basin hopping and zeroth-order prox on Rastrigin, Griewank, Lennard-Jones, and deep-learning scaling-law fitting, with the gap widening in higher dimension.

## Method
Replaces the ideal proximal step on $f \circ T_f$ (where $T_f$ is a deterministic local solver mapping to attractors $\mathrm{Att}(M)$) with a zeroth-order Gaussian smoothing: draw $N$ samples $y_i \sim \mathcal{N}(x, \delta\gamma I_d)$, locally minimize each, take the temperature-weighted barycenter $\sum T_f(y_i) e^{-f(T_f(y_i))/\delta} / \sum e^{-f(T_f(y_i))/\delta}$, then re-minimize. The schedule increases $\gamma$ (basin width) on non-improvement and decreases $\delta$ (temperature) each step; proofs use Gaussian large-deviations on $V_x(M) := f(M) + \tfrac{1}{2\gamma}\mathrm{dist}(x, \mathrm{Att}(M))^2$ to show concentration of the weighted barycenter on $\arg\min V_x$ as $\delta \downarrow 0$.

## Result
Four nested convergence theorems: ideal PBH converges in finite iterations (Thm 1); exact-expectation PBH converges as $\delta \to 0$ (Thm 2); approximate-expectation PBH converges with $N \to \infty$ (Thm 3) and with finite $N$ w.h.p. via $P(\|m_{N,\delta,\gamma} - m_{\delta,\gamma}\| \le \varepsilon) \ge 1 - \alpha(\varepsilon)/N$ (Thm 4, Prop 3); inexact-solver variant converges if $\varepsilon/\delta \to 0$ and $\|T_f^\varepsilon - T_f\| \to 0$ uniformly. Empirically PBH dominates BH and ZOP up to $d=200$, with $N=5$–$15$ samples sufficient on scaling-law fits ($d \le 47$).

## Why it matters here
Directly relevant to the agent's optimizer toolkit for problems with many local minima — sphere-packing configurations (P1), Hardin-Sloane–style point clouds (P11), Lennard-Jones-like geometric packings, and any landscape where basin hopping is currently used; PBH offers a principled, parallelizable, theoretically-grounded upgrade with a finite-sample probabilistic guarantee.

## Open questions / connections
- Does PBH outperform parallel tempering and CMA-ES (not benchmarked here) on float64 Einstein Arena problems?
- The value-gap assumption ($f_{\min} + \mu < f(M)$ on non-global local mins) — how to estimate $\mu$ a priori for sphere packing / kissing / autocorrelation landscapes?
- Extension to aggregation of top-$k$ samples vs. weighted barycenter (acknowledged limitation) — could improve robustness when multiple competitive basins exist.
- Connections to Zhang et al. 2024 zeroth-order prox and Wales-Doye 1997 basin hopping; opens path to quantify sample-size × inexactness trade-off in existing local-min-search workflows.

## Key terms
proximal basin hopping, global optimization, basin hopping, zeroth-order proximal, Gaussian smoothing, large deviations, attractor basin, local minimizer, gradient descent, Lennard-Jones cluster, Rastrigin function, Griewank function, scaling laws, Wales-Doye, non-convex optimization
