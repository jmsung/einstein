---
type: source
kind: paper
title: Multiple zeros of nonlinear systems
authors: Barry H. Dayton, Tien-Yien Li, Zhonggang Zeng
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2103.05738
source_local: ../raw/2011-dayton-multiple-zeros-nonlinear-systems.pdf
topic: general-knowledge
cites:
---

# Multiple zeros of nonlinear systems

**Authors:** Barry H. Dayton, Tien-Yien Li, Zhonggang Zeng  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/2103.05738

## One-line
Formulates a numerically computable multiplicity structure for an isolated zero of a general nonlinear system and gives a depth-deflation algorithm that recovers multiple zeros accurately in floating-point arithmetic.

## Key claim
At an isolated zero $\hat x$ of $f:\mathbb{C}^s\to\mathbb{C}^t$, the dual space $D_{\hat x}(F)$ of differential functionals $\partial^{j}[\hat x]$ closed under anti-differentiation $\phi_i$ has finite dimension $m$ equal to the classical intersection multiplicity (for polynomial systems), and $m$ zeros emerge under generic perturbation. The depth $\delta_{\hat x}(F) = \max\{\alpha : h(\alpha)>0\}$ of the Hilbert function bounds the number of deflation steps needed to regularize the singularity — strictly tighter than the multiplicity bound of Leykin–Verschelde–Zhao.

## Method
Define dual subspaces $D^\alpha_{\hat x}(F)$ via the closedness condition $\phi_i(c)\in D^{\alpha-1}_{\hat x}(F)$ and realize them as kernels of Macaulay matrices $S_\alpha$ whose entries are $\partial^{j}[\hat x]\bigl((x-\hat x)^k f_i\bigr)$; numerical rank-revealing on $S_\alpha$ recovers Hilbert function, breadth (Jacobian nullity), and depth. The depth-deflation method appends auxiliary variables $x_2,\dots,x_{2^\alpha}$ encoding higher-order operators $\Phi_\alpha = \sum_\zeta x_{2^\alpha+\zeta}\cdot\Delta_{x_\zeta}$ and a random normalization $R_\alpha x = e_1$, producing an expanded system whose Jacobian becomes full-rank after at most $\delta_{\hat x}(F)$ steps. A specialized breadth-one variant uses a single operator $\Psi = \sum x_{\eta+1}\cdot\Delta_{x_\eta}$ and grows the system linearly (size $\sim m\cdot t$ instead of $2^{m-1}t$).

## Result
Three foundational theorems: Local Finiteness (multiplicity is finite iff zero is isolated, for analytic $F$); Multiplicity Consistency (matches algebraic-geometry intersection multiplicity for polynomial systems); Perturbation Invariance ($m$-fold zero splits into exactly $m$ nearby zeros under small analytic perturbation). The depth-deflation regularizes any isolated singular zero in $\le \delta_{\hat x}(F)$ steps, defeating the "attainable accuracy = digits/multiplicity" barrier — e.g., on inexact breadth-one systems with multiplicity 22 and depth 21 the algorithm recovers full-precision dual bases (Example 5, Table 2).

## Why it matters here
General background; no direct arena tie. Potentially relevant only if an arena problem reduces to extracting an isolated multiple root of a polynomial/analytic system (e.g., equioscillation conditions, KKT systems at degenerate optima, or basin-rigidity proofs requiring the exact multiplicity structure of a stationary point) — none of the 23 current problems are framed this way.

## Open questions / connections
- Conjecture 1: BreadthOneMultiplicity always terminates exactly at $\gamma = \delta_{\hat x}(f)$ with a complete dual basis — unproven.
- Empirical observation: for breadth $>1$, depth-deflation usually terminates in 1 step regardless of multiplicity; no theoretical characterization of when this fails.
- Extends Macaulay (1916), Mourrain, Stetter–Thallinger numerical dual-basis work; relates to Leykin–Verschelde–Zhao Newton-with-deflation but deflates depth not multiplicity.
- Could plug into KKT-degeneracy diagnosis in optimizer polish phases (mpmath ULP polish near saddle/degenerate stationary points) — speculative.

## Key terms
multiplicity structure, isolated zero, dual space, Macaulay matrix, Hilbert function, depth-deflation, breadth, closedness condition, anti-differentiation, intersection multiplicity, Gröbner duality, numerical rank revealing, Newton's method, perturbation invariance, Macaulay, Stetter, Mourrain, Leykin
