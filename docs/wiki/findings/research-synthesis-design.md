---
type: finding
author: agent
drafted: 2026-05-25
question_origin: js/feat/research-synthesis G0
status: answered
related_problems: []
related_concepts:
  - agentic-harness
related_findings:
  - finding-the-fertile-gaps
  - cross-pollination-not-compute
related_personas: []
cites:
  - ../../source/2026-lee-meta-harness-end-to-end-optimization-model.md
  - ../../source/2026-lin-agentic-harness-engineering-ahe.md
  - ../../source/2025-zhao-sirius-self-improving-multi-agent-systems.md
  - ../../source/2026-ning-code-as-agent-harness.md
  - ../../source/2024-baek-researchagent-iterative-research-idea.md
  - ../../source/2026-zhang-hyperagents.md
  - ../../source/2024-ajith-litsearch-retrieval-benchmark-scientific.md
  - ../../source/2024-press-citeme-can-language-models.md
  - ../../source/2024-wang-autosurvey-large-language-models.md
  - ../concepts/agentic-harness.md
---

# Research-synthesis as a design pattern: literature-driven planning for jsagent

## TL;DR

Six recent harness papers, two literature-retrieval studies, and one auto-survey
system converge on a pattern this repo has not yet enforced: **before generating
an attempt, the agent should synthesize from a retrieved subset of its own
ingested literature and carry citations forward into the attempt as a
first-class field**. The harness loop already cited in
[`../concepts/agentic-harness.md`](../concepts/agentic-harness.md) covers
*generator → evaluator → memory → controller* as a runtime architecture; this
finding is the sibling claim at the layer above: **the memory must be queried
deliberately at cycle-start, and the queries that pay off must be tracked as
provenance the way scores are tracked**. That makes "which ingested papers
actually informed real attempts" a measurable signal — the missing leg of the
self-improvement loop.

## The question

The branch [`js/feat/research-synthesis`](../../../../mb/active/js-feat-research-synthesis.md)
opens with a concrete asymmetry: `docs/source/` now holds 1256 distilled
papers and `docs/wiki/` holds 194 synthesis pages, but `mb/<problem>/`
cycles rarely cite anything from either. The wiki grows; attempt provenance
doesn't. **What design pattern, attested in literature, would close that loop
without bolting on a parallel system?**

## What each source shows

- **Meta-Harness** ([`2026-lee-meta-harness-end-to-end-optimization-model.md`](../../source/2026-lee-meta-harness-end-to-end-optimization-model.md))
  runs a coding-agent proposer over the *entire filesystem of prior candidates'
  code + traces* (~10 MTok/iter, ~3 orders of magnitude beyond compressed
  baselines). The decisive ablation: raw execution traces beat
  scores+LLM-summary by 34.9 → 50.0 median accuracy. **Implication: the memory
  layer must hand the next attempt the raw artifact, not a compressed summary.**

- **AHE** ([`2026-lin-agentic-harness-engineering-ahe.md`](../../source/2026-lin-agentic-harness-engineering-ahe.md))
  decouples a harness into seven file-mounted components and pairs every edit
  with a *change-manifest entry naming evidence, root cause, fix, predicted
  fixes, predicted regressions*. Ten iterations lift TerminalBench-2 from 69.7
  → 77.0. The honest finding: self-attribution is asymmetric — fixes are
  foreseeable (precision/recall both high), regressions are not (cumulative
  precision 11.6%, recall 11.1%, 40 unforeseen vs 5 foreseen).

- **SiriuS** ([`2025-zhao-sirius-self-improving-multi-agent-systems.md`](../../source/2025-zhao-sirius-self-improving-multi-agent-systems.md))
  retains trajectories whose outcome reward $R > \epsilon$ into a per-agent
  experience library and, for failed trajectories, has an external feedback
  agent regenerate the answer + *rephrase it to look like a first-pass
  solution* before adding to the library. Outcome-only reward — no per-step
  credit needed — is enough for SFT to lift PubMedQA / College Chemistry by
  1–10 points over CoMM, STaR, TextGrad.

- **Code-as-Agent-Harness survey** ([`2026-ning-code-as-agent-harness.md`](../../source/2026-ning-code-as-agent-harness.md))
  reframes ~480 references around the claim that **agent-initiated code
  artifacts** (regression tests, temporary tools, DSL programs, intermediate
  states, reusable skills) are the operational substrate. The survey's open
  problem list explicitly names "regression-free self-evolving harnesses" and
  "semantic verification under incomplete feedback" — both of which the
  einstein triple-verify axiom is a direct response to.

- **ResearchAgent** ([`2024-baek-researchagent-iterative-research-idea.md`](../../source/2024-baek-researchagent-iterative-research-idea.md))
  augments idea-generation with (a) citation-graph–retrieved related papers
  and (b) a sparse **entity co-occurrence matrix** built by entity-linking
  across post-2023 papers, with top-$k$ retrieval $\arg\max_I \sum_{e_j}
  P(e_j \mid e_i) P(e_i)$. The entity store is what surfaces concepts
  *outside* the seed paper's context — i.e., the cross-pollination move.
  Independently contributes gains beyond reference-graph retrieval alone.

- **Hyperagents / DGM-H** ([`2026-zhang-hyperagents.md`](../../source/2026-zhang-hyperagents.md))
  makes the *meta-modification procedure itself* editable inside the agent's
  own program and runs an archive-based evolutionary loop. Emergent moves
  include persistent JSON memory, performance trackers, and rediscovery of
  UCB-style parent selection. Meta-skills transferred from paper-review +
  robotics to Olympiad math grading: "BetterGrader" beats ProofAutoGrader by
  +4.06% by recovering Almost/Partial labels.

- **LitSearch** ([`2024-ajith-litsearch-retrieval-benchmark-scientific.md`](../../source/2024-ajith-litsearch-retrieval-benchmark-scientific.md))
  benchmarks 597 realistic scientific-literature queries: GritLM-7B (dense)
  beats BM25 by 24.8 R@5; GPT-4o reranking adds 4.4%; commercial Scholar /
  Elicit trail by up to 32 points. **Lex-only retrieval over the wiki is
  measurably weaker** — load-bearing for Goal 1's qmd vector-embed fix.

- **CiteME** ([`2024-press-citeme-can-language-models.md`](../../source/2024-press-citeme-can-language-models.md))
  asks whether language models *cite accurately*. The answer matters: a
  citation provenance field that the model fabricates is worse than none, so
  the schema needs to be machine-verifiable against actual `docs/source/*.md`
  filenames, not free-text references.

- **AutoSurvey** ([`2024-wang-autosurvey-large-language-models.md`](../../source/2024-wang-autosurvey-large-language-models.md))
  uses a retrieve → outline → parallel-draft → refine → multi-judge pipeline.
  Multi-LLM-as-judge agreement with humans $\rho \approx 0.54$ — a calibration
  point for any automated wiki-quality scorer.

## Cross-source patterns (≥3)

### Pattern A — Raw retrieved artifact, not a summary, is the load-bearing input

Meta-Harness's +15-pt traces-over-summary ablation, AHE's per-component file
mounts read by the evolve agent, Sirius's verbatim retained trajectories, the
Code-as-Harness survey's "intermediate program state" category, and
ResearchAgent's full-related-paper context all carry the same shape: the next
attempt is conditioned on the *artifact* the prior attempt produced, with
minimal compression. Five sources, same move. The einstein wiki already
follows this for `docs/source/` (1:1 distillation of each ingested paper) —
the gap is that the cycle prompt does not hand those distillations to the
attempt generator. G2 fixes this.

### Pattern B — Falsifiable change manifests with explicit predicted regressions

AHE makes this load-bearing (the change-manifest is the unit of self-attribution
and the rollback substrate); Meta-Harness implicitly via Pareto-frontier
filtering of regressing children; SiriuS via outcome-reward thresholding;
einstein's existing [`failure-is-a-finding`](../../../.claude/rules/failure-is-a-finding.md)
rule names the same shape but lacks the *predicted-regression* field.
The honest data point from AHE: 89% of regressions go unforeseen by a strong
evolve agent (recall 11.1%, 40 unforeseen vs 5 foreseen). **This is the
project-relevant open problem**, not a solved pattern — flagging it as a
question rather than a recipe (see open questions below).

### Pattern C — Citation provenance as the cross-cycle promotion signal

This is the novel synthesis, not yet attested as a single named pattern in any
of the cited sources but emergent from combining ResearchAgent's
entity-co-occurrence retrieval, AutoSurvey's multi-judge cite tracking, CiteME's
verifiability concern, and the einstein wiki's existing 3-cite promotion rule
in [`wiki-attribution.md`](../../../.claude/rules/wiki-attribution.md).
The proposal: extend the cycle-log row schema with `cited_sources: []`, and
when a `docs/source/<file>.md` accumulates ≥3 cite counts across cycles,
auto-surface it as a promotion candidate from `source/` → `concepts/`. This
turns "the wiki compounds" from an intent into a measured quantity per cycle.
G4 implements; G7 measures whether the signal is real.

### Pattern D — Pre-cycle synthesis as a step distinct from generation

Meta-Harness's proposer reads ~82 files/iter before emitting code;
ResearchAgent's pipeline runs $L = $ literature-retrieval as the *first* term
before $p, m, d$; AutoSurvey runs retrieval before outline; even DGM-H's parent
selection is a synthesis-over-archive step before the child is modified.
Across systems, the pattern is the same: **read first, synthesize, then
generate** — the linear order matters, because synthesis run *after* the
attempt is selection bias dressed up as introspection. The einstein
[`wiki-first-lookup`](../../../.claude/rules/wiki-first-lookup.md) rule
already encodes this stance but enforces it only on Q&A turns; G2 makes it a
mandatory cycle-start step with a typed output (`LiteratureSynthesis`).

## What generalizes vs what's einstein-specific

| Aspect | Portable primitive | Einstein-specific |
|---|---|---|
| Retrieval substrate | hybrid lex+vec over a flat-file distilled corpus | `qmd` collections `einstein-wiki` / `einstein-wiki-source` |
| Synthesis step | `LiteratureSynthesis` schema (queries, top-k hits, cross-source patterns, proposed approaches, gaps) | problem-id keying, mb path layout |
| Provenance field | `cited_sources: []` on every attempt log row | inner agent's specific cycle-log writer |
| Promotion signal | N-cite threshold on a source → concept candidate | persona triggers, problem inventory mapping |
| Council enrichment | persona prompt seeded with top-k hits per trigger category | the 10-persona core council list |
| Gap → ingest chain | stale-question detector → external search → human-gated ingest | arxiv-math categories, qmd refresh script |

The portability test [`agent-stance.md`](../../../.claude/rules/agent-stance.md)
demands ("would this scale to N=23 problems, multiple cycles, both authors?")
also applies here: every primitive in the left column was sized for the full
1450-source corpus and the multi-cycle log, not a single problem.

## Design implications for G1–G7

- **G1 (qmd vector-embed fix)**: LitSearch's 24.8-point dense-over-BM25 gap is
  the empirical case for fixing the Metal-compile failure now rather than
  deferring. Lex-only retrieval is half-blind for the cross-source connection
  work that Pattern A requires.
- **G2 (pre-cycle synthesis)**: implement Pattern D as `cb/scripts/research_synthesis.py`
  with the typed `LiteratureSynthesis` schema. Hybrid retrieval (post-G1) is
  load-bearing — the cross-source patterns aren't visible in keyword overlap
  alone.
- **G3 (council enrichment)**: ResearchAgent's entity-co-occurrence trick maps
  onto persona-trigger seeding. Persona output still respects
  [`council-dispatch`](../../../.claude/rules/council-dispatch.md) (questions,
  not solutions); citations make the questions falsifiable.
- **G4 (cycle-log + promotion candidates)**: Pattern C. CiteME's verifiability
  concern says the field must validate against existing `docs/source/*.md`
  paths, not accept free text.
- **G5 (gap → arxiv loop)**: closes the loop AHE leaves open (89% of
  regressions unforeseen) by escalating questions that survive 3+ cycles
  unanswered to external search. Not a fix for regression foresight; a
  release valve for stale gaps.
- **G6 (shadow A/B)**: AutoSurvey's $\rho = 0.54$ multi-judge calibration warns
  that any automated outcome metric will be noisy; the promotion gate must
  combine quantitative (findings-citing-sources count) and qualitative
  (human sign-off) signals.
- **G7 (first unattended run + extraction)**: after the run, distinguish the
  portable left-column primitives from the right-column einstein-specific
  ones, per the table above.

## Open questions

- The regression-foresight gap AHE names (89% unforeseen, recall 11.1%) is
  the most consequential open problem in this set. **What structural signal
  would surface a regression before the commit?** Filed separately as
  [`../questions/2026-05-25-regression-foresight-self-evolving-harness.md`](../questions/2026-05-25-regression-foresight-self-evolving-harness.md).
- Does citation provenance (Pattern C) actually compound, or do agents
  preferentially cite the same handful of high-recall sources and starve the
  long tail? Measurable in G7's cycle-log analysis.
- ResearchAgent's entity co-occurrence requires entity linking over 1450
  source papers; lighter weight is the qmd hybrid-search top-k. **Is the
  weaker retrieval sufficient, or does the entity store add a non-trivial
  cross-pollination boost?** Out of scope for this branch; surfaceable later.

## Triggering pattern

This finding is the literature anchor for the rest of the branch. Future cycles
that touch research-synthesis design should cite this page rather than
re-deriving the cross-source synthesis. Subsequent goals (G1–G7) should each
add their own finding citing both the source papers they implement against
*and* this finding, so the lineage is traceable.

See also: [`../concepts/agentic-harness.md`](../concepts/agentic-harness.md)
(the harness-loop sibling at the runtime layer),
[`finding-the-fertile-gaps.md`](finding-the-fertile-gaps.md) (Type-2 gap
methodology — what to consider),
[`cross-pollination-not-compute.md`](cross-pollination-not-compute.md) (the
filter — what to keep),
[`../../../.claude/rules/wiki-first-lookup.md`](../../../.claude/rules/wiki-first-lookup.md)
(the rule this finding's G2 makes mandatory at cycle-start).
