---
type: source
kind: paper
title: Bounded Degree Spanners of the Hypercube
authors: R. Nenadov, Mehtaab Sawhney, B. Sudakov, A. Wagner
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1910.09868
source_local: ../raw/2019-nenadov-bounded-degree-spanners-hypercube.pdf
topic: general-knowledge
cites:
---

# Bounded Degree Spanners of the Hypercube

**Authors:** R. Nenadov, Mehtaab Sawhney, B. Sudakov, A. Wagner  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1910.09868

## One-line
Constructs sparse, bounded-degree subgraphs of the Boolean hypercube $Q_n$ that approximately preserve distances, resolving a question of Erdős–Hamburger–Pippert–Weakley and improving the best known degree bound for $2k$-additive spanners.

## Key claim
Two results: (1) there is a spanning subgraph of $Q_n$ with maximum degree $\leq 120$ and diameter exactly $n$; (2) for all $k \in \mathbb{N}$ and $n$ large, there is a $2k$-additive spanner of $Q_n$ with maximum degree $\leq 10^{4k} \cdot \frac{n \ln^{(k+1)} n}{\ln n}$, improving the prior $20 \cdot \frac{n \ln n}{\ln \ln n}$ bound of Arizumi–Hamburger–Kostochka.

## Method
Both constructions hinge on **perfect 1-error-correcting codes** in $Q_{2^r-1}$ and a "nearly perfect code" extension to arbitrary $n$ (via block-parity reduction). For the diameter-$n$ result, an antipodal $2n$-cycle is translated by a nearly perfect code in a transformed basis $f_k = \sum_{i \leq k} e_i$, then composed across 4 coordinate blocks. For the additive spanner, the construction is recursive on $k$: split coordinates into a block $B_0$ of size $\approx \sqrt{n}$ and $t$ remaining blocks, partition $Q_{|B_0|}$ into perfect codes, and assign to each codeword a recursive $2(k{-}1)$-spanner on a chosen $s$-tuple of blocks ($H_2$), plus a "coordinate-sum modulo $s/500k$" gadget ($H_3$) to access the remaining blocks. The invariant tracked: paths between distance-$\ell$ pairs achieve $\geq \ell/(3 \cdot 2^k)$ distinct coordinate sums.

## Result
**Theorem 1.2:** $\exists$ spanning $G \subset Q_n$ with $\Delta(G) \leq 120$ and $\mathrm{diam}(G) = n$ (constant-degree, answering Erdős et al.'s question). **Theorem 1.3:** $\Delta_{2k,\infty}(n) \leq 10^{4k} \cdot n \ln^{(k+1)}(n) / \ln(n)$, where $\ln^{(k+1)}$ is the $(k{+}1)$-fold iterated log. The matching lower bound from prior work is $\Delta_{2k,\infty}(n) \geq e^{-4k} \cdot n \ln n / \ln \ln n$ — exponentially close in $k$.

## Why it matters here
General background; no direct arena tie. The technique of *translating a base structure by a perfect/nearly-perfect code to tile $\{0,1\}^n$ with bounded overlap* is a reusable extremal-combinatorics construction pattern that could inform any arena problem touching Hamming-space tilings, coding-theoretic packings, or hypercube extremal questions.

## Open questions / connections
- Closing the $e^{-4k}$ vs $10^{4k}$ multiplicative gap (and the $\ln^{(k+1)} n$ vs $\ln \ln n$ iterated-log gap) in $\Delta_{2k,\infty}(n)$.
- Question 4.1 (Erdős–Hamburger–Pippert–Weakley): minimum edge count of a diameter-$n$ subgraph of $Q_n$ — current bounds $2^n + \Theta(2^n/n) \leq e_{\min} \leq 2^n + \lfloor n/\binom{n}{n/2}\rfloor - 2$.
- Integrity $I(Q_n)$: gap between $c \cdot 2^n/\sqrt{n}$ and $C \cdot 2^n \sqrt{\log n}/\sqrt{n}$.
- Fewest-edges 2-additive spanner $f_2(n)$: gap $c \cdot 2^n \log n \leq f_2(n) \leq C \cdot 2^n \sqrt{n}$.

## Key terms
hypercube, $Q_n$, additive spanner, $k$-detour subgraph, perfect 1-error-correcting code, Hamming code, bounded degree, diameter preservation, iterated logarithm, nearly perfect code, antipodal cycle, integrity, Erdős–Hamburger–Pippert–Weakley, Arizumi–Hamburger–Kostochka, MacWilliams–Sloane
