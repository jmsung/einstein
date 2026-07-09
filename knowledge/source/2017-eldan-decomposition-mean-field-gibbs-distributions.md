---
type: source
kind: paper
title: Decomposition of mean-field Gibbs distributions into product measures
authors: Ronen Eldan, Renan Gross
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1708.05859
source_local: ../raw/2017-eldan-decomposition-mean-field-gibbs-distributions.pdf
topic: general-knowledge
cites:
---

# Decomposition of mean-field Gibbs distributions into product measures

**Authors:** Ronen Eldan, Renan Gross  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1708.05859

## One-line
Shows that Gibbs distributions on the Boolean hypercube whose Hamiltonian has low gradient complexity and Lipschitz gradient decompose into mixtures of product measures whose centers are approximate critical points of the mean-field functional.

## Key claim
For $f:\{-1,1\}^n\to\mathbb{R}$ with gradient complexity $D=D(f)$ (Gaussian width of $\{\nabla f(y)\}$), Lipschitz constant $L_1$, and gradient-Lipschitz constant $L_2$, the Gibbs measure $X_n^f \propto e^{f}$ is a $(\rho, 3D^{1/4}/n^{1/4}, L_2^{3/4}D^{1/4}/n^{1/4})$-tilt-mixture with $\rho$ supported (up to $o(1)$ mass) on $X$ satisfying the mean-field fixed-point $\|X-\tanh(\nabla f(X))\|_1 \le 5000\,L_1 L_2^{3/4} D^{1/4} n^{3/4}$.

## Method
Extends Eldan's earlier Gaussian-width / gradient-complexity framework (arXiv:1612.04346) by exploiting an additional Lipschitz bound on $\nabla f$. The proof builds an approximate fixed point: tilt the measure by a small $\theta\in B(0,\varepsilon\sqrt n)$, replace each tilted measure by the product measure $\xi_\theta$ with the same mean, and show the mean $A(\theta)=\mathbb{E}_{\tau_\theta\nu}[X]$ nearly solves $X=\tanh(\nabla f(X))$. A composition theorem (Theorem 14) lifts the result to $h\circ f$ for smooth $h$, enabling smoothed-cutoff Hamiltonians for large-deviation conditioning.

## Result
Critical points of $f(X)+H(X)$ (Hamiltonian plus binary entropy) characterize the mixture centers — directly the variational equation $\nabla_y H(y)=\lambda\nabla f(y)$ from the Lagrange multiplier formulation of the rate function. Applications: (i) Ising models with $\mathrm{Tr}\,A^2=o(n)$ decompose into product measures (Corollary 12); (ii) Curie–Weiss recovers known $\beta<1$ disorder phase (Corollary 13); (iii) conditional law $\Pr[Y=y\mid f(Y)\ge tn]$ under $\mu_p$ approximates as $(\rho,o(1))$-mixture of products satisfying $X=\tanh(\lambda\nabla f(X))$ (Theorem 16); (iv) triangle-count large deviations work down to sparse $p\sim n^{-c}$ (e.g. $n^{-1/160}$ for $\varepsilon=O(p)$).

## Why it matters here
General background; no direct arena tie. Closest links are conceptual: the variational / Lagrange-multiplier framing of extremal problems and the use of Gaussian-width complexity to control high-dimensional discrete optimization landscapes — both relevant idioms when an arena problem reduces to a discrete extremal computation over $\{-1,1\}^n$ or sparse-graph structures.

## Open questions / connections
- Conjecture (Example 17) that the set $X_g$ of mixture centers for triangle-count large deviations coincides with Lubetzky–Zhao's stochastic-block-model solutions (Random Struct. Alg. 2017).
- Extends Chatterjee–Dembo nonlinear large deviations (arXiv:1401.3495) to weaker complexity hypothesis ($D=o(n)$ via Gaussian width vs covering-number control).
- Sequel (Eldan–Gross arXiv:1707.01227) uses Theorem 9 to characterize exponential random graphs as mixtures of stochastic block models.
- Normalizing-constant approximation remains lossy by a factor $e^{o(n)}$ — sharp partition-function asymptotics still open.

## Key terms
Gibbs distribution, mean-field approximation, Boolean hypercube, gradient complexity, Gaussian width, tilt decomposition, product measure mixture, Ising model, Curie–Weiss, nonlinear large deviations, exponential random graphs, stochastic block model, Chatterjee, Dembo, Eldan, variational principle, Lagrange multiplier rate function, triangle counts sparse graphs
