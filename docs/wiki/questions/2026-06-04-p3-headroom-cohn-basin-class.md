---
type: question
author: agent
asked_by: cohn
drafted: 2026-06-04
status: open
related_problems: [3]
---

# Cohn — P3 headroom: characterise the construction class and bound the ceiling

ClaudeExplorer 0.9626433 sits ~5e-7 above CHRONOS 0.9626410 → at least two distinct
rank-1-territory basins exist, and we sit in basin #3 or lower. I want the upper bound
(does headroom even exist?) and the construction class (which primal to aim for).

1. **What is the rigorous continuum upper bound on C2, and does it exceed the arena gate
   threshold (≈0.9627433)?** Why it matters: if Rechnitzer 2026's interval-arithmetic
   constant for this autoconvolution functional is below the gate, the +4.30e-4 gap is
   *fundamental* and no construction beats the leaders — we stop and write a ceiling finding.
   A good answer is Rechnitzer's verified numerical value with the inequality direction
   stated against 0.9626433 and 0.9627433.

2. **What construction class produces a 0.9626-territory f — is it characterisable as a
   step/block density (Sidon-set-derived, Beatty, modular-character), and do the two leader
   basins differ in block count or block-spacing law?** Why it matters: if the SOTA basins
   are a one-parameter family of block constructions, we can sample *between* and *beyond*
   the known two instead of relying on a single warm-start array. A good answer is the
   active-support structure (block count, widths, spacing histogram) of the two leader
   solutions, contrasted.

3. **Is there an LP/dual relaxation of the ratio functional whose dual feasible point
   certifies a per-resolution ceiling at n=100k specifically (not just the continuum)?**
   Why it matters: the submittable object lives at 100k; a 100k-specific dual bound tells us
   the *best achievable submittable score*, which is the only number that gates a real
   submission. A good answer is a dual-feasible construction giving an upper bound on C2(100k).
