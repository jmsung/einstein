---
type: source
kind: paper
title: Gaussian width bounds with applications to arithmetic progressions in random settings
authors: J. Briët, S. Gopi
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1711.05624
source_local: ../raw/2017-brit-gaussian-width-bounds-applications.pdf
topic: general-knowledge
cites:
---

# Gaussian width bounds with applications to arithmetic progressions in random settings

**Authors:** J. Briët, S. Gopi  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1711.05624

## One-line
Upper bounds on the Gaussian width of images of the Boolean hypercube under low-degree multilinear 0-1 polynomial maps, with applications to random-difference Szemerédi theorems and large deviations for arithmetic progressions in random subsets of $\mathbb{Z}/N\mathbb{Z}$.

## Key claim
For a polynomial map $\psi: \mathbb{R}^n \to \mathbb{R}^k$ whose coordinates are multilinear 0-1 polynomials of degree $\le d$ and multiplicity $\le t$, $\mathrm{GW}(\psi(\{0,1\}^n)) \lesssim_d nt \sqrt{k \, n^{1-1/\lceil d/2 \rceil} \log n}$. Two consequences: (i) $[\mathbb{Z}/N\mathbb{Z}]_p$ is $\ell$-intersective w.h.p. when $p \ge \omega(N^{-\beta_\ell} \log N)$ for $\beta_\ell = 1/\lceil (\ell+1)/2 \rceil$; (ii) for odd $k \ge 5$, the BGSZ upper-tail estimate $\Pr[X_k \ge (1+\delta)\mathbb{E}X_k] = p^{(1+o(1))\sqrt{\delta}\,p^{k/2} N}$ holds for $p \ge \omega(N^{-c_k} \log N)$ with $c_k = 1/(6k\lceil (k-1)/2\rceil)$.

## Method
Two-step reduction: (1) homogenize each coordinate polynomial to degree $2\lceil d/2 \rceil$ via Proposition 2.4 (handshaking + extra vertices, preserving multiplicity); (2) reduce to the quadratic case via a "matrix lemma" that realizes $p_H(x) \propto \langle A x^{\otimes m}, x^{\otimes m}\rangle$ for $m = C_r n^{1-1/r}$, using a generalized Birthday-Paradox argument on hypergraph matchings to construct a bounded-norm adjacency matrix $A$. The quadratic bound then follows from the non-commutative Khintchine / Tomczak-Jaegermann (1974) inequality $\mathbb{E}\|\sum g_i A_i\| \lesssim \sqrt{\log N} \, (\sum \|A_i\|^2)^{1/2}$.

## Result
- $\ell$-intersectivity threshold for random differences: $\beta_\ell = 1/\lceil(\ell+1)/2\rceil$, polynomially improving Frantzikinakis-Lesigne-Wierdl's $\beta_\ell = 1/(\ell+1)$ for all $\ell \ge 3$; reproves [BDG17] without LDC/quantum machinery.
- Upper-tail validity range for $k$-APs in $[\mathbb{Z}/N\mathbb{Z}]_p$: quadratic improvement of $c_k$ from $1/(6k(k-1))$ to $1/(6k\lceil(k-1)/2\rceil)$ for odd $k \ge 5$.
- Lemma 1.5 ties the bound to type-$p$ constants of injective tensor products of $\ell_{s_i}^n$ spaces.

## Why it matters here
General background; no direct arena tie — this is high-dimensional probability / additive combinatorics machinery (Gaussian width, non-commutative Khintchine, hypergraph matching decompositions). Most relevant tangentially to sieve/AP-style problems and as a reminder that Tomczak-Jaegermann's matrix Khintchine inequality is the right tool for $\mathbb{E}\|\sum g_i A_i\|$ bounds.

## Open questions / connections
- Can the $\lceil d/2 \rceil$ ceiling in the exponent be replaced by $d/2$? Would yield $1 - 2/d$ and imply conjectured intersectivity / LDP / LDC bounds.
- For constant $d$, an $o(1)$ exponent would resolve conjectures of FLW ($\beta_\ell = 1$ suffices) and BGSZ ($p$ slightly above $N^{-1/(k-1)}$ suffices for the AP upper-tail estimate).
- Lower bounds from LDCs: smallest possible exponent is $\ge (\log\log n)^{r - o(1)}/\log n$ for $d = 2r$, $r \ge 3$ — suggests near-optimality but a gap remains.
- Better type-$p$ constants for $L^n_{r_1,\dots,r_d}$ (injective tensor products) would directly improve Theorem 1.1 via Lemma 1.5.

## Key terms
Gaussian width, non-commutative Khintchine inequality, Tomczak-Jaegermann, Szemerédi theorem, $\ell$-intersective sets, random differences, arithmetic progressions, upper tail large deviations, locally decodable codes, Banach space type, injective tensor product, generalized birthday paradox, hypergraph matching decomposition, multilinear polynomial, Frantzikinakis-Lesigne-Wierdl, Bhattacharya-Ganguly-Shao-Zhao, Chatterjee-Dembo nonlinear LDP
