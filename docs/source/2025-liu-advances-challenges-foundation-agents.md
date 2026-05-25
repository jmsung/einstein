---
type: source
kind: paper
title: Advances and Challenges in Foundation Agents: From Brain-Inspired Intelligence to Evolutionary, Collaborative, and Safe Systems
authors: Bangbang Liu, Xinfeng Li, Jiayi Zhang, Jinlin Wang, Tanjin He, Sirui Hong, Hongzhang Liu, Shaokun Zhang, Kaitao Song, Kunlun Zhu, Yuheng Cheng, Suyuchen Wang, Xiaoqian Wang, Yuyu Luo, Haibo Jin, Peiyan Zhang, Ollie Liu, Ollie Liu, Jiaqi Chen, Huan-Rui Zhang, Zhaoyang Yu, Hao Shi, Boyan Li, D. Wu, Dekun Wu, Xiao Jia, Jiawei Xu, Jinyu Xiang, Yizhang Lin, Tianming Liu, Tongliang Liu, Yu Su, Huan Sun, Glen Berseth, Jianyun Nie, Ian T. Foster, Logan Ward, Qingyun Wu, Yu Gu, Mingchen Zhuge, Xiangru Tang, Haohan Wang, Jiaxuan You, Chi Wang, Jian Pei, Qiang Yang, Xiaoli Qi, Chenglin Wu
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2504.01990
source_local: ../raw/2025-liu-advances-challenges-foundation-agents.pdf
topic: general-knowledge
cites:
---

# Advances and Challenges in Foundation Agents: From Brain-Inspired Intelligence to Evolutionary, Collaborative, and Safe Systems

**Authors:** Bangbang Liu, Xinfeng Li, Jiayi Zhang, Jinlin Wang, Tanjin He, Sirui Hong, Hongzhang Liu, Shaokun Zhang, Kaitao Song, Kunlun Zhu, Yuheng Cheng, Suyuchen Wang, Xiaoqian Wang, Yuyu Luo, Haibo Jin, Peiyan Zhang, Ollie Liu, Ollie Liu, Jiaqi Chen, Huan-Rui Zhang, Zhaoyang Yu, Hao Shi, Boyan Li, D. Wu, Dekun Wu, Xiao Jia, Jiawei Xu, Jinyu Xiang, Yizhang Lin, Tianming Liu, Tongliang Liu, Yu Su, Huan Sun, Glen Berseth, Jianyun Nie, Ian T. Foster, Logan Ward, Qingyun Wu, Yu Gu, Mingchen Zhuge, Xiangru Tang, Haohan Wang, Jiaxuan You, Chi Wang, Jian Pei, Qiang Yang, Xiaoli Qi, Chenglin Wu  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2504.01990

## One-line
A book-length survey framing LLM-based intelligent agents as modular, brain-inspired architectures spanning cognition, memory, world models, reward, emotion, perception, action, self-evolution, multi-agent collaboration, and safety.

## Key claim
Foundation agents are best designed as modular systems whose components map onto human-brain functionalities (memory, world-modeling, reward processing, goals, emotion), and whose self-improvement, collective intelligence, and safety properties can be analyzed within a unified taxonomy of optimization paradigms (prompt / workflow / tool / online–offline self-improvement) and intrinsic/extrinsic threat surfaces.

## Method
Literature synthesis across cognitive science, neuroscience, and LLM-agent research, organized into four parts: (I) core modules (cognition, memory, world model, reward, emotion, perception, action), (II) self-evolution (prompt/workflow/tool optimization, iterative LLM optimization, online/offline self-improvement, scientific-discovery agents formalized via a KL-divergence intelligence measure), (III) multi-agent systems (topologies, collaboration paradigms, communication protocols, collective intelligence), and (IV) safety (jailbreak/prompt-injection/hallucination/poisoning, perception and action threats, agent–memory/environment/agent interactions, superalignment, scaling laws for safety).

## Result
No new theorems or numerical bounds; the contribution is the unified modular taxonomy, the agent-loop notation, the brain-to-module mapping, the optimization-space decomposition (prompt × workflow × tool, online vs. offline, hybrid), the KL-divergence-based formulation of intelligence growth via scientific discovery ($I \propto D_{KL}(p_{\text{posterior}} \| p_{\text{prior}})$-style framing), and a structured catalog of intrinsic/extrinsic agent threats with mitigation strategies.

## Why it matters here
General background; no direct arena tie — the survey informs the *agent-architecture* side of einstein (council dispatch, self-improvement loop, cycle-discipline, prompt/workflow/tool optimization, multi-agent safety) rather than any specific math problem; relevant when designing the autonomous-loop agent itself, especially the gap→ingest→distill cycle and council-of-personas collaboration patterns.

## Open questions / connections
- How to operationalize the KL-divergence intelligence measure as a *metric* in `docs/agent/metrics.md` for measuring per-cycle wiki-information gain.
- Which workflow-optimization paradigms (edges vs nodes) best suit the einstein math-solving protocol's fixed 10-step loop?
- Mapping the survey's online/offline self-improvement dichotomy onto einstein's cycle-log + skill-library compounding mechanism — extends prior agentic-system findings in the wiki (AFlow, ADAS, GEPA, TextGrad, ExpeL, Voyager, Self-Refine).

## Key terms
foundation agents, modular agent architecture, brain-inspired AI, agent memory, world model, reward modeling, intrinsic reward, multi-agent systems, collective intelligence, prompt optimization, workflow optimization, tool optimization, online self-improvement, offline self-improvement, KL-divergence intelligence measure, superalignment, jailbreak, prompt injection, agent safety, scaling laws
