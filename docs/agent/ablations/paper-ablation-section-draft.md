---
type: paper-section-draft
author: agent
drafted: 2026-06-30
status: draft                # for human edit → lift into main.tex §6
confirmed_by:                # set after Jongmin's review
cites:
  - results-compounding-evidence.md
  - mechanism-claims-test-matrix.md
  - 2026-06-27-council-preregistration.md
  - 2026-06-28-prompt-tone-effort-vs-efficiency-preregistration.md
  - config/ablation_transfer_near.yaml
purpose: "Draft of the paper's ablation/limitations section in the agreed shape: fact-first nulls → one principled estimand limitation → case-study existence proofs → named tail-sensitive test. Edit wording, then move into the methodology paper."
---

# §6 — Do the agent's mechanisms work? A pre-registered ablation program

> Drafting note (delete before submission): every number here is verified against
> `results-compounding-evidence.md` and `mechanism-claims-test-matrix.md`. Pilot rows
> (council, prompt-tone) are n=8 and **underpowered** — labelled as such on purpose.
> The section's job is to be the most *trustworthy* part of the paper, not the most
> flattering. Order is deliberate: state the measured fact first, interpret second.

JSAgent is a stack of mechanisms — a persona *council* that writes questions before
solving, a co-evolved *knowledge base* (KB) the agent reads and writes, problem-specific
optimizer *plugins*, a system-prompt *rules* layer, a *triple-verify* guard, and a
*trajectory classifier*. A methodology paper that merely asserts these help is worth
little. We instead subjected each to a **pre-registered, air-gapped, paired controlled
ablation**, scored by the harness (never the agent's self-report), and we report the
results — including the nulls — exactly as the pre-registrations committed us to.

The honest one-line summary is: **one mechanism shows a clean, well-powered effect
(KB → efficiency); one is supported on a headroom family (plugins); the rest are null,
narrow, or underpowered at the scales we could afford.** We argue below that this is a
*finding about where the value lives*, not a negative verdict on the agent — but we make
that argument carefully, and we are explicit about what the data does and does not license.

## 6.1 The scoreboard (measured fact, stated first)

| # | Mechanism | Estimand | Verdict | Key numbers |
|---|---|---|---|---|
| 4 | **KB memory** (Cold vs Warm) | gap-closed; efficiency | **Capability NULL; efficiency SUPPORTED** | quality Δ=+2.9 pts, 95% CI **[−2.3, +8.3]** (S=18, paired). Efficiency: warm times out **4.6% vs 26.9%** (~6×) and runs **~35% faster** (242 s vs 370 s). |
| 3 | **Plugins** (per-family optimizers) | score / time-to-target | **SUPPORTED** | Riemannian vs generic on Tammes n=50: 0.499 vs 0.285, Δ=+0.214, CI [+0.185, +0.242], 100% win, ~30× faster (on a family with genuine headroom). |
| 7 | **Triple-verify** | catch rate | **NARROW + corrected** | catches arithmetic/evaluator **drift** 100% (0 false positives) — but red-teaming found it passes geometrically infeasible configs; "catches fake scores" was overstated and is being fixed. |
| 6 | **Trajectory classifier** | label accuracy | **NARROW + corrected** | 13/13 on honest cases, but red-teaming found placeholder strings yield false "solved"; the "SUPPORTED" claim was walked back. |
| 1 | **Council** (questions-first) | gap-closed @ equal budget | **NULL (pilot, n=8)** | mean Δ=+0.004, 95% CI [−0.11, +0.13]; Heilbronn × Haiku. |
| 8b | **System-prompt** (encouraging vs length-matched neutral) | gap-closed @ fixed budget | **NULL (pilot, n=8)** | mean Δ=+0.035, 95% CI [−0.10, +0.18]. |
| 2 | **Adaptive scheduling** (boost recent winners) | score @ fixed budget | **NULL** | adaptive 0.391 vs uniform 0.392, Δ=−0.0008, CI [−0.010, +0.009]. |
| 4-v3 | **Cross-family transfer**, far (geometry→1-D) | warm−cold solve-rate | **NULL** | Heilbronn→autocorrelation: 0.125 vs 0.125, Δ=0.00. |
| 4-v3 | **Cross-family transfer**, near (geometry→geometry) | warm−cold solve-rate | **NULL by saturation** | Heilbronn→equal-circles (n=28/34, **true Packomania optima**): cold reaches gap 1.00/0.98 *cold*; warm ≈ cold (0.98/0.95). No headroom to transfer into. |
| 5 | **Evolve / mutate engine** | Δ over champion | **not run** | asserted only; future work. |

Five of the ten rows are nulls. We report them because the pre-registrations required it,
and because a paper that hides them is not measuring anything. Two further rows (6, 7)
are cases where our **own red-teaming caught us overstating** a result and we corrected it
in-place — we keep that visible, because the correction is part of the evidence that the
process is honest.

## 6.2 The one clean positive, and what it is *not*

The KB ablation (#4) is the best-powered result in the program (S=18, paired cold-init,
air-gapped clean-room checkout, contamination ruled out by a clean re-run). Its verdict is
specific: **memory did not raise solution quality — the quality CI straddles zero — but it
made the agent substantially more time-efficient, reaching comparable solutions ~35% faster
and exhausting its budget ~6× less often.** Memory's value here is *skipping rediscovery*,
a time-to-solution / sample-efficiency effect, not a higher ceiling. The plugin result (#3)
is the other genuine positive, on a family with confirmed headroom.

We flag one thing the efficiency result is *not*: it is not "the model thinks harder." A
gain that comes only from spending more compute ("pushing to the limit," longer inference)
is the **effort channel** — equivalent to raising the budget — and our fixed-budget design
holds it constant by construction, precisely so an efficiency claim cannot be smuggled in
as effort. The prompt-tone ablation (#8b) was built to test exactly this and found the
expected frontier-model null.

## 6.3 Why so many nulls — one principled limitation, not ten excuses

It would be easy, and dishonest, to explain away each null with a bespoke reason. We make
instead a **single structural argument** that applies across all of them, and we state it
in falsifiable terms.

**The estimand we measured is the body of a heavy-tailed distribution; the value of these
mechanisms, if any, lives in the tail.** Our dependent variable is *mean improvement on
routine cells at a fixed budget*. But progress on hard optimization is not Gaussian — it is
rare, spontaneous, and heavy-tailed: most cells move the score a little, and a small number
of lucky operator/configuration events produce a real jump. A mechanism can leave the
**mean unchanged while fattening the tail** — occasionally enabling a breakthrough that the
mean-over-routine-cells DV is, almost by construction, blind to. With n=8 (council,
prompt-tone) we have essentially no power to see a tail effect even if it is real.

Two corollaries, both honest limitations rather than rescues:

- **Saturation hides transfer (the near-transfer null).** With a capable model (Sonnet),
  the near family is solved *cold* to its true optimum even at n=34 — so there is no gap for
  memory to help close. This is not a reference artifact: we used true Packomania optima
  precisely to rule that out, and warm still ≈ cold. The honest reading is "no headroom to
  measure into on these instances," which is itself a result: *the value of an external
  memory shrinks toward zero as the base model's solo competence rises* — the
  "shipped-model-doesn't-need-the-notes" ceiling.

- **The effect, if present, is an interaction, not a main effect.** model capability ×
  instance difficulty × budget × persistence all matter and interact; a single-cell
  main-effect test at one (model, difficulty, budget) point cannot resolve an effect that
  only appears at a different point in that space. Our pilots sample one corner.

We are deliberate about what this licenses. It licenses "**no detected typical-case
effect**." It does **not** license "the mechanisms work" — the data does not support that,
and we do not claim it. Three independent nulls should, and do, move our prior *down* on
"these reliably help the typical case." What survives is a narrower, open claim: whether
they help in the **rare-event tail** is untested, because we measured the wrong quantity to
see it.

## 6.4 Case-study existence proofs (kept separate, on purpose)

The reason the tail claim is not merely wishful is that the project's own record book
contains the events the controlled DV cannot capture. We present these as **case studies /
existence proofs, explicitly not as controlled evidence**, and we keep them in a separate
bucket so the reader is never asked to mistake an anecdote for an ablation:

- **KB → a verified arena record (P2).** The P2 record (1.5028609 → 1.5028506, a verified
  strict improvement of ≈1.0×10⁻⁵ over a two-agent tie held to 1e-13) came from a single
  warm-memory-derived operator — *data-driven self-pruning* — whose prescription had been
  written, verbatim, into a dead-end finding four days earlier. The agent executed a move
  its memory had already recorded; it did not reinvent it that session.

- **Council → a wall broken (P4).** On the P4 basin wall, ten-plus brute-force optimizer
  variants over hours made no progress; a council re-dispatch then diagnosed the obstruction
  (a discrete incompressible sign topology) and ruled out whole families in minutes,
  redirecting the search that produced the breakthrough.

These are exactly the rare, spontaneous tail events §6.3 describes — and exactly what an
8-cell mean-gap ablation of the *same* mechanisms nulls out on. **The tension between the
controlled nulls and the case-study wins is the central empirical finding of this section,
not a contradiction to be smoothed over.** Memory and the council each demonstrably
contributed to a real record in a specific moment; neither moves the mean on routine cells.

## 6.5 What would settle it (pre-committed)

The honest resolution is not rhetoric but a better experiment, which we pre-specify rather
than run post-hoc:

- **Measure the tail, not the body.** Replace mean-gap with a tail-sensitive estimand:
  P(new personal-best) or **max (not mean)** improvement over many seeds, on a fixed *hard*
  instance with genuine headroom, run to a long budget. A mechanism that fattens the tail
  shows up here and is invisible to the mean.
- **Power the pilots.** Council and prompt-tone at S≈18 (the level at which the KB
  capability effect's CI tightened around zero) before any verdict beyond "no detected
  pilot effect."
- **Pick the regime where headroom exists.** Cross-family transfer needs graded-difficulty
  families with known optima *and* genuine model-failure headroom; on a capable model the
  near family saturates, so the measurement must move to a weaker model or harder instances.

Until those run, our claim is bounded and we state it plainly: **on the controlled,
typical-case evidence we have, only KB-efficiency and plugins clear the bar; the council,
prompt framing, adaptive scheduling, and cross-family transfer show no detected effect at
the scales tested — and whether their demonstrated rare-event value (the P2/P4 records)
generalizes remains an open, named question.** That is the most we can honestly say, and we
prefer it to a stronger claim the data would not carry.
