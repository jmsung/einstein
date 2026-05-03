---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 18
arena_url: unknown
status: hidden
score_current: 0.275
tier: A
concepts_invoked: [uncertainty-principle.md, bourgain-clozel-kahane.md, k-climbing-and-dof-augmentation.md, parameterization-selection.md, arena-tolerance-drift.md]
techniques_used: [k-climbing.md, gap-space-parameterization.md, mpmath-ulp-polish.md]
findings_produced: [verification-patterns.md]
private_tracking: ../../mb/tracking/problem-18-uncertainty/
---

# Problem 18 — Uncertainty (P18 slot)

## Statement
The P18 arena slot is the same uncertainty-principle objective as P9 (a polynomial-based bound for sign-uncertainty in dimension 12). The two tracking directories `problem-18-uncertainty/` and `problem-18-uncertainty-principle/` reflect divergent strategy snapshots taken before the P9 verifier issue surfaced.

## Approach
The polynomial g(x) has exactly one sign change at x_star; score = x_star / (2*pi). Coarse-grid roots (multiples of 0.125) opened a new basin below 1/pi, contradicting the prior consensus that S = 1/pi was a hard floor. Warm-start hillclimb with k-climbing (k=15 -> 16 -> 17), exact sympy verification per candidate, and per-root coordinate search with adaptive step sizes drove the score lower. Most responsive roots were mid-cluster and far-cluster doubles. Local optimization converges to the same ~1/pi basin without coarse-grid restart.

## Result
- **Score**: 0.275 (last valid arena submission, k=16)
- **Rank**: top of leaderboard prior to hide
- **Date**: as of 2026-04-19
- **Status**: HIDDEN by arena pending verifier fix (see P9). All scores below 0.2025 (Bourgain-Clozel-Kahane lower bound) are evaluator-bug artifacts and not real improvements.

## Wisdom hook
k-climbing plus coarse-grid restart escapes fixed-k basin plateaus — but the verifier-mismatch trap means triple-verify every score against a sympy-exact reimplementation before celebrating.

## Concepts invoked
- [uncertainty-principle.md](../concepts/uncertainty-principle.md)
- [k-climbing-and-dof-augmentation.md](../concepts/k-climbing-and-dof-augmentation.md)
- [parameterization-selection.md](../concepts/parameterization-selection.md)
- [arena-tolerance-drift.md](../concepts/arena-tolerance-drift.md)

## Techniques used
- [k-climbing.md](../techniques/k-climbing.md)
- [gap-space-parameterization.md](../techniques/gap-space-parameterization.md)
- [mpmath-ulp-polish.md](../techniques/mpmath-ulp-polish.md)

## Findings
- [verification-patterns.md](../findings/verification-patterns.md)

## References
- Bourgain, Clozel, Kahane (2010); Cohn et al. (uncertainty bounds, dimension 12).
- vinid GitHub issue #51 — arena verifier bug.

## Private tracking
For owner's reference: `mb/tracking/problem-18-uncertainty/` and `mb/tracking/problem-18-uncertainty-principle/` contain divergent strategy snapshots and the constraint-verification audit. Not part of the public artifact.
