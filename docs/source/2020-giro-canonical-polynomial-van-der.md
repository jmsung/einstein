---
type: source
kind: paper
title: A Canonical Polynomial Van der Waerden's Theorem
authors: António Girão
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2004.07766
source_local: ../raw/2020-giro-canonical-polynomial-van-der.pdf
topic: general-knowledge
cites:
---

# A Canonical Polynomial Van der Waerden's Theorem

**Authors:** António Girão  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2004.07766

## One-line
Proves a canonical (infinite-colouring) version of the polynomial Van der Waerden theorem: in any colouring of $\mathbb{Z}$, every finite family of integer polynomials with zero constant term admits a monochromatic or rainbow shifted copy.

## Key claim
For any $\{p_1,\dots,p_k\} \subset \mathbb{Z}[x]$ with $p_i(0)=0$, and for any colouring of $\mathbb{Z}$ (possibly with infinitely many colours), there exist $a,d \in \mathbb{Z}$ such that $\{a, a+p_1(d), \dots, a+p_k(d)\}$ is either monochromatic or rainbow (Theorem 1.3).

## Method
Purely combinatorial double induction: an outer induction on a weight vector $\omega(\mathcal{B}) = (N_1,\dots,N_D)$ counting distinct leading coefficients by degree, and an inner induction on a tweaked $\ell_1$-norm $\lVert\mathcal{F}\rVert$ over collections of "fully-rainbow $\mathcal{B}$-focused" sets. The argument adapts Walters' combinatorial proof of polynomial VdW (2000) by partitioning $[N']$ into blocks of length $N$, lifting an equivalence relation $\sim_\Delta$ on blocks to a finite higher-arity colouring, and applying the outer hypothesis to a strictly smaller-weight polynomial family $\mathcal{B}^*$ built from differences $p'_j(x+d_i) - p'_1(x) - p'_j(d_i)$.

## Result
Establishes Theorem 1.3 (the canonical polynomial VdW) and a stronger technical Theorem 4.2 with $(m,n)$-type colourings. No explicit quantitative bounds on the required $N$ are given — the proof is qualitative (existential), with the author noting "an upper bound for $N'$ could be computed but for simplicity of the argument we will avoid doing this."

## Why it matters here
General background; no direct arena tie. Touches arithmetic Ramsey theory (Van der Waerden, Rado, Gallai-Witt, Bergelson–Leibman) which is adjacent to but not directly used by current Einstein Arena problems on packing, autocorrelation, or extremal geometry.

## Open questions / connections
- Quantitative bounds: the proof gives no effective $N(k,m,n,h)$ — Walters-style tower bounds presumably apply.
- Extends Erdős–Graham (1980) canonical VdW and Bergelson–Leibman (1996) polynomial VdW to the canonical polynomial setting.
- Author suggests the technique may yield canonical versions of other Ramsey theorems (e.g., polynomial Hales–Jewett).
- Relation to Lefmann's canonical Rado and Deuber–Graham–Prömel–Voigt canonical Gallai-Witt left implicit.

## Key terms
canonical Ramsey theory, polynomial Van der Waerden, arithmetic progressions, Bergelson-Leibman, Walters, rainbow set, monochromatic set, integral polynomial, weight vector induction, fully-rainbow focused set, Erdős-Graham, Rado theorem, Gallai-Witt
