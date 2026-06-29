---
type: ablation-protocol
author: hybrid
drafted: 2026-06-28
status: draft            # NOT yet frozen — sketch for review; freeze §3–§6 before run 1
hypothesis: "An encouraging prompt preamble does not improve the agent's score-per-unit-compute on the solve loop. H1 (effort): any score gain is mediated by increased compute (more cycles/tokens/iterations) and vanishes at a fixed budget. H2 (efficiency): the encouraging arm's score-vs-compute frontier sits strictly above neutral at equal budget. Default expectation on a frontier model: NULL (no separation at fixed budget)."
factor: prompt_tone   # {neutral (control), encouraging, optional: stakes/harsh}
model: claude-haiku-4-5   # tier-1 cheap; add claude-opus-4-8 only if Haiku shows a signal worth pricing
harness: src/einstein/meta_loop/compounding_ablation.py + ablation_runner.py   # + a prompt_tone factor + a fixed-budget cap (NOT YET BUILT)
relates:
  - 2026-06-26-heilbronn-haiku-compounding-preregistration.md   # v2 — the within-family design this borrows
  - 2026-06-26-cross-family-generalization-preregistration.md   # v3 — the capability/effort/efficiency split, reused here
paper_hook: "main.tex §6 — does prompt framing affect the agent, and is it effort or efficiency? Honest result either way."
question: ../../wiki/questions/2026-06-28-does-prompt-tone-change-agent-performance.md
---

# Pre-registration (DRAFT) — Encouraging prompt: effort, efficiency, or null?

> **Status: DRAFT.** Sketch for review. The §3 problem/seed/budget freeze and the §4
> arm strings must be locked **before run 1**. Gated behind `feat/ablation-v3-llm-runs`
> for the shared Claude rate limit (§6).

---

## 0. The claim and why it needs a controlled test

The human reports an encouraging `/auto-branch` preamble ("never give up, push to rank 1")
felt helpful in the early competition phase. That is an **uncontrolled** observation —
recall bias plus early-phase low-hanging fruit. EmotionPrompt-style gains are real on
weaker models but shrink toward noise on frontier models. So the prior is *small, possibly
null*, and the claim must be measured, not trusted. A clean null is a useful, paper-worthy
result and is consistent with the v2 finding (efficiency, not capability).

## 1. The two mechanisms — what must be disentangled

If an encouraging preamble lifts the final score, it is one of two things:

- **H1 — EFFORT.** The preamble makes the agent *spend more* (more reasoning cycles, more
  tokens, longer optimizer runs). Equivalent to raising the budget; reachable by spending
  the same compute on the neutral prompt. **Not interesting.**
- **H2 — EFFICIENCY.** The preamble lifts *score-per-unit-compute*: higher score at the
  **same** token / wall-clock budget. **The interesting claim.**

**Endpoint comparison cannot tell these apart** (a higher endpoint may just be more spend).
The estimand is therefore the **score-vs-compute frontier**, not the final score.

## 2. The estimand — the score-vs-compute frontier  **[FROZEN]**

For each (arm, seed), record the trajectory of best-score-so-far against cumulative
compute on three x-axes already logged by the harness:
- cumulative **output tokens** (exact, from the `claude_headless --output-format json` envelope),
- cumulative **wall-clock** seconds (the measured `hours` field, per-cycle),
- cumulative **optimizer iterations** (script-side, where the solve loop exposes it).

Primary x-axis = **output tokens** (cleanest compute proxy; wall-clock as robustness check).
Primary comparison: at a set of pre-committed budget checkpoints `B ∈ {b1<b2<…}`, the
mean best-score of `encouraging` minus `neutral` at equal cumulative budget, with a
seed-clustered CI. Secondary: area-under-the-score-vs-budget-curve per arm.

## 3. Design: tone × budget-regime  **[FREEZE before run 1]**

A 2×2 (tone × regime) crossing isolates the mechanism:

| | Fixed budget (cap tokens **and** cycles equal across arms) | Unconstrained (natural stopping) |
|---|---|---|
| **neutral** | control | control |
| **encouraging** | **H2 test** (efficiency) | **H1 test** (effort) — also record extra spend |

- **Fixed-budget regime** — every arm gets the same hard cap (token ceiling AND max cycles;
  whichever binds first). If `encouraging` still beats `neutral` here → **H2 supported**.
- **Unconstrained regime** — each arm stops on its own gate. If `encouraging` only wins here,
  ties under fixed budget, and spent more → **H1 supported** (effort, not quality).
- If neither regime separates the arms across seeds → **NULL**.

**To freeze before run 1:**
- **Problems** (`instances`): reuse a v2/v3 family with confirmed cold headroom (e.g. Heilbronn
  set) so a score signal *can* exist; list the exact instances + frozen `reference_optimum`s.
- **Seeds**: N per cell — start exploratory small-S, then freeze S after the variance check
  (same S-freeze rule as v3 §6); same paired cold-init per seed across arms (ONE variable = the
  preamble string).
- **Budget checkpoints** `B` and the fixed-budget caps (token ceiling + max cycles).
- **One-variable invariant**: arms differ ONLY in the preamble prepended to the session system
  prompt. Identical problems, seeds, cold-init, model, temperature, tools, solve budget otherwise.

## 4. The arm strings  **[FREEZE before run 1 — verbatim]**

- **neutral** (control): no preamble (or a length-matched neutral filler to control for token
  count — decide and freeze which; a length-matched neutral is the stronger control).
- **encouraging**: the human's actual phrasing, frozen verbatim, e.g.
  *"You can do it. Never give up. Push to the ultimate limit. Keep it up. Never stop until
  reaching rank 1."*
- **(optional) stakes/harsh** third arm — only if the 2-arm test shows separation worth
  resolving; otherwise drop to save budget.

**Confound to declare:** an encouraging preamble may *also* change persistence/length. The
fixed-budget regime is precisely the control that holds effort constant; the unconstrained
regime measures the effort channel explicitly. Report both — do not collapse them.

## 5. Analysis  **[FROZEN]**

- Per regime: mixed model `best_score ~ tone + (1|seed)` evaluated at each budget checkpoint
  (fixed regime) / at natural stop (unconstrained), seed as random effect.
- Mechanism verdict from the 2×2:
  - separation in **fixed** column → **H2 (efficiency)**;
  - separation only in **unconstrained** column + higher spend → **H1 (effort)**;
  - no separation either column → **NULL**.
- Non-inferiority guard: `encouraging` must not score *worse* than `neutral` at equal budget
  (a real possibility — verbose preambles can distract).
- Distributional, not best-of-N: reuse `rank_arms`; report CIs, not point wins.

## 6. Staging & cost  **[FROZEN staging]**

1. **Gate:** do NOT start until `feat/ablation-v3-llm-runs` is idle — both drive headless
   sessions on the same Claude subscription; concurrent runs contend for the rate limit.
2. **Harness work first (no LLM):** add a `prompt_tone` factor + a fixed-budget cap
   (token ceiling + max-cycles) to `ablation_runner.py` / `compounding_ablation.py`, behind
   mock tests. This is the only code this branch ships pre-run.
3. **Exploratory small-S** (Haiku, fixed + unconstrained, 2 arms) → variance check → freeze S.
4. **Confirmatory** at frozen S; add Opus + the optional 3rd arm only if Haiku separates.
5. **Land** results in a `results-prompt-tone.md` ledger + `mechanism-claims-test-matrix.md`;
   close the question with the finding; move this protocol to `status: frozen`/done.

## 7. Threats

- **Recall-bias prior** — the motivating observation is uncontrolled; treat H0=null as the
  honest default and require fixed-budget separation to claim H2.
- **Token-count confound** — neutral arm should be length-matched, else "encouraging" also
  buys raw tokens. Freeze the control choice in §4.
- **Single-family** — a tone effect could be family-specific; if Haiku separates, replicate
  across ≥2 families (borrow v3 §3 headroom screen) before any general claim.
- **Persistence confound** — addressed by the budget-regime crossing; must report both columns.

## 8. Implications

- **H2 (efficiency):** cheap, real lever — bake the preamble into the autonomous loop's system
  prompt; document in `.claude/`.
- **H1 (effort):** not a free lunch — equivalent to raising the budget; prefer an explicit
  budget knob over a motivational string.
- **NULL:** retire the practice as folklore; record the dead-end finding (failure-is-a-finding).
  Either way the README/paper gains a measured statement about prompt framing.
