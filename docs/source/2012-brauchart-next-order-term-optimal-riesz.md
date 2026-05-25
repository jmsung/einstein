---
type: source
kind: paper
title: The next-order term for optimal Riesz and logarithmic energy asymptotics on the sphere
authors: J. Brauchart, D. Hardin, E. Saff
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1202.4037
source_local: ../raw/2012-brauchart-next-order-term-optimal-riesz.pdf
topic: general-knowledge
cites:
---

# The next-order term for optimal Riesz and logarithmic energy asymptotics on the sphere

**Authors:** J. Brauchart, D. Hardin, E. Saff  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1202.4037

## One-line
Survey + conjectures for the next-order ($N$ or $N^{1+s/d}$) term in the asymptotic expansion of optimal Riesz $s$-energy and logarithmic energy of $N$ points on $S^d$, derived by analytic continuation in $s$.

## Key claim
For $d \in \{2,4,8,24\}$, the order-$N$ coefficient in $E_{\log}(S^d;N) = V_{\log}(S^d)N^2 - \tfrac{1}{d}N\log N + C_{\log,d}N + o(N)$ is conjectured to be $C_{\log,d} = \tfrac{1}{d}\log(\mathcal{H}^d(S^d)/|\Lambda_d|) + \zeta'_{\Lambda_d}(0)$; for $d=2$, $C_{\log,2} = 2\log 2 + \tfrac{1}{2}\log\tfrac{2}{3} + 3\log\tfrac{\sqrt{\pi}}{\Gamma(1/3)} \approx -0.05560530$.

## Method
Analytic continuation in $s$: differentiate the conjectured Riesz $s$-energy expansion $E_s(S^d;N) = V_s(S^d)N^2 + C_{s,d}[\mathcal{H}^d(S^d)]^{-s/d}N^{1+s/d} + o(\cdot)$ at $s\to 0^+$ to get the log case, and take $s\to d$ (where $V_s$ has a simple pole) to get the boundary case. Uses Epstein zeta $\zeta_{\Lambda_d}(s)$ of the lattice $\Lambda_d$ (hexagonal, $D_4$, $E_8$, Leech), with factorization $\zeta_{\Lambda_2}(s) = 6\zeta(s/2)L_{-3}(s/2)$. Lower/upper bounds for hypersingular $s\ge d$ proved via Wagner's positive-definite kernel trick ($K_\varepsilon(t)=(2-2t+\varepsilon)^{-d/2}$) on spherical caps.

## Result
- Conjecture 3: For $-2<s<d+2$, $s\ne d$, $C_{s,d}=|\Lambda_d|^{s/d}\zeta_{\Lambda_d}(s)$ in dimensions $d=2,4,8,24$.
- Conjecture 5 (boundary $s=d=2$): $E_2(S^2;N) = \tfrac{1}{4}N^2\log N + C_{2,2}N^2 + O(1)$ with $C_{2,2} = \tfrac{1}{4}[\gamma - \log(2\sqrt{3}\pi)] + \tfrac{\sqrt{3}}{4\pi}[\gamma_1(2/3)-\gamma_1(1/3)] \approx -0.08576841$.
- Proposition 3 (proved): $\tfrac{1}{4}N^2\log N - c(d)N^2 + O(\cdot) \le E_d(S^d;N) \le \tfrac{1}{4}N^2\log N + O(N^2\log\log N)$.

## Why it matters here
Direct background for any sphere-energy / sphere-distribution problem on Einstein Arena: gives the explicit next-order coefficient one should fit to in numerical experiments, and pins the conjectured constants to Epstein zeta values of $\Lambda_2, D_4, E_8, \Lambda_{24}$ — the same magic lattices behind Cohn–Elkies/Viazovska sphere packing. Anchors triple-verify checks for any optimizer producing $E_s(S^2;N)$ numbers near the conjectured asymptotic.

## Open questions / connections
- No proof that $C_{s,d} = |\Lambda_d|^{s/d}\zeta_{\Lambda_d}(s)$ even for $d=2$; tied to Cohn–Kumar universal optimality.
- Existence/form of $p\ge 1$ higher-order terms in $E_s$ unclear (Kiessling: may oscillate; Melnyk et al: phase-transition-like jumps).
- Smale's Problem #7: design polynomial-time algorithm achieving $E_{\log}(x_1,\dots,x_N)-E_{\log}(S^2;N)\le c\log N$.
- Numerical convergence is slow; Womersley data up to $N=22801$ supports but doesn't confirm Conjecture 4.

## Key terms
Riesz s-energy, logarithmic energy, sphere $S^d$, Epstein zeta function, hexagonal lattice $\Lambda_2$, $E_8$ lattice, Leech lattice, Cohn–Elkies, transfinite diameter, Smale Problem 7, Wagner positive-definite kernel, Poppy-seed Bagel theorem, Stieltjes constants, Dirichlet L-series $L_{-3}$, Brauchart, Hardin, Saff, Rakhmanov–Saff–Zhou
