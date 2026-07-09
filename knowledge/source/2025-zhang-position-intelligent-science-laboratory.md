---
type: source
kind: paper
title: "Position: Intelligent Science Laboratory Requires the Integration of Cognitive and Embodied AI"
authors: Sha Zhang, Suorong Yang, Tong Xie, Xiangyuan Xue, Zixuan Hu, Rui Li, Wenxi Qu, Zhenfei Yin, Tianfan Fu, Di Hu, Andrés M Bran, Nian Ran, B. Hoex, Wangmeng Zuo, P. Schwaller, Wanli Ouyang, Lei Bai, Yanyong Zhang, Ling-Yu Duan, Shixiang Tang, Dongzhan Zhou
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2506.19613
source_local: ../raw/2025-zhang-position-intelligent-science-laboratory.pdf
topic: general-knowledge
cites:
---

# Position: Intelligent Science Laboratory Requires the Integration of Cognitive and Embodied AI

**Authors:** Sha Zhang, Suorong Yang, Tong Xie, Xiangyuan Xue, Zixuan Hu, Rui Li, Wenxi Qu, Zhenfei Yin, Tianfan Fu, Di Hu, Andrés M Bran, Nian Ran, B. Hoex, Wangmeng Zuo, P. Schwaller, Wanli Ouyang, Lei Bai, Yanyong Zhang, Ling-Yu Duan, Shixiang Tang, Dongzhan Zhou  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2506.19613

## One-line
Position paper proposing Intelligent Science Laboratories (ISLs) — a three-layer architecture (foundation model + agent + embodied robotics) that closes the loop between AI reasoning and physical wet-lab experimentation.

## Key claim
Current AI scientist systems are stuck in virtual environments and current automated labs are rigidly pre-scripted; only a tightly integrated cognitive+embodied closed-loop system can fully automate scientific discovery. The authors formalize this as a four-level taxonomy (L0 script automation → L3 self-evolving discovery) and argue L2+ requires unifying foundation models, a meta-agent workflow orchestrator, and a perception/navigation/manipulation embodied layer under a Real2Sim2Real cycle.

## Method
Conceptual / position paper — no theorem, no experiment. Surveys prior work on AI scientists, self-driving labs, foundation models (Galactica, ChemCrow, SciBERT, MatSciBERT, AlphaFold), embodied policies (diffusion policy, $\pi_0$, RT-X), meta-learning (MAML), PEFT (LoRA, adapters), and Bayesian optimization, then synthesizes a layered architecture with a Model-Call Protocol (MCP) abstraction for invoking proprietary expert models as callable agents.

## Result
No quantitative result. Deliverables: (1) a four-level autonomy taxonomy mapping capabilities across Foundation/Agent/Embodied layers; (2) a six-stage scientific workflow (problem formulation → literature → proposal → execution → analysis → conclusion); (3) identified open challenges including transparent-labware perception, fine-grained liquid handling, heterogeneous sensor fusion, sim-to-real gap, equity/data-governance concerns.

## Why it matters here
General background; no direct arena tie. The Einstein Arena agent is a purely *cognitive* loop on math problems (no wet-lab, no embodiment), so the embodied layer is irrelevant — but the paper's framing of a meta-agent that auto-composes workflows from modular agents and its closed-loop "hypothesis → execute → feedback → update" structure parallel the einstein self-improvement-loop and council-dispatch rules.

## Open questions / connections
- Does the meta-agent's "automatic workflow design" (vs fixed templates) translate to council-dispatch / persona-selection in a math-solving agent — i.e., should persona selection itself be learned rather than hard-coded?
- MCP-style abstraction for wrapping proprietary models (AlphaFold cited as canonical example) — analog for einstein would be wrapping solvers (HiGHS LP, mpmath, CMA-ES) behind a unified call interface.
- Four-level autonomy taxonomy (L0–L3) as a possible self-assessment frame for the einstein cycle-log: where on L0–L3 is the current loop, and what specifically gates L2 → L3?

## Key terms
intelligent science laboratory, ISL, foundation model, embodied AI, meta-agent, closed-loop learning, Model-Call Protocol, MCP, Real2Sim2Real, sim-to-real, self-driving lab, autonomous experimentation, AlphaFold, diffusion policy, meta-learning, MAML, LoRA, PEFT, Bayesian optimization, agentic workflow, four-level autonomy taxonomy
