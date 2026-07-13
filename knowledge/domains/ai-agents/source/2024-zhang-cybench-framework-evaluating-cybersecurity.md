<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models
authors: [Andy K. Zhang, Neil Perry, Riya Dulepet, Joey Ji, Celeste Menders, Justin W. Lin, Eliot Jones, Gashon Hussein, Samantha Liu, D. Jasper, Pura Peetathawatchai, Ari Glenn, V. Sivashankar, Daniel Zamoshchin, Leo Glikbarg, Derek Askaryar, Mike Yang, Teddy Zhang, Rishi K. Alluri, Nathan Tran, Rinnara Sangpisit, Polycarpos Yiorkadjis, Kenny Osele, Gautham Raghupathi, D. Boneh, Daniel E. Ho, Percy Liang]
year: 2024
source_url: https://arxiv.org/abs/2408.08926
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models

**Authors:** Andy K. Zhang, Neil Perry, Riya Dulepet, Joey Ji, Celeste Menders, Justin W. Lin, Eliot Jones, Gashon Hussein, Samantha Liu, D. Jasper, Pura Peetathawatchai, Ari Glenn, V. Sivashankar, Daniel Zamoshchin, Leo Glikbarg, Derek Askaryar, Mike Yang, Teddy Zhang, Rishi K. Alluri, Nathan Tran, Rinnara Sangpisit, Polycarpos Yiorkadjis, Kenny Osele, Gautham Raghupathi, D. Boneh, Daniel E. Ho, Percy Liang  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2408.08926

## One-line
An open-source benchmark of 40 professional-level Capture-the-Flag tasks (with subtask decompositions) for evaluating LM agents on autonomous cybersecurity exploitation, grounded in human first-solve-time as a difficulty signal.

## Key claim
Frontier LM agents (Claude 3.5 Sonnet, GPT-4o, o1-preview, Claude 3 Opus) can solve CTF tasks with human first-solve-time (FST) up to 11 minutes but fail on every task with FST > 11 min (max FST = 24 h 54 min, a 136× gap), and FST is a strong empirical predictor of agent difficulty.

## Method
Tasks are specified by description + starter files + binary evaluator, executed by a Kali-Linux Docker agent following an act/execute/update memory loop inspired by ReAct, Reflexion, and MLAgentBench (response = reflection, plan/status, thought, log, action). Each task is decomposed into ordered subtasks with per-subtask Q/A for granular scoring; metrics are unguided performance, subtask-guided performance, and fractional subtask performance. Scaffolds ablated: structured bash, action-only, pseudoterminal, and bash + web search; evaluated on 8 LMs.

## Result
On the structured-bash agent (single attempt): Claude 3.5 Sonnet 17.5% unguided / 43.9% subtask; GPT-4o 12.5% / 28.7%; o1-preview 10.0% unguided but 46.8% subtask; Claude 3 Opus 10.0% / 36.8%; Gemini 1.5 Pro, Mixtral 8x22B, Llama 3.1 405B, Llama 3 70B trail at 5–7.5% unguided. With 3 attempts and pseudoterminal scaffolding, Claude 3.5 Sonnet rises to 27.5% subtask-guided and clears a 2 h 3 min FST task; scaffold effects are model-dependent (helps Claude, hurts GPT-4o). No model solves any task with FST > 11 min unguided.

## Key terms
Cybench, Capture the Flag, CTF benchmark, LM agent, subtask decomposition, first solve time, FST, agent scaffolding, ReAct, Reflexion, MLAgentBench, Kali Linux, pseudoterminal, Claude 3.5 Sonnet, GPT-4o, o1-preview, penetration testing, vulnerability exploitation, train-test overlap
