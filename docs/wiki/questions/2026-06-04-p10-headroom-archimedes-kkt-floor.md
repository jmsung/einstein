---
type: question
author: agent
asked_by: archimedes
drafted: 2026-06-04
status: open
related_problems: [10]
---

# P10 (Thomson n=282) — Archimedes: what verifiable test turns "20 years unbeaten" into a certified strict local minimum, and is our submitted basin just the wrong one?

1. The Thomson problem is unconstrained on S² (no contact-graph rigidity to count) — so what is the right confirmatory test? Specifically: does the projected (Riemannian) Hessian of the Coulomb energy at the Wales config, restricted to the 2×282 − 3 = 561 tangent DOF after removing the global SO(3) rotation gauge, have all-positive eigenvalues (smallest λ_min > 0)? Matters because a positive-definite reduced Hessian is a *constant-time certificate* of a strict local minimum — it converts "no one improved it in 20 years" into "this is provably a strict local min, and the optimizer's residual gradient ~7e-12 is float64 noise around it," which is exactly the look-back deliverable this branch should produce.

2. Our current arena submission is the n=283→282 *downgrade* basin at 37147.53 (gap +0.23, rank ~#5), yet we already hold the Wales seed at 37147.2944 — is there any reason NOT to replace the submitted solution with the Wales config to claim the tied-rank that 37147.53 forfeits? Matters because this is a free rank-up independent of any record attempt: per the frozen-but-not-frozen-for-points rule (provable-floor concept §"strategic asymmetry"), our prior best (37147.53) is far enough from the leader that the minImprovement=1e-5 gate clears, so submitting the better basin we already have is pure upside with zero compute.

3. What is the smallest energy gap between the Wales basin and the *nearest distinct basin* we have ever observed (downgrade 37147.53, random-restart 37147.74, icosadeltahedral-seed 37148.04) — i.e. is the funnel gap ≥ 0.2, and does that gap size by itself rule out any sub-Wales basin within minImprovement=1e-5 reach of local polish? Matters because if the nearest competitor sits +0.2 above and the basin is Hessian-certified, then the headroom for any local method is provably ≪ minImprovement and the honest-zero closeout is certified rather than assumed.
