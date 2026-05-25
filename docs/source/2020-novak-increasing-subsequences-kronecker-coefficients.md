---
type: source
kind: paper
title: Increasing Subsequences and Kronecker Coefficients
authors: Jonathan Novak, B. Rhoades
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2006.13146
source_local: ../raw/2020-novak-increasing-subsequences-kronecker-coefficients.pdf
topic: general-knowledge
cites:
---

# Increasing Subsequences and Kronecker Coefficients

**Authors:** Jonathan Novak, B. Rhoades  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2006.13146

## One-line
Proposes a representation-theoretic strengthening of Chen's conjecture that the distribution of the longest increasing subsequence length $LIS_n$ in a random permutation is log-concave.

## Key claim
Conjecture 2: for $n \geq 3$ and $2 \leq k \leq n-1$, there exists an $S_n$-equivariant injection $V_{n,k-1} \otimes V_{n,k+1} \hookrightarrow V_{n,k} \otimes V_{n,k}$, where $V_{n,k} = \bigoplus_{\lambda \vdash n,\ \ell(\lambda)=k} f^\lambda V^\lambda$. This implies Chen's log-concavity $a_{n,k-1} a_{n,k+1} \leq a_{n,k}^2$ for $a_{n,k} = \#\{\pi \in S_n : LIS(\pi) = k\}$.

## Method
Lift the numerical log-concavity inequality to a Schur-positivity / module-injection statement using Robinson-Schensted, the Frobenius isomorphism $R(S_n) \to \Lambda_n$, and Kronecker coefficients $g^\nu_{\lambda\mu}$. The strategy is illustrated by the simpler case of binomial coefficient log-concavity, where the required module is realized as a bigraded piece of the fermionic diagonal coinvariant ring $FDR_n = \wedge\{\Theta_n, \Xi_n\}/\langle \wedge\{\Theta_n,\Xi_n\}^{S_n}_+\rangle$ (Kim-Rhoades).

## Result
Equivalent reformulations: (Conj. 3) a Kronecker-coefficient/hook-length inequality $\sum_{\ell(\lambda)=k-1, \ell(\mu)=k+1} g^\nu_{\lambda\mu}/(H_\lambda H_\mu) \leq \sum_{\ell(\lambda)=\ell(\mu)=k} g^\nu_{\lambda\mu}/(H_\lambda H_\mu)$ for every $\nu \vdash n$; (Conj. 4) Schur-positivity $S_{n,k-1} * S_{n,k+1} \leq S_{n,k} * S_{n,k}$ where $S_{n,k} = \sum_{\ell(\lambda)=k} f^\lambda s_\lambda$. Conjecture 4 verified by computer for $n \leq 15$. As warm-up, the binomial log-concavity $\binom{n-1}{k}^2 \geq \binom{n-1}{k-1}\binom{n-1}{k+1}$ is recovered from $Frob(V_{n,k}) = s_{(n-k,1^k)} * s_{(k+1,1^{n-k-1})} - s_{(n-k+1,1^{k-1})} * s_{(k+2,1^{n-k-2})}$.

## Why it matters here
General background; no direct arena tie — none of the 23 Einstein Arena problems currently centers on $LIS_n$ log-concavity or Kronecker coefficients. Tangential value: demonstrates the "strengthen-to-prove" tactic (lift a numerical inequality to a Schur-positivity or module-injection statement), a methodological pattern occasionally useful in extremal combinatorics work.

## Open questions / connections
- Construct an explicit $S_n$-equivariant injection $V_{n,k-1} \otimes V_{n,k+1} \to V_{n,k} \otimes V_{n,k}$ (or prove Schur-positivity of Conj. 4) for all $n$.
- Extends Bóna-Lackner-Sagan partial log-concavity results and Chen's 2008 conjecture; builds on Kim-Rhoades fermionic diagonal coinvariant theory (arXiv:2003.10031).
- Whether a Kim-Rhoades-style coinvariant module realizes the Frobenius image $S_{n,k}*S_{n,k} - S_{n,k-1}*S_{n,k+1}$ as a graded piece is the natural next target.

## Key terms
longest increasing subsequence, log-concavity, Kronecker coefficients, Schur positivity, Robinson-Schensted, hook-length formula, Young tableaux, symmetric group representations, Frobenius isomorphism, fermionic diagonal coinvariants, Chen conjecture, Erdős-Szekeres
