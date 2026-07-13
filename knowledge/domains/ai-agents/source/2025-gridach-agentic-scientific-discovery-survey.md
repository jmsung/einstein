<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning, bio-drug-discovery]
title: "Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions"
authors: [Mourad Gridach, Jay Nanavati, Khaldoun Zine El Abidine, Lenon Mendes, C. Mack]
year: 2025
source_url: https://arxiv.org/abs/2503.08979
drive_file_id: 1bt9ntuBs-DE20ipmA-FLtawiUnyniVDa
text_source: paperclip
ingested_by: agent
---

# Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions

**Authors:** Mourad Gridach, Jay Nanavati, Khaldoun Zine El Abidine, Lenon Mendes, C. Mack  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2503.08979

## One-line
Survey of LLM-driven autonomous and human-collaborative agent systems automating scientific research workflows (literature review, hypothesis generation, experimentation, paper writing) across chemistry, biology, and materials science.

## Key claim
Agentic AI can automate substantial parts of the scientific research lifecycle, but literature review remains the highest-failure-rate phase across systems (e.g., Agent Laboratory, ResearchAgent, AI Scientist) — and trustworthiness, calibration, and human-AI collaboration are the binding constraints, not raw capability.

## Method
Narrative survey + taxonomy. Categorizes systems along two axes: (a) **single-agent vs multi-agent** (Minsky's Society-of-Mind framing), and (b) **fully autonomous vs human-AI collaborative**. Tabulates implementation frameworks (AutoGen, MetaGPT, Letta/MemGPT, CAMEL, LangChain, AutoGPT), datasets (LAB-Bench, MoleculeNet, ZINC, MatText, ChEMBL, AlphaFold DB, ICLR OpenReview), and evaluation metrics (accuracy, task-completion rate, NeurIPS-style quality/significance/clarity/soundness scores).

## Result
Catalogs domain agents — chemistry: Coscientist (GPT-4 plans/executes Pd cross-coupling), ChemCrow (18 expert tools), LLaMP (RAG over Materials Project), Organa (~20% time reduction on electrochemistry tasks), LLM-RDF, ChatMOF, MOOSE-CHEM; biology: BIA (scRNA-seq workflows), CellAgent (Planner/Executor/Evaluator, 92% task completion), TAIS, ProtAgents, CRISPR-GPT; general: AI Scientist (Lu 2024), Agent Laboratory, Virtual Lab (SARS-CoV-2 nanobodies), ResearchAgent, BioPlanner. Identifies five open challenges: trustworthiness/benchmarking, ethics/bias, blast-radius/safety, generalizability across domains, and calibration of model confidence.

## Key terms
agentic AI, LLM agents, multi-agent systems, scientific discovery, literature review automation, hypothesis generation, AutoGen, MetaGPT, MemGPT, Coscientist, ChemCrow, Agent Laboratory, AI Scientist, ResearchAgent, calibration, trustworthiness, human-in-the-loop, Society of Mind, RAG, Minsky
