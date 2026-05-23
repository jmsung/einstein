---
type: source
kind: paper
title: Variants of the Selberg sieve, and bounded intervals containing many primes
authors: D. Polymath
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1407.4897
source_local: ../raw/2014-polymath-variants-selberg-sieve-bounded.pdf
topic: general-knowledge
cites:
---

# Variants of the Selberg sieve, and bounded intervals containing many primes

**Authors:** D. Polymath  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1407.4897

## One-line
Polymath8b extends Maynard's multidimensional Selberg sieve and pushes the unconditional bound on prime gaps to $H_1 \le 246$, with $H_1 \le 6$ under the generalized Elliott-Halberstam conjecture.

## Key claim
Unconditionally $H_1 := \liminf_n (p_{n+1}-p_n) \le 246$; assuming GEH$[\vartheta]$ for all $\vartheta<1$, $H_1 \le 6$ — and this 6 is provably the best a purely sieve-theoretic argument can deliver (parity barrier). Also $H_m \ll m \exp((4-\tfrac{28}{157})m)$ unconditionally and $H_m \ll m e^{2m}$ under EH.

## Method
A generalized multidimensional Selberg sieve where the cutoff function $F:[0,\infty)^k\to\mathbb{R}$ is allowed support beyond the simplex $R_k = \{t : \sum t_i \le 1\}$ (under GEH, into larger regions whose sumset $R+R$ is still treatable). Reduces $H_m$ bounds to a multidimensional variational problem $M_k = \sup_F \frac{\sum_i \int F_i'^2}{\int F^2}$; the paper develops efficient numerics for small/medium $k$ and sharper asymptotics for large $k$. Narrow admissible $k$-tuples are constructed via shifted-Schinzel and shifted-greedy sieves with parallelized admissibility testing.

## Result
Unconditional: $H_1 \le 246$, $H_2 \le 398{,}130$, $H_3 \le 24{,}797{,}814$, $H_4 \le 1.43\times 10^9$, $H_5 \le 8.06\times 10^{10}$, and $H_m \ll m e^{(4-28/157)m}$. Under EH: $H_2 \le 270$, $H_3 \le 52{,}116$, $H_m \ll m e^{2m}$. Under GEH: $H_1 \le 6$, $H_2 \le 252$, plus a disjunction (Theorem 1.5): either the twin prime conjecture holds, or every large even $n$ lies within 2 of a sum of two primes. Tuple bounds include exact $H(50)=246$, $H(51)=252$, $H(54)=270$.

## Why it matters here
General background; no direct arena tie — this is sieve theory / prime-gap territory, useful as a methodological reference for sieve_theory problems if any arise, and as an exemplar of variational-problem-reduction (turning a number-theoretic bound into an optimization over cutoff functions $F$) and of dense-admissible-set construction (greedy/shifted sieving over residue classes).

## Open questions / connections
- Can GEH be relaxed back to EH while keeping $H_1 \le 6$? Parity barrier doesn't forbid it; needs new sieve refinement.
- Improving the MPZ$[\varpi,\delta]$ range (currently $600\varpi+180\delta<7$, conjectured to extend to $1080\varpi+330\delta<13$) via square-root cancellation in a 4-d exponential sum.
- Optimal placement of $F$-support beyond the simplex (free-boundary variational problem); non-Selberg sieves did not beat Selberg numerically — Selberg appears to be a local max in the non-negative-sieve space.
- Connects to / extends: Goldston-Pintz-Yıldırım (GPY), Zhang's $H_1\le 7\times 10^7$, Maynard's $H_1\le 600$, Bombieri-Vinogradov, Motohashi-Pintz-Zhang.

## Key terms
Selberg sieve, multidimensional sieve, Elliott-Halberstam conjecture, generalized Elliott-Halberstam, Bombieri-Vinogradov, prime gaps, admissible k-tuple, Hardy-Littlewood prime tuples, Maynard, Zhang, Goldston-Pintz-Yıldırım, parity problem, variational problem, narrow admissible tuple, shifted Schinzel sieve, Motohashi-Pintz-Zhang, sieve theory
