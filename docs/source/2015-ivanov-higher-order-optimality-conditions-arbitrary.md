---
type: source
kind: paper
title: Higher-order optimality conditions with an arbitrary non-differentiable function
authors: Vsevolod I. Ivanov
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1511.09438v2
source_local: ../raw/2015-ivanov-higher-order-optimality-conditions-arbitrary.pdf
topic: general-knowledge
cites:
---

# Higher-order optimality conditions with an arbitrary non-differentiable function

**Authors:** Vsevolod I. Ivanov  ·  **Year:** 2015  ·  **Source:** http://arxiv.org/abs/1511.09438v2

## One-line
Constructs a new $n$-th order Hadamard-type directional derivative and subdifferential defined for *arbitrary* proper extended real functions, and derives matching necessary/sufficient conditions for local, strict-local, isolated-local-of-order-$n$, and global minimizers.

## Key claim
The recursively-defined lower Hadamard derivative $f_-^{(n)}(x; x_1^*, \ldots, x_{n-1}^*; u)$ (Def. 2.7) satisfies all four desired properties simultaneously — necessary+sufficient optimality, agreement with classical Fréchet derivative when it exists, definability for any proper extended real function, and extensibility to all orders $n$ — which no prior derivative (Studniarski, Demyanov, Ginchev, Dini, Rockafellar epi-derivative) achieves jointly. Theorem 5.1 gives a complete characterization of isolated local minimizers of order $n$; Proposition 5.5 shows Demyanov's $f_n^\downarrow(x) > 0$ is equivalent to this property.

## Method
Recursive construction: define $f_-^{(1)}$ as the lower Hadamard directional derivative, then build the order-$n$ derivative by subtracting off lower-order subdifferential elements inside a $\liminf_{t\downarrow 0,\, u'\to u}$ with the Hadamard joint convergence. Order-$n$ subdifferential $\partial_-^{(n)} f(x; x_1^*, \ldots, x_{n-1}^*)$ is the polar set of $n$-linear operators dominated by $f_-^{(n)}$. The framework also introduces "critical directions of order $m$" and "higher-order invex functions" — the largest class for which the necessary conditions become sufficient for global minima (Theorem 4.1).

## Result
- Theorem 3.1 (necessary): $\bar{x}$ local min $\Rightarrow 0 \in \partial_-^{(1)}f(\bar{x})$ and $0 \in \partial_-^{(n)}f(\bar{x}; 0,\ldots,0)$ for all $n \ge 2$.
- Theorem 3.3 (sufficient for strict local min): for every $u \ne 0$, either $f_-^{(1)}(\bar{x};u) > 0$ or some $n(u)$ exists with the order-$n(u)$ derivative strictly positive.
- Theorem 5.1: $\bar{x}$ is an isolated local minimizer of order $n$ iff Conditions (4) hold and $f_-^{(n)}(\bar{x};0,\ldots,0;d) > 0$ for every order-$(n{-}1)$ critical direction $d \ne 0$.
- Relation: $f_-^{(n)}(x;0,\ldots,0;u) = n!\, d_n f(x;u)$ (Studniarski), and $f_n^\downarrow(x) = \min_{u \in S} d_n f(x;u)$.
- Theorem 4.1: $f$ is invex of order $n$ iff every order-$n$ stationary point is a global minimizer.

## Why it matters here
General background; no direct arena tie. The framework is abstract nonsmooth optimization theory — relevant only if an arena problem requires certifying isolated local minimizers of order $n > 2$ for a non-smooth objective where Fréchet derivatives fail (e.g., a kink-laden penalty in a contact-graph polish). The "order-$n$ critical direction" idea has the flavor of higher-order basin-rigidity diagnostics but no concrete computational recipe is given.

## Open questions / connections
- No calculus rules (sum/chain) are derived — Property 5 from the paper's own desiderata is explicitly left open.
- Computational implementation of $f_-^{(n)}$ via a $\liminf$ over joint $(t, u')$ convergence is nontrivial; the paper gives no algorithm.
- Connects to Rockafellar's second-order epi-derivative (coincides under lower semicontinuity) and to higher-order invex / pseudoinvex theory (Ivanov 2013).
- Open: does this framework certify any of the per-problem fixed points encountered in P11/P15/P16 (active-pair / equioscillation polish) that the SLSQP tolerance misses?

## Key terms
higher-order optimality conditions, Hadamard directional derivative, subdifferential, isolated local minimizer of order n, strict local minimum, critical direction of order m, invex function, Fréchet derivative, Studniarski derivative, Demyanov derivative, Ginchev derivative, lower Dini derivative, Rockafellar epi-derivative, proper extended real function, nonsmooth optimization
