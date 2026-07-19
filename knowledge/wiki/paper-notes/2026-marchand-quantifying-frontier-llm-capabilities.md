---
type: note
kind: paper-relevance
about: 2026-marchand-quantifying-frontier-llm-capabilities
canonical: ../../domains/ai-agents/source/2026-marchand-quantifying-frontier-llm-capabilities.md
---

# Relevance note — Quantifying Frontier LLM Capabilities for Container Sandbox Escape

Canonical distillation: [`2026-marchand-quantifying-frontier-llm-capabilities.md`](../../domains/ai-agents/source/2026-marchand-quantifying-frontier-llm-capabilities.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — this is a security/AI-control benchmark, not a math optimization paper, so it does not feed sphere-packing, autocorrelation, or any of the 23 Einstein Arena problems. Only tangential relevance is methodological: nested-sandbox evaluation design and inference-time-compute scaling curves as exemplars of careful agentic-benchmark construction.

## Open questions / connections
- Why does GPT-5.2 regress vs GPT-5 on agentic skills, and why do hints help Opus but not GPT-5 — what trained behaviors mediate vulnerability-knowledge-to-exploit translation?
- Parallel-vs-sequential inference-compute allocation: threshold-effect scenarios (e.g. dac_read_search) favor longer single attempts; stochastic-search scenarios (e.g. pid_namespace) favor more retries.
- Extends container-security surveys (Jarkas et al. 2025; Lin et al. 2018) and CTF benchmarks (NYU CTF Bench, CyBench, CVE-Bench, CyberGym) into the previously unmeasured container-escape axis; leaves open whether models will discover novel (zero-day) container vulnerabilities at future capability levels.
