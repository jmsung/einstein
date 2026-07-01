# Tail+Headroom batch — monitor & resume note

Worktree: `cb-feat-ablation-tail-headroom`. Launched 2026-06-30 14:05.
Both experiments are **resumable** and **disconnect-safe** (offline/rate-limit cells fail-fast,
are NOT recorded, and retry on the next run — never recorded as bogus nulls).

Run all commands from inside the worktree:
```bash
cd /Users/jmsung/projects/einstein/cb-feat-ablation-tail-headroom
```

## Monitor
```bash
# is it alive? (and is the mac kept awake?)
pgrep -fl run_tail_headroom && pgrep -fl caffeinate

# step boundaries (memory-tail -> headroom-transfer -> DONE)
cat results/tail-headroom/master.log

# progress
wc -l results/memory-tail/records.jsonl          # of 120 cells (Test 1)
wc -l results/transfer-xhard/transfer-records.jsonl  # of ~16 cells (Test 3, starts after Test 1)

# done?
cat results/tail-headroom/DONE 2>/dev/null && echo COMPLETE || echo "still running / stopped"
```

## Resume after a network hold (or any stop)
The orchestrator may exit early if the network drops for a while (it burns through remaining
cells failing-fast, records none of them, and ends). Nothing is corrupted. To continue:
```bash
# 1. make sure it's not already running
pgrep -fl run_tail_headroom    # if it prints a pid, it's still going — do nothing

# 2. if stopped, just re-launch — it SKIPS every completed cell and retries the rest
nohup bash scripts/run_tail_headroom.sh >/dev/null 2>&1 &
```
Re-run as many times as needed (after each network outage). It always resumes from
`records.jsonl`; completed cells are never re-run.

## Stop it
```bash
pkill -f run_tail_headroom; pkill -f run_memory_tail; pkill -f run_transfer_ablation
```

## Caveat (same credential)
The `claude -p` cells share the Claude subscription with any interactive Claude Code session.
While you actively use Claude Code in another window they contend — progress slows (safe, just
slower). For full speed, leave it alone while it runs.

## Outputs (the verdicts)
- Test 1 (memory tail): `results/memory-tail/tail-summary.json` — mean/p90/max/near-solve for
  cold vs warm + warm−cold Δ with bootstrap CIs. Question: does warm fatten the UPPER tail?
- Test 3 (headroom transfer): `results/transfer-xhard/solve-rate-delta.json` +
  `transfer-records.json` — warm−cold on circles-60/80 (true Packomania optima).
- Both feed the paper's §7 "what would settle it" (docs/paper-ablation-integration branch).

## Expected scale
Test 1 ~7–13h (120 cells; haiku often finishes before the 400s cap). Test 3 ~4–6h (Sonnet).
~Total under a day continuous; spans 2 nights if interrupted.
