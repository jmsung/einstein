---
type: question
author: agent
asked_by: tao
drafted: 2026-06-04
status: answered
answer_finding: ../findings/dead-end-p4-organon-floor-negative-content-lever.md
related_problems: [4]
---

> **ANSWERED (2026-06-04, Goal 4):** The shared P2/P4 technique is "push more of f to its feasible boundary than the equioscillation basin does" — P2 drives ~17% of cells to exactly zero (compact support), P4 drives ~27% negative. OrganonAgent holds both via this one lever. See [dead-end-p4-organon-floor-negative-content-lever.md](../findings/dead-end-p4-organon-floor-negative-content-lever.md).


# P4 headroom (Tao) — what single technique lets OrganonAgent hold BOTH P2 and P4?

1. P2 (f≥0) and P4 (signed f) are both `min(max(f★f))/(∫f)²` and OrganonAgent leads both — on the Fourier side, `(f★f)^ = f̂·f̂` for the cross-correlation but for the *auto*-correlation `(f★f)^ = |f̂|²` (P2) vs the signed product structure of P4; is there one Fourier-positivity / spectral-factorization move that produces the extremizer in both, differing only in whether `f̂` is constrained real-nonneg? — If so, the family-twin technique is "optimize on the Fourier side and impose/relax one positivity constraint," which is a parameterization we have not tried on either problem.

2. What is the single obstruction that capped *our* P4 at 1.4525212 — is it (a) the larger-n cascade saturating (resolution-bound), (b) the smooth-max β-cascade ceiling at 1e10 rounding the true max, or (c) a genuinely lower basin our warm-start can't reach from the n=400 SOTA? — Naming which of the three blocks us decides whether the next move is higher β, higher n, or a cold-start from a signed ansatz; right now we are guessing.

3. Could OrganonAgent's edge be a *scale-separation* construction — f built as a structured low-frequency envelope times a pseudo-random high-frequency carrier, so f★f's max is suppressed by destructive interference at nonzero lags — and is that the same envelope×carrier move that would also lower P2? — Dyadic envelope/carrier constructions for autocorrelation suppression are standard in the harmonic-analysis literature but absent from our P4 attempts (we only ever warm-started the equioscillation basin).
