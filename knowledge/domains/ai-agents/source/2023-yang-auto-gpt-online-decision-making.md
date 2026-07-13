<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: "Auto-GPT for Online Decision Making: Benchmarks and Additional Opinions"
authors: [Hui Yang, Sifu Yue, Yunzhong He]
year: 2023
source_url: https://arxiv.org/abs/2306.02224
drive_file_id: 1WiD64jgDh1nqGZxyyCxsYtwtcRWenqpQ
text_source: paperclip
ingested_by: agent
---

# Auto-GPT for Online Decision Making: Benchmarks and Additional Opinions

**Authors:** Hui Yang, Sifu Yue, Yunzhong He  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2306.02224

## One-line
Benchmarks Auto-GPT-style LLM agents (GPT-4, GPT-3.5, Claude, Vicuna) on online decision-making tasks and shows that injecting top-$k$ "additional opinions" from a small supervised expert model into the agent's prompt significantly boosts performance without fine-tuning.

## Key claim
On WebShop (50 instructions) and ALFWorld (134 unseen games), GPT-4 Auto-GPT augmented with top-$k$ imitation-learning (IL) suggestions beats both the IL baseline and vanilla Auto-GPT: WebShop success rate $0.24 \to 0.32$ (top-5 IL opinions) vs IL baseline $0.227$; ALFWorld success rate $0.485 \to 0.515$ (top-1 IL opinion) vs IL baseline $0.306$.

## Method
Auto-GPT is adapted by exposing each environment action as a "tool" with 1–3 few-shot demonstrations and feeding the high-level instruction as the goal. The Additional Opinions algorithm samples top-$k$ candidate actions from an external expert (here, BART+BERT IL models for WebShop; DAgger IL for ALFWorld) and injects them into the LLM context with a "use this suggestion as a reference and make your own judgement" template before the LLM commits to an action. No LLM fine-tuning; only the IL expert is trained.

## Result
GPT-4 with top-5 IL opinions on WebShop: success $0.32$, reward $61.55$, precision $0.372$ — best across all variants. GPT-4 with top-1 IL on ALFWorld: success $0.515$, precision $0.789$. Ablations: random opinions to GPT-3.5 collapse performance to rule-baseline ($0.06$ success, reward $22.3$); GPT-3.5 is easily confused by repetitive IL advice while GPT-4 robustly disagrees with bad suggestions (disagreement rate $0.854$ on ALFWorld). Vicuna fails to produce parseable outputs ($0.0$). Claude is faster but consistently weaker than GPT-4.

## Key terms
Auto-GPT, LLM agents, online decision making, WebShop, ALFWorld, imitation learning, DAgger, additional opinions, top-k sampling, ReAct, Reflexion, chain-of-thought, GPT-4, expert ensembling, in-context learning
