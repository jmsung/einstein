---
type: source
kind: paper
title: Scale-free online learning
authors: Francesco Orabona, Dávid Pál
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1601.01974
source_local: ../raw/2016-orabona-scale-free-online-learning.pdf
topic: general-knowledge
cites:
---

# Scale-free online learning

**Authors:** Francesco Orabona, Dávid Pál  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1601.01974

## One-line
Designs FTRL and Mirror Descent variants for online linear optimization whose decisions are invariant to rescaling of the loss sequence, so no upper bound on $\|\ell_t\|_*$ needs to be known a priori.

## Key claim
SOLO FTRL with regularizer $R_t(w) = R(w)\sqrt{\sum_{i<t}\|\ell_i\|_*^2}$ (any $\lambda$-strongly convex $R$) achieves $\mathrm{Regret}_T(u) \le R(u) + \tfrac{2.75}{\lambda}\sqrt{\sum_t \|\ell_t\|_*^2} + 3.5\min(\sqrt{(T-1)/\lambda},\, D)\max_t \|\ell_t\|_*$ — the **first** non-vacuous adaptive bound on **unbounded** decision sets. Matched by $\Omega(\tfrac{D}{\sqrt 8}\sqrt{\sum_t \|\ell_t\|_*^2})$ lower bound.

## Method
Replace AdaGrad-FTRL's $\sqrt{\delta + \sum \|\ell_i\|_*^2}$ regularizer with the $\delta=0$ form, which makes predictions exactly homogeneous of degree 0 in the losses. New refined analysis avoids the off-by-one term that previously forced $\delta > 0$, using homogeneous inequalities (Lemmas 3, 7) of independent interest. Companion algorithms: Scale-Free MD (generalizing AdaGrad MD to any strongly convex regularizer; needs bounded Bregman divergence) and AdaFTRL (generalizing AdaHedge beyond entropy).

## Result
- SOLO FTRL: $O\!\left(\sqrt{\sup_{v\in K} f(v) \sum_t \|\ell_t\|_*^2}\right)$ on bounded sets with constant $13.3$; non-vacuous on unbounded $K=\mathbb{R}^d$ — open before this paper.
- Scale-Free MD: $O\!\left(\sqrt{\sup_{u,v} B_f(u,v) \sum_t \|\ell_t\|_*^2}\right)$, but $\Omega(T)$ on unbounded domains (proved via explicit Hedge-on-simplex and 1D counterexamples → FTRL strictly stronger than MD here).
- Lower bound: any OLO algorithm on a set of diameter $D$ incurs $\mathrm{Regret}_T \ge \tfrac{D}{\sqrt 8}\sqrt{\sum_t \|\ell_t\|_*^2}$ in expectation under Rademacher losses (Khinchin).

## Why it matters here
General background; no direct arena tie. Adjacent — closest relevance is methodological: the "design for scale invariance to remove a hyperparameter" pattern echoes the agent's need for tuning-free optimizer settings, and the $\sqrt{\sum \|\ell_t\|_*^2}$ adaptivity bound is the standard target the einstein optimizer rarely uses (we mostly do offline polish, not online).

## Open questions / connections
- Can the scale-free FTRL framework be extended to non-linear / second-order online optimization, retaining unbounded-domain guarantees?
- Proximal regularizers beyond the 2-norm — paper notes no general construction is known; this remains open.
- Connection to parameter-free online learning (Cutkosky, Orabona follow-ups): scale-freeness is a precondition for true parameter-free regret.

## Key terms
online linear optimization, OLO, regret bound, Follow the Regularized Leader, FTRL, Mirror Descent, scale-free, scale invariance, AdaGrad, AdaHedge, Bregman divergence, strongly convex regularizer, Fenchel conjugate, unbounded decision set, dual norm, Khinchin inequality, Orabona, Pál
