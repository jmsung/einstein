<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "OpenHands: An Open Platform for AI Software Developers as Generalist Agents"
authors: [Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan, Yueqi Song, Bowen Li, Jaskirat Singh, Hoang H. Tran, Fuqiang Li, Ren Ma, Mingzhang Zheng, Bill Qian, Yanjun Shao, Niklas Muennighoff, Yizhe Zhang, Binyuan Hui, Junyang Lin, Robert Brennan, Hao Peng, Heng Ji, Graham Neubig]
year: 2024
source_url: https://arxiv.org/abs/2407.16741
drive_file_id: 1lyFaJ8v7oDthnJR1_FE0WnyogZrYoksF
text_source: paperclip
ingested_by: agent
---

# OpenHands: An Open Platform for AI Software Developers as Generalist Agents

**Authors:** Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan, Yueqi Song, Bowen Li, Jaskirat Singh, Hoang H. Tran, Fuqiang Li, Ren Ma, Mingzhang Zheng, Bill Qian, Yanjun Shao, Niklas Muennighoff, Yizhe Zhang, Binyuan Hui, Junyang Lin, Robert Brennan, Hao Peng, Heng Ji, Graham Neubig  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2407.16741

## One-line
An open-source MIT-licensed platform for building generalist LLM agents that interact with software via bash, Python (IPython), web browser, and a shared event-stream architecture inside a Docker sandbox.

## Key claim
A single generalist CodeActAgent — without per-benchmark prompt tuning — is competitive across software, web, and miscellaneous task categories: 26% on SWE-Bench Lite (claude-3.5-sonnet), 79.3% on HumanEvalFix (gpt-4o, 0-shot), 53.1% on GPQA Diamond (gpt-4o), and 15.3% on WebArena.

## Method
Three-component architecture: (1) an **agent abstraction** with a `step(state) -> action` interface over an event stream of past actions/observations; (2) a **Docker-sandboxed runtime** exposing `CmdRunAction` (bash), `IPythonRunCellAction` (Jupyter), and `BrowserInteractiveAction` (BrowserGym/Playwright DSL) via a REST action-execution API; (3) an extensible **AgentSkills** library of Python tools (edit_file, scroll, parse_pdf/image, etc.) auto-imported into the IPython environment. Multi-agent coordination via `AgentDelegateAction`; integration tests mock LLM calls with hash-keyed prompt-response pairs for determinism.

## Result
Across 15 integrated benchmarks (SWE-Bench, HumanEvalFix, BIRD, ML-Bench, BioCoder, APIBench, ToolQA, WebArena, MiniWoB++, GAIA, GPQA, AgentBench, MINT, EDA, ProofWriter), CodeActAgent v1.8 nearly matches specialist agents (e.g., 26% vs. Aider's 26.3% and Moatless's 26.7% on SWE-Bench Lite) and beats them on generality. HumanEvalFix: 79.3% (0-shot) vs. StarCoder2-15B's 48.6% non-agentic and SWE-Agent's 87.7% (1-shot). GPQA Diamond hits 53.1% with gpt-4o, exceeding GPT-4 few-shot CoT (38.8%). Average per-instance cost ~$1.10–$1.72 on SWE-Bench Lite.

## Key terms
OpenHands, OpenDevin, CodeAct, generalist agent, agent framework, Docker sandbox, event stream, IPython, BrowserGym, SWE-Bench, AgentSkills, agent-computer interface, multi-agent delegation, integration testing, LLM mocking
