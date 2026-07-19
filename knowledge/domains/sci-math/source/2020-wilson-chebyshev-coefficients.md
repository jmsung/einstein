---
type: source
kind: paper
title: On coefficients satisfying Chebyshev's approximation of pi(x)
authors: Connor Paul Wilson
year: 2020
author: agent
drafted: 2026-07-04
ingested_at: 2026-07-04
source_type: arxiv
source_url: https://arxiv.org/abs/2012.14387
source_local: ../raw/arxiv-2012.14387.pdf
topic: P7-prime-number-theorem
distillation_depth: full (6/6 pages read)
cites: 
---

# On coefficients satisfying Chebyshev's approximation of π(x) (Wilson 2020)

**This is P7's mathematical frame, verbatim.** The paper studies finitely-supported
coefficient sets a(d) ≈ μ(d) subject to exactly our two conditions:

    Σ_d a(d)/d = 0        (our key-1 / zero-sum normalization)
    −Σ_d a(d)·log d / d ≈ 1   (our score S; the closer to 1, the tighter the π(x) bounds)

## Core mechanics (§1–2)

- Möbius inversion Λ(n) = Σ_{d|n} μ(d) log(n/d) → ψ(x) = Σ_{d≤x} μ(d) S(x/d) with
  S(x) = Σ_{n≤x} log n = x log x − x + O(log x). Replacing μ by finitely-supported a(d):
  Σ_{d∈D} a(d) S(x/d) = (x log x − x)·Σ a(d)/d − x·Σ a(d) log d/d + O(log x)  (eq 1.1)
  — the zero-sum kills the x log x term; the log-weighted sum becomes the linear coefficient.
- The error functional is E(t) = Σ_{d | n ≤ t} a(d) = −Σ_d a(d){t/d}, **periodic with
  period lcm(d ∈ D)** — the structure that makes G(x) checks finite in principle.
- Chebyshev D={1,2}: a=(1,−2) gives Σ a(d)log d/d = log 2 → (log 2)·x/log x < π(x) <
  (2 log 2)·x/log x. His 1850 D={1,2,3,5,30}, a=(1,−1,−1,−1,1): score log2/2 + log3/3 +
  log5/5 − log30/30 ≈ 0.9212 → the famous 0.9212 < π(x)·log x/x < 1.057. **The arena's
  AlphaEvolve baseline 0.92129 IS Chebyshev 1850.**

## Theorem 3.1 (the P7 statement)

Finding a(d) = {a_1..a_n} yielding α·x/log x < π(x) < β·x/log x via Chebyshev's method
⟺ finding the set with Σ 1/a_k = 0 and Σ log|a_k|/k ≈ 1 [notation loose in the paper —
the intended content is the two conditions above]. Notes that "research into finding
better sets of these coefficients is limited-to-none" — i.e., **the optimal-finite-set
question is explicitly under-studied** — but dismisses it as of "cursory interest"
because of Diamond–Erdős (below). **For P7 the dismissal does NOT apply: the 2000-key
cap makes the finite-set optimum the whole game.**

## Theorem 4.1, Diamond–Erdős (why unbounded support ⇒ score → 1)

Define the truncated Möbius μ_T(n) = μ(n) for n<T; at n=T set −T·Σ_{j<T} μ(j)/j (a
single compensating mass restoring the zero-sum); 0 beyond. Then as T→∞,
lim sup |π(x)/(x/log x) − 1| < ε — via Erdős's "hyperbolic method" splitting
Σ Λ∗m_T into ψ-terms and an M_T(x/i)Λ(i) middle term bounded O(x/K). Support size is
~T (all integers below T): **the construction is inherently DENSE. It says nothing
about sparse (cardinality-capped) supports — our c* question survives untouched.**

## Relevance to P7

1. Confirms the exact correspondence: P7 = "best finite Chebyshev coefficient set"
   with |D| ≤ 2000, |a| ≤ 10, plus the arena's finite-grid verifier.
2. The compensating-mass trick (μ_T's single balancing key at T) is a *construction
   pattern* worth testing in supports: a few heavy balancing keys instead of a smooth
   tail.
3. Confirms the literature gap: optimal sparse coefficient sets are unstudied ("limited
   to none"), consistent with c* being ownable.
