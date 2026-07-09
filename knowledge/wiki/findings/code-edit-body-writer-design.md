---
type: finding
author: agent
drafted: 2026-06-02
question_origin: branch-js-feat-code-edit-body-writer
status: answered
related_concepts: []
related_techniques: []
related_personas: []
cites:
  - ../../source/2026-ma-skillclaw-let-skills-evolve.md
  - ../../source/2026-sherwood-alphazero-coding-agents.md
  - ../../source/2026-lee-meta-harness-end-to-end-optimization-model.md
  - ../../source/2026-lin-agentic-harness-engineering-ahe.md
  - ../../source/2026-ning-code-as-agent-harness.md
  - ../../source/2025-zhang-darwin-godel-machine-open-ended.md
  - tool-autosynthesis-design.md
  - meta-loop-design-from-literature.md
---

# Code-edit body-writer design — LLM fills the stub, gates stay

## TL;DR

`tool-autosynthesis` (the `code_edit` proposer) drafts the *contract* of a new
optimizer — path, signature, docstring, citation block — and leaves a
`NotImplementedError` body. That was the SkillClaw "skip > speculative edit"
guardrail at a stage when the LLM had no structural examples to learn from.

Phases 1a/1b/2a have since written ~10 real optimizer bodies under
`scripts/<problem>/`. This branch adds an **opt-in body-writer**: given a
`ToolGap` + the cited problems' existing scripts + the relevant technique
page + the open question, an LLM proposes a *real* body. The output stays
gated exactly as before — validator (now + smoke-dispatch) → shadow A/B →
human approval. The risk delta vs. the stub is "the body could be wrong,"
and that delta is absorbed by the gate chain, not by trusting the LLM.

## Why now, not in Phase 1

SkillClaw ([2026-ma-skillclaw-let-skills-evolve.md](../../source/2026-ma-skillclaw-let-skills-evolve.md))
is the anchor: skill bodies evolve **from grouped session evidence**, under a
validator gate, with a mandatory `v<N>.md` + `v<N>_evidence.md` ledger and
*conservative editing* ("preserve API contracts/endpoints; do not bloat with
runtime advice"). Two preconditions it implies map directly here:

1. **Evidence must exist before generation.** SkillClaw evolves from real
   trajectories; it doesn't hallucinate skills from nothing. Phase 1 had no
   hand-written bodies to learn from, so the honest move was the stub. Now
   the cited problems' `scripts/<problem>/` dirs *are* the evidence ledger —
   the body-writer reads them as in-context examples (Goal 1's
   `gather_context`).
2. **Conservative editing = preserve the contract.** SkillClaw preserves API
   contracts across edits. Our analogue: the body-writer must preserve the
   module docstring + citation block (the `- problems: [...]` line that
   `shadow._apply_code_edit_graduation` parses to wire the manifest). The
   LLM only replaces the function body — it may not rewrite the cite block.
   This is the single hardest invariant of the design.

## Why the gate chain is sufficient for the risk delta

The stub could only fail one way: a dispatcher picks it and gets
`NotImplementedError` → dead-end finding (the promotion gate keys on exactly
this). A body-written draft adds a new failure mode: code that runs but
computes a *wrong* score. Three gates catch the three sub-cases:

| Failure mode | Caught by |
|---|---|
| Syntax / import error | sandbox validator (ruff + import) — unchanged |
| Runs but is a `NotImplementedError` stub anyway | **smoke-dispatch** (Goal 4) — the only validator change |
| Runs, produces a number, but the number is wrong | shadow A/B (no finding produced) → triple-verify in the inner loop before any submission (axioms A1) |

The AlphaZero-coding-agents result ([2026-sherwood-alphazero-coding-agents.md](../../source/2026-sherwood-alphazero-coding-agents.md))
is the capability prior: by April 2026 a frontier agent reliably implements a
non-trivial pipeline end-to-end under a hard verification anchor (the Pons
solver). The lesson imported here is *not* "trust the generated code" — it is
"a generated body is worth trying **when an oracle gates it**." Our oracle is
the validator + shadow A/B + triple-verify, not a Connect-Four solver.

## Design decisions

- **Opt-in, default-off.** `make_code_edit_proposal(gap, write_body=False)`
  keeps the stub. `write_body=True` swaps in the LLM body. The default stays
  the safe stub so nothing downstream changes unless a caller asks for it.
- **Swappable proposer.** `write_body_llm(gap, context, proposer=...)` mirrors
  `propose.run(proposer=...)`: tests inject a stub callable; the default
  shells out to `claude_headless` with the body-writer system prompt at
  `docs/agent/proposer_prompts/body-writer-v1.md`. Prompt-in-a-file so it can
  be A/B'd without a code edit ([meta-loop-swap-surface](meta-loop-swap-surface.md)).
- **Token budget cap.** ~30K input + ~5K output per proposal. The context
  gatherer truncates each example script to a head budget so a fat
  `scripts/<problem>/` dir can't blow the input.
- **Contract preservation is verified, not trusted.** `write_body_llm` splices
  the LLM body into the *existing* stub's docstring+cite block rather than
  letting the LLM emit the whole file. The cite block is immutable by
  construction — the LLM never sees a path where it can rewrite it.

## What this rules in for later

The pattern extractor (`gather_context`) is reusable for any future proposer
that wants sibling-problem context — `manifest_tweak` could read sibling
manifest entries the same way. Phase 4 (autonomous record-hunt) depends on
this: with the body-writer off, autosynth surfaces gaps but a human always
writes the body, capping the loop's autonomy. With it on (and gated), the
next recurring gap arrives with a candidate fix attached.

See also: [tool-autosynthesis-design](tool-autosynthesis-design.md),
[meta-loop-design-from-literature](meta-loop-design-from-literature.md).
