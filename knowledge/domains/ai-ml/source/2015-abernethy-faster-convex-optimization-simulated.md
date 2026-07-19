---
type: source
kind: paper
title: "Faster Convex Optimization: Simulated Annealing with an Efficient Universal Barrier"
authors: Jacob D. Abernethy, Elad Hazan
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1507.02528
source_local: ../raw/2015-abernethy-faster-convex-optimization-simulated.pdf
topic: general-knowledge
cites:
---

# Faster Convex Optimization: Simulated Annealing with an Efficient Universal Barrier

**Authors:** Jacob D. Abernethy, Elad Hazan  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1507.02528

## One-line
Proves that simulated annealing's "heat path" coincides with the central path of an interior-point method using the entropic universal barrier, yielding a faster membership-oracle convex optimizer.

## Key claim
For convex optimization over a bounded $K \subset \mathbb{R}^n$ accessed only by a membership oracle, simulated annealing with a tightened temperature schedule $t_k = (1 - \tfrac{1}{4\sqrt{\nu}}) t_{k-1}$ runs in $\tilde{O}(\sqrt{\nu}\, n^4)$ time, improving the Kalai–Vempala $\tilde{O}(n^{4.5})$ bound by a factor of $\tilde{O}(\sqrt{n/\nu})$, where $\nu$ is the self-concordance parameter of the entropic barrier ($\nu \le n(1+o(1))$, often much smaller for structured cones — e.g. $\nu = n$ for the PSD cone vs. naive $n^2$).

## Method
Identify the entropic barrier $A^*_-(x) = \sup_\theta\{-\theta^\top x - \log\int_K e^{-\theta^\top y}dy\}$ (Bubeck–Eldan) as a $\nu$-self-concordant barrier whose gradient map sends $\theta \mapsto \mathbb{E}_{X\sim P_\theta}[X]$, so computing barrier-central-path iterates is equivalent to estimating Boltzmann means via Hit-and-Run sampling. Use Nesterov–Nemirovskii damped-Newton invariants (Newton-decrement $\lambda(x,t)<1/3$, Lemmas 1–3) to bound the KL/$\chi^2$ divergence between successive Boltzmann distributions $P_\theta$ and $P_{(1+\gamma)\theta}$, certifying the Kalai–Vempala $\ell_2$-closeness condition with the new, more aggressive schedule.

## Result
Theorem 4: the schedule $\theta_k = (1 - \tfrac{1}{4\sqrt{\nu}})\theta_{k-1}$ satisfies the $\ell_2$-mixing condition $\max\{\|P_\theta/P_{\theta'}\|_2, \|P_{\theta'}/P_\theta\|_2\}\le 10$, giving an $\epsilon$-approximate solution in $\tilde{O}(\sqrt{\nu}\, n^4)$ time. Corollary 2 establishes HeatPath $\equiv$ CentralPath$(A^*_-)$ as geometric curves. Consequence: the first efficiently *computable* universal self-concordant barrier for arbitrary convex $K$ given only a membership oracle (implicit access via sampling).

## Why it matters here
General background; no direct arena tie — Einstein Arena problems don't currently route through membership-oracle convex optimization at this scale. Could inform any future workload that builds a barrier-based polish on a set defined only by feasibility checks (e.g., LP/SDP relaxations in P1 sphere-packing flag algebras), and reinforces the entropic-barrier $=$ log-determinant identification for PSD cones.

## Open questions / connections
- When is $\nu$ for the entropic barrier strictly $o(n)$ on cones relevant to arena problems (PSD, Lorentz, $\ell_p$-balls)?
- Can the heat-path/central-path equivalence be exploited to *warm-start* an SDP polish from MCMC samples on the feasible set?
- Extends Kalai–Vempala (2006) and Narayanan–Rakhlin (2010); leaves open whether the $\tilde{O}(n^4)$ Hit-and-Run mixing cost itself can be tightened with isotropic preconditioning.

## Key terms
simulated annealing, entropic barrier, universal barrier, self-concordance, interior point method, central path, heat path, Hit-and-Run, Boltzmann distribution, Newton decrement, Fenchel dual, log-partition function, Kalai–Vempala, Bubeck–Eldan, membership oracle, PSD cone, Lorentz cone
