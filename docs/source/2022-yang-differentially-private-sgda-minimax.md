---
type: source
kind: paper
title: Differentially Private SGDA for Minimax Problems
authors: Zhenhuan Yang, Shu Hu, Yunwen Lei, Kush R. Varshney, Siwei Lyu, Yiming Ying
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2201.09046
source_local: ../raw/2022-yang-differentially-private-sgda-minimax.pdf
topic: general-knowledge
cites:
---

# Differentially Private SGDA for Minimax Problems

**Authors:** Zhenhuan Yang, Shu Hu, Yunwen Lei, Kush R. Varshney, Siwei Lyu, Yiming Ying  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2201.09046

## One-line
Establishes the first utility (generalization) bounds for differentially private stochastic gradient descent ascent (DP-SGDA) on minimax problems, in both convex-concave and nonconvex-strongly-concave settings.

## Key claim
DP-SGDA achieves the optimal weak primal-dual population risk rate $O(1/\sqrt{n} + \sqrt{d\log(1/\delta)}/(n\epsilon))$ under $(\epsilon,\delta)$-DP for convex-concave problems (smooth AND nonsmooth), and achieves excess primal population risk $O(1/n^{1/3} + \sqrt{d\log(1/\delta)}/n^{5/6})$ for nonconvex-strongly-concave problems under the PL condition — the first known DP-SGDA result in the nonsmooth and nonconvex regimes.

## Method
Algorithmic stability analysis: decompose the population risk into optimization error + generalization error, then bound each. Generalization is controlled via a *weak-stability* notion (for convex-concave) and via uniform argument stability + a quadratic-growth consequence of PL (for nonconvex). Privacy is obtained per-iteration via Gaussian gradient perturbation calibrated by the moments accountant (Abadi et al. 2016), with *separate* noise levels $\sigma_w,\sigma_v$ on primal/dual gradients matched to their distinct $\ell_2$-sensitivities.

## Result
**Convex-concave** (Thm 2): with $T \asymp n$ (smooth) or $T \asymp n^2$ (nonsmooth) and tuned $\eta$, the weak PD risk is $O(\max(1/\sqrt n, \sqrt{d\log(1/\delta)}/(n\epsilon)))$ — optimal, matching the convex-ERM lower bound, and improving Boob–Guzmán's NSEG complexity from $O(n^2)$ to $O(n^{3/2})$ in a single-loop algorithm. **Nonconvex-strongly-concave** (Thms 3–5): under PL + strong concavity, primal empirical risk converges at rate $O(\kappa^{3.5}/(\mu^{2.5} T^{2/3}))$ (new even non-privately, for the *last iterate*); combined with stability this gives excess primal population risk $O(n^{-1/3} + \sqrt{d\log(1/\delta)}/n^{5/6})$. Experiments on ijcnn1/MNIST/Fashion-MNIST AUC maximization confirm DP-SGDA dominates NSEG in AUC at matched $(\epsilon,\delta)$.

## Why it matters here
General background; no direct arena tie. Einstein Arena problems are deterministic math optimization (sphere packing, autocorrelation, kissing number), not ML training with privacy constraints — so DP-SGDA's privacy machinery doesn't apply. The only tangential connection is the *PL-condition convergence analysis for last-iterate SGD-style methods* (Thm 3 / Lemmas 9–11), which could distantly inform expectations about local-iterate convergence in basin-polish phases, but the wiki already has better-targeted material on basin rigidity and equioscillation.

## Open questions / connections
- Whether the coupled-recursion proof technique (tracking $a_t = R_S(w_t) - R_S^*$ and $b_t = \|v_t - \hat v_S(w_t)\|^2$ with weights $\lambda_t$) generalizes to other non-convex-non-concave settings beyond PL-SC.
- Bounding $\sup_{S,S'} \|\pi_{S'}(\pi_S(w_T)) - \pi_{S'}(w_T')\|$ under DP — left as an open problem to justify Assumption (A4) without uniqueness of saddle points.
- Extends Hardt–Recht–Singer (2016), Bassily et al. (2019, 2020), Lei–Ying (2020,2021), and Boob–Guzmán (2021) — closing the nonsmooth and nonconvex gaps in DP minimax theory.

## Key terms
differential privacy, DP-SGDA, stochastic gradient descent ascent, minimax optimization, convex-concave, nonconvex-strongly-concave, Polyak-Łojasiewicz condition, algorithmic stability, weak primal-dual risk, moments accountant, AUC maximization, GAN training
