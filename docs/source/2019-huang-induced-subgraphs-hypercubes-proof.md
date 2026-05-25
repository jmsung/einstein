---
type: source
kind: paper
title: Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture
authors: Hao-wei Huang
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1907.00847
source_local: ../raw/2019-huang-induced-subgraphs-hypercubes-proof.pdf
topic: general-knowledge
cites:
---

# Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture

**Authors:** Hao-wei Huang  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1907.00847

## One-line
A two-page spectral argument resolves the 30-year-old Sensitivity Conjecture by proving a tight $\sqrt{n}$ maximum-degree lower bound for "more-than-half" induced subgraphs of the Boolean hypercube.

## Key claim
For every $n \ge 1$, any induced subgraph $H$ of $Q_n$ on $2^{n-1}+1$ vertices satisfies $\Delta(H) \ge \sqrt{n}$ (tight when $n$ is a perfect square). Via the Gotsman–Linial equivalence, this gives $s(f) \ge \sqrt{\deg(f)}$, hence $bs(f) \le s(f)^4$ for every Boolean function $f$.

## Method
A signed adjacency matrix $A_n$ of $Q_n$ is built recursively ($A_1 = \begin{pmatrix}0&1\\1&0\end{pmatrix}$, $A_n = \begin{pmatrix}A_{n-1}&I\\I&-A_{n-1}\end{pmatrix}$), entries in $\{-1,0,1\}$, with $A_n^2 = nI$ and trace $0$, so its spectrum is $\pm\sqrt n$ each with multiplicity $2^{n-1}$. Restricting to any $(2^{n-1}+1)$-vertex induced subgraph $H$ gives a principal submatrix $A_H$; Cauchy interlacing forces $\lambda_1(A_H) \ge \sqrt n$, and a sign-flip eigenvector argument shows $\Delta(H) \ge \lambda_1(A_H)$.

## Result
$\Delta(H) \ge \sqrt n$ on $|V(H)| = 2^{n-1}+1$, improving the prior $\Omega(\log n)$ bound of Chung–Füredi–Graham–Seymour (1988) and matching their construction. Consequences: $s(f) \ge \sqrt{\deg(f)}$ (Gotsman–Linial conjecture confirmed; tight for AND-of-ORs); combined with Tal's $bs(f) \le \deg(f)^2$, this yields $bs(f) \le s(f)^4$, settling Nisan–Szegedy's Sensitivity Conjecture.

## Why it matters here
General background; no direct arena tie. The transferable wisdom is methodological: a signed/weighted adjacency matrix with a designed spectrum + Cauchy interlacing converts an extremal-combinatorics question into a one-line eigenvalue bound — a template potentially relevant to extremal-graph and discrete-geometry arena problems where a $\pm 1$ signing of the constraint graph might unlock a spectral lower bound.

## Open questions / connections
- Asymptotics of $g(n,k)$: minimum vertex count forcing $\Delta \ge k$ in $Q_n$ induced subgraphs (paper resolves only $k=\sqrt n$).
- Closing the gap between $bs(f) \le s(f)^4$ and the best known quadratic separation $bs \approx \tfrac{2}{3}s^2$ (Ambainis–Sun); the suggestion is to apply the spectral method directly to Boolean functions.
- Generalization: for which highly symmetric graphs $G$ does the signed-matrix-with-$A^2 = \lambda I$ trick yield a tight $\Delta$ bound on $(\alpha(G)+1)$-vertex induced subgraphs?

## Key terms
sensitivity conjecture, block sensitivity, Boolean function degree, hypercube induced subgraph, Cauchy interlace theorem, signed adjacency matrix, spectral graph theory, Gotsman-Linial equivalence, maximum degree lower bound, Huang, Nisan-Szegedy, eigenvalue method
