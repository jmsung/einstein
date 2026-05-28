---
type: finding
author: agent
drafted: 2026-05-27
question_origin: branch-js-chore-meta-loop-swap-surface
status: answered
related_concepts: []
related_techniques: []
related_personas: []
cites:
  - ../../../src/einstein/meta_loop/propose.py
  - ../../../src/einstein/meta_loop/proposals.py
  - ../../../src/einstein/meta_loop/meta_gate.py
  - meta-loop-design-from-literature.md
---

# Meta-loop proposer swap surface — the Callable contract is the plug point

## TL;DR

The meta-loop is "modular for the family of meta-learners that emit diffs." The
single swap point for that family is one function type:

```python
Callable[[ProposerInput], list[dict]]
```

A proposer is *any* callable that reads a `ProposerInput` and returns a list of
raw proposal dicts. `propose.run(proposer=...)` injects it; `_coerce_raw` +
`Proposal._validate()` + the 6-gate chain (`meta_gate.evaluate`) handle the rest
identically regardless of who produced the dict. To add a non-LLM proposer
(bandit, evolutionary, heuristic) you write one callable and tag it with a
`proposer_id` — no change to the schema, the store, the gates, or the audit log.

Two cheap edits on `js/chore/meta-loop-swap-surface` widened this surface
*before* the first non-LLM proposer (`skill-bandit`) lands:

1. **`proposer_id: str` provenance** on every `Proposal` and every audit row.
2. **Externalized proposer prompt** (`docs/agent/proposer_prompts/metaharness-v1.md`,
   loaded via `run(prompt_path=...)`), so the LLM proposer is A/B-able by file,
   not by code edit.

## The contract, precisely

`ProposerInput` (in `propose.py`) is everything a proposer is handed:

| field | meaning |
|---|---|
| `report_text` | rendered diagnostic (the launchpad, not a substitute for raw files) |
| `cycle_log_path`, `skill_library_path`, `findings_dir`, `questions_dir`, `mb_logs_dir` | raw filesystem roots the proposer may read |
| `allowed_types` | the proposal types the gate chain will accept |
| `prompt_path` | system-prompt file (LLM proposers); non-LLM proposers ignore it |

The proposer returns `list[dict]`, where each dict is a raw proposal with keys
matching the `Proposal` schema (`type`, `target_path`, `proposed_diff`,
`evidence_cycles`, `expected_metric_delta`, `predicted_regressions`,
`confidence`, `requires_shadow`, `rationale`, and optionally `proposer_id`).
Everything downstream — coercion, validation, target-path policy, the 6 gates,
the audit row — is proposer-agnostic. **That is the whole point: the proposer is
the only part that changes.**

## `proposer_id` convention

Free-text, not an enum — a new proposer kind must not require editing a closed
type. Convention: `<approach>-<variant>`.

- `metaharness-llm-v1` — the default LLM proposer (`_coerce_raw` tags this when a
  raw dict carries no `proposer_id`; see `DEFAULT_PROPOSER_ID` in `propose.py`).
- `thompson-bandit-v0` — a future skill-bandit proposer.
- `evo-island-v0`, `heuristic-stagnation-v1` — further proposers.

Empty `proposer_id` is written to the audit log as `(legacy)` — it disambiguates
rows from before the column existed (the migration shim in
`meta_gate._parse_audit_log`). Once `skill-bandit` lands, the audit log answers
"which proposer produced this proposal?" from row one — no backfill, no gap.

## Three worked examples (one callable each)

### 1. LLM / metaharness (the default, already shipped)

`_default_proposer` shells out to `claude_headless` with the rendered prompt,
parses a fenced JSON array, returns it. `proposer_id` defaults to
`metaharness-llm-v1`. The prompt is now a file, so a `metaharness-v2.md` is a
new-file + `run(prompt_path=...)` A/B — zero code change.

### 2. Thompson bandit (skill-bandit, next-but-one branch)

```python
def thompson_proposer(inp: ProposerInput) -> list[dict]:
    arms = parse_skill_library(inp.skill_library_path)      # tried/top3/finding counts
    arm = sample_thompson(arms)                              # Beta posterior per technique
    return [{
        "type": "manifest_tweak",
        "target_path": "src/einstein/<problem>/manifest.yaml",
        "proposed_diff": render_manifest_diff(arm),
        "evidence_cycles": arm.recent_cycles,
        "predicted_regressions": ["bandit explore step may pick a worse arm"],
        "confidence": "low",
        "proposer_id": "thompson-bandit-v0",
    }]
```

No LLM call, no prompt. It reads the same `ProposerInput`, emits the same dict
shape, and the same gates judge it. The bandit's exploration is *inside* the
callable; the harness doesn't know or care.

### 3. Evolutionary / heuristic (illustrative)

```python
def stagnation_heuristic(inp: ProposerInput) -> list[dict]:
    if not detect_stagnation(inp.cycle_log_path):           # pure rule, no model
        return []                                           # honest empty is correct
    return [{
        "type": "queue_reorder",
        "target_path": "scripts/autonomous_loop.py",
        "proposed_diff": demote_stalled_problem_diff(inp.cycle_log_path),
        "evidence_cycles": last_n_cycle_ids(inp.cycle_log_path, n=5),
        "predicted_regressions": ["may starve a problem that was about to break"],
        "confidence": "medium",
        "proposer_id": "heuristic-stagnation-v1",
    }]
```

Same contract. A genetic/island proposer that mutates manifest params across a
population is the same shape: callable in, `list[dict]` out, `proposer_id` tags
the lineage.

## Deliberate non-abstraction (record so a future reader doesn't "helpfully" add it)

- **No `AbstractProposer` class hierarchy.** The free `Callable` *is* the swap
  point. A class hierarchy buys nothing until ≥2 concrete proposer types share
  behavior worth factoring — and even then, a shared *helper module* beats a base
  class. Adding the hierarchy now would constrain the action surface before we
  know its real shape (`agent-stance.md`: scalable > toy, but also: don't
  pre-abstract on day one — extract from evidence, like AEVO's post-hoc split).
- **No `MetaPolicy` interface for non-proposal paradigms** (runtime steering,
  self-rewriting). Those aren't diff-shaped; speculating an interface now would
  constrain the wrong axis. Add only when a real non-diff-shaped approach lands.

The widening, not wrapping, stance: we widened the `Callable` contract (added
`prompt_path` to `ProposerInput`, `proposer_id` to `Proposal`) rather than wrap
it in ceremony. The diff stays minimal; the family stays evolvable.

## What this rules out / what it enables

- **Rules out**: needing a code change to the schema/store/gates when a new
  proposer arrives. If a future proposer *does* force such a change, that's the
  signal the contract was too narrow — revisit then, with the concrete case in
  hand.
- **Enables**: shadow A/B *across proposers* (Goal 5 harness), since every
  proposal now self-identifies; prompt A/B *within* the LLM proposer; and a clean
  audit answer to "who proposed this?" from the first non-LLM proposal onward.

## See also

- [meta-loop-design-from-literature](meta-loop-design-from-literature.md) — the 7-paper synthesis this branch implements; "edit the mechanism, not the next candidate."
- `src/einstein/meta_loop/propose.py` — `ProposerInput`, `_default_proposer`, `run(proposer=, prompt_path=)`, `DEFAULT_PROPOSER_ID`.
- `src/einstein/meta_loop/proposals.py` — `Proposal.proposer_id`, schema + store.
- `src/einstein/meta_loop/meta_gate.py` — 6-gate chain + audit-log `proposer_id` column + legacy migration shim.
- Branch: `js/chore/meta-loop-swap-surface` — `mb/active/js-chore-meta-loop-swap-surface.md`.
