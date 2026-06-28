---
type: claims-test-matrix
author: hybrid
drafted: 2026-06-27
status: live                 # the master tracker for "prove every JSAgent claim with a controlled test"
paper_hook: "main.tex — every claimed mechanism gets a controlled-evidence row or an honest null"
relates:
  - results-compounding-evidence.md          # the per-result evidence ledger (numbers land there)
  - 2026-06-26-heilbronn-haiku-compounding-preregistration.md   # v2 (claim 4, done)
  - 2026-06-26-cross-family-generalization-preregistration.md   # v3
  - 2026-06-27-longsequence-compounding-preregistration.md      # v4
purpose: "Turn each JSAgent README claim into a falsifiable, pre-registered, controlled test. Track status + result for every one so the paper's claims are EVIDENCE-BACKED, not asserted. Nothing tested gets lost; every result flows to the evidence ledger and the paper."
---

# Mechanism-claims test matrix — prove (or honestly reframe) every JSAgent claim

**Principle (learned from claim 4):** a plausible mechanism may NOT survive a powered controlled
test — the Cold/Warm "memory helps capability" claim went *null* and reframed to *efficiency*.
So every mechanism below gets the same treatment: isolate it (toggle ONE variable), control the
confound, power it, pre-register, apply the decision rule ONCE, and **report the result whatever
it is.** Outcome is either a *controlled-evidence* claim or an *honest reframing* — both strengthen
the paper; only un-tested assertion is weak.

## Status legend
`asserted` (claimed, untested) · `designed` (pre-reg written) · `running` · `DONE✓` (verdict in) · `reframed` (claim changed by data)

## Recording protocol (so nothing is lost, all → paper)
1. Each claim gets a pre-reg (or a §here for cheap code tests) before data.
2. Numbers land in `results-compounding-evidence.md` (or a sibling `results-<claim>.md`).
3. This matrix's **Status / Result / Paper-§** columns are updated the moment a verdict lands.
4. Figures/tables enumerated per claim feed the paper directly.

---

## The matrix

| # | Mechanism (README claim) | Falsifiable claim | Ablation: toggle ONE var | Primary DV | Key confound | Cost | Status | Result |
|---|---|---|---|---|---|---|---|---|
| 1 | **Council of personas** | persona *questions* before optimizing improve outcomes | council-on vs off (solve directly) | gap_closed + time-to-target | **budget-match** (off-arm gets equal tokens) | 💸 LLM | **wired + smoke-clean; full run GATED on cwd-isolation fix** | bugs fixed + re-smoke validated (30c307a): air-gap `passed=True`, personas on-topic (Heilbronn). ⚠️ council-ON gave no-parse (n=1) — watch injection derailing solve. **BLOCKER for the real run: the cross-cell cwd contamination (see below) affects #1 too** — fix per-cell cwd isolation first. |
| 2 | **Adaptive optimizer** (boost recent winners) | adaptive scheduling > fixed/uniform | `select_strategies` adaptive vs uniform/round-robin | score @ fixed budget | isolate scheduling from plugin set | 🟢 code | **DONE✓ NULL** | Tammes n=50, 30 seeds, 8 iters × 2 picks: adaptive **0.391 vs uniform 0.392**, Δ=**−0.0008** CI [−0.010,+0.009], 40% win. Pool sets the ceiling; scheduling doesn't move it. (null in this regime) |
| 3 | **Problem-specific plugins** | each plugin > generic optimizer on its family | plugin vs generic baseline, per family | score / time-to-target | **family must have generic headroom** (NOT saturated) | 🟢 code | **DONE✓ SUPPORTED** | Tammes n=50, 30 seeds: Riemannian plugin **0.499 vs generic 0.285**, Δ=**+0.214** CI [+0.185,+0.242], **100% win**, ~30× faster. Thomson screened out (smooth→no headroom). |
| 4 | **KB cross-problem wisdom** | curated wiki > firewalled web > model-only | 3-arm (Cold/Warm is the 2-arm slice) | gap_closed + efficiency | air-gap, paired, power | 💸 LLM | **DONE✓ (2-arm) / reframed** | capability NULL; **efficiency win** (warm timeout 4.6% vs cold 26.9%) |
| 5 | **AlphaEvolve mutate engine** | mutate-K + strict-improve climbs on *stuck* problems | mutate-engine vs random-restart | Δ over champion @ budget | only on stuck-WITH-headroom problems | 🟡 code-ish | asserted | — |
| 6 | **Trajectory classifier** | labels improving/solved/stuck correctly | accuracy vs ground truth (not A/B) | classification accuracy | label leakage | 🟢 valid. | **DONE (narrow) + BUG (red-team)** | 13 cases 100% (honest), BUT `certificate_of` accepts placeholder strings (`tbd`/`???`) → false SOLVED_AT_FLOOR. Overstated as "SUPPORTED"; bug to fix. `scripts/validate_classifier.py` |
| 7 | **Triple-verify** | catches fake scores / evaluator drift | inject drifted evaluators + bad configs | catch rate | — (real saves: P9/P14/P17) | 🟢 valid. | **DONE (narrow) + BUG (red-team)** | drift catch real (100% >tol, 0% FP). BUT infeasible configs (out-of-square / neg-radius / dup) pass `passed=True`, and no claimed-score check. "catches fake scores" overstated → catches arithmetic drift only. Repo-wide safeguard bug to fix. |
| 8 | **Meta-learning "evolves over time"** | the loop makes the agent measurably better across cycles | = the controlled compounding slices (v2/v3/v4) | gap/efficiency vs cycle | arena trajectory is observational | 💸 LLM | in progress (via 4) | — |

## Strategic order (cheap-deterministic → expensive-LLM → validation)
1. **🟢 #3 plugins, #2 adaptive** — pure optimizer code, no LLM → thousands of seeds, tight CIs, minutes, ~free, most likely to CONFIRM. Do first. (#3 harness skeleton: `scripts/ablation_mechanism.py`.)
2. **🟡 #5 mutate engine** — code-ish; needs stuck-with-headroom problem set.
3. **🟢 #6 classifier, #7 triple-verify** — validation/accuracy framing, cheap; #7 partly writable from existing saves.
4. **💸 #1 council, #4 3-arm KB, #8 system** — LLM-in-loop, expensive, riskiest (claims may not survive). Use the `compounding_ablation` harness; budget S×k seeds each.

## Design rules every test inherits (from claim 4)
- **Headroom screen** — the family/regime must let the *baseline* fail (so there's room to show an effect); a saturated family gives a null for the wrong reason (why circle packing is a bad plugin-ablation target despite being "clean").
- **Budget-match** — any arm that does extra work (council, KB) must be compared at equal total compute, else "it helps" = "more compute."
- **Paired** by seed/cold-init; **pre-register**; **apply the decision rule ONCE**; **power** it (per-cell noise can dwarf the effect — see ledger §2.5); **report nulls** (pre-committed).

---

## Results (paper-ready) — 2026-06-27

So far **3 confirmations + 2 nulls** — exactly the spread that makes the program credible
(not "everything we built works"). Confirmed: specialization (#3), the verification safeguard
(#7), the trajectory classifier (#6). Null: cross-problem memory on *capability* (#4, → efficiency)
+ adaptive scheduling (#2). Pattern emerging: **what the agent KNOWS/uses + its
correctness/measurement scaffolding (plugins, verification, honest status) is what holds;
cleverness in HOW it schedules/remembers is marginal in these regimes.**

**#6 Trajectory classifier — SUPPORTED.** 13 labeled trajectories spanning all four classes plus
the hard cases (certificate precedence, minimize vs maximize, the window boundary where an old
gain must NOT read as improving, empty trajectory): **100% correctly classified**. The classifier
faithfully implements its precedence spec (cert → improving → stuck → unknown). Robustness caveat
for the paper: the gain test is strict with no noise floor (a 1e-12 improvement labels IMPROVING)
— sound for verified best-scores, worth a guard if inputs are noisy. Tool/data:
`scripts/validate_classifier.py`, `results/ablation-mechanism/classifier.json`.

**#2 Adaptive scheduling — NULL.** Tammes n=50, 30 seeds, 8 iters × 2 picks from the 4-strategy
pool (real effectiveness variance: gradient strategies stall on the non-smooth objective,
derivative-free ones work). Adaptive (boost recent winners) **0.391 vs uniform round-robin
0.392**, Δ=−0.0008, CI [−0.010,+0.009], 40% win-rate, ~equal wall. Both plateau ~0.39 (≪ plugin
0.499). *Paper:* the strategy POOL sets the ceiling; bandit-style scheduling over it doesn't move
the result here. Honest null (this regime — larger pools / more iters untested). Data:
`results/ablation-mechanism/adaptive.jsonl`.


**#3 Problem-specific plugins — SUPPORTED.** On Tammes (n=50, sphere; non-smooth min-pairwise-
angle objective with genuine headroom — Thomson screened out as too smooth), a manifold-aware
Riemannian projected-gradient plugin vs the generic flat optimizer, paired by cold-init, 30 seeds:
**plugin 0.499 vs generic 0.285, paired Δ = +0.214, 95% CI [+0.185, +0.242], 100% win-rate, ~30×
faster** (0.07s vs 2.06s). Mechanism: the generic finite-difference optimizer sees ~zero gradient
on the non-smooth objective and stalls at cold-init; the specialized smooth-surrogate + manifold
retraction climbs. *Paper:* clean evidence that specialization beats the generic loop where the
problem structure demands it — and is far cheaper. Data: `results/ablation-mechanism/sphere-plugins.jsonl`.

**#7 Triple-verify — SUPPORTED.** Reproduces the P9/P14/P17 failure mode (a local evaluator
drifting from truth) by injecting drift δ into one of the three independent score paths over 200
configs: **0% false alarms at zero drift, 100% catch for δ above tolerance (≥1e-8), 0% flags below
tolerance** (correctly tolerates numerical noise) — a textbook threshold detector. *Paper:* the
triple-verify safeguard provably catches evaluator drift, not just anecdotally (P9/P14/P17). Tool:
`scripts/validate_triple_verify.py`; data: `results/ablation-mechanism/triple-verify.json`.

**#4 KB compounding — reframed null** (see evidence ledger): capability null, efficiency win.

---

## Red-team audit (2026-06-27) — adversarial attack on #2/#3/#6/#7

An independent adversarial agent re-derived all four from raw JSONL (matched to machine
precision — no recording-layer fabrication) and tried to break each. Outcome:

- **#3 plugins — SURVIVES (HIGH).** Plugin `score` is byte-for-byte the arena objective (diff
  ≤5e-16); a *fair* generic at **700× compute** still loses (Δ +0.18→+0.09, never collapses);
  headroom honest. Caveat: current JSONL = **n=5** seeds (the 30-seed headline data was
  overwritten) → re-run 30 seeds to restore it.
- **#2 adaptive — NULL holds (HIGH), explanation CORRECTED.** `get_strategy_priors("continuous")`
  returns `[]`, so "adaptive" locks onto hillclimb from iter 0 (insertion-order tie-break) — it is
  NOT "learning to favor winners". It *does* schedule strictly better (hillclimb 12/12 vs 3/12),
  yet still ties because hillclimb self-saturates and the other 3 never improve. Null is real; the
  prior docstring/ledger mechanism story ("boosts winners → learns") is wrong — corrected.
- **#6 classifier — OVERSTATED (downgrade to SUPPORTED-narrow + BUG).** 13 cases honest, but
  `certificate_of` (trajectory.py:178) accepts any non-empty string incl. **`tbd`/`???`** →
  false `SOLVED_AT_FLOOR` (the exact frozen≠proven failure it exists to prevent). Real FP vector
  the suite missed. **FIX NEEDED.**
- **#7 triple-verify — OVERSTATED (downgrade + BUG).** Injected-drift catch is real, but
  **infeasible configs pass `passed=True`** — out-of-square / negative-radius / duplicate centers
  (feasibility checks vacuous when r≤0; evaluator.py:104-113); and there's **no claimed-score
  check** (recomputes from centers, so a formula bug shared by all 3 paths, or a "claim 0.9 submit
  0.2" optimizer, isn't caught). Catches arithmetic drift, NOT invalid geometry / fake scores.
  **FIX NEEDED** — this safeguard is repo-wide (arena submissions), so the gap matters beyond this study.

**Net:** the two headline verdicts (#3 SUPPORTED, #2 NULL) survive adversarial attack; #6/#7 were
overstated by me and have real bugs; #2's mechanism explanation was wrong. The audit is doing its job.

---

## Architecture call-map (so the harness work isn't lost) — from the optimizer Explore, 2026-06-27

**Generic optimizer** — `src/einstein/optimizer.py`:
- `class Optimizer(score_fn, direction, category, verify_fn)` (L130/140)
- `run_iteration(solution, strategies=None, seed=None) -> {best_score, best_solution, strategy_results}` (L185). Per-strategy RNG `RandomState(seed + hash(name)%10000)` (L214) → seed-paired.
- `add_strategy(name, fn)` (L163); built-in strategy fns: `_strategy_hillclimb` (L27), `_strategy_nelder_mead` (L62), `_strategy_lbfgsb` (L83), `_strategy_perturbation` (L102). Strategy fn sig: `fn(solution_list, score_fn, rng, is_better) -> (candidate, score)`.
- **Adaptive scheduling (claim 2)** — `select_strategies(max_strategies)` (L167) boosts improved strategies (+3.0, L177) from `knowledge.get_strategy_priors(category)`. Toggle: pass explicit `strategies=[...]` (fixed) vs let it self-select (adaptive); or empty knowledge → uniform.

**Plugins (claim 3):**
- Circle packing SLSQP: `src/einstein/circle_packing_square/polish.py::polish` (L82). ⚠️ circle packing is SATURATED — null for the wrong reason; pick a family with generic headroom.
- Sphere PT-SA / Riemannian: `src/einstein/gpu_tempering/` `run_fused_tempering(vectors, ...)`, `manifolds.py::SphereManifold/FlatManifold` (needs torch/MPS).
- Manifest dispatch: `src/einstein/optimizer_dispatch.py::dispatch(problem_id, strategy)` (L137) + `optimizer_manifest.yaml`.

**Evaluators:** `src/einstein/ablation_packing/families.py::get_family(name)` → `.score`, `.triple_verify` (only `equal_circles_in_unit_square`, `heilbronn_triangle` registered). Per-problem: `src/einstein/{problem}/evaluator.py::evaluate(data)->float` (arena-exact, higher=better).

**Open decision for #3:** pick a (family, plugin) pair with BOTH an existing evaluator AND generic headroom. Circle packing fails the headroom screen. Best candidates: a sphere problem (Thomson/Tammes) with the Riemannian/PT-SA plugin vs generic flat optimizer — needs a sphere family/evaluator wired into the screen. Finalize before running #3 for real.

---

*Maintenance: update Status/Result the moment any verdict lands; push numbers to the evidence ledger; keep the roadmap (`mb/active/compounding-ablation-roadmap.md`) cross-linked.*
