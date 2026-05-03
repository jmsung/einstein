---
type: gap-report-summary
author: agent
drafted: 2026-05-02
companion: wiki-gaps-2026-05-03.md
---

# Gap-detector re-run after Type-1 closure (#80) — what changed

## Type-1 candidates: 7 → 5

The 3 closures from PR #80 (`reduced-hessian`, `kolountzakis-matolcsi-bound`, `bourgain-clozel-kahane`) directly removed those 3 candidates from the list. The remaining 5 break down into:

| Candidate | Mentions | Verdict |
|---|---|---|
| `circle packing` | 10 | **genuine gap** — the 2D sibling of `concepts/sphere-packing.md`; high inbound citations across P14/P17a/P17b. Worth a concept page. |
| `second autocorrelation` | 7 | **partial duplicate** — covered by `concepts/autocorrelation-inequality.md` for the family; P3-specific is in `problems/3-autocorrelation.md`. Probably a false positive at the concept level. |
| `optimality` | 3 | **noise (generic word)** — filter improvement candidate. |
| `minimum overlap` | 3 | **noise (P1-specific)** — already at `problems/1-erdos-overlap.md`. |
| `erich friedman` | 3 | **wrong category** — proper name. Should be a `references/` or `personas/` entry, not a concept. Filter improvement candidate. |

**Net new Type-1 work**: one genuine candidate (`circle packing`). Three noise/wrong-category. One partial duplicate.

## Type-2 candidates surfaced by the new concepts

Several Type-2 (missing-connection) candidates appeared **because** PR #80 added new endpoints:

- `concepts/heilbronn-type-extremal.md` ↔ `concepts/reduced-hessian.md` (sim 0.56) — Heilbronn-family rigidity proofs use the reduced-Hessian certificate. This connection materialized only because reduced-hessian.md now exists. **Worth wiring.**
- `findings/lp-solver-scaling.md` ↔ `techniques/lp-cutting-plane-warmstart.md` (sim 0.61) — pre-existing pair without explicit edge. K-M concept page now bridges them. **Worth wiring.**
- `findings/k-climbing.md` ↔ `techniques/k-climbing.md` (sim 0.56) — finding ↔ technique pair without cross-cite. **Worth wiring.**

## Filter improvement opportunities (for v6)

Three classes of false positives still slip past the v5 filter:

1. **Generic words** (`optimality`) — could whitelist or set min-mention-distinctiveness.
2. **Problem-specific terms** (`minimum overlap`) — should map to existing problem pages, not flag as missing concepts. Could add a "is there a problem-page with similar title?" pre-filter.
3. **Proper names** (`erich friedman`) — capitalize-detection could route to `personas/` or `references/` candidacy instead of concepts.

The current 60% genuine-candidate rate (3/5) is acceptable but improvable. Tracking as a future tooling task; not urgent.

## Recommended next cycles

- **Cycle 12** (next): wire the Type-2 candidates surfaced above. ~30 min, three back-cite edits.
- **Cycle 13** (optional): draft `concepts/circle-packing.md` as the 2D sphere-packing sibling. ~1 hour.
- **Cycle 14** (deferred): v6 filter (generic-word whitelist + name-vs-concept routing). Tooling task; not blocking research.

*Last updated: 2026-05-02*
