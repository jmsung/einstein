---
type: source
kind: paper
title: Some remarks on the lonely runner conjecture
authors: T. Tao
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1701.02048
source_local: ../raw/2017-tao-some-remarks-lonely-runner.pdf
topic: general-knowledge
cites:
---

# Some remarks on the lonely runner conjecture

**Authors:** T. Tao  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1701.02048

## One-line
Tao slightly improves the trivial $\frac{1}{2n}$ lower bound for the lonely runner conjecture's "gap of loneliness" $\delta_n$ using rank-3 Bohr-set estimates plus sieve theory, and reduces the conjecture to a finite check over integer speeds of size $n^{O(n^2)}$.

## Key claim
Three results: (1) $\delta_n \geq \frac{1}{2n} + \frac{c \log n}{n^2 (\log \log n)^2}$ for large $n$ and some absolute $c>0$ (previously the additive gain was $O(1/n^2)$); (2) the conjecture for all $n \leq n_0$ is equivalent to checking it only for tuples $(v_1,\dots,v_n)$ with $|v_i| \leq n^{C_0 n^2}$, making it algorithmically decidable; (3) if all $v_i \leq 1.2n$, then $\delta(v_1,\dots,v_n) \geq \frac{1}{n+1}$ unconditionally.

## Method
Reformulates the conjecture as covering $\mathbb{R}/\mathbb{Z}$ by rank-1 Bohr sets $B(v_i;\delta_n)$. Pushes beyond the union-bound / rank-2 second-moment arguments of prior work by invoking a Hölder/Cauchy–Schwarz third-moment estimate that forces many rank-3 Bohr sets $B(v_i,v_j,v_k;\delta_n,\delta_n,\delta_n)$ to be large. Fourier analysis + generalised arithmetic progressions (Freiman-style) then localise most velocities inside a short progression; standard sieve bounds on medium-sized prime factors ($\log^{10} n \leq p \leq n^{1/10}$) carve out disjoint "major arc" overlaps that beat the union bound. Theorem 1.3 uses Freiman homomorphisms into proper GAPs plus a Fourier comparison identity to transfer a forced collision $v'_i = v'_j$ back to the original tuple.

## Result
- $\delta_n \geq \frac{1}{2n} + \frac{c \log n}{n^2 (\log \log n)^2}$ — the first improvement gaining a logarithmic factor in the numerator.
- Decidability: deciding the conjecture for $n \leq n_0$ takes time $O(n_0^{O(n_0^2)})$ via brute-force check over $|v_i| \leq n_0^{C_0 n_0^2}$.
- Proposition 1.5: speeds bounded by $1.2n$ ⇒ conjecture holds; Proposition 1.6: speeds bounded by $Cn$ ⇒ $\delta \geq \frac{1+c}{2n}$ with $c=c(C)>0$.

## Why it matters here
Direct background for autocorrelation / Sidon / covering-by-Bohr-sets problems in the arena — the same union-bound-with-Fourier-correction template recurs in extremal-set and packing-density arguments. The "sunflower of primes" example (rank-1 Bohr sets indexed by primes in $[n/4, n/2]$ achieve $1+O(1/n)$ union-bound tightness) is a transferable construction-vs-bound gap diagnostic. The Freiman-into-GAP + Fourier-transfer trick (Section 4) is reusable wherever the agent needs to reduce a continuous optimisation over integer tuples to a bounded finite search.

## Open questions / connections
- Can the $\log \log n$ factors in the denominator be removed? Tao notes one likely can; improving the $\log n$ in the numerator looks like it needs new ideas.
- Closing the gap between $1.2n$ (Prop 1.5) and $n^{C_0 n^2}$ (Thm 1.3) — natural target $2n$, since multiple extremiser families exist there (Goddyn–Wong tuples).
- Extends Chen (1994), Chen–Cusick (1999), Perarnau–Serra (2016) rank-2 Bohr-set methods to rank 3; further extension to rank $r$?
- Connects view-obstruction (Cusick), Diophantine approximation (Wills), distance-graph chromatic numbers, and regular-matroid flows (Bienia et al).

## Key terms
lonely runner conjecture, Bohr sets, gap of loneliness, view obstruction, Diophantine approximation, generalised arithmetic progressions, Freiman homomorphism, union bound, Hölder inequality, sieve theory, medium-sized primes, Farey sequence, rank-3 Bohr set, Cusick, Wills, Tao, Chen, Perarnau-Serra, sunflower lemma, multiplicity function, Dirichlet approximation
