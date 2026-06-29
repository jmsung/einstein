---
type: results-ledger
author: hybrid
drafted: 2026-06-27
status: live                 # append-only; updated as runs/analyses land
pre_regs:
  - 2026-06-26-heilbronn-haiku-compounding-preregistration.md   # v2 (level + compounding, Heilbronn×Haiku)
  - 2026-06-26-cross-family-generalization-preregistration.md   # v3 (generalization, draft)
paper_hook: "main.tex §6 (controlled compounding test) + §10 (methodology)"
purpose: "Capture every paper-worthy intermediate record so nothing is lost at write-up. The result tables are the deliverable; the intermediate analyses + design rationale are the methodology narrative."
---

# Paper evidence ledger — controlled Cold-vs-Warm compounding test

**This file is for the write-up.** Every entry below is something the paper can cite —
a number, a table, a mechanism, or a design decision with its rationale. Append-only;
do not rewrite past entries (correct via a dated note). Confirmatory verdicts get the
§7 decision rules applied ONCE (see v2 pre-reg) and are marked FINAL.

> Honesty contract (pre-committed): nulls are reported, not hidden. The compounding
> null below is a *result*, not a failure — it ships.

## 0. Claim → evidence status (keep current)

| Claim | Estimand | Evidence | Status (Stage C FINAL, S=18) |
|---|---|---|---|
| **A** Warm > Cold (level) | mean Δ > 0 (H1) | Stage C 216/216 | **NOT supported** — Δ=+2.9 pts, 95% CI **[−2.3, +8.3]** (includes 0). Effect *shrank* with power: +13→+6.5→+2.9 |
| **B** compounds over time | Δ-vs-banked slope > 0 (H2) | Stage C | **null** — slope +0.012, CI [−0.016, +0.042]; long-range shape still needs v4 |
| **C** statistically significant | tight CI excluding 0 | Stage C | **no** — CI includes 0 even at S=18 |
| **D (emergent) Warm is more EFFICIENT** | timeout rate / wall-clock | Stage C telemetry | **SUPPORTED** — cold times out **26.9%** vs warm **4.6%** (~6×); mean wall cold 370s vs warm 242s. The cleanest result. |

---

## 1. Methodology (paper §10) — verbatim-usable design facts

- **Controlled A/B, one variable.** Cold vs Warm identical in base model (claude-haiku-4-5),
  tools, solver code, compute budget, problem statement, cold-init. The ONLY difference:
  Warm reads + persists lessons across the sequence; Cold's memory is wiped between
  problems (and its reflection is written-then-discarded to equalize effort).
- **Air-gap by construction.** Clean-room checkout with the knowledge layer stripped +
  tool set omits all web/retrieval tools → the agent physically cannot reach an answer
  key. Per-cell air-gap receipt logged (§10.7). Manipulation checks void the run on breach.
- **Paired cold-init.** For each (problem, seed) both arms start from the SAME random
  configuration → Δ is a paired difference; cold-init noise cancels between arms.
- **Harness-side scoring.** `gap_closed = (final − coldinit)/(ref − coldinit)`, clamped
  [0,1], recomputed by an independent generic evaluator + triple-verify (A1). The agent's
  self-reported score is ignored — it cannot inflate the DV.
- **Counterbalanced order (Latin square).** Each seed runs the L=6 Heilbronn problems
  (n=11..16) in cyclic rotation `k = seed mod 6`, so each problem is met with 0,1,2,3,4,5
  lessons banked across seeds → decouples *accumulation* from *difficulty*. S=18 = three
  full Latin squares.
- **Family choice rationale (why Heilbronn, not circle packing):** circle packing is
  recallable from training → Cold never flails → no signal. Heilbronn (max min triangle
  area) is non-smooth/deceptive → Cold lands mid-range (0.2–0.6) → genuine headroom.
- **Pre-registration discipline:** design frozen before confirmatory data; decision rules
  applied once; nulls pre-committed to publication.

---

## 2. Results ledger (append-only)

### 2.1 Stage B — exploratory, S=3 (36 cells) — 2026-06-26 — FINAL (exploratory)
Mean gap_closed: **Cold 43.0% · Warm 49.5% · Δ = +6.5 pts**; Warm wins 4/6 problems.

| problem | cold% | warm% | Δ |
|---|---|---|---|
| n11 | 49.1 | 68.8 | +19.8 |
| n12 | 66.2 | 49.6 | −16.6 |
| n13 | 41.1 | 64.5 | +23.4 |
| n14 | 26.1 | 47.7 | +21.7 |
| n15 | 44.2 | 46.5 | +2.4 |
| n16 | 31.7 | 19.9 | −11.8 |

GO/NO-GO: all pass (manipulation OK, cold non-saturated 26–66%, Δ ≥ 0) → GO to Stage C.
**Note for paper:** the effect *halved* from the 2-seed interim (+13.3 → +6.5) as the 3rd
seed landed — a clean illustration of why S=3 is exploratory, not confirmatory.

### 2.2-CLEAN — confirmatory RE-RUN, S=18 (216 cells), isolated cwds — 2026-06-28 — **FINAL (supersedes 2.2)**
After the cross-cell filesystem contamination was fixed (per-cell isolated cwd, commit 457d3eb),
the whole S=18 was re-run clean in `results/ablation-heilbronn-clean`. **The verdict held — the
contamination was NOT the cause of the null:**
- **H1 (capability): NOT supported.** Cold 42.9% · Warm 46.6% · mean Δ = **+3.6 pts**, 95% CI
  **[−0.7, +7.9]** (includes 0, *barely*). Warm wins **5/6**. (Contaminated was Δ+2.9, CI[−2.3,+8.3].)
- **H2 (compounding): NOT supported.** within-problem slope +0.006, CI [−0.022, +0.034].
- **Efficiency (D): SUPPORTED.** cold timeout **26%** vs warm **9%** (~3×); mean wall cold 344s vs warm 255s.
- **Noise dropped** with isolation (pooled per-cell SD 0.158 vs contaminated 0.19) → the clean CI is
  *tighter* and the effect slightly larger (+3.6 vs +2.9), so capability is now **borderline** (lower
  bound −0.7, right at 0) rather than clearly null — but per the pre-reg rule it does not clear 0 → inconclusive.
- **Headline confirmed, contamination-free:** *memory buys efficiency, not capability.* The clean run
  ≈ the contaminated run, so the cross-cell channel wasn't masking a hidden Warm advantage. The bug
  was a real validity fix; it didn't change the science.

### 2.2 Stage C — confirmatory, S=18 (216 cells) — 2026-06-27 — **SUPERSEDED by 2.2-CLEAN (was confounded by cwd contamination)**
Mean gap_closed: **Cold 44.5% · Warm 47.4% · Δ = +2.9 pts**; Warm wins 4/6.

| problem | cold% | warm% | Δ |
|---|---|---|---|
| n11 | 61.1 | 66.5 | +5.4 |
| n12 | 54.2 | 56.3 | +2.2 |
| n13 | 45.4 | 54.4 | +9.1 |
| n14 | 38.6 | 43.7 | +5.1 |
| n15 | 38.4 | 35.9 | −2.5 |
| n16 | 29.3 | 27.7 | −1.6 |

**§7 decision rules applied ONCE (confirmatory):**
- **H1 (level): NOT supported.** mean Δ = +0.029, 95% CI **[−0.023, +0.083]** → includes 0.
- **H2 (compounding): NOT supported.** within-problem Δ-vs-banked slope = +0.012, CI [−0.016, +0.042].
- **Verdict: null** (pre-committed to reporting). Pooled per-cell stdev 0.192.
- **Effect shrank monotonically with power:** +13.3 (2 seeds) → +6.5 (S=3) → **+2.9 (S=18)** — the
  textbook signature of a small/near-zero true effect regressing to truth as power rose. The
  early "warm wins big" was an underpowered illusion.

**Data-quality note (timeouts are valid, not failures):** 34/216 cells hit the 600 s budget
(`ok=false`, `error_kind=timeout`); **32 still produced triple-verified results** (only 2 truly
bad: 1 outside-square, 1 unparseable). Timeout-capped cells are legitimate budgeted results and
are KEPT — the all-cells analysis above is correct. Excluding them would *bias* Δ upward (drops
hard-fought cold cells). The earlier hourly "7 ok=false" counts were a grep-pattern error.

### 2.3 Compounding (H2) — INTERIM, NULL
- Within-problem slope of Δ on lessons-banked = **−0.0043**, 95% CI **[−0.043, +0.038]** → no compounding.
- Raw r(banked, Δ) ≈ **−0.02**. Re-test against banked *chars* (substance, not count): slope ≈ 0, r ≈ −0.004 → still flat.
- Δ by banked level (0→5 lessons): **[+8.2, +4.6, −2.2, +24.5, +3.6, −0.8]** pts — flat/noisy, no monotone rise. (+24.5 at banked=3 is a small-n artifact.)
- **Paper framing:** "H1-maybe, H2-no" — *having* memory gives a small constant lift; *accumulating more* of it does not (yet) help more, over this 0–5 banked range.

### 2.4 Mechanism — why compounding is flat (lesson-quality analysis) — 2026-06-27
- Lessons are NOT near-duplicates: pairwise token Jaccard **0.27**, char SequenceMatcher **0.14**.
- But substance is wildly uneven: lesson length **42–1910 chars** (mean 677, cap 4000); some are throwaway.
- Novel tokens added by each successive lesson (banked 0→5): **[54, 48, 5, 51, 35, 12]** — lumpy, not decaying → "not every lesson helps" (relevance/quality variance), so banked *count* is a poor proxy for *useful* knowledge.
- **Paper value:** this is the constructive finding — the lever is lesson *quality/diversity*, not count; and the dose axis (0–5) is too short to see plateau-vs-climb (motivates v4 long-sequence).

### 2.5 Noise & power — 2026-06-27
- Per-cell within-problem SD ≈ **28–30 pts**; signal/noise per cell ≈ **0.23** (effect is ¼ of one cell's noise). Noise is **seed-dominated** (cold-init lottery + LLM sampling), NOT problem-dominated → problem-fixed-effect control barely helps.
- Power for the level effect (A): S=12 → 51%, S=18 → 68%, S=24 → 80%, S=30 → 88%, S=40 → 95%.
- **k-replicate vs more-seeds:** SE ∝ 1/√(S·k) at cost ∝ S·k → compute-EQUIVALENT for A. k-replicate's distinct value is per-cell precision (for H2 shape + heavy-tail), not a power bargain. (Worth a methods footnote — a subtlety easy to get wrong.)

### 2.6 Heavy-tailed benefit — 2026-06-27
- Warm's advantage is intermittent-large, not steady: per-seed Δ e.g. n14 **[−2, +61, +5]**, n13 **[−10, +55, +25]**; cold per-seed means 55.1 / 35.8 / 40.4.
- **Paper implication:** the mean-Δ test may *understate* a real "occasionally unlocks a much better basin" effect → add a secondary **win-rate / quantile** read, not just the mean.

### 2.7 EFFICIENCY — the emergent clean result (D) — 2026-06-27 — FINAL
On the same S=18 Stage C data, the arms differ sharply in *how hard they have to work*:

| arm | timeout rate | mean wall-clock |
|---|---|---|
| cold | **26.9%** (29/108) | 370 s |
| warm | **4.6%** (5/108) | 242 s |

Cold hits the 600 s budget ~**6× more often** and runs ~**35% longer** on average. Even where the
*final* gap_closed is statistically indistinguishable (A is null), **Warm reaches comparable
solutions far faster and far more reliably within budget.** This is a *time-to-solution /
sample-efficiency* claim — well-controlled (same budget, paired cold-init) and the strongest
signal in the dataset. **Paper framing:** the loop's value here is **efficiency, not capability** —
memory lets the agent skip rediscovery and finish in budget, rather than reaching a higher ceiling.
(Mechanistically consistent with the heavy-tail read §2.6 and the v2 "efficiency-DV" intuition.)

---

## 3. Design decisions + rationale (paper §10 / footnotes)

| Decision | Why | Record |
|---|---|---|
| Heilbronn × Haiku (not circle packing × Opus) | circle packing saturates (cold solves it from training) → no signal; Haiku keeps headroom + buys seed count | v2 §1 |
| Counterbalanced Latin square | fixed increasing-n order confounds "Δ grows with position" with difficulty | v2 §5 |
| Freeze S=18 (raised from 12) | measured within-problem SD ≈28pts → S=12 CI still straddles 0; S=18 clears it | v2 §8 (set pre-verdict) |
| k-replicate option | per-cell denoising for H2 shape + heavy-tail (NOT cheaper than seeds for level) | branch `js/feat/ablation-kreplicate` |
| Long-sequence v4 (planned) | banked range 0–5 too short to show plateau-vs-climb | v4 (to draft) |

---

## 4. Figures / tables the paper needs (with data source)

1. **Cold-vs-Warm gap table** (per-problem + mean) — `results/ablation-heilbronn/runs.jsonl` → `scripts/summarize_ablation.py` → `SUMMARY.md`. (Stage C FINAL.)
2. **Δ-vs-banked scatter + within-problem regression** (the H2 / compounding figure) — `scripts/analyze_ablation.py`.
3. **Power curve** (CI half-width vs S, and S·k equivalence) — power analysis in this ledger §2.5.
4. **Lesson-substance figure** (length distribution + novel-token growth) — §2.4 analysis.
5. **Heavy-tail figure** (per-seed Δ distribution / win-rate) — §2.6.
6. **Design schematic** (air-gap, paired cold-init, Latin square) — §1.

---

## 5. Honest negatives to report (pre-committed)

- **Capability (H1, level) NOT supported** at S=18 — Δ gap_closed CI includes 0; effect shrank
  with power (+13→+6.5→+2.9). Report the null plainly; do not over-claim.
- **Compounding (H2) null** over the 0–5 banked range — reported, not hidden; long-range (v4) open.
- These are strengths, not weaknesses, of a controlled pre-registered design.

---

## 6. Revised paper narrative (post Stage C, 2026-06-27)

The controlled test rewrites the paper's compounding section — to its benefit. The old draft hook
("warm scores higher / compounds") would have rested on an effect that **vanished under power**.
The honest, stronger arc:

1. **Setup.** A pre-registered, air-gapped, paired Cold-vs-Warm A/B on a non-smooth family
   (Heilbronn) where the agent genuinely flails — the one regime that can show a memory effect.
2. **Capability is null (honest negative).** With adequate power (S=18, paired, counterbalanced),
   accumulated human-readable lessons do **not** raise the solution ceiling (Δ gap_closed CI
   [−2.3,+8.3]) and do **not** compound on score. The naïve few-seed signal was an underpowered
   illusion — a cautionary, methodologically valuable result on its own.
3. **Efficiency is the real, clean win.** Same data: warm hits the budget **6× less** (4.6% vs
   26.9% timeout) and solves **~35% faster** (242 s vs 370 s). Memory's value is **skipping
   rediscovery**, not a higher ceiling → a *time-to-solution / sample-efficiency* claim.
4. **Mechanism.** Lessons are uneven (42–1910 chars; "not every lesson helps"); the benefit is
   heavy-tailed (occasionally large). Count is a poor proxy for *useful* knowledge.
5. **Open / future (v3, v4).** Does the efficiency win (a) *compound* over a long sequence and
   plateau (v4, efficiency dose-response), and (b) *generalize* across families (v3, efficiency
   meta-test)? These are now framed around the efficiency DV (`time_to_target`), not gap_closed.

**One-line claim for the abstract:** *"In a controlled, pre-registered test, a reusable lesson
memory did not improve solution quality but made the agent substantially more time-efficient —
it reached comparable solutions ~35% faster and ran out of budget 6× less often."*

Section/figure mapping unchanged from §4, with the **efficiency figure (timeout rate + wall-clock
by arm; later time-to-target survival curve)** promoted to the headline.

---

## v3 — cross-family transfer (does wisdom generalize across problem TYPES?) — 2026-06-29

Pre-reg: `2026-06-26-cross-family-generalization-preregistration.md` (§0b transfer, §0c model factor,
§3 headroom). Harness: the generalized `Family` abstraction + frozen-KB inject + `run_transfer_experiment`
+ `solve_rate_screen` (PR #132 + branch `feat/ablation-v3-llm-runs`).

**Headline: the near-vs-far gradient is NOT cleanly measurable with the wired families — model
capability dominates these small problems — and the one transfer cell we could measure (far) is NULL.**

1. **Model capability dominates difficulty (3-model screen on fixed instances).** Haiku / Sonnet / Opus
   on the same candidates: **Opus saturates everything** (solves all geometric + 1D candidates to the
   reference → no headroom; "the strong model you'd ship doesn't need the notes"). **Sonnet** solves the
   geometric families (Tammes n=12–18, Heilbronn) reliably; only the FAR family `autocorrelation n=32`
   lands in a measurable band. **Haiku** can't do the geometric families. → The **near (geometric packing)
   family is BINARY across models** — solve-or-don't, threshold *between* Haiku and Sonnet; no
   intermediate-difficulty near cell exists at any model. The intended near-vs-far *gradient* is therefore
   unachievable with these 4 families.

2. **The §3 gap-band screen is the wrong instrument here; reframed to SOLVE-RATE.** At a fixed budget the
   outcomes are bimodal (gap ≈ 0 or ≈ 1), so the gap∈[0.2,0.8] band barely exists. Switched the DV to the
   **cold solve-rate across seeds** (matches the post-#4 efficiency pivot): keep instances cold solves
   *some-but-not-all* of the time. Only `autocorr-32` @ Sonnet qualified (screen solve-rate 0.50).

3. **Far transfer = NULL (the one clean measurement).** Heilbronn (source) → `autocorr-32` (far) @ Sonnet,
   8 seeds, paired cold-init, KB_A = 2 Heilbronn lessons (manipulation confirmed — warm read 2 lessons):
   **cold solve-rate 0.125 (1/8) vs warm-transfer 0.125 (1/8) → delta 0.00.** Geometric lessons did not
   help the 1D autoconvolution problem — generic meta-strategy does not cross to a structurally unrelated
   family, exactly the pre-registered prior. *Caveat:* the baseline is noisy (cold 0.125 here vs 0.50 in
   the screen — bimodality × n=8), so this is "no detectable lift on a noisy baseline," not a tight zero.

**Methodological takeaway (the real v3 contribution):** with a small set of self-contained optimization
families, *cross-family transfer at a measurable difficulty is elusive* — model capability swamps the
per-family difficulty knob (binary outcomes; Opus ceilings), leaving only a narrow far@Sonnet cell, which
shows null transfer. To measure a near-vs-far gradient one needs families that are **graded-difficulty for
a fixed model** (the 4 current families aren't) — a wiring/design prerequisite, not just more compute. The
efficiency-DV generalization question (v3's original aim) is answered negatively *for these families*.

---

*Maintenance: append after every run/analysis. Cross-ref the roadmap (`mb/active/compounding-ablation-roadmap.md`) for branch state + next actions.*
