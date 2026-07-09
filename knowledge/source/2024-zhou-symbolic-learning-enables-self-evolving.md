---
type: source
kind: paper
title: Symbolic Learning Enables Self-Evolving Agents
authors: Wangchunshu Zhou, Yixin Ou, Shengwei Ding, Long Li, Jialong Wu, Tiannan Wang, Jiamin Chen, Shuai Wang, Xiaohua Xu, Ningyu Zhang, Huajun Chen, Y. Jiang
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2406.18532
source_local: ../raw/2024-zhou-symbolic-learning-enables-self-evolving.pdf
topic: general-knowledge
cites:
---

# Symbolic Learning Enables Self-Evolving Agents

**Authors:** Wangchunshu Zhou, Yixin Ou, Shengwei Ding, Long Li, Jialong Wu, Tiannan Wang, Jiamin Chen, Shuai Wang, Xiaohua Xu, Ningyu Zhang, Huajun Chen, Y. Jiang  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2406.18532

## One-line
A framework that lets LLM-based agents update their own prompts, tools, and pipeline structure by mimicking neural-network backpropagation in natural language.

## Key claim
Jointly optimizing all symbolic components of a language agent (prompts, tools, pipeline topology) via language-based "loss," "gradients," and "optimizers" outperforms per-component prompt optimization (DSPy, AutoPE) and hand-built pipelines on MATH, HotpotQA, software-dev, and creative writing — e.g., 3.8 vs 2.4 (Agents) vs 1.6 (GPTs) on a 5-task software-dev average; 7.4 vs 6.8 (ToT) on GPT-4 creative writing.

## Method
Treats the agent as a symbolic network: pipeline = computation graph, node = layer, prompts/tools = weights. A forward pass logs a trajectory $\tau$ of $(I_n, O_n, P_n, T_n)$; a prompt-based **language loss** $L_{\text{lang}} = \text{LLM}(P_{\text{loss}}(\tau))$ (with or without ground truth) scores the run; **language gradients** $\nabla^n_{\text{lang}} = \text{LLM}(P_{\text{gradient}}(\nabla^{n+1}_{\text{lang}}, I_n, O_n, P_n, T_n, L_{\text{lang}}))$ are backpropagated node-by-node as textual critiques; three **symbolic optimizers** (PromptOptimizer, ToolOptimizer, PipelineOptimizer) edit prompts, add/delete/edit tools, and apply add/delete/move atomic ops to the pipeline graph. Illegal updates retry up to 3× then discard; a rollback re-runs the example and reverts regressions.

## Result
On MATH, HotpotQA, HumanEval the framework consistently improves over Agents baseline and DSPy/AutoPE (which sometimes degrade). On 5 software-dev tasks (Flappy bird, Tank, 2048, Snake, Brick breaker) averages 3.8/5 vs GPTs 1.6, Agents 2.4. On creative writing, 6.9 (GPT-3.5) / 7.4 (GPT-4), beating Tree-of-Thoughts (3.8/6.8). Recovers MetaGPT-like SOPs and plan→write→revise pipelines from a minimal init; over-engineered inits destabilize training. Unsupervised mode (no ground truth) enables post-deployment self-evolution.

## Why it matters here
Directly relevant to the einstein autonomous-loop architecture: the council-dispatch / self-improvement-loop / failure-is-a-finding pipeline is a hand-coded analog of this framework — the wiki is the "memory weights," findings are crystallized gradients. Suggests the loop could itself become a learnable object (gradient-style critique over the trajectory of a problem-solving cycle), and informs the [[self-improvement-loop]] and [[council-dispatch]] design vs prior wiki content which only treats agent learning informally.

## Open questions / connections
- Can language gradients backpropagate through a multi-cycle wiki — i.e., treat findings/concepts as long-lived "weights" updated by per-cycle losses (verification score, submission delta)?
- Extends DSPy (Khattab 2023) and GPTSwarm (Zhuge 2024) by adding pipeline-topology edits; complementary to fine-tuning approaches (FireAct, AutoAct) that update the LLM backbone instead.
- Open: rollback strategy is greedy per-example; no analog of momentum, learning rate, or batched updates — does language-gradient SGD have stability theory?
- Open: unsupervised loss is itself an LLM — risk of reward hacking / loss drift over many cycles, especially without a triple-verify analog on the loss signal.

## Key terms
agent symbolic learning, language gradient, language loss, backpropagation in natural language, prompt optimization, tool optimization, pipeline optimization, self-evolving agents, DSPy, GPTSwarm, AgentOptimizer, computation graph, MetaGPT, Tree of Thoughts, data-centric agent learning, symbolic optimizer
