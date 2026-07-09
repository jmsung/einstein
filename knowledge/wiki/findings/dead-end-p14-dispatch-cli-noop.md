---
type: finding
author: agent
drafted: 2026-05-27
question_origin: problem-14
status: answered
related_concepts: [float64-ceiling, arena-tolerance-drift]
cites:
  - src/einstein/optimizer_dispatch.py
  - src/einstein/optimizer_manifest.yaml
  - scripts/circle_packing_square/newton_max.py
  - scripts/circle_packing_square/slsqp_polish.py
  - docs/wiki/findings/p14-manifest-wire-fix-verified.md
  - docs/wiki/findings/dead-end-newton-max-strict-tol-lockout-p14.md
---

# Dead end: the autonomous loop's sanctioned P14 execution channel is a no-op

> **RESOLVED 2026-06-01** (branch `js/feat/manifest-coverage-sprint`). All three
> wiring breaks are fixed: (1) `optimizer_dispatch.py` now has an `argparse`
> `main()` that prints the `DispatchResult` as JSON and sets the exit code; (2)
> the broken `newton_max` manifest entry was **dropped** (it emitted `sum_r` to a
> gitignored path and defaulted to the rejected tolerance exploit); `slsqp_polish`
> + `mpmath_ulp_polish` cover P14. The sanctioned `-m einstein.optimizer_dispatch`
> command is now real end-to-end. Closes question
> `2026-05-27-optimizer-dispatch-cli-entrypoint`. The finding below is kept as the
> diagnosis-of-record.

## What we tried

Autonomous-loop cycle (2026-05-27, attempt 2/3) tried to run a strict-disjoint
optimizer for P14 *through the sanctioned channel* — the command the cycle task
and `slsqp_polish.py`'s own docstring (line 28) both prescribe:

```
uv run python -m einstein.optimizer_dispatch --problem-id 14 --strategy newton_max
```

Ran it twice. Both times: **exit 0, zero stdout, no result file written.**

## Why it failed — three independent wiring breaks

1. **`optimizer_dispatch.py` has no CLI entrypoint.** `grep` for
   `__main__ | argparse | def main | sys.argv | ArgumentParser` → no matches.
   The module defines `dispatch()` as a *library function* (called
   programmatically by `autonomous_loop.py`) but has no `if __name__ ==
   "__main__"` block. Running it with `python -m …` executes only the
   top-level `def`s, then exits 0 silently. The `--problem-id`/`--strategy`
   flags are swallowed by Python's `-m` machinery and ignored. **The
   sanctioned command does nothing.**

2. **The `newton_max` manifest entry cannot parse even if (1) were fixed.**
   - manifest `result_file: results/circle_packing_square/newton_max_result.json`,
     but `newton_max.py --output` defaults to `results-temp/p14_newton.json`
     and the manifest's `cli_args: ["--pair-gap","0"]` never passes `--output`.
   - manifest `cli_args` never passes `--base`, so the script falls back to
     `--base results-temp/p14_top.json`, which **does not exist** (`results-temp/`
     is absent in the worktree) → the script raises at `open()` → exit 1.
     *This is the actual root cause of cycles 47–48's "exit code 1", not the
     strict-tol issue the cycle-49 narrative inferred.*
   - `newton_max.py` writes `{"circles":…, "sum_r":…, "pair_gap":…}` — it has
     **no `score` key**, so the `json_score_payload` parser would reject it
     ("result_file missing required 'score' field") even on a clean run.

3. **Direct script invocation is not in the autonomous toolset whitelist.**
   `uv run python scripts/circle_packing_square/newton_max.py …` requires
   approval — outside `Bash(qmd:*)`, `Bash(gap_search.py:*)`,
   `Bash(uv run python -m einstein.optimizer_dispatch:*)`. So the autonomous
   agent literally cannot reach the working code path through permitted tools.

## The verification-integrity hazard

A stale `results/circle_packing_square/slsqp_polish_result.json` (score
2.6359830849175245) was present from a prior direct/programmatic run. A naive
cycle that runs the no-op `-m` command and then reads that file would report
2.6359830849175245 as **this cycle's fresh output** — a phantom execution.
This is precisely the local↔ground-truth drift `triple-verify` and
`agent-stance` (objective > subjective) exist to catch. This cycle refused to
claim the stale file; hence `score: null`.

## Correction to `p14-manifest-wire-fix-verified.md` (cycle 52)

That finding's *result* claim is real — `slsqp_polish.py` run **directly**
(or via the programmatic `dispatch()` from `autonomous_loop.py`) does produce
the strict-tol-verified 2.6359830849175245. But its *mechanism* claim — that
it ran `uv run python -m einstein.optimizer_dispatch … --strategy slsqp_polish`
end-to-end — is not reproducible: that CLI is a no-op. And its claim that
`newton_max` "stays available but disarmed … even an explicit `--strategy
newton_max` runs strict-disjoint" is false: that path can't parse. The wire-fix
was **half-done** — the optimizer script is correct, the dispatch/manifest
plumbing around it is not.

## What this rules out

- Reporting any P14 score from an autonomous cycle that only used the
  sanctioned `-m` channel — the channel cannot execute anything.
- Trusting `dispatch-failed` vs `no-op` cycle outcomes as signal about the
  *problem*; they are signal about *plumbing*.

## What might still work (out of this cycle's write scope — `src/`, `scripts/`)

- Add an `argparse` `main()` to `optimizer_dispatch.py` (`--problem-id`,
  `--strategy`, print the `DispatchResult` as JSON, `raise SystemExit(0/1)`).
- Either fix the `newton_max` manifest entry (`cli_args` must pass a real
  `--base` seed and an `--output` equal to `result_file`; teach the script to
  emit a `score` key) **or** drop the entry and keep `slsqp_polish` the sole
  P14 optimizer.
- The score itself stays float64-ceiling-locked at 2.6359830849175245
  regardless (rank #2). This finding is about execution integrity, not headroom.

## See also

- [p14-manifest-wire-fix-verified](p14-manifest-wire-fix-verified.md) — the
  finding this corrects.
- [dead-end-newton-max-strict-tol-lockout-p14](dead-end-newton-max-strict-tol-lockout-p14.md)
- [float64-ceiling](float64-ceiling.md)
- [verify-seed-dispatch-pattern](verify-seed-dispatch-pattern.md) — the wiring that resolved this.
