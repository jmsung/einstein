---
type: source
kind: paper
title: A Chebotarev variant of the Brun-Titchmarsh theorem and bounds for the Lang-Trotter conjectures
authors: Jesse Thorner, Asif Zaman
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1606.09238
source_local: ../raw/2016-thorner-chebotarev-variant-brun-titchmarsh-theorem.pdf
topic: general-knowledge
cites:
---

# A Chebotarev variant of the Brun-Titchmarsh theorem and bounds for the Lang-Trotter conjectures

**Authors:** Jesse Thorner, Asif Zaman  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1606.09238

## One-line
Sharpens the Chebotarev-flavored Brun-Titchmarsh upper bound for prime ideals in conjugacy classes by plugging in a log-free zero-density estimate plus Deuring-Heilbronn zero repulsion for Hecke $L$-functions, then applies it to Lang-Trotter conjectures and binary quadratic form primes.

## Key claim
For a Galois extension $L/F$ with group $G$, conjugacy class $C$, abelian subgroup $H$ meeting $C$, fixed field $K$, and $Q=Q(L/K)=\max_{\chi\in\hat H} N_{K/\mathbb{Q}}\mathfrak{f}_\chi$, one has $\pi_C(x,L/F) \ll \tfrac{|C|}{|G|}\mathrm{Li}(x)$ whenever $x \gg D_K^{246} Q^{185} + D_K^{82} Q^{130}[K:\mathbb{Q}]^{246[K:\mathbb{Q}]}$ (Theorem 1.1) — improving the Lagarias-Montgomery-Odlyzko range $\log x \gg (\log D_L)(\log\log D_L)(\log\log\log e^{20}D_L)$.

## Method
Smoothed Maynard-style weight function $f$ with Laplace transform $F$, controlled to be $O(n_K)$-times differentiable so $F(\sigma+it)$ decays like $|t|^{-O(n_K)}$. Bound $\psi_C(x)$ via the explicit formula for $Z_C(s)=\sum_\chi \tfrac{|C|}{|G|}\overline{\chi(g_C)}(-L'/L)(s,\chi)$, controlling zero contributions with the log-free zero density estimate and Deuring-Heilbronn zero repulsion for Hecke $L$-functions from Thorner-Zaman (arXiv/1604.01750); refined case analysis on the size of $\lambda_1=L(1-\beta_1)$ (Siegel-zero regime vs. not) recovers the constant $2$ in $\pi_C < (2+o(1))\tfrac{|C|}{|G|}\mathrm{Li}(x)$ (Theorem 1.2).

## Result
Theorem 1.2: $\pi_C(x,L/F) < (2+O([K:\mathbb{Q}]x^{-1/(166[K:\mathbb{Q}]+327)}))\tfrac{|C|}{|G|}\mathrm{Li}(x)$ for $x\gg D_K^{695}Q^{522}+D_K^{232}Q^{367}[K:\mathbb{Q}]^{290[K:\mathbb{Q}]}$; error term vanishes when $K$ has a normal tower over $\mathbb{Q}$, recovering Maynard's $C(\theta)=2$ for $\theta\le 1/522$. Corollary 1.3: for a positive-definite primitive binary quadratic form of discriminant $-D$, $\#\{p\le x: p \text{ represented}\}\ll \mathrm{Li}(x)/h(-D)$ for $x\gg D^{164}$, comparable up to exponent to the GRH range $D^{1+\epsilon}$. Theorem 1.4: $\pi_f(x,a)\ll_{N_f} x(\log\log x)^2/(\log x)^2$ (Lang-Trotter for newforms), and Theorem 1.5: $\pi_E(x,k)\ll_{N_E,k} x\log\log x/(\log x)^2$ for elliptic Frobenius fields — both shaving a $\log\log x$ over V.K. Murty 1997 and Zywina.

## Why it matters here
General background; no direct arena tie. The closest hooks are sieve-theoretic and zero-density technology that could inform sieve-style problems (Sidon-set / autocorrelation / extremal counting), and the smoothed weight + Laplace-transform decay trick is a transferable analytic technique.

## Open questions / connections
- Can the exponents $246, 185, 695, 522$ on $D_K$ and $Q$ in (1.10)/(1.12) be reduced toward the GRH-predicted linear range?
- Does eliminating Landau-Siegel zeros (currently the bottleneck for the constant-$2$ statement) yield $\pi_C < (1+o(1))\tfrac{|C|}{|G|}\mathrm{Li}(x)$, mirroring conjectural Brun-Titchmarsh?
- Extends/complements Maynard (Acta Arith. 2013) for arithmetic progressions, Lagarias-Montgomery-Odlyzko (Invent. Math. 1979), Weiss (1983), V.K. Murty (1997), Zywina (2015); leaves open the full Lang-Trotter $\sqrt{x}/\log x$ asymptotic.

## Key terms
Brun-Titchmarsh, Chebotarev density theorem, Hecke L-functions, log-free zero density estimate, Deuring-Heilbronn zero repulsion, Landau-Siegel zero, Lang-Trotter conjecture, Frobenius traces, binary quadratic forms, ring class field, Maynard, Lagarias-Montgomery-Odlyzko, Artin L-function
