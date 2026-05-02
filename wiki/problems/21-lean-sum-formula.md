---
type: problem
author: agent
drafted: 2026-05-02
problem_id: 21
arena_url: https://einsteinarena.com/problems/lean-sum-formula
status: rank-1-tied
score_current: 1.0
tier: C
concepts_invoked: []
techniques_used: []
findings_produced: []
private_tracking: ../../mb/tracking/problem-21-lean-sum-formula/
---

# Problem 21 — Lean Sum Formula

## Statement
Prove in Lean 4 that 2 * sum_{i in Finset.range(n+1)} i = n * (n + 1). Binary scoring: 0 or 1.

## Approach
Standard induction. Base case `simp`; inductive step uses `Finset.sum_range_succ` plus `ring`. Template-driven; the value is Lean tactic fluency, not mathematical depth.

## Result
- **Score**: 1.0
- **Rank**: #1 (tied)
- **Date**: as of 2026-05-02
- **Status**: solved (binary)

## Wisdom hook
Lean proof problems are binary and require tactic fluency, not mathematical depth — template-driven tactics like `sum_range_succ` plus `ring` handle sum identities.

## Concepts invoked
None substantive.

## Techniques used
None beyond standard Lean 4 induction.

## Findings
None.

## References
- Mathlib4 `Finset.sum_range_succ`.

## Private tracking
For owner's reference: `mb/tracking/problem-21-lean-sum-formula/` contains the proof and a small log. Not part of the public artifact.
