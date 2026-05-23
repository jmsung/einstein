---
type: source
kind: paper
title: The Erdős–Selfridge problem with square-free
moduli
authors: P. Balister, B. Bollob'as, R. Morris, J. Sahasrabudhe, M. Tiba
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1901.11465
source_local: ../raw/2019-balister-erd-selfridge-problem-square-free.pdf
topic: general-knowledge
cites:
---

# The Erdős–Selfridge problem with square-free moduli

**Authors:** P. Balister, B. Bollobás, R. Morris, J. Sahasrabudhe, M. Tiba  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1901.11465

## One-line
Proves that any covering system of $\mathbb{Z}$ by arithmetic progressions with distinct square-free moduli must contain at least one even modulus, resolving the square-free case of the Erdős–Selfridge problem.

## Key claim
**Theorem 1.1:** In any finite collection of arithmetic progressions with *distinct square-free* moduli that covers $\mathbb{Z}$, at least one modulus is even. (Stronger form: the square-free assumption is only needed on the 73-smooth part of the moduli.)

## Method
Geometric reformulation via CRT: covering systems with square-free, odd, $p_{n+1}$-smooth moduli correspond to coverings of the box $Q = [p_2] \times \cdots \times [p_{n+1}]$ by non-parallel hyperplanes. The proof extends the Hough/Balister-Bollobás-Morris-Sahasrabudhe-Tiba distortion-sieve: a probability measure $P_k$ is built dimension-by-dimension on the uncovered set, with damping constants $\delta_k \in [0, 1/2]$ chosen so $P_k(B_k)$ stays small. Moments $M_k^{(1)}, M_k^{(2)}$ of the per-fibre removal fraction $\alpha_k(x)$ are controlled by the generating function $c_k(x) = \sum_{I,J} c(I)\nu(J) x^{|I|+|J|}$; a new geometric bound (Theorem 3.2 eq. 13) sharpens $M_k^{(2)}$ when codim-1 hyperplanes are stripped first. Primes are split into three groups — $\{3,5,7,11\}$ (LP-optimized via Gurobi over ~7637 reduced configurations), $\{13,\ldots,73\}$ (coordinate-wise $\delta_k$ optimization), $p > 73$ (asymptotic termination criterion $f_{21} \leq 138.877$).

## Result
The covering threshold reduces to verifying $c_5(3) - 3c_5(1)/4 \leq 9.019$ over all hyperplane configurations on $Q_5 = [2]\times[4]\times[6]\times[10]$ (sizes after codim-1 removal); LP over the colex-reduced 7637 configurations (plus 2 worst-case explicit configurations in Table 1) gives $\leq 9.018071$. Side result (Theorem 1.4): if $\liminf q_k/k > 3$, then any covering of $[q_1]\times\cdots\times[q_n]$ by non-parallel hyperplanes uses some $F(A) \subseteq [C]$; Proposition 4.1 shows the constant 3 cannot be replaced by 1 (essentially sharp).

## Why it matters here
General background; no direct arena tie. The distortion-sieve / probabilistic-measure-on-uncovered-set technique is structurally similar to LP-bound methods (Cohn–Elkies, Delsarte) the agent uses for sphere packing and kissing-number problems — same flavor of "build a measure that certifies non-coverage / non-packing", with weights chosen by LP optimization. Useful as a paradigm: when direct combinatorial bounds fail, build a damped probability measure and bound its moments.

## Open questions / connections
- Can the prime threshold $p \leq 73$ in the square-free condition be lowered? Reducing it below 3 would solve the full Erdős–Selfridge problem (existence of all-odd covering systems).
- Extends Hough (2015) minimum-modulus result and Hough–Nielsen (divisibility by 2 or 3); leaves open the non-square-free Erdős–Selfridge (1965) and Erdős's 1977 conjecture that covering systems exist with all prime factors arbitrarily large.
- Schinzel's connection: non-existence of odd-modulus covering systems implies irreducibility of $x^n + f(x)$ for infinite arithmetic progressions of $n$ — square-free case now resolved.

## Key terms
covering systems, Erdős–Selfridge problem, square-free moduli, distortion sieve, hyperplane covering, Chinese Remainder Theorem, minimum modulus problem, Hough sieve, LP optimization, Schinzel irreducibility, parallel hyperplanes, probabilistic method, Balister-Bollobás-Morris-Sahasrabudhe-Tiba, smooth numbers
