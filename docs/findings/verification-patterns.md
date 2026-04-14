# Verification Patterns

How to build reliable evaluation pipelines that catch false positives before wasting submissions.

## Two-Tier Architecture

Every problem should have two evaluation tiers:

### Fast Evaluator (Inner Loop)
- **Purpose**: Drive the optimization loop at maximum speed
- **Implementation**: FFT, numpy vectorized, numba-compiled
- **Speed**: Milliseconds per evaluation
- **Accuracy**: Sufficient for ranking candidates, but may produce false positives

### Exact Evaluator (Quality Gate)
- **Purpose**: Verify candidates before trusting their scores
- **Implementation**: sympy, np.convolve, mpmath, direct O(n²) loops
- **Speed**: Seconds to minutes per evaluation
- **Accuracy**: Bit-exact match to arena verifier

### Never Collapse the Tiers

- **Exact-only**: Cripples search speed (100-1000x slower inner loop)
- **Fast-only**: Lets false positives through (wasted submissions, phantom progress)

### Hybrid Evaluator (Best of Both)

For P18 (uncertainty principle), a hybrid approach gives 8x speedup over full sympy:
- Use sympy for polynomial construction (where precision matters)
- Use numpy for root-finding (where speed matters)
- The exact polynomial coefficients ensure correctness; the fast root-finding enables iteration

## Triple Verification Protocol

Before submitting any solution, verify with three independent methods:

1. **Fast evaluator** — the score you optimized against
2. **Exact reimplementation** — different code path, same formula
3. **Cross-check** — different method entirely (e.g., FFT vs direct convolution)

If any two disagree by more than expected numerical noise, reject the candidate.

### Where False Positives Concentrate

- **Far-field evaluations**: Sign changes at x >> expected range (P18 uncertainty)
- **Float64 → mpmath discrepancies**: Scores that look perfect in float64 but have residual in mpmath (P6 kissing)
- **Boundary cases**: Piecewise functions evaluated near breakpoints (P13 edges-triangles)
- **Constraint violations**: Near-feasible solutions that pass fast checks but fail exact checks (packing problems)

## Arena Parity Testing

For every problem, maintain a test suite that:
1. Downloads top-K leaderboard solutions
2. Evaluates each with your evaluator
3. Asserts bit-exact score match with the arena

This catches evaluator bugs before they waste submissions. Run parity tests after any evaluator change.

## Pre-Submission Checklist

Before every submission:
- [ ] Fast evaluator score matches exact evaluator score
- [ ] Score improves on your previous best by ≥ minImprovement
- [ ] Score improves on EVERY leaderboard entry within minImprovement window
- [ ] Solution satisfies all constraints at the exact (not approximate) level
- [ ] Solution format matches the arena schema exactly
- [ ] Parity tests still pass (evaluator hasn't drifted)

*Last updated: 2026-04-13*
