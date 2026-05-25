---
type: source
kind: paper
title: Near-Optimal Methods for Minimizing Star-Convex Functions and Beyond
authors: Oliver Hinder, Aaron Sidford, N. Sohoni
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1906.11985
source_local: ../raw/2019-hinder-near-optimal-methods-minimizing-star-convex.pdf
topic: general-knowledge
cites:
---

# Near-Optimal Methods for Minimizing Star-Convex Functions and Beyond

**Authors:** Oliver Hinder, Aaron Sidford, N. Sohoni  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1906.11985

## One-line
Accelerated first-order method for minimizing smooth functions that are unimodal along every line through a global minimizer (γ-quasar-convex), with matching lower bounds.

## Key claim
For $L$-smooth $\gamma$-quasar-convex $f$ with initial distance $R$ to optimum, an $\epsilon$-minimizer is found in $O(\gamma^{-1} L^{1/2} R \epsilon^{-1/2} \log(\gamma^{-1}\epsilon^{-1}))$ function+gradient evaluations; a lower bound of $\Omega(\gamma^{-1} L^{1/2} R \epsilon^{-1/2})$ shows this is tight up to a log factor.

## Method
Generalize AGD's momentum step: at each iterate, the momentum parameter $\alpha^{(k)}$ is computed by a 1-D **binary line search** on the segment between $x^{(k)}$ and $v^{(k)}$ to satisfy an inequality that convexity would give for free. A constructive existence lemma (Lemma 2) shows a valid $\alpha$ always exists; the line-search runtime contributes only the $\log$ factor. Strongly quasar-convex ($\mu>0$) variant gives $O(\gamma^{-1}\kappa^{1/2}\log(\gamma^{-1}\epsilon^{-1}))$ iterations with $\kappa=L/\mu$.

## Result
Theorem 1 (strongly quasar-convex): $O(\gamma^{-1}\kappa^{1/2}\log(\gamma^{-1}\kappa)\log(\gamma^{-1}\epsilon^{-1}))$ evaluations. Theorem 3 (lower bound): any deterministic first-order method needs $\Omega(\gamma^{-1}L^{1/2}R\epsilon^{-1/2})$ gradient calls on this class, proved by adapting the Carmon–Duchi–Hinder–Sidford zero-chain construction with the Nesterov chain quadratic $q$ and the $\Upsilon$ bump. Improves on Hardt et al.'s $O(\gamma^{-1})$-iteration bound (matches) and Nesterov-Polyak $O(\gamma^{-3/2})$ (beaten by factor $\gamma^{1/2}$).

## Why it matters here
General background; no direct arena tie — this is a nonconvex-optimization complexity result. Tangentially relevant if any arena problem reduces to minimizing a structured nonconvex objective with a known-good basin (e.g., learning-linear-dynamical-systems-style targets in the multistart/basin-hopping regime), where star-convexity around a candidate optimum could justify cheap accelerated polish instead of full SA/CMA-ES.

## Open questions / connections
- Extends Nesterov–Polyak star-convexity [47] and Hardt et al.'s weak-quasi-convexity [29]; supersedes the subspace-search method of [26] and line-search-with-known-$f^*$ method of [48].
- Can the $\log(\gamma^{-1}\epsilon^{-1})$ factor be removed to match the lower bound exactly?
- Does the "robustified AGD" interpretation (use standard-AGD $\alpha$ as guess; fall back to binary search only on convexity violations) extend to stochastic / proximal / higher-order settings?
- Connection to PL condition, one-point convexity, variational coherence, restricted strong convexity — all sit in the same "structured nonconvex" landscape.

## Key terms
quasar-convex, star-convex, weak quasi-convexity, accelerated gradient descent, AGD, Nesterov acceleration, momentum binary line search, Polyak-Łojasiewicz, strong quasar-convex, condition number, first-order lower bound, zero-chain construction, smooth nonconvex optimization, Hinder, Sidford
