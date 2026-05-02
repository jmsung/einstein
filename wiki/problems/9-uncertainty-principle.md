---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 9
arena_url: https://einsteinarena.com/problems/uncertainty-principle
status: hidden
score_current: 0.275
tier: A
concepts_invoked: [uncertainty-principle.md, k-climbing-and-dof-augmentation.md, parameterization-selection.md, arena-tolerance-drift.md]
techniques_used: [k-climbing.md, gap-space-parameterization.md, cma-es-with-warmstart.md, mpmath-ulp-polish.md]
findings_produced: [verification-patterns.md]
private_tracking: ../../mb/tracking/problem-9-uncertainty-principle/
---

# Problem 9 — Uncertainty Principle

## Statement
Minimize a polynomial-based uncertainty bound for Hermite/Laguerre eigensystems, subject to constraints on f-evenness and the signs of f(0), f-hat(0). The +1 sign-uncertainty constant in dimension 12.

## Approach
The polynomial g(x) has exactly one sign change at x_star; score S = x_star / (2*pi). All standard local optimizers (CMA-ES, NM, hillclimb, DE, basin-hopping) converge to the same fixed-k basin around 1/pi. The breakthrough was k-climbing: rather than optimizing at fixed k, repeatedly increase the polynomial degree (k = 13 to 14 to 19 to 50), each insertion creates new degrees of freedom that escape the lower-k plateau. Two-tier verification (fast evaluator screens, sympy exact verifies) catches the 90+ percent false-positive rate of the smooth evaluator.

## Result
- **Score**: 0.275 (last valid arena submission, k=16)
- **Rank**: top-tier locally
- **Date**: as of 2026-04-19
- **Status**: HIDDEN by arena pending verifier fix (the server cannot enforce the f(0) < 0 / f-hat(0) < 0 constraints; the agent's local evaluator has the same bug and must be augmented). Known theoretical bounds: 0.2025 (Bourgain-Clozel-Kahane) <= S <= 0.3102 (Cohn-de Laat-Goncalves).

## Wisdom hook
k-climbing (adding DOF via dimensionality increase) escapes fixed-k basin plateaus — always verify all mathematical constraints in the evaluator before optimization.

## Concepts invoked
- [uncertainty-principle.md](../concepts/uncertainty-principle.md)
- [k-climbing-and-dof-augmentation.md](../concepts/k-climbing-and-dof-augmentation.md)
- [parameterization-selection.md](../concepts/parameterization-selection.md)
- [arena-tolerance-drift.md](../concepts/arena-tolerance-drift.md)

## Techniques used
- [k-climbing.md](../techniques/k-climbing.md)
- [gap-space-parameterization.md](../techniques/gap-space-parameterization.md)
- [cma-es-with-warmstart.md](../techniques/cma-es-with-warmstart.md)
- [mpmath-ulp-polish.md](../techniques/mpmath-ulp-polish.md)

## Findings
- [verification-patterns.md](../findings/verification-patterns.md)

## References
- Bourgain, Clozel, Kahane (2010) — sign uncertainty bounds.
- Cohn, de Laat, Goncalves (unpublished) — upper bound 0.3102.
- Goncalves (2017), Hermite uncertainty.
- Georgiev et al. (2025), exploration of related extremal polynomials.
- vinid GitHub issue #51 — arena verifier bug report.

## Private tracking
For owner's reference: `mb/tracking/problem-9-uncertainty-principle/` contains the constraint-verification audit, k-climbing log, and theoretical-bound writeup. Not part of the public artifact.
