---
type: source
kind: paper
title: When the sieve works
authors: Andrew Granville, Dimitris Koukoulopoulos, Kaisa Matomäki
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1205.0413v2
source_local: ../raw/2012-granville-when-sieve-works.pdf
topic: general-knowledge
cites: 
---

# When the sieve works

**Authors:** Andrew Granville, Dimitris Koukoulopoulos, Kaisa Matomäki  ·  **Year:** 2012  ·  **Source:** http://arxiv.org/abs/1205.0413v2

## One-line
Identifies when sieving an interval of length $x$ by a set $\mathcal{P}$ of primes (including some in $(\sqrt{x}, x]$) leaves the expected number of unsieved integers, using additive-combinatorial reductions.

## Key claim
If $\mathcal{P} \subseteq \{p \le x\}$ and there exists $v \le c\sqrt{\log x}$ with $\sum_{p \in \mathcal{P}, x^{1/ev} < p \le x} 1/p \ge 1 + \lambda$, then $\Psi(x; \mathcal{P})/x \gg v^{-O(v)} \prod_{p \in \mathcal{E}}(1 - 1/p)$, where $\mathcal{E}$ is the complementary set of primes. The key quantity governing sieve behavior is $\kappa = \sum_{p \in \mathcal{P}, p \ge y} 1/p$ for the largest $y$ where $\kappa > 1$.

## Method
Reduces the lower-bound problem for $\Psi(x; \mathcal{P})$ to a quantitative continuous-additive-combinatorics question (Hypothesis T, after Bleichenbacher's theorem on $\int dt/t > 1/u$ implying solutions to $t_1 + \cdots + t_k = 1$). Introduces equivalent discrete (Hypothesis A) and prime-counting (Hypothesis P) versions; proves Hypothesis A using Balog–Szemerédi–Gowers (Lemma 5.1), Ruzsa–Chang / Freiman-type structure (Lemma 5.2), and popular-subset arguments on generalized arithmetic progressions (Lemma 5.3).

## Result
Theorem 1: explicit lower bound $\Psi(x; \mathcal{P})/x \gg v^{-O(v)} \prod_{p \in \mathcal{E}}(1-1/p)$ under the $1 + \lambda$ tail-sum hypothesis. Corollary 2.3: as soon as $\kappa > \epsilon$, some $t \in [x^{1/u}, x]$ achieves expected size. Proposition 2.6: if $\kappa = o(1)$, then $\Psi(t; \mathcal{P})$ is much smaller than expected for some $t \in [\sqrt{x}, x]$, with explicit Rankin-method bound $\Psi(x; \mathcal{P})/x \ll e^{O(u)}/(u \log u)^u \cdot \prod_p (1-1/p)$.

## Why it matters here
General background for sieve-theory problems (P12 prime-counting, sieve-bound-style discrete combinatorics); the criterion "$\kappa > 1$ governs sieve success" is a transferable diagnostic. Bleichenbacher-style continuous additive-combinatorics reductions may inform autocorrelation / interval-packing problems where the sieve metaphor is structural.

## Open questions / connections
- Hypothesis T conjectured for all $\lambda_3 > 0$; current proof gives a large unspecified $\lambda$ (estimated $< 21$ via Lev's refinement) — sharp constant open.
- Conjecture 1: bolder guess $A_v \sim v \rho(v)$ where $\rho$ is Dickman–de Bruijn.
- Extends Hildebrand (1987), Friedlander (1976), Hall (1974); applies via Matomäki to counting real zeros of holomorphic cusp forms.

## Key terms
sieve theory, Bleichenbacher theorem, Balog-Szemerédi-Gowers, Ruzsa-Chang, additive combinatorics, Dickman-de Bruijn function, smooth numbers, Rankin method, generalized arithmetic progression, Granville, Koukoulopoulos, Matomäki, prime sieving, $\Psi(x;\mathcal{P})$
