---
type: ablation-protocol
author: hybrid
drafted: 2026-06-27
status: draft               # NOT frozen — sketch for review; freeze §4/§5/§7 before run 1
builds_on: 2026-06-26-heilbronn-haiku-compounding-preregistration.md   # v2 — level + short-range compounding
hypothesis: "Over a LONG problem sequence (banked range 0→L-1, L≈18), the Warm-vs-Cold advantage Δ has a measurable dose-response on accumulated useful knowledge, and its SHAPE (sustained climb vs saturating plateau) is identifiable — provided the lesson context is not the binding constraint."
family: heilbronn_triangle
model: claude-haiku-4-5
harness: src/einstein/meta_loop/compounding_ablation.py + ablation_runner.py + --replicates (js/feat/ablation-kreplicate)
relates:
  - 2026-06-26-heilbronn-haiku-compounding-preregistration.md   # v2: why this is needed (banked maxed at 5)
  - results-compounding-evidence.md                              # the paper ledger this feeds
paper_hook: "main.tex §6 — the dose-response of compounding; the headline 'does it compound, and does it plateau?' figure."
---

# Pre-registration v4 (DRAFT) — Does compounding have a dose-response, and does it plateau?

> **What this adds over v2.** v2 tested the *level* (H1) cleanly and found compounding
> (H2) **flat** — but over a banked range of only **0–5** (L=6 sequence). A flat slope on
> 0–5 cannot distinguish "no compounding" from "compounding we didn't give room to show."
> v4 extends the sequence to **L≈18** so banked climbs **0→17**, turning H2 from a yes/no
> into a *shape*: linear climb, saturating plateau, or genuinely flat. It reuses v2's
> controls verbatim and adds the long-sequence machinery + the context-cap fix below.

---

## 0. REVISED FRAMING — efficiency, not capability (post Stage C, 2026-06-27)

**Stage C (S=18) changed what v4 should measure.** The *capability* claim is dead at this
power: mean Δ(gap_closed) = +2.9 pts, 95% CI [−2.3, +8.3] (null); compounding slope null. But a
clean **efficiency** result emerged: cold timed out **26.9%** vs warm **4.6%** (~6×), mean wall
370 s vs 242 s. Warm reaches *comparable* solutions **faster and within budget far more often** —
the loop's value is efficiency, not a higher ceiling (evidence ledger §2.7).

**So v4's primary DV pivots from gap_closed to time-to-solution.** The compounding question
becomes: **does the agent get FASTER as it banks more knowledge, and does that speed-up plateau?**

- **Primary DV (v4):** `time_to_target` — wall-clock (or token cost) to first reach a fixed
  gap_closed target τ (e.g. τ = the cold median gap for that n), right-censored at the 600 s
  budget; plus the binary **within-budget success** and **timeout rate**. gap_closed becomes a
  *secondary/quality* DV (must not be *worse* for warm — a non-inferiority check).
- **H2-eff (the real test):** within-problem slope of (cold − warm) `time_to_target` on banked > 0
  (warm's time advantage grows with banked knowledge), and its **shape** (sustained vs plateau).
- **Build addition:** the harness currently logs only (coldinit, final) + total wall. v4 needs a
  **timestamped best-so-far trajectory** per cell so time-to-target is computable (survival
  analysis: Cox / Kaplan–Meier on time-to-τ, banked as covariate, problem stratum). This replaces
  the gap-centric §7 below as primary; gap H1/H2 are retained as secondary.
- Everything else (L≈18 long sequence, context-cap control §6, randomized order §5, k-replicate)
  carries over unchanged — they serve the efficiency dose-response just as well.

The rest of this doc is written gap-first (pre-Stage-C); read §7's H-set as **secondary** now,
with the efficiency H2-eff above as the headline. Freeze the DV choice before run 1.

---

## 1. Why v4 (the specific gap v2 left)

From the v2 evidence (`results-compounding-evidence.md` §2.3–2.4):
- within-problem slope of Δ on banked = **−0.004, CI [−0.043, +0.038]** (flat) over banked 0–5;
- lessons are uneven in substance (42–1910 chars), so *count* is a poor knowledge proxy.

Two things v2 structurally **could not** answer, both addressed here:
1. **Range.** Does Δ rise then plateau (diminishing returns) or keep climbing? Unanswerable on 0–5.
2. **Context confound.** At ~677 chars/lesson and a 4000-char cap, Warm's context **saturates
   by ~6 lessons** — beyond that, extra banked lessons add *no context*, so any flatness is a
   **cap artifact**, not a property of the loop. v2 never reached this regime; v4 lives in it
   and must neutralize it (see §6).

---

## 2. The claim under test

> *Accumulated useful knowledge has a dose-response on the Warm advantage: Δ increases with
> banked knowledge, and the curve's shape (sustained vs saturating) is identifiable — once
> context is not the binding constraint.*

This is strictly the **compounding** claim (B), at the dose resolution v2 lacked. Level (A) is
re-estimated as a by-product but is not the focus.

---

## 3. Independent variable — the two arms  **[FROZEN by reference to v2 §3]**

Identical to v2: Cold (memory wiped between problems, reflection discarded) vs Warm (lessons
persist + are read). One variable: the memory loop. Air-gap, equal compute, web/personas OFF
for both.

---

## 4. Problem sequence — long Heilbronn  **[FREEZE before run 1]**

- **L ≈ 18 consecutive Heilbronn instances** (target **n = 8…25**), so a technique lesson can
  transfer across the whole run and banked spans **0…L−1**.
- **Reference optima [FREEZE]:** best-known min-triangle-area for every n in the range, sourced
  + frozen in `config/` before run 1 (Goldberg / Yang / Cantrell / Friedman tables). **Build
  risk:** reliable best-known thins out above n≈16–20. **Decision rule:** set L to the longest
  *contiguous* n-range with trustworthy best-known values (so gap_closed's denominator is
  sound); if that is < 15, drop the high end rather than use shaky optima. Record the final
  range here before freezing.
- **Held-out / generic** objective only — no problem-specific plugin or stored configuration
  (v2 §4 generic-solvers rule). Cold flailing (mid-range gap_closed) confirms non-memorization.

---

## 5. Order design — randomized permutations, NOT a full Latin square  **[FREEZE]**

A full L×L Latin square (each problem at each position) needs S = multiple of 18 → prohibitive.
Instead: **each seed runs a fresh random permutation** of the L problems (seeded by `seed`, so
it is deterministic + reproducible, shared across arms). Over S seeds each problem visits a
*spread* of banked positions and each position is visited by a *spread* of problems.

**Why this is still clean for the dose-response:** the estimand is the **within-problem** slope
of Δ on banked (problem as a fixed effect). Randomized order makes banked position *independent
of problem difficulty* (a problem at banked=17 is a random problem, not the hardest), and the
fixed effect removes per-problem difficulty entirely. Counterbalancing-by-randomization is more
sample-efficient than a Latin square for estimating a slope/curve and avoids the S=18 blow-up.
(Trade-off recorded: it gives a *balanced-in-expectation* design, not the exact balance of a
Latin square — fine for a regression, and bootstrap CIs absorb the residual imbalance.)

---

## 6. THE key control — context must not be the binding constraint  **[FROZEN]**

Without this, v4 measures the context cap, not compounding.

- **Scale the lesson budget with L.** Set `--max-lesson-chars` high enough to fit **all L
  banked lessons** at the observed ~700-char mean (≥ ~15–18k chars), so at banked=k Warm can
  actually *read* all k lessons. Held EQUAL across arms (Cold's is still empty) → the equal-max-
  context control (v2 §6) is preserved; only the ceiling moves.
- **Cap-as-a-factor (secondary, optional):** run a small capped vs uncapped contrast. **If
  raising the cap un-flattens the slope, the binding lever is context/retrieval, not the loop**
  — itself a publishable finding. If the slope is flat even uncapped, that is true non-compounding.
- **Dose on *useful* knowledge, not just count (per v2 §2.4):** record, per cell, both
  `banked` (count) and **`banked_substance`** = cumulative chars / novel-tokens of the lessons
  actually in context. Primary H2 is tested against *both* x-axes.
- **k-replicate (`--replicates 2`):** per-cell denoising so the *curve* is estimable, not just
  the grand mean. (Reminder from the evidence ledger: k-replicate is compute-equivalent to more
  seeds for the *level* test; its value here is per-cell precision for the *shape*.)

---

## 7. Dependent variable, hypotheses & decision rules  **[FROZEN]**

**Primary DV:** `gap_closed` (v2 §8), harness triple-verified. **Δ(P,s) = warm − cold**, paired
by cold-init. `banked(P,s)` and `banked_substance(P,s)` per §6.

- **H2a (a slope exists):** within-problem slope of Δ on banked > 0.
  *Decision:* supported if the slope's 95% bootstrap CI excludes 0 (positive). Tested against
  **both** banked-count and banked-substance; report both.
- **H2b (the shape):** fit and compare **flat vs linear vs saturating** (log / Michaelis–Menten)
  models for Δ(banked), within-problem, by bootstrap/AIC.
  *Report:* the best-fit shape and, if saturating, the **plateau point** ("knowledge half-life"
  — banked level at which 50%/90% of the asymptotic Δ is reached). This is the headline figure.
- **H2-null (pre-committed):** if the slope CI includes 0 **even with the cap raised (§6)**,
  that is *true* non-compounding over a long range — the strongest possible null, reported, not
  hidden. If flat only when capped, report it as a **context-bound**, not a loop property.
- **Secondary:** level Δ (A) re-estimated; win-rate / heavy-tail read (evidence ledger §2.6).

---

## 8. Staged execution  **[FROZEN staging]**

- **Stage A — smoke (~$2):** 1 Warm + 1 Cold long sequence on a short L (e.g. 4) — verifies the
  long-run KB threading, the raised context budget actually delivers all lessons, randomized
  order + per-cell resume, k-replicate aggregation.
- **Stage B — exploratory (~$40):** L≈18 × 2 arms × **S=4** × **k=1**. Manipulation checks at
  scale; estimate the slope's variance and a directional shape; confirm the raised cap is fitting
  all lessons. GO/NO-GO: manipulation OK, cold non-saturated, *some* banked-position spread achieved.
- **Freeze S, k** from Stage B's slope variance (record here). Provisional target: **S=12, k=2**
  (≈ 18×2×12×2 = 864 sessions ≈ $400) — trim to k=1 (≈$200) if the level isn't the focus and the
  slope variance permits.
- **Stage C — confirmatory:** apply §7 rules ONCE to the frozen (S, k).

Cost is real — this is the most expensive of the three pre-regs. Sequence-length L drives it
linearly; consider L=12–15 if best-known optima or budget force it (still ≫ the v2 range of 5).

---

## 9. Execution & resume

Reuse v2 §9 verbatim: strictly sequential, one `claude -p` at a time, small seed-batches,
crash-resilient per-cell resume reusing the on-disk Warm run-KB. Re-running the command is safe.
Longer sequences mean a crash risks more per (arm, seed) cell → run one seed at a time.

---

## 10. Build checklist (delta over v2's validated harness)

1. **Extended optima config** — frozen best-known for the chosen contiguous n-range (the §4 risk).
2. **Randomized-order generator** — deterministic per-seed permutation (replaces/augments
   `cyclic_order`); record each cell's `banked` + `banked_substance`.
3. **Raised `--max-lesson-chars`** to fit all L lessons; record actual chars-in-context per cell.
4. **`banked_substance`** recorded in the run record (cumulative chars / novel tokens in context).
5. **H2-shape analysis** — flat/linear/saturating model comparison + plateau-point estimate +
   bootstrap CIs; dual x-axis (count + substance); added to `analyze_ablation.py`.
6. **k-replicate** — already built (`js/feat/ablation-kreplicate`); merge first.

---

## 11. Threats to validity & mitigations

| Threat | Mitigation |
|---|---|
| Context cap saturates the dose (flat = artifact) | **§6** — raise the budget to fit all L lessons; cap-as-a-factor contrast |
| Difficulty↑ with n confounds banked | randomized order (§5) + within-problem fixed effect |
| High-n best-known optima unreliable → bad denominator | §4 decision rule: shrink L to trustworthy contiguous range |
| Lesson dilution ("needle in haystack" as context grows) | record banked_substance; flag if Δ tracks *recent* lessons not *all* — points to retrieval (future v5) |
| Slope buried in seed noise | k-replicate per-cell denoising + bootstrap CIs + adequate S |
| Cost blow-up | staged; L and k are the cost dials; trim before confirmatory |
| Null quietly re-run | pre-committed null reporting; 1:1 logging; decision rules applied once |

---

## 12. Implications

- **Positive slope + identifiable shape** → the headline: compounding is real and we can state
  whether it saturates (and where) — replaces the v2 "flat over 0–5" with a real dose-response.
- **Flat even uncapped** → strong, honest null: the loop does not compound even given range and
  context — a genuine limit of read-all-lessons memory, motivating retrieval/curation (v5).
- **Flat only when capped** → the bottleneck is *context/retrieval*, not the loop — redirects the
  whole research program toward lesson selection, not lesson accumulation.

*DRAFT pre-registration 2026-06-27. Freeze §4 (range+optima), §5 (order), §6 (budget), §7 before
the first confirmatory run. Results → `results-compounding-evidence.md` + a `results-v4-…md`.*
