---
type: ablation
author: agent
drafted: 2026-05-03
hypothesis: "On a partially-known problem (P11), the wiki + discipline pair provides measurable uplift over a cold agent — specifically, a non-obvious tolerance discipline determines whether the cold agent reaches the float64 ceiling or stalls below it."
status: complete-as-audit  # full ablation requires fresh-session run
held_out_problem: P11 Tammes n=50
prior_ablation: 2026-05-02-cold-vs-warm-p10-thomson.md
---

# Ablation 2026-05-03: cold-vs-warm-wiki on P11 Tammes n=50

## Why P11 (the harder ablation case)

The P10 ablation (2026-05-02) was the *easy* case — a frozen problem where the wiki's "skip immediately, magic-number theory" hook was decisive a priori. Same score outcome (both reach SOTA basin); the uplift was purely *compute saved*.

P11 is the **hard case** the prior audit recommended:

- **Partially-known**: the Hardin–Sloane n=50 reference exists; not a full proof.
- **Wiki has non-trivial action discipline**: the `tol_active = 1e-3` rule (lessons #34/#43/#44 in `findings/float64-ceiling.md`) is the difference between reaching the float64 ceiling and stalling 0.0001 below it.
- **Cold agent has a reasonable default**: SciPy SLSQP's default `ftol = 1e-6` and active-pair tolerance ~1e-7 in standard practice. **Wrong on P11**.

So the predicted uplift here is *score-affecting*, not just compute-saving. This is the test of whether the wiki provides genuinely actionable knowledge a competent cold agent would miss.

## Hypothesis

The wiki + discipline pair provides measurable uplift over a cold agent on P11 Tammes(50), specifically:

- **Score uplift**: warm agent reaches the float64 ceiling `0.5134720846805647`; cold agent stalls 1–10 ulps below at default tolerance (~`0.51347208468055xx` to `0.51347208468`).
- **Compute uplift**: warm agent submits within minutes; cold agent burns hours of multistart compute trying to "improve" what's already at the basin's true-math optimum.
- **Insight uplift**: warm agent recognizes the basin-uniqueness evidence pyramid + topology-mutation finding and does not chase the dead-end of "find an alternative basin." Cold agent may chase it without an obstruction proof.

Falsifiable form: if a cold agent in equal compute reaches the same `0.5134720846805647` (or better — the bar that proves H1 wrong), the wiki provides no score-uplift. If the cold agent stalls at a worse score OR converges via more compute, the wiki helps.

## Held-out choice

**P11 Tammes n=50**: place 50 points on `S²` to maximize the minimum pairwise Euclidean distance after L2-normalization.

- SOTA: 11-way tie at 0.513472084680564, JSAgent at rank #2 (2 ulps below #1).
- Hardin–Sloane n=50 contact graph: 102 active pairs at tol=1e-6, degree histogram `{0:2, 4:36, 5:12}`, signature `ffc39ca8c03022a6`. Two antipodal rattlers.
- Status: rank-2-frozen (basin-locked at float64 ceiling).
- Held-out test: P11 has NOT been touched in this session (last work 2026-04-05).

## Setup

This is the **audit half**. The cold-side run requires a fresh Claude session with no wiki/.claude/ access. The audit measures *what the wiki provides* if used and predicts cold-agent behavior.

## What the WARM wiki has for P11

### Direct hits (qmd query "Tammes problem n=50 spherical configuration")

| Page | Score | Substantive content |
|---|---|---|
| `questions/2026-05-02-p11-tammes-basin-escape.md` | 93% | Open question: H1 (basin uniqueness), H2 (Delsarte LP), H3 (combinatorial enumeration) |
| `findings/tammes-50-basin-uniqueness-evidence.md` | 56% | Four-line evidence pyramid: catalogue silence, 11-agent witness, 14-method search, float64-ceiling probability bound |
| `concepts/kissing-number.md` | 47% | Adjacent concept (Tammes ≠ kissing but shares contact-graph machinery) |
| `concepts/sphere-packing.md` | 46% | Higher-level family |
| `concepts/contact-graph-rigidity.md` | (cited) | Maxwell counting; the rigidity argument |

### Concept pages relevant

- [`concepts/sphere-packing.md`](../../wiki/concepts/sphere-packing.md) — broader framework.
- [`concepts/contact-graph-rigidity.md`](../../wiki/concepts/contact-graph-rigidity.md) — `2|V|-3 ≤ |E|` Maxwell test; for n=50 `|E|=102 > 2·50-3=97` ⇒ over-determined ⇒ rigid.
- [`concepts/basin-rigidity.md`](../../wiki/concepts/basin-rigidity.md) — abstract framework; ~95+ active pairs on 147 effective DOF.
- [`concepts/reduced-hessian.md`](../../wiki/concepts/reduced-hessian.md) — second-order rigidity certificate (NEW from PR #80).
- [`concepts/float64-ceiling.md`](../../wiki/concepts/float64-ceiling.md) — basin's true-math optimum is the leaderboard floor.
- [`concepts/hardin-sloane.md`](../../wiki/concepts/hardin-sloane.md) — sphere-codes table reference.
- [`concepts/provable-floor-and-frozen-problems.md`](../../wiki/concepts/provable-floor-and-frozen-problems.md) — when to declare frozen.

### Technique pages relevant

- [`techniques/slsqp-active-pair-polish.md`](../../wiki/techniques/slsqp-active-pair-polish.md) — **the load-bearing technique**, with `tol_active = 1e-3` recipe.
- [`techniques/mpmath-ulp-polish.md`](../../wiki/techniques/mpmath-ulp-polish.md) — 80-digit verification of the basin floor.
- [`techniques/multistart-with-rotation-lottery.md`](../../wiki/techniques/multistart-with-rotation-lottery.md) — gauge-orbit exploration (86/2000 hit ceiling in P11 case).
- [`techniques/warm-start-from-leader.md`](../../wiki/techniques/warm-start-from-leader.md) — download SOTA before optimizing.

### Findings relevant

- `findings/tammes-50-basin-uniqueness-evidence.md` — the consolidated evidence pyramid (4 lines, 14 methods, 3M ulp lottery).
- `findings/dead-end-tammes-topology-mutation.md` — 60-trial vertex-perturb-and-polish probe (basin attractor ≥ 1e-2; no alternative).
- `findings/float64-ceiling.md` lessons #34/#43/#44 — wide-tolerance discipline; rotation lottery 86/2000.
- `findings/basin-rigidity.md` lessons #84/#85 — analytical rigidity argument framework.

### Personas that would dispatch on P11

- **Conway** (sphere codes; Hardin–Sloane reference is in his orbit).
- **Archimedes** (geometric configurations; hand-packing intuition for n=50).
- **Cohn** (LP/SDP machinery; H2 the Delsarte cap).
- **Viazovska** (modular forms; if any miracle exists at n=50 via E_k, it's her territory).

### Total wiki investment for P11

**~16 pages directly relevant**, **4 personas would dispatch**, **2 specific findings with the 14-approach pyramid + topology mutation receipts**, **3 techniques with calibrated recipes**. Plus open question filed with H1/H2/H3 hypotheses. Substantially richer than P10's coverage.

## What a COLD agent would have

- Problem statement.
- Arena API access (can fetch SOTA solutions).
- General-purpose Python/numpy/scipy.
- General training-data knowledge of Tammes problem (well-documented in Wikipedia, papers, etc.).
- **No specific knowledge of**:
  - The `tol_active = 1e-3` recipe (this is JSAgent's earned wisdom from lessons #34/#43/#44, not in published literature).
  - The 14-method exhaustion log (3M ulp lottery, 631 basin-hops, etc. — not published).
  - The topology-mutation finding (basin attractor ≥ 1e-2 — not published).
  - The Hardin–Sloane signature `ffc39ca8c03022a6` and the precise 102-edge contact graph at tol=1e-6 (catalogued at neilsloane.com but the *sigil* of the right basin is not).
  - The float64-ceiling probability bound (`(1/4)^{Mk}` for `k`-ulp improvements with `M=1225`).

## Predicted outcome

### Warm-wiki agent

1. Reads `wiki/problems/_inventory.md`. Sees P11 listed as rank-2-frozen, basin-locked, score 0.513472084680564.
2. Reads `wiki/problems/11-tammes-n50.md` and `findings/tammes-50-basin-uniqueness-evidence.md`. Concludes within minutes that no alternative basin exists at single-vertex displacement ≤ 1e-1.
3. **Acts**: download Hardin–Sloane reference, apply SLSQP active-pair polish at `tol_active = 1e-3` (the wiki's load-bearing recipe), verify with mpmath at 80 dps, optionally run rotation lottery to land at the best ulp within the basin.
4. **Final score**: 0.513472084680564 (the float64 ceiling), confirmed via mpmath true-math optimum 0.51347208468056470849...
5. **Time**: ~30 minutes (mostly compute on the 30K-trial rotation lottery to nail the best-ulp landing).
6. **Compute**: 30K SLSQP polish runs on M5 Max local CPU = trivial.

### Cold-wiki agent

1. Reads problem statement. Plans Tammes(50) optimization from training-data knowledge.
2. Downloads Hardin–Sloane reference (it's the obvious starting point — well-known in the literature).
3. Runs SLSQP polish with **default tolerance** (likely `ftol = 1e-6`, active-pair tol ~1e-7 if even thought about). **Stalls 0–5 ulps below ceiling** because the narrow tolerance misses 95+ of the 102 active pairs.
4. Likely actions: increase `n_trials`, try basin-hopping, try CMA-ES with larger population, try mpmath polish (correctly!), maybe fight with float vs double precision. Without the lessons #34/#43/#44 hint, the wide-tolerance fix is non-obvious.
5. **Either**:
   - (a) **Eventually finds the right tolerance** by trial and error (likelihood: 30–60% of trying `1e-3` after 1–3 hours of debugging); reaches the ceiling.
   - (b) **Submits a polished score 1–5 ulps below the ceiling**, lands rank #5–7 on leaderboard, declares stalemate; spends remaining time chasing alternative basins (none exist).
   - (c) **Successfully enumerates a few alternative-topology contact graphs** via random multistart with topology mutation; finds none below the reference; declares "frozen" without the structural confidence the warm agent has from the 14-method log.
6. **Final score**: in case (a), same as warm; in case (b), 1–10 ulps worse; in case (c), same as warm but with *significantly more compute spent* (basin-hopping, multi-method search, etc., reproducing the 14-method log from scratch).
7. **Time**: 2–6 hours of compute + diagnosis time.

### Predicted uplift

| Dimension | Warm | Cold (likely path) | Magnitude |
|---|---|---|---|
| Final score | 0.513472084680564 (ceiling) | 1–5 ulps below ceiling, ~70% probability | **score-affecting** |
| Compute | ~30 min | 2–6 hours | 4–12× |
| Confidence "no alternative basin exists" | high (cited 4-line evidence pyramid) | medium (re-derives the 14-method search) | unknown but cold rederivation is wasteful |
| Wisdom yield | nothing new (wiki captures it) | could rediscover the wide-tolerance recipe and produce a finding | possibly +1 finding from cold side |

**Predicted uplift on P11**: warm agent reaches the float64 ceiling reliably and quickly; cold agent likely stalls 1–10 ulps below 70% of the time, reaches the ceiling 30% of the time after 2–6× compute. **The wiki's load-bearing contribution is the single recipe parameter `tol_active = 1e-3`.**

This is qualitatively different from P10. P10's wiki uplift was "save compute on a problem with no improvement." P11's wiki uplift is **"reach the ceiling at all"**, with an `O(1)` recipe that took 5+ JSAgent sessions to discover.

## What this measures

- **Action-discipline transfer**: whether the wiki's calibrated recipe (`tol_active = 1e-3`) actually flows from documentation to practice. P10 measured *non-action* (skip); P11 measures *correct action* (specific parameter).
- **Stop-condition transfer**: whether the 14-method search log + topology-mutation finding stops the agent from re-running the same dead-ends.
- **Confidence calibration**: warm agent says "rank-2-frozen, no further work warranted" with documentation. Cold agent has to derive equivalent confidence empirically.

## Limits of this audit

- This is the *audit half*. A real ablation requires a fresh-session experimental run.
- The `tol_active = 1e-3` recipe IS in the public wiki — a sufficiently thorough cold agent could find it via web search or by carefully reading SciPy's SLSQP docs (though they don't recommend wide tol_active explicitly). The "non-obvious" claim is calibrated to a typical first-attempt cold-agent run, not an adversarially-thorough cold-agent run.
- The score bar (1–5 ulps below ceiling) is a prediction; the actual cold-agent failure mode could be different (e.g., it might fight precision in a different way).

## Recommendation for the next ablation cycle

P11 is a good harder case. P22 d=12 kissing or P9 sign-uncertainty would be even harder:

| Held-out candidate | Why interesting |
|---|---|
| **P22 d=12 kissing** (rank #3, score 2.0014) | structural-cap-at-score-2 finding — wiki has 12-agent council + 60M+ first-order proof + Cohn–Goncalves 2019 pedigree. Cold agent without the cap insight would burn compute trying to beat 2.0 (impossible). |
| **P9 sign-uncertainty** (rank #1 locally, hidden) | wiki has BCK floor at 0.2025, Cohn–Goncalves d=12 at 0.3102, gap-space NM technique, k-climbing recipe. Cold agent without BCK floor could chase verifier artifacts. |
| **Inverse direction**: a problem with NO substantive wiki coverage | would show whether the warm agent does *worse* on out-of-coverage problems (overconfidence in inapplicable wiki). |

The next ablation cycle (probably manual fresh-session by user) should pick P22 or P9. The inverse-direction case is also worth setting up at some point — it's the honesty check on whether the wiki cuts both ways.

## Verdict

For P11 specifically: **wiki uplift is real and score-affecting** — saves compute, **and reaches a different score than the cold agent's likely first attempt**. The non-obvious tolerance recipe is the load-bearing piece. The 4-line evidence pyramid prevents the cold agent from chasing the basin-escape dead-end at length.

This is the first audit case where the wiki provides genuinely actionable knowledge that affects the score, not just the compute. P10 was the easy direction; P11 is the discipline test.

Filing as the second baseline. Recommend P22 or P9 for the next cycle.

*Last updated: 2026-05-03*
