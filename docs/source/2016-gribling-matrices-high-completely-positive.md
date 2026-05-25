---
type: source
kind: paper
title: Matrices With High Completely Positive Semidefinite Rank
authors: S. Gribling, David de Laat, M. Laurent
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1605.00988
source_local: ../raw/2016-gribling-matrices-high-completely-positive.pdf
topic: general-knowledge
cites:
---

# Matrices With High Completely Positive Semidefinite Rank

**Authors:** S. Gribling, David de Laat, M. Laurent  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1605.00988

## One-line
Constructs explicit completely positive semidefinite (cpsd) matrices whose factorization rank grows exponentially in matrix size, via extremal bipartite correlation matrices and Clifford algebra representations.

## Key claim
For every positive integer $k$, there exists a cpsd matrix $M$ of size $4k^2+2k+2$ with $\text{cpsd-rank}_{\mathbb{C}}(M) = 2^k$. Hence any upper bound on cpsd-rank as a function of matrix size $n$ must grow at least exponentially. Separately, for $M_k = \begin{pmatrix} I_k & \tfrac{1}{k}J_k \\ \tfrac{1}{k}J_k & I_k \end{pmatrix}$, $\text{cpsd-rank}_{\mathbb{C}}(M_k)=k$ while $\text{cp-rank}(M_k)=k^2$, and $\text{cpsd-rank}_{\mathbb{R}}(M_k)=k$ iff a real Hadamard matrix of order $k$ exists.

## Method
Reduce cpsd-rank lower bounds to finding extreme points of the bipartite correlation polytope $\text{Cor}(m,n)$ with large rank, using Tsirelson's characterization: any nondegenerate commuting operator representation of an extreme correlation is Clifford. Construct extreme $C \in \text{Cor}(r, \binom{r}{2}+1)$ of rank $r$ explicitly (columns $(e_i-e_j)/\sqrt{2}$ and $(e_1+\dots+e_r)/\sqrt{r}$), then invoke Clifford algebra representation theory ($C(r)\otimes C(r)$ irreducible representations have size $\geq (2^{\lfloor r/2\rfloor})^2$) to force exponential local dimension. Lift correlations to quantum correlations $p(a,b|s,t)=\psi^*(X_s^a\otimes Y_t^b)\psi$, which become cpsd matrices of bounded cpsd-rank.

## Result
The $4k^2+2k+2$ matrix achieves the best known size-to-cpsd-rank ratio via this technique, saturating Tsirelson's bound $m+n-1 \geq \binom{r}{2}+1$. Corollary 4.5: any extreme bipartite correlation of rank $r$ requires tensor operator representation of local dimension $\geq 2^{\lfloor r/2\rfloor}$. Provides quadratic separation $\text{cp-rank}/\text{cpsd-rank}_{\mathbb{C}} = k$ for the $M_k$ family.

## Why it matters here
General background; no direct arena tie. Relevant if any arena problem reduces to cpsd / cp matrix factorization or to quantum correlation polytopes; the Tsirelson + Clifford + extreme-point machinery is a template for rank lower bounds in convex factorization cones, conceptually adjacent to LP/SDP bounds the council might invoke for packing/correlation problems.

## Open questions / connections
- Is $\text{cpsd-rank}_{\mathbb{R}}(M_k) = 2k$ when no real Hadamard matrix of order $k$ exists? (Question 2.4)
- Is cpsd-rank of an $n\times n$ cp matrix always $\leq n$? (Question 2.5)
- Whether the set of quantum correlations is closed — would follow if cpsd-rank admits any uniform upper bound; this paper rules out subexponential bounds.
- Extends/parallels Slofstra's XOR-game entanglement lower bound and independent work of Prakash–Sikora–Varvitsiotis–Wei (arXiv:1604.07199).

## Key terms
completely positive semidefinite rank, cpsd cone, bipartite correlation matrix, elliptope, Tsirelson bound, Clifford algebra, extreme point, quantum correlation, Hadamard matrix, XOR game, tensor operator representation, universal rigidity, Gribling, de Laat, Laurent, Slofstra
