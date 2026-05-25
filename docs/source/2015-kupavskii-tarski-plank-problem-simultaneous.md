---
type: source
kind: paper
title: From Tarski's Plank Problem to Simultaneous Approximation
authors: A. Kupavskii, J. Pach
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1511.08111
source_local: ../raw/2015-kupavskii-tarski-plank-problem-simultaneous.pdf
topic: general-knowledge
cites:
---

# From Tarski's Plank Problem to Simultaneous Approximation

**Authors:** A. Kupavskii, J. Pach  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1511.08111

## One-line
Proves a near-tight converse to Bang's theorem: slabs whose widths sum sufficiently fast (relative to $\log(1/w_n)$) admit a translative covering of $\mathbb{R}^d$, and applies this to settle Makai–Pach's polynomial-controlling conjecture.

## Key claim
**Theorem 1:** If $w_1 \ge w_2 \ge \dots > 0$ satisfies $\limsup_{n\to\infty} \frac{w_1+\dots+w_n}{\log(1/w_n)} > 0$, then slabs of those widths permit a translative covering of $\mathbb{R}^d$. **Theorem 3:** A sequence $x_1 \le x_2 \le \dots$ is $\mathcal{P}_d$-controlling (every degree-$\le d$ polynomial passes within distance $1$ of some $(x_i,y_i)$) iff $\sum_{i=1}^\infty 1/x_i^d = \infty$ — settling Conjecture 3.2.B of Makai–Pach [15].

## Method
Two-stage greedy/volumetric covering argument descended from Rogers [17]. **Theorem 2:** for finite slab systems, halve each slab's width, then greedily place each shrunk translate to cover a $w_i/3$-fraction of the uncovered volume (pigeonhole on $\lceil 2/w_i\rceil$ candidate positions); the residual volume drops as $\prod(1-w_i/3) \le \exp(-\frac{1}{3}\sum w_i)$, so under $\sum w_i \ge 3d\log(2/w_n)$ no ball of radius $w_n/4$ remains uncovered. **Theorem 3** refines this with a lemma giving $d+1$ linearly independent directions $u_j$ on the moment curve $(1,x,x^2,\dots,x^d)$ satisfying a monotone-ratio condition $\langle x_{i+1},u_1\rangle/\langle x_i,u_1\rangle \le \langle x_{i+1},u_j\rangle/\langle x_i,u_j\rangle$ plus an angle lower bound $\langle x_i,u_j\rangle \ge \tfrac13 \|x_i\|\|u_j\|$, enabling a simplex-stacking covering along the moment curve.

## Result
For $d \ge 3$, slabs of widths $w_i = 1/i$ admit a translative covering of $\mathbb{R}^d$ (improving Groemer's $\sum w_i^{(d+1)/2} = \infty$ [10] threshold, e.g. $w_i = i^{-1/2}$ in $d=3$). The polynomial-control characterization is exact: $\sum 1/x_i^d = \infty$ is both necessary (via Bang) and sufficient. The Makai–Pach translative plank conjecture (full $\sum w_i = \infty$ suffices) remains open in $d \ge 3$; this paper closes a logarithmic gap.

## Why it matters here
General background; no direct arena tie. Useful for discrete-geometry / covering problems and for the duality "covering R^d by slabs ↔ controlling a function class by a point set" — relevant if any arena problem asks about sequences hitting graphs of bounded-degree polynomials or hyperplane-arrangement covering.

## Open questions / connections
- **Makai–Pach translative plank conjecture** ($\sum w_i = \infty$ suffices) still open for $d \ge 3$; Theorem 1 closes to within a $\log(1/w_n)$ factor.
- **Bang's affine plank problem** ($\sum w(S_i)/w(C,v_i) \ge 1$) open even for 3 slabs; Ball [1] settled centrally symmetric case.
- **Strong translative plank conjecture** (uniform constant $c(d)$): equivalent to translative plank conjecture by Ruzsa [14].
- Generalize controlling-sequence question to other function classes $f:\mathbb{R}^k\to\mathbb{R}^l$ (see [13], [15]).

## Key terms
Tarski plank problem, Bang theorem, affine plank problem, translative covering, slab width, Makai–Pach conjecture, polynomial controlling sequence, moment curve, Rogers covering, greedy volumetric covering, simultaneous approximation, Keith Ball symmetric plank, Groemer covering bound
