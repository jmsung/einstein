<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: "Optimizing LLM-Based Multi-Agent System with Textual Feedback: A Case Study on Software Development"
authors: [Ming Shen, Raphael Shu, Anurag Pratik, James Gung, Yubin Ge, Monica Sunkara, Yi Zhang]
year: 2025
source_url: https://arxiv.org/abs/2505.16086
drive_file_id: 1XiY1hheZgs1m2zBdIsFf3ahHuFTj1nfG
text_source: paperclip
ingested_by: agent
---

# Optimizing LLM-Based Multi-Agent System with Textual Feedback: A Case Study on Software Development

**Authors:** Ming Shen, Raphael Shu, Anurag Pratik, James Gung, Yubin Ge, Monica Sunkara, Yi Zhang  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2505.16086

## One-line
A two-step locate-then-optimize pipeline that uses LLM-generated textual feedback to improve system prompts of role-based multi-agent systems, evaluated on software development tasks.

## Key claim
Group optimization with textual feedback outperforms unoptimized, one-shot, and direct-optimization (TextGrad-style) baselines across all five evaluation dimensions (functionality, robustness, test coverage, documentation, PEP-8 violations); online+group+one-pass setting reaches functionality 7.26 (vs 6.90 unoptimized) and reduces violations from 6.62 to 3.24.

## Method
Model the multi-agent system as a directed graph $G=\{N,E\}$ where each node $n$ runs $O_n = \text{LLM}(I_n \oplus P_n)$. A critic $f(Y_i, X_i) \to (U_i, I_i)$ generates a scalar score and textual feedback per evaluation dimension. Step 1 (Locator): an LLM identifies underperforming agents $N_f \subseteq N$ and produces per-agent failure explanations $E$ from $(X, I, G)$. Step 2 (Optimizer): an LLM rewrites the system prompt $P_n$ of each identified agent using $E_n$ and its I/O trace. Compared settings: online vs offline feedback collection, individual vs group updates, and one-pass vs multi-pass prompting for the group case.

## Result
On SRDD (1200 software tasks, 60/20/20 split, GPT-4-0613, 5 optimization steps), group beats individual and online beats offline. Online group one-pass: functionality 7.26, robustness 7.74, coverage 7.81, documentation 20.33, violations 3.24 — best or near-best across all five dimensions. One-pass ≈ multi-pass in quality but cheaper. More than 5 steps shows flat or declining curves on train/dev.

## Key terms
multi-agent system, prompt optimization, textual feedback, credit assignment, locator, reflective optimization, TextGrad, DSPy, GPTSwarm, role-based agents, LLM-as-judge, software development, SRDD, ChatDev
