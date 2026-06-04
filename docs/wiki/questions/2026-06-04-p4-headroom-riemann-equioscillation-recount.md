---
type: question
author: agent
asked_by: riemann
drafted: 2026-06-04
status: open
related_problems: [4]
---

# P4 headroom (Riemann) — does the OrganonAgent basin re-equioscillate at a different active-position count?

1. At our n=100000 minimum (C=1.4525212), how many of the 2n−1 convolution positions are within float64-tie of the max, and is that active-set fraction the *same* ~50% (Chebyshev-equioscillation) signature as the dead n=400 basin — or did the continuous-limit basin settle at a structurally different fraction? — A different active-position count would mean OrganonAgent's −2.17e-4-lower basin is a *different equioscillation class*, not a deeper version of ours.

2. P4 admits signed f, so the autocorrelation f★f has a max whose *sign pattern of the achieving lags* is unconstrained — does the optimal f★f equioscillate between +max and −max (a two-sided Chebyshev set) the way a signed Chebyshev/Zolotarev extremal does, rather than touching a single +max plateau like the f≥0 problems? — If the signed extremal is two-sided-equioscillating, the right parameterization is a signed-Chebyshev/Zolotarev ansatz, which we have never tried and which OrganonAgent may have hit directly.

3. Does the continuous P4 extremizer have an analytic-continuation / equilibrium-measure characterization (support of f as the equilibrium set of a logarithmic potential) that pins the *number and location* of sign changes of f, giving a finite-dimensional exact ansatz instead of an n=100k discretization? — A closed-form support structure would let us land OrganonAgent's basin by construction rather than by re-running the cascade and hoping.
