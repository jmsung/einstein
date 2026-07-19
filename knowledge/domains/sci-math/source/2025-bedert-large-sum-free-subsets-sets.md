---
type: source
kind: paper
title: Large sum-free subsets of sets of integers via $L^1$-estimates for trigonometric series
authors: Benjamin Bedert
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2502.08624
source_local: ../raw/2025-bedert-large-sum-free-subsets-sets.pdf
topic: general-knowledge
cites:
---

# Large sum-free subsets of sets of integers via $L^1$-estimates for trigonometric series

**Authors:** Benjamin Bedert  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2502.08624

## One-line
Proves that every set of $N$ integers contains a sum-free subset of size at least $N/3 + c \log\log N$, settling a long-standing problem of Erdős.

## Key claim
There exists an absolute constant $c > 0$ such that for every finite $A \subset \mathbb{Z}$, $S(A) \geq |A|/3 + c \log\log |A|$ — the first super-constant improvement over the Erdős–Alon–Kleitman–Bourgain $N/3 + O(1)$ bound, answering Problem 1 on Green's list of 100 open problems. Also a "99% structure theorem": sets $A$ with $S(A) \leq N/3 + C$ admit a partition $A = \bigsqcup A_j \cup B$ where each $A_j$ has small doubling $\ll (CK)^{O(1)}|A_j|$ and $|B| \ll (CK)^{-10} N$.

## Method
Refines Bourgain's Fourier-analytic approach: bounding $S(A)$ reduces to lower-bounding the $L^1$-norm of $F_A(x) = \sum_{a\in A}\sum_{n\geq 1} \chi(n)/n \cdot \cos(2\pi nax)$ where $\chi$ is the nontrivial character mod 3. The new ingredients are (i) an inverse $L^1$-theorem (via Rudin's inequality + a modified McGehee–Pigno–Smith test-function construction) showing $\|\hat{1}_B\|_1 \ll C \log N$ forces small additive dimension $\dim(B) \ll C^2 (\log N)^3$; (ii) Freiman-rectification to a "dense" model in $[-N^{C^{O(1)}}, N^{C^{O(1)}}]$; (iii) a non-Archimedean analysis of $A$'s distribution modulo small primes $p \leq (\log N)^{1/2}$, culminating in a $p$-adic-ordered MPS test function (Thm 8.2) that produces a chain of $J \gg \log N / \log\log N$ nested residue classes witnessing $\|F_A\|_1 \gg \log\log N$.

## Result
$S(N) \geq N/3 + c \log\log N$ for an absolute $c > 0$, improving Bourgain's $N/3 + 2/3$. Equivalently, there is an $F_4$-isomorphic copy $B$ of $A$ with $\|F_B\|_1 \gg \log\log |B|$. Companion inverse result (Cor 5.2): $\dim(B) \ll \|\hat{1}_B\|_1^2 \log |B|$, tight up to constants (Fejér kernel example). The structure theorem gives Bohr-progression-like control whenever $S(A) - N/3$ stays bounded.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological: $L^1$-estimates for character/cosine polynomials, Rudin's dissociated-set inequality, additive-dimension inverse theorems, and Freiman/Balog–Szemerédi–Gowers rectification — toolbox shared with autocorrelation-inequality problems and any extremal-additive-combinatorics task where one is bounding $\max_x \sum_a g(ax)$ for a fixed sum-free or interval-shaped $g$.

## Open questions / connections
- Closing the $\log\log N$ vs $o(N)$ gap against Eberhard–Green–Manners' matching upper bound $N/3 + o(N)$ — quantitative version of $o(N)$ remains open and ineffective.
- Extending the non-Archimedean MPS construction to $(k,\ell)$-sum-free problems where the maximal sum-free subinterval of $\mathbb{T}$ is unique (Bourgain's symmetric-interval trick fails) — Jing–Wu handled the asymmetric cases.
- Sharpening the inverse $L^1$-theorem (Thm 5.1): is the $(|D|/\log N)^{1/2}$ exponent tight in the Littlewood-conjecture regime? Connects to Konyagin / Pichorides bounds.

## Key terms
sum-free set, Erdős problem, Littlewood $L^1$ conjecture, McGehee–Pigno–Smith, Bourgain, Rudin inequality, dissociated set, additive dimension, Freiman isomorphism, Balog–Szemerédi–Gowers, generalised arithmetic progression, character mod 3, non-Archimedean test function, additive combinatorics, de la Vallée-Poussin kernel
