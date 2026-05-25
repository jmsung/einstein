---
type: source
kind: paper
title: A maximal extension of the best-known bounds for the Furstenberg–Sárközy theorem
authors: Alex Rice
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1612.01760
source_local: ../raw/2016-rice-maximal-extension-best-known-bounds.pdf
topic: general-knowledge
cites:
---

# A maximal extension of the best-known bounds for the Furstenberg–Sárközy theorem

**Authors:** Alex Rice  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1612.01760

## One-line
Extends the best-known Pintz–Steiger–Szemerédi-style density bound for square-difference-free sets to all intersective polynomials of any degree, via a polynomial-specific sieve using Hensel's Lemma.

## Key claim
If $h \in \mathbb{Z}[x]$ is an intersective polynomial of degree $k \geq 2$ and $A \subseteq [1,N]$ has no nonzero differences of the form $h(n)$, then $|A|/N \ll_{h,c} (\log N)^{-c \log \log \log \log N}$ for any $c < (\log((k^2+k)/2))^{-1}$. Previously this $(\log N)^{-c \log\log\log\log N}$ bound was known only for monomials $n^k$ and intersective quadratics.

## Method
Fourier-analytic double iteration (Hardy–Littlewood circle method on $\mathbb{Z}/N\mathbb{Z}$, following Pintz–Steiger–Szemerédi [19]) using a polynomial-specific sieve: instead of sieving by coprimality to a primorial $W$ (Balog–Pelikán–Pintz–Szemerédi), the inputs are restricted to $n$ where $h'_d(n) \not\equiv 0 \pmod{p^{\gamma_d(p)}}$ for small $p$. Hensel's Lemma then forces square-root cancellation $q^{-1/2}$ in the local exponential sums $\sum_{s \in W_q(Y)} e^{2\pi i h(s) a/q}$ for $q \leq Y$, which is the crucial ingredient the double-iteration method needs. Theorem 1.2 (sums $g(m)+h(n)$ of two intersective polynomials, giving $|A|/N \ll e^{-c(\log N)^\mu}$ with $\mu(2,2)=1/2$) uses a simpler single $L^2$ density increment.

## Result
Theorem 1.1 gives the maximal extension to all intersective polynomials. Theorem 1.2 gives $|A|/N \ll_{g,h} \exp(-c(\log N)^\mu)$ for sums of two intersective polynomials, with $\mu(2,2) = 1/2$. Theorem 5.7 extends to sums of $\ell \geq 3$ intersective polynomials with $\mu = 1/2$ when $\sum \deg(h_i)^{-1} \geq 1$, else $\mu = 1/6$. The standalone exponential sum theorem (Theorem 2.7) packages major-arc asymptotic, square-root cancellation, and a Weyl-type minor-arc estimate over the sieved set $W(Y)$.

## Why it matters here
General background; no direct arena tie. Relevant to additive-combinatorics problems in the inventory that involve **difference sets, polynomial patterns, or Sárközy-style density bounds** — the circle-method + sieve template (auxiliary polynomial $h_d(x)=h(r_d+dx)/\lambda(d)$, Hensel-lifting for square-root cancellation, double iteration vs single $L^2$ increment) is the canonical density-increment toolkit when extremal sets must avoid prescribed arithmetic patterns.

## Open questions / connections
- Can the constant $c$ in Theorem 1.1 be made independent of $k$, ideally approaching the method's natural limit $1/\log 3$? (Rice notes this is plausible by mimicking [1] and [8] more closely.)
- Lower-bound side is wide open: Ruzsa's construction gives $N^c$ with $c \approx 0.7334$ (Lewko's $q=205,|B|=12$); the true threshold for square-difference-free sets is conjectured by some to be $N^{1-\epsilon}$.
- Multivariable extension to intersective polynomials not expressible as sums of single-variable intersective polynomials (e.g. $x^3+y^3-p$ for $p$ not a sum of two integer cubes) remains.

## Key terms
Furstenberg–Sárközy theorem, intersective polynomial, difference set, density increment, Hardy–Littlewood circle method, Hensel's Lemma, Weyl sum, square root cancellation, double iteration, auxiliary polynomial, sieve, Pintz–Steiger–Szemerédi, Sárközy, additive combinatorics
