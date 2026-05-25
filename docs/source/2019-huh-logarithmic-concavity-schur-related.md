---
type: source
kind: paper
title: Logarithmic concavity of Schur and related polynomials
authors: June Huh, Jacob P. Matherne, Karola M'esz'aros, Avery St. Dizier
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1906.09633
source_local: ../raw/2019-huh-logarithmic-concavity-schur-related.pdf
topic: general-knowledge
cites:
---

# Logarithmic concavity of Schur and related polynomials

**Authors:** June Huh, Jacob P. Matherne, Karola M'esz'aros, Avery St. Dizier  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1906.09633

## One-line
Proves that normalized Schur polynomials are Lorentzian, establishing strong log-concavity of Kostka numbers and a special case of Okounkov's log-concavity conjecture for Littlewood–Richardson coefficients.

## Key claim
For any partition $\lambda$, the normalized Schur polynomial $N(s_\lambda(x_1,\ldots,x_m)) = \sum_\mu K_{\lambda\mu} \frac{x^\mu}{\mu!}$ is Lorentzian. Consequently $K_{\lambda\mu}^2 \ge K_{\lambda\mu(i,j)} K_{\lambda\mu(j,i)}$ for all $i,j \in [m]$, where $\mu(i,j) = \mu + e_i - e_j$ (discrete log-concavity along root directions $e_i - e_j$).

## Method
Realize $N(s_\lambda)$ as a volume polynomial $\mathrm{vol}_{Y,H}$ of an irreducible projective variety $Y \subset (\mathbb{P}^\ell)^m$ (constructed as a degeneracy locus from generic global sections), with nef divisor classes $H_i = c_1(\pi_i^* \mathcal{O}(1))$. By Brändén–Huh's theorem that volume polynomials of irreducible varieties w.r.t. nef classes are Lorentzian, the result follows. The Schubert-polynomial generalization $\mathcal{S}_w^\vee$ uses Fulton's degeneracy-locus formula and matrix Schubert varieties.

## Result
Three main theorems: (1) continuous log-concavity of $N(s_\lambda)$ on $\mathbb{R}^m_{>0}$; (2) discrete log-concavity $K_{\lambda\mu}^2 \ge K_{\lambda\mu(i,j)} K_{\lambda\mu(j,i)}$; (3) $N(s_\lambda)$ is Lorentzian. Extends to Schubert polynomials ($\mathcal{S}_w^\vee$ Lorentzian for all $w \in S_n$), products of normalized Schur polynomials, and gives an Alexandrov–Fenchel-based proof for Verma module weight multiplicities. Counterexamples noted: $s_\lambda$ itself (unnormalized) need not be Lorentzian; $N(s_\lambda)$ need not be stable; analog fails for $\mathrm{sp}_4(\mathbb{C})$.

## Why it matters here
General background; no direct arena tie. Lorentzian/strongly-log-concave polynomial machinery (Brändén–Huh, Anari–Oveis Gharan–Vinzant) is a powerful general-purpose tool for log-concavity inequalities — potentially relevant to extremal combinatorics problems (P-class) if a generating-function reformulation surfaces, but not directly applied to current arena problems.

## Open questions / connections
- Conjecture 15: $N(\mathfrak{S}_w)$ Lorentzian for all $w \in S_n$ (verified for $n \le 8$); double Schubert and double Grothendieck analogs.
- Conjecture 19/20/23: normalized skew Schur, Schur P-polynomials, and key polynomials all conjecturally Lorentzian.
- Conjecture 10/12: extends discrete log-concavity to all $\mathfrak{sl}_m(\mathbb{C})$ weight multiplicities (not just dominant $\lambda$); fails for symplectic types.
- Okounkov's full LR-coefficient log-concavity conjecture remains open in general (and is refuted in some cases by Chindris–Derksen–Weyman 2007).

## Key terms
Schur polynomial, Kostka number, Lorentzian polynomial, strongly log-concave, M-convex set, generalized permutohedron, Littlewood–Richardson coefficient, Schubert polynomial, volume polynomial, Alexandrov–Fenchel inequality, Okounkov conjecture, Huh, Brändén, Verma module
