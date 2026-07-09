---
type: source
kind: paper
title: Densities of Short Uniform Random Walks
authors: J. Borwein, A. Straub, J. Wan, W. Zudilin, D. Zagier
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1103.2995
source_local: ../raw/2011-borwein-densities-short-uniform-random.pdf
topic: general-knowledge
cites:
---

# Densities of Short Uniform Random Walks

**Authors:** J. Borwein, A. Straub, J. Wan, W. Zudilin, D. Zagier  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1103.2995

## One-line
Closed-form hypergeometric representations for the radial densities $p_n(x)$ of $n$-step uniform random walks in the plane, with full treatment for $n=3,4$ and partial results for $n=5$.

## Key claim
The 4-step density admits the closed form $p_4(x) = \frac{2}{\pi^2}\frac{\sqrt{16-x^2}}{x}\,\mathrm{Re}\,{}_3F_2\!\left(\tfrac{1}{2},\tfrac{1}{2},\tfrac{1}{2};\tfrac{5}{6},\tfrac{7}{6};\tfrac{(16-x^2)^3}{108x^4}\right)$ on $(0,4)$, complementing the classical elliptic-integral form for $p_3$, and $p_n$ satisfies a linear ODE of order $n-1$ derived from the Mellin transform of the moment recurrence.

## Method
Bessel-integral (Kluyver) representation $p_n(x)=\int_0^\infty xt J_0(xt) J_0^n(t)\,dt$ combined with Mellin-transform translation of the moment recurrence $W_n(s)$ into an ODE $A_n\cdot p_n=0$. Singularity structure at $x=0$ and $x=n$ is read off from poles of $W_n(s)$ (Frobenius method at regular singular points); for $p_4$ the ODE reduces to a symmetric square of a Heun-type 2nd-order equation, yielding a $_3F_2$ representation. Modular parameterization via Dedekind $\eta$-quotients (cubic AGM, theta functions $b,c$) and Chowla–Selberg evaluations at singular moduli give explicit special values.

## Result
Hypergeometric closed forms: $p_3(x)=\frac{2\sqrt{3}x}{\pi(3+x^2)}\,{}_2F_1\!\left(\tfrac{1}{3},\tfrac{2}{3};1;\tfrac{x^2(9-x^2)^2}{(3+x^2)^3}\right)$ and the $p_4$ form above. Singularity asymptotics: $p_3(x)\sim\tfrac{3}{2\pi^2}\log\tfrac{4}{|x-1|}$ near $x=1$; $p_4(x)\sim\tfrac{\sqrt{2}}{\pi^2}\sqrt{4-x}$ near $x=4$. Special value $p_4(1)=p_5'(0)=\tfrac{1}{2\pi^2}\Gamma(\tfrac{1}{15})\Gamma(\tfrac{2}{15})\Gamma(\tfrac{4}{15})\Gamma(\tfrac{8}{15})/[5\Gamma(\tfrac{7}{15})\Gamma(\tfrac{11}{15})\Gamma(\tfrac{13}{15})\Gamma(\tfrac{14}{15})]$. Mahler-measure identity $W_4'(0)=m(1+x_1+x_2+x_3)=7\zeta(3)/(2\pi^2)$; Zagier's appendix proves a combinatorial identity $\sigma_k$ of squares of $(n-2m_i)$ equals a constrained sum over $\alpha$-sequences, supplying the characteristic polynomial of the moment recurrence.

## Why it matters here
General background; no direct arena tie. Provides closed-form / hypergeometric machinery (Mellin↔ODE translation, Frobenius at regular singularities, modular parameterization of $_3F_2$) that may inform problems involving radial integrals, Bessel-moment evaluations, or Mahler measures if any arena problem reduces to such structure.

## Open questions / connections
- Conjectural Eta-product integral for $W_5'(0)$ (Rodriguez-Villegas) verified to 600 digits but unproven; similar for $W_6'(0)$ to 80 digits.
- Conjectural evaluation $r_{5,1}=\tfrac{13}{225}r_{5,0}-\tfrac{2}{5\pi^4 r_{5,0}}$ verified to 400 digits.
- No expected hypergeometric closed form for $p_n$, $n\ge 5$; extends [BNSW09, BSW11] on random-walk moments.

## Key terms
uniform random walk density, Bessel moment, Kluyver integral, Mellin transform, hypergeometric $_3F_2$, Meijer G-function, Mahler measure, Dedekind eta, modular parameterization, cubic AGM, Domb numbers, Chowla–Selberg formula, Carlson's theorem, Frobenius method, Borwein, Zagier
