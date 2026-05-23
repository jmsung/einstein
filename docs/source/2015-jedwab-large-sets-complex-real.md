---
type: source
kind: paper
title: Large sets of complex and real equiangular lines
authors: J. Jedwab, Amy Wiebe
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1501.05395
source_local: ../raw/2015-jedwab-large-sets-complex-real.pdf
topic: general-knowledge
cites:
---

# Large sets of complex and real equiangular lines

**Authors:** J. Jedwab, Amy Wiebe  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1501.05395

## One-line
Constructs $\Theta(d^2)$ equiangular lines in $\mathbb{C}^d$ and $\mathbb{R}^d$ directly from sets of mutually unbiased bases (MUBs) via a concatenation-with-scaled-entries trick.

## Key claim
For any positive integer $t$: there exist $d^2$ equiangular lines in $\mathbb{C}^{(t+1)d}$ when $d$ is a prime power (Corollary 2), and $d^2/2$ equiangular lines in $\mathbb{R}^{(t+1)d}$ when $d$ is a power of $4$ (Corollary 3). The common angle is $\arccos(1/(1+\sqrt{d}))$ regardless of $t$.

## Method
Given $r$ MUBs $B_1,\dots,B_r$ in $\mathbb{C}^d$ whose vectors have unit-magnitude entries, scale the $j$-th entry of basis $B_j$ by parameters $v \in \{a_1,\dots,a_t, t+1-\sum a_j\}$, then concatenate the $t+1$ scaled copies into vectors in $\mathbb{C}^{(t+1)d}$. The MUB property $|\langle x,y\rangle|=\sqrt{d}$ for vectors from distinct bases, plus orthogonality within a basis, forces only two possible inner-product magnitudes; choosing $a_j = 1+d^{1/4}/\sqrt{t}$ equates them. A weighted generalization with real coefficients $c_1,\dots,c_t$ preserves the same common angle.

## Result
Concrete bound: $d^2$ complex equiangular lines in dimension $(t+1)d$ for any $t\geq 1$ and prime-power $d$, and $d^2/2$ real equiangular lines in dimension $(t+1)d$ for $d$ a power of $4$ (using $d/2+1$ real MUBs from Calderbank–Cameron–Kantor–Seidel). This matches the $\Theta(D^2)$ order of magnitude in the ambient dimension $D=(t+1)d$, giving a flexible family that varies $t$ while keeping the common angle $\arccos(1/(1+\sqrt{d}))$ fixed. A small extension yields $16$ equiangular lines in $\mathbb{R}^8$ (case $t=1$, $d=4$).

## Why it matters here
General background for problems involving equiangular line systems, Welch-type bounds, and code-design constructions; relates to discrete-geometry / packing problem categories via the $D^2$-vs-$D(D+1)/2$ extremal question. Adds a direct MUB→equiangular-lines construction recipe to the wiki's repertoire of explicit large equiangular families (Köenig $d^2-d+1$, de Caen $2(d+1)^2/9$).

## Open questions / connections
- Open: can the Gerzon bound $D(D+1)/2$ (real) or $D^2$ (complex) be attained for infinitely many $D$? This paper gives $\Theta(D^2)$ but not the exact upper bound.
- Extends Jedwab–Wiebe 2014 (arXiv:1408.5169) special case $t=1$, $r=d$, removing the relative-difference-set restriction.
- The $\mathbb{R}^8$ extension to 16 lines (matching Gerzon bound for $D=8$) does not obviously generalize — what structural obstruction prevents lifting it to larger $d$?

## Key terms
equiangular lines, mutually unbiased bases, MUBs, Gerzon bound, Welch bound, prime power dimension, Hermitian inner product, Delsarte-Goethals-Seidel, de Caen construction, Calderbank-Cameron-Kantor-Seidel, real equiangular lines, complex equiangular lines, sphere packing in projective space, frame theory
