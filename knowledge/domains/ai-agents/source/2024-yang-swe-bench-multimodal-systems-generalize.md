<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?"
authors: [John Yang, Carlos E. Jimenez, Alex L. Zhang, Kilian Adriano Lieret, Joyce Yang, Xindi Wu, O. Press, Niklas Muennighoff, Gabriel Synnaeve, Karthik R. Narasimhan, Diyi Yang, Sida Wang, Ofir Press]
year: 2024
source_url: https://arxiv.org/abs/2410.03859
drive_file_id: 1u-KR-azUjMwyy-3VxW4LZOaFE6-DLkwj
text_source: paperclip
ingested_by: agent
---

# SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?

**Authors:** John Yang, Carlos E. Jimenez, Alex L. Zhang, Kilian Adriano Lieret, Joyce Yang, Xindi Wu, O. Press, Niklas Muennighoff, Gabriel Synnaeve, Karthik R. Narasimhan, Diyi Yang, Sida Wang, Ofir Press  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2410.03859

## One-line
Introduces SWE-bench M, a 617-instance benchmark of visual JavaScript bug-fixing tasks from 17 GitHub repos, showing top SWE-bench systems fail to generalize across language (Python→JS) and modality (text→image).

## Key claim
Existing top SWE-bench solvers drop sharply on SWE-bench M because they rely on Python-specific AST tooling and lack visual reasoning; SWE-agent (language-agnostic, multimodal) resolves 12% vs ≤6% for Agentless JS / RAG. 83.5% of image-bearing tasks require the image to be solvable.

## Method
Curated GitHub PRs from 17 user-facing JS libraries (mapping, plotting, diagramming, syntax highlighting, UI design) with ≥5k stars and ≥500 PRs, filtered to instances whose issue text or test patch contains image/video links, then validated via 10×-repeat test-stability checks and human annotation. Adapted four open-source SWE-bench agents (SWE-agent Base/JS/M, Agentless JS, RAG; AutoCodeRover and Moatless rejected as too Python-coupled) and evaluated on GPT-4o and Claude 3.5 Sonnet. Image necessity, OCR-representability, and category distribution measured by human annotators on all 862 problem-statement images.

## Result
Best system SWE-agent M with GPT-4o resolves 12.2% (avg \$2.94/task); SWE-agent Base with Claude 3.5 Sonnet 12.2% (\$1.52); Agentless JS only 3.1–6.2%; RAG 5.0–6.0%. Removing images degrades performance, and tasks where annotators labeled images "necessary" show larger image-on/off gaps. Task difficulty distribution: 13% <15min, 43% 15min–1h, 38% 1–4h, 6% >4h — substantially harder than SWE-bench Verified. Post-cutoff (after GPT-4o training cutoff Oct 2023) performance exceeds pre-cutoff even after reweighting, indicating no leakage advantage.

## Key terms
SWE-bench, SWE-bench Multimodal, SWE-agent, Agentless, AutoCodeRover, Moatless, agent-computer interface, multimodal code agents, JavaScript benchmark, GitHub-issue benchmark, fail-to-pass tests, visual software engineering, GPT-4o, Claude 3.5 Sonnet, language-agnostic agent
