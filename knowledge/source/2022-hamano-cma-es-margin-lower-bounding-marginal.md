---
type: source
kind: paper
title: "CMA-ES with Margin: Lower-Bounding Marginal Probability for Mixed-Integer Black-Box Optimization"
authors: Ryoki Hamano, Shota Saito, Masahiro Nomura, Shinichi Shirakawa
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2205.13482v2
source_local: ../raw/2022-hamano-cma-es-margin-lower-bounding-marginal.pdf
topic: general-knowledge
cites:
---

# CMA-ES with Margin: Lower-Bounding Marginal Probability for Mixed-Integer Black-Box Optimization

**Authors:** Ryoki Hamano, Shota Saito, Masahiro Nomura, Shinichi Shirakawa  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2205.13482v2

## One-line
Modifies CMA-ES for mixed-integer black-box optimization by lower-bounding the marginal probability of each integer/binary coordinate to prevent premature fixation on a discretization plateau.

## Key claim
Inserting a diagonal affine factor $\mathbf{A}$ into the sampling distribution $\mathcal{N}(\mathbf{m},\sigma^2 \mathbf{A}\mathbf{C}\mathbf{A}^\top)$ and correcting $(\mathbf{m},\mathbf{A})$ each step so that $\Pr([\bar v]_j = z)\ge \alpha$ for every dominant integer value yields 100% success on SphereOneMax / LeadingOnes / Sphere/EllipsoidInt benchmarks at $N\in\{20,40,60\}$, where Hansen's CMA-ES-IM (with or without box constraint) drops to 0–80% as $N$ grows.

## Method
Discretize via thresholds $\ell_{j,k|k+1}=(z_{j,k}+z_{j,k+1})/2$, sample $\mathbf{v}_i=\mathbf{m}+\sigma\mathbf{A}\mathbf{y}_i$, evaluate $\bar{\mathbf{v}}_i=\mathrm{Encoding}_f(\mathbf{v}_i)$, and run vanilla CMA-ES updates on $(\mathbf{m},\mathbf{C},\sigma)$. After each step, for binary coords shift $[\mathbf{m}]_j$ toward the threshold using the chi-squared confidence interval $\mathrm{CI}_j(1-2\alpha)=\sqrt{\chi^2_{\mathrm{ppf}}(1-2\alpha)\,\sigma^2\langle\mathbf{A}\mathbf{C}\mathbf{A}^\top\rangle_j}$; for integer coords solve a 2x2 linear system in $([\mathbf{m}]_j,\langle\mathbf{A}\rangle_j)$ forcing both tail marginals $\ge\alpha/2$. Default $\alpha=(N\lambda)^{-1}$, mirroring PBIL's $[1/N,1-1/N]$ marginal clipping.

## Result
On 6 MI-BBO benchmarks (Sphere/Ellipsoid × OneMax/LeadingOnes/Int) at $N=20,40,60$ with $N_{\mathrm{co}}=N_{\mathrm{bi/int}}=N/2$, the proposed method holds 100/100 success across all 18 cells while CMA-ES-IM degrades sharply (e.g., EllipsoidLeadingOnes $N=40$: IM = 0/100, IM+box = 4/100, proposed = 100/100 at ~41k evals). On EllipsoidInt $N=60$ the proposed method reaches the optimum in ~42k evals vs ~89k for IM — roughly 2× faster *and* universally reliable. Affine invariance of CMA-ES is preserved since the correction is itself an affine map.

## Why it matters here
General background; no direct arena tie. Most arena problems are continuous; if a mixed-integer subproblem arose (e.g., choosing combinatorial structure + continuous coords jointly), this method is the state-of-the-art drop-in for CMA-ES — relevant to [[cma-es-with-warmstart]] and to any contact-graph / lattice-selection wrapper around continuous polish.

## Open questions / connections
- Authors flag non-separable ill-conditioned rotated-Ellipsoid MI problems (Tušar et al. 2019) as still unsolved — would require correlated multi-dimensional margin correction, not just diagonal $\mathbf{A}$.
- Connection to PBIL's marginal clamping $[1/N,1-1/N]$ suggests a unified "anti-fixation lower bound" view across EDAs and ES.
- Does the margin idea transfer to discrete-only optimizers (e.g., for kissing-number contact-graph search where each pair toggles in/out)?

## Key terms
CMA-ES, mixed-integer optimization, marginal probability lower bound, affine invariance, evolution strategies, integer mutation, PBIL, EDA, step-size adaptation, plateau stagnation, binary variables, discretization granularity
