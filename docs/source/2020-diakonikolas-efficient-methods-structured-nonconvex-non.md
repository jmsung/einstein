---
type: source
kind: paper
title: Efficient Methods for Structured Nonconvex-Nonconcave Min-Max Optimization
authors: Jelena Diakonikolas, C. Daskalakis, Michael I. Jordan
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2011.00364
source_local: ../raw/2020-diakonikolas-efficient-methods-structured-nonconvex-non.pdf
topic: general-knowledge
cites:
---

# Efficient Methods for Structured Nonconvex-Nonconcave Min-Max Optimization

**Authors:** Jelena Diakonikolas, C. Daskalakis, Michael I. Jordan  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2011.00364

## One-line
Introduces a generalized extragradient method (EG+) that provably converges to stationary points of structured nonconvex-nonconcave min-max problems under a "weak Minty variational inequality" condition that is strictly weaker than assuming a Minty solution exists.

## Key claim
Under the weak-MVI Assumption 1 — $\exists u^* \in U^*$ such that $\langle F(u), u-u^*\rangle \geq -\tfrac{\rho}{2}\|F(u)\|_{p^*}^2$ for $\rho \in [0, \tfrac{1}{4L})$ — EG+ converges at rate $O(1/\sqrt{k})$ to an $\epsilon$-stationary point ($\|F(u)\|_{p^*} \leq \epsilon$), matching the best known rates for the *stronger* MVI-exists assumption while admitting non-monotone (cohypomonotone / negatively comonotone) operators.

## Method
A generalization of Korpelevich's extragradient algorithm with an "aggressive interpolation" step (EG+): the extrapolation step uses a parameter $\beta \in (0,1]$ that effectively under-relaxes the lookahead, sacrificing the monotone-case progress in exchange for tolerance to non-monotonicity. Extended to general $\ell_p$ normed spaces via Bregman / mirror-prox machinery (EGp+), and to stochastic oracle settings with explicit sample-complexity bounds.

## Result
Iteration complexity $O(1/\epsilon^2)$ for $p=2$ with $\rho \in (0, 1/(4L))$, matching prior $O(1/\epsilon^2)$ rates that required the stronger MVI assumption. For $\ell_p$, $p \in (1,2]$: same $O(1/\epsilon^2)$; for $p > 2$: $O(1/\epsilon^p)$, with explicit constants depending on $\|u^* - u_0\|_p$ and $L$. Stochastic variant achieves $O(1/\epsilon^2)\cdot(1 + \sigma^2/(L\epsilon^2(\bar\rho - \rho)))$ oracle queries. Accumulation points of iterates are shown to be SVI solutions.

## Why it matters here
General background; no direct arena tie. The Einstein Arena problems are scalar-objective optimization (sphere packing, autocorrelation, kissing numbers), not adversarial min-max games — extragradient / variational-inequality machinery doesn't apply to the current 23 problems. Potentially relevant only if a future arena problem framed adversarially (e.g., a primal-dual SDP solver for Cohn-Elkies LP bounds with non-monotone Lagrangian) needed a saddle-point optimizer.

## Open questions / connections
- Can the weak-MVI condition be relaxed further while preserving $O(1/\sqrt{k})$ tractability, given the PPAD-hardness of general smooth nonconvex-nonconcave min-max (Daskalakis-Skoulakis-Zampetakis 2021)?
- Extension to constrained settings (the unconstrained assumption is a real limitation — Malitsky 2019, Mertikopoulos et al. 2019 handle constraints under stronger assumptions).
- Connection to cohypomonotone operators (Combettes-Pennanen 2004) and negatively comonotone operators (Bauschke-Moursi-Wang 2020) — EG+ gives the first non-asymptotic rate for these classes.

## Key terms
extragradient method, EG+, variational inequality, Stampacchia VI, Minty VI, weak MVI, cohypomonotone, comonotone, nonconvex-nonconcave, min-max optimization, saddle point, mirror-prox, $\ell_p$ norm, stochastic oracle, Korpelevich, PPAD-hardness
