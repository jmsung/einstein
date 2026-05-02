---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P1, P2, P4]
compute_profile: [local-cpu]
cost_estimate: "minutes (one Remez run on SOTA)"
hit_rate: "TBD"
---

# Remez Exchange — Equioscillation Diagnostic

## TL;DR

The Remez exchange algorithm is the canonical Chebyshev-equioscillation test for minimax problems. **As a diagnostic** (not as an optimizer): given a candidate SOTA, count how many active shifts (or grid points) attain the max within a tight tolerance — if Remez requires zero exchanges and the active count ≥ n/2, the SOTA satisfies the equioscillation necessary conditions. P1 Erdős: zero exchanges at 437 active shifts → minimax local-optimal at SOTA.

## When to apply

- Discretized-function minimax problem (max_k f(k) or min_k f(k)) — P1 Erdős, P2/P4 autocorrelation.
- A candidate SOTA exists; question is whether it's locally optimal.
- Combine with first-order (PyTorch L-BFGS gradient) and second-order (CMA-ES sigma collapse) for a three-way local-optimality proof (lesson #96).

## Procedure

1. **Compute active set** at the candidate SOTA: `{k : f(k) ≥ max_k f − tol}` with tol ≈ 1e-12.
2. **If `|active| ≥ n/2`**: equioscillation fingerprint present; proceed to Remez.
3. **Run Remez exchange**: at each iteration, find the worst-violating point not in the current active set; swap it in. Standard implementation (see `scipy.signal.remez` for filter-design analog).
4. **Stop condition**: zero exchanges → SOTA satisfies Chebyshev equioscillation necessary conditions.
5. **Combine with three-way proof** (lesson #96):
   - First-order: PyTorch L-BFGS gradient = 0.
   - Second-order: CMA-ES sigma collapse to 1e-15.
   - Minimax: Remez = zero exchanges.
   All three converging in ~10 min total = strongest computational proof of local optimality.

## Pitfalls

- **Discretization vs continuous bound** (lesson #51): equioscillation at n=400 may be the *discretization* bound, not the continuous bound. Test larger-n escape (`larger-n-cascade.md`) before declaring "frozen at theoretical bound" — the tied trio on P4 was at the discretization bound only.
- **Bilinear minimax defeats Remez naïvely**: if the score has bilinear structure (P1: `h(x) · (1 − h(x+k))`), the SDP relaxation is loose AND classic Remez may converge to a non-tight bound. Use Remez as a LOCAL-optimality diagnostic, not a global optimizer.
- **Active-count threshold**: ≥ n/2 is the textbook fingerprint, but tight problems can have active counts ≥ n/2 even when not yet at the optimum. Pair with the gradient/sigma tests.
- **Don't use Remez as optimizer for high-dim problems**: it's a 1D minimax tool by design. Larger-n autocorrelation problems use L-BFGS smooth-max β-cascade for the actual descent; Remez is the verification step.

## Compute profile

Local CPU. One Remez run on a candidate SOTA: minutes. Sequential — GPU sits idle.

## References

- `wiki/findings/equioscillation-escape.md` (lessons #34, #51, #52 — discretization vs continuous).
- `wiki/findings/basin-rigidity.md` (lesson #96 — three-way local-optimality proof).
- knowledge.yaml pattern `equioscillation-active-triple-diagnostic`.
- `wiki/techniques/larger-n-cascade.md` (the escape path when discretization is the trap).
- `wiki/techniques/cma-es-with-warmstart.md` (companion second-order test).
- `mb/wiki/problem-1-erdos-overlap/strategy.md` (437 active shifts).
