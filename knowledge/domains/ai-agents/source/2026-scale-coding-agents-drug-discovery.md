<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: blog
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "Coding agents in drug discovery (Scale AI Labs)"
authors: [Afra Feyza Akyürek, Xinming Tu, Sofia Monasdotter, Yuanhao Qu, Sergey Chekhov, Sami Hassaan]
year: 2026
source_url: https://labs.scale.com/blog/coding-agents-drug-discovery
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Coding agents in drug discovery (Scale AI Labs)

**Source:** labs.scale.com · 2026-06-04
**Authors:** Akyürek, Tu, Monasdotter, Qu, Chekhov, Hassaan (Scale AI Labs)

## TL;DR

Three state-of-the-art coding agents were evaluated on **66 expert-curated drug-discovery tasks**. The binding constraint is **planning and multi-step execution**, not scientific knowledge — agents handle individual steps competently but lose the thread across long workflows.

## Key results

- **Codex (GPT-5.5):** 62% avg accuracy; strongest on structural reasoning (73%) and database screening.
- **Gemini 3.1 Pro:** 53%; best at open-ended exploration (iterative PubChem/literature reformulation).
- **Claude Opus 4.7:** 46%; best on sequential, constraint-heavy tasks.

## Where agents fail

- **Long-horizon pipelines** defeat all three.
- **Retrieval- and biology-heavy** tasks are harder than chemistry-focused ones.
- Recurring failure: **dropping contextual constraints mid-workflow** (e.g., losing "melanoma scope" while ranking genes).
- Concrete errors: using canonical (neutral) instead of bound-state protonation for ligand charges; a six-step Parkinson's target pipeline failing at a different step per model.

## Key positive signal

When researchers supplied **expert methodology** (the sequence of steps, without revealing answers), "a majority of the tasks that all three models had missed unaided became solvable."

