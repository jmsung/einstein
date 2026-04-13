# Float64 Polish & Precision Techniques

Techniques for squeezing the last bits of improvement at the float64 precision floor.

## When You're at the Float64 Floor

You're at the float64 floor when:
- All smooth optimizers (L-BFGS, Adam, SLSQP) report zero improvement
- Multiple agents submit byte-identical solutions
- mpmath high-precision evaluation shows the true-math score is only ulps away from the float64 score

## ULP-Step Discrete Descent

Once smooth optimizer noise (~1e-12) exceeds residual loss (~1e-13), continuous methods are unproductive. Switch to discrete ulp-step descent:

1. For each variable x[i], try x[i] ± {1, 2, 4} ulps
2. Re-evaluate the full objective
3. Accept if score improves

**Alternating sweeps** find more improvements:
- Single-coordinate sweeps: change one variable at a time
- 2-coordinate sweeps: change two variables simultaneously (within the same structure, e.g., intra-row for vectors)

Used successfully on P6 (kissing number) to push past the smooth optimizer floor.

## Float64 Screen + mpmath Verify

For problems requiring high-precision evaluation (P6, P18):

1. Use fast float64 to identify **active constraints** (~10% of all constraint pairs)
2. Evaluate only those constraints in mpmath at high precision
3. This is 10x faster than evaluating everything in mpmath

Rule of thumb for required precision:
- `dps ≥ log10(condition_number) + safety_buffer`
- P18 Laguerre k=15: condition ~10³⁸ → dps ≥ 30

## Float-Precision Lottery

When the mathematical optimum projects onto many near-equivalent float64 representations:

1. Apply random isometries (rotation, translation, small scaling)
2. Re-evaluate the transformed solution
3. Keep the best float64 representation

This works because different orientations of the same mathematical solution land on different float64 grid points.

## Byte-Identical Consensus

When 8+ independent agents submit byte-identical solutions, the solution is at the **float64 ceiling of a known published construction**. No from-scratch optimization can beat it without a fundamentally different algorithm.

At this point:
- **Download and verify**: Use the published solution as your warm-start
- **Check mpmath ceiling**: If the true-math gap is less than minImprovement, stop
- **Consider arena tolerance exploitation**: Some problems allow small constraint violations (see P17 circles-in-rectangle)

## mpmath Verifier Shift Trap

When a verifier upgrades from float64 to mpmath:
- Solutions that appeared to have score 0.0 in float64 may have residual ~10⁻¹³ in mpmath
- Float64's display precision (16 digits) hides the mpmath residual
- Always re-evaluate at mpmath dps=50+ before trusting a "perfect" score

This affected P6 (kissing number) when the arena switched verifiers mid-competition.

*Last updated: 2026-04-13*
