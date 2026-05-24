---
type: source
kind: paper
title: Infinite computable version of Lovasz Local Lemma
authors: Andrey Rumyantsev
year: 2010
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1012.0557v1
source_local: ../raw/2010-rumyantsev-infinite-computable-version-lovasz.pdf
topic: general-knowledge
cites:
---

# Infinite computable version of Lovasz Local Lemma

**Authors:** Andrey Rumyantsev  ·  **Year:** 2010  ·  **Source:** http://arxiv.org/abs/1012.0557v1

## One-line
Extends the Moser–Tardos constructive proof of the Lovász Local Lemma to infinite systems of constraints, yielding a *computable* satisfying assignment under a slightly strengthened LLL condition.

## Key claim
If a countable family of forbidden events $\mathcal{A}$ over computable independent variables $P_0, P_1, \ldots$ admits a computable $x: \mathcal{A} \to (0,1)$ and constant $\varepsilon \in (0,1)$ with $\Pr[A] \le (1-\varepsilon)\, x(A) \prod_{E \in \Gamma(A)} (1 - x(E))$, then a *computable* assignment avoiding all $A \in \mathcal{A}$ exists (Theorem 2).

## Method
Modify Moser–Tardos resampling for an infinite event set by ordering events via the maximum variable index they touch, so the algorithm reduces to the finite Moser–Tardos run on each prefix $P_0,\ldots,P_n$. Tree-witness arguments give predictable convergence — each variable stabilizes a.s. with computable confidence bounds (Lemma 3). A computable output distribution concentrated on satisfying assignments then yields a computable element via a sequential positive-measure selection (Lemma 4).

## Result
Theorem 2 (computable infinite LLL); Theorem 3: every effective infinite CNF with $m$-variable clauses and at most $2^{m-2}$ neighbors per clause has a computable satisfying assignment; Theorem 4: for any $\alpha \in (0,1)$ some $N$ exists such that any effective infinite CNF where each variable lies in $\le 2^{\alpha n}$ clauses of size $n$ and all clauses have size $\ge N$ has a computable satisfying assignment. Corollary: for decidable $F \subset \{0,1\}^*$ with $|F \cap \{0,1\}^n| \le 2^{\alpha n}$, a computable infinite (or bi-infinite, or 2D) sequence avoiding all long $F$-substrings exists.

## Why it matters here
General background for constructive existence proofs: shows that LLL-style probabilistic existence (probability 0 events!) can be upgraded to algorithmic / computable constructions — relevant when an arena problem requires producing an explicit witness, not just proving one exists. No direct tie to current arena problems (sphere packing, autocorrelation, kissing); useful if a future problem reduces to satisfying a large sparse constraint family.

## Open questions / connections
- Extends Moser–Tardos (2010) [arxiv:0903.0544] from finite to countable; can the $1-\varepsilon$ slack be removed?
- 2D analogue (computable $\mathbb{Z}^2 \to \{0,1\}$ avoiding forbidden patterns) noted as not derivable without Moser–Tardos — what other lattice/geometric constructions does this unlock?
- Connection to Kolmogorov-complexity proofs of forbidden-substring avoidance (Rumyantsev STACS 2006, Miller subshifts) — when is the LLL route strictly stronger?

## Key terms
Lovász Local Lemma, Moser–Tardos algorithm, constructive proof, computable assignment, resampling, infinite CNF satisfiability, forbidden substrings, subshifts, Kolmogorov complexity, compactness argument, probabilistic method, effective combinatorics
