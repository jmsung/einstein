<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "SFR-DeepResearch: Towards Effective Reinforcement Learning for Autonomously Reasoning Single Agents"
authors: [Xuan-Phi Nguyen, Shrey Pandit, Revanth Gangi Reddy, Austin Xu, Silvio Savarese, Caiming Xiong, Shafiq Joty]
year: 2025
doi: 10.48550/arxiv.2509.06283
source_url: https://doi.org/10.48550/arxiv.2509.06283
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# SFR-DeepResearch: Towards Effective Reinforcement Learning for Autonomously Reasoning Single Agents

## TL;DR
A continual-RL recipe that turns reasoning-optimized open LLMs into autonomous single-agent Deep Research systems using only three primitive tools (search, browse, Python) and entirely synthetic training data; the best variant (SFR-DR-20B, from gpt-oss-20b) reaches 28.7% on Humanity's Last Exam, rivaling larger proprietary agents.

## Key findings
- **Single-agent over multi-agent.** The authors argue an autonomous single agent—one LLM deciding its next tool call from context with no intermediate directives—generalizes better to unseen tasks than role-scripted multi-agent workflows, and can itself be dropped into a multi-agent system as a sub-agent.
- **Minimal toolset is a design choice, not a limitation.** Only `search_internet` (top-10 results via serper.dev), `browse_page` (HTML→Markdown, hyperlinks *stripped* so new URLs come only from search, with `section_id` scrolling), and a *stateless* `code_interpreter` (5-min timeout, no shell/package-install/filesystem). Easy tools under-challenge the agent during RL.
- **Model-family-specific scaffolding.** For QwQ-32B and Qwen3-8B, the multi-turn tool conversation is recast as an *iterative single-turn* contextual QA problem (all prior calls/results packed into one growing user turn), and **prior long-CoT "thinking" tokens are dropped** each step—naively interleaving them fills context and degrades into erratic output. This gave training-free gains (e.g. +10% absolute FRAMES on 32B, Table 2). gpt-oss-20b has stronger multi-turn ability and keeps its native harmony template.
- **Self-managed memory = unbounded context.** A `clean_memory(content)` tool lets the agent overwrite its own context when nearing a memory limit `Lmem < L`; any other tool call returns a "memory overflow" error until it cleans up. gpt-oss variants instead edit/delete individual past tool results.
- **Length-normalized REINFORCE.** Step-level advantage is the trajectory reward (z-scored within a group) divided by trajectory length `Ti` (Eq. 1), so steps in long rollouts carry lower magnitude. Without it, long failing trajectories dominate the loss and the agent degenerates into **repetitive identical tool calls**—tool usage spikes while HLE performance collapses (Fig. 2). Same reward at every step; no intermediate rewards.
- **Trajectory filtering + partial rollouts.** Invalid/truncated/malformed trajectories are dropped and positive:negative ratios bounded to prevent collapse; unfinished rollouts are reused as fresh independent initial states (Monte-Carlo restart with the same policy, unlike Kimi's continue-with-updated-policy).
- **Synthetic data harder than existing sets.** Iteratively constructed multi-hop QA (plus math/code and long-form report tasks with LLM rubrics) is hard enough that OpenAI Deep Research with o3 scores <65% and an o4-mini agent needs up to 50 tool calls per question.
- **Results (Pass@1, contamination blocklist):** SFR-DR-20B — FRAMES 82.8, GAIA 66.0, HLE 28.7 (a 65% relative gain over base gpt-oss-20b's 17.3). SFR-DR-32B — 72.0 / 52.4 / 16.2. SFR-DR-8B — 63.3 / 41.7 / 13.2.
- **More tool calls ≠ better.** Gains come from *diverse, strategic* calls. SFR-DR-20B makes ~10× more tool calls than QwQ/Qwen3 variants (which often just reason internally) yet emits <2,000 tokens/step (4–5× more token-efficient); RL *shrank* its per-step length while lengthening the Qwen-family's (Fig. 3).

## Methods (brief)
Continual RLVR on three reasoning-optimized backbones (QwQ-32B, Qwen3-8B, gpt-oss-20b) with a clipped-surrogate REINFORCE variant, length-normalized advantages, trajectory filtering, and partial-rollout reuse. The same base LLM serves as verifier—semantic-consistency reward for short-form QA, multi-criteria weighted + ranking score (factuality, compliance, writing, citations) for reports. In-house pipeline co-locates SGLang inference, verifier, and training models on shared GPUs; tools run locally with result caching; a domain blocklist (e.g. huggingface.co) prevents benchmark contamination.

## Limitations
Synthetic-only training and LLM-as-verifier rewards (no human-graded gold for long-form). Scaffolding is hand-tuned per model family (single-turn recast helps Qwen-family but gpt-oss uses native multi-turn), so the recipe is not fully one-size-fits-all. Reported baseline numbers were re-run under the authors' own blocklist and may differ from originals; results are Pass@1 only.

## Citations of interest
- OpenAI Deep Research / o3 system card [30] — the proprietary single-agent DR system this work targets and uses as a strong baseline.
- gpt-oss-20b/120b model card [1] — the backbone for the best variant SFR-DR-20B.
- Humanity's Last Exam [33], GAIA [24], FRAMES [15] — the three evaluation benchmarks.
- Kimi-Researcher [26] — end-to-end RL single-agent DR; contrast point for partial-rollout handling.
- DAPO [50] / DeepSeekMath GRPO [38] — RL objectives the length-normalized advantage modifies.
- ReAct [49] — foundational reasoning-and-acting agent paradigm.
- Search-time data contamination [11] — motivates the evaluation blocklist (up to 3.4% of HLE samples contaminable).
