---
type: paper-section-draft
author: hybrid
drafted: 2026-06-27
status: draft               # for main.tex §6 (controlled evaluation) — lift + edit
sources:
  - mechanism-claims-test-matrix.md          # the test program + per-claim status
  - results-compounding-evidence.md          # claim #4 (KB) full evidence
  - results/ablation-mechanism/*.json[l]     # #2/#3/#6/#7 raw data
purpose: "A ready-to-edit paper section reporting the controlled tests of JSAgent's mechanisms — 3 confirmed, 2 null. Drop into main.tex and tighten."
---

# §6 — Does it actually work? A controlled test of each mechanism

*(Draft for the JSAgent paper. Numbers are from the runs recorded in the evidence ledger
and `results/ablation-mechanism/`. Edit freely.)*

## 6.1 Why this section exists

JSAgent is built from several mechanisms — a persona council, an adaptive optimizer with
problem-specific plugins, a compounding knowledge base, a triple-verification safeguard, and a
self-diagnosing meta-learning loop. It is easy to *assert* that each helps. It is harder, and
more honest, to *test* it. This section reports controlled ablations of those mechanisms. Each
isolates one variable, pairs treatment against control on a shared random start, runs on a
problem regime with genuine headroom, and — where pre-registered — applies its decision rule
once and reports the result whatever it is. The outcome is deliberately mixed: **three
mechanisms survive a powered test, two do not.** We report the nulls as first-class results.

## 6.2 Method

Two tiers. **Pure-code ablations** (optimizer mechanisms) are deterministic and LLM-free, so we
run hundreds of paired seeds and obtain tight bootstrap confidence intervals in seconds.
**LLM-in-loop ablations** (the knowledge loop) launch fresh air-gapped agent sessions and are
expensive and high-variance, so they are pre-registered with a frozen seed count and a single
confirmatory analysis to avoid optional-stopping bias.

Common design across all tests: (i) **one variable** — treatment and control are identical
except the mechanism under test; (ii) **paired** by random seed / cold-start, so shared
start-point noise cancels; (iii) a **headroom screen** — the baseline must be able to fail, or a
null is uninformative (we discard saturated regimes such as circle packing); (iv) **budget
matching** — any arm that does extra work is compared at equal total compute; (v) **honest
nulls** — pre-committed, no quiet re-runs.

## 6.3 Results

| Mechanism | Test | Result |
|---|---|---|
| Problem-specific plugins | Riemannian vs generic optimizer, Tammes n=50, 30 paired seeds | **Confirmed** — Δ=+0.214 [+0.185,+0.242], 100% win, 30× faster |
| Triple-verification | inject evaluator drift, 200 configs | **Confirmed** — 0% false alarm, 100% catch above tolerance |
| Trajectory classifier | 13 labeled trajectories, all classes + edges | **Confirmed** — 100% accuracy |
| Adaptive scheduling | boost-winners vs round-robin, Tammes n=50, 30 seeds | **Null** — Δ=−0.0008 [−0.010,+0.009] |
| Compounding knowledge base | Cold vs Warm, Heilbronn, S=18 (216 sessions, contamination-free re-run) | **Null on capability; efficiency win** |

**Problem-specific plugins help, decisively.** On the Tammes problem (maximize the minimum
pairwise angle of n points on the sphere; non-smooth, so a generic finite-difference optimizer
sees a near-zero gradient and stalls), a manifold-aware Riemannian plugin reaches min-distance
0.499 versus the generic optimizer's 0.285 — a paired gain of +0.214 (95% CI [+0.185, +0.242]),
winning all 30 seeds and running ~30× faster. The smooth Thomson problem was screened out: there
a flat quasi-Newton method matches the Riemannian one (no headroom), and we report that rather
than cherry-picking the favorable family.

**Triple-verification catches what it claims to.** The agent scores every candidate three
independent ways (numpy, mpmath, scipy) and rejects it unless they agree. Injecting a drift δ
into one path — the real failure mode that hid problems P9/P14/P17 — the safeguard flags 100% of
drifts above its tolerance and raises **zero** false alarms at zero drift, with correct
tolerance of sub-threshold numerical noise: a textbook detector.

**The self-diagnosis classifier is correct.** Across 13 labeled trajectories spanning all four
labels (improving / solved-at-floor / stuck / unknown) and the hard cases (certificate
precedence, both optimization directions, the window boundary, empty input), it labels 100%
correctly. One caveat for honesty: its gain test is strict with no noise floor, so on noisy
inputs a negligible improvement would read as "improving."

**Adaptive scheduling does not beat uniform.** Giving the optimizer a bandit that boosts
recently-successful strategies, versus a plain round-robin over the same strategy pool at equal
budget, yields no advantage: 0.391 vs 0.392 (Δ=−0.0008, CI [−0.010, +0.009]), a 40% win-rate.
Both plateau well below the specialized plugin. The *pool* sets the ceiling; cleverness in
*scheduling* over it does not move the result in this regime.

**Cross-problem memory helps efficiency, not capability.** Our largest test (pre-registered, 216
air-gapped sessions) compared an agent that accumulates and reuses human-readable lessons (Warm)
against an identical agent whose memory is wiped between problems (Cold), on the Heilbronn family.
On solution *quality* the loop is null: mean gap-closed advantage **+3.6 points, 95% CI
[−0.7, +7.9]** — the interval includes zero (Warm wins 5 of 6 problems, so the effect is
positive-but-borderline, not clearly absent). But on *efficiency* the loop wins cleanly: the Warm
agent exceeds its time budget **9% of the time versus 26% for Cold (~3× fewer)**, and finishes
~26% faster (255 s vs 344 s). Memory lets the agent skip rediscovery rather than reach a higher
ceiling — an efficiency claim, not a capability claim, and we frame it as such.

This result is **contamination-free**: an initial run was confounded by a cross-cell filesystem
channel (the Cold arm could read earlier cells' scratch, violating its "no memory" guarantee). We
fixed it (per-cell isolated working directories) and re-ran the full S=18. The clean verdict
(+3.6) closely matched the confounded one (+2.9), establishing that the channel was *not* masking a
Warm advantage — the capability null is a property of the loop, not an artifact. (Isolation also
lowered per-cell noise, tightening the interval, which is why the clean effect is borderline rather
than clearly null.)

## 6.4 What the pattern says

Read together, the five tests tell one story: **the mechanisms that encode or check knowledge —
specialized plugins, triple-verification, honest status classification — are the ones that
survive a controlled test, while the mechanisms that add cleverness to *how* the agent schedules
or remembers (an adaptive bandit, a reusable lesson memory) are marginal-to-null on capability.**
Where memory pays off, it pays off as efficiency. This is a more defensible and more interesting
claim than "every component helps," and it points the next round of work at lesson *quality and
retrieval* rather than lesson *accumulation*.

## 6.5 Threats to validity

The pure-code results are single-family (Tammes / Heilbronn) and single-model (Haiku); the
plugin and adaptive findings should be replicated across families before being stated as general
(planned). The null results are "null in the tested regime": adaptive scheduling was tested with
a 4-strategy pool over 8 iterations, and compounding over a banked range of 0–5 — both could
differ at larger scale (a longer-sequence and cross-family pre-registration are designed). The
LLM-in-loop test inherits Haiku's stochasticity (per-cell noise ≈ 4× the effect), which is why it
is powered to S=18 and reported with confidence intervals rather than point estimates.

## 6.6 Figures
1. Plugin vs generic on Tammes — paired per-seed scores (the +0.214 gap). [`sphere-plugins.jsonl`]
2. Triple-verify ROC — catch rate vs injected drift δ. [`triple-verify.json`]
3. Compounding — Cold vs Warm gap-closed (null) beside the efficiency panel (timeout rate +
   wall-clock, the win). [`results-compounding-evidence.md` §2.2/§2.7]
4. The scoreboard table above as the section's anchor figure.
