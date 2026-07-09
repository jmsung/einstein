---
type: finding
author: agent
drafted: 2026-06-01
question_origin: problem-17
status: answered
related_concepts: [float64-ceiling]
related_problems: [17]
cites:
  - src/einstein/ulp_polish.py
  - src/einstein/hexagon/evaluator.py
---

# Dead end: dual-gate ULP polish on P17 (hexagon packing) — no seed, penalty-shaped score

## What we tried

Phase 2a listed P17 (hexagon packing, both halves "a/b") as a dual-gate ULP-polish
target. We inspected `src/einstein/hexagon/evaluator.py` and the scripts tree for a
wiring path.

## Why it failed — two obstructions

1. **No in-repo seed.** There is no `scripts/hexagon/seeds/best.json`. The
   `optimize_hexagon.py` warm-starts are heuristic ("Feynman_centered" ≈ 3.9419)
   and P17 is not in the `verify_seed` registry or the dispatch manifest — there
   is no canonical rank-current config to polish.

2. **The score is penalty-shaped, not a smooth packing objective.**
   `evaluate(data) = outer_side_length + penalty·num_violations`, where the
   violations come from SAT polygon-overlap + containment tests over 12 hexagons
   each with a **rotation** DOF (`[cx, cy, angle]`) plus 4 outer-frame params.
   The dual-gate ULP polish assumes a continuous objective whose exact (mpmath)
   value the gate can rank monotonically (Σr, min distance, distance ratio). A
   discrete penalty term and SAT overlap booleans give the ulp gate nothing to
   climb: a sub-ulp coordinate step either leaves `num_violations` unchanged
   (merit flat → rejected) or flips a SAT boolean (merit jumps by `penalty` →
   not a sub-ulp regime). The technique's accept signal does not exist here.

## What this rules out

The dual-gate ULP polish needs a **continuous, exactly-evaluable** objective. It
does not apply to penalty-shaped / combinatorial-feasibility objectives (SAT
overlap, rotation DOF), independent of seed availability. P17's float64 ceiling,
if it has one, must be characterized by the hexagon-specific KKT/contact analysis,
not by coordinate ulp descent.

## What might still work

- A seed backfill + a hexagon-specific active-contact polish that treats the
  outer side length as the smooth objective and the SAT overlaps as hard
  constraints (analogous to the packing dual gate, but with polygon-distance
  constraints) — a separate technique, not this one.

## See also

- [mpmath-ulp-polish-dual-gate-p14](mpmath-ulp-polish-dual-gate-p14.md)
- [dead-end-ulp-polish-scale-limit-kissing-p22-p23](dead-end-ulp-polish-scale-limit-kissing-p22-p23.md) — the other Phase-2a scope boundary.
