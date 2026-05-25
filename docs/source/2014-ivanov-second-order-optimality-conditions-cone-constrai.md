---
type: source
kind: paper
title: Second-Order Optimality Conditions in Cone-Constrained Vector Optimization with Arbitrary Nondifferentiable Functions
authors: Vsevolod I. Ivanov
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1411.4382v1
source_local: ../raw/2014-ivanov-second-order-optimality-conditions-cone-constrai.pdf
topic: general-knowledge
cites:
---

# Second-Order Optimality Conditions in Cone-Constrained Vector Optimization with Arbitrary Nondifferentiable Functions

**Authors:** Vsevolod I. Ivanov  ·  **Year:** 2014  ·  **Source:** http://arxiv.org/abs/1411.4382v1

## One-line
Introduces a new lower Hadamard-type second-order directional derivative that yields necessary and sufficient optimality conditions for arbitrary (possibly discontinuous) nondifferentiable functions, and extends them to cone-constrained vector optimization.

## Key claim
For any proper extended real function $f: E \to \mathbb{R} \cup \{+\infty\}$ and $\bar{x} \in \mathrm{dom}\, f$: $\bar{x}$ is an isolated local minimizer of second order iff $f^{(1)}_-(\bar{x};u) \ge 0$ for all $u$ and $f^{(2)}_-(\bar{x};0;u) > 0$ for all $u \ne 0$ (Theorem 2). The conditions require no smoothness, Lipschitz, or even semicontinuity assumptions, and reduce to the classical Fréchet second-order conditions when $f$ is twice Fréchet differentiable.

## Method
Defines $f^{(2)}_-(x; x_1^*; u) := \liminf_{t \downarrow 0,\, u' \to u} 2 t^{-2}[f(x+tu') - f(x) - t x_1^*(u')]$ where $x_1^*$ is a fixed element of the lower Hadamard subdifferential $\partial^{(1)}_- f(x)$. Key trick: replace $u$ by the Hadamard direction $u'$ inside the linear correction term, which keeps the derivative finite for arbitrary $f$ unlike Ginchev's earlier $f^{[2]}_G$ which blows to $-\infty$. Cone-constrained vector problems are reduced to a scalar penalty function $F(x) = \max\{\lambda \cdot [f(x)-f(\bar{x})] + \mu \cdot g(x) \mid (\lambda,\mu) \in \Lambda\}$ over polar-cone duals, then scalar Theorems 1–2 apply.

## Result
Theorems 1, 2 (unconstrained scalar); Theorem 3 (introduces 2-invex functions: every 2-stationary point is a global minimizer iff $f$ is 2-invex); Theorems 4, 5 (strongly pseudoconvex characterization of isolated 2nd-order minimizers); Theorems 6, 7 (cone-constrained vector necessary + sufficient). Section 7 shows that prior conditions of Bednařík–Pastor (l-stable), Ginchev–Guerraggio–Rocca ($C^{1,1}$), Hiriart-Urruty–Strodiot–Nguyen (generalized Hessian), Cominetti–Correa, Chaney, Huang–Ng, Ben-Tal–Zowe, Rockafellar (epi-derivatives), Yang–Jeyakumar, and others are corollaries of Theorems 1–2.

## Why it matters here
General background; no direct arena tie. None of the 23 Einstein Arena problems currently relies on nonsmooth second-order optimality theory — our optimizer stack uses L-BFGS / SLSQP / basin-hopping / mpmath polish on smooth or $C^{1,1}$ objectives where standard Hadamard/Dini conditions already suffice.

## Open questions / connections
- Could the 2-invex class (Theorem 3) certify global optimality of nonsmooth penalty reformulations used in P11 / P17 contact-graph problems?
- The strongly-pseudoconvex characterization (Theorem 5) reduces 2nd-order isolated-minimizer detection to a first-order subdifferential check — potentially relevant for verifying whether an SLSQP-polished point is genuinely isolated.
- Extends prior $C^{1,1}$ literature to functions that are not even semicontinuous; mostly of theoretical interest until we hit a problem where the local evaluator is discontinuous.

## Key terms
lower Hadamard derivative, second-order subdifferential, isolated local minimizer of order two, 2-invex function, strongly pseudoconvex, cone-constrained vector optimization, l-stable function, epi-derivative, Dini derivative, generalized Hessian, $C^{1,1}$ optimization, nonsmooth optimality conditions
