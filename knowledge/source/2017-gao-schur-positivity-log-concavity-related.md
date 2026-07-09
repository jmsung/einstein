---
type: source
kind: paper
title: Schur positivity and log-concavity related to longest increasing subsequences
authors: Alice L. L. Gao, M. H. Xie, A. Yang
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1703.06382
source_local: ../raw/2017-gao-schur-positivity-log-concavity-related.pdf
topic: general-knowledge
cites:
---

# Schur positivity and log-concavity related to longest increasing subsequences

**Authors:** Alice L. L. Gao, M. H. Xie, A. Yang  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1703.06382

## One-line
Proves log-concavity of standard-Young-tableau counts $f^\lambda$ along two rectangular partition families by establishing Schur positivity of the corresponding Schur-function differences, generalizing Bóna–Lackner–Sagan from $m=1,2$ to all $m$.

## Key claim
For positive integers $m,n$: (1) for $\lceil n/2\rceil < k < n$, $(f^{(k^m,(n-k)^m)})^2 \ge f^{((k+1)^m,(n-k-1)^m)} f^{((k-1)^m,(n-k+1)^m)}$; (2) for $1 < k < n$, $(f^{(k^m,1^{m(n-k)})})^2 \ge f^{((k+1)^m,1^{m(n-k-1)})} f^{((k-1)^m,1^{m(n-k+1)})}$. Equivalently, the differences $s_\lambda^2 - s_{\lambda^+} s_{\lambda^-}$ of Schur functions are Schur positive.

## Method
Two proofs. (1) Hook-length formula via the Frobenius/Frame–Robinson–Thrall identity, reducing log-concavity to AM-GM on linear factors $(2k-n+1+i_1+i_2)$ plus log-convexity of a Gamma-function ratio (digamma/trigamma $\psi'(z) = \sum 1/(z+k)^2 > 0$ and decreasing). (2) Schur-positivity proof using Lam–Postnikov–Pylyavskyy's theorem on $s_{\lfloor(\lambda+\nu)/2\rfloor}s_{\lceil(\lambda+\nu)/2\rceil} - s_\lambda s_\nu$ (resolving an Okounkov conjecture) plus their $\text{sort}_1,\text{sort}_2$ result (Fomin–Fulton–Li–Poon conjecture).

## Result
Theorem 1.1 (both parts above) is established for all positive integers $m$. As Corollary 2.3, this proves log-concavity of $\{\ell^\Lambda_{mn,k}\}$ and $\{i^\Lambda_{mn,k}\}$ for $\Lambda$ the two rectangular shape families, extending Bóna–Lackner–Sagan Theorems 1.4 beyond $m\in\{1,2\}$. The Schur-positivity route also suggests new Schur-positive strengthenings of Chen's original conjectures (Conjectures 3.4, 3.5, 3.7), verified numerically up to $n\le 9$, $n\le 20$, $n\le 30$ respectively.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological — log-concavity via algebraic positivity (Schur expansion) is a structural technique that could inform extremal-combinatorics problems where a sequence of counts needs a unimodality/log-concavity certificate.

## Open questions / connections
- Chen's full conjecture (log-concavity of $\{\ell_{n,k}\}$ for all $S_n$) and Bóna–Lackner–Sagan's involution analog remain open; this paper proposes Schur-positive lifts as a possible route.
- Conjecture 3.7 (perfect-matchings / even-column-length $\Theta$ case) verified for $n\le 30$ but unproven; Conjecture 3.8 admits no analogous Schur-positive lift (counterexample at $n=10$).
- Connects to Lam–Postnikov–Pylyavskyy's broader Schur-log-concavity machinery and Okounkov's character log-concavity for $U(\infty)$.

## Key terms
Schur positivity, log-concavity, longest increasing subsequence, Robinson-Schensted correspondence, hook-length formula, standard Young tableau, Schur function, rectangular partition, Lam-Postnikov-Pylyavskyy, Okounkov conjecture, symmetric group, involutions, digamma function
