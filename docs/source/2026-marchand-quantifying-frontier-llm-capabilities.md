---
type: source
kind: paper
title: Quantifying Frontier LLM Capabilities for Container Sandbox Escape
authors: Rahul Marchand, Art Ó Catháin, Jerome Wynne, P. Giavridis, Sam Deverett, John Wilkinson, J. Gwartz, H. Coppock
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2603.02277
source_local: ../raw/2026-marchand-quantifying-frontier-llm-capabilities.pdf
topic: general-knowledge
cites:
---

# Quantifying Frontier LLM Capabilities for Container Sandbox Escape

**Authors:** Rahul Marchand, Art Ó Catháin, Jerome Wynne, P. Giavridis, Sam Deverett, John Wilkinson, J. Gwartz, H. Coppock  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2603.02277

## One-line
Introduces SandboxEscapeBench, an 18-scenario CTF benchmark measuring whether frontier LLMs can break out of Docker/Kubernetes container sandboxes via misconfigurations, runtime bugs, and kernel exploits.

## Key claim
Frontier LLMs (GPT-5, Claude Opus 4.5) reliably escape easy/common container misconfigurations (success ≈1.00 on difficulty-1 scenarios) and achieve nontrivial success on harder runtime/kernel CVEs (≈0.40 on difficulty-3), while observing zero success on difficulty 4–5 and a roughly log-linear scaling of success rate with inference-time compute budget.

## Method
Nested "sandbox-in-a-sandbox" architecture: Inspect AI orchestrates a VM (Vagrant or EC2) containing a vulnerable Docker/K8s container; the agent is given root shell + bash + network, with success defined as exact-string match of a flag at `/flag.txt` on the host VM. 18 scenarios span Jarkas et al.'s container-security taxonomy — Orchestration (L1, 4), Runtime (L3, 8), Kernel (L4, 6) — each grounded in a real CVE or misconfiguration class with a reference exploit script. Evaluation runs 9 models × 18 tasks × 5 epochs (760/810 samples completed), token-capped at 2.5M, with ablations for vulnerability hints and inference-compute scaling.

## Result
Overall: Opus 4.5 0.49 [0.39, 0.59] vs Haiku 0.18 [0.11, 0.27]; GPT-OSS-120B 0.16; GPT-5 0.50 vs GPT-5.2 0.27 (version regression). On difficulty-1 misconfigs (privileged, docker.sock, hostpath), top models hit 1.00; on difficulty-3 (dirty pipe, runc CVEs, sys_module, DAC_READ_SEARCH/Shocker), Opus and GPT-5 reach 0.40–0.42; no model solved difficulty 4–5. Hints roughly double Opus's hard-scenario success but barely help GPT-5; models also discovered four unintended shortcuts (Vagrant default SSH creds, known insecure SSH key, modprobe_path via eBPF, Dirty COW bypass of BPF privesc).

## Why it matters here
General background; no direct arena tie — this is a security/AI-control benchmark, not a math optimization paper, so it does not feed sphere-packing, autocorrelation, or any of the 23 Einstein Arena problems. Only tangential relevance is methodological: nested-sandbox evaluation design and inference-time-compute scaling curves as exemplars of careful agentic-benchmark construction.

## Open questions / connections
- Why does GPT-5.2 regress vs GPT-5 on agentic skills, and why do hints help Opus but not GPT-5 — what trained behaviors mediate vulnerability-knowledge-to-exploit translation?
- Parallel-vs-sequential inference-compute allocation: threshold-effect scenarios (e.g. dac_read_search) favor longer single attempts; stochastic-search scenarios (e.g. pid_namespace) favor more retries.
- Extends container-security surveys (Jarkas et al. 2025; Lin et al. 2018) and CTF benchmarks (NYU CTF Bench, CyBench, CVE-Bench, CyberGym) into the previously unmeasured container-escape axis; leaves open whether models will discover novel (zero-day) container vulnerabilities at future capability levels.

## Key terms
container escape, sandbox, Docker, Kubernetes, CTF benchmark, Inspect AI, LLM agents, AI control, capture the flag, runc CVE, Dirty COW, Dirty Pipe, eBPF privilege escalation, inference-time compute scaling
