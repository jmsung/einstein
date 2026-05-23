---
type: source
kind: paper
title: On the permanent of a random symmetric matrix
authors: Matthew Kwan, Lisa Sauermann
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2010.08922
source_local: ../raw/2020-kwan-permanent-random-symmetric-matrix.pdf
topic: general-knowledge
cites:
---

# On the permanent of a random symmetric matrix

**Authors:** Matthew Kwan, Lisa Sauermann  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2010.08922

## One-line
Resolves Vu's conjecture: the permanent of a random symmetric $\pm 1$ matrix has magnitude $n^{n/2+o(n)}$ with high probability.

## Key claim
For $M_n$ a random symmetric $n\times n$ matrix with i.i.d. Rademacher entries on/above the diagonal, asymptotically almost surely $|\operatorname{per} M_n| = n^{n/2+o(n)}$. Quantitatively: $\Pr(|\operatorname{per} M_n| \le n^{n/2-\varepsilon n}) \le n^{-c}$ for some $c>0$ (e.g. $c=1/150$).

## Method
Upper bound: second-moment computation $\mathbb{E}[(\operatorname{per} M_n)^2] \le n^{n+o(n)}$ + Markov. Lower bound: an inductive "heavy submatrix growth" scheme extending Tao–Vu's row-exposure argument to the symmetric case, where adding a row/column at each step makes permanents of submatrices *quadratic* (not linear) polynomials in the new entries. Anti-concentration is controlled via Erdős–Littlewood–Offord, Meka–Nguyen–Vu polynomial anti-concentration (graph matching number $\nu(G^{(r)}(f))$), Azuma–Hoeffding, and a vertex-cover dichotomy (easy / short / interesting indices).

## Result
Combines Proposition 1.2 ($\Pr(|\operatorname{per} M_n| \ge n^{n/2+\varepsilon n}) \le n^{-\varepsilon n}$) with Theorem 1.3 (matching lower bound w.h.p.). In particular $\Pr(\operatorname{per} M_n = 0) \le n^{-c}$, the first nontrivial bound on symmetric-permanent singularity. Generalizes to GOE / arbitrary off-diagonal $\mu$ with support $\ge 2$ points; the same $n^{n/2+o(n)}$ magnitude holds.

## Why it matters here
General background; no direct arena tie. Adjacent to combinatorial anti-concentration tooling (Erdős–Littlewood–Offord, Meka–Nguyen–Vu) that *could* be relevant for autocorrelation / Sidon-style discrete problems, but the symmetric-permanent result itself is not a known lever for any of the 23 Einstein Arena problems.

## Open questions / connections
- Sharper concentration: can $\Pr(\operatorname{per} M_n = a) \le n^{-\omega(1)}$, or even $n^{-cn}$? Vu conjectures $\Pr(\operatorname{per} A_n = 0) = \omega(1)^{-n}$ (unlike $\det$, which is $2^{-n+o(n)}$).
- Central limit theorem for $\log|\operatorname{per} M_n|$, paralleling Nguyen–Vu (det $A_n$) and Bourgade–Mody (det $M_n$).
- Quantum-computing tie: Aaronson–Arkhipov boson-sampling rests on a *stronger* permanent anti-concentration conjecture not resolved here.

## Key terms
random symmetric matrix, permanent, Rademacher entries, Erdős–Littlewood–Offord inequality, Meka–Nguyen–Vu anti-concentration, Tao–Vu, GOE, singularity probability, Azuma–Hoeffding, quadratic polynomial anti-concentration, graph matching number, boson sampling
