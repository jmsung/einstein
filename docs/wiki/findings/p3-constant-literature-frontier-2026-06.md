---
type: finding
author: agent
drafted: 2026-06-05
question_origin: problem-3
status: answered
answer_question: ../questions/2026-06-04-p3-arena-resolution-cap-2M.md
related_concepts: [autocorrelation-inequality, kolountzakis-matolcsi-bound]
related_problems: [3]
cites:
  - ../../source/2025-jaech-autoconvolution.md
  - ../../source/2025-boyer-autoconvolution.md
  - ../../source/2022-white-almost-tight-autoconvolution-inequality.md
  - ../../source/2019-barnard-three-convolution-inequalities-real.md
  - p3-closed-form-baseline-landscape.md
  - dead-end-p3-jaech-cascade-extended.md
  - https://arxiv.org/abs/2508.02803
---

# P3 second-autocorrelation constant: the arena is ahead of published mathematics; the ceiling is open

## The question
Is there a construction or literature lead that beats the arena's 0.9626433 on
P3's ratio `R(f) = ‖f★f‖₂²/(‖f★f‖₁·‖f★f‖∞)`, `f ≥ 0`? Is 0.9626433 a known
barrier, or just where greedy local search stalls? (Asked after a 10h, ~1,500-task
parallel 400k new-basin hunt found zero improvement over the leader.)

## Answer: no known construction beats it; the constant is genuinely open
P3's `sup_f R(f)` is exactly the **second-autocorrelation / improved-Hölder
inequality constant** — an actively-researched open problem. The frontier:

| bound | value | who / how |
|---|---|---|
| trivial upper (Hölder/Cauchy–Schwarz) | **1.0** | — |
| best *published* lower bound | **0.94136** | Jaech–Joseph 2025 (arXiv 2508.02803): 2,399 equal intervals, then 4× upsample of a 559-interval Adam optimizer |
| prior published | 0.901562 | Boyer–Li 2025 (575 intervals) |
| **arena #1 (ClaudeExplorer)** | **0.9626433** | finer-resolution (400k) tuned step function |
| our local (unsubmittable 1.6M) | 0.9627190 | same family, higher resolution, >4.5MB cap |

**Two decisive facts:**
1. **The arena is AHEAD of the peer-reviewed literature.** The best published
   construction (Jaech–Joseph 0.94136) is *below* the arena's 0.9626433. The
   arena's approach is literally the finer-resolution evolution of Jaech's
   interval+upsample method (the wiki's `2025-jaech-autoconvolution` distillation
   documents this lineage). So **no published construction would seed us higher** —
   beating 0.9626433 means beating the world record, not catching up to it.
2. **No non-trivial UPPER bound exists.** Every paper bounds `sup R` from *below*
   via constructions; the best *upper* bound anyone has proven is the trivial 1.0.
   Proving `sup R < 1` is the open Martin–O'Bryant question. So the true ceiling is
   unpinned in **(0.9626433, 1.0]** — a record is not ruled out, but reaching it is
   unsolved mathematics, not an optimizer-tuning gap.

## Why local search (and our hunt) stalls exactly here
- **Closed forms cap at 0.722** (`p3-closed-form-baseline-landscape`); the
  arcsine/power-law family (White/Barnard's extremals for the *different* μ₂ and
  averaged-autocorrelation constants) scores 0.574–0.722 on *this* ratio — verified
  again 2026-06-05 (power-law sweep: best 0.724 at c=1.5). Those leads do not
  transfer: P3's ratio rewards a FLAT `f★f`, not the arcsine profile.
- **From-scratch/random init caps at 0.901** (`dead-end-p3-jaech-cascade-extended`),
  a basin structurally disjoint from the SOTA basin.
- **The 0.9626433 basin is a single saturated optimum**: ClaudeExplorer and CHRONOS
  are shape-identical (correlation 0.999, same support). Our 10h 18-core hunt —
  intensify + large-perturbation escape + CHRONOS seed + 6 from-scratch
  constructions, ~1,500 tasks — never exceeded the leader (best worker 0.962633).

## What this rules in / out
- **RULES OUT** (for beating 0.9626433): the literature interval-construction method
  (coarser than arena), closed-form ansätze, from-scratch multistart, and basin
  perturbation. All converge ≤ 0.9626433.
- **RULES IN** (the only residual levers, both hard):
  1. A **rigorous (or numerical) upper bound** via White/Rechnitzer-style Fourier
     reformulation (`‖f★f‖₂² = ‖f̂‖₄⁴`) + an SOS/moment SDP certificate that
     `‖f★f‖∞ ≥ C`. Decisive: if the bound lands ≈0.9627 the record is the ceiling;
     if higher, a chase is justified. But a *rigorous* `sup R < 1` is an open problem;
     only a non-rigorous numerical estimate is realistically buildable.
  2. Number-theoretic construction-driven seeds (Sidon/Beatty/modular) — ~10% odds
     of a distinct higher basin (`dead-end-p3-jaech-cascade-extended` residue path 1).

## Decisive payload-frontier sweep (2026-06-06)
Cross-resolution transfer (upsample leader + long Dinkelbach — the method that made
our 0.96272 at 1.6M) run as a 6-way parallel sweep across the full submittable band,
~5h/core. Best per resolution, all payload-fitting:

| n | best C2 | vs record |
|---|---|---|
| 450k | 0.96259551 | −4.78e-5 |
| 500k | 0.96260049 | −4.28e-5 |
| 550k | 0.96260027 | −4.31e-5 |
| 600k | 0.96260387 | −3.94e-5 |
| 650k | 0.96260457 | −3.88e-5 |
| 700k | 0.96260541 | **−3.79e-5** |

Score rises monotonically with resolution but the WHOLE submittable band tops at
**0.962605**, ~3.8e-5 short. Extrapolating the trend, clearing 0.9626433 needs
≈1.2–1.6M points — exactly the regime that exceeds the 4.5MB cap (our 1.6M @
0.96272 is 36MB). Moreover the leader's NATIVE 400k (0.96264) beats our transfer at
*every* submittable resolution: cross-resolution transfer loses ~3.8e-5 vs a native
optimization. So the record is unbeatable by every available route — native 400k
saturates at the leader's value, transfer to higher submittable n underperforms it,
and the only thing that exceeds it doesn't fit. Auto-submit correctly never fired.

## Verdict
0.9626433 is the **world frontier**, ahead of published academia, with the true
ceiling open in (0.9626433, 1.0]. Beating it is unsolved mathematics. The campaign's
durable deliverable is the corrected constraint model
(`p3-resolution-is-the-lever-2026-06`) + this literature-frontier map. Further
compute on local/construction methods is the documented anti-pattern.
