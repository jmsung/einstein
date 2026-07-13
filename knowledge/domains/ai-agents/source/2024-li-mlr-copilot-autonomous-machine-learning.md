<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-ml]
title: "MLR-Copilot: Autonomous Machine Learning Research based on Large Language Models Agents"
authors: [Ruochen Li, Teerth Patel, Qingyun Wang, Xinya Du]
year: 2024
source_url: https://arxiv.org/abs/2408.14033
drive_file_id: 1-uQnCVRtunT2amdhcMbJsjy4ylgYSFF6
text_source: paperclip
ingested_by: agent
---

# MLR-Copilot: Autonomous Machine Learning Research based on Large Language Models Agents

**Authors:** Ruochen Li, Teerth Patel, Qingyun Wang, Xinya Du  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2408.14033

## One-line
A three-stage LLM-agent framework that automates ML research by generating ideas from papers, implementing experiments via retrieved prototype code/models/data, and iteratively executing with debugging + human feedback.

## Key claim
With an RL-tuned IdeaAgent (fine-tuned Llama3-7B) plus an ExperimentAgent, the system beats one-pass prompting on 5 ML tasks: average improvement over SOTA prototype is 44.16% (Claude-3.7), with a 50% success rate (≥10% improvement) across 8 trials, vs 0% for 1-Prompt baseline.

## Method
Stage 1: IdeaAgent ingests a paper $c$ via Semantic Scholar API, extracts task $t$, gaps $g$, keywords $k$, retrieves related works $R$, and generates methodology $h$ + experiment plan $e$ to produce research idea $RI = \{P, R, h, e\}$. The agent is SFT'd on 1,000 paper-idea pairs then RL-tuned with multi-dimensional reward models for novelty, feasibility, effectiveness. Stages 2–3: ExperimentAgent retrieves prototype code $I$ and HuggingFace models $M$ / datasets $D$, integrates them into setup $S$, then executes with iterative debugging and optional human feedback.

## Result
On 5 tasks (SemRel, IMDB, Spaceship-Titanic, ELLIPSE feedback, Identify-Contrails), Claude-3.7 backbone gives mean +44.16% over SOTA prototype (best per-task: IMDB +76.2%, ELLIPSE +60.2%); GPT-4 gives +39.74%; Claude-2.1 +38.0%. IdeaAgent beats BaseLLM and ResearchAgent on all manual + automated Likert criteria (clarity 4.4, rigor 4.3, innovativeness 3.9) with lower similarity-to-existing (0.13 vs 0.32), suggesting more novelty.

## Key terms
LLM agents, autonomous research, idea generation, experiment automation, reinforcement learning fine-tuning, reward models, novelty feasibility effectiveness, prototype code retrieval, HuggingFace model retrieval, iterative debugging, human-in-the-loop, MLAgentBench, AI Scientist
