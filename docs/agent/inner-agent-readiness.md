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
                    _try_llm_path(problem, …)   scripts/autonomous_loop.py:1069
                      1. render_prompt()        docs/tools/inner_agent_prompt.py
                      2. claude_headless.run()  docs/tools/claude_headless.py
                           claude -p --model claude-opus-4-7[1m]
                           --allowedTools Read,Grep,Write,Bash(qmd:*),
                             Bash(gap_search.py:*),
                             Bash(uv run python -m einstein.optimizer_dispatch:*),Task
                           --add-dir <mb>   timeout=1800s
                      3. parse_response()       docs/tools/inner_agent_output.py
                      4. record_token_usage()   docs/tools/inner_agent_gates.py
                      5. if score+payload → _call_auto_submit (A2 gate chain)
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
by the A2 6-gate chain and its own kill switch (`EINSTEIN_AUTO_SUBMIT=0`).

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
| R9 | **Auto-submit safety** — with `EINSTEIN_AUTO_SUBMIT=0` no submission occurs; with it armed, only A2-gate-passing records submit, all logged. | 0 spurious submits; audit log complete | `mb/logs/auto-submit.md` |

## What a NO-GO looks like

Any of: R1 > 0 (a crash escapes), R2 > 20% (the LLM path is unreliable enough that we're
mostly paying for fallback), R7 < 100% (captures are skippable → the loop drifts back to
discretionary), or R8 below bar (the loop spams the wiki). A NO-GO does not kill Phase 2 —
it routes back to a fix + re-pilot, and the failure modes get dead-end findings.

## See also

- `docs/agent/meta-learning-automation.md` — Gap 1 / Phase 2 in the full design.
- `scripts/autonomous_loop.py` — `_try_llm_path`, `inner_attempt`, `run_one_visit`.
- `docs/tools/{claude_headless,inner_agent_prompt,inner_agent_output,inner_agent_gates}.py`.
- `.claude/rules/axioms.md` — A2 auto-submit gate chain.
