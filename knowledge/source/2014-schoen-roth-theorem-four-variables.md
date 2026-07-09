---
type: source
kind: paper
title: ROTH’S THEOREM FOR FOUR VARIABLES AND ADDITIVE STRUCTURES IN SUMS OF SPARSE SETS
authors: T. Schoen, Olof Sisask
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1408.2568
source_local: ../raw/2014-schoen-roth-theorem-four-variables.pdf
topic: general-knowledge
cites:
---

# ROTH'S THEOREM FOR FOUR VARIABLES AND ADDITIVE STRUCTURES IN SUMS OF SPARSE SETS

**Authors:** T. Schoen, Olof Sisask  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1408.2568

## One-line
Establishes near-Behrend-shape upper bounds for the largest subset of $[N]$ avoiding solutions to $x+y+z=3w$, closing the exponential gap between three-variable and many-variable Roth-type theorems.

## Key claim
If $A \subseteq [N]$ has no non-trivial solutions to $x+y+z=3w$, then $|A| \leq N / \exp(c(\log N)^{1/7})$. In $\mathbb{F}_q^n$ the analogous bound is $\alpha \leq \exp(-\Omega(n^{1/5}))$. The exponent $1/7$ cannot exceed $1/2$ (Behrend lower bound).

## Method
Density increment strategy combined with $L^p$-almost-periodicity of convolutions (Croot–Sisask) and Chang–Sanders spectral structure for Bohr sets. Two proofs: (i) $L^\infty$-almost-periodicity of three-fold convolutions $1_{-3\cdot A} * 1_A * 1_{A+A}$, splitting on whether $|A+A|$ is large/small; (ii) combinatorial control via three-fold sumset structure $B+A-A$. Iterates on regular Bohr sets with rank growth $\sim \log^4(2/\alpha)$ per step.

## Result
Four-variable equation $x+y+z=3w$: $|A| \leq N/\exp(c(\log N)^{1/7})$ (Thm 1.4). Finite field version: $\alpha \leq \exp(-\Omega(n^{1/5}))$ in $\mathbb{F}_q^n$ (Thm 1.5). Sumset structure: $3A$ for $A \subseteq [N]$ of density $\alpha$ contains an AP of length $\exp(c(\log N / \log^3(2/\alpha))^{1/2})$ (Thm 1.6), non-trivial down to $\alpha \geq \exp(-c(\log N)^{1/5})$. In $\mathbb{F}_5^n$, $3A$ contains an affine subspace of dimension $\geq cn/\log^3(2/\alpha) - \log(1/\alpha)$ (Thm 1.7).

## Why it matters here
General background on additive-combinatorics density-increment techniques and Bohr-set machinery; no direct Einstein Arena tie. Tangentially relevant to any arena problem involving extremal set densities under linear constraints (sieve, Sidon-like) — informs how "almost-periodicity + spectral structure" produces sub-exponential density bounds.

## Open questions / connections
- Does the four-fold-sumset behavior ($4A$ contains a full affine subspace of codim $C\log^4(1/\alpha)$) actually hold for $3A$? A positive answer likely implies Behrend-shape bounds for Roth's theorem itself.
- Closing the gap between $(\log N)^{1/7}$ and the conjectured $(\log N)^{1/2}$ for four-variable equations.
- Question 9.2: do $A,B \subseteq [N]$ of density $N^{-c}$ and $C$ of density $\exp(-C(\log N)^{2/3})$ force $A+B+C$ to contain unbounded APs?
- Extends Schoen–Shkredov (six-variable, exp 1/7) and Bloom (four/five-variable, logarithmic) — bridges them with Behrend-shape exponents.

## Key terms
Roth's theorem, four-variable equation, $x+y+z=3w$, Behrend construction, density increment, Bohr sets, almost-periodicity, Croot–Sisask lemma, Chang's theorem, Bogolyubov–Ruzsa lemma, sumsets, arithmetic progressions, translation-invariant equations, additive combinatorics, finite field model
