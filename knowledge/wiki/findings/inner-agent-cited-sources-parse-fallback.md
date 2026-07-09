---
type: finding
author: agent
drafted: 2026-06-09
question_origin: problem-meta
status: answered
related_problems: [14]
related_concepts: [meta-learning-automation]
cites:
  - docs/agent/inner-agent-readiness.md
  - docs/tools/inner_agent_output.py
  - docs/tools/inner_agent_telemetry.py
  - scripts/autonomous_loop.py
---

# Finding: strict `cited_sources` parsing forced inner-agent fallbacks

## Context

Phase 2 Goal 1 of `js/feat/meta-learning-inner-agent`: instrument the headless
LLM inner-agent path (`autonomous_loop._try_llm_path`) and run a ≥5-cycle
attended pilot on a low-risk problem (P14, `rank-2-frozen`) to surface
real-world failure modes before the Phase-3 scheduler. New per-cycle telemetry
(`docs/tools/inner_agent_telemetry.py`) made the readiness criteria in
`docs/agent/inner-agent-readiness.md` measurable.

## What the pilot found

The dominant failure mode is a **schema-validation fallback**, not a model or
compute problem. The inner agent, following the math-solving protocol, reads
prior `knowledge/wiki/findings/` pages and honestly lists them in the response's
`cited_sources` field. But `inner_agent_output.parse_response` required *every*
`cited_sources` entry to start with `knowledge/source/` — so one findings-path entry
raised `InnerAgentOutputError`, which `_try_llm_path` catches as a parse failure
and **falls back to the mechanical path**, discarding an otherwise-valid LLM
cycle (correct strategy, score, notes).

This happened on 2 of the first 5 pilot cycles — each time a *different*
findings page, confirming it's a recurring behavioral mismatch (the agent
reliably cites findings/concepts it actually read), not a one-off:

```
cycle 1: cited_sources[0] = knowledge/wiki/findings/p14-ae-tied-seed-at-f64-ceiling.md   → fallback
cycle 2: cited_sources[0] = knowledge/wiki/findings/p14-strict-tol-wire-fix-...md         → fallback
cycles 3-5: valid/empty cited_sources                                                → LLM path
```

## Why it failed (the obstruction)

`cited_sources` is an **optional, informational** field (defaults to `[]`,
added in research-synthesis G4) whose only consumer is the knowledge/source/-only
promotion-candidate detector. Yet it was validated as *strictly* as the
load-bearing path fields (`dead_end_finding`, `new_questions`, `wiki_writes`).
A single stray entry in a non-load-bearing field had the power to void a whole
cycle. The strictness bought nothing — the promotion detector already ignores
non-source/ paths — while costing a ~40% fallback rate.

## Measured numbers (readiness criteria, P14 pilot)

| Criterion | Pre-fix (N=5 P14 pilot) | GO bar | Expected post-fix |
|---|---|---|---|
| R1 unhandled exceptions | 0 | 0 | 0 |
| R2 fallback_rate | **0.40 ❌** | ≤ 0.20 | 0.0 (both fallbacks were this bug) |
| R3 parse_success | **0.60 ❌** | ≥ 0.90 | 1.0 (parser no longer raises on it) |
| R4 timeout_rate | 0.00 ✅ | ≤ 0.10 | 0.00 |
| R5 mean tokens/llm-cycle | 6692 ✅ | ≤ 250000 | ~6700 |
| mean wall-clock | 38.0s | — | ~40s |

The graceful-fallback contract held (R1=0: no crash escaped the loop), but R2/R3
failed — the loop was *safe* but *unreliable*, paying for a fallback on 40% of
cycles. R4/R5 passed comfortably; the LLM path is cheap (~7k tokens, ~40s).

**Why post-fix is "expected", not measured here:** both pre-fix fallbacks had
the identical, deterministic cause (a `knowledge/wiki/findings/...` entry in
`cited_sources`), which the fix removes — the parser no longer raises on it
(unit-tested in `test_inner_agent_output.py`), so `_try_llm_path` cannot take
the parse-error fallback for this reason. The authoritative post-fix *live*
numbers are produced by Goal 4's ≥8-cycle verdict pilot, which runs the fixed
code — re-running a separate post-fix pilot here would duplicate that. A quick
post-fix re-pilot was started and stopped once the fix path was confirmed, to
avoid burning ~30 min/cycle of redundant compute on a frozen problem.

## The fix

`inner_agent_output`: a new `_filter_path_list` used for `cited_sources` only —
a non-list is still a hard error (structurally malformed field), but individual
entries that aren't `knowledge/source/` strings are **dropped with a warning**
instead of raising. Load-bearing path fields stay strict. Result: a stray
citation degrades to "fewer cited sources," never a fallback.

## What this rules out / generalizes

- **Don't validate optional informational fields as strictly as load-bearing
  ones** in an agent's structured output. The blast radius of a strict check on
  a non-critical field is the *entire* cycle. Lenient-drop is the right policy
  for fields whose consumer already filters.
- The telemetry that caught this (`path_taken` + `llm_error_kind`) is the
  general mechanism: without the per-cycle ledger, a 40% silent fallback rate
  looked like "the loop ran fine" — every cycle still produced a cycle-log row.
  Measure the path taken, or graceful degradation hides unreliability.

## What might still work next

- Tighten the prompt to tell the agent `cited_sources` is `knowledge/source/`-only
  (belt-and-suspenders; the parser fix is the durable layer).
- Goal 3 will replace the `len(text)//4` token *estimate* with exact
  `--output-format json` envelope counts so R5 / `$/cycle` are exact.
- Goal 4 extends the pilot to ≥8 cycles for the GO/NO-GO verdict.
