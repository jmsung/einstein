---
type: question
author: agent
drafted: 2026-06-28
asked_by: agent
status: answered
answer_finding: ../findings/p7-n16000-degeneracy-crossover-off.md
related_problems: [P7]
related_concepts: [sieve-theory-as-lp.md, lp-cutting-plane-warmstart.md]
---

> **Answered (2026-06-28):** the LP is tractable — the wall was a *degenerate optimal
> face* (Mertens identity binds ~2600 constraints), and HiGHS default crossover stalls
> on it. Fix: `solver=ipm`, `run_crossover=off` → solves in ~320s. See
> [p7-n16000-degeneracy-crossover-off](../findings/p7-n16000-degeneracy-crossover-off.md).

# How do the leaders solve the P7 base LP at N=16000 fast, when our cutting-plane stack walls?

## The unknown
The P7 leaders (MAOJIASONG, CHRONOS, 2026-06-27) reach maxkey=16000 with a base LP
score 0.99622 — a +1.4e-3 gain over our frozen N=3349 (0.99485). Our primal
cutting-plane + `scipy.linprog(method="highs")` solves N≤3350 in minutes but does not
return a single round at N=16000 within a 580s wall (see experiment-log Exp 10,
wall-ledger 2026-06-28). What formulation makes the N=16000 LP tractable?

## Data / constraints
- Variables: f(k), k squarefree in [2, N], bounds [-10,10], cardinality cap ≤2000.
- Objective: minimize Σ f(k)·log(k)/k (= maximize the arena score).
- Constraint: Σ f(k)(⌊x/k⌋ − x/k) ≤ 1 for all integer x ≥ 1 (sup attained at finite x
  after the Σf(k)/k=0 normalization kills the linear term).
- Our violation check sweeps x∈[1, 10·maxkey]=160000; each cutting-plane round
  re-solves from scratch (scipy gives no cross-round basis warm-start).

## Falsifiable answer shape
A concrete recipe that returns a feasible base score ≥0.99622 at maxkey=16000 in
< ~10 min on the a local workstation. Candidate operators to test (the untried moves):
1. **Dual / column-generation** (`scripts/prime/colgen_prime.py`): solve the dual or
   generate keys by reduced cost; the dual constraint count may be far smaller.
2. ~~**Bounded violation range**~~ — **RULED OUT** (measured 2026-06-28): the worst-case
   x for the leaders' feasible solutions sits at x≈8·maxkey (119813 / 148874), and
   near-binding x span the full [1, 157397]. Truncating the sweep misses binding
   constraints. The full 10·maxkey range is required.
3. **`highspy` directly** with warm-started basis carried across cutting-plane rounds.

## Why it matters
This is the gate on the real N-extension beat. Without it, P7 reclaim is limited to
the saturated tolerance-edge rescale (Exp 8/10), which beats #1 by only ~1e-6 and adds
no math wisdom. Answering this re-opens the genuine basin advance the leaders found.

## Suggested next step
Re-dispatch the council (Cohn/Tao/Razborov on the sieve-LP dual structure) seeded with
the two failed attempts, OR test operator (2) cheaply first (measure where the worst x
lives for a known feasible solution). Human compute-budget decision pending.
