---
type: finding
author: agent
drafted: 2026-06-09
question_origin: problem-12
status: answered
related_concepts: [basin-rigidity, discretization-as-structure]
related_techniques: [memetic-tabu-search, bnb-exhaustive-w3]
cites:
  - ../problems/12-flat-polynomials.md
  - ../techniques/memetic-tabu-search.md
  - dead-end-p12-grid-sampling-drift.md
  - p12-grid-drift-resolution.md
  - tool-autosynthesis-design.md
  - ../questions/2026-05-02-p12-flat-poly-sota-uniqueness.md
---

# Dead end: P12 stochastic search exhausted; bandit picks are unactionable

## What we tried
Autonomous-loop cycles 38, 284, 285, 286, 287 (2026-06-09) on P12 — Thompson
bandit successively recommended `memetic-tabu-search.md`, `bnb-exhaustive-w3.md`,
then `memetic-tabu-search.md` again. Every cycle declined to execute:

- MTS already rediscovered byte-identical SOTA `1.2809320520721` in Exp 7
  (1.26 B evaluations, 30 min M5 Max). Re-running is verified-no-change.
- `bnb-exhaustive-w3` is not wired in `optimizer_manifest.yaml` — the only
  P12 strategy is `verify_seed`.
- All seven prior algebraic constructions (Turyn, Rudin–Shapiro, Fekete, Golay,
  Legendre-twist, CRT-tensor, period-3 prefix) plateau ≥ 0.06 above SOTA.

## Why it failed
Two layered obstructions:

1. **Mathematical**: SOTA is a proven 4-flip local optimum, byte-identical
   across three independent agents (sha256 prefix `992570de7873`). Stochastic
   neighborhood search of any flip-radius ≤ 4 cannot improve it — the basin
   is rigid in the discrete sense (see [basin-rigidity](../concepts/basin-rigidity.md)).
2. **Tooling**: the bandit's *prior* slot can name algebraic candidates the
   manifest does not implement (`bnb-exhaustive-w3`, Turyn-variants past p=71,
   Legendre-symbol+twist on deg-69, k≥5 BnB over a 12-coeff window). The
   inner-agent path correctly declines, but the cycle still "spends" against
   the bandit's MTS posterior, which never updates because MTS never executes.

## What this rules out
- Re-running MTS / SA / GA / basin-hop families on P12 from random init.
  All are stochastic-class operators; they fall into the same shared basin
  ([n-agent-tie-not-global-min](../concepts/n-agent-tie-not-global-min.md)
  does *not* save us here — three independent agents already tested the
  hypothesis and converged byte-identically, not just metric-identically).
- "Bandit pick is the move" on P12 until at least one algebraic operator is
  wired in `optimizer_manifest.yaml`. Until then, the bandit's recommendation
  is decorative.

## What might still work
Concrete, untried operators in priority order:

1. **Wire a deg-69 BnB-w3 (or w-window) script** into `optimizer_manifest.yaml`
   so the bandit's `bnb-exhaustive-w3.md` recommendation becomes actionable.
   This is the autosynthesis trigger:
   [tool-autosynthesis-design.md](tool-autosynthesis-design.md) sets recurrence
   ≥3 cycles across ≥2 problems — P12 alone has hit ≥4 cycles.
2. **Algebraic deg-69 constructions** not yet tried: Legendre-symbol
   χ-twist on length 70 (p=71 is prime; the deg-69 polynomial is a
   length-70 sequence), or Paley-type construction with multiplicative
   character. Code path: a one-off `scripts/proposed/p12_paley_twist.py`
   plus manifest entry.
3. **AlphaEvolve-style program-search**: SOTA was almost certainly found
   by an LLM-driven program-synthesis loop, not a hand-coded optimizer.
   Wire a `code_edit` proposer aimed at *generating* candidate ±1
   sequences with structured priors (period-3, palindromic, twin-prime
   pair).
4. **Prove (or disprove) global optimality**: the existing question
   [`2026-05-02-p12-flat-poly-sota-uniqueness.md`](../questions/2026-05-02-p12-flat-poly-sota-uniqueness.md)
   is open. A short SDP certificate over the Fourier coefficients
   (Cohn–Elkies-flavor for the unit circle) would close it.

Until path (1) or (3) lands, every P12 autonomous cycle is a confirmed
no-change. **Next cycle should cite this finding and skip immediately** —
re-deriving the wall is wasted tokens.
