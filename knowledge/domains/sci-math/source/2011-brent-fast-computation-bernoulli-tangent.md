---
type: source
kind: paper
title: Fast computation of Bernoulli, Tangent and Secant numbers
authors: R. Brent, David Harvey
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1108.0286
source_local: ../raw/2011-brent-fast-computation-bernoulli-tangent.pdf
topic: general-knowledge
cites:
---

# Fast computation of Bernoulli, Tangent and Secant numbers

**Authors:** R. Brent, David Harvey  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1108.0286

## One-line
Asymptotically fast algorithms for computing the first $n$ Bernoulli, Tangent, and Secant numbers in $O(n^2 (\log n)^{2+o(1)})$ bit-operations, plus simple in-place $O(n^2)$ integer-operation algorithms based on three-term recurrences.

## Key claim
The Tangent numbers $T_1,\dots,T_n$ and Bernoulli numbers $B_2,B_4,\dots,B_{2n}$ (and analogously Secant numbers) can all be computed in $O(n^2 (\log n)^{2+o(1)})$ bit-operations using $O(n^2 \log n)$ space — matching the prior best complexity for a *single* $B_n$ (Harvey 2010) while delivering the whole sequence.

## Method
Uses the Kronecker–Schönhage trick: encode the entire scaled sequence $T_k'_{,n} = T_k \cdot (2n-1)!/(2k-1)!$ into the binary expansion of a single high-precision real $z^{1-2n}(2n-1)! \tan z$ with $z = 2^{-\lceil n \lg n \rceil}$, computed via one $N$-bit Newton-iteration division of truncated $\sin z / \cos z$ power series ($N = 2np + 2$) using Schönhage–Strassen multiplication. The simpler $O(n^2)$ companion algorithms exploit the three-term recurrence $p_{n,j} = (j-1)p_{n-1,j-1} + (j+1)p_{n-1,j+1}$ for derivatives of $\tan x$ (resp. $\sec x$) at $0$, executed in-place on positive integers (no cancellation, perfectly stable).

## Result
Theorem 1: $T_1,\dots,T_n$ and $B_2,\dots,B_{2n}$ in $O(n^2 (\log n)^{2+o(1)})$ bit-ops, $O(n^2 \log n)$ space; same for Secant numbers $S_0,\dots,S_n$. Lemmas 1–5 bound truncation/approximation errors at $<0.12 < 1/2$, ensuring integer recovery. Empirically (Magma, 2.26 GHz Core 2 Duo): TangentNumbers computes first 1000 in 1.50 s vs Atkinson's 4.51 s; crossover with FastTangentNumbers occurs somewhat above $n = 1000$. Bernoulli numbers are then recovered via $T_k = (-1)^{k-1} 2^{2k}(2^{2k}-1) B_{2k}/(2k)$.

## Why it matters here
General background; no direct arena tie. Bernoulli numbers appear in Euler–Maclaurin summation used for high-precision evaluation of special functions, which could touch any problem requiring precise zeta-value or asymptotic-expansion work, but no current arena problem in the wiki turns on fast Bernoulli computation.

## Open questions / connections
- Open: can a *single* $B_{2n}$ be computed in $o(n^2)$ bit-operations? (Authors explicitly flag this.)
- Trade-off: Harvey's modular algorithm uses $O(n)$ less space for a single $B_n$ but $O(n)$ more time for all of $B_1,\dots,B_n$; better locality and parallelism.
- Connects to Kronecker–Schönhage substitution as a general "reduce-everything-to-multiplication/division" pattern (Steel 2006), applicable to other sequence-encoding problems.

## Key terms
Bernoulli numbers, Tangent numbers, Secant numbers, Euler numbers, Kronecker–Schönhage trick, Schönhage–Strassen multiplication, Newton iteration power series division, three-term recurrence, Akiyama–Tanigawa, Atkinson algorithm, Von Staudt–Clausen, Euler–Maclaurin, Riemann zeta values, generating functions, high-precision arithmetic
