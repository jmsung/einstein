# docs/ops/ — autonomous-loop deployment artifacts

Files here let you actually run the autonomous loop on a real Mac and walk
away — closes the user-facing "leave it running, come back later" promise
(Goal 7.8 in `mb/active/feat-autonomous-loop.md`).

## What lives here

- **`com.einstein.autonomous-loop.plist`** — macOS `launchd` template.
  Fires `scripts/autonomous_loop.py --max-problems 1 --skip-if-recent 60`
  every 30 minutes. Replace `__PROJECT_ROOT__` with your local checkout's
  absolute path before installing.

## Install (macOS)

```bash
# From the repo root:
PROJECT_ROOT="$(pwd)"
PLIST_LOCAL="docs/ops/com.einstein.autonomous-loop.plist"
PLIST_INSTALLED="$HOME/Library/LaunchAgents/com.einstein.autonomous-loop.plist"

# 1. Substitute the placeholder
sed "s|__PROJECT_ROOT__|$PROJECT_ROOT|g" "$PLIST_LOCAL" > "$PLIST_INSTALLED"

# 2. Bootstrap + enable for the GUI session
launchctl bootstrap "gui/$UID" "$PLIST_INSTALLED"
launchctl enable    "gui/$UID/com.einstein.autonomous-loop"

# 3. Verify
launchctl list | grep einstein
```

## Stop / uninstall

```bash
launchctl bootout "gui/$UID/com.einstein.autonomous-loop"
rm "$HOME/Library/LaunchAgents/com.einstein.autonomous-loop.plist"
```

## How to know it's working

- **Logs**: `mb/autonomous-loop.out.log` and `mb/autonomous-loop.err.log`
  (see `StandardOutPath` / `StandardErrorPath` in the plist).
- **Cycle log**: `docs/agent/cycle-log.md` — one new row every 30 min when
  the queue has live problems.
- **Daily budget**: `uv run python docs/tools/inner_agent_budget.py show`.
- **Macros notification**: when `auto_submit` accepts a new arena record,
  a native banner fires (Goal 7.8c — see `docs/tools/notify_milestone.py`).
- **Sentinel**: if cycle_runner detects a regression (wiki_lint hard fail),
  it drops `mb/.inner-agent-disabled`. Future cycles skip until you `rm`
  the file. The sentinel body records the cycle id + reason.

## Updating the plist after edits

`launchd` reads the plist file once at `bootstrap`-time; edits don't
propagate automatically. To pick up changes:

```bash
launchctl bootout "gui/$UID/com.einstein.autonomous-loop"
sed "s|__PROJECT_ROOT__|$(pwd)|g" docs/ops/com.einstein.autonomous-loop.plist \
  > "$HOME/Library/LaunchAgents/com.einstein.autonomous-loop.plist"
launchctl bootstrap "gui/$UID" "$HOME/Library/LaunchAgents/com.einstein.autonomous-loop.plist"
```

## Tunable knobs

Edit the plist before reinstalling — common adjustments:

| Knob | Where | Default | Notes |
|---|---|---|---|
| Cadence | `StartInterval` | 1800 (30 min) | Lower → more cycles, more token spend |
| Path to uv | `PATH` in `EnvironmentVariables` | Homebrew + system | `which uv` to check |
| Log paths | `StandardOutPath` / `StandardErrorPath` | `mb/*.log` | Rotate manually if they get huge |
| Run at load | `RunAtLoad` | `false` | Set `true` to fire immediately after `bootstrap` |

## Kill switches

| Switch | Effect | How to set |
|---|---|---|
| `EINSTEIN_INNER_AGENT=0` | Reverts to mechanical mode (skip LLM) | `EnvironmentVariables` in plist, or `launchctl setenv` |
| `mb/.inner-agent-disabled` | Skips the visit entirely | `touch mb/.inner-agent-disabled` |
| Bootout | Stop scheduling cycles | `launchctl bootout …` (above) |

## Meta-loop (Goal 6 of `js/feat/meta-loop`)

A second plist, `com.einstein.meta-loop.plist`, runs the meta-loop's
agentic proposer once a day (default 04:00 local). It's deliberately
*much* less frequent than the inner loop — the meta-loop only needs
new cycle artifacts to chew on, and those accumulate overnight.

Install:

```bash
PROJECT_ROOT="$(pwd)"
sed "s|__PROJECT_ROOT__|$PROJECT_ROOT|g" docs/ops/com.einstein.meta-loop.plist \
  > "$HOME/Library/LaunchAgents/com.einstein.meta-loop.plist"
launchctl bootstrap "gui/$UID" "$HOME/Library/LaunchAgents/com.einstein.meta-loop.plist"
launchctl enable    "gui/$UID/com.einstein.meta-loop"
```

The meta-loop has its own kill switch: `EINSTEIN_META_LOOP=0` rejects
every proposal at the gate chain (audit row still written). Separate
from `EINSTEIN_INNER_AGENT` so you can pause one without the other.

Outputs:

- **Diagnostic** — `mb/logs/meta-loop-report.md` (refreshed on every run)
- **Pending proposals** — `mb/proposals/pending/<id>.md`
- **Audit log** — `mb/logs/meta-proposals.md`
- **Token budget** — `mb/logs/meta-loop-budget.md`
- **Shadow runs** — `mb/logs/meta-shadow-runs.md` (operator-initiated; not from the daily plist)

Review pending proposals each morning:

```bash
uv run python scripts/meta_loop.py review --list      # quick triage
uv run python scripts/meta_loop.py review             # interactive
```

## Non-macOS

`launchd` is macOS-only. For Linux, use `systemd --user` timers or `cron`.
The `--skip-if-recent` + lockfile semantics in `autonomous_loop.py` work
across schedulers; only the plist is macOS-specific.

## Related

- `.claude/rules/cycle-discipline.md` — what every cycle must produce
- `mb/active/feat-autonomous-loop.md` — branch-level design + status
- `docs/tools/cycle_runner.sh` — per-cycle housekeeping (incl. sentinel drop)
- `docs/tools/inner_agent_gates.py` — kill switch + sentinel + budget gates
- `docs/tools/inner_agent_budget.py` — CLI for the budget ledger
- `docs/tools/notify_milestone.py` — macOS notification helper
