---
type: source
kind: paper
title: A construction of binary linear codes from Boolean functions
authors: C. Ding
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1511.00321
source_local: ../raw/2015-ding-construction-binary-linear-codes.pdf
topic: general-knowledge
cites:
---

# A construction of binary linear codes from Boolean functions

**Authors:** C. Ding  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1511.00321

## One-line
Survey + open-problems paper on building binary linear codes by using the support $D_f = \{x : f(x)=1\}$ of a Boolean function $f:\mathrm{GF}(2^m)\to\mathrm{GF}(2)$ as the defining set of a trace code $C_{D_f} = \{(\mathrm{Tr}(xd))_{d\in D_f} : x\in\mathrm{GF}(2^m)\}$.

## Key claim
For any $f$ with $2n_f + \hat f(w) \ne 0$ for all $w\ne 0$, $C_{D_f}$ is an $[n_f, m]$ binary linear code whose weight distribution is the multiset $\{(2n_f + \hat f(w))/4 : w\in\mathrm{GF}(2^m)^*\}\cup\{0\}$ — so the code's weights are read directly off the Walsh spectrum of $f$ (Theorem 1).

## Method
Defining-set / trace construction: pick $D\subseteq\mathrm{GF}(2^m)$, form $C_D$ via the absolute trace, then evaluate Hamming weights via the canonical additive character to get $\mathrm{wt}(c_x) = (n - \chi_1(xD))/2$. Specializing $D = D_f$ converts the character sum into the Walsh transform $\hat f$, so weight-distribution problems become Walsh-spectrum problems. The survey then plugs in bent, semibent, almost-bent (AB), quadratic, APN, and o-polynomial families to harvest few-weight codes.

## Result
Concrete code families with explicit weight distributions: two-weight $[n_f, m]$ codes from bent $f$ (Hadamard difference-set parameters, Corollary 3); three-weight codes from semibent and from AB monomials $x^d$ with $d\in\{2^h+1, 2^{2h}-2^h+1, 2^{(m-1)/2}+3, \ldots\}$ (Corollaries 5, 7); four- and five-weight codes from cross-correlation decimations and Niho exponents; one-/three-/five-weight families from o-polynomials (Segre, Glynn, Cherowitzo, Payne, Subiaco) via $f_u(x) = f(x)+ux$. Many of the resulting codes are optimal or almost-optimal (e.g. $[16,6,6]$ and $[64,8,28]$ from Theorem 42).

## Why it matters here
General background; no direct arena tie — the 23 Einstein problems are continuous optimization (sphere packing, autocorrelation, kissing), not coding theory. Closest tangent is the difference-set / character-sum machinery, which connects to Cohn–Elkies LP-style additive-character arguments and to extremal combinatorial constructions, but the connection is loose.

## Open questions / connections
- A dozen explicit conjectures on weight distributions of $C_{D(f^*)}$ for trinomial difference sets with Singer parameters (Conjectures 36–41) — verified by Magma for small $m$, open in general.
- Conjectured o-polynomial families (Cherowitzo, Payne extensions) with no known proof of the o-polynomial property.
- Extends Delsarte's coding-theoretic characterization of APN / AB / semibent functions; complementary to the Reed–Muller / Kerdock lineage.

## Key terms
Boolean functions, Walsh spectrum, bent functions, semibent functions, almost bent functions, APN functions, o-polynomials, difference sets, Singer parameters, trace codes, weight distribution, cross-correlation
