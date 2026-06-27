---
type: ablation-protocol
author: hybrid
drafted: 2026-06-26
status: proposed            # pre-registered; not yet run
supersedes: 2026-06-26-knowledge-compounding-preregistration.md   # circle-packing v1 — empirically saturated, see §1
hypothesis: "An agent that logs what it learns each cycle and reuses it on later problems (Warm) closes more of the start→optimum gap than an identical agent whose memory is wiped between problems (Cold), AND its advantage on a given problem grows with the number of lessons already banked when that problem is reached — even after controlling for the problem's difficulty (counterbalanced order)."
family: heilbronn_triangle
model: claude-haiku-4-5
harness: src/einstein/meta_loop/compounding_ablation.py + ablation_runner.py   # reuse arms/run-KB/driver/analysis
relates:
  - 2026-06-26-knowledge-compounding-preregistration.md   # v1 (circle packing) — superseded, kept for the record
  - RUNBOOK-knowledge-compounding.md                       # smoke + calibration evidence
paper_hook: "main.tex §6, §10 — the controlled causal test of the compounding claim."
---

# Pre-registration v2 — Does the accumulation loop compound? (Heilbronn × Haiku)

> **Pre-registration discipline.** Everything marked **[FROZEN]** is fixed *before*
> the first confirmatory run. Changing it after data collection voids the
> pre-registration (new file, new date). Results go in a separate `results-…md`.
> The power pilot (§8) is explicitly *exploratory* and runs *before* freezing S.

---

## 1. Why a v2 (what the v1 run taught us empirically)

v1 (circle packing in the unit square, n=10–15) is **empirically saturated** and
cannot test the loop. Live headless probes (recorded in the runbook):

| set / model | cold gap_closed | meaning |
|---|---|---|
| circle-packing / **Opus** | 1.000 (even n=15) | solved cold |
| circle-packing / **Haiku** | 0.96–1.00 | solved cold |
| **Heilbronn / Haiku** | **n=11 → 0.63, n=16 → 0.20** | **cold genuinely flails** |

Root cause for circle packing: the optimal method (SLSQP-with-radius-as-variable +
multistart) is **recallable from training**, so Cold never flails — the lesson
Warm banks is not knowledge Cold lacks. The binding constraint is *problem
difficulty*, not model strength (Haiku saturates it too), and budget-capping
doesn't help (a ~$0.65 session floor + a step-function time-curve, see runbook).

**Two changes restore a real test, both evidence-backed:**
- **Family → Heilbronn triangle** (max min triangle area): non-smooth, deceptive
  landscape; naive optimization reaches only ~20% of best-known; cold Haiku lands
  mid-range (0.2–0.6) → genuine headroom.
- **Model → Haiku**: keeps headroom *and* is ~2–3× cheaper than Opus, which buys
  the seed count needed for statistical power.

---

## 2. The claim under test (unchanged from v1)

> *Accumulated, reused, human-readable knowledge causally makes the agent better
> across cycles — it compounds — beyond the raw model.*

This is the controlled causal test: same agent, same problems, the **only**
difference is whether lessons persist and are reused.

---

## 3. Independent variable — the two arms  **[FROZEN]**

Identical except the memory loop (enforced by `compounding_ablation.arms_isolated`).

| | **Cold (control)** | **Warm (treatment)** |
|---|---|---|
| Start-of-run KB | empty | empty |
| Read lessons before a problem | ✗ | ✓ (its own, banked earlier in this run) |
| Write a lesson after a problem | ✗ (discarded) | ✓ (persisted) |
| Memory between problems | wiped | carried |
| Base model, tools, compute, cold-init | identical | identical |
| Web search, personas | OFF (both) | OFF (both) |

A "lesson" = ≤1 page (technique/parameterization that worked, dead-ends to skip,
transferable structure). Cold also writes one (to equalize reflection effort) but
it is discarded and never re-read.

---

## 4. Problem family — Heilbronn triangle  **[FROZEN]**

**Objective:** place n points in the unit square [0,1]²; maximize the **minimum
triangle area** over all C(n,3) triples. Maximize (higher = better). Non-smooth
(a min over many terms) — this is *why* it isn't one-shot from training.

**Sequence [FROZEN]:** L = 6 consecutive instances, **n = 11, 12, 13, 14, 15, 16**.
Consecutive n share machinery, so a technique lesson can transfer.

**Reference optima [FROZEN]** — best-known (Erich Friedman packing tables;
*best-known, not proven optimal* — a fixed denominator for gap_closed, which is
fine):

| n | best-known min-area | source |
|---|---|---|
| 11 | 1/27 = 0.0370370 (exact) | Goldberg 1972 |
| 12 | 0.0325… | Comellas–Yebra 2001 |
| 13 | 0.0270… | Karpov 2011 |
| 14 | 0.0243… | Beyleveld 2006 |
| 15 | 0.0211… | Karpov 2011 |
| 16 | 7/341 = 0.0205279 (exact) | Beyleveld 2006 |

(Full-precision decimals for n=12–15 sourced and frozen in `config/` before run 1.)

**Held-out:** these n are scored by a *generic* objective only; no problem-specific
plugin or stored configuration is provided (pre-reg-v1 §4 generic-solvers rule).

---

## 5. The big rigor upgrade — counterbalanced order  **[FROZEN]**

**The v1 flaw:** under a *fixed increasing-n order*, Heilbronn gets harder with n
(cold 0.63→0.20), so "Δ grows with position" (H2) is confounded — Δ could rise
because later problems are harder, not because lessons accumulated.

**Fix:** present the 6 problems in a **different order per seed**, using the **6
cyclic rotations** of the n-ascending order (a Latin square: over any 6 seeds each
problem appears at each position 0…5 exactly once). Seed s uses rotation
`s mod 6`. So each problem is met with **0,1,2,3,4,5 lessons already banked**
across seeds, decoupling *accumulation* from *difficulty*.

This converts H2 from a confounded "Δ vs position" into a clean **within-problem,
across-banked-count** test (§7).

---

## 6. Controls & isolation  **[FROZEN]**

- **Paired cold-init:** for a given (problem, seed) both arms start from the *same*
  random configuration (`cold_init(n, seed)`), so Δ is a paired difference — the
  cold-init noise cancels.
- **Equal context budget:** Warm's banked lessons are capped to a fixed character
  budget (`max_lesson_chars`); both arms get the same max context. Prevents "Warm
  wins via more tokens."
- **Reflection equalized:** Cold writes-then-discards a lesson.
- **Air-gap by construction:** clean-room checkout (no wiki/answers on disk) + tool
  set omits all web/retrieval tools. Independent harness-side triple-verify scores
  the agent's output; a self-reported score is ignored.
- **Manipulation checks (run void if any fail):** Warm KB grows ≥1 lesson/problem
  and is read on later problems; Cold KB provably empty at each problem start;
  air-gap receipt passes. (All enforced by the harness.)

---

## 7. Dependent variable, hypotheses & decision rules  **[FROZEN]**

**Primary DV:** `gap_closed = (final − coldinit) / (ref − coldinit)`, clamped [0,1],
scored locally + triple-verified. **No arena submission.**

**Δ(P,s) = gap_closed(Warm,P,s) − gap_closed(Cold,P,s)** — paired by cold-init.
`banked(P,s)` = number of lessons in the Warm KB when problem P is reached in seed
s (= its position in that seed's order, 0…5).

- **H1 (level — knowledge helps):** mean Δ over all (P,s) > 0.
  *Decision:* supported if the 95% bootstrap CI of mean Δ excludes 0
  (equivalently mean Δ exceeds its standard error by a clear margin).
- **H2 (compounding — it accumulates):** the slope of Δ on `banked`, **with problem
  P as a control** (fixed effect / within-problem), is **positive**.
  *Decision:* supported if the `banked` coefficient's 95% bootstrap CI excludes 0
  and is positive. This is the headline — and because order is counterbalanced, a
  positive slope means *more banked lessons → bigger advantage on the same
  problem*, i.e. genuine accumulation, not difficulty.
- **H1 holds, H2 fails:** knowledge helps but does not compound within the run —
  a level shift, honestly reported (weaker claim).
- **Both fail (Warm ≈ Cold):** the loop earns nothing in this regime. **Pre-committed
  to publishing the null** — no quiet re-runs.

**Secondary (reported, not relied on):** wall-clock / cost per problem (efficiency);
dead-ends-avoided. Noisy on LLM sessions — context, not decision.

---

## 8. Staged execution — small first, then larger  **[FROZEN staging]**

Run in stages so the pipeline is de-risked cheaply before any large spend. The
small stages are **exploratory** (pipeline + manipulation checks + variance); the
**confirmatory** stage has S frozen *before* it starts and its decision rules (§7)
applied **once**. Peeking at the exploratory stages may inform S and GO/NO-GO, but
**not** the H1/H2 verdict — that prevents optional-stopping bias.

- **Stage A — smoke (~$1):** 1 Warm + 1 Cold Heilbronn session on one n. Verifies
  the full pipeline end-to-end: lesson written → banked → read on the next problem,
  harness-side scoring, record schema, crash-resilient resume.
- **Stage B — small exploratory run (~$17):** all 6 problems × 2 arms × **S = 3**
  (3 of the 6 cyclic rotations) = 36 sessions. Purpose: manipulation checks pass at
  scale (Warm reuses lessons), estimate per-cell stdev of gap_closed and rough Δ,
  get a *directional* read. **GO/NO-GO criteria (exploratory, not the hypothesis
  test):** proceed iff (i) manipulation checks pass, (ii) cold gap_closed is
  non-saturated and non-floored (still in ~0.1–0.9), (iii) Δ is directionally ≥ 0.
- **Freeze S** from Stage B's variance: smallest multiple of 6 whose expected 95% CI
  of mean Δ is narrower than the observed Δ — **min S = 6**, **target S = 12**.
  Record the chosen S here, then freeze.
- **Stage C — confirmatory run:** extend to the frozen S (resumable — Stage B's
  seeds count toward S only if S was pre-committed to include them; otherwise
  Stage C uses fresh seeds). Apply §7 decision rules **once** to the confirmatory
  set.

Confirmatory cost: S=6 → 72 sessions ≈ **$33**; S=12 → 144 ≈ **$66**. Sequential,
resumable, run one seed-batch at a time (§9).

---

## 9. Execution (matched to a memory-tight, crash-prone machine)

- **Strictly sequential** — one `claude -p` alive at a time (no concurrency). Run
  from a plain terminal with other apps / Claude sessions closed (frees RAM and
  the shared subscription rate limit).
- **Small batches** — one seed at a time (`--seeds k`); a crash risks only ~6
  sessions.
- **Crash-resilient resume** — per-*cell* resume reusing the on-disk Warm run-KB, so
  a mid-sequence crash continues from the exact problem (falls back to safe
  sequence-restart if KB state ≠ log). Re-running the command is always safe.

---

## 10. Build checklist (to this pre-reg)

Reuse the validated runner/harness; new work only where Heilbronn differs:
1. **Heilbronn evaluator** — `min_triangle_area(centers)` + triple-verify + cold-init
   (mirror `ablation_packing`). Generic objective, no baked method.
2. **Generalize `build_prompt`** — objective text comes from the statement/config
   (drop the circle-packing "common radius" hardcode) → family-agnostic runner.
3. **Config + statements** — the 6 Heilbronn problems + frozen refs (full precision).
4. **Counterbalanced order** — per-seed cyclic-rotation order in the matrix builder;
   record each cell's `position` / `banked` count in the run record.
5. **Crash-resilient per-cell resume** — continue a partial Warm sequence from the
   on-disk KB.
6. **Analysis** — add the H2 within-problem regression (Δ on banked, problem fixed
   effect, bootstrap CIs) to `analyze`/`analyze_ablation.py`.
7. **Power pilot** (§8) → record numbers → freeze S → confirmatory run.

---

## 11. Threats to validity & mitigations

| Threat | Mitigation |
|---|---|
| Difficulty↑ with n confounds H2 | **counterbalanced order** (§5) — the core fix |
| Model memorized Heilbronn optima | best-known configs are irregular/unproven; cold flails (0.2–0.6) confirms not memorized; biases both arms equally anyway |
| Warm wins via more context tokens | fixed lesson-token cap; equal max context |
| Reflection-time confound | Cold reflects then discards |
| No transfer (lessons don't generalize) | consecutive n share method; the banked-count slope tests transfer directly; null is reported, not hidden |
| Stochastic noise mistaken for effect | paired Δ + S≥6 (Latin square) + bootstrap CIs |
| Null quietly re-run until positive | pre-committed to publishing the null; 1:1 logging, no cherry-pick |
| LLM self-reports inflated score | harness-side independent triple-verify; self-report ignored |

---

## 12. Implications

- **H1 + H2** → controlled causal evidence the loop compounds; replaces the paper's
  observational hedge.
- **H1 only** → knowledge helps; "compounds" unproven — soften the claim.
- **Null** → strongest honesty signal; report that the loop didn't pay off in this
  regime. Pre-committed.

*Pre-registered 2026-06-26. Confirmatory results → a separate `results-…md`; do not
edit this document after the first confirmatory run.*
