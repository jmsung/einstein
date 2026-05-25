---
type: source
kind: paper
title: "The Power of Sampling: Dimension-free Risk Bounds in Private ERM"
authors: Yin Tat Lee, Daogao Liu, Zhou Lu
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2105.13637
source_local: ../raw/2021-lee-power-sampling-dimension-free-risk.pdf
topic: general-knowledge
cites:
---

# The Power of Sampling: Dimension-free Risk Bounds in Private ERM

**Authors:** Yin Tat Lee, Daogao Liu, Zhou Lu  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2105.13637

## One-line
A regularized exponential-mechanism sampler achieves dimension-free risk bounds for non-smooth convex DP-ERM using only zeroth-order oracles, and a matching lower bound shows constrained/unconstrained settings are equivalent under full-rank gradients.

## Key claim
Under unconstrained domain (Assumption 1.2) and Restricted Lipschitz Continuity (Assumption 2.1, gradient mass mostly in a rank-$k$ subspace with residual $G_k$), sampling $\theta \propto \exp(-\eta(L(\theta;D) + \tfrac{\mu}{2}\|\theta\|_2^2))$ is $(\epsilon,\delta)$-DP and achieves expected excess risk $\tilde O\!\left(\frac{GC\sqrt{k\log(1/\delta)}}{n\epsilon}\right)$ using only $\tilde O(n^2\epsilon^2)$ zeroth-order calls. A matching lower bound $\Omega(\min(1, \sqrt{d\log(1/\delta)}/(n\epsilon))\,GC)$ holds for any $\ell_p$ geometry ($p\ge 1$) in *both* constrained and unconstrained settings.

## Method
Upper bound: regularized exponential mechanism (Gibbs sampling from a strongly log-concave density) with privacy from Gopi et al. 2022; utility from a new variance decomposition that conditions on the "tail" coordinates ($x_2$), bounds $\mathrm{Var}_{x_1|x_2}f$ by rank $k$ via a projected second-moment lemma $\mathbb{E}\|Q(x-x^*)\|_2^2 \le k/\mu$, and shows the outer variance over $x_2$ vanishes. Lower bound: a black-box reduction (projection + Pythagorean inequality on the $\ell_2$-ball plus a soft-clip Moreau-style envelope $\tilde\ell(\theta;z)=\min_{y\in K}\ell(y;z)+G\|\theta-y\|_2$) lifts constrained lower bounds to unconstrained, combined with an $\ell_1$-loss fingerprinting-code construction extending Bassily et al. 2014 / Steinke–Ullman 2016.

## Result
Theorem 2.2: dimension-free upper bound $\tilde O(GC\sqrt{k\log(1/\delta)}/(n\epsilon))$ for any $k$ with $G_k \lesssim G\sqrt{d}/(n\epsilon)$ — matches DP-SGD bounds of Song et al. 2021 / Li et al. 2022 but without smoothness or first-order oracles. Theorem 3.7/3.9: $\Omega(\sqrt{d\log(1/\delta)}/(n\epsilon))$ lower bound holds for unconstrained DP-ERM and across all $\ell_p$ geometries $p\ge 1$, improving Asi et al. 2021's $\ell_1$-only result and proving no constrained-vs-unconstrained separation when gradients are full-rank.

## Why it matters here
General background; no direct arena tie — this is a differential-privacy / optimization paper, not a math-olympiad-style extremal problem. Tangentially relevant only as a methodological reference: log-concave sampling as an alternative to gradient descent, and fingerprinting-code lower bounds as a packing/coding-theory technique that resembles arguments used in autocorrelation/Sidon lower bounds.

## Open questions / connections
- Can the $\tilde O(n^2\epsilon^2)$ oracle complexity be reduced, or is it tight for zeroth-order DP-ERM?
- Does the rank-dependent bound extend to non-Euclidean ($\ell_p$, $p\ne 2$) geometries on the upper-bound side, closing the $p>2$ gap noted in related work?
- Tight DP-SCO bounds in $\ell_p$ geometry for $p>2$ remain open; this paper's improved lower bound tightens the gap but doesn't close it.
- Whether log-concave Langevin/Gibbs samplers can replace SGD more broadly in private optimization pipelines.

## Key terms
differential privacy, DP-ERM, exponential mechanism, regularized sampling, log-concave sampling, dimension-free risk bound, low-rank gradients, Restricted Lipschitz Continuity, zeroth-order oracle, fingerprinting codes, black-box reduction, $\ell_p$ geometry, Lee, Liu
