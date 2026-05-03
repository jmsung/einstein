---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 11
arena_url: https://einsteinarena.com/problems/tammes-problem
status: rank-2-frozen
score_current: 0.513472084680564
tier: B
concepts_invoked: [sphere-packing.md, contact-graph-rigidity.md, float64-ceiling.md, basin-rigidity.md]
techniques_used: [slsqp-active-pair-polish.md, mpmath-ulp-polish.md, multistart-with-rotation-lottery.md, warm-start-from-leader.md]
findings_produced: [float64-ceiling.md]
private_tracking: ../../mb/tracking/problem-11-tammes/
---

# Problem 11 — Tammes Problem (n=50)

## Statement
Place 50 points on the unit 2-sphere to maximize the minimum pairwise Euclidean distance after L2 normalization.

## Approach
Tammes(50) is a known optimum tracked by Hardin-Sloane sphere-codes tables. Multi-agent consensus converges to the contact graph; final rank is determined by float64-ceiling polish. Wide active-pair tolerance (tol_active = 1e-3) is essential — narrow tolerance (1e-7) misses 95+ near-contact pairs and the SLSQP polish stalls below the ceiling. Pipeline: warm-start from public SOTA, SLSQP active-pair polish at wide tolerance, mpmath 80-digit verification, ulp-level coordinate descent. Rotation lottery (86/2000 hit ceiling) explored gauge orbit.

## Result
- **Score**: 0.513472084680564
- **Rank**: #2 (2 ulps below #1)
- **Date**: as of 2026-04-05
- **Status**: basin-locked at float64 ceiling

## Wisdom hook
Contact-graph-locked basins require wide active-pair tolerance (tol=1e-3) to capture all near-contact pairs — narrow tolerance (1e-7) misses 95+ pairs and stalls below ceiling.

## Concepts invoked
- [sphere-packing.md](../concepts/sphere-packing.md)
- [contact-graph-rigidity.md](../concepts/contact-graph-rigidity.md)
- [float64-ceiling.md](../concepts/float64-ceiling.md)
- [basin-rigidity.md](../concepts/basin-rigidity.md)

## Techniques used
- [slsqp-active-pair-polish.md](../techniques/slsqp-active-pair-polish.md)
- [mpmath-ulp-polish.md](../techniques/mpmath-ulp-polish.md)
- [multistart-with-rotation-lottery.md](../techniques/multistart-with-rotation-lottery.md)
- [warm-start-from-leader.md](../techniques/warm-start-from-leader.md)

## Findings
- [tammes-50-basin-uniqueness-evidence.md](../findings/tammes-50-basin-uniqueness-evidence.md) — 4-line evidence pyramid: catalogue silence, 11-agent convergence, 14-method search, float64-ceiling bound. Empirical H1 supported; formal H1 (LP/SDP certificate) still open.
- [dead-end-tammes-topology-mutation.md](../findings/dead-end-tammes-topology-mutation.md) — 60-trial vertex-perturb-and-polish topology-mutation probe (2026-05-02). Basin attractor radius ≥ 1e-2; no alternative basin found.
- [float64-ceiling.md](../findings/float64-ceiling.md) — cross-problem inventory of float64-ceiling occurrences (P2, P5, P6, P10, P11, P14, P15, P17a/b, P23)

## Open questions
- [2026-05-02-p11-tammes-basin-escape.md](../questions/2026-05-02-p11-tammes-basin-escape.md) — is the Hardin–Sloane contact graph uniquely optimal? Empirically yes (overwhelming); formally unproven (no LP/SDP certificate).

## References
- Hardin and Sloane, sphere-codes tables.
- Conway and Sloane, "Sphere Packings, Lattices and Groups."
- Tammes (1930), original biological motivation.

## Private tracking
For owner's reference: `mb/tracking/problem-11-tammes/` contains the SLSQP tolerance calibration log and rotation lottery statistics. Not part of the public artifact.
