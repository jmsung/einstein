---
type: source
kind: paper
title: "MetaGPT: Meta Programming for Multi-Agent Collaborative Framework"
authors: Sirui Hong, Xiawu Zheng, Jonathan P. Chen, Yuheng Cheng, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Z. Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2308.00352
source_local: ../raw/2023-hong-metagpt-meta-programming-multi-agent.pdf
topic: general-knowledge
cites:
---

# MetaGPT: Meta Programming for Multi-Agent Collaborative Framework

**Authors:** Sirui Hong, Xiawu Zheng, Jonathan P. Chen, Yuheng Cheng, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Z. Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2308.00352

## One-line
MetaGPT encodes human Standardized Operating Procedures (SOPs) into an LLM multi-agent framework with role specialization, structured-document communication, and executable feedback, applied to autonomous software engineering.

## Key claim
Embedding SOPs + structured outputs + an executable-feedback loop into an LLM-multi-agent "software company" yields SoTA on code-generation benchmarks: $85.9\%$ Pass@1 on HumanEval and $87.7\%$ on MBPP, with $100\%$ task completion on a 70-task SoftwareDev set and executability $3.75/4$ vs ChatDev's $2.25$.

## Method
Five specialized agents (Product Manager, Architect, Project Manager, Engineer, QA Engineer) follow a fixed SOP pipeline, each emitting *structured artifacts* (PRDs, class/interface specs, task lists, code, unit tests) rather than free-form dialogue. Communication uses a shared *message pool* + *publish-subscribe* filter on role profiles to avoid information overload. The Engineer runs an *executable-feedback* loop — generate code, run unit tests, debug from execution traces, up to 3 retries — which the ablation shows contributes $+4.2\%$ / $+5.4\%$ Pass@1 on HumanEval / MBPP.

## Result
Beyond benchmark Pass@1 numbers, on SoftwareDev MetaGPT used $124.3$ tokens/line vs ChatDev's $248.9$, cut human-revision count from $2.25 \to 0.83$ with the feedback loop, and averaged executability $3.9$ vs $1.0$ for AutoGPT/LangChain/AgentVerse and $2.1$ for ChatDev. Role-ablation shows monotone gains in executability ($1.0 \to 4.0$) and reduction in revisions ($10 \to 2.5$) as Product Manager, Architect, and Project Manager roles are added on top of a sole Engineer. Appendix A also sketches a self-referential extension where agents rewrite their own *role constraint prompts* from prior-project feedback (recursive self-improvement à la Schmidhuber 1987).

## Why it matters here
General background; no direct arena tie. Relevant only as design reference for the einstein agent's own infrastructure — the *council dispatch* pattern (specialized personas writing structured outputs), structured message handoffs, and the executable-feedback / self-correction loop echo what `.claude/rules/council-dispatch.md` and `self-improvement-loop.md` already prescribe; the SOP-driven structured-output discipline is the same intuition behind mandatory wiki frontmatter + cycle-log discipline.

## Open questions / connections
- Does SOP-style structured handoff between mathematician personas (PRD-analog → architecture-analog → execution) outperform the current free-form "each persona writes 2–3 questions" council dispatch? Worth testing on one arena problem.
- The recursive constraint-prompt rewriting in Appendix A is a concrete implementation of "agent rewrites its own rules from cycle feedback" — could inspire a `/agent-reflect` step that proposes edits to `docs/wiki/personas/*.md` from cycle-log outcomes.
- Extends NLSOM (Zhuge 2023) and ChatDev (Qian 2023); leaves open whether SOPs help for *research / proof* tasks (vs the well-scoped software-dev SOP that already exists in industry).

## Key terms
MetaGPT, multi-agent LLM framework, Standardized Operating Procedure, SOP, role specialization, structured communication, publish-subscribe message pool, executable feedback loop, HumanEval, MBPP, ChatDev, AutoGPT, recursive self-improvement, meta-programming, agent council
