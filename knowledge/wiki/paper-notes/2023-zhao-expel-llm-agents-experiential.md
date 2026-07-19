---
type: note
kind: paper-relevance
about: 2023-zhao-expel-llm-agents-experiential
canonical: ../../domains/ai-agents/source/2023-zhao-expel-llm-agents-experiential.md
---

# Relevance note — ExpeL: LLM Agents Are Experiential Learners

Canonical distillation: [`2023-zhao-expel-llm-agents-experiential.md`](../../domains/ai-agents/source/2023-zhao-expel-llm-agents-experiential.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — but methodologically relevant to the einstein self-improvement loop: ExpeL's ADD/EDIT/UPVOTE/DOWNVOTE insight curation with importance counts is a concrete design pattern for the wiki's findings→concepts promotion mechanism, and its success/failure-pair distillation parallels the failure-is-a-finding rule. Trajectory retrieval by task similarity is a candidate pattern for council-dispatch persona seeding.

## Open questions / connections
- How to manage insight list growth as it exceeds context window? (paper suggests retrieval over insights but does not implement.)
- Does insight quality depend critically on gpt-4 vs gpt-3.5 for the extractor — i.e. is there a minimum capability threshold below which the curation operators hallucinate?
- Relation to skill-library counting (`tried`/`top3`/`finding`) in einstein's cycle-discipline: ExpeL's importance counts are a weaker signal (no cross-problem citation tracking).
- Extends Reflexion (intra-task) to inter-task; relates to Voyager skill learning, generative-agents memory (recency/relevance/importance triple), prioritized experience replay.
