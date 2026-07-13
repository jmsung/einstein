<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: "CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery"
authors: [Ao Qu, Handi Zheng, Zijian Zhou, Yihao Yan, Yihong Tang, S. Y. Ong, Fenglu Hong, Kai-Qing Zhou, Chonghe Jiang, Minwei Kong, Jiacheng Zhu, Xuan Jiang, Sirui Li, Cathy Wu, Bryan Kian Hsiang Low, Jinhua Zhao, P. Liang]
year: 2026
source_url: https://arxiv.org/abs/2604.01658
drive_file_id: 1bdJNCusfLgAigLxtjIquIRRHHRjZ8_ss
text_source: paperclip
ingested_by: agent
---

# CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery

**Authors:** Ao Qu, Handi Zheng, Zijian Zhou, Yihao Yan, Yihong Tang, S. Y. Ong, Fenglu Hong, Kai-Qing Zhou, Chonghe Jiang, Minwei Kong, Jiacheng Zhu, Xuan Jiang, Sirui Li, Cathy Wu, Bryan Kian Hsiang Low, Jinhua Zhao, P. Liang  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2604.01658

## One-line
A framework for autonomous multi-agent evolutionary search where long-running LLM agents coordinate through a shared persistent file-system memory, replacing fixed evolutionary-search heuristics with agent-level decisions about what to retrieve, when to evaluate, and what knowledge to externalize.

## Key claim
Delegating RETRIEVE / PROPOSE / EVALUATE / UPDATE decisions to autonomous agents and letting multiple agents co-evolve through shared memory yields new SOTA on 10 of 13 open-ended tasks, with 3–10× higher improvement rates and ~10× fewer evaluations than fixed evolutionary search (OpenEvolve, ShinkaEvolve, EvoX); on Anthropic's VLIW SIMD kernel-engineering task, 4-agent CORAL pushes the best known result from 1363 → 1103 cycles (a 20% gain, 133.9× speedup over baseline).

## Method
CORAL formalizes open-ended discovery as the 4-stage loop (retrieve → propose → evaluate → update) and shifts each stage from fixed rules to the agent. Three core mechanisms: (1) **shared persistent memory** as a structured filesystem (`attempts/`, `notes/`, `skills/`) symlinked into each agent's isolated git worktree; (2) **asynchronous multi-agent organization** — N stateful agents run in parallel with no messaging protocol, coordinating only via the shared file system; (3) **heartbeat interventions** — periodic injected prompts for per-iteration *reflection*, every-10-eval *consolidation*, and 5-plateau-triggered *pivot*. Safeguards include evaluator isolation (`.coral/private/`), per-attempt git commits, SIGINT-based session save/resume, and a 300s grader timeout.

## Result
Single-agent CORAL beats OpenEvolve / ShinkaEvolve / EvoX on all 11 math+systems tasks (e.g., Circle-Pack 2.6360 vs SOTA 2.6359 in 11 evals; 3rd-Autocorrelation 1.4557 in 5 evals; Erdős minimum overlap 0.38089). 4-agent co-evolution further improves stress-test scores by 18.3% on Kernel Engineering (1350→1103 cycles) and 5.0% on Polyominoes (80.2→84.2, or 89.4 with web search — also SOTA). Improvement-rate gains generalize to an open-source stack (MiniMax M2.5 + OpenCode). Mechanistic analysis attributes gains to local verification (61% local-test rate on Transaction Scheduling, 57% on Kernel Eng.) and knowledge accumulation (0.55–0.68 artifacts/attempt on advanced tasks vs 0.05 on standard).

## Key terms
autonomous evolution, multi-agent LLM, shared persistent memory, heartbeat reflection, OpenEvolve, ShinkaEvolve, AlphaEvolve, FunSearch, MAP-Elites, kernel engineering, Erdős minimum overlap, circle packing, open-ended discovery, skill library
