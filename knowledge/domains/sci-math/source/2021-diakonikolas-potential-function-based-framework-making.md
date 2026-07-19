---
type: source
kind: paper
title: Potential Function-based Framework for Making the Gradients Small in Convex and Min-Max Optimization
authors: Jelena Diakonikolas, Puqian Wang
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2101.12101
source_local: ../raw/2021-diakonikolas-potential-function-based-framework-making.pdf
topic: general-knowledge
cites:
---

# Potential Function-based Framework for Making the Gradients Small in Convex and Min-Max Optimization

**Authors:** Jelena Diakonikolas, Puqian Wang  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2101.12101

## One-line
Introduces a unifying potential-function framework that explains why standard first-order methods make $\|\nabla f\|$ small as a trade-off between gradient norm and an optimality gap, covering gradient descent, Nesterov FGM, Kim-Fessler OGM, gradient descent-ascent, and Halpern iteration.

## Key claim
A single potential-function template $C_k = A_k \|\nabla f(x_k)\|^2 + B_k(f(x_k) - f(x^*))$ (and analogues for operators) recovers the known rates $\|\nabla f(x_k)\|^2 = O(L(f(x_0)-f^*)/k)$ for GD, $O(L(f(x_0)-f^*)/k^2)$ for FGM, and $O(L(f(x_0)-f^*)/k^2)$ for OGM via an elementary cocoercivity-only proof; for cocoercive operators, a new $\Omega(LD/\sqrt{K})$ lower bound for constant-step methods of the form $u_{k+1} = u_k - \sum_i \beta_{i,k} F(u_i)$ establishes that GDA / Krasnosel'skiı-Mann is optimal in that class and Halpern's $O(1/k)$ requires iteration-dependent step sizes.

## Method
Potential function $C_k$ combines a weighted gradient-norm term and a weighted optimality-gap term; one chooses weight sequences $\{A_k\}, \{B_k\}, \{a_k\}, \{b_k\}$ so that $C_{k+1} \le C_k$ (or telescopes) using only the cocoercivity characterization of smooth convex $f$ (Fact 1.1: $\frac{1}{2L}\|\nabla f(y) - \nabla f(x)\|^2 \le f(y) - f(x) - \langle \nabla f(x), y - x\rangle$). The min-max lower bound is built from the bilinear-plus-quadratic saddle $\phi(x,y) = \frac{\eta}{2}\|x\|^2 - \frac{\eta}{2}\|y\|^2 + \alpha x^Ty + b^Tu$, reducing iterate complexity to a polynomial-extremal problem $\sup_{\eta} L\eta |c_0'(\eta)|^{2K}$ controlled via a Lemma 3.6 polynomial bound.

## Result
For L-smooth convex $f$: GD gives $\|\nabla f(x_k)\|^2 \le \frac{2L(f(x_0)-f^*)}{2k+1}$; FGM gets $1/k^2$ via the same potential, OGM achieves $A_0 \ge (K+2)^2/4$ which translates to optimal $O(L(f(x_0)-f^*)/K^2)$ gradient norm. For $1/L$-cocoercive operators: any constant-step linear-combination method has worst-case $\|F(u_K)\| \ge \frac{LD}{\sqrt{80}\, p \sqrt{K}}$, while Halpern iteration with iteration-dependent anchoring achieves $O(1/k)$ — proving Halpern's step-size dependence on $k$ is necessary, not incidental.

## Why it matters here
General background; no direct arena tie. Most relevant if the agent ever needs gradient-norm (not function-value) convergence for an inner solver, or wants to understand why FGM is *not* the right outer loop when the stopping criterion is $\|\nabla f\| \le \epsilon$ — feeds the optimizer-selection corner of techniques/compute-router.

## Open questions / connections
- Extend the potential-function framework beyond Euclidean to general $\ell_p$ norms (only $p \in [1,2]$ and $\ell_\infty$ have near-optimal results, via regularization tricks [16,52]).
- Prove that fixing $N$ or $\epsilon$ in advance is necessary for $O(1/k^2)$ gradient norm in the convex case — the authors conjecture this; would require new lower-bound techniques.
- Lower bounds for gradient-norm minimization in convex-concave min-max outside the Euclidean setup are entirely open.

## Key terms
gradient norm minimization, potential function, cocoercive operator, smooth convex optimization, Nesterov fast gradient method, optimized gradient method, Kim-Fessler, Halpern iteration, Krasnosel'skiı-Mann, gradient descent-ascent, min-max optimization, monotone operator, lower bound, first-order method
