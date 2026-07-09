---
type: source
kind: paper
title: Sphere Packings in Euclidean Space with Forbidden Distances
authors: Felipe Gonçalves, Guilherme Vedana
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2308.03925v4
source_local: ../raw/2023-gonalves-sphere-packings-euclidean-space.pdf
topic: general-knowledge
cites: 
---

# Sphere Packings in Euclidean Space with Forbidden Distances

**Authors:** Felipe Gonçalves, Guilherme Vedana  ·  **Year:** 2023  ·  **Source:** http://arxiv.org/abs/2308.03925v4

## One-line
Extends Viazovska's modular-form magic-function technique to solve a *constrained* sphere packing problem where certain short center-to-center distances are forbidden, proving extremal even unimodular lattices are optimal in dimension 48 (and conditionally in all $8|d$, $d \not\equiv 16 \pmod{24}$, up to $d \le 1200$).

## Key claim
Any sphere packing in $\mathbb{R}^{48}$ with radius $r$ that avoids the interval $\sqrt{4/3} < |x_1-x_2|/(2r) < \sqrt{5/3}$ has center density $\le (3/2)^{24}$, with equality iff the packing is a 48-dim even unimodular extremal lattice ($P_{48p}, P_{48q}, P_{48m}, P_{48n}$). This is strong evidence for the conjecture that extremal lattices are unconstrained optimal in $d=48$.

## Method
New Cohn–Elkies-style LP bound $\Delta_d^{LP}(K)$ for $K$-admissible packings (Theorem 3), paired with explicit "magic" radial Schwartz functions $H_d$ constructed via the Viazovska integral transform with $p(s)=\sin^2(\pi s/2)$ over modular forms on $\Gamma(2)$ and $\Gamma(1)$ (Lemmas 17–18, Theorem 4). The sign conditions on $H_d$ and $\widehat{H_d}$ (which *do* change sign — unlike pure positivity-of-Fourier-coefficients arguments) are verified via a rational-arithmetic computer-assisted procedure using Sturm's method on truncated $q$/$r$-expansions and effective tail bounds (Lemma 19).

## Result
- **Theorem 1 ($d=48$):** density bound $(3/2)^{24}$ on the forbidden-interval problem, uniqueness on periodic packings.
- **Theorem 2 ($8 \le d \le 1200$, $8|d$, $d \not\equiv 16 \pmod{24}$):** for the forbidden set $A_d = \bigcup_i (a_1 + 2i/a_d, a_1 + 2(i+1)/a_d)$ where $a_d = 2 + 2\lfloor d/24 \rfloor$, periodic packings with $\min\ell(\Lambda^*) > 2r\sqrt{c_d}$ obey $\text{dens} \le \text{vol}(B_d)(\sqrt{a_d}/2)^d$, attained uniquely by extremal even unimodular lattices.
- The $d=8, 24, 48$ cases have $c_d = 0$, removing the spectral condition; this recovers Viazovska's $E_8$/Leech results inside a unified family.

## Why it matters here
Directly relevant to **P19/sphere-packing-style problems** and the broader Cohn–Elkies LP method already in the wiki ([[cohn-elkies-lp-bound]], [[viazovska-magic-function]]): demonstrates a *constructible* family extending the magic-function technique beyond $d=8,24$, and provides a computer-assisted recipe (Sturm method + truncated modular-form expansions + rational tail bounds) for certifying sign conditions when positivity-of-coefficients fails. Useful for any arena problem where LP bounds with forbidden-distance constraints could tighten standard sphere-packing/kissing bounds.

## Open questions / connections
- Conjecture 1: extremal lattices in $d=48$ are unconstrained optimal — Theorem 1 reduces this to handling the gap $\sqrt{8} < |x| < \sqrt{10}$.
- Conjecture 3: generalization of Theorem 2 with no spectral assumption — would require finding magic functions with larger $\ell_d$ (currently fails for small perturbations $\delta$).
- $d \equiv 16 \pmod{24}$ excluded — magic function exists but $\widehat{H}$ becomes nonpositive away from origin; needs more forbidden distances.
- Algorithm is $\sim O(1.1^{d/8})$-seconds — reaching the $d_{\max} \le 163264$ extremal-lattice bound is computationally infeasible.
- Connects to Boyvalenkov–Cherkashin (2025) kissing number in $d=48$ with forbidden distances (52,416,000) and the Naslund chromatic-number-of-$\mathbb{R}^d$ program.

## Key terms
sphere packing, forbidden distances, Cohn-Elkies LP bound, Viazovska magic function, modular forms, even unimodular extremal lattice, dimension 48, $P_{48p}$, $E_8$, Leech lattice, Eisenstein series, Sturm method, kissing number, center density, $\Gamma(2)$ congruence subgroup, $\widehat{f}$ sign condition
