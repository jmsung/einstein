---
type: concept
author: agent
drafted: 2026-05-23
related_problems: [P1, P6, P12, P19]
related_techniques: [memetic-tabu-search.md, basin-hopping-multistart.md]
related_findings: []
related_personas: []
cites:
  - ../../domains/ai-reasoning/source/2023-romera-paredes-funsearch.md
  - ../../domains/ai-agents/source/2023-wang-voyager-open-ended-embodied-agent.md
  - ../../domains/ai-agents/source/2023-zhao-expel-llm-agents-experiential.md
  - ../../domains/ai-reasoning/source/2022-fawzi-alphatensor.md
  - ../../domains/ai-agents/source/2025-novikov-alphaevolve.md
  - ../../domains/ai-agents/source/2023-jimenez-swe-bench-can-language-models.md
  - ../../domains/ai-agents/source/2024-chan-mle-bench-evaluating-machine-learning.md
---

# Agentic Harness

## TL;DR

An **agentic harness** is the scaffolding around an LLM that turns "one-shot generation" into a search loop: a generator (the model), an evaluator (executable verification), a memory (skill library or finding log), and a controller (curriculum / strategy picker). The harness is the agent — the LLM is just one swappable component inside it. Two design moves dominate: (1) **executable verification over preference judgement** — a unit test, a score, a constraint check — so the loop closes deterministically; (2) **persistent memory across attempts** — a skill library, an insight buffer, or a wiki — so each cycle compounds.

## What it is

The pattern, across systems:

```
generator → candidate → evaluator → result ─┐
   ▲                                        │
   └────────── memory + controller ◀────────┘
```

- **Generator**: LLM or program-synthesis model emitting code, a configuration, or a chain-of-thought.
- **Evaluator**: deterministic check — unit tests (SWE-bench, [`domains/ai-agents/source/2023-jimenez-swe-bench-can-language-models.md`](../../domains/ai-agents/source/2023-jimenez-swe-bench-can-language-models.md)), Kaggle leaderboard scoring ([MLE-bench](../../domains/ai-agents/source/2024-chan-mle-bench-evaluating-machine-learning.md)), Minecraft game state ([Voyager](../../domains/ai-agents/source/2023-wang-voyager-open-ended-embodied-agent.md)), arena verifier (this repo).
- **Memory**: structured store the controller and generator can both read — Voyager's skill library, ExpeL's insight buffer ([`domains/ai-agents/source/2023-zhao-expel-llm-agents-experiential.md`](../../domains/ai-agents/source/2023-zhao-expel-llm-agents-experiential.md)), FunSearch's program database ([`domains/ai-reasoning/source/2023-romera-paredes-funsearch.md`](../../domains/ai-reasoning/source/2023-romera-paredes-funsearch.md)), AlphaEvolve's evolutionary database ([`domains/ai-agents/source/2025-novikov-alphaevolve.md`](../../domains/ai-agents/source/2025-novikov-alphaevolve.md)), this repo's `knowledge/wiki/`.
- **Controller**: picks the next prompt / strategy — curriculum (Voyager), evolutionary selection (FunSearch, AlphaEvolve), strategy picker with 1+1 rule (this repo's [`docs/tools/strategy_picker.py`](../../tools/strategy_picker.py)).

## When it applies

Any task where **one-shot LLM performance is well below ceiling** but **the answer can be cheaply verified**:

- **Math discovery** — extremal bounds, constructions, optimization-arena problems. FunSearch found new cap-set lower bounds; AlphaTensor ([`domains/ai-reasoning/source/2022-fawzi-alphatensor.md`](../../domains/ai-reasoning/source/2022-fawzi-alphatensor.md)) found faster $4\times 4$ matrix-mult algorithms; AlphaEvolve discovered new algorithms across several domains. This repo's autonomous loop fits the same shape.
- **Software engineering** — Claude 2 + BM25 retrieval solves only $1.96\%$ of SWE-bench tasks unaided; modern harnesses (Aider, SWE-agent, Devin, Cursor) push this dramatically higher by adding retrieval, planning, and tool use — same model, different scaffold.
- **ML engineering** — o1-preview with the AIDE scaffold earns a Kaggle bronze medal in $16.9\%$ of MLE-bench competitions at pass@1; the scaffold contribution is at least as large as the base model.
- **Open-ended exploration** — Voyager's automatic curriculum + skill library + iterative prompting achieves $3.3\times$ more unique items and $15.3\times$ faster tech-tree unlocks vs ReAct / Reflexion / AutoGPT in Minecraft, and zero-shot transfers to a new world.

## Why it works

Three failure modes the harness defeats:

1. **Single-shot bound**: an LLM's per-call success rate is a fixed ceiling. Harnesses amortize across many samples (FunSearch: islands of programs evaluated by score; AlphaEvolve: long-running evolution). The ceiling per sample stays low, but cumulative discovery rate stays high.
2. **Context decay**: LLM context windows are bounded, and within-window reasoning quality decays with length. A persistent memory (skill library, insight buffer, wiki) externalises what would otherwise be lost between calls.
3. **Reward hacking**: when the evaluator is a learned preference model, agents drift into mode-collapse. Executable verification (unit tests, scores, theorems) is hack-proof at the harness boundary, so the search loop terminates honestly.

The deep claim across all five harnesses cited: **the rate of discovery scales with (compute × memory-quality × evaluator-fidelity)**, not with model size alone. ExpeL's positive forward-transfer from HotpotQA → FEVER is the cleanest demonstration that the *memory layer* — not just the model — is doing the learning.

## In this repo

The autonomous-loop branch (`feat/autonomous-loop`) instantiates the pattern:

| Harness component | This repo's analogue |
|---|---|
| Generator | Claude (via `claude -p` in `llm_distill.py`, council dispatch via `src/einstein/council.py`) |
| Evaluator | Triple-verify infrastructure + arena verifier ([`knowledge/wiki/concepts/arena-platform.md`](arena-platform.md)) |
| Memory | `knowledge/wiki/` + `knowledge/source/` (1193 entries as of 2026-05-23) + `docs/agent/skill-library.md` + `docs/agent/cycle-log.md` |
| Controller | `docs/tools/strategy_picker.py` (1+1 rule), `scripts/autonomous_loop.py` (outer + inner) |
| Curriculum | Problem queue with tier-S→C priority + active/inactive predicate |

Two anti-patterns the design explicitly avoids:

- **Theatrical self-improvement** — cherry-picking only the impressive cycles. Mitigated by the cycle-discipline rule: every cycle logged, failures count ([`.claude/rules/cycle-discipline.md`](../../.claude/rules/cycle-discipline.md)).
- **Skipping the memory write** — knowledge generated in-context and lost at session end. Mitigated by the self-improvement-loop rule: file the question, distill the finding, propose the concept ([`.claude/rules/self-improvement-loop.md`](../../.claude/rules/self-improvement-loop.md)).

## Diagnostic tells (when a harness is broken)

- **Same approach tried twice with no logged failure** → memory layer is read-only in practice; strategy_picker is not consulting it.
- **Per-cycle score curve flat across many sweeps** → either the problem is genuinely converged (rigid basin — see [basin-rigidity](basin-rigidity.md)) or the controller is stuck in a single strategy. Distinguish by inspecting `skill-library.md` strategy diversity.
- **Wiki grows but no finding is cited 3+ times** → distillation is producing content without compounding. Run promotion check; if no candidates surface, the corpus is wide but shallow.
- **Auto-ingest fills `source/` with off-topic papers** → evaluator (the arxiv relevance threshold + math-category filter) is mis-calibrated. The harness boundary leaked.

## Related

- Concepts: [arena-platform](arena-platform.md), [probabilistic-method](probabilistic-method.md) (multistart is the probabilistic instantiation of the search loop), [provable-floor-and-frozen-problems](provable-floor-and-frozen-problems.md).
- Rules: [self-improvement-loop](../../.claude/rules/self-improvement-loop.md), [cycle-discipline](../../.claude/rules/cycle-discipline.md), [council-dispatch](../../.claude/rules/council-dispatch.md), [failure-is-a-finding](../../.claude/rules/failure-is-a-finding.md).
- Sources: [Voyager](../../domains/ai-agents/source/2023-wang-voyager-open-ended-embodied-agent.md), [ExpeL](../../domains/ai-agents/source/2023-zhao-expel-llm-agents-experiential.md), [FunSearch](../../domains/ai-reasoning/source/2023-romera-paredes-funsearch.md), [AlphaTensor](../../domains/ai-reasoning/source/2022-fawzi-alphatensor.md), [AlphaEvolve](../../domains/ai-agents/source/2025-novikov-alphaevolve.md), [SWE-bench](../../domains/ai-agents/source/2023-jimenez-swe-bench-can-language-models.md), [MLE-bench](../../domains/ai-agents/source/2024-chan-mle-bench-evaluating-machine-learning.md).
