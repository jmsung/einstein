---
type: source
kind: paper
title: Binary Linear Codes With Few Weights From Two-to-One Functions
authors: Kangquan Li, Chunlei Li, T. Helleseth, Longjiang Qu
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2006.12395
source_local: ../raw/2020-li-binary-linear-codes-few.pdf
topic: general-knowledge
cites:
---

# Binary Linear Codes With Few Weights From Two-to-One Functions

**Authors:** Kangquan Li, Chunlei Li, T. Helleseth, Longjiang Qu  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2006.12395

## One-line
Constructs binary linear codes with 1, 3, 4, or 5 nonzero weights by feeding two-to-one functions over $\mathbb{F}_{2^n}$ into two standard generic code constructions, then computing Walsh transforms of the underlying quadratics.

## Key claim
For two families of two-to-one functions over $\mathbb{F}_{2^n}$ — (a) generalized quadratics $f$ with $f(x^e)$ quadratic and $\gcd(e, 2^n-1)=1$, and (b) $f(x)=(x^{2^t}+x)^e$ with $\gcd(t,n)=\gcd(e,2^n-1)=1$ — the authors derive explicit weight distributions of the resulting codes $C_f$ and $C_{D(f)}$, including new 1-, 3-, 4-, and 5-weight codes, several of which meet the sphere-packing bound on the dual (Theorem 1: $d^\perp_{D(f)}=3,4$; equality at $d_{K_2}=1$).

## Method
Two generic constructions: $C_f = \{(\mathrm{Tr}_n(ax+bf(x)))_{x\in\mathbb{F}_{2^n}^*}\}$ and $C_{D(f)}$ defined by the image set $D(f)=\mathrm{Im}(f)\setminus\{0\}$ of a two-to-one $f$. Hamming weights are read off Walsh transforms $W_f(a,b)=\sum_x (-1)^{\mathrm{Tr}_n(ax+bf(x))}$; for quadratic $f$, $W_f(a,b)\in\{0,\pm 2^{(n+d_b)/2}\}$ where $d_b=\dim\ker B_{\varphi_b}$. Weight distributions are pinned down via the first three Pless power moments. Proposition 22 reduces $W_f$ for $f=P\circ\psi$ (with $\psi$ two-to-one onto $\ker\mathrm{Tr}_n$) to the Walsh spectrum of $\mathrm{Tr}_n(xe)$, linking the codes to almost-bent / Niho exponents.

## Result
- 1-weight (constant-weight) and 3-weight code families derived from quadrinomial / trinomial two-to-one maps in Lemmas 5–7 (e.g. $f(x)=x^{(2^{n-1}+2^{m-1})/3}+x^{2^m}+\omega x$, $n=2m$, $m$ odd), with explicit multiplicities (Tables I–IX).
- $C_{D(f)}$ has parameters $[2^{n-1}-1, n]$ with three weights $2^{n-2}\pm 2^{m-1}$ and $2^{n-2}$ (Hadamard-like; dual is the binary Hamming code $[2^{n-1}-1, 2^{n-1}-n, 3]$).
- For $f=(x^{2^t}+x)^e$ with $e$ almost-bent (Gold, Kasami, Welch, Niho-1/2), $C_{D(f)}$ is a 3-weight code with weights $2^{n-2}, 2^{n-2}\pm 2^{(n-3)/2}$ (Theorem 24).
- For Gold $e=2^i+1$, $C_f$ has 5 weights $2^{n-1}, 2^{n-1}\pm 2^{(n\pm 1)/2}$ (Theorem 25).
- Several constructions are optimal or match best-known parameters in Grassl's table.

## Why it matters here
General background; no direct arena tie. None of the 23 Einstein Arena problems sits in binary-code/Walsh-spectrum territory, so this paper does not inform a current optimizer. The closest relevance is methodological — Walsh-transform / character-sum bookkeeping and Pless-moment systems as templates for any problem where a small image set forces a discrete weight/score distribution.

## Open questions / connections
- Problem 20 / Conjecture 21 / Conjecture 26: weight distributions of $C_f$ for Theorem 10, Theorem 17, the $3\cdot 2^{m+1}+1$ family, and the $(x^{2^t}+x)^e$ Gold-Cf family remain open.
- Proposition 22 generalizes: any $e$ with $t$-valued Walsh spectrum of $\mathrm{Tr}_n(x^e)$ yields a $t$-weight $C_{D(f)}$ — exploitable for Kasami/Welch/Niho extensions surveyed in Li–Zeng [24].
- Builds on Mesnager–Qu's systematic study of two-to-one maps [25] and Li–Mesnager–Qu trinomial/quadrinomial families [22].

## Key terms
binary linear codes, two-to-one functions, Walsh transform, Walsh spectrum, quadratic Boolean functions, almost bent functions, Gold exponent, Kasami exponent, Welch exponent, Niho exponent, Pless power moments, sphere packing bound, weight distribution, defining-set construction, Hamming code
