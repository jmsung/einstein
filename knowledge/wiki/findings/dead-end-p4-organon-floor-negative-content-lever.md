---
type: finding
author: agent
drafted: 2026-06-04
question_origin: problem-4
status: answered
related_concepts: [autocorrelation-inequality, equioscillation, parameterization-selection, triple-verify]
related_problems: [2, 4]
cites:
  - ../problems/4-third-autocorrelation.md
  - ../findings/dead-end-p2-compact-support-basin-floor.md
  - ../findings/autocorrelation-family-displaced-2026-06.md
  - scripts/third_autocorrelation/optimize_fft.py
  - ../questions/2026-06-04-p4-headroom-tao-family-twin-technique.md
---

# Dead end: P4 is at OrganonAgent's floor; the family-twin lever is negative-lobe cancellation

## What we tried
P4 (`min C = |max(f★f)|/(∫f)²`, f MAY be negative — the signed twin of P2). Plan:
mirror Goal 3's architecture and try the untried signed parameterization. First
the cheapest-decisive checks (mirroring the P2 win): download OrganonAgent's #1
P4 solution, compare its sign structure to ours, and polish it to probe the floor.

## What we found

**1. The family-twin lever is the amount of negative content.** Both leaders'
and our P4 solutions are full-support n=100000; the difference is how much of f
is negative:

| solution | n | negative cells | score |
|---|---|---|---|
| OrganonAgent #1 | 100000 | **27524 (27.5%)** | 1.4523043332 |
| JSAgent #2 (ours) | 100000 | 23591 (23.6%) | 1.4525211550 |
| alpha_omega #3 | 100000 | 23591 (23.6%) | 1.4525211550 |

P4's score only counts the *positive* peak of f★f; negative excursions of f are
free. OrganonAgent exploits that freedom *more* — ~4% more cells driven negative
— buying the −2.17e-4 edge. We are in a less-negative basin.

**2. OrganonAgent's basin is at its floor.** Ran the smooth-max L-BFGS β-cascade
(1e6→1e10, 400 iters) warm-started from OrganonAgent's #1. Every β level returned
C ≥ the initial; final best = **1.4523043331832**, bit-identical to the start. No
improvement — the leader's signed basin is locally minimal under our optimiser.

## The unifying P2+P4 insight (answers Tao's family-twin question)
OrganonAgent holds **both** P2 and P4 — the twin `min max(f★f)/(∫f)²` problems —
and the single transferable idea is: **exploit the constraint freedom more fully
than the equioscillation basin does.**

- **P2** (f ≥ 0): drive ~17% of cells to *exactly zero* → a compact-support basin
  (`dead-end-p2-compact-support-basin-floor`).
- **P4** (f signed): drive ~27% of cells *negative* → a more-cancelling basin.

Both are the same move — push more of f to the boundary of its feasible set
(zero for P2, negative for P4) than the symmetric equioscillation basin does. Our
basins on both problems stop short of that boundary, which is exactly the residual
gap. This is the family technique the displacement finding asked about.

## What this rules out
- **Polishing our P4 basin (or the leader's) to a record.** The leader's basin is
  at its floor; ours is a distinct, less-negative basin a polish cannot cross.
- **Treating P4 as separate from P2.** They share one lever; a win on one
  parameterisation idea (push-to-boundary) should be tried on both together.

## What might still work (low EV)
- **Signed new-basin search with a negative-content target**: re-optimise with a
  schedule that *encourages* more negative cells (toward/above 27.5%), or a
  signed-Chebyshev / both-sign-Fourier ansatz
  (`2026-06-04-p4-headroom-hilbert-signed-parameterization`), aiming to beat
  1.4523043332. EV is low — the leader's basin is already locally minimal and
  only two agents reach it — but this is the one untried lever. A Cohn signed-f
  LP/SDP dual certificate would decide whether 1.4523 is the continuous infimum.
- Honest-zero for this branch; the negative-content lever is the wisdom.

## RESOLVED (2026-06-06, branch js/feat/p4-record-breakthrough)
The "untried lever" above was tried and is now closed — see
[dead-end-p4-negative-content-ceiling](dead-end-p4-negative-content-ceiling.md).
Forcing the negative fraction past 27.5% (annealed nudge, n=100000, leader
warm-start) **monotonically WORSENS C** (27.5%→1.4523058 best, 29.5%→1.4564);
cold both-sign Fourier lands ~1.49. The negative content is a *saturated basin
coordinate at its optimum*, not a lever with headroom. The framing in this page
("push more of f to its feasible boundary") correctly *describes* the gap but
wrongly implies headroom — there is none above the leader's fraction. The only
remaining lever is the signed-f dual certificate (research, deferred).
