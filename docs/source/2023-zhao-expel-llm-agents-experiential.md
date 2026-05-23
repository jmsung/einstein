---
type: source
kind: paper
title: ExpeL: LLM Agents Are Experiential Learners
authors: Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Y. Liu, Gao Huang
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2308.10144
source_local: ../raw/2023-zhao-expel-llm-agents-experiential.pdf
topic: general-knowledge
cites:
---

# ExpeL: LLM Agents Are Experiential Learners

**Authors:** Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Y. Liu, Gao Huang  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2308.10144

## One-line
An LLM agent that autonomously gathers training-task experiences, distills them into natural-language insights, and retrieves similar successful trajectories at test time — improving without any gradient updates.

## Key claim
Cross-task experiential learning via insight extraction + similarity-based trajectory retrieval consistently beats ReAct/Act baselines and matches/exceeds Reflexion (which re-tries the same task) on HotpotQA, ALFWorld, and WebShop — e.g. ALFWorld 59% vs Reflexion R3 54%, with positive forward transfer HotpotQA → FEVER.

## Method
Three-stage pipeline: (1) gather success/failure trajectories via ReAct + Reflexion retry loop into an experience pool; (2) an `LLM_insights` (gpt-4-0613) iteratively maintains a list of insights using four operators — ADD, EDIT, UPVOTE, DOWNVOTE — applied over success/fail pairs and L-sized success batches, with importance counts and zero-removal to filter noise; (3) at inference, augment the policy prompt with the full insight list plus top-$k$ task-similar successful trajectories retrieved from a Faiss/kNN store using `all-mpnet-base-v2` embeddings. Transfer learning "finetunes" insights via a target-domain prompt with a few target fewshots.

## Result
ExpeL (gpt-3.5-turbo policy, gpt-4 insight extractor) outperforms ReAct/Act baselines across three domains; insights-only vs retrieve-only ablations show synergy (HotpotQA leans on insights 36/31%; ALFWorld leans on retrieval 50/55%; WebShop near-balanced 37/38%). Source→target transfer (HotpotQA→FEVER) shows positive forward transfer with only a small number of target fewshot examples. Emergent abilities observed qualitatively: analytical guessing when search exhausted, world-model belief updates (pan location), self-correction (putting back wrong objects).

## Why it matters here
General background; no direct arena tie — but methodologically relevant to the einstein self-improvement loop: ExpeL's ADD/EDIT/UPVOTE/DOWNVOTE insight curation with importance counts is a concrete design pattern for the wiki's findings→concepts promotion mechanism, and its success/failure-pair distillation parallels the failure-is-a-finding rule. Trajectory retrieval by task similarity is a candidate pattern for council-dispatch persona seeding.

## Open questions / connections
- How to manage insight list growth as it exceeds context window? (paper suggests retrieval over insights but does not implement.)
- Does insight quality depend critically on gpt-4 vs gpt-3.5 for the extractor — i.e. is there a minimum capability threshold below which the curation operators hallucinate?
- Relation to skill-library counting (`tried`/`top3`/`finding`) in einstein's cycle-discipline: ExpeL's importance counts are a weaker signal (no cross-problem citation tracking).
- Extends Reflexion (intra-task) to inter-task; relates to Voyager skill learning, generative-agents memory (recency/relevance/importance triple), prioritized experience replay.

## Key terms
ExpeL, experiential learning, LLM agent, ReAct, Reflexion, in-context learning, insight extraction, trajectory retrieval, Faiss kNN, all-mpnet-base-v2, transfer learning, prompt-based learning, HotpotQA, ALFWorld, WebShop, FEVER, self-improvement loop, cross-task memory
