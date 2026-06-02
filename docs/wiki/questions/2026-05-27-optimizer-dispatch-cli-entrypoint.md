---
type: question
author: agent
drafted: 2026-05-27
asked_by: autonomous_loop
status: answered
answer_finding: docs/wiki/findings/verify-seed-dispatch-pattern.md
related_problems: [14, 22]
related_concepts: [float64-ceiling]
cites:
  - src/einstein/optimizer_dispatch.py
  - src/einstein/optimizer_manifest.yaml
  - docs/wiki/findings/dead-end-p14-dispatch-cli-noop.md
---

> **ANSWERED 2026-06-01** (branch `js/feat/manifest-coverage-sprint`).
> **Q-A — yes, add the CLI.** `optimizer_dispatch.py` now has an `argparse`
> `main()` that runs `dispatch()`, prints the `DispatchResult` as JSON, and sets
> the exit code (0 ok / 1 fail; `--dry-run` is an informational 0). This makes
> the whitelisted `python -m einstein.optimizer_dispatch` command real — it was a
> silent no-op before, so the entire manifest (not just P14) was unreachable.
> **Q-B — drop `newton_max`.** It emitted `sum_r` (not `score`) to a gitignored
> `results-temp/` path and defaulted to the rejected `--pair-gap=-9e-10` exploit;
> unfixable cheaply and unsafe. `slsqp_polish` (default) + `mpmath_ulp_polish`
> cover P14. See [verify-seed-dispatch-pattern](../findings/verify-seed-dispatch-pattern.md).

# Should `optimizer_dispatch.py` expose a CLI, and should the broken `newton_max` manifest entry be fixed or dropped?

## The question

The autonomous loop's per-problem execution is documented (in cycle tasks and
in `slsqp_polish.py`'s docstring) as:

```
uv run python -m einstein.optimizer_dispatch --problem-id <id> --strategy <name>
```

But `optimizer_dispatch.py` has **no `__main__`/argparse block** — that command
is a silent no-op (exit 0, no output, no result file). See
[`dead-end-p14-dispatch-cli-noop`](../findings/dead-end-p14-dispatch-cli-noop.md).
Only the *programmatic* `dispatch()` function works, and direct optimizer-script
invocation is outside the autonomous toolset whitelist. **Net effect: an
autonomous cycle cannot execute any optimizer for any manifest problem through
its permitted tools** — this is not P14-specific (P22's `stub_no_op` is equally
unreachable via the CLI).

**Question A**: Add an `argparse` `main()` to `optimizer_dispatch.py` that runs
`dispatch(problem_id, strategy)` and prints the `DispatchResult` as JSON + sets
the exit code? (This makes the whitelisted command real and lets cycles report
genuine scores instead of risking phantom-execution off stale result files.)

**Question B**: For the `newton_max` P14 entry — fix it (pass a real `--base`
seed + `--output` == `result_file`; emit a `score` key) or drop it, leaving
`slsqp_polish` as the sole P14 optimizer? The entry currently cannot parse
under `json_score_payload` regardless of `--pair-gap`.

## Why this matters

- It is a **cross-cutting integrity gap**: every future autonomous cycle on a
  manifest-wired problem either no-ops or, worse, misreads a stale result file
  as fresh output. Fixing the CLI is the difference between the autonomous loop
  measuring real optimizer runs and measuring nothing.
- It is the prerequisite for the open
  [`2026-05-25-p14-mpmath-ulp-polish-wiring`](2026-05-25-p14-mpmath-ulp-polish-wiring.md)
  question — wiring a new optimizer block is pointless if the dispatch channel
  that would invoke it is a no-op.

## Next step

A wiring task (NOT research, and outside the autonomous agent's `src/`+`scripts/`
write scope): add the CLI entrypoint to `optimizer_dispatch.py`, reconcile the
`newton_max` manifest entry, then re-run a P14 cycle through the sanctioned
command and confirm a non-stale `slsqp_polish_result.json` with a fresh mtime.
</content>
