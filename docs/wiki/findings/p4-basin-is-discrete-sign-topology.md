---
type: finding
author: agent
drafted: 2026-06-06
question_origin: problem-4
status: answered
related_concepts: [equioscillation, autocorrelation-inequality, parameterization-selection, basin-rigidity]
related_problems: [2, 4]
related_personas: [tao, hilbert, cohn, hadamard]
cites:
  - ../problems/4-third-autocorrelation.md
  - ../findings/p4-fragmentation-not-fraction-shared-envelope.md
  - ../findings/dead-end-p4-negative-content-ceiling.md
  - ../concepts/equioscillation.md
  - src/einstein/third_autocorrelation/optimizer.py
  - scripts/third_autocorrelation/signed_dual_bound.py
---

# P4 basins are indexed by a discrete sign topology continuous descent cannot change

## Question
A collaborator confirms a P4 record exists: a piecewise-constant solution in a
DIFFERENT basin at C≈1.45220 (~1e-4 below the leader 1.4523043332). Ten+
optimisation variants (smooth-max polish, basin-hop, LP fixed-point, escapes,
neg-nudge, greedy-noise, fine cascade) all cap in our 23%-neg basin (~1.4525) or
return to the leader. Why, and what reaches the third basin?

## Answer — the math council converged (Tao, Hilbert, Hadamard, independently)
**The basin is selected by a discrete combinatorial parameter — the sign-change
count / placement (the "sign topology") of f.** Continuous descent (L-BFGS
smooth-max, LP fixed-point, basin-hop) cannot cross sign-change barriers:
inserting/removing a sign change is a discrete event with an energy wall, so
every gradient method is confined to the homotopy class of its starting sign
pattern. Our basin has 823 negative runs; the leader has 4705; the record is a
*third* sign topology none of our methods ever seeded. Every method we ran let
the optimiser *choose* the signs as an emergent output; **none imposed them as an
input.** That is the whole obstruction.

This sharpens the earlier findings: the gap is not negative *fraction* (saturated,
`dead-end-p4-negative-content-ceiling`) nor the low-Fourier *envelope* (shared,
`p4-fragmentation-not-fraction-shared-envelope`) — it is the **sign topology**
riding on that shared envelope.

## What we verified
- **`frozen_sign_descent` (f = s·v², signs frozen, optimise magnitudes):**
  imposing the leader's OWN sign pattern + |leader| magnitudes reconstructs and
  holds C=1.4523043332 exactly. The parameterisation is correct.
- **Periodic imposed sign patterns fail badly** (uniform square-wave, any
  run-count → C≈2.5, 50% neg): the good sign topologies are *aperiodic and
  co-adapted with the magnitudes*; frequency alone is not enough — placement
  matters. So "sweep the fragmentation frequency with a periodic ansatz" does
  not reach the basin.
- **The leader is a strong sign-topology optimum too**: a single discrete
  block-flip + magnitude re-polish jumps C to ~1.497 — the adjacent single-edit
  neighbourhood is all worse, so the 1.45220 basin is NOT one discrete edit away
  from the leader.
- **Cohn's signed dual SDP collapses to ~1.0** (`max λ s.t. y≥0, Σy=1,
  G(y)−λ11ᵀ⪰0`, bound C≥λ/dx → 1.026→1.013→1.008, decreasing). Same trivial-bound
  failure as Lasserre-L2 on P2 — confirms the literature has no usable signed
  lower bound, so feasibility of 1.45220 cannot be decided by duality.

## What this rules out
- Reaching the record by any continuous optimiser seeded from a smooth envelope
  or by polishing/perturbing the leader or our basin (all stay in-topology).
- Periodic / frequency-swept sign ansätze (too crude; the topology is aperiodic).
- A dual certificate deciding feasibility (collapses).

## What might still work
- **Seeding the correct sign topology directly** — i.e. obtaining a low-res
  version of the record's sign pattern (the collaborator's offered hint) and
  escaping it; `frozen_sign_descent` then lands in the right basin. This is the
  validated unlock and the standing request.
- **Sign-topology search co-adapting magnitudes** (not single-edit, not
  periodic): a larger-move combinatorial search where each proposal re-polishes
  magnitudes fully — expensive, EV uncertain, but the only blind route left.
- The escape that produced the leader's 4705-run topology was stochastic; a
  much stronger reproduction of the original larger-n escape over many seeds
  might sample a better topology, but our escape pipeline currently underperforms
  the original (1.4526 vs 1.45252), so this needs pipeline work first.

## The durable wisdom
For the autocorrelation family (P2/P4), once the envelope and negative-fraction
levers are exhausted, **what remains is a discrete sign-topology selection
problem** — outside the reach of gradient and LP methods. The lever is to make
the sign pattern an explicit input (`f = s·v²`), but the *right* aperiodic `s`
must come from a seed or a genuine combinatorial search, not a parametric sweep.
