---
type: source
kind: paper
title: Subset sums, completeness and colorings
authors: David Conlon, Jacob Fox, Huy Tuan Pham
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2104.14766v1
source_local: ../raw/2021-conlon-subset-sums-completeness-colorings.pdf
topic: general-knowledge
cites: 
---

# Subset sums, completeness and colorings

**Authors:** David Conlon, Jacob Fox, Huy Tuan Pham  ·  **Year:** 2021  ·  **Source:** http://arxiv.org/abs/2104.14766v1

## One-line
Develops a unified partition-based framework for finding long (homogeneous) arithmetic progressions in subset sums $\Sigma(A)$, resolving several long-standing Erdős-era problems on Ramsey-complete sequences, monochromatic-sum colorings, and extremal subset-sum-avoidance.

## Key claim
For every $r\ge 2$ there is an $r$-Ramsey-complete sequence with $|A\cap[n]|\le Cr\log^2 n$ and none with $|A\cap[n]|\le cr\log^2 n$ (Thm 1.1); every subset $A\subset[n]$ with $|A|\ge C\sqrt n$ contains a *homogeneous* arithmetic progression of length $n$ in $\Sigma(A)$ (Thm 1.9), the common strengthening of Szemerédi–Vu and Freiman–Sárközy; and $f(n)=\Theta\!\big(n^{1/3}(n/\varphi(n))/((\log n)^{1/3}(\log\log n)^{2/3})\big)$ for the Alon–Erdős monochromatic-sum coloring problem (Thm 1.5).

## Method
Four-step framework: (i) partition $S$ into $\ell$ near-equal parts $S_i$; (ii) split each $S_i=S_i'\cup S_i''$ and show, for $s\in S_i''$, that $\Sigma(S_i')\bmod s$ is large — the technical heart, using probabilistic arguments, Freiman-type structure, and analytic-number-theory sieve estimates (Selberg sieve, Mertens' theorem, $W$-trick on smooth numbers); (iii) deduce $\Sigma(S_i)$ is dense in a long interval; (iv) combine across $i$ to extract a long (homogeneous) progression. Density Lemma 2.8 supplies the random-set core for sparse Ramsey-complete constructions.

## Result
Tight bounds across four problems: (1) sparsest $r$-Ramsey-complete sequence is $\Theta(r\log^2 n)$, extended to all complete polynomial sequences (Thm 1.2); (2) $\varepsilon$-density-complete sequences exist with growth $f_n=e^{(1/(2\log(1/\varepsilon))+o(1))(\log n)^2}$ (Thm 1.3, 1.4); (3) exact $f(n)$ formula with surprising non-monotone $\log\log n$ fluctuations driven by $n/\varphi(n)$; (4) exact $g(n,m)=s(n,m)=\lfloor n/\mathrm{snd}(m)\rfloor+\mathrm{snd}(m)-2$ for $Cn\log n\le m\le n^2/(12\log^2 n)$, asymptotic $\max(s(n,m),(1+o(1))\sqrt{2m})$ up to $\binom{n+1}{2}$ (Thm 1.7); (5) homogeneous-progression version of Szemerédi–Vu at threshold $C\sqrt n$.

## Why it matters here
Direct relevance to additive-combinatorics arena problems: subset-sum density, Sidon-set / $B_h$-set type extremal questions, and any problem where one must guarantee a target integer lies in $\Sigma(A)$. The homogeneous-progression strengthening (Thm 1.9) and the $\sqrt n$ threshold are sharp tools for autocorrelation/sumset problems; the $W$-trick + Selberg-sieve estimates (Lemmas 5.2, 5.9, B.2) are reusable for any "coprime-to-small-primes" residue counting that arises in extremal constructions.

## Open questions / connections
- Extends Szemerédi–Vu (2006), Freiman (1993), Sárközy (1989), Folkman (1966) into one framework; sharpens Alon–Erdős (1996), Alon–Freiman, Lipkin, Tran–Vu–Wood (2017).
- Polynomial-sequence Ramsey-completeness constant $C(k)$ — is the dependence on degree $k$ tight?
- Density-complete behavior below the $\sqrt n$ threshold and for non-polynomial sparse sequences.
- Application to Straus's question on non-averaging sets (mentioned but truncated in source).

## Key terms
subset sums, Ramsey completeness, density completeness, monochromatic sum coloring, Alon-Erdős conjecture, Szemerédi-Vu theorem, Freiman-Sárközy, homogeneous arithmetic progression, Selberg sieve, W-trick, Erdős-Graham extremal, Euler totient, complete sequence, smallest non-divisor
