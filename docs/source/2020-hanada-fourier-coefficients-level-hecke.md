---
type: source
kind: paper
title: Fourier coefficients of level 1 Hecke eigenforms
authors: Mitsuki Hanada, Rachana Madhukara
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2007.08683
source_local: ../raw/2020-hanada-fourier-coefficients-level-hecke.pdf
topic: general-knowledge
cites:
---

# Fourier coefficients of level 1 Hecke eigenforms

**Authors:** Mitsuki Hanada, Rachana Madhukara  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2007.08683

## One-line
Rules out many odd integers as possible values of the Ramanujan $\tau$-function and the Fourier coefficients $\tau_{2k}(n)$ of the other five level-1 Hecke eigenforms in dimension-1 cusp spaces (weights 16, 18, 20, 22, 26).

## Key claim
For $n>1$: $\tau(n) \notin \{-9, \pm15, \pm21, -25, -27, -33, \pm35, \pm45, \pm49, -55, \pm63, \pm77, -81, \pm91\}$ (unconditional), with substantial extensions under GRH; analogous exclusion lists are established for $\tau_{16}, \tau_{18}, \tau_{20}, \tau_{22}, \tau_{26}$. Also: $\tau_{20}(n)\neq \pm 617$, $\tau_{22}(n)\neq \pm 131$ unconditionally (and $\pm 593$ under GRH), where these primes divide numerators of Bernoulli numbers $B_{2k}$.

## Method
Combine (i) the Bilu–Hanrot–Voutier classification of primitive prime divisors of Lucas sequences $\{u_m(\alpha_p,\beta_p)\}$ arising from $F_p(x)=x^2 - a_f(p)x + p^{2k-1}$, (ii) Swinnerton-Dyer's mod-$\ell$ congruences for level-1 forms (e.g. $\tau_{2k}(n)\equiv \sigma_{2k-1}(n)\pmod{\ell}$ for exceptional primes $\ell\in\{691,3617,43867,\dots\}$) to constrain the prime $d$ with $n=p^{d-1}$, and (iii) reduction to integer points on hyperelliptic curves $Y^2 = X^{2k-1}\pm c$, $Y^2 = 5X^{2(2k-1)}\pm 4c$ and Thue equations $F_{d-1}(X,Y)=\pm c$, solved via Barros's algorithm, Bilu–Hanrot high-degree Thue methods, and continued-fraction expansions of $2\cos(2\pi k/\ell)$.

## Result
For each of the six weights, an explicit list of odd integers $\alpha$ with $|\alpha|<99$ (and certain composites) is shown to lie outside the image of $\tau_{2k}$, both unconditionally and under GRH (Theorems 1.1, 1.2). For exceptional primes dividing $B_{2k}$ numerators, either full exclusion (131, 617; 593 under GRH) or a tight restriction on $n$'s form (e.g. $\tau_{16}(n)=\pm 3617 \Rightarrow n=p^{112}$; $\tau_{20}(n)=\pm 283 \Rightarrow n=p^2$) is proved (Theorems 1.3, 1.4). All computations carried out in SageMath.

## Why it matters here
General background; no direct arena tie — this is analytic number theory on modular-form coefficients, not optimization. May tangentially inform problems involving modular forms / Eisenstein-series style constructions (Cohn–Elkies-type magic functions in sphere packing) by exposing the Lucas-sequence / Thue-equation / hyperelliptic-curve toolkit for arithmetic obstructions.

## Open questions / connections
- Can $\pm 283, \pm 3617, \pm 43867, \pm 657931$ be fully ruled out as $\tau_{2k}$ values by resolving the remaining ultra-high-degree Thue equations ($F_{112}, F_{2436}, F_{240}$)?
- Extends Murty–Murty–Shorey (1987) finiteness and Balakrishnan–Craig–Ono–Tsai (2020) prime-value exclusions to composite odd values and the full weight-1-dimensional family.
- Lehmer's conjecture $\tau(n)\neq 0$ remains untouched; this work narrows but does not address vanishing.

## Key terms
Ramanujan tau function, Hecke eigenform, level 1 cusp form, Lehmer's conjecture, Lucas sequence, primitive prime divisor, Bilu-Hanrot-Voutier, Swinnerton-Dyer congruences, Thue equation, hyperelliptic curve, Bernoulli numbers, Galois representation, GRH, modular forms
