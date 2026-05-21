---
type: question
author: agent
drafted: 2026-05-02
status: open
asked_by: cohn
related_problems: [P19]
related_concepts: [provable-floor-and-frozen-problems.md, lp-duality.md, p19-fully-resolved.md, kolountzakis-matolcsi-bound.md]
child_questions: [2026-05-03-p19-bernshteyn-tait-tightening.md]
cites:
  - 2026-05-03-p19-bernshteyn-tait-tightening.md
  - ../concepts/p19-fully-resolved.md
---

> **2026-05-03 update**: see [`2026-05-03-p19-bernshteyn-tait-tightening.md`](2026-05-03-p19-bernshteyn-tait-tightening.md) for the concrete attack-route scoping. The Bernshteyn–Tait 2019 LP route (with 4 sub-hypotheses H2.1–H2.4) is the most promising operational path under H2 below.

# Is the P19 7-way tie a structural cap, and if so what is the LP/SDP certificate?

## Question

Several P19 attempts converge to 2.639027 (7-way tie). Analogous to how κ(12)=840 is provably capped (P22), is there an LP or SDP dual certificate that proves the P19 ratio cannot drop below this value?

## Why it matters

A proven cap = formal negative result (publishable wisdom). It also closes off compute waste on an unwinnable problem and lets the agent move to richer territory.

## What would the certificate look like?

For sphere packings, the Cohn–Elkies bound is a Fourier-positive "magic function" `f` whose value at 0 over Plancherel sum bounds the packing density from above. The analog for difference bases would be a function on Z (or Z/NZ) with appropriate positivity that bounds `|B|² / max_diff_set` from above.

## Hypotheses

- **H1**: Direct LP relaxation over indicator vectors of `B` ⊂ {0,...,N} with constraints encoding "difference set covers [1,V]" — write as IP, relax to LP, dual gives certificate.
- **H2**: Spectral / Fourier dual: `1_B \star 1_{-B}` has L¹ mass bounded by Plancherel; combined with covering condition, may give an additive-combinatorics dual.
- **H3**: Group-theoretic obstruction: if all length-V difference bases factor through Z/pZ for some prime p, character bounds give the certificate.

## Next step

1. Formulate LP relaxation in `cb/scripts/p19/`. Solve via HiGHS IPM.
2. Inspect dual variables — if dual hits 2.639027, that's the certificate.
3. If LP is loose (dual < 2.639027), try Plancherel/Fourier dual via the autocorrelation framing.

## References

- `wiki/concepts/lp-duality.md`
- `wiki/concepts/provable-floor-and-frozen-problems.md`
- `wiki/techniques/lp-cutting-plane-warmstart.md`
- `source/papers/2010-vinuesa-sidon-thesis.md`
- `source/papers/2007-gyarmati-sums-differences.md`
