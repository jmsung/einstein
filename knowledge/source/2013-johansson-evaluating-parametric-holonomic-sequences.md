---
type: source
kind: paper
title: Evaluating parametric holonomic sequences using rectangular splitting
authors: Fredrik Johansson
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1310.3741
source_local: ../raw/2013-johansson-evaluating-parametric-holonomic-sequences.pdf
topic: general-knowledge
cites:
---

# Evaluating parametric holonomic sequences using rectangular splitting

**Authors:** Fredrik Johansson  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1310.3741

## One-line
Adapts the Paterson–Stockmeyer rectangular-splitting (baby-step/giant-step) trick to evaluate the $n$-th term of a parametric holonomic (P-finite) sequence using only $O(n^{1/2})$ "expensive" nonscalar multiplications.

## Key claim
For a holonomic recurrence with matrix $M \in C[x][k]^{r\times r}$ evaluated at $x=z \in H$ (where ops in $H$ are expensive), Algorithm 3 computes $c(z,n)$ in $O(m + n/m)$ nonscalar multiplications, $O(n)$ scalar ops, and $O((n/m)\mathsf{M}(m)\log m)$ coefficient ops; with $m \sim n^{1/2}$ this gives $O(n^{1/2})$ nonscalar mults, $O(n)$ scalar ops, $O(\mathsf{M}(n)\log n)$ coefficient ops, with $O(n^{1/2}\log n)$-bit coefficients over $\mathbb{Z}$.

## Method
Rectangular splitting: write the matrix product $\prod_{i=0}^{n-1} M(x,i)$ as a $w \times m$ grid, precompute a power table $\{z^j\}_{j\le m\deg_x M}$, binary-split each row's small product in $C[x]^{r\times r}$, then evaluate at $x=z$ using only scalar mults against the power table, and accumulate the $w = n/m$ row products in $H^{r\times r}$. Generalizes Smith's algorithms for rising factorials (1989) and hypergeometric series (2001), and an improved variant (Algorithm 4) uses an explicit difference formula $\Delta_m = \prod(x+k+m+i) - \prod(x+k+i)$ with a recurrence due to Kauers for the coefficients.

## Result
Implementation in Arb/FLINT achieves ~20× speedup over naive evaluation for rising factorials at large $n$, and is competitive with fast multipoint evaluation up to $\sim 10^6$ bits while having better numerical stability (loses only a few digits vs. a few percent). Concrete Γ(x) timings: 0.25s at 10000 decimals, 2.7s at 30000, 39s at 100000 — substantially faster than Pari/GP. Generalization to $v$ parameters gives $O(n^{1-1/v})$ nonscalar mults but with rapidly diminishing returns ($O(n^{2v/(v+1)})$ scalar mults).

## Why it matters here
General background; no direct arena tie. Could inform any sub-problem where high-precision special-function evaluation (Γ, hypergeometric, Bessel, error function) becomes the bottleneck inside an optimizer's inner loop — e.g., mpmath polish stages for P5/P6/P11/P14/P17 where ulp-level precision matters. The technique sits between naive and fast-multipoint regimes, the same band where most einstein mpmath work lives ($10^3$–$10^6$ bits).

## Open questions / connections
- Is there a class of parametric holonomic sequences (broader than hypergeometric) where coefficients can be kept at $O(\log n)$ bits rather than $O(n^{1/2}\log n)$?
- Can rectangular splitting be optimized further for specific subclasses (e.g., Bessel-type or confluent hypergeometric series used in extremal-function constructions)?
- Extends Paterson–Stockmeyer (1973), Smith (1989, 2001); complements Chudnovsky–Chudnovsky/Bostan–Gaudry–Schost fast multipoint evaluation and the bit-burst algorithm of van der Hoeven.

## Key terms
holonomic sequence, P-finite recurrence, rectangular splitting, Paterson-Stockmeyer, baby-step giant-step, binary splitting, fast multipoint evaluation, hypergeometric series, gamma function, rising factorial, Stirling series, mpmath polish, Arb library, Johansson, Smith
