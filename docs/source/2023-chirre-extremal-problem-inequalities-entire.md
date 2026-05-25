---
type: source
kind: paper
title: An extremal problem and inequalities for entire functions of exponential type
authors: Andrés Chirre, Dimitar K. Dimitrov, Emily Quesada-Herrera, Mateus Sousa
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2304.05337v2
source_local: ../raw/2023-chirre-extremal-problem-inequalities-entire.pdf
topic: general-knowledge
cites: 
---

# An extremal problem and inequalities for entire functions of exponential type

**Authors:** Andrés Chirre, Dimitar K. Dimitrov, Emily Quesada-Herrera, Mateus Sousa  ·  **Year:** 2023  ·  **Source:** http://arxiv.org/abs/2304.05337v2

## One-line
Studies two variations of the classical Carathéodory–Fejér–Turán one-delta problem for entire functions of exponential type: a monotone-delta variant requiring radial decrease, and a derivative-weighted variant minimizing sums of $L^2$-norms of $g$ and its derivatives.

## Key claim
For the monotone-delta constant $A_1 = \inf_{f \in \mathcal{F}_1, f(0) \neq 0} \|f\|_1/f(0)$ (over radially-decreasing nonnegative entire functions of exponential type $\leq 2\pi$), proves $1.2750 < A_1 < 1.27714$ and conjectures $A_1 = 1.277135042\ldots$ to 9 digits. Establishes Theorem 2: a Duffin–Schaeffer-style $L^2$ inequality $\left(\int_0^1 P(t^2)^{-1} dt\right)^{-1} \leq \sum_{n=0}^N \frac{a_n}{\pi^{2n}} \int |g^{(n)}|^2 dx$ for any positive polynomial $P$, with explicit extremizer $g(z) = \int_0^1 \cos(\pi z t) P(t^2)^{-1} dt / \int_0^1 P(t^2)^{-1} dt$.

## Method
Reformulates the monotone-delta problem via a Krein-decomposition lemma into $A_1 = \inf \int x^2|h|^2 dx / (\int |x||h|^2 dx)^2$ over Paley–Wiener-like class $\mathcal{F}_2$. Two computational approaches: (1) an $L^2$ approach using a complete orthonormal system $h_k(x) = \frac{4\sqrt{2}}{\pi}\cos(\pi x)/((2k-1)^2 - 4x^2)$, reducing to a largest-eigenvalue problem on a matrix $Q$ with explicit entries involving $\mathrm{Si}(\pi(2k-1))$, with rigorous Arb-library ball arithmetic; (2) polynomial parameterization $h = \sqrt{1/4 - x^2}\, g(x)\chi_I$ with smooth optimization over $\mathbb{R}^{d+1}$. Theorem 2 follows by Plancherel + Cauchy–Schwarz on the Paley–Wiener support $[-1/2, 1/2]$.

## Result
Polynomial approach converges faster: degree-20 polynomial gives $A_1 \leq 1.277135052$ vs $L^2$ approach at $d=3010$ giving $1.2771350422$. Explicit example $h_0(x) = \sqrt{1/4-x^2}(1 - 9x^2/5)\chi_I$ yields the closed-form bound $A_1 \leq 49484/38745 = 1.27717\ldots$ in exact rational arithmetic. Corollaries recover the $L^2$ Bernstein inequality, the Duffin–Schaeffer inequality $|g|^2 + |g'|^2/\pi^2 \leq 1$, and a Hardy–Littlewood-type bound: $\int(|g|^2 + |g'|^2/\pi^2) dx \geq 4/\pi$ for $g \in PW_2$, $g(0)=1$.

## Why it matters here
General background for Paley–Wiener / Fourier-optimization techniques; relevant to autocorrelation-inequality (P14, P15, P16) and uncertainty-principle problems where extremal entire-function constructions, Krein decomposition, and orthonormal expansion via $\cos(\pi x)/((2k-1)^2 - 4x^2)$ systems are standard tools. The hybrid rigorous numerics + polynomial-parameterization + explicit rational-arithmetic upper-bound pattern is directly transferable as a triple-verify protocol for arena problems.

## Open questions / connections
- Sharp value of $A_1$ remains conjectural at $1.277135042\ldots$ — upper bound proven, matching lower bound open.
- The monotone-delta problem in odd dimensions $d \geq 3$ remains open (even-$d$ solved in [Carneiro et al., 2304.06442]); kissing-number connections via Beurling–Selberg majorants.
- Extends Holt–Vaaler (1996) Beurling–Selberg extremal-ball framework with monotonicity constraint, and Duffin–Schaeffer (1938) derivative inequalities via the positive-polynomial family $P$.

## Key terms
Carathéodory–Fejér–Turán problem, one-delta problem, Paley–Wiener space, entire functions exponential type, Beurling–Selberg, Duffin–Schaeffer inequality, Krein decomposition, monotone extremal function, Fejér kernel, Bernstein inequality, Hardy–Littlewood, ball arithmetic Arb, autocorrelation inequalities
