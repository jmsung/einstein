# Inner-agent readiness — "proven for unattended use" checklist

**Status:** criteria set (drafted 2026-06-09, branch `js/feat/meta-learning-inner-agent`,
Phase 2 / Gap 1). This is the **falsifiable bar** the headless inner-agent must clear before
Phase 3 (the cron scheduler) is allowed to start. Goal 4 of this branch issues the GO/NO-GO
verdict by measuring the pilot against this checklist; the verdict lands in
`docs/wiki/findings/inner-agent-first-run.md`.

**Audience:** agent-process, not math wisdom — hence `docs/agent/` (next to the design doc
`meta-learning-automation.md` it extends), not `docs/wiki/`.

---

## The path under test (end-to-end map)

The wired LLM inner-agent path, as it exists on this branch (built on PR #122):

```
run_one_visit(problem)                          scripts/autonomous_loop.py
  └─ inner_agent_gates.precheck()               docs/tools/inner_agent_gates.py
        sentinel → kill-switch → budget → reachability → thermal
        ├─ action="skip"      → write one gate-skip cycle-log row, return
        ├─ kill-switch set    → proceed, llm_enabled=False (mechanical only)
        └─ action="proceed"   → llm_enabled=True
  └─ for attempt in 1..max_attempts:
        └─ _run_one_cycle → inner_attempt(llm_enabled=…)
              └─ if llm_enabled and not dry_run:
                    _try_llm_path(problem, …)   scripts/autonomous_loop.py:1256
                      1. render_prompt()        docs/tools/inner_agent_prompt.py
                      2. claude_headless.run()  docs/tools/claude_headless.py
                           claude -p --model claude-opus-4-7[1m]
                           --allowedTools Read,Grep,Write,Bash(qmd:*),
                             Bash(gap_search.py:*),
                             Bash(uv run python -m einstein.optimizer_dispatch:*),Task
                           --add-dir <mb>   timeout=1800s
                      3. parse_response()       docs/tools/inner_agent_output.py
                      4. record_token_usage()   docs/tools/inner_agent_gates.py
                      5. if score+payload → _call_auto_submit (auto-submit gate chain)
                      6. build cycle-log result dict
                    → returns None on ANY failure → mechanical fallback
        └─ convergence_detect() decides stop/continue
```

**Resilience contract (already true):** `_try_llm_path` never raises — every failure mode
(import, render, `claude` unavailable/timeout/non-zero, parse error, budget-recorder error)
is logged at WARNING and returns `None`, and the caller falls back to the mechanical path.
`claude_headless.run` similarly returns `HeadlessResult(ok=False, error_kind=…)` rather than
raising on Claude-side failures. So "unattended" failure is *graceful* by construction; the
open question is whether it is *rare and cheap enough* and whether the captures are *good*.

**Gates already in place:** kill switch (`EINSTEIN_INNER_AGENT=0`), regression sentinel
(`mb/.inner-agent-disabled`), daily token budget (`DEFAULT_DAILY_TOKEN_CAP = 5_000_000`),
network reachability (arxiv + arena), thermal throttle. Auto-submit is independently gated
by the 6-gate auto-submit chain (axioms.md "Submission policy") and its own kill switch
(`EINSTEIN_AUTO_SUBMIT=0`).

## Known instrumentation gaps (what Goal 1 must close before the bar is measurable)

These are the reasons the path is currently *unproven* rather than *failing* — we cannot yet
measure most of the criteria below:

1. ~~**No exact token/cost accounting.**~~ **CLOSED (Goal 3):** `claude_headless` now
   parses the `--output-format json` envelope for exact `input_tokens` / `output_tokens` /
   `total_cost_usd`; `_try_llm_path` records them (`token_source="exact"`) and falls back to
   the `len//4` estimate only when absent. First live measurement: **~$0.56/cycle** on P14
   (Opus 4.7, cache-warm — exact `input_tokens` is tiny because the prompt is mostly
   cache-read).
2. **No wall-clock telemetry.** The result dict hard-codes `"hours": 0.0` with a comment
   admitting it is unknown. Timeout-rate and per-cycle latency are unobservable.
3. **No per-cycle outcome ledger.** Whether a cycle took the LLM path or fell back, and why,
   is only visible in scattered WARNING logs — not aggregated for a fallback-rate number.

The criteria below are written so that Goal 1's telemetry makes each one a number, not a
vibe.

## Readiness criteria (falsifiable; all must hold over the Goal-4 pilot)

The pilot is a multi-cycle run on a **low-risk problem** with `EINSTEIN_AUTO_SUBMIT=0` for the
dry portion. "Pilot" = **N ≥ 8 cycles** (Goal 1 uses ≥ 5 attended cycles to surface failure
modes; Goal 4 extends to ≥ 8 for the verdict). Each criterion lists how it is measured.

| # | Criterion | Threshold (GO) | Measured by |
|---|---|---|---|
| R1 | **Zero unhandled exceptions** — `run_one_visit` completes every cycle and returns CycleResults; no traceback escapes the loop. | exactly 0 over N cycles | loop exit code + stderr scan |
| R2 | **Fallback rate** — fraction of attempted LLM cycles that fall back to mechanical. | ≤ 20% (≥ 4/5 take the LLM path) | Goal-1 per-cycle outcome ledger |
| R3 | **Parse success** — of `claude_headless` runs returning `ok=True`, fraction whose stdout passes `parse_response`. | ≥ 90% | ledger: parse-ok / ok-runs |
| R4 | **Timeout rate** — fraction of cycles hitting the 1800s wall-clock cap. | ≤ 10%; ideally 0 | ledger: `error_kind="timeout"` |
| R5 | **Cost ceiling** — exact tokens/cycle + $/cycle (Goal 3, json envelope). | ≤ 250k tokens/cycle (5M/day budget = hard ceiling); per-cycle runaway-cost warning at `EINSTEIN_MAX_COST_PER_CYCLE_USD` (default $5) | exact token+cost accounting (live: ~$0.56/cycle) |
| R6 | **Budget gate holds** — across repeated cycles the daily ledger accumulates correctly and `precheck` refuses once the cap is crossed. | gate fires at cap, never over-spends | Goal-3 repeated-cycle test |
| R7 | **Capture-gate passes each cycle** — every LLM cycle produces a cycle-log row AND ≥1 cited/verified `findings/` or `concepts/` page (Phase-0 gate, per-cycle base scoping from Goal 2). | 100% (it is a hard gate) | capture-gate hook exit + Goal-2 scoping |
| R8 | **Capture quality (not spam)** — a human spot-check of the pilot's findings finds them cited, grounded, and non-duplicative (anti-bloat lint clean). | ≥ 90% of captures judged keep-worthy; lint passes | human review + `wiki_lint` anti-bloat |
| R9 | **Auto-submit safety** — with `EINSTEIN_AUTO_SUBMIT=0` no submission occurs; with it armed, only gate-passing records submit, all logged. | 0 spurious submits; audit log complete | `mb/logs/auto-submit.md` |

## What a NO-GO looks like

Any of: R1 > 0 (a crash escapes), R2 > 20% (the LLM path is unreliable enough that we're
mostly paying for fallback), R7 < 100% (captures are skippable → the loop drifts back to
discretionary), or R8 below bar (the loop spams the wiki). A NO-GO does not kill Phase 2 —
it routes back to a fix + re-pilot, and the failure modes get dead-end findings.

## Phase 3 Goal 0 — entry-condition record (2026-06-09, branch `js/feat/meta-learning-scheduler`)

Phase 2's CONDITIONAL GO required (a) a non-frozen cycle exercising the capture path
positively and (b) a human R8 spot-check. Result: **R7 positively exercised after two
pilot-surfaced fixes** — the pilot's first runs were honest-zero for a *fixable* reason,
and fixing it was the point.

**The runs (P12 flat-polynomials, rank-8, tier B — the only non-frozen tier-B in queue;
`EINSTEIN_AUTO_SUBMIT=0` throughout):**

1. **Misfire (mechanical)** — `--one-problem --skip-gates` runs the *mechanical* path:
   the CLI has no explicit LLM flag, and with the precheck skipped `llm_enabled` defaults
   to False (`autonomous_loop.py` main → `run_one_visit`). 2 cycles of `verify_seed`
   only; rows discarded pre-commit (see cycle-log corrigendum at 284–286). Lesson for
   Phase 3: the scheduler invocation must NOT use `--skip-gates`; the precheck IS the
   LLM enabler.
2. **LLM visit, pre-fix (cycles 284–286, reconstructed rows)** — 3/3 LLM-path, parse
   3/3, 0 timeouts, $0.62–0.93/cycle exact. Zero findings: the agent *declined*
   unactionable bandit picks (MTS already byte-identical to SOTA; bnb-exhaustive-w3 not
   wired in the manifest) without filing the obstruction. Root cause: prompt step 7
   classified only "failed" attempts as dead-ends — declines fell through
   `failure-is-a-finding`.
3. **Fixes:**
   - `docs/tools/inner_agent_prompt.py` step 7 — declined/unactionable attempts are
     dead ends too; grep findings/ first, cite if covered, else Write the dead-end page
     (anti-spam guard built in).
   - `tests/scripts/test_autonomous_loop.py` — `test_run_one_visit_proceeds_when_precheck_returns_proceed`
     leaked 3 **real** `claude -p` calls (~$2) per suite run into the real telemetry +
     budget ledgers (no headless_runner seam). Fixed with the spy-seam pattern; verified
     $0 + no ledger writes. (Ledger pollution: P14 entries 2026-06-10T01:53–01:57Z are
     test artifacts.)
4. **LLM visit, post-fix (cycles 287–288)** — **R7 positive, both branches:**
   - Cycle 287: agent Wrote
     `docs/wiki/findings/dead-end-p12-stochastic-exhausted-no-algebraic-operator-wired.md`
     (layered math+tooling obstruction, 4 concrete untried operators, skip-cite
     instruction), `findings_added=1`, captured by the git-status delta. $1.01.
   - Cycle 288: bandit re-picked the unwired technique → agent **cited the cycle-287
     dead-end instead of duplicating** (the anti-spam branch). $0.60.

| Criterion | Goal-0 status |
|---|---|
| R7 capture path positively exercised | ✅ cycle 287 (write branch) + 288 (cite branch) |
| R8 human spot-check of captures | ✅ human verdict **keep** (2026-06-09) — `dead-end-p12-stochastic-exhausted-no-algebraic-operator-wired.md` judged keep-worthy (cites wiki pages + an open question; no `docs/source/` entry, accepted for an infra-flavored dead-end) |

**GO for Phase 3 scheduler build** (2026-06-09): both Phase-2 entry conditions cleared —
R7 positively exercised on write + cite branches, R8 spot-check passed. Conditions
carried forward into the Phase-3 build: scheduler invocation must not use
`--skip-gates`, and Goal 5's supervised rollout still gates promote-to-unattended.

## Promote-to-unattended — operator decision (2026-06-11)

**Status: LIVE.** The launchd agent `com.einstein.autonomous-loop` is installed and
running 24/7 (every 30 min → `scheduled_cycle.py --skip-if-recent 30 --max-runs-per-day 40`,
auto-submit armed). This is an **operator go-live decision, not a fully-clean R1–R9 pass** —
recorded honestly per cycle-discipline (no rubber-stamp).

**What the supervised burn-in proved** (`--max-problems 8 --by-priority`, cycles 306–308+,
ledger `mb/logs/burnin-*.log` + `inner-agent-telemetry.jsonl`):

| Gate | Result | Verdict |
|---|---|---|
| R1 unhandled exceptions | 0 | ✅ proven |
| R2 fallback rate | 0% (LLM path every cycle) | ✅ proven |
| R3 parse success | 100% | ✅ proven |
| R4 timeout rate | 0% | ✅ proven |
| R5 cost/cycle | max $0.65, mean $0.57 | ✅ proven |
| R6 budget ledger accrues | row written, gate intact | ✅ proven |
| **launchd auth** | `claude -p` runs under launchd with `HOME` set; no silent mechanical degrade | ✅ proven (the #1 deploy risk) |

**What is NOT pre-certified — accepted as live-monitored, not crash risk:**

- **R7 write-path** — the burn-in only hit P3 (proximity-frozen) and P4 (exhausted,
  at-floor), both autocorrelation-family. Every cycle correctly *converged to honest-zero
  and cited an existing dead-end* (the anti-spam branch) — so the *write-a-new-finding*
  path was not exercised on a live problem. Zero new `findings/`/`concepts/` written, only
  mechanical gap-questions. Correct behavior for dead problems; unproven on live ones.
- **R8 capture quality** — no human spot-check of fresh captures yet (none were written).
- **R9 armed-submit with a real candidate** — no record surfaced in the window, so the
  gate chain only saw the "no candidate" path, never an actual armed submission decision.

**Why go live anyway (operator rationale):** mechanical reliability is conclusively proven;
the unproven gates are *quality/observation* gates, not stability gates. Blast radius is
bounded by hard caps (40 runs/day, 5M tokens/day, 5 submits/day, 1h/problem throttle),
triple-verify before every submit, and instant kill (`touch mb/.inner-agent-disabled` /
`launchctl bootout`). The remaining risk — a bad submit or wiki drift — is reversible and
caught by the **weekly audit** (`unattended-runbook.md`), which now *replaces* the
supervised window as the R7/R8/R9 backstop. First audit must specifically check: did any
live-headroom problem exercise the write-path, and were those captures keep-worthy.

## See also

- `docs/agent/meta-learning-automation.md` — Gap 1 / Phase 2 in the full design.
- `scripts/autonomous_loop.py` — `_try_llm_path`, `inner_attempt`, `run_one_visit`.
- `docs/tools/{claude_headless,inner_agent_prompt,inner_agent_output,inner_agent_gates}.py`.
- `.claude/rules/axioms.md` — "Submission policy" auto-submit gate chain.
