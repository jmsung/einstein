<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-retrieval, sci-physics]
title: Accelerating earth science discovery via multi-agent LLM systems
authors: [Dmitrii Pantiukhin, Boris Shapkin, Ivan Kuznetsov, A. Jost, Nikolay Koldunov]
year: 2025
source_url: https://arxiv.org/abs/2503.05854
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Accelerating earth science discovery via multi-agent LLM systems

**Authors:** Dmitrii Pantiukhin, Boris Shapkin, Ivan Kuznetsov, A. Jost, Nikolay Koldunov  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2503.05854

## One-line
A Perspective proposing multi-agent LLM systems (MAS) for geoscience data discovery, illustrated by "PANGAEA GPT" — a centralized supervisor-plus-sub-agents pipeline over the PANGAEA Earth-science repository.

## Key claim
Centralized MAS architectures with a supervisor agent dispatching domain-specialized sub-agents (oceanography, geology, climatology), each equipped with tool sandboxes, RAG memory, and validator/reflection modules, can manage heterogeneous geoscientific data better than single-agent or fine-tuned-LLM approaches; no quantitative bound is established — it is a position/architecture paper.

## Method
Centralized orchestration: a supervisor LLM agent decomposes user queries, spawns subdomain sub-agents on demand, each with localized memory, tool sandboxes (GDAL, NetCDF, xarray, Python/R), and RAG over curated metadata. A two-tier memory (short-term context + vector-DB long-term store) plus validator agents that cross-check outputs against domain vocabularies (e.g. SeaDataNet) and visualization conventions (reversed depth axes, unit scales) act as quality gates.

## Result
Demonstrated as the open-source PANGAEA GPT prototype (github.com/dmpantiu/pangaeaGPT) integrated with PANGAEA's 400,000+ datasets. Reports >93% of PANGAEA datasets are uncited as motivation. Identifies the gap that no MAS framework was previously tightly integrated with a geoscience database, and that Earth-science lacks "imaging" and statistical benchmarks analogous to SWE-bench — addressed via domain-specific validator-agent checklists rather than universal benchmarks.

## Key terms
multi-agent systems, MAS, LLM agents, supervisor agent, retrieval-augmented generation, RAG, PANGAEA, geoscience data, validator agent, reflection loop, vector database memory, tool integration, sub-agent orchestration, chain-of-thought, hierarchical agents, swarm intelligence
