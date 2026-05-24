---
type: source
kind: paper
title: Marginal Probability-Based Integer Handling for CMA-ES Tackling Single-and Multi-Objective Mixed-Integer Black-Box Optimization
authors: Ryoki Hamano, Shota Saito, Masahiro Nomura, Shinichi Shirakawa
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2212.09260v2
source_local: ../raw/2022-hamano-marginal-probability-based-integer-handling.pdf
topic: general-knowledge
cites:
---

# Marginal Probability-Based Integer Handling for CMA-ES Tackling Single-and Multi-Objective Mixed-Integer Black-Box Optimization

**Authors:** Ryoki Hamano, Shota Saito, Masahiro Nomura, Shinichi Shirakawa  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2212.09260v2

## One-line
Fixes CMA-ES on mixed-integer/binary black-box problems by lower-bounding the marginal probability that each discrete variable can flip, preventing premature fixation when the sampling variance shrinks below the discretization granularity.

## Key claim
A simple affine correction — termed "CMA-ES with Margin" — that enforces $\min(\Pr([\bar v]_j = z_{j,k}), \Pr([\bar v]_j = z_{j,k+1})) \geq \alpha$ for every integer coordinate via diagonal matrix $A$ and mean-vector clipping, robustly solves binary-and-integer benchmarks (SphereOneMax, DSLOTZ, DSInt) where Hansen 2011's integer-mutation CMA-ES (CMA-ES-IM) stagnates. Recommended hyperparameter: $\alpha = (N\lambda)^{-1}$.

## Method
The sampling distribution is redefined as $\mathcal{N}(m, \sigma^2 A C A^\top)$ with $A^{(0)} = I$; CMA-ES updates of $m, C, \sigma$ are unchanged, and after each step (i) the diagonal entries of $A$ are scaled so the confidence interval $\mathrm{CI}_j(1-2\alpha) = \sqrt{\chi^2_{\mathrm{ppf}}(1-2\alpha)\,\sigma^2 (A C A^\top)_{jj}}$ around the nearest discretization threshold $\ell$ is wide enough, and (ii) the mean is clipped toward $\ell$ when it drifts too far. For multi-objective, the same `MarginCorrection` step is dropped into the elitist MO-CMA-ES of Igel/Voß. Affine-invariance of CMA-ES is preserved.

## Result
On 40-D SphereOneMax, CMA-ES-IM (with/without box constraint) fails because the coordinate-wise std for binary dims collapses while the mean is stuck far from the 0/1 threshold, and the geometric-distribution mutation injection in Step 1–6 produces displacements smaller than the mean-to-threshold gap. CMA-ES with Margin succeeds robustly across $N \in \{10,20,30\}$ and $\lambda \in \{10,50,100\}$. On bi-objective DSLOTZ at $N=30$, MO-CMA-ES without margin stagnates after ~400 iters as binary coordinates fix; with $\alpha=(N\lambda)^{-1}$ the hypervolume continues to climb, and NSGA-II underperforms because some final solutions drift outside the box. DSInt is easier (any one fixed integer still leaves a Pareto-optimal solution reachable), so margin gives smaller gains there.

## Why it matters here
Direct relevance to the einstein optimizer stack: CMA-ES-with-warmstart and basin-hopping-multistart pages (`docs/wiki/techniques/cma-es-with-warmstart.md`) assume continuous parameterizations, but several arena problems have discrete/integer choices buried in the configuration (lattice indices in kissing-number P23, contact-pattern integers in P18 circles-rectangle, combinatorial structure selection). When CMA-ES is used on such problems, premature variance collapse on the discrete dims is exactly the failure mode this paper diagnoses and patches.

## Open questions / connections
- Non-separable ill-conditioned MI problems (rotated Ellipsoid) remain unsolved — the diagonal-only $A$ correction does not couple integer dimensions.
- Alternative: joint MGD × Bernoulli distribution (PBIL hybrid) instead of continuous relaxation; balance between the two updates is open.
- Connects to PBIL's $[1/N, 1-1/N]$ marginal clipping (Baluja 1994) — same idea, lifted to MGD.
- For arena problems where integer choice is small-cardinality (binary contact-graph edges, lattice-vector signs), this is the right CMA-ES variant; current wiki has no entry on it.

## Key terms
CMA-ES, mixed-integer black-box optimization, marginal probability, integer handling, affine invariance, MO-CMA-ES, NSGA-II, population-based incremental learning, PBIL, evolution strategies, hypervolume, Hansen, covariance matrix adaptation, discrete relaxation, step-size adaptation
