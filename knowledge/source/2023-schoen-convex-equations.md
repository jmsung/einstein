---
type: source
kind: paper
title: On convex equations
authors: Tomasz Schoen
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2310.09584v1
source_local: ../raw/2023-schoen-convex-equations.pdf
topic: general-knowledge
cites: 
---

# On convex equations

**Authors:** Tomasz Schoen  ·  **Year:** 2023  ·  **Source:** http://arxiv.org/abs/2310.09584v1

## One-line
Improves the upper bound on subsets of $\{1,\dots,N\}$ avoiding solutions to $x+y+z=3w$, narrowing the gap to Behrend's lower bound via a refined $L^\infty$ almost-periodicity lemma for convolutions.

## Key claim
If $A \subseteq \{1,\dots,N\}$ contains no nontrivial solution to $x+y+z=3w$, then $|A| \leq \exp(-c(\log N)^{1/5} e^{-C\log\log(1/N)}) N$ — improving the prior $1/7$ exponent (Schoen–Shkredov 2014) and $1/(6+\gamma_m)$ (Kościuszko 2023) for 4-variable invariant equations.

## Method
Density-increment along regular Bohr sets, replacing the standard $L^\infty$-almost-periodicity of three-fold convolutions (Theorem 7) with a new variant (Theorem 9) that gives a dichotomy: either a substantial density increment on a Bohr set whose rank grows by $\log^{4+o(1)}(1/\alpha)$, or a modest increment on a Bohr set whose rank grows by only $\log^{1+o(1)}(1/\alpha)$. The new lemma probabilistically replaces $1_M * \mu_B$ by a much larger random set $R$ using Bernstein's inequality, then reapplies Theorem 7 to $R$ for sharper bounds on radius shrinkage.

## Result
Theorem 4 gives $|A| \leq \exp(-c(\log N)^{1/5} e^{-C\log\log(1/N)}) N$ for $A$ avoiding $x+y+z=3w$. Behrend's lower bound is $\exp(-C(\log N)^{1/2}) N$. Conditional on a conjectured improvement of Bogolyubov's lemma (replacing $C\log^4(2/\alpha)$ with $C\log(2/\alpha)$ in Sanders' rank bound), the method would yield $\exp(-c(\log N)^{1/2-o(1)}) N$, essentially matching Behrend.

## Why it matters here
General background for additive combinatorics; no direct Einstein Arena tie — but informs sieve-theory and extremal-combinatorics problems where Bohr-set / density-increment machinery and almost-periodicity of convolutions arise. The dichotomy structure (big-increment-big-rank vs small-increment-small-rank) is a transferable proof template worth noting alongside Kelley–Meka and Bloom–Sisask.

## Open questions / connections
- Can Theorem 9 be applied inside the Kelley–Meka proof of 3-APs? Author notes obstruction: Kelley–Meka uses Theorem 7 on low-density intersection sets $X = \bigcap_i (A+s_i)$, where the gain from Theorem 9 is marginal.
- Conjecture: in Bogolyubov-type results, $2A-2A$ contains a Bohr set of rank $C\log(1/\alpha)$ (currently $C\log^4(2/\alpha)$ via Sanders) — would close gap to Behrend $1/2$ exponent.
- Extends Schoen–Sisask 2016 (4-variable invariant equations, exponent $1/7$) and Kościuszko 2023 (exponent $1/(6+\gamma_m)$); leaves the 3-variable case (Roth / Kelley–Meka at $1/9$) as the still-harder frontier.

## Key terms
convex equations, invariant linear equations, density increment, Bohr sets, almost-periodicity, convolution, Behrend bound, Kelley-Meka, Roth theorem, Bogolyubov lemma, Bernstein inequality, Schoen, Sanders, additive combinatorics
