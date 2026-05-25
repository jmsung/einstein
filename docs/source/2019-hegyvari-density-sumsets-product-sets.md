---
type: source
kind: paper
title: On the density of sumsets and product sets
authors: Norbert Hegyv'ari, F. Hennecart, P'eter P'al Pach
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1902.02512
source_local: ../raw/2019-hegyvari-density-sumsets-product-sets.pdf
topic: general-knowledge
cites:
---

# On the density of sumsets and product sets

**Authors:** Norbert Hegyv'ari, F. Hennecart, P'eter P'al Pach  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1902.02512

## One-line
Investigates how the asymptotic density of an integer set $A$ constrains the densities of its sumset $A+A$, its set of subset sums $P(A)$, and its product set $A\cdot A$.

## Key claim
Three headline results: (i) for every $0\le\alpha\le 1$ there is a normalized $A$ with $\underline{d}A=\alpha$ and $d(A+A)=1$; (ii) if $|a_n-s_{n-1}|=\theta(s_{n-1})$ with $\theta(k)\ll(\log k/k)^2$ where $s_n=\sum_{i\le n}a_i$, then the density $d(P(A))$ exists (partial answer to Ruzsa); (iii) for every $0\le\alpha\le\beta\le 1$ there is $A$ with $dA=0$, $\underline{d}(A\cdot A)=\alpha$, $\overline{d}(A\cdot A)=\beta$ (Theorem 4.4).

## Method
Direct constructive arguments: thin additive bases unioned with arithmetic-progression skeletons for sumset realizations; an interval-decomposition / telescoping estimate $\delta_n-\delta_{n-1}=O(\theta(s_n)/s_n)$ combined with the lower bound $s_n\gg 2^n$ to force convergence of subset-sum density; inclusion-exclusion / sieve over mutually coprime divisors using $\sum 1/a_i=\infty$ and $1-u\le e^{-u}$ for the product-set density-1 result; recursive set-trimming alternating between odd/even stages to hit prescribed $\underline{d}, \overline{d}$ targets; Erdős-Kac / Hardy-Ramanujan normal order of $\Omega(n)$ plus Hildebrand's friable-integer estimate $\Psi(x,z)$ for the $dA=0$, $d(A^2)=1$ example.

## Result
Proposition 2.1: $\underline{d}A=\alpha$, $d(A+A)=1$ achievable for any $\alpha$. Proposition 2.2: $dA$ may exist while $d(A+A)$ does not (example with density $3/7$, sumset oscillating between $6/7$ and $1$). Proposition 3.1: subset-sum density exists under the $\theta\ll(\log k/k)^2$ growth condition. Propositions 4.1-4.3 + Theorem 4.4: full realization of $(0,\alpha,\beta)$ triples for $(dA,\underline{d}(A^2),\overline{d}(A^2))$; explicit $A=\{n:\Omega(n)\le 0.75\log\log n+1\}$ has $dA=0$ but $d(A^2)=1$. Conditional density-1 propagation: $dA=1$ plus an infinite mutually-coprime subset with divergent reciprocal sum forces $d(A^2)=1$.

## Why it matters here
General background; no direct arena tie — additive/multiplicative density results don't map onto the Einstein Arena's sphere-packing, kissing-number, autocorrelation, or extremal-geometry problems. Possible distant relevance to Sidon-set / $B_2$-set extremal questions where sumset density obstructions appear, but the paper itself is pure asymptotic-density combinatorics.

## Open questions / connections
- Ruzsa's open inequality $\overline{d}(A+A)\ge c\cdot(\underline{d}(A+A))^{1-\nu}(dA)^\nu$ with $\nu\ge 1/2$ — still unsettled.
- Does $dA=1$ alone (without the coprime-divergent-reciprocal hypothesis) imply $d(A^2)=1$? Posed as an explicit question.
- Extends/answers Zannier's conjecture (proved by Ruzsa for $a_n\le 2a_{n-1}$) and Ruzsa's follow-up about $a_n\le s_{n-1}+c$ ensuring $d(P(A))$ exists.
- Characterize multiplicatively stable sets ($A^2=A$) with $0<dA<1$ beyond the $\{n:\gcd(n,k)=1\}\cup k\ell\mathbb{N}$ family.

## Key terms
asymptotic density, sumset, product set, subset sums, Kneser's theorem, Freiman's theorem, Ruzsa, Erdős, Hardy-Ramanujan, Erdős-Kac, Hildebrand friable integers, $\Omega(n)$ normal order, mutually coprime, sieve inclusion-exclusion, additive basis, multiplicatively stable sets
