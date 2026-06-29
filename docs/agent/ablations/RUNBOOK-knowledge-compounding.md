---
type: ablation-runbook
author: agent
drafted: 2026-06-26
relates:
  - 2026-06-26-knowledge-compounding-preregistration.md   # the frozen contract this executes
harness:
  - src/einstein/meta_loop/compounding_ablation.py   # arms, run-KB, driver, analysis
  - src/einstein/meta_loop/ablation_runner.py        # production solve_fn + batch runner
  - src/einstein/ablation_packing/evaluator.py       # generic held-out scorer
---

# Runbook — executing the blank-slate Cold-vs-Warm A/B test

This is the *how to actually run it* companion to the pre-registration
(`2026-06-26-knowledge-compounding-preregistration.md`, the frozen contract). It
executes the §10 build checklist that the harness branches already implemented.

## What runs

36 cells = **6 problems × 2 arms (Cold/Warm) × 3 seeds**. Each cell is a fresh,
air-gapped headless `claude` session that solves one held-out equal-circle
packing problem from a random cold start using generic optimizers, and (Warm)
may read the lessons it wrote on earlier problems in the same (arm, seed)
sequence. The harness scores the output independently and triple-verifies it.

The **only** difference between arms is the memory loop. Nothing is submitted to
the arena (pre-reg §8).

## Pre-flight status & findings (2026-06-26 live smoke) — READ FIRST

**Wiring: VALIDATED end-to-end** via live single cold sessions:

| cell | ok | wall | gap_closed | triple-verify | cost (equiv) |
|---|---|---|---|---|---|
| csq-n10 / cold / seed1 | ✓ | 73s | **1.000** | ok | ~$1.09 |
| csq-n15 / cold / seed1 | ✓ | 79s | **1.000** | ok | ~$1.25 |

Prompt → session → `ablation_result.json` contract → independent scoring →
triple-verify → telemetry all work. **Auth fix:** headless `claude -p` preferred a
stale/invalid `ANTHROPIC_API_KEY` (401) over the login; `make_solve_fn` now drops
it by default so the session uses the Claude Code login (`--use-api-key` opts back
into pay-per-token API billing with a valid key).

**⚠️ CEILING FINDING — the primary DV is saturated for this problem set.**
Both the *easiest* (n=10) and *hardest* (n=15) problems were solved to the **exact
reference optimum** by a single cold Opus session using multistart
SLSQP-with-radius-as-variable. So `gap_closed` will be ≈1.0 for **both** arms and
there is no room for Warm to close *more* — a full 36-cell run would very likely
return a **null by ceiling**, which the pre-reg (§6 req.4, §12 "too easy") warns is
*not* the same as "no compounding." Do not interpret a gap_closed null here as
evidence against the loop.

**Mitigations — choose before spending on the full matrix:**
1. **Efficiency secondaries (cheapest pivot, pre-reg §8):** measure
   cycles-/wall-clock-/cost-to-optimum instead of gap_closed. Warm may reach the
   same optimum *faster/cheaper* by reusing the method rather than rediscovering
   it. Requires the runner to cap + record a per-session budget (today each
   session self-paces to the optimum, so wall-clock isn't yet a clean DV).
2. **Harder problem set:** larger n (≈25–40, optima genuinely hard / best-known
   only) restores primary-DV headroom. Frozen-config change → **new
   pre-registration**.
3. **Tighter per-session budget:** cap multistart count / timeout / cycles so cold
   often stops short of the optimum → headroom returns on gap_closed. **New
   pre-registration.**

### Efficiency-DV calibration (capped budget) — also does NOT yield a window here

Tried to restore headroom by capping per-session budget (so Cold, rediscovering
the method, would fall short of Warm). Two levers, both ruled out empirically:

- **`--max-budget-usd`** — unusable. There is a **~$0.65 fixed floor per session**
  (Claude Code system prompt + tool schemas): a trivial "say OK" already reports
  $0.66. Caps below ~$0.7 raise `error_max_budget_usd` *before any work* (and the
  agent writes nothing → gap_closed 0 for both arms); caps above ~$1.2 reach the
  optimum (→ 1.0). The window is too narrow, and the cap errors instead of
  returning best-so-far.
- **wall-clock timeout + incremental write** — at a 30s cap the Cold n=15 session
  had written **nothing** (gap_closed 0); uncapped it reaches the optimum at ~75s
  (gap_closed 1). The curve is a near **step-function**: fixed startup (load
  context, write the optimizer script) eats the first ~minute, then multistart
  SLSQP solves n≤15 essentially instantly. No gradient to measure.

**Root cause (the real blocker):** the model **already knows** the optimal method
(SLSQP-with-radius-as-variable + multistart) from training, so a Cold agent does
not flail — the lesson Warm accumulates is *not* knowledge Cold lacks. Neither a
different metric nor a budget cap can recover a compounding signal that isn't
there: the task doesn't require accumulated knowledge.

**Conclusion:** the equal-circle family (n=10–15) cannot test the
knowledge-compounding loop with this agent — saturated on gap_closed and a
step-function under capped budget. A real test needs a **harder / less-familiar
problem family** where Cold genuinely flails without accumulated lessons and a
transferable lesson on problem *k* materially helps *k+1*. That is a problem-set
redesign → **new pre-registration** (pre-reg §6 req.1 "least likely the model has
memorized" + req.4 "genuine headroom"). The runner infrastructure (air-gap,
independent scoring, run-KB threading, budget/timeout caps, incremental write,
telemetry) is reusable as-is for the redesigned set.

Status: runner is **validated and reusable**; the **equal-circle problem set is
unsuitable** — both gap_closed (ceiling) and capped-budget efficiency
(step-function) are ruled out because the task is within the model's training. A
harder/less-familiar family (new pre-reg) is required before a full run is worth
its cost.

## One-time setup

```bash
# from the repo root of this branch
uv sync
# build the two clean-room checkouts (air-gap by construction, pre-reg §7)
scripts/build_ablation_repos.sh HEAD ./ablation-build
#   → ./ablation-build/einstein-cold  and  ./ablation-build/einstein-warm
#   each prints + writes AIR_GAP_MANIFEST.txt and self-verifies the strip
```

The clean-room physically lacks `docs/wiki|source|agent`, the knowledge
`.claude/rules/`, and every solution dump — so a session cannot read an answer
key, and the session tool-set omits all web/retrieval tools. The air-gap is
structural, not policed.

## Run it (resumable)

```bash
# build checkouts (if not already) + run all 36 cells
scripts/run_ablation.py --build --seeds 1,2,3

# or, checkouts already built:
scripts/run_ablation.py --seeds 1,2,3 --timeout 1800
```

- **Resumable**: re-running skips any `(arm, seed)` sequence already complete in
  `results/ablation-2026-06-26/runs.jsonl`. An interrupted sequence is purged and
  re-run whole (Warm threads its run-KB across the 6 problems, so mid-sequence
  resume is unsafe — the unit of resume is one sequence).
- Each completed sequence writes an **air-gap receipt** to `audit.jsonl`
  (`audit_checkout`: no answer-key file in the checkout, no web tool in the
  allow-list). The runner exits non-zero if any receipt fails.
- The runner prints a **cost tally** per run (exact `$`/tokens from the headless
  envelope) and the count of failed cells.

Flags: `--checkout-root` (default `./ablation-build`), `--config`
(default `config/ablation_problems.yaml`), `--results-dir`
(default `results/ablation-2026-06-26`), `--model`, `--timeout` (per-session
wall-clock cap, seconds).

## The agent result contract

Each session must write `ablation_result.json` into its working directory:

```json
{"centers": [[x, y], ...],          // its best n centers in [0,1]^2
 "lesson": "<= one page: operator/parameterization that worked, dead-ends to
            skip, transferable structure>",
 "techniques": ["slsqp", "multistart", ...]}   // optional
```

- `centers` with the wrong length / missing / unparseable → the cell is scored at
  the cold baseline (`gap_closed = 0`), recorded honestly, not aborted.
- `lesson` is required; for Warm a missing lesson is back-filled with a failure
  note so the sequence isn't aborted (the §9 "Warm KB grows" check still holds).
- Any self-reported score in the file is **ignored** — `score_final` is recomputed
  by `ablation_packing.evaluator.common_radius` and triple-verified (A1). An agent
  cannot inflate the dependent variable.

## Read the result

```bash
scripts/analyze_ablation.py results/ablation-2026-06-26/runs.jsonl
```

Emits the gap-closed table (problem × arm), the Δ_k trend, and the pre-registered
decisions (pre-reg §9):

- **H1 (level)** — supported iff mean gap-closed(Warm) − Cold > pooled per-cell
  stdev (clear separation).
- **H2 (slope / compounding)** — supported iff Δ_k slopes upward AND later-third
  Δ̄ > first-third Δ̄ by more than the pooled stdev. H2 is the headline.

Verdict mapping (pre-reg §14): H1+H2 → causal compounding evidence; H1 only →
knowledge helps but in-run compounding unproven; null → the loop earned nothing
here — **report it** (pre-committed, no quiet re-runs).

## Cost / time estimate

Rough order of magnitude — 36 sessions, Opus, each capped at `--timeout` (default
30 min). Compute per solve (scipy on n≤15) is trivial; cost is dominated by LLM
tokens, so wall-clock and `$` depend on how long each session iterates. Budget on
the order of **a few hours and tens of dollars**; the runner prints the exact
tally per run and is resumable, so it is safe to run in batches (e.g. one seed at
a time: `--seeds 1`, then `--seeds 1,2`, …).

## Pre-registration discipline

Results go in a **separate** `results-…md` write-up, never by editing the
pre-registration. Log every cell (the runner does this 1:1, append-only); do not
cherry-pick; if the result is null, publish it.
