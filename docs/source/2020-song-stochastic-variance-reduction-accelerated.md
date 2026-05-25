---
type: source
kind: paper
title: Stochastic Variance Reduction via Accelerated Dual Averaging for Finite-Sum Optimization
authors: Chaobing Song, Yong Jiang, Yi Ma
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2006.10281
source_local: ../raw/2020-song-stochastic-variance-reduction-accelerated.pdf
topic: general-knowledge
cites:
---

# Stochastic Variance Reduction via Accelerated Dual Averaging for Finite-Sum Optimization

**Authors:** Chaobing Song, Yong Jiang, Yi Ma  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2006.10281

## One-line
A simplified accelerated variance-reduction method (VRADA) that solves finite-sum convex optimization $\min_x \frac{1}{n}\sum g_i(x) + l(x)$ in $O(n\log\log n)$ stochastic gradient evaluations to reach $\Theta(L/n)$ accuracy, improving the prior $O(n\log n)$.

## Key claim
VRADA simultaneously matches the lower bounds in all three regimes — general convex, strongly convex with $n \le \Theta(\kappa)$, and strongly convex with $n \gg \kappa$ — up to a $\log\log n$ factor, achieving rates $O(n\log\log n + \sqrt{nL/\varepsilon})$ (general convex) and $O(n + \frac{n\log(n/\kappa)}{\log(n/\kappa)}\log(1/\varepsilon))$ (strongly convex, $n \gg \kappa$).

## Method
Two structural innovations: (1) **separate** Nesterov acceleration (outer loop, via uniform averaging of inner iterates) from variance reduction (inner loop, via SVRG-style $\tilde\nabla g_i = \nabla g_i(y) - \nabla g_i(\tilde x) + \nabla g(\tilde x)$); (2) use **accelerated dual averaging** with a generalized estimation sequence $\psi_{s,k}(z) := \psi_{s,k-1}(z) + a_s(g(y_{s,k}) + \langle \tilde\nabla_{s,k}, z-y_{s,k}\rangle + l(z))$ that accumulates strong convexity along the whole trajectory rather than only per-step. A novel initialization (one proximal gradient step + $\psi_{2,0} := m\psi_{1,1}$) cancels accumulated randomized error, yielding a superlinear initial phase $A_s \ge \frac{m}{2L}(2/m)^{2^{-(s-1)}}$.

## Result
Theorem 1: $\mathbb{E}[f(\tilde x_s)] - f(x^*) \le \|\tilde x_0 - x^*\|^2 / (2A_s)$ with $A_s$ growing superlinearly for $s \le 1 + \log_2\log_2(m/2)$ then accelerated sublinearly $A_s \ge \frac{m}{32L}(s-s_0+2\sqrt 2)^2$, and accelerated linearly $A_s \ge \frac{m}{4L}(1+\sigma m/(2L))^{s-s_0}$ in the strongly convex case. Setting $m = \Theta(n)$ yields the table-2 bounds; empirically beats Katyusha/MiG on a9a, covtype, mnist, cifar10 logistic regression across $\lambda \in \{0, 10^{-8}, 10^{-4}\}$.

## Why it matters here
General background; no direct arena tie — this is convex stochastic optimization for finite-sum ERM, not the smooth/non-convex / discrete-geometry / LP-bound regimes that Einstein Arena problems live in. The dual-averaging-accumulates-strong-convexity insight is a generic optimizer trick that *could* inform the agent's choice of solver for L-BFGS-style polishing of ERM-shaped sub-problems, but no current arena problem fits the $\frac{1}{n}\sum g_i$ form.

## Open questions / connections
- Can the superlinear initial-phase phenomenon (log log n passes to $\Theta(L/n)$ accuracy) be theoretically justified for vanilla SVRG, Katyusha, MiG — empirically all three exhibit it, but only VRADA proves it.
- Why does the without-replacement sampling assumption let VRADA beat the Lan-Zhou [20] lower bound $\Omega(n + \sqrt{n\kappa}\log(1/\varepsilon))$ by a $\log(n/\kappa)$ factor when $n \gg \kappa$? Connects to Hannah et al. [13] "breaking the span assumption" and SDCA's exclusion from this gain.
- The dual-averaging vs mirror-descent separation in acceleration mirrors the same split for deterministic Nesterov methods — open whether ADA-style accumulation helps in non-finite-sum settings the agent actually faces.

## Key terms
variance reduction, SVRG, Katyusha, accelerated dual averaging, Nesterov acceleration, estimation sequence, finite-sum optimization, ERM, strong convexity, condition number, stochastic gradient, mirror descent, lower bound matching, Lipschitz smoothness, proximal operator
