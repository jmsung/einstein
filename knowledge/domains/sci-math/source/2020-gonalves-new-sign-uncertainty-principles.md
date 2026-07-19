---
type: source
kind: paper
title: New Sign Uncertainty Principles
authors: Felipe Gonçalves, Diogo Oliveira e Silva, João P. G. Ramos
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2003.10771v4
source_local: ../raw/2020-gonalves-new-sign-uncertainty-principles.pdf
topic: author-sweep
cites: 
---

# New Sign Uncertainty Principles

**Authors:** Felipe Gonçalves, Diogo Oliveira e Silva, João P. G. Ramos  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2003.10771v4

## One-line
Generalizes the Bourgain–Clozel–Kahane and Cohn–Gonçalves $\pm 1$ sign uncertainty principles to a broad operator-theoretic framework, yielding new sign uncertainty inequalities for Fourier/Dini series, the Hilbert transform, discrete Fourier and Hankel transforms, spherical harmonics, and Jacobi polynomials.

## Key claim
A general "Operator Sign Uncertainty Principle" (Theorem 1.1): for any pair $(f,g)$ in a family $F \subseteq L^p(X)\times L^q(Y)$ satisfying three norm bounds ($\|g\|_\infty \le a\|f\|_1$, $\|g\|_q \le b\|f\|_p$, $\|f\|_p \le c\|g\|_q$) with $\int f \le 0$ and $\int g \le 0$, one has $\mu(\{f<0\})^{1/p'} \nu(\{g<0\})^{1/q'} \ge a^{-1} b^{-q/q'} (2c)^{-q'}/q$. A companion "Orthonormal Sign Uncertainty Principle" (Theorem 1.4) gives the discrete analogue on admissible metric measure spaces with explicit constant $1/16$.

## Method
Three norm-bound hypotheses plus two integral-sign conditions force a quantitative obstruction between the negativity sets of $f$ and its image $g=Tf$ under an invertible operator $T$. For orthonormal-basis settings, the proof tracks the expansion $f=\sum \hat f(n)\phi_n$ via a Lebesgue-point identity at a distinguished origin $0\in X$ and the bound $\|\phi_n\|_\infty = \phi_n(0)$. Reductions to Jacobi-polynomial expansions use the Christoffel–Darboux formula and Stirling-style estimates for $\Gamma$.

## Result
Lower bound $B_s(S^{d-1}) \ge 2\Gamma(\tfrac{d+1}{2})^{1/(d-1)}/[(4e^{1/12})^{(d-1)/2}(d/2-1)^{1/2}] \approx e^{-1}+O(d^{-1}\log d)$ for the sphere uncertainty constant, vs $\sqrt{d}$-growth in the Euclidean case. New numerical data (Tables 1–3) for discrete Fourier/Hankel transforms yields the bound $A_+(1) < 0.555$ (Conjecture 1.7) — strictly below the golden-ratio guess $(2\varphi)^{-1/2} = 0.5558$ — and surfaces conjectural quadratic patterns $q_-(k)=(k-1)^2/2$, $k^2/4$, $(k^2+6k-8)/8$, $(k^2+2k-1)/4$ for $(s,d)\in\{(-,1),(-,8),(-,24),(+,12)\}$.

## Why it matters here
Directly underpins the Cohn–Elkies LP framework: the $-1$ uncertainty principle satisfies $A_-(d) \le A_{LP}(d)$, with conjectured equality (Conjecture 1.5) — so discrete-Hankel sign uncertainty constants are a numerical probe of $A_{LP}(d)$ for sphere packing in dimensions outside $\{1,2,8,12,24\}$. Relevant to any arena problem touching sphere packing (P1, related LP-bound problems), kissing numbers, and Fourier-optimization problems where $\pm 1$ eigenfunctions and equioscillation arise.

## Open questions / connections
- Conjecture 1.6: $A_{LP}(2)=A_-(2)=(3/4)^{1/4}$ in dimension 2 (hexagonal); magical function still unknown.
- Conjecture 1.7: numerical evidence that minimizers for $A_+(1)$ vanish identically on intervals after the last sign change — unusual root structure unlike Hermite-style isolated zeros.
- Conjecture 3.10 (in §3): explicit quadratic formulas for discrete-Hankel jump function $q_s(k;d)$ in the four "magic" cases $(-,2),(-,8),(-,24),(+,12)$ — converge to continuous $A_s(d)$ in the limit.
- Connects to spherical $t$-designs: tight designs (Delsarte–Goethals–Seidel) realize the sphere-uncertainty extremum; classified only for $t \in \{1,2,3,4,5,7,11\}$ (Bannai–Damerell).
- Modular-bootstrap CFT prediction (Afkhami-Jeddi et al.) of $c=1/\pi$ in $A_\pm(d) \sim c\sqrt{d}$ remains open.

## Key terms
sign uncertainty principle, Cohn-Elkies linear programming bound, sphere packing, Bourgain-Clozel-Kahane, Cohn-Gonçalves, Viazovska modular forms, $\pm 1$ eigenfunction, Jacobi polynomials, Gegenbauer polynomials, discrete Hankel transform, spherical harmonics, spherical designs, Delsarte-Goethals-Seidel, $A_+(d)$, $A_-(d)$, $A_{LP}(d)$, magic function, Christoffel-Darboux, golden ratio bound, last sign change
