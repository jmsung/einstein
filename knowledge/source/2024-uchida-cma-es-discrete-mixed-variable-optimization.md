---
type: source
kind: paper
title: CMA-ES for Discrete and Mixed-Variable Optimization on Sets of Points
authors: Kento Uchida, Ryoki Hamano, Masahiro Nomura, Shota Saito, Shinichi Shirakawa
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2408.13046v1
source_local: ../raw/2024-uchida-cma-es-discrete-mixed-variable-optimization.pdf
topic: general-knowledge
cites:
---

# CMA-ES for Discrete and Mixed-Variable Optimization on Sets of Points

**Authors:** Kento Uchida, Ryoki Hamano, Masahiro Nomura, Shota Saito, Shinichi Shirakawa  ·  **Year:** 2024  ·  **Source:** http://arxiv.org/abs/2408.13046v1

## One-line
Extends CMA-ES to optimize over search spaces where each coordinate block is a finite *set of arbitrary points* (not a grid), via Voronoi-based encoding plus an adaptive margin on the covariance matrix.

## Key claim
A new variant, **CMA-ES-SoP**, reliably solves discrete and mixed-variable optimization on sets of points where naive CMA-ES collapses: success rate 1.00 (vs 0.00 for naive CMA-ES) on 20- and 30-dim Sphere/Ellipsoid/Rosenbrock benchmarks, with the adaptive margin doing the heavy lifting in higher dimensions.

## Method
Three pieces bolted onto standard CMA-ES: (1) **sample encoding** — each sampled $x_k^{\langle i \rangle}$ is projected to its nearest point in subspace $S_k$ via the Voronoi diagram; (2) **margin correction** — after the usual update, $C^{(t+1)}$ is rank-1 modified along each direction $\xi_{k,b}$ pointing from the mean toward a neighboring Voronoi mid-point, forcing the marginal tail probability $p_{k,b}^{(t+1)} = \Phi_{\mathrm{cdf}}(-d_{k,b}) \geq \alpha_k^{(t)}$; (3) **margin adaptation** — $\alpha_k^{(t)}$ is multiplicatively driven by factor $\beta = 1+1/N$ so the *average* marginal probability tracks a target $\alpha_{\mathrm{target}} = 1/(N\lambda)$. Inherits CMA-ES-with-margin (Hamano et al. 2022) but generalizes from integer grids to arbitrary point sets.

## Result
On discrete benchmarks with $(N_k, L_k) \in \{(2,10),(5,40)\}$ and $N \in \{10,20,30\}$, CMA-ES-SoP hits success rate $\geq 0.96$ on all 18 settings, vs naive CMA-ES at $0.00$ on every $N \geq 20$ case. On mixed-variable Sphere/Ellipsoid/Reversed-Ellipsoid the gap grows with dimension: at $N=30$, SP1 (avg evals / success rate) for Sphere is $\sim 6{,}400$ (SoP) vs $\sim 120{,}000$ (CMA-ES). Margin adaptation strictly helps in high-D; fixed-margin ablation lags. Naive CMA-ES fails by premature collapse of the covariance eigenvalues around a non-optimal point.

## Why it matters here
General background for the agent's optimizer toolkit: relevant whenever a problem's decision space is a finite catalog of candidate configurations (not a grid, not continuous) — closest arena analogues are kissing-number / sphere-packing seed selection from a discrete codebook, or selecting from a precomputed library of configurations. No direct arena problem currently uses this; complements [[cma-es-with-warmstart]] and [[basin-hopping-multistart]] by adding a *categorical/set-valued* axis the existing CMA-ES wrapper doesn't handle.

## Open questions / connections
- Authors note step-size adaptation still assumes continuous space — could be re-engineered for sets-of-points geometry.
- Benchmark functions were lifted from continuous benchmarks; no native "sets-of-points" testbeds exist yet — open invitation for problem design.
- Factor $\beta = 1+1/N$ untuned; tuning may further widen the gap vs CMA-ES on Ellipsoid where naive method was occasionally competitive.
- Extends CMA-ES-with-margin (Hamano 2022) and DX-NES-ICI (Ikeda & Ono 2023) — same lineage, broader domain.

## Key terms
CMA-ES, covariance matrix adaptation, evolution strategy, margin correction, marginal probability, Voronoi diagram, discrete optimization, mixed-variable optimization, sets of points, premature convergence, Mahalanobis distance, rank-1 update, sample encoding, Hamano margin, black-box optimization
