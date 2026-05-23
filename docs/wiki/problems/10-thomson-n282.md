---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 10
arena_url: https://einsteinarena.com/problems/thomson
status: rank-5-frozen
score_current: 37147.53
tier: B
concepts_invoked: [sphere-packing.md, basin-rigidity.md, symmetry-and-fundamental-domain.md, provable-floor-and-frozen-problems.md]
techniques_used: [basin-hopping-multistart.md, mpmath-ulp-polish.md, parallel-tempering-sa.md]
findings_produced: [frozen-problem-triage.md]
private_tracking: ../../mb/tracking/problem-10-thomson/
---

# Problem 10 — Thomson Problem (n=282)

## Statement
Place 282 points on the unit 2-sphere to minimize the Coulomb energy E = sum_{i<j} 1 / ||p_i - p_j||.

## Approach
n=282 is an icosadeltahedral magic number (T=28; 12 pentagonal defects, 270 hexagonal vertices) under the chiral icosahedral group I. The Wales Cambridge database putative global minimum at E = 37147.29441846226 has stood unbeaten for 20+ years. Three independent agents converge to bit-identical scores — extremely strong evidence of true global optimum. Riemannian gradient descent, L-BFGS on SO(3), micro-perturbation 1e-7 to 1e-14, basin-hopping with rotation lottery, and upgrade/downgrade probes (n=281, 283) all confirm the same basin. The only "improvements" are float64 noise.

## Result
- **Score**: 37147.53 (current submission); SOTA 37147.2944 frozen
- **Rank**: #5 pending
- **Date**: as of 2026-05-02
- **Status**: frozen at putative global minimum (magic-number configuration)

## Wisdom hook
Magic-number Thomson configurations (icosadeltahedral, n=282) sit at proven/putative global optima — skip immediately, compute will only confirm.

## Concepts invoked
- [sphere-packing.md](../concepts/sphere-packing.md)
- [basin-rigidity.md](../concepts/basin-rigidity.md)
- [symmetry-and-fundamental-domain.md](../concepts/symmetry-and-fundamental-domain.md)
- [provable-floor-and-frozen-problems.md](../concepts/provable-floor-and-frozen-problems.md)

## Techniques used
- [basin-hopping-multistart.md](../techniques/basin-hopping-multistart.md)
- [mpmath-ulp-polish.md](../techniques/mpmath-ulp-polish.md)
- [parallel-tempering-sa.md](../techniques/parallel-tempering-sa.md)

## Findings
- [frozen-problem-triage.md](../findings/frozen-problem-triage.md)

## References
- Wales Cambridge Cluster Database (Thomson minima, 20+ year archive).
- Smale's 7th problem (Thomson energy minimization).
- Caspar-Klug icosadeltahedral triangulation theory.

## Private tracking
For owner's reference: `mb/tracking/problem-10-thomson/` contains the basin diagnostic and the frozen-problem rationale. Not part of the public artifact.
