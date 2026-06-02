# Record campaign — operations runbook

The **autonomous record campaign** (Phase 4) runs the full stack — bandit +
research-synthesis + autosynth/body-writer + auto-submit — on a `launchd`
schedule, over the audited input set, 24/7. This page is install /
kill-switch / what-to-do-when-it-breaks.

**This is the highest-blast-radius deployment in the repo.** It can submit to
the live arena without a human in the loop. The safety is the
[axioms](../../.claude/rules/axioms.md) gate chain, not a person watching — so
the gates, the monitor, and the kill switches below are load-bearing. Read this
whole page before flipping `EINSTEIN_AUTO_SUBMIT=1`.

## What lives here

| File | Role |
|---|---|
| `com.einstein.record-campaign.plist` | launchd template: `autonomous_loop.py --max-problems 3` every 30 min, daily-rotated log. Ships `EINSTEIN_AUTO_SUBMIT=0`. |
| `record-campaign-input-set.md` | Goal 0 audit — the 5 problems (P5, P11, P14, P15, P19) the campaign targets, with inclusion criteria. |
| `../../scripts/record_campaign_monitor.py` | Health monitor — alerts on triple-verify mismatch, dispatch-failure streaks, or auto-submit over cap. |

## The two phases (do not skip the dry-run)

The plist ships with `EINSTEIN_AUTO_SUBMIT=0` on purpose. Bring the campaign up
in two phases:

1. **Dry-run (24h, `AUTO_SUBMIT=0`)** — the loop runs full-stack but *cannot*
   submit. Confirm the cycle log fills with sensible rows and the monitor stays
   all-clear. This is Goal 4's gate.
2. **Live (`AUTO_SUBMIT=1`)** — only after the dry-run passes. Flip the env var
   in the installed plist and reload (see "Updating the plist"). Record the flip
   in `mb/logs/record-campaign-gate.md`.

## Install (macOS)

```bash
# From the cb worktree root:
PROJECT_ROOT="$(pwd)"
PLIST_LOCAL="docs/ops/com.einstein.record-campaign.plist"
PLIST_INSTALLED="$HOME/Library/LaunchAgents/com.einstein.record-campaign.plist"

# 1. Substitute the placeholder
sed "s|__PROJECT_ROOT__|$PROJECT_ROOT|g" "$PLIST_LOCAL" > "$PLIST_INSTALLED"

# 2. Bootstrap + enable for the GUI session
launchctl bootstrap "gui/$UID" "$PLIST_INSTALLED"
launchctl enable    "gui/$UID/com.einstein.record-campaign"

# 3. Verify
launchctl list | grep record-campaign
```

## Stop / uninstall

```bash
launchctl bootout "gui/$UID/com.einstein.record-campaign"
rm "$HOME/Library/LaunchAgents/com.einstein.record-campaign.plist"
```

## Updating the plist after edits (e.g. flipping AUTO_SUBMIT)

`launchd` reads the plist once at `bootstrap`-time; edits don't propagate.
After editing the local template (or to flip `EINSTEIN_AUTO_SUBMIT`):

```bash
launchctl bootout "gui/$UID/com.einstein.record-campaign"
sed "s|__PROJECT_ROOT__|$(pwd)|g" docs/ops/com.einstein.record-campaign.plist \
  > "$HOME/Library/LaunchAgents/com.einstein.record-campaign.plist"
# (edit EINSTEIN_AUTO_SUBMIT in the installed file to 1 here, or edit the
#  template before the sed above)
launchctl bootstrap "gui/$UID" "$HOME/Library/LaunchAgents/com.einstein.record-campaign.plist"
```

## Kill switches (axioms gate 5)

All three revert behavior cleanly; set in the plist `EnvironmentVariables` (then
reload) or `launchctl setenv` for an immediate session-wide override.

| Switch | Effect | Set |
|---|---|---|
| `EINSTEIN_AUTO_SUBMIT=0` | No arena submissions (dry-run). The big one. | plist / `launchctl setenv` |
| `EINSTEIN_BANDIT=0` | Static technique selection (no Thompson sampling) | plist |
| `EINSTEIN_INNER_AGENT=0` | Mechanical mode — skip the LLM dispatch entirely | plist |
| `mb/.inner-agent-disabled` | Skip every visit until removed (regression sentinel) | `touch` / auto-dropped |
| Bootout | Stop scheduling cycles altogether | `launchctl bootout …` |

## Monitoring

Run the health monitor on a schedule (cron / a sibling launchd plist) or by
hand. It exits non-zero and fires a macOS notification per alert:

```bash
uv run python scripts/record_campaign_monitor.py           # check + notify
uv run python scripts/record_campaign_monitor.py --quiet   # exit code only (for cron)
```

It alerts on:

- **(a) triple-verify mismatch** — a genuine evaluator disagreement (axiom A1),
  or the `mb/.inner-agent-disabled` sentinel being present.
- **(b) ≥5 consecutive `blocked` cycles on one problem** — the loop is stuck.
- **(c) auto-submit rate over the daily cap** — more `submitted` rows today than
  the cap (default 5).

Eyeball signals:

- **App log**: `mb/logs/record-campaign-YYYY-MM-DD.log` (one file per day).
- **launchd log**: `mb/logs/record-campaign.launchd.{out,err}.log`.
- **Cycle log**: `docs/agent/cycle-log.md` — new rows as the loop runs.
- **Auto-submit audit**: `mb/logs/auto-submit.md` — every submit/reject decision.
- **Daily budget**: `uv run python docs/tools/inner_agent_budget.py show`.

## When something breaks

| Symptom | Likely cause | Action |
|---|---|---|
| Monitor fires **triple-verify mismatch** | A score disagrees across evaluators (axiom A1) — or the loop already self-disabled | **Stop.** Do not submit. The score is fake until debugged. The auto-submit gate already rejected it; write a finding (`failure-is-a-finding`). `rm mb/.inner-agent-disabled` only after the cause is fixed. |
| Monitor fires **dispatch failures** | A problem's optimizer/manifest is broken | Inspect the app log for that problem; fix the manifest/dispatch or set `in_active_queue: false` to park it. |
| Monitor fires **auto-submit over cap** | Throttle/cap logic misbehaving, or genuine burst | Set `EINSTEIN_AUTO_SUBMIT=0` immediately; inspect `mb/logs/auto-submit.md`. |
| No new cycle-log rows | launchd not firing, or lock stuck | `launchctl list | grep record-campaign`; check `.err.log`; remove a stale lockfile if present. |
| Runaway token spend | Cadence too high or K too high | Lower `StartInterval`/`EINSTEIN_PARALLEL_K`; check `inner_agent_budget.py show`. |

## Auto-submit gate chain (axioms, revised 2026-05-24)

Auto-submission requires **all six** gates to pass; otherwise the candidate is
logged for human review. Summary — the canonical text is
[`.claude/rules/axioms.md`](../../.claude/rules/axioms.md):

1. **Strict improvement over arena #1** (≥ per-problem `minImprovement`).
2. **Triple-verify passes** (axiom A1) — any 2-way disagreement blocks + files a finding.
3. **1-hour throttle** per problem (`mb/logs/auto-submit.md` is source of truth).
4. **Daily cap** (default 5 across all problems).
5. **Kill switch** — `EINSTEIN_AUTO_SUBMIT=0` disables everything.
6. **Audit log mandatory** — every decision appended to `mb/logs/auto-submit.md`.

Everything outside "new arena record" still needs human approval (polish below
#1, tied-SOTA floors, anything triple-verify flagged, hidden/retired problems).

## Non-macOS

`launchd` is macOS-only. On Linux use `systemd --user` timers or `cron`; the
`--skip-if-recent` + lockfile semantics in `autonomous_loop.py` are
scheduler-agnostic. Only the plist is macOS-specific.

## Related

- [`record-campaign-input-set.md`](record-campaign-input-set.md) — the target problems
- [`README.md`](README.md) — the base autonomous-loop deployment (this builds on it)
- [`.claude/rules/axioms.md`](../../.claude/rules/axioms.md) — A1 triple-verify + the gate chain
- [`.claude/rules/triple-verify.md`](../../.claude/rules/triple-verify.md) — the verification procedure
- `mb/active/js-feat-autonomous-record-campaign.md` — branch design + status
