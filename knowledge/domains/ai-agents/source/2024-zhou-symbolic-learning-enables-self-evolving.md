<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Symbolic Learning Enables Self-Evolving Agents
authors: [Wangchunshu Zhou, Yixin Ou, Shengwei Ding, Long Li, Jialong Wu, Tiannan Wang, Jiamin Chen, Shuai Wang, Xiaohua Xu, Ningyu Zhang, Huajun Chen, Yuchen Eleanor Jiang]
year: 2024
doi: 10.48550/arXiv.2406.18532
source_url: https://doi.org/10.48550/arXiv.2406.18532
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Symbolic Learning Enables Self-Evolving Agents

## TL;DR
The paper introduces **agent symbolic learning**, a framework that lets LLM-based language agents optimize themselves end-to-end by mimicking back-propagation and gradient descent in *natural-language space* — treating prompts, tools, and pipeline structure as "learnable weights" jointly tuned against a language-based loss, enabling "self-evolving agents" that update after deployment.

## Key findings
- **Core analogy:** an agent pipeline ↔ a neural net's computational graph; a node ↔ a layer; the prompts + tools of a node ↔ the layer's weights. The framework implements language-based **loss**, **gradients**, and **optimizers** to jointly optimize all symbolic components, rather than tuning isolated prompts/nodes (the limitation of DSPy, GPTSwarm, Agent-pro, AgentOptimizer).
- **Procedure (Algorithm 1):** (1) *forward pass* = normal agent execution but stores input/output/prompts/tools per node in a **trajectory**; (2) a prompt-based **language loss function** evaluates the trajectory, emitting both NL comments and a 0–10 numeric score; (3) **back-propagation** iterates last→first node, generating per-node "language gradients" (textual analyses/reflections) conditioned on the downstream node's gradient; (4) three **symbolic optimizers** — PromptOptimizer, ToolOptimizer (edit/delete/create tools), PipelineOptimizer (add/delete/move nodes) — update the agent.
- **Supervised vs. unsupervised:** loss can use ground-truth (supervised) or evaluate purely from task description with **no ground-truth** (unsupervised) — the latter is what enables self-evolution in the wild.
- **Engineering details:** illegal code-space updates retried up to 3× then discarded; a **rollback** strategy reverts updates if language-loss-evaluated performance drops; a per-prompt "learning rate" controls update aggressiveness; a **batched training** variant feeds a batch of per-node gradients (mimicking mini-batch SGD) for stability.
- **Standard benchmarks (Table 1):** consistently beats GPTs, Agents, Agents+AutoPE, DSPy. Largest gain on MATH — GPT-4 53.1→**60.7** acc; GPT-3.5 23.2→**38.8**. HumanEval GPT-4 Pass@1 71.7→**85.8**. HotPotQA GPT-4 F1 44.3→**54.0**. Baseline prompt-optimizers (AutoPE, DSPy) were unstable — sometimes degrading performance.
- **Complex tasks (Tables 2–3):** software development avg executability score 1.6 (GPTs) / 2.4 (Agents) → **3.8** (Ours, out of 4) across 5 games. Creative writing GPT-4 score 6.0→**7.4**, beating even Tree-of-Thoughts (6.8). The framework spontaneously recovered a plan→write→revise pipeline and a MetaGPT-like SOP for software dev.
- **Initialization matters:** simplest initial agents optimize best; over-engineered initial agents become unstable — suggesting a future "pre-train then adapt" paradigm for general-purpose agents.

## Methods (brief)
Proof-of-concept experiments on HotpotQA (hard split), MATH, HumanEval (tools disabled for comparability), plus two open-ended agentic tasks (creative writing scored by GPT-4; software dev scored 1–4 by executability). Built atop the open-source *Agents* framework (config-file-defined pipelines, easing programmatic edits), tested with gpt-3.5-turbo-0125 and gpt-4-turbo-0409. All loss/gradient/optimizer prompt templates are provided in the appendix and open-sourced.

## Limitations
Proof-of-concept scale only; GPT-3.5/GPT-4-turbo specific; "language loss" and creative-writing/GPT-4-score metrics are themselves LLM-judged and noisy; software-dev evaluated on 5 simple games with a coarse 1–4 score. No fine-tuning of the LLM backbone (explicitly left to future work), so "all components" optimization excludes model weights. No standardized benchmark exists for agent-learning, which the authors flag as a community gap.

## Citations of interest
- **Khattab et al. 2023 (DSPy)** — search-based prompt/pipeline compilation; the key baseline whose isolated-component, equation-defined-metric limits this work addresses.
- **Zhuge et al. 2024 (GPTSwarm)** — language agents as optimizable graphs; iterative combinatorial optimization compared against.
- **Zhou et al. 2023b (Agents)** — the open-source agent framework + programming language this method is built on.
- **Hong et al. 2023 (MetaGPT)** — multi-agent SOP framework whose software-dev workflow the optimizer rediscovered.
- **Yao et al. 2023 (Tree-of-Thoughts)** — creative-writing task setup and a baseline this method outperforms.
- **Hinton 1990 (Connectionist learning procedures)** — the back-propagation/gradient-descent procedure the whole framework is analogized from.
- **Zhang et al. 2024a/b (AgentOptimizer / Agent-pro)** — prior prompt/tool optimizers operating on isolated agent components.
