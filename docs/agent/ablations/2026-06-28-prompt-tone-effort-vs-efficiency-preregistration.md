---
type: ablation-protocol
author: hybrid
drafted: 2026-06-28
status: frozen           # §3/§4 frozen 2026-06-29 (directional pilot — see §9)
hypothesis: "An encouraging prompt preamble does not improve the agent's score-per-unit-compute on the solve loop. H1 (effort): any score gain is mediated by increased compute (more cycles/tokens/iterations) and vanishes at a fixed budget. H2 (efficiency): the encouraging arm's score-vs-compute frontier sits strictly above neutral at equal budget. Default expectation on a frontier model: NULL (no separation at fixed budget)."
factor: prompt_tone   # {neutral (control), encouraging, optional: stakes/harsh}
model: claude-haiku-4-5   # tier-1 cheap; add claude-opus-4-8 only if Haiku shows a signal worth pricing
harness: src/einstein/meta_loop/compounding_ablation.py + ablation_runner.py + prompt_tone.py   # prompt_tone factor + fixed-budget cap (max_budget_usd) — BUILT on this branch
relates:
  - 2026-06-26-heilbronn-haiku-compounding-preregistration.md   # v2 — the within-family design this borrows
  - 2026-06-26-cross-family-generalization-preregistration.md   # v3 — the capability/effort/efficiency split, reused here
paper_hook: "main.tex §6 — does prompt framing affect the agent, and is it effort or efficiency? Honest result either way."
question: ../../wiki/questions/2026-06-28-does-prompt-tone-change-agent-performance.md
---

# Pre-registration — Encouraging prompt: effort, efficiency, or null?

> **Status: FROZEN (2026-06-29), run as a directional pilot — see §9.** The §3
> problem/seed/budget and the §4 arm strings were locked before run 1; results landed
> in `results-compounding-evidence.md` (NULL pilot, Δ=+0.035, 95% CI [−0.10, +0.18]).
> §0–§8 below preserve the original exploratory design rationale; §9 holds the frozen
> directional choices actually run. Gated behind `feat/ablation-v3-llm-runs` for the
> shared Claude rate limit (§6).

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

| | Fixed budget (`max_budget_usd` cost/token ceiling equal across arms) | Unconstrained (natural stopping) |
|---|---|---|
| **neutral** | control | control |
| **encouraging** | **H2 test** (efficiency) | **H1 test** (effort) — also record extra spend |

- **Fixed-budget regime** — every arm gets the same hard `max_budget_usd` cap (the
  cost/token-spend ceiling; the single-session `claude -p` runner exposes no per-session
  cycle cap, so the budget is the cost ceiling, not a max-cycles count). If `encouraging`
  still beats `neutral` here → **H2 supported**.
- **Unconstrained regime** — each arm stops on its own gate. If `encouraging` only wins here,
  ties under fixed budget, and spent more → **H1 supported** (effort, not quality).
- If neither regime separates the arms across seeds → **NULL**.

**To freeze before run 1:**
- **Problems** (`instances`): reuse a v2/v3 family with confirmed cold headroom (e.g. Heilbronn
  set) so a score signal *can* exist; list the exact instances + frozen `reference_optimum`s.
- **Seeds**: N per cell — start exploratory small-S, then freeze S after the variance check
  (same S-freeze rule as v3 §6); same paired cold-init per seed across arms (ONE variable = the
  preamble string).
- **Budget checkpoints** `B` and the fixed-budget cap (the `max_budget_usd` cost/token ceiling).
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
2. **Harness work first (no LLM):** add a `prompt_tone` factor (`prompt_tone.py`) + a
   fixed-budget cap (`max_budget_usd`, the cost/token ceiling — `claude -p` exposes no
   per-session max-cycles knob) to `ablation_runner.py` / `compounding_ablation.py`, behind
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
- **Air-gap fidelity (audited 2026-06-28).** The runner air-gap is two mechanisms:
  (a) `ALLOWED_TOOLS` omits every web/retrieval tool (`ablation_runner.py:51` — no
  `WebSearch`/`WebFetch`/`Task`), and (b) the clean-room checkout physically strips the
  knowledge layer (`build_ablation_repos.sh` `rm -rf knowledge/wiki knowledge/source docs/agent mb
  results`), verified by `audit_checkout` (`_ANSWER_KEY_DIRS`). Consequence for *this*
  ablation and the live v3 runs: the 2026-06-29 knowledge ingest (PR #134, +1147
  `knowledge/source/` pages) is **outside** the checkout the arms run in **regardless of which
  commit the checkout is built from** — the build deletes `knowledge/source/` wholesale — so it
  cannot contaminate any arm. **Residual hole:** the cwd lives inside the arm checkout (so
  `uv run` resolves the venv) and is explicitly *"not a hard sandbox — absolute-path access
  remains"* (`ablation_runner.py:226`); `Bash`/`qmd` could in principle reach the *real*
  repo by absolute path. A solving prompt never points there, but it is not impossible.
  **Mitigation (now implemented on this branch):** `audit_checkout` was a post-hoc receipt
  that did not abort on a leak — it is now a **hard gate** (`assert_clean_checkout` +
  `AirGapViolation`): `run_experiment` pre-flight-audits **both** arm checkouts before any
  compute and aborts on breach, and the post-run receipt now also raises on mid-run drift
  (`phase: preflight|postrun` in `audit.jsonl`). **Verification step before pooling any run:**
  confirm every `audit.jsonl` receipt is `passed:true`, and `grep` the per-cell transcripts
  (saved at `ablation_runner.py:230-235`) for `qmd`/`docs/`/absolute repo paths to rule out
  an absolute-path escape. Question: `../../wiki/questions/2026-06-28-does-prompt-tone-change-agent-performance.md`.

## 8. Implications

- **H2 (efficiency):** cheap, real lever — bake the preamble into the autonomous loop's system
  prompt; document in `.claude/`.
- **H1 (effort):** not a free lunch — equivalent to raising the budget; prefer an explicit
  budget knob over a motivational string.
- **NULL:** retire the practice as folklore; record the dead-end finding (failure-is-a-finding).
  Either way the README/paper gains a measured statement about prompt framing.

## 9. FROZEN directional design (2026-06-29)

Run as a **directional pilot** alongside the council ablation (single-credential serial
budget; the §3 S-freeze power target is deferred — same rationale as the council prereg §9).

- **§4 neutral control FROZEN = length-matched** (`PREAMBLES[NEUTRAL] = NEUTRAL_LENGTH_MATCHED`,
  123 chars vs ENCOURAGING 103, rel 0.16 ≤ 0.20 — passes `assert_length_matched`). This is
  the stronger control: any tone effect cannot be raw-token count. Encouraging string frozen
  verbatim (§4).
- **Regime:** fixed-budget only (the **H2 efficiency** test — the interesting one). 600 s
  equal-budget cap both arms. The unconstrained H1 (effort) regime is deferred — the
  single-session `claude -p` runner has no per-session cycle cap, and $ billing is $0
  (login), so wall-clock is the only budget; fixed-budget is the clean efficiency read.
- **Instances:** `heil-n13`, `heil-n14`; **Seeds:** S=4; paired cold-init. **Model:** haiku.
- **DV:** `gap_closed` paired delta (encouraging − neutral), mean + 95% bootstrap CI.
- **Driver:** `scripts/run_tone_ablation.py` (resumable). 8 cells.
- **Reporting caveat:** 8 cells underpowered — report directional Δ + CI as a pilot; a
  CI straddling 0 is the honest expected NULL on a frontier model (§0), not proof of none.

*Frozen 2026-06-29 (was draft 2026-06-28). Results → `results-compounding-evidence.md`.*
