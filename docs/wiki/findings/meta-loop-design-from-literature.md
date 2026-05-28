---
type: finding
author: agent
drafted: 2026-05-25
question_origin: branch-js-feat-meta-loop
status: answered
related_concepts: []
related_techniques: []
related_personas: []
cites:
  - ../../source/2026-lee-meta-harness-end-to-end-optimization-model.md
  - ../../source/2026-zhang-hyperagents.md
  - ../../source/2026-lin-agentic-harness-engineering-ahe.md
  - ../../source/2026-ning-code-as-agent-harness.md
  - ../../source/2025-zhao-sirius-self-improving-multi-agent-systems.md
  - ../../source/2026-zhang-aevo-agentic-evolution.md
  - ../../source/2026-zou-recursive-multi-agent-systems.md
---

# Meta-loop design from literature — what 7 recent papers say about building a self-improving outer loop

## TL;DR

The meta-loop being scaffolded on `js/feat/meta-loop` sits on top of `scripts/autonomous_loop.py`'s *inner* cycle loop. The seven ingested papers converge on a small set of architectural commitments that — taken together — predict what compounds and what doesn't:

1. **Filesystem-as-feedback beats compressed summaries** (Meta-Harness, AHE). Raw traces, not scalar scores or LLM summaries, are the load-bearing input to the proposer. Our `cycle-log.md` + `docs/wiki/findings/` + `mb/logs/auto-submit.md` already are this layer; the meta-loop must *read raw*, not pre-digest.
2. **Edit the mechanism, not the next candidate** (AEVO, AHE, HyperAgents). The compounding gain is in revising the procedure/skills/rules/notes — not in burning iterations on more inner attempts. Our proposal channel (`mb/proposals/`) targets rules / manifest / queue *because that's where the math says compounding lives*.
3. **Falsifiable contracts with rollback are the safety surface** (AHE). Every edit ships a change-manifest naming evidence + predicted regressions; the next round verifies and auto-rolls back ineffective edits. Our 6-gate chain + applied/reverted directories must enforce this — the diff alone is not the contract.
4. **Self-attribution is asymmetric** (AHE). Fixes are foreseeable; regressions are not (11% recall on AHE's data, 89% of regressions unforeseen). This empirically validates `triple-verify` as the regression-foresight gap-filler and motivates **shadow A/B** as the only honest way to greenlight non-trivial edits.
5. **Persistent cross-cycle state is the ratchet** (AEVO, HyperAgents, MetaHarness). AEVO's VLIW kernel result (1774→1138 cycles via a persistent "family map" of falsified architectures) is the same shape as our `findings/` + `dead-ends/` graph. The wiki is not decoration; it is the substrate the next cycle stands on.
6. **Metacognitive modification (meta editing meta) is the recursive case** (HyperAgents). Deferred to a separate branch (`js/feat/recursive-meta`) per the 5-branch sequence — too risky for this branch.

## The seven papers, one paragraph each

**Meta-Harness (Lee et al., 2026)** — Outer loop maintains a population/Pareto frontier on a filesystem D; a Claude-Code/Opus-4.6 proposer queries D via `grep`/`cat` (median 82 files/iter), proposes single-file Python harnesses, validates + evaluates, logs code+scores+traces back. The critical ablation result: scores+summary → 34.9, full execution traces → 50.0 median accuracy. Compressed-feedback methods (ACE, MCE) lose by ~7 pts at 4× more tokens. **For us**: feed the proposer raw `cycle-log.md` rows + raw findings, not a pre-digested digest.

**AHE (Lin et al., 2026)** — Three observability pillars on the NexAU framework: component observability (7 editable component types as files), experience observability (10M trajectory tokens → 10K-token layered evidence corpus with root-cause reports), decision observability (every edit ships a change-manifest with predicted fixes + regressions; the next round verifies). Ten AHE iterations: 69.7 → 77.0 on Terminal-Bench 2, beating Codex 71.9 and ACE 68.9. Cross-model transfer: +5.1 to +10.1 pp on three other base models. **For us**: the change-manifest pattern *is* our proposal schema. The asymmetric self-attribution result (89% of regressions unforeseen) is the strongest empirical argument for shadow A/B.

**HyperAgents / DGM-H (Zhang et al., 2026)** — One editable Python program containing both task agent and meta agent; DGM's archive-based evolutionary loop; parent selection by score×1/(compiled-children+1). Achieves open-ended self-improvement that transfers across domains (coding, paper review, robotics reward design, IMO grading); emergent meta-improvements include persistent JSON memory, performance trackers, compute-aware budgeting, bias detection (fixed 99% accept-rate collapse 49% → 63% accuracy). **For us**: the metacognitive case (meta-loop editing the meta-loop) is real and important — but recursive. We defer it deliberately and ship the non-recursive case first.

**AEVO (Zhang et al., 2026)** — Treats the evolution loop as an environment; meta-agent observes state and outputs an *edit action* on the mechanism (procedure code, skills, goals, notes, validators); two-phase loop alternates meta-editing with evolution segments. Result: 53.8 vs 44.3 best baseline on Terminal-Bench; 47.0 vs 36.0 on ARC-AGI-2; **1774 → 1138 cycles** on VLIW kernel via layered durable state (task skill, hypothesis-carrying goals, persistent family map, replay utilities, structured session notes). **For us**: this is the model our `mb/active/<branch>.md` + `findings/` graph is approximating manually. The validation result is that *persistent state is what compounds*; the meta-loop's job is to maintain it.

**Code-as-Agent-Harness survey (Ning et al., 2026)** — Names what we already have. Three layers — harness interface (code for reasoning/acting/env modeling), harness mechanisms (planning/memory/tool use/optimization), multi-agent orchestration over shared code artifacts. Open problems explicitly named: regression-free self-evolving harnesses, evaluation beyond final task success, semantic verification under incomplete feedback. **For us**: vocabulary anchor + a forward-looking checklist of open problems to track.

**SiriuS (Zhao et al., 2025)** — Per-agent SFT on retained successful multi-agent trajectories + rephrased corrections of failures. 2.86%–21.88% gains over single-agent / STaR / CoMM / TextGrad; Judgment Agent is the load-bearing component (largest drop on ablation). The "rephrase regenerated answers to look first-pass" trick is directly applicable to distilling findings from failed cycles. **For us**: tangential — no fine-tuning loop, but the credit-assignment problem is the same when a persona-council collaboration produces only a final triple-verified score.

**RecursiveMAS (Zou et al., 2026)** — Latent-space cross-agent transfer via residual projection modules ("RecursiveLink"). +8.3% on 9 benchmarks; 1.2×–2.4× speedup; 34.6%–75.6% token reduction. **For us**: tangential. Latent-state collaboration would hide reasoning from human review and break wiki-attribution + triple-verify. Park as architectural lookahead only.

## Design pattern: filesystem-as-feedback (MetaHarness)

The single most actionable result across the seven papers is MetaHarness's ablation: raw execution traces beat scalar scores + LLM summaries by ~15 pts median accuracy at 4× fewer context tokens. The mechanism — feed the agentic proposer the *whole filesystem* of prior candidates' code, scores, and traces; let `grep`/`cat` do the routing.

Mapped to this repo:

| MetaHarness | einstein equivalent |
|---|---|
| Filesystem D | `docs/agent/cycle-log.md`, `docs/wiki/findings/`, `mb/logs/auto-submit.md`, `mb/logs/inner-agent-budget.md`, `mb/problems/<id>/experiment-log.md` |
| Single-file harness candidate | A single typed proposal (rule edit, manifest tweak, queue reorder, new question) |
| Population + Pareto frontier | `mb/proposals/{pending,applied,rejected,reverted}/` |
| Validator + held-out evaluator | 6-gate chain + shadow A/B harness (Goal 5) |
| Execution traces | The full cycle row + the findings it cites + the dead-ends it produced |

The implementation commitment: the proposer (Goal 2) reads *raw* files, not a pre-summarized digest. The Goal 1 diagnostic report exists to surface patterns for the human, not to feed the agent. This is the opposite of the natural instinct to "summarize before sending."

## Metacognitive modification — the recursive case (HyperAgents, AEVO)

HyperAgents's DGM-H shows the meta-mechanism itself can be edited and that this is empirically useful — emergent persistent memory, performance trackers, compute-aware budgeting, bias detection all came from the meta-edit channel. AEVO formalizes the same as `Edit(Π_r, a_r)` on the transition mechanism.

For us, this is the `js/feat/recursive-meta` branch — deferred deliberately:

- **Gates need to be tighter.** A meta-edit to the gate chain itself, applied carelessly, removes the safety surface. Recursive self-edits demand a notion of *protected invariants* that the meta-loop cannot weaken without human approval.
- **Shadow A/B is mandatory** for recursive edits — no exceptions. Self-attribution asymmetry (AHE) is *more* asymmetric for self-edits because the agent is grading its own paper.
- **Budget and audit live in a separate ledger** (`mb/logs/meta-loop-budget.md`) so recursive runaway is visible.

This branch ships the non-recursive case: the meta-loop edits rules / manifest / queue / questions, but **not itself**. The proposal type `meta_self_edit` is explicitly excluded from Goal 2.

## Evaluation framework — what counts as evidence (AHE, AEVO)

The hardest piece is also the most under-specified in the papers: how do you know a meta-edit *worked*?

AHE's answer: the change-manifest predicts task-level deltas; the next round verifies; ineffective edits are rolled back at file granularity. Their self-attribution data is the honesty floor — fixes are foreseeable (high precision/recall), regressions are not (11.6% precision, 11.1% recall on cumulative regressions). The implication: **you cannot trust the agent's prediction of "this edit will not regress X."** You must measure.

AEVO's answer: budget meta-edits per segment, run an *evolution segment* of fixed length under the new mechanism, compare segment-level outcome stats. This is shadow A/B in batch form.

For us — the einstein-specific shape:

- **Outcome metrics** read from `docs/agent/cycle-log.md`: top-3 hits/cycle, new findings/cycle, dead-ends/cycle, tokens/cycle. These are the candidate "metric delta" signals.
- **Shadow A/B** (Goal 5): fork two worktrees `cb-shadow-<id>-{A,B}` (proposed edit + control), run N=10 cycles each, compute Δ on the four metrics, require human sign-off before promotion.
- **Triple-verify maps cleanly**: outcome counts (fast eval), tokens/cycle (independent reimplementation of "did this make us cheaper"), human read of the diff (cross-check). The three signals already-named in `triple-verify.md` survive intact.

## What generalizes vs. what's domain-specific

| Component | Generalizes (portable) | Math-specific (adapter only) |
|---|---|---|
| Proposal schema (pydantic) | ✅ id/type/target/diff/evidence/Δ/confidence/shadow | — |
| Gate chain (6 gates) | ✅ kill-switch/evidence/cap/throttle/pending/audit pattern | the *interpretation* of "evidence" (cycle-log structure) |
| Audit log writer | ✅ append-only markdown | column choices |
| Shadow A/B harness | ✅ fork-N-worktrees, run-N-cycles, compute-Δ | what "Δ" means (cycle-log fields) |
| Token budget ledger | ✅ separate from inner-loop budget | — |
| Filesystem-as-feedback channel | ✅ read raw, don't summarize | which files (`cycle-log.md` etc.) |
| Inner loop | — | `scripts/autonomous_loop.py` is math-specific |
| Council dispatch | — | persona files, problem categories |
| Arena verifier | — | `arena_submit.py`, `check_submission.py` |
| Manifest (`optimizer_manifest.yaml`) | — | problem-keyed |

The discipline (`agent-stance.md` "scalable system > toy model"): **do not pre-abstract on day one.** Write the math-specific call sites naturally with portability in mind; after Goal 6, look at what *actually* turned out generic and extract `scripts/meta_loop_core/` + `scripts/meta_loop_adapters/einstein.py` based on evidence, not speculation. This mirrors AEVO's design — their procedure-mode and agent-mode share an outer harness but differ in the action surface.

## Design constraints for this branch's implementation

1. **Proposer reads raw filesystem.** No pre-summarized digest. (Meta-Harness ablation.)
2. **Change-manifest = proposal schema.** Every proposal carries evidence_cycles, expected_metric_delta, predicted_regressions, requires_shadow. (AHE pattern.)
3. **6 gates mirror `auto_submit.py`.** Kill switch → evidence threshold (≥3 cycles) → daily cap (≤2/day) → pending-throttle → shadow A/B (optional) → audit row. (Existing repo pattern; lowest-friction adoption.)
4. **Separate budget ledger.** `mb/logs/meta-loop-budget.md`, distinct from `inner-agent-budget.md`. (HyperAgents emergent insight: compute-aware budgeting wants per-loop visibility.)
5. **Asymmetric foresight → shadow A/B is the regression-foresight gap-filler.** Required for `code_edit` and `meta_self_edit` types; optional for `rule_edit`/`manifest_tweak`/`queue_reorder`/`new_question` (these are read-mostly or easily reversible). (AHE self-attribution data.)
6. **`meta_self_edit` is excluded** from this branch. Deferred to `js/feat/recursive-meta`. (HyperAgents → tighter gates needed.)
7. **Failures-as-findings discipline survives.** Rejected proposals that *would have been reasonable* get a `dead-end-<slug>.md` per `failure-is-a-finding.md`. Trivial-malformed rejections don't.
8. **`triple-verify` maps directly to shadow A/B.** Three signals: outcome counts (fast), tokens/cycle (independent), human read of diff (cross-check). No new verification primitive needed.
9. **Stance discipline.** The meta-loop is not a workaround for the self-improvement loop — it must respect `cycle-discipline.md` (every accepted code-change proposal that's non-trivial triggers a wiki finding). Proposals are not a backdoor.

## Open questions surfaced (to file as `wiki/questions/` later)

- **Mechanism-edit cadence**: AEVO uses heuristic budgets for the meta-edit/evolution-segment alternation. Is there a principled schedule for jsagent, or is it problem-dependent?
- **Persistent family map vs. flat findings**: AEVO's VLIW result lives on a *graph* of falsified architectures with explicit cross-links. Our `findings/` is a flat directory with markdown crosslinks. Does explicit graph structure compound faster? (Partially answered by `docs/tools/wiki_graph.py` — measure.)
- **Goodhart on cycle-log metrics**: HyperAgents notes evaluation gaming as the dominant failure mode for compounding self-modification. If the meta-loop optimizes top-3-hits/cycle, what's the most likely Goodhart shape? Pre-register predictions.
- **Cross-domain transfer claim**: AHE shows +5.1 to +10.1 pp on three alternate base models *without re-evolution*. If we run the meta-loop with Opus 4.7 and then swap to Sonnet 4.6, does the harness still help? Should test at Goal 6.
- **Recursive case: what's the simplest safe meta_self_edit?** Defer to `js/feat/recursive-meta` design; surface here so the question is filed.

## Why this matters for the einstein wiki itself

This finding is the literature-anchor for the entire branch. The branch's PR body (`mb/active/js-feat-meta-loop.md`) names 7 papers; this page is the synthesis those papers feed into. Subsequent goals (1–6) cite back to this finding rather than re-litigating "why this design." That's the compounding signal `wiki-attribution.md` and `self-improvement-loop.md` both demand.

If/when this branch ships and Goal 6 produces the post-hoc finding (`meta-loop-first-run.md`), that page should *cite this one* and call out which of the literature predictions held vs. which didn't. The honesty check is whether the post-hoc finding has the courage to disagree with this one.

## See also

- [meta-loop-swap-surface](meta-loop-swap-surface.md) — the `Callable[[ProposerInput], list[dict]]` swap point + `proposer_id` convention; how non-LLM proposers (bandit, evolutionary, heuristic) plug in. Implements "edit the mechanism, not the next candidate" as a pluggable proposer family.
- Branch: `js/feat/meta-loop` — `mb/active/js-feat-meta-loop.md`
- Inner loop: `scripts/autonomous_loop.py` (~1374 LOC)
- Pattern to mirror: `src/einstein/auto_submit.py` (6-gate chain, 342 LOC)
- Discipline guards: [self-improvement-loop](../../../.claude/rules/self-improvement-loop.md), [cycle-discipline](../../../.claude/rules/cycle-discipline.md), [failure-is-a-finding](../../../.claude/rules/failure-is-a-finding.md), [triple-verify](../../../.claude/rules/triple-verify.md), [agent-stance](../../../.claude/rules/agent-stance.md)
