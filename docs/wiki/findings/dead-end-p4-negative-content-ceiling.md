---
type: finding
author: agent
drafted: 2026-06-06
question_origin: problem-4
status: answered
related_concepts: [autocorrelation-inequality, equioscillation, parameterization-selection, triple-verify]
related_problems: [2, 4]
cites:
  - ../problems/4-third-autocorrelation.md
  - ../findings/dead-end-p4-organon-floor-negative-content-lever.md
  - ../findings/p4-fragmentation-not-fraction-shared-envelope.md
  - ../questions/2026-06-04-p4-headroom-cohn-signed-dual-certificate.md
  - scripts/third_autocorrelation/campaign_signed.py
---

# Dead end: forcing P4 negative content past 27.5% monotonically WORSENS C

## What we tried
The one untried lever from `dead-end-p4-organon-floor-negative-content-lever`:
a signed search that *encourages* more negative content than the leader's 27.5%.
Built `signed_descent` (smooth-max L-BFGS β-cascade) with an annealed
negative-content nudge (`surrogate_with_neg`), warm-started from OrganonAgent's
full n=100000 structure, and swept neg_target ∈ {0.30…0.40} × detail_scale at
n=100000 (`campaign_signed.py`).

## Why it failed — the negative fraction has a ceiling, not headroom
Every increase in forced negative fraction strictly raised C:

| neg fraction | C | Δ vs leader |
|---|---|---|
| 27.53% (control, no nudge) | 1.4523057621285 | +1.43e-6 |
| 29.08% | 1.4525846228294 | +2.80e-4 |
| 28.76% | 1.4531651688955 | +8.61e-4 |
| 28.92% | 1.4545482519174 | +2.24e-3 |
| 29.49% | 1.4564318937134 | +4.13e-3 |

Monotonic. The control (no nudge, tiny perturbation) returns to within 1.43e-6 of
the leader floor and is the best of the sweep; triple-verified (arena/scipy/rfft
agree to 4.44e-16). **The leader's 27.5% sits at the optimal fragmentation
tradeoff.** Driving more of f negative raises the positive autocorrelation peak
`max(f★f)` faster than it shrinks the `(∫f)²` denominator — the cancellation that
negative lobes buy is already saturated at ~27.5%. There is no free boundary to
push toward, contrary to the "push more of f to its feasible boundary" framing.

This *corrects* the prior two findings: the negative-content difference is a real
description of the leader↔our gap, but it is a **basin coordinate at its
optimum**, not a lever with headroom. Polishing either basin (Goal 0) and forcing
past the leader's fraction (this finding) both fail — the construction/upper-bound
side is exhausted for the smooth-max optimizer family.

## What this rules out
- **The whole negative-content-push family on P4** (and, by the P2/P4 family
  symmetry, the analogous compact-support-fraction push on P2). The feasible-set
  boundary is not a free lever; the leaders sit at its optimum.
- **More overnight optimizer runs of this shape.** The monotonic evidence makes
  EV ≈ 0; a "refined run #2" of the same lever would be fishing.

## What might still work (the only remaining lever — not an optimizer run)
- A **signed-f dual certificate** (Cohn-style LP/SDP) to decide whether
  1.4523043332 is the continuous infimum. The signed case currently sits on no
  known lower bound (`2026-06-04-p4-headroom-cohn-signed-dual-certificate`); the
  f≥0 majorant apparatus loses the ∫f=‖f‖₁ pairing. This is research requiring
  unbuilt LP/SDP wiring — deferred. If 1.4523 is provably the infimum, P4 is
  closed; if a gap remains, the certificate's dual points at the structure to
  exploit. Either way it is the next door, and it is not a hill-climb.

## Verdict
Honest-zero for `js/feat/p4-record-breakthrough`. Wisdom banked: the negative
fraction is a saturated basin coordinate, not a lever — across the whole P2/P4
autocorrelation family.
