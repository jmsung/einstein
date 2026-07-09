---
type: question
author: agent
drafted: 2026-07-02
asked_by: agent
status: open
related_problems: [P7]
related_findings: [p7-n16000-degeneracy-crossover-off.md, prime-number-theorem-lp.md]
---

# Where does P7 base-LP N-extension saturate, and what is the LP→true-constant gap as maxkey→∞?

## The unknown

The field's 06-21→06-30 record burst is pure N-extension of the same base LP:
0.99485 (maxkey 3349) → 0.99568 (4501) → 0.99622 (16000) → ~0.99642 (24000, CHRONOS
06-30 base, rescale backed out). Support stays capped at ~2000 keys throughout — the
gain comes from *selecting a better 2000-key subset from a wider squarefree range*,
not from more keys. Two precise unknowns:

1. **Saturation**: as maxkey → ∞ with the ~2000-key cardinality cap fixed, does the
   base LP optimum converge, and at what maxkey does the marginal gain drop below the
   arena `minImprovement` (1e-6)? The gain per doubling is shrinking (+1.4e-3 for
   3349→16000, ~+2e-4 for 16000→24000) but is not yet < 1e-6.
2. **Gap**: what is the analytic limit of this LP family (constraint
   Σ f(k)⌊x/k⌋ ≤ 1, f supported on squarefree k, |f| ≤ 10, Mertens-type normalization)
   — is the limit the true PNT constant 1, and what does the remaining gap
   (1 − 0.9964 ≈ 3.6e-3) decompose into (cardinality cap vs finite maxkey vs |f| box)?

## Falsifiable answer shape

A curve base(maxkey) for maxkey ∈ {16k, 24k, 32k, 48k, 64k} at fixed 2000-key support,
plus either (a) an extrapolated limit with fit residuals, or (b) a dual-certificate
argument bounding the LP family's limit away from 1.

## Why it matters

Decides whether P7 reclaim is a compute ladder (keep extending N ahead of the field)
or a dead-end (saturation below the current record) — and whether the ~2000-key cap
is the binding constraint worth attacking instead.
