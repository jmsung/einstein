<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "AgentBench: Evaluating LLMs as Agents"
authors: [Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, Jie Tang]
year: 2023
doi: 10.48550/arXiv.2308.03688
source_url: https://doi.org/10.48550/arXiv.2308.03688
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# AgentBench: Evaluating LLMs as Agents

## TL;DR
AgentBench is a multi-dimensional benchmark of 8 distinct interactive environments (code-, game-, and web-grounded) that evaluates LLMs as autonomous agents; across 29 API-based and open-source models it exposes a large capability gap between top commercial LLMs (gpt-4) and OSS models ≤70B, attributing failures mainly to weak long-term reasoning, decision-making, and instruction following.

## Key findings
- **Benchmark structure**: 8 environments across 3 groundings — Code (Operating System, Database, Knowledge Graph), Game (Digital Card Game/Aquawar, Lateral Thinking Puzzles, House-Holding/ALFWorld), Web (Web Shopping/WebShop, Web Browsing/Mind2Web). Five of eight are newly created. Dev/Test splits sized 269/1,014 samples (~3k/11k inference calls, comparable to MMLU).
- **Large commercial-vs-OSS gap**: gpt-4 scores an overall (OA) **4.01**, best on 6 of 8 environments. Average API-based model OA = **2.32** vs OSS average = **0.51**. Best OSS model ≤70B is codellama-34b at OA **0.96**, still trailing gpt-3.5-turbo. All API models score above 1.00.
- **Standout single results**: gpt-4 reaches **78%** success on House-Holding; **74.5** on Knowledge Graph; claude-3 (opus) leads Digital Card Game at **51.7**.
- **Failure-mode taxonomy** (5 finish reasons): Context Limit Exceeded (only in 2,048-ctx text-davinci models), Invalid Format (IF), Invalid Action (IA), Task Limit Exceeded (TLE), and Complete. TLE is the dominant failure — indicating weak multi-turn reasoning. DB and Card Game suffer most from IF (strict formatting); House-Holding and Web Browsing from IA (actions outside the allowed space).
- **Instruction following matters**: OSS models show 10.4% IF and 13.6% IA vs commercial 6.0% and 4.6%. Even gpt-4 occasionally drops required "Action:" labels.
- **Code training is a double-edged sword**: codellama beats llama-2 on procedural tasks (Web Shopping) but underperforms on Digital Card Game and OS, where general reasoning matters more than writing bash — a trade-off between procedure-following and general thinking.
- **High-quality alignment helps**: vicuna-13b (aligned on gpt-4/gpt-3.5 ShareGPT data) outperforms llama-2-13b on the same base and rivals 3× larger codellama-34b.
- **Scaling anomaly**: llama-2-13b and llama-2-70b perform similarly, suggesting the 70B model was under-trained (2T tokens for both, contra Chinchilla scaling) and/or inadequately instruction-aligned.
- **Repetition drives TLE**: >90% of TLE trajectories contain two responses in the last 10 rounds with Rouge-L ≥ 0.8 — models loop/repeat prior content. TLE trajectories average 25.5 rounds vs ~7.95 for completed tasks; completed tasks median 6 rounds / 1,850 tokens.

## Methods (brief)
All environments are reformulated as text-only interactive tasks evaluated with primitive CoT prompting (no ensemble/reflection/search), greedy decoding (temperature=0), and a Thought+Action single-round format adapted from ReAct. A Server–Client toolkit decouples task servers (Dockerized, isolated workers), agent servers (HTTP API), and an evaluation client that uses a max-flow (Edmonds–Karp) algorithm to optimally assign agent–task evaluation pairs; evaluation is resumable. An overall score normalizes each task to average 1.0 across models then averages, preventing high-scoring tasks (e.g. Web Shopping) from dominating.

## Limitations
OSS models capped at ≤70B (compute-limited), so larger open models are untested. Results reflect 2023–2024 model snapshots and primitive single-trial CoT — advanced strategies (reflection, search, self-consistency) are deliberately excluded and would shift scores. Some environments use small test sets (e.g. 500 KG/Web tasks, 134 ALFWorld tasks) and automatic LTP judging is noted to be more lenient than human evaluation.

## Citations of interest
- Yao et al. 2023b (**ReAct**) — synergizing reasoning and acting; the Thought+Action prompting format AgentBench adopts.
- Shridhar et al. 2020b (**ALFWorld**) — embodied text-game environment used for the House-Holding task.
- Yao et al. 2022 (**WebShop**) — simulated e-commerce environment and reward function for Web Shopping.
- Deng et al. 2023 (**Mind2Web**) — generalist web-agent benchmark adapted for Web Browsing.
- Wei et al. 2022b (**Chain-of-Thought**) — the reasoning strategy underlying all evaluations.
- Hoffmann et al. 2022 (**Chinchilla** scaling laws) — invoked to explain llama-2-70b's under-training anomaly.
