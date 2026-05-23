---
type: source
kind: paper
title: Flip Graphs with Symmetry and New Matrix Multiplication Schemes
authors: Jakob Moosbauer, M. Poole
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2502.04514
source_local: ../raw/2025-moosbauer-flip-graphs-symmetry-new.pdf
topic: general-knowledge
cites:
---

# Flip Graphs with Symmetry and New Matrix Multiplication Schemes

**Authors:** Jakob Moosbauer, M. Poole  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2502.04514

## One-line
Imposing $C_3$ and $C_3 \times Z_2$ symmetry on the flip graph search for matrix multiplication decompositions shrinks the space enough to discover new rank-93 ($5\times 5$) and rank-153 ($6\times 6$) schemes over arbitrary fields.

## Key claim
New upper bounds on the tensor rank of small matrix multiplication: $R(\langle 5,5,5 \rangle) \le 93$ (improving 97, and 94 over $\mathbb{F}_2$) and $R(\langle 6,6,6 \rangle) \le 153$ (improving 160), both valid over arbitrary ground fields via Hensel lifting from $\mathbb{F}_2$ to $\mathbb{Z}$.

## Method
Extends the Kauers–Moosbauer flip graph algorithm — random walks on a graph of rank-$r$ decompositions of $M_n = \sum E_{i,j} \otimes E_{j,k} \otimes E_{k,i}$ connected by flips, reductions, and plus-transitions — by restricting to $G$-invariant schemes for $G = C_3$ (cyclic permutation of factors) or $G = C_3 \times Z_2$ (plus row/column reversal). Theorem 4 shows flips/reductions on orbit representatives lift to whole-orbit transformations, so the search runs on representatives. Starting points are seeded from "diagonal partitions" of $\{1,\dots,n\}$ to handle the $C_3$-fixed diagonal tensors; solutions over $\mathbb{F}_2$ are lifted via a symmetry-preserving cyclic Brent-equation Hensel lift through 2-adic approximations.

## Result
- $n=5$: $G=C_3$, partition $\{\{1,5\},\{2,4\},\{3\}\}$, flip limit $10^8$ → rank 93 in minutes on a laptop.
- $n=6$: $G=C_3 \times Z_2$, partition $\{\{1,2\},\{3,4\},\{5,6\}\}$, flip limit $10^9$ → rank 153 in ~80 CPU-hours; "atomic" (not built from smaller schemes).
- $n=3$: matches known 23; $n=4$: symmetric rank 49 (vs 47 unsymmetric).
- Crossing $\log_5 91 = 2.803$ or $\log_6 152 = 2.804$ would beat Strassen's exponent asymptotically. Implementation runs 1–6 billion flips/min in optimized C++.

## Why it matters here
General background; no direct arena tie. The flip-graph-with-symmetry pattern — restrict search to a group-invariant subspace, then lift from a small finite field — is a transferable methodology relevant to any problem where a symmetry ansatz collapses a combinatorial search space (e.g. symmetric sphere packings, symmetric autocorrelation extremizers, equioscillating configurations).

## Open questions / connections
- Can the bound for $n=5$ drop by 2 (to 91) or $n=6$ by 1 (to 152) to beat Strassen's $\omega$ asymptotically?
- Why is liftability $\mathbb{F}_2 \to \mathbb{Z}$ empirically much more common for symmetric schemes than asymmetric ones? Authors observe this but don't prove it.
- Extends Kauers–Moosbauer flip graphs [16,17], Arai–Ichikawa–Hukushima plus-transitions [2], Ballard et al. symmetric numerical search [3], Grochow–Moore group-orbit constructions [12], Burichenko symmetry analysis [5,6].
- Connectivity of the symmetric flip graph fails when char $K$ divides $|G|$ (e.g. Strassen over $\mathbb{F}_2$ unreachable from some starting points) — choice of starting point becomes load-bearing.

## Key terms
matrix multiplication tensor, tensor rank, flip graph, Strassen algorithm, symmetry group, $C_3$ cyclic symmetry, $Z_2$ reversal, orbit flip, Hensel lifting, Brent equations, plus-transition, diagonal partition starting point, $\omega$ matrix multiplication exponent, Moosbauer, Kauers
