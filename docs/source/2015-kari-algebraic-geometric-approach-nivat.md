---
type: source
kind: paper
title: An Algebraic Geometric Approach to Nivat's Conjecture
authors: J. Kari, Michal Szabados
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1510.00177
source_local: ../raw/2015-kari-algebraic-geometric-approach-nivat.pdf
topic: general-knowledge
cites:
---

# An Algebraic Geometric Approach to Nivat's Conjecture

**Authors:** J. Kari, Michal Szabados  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1510.00177

## One-line
Recasts low-complexity multidimensional configurations as formal power series and uses polynomial annihilator ideals + Hilbert's Nullstellensatz to prove an asymptotic Nivat's conjecture: any non-periodic 2D configuration satisfies $P_c(m,n) \le mn$ for only finitely many rectangles.

## Key claim
**Theorem 4 (asymptotic Nivat):** If $c \in A^{\mathbb{Z}^2}$ is non-periodic, then $P_c(M,N) > MN$ for all but finitely many $(M,N) \in \mathbb{N}^2$. Equivalently (Cor. 3), if $P_c(M,N) \le MN$ holds for infinitely many $(M,N)$, then $c$ is periodic. **Decomposition theorem (Thm 2):** every finitary integral configuration with a non-trivial annihilator is a finite sum $c = c_1 + \cdots + c_m$ of periodic integral configurations (possibly with unbounded values).

## Method
Encode $c \in A^{\mathbb{Z}^d}$ as a formal Laurent power series in $\mathbb{C}[[X^{\pm 1}]]$; low complexity $P_c(D) \le |D|$ implies (Lemma 1) a non-trivial Laurent polynomial $f$ with $fc=0$, so $\mathrm{Ann}(c) \trianglelefteq \mathbb{C}[X]$ is a non-zero ideal. Using a Frobenius-style mod-$p$ trick ($f^p(X) \equiv f(X^p) \pmod p$) and Hilbert's Nullstellensatz, show every common root of $\mathrm{Ann}(c)$ is killed by a product $\prod (X^{v_i}-1)$ (Thm 1) — yielding "difference-operator" factorization. In $d=2$, prove $\mathrm{Ann}(c)$ is radical (Lemma 5) and factor it as $\varphi_1\cdots\varphi_m \cdot H$ with line polynomials $\varphi_i$ in distinct directions plus a 0-dim ideal $H$ (Lemma 6); bound block counts in one-periodic factors (Lemmas 7–9) to get $P_c(M,N) > (M-m)(N-n)$ with a multiplicative gain when $\mathrm{ord}(c) \ge 3$ or directions are oblique.

## Result
Defines invariant $\mathrm{ord}(c) = m$; configuration is doubly-periodic iff $\mathrm{ord}=0$, one-periodic iff $\mathrm{ord}=1$, non-periodic iff $\mathrm{ord} \ge 2$ (Cor. 1). Quantitative complexity bound (Cor. 2): for non-periodic $c$ with annihilator of box $(m,n)$, $P_c(M,N) > (M-m)(N-n)$, strengthened to $\alpha(M-m)(N-n)$ for some $\alpha>1$ under oblique directions, and to $2(M-m)(N-n)$ when $\mathrm{ord}(c) \ge 3$. Combining "thin" and "fat" rectangle regimes proves the asymptotic conjecture; Lemma 10 reduces general alphabets to binary.

## Why it matters here
General background; no direct arena tie. Provides a template (annihilator-ideal / Nullstellensatz machinery on power-series-encoded configurations) potentially useful for any Einstein Arena problem where a discrete configuration on $\mathbb{Z}^d$ with low local pattern complexity must be forced into periodic structure — relevant to combinatorial / extremal-graph / Sidon-set-style problems where periodicity or near-periodicity is the target structure.

## Open questions / connections
- Does Lemma 5 (radicality of $\mathrm{Ann}(c)$) extend to $d \ge 3$? Authors conjecture yes but their 2D ideal-decomposition proof fails in higher dimensions.
- Full Nivat's conjecture (not just asymptotic) — converting "finitely many $(m,n)$" to "no such $(m,n)$" — remains open; this gives best general result toward it (prior bounds were $P_c(m,n) \le mn/144$, $mn/16$, $mn/2$).
- Periodic Tiling Problem of Lagarias–Wang for $d=2$: same annihilator framework applies (Ex. 2 reproves Szegedy's prime-size case in two lines); does the radical/decomposition structure imply periodic co-tilers exist?
- Example 4 shows periodic summands $c_i$ in the decomposition may necessarily be non-finitary (unbounded integer values) — refining to finitary periodic decomposition is a structural gap.

## Key terms
Nivat's conjecture, Morse-Hedlund theorem, pattern complexity, subshift, annihilator ideal, formal power series, Hilbert Nullstellensatz, line polynomial, periodic tiling problem, Lagarias-Wang, radical ideal, symbolic dynamics, polyomino tiling, Szegedy prime co-tiler, one-periodic configuration
