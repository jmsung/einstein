<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: "MetaGPT: Meta Programming for Multi-Agent Collaborative Framework"
authors: [Sirui Hong, Xiawu Zheng, Jonathan P. Chen, Yuheng Cheng, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Z. Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu]
year: 2023
source_url: https://arxiv.org/abs/2308.00352
drive_file_id: 19WIINevoTUt5ro2JjsJI5AjjXyC-WR-H
text_source: paperclip
ingested_by: agent
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

## Key terms
MetaGPT, multi-agent LLM framework, Standardized Operating Procedure, SOP, role specialization, structured communication, publish-subscribe message pool, executable feedback loop, HumanEval, MBPP, ChatDev, AutoGPT, recursive self-improvement, meta-programming
