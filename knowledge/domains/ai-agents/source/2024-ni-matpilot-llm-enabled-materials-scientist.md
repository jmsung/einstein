<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, sci-chem, ai-retrieval]
title: "MatPilot: an LLM-enabled AI Materials Scientist under the Framework of Human-Machine Collaboration"
authors: [Ziqi Ni, Yahao Li, Kaijia Hu, K. Han, Ming Xu, Xingyu Chen, Fengqi Liu, Y. Ye, Shuxin Bai]
year: 2024
source_url: https://arxiv.org/abs/2411.08063
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# MatPilot: an LLM-enabled AI Materials Scientist under the Framework of Human-Machine Collaboration

**Authors:** Ziqi Ni, Yahao Li, Kaijia Hu, K. Han, Ming Xu, Xingyu Chen, Fengqi Liu, Y. Ye, Shuxin Bai  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2411.08063

## One-line
Describes MatPilot, an LLM-driven multi-agent system that pairs a cognition module (RAG knowledge base + divergent/convergent agent debate) with an automated wet-lab execution module to iteratively design and run materials-discovery experiments (energy-storage ceramics as the running example).

## Key claim
A human-in-the-loop framework combining retrieval-augmented LLMs, multi-agent debate (exploration / evaluation / integration agents), and an automated solid-state sintering pipeline can drive iterative materials discovery; no quantitative materials-science benchmark is reported.

## Method
Cognition module uses RAG over a curated knowledge base built by literature screening → structured data extraction → knowledge distillation → knowledge-graph construction, plus a multi-agent debate framework (explorer/evaluator/integrator) implementing divergent–convergent "structural intelligence." Execution module integrates automated workstations for dispensing, ball milling, sintering, molding, DMS, DHM, with planned embodied-intelligence robotics (ALOHA-style imitation learning, ReKep keypoint constraints) for sieving/pouring/scraping. The overall loop is framed as evolutionary optimization over experimental parameters.

## Result
A working system architecture (MatPilot) with demonstrated automation of the solid-state ceramic-sintering workflow and an LLM-based hypothesis/protocol generator; the paper presents the framework and qualitative workflow rather than a benchmarked discovery, novel material, or measured speedup.

## Key terms
LLM agents, retrieval-augmented generation, multi-agent debate, human-machine collaboration, knowledge graph, materials discovery, autonomous laboratory, solid-state sintering, embodied intelligence, ALOHA, ReKep, evolutionary optimization
