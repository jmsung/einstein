---
type: source
kind: paper
title: Breaking the logarithmic barrier in Roth's theorem on arithmetic progressions.
authors: T. Bloom, Olof Sisask
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2007.03528
source_local: ../raw/2020-bloom-breaking-logarithmic-barrier-roth.pdf
topic: general-knowledge
cites:
---

# Breaking the logarithmic barrier in Roth's theorem on arithmetic progressions.

**Authors:** T. Bloom, Olof Sisask  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2007.03528

## One-line
First proof that subsets of $\{1,\dots,N\}$ with no 3-term arithmetic progression have size $\ll N/(\log N)^{1+c}$, breaking the long-standing $\log N$ density barrier.

## Key claim
If $A\subset\{1,\dots,N\}$ contains no non-trivial 3-AP (no $x+y=2z$ with $x\neq y$), then $|A|\ll N/(\log N)^{1+c}$ for an absolute constant $c>0$ (in principle effective but tiny, heuristically $c\approx 2^{-2^{1000}}$). As a corollary, every $A\subset\mathbb{N}$ with $\sum_{n\in A}1/n=\infty$ contains infinitely many 3-APs — the first non-trivial case of Erdős's conjecture.

## Method
Fourier-analytic density-increment in Bohr sets: spectrum $\Delta_\eta(A)$ at level $\eta$ has size $\gtrsim \alpha\eta^{-3}$ (Shkredov's higher-energy inequality $E_{2m}(\Delta)\gtrsim\alpha\eta^{2m}|\Delta|^{2m}$); Bateman–Katz "additively non-smoothing" structure ($e_8\approx e_4^3$) yields subsets $X,H$ with $|X||H|\approx\alpha^2|\Delta|^2$ and $E(X,H)\gtrsim|X||H|^2$, $\dim H = O(1)$; new "spectral boosting" converts this spectral $X,H$ structure into an $L^\infty$ density increment on a Bohr set; Croot–Sisask almost-periodicity supplies the physical-space regularity. Iterating the dichotomy [many 3-APs] vs [increment of strength $[K^{O(1)},K^{O(1)}]$ or $[K,K^{-1}\alpha^{-1}]$] with $K=\alpha^{-c}$ gives $T(A)\geq\exp(-O(\alpha^{-1+c}))$.

## Result
Density bound $r(N)\ll (\log N)^{-1-c}$, improving the prior $(\log N)^{-1+o(1)}$ (Sanders 2011, Bloom 2016, Bloom–Sisask 2019, Schoen 2020). Yields 3-APs in primes via Chebyshev alone, with relative density $\ll(\log N)^{-c}$ (vs Naslund's $(\log\log N)^{-1+o(1)}$). Lower bound (Behrend) remains $r(N)\geq\exp(-O(\sqrt{\log N}))$; gap to conjectured $\exp(-c(\log N)^{1/2})$ remains huge.

## Why it matters here
Direct relevance to extremal/combinatorial AP-free set problems and any Einstein Arena problem touching Roth-type counting, additive energy, or spectrum structure (Sidon sets, sieve theory, autocorrelation inequalities). Introduces *spectral boosting* and *non-smoothing structure theorems* — generic tools for converting "Fourier mass is concentrated on a structured set" into a usable $L^\infty$ bump, which is the universal density-increment template behind many extremal-combinatorics bounds.

## Open questions / connections
- Conjecture 13.2/13.4: every spectrum $\Delta_\eta(A)$ contains $X,H$ with $|X||H|\gtrsim\alpha\eta^2|\Delta|^2$ and $E(X,H)\gtrsim|X||H|^2$ — would push the upper bound toward $\exp(-c(\log N)^{c'})$.
- Conjecture 13.3/13.5: every spectrum has a subset of size $\epsilon|\Delta_\eta(A)|$ with dimension $\lesssim\epsilon\eta^{-2}$ — strengthens Chang's lemma; open in range $\eta\geq\epsilon\geq\eta^2$.
- Strengthen Theorem 9.1 (non-smoothing structure) from polynomial in $\tau^{-1/\log k}$ to $\tau^{-1/k}$; replace crude energy bounds in Prop 8.1 to avoid large increments — together would yield $r(N)\ll\exp(-c(\log N)^{c'})$, possibly with $c'=1/2$ (best possible).
- Polynomial method (Croot–Lev–Pach, Ellenberg–Gijswijt) gives $|A|\leq c^n$ in $\mathbb{F}_3^n$ but has not been adapted to $\mathbb{Z}$; Fourier methods remain the only route here.

## Key terms
Roth's theorem, 3-term arithmetic progressions, density increment, Bohr sets, spectrum, additive energy, non-smoothing sets, spectral boosting, Chang's lemma, almost-periodicity, Bateman–Katz, Behrend construction, Shkredov, Erdős conjecture, Meshulam bound
