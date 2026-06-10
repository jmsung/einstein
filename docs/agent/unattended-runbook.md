# Unattended-loop runbook — kill switches, cadence, weekly audit

**Status:** drafted 2026-06-09 (Phase 3 Goal 4, branch `js/feat/meta-learning-scheduler`).
Operational companion to `inner-agent-readiness.md` (the bar) and
`meta-learning-automation.md` (the design). **Live cron is gated on Goal 5's
promote-to-unattended verdict** — nothing below is installed until then.

## The stack (one line each)

| Layer | Entry | Guards owned there |
|---|---|---|
| cron | `scripts/scheduled_cycle.py` | runs/day cap (8), 7200s hard timeout, run ledger |
| loop | `scripts/autonomous_loop.py --one-problem --by-priority --skip-if-recent 45` | precheck (sentinel → kill switch → 5M-token/day budget → reachability → thermal), lockfile (exit 75), priority picker |
| inner agent | `claude -p` via `claude_headless` | 1800s/call timeout, tool allow-list, output schema |
| submission | `auto_submit` 6-gate chain (axioms.md) | strict-improvement, triple-verify, 1h throttle, 5/day cap, kill switch, audit log |

## Kill switches (fastest first)

| Action | Effect | Scope |
|---|---|---|
| `touch mb/.inner-agent-disabled` | precheck skips every visit until the file is removed; one gate-skip cycle-log row per attempt | everything (LLM + mechanical) |
| `EINSTEIN_INNER_AGENT=0` | LLM path off; visits proceed mechanically | LLM only |
| `EINSTEIN_AUTO_SUBMIT=0` | no submissions, everything else runs | submission only |
| `EINSTEIN_BANDIT=0` | bandit recommendation off | strategy hint only |
| `EINSTEIN_CONNECT_DOTS=0` | sibling-findings prompt section off | cross-pollination only |
| remove the cron entry | no new runs; in-flight run finishes (≤ 7200s) | cadence |

Escalation order when something looks wrong: **sentinel first** (stops the
bleeding, leaves an audit trail), diagnose from ledgers, then narrow to the
specific switch.

## Health monitor

```bash
uv run python docs/tools/scheduler_health.py        # exit 0 healthy / 1 unhealthy
```

Checks: last-run age vs cadence (default 6h), consecutive-failure streak
(≥3; exit 75 lock-skips are benign), trailing fallback rate vs R2 (≤0.20),
per-cycle runaway cost vs R5 ($5), sentinel presence. Cron it at half the
loop cadence and route non-zero exits to a notification.

Ledgers it reads (all under `mb/logs/`): `scheduler-runs.log` (scheduler),
`inner-agent-telemetry.jsonl` (per-cycle path/parse/cost),
`inner-agent-budget.md` (daily tokens), plus `mb/.inner-agent-disabled`.

Deeper digging: `docs/tools/monitor.py` (cycle-outcome dashboard),
`docs/agent/metrics.md` (compounding), `mb/logs/scheduler.log` (raw stdout).

## Cron spec (install only after Goal 5 GO)

```cron
# loop: every 2h (≤8 runs/day cap is belt-and-suspenders at 12 slots)
0 */2 * * *  cd <cb> && uv run python scripts/scheduled_cycle.py >> <mb>/logs/scheduler.log 2>&1
# health: hourly, alert on non-zero
30 * * * *   cd <cb> && uv run python docs/tools/scheduler_health.py >> <mb>/logs/health.log 2>&1
```

(Equivalent `schedule` skill / CronCreate definitions work too; the commands
are the contract, the carrier is not.)

## Weekly audit (human, ~15 min)

Per axioms.md submission-policy gate 6 ("Human reviews weekly"):

1. **Auto-submit audit** — read `mb/logs/auto-submit.md` for the week: every
   submit/reject must have a reason; any submit must trace to a gate-chain
   pass. Abuse → flip `EINSTEIN_AUTO_SUBMIT=0` and file a finding.
2. **Capture quality** — run `/wiki-audit` (or minimally
   `docs/tools/wiki_lint.py`): near-duplicates and uncited agent pages are
   the R8 drift signal. Spot-check 2-3 of the week's agent-authored findings.
3. **Ledger glance** — `scheduler_health.py` output, budget ledger trend,
   `docs/agent/promotion-log.md` for pending promotion candidates (human-gated).
4. **Wisdom check** — does `surface_cross_pollination` (logged per run) trend
   above zero? A flat zero for a week means the scheduler is grinding silos
   and the connect-the-dots section needs attention.

## Known operational gotchas

- `--skip-gates` silently disables the LLM path (no explicit LLM flag; the
  precheck is the enabler). Never use it in scheduled invocations. (Goal 0.)
- Dry runs skip the precheck entirely — kill-switch behavior cannot be
  verified with `--dry-run`; use the Phase-2 unit tests or a real run.
- Telemetry entries on P14 stamped 2026-06-10T01:53–01:57Z are test-leak
  artifacts (fixed in Goal 0); exclude them from R-metric recomputations.
