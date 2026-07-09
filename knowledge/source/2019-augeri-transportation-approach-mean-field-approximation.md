---
type: source
kind: paper
title: A transportation approach to the mean-field approximation
authors: F. Augeri
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1903.08021
source_local: ../raw/2019-augeri-transportation-approach-mean-field-approximation.pdf
topic: general-knowledge
cites:
---

# A transportation approach to the mean-field approximation

**Authors:** F. Augeri  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1903.08021

## One-line
Develops new transportation-entropy inequalities on the discrete hypercube and exponential measure that are saturated by tilted (affine log-density) measures, and uses them to derive a dimension-free mean-field approximation of Gibbs free energy.

## Key claim
For the Ising model on $\{-1,1\}^n$ with interaction matrix $J$ (zero diagonal), the mean-field approximation is within $O(\sqrt{n}\,\|J\|_2)$ of the free energy, where $\|J\|_2$ is the Hilbert-Schmidt norm — improving the prior $O((n\|J\|_2)^{2/3})$ bound of Jain-Koehler-Risteski.

## Method
Construct transportation-entropy inequalities $W_c(\nu,\tilde\mu) \le H(\nu|\mu)$ where the cost $c$ is chosen so equality holds for tilts of $\mu$ (product measures on the hypercube; scalings of the exponential). On the hypercube the cost couples $\nu \in P(\{-1,1\}^n)$ to the uniform measure on $[-1,1]^n$ via $w_p(x,u) = \sum_i 2|I_p'(u_i)|\mathbf{1}_{x_i(h_0-u_i)<0}$. By Kantorovich duality this yields a sub-Gaussian integrability bound $\log\int e^{\sup_{\xi\in V}\{\langle\xi,x\rangle - \Lambda_\mu(\xi)\}}d\mu \le \kappa\, b(V)$, where $b(V) = \mathbb{E}\sup_{\xi\in V}\langle\xi,\varepsilon\rangle$ is the Rademacher mean-width; Bednorz-Latała's characterization of Bernoulli processes converts this to a dimension-free constant.

## Result
Theorem 2.6: $\log\int e^f d\mu \le \sup_{y\in[-1,1]^n}\{f(y) - I(y)\} + \kappa\, b(\nabla f([-1,1]^n))$, with $b(V)$ the Rademacher mean-width (dimension-free — replaces the Gaussian mean-width $g(V)$ of Eldan's bound and removes its $n^{1/3}$ factor). Corollary 2.9 specializes to Ising: error $\kappa \|J\|_2 \sqrt{n}$. Also proves: (i) Prop 2.1 — exponential measure satisfies a tilt-saturated transport inequality with cost $\sum y_i\Lambda_\eta^*(x_i/y_i)$; (ii) Thm 2.12 — dimension-free nonlinear large-deviations bound; (iii) Prop 2.14 — reverse log-Sobolev inequality $I(\nu) \le H(\nu|\mu) + \kappa\sup_{y\in C^n}\int\langle\nabla f(y),x\rangle d\mu$ on the hypercube, analogous to Eldan-Ledoux's Gaussian version.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological — transportation-entropy inequalities and Rademacher mean-width as tools for bounding suprema of empirical processes, which could inform LP-duality / mean-width arguments in autocorrelation or sphere-packing contexts. The tilt-saturation idea (cost functions chosen so equality holds on the target submanifold) is a useful design principle for inequality-based bounds.

## Open questions / connections
- Extends Talagrand 1996 (Gaussian transportation) to Bernoulli/exponential; relates to Marton, Otto-Villani log-Sobolev ↔ transport equivalences.
- Improves on Chatterjee-Dembo nonlinear LDP, Eldan's Gaussian-width / decomposition bounds, Basak-Mukherjee, Jain-Koehler-Mossel/Risteski for Ising.
- Eldan's $p$-Schatten bound and Augeri's $\|J\|_2\sqrt{n}$ bound are incomparable for $p<2$ (e.g. Curie-Weiss / exponentially-decaying spectrum favors Eldan); unifying both is open.
- Could the tilt-saturated transport approach extend to non-product backgrounds (e.g. spherical measures relevant to sphere-packing LP duals)?

## Key terms
transportation-entropy inequality, mean-field approximation, Gibbs measure, Ising model, free energy, Rademacher mean-width, Bernoulli process, Talagrand inequality, log-Sobolev inequality, nonlinear large deviations, Hilbert-Schmidt norm, tilt-saturated cost, Bednorz-Latała, Augeri, Eldan, Chatterjee-Dembo
