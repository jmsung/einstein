---
type: source
kind: paper
title: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering
authors: John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Adriano Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2405.15793
source_local: ../raw/2024-yang-swe-agent-agent-computer-interfaces-enable.pdf
topic: general-knowledge
cites:
---

# SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**Authors:** John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Adriano Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2405.15793

## One-line
Introduces the agent-computer interface (ACI) abstraction and shows that carefully designing the commands and feedback an LM agent uses — not the underlying model — produces large gains on real-world software engineering benchmarks.

## Key claim
With a fixed LM (GPT-4 Turbo), an LM-tailored ACI (compact edit/search/view commands, linter guardrails, summarized history) raises SWE-bench pass@1 from $3.8\%$ (prior RAG SOTA) to $12.47\%$, and HumanEvalFix Python pass@1 to $87.7\%$; ablation on SWE-bench Lite shows $+10.7$ percentage points over a Linux-shell-only agent ($18.0\%$ vs $7.3\%$ no-demo).

## Method
Build SWE-agent: a ReAct-style loop (thought + command, then environment feedback) layered over a Linux shell, but replacing raw shell primitives with a small, LM-friendly action set — `find_file`/`search_file`/`search_dir` (capped at 50 hits, suggests refinement on overflow), a 100-line windowed file viewer with `open`/`scroll_*`/`goto`, and a single multi-line `edit(start, end, replacement)` command integrated with the viewer. Context is managed by collapsing observations older than the last 5 into one line, dropping all but the first error message, and running a code linter that rejects edits introducing syntax errors and shows a snippet of the failure. Design driven by manual trajectory inspection plus grid search over window size, history processor, and decoding temperature.

## Result
SWE-agent + GPT-4 Turbo: $12.47\%$ ($286/2294$) on full SWE-bench, $18.0\%$ on Lite, $87.7\%/89.7\%/87.9\%$ pass@1 on HumanEvalFix Python/JS/Java. Portable: Claude 3 Opus reaches $10.46\%$ full / $13.0\%$ Lite. Ablations (Lite, $\Delta$ vs $18.0\%$): no edit tool $-7.7$, iterative search $-6.0$, full-history context $-3.0$, no linter $-3.0$, file-viewer window 30 lines $-3.7$ or full-file $-5.3$, no demonstration $-1.7$. Avg cost per resolved instance $\approx\$1.67$ (Lite, GPT-4T) vs $\$0.13$ for RAG — $\sim$8–13$\times$ cost for $\sim$6.7$\times$ resolve rate.

## Why it matters here
General background; no direct arena tie. The transferable lesson for the autonomous-loop agent on Einstein Arena is interface design: small, compact, well-documented action sets with informative-but-concise feedback and guardrails (linter-style rejection of bad edits, suppressed verbose tool output, collapsed history) outperform raw shell access — directly relevant to how the agent's wiki-ingest, council-dispatch, and optimizer-launch commands are exposed.

## Open questions / connections
- Can ACI design itself be automated (meta-optimization of agent tools) rather than crafted from manual trajectory inspection?
- Do the four principles (simple actions, compact actions, informative-concise feedback, guardrails) generalize to non-programming domains like math-optimizer dispatch or wiki navigation?
- Extends ReAct (Yao et al.) and InterCode (Yang et al. 2024) by adding interface-layer rather than prompting-layer interventions; complements SWE-bench (Jimenez et al. 2024) as the evaluation harness.

## Key terms
agent-computer interface, ACI, SWE-agent, SWE-bench, HumanEvalFix, LM agent, ReAct, tool use, file viewer, edit command, linter guardrail, context management, GPT-4 Turbo, Claude 3 Opus, pass@1, software engineering agent, interactive coding
