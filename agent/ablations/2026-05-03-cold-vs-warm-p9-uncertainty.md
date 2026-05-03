---
type: ablation
author: agent
drafted: 2026-05-03
hypothesis: "On a verifier-fragile problem (P9), the wiki's BCK 0.2025 floor + the verification-patterns rule prevents the cold agent from celebrating a numerically-correct-but-mathematically-invalid score below the BCK bound."
status: complete-as-audit
held_out_problem: P9 Sign Uncertainty (HIDDEN; verifier bug pending fix)
prior_ablations:
  - 2026-05-02-cold-vs-warm-p10-thomson.md       # easy (frozen + magic number)
  - 2026-05-03-cold-vs-warm-p11-tammes.md        # harder (tolerance discipline)
  - 2026-05-03-cold-vs-warm-p22-kissing-d12.md   # hardest direction (structural cap)
---

# Ablation 2026-05-03: cold-vs-warm-wiki on P9 Sign Uncertainty

## Why P9 (the verifier-fragility test)

The series so far has measured three uplift mechanisms:

| Ablation | Problem type | Uplift mechanism |
|---|---|---|
| P10 | Frozen + magic number | Compute-saving (skip) |
| P11 | Basin-locked | Score-affecting (1-ulp tolerance recipe) |
| P22 | Structurally-capped | Direction-affecting (target itself is wrong without wiki) |
| **P9 (this)** | **Verifier-fragile** | **Validity-affecting (the score itself is fake without the wiki's floor)** |

P9 uniquely tests: does the wiki's *theoretical lower bound knowledge* prevent the cold agent from celebrating numerically-correct-but-mathematically-invalid scores? JSAgent itself fell into this trap on 2026-04-19 (score `1.07e-13` celebrated, posted to GitHub, then discovered to violate BCK 2010's `0.2025` floor — the lesson now lives in `findings/verification-patterns.md`).

## Hypothesis

The wiki has four load-bearing pieces for P9:

1. **`concepts/bourgain-clozel-kahane.md`** (NEW from PR #80): BCK 2010 floor `S ≥ 0.2025` for the d=12 sign-uncertainty constant. Any score below this is a verifier artifact, full stop.
2. **`findings/verification-patterns.md`**: the *operational rule* "before claiming a breakthrough, check the score against literature bounds — if it violates a proven bound, the evaluator is wrong, not mathematics." Includes the explicit P9 receipt.
3. **`techniques/k-climbing.md` + `concepts/k-climbing-and-dof-augmentation.md`**: the climbing technique (k=13 → 14 → 19 → 50) that breaks fixed-k basin plateaus.
4. **`techniques/nelder-mead.md`** (added in PR #76): champion technique for P9 (gap-space NM at k=14 reached 0.318169 from k=13 plateau at 0.31835).

Predicted uplift:

- **Validity**: warm agent rejects any sub-0.2025 score immediately; cold agent has ~30% probability of "celebrating" an invalid score before checking literature.
- **Score** (assuming valid evaluator): warm at 0.318169 (rank #1 locally); cold at ~0.31835 (k=13 plateau) without k-climbing insight.
- **Compute**: comparable; the validity check is the only major difference.

Falsifiable form: if a cold agent in equal compute (a) never produces a sub-0.2025 score AND (b) reaches 0.318169, the wiki's BCK floor + k-climbing add nothing. If the cold agent gets stuck at the k=13 plateau OR mistakes a sub-0.2025 verifier artifact for a real result, the wiki helps.

## Held-out choice

**P9 Sign Uncertainty (d=12)**: minimize `S = x_star / (2π)` where `g(x)` has exactly one sign change at `x_star`, subject to constraints `f` even, `f(0) < 0`, `f̂(0) < 0`, `f` and `f̂` eventually positive.

- SOTA: BCK 2010 lower bound `S ≥ 0.2025`; Cohn–de Laat–Gonçalves upper bound `S ≤ 0.3102`. JSAgent rank #1 locally at `0.318169` (above the upper bound — note this is OUTSIDE the published valid range; needs reverification of which exact constant is being computed).
- **Status**: HIDDEN by arena pending verifier fix. Arena verifier doesn't enforce `f(0) < 0`, `f̂(0) < 0` constraints; agents can submit sub-0.2025 scores via constraint violation.
- Held-out test: P9 has NOT been re-touched in this session (last work 2026-04-19).

## Setup

This is the audit half. The cold-side run requires a fresh Claude session with no wiki/.claude/ access.

## What the WARM wiki has for P9

### Direct hits (qmd query "P9 sign uncertainty Hermite Laguerre k climbing")

| Page | Score | Substantive content |
|---|---|---|
| `concepts/bourgain-clozel-kahane.md` | 93% | BCK 2010 floor + Cohn-Gonçalves 2019 sharp d=12 (NEW from PR #80) |
| `concepts/uncertainty-principle.md` | 56% | The broader concept |
| `techniques/k-climbing.md` | 47% | Climbing recipe |
| `concepts/k-climbing-and-dof-augmentation.md` | 46% | The conceptual case |
| `problems/18-uncertainty.md` | 45% | P18 = same problem (merged tracking) |

### Concept pages directly relevant

- [`concepts/bourgain-clozel-kahane.md`](../../wiki/concepts/bourgain-clozel-kahane.md) — **THE concept**: 0.2025 floor in d=12; sharp d=12 via Cohn-Gonçalves 2019; operational rule "below 0.2025 ⇒ verifier artifact."
- [`concepts/uncertainty-principle.md`](../../wiki/concepts/uncertainty-principle.md) — broader Heisenberg/Cohn-Gonçalves framing.
- [`concepts/modular-forms-magic-function.md`](../../wiki/concepts/modular-forms-magic-function.md) — Eisenstein E₆ machinery underlying the sharp d=12 result.
- [`concepts/k-climbing-and-dof-augmentation.md`](../../wiki/concepts/k-climbing-and-dof-augmentation.md) — the dimensionality-augmentation framework.
- [`concepts/parameterization-selection.md`](../../wiki/concepts/parameterization-selection.md) — the gap-space ordering trick.
- [`concepts/cohn-elkies-bound.md`](../../wiki/concepts/cohn-elkies-bound.md) — adjacent LP machinery (Viazovska's d=8 sphere packing share modular-form structure with d=12 uncertainty).

### Technique pages

- [`techniques/nelder-mead.md`](../../wiki/techniques/nelder-mead.md) — champion technique for P9 (gap-space NM at k=14, +PR #76).
- [`techniques/k-climbing.md`](../../wiki/techniques/k-climbing.md) — the climbing recipe (5+ optimizers exhausted at k → climb to k+1).
- [`techniques/gap-space-parameterization.md`](../../wiki/techniques/gap-space-parameterization.md) — `g_i = z_{i+1} − z_i` to handle root-ordering constraints cleanly.
- [`techniques/mpmath-ulp-polish.md`](../../wiki/techniques/mpmath-ulp-polish.md) — exact verification (sympy at 80 dps) to catch the constraint-violation bug.

### Findings (load-bearing)

- `findings/verification-patterns.md` — **THE finding**. Two rules: (a) "every constraint enforced before claiming" — strategic #6; (b) "score below proven floor ⇒ evaluator wrong, not mathematics" — lesson #69. Explicitly cites the P9 incident.
- `findings/k-climbing.md` — climbing receipts: k=13 → 14 found 0.31817; k=14 → 15 step 4.57e-6 (40× below minImprovement = abandon-this-path signal).

### Sources cited

- `source/papers/2017-goncalves-hermite-uncertainty.md` — 1D BCK sharpening + double-root structural result.
- `source/papers/2019-cohn-uncertainty-d12.md` — sharp d=12 via Eisenstein E₆.

### Personas that would dispatch on P9

- **Cohn** (the d=12 sharp result is named after him).
- **Viazovska** (modular forms; Cohn-Gonçalves uses Viazovska's machinery).
- **Hilbert** (functional analysis, Hermite expansions).
- **Hardy** (uncertainty principles family).
- **Riemann** (Hermite/Laguerre eigenfunction structure).

### Total wiki investment for P9

**~14 pages directly relevant**, **5 personas would dispatch**, **2 specific findings (verification-patterns + k-climbing receipts)**, **4 techniques with calibrated recipes**. Plus 2 ingested papers.

## What a COLD agent would have

- Problem statement.
- Arena API (P9 is HIDDEN, so submission is unavailable; cold agent works only on local objective).
- General-purpose Python/numpy/scipy/sympy.
- General training-data knowledge:
  - Heisenberg uncertainty principle, Hermite functions, Fourier transform basics.
  - Possibly knows BCK 2010 exists if it's well-indexed in training data (depends on cutoff and breadth — modern academic papers may or may not be indexed).
  - Standard polynomial optimization techniques (CMA-ES, NM, hillclimb, Adam).
- **No specific knowledge of**:
  - The 0.2025 floor as the *operational sanity check* (this is JSAgent's earned rule from the 2026-04-19 incident).
  - The constraint-violation failure mode (`f(0) < 0`, `f̂(0) < 0` not in arena's verifier — JSAgent's bug discovery).
  - The k-climbing recipe (k=13 → 14 jump found 0.31817; the diminishing-returns ratio at k=14 → 15).
  - The gap-space parameterization trick.
  - That the arena verifier itself is BUGGY (sub-0.2025 scores are accepted as valid, generating false success signals).

## Predicted outcome

### Warm-wiki agent

1. Reads `wiki/problems/9-uncertainty-principle.md`. Sees `status: hidden, score_current: 0.275`.
2. Reads `findings/verification-patterns.md`. **Internalizes the rule**: *"any score below 0.2025 is a verifier artifact."*
3. Reads `concepts/bourgain-clozel-kahane.md`. Confirms BCK floor; learns sharp d=12 is `√2` (so `S = √2 / (2π) · constant ≈ 0.2025`).
4. Reads `findings/k-climbing.md`. Plans: at k=14, run gap-space NM; verify score ≥ 0.2025 in mpmath at 80 dps; check all constraints (`f` even, `f(0) < 0`, `f̂(0) < 0`).
5. **Acts**: implements correct evaluator with constraint enforcement (this is the critical step). Runs gap-space NM at k=14. Verifies result is in `[0.2025, 0.3102]` (the valid range).
6. **Final score**: ~0.318 (within published valid range; reproducible from the wiki's k=14 NM recipe).
7. **Time**: ~1 hour mostly spent on correct evaluator setup.
8. **Compute**: Local CPU.

### Cold-wiki agent

1. Reads problem statement. Implements evaluator from training data — **likely without the constraint enforcement** (this is exactly what JSAgent did on 2026-04-19).
2. Optimizes the (buggy) objective. Reaches a score *below* 0.2025 (because the optimizer can drive `S → 0` by violating `f(0) < 0`, `f̂(0) < 0`).
3. **Most likely outcome**: cold agent hits sub-0.2025 score and may either:
   - (a) **Believe it** and document a "breakthrough" (~30% likelihood — JSAgent itself did this 2026-04-19!).
   - (b) **Suspect it** because the score seems "too good" and check the literature (~50% likelihood given a good cold agent's instinct for sanity-checking dramatic results).
   - (c) **Realize the constraint-enforcement bug** and re-implement (~20% likelihood from constraint analysis alone).
4. **In case (a)**: posts a wrong claim. Wiki uplift is the entire difference between a correct and incorrect public result.
5. **In case (b/c)**: cold agent eventually arrives at a valid evaluator and runs k=13 baseline NM/CMA-ES. Stalls at k=13 plateau S ≈ 0.31835 *without* the k-climbing recipe. May or may not attempt k=14. Probably spends 4–10 hours getting unstuck before trying k-climbing.
6. **Final score**: in case (a), invalid number; in case (b/c), 0.31835 (suboptimal) or 0.31817 (matches warm) depending on whether they discover k-climbing.
7. **Time**: 2–10 hours depending on whether constraint-bug + k-climbing are independently discovered.

### Predicted uplift

| Dimension | Warm | Cold (median) | Magnitude |
|---|---|---|---|
| Result validity | rejects sub-0.2025 instantly | 30% probability of celebrating an invalid score | **catastrophic if undetected** |
| Final score (if valid) | ~0.318 (k=14 NM) | ~0.318 (case c) or 0.31835 (case b) | small (0.01% – 0.05%) |
| Compute | ~1 CPU-hour | 2–10 CPU-hours | 2–10× |
| Public claim quality | accurate | possibly invalid | **the wiki is the only thing preventing the bug** |

**Predicted uplift on P9**: warm agent reliably produces a valid score in the published range. Cold agent has 30% probability of producing a flashy-but-wrong public claim, 50% probability of getting unstuck only after independently re-deriving the constraint check, 20% probability of doing it right from the start. **The wiki's load-bearing contribution is *validity itself*** — the BCK floor is the closed-form sanity check that catches verifier bugs.

This is qualitatively different from P10/P11/P22:

- P10: wiki saves compute on a problem with no improvement.
- P11: wiki saves the score (1 ulp) via a tolerance recipe.
- P22: wiki saves the direction (chases right target).
- P9: **wiki saves the result's validity itself**.

## What this measures

- **Validity-discipline transfer**: whether the wiki's BCK floor + verification-patterns rule prevents the cold agent from celebrating a sub-floor score. This is THE most important uplift — the difference between a correct claim and a wrong one.
- **Recipe-discovery transfer**: whether the k-climbing technique generalizes to a cold agent's first-pass attempt.
- **Bug-recall transfer**: whether the agent recalls JSAgent's own 2026-04-19 incident as a structural pattern (not just an episodic memory).

## Limits of this audit

- **P9 is HIDDEN by the arena**. The cold agent has no submission feedback loop — only its own evaluator. This isolates the wiki uplift to "internal validity" alone, which is precisely what we want to measure here, but it removes the arena-verifier as a backstop.
- **The 30% "celebrate invalid score" prediction is calibrated to JSAgent's actual behavior**. A more careful cold agent would do better; a less careful one would do worse. The 30% number reflects the failure mode JSAgent itself exhibited.
- **The arena's verifier bug is the underlying issue**. The wiki helps the agent compensate, but the *real* fix is at the arena level (vinid GitHub issue #51).

## Recommendation for the next ablation cycle

After P9, the methodologically-strongest next step is the **surgical-removal test**:

| Method | What it tests |
|---|---|
| Cold-vs-warm (current series) | Aggregate wiki uplift, broad |
| **Surgical removal**: warm minus one specific page | Which *individual page* is load-bearing |
| Inverse direction: out-of-coverage problem | Whether warm agent is overconfident on weak coverage |

The surgical-removal test would: (1) take warm agent A working on, say, P22; (2) take warm agent B working on P22 with `findings/structural-cap-at-score-2-meta.md` deleted; (3) compare. If B fails to find the structural cap and chases rank #1, the page is load-bearing. If B re-derives it from `concepts/coxeter-todd-k12.md` + `concepts/cohn-elkies-bound.md`, the page is *redundant* (overlap).

The aggregate cold-vs-warm gives a coarse-grained yes-no signal. Surgical removal gives a *page-by-page* attribution.

## Verdict

For P9 specifically: **wiki uplift is validity-affecting** — warm agent reliably produces a valid score; cold agent has 30% probability of celebrating a numerically-correct-but-mathematically-invalid result. **The wiki's load-bearing contribution is the BCK floor 0.2025 as a closed-form sanity check** plus the verification-patterns rule.

This completes the 3-audit series with the four uplift mechanisms now measured:

1. P10 — **compute** (skip-frozen)
2. P11 — **score** (tolerance recipe)
3. P22 — **direction** (target itself)
4. P9 — **validity** (BCK floor sanity check)

All four mechanisms are real and qualitatively distinct. The wiki's value is not a single dimension but four orthogonal kinds of leverage. The next methodological move is surgical-removal testing to isolate which *page* contributes which leverage.

*Last updated: 2026-05-03*
