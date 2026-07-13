<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-verification]
title: "TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks"
authors: [Frank F. Xu, Yufan Song, Boxuan Li, Yuxuan Tang, Kritanjali Jain, Mengxue Bao, Zora Z. Wang, Xuhui Zhou, Zhitong Guo, Murong Cao, Mingyang Yang, Hao Yang Lu, Amaad Martin, Zhe Su, Leander Maben, Raj Mehta, Wayne Chi, Lawrence Jang, Yiqing Xie, Shuyan Zhou, Graham Neubig]
year: 2024
source_url: https://arxiv.org/abs/2412.14161
drive_file_id: 1RASAmHCQudHLoMXRUwv89PLglxz28H5D
text_source: pdf
ingested_by: agent
---

# TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks

**Authors:** Frank F. Xu, Yufan Song, Boxuan Li, et al. (CMU, Independent, Duke)  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2412.14161

## One-line
A self-hosted, reproducible benchmark of 175 realistic professional tasks (SWE, PM, HR, admin, finance) simulating a software company, used to measure how much of real knowledge work LLM agents can currently automate.

## Key claim
Current best LLM agents can autonomously complete a meaningful but still minority share of real-world professional tasks — the strongest agent (Claude 3.5 Sonnet) fully completed only 24.0% of 175 tasks — showing task automation is real but far from comprehensive, with long-horizon, multi-step tasks remaining largely out of reach.

## Method
Built a self-contained, self-hostable "digital workplace" using open-source software mimicking a real company's stack: GitLab (code/wiki), OwnCloud (docs), Plane (project management), and RocketChat (team chat), populated with realistic mock company data. Simulated colleagues (via the Sotopia platform, backed by Claude-3.5-Sonnet) can be messaged for clarifying info agents need but aren't given upfront. Tasks span 5 role categories (SWE, PM, HR, Admin, Finance) and require browsing, coding, running programs, and communicating with NPCs. Each task decomposes into checkpoints (weighted intermediate milestones) checked by deterministic Python evaluators (env/state checks) or LLM-based evaluators (Claude-3.5-Sonnet judging subjective/collaborative outputs, e.g., correct message sent to the right colleague). Two metrics: binary full completion score $S_{full}$, and partial completion score $S_{partial} = 0.5 \cdot \frac{\text{Result}}{\text{Total}} + 0.5 \cdot S_{full}$, which credits partial checkpoint progress while still strongly rewarding full completion. Baseline agents run on the OpenHands agent framework, tested across 7 backbone LLMs (Claude, GPT-4o, Gemini, Amazon Nova, Llama, Qwen).

## Result
- 175 total tasks across SWE, PM, HR, Admin, Finance categories, each with an English task intent plus multiple point-weighted checkpoints.
- Best model (Claude 3.5 Sonnet, 20241022) achieved 24.0% full completion score and 34.4% partial completion score — the top result among all 7 tested backbones.
- Simpler, well-scoped tasks are solvable autonomously; longer-horizon, multi-step tasks with ambiguity or required colleague interaction remain largely unsolved.
- Benchmark uniquely combines diverse real-world work coverage, NPC interaction requirements, long-horizon tasks with checkpoint-based grading, a versatile multi-interface environment (browser, terminal, chat, code), and full self-hosted reproducibility — differentiating it from prior agent benchmarks (e.g., WebArena, SWE-bench, τ-bench, Mind2Web) which each cover only a subset of these dimensions.

## Key terms
LLM agents, agentic benchmark, checkpoint-based evaluation, partial completion score, full completion score, OpenHands, simulated colleagues, Sotopia, self-hosted reproducible environment, long-horizon tasks, real-world task automation, NPC interaction
