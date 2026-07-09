---
type: source
kind: paper
title: "ChatMOF: An Autonomous AI System for Predicting and Generating Metal-Organic Frameworks"
authors: Y. Kang, Jihan Kim
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2308.01423
source_local: ../raw/2023-kang-chatmof-autonomous-system-predicting.pdf
topic: general-knowledge
cites:
---

# ChatMOF: An Autonomous AI System for Predicting and Generating Metal-Organic Frameworks

**Authors:** Y. Kang, Jihan Kim  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2308.01423

## One-line
An autonomous LLM agent (GPT-4 / GPT-3.5-turbo) that predicts properties of and inversely designs metal-organic frameworks (MOFs) by orchestrating databases, ML predictors, and a genetic algorithm.

## Key claim
A ReAct/MRKL-style agent with three components (agent, toolkit, evaluator) achieves $96.9\%$, $95.7\%$, and $87.5\%$ accuracy on search, property-prediction, and inverse-generation tasks for MOFs (GPT-4; excluding token-limit failures), and the LLM-driven genetic algorithm pushes mean accessible surface area from $\sim 3{,}748$ to $\sim 5{,}554\,\mathrm{m^2/g}$ over 3 generations.

## Method
LLM acts as central planner: parses a textual query, picks among toolkits (table-searcher over CoREMOF/QMOF/MOFkey/DigiMOF, MOFTransformer ML predictor, genetic-algorithm generator, ASE/LangChain utilities), and the evaluator decides whether to finalize or re-plan. Inverse design uses an LLM-driven genetic algorithm: MOFs are encoded as $\text{topology}+\text{block}_1+\text{block}_2$ gene strings (e.g. $\mathrm{tbo+N17+N10}$ for HKUST-1); the LLM selects parents from the database satisfying max/min/near-target objectives and emits child gene strings, which are built into structures and re-evaluated via ML.

## Result
GPT-4 outperforms GPT-3.5-turbo across all three tasks ($95\% / 91\% / 77.8\%$ for 3.5-turbo). Generated max-surface-area MOF ($\mathrm{rtl+N535+N234}$) predicted $6411.28\,\mathrm{m^2/g}$, Zeo++-verified $7647.62\,\mathrm{m^2/g}$ (third-highest in CoREMOF). Target-matching example: requested H$_2$ uptake $500\,\mathrm{cm^3/cm^3}$ at $100\,\mathrm{bar},77\,\mathrm{K}$ → predicted $499.998$, RASPA-verified $495.823$. Limitations: $\sim 4{,}000$-token cap restricts population size to $\sim 100$ (vs $10^5$ in classical GA), and "near-target" objectives can fail to retrieve any parents.

## Why it matters here
General background; no direct arena tie. Relevant as a **reference architecture for autonomous-loop agents** — the agent/toolkit/evaluator decomposition, ReAct/MRKL planning loop, LLM-as-GA-operator pattern, and the small-population-vs-token-budget tradeoff all map onto design choices for the einstein autonomous loop (council dispatch, toolkit selection, generator-style proposal of candidate solutions).

## Open questions / connections
- Can an LLM-driven GA with population $\sim 100$ compete with classical GA at population $\sim 10^5$ on continuous geometric optimization (sphere packing, kissing configurations)? The MOF surface-area result suggests yes for discrete combinatorial encodings but is silent on continuous coordinates.
- The "near-target" failure mode (no parent satisfies the band) is structurally identical to basin-rigidity failures in Einstein Arena — when does an LLM gene-mixer escape vs stay trapped?
- Extends ReAct (Yao et al.) and MRKL into materials science; complements HuggingGPT-style model selection. Open: how to scale beyond fine-tuned model registry to a shared open repository.

## Key terms
ChatMOF, autonomous LLM agent, ReAct, MRKL, HuggingGPT, MOFTransformer, genetic algorithm, inverse design, metal-organic framework, CoREMOF, QMOF, GPT-4, LangChain, toolkit orchestration
