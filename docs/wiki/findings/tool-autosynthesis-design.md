---
type: finding
author: agent
drafted: 2026-05-31
question_origin: branch-js-feat-tool-autosynthesis
status: answered
related_concepts: []
related_techniques: []
related_personas: []
cites:
  - ../../source/2026-lee-meta-harness-end-to-end-optimization-model.md
  - ../../source/2026-ning-code-as-agent-harness.md
  - ../../source/2026-lin-agentic-harness-engineering-ahe.md
  - ../../source/2026-ma-skillclaw-let-skills-evolve.md
  - ../../source/2026-xia-skillrl-evolving-agents-recursive.md
  - ../../source/2025-zhang-darwin-godel-machine-open-ended.md
  - meta-loop-design-from-literature.md
  - meta-loop-swap-surface.md
  - recursive-meta-design.md
  - research-synthesis-design.md
---

# Tool autosynthesis design — `code_edit` proposal type, grounded

## TL;DR

`code_edit` is the proposal type that lets the meta-loop **draft a new
optimizer script** when the inner agent repeatedly hits the same tool gap
(no manifest entry, no script for technique X). Tighter gates than
`meta_self_edit` because the blast radius is a fresh dispatchable artifact:

- **Recurrence threshold ≥ 3 cycles across ≥ 2 problems** before the
  proposer fires (vs ≥ 10 for `meta_self_edit`, ≥ 3 for `rule_edit`). Lower
  than `meta_self_edit` because the artifact is sandboxed; higher than
  `rule_edit` because the artifact is *executable*.
- **Drafts land in `scripts/proposed/<tool>.py`, not `scripts/`.** Promotion
  = mv + manifest wire + tests + shadow A/B. The two-directory pattern
  matches Lin AHE's "file-level edits with git-versioned rollback"
  ([2026-lin-agentic-harness-engineering-ahe.md](../../source/2026-lin-agentic-harness-engineering-ahe.md):
  Section 3).
- **Mandatory sandbox validator** before any shadow run (ruff + import +
  colocated tests; NEVER dispatches to a live problem).
- **Mandatory shadow A/B** with a citation-grounded "A-arm actually used
  the tool AND produced a finding" promotion criterion.
- **Never auto-merge** — the submission-policy gate chain
  ([axioms A1–A4 + submission policy](../../../.claude/rules/axioms.md))
  does not extend here. Human approval is the final gate.

This finding grounds those choices in the literature and the existing
einstein meta-loop. The implementation lives across G1–G6 on this branch.

## Why this is more dangerous than `rule_edit`, less than `meta_self_edit`

| | `rule_edit` | `code_edit` | `meta_self_edit` |
|---|---|---|---|
| Touches | `.claude/rules/*.md` | `scripts/proposed/*.py` → `scripts/*.py` | `scripts/meta_loop.py` |
| Worst case | bad guidance → 1 bad cycle, dead-end filed | broken optimizer dispatched against a problem → wasted cycle, false score | proposer/gate weakens itself ([2025-zhang-darwin-godel-machine-open-ended.md](../../source/2025-zhang-darwin-godel-machine-open-ended.md): node-114 Goodhart) |
| Sandbox before live | n/a (markdown) | **ruff + import + colocated tests** | n/a (uses shadow A/B) |
| Recurrence floor | ≥ 3 cycles | ≥ 3 cycles, ≥ 2 problems | ≥ 10 cycles |
| Auto-promote? | No (gate chain) | No (validator + shadow + human) | No (queue for human review) |

The new risk vector `code_edit` introduces vs `rule_edit`: the artifact is
**dispatchable**. A bad rule mis-guides one cycle; a bad script can be picked
up by the strategy_picker and burn compute against a real problem, producing
a score the triple-verify gate then has to catch. The sandbox validator
forecloses the "broken script ever reaches dispatch" path by construction.

The reduced risk vector vs `meta_self_edit`: the artifact is **additive**.
`scripts/proposed/<tool>.py` cannot regress the existing manifest until the
promotion step explicitly wires it. Compare this to `scripts/meta_loop.py`
where every edit ships immediately as the next driver run. Additive-only is
what lets the recurrence floor drop from 10 to 3.

## Gap-detector heuristics (Goal 1)

A *tool gap* is a recurring failure mode in the cycle-log notes column where
the inner agent could have dispatched if a script existed but couldn't. The
detector parses `docs/agent/cycle-log.md` (and open questions tagged
`tool-gap`) for these markers — they were inventoried directly from real
cycle-log rows on this branch (cycles 45–51):

| Marker | Example cycle-log note |
|---|---|
| `dispatch-failed` | `dispatch-failed: optimizer exited with code 1` (cycle 47) |
| `dispatch: no-manifest-entry` | `dispatch: no-manifest-entry` (cycles 45, 46) |
| `manifest only exposes ...` | `manifest only exposes newton_max (strict-tol-failing per exp log)` (cycle 49) |
| `not yet wired into ... manifest` | `mpmath-ulp-polish (novel; not yet wired into P14 manifest)` (cycle 49) |
| `(no library matches — council needed)` | recurring across cycles 35, 45–48 |

Canonical-form clustering: gaps with the same *suggested script name* OR
the same *missing manifest entry* OR the same *(category, technique)* pair
cluster into one `ToolGap` record. The detector counts (citing cycles,
distinct problem ids) per cluster.

**Threshold rationale**: a single occurrence is noise (a one-off `category=X
prior=novel.md(0.50)` strategy whose script the inner agent might still
write next cycle). ≥ 3 cycles is the same floor `rule_edit` uses. The
extra requirement ≥ 2 *distinct* problem ids prevents "one problem
repeatedly hits the same gap → looks like 3 cycles but is just one stuck
cycle" — the recurrence has to *generalize* before the proposer fires.

The detector is **read-only**, mirrors `diagnose.py`'s style, and emits
structured `ToolGap` records the proposer consumes.

## Proposal schema (Goal 2)

`ProposalType.CODE_EDIT = "code_edit"`. Target-path pattern in
`_TARGET_PATTERNS`:

```python
ProposalType.CODE_EDIT.value: [
    re.compile(r"^scripts/proposed/[a-z0-9_\-]+\.py$"),
],
```

The draft body (the `proposed_diff` field) is a *full file*, not a unified
diff — matching the `NEW_QUESTION` pattern in
[`proposals.py`](../../../src/einstein/meta_loop/proposals.py)
(`_TARGET_PATTERNS[NEW_QUESTION]`). `apply_proposal_to_worktree` writes the
file directly rather than `git apply`-ing, because the path is new.

Body skeleton (the `make_code_edit_proposal` helper emits this when the
proposer fires; the proposer LLM can refine the body via `_coerce_raw`):

```python
"""<tool slug> — autosynthesized from gap cluster <gap-id>.

Citation block (immutable — promotion gate verifies this):
- gap: <canonical form, e.g. "P12 algebraic-construction unwired">
- evidence_cycles: [49, 50, 51, ...]
- problem_ids: ["P14", "P12", ...]
- originating_question: docs/wiki/questions/<date>-<slug>.md
"""
def main():
    # TODO(autosynth): implement <one-line spec from the gap question>
    raise NotImplementedError("draft from tool-autosynthesis — needs body")
```

The "TODO body + cite block" pattern follows Ma SkillClaw's "skip >
speculative edit" guardrail
([2026-ma-skillclaw-let-skills-evolve.md](../../source/2026-ma-skillclaw-let-skills-evolve.md)):
the proposer drafts the *contract* (signature, docstring, gap citation)
and refuses to hallucinate the body. The shadow A/B's A-arm (treatment)
then has the chance to flesh it out from inside a real cycle, or the
human writes the body during the human-approval step.

## Sandbox validator spec (Goal 3)

`validate_proposed_tool(path) -> ValidationReport` runs:

1. **ruff check** on `scripts/proposed/<tool>.py` (same linter the repo
   pre-commit uses).
2. **Import** the module in an isolated subprocess (`uv run python -c
   "import importlib.util; ..."`), catching `ImportError` / `SyntaxError`.
3. **Pytest** any colocated `tests/proposed/test_<tool>.py` (skip if
   absent — the draft can be unit-test-less at first).
4. **NEVER dispatch** the tool against a live problem. The validator is
   pure static + import + unit-test checks, no autonomous_loop invocation.

Report serializes to `mb/proposals/pending/<id>/validation.json`. Failure
at any stage blocks the shadow A/B from running — same pattern as
research-synthesis G6 wiring (see
[research-synthesis-design.md](research-synthesis-design.md)).

The "import in subprocess, never in-process" choice is from Ning et al.'s
code-as-harness survey
([2026-ning-code-as-agent-harness.md](../../source/2026-ning-code-as-agent-harness.md):
"transactional shared program state"): in-process import pollutes the
parent's `sys.modules` and a malformed proposed tool could break the
validator itself, not just fail it. Subprocess isolation is a hard
boundary.

## Shadow A/B contract (Goal 4)

Same A/B harness as
[`shadow.run_shadow`](../../../src/einstein/meta_loop/shadow.py),
extended to handle the `code_edit` apply step. **Arm convention matches
the rest of the meta-loop** (`research_synthesis_shadow`,
`shadow.run_shadow` which calls
`apply_proposal_to_worktree(proposal, arm_a, ...)`):

- **A-arm** (treatment): `apply_proposal_to_worktree` runs `mv
  scripts/proposed/<tool>.py scripts/<tool>.py` AND writes the manifest
  entry — both happen in the worktree only, not on the human's checkout.
- **B-arm** (control): current manifest, current scripts dir.
- **N cycles per arm** with `EINSTEIN_SHADOW_ARM=A|B` env so the sidecar
  citation records tag per-arm
  (research-synthesis G9 pattern,
  [research-synthesis-design.md](research-synthesis-design.md)).
- **`compute_arm_metrics` extension**: a new `tool_invoked_cycles` field
  counts cycles whose `notes` mention the proposed tool's slug —
  populated on both arms; ≥ 1 in A is the citation-grounded promotion
  signal (B should normally be 0 since the tool isn't wired there).

## Promotion gate (Goal 5)

`tool_autosynthesis_promotion_decision(*, arm_a, arm_b, validator) ->
ToolPromotionDecision`. A wins iff all four:

1. **≥ 1 A-arm cycle invoked the proposed tool** (citation-grounded:
   `arm_a.tool_invoked_cycles ≥ 1`, not just "A-arm produced more
   findings").
2. **≥ 1 finding produced in A** (positive OR dead-end — either is
   signal that the dispatch did real work).
3. **No regression vs control** — `arm_a.findings_added ≥
   arm_b.findings_added` (matching `ShadowDelta.a_wins` semantics:
   treatment must not lag control).
4. **Validator clean** (from Goal 3 — already enforced earlier,
   re-asserted in the audit row for transparency).
5. **Human approval** — there is no auto-merge path. Compare to
   research-synthesis where research synthesis's promotion is also
   human-gated; we hold the same line here because the new artifact is
   *executable* and a hallucinated body could survive validator + shadow
   (e.g. it never gets dispatched in either arm) but break production
   when the strategy_picker picks it later.

Audit row to `mb/logs/tool-autosynthesis.md` (schema mirrors
`mb/logs/meta-shadow-runs.md`):

```
| timestamp_utc | proposal_id | tool_slug | n_cycles_per_arm |
  A_findings (treatment) | B_findings (control) | tool_invoked_cycles_A |
  validator_passed | a_wins | promoted | reason |
```

Reject paths also log — same transparency pattern as research-synthesis
("rejected with reason" beats "silently dropped"). A reject row carries
the originating gap cluster id so the next cycle's detector can decide
whether to re-propose (e.g. with a different draft body) or back off.

## Recurrence threshold rationale

Why ≥ 3 cycles, ≥ 2 problems for the proposer to fire? Three converging
arguments:

1. **Cross-problem generalization is the signal** — Xia SkillRL
   ([2026-xia-skillrl-evolving-agents-recursive.md](../../source/2026-xia-skillrl-evolving-agents-recursive.md))
   distills *recurring* failure categories into new skills; a single
   problem's failure is hill-climbing noise, two problems' shared failure
   is a missing rung in the manifest.
2. **Below 3 cycles, the inner agent might still write the script
   itself** — the autonomous loop has its own per-problem strategy_picker
   that emits novel-technique candidates. We don't want
   tool-autosynthesis to *replace* the per-problem agent's own
   tool-writing; we want it to handle the *cross-problem* recurrences the
   per-problem agent keeps deferring.
3. **Above 3 cycles, the gap is paying compounding cost** — every
   subsequent cycle that hits the same dispatch failure burns LLM tokens
   and human attention re-deriving "we still don't have this tool." 3
   cycles is roughly the point where the file-the-question /
   file-the-finding hygiene also kicks in for a recurring gap (see
   [self-improvement-loop](../../../.claude/rules/self-improvement-loop.md)).

The ≥ 2 distinct problem ids constraint is the cheap-but-decisive guard
against one-stuck-problem masquerading as recurrence. Empirically on this
branch's cycle-log: cycles 45–46 are both P1, cycles 49–51 are all P14 —
that's two distinct problems with 2 + 3 cycles each, exactly the shape
the threshold is calibrated for.

## Open question: standing live A/B candidate

Goal 6 runs a live A/B on the **P12 flat-polynomials
algebraic-construction gap** — picked because cycle 38 already shows
`category=discrete-combinatorics; prior=kronecker-search-decomposition.md(0.00);
novel=bnb-exhaustive-w3.md(finding_rate=1.00)` but P12 has no
`algebraic-construction-*` script wired despite the Rudin-Shapiro concept
([`concepts/rudin-shapiro.md`](../concepts/rudin-shapiro.md)) explicitly
naming algebraic construction as the analytic backbone. The expected
verdict: A-arm (treatment) drafts
`scripts/proposed/algebraic-construction-flat-poly.py`, gets dispatched
in ≥ 1 of 10 A-arm cycles, produces either a positive finding (a new
flat-polynomial candidate) or a dead-end finding (the construction is
too coarse for n ≈ 200), either of which satisfies the promotion
criterion. A *rejection* verdict — A-arm dispatches the tool but it
produces no finding either way — would be a higher-information
outcome, suggesting the gap-detector misclassified an "agent-can-still-do-it"
gap as a tool gap. Either signal updates the threshold calibration for the
next branch.

## Lifecycle (post-G5 revision, 2026-05-31)

Now that the infrastructure has landed (G0–G5), the lifecycle of a
`code_edit` proposal is:

1. **Cycle log accumulates** signals (`dispatch-failed`, `manifest only
   exposes ...`, `<slug> ... not yet wired`). The signals come for free
   from the inner agent's normal cycle-end writeback —
   [`autonomous_loop.py`](../../../scripts/autonomous_loop.py) writes
   them to `docs/agent/cycle-log.md`.

2. **Gap detector fires** (Goal 1).
   [`meta_loop.tool_gaps.detect_recurring_tool_gaps`](../../../src/einstein/meta_loop/tool_gaps.py)
   clusters the signals into `ToolGap` records and applies the
   ≥3-cycles-across-≥2-problems threshold. Fungible markers
   (`no-manifest-entry`, `no-library-match`, `dispatch-failed`) collapse
   into one cluster so three different problems with one cycle each
   still pass the threshold.

3. **Proposer drafts** (Goal 2).
   [`meta_loop.code_edit.make_code_edit_proposal`](../../../src/einstein/meta_loop/code_edit.py)
   emits a `Proposal` with `type=code_edit`, `target_path=scripts/proposed/<slug>.py`,
   and `proposed_diff` = full file body (cite block + `NotImplementedError`
   stub). The proposal is stored at `mb/proposals/pending/<id>.md` via
   `ProposalStore.write_pending`.

4. **Validator runs** (Goal 3).
   [`meta_loop.sandbox.validate_proposed_tool`](../../../src/einstein/meta_loop/sandbox.py)
   ruff-checks, imports in a subprocess, and runs any colocated
   `tests/proposed/test_<slug>.py`. Result serialized to
   `mb/proposals/pending/<id>/validation.json`. NEVER dispatches.

5. **Shadow A/B runs** (Goal 4).
   [`meta_loop.shadow.run_shadow`](../../../src/einstein/meta_loop/shadow.py)
   forks two worktrees from current HEAD. The A-arm (treatment) gets
   `apply_proposal_to_worktree` which graduates the draft
   (`scripts/<slug>.py`) AND wires stub manifest entries under every
   cited problem id. Each arm runs `n_cycles` cycles via
   `default_cycle_runner` (shells out to `scripts/autonomous_loop.py`).
   The cycle-log notes from each arm are then aggregated by
   `compute_arm_metrics(rows, tool_slug=<slug>)` — the new
   `tool_invoked_cycles` field counts cycles whose notes mention the
   slug (typically ≥ 1 in A, 0 in B).

6. **Promotion gate** (Goal 5).
   [`meta_loop.tool_autosynthesis.tool_autosynthesis_promotion_decision`](../../../src/einstein/meta_loop/tool_autosynthesis.py)
   returns `a_wins=True` iff validator passed AND
   `arm_a.tool_invoked_cycles ≥ 1` AND `arm_a.findings_added ≥ 1` AND
   `arm_a.findings_added ≥ arm_b.findings_added` (no regression vs
   control). The mechanical verdict is logged to
   `mb/logs/tool-autosynthesis.md` (and the parallel
   `mb/logs/meta-shadow-runs.md`) regardless of outcome — reject paths
   also log.

7. **Human approval** flips `decision.promoted = True`. This is the only
   path that actually `mv`s `scripts/proposed/<slug>.py` to
   `scripts/<slug>.py` on `main` and commits the manifest wire. The
   submission-policy gate chain
   ([`axioms.md`](../../../.claude/rules/axioms.md)) deliberately does
   NOT extend here.

The standing live A/B candidate (P12 algebraic-construction gap) does
not yet appear in the cycle-log because the inner agent has only just
gained the ability to surface "not yet wired" markers (cycles 49–51 of
P14 are the precedent). The P12 case will manifest organically once the
autonomous loop runs against P12 with a strategy_picker that flags the
gap. Pending that trigger, the [G6 verdict row in
`mb/logs/meta-shadow-runs.md`](../../../mb/logs/meta-shadow-runs.md)
records "infrastructure landed, live A/B deferred" — mirroring the
[skill-bandit branch's same-shape status entry](../../../mb/logs/meta-shadow-runs.md).

## See also

- [[meta-loop-design-from-literature]] — the L1 design that introduced
  the proposal type system.
- [[recursive-meta-design]] — the highest-blast-radius proposal type's
  design; this finding pairs with that one as the "lower-blast-radius but
  still executable" sibling.
- [[research-synthesis-design]] — closest analogue for promotion-gate
  shape (sidecar citation records, per-arm tags).
- [[meta-loop-swap-surface]] — proposer pluggability surface; the
  `code_edit` proposer can be swapped (LLM, gap-detector-only, hybrid)
  without touching the gate chain.
- [Proposals module](../../../src/einstein/meta_loop/proposals.py) — the
  schema this finding extends.
- [Shadow harness](../../../src/einstein/meta_loop/shadow.py) — the A/B
  contract Goal 4 extends.
- [Auto-submit gate chain](../../../.claude/rules/axioms.md) — the
  submission policy this finding deliberately does NOT extend (no
  auto-promote for `code_edit`).
