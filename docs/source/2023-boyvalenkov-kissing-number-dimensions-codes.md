---
type: source
kind: paper
title: The Kissing Number in 48 Dimensions for Codes with Certain Forbidden Distances is 52 416 000
authors: P. Boyvalenkov, D. Cherkashin
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2312.05121
source_local: ../raw/2023-boyvalenkov-kissing-number-dimensions-codes.pdf
topic: general-knowledge
cites:
---

# The Kissing Number in 48 Dimensions for Codes with Certain Forbidden Distances is 52 416 000

**Authors:** P. Boyvalenkov, D. Cherkashin  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2312.05121

## One-line
Proves that among antipodal spherical codes on $S^{47}$ with inner products forbidden in $F = [-1/3, -1/6] \cup [1/6, 1/3]$, the maximum cardinality is exactly $52\,416\,000$, attained by the kissing configurations of the four known even unimodular extremal lattices.

## Key claim
For any antipodal spherical code $C \subset S^{47}$ (or any spherical 3-design) with $I(C) \cap F = \emptyset$, $|C| \le 52\,416\,000$ (Thm 5.1); conversely, any spherical 11-design on $S^{47}$ avoiding inner products in $F$ (or in $F' = \{\pm 1/3, \pm 1/2\}$) has $|C| \ge 52\,416\,000$ (Thms 6.1, 6.2). Equality forces the distance distribution of the minimal vectors of $P_{48p}, P_{48q}, P_{48m}, P_{48n}$.

## Method
Modified Delsarte–Goethals–Seidel linear programming (LP) bounds for spherical codes/designs, with Gegenbauer polynomial expansions $f(t)=\sum f_i P_i^{(48)}(t)$. The bounding polynomials are constructed by hand: $h(t)=(t+1)^2 t^2 (t+1/2)^2(t-1/2)(t^2-1/36)(t^2-1/9)$ for the upper bound (degree 11, double zeros at internal forbidden interval endpoints, simple zeros at boundary), and analogous $g, u$ polynomials for the design lower bounds — with Gegenbauer coefficients verified $\ge 0$ on even indices (antipodal LP).

## Result
$|C| \le h(1)/h_0 = 52\,416\,000$ exactly. The forced distance distribution: $A_{\pm 1/2}=36848$, $A_{\pm 1/3}=1\,678\,887$, $A_{\pm 1/6}=12\,608\,784$, $A_0=23\,766\,960$, $A_{-1}=1$. This is the first such bound for spherical codes with *forbidden* inner products (vs the standard unrestricted kissing bound of $867\,897\,072$ for dim 48). Also: the $A_0$ orthogonal subset is itself a 47-dim kissing configuration.

## Why it matters here
Directly informs kissing-number / spherical-code problems via the **forbidden-distance LP variant** — a tightening trick: restricting $I(C)$ to a smaller set lets a single hand-built polynomial close to the true value of LP. Anchor for Cohn–Elkies-style and Levenshtein-style bound construction, with concrete degree-11 polynomial recipe for designs.

## Open questions / connections
- Extends Gonçalves–Vedana 2023 (arXiv:2308.03925) on sphere packing in dim 48 with forbidden distances → analogous dim-8 / dim-24 versions for $E_8$ / Leech?
- Section 7: which other highly symmetric non-sharp codes become optimal once "appropriate" distances are forbidden? (Energy / polarization variants noted.)
- Gap between forbidden-distance bound $52.4\text{M}$ and unrestricted kissing bound $867.9\text{M}$ in dim 48 — what's the right restriction class?

## Key terms
kissing number, dimension 48, even unimodular extremal lattice, P48p P48q P48m P48n, antipodal spherical code, spherical 11-design, Delsarte-Goethals-Seidel LP bound, Gegenbauer polynomials, forbidden inner products, Levenshtein bound, Cohn-Elkies, Viazovska, distance distribution, Venkov theorem
