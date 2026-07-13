<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-retrieval, sci-chem]
title: "SciAgents: Automating scientific discovery through multi-agent intelligent graph reasoning"
authors: [Alireza Ghafarollahi, Markus J. Buehler]
year: 2024
source_url: https://arxiv.org/abs/2409.05556
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# SciAgents: Automating scientific discovery through multi-agent intelligent graph reasoning

**Authors:** Alireza Ghafarollahi, Markus J. Buehler  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2409.05556

## One-line
A multi-agent LLM framework that traverses an ontological knowledge graph to autonomously generate, expand, and critique scientific hypotheses in bio-inspired materials.

## Key claim
Combining (1) a large ontological knowledge graph built from ~1,000 papers, (2) random-path subgraph sampling between concept nodes, and (3) a team of role-specialized LLM agents (Ontologist, Scientist_1, Scientist_2, Critic, Planner, novelty-check assistant) produces more novel and detailed hypotheses than single-LLM or shortest-path baselines.

## Method
Two architectures are compared: (a) a pre-programmed pipeline with fixed agent sequence, and (b) a fully automated self-organizing multi-agent system with human-in-the-loop and a Semantic Scholar novelty-check tool. Hypothesis generation begins with two seed concepts, samples a **random path** (not shortest path) through the knowledge graph to surface richer intermediate concepts, then a hierarchical expansion produces a JSON-structured proposal with seven fields (hypothesis, outcome, mechanisms, design principles, unexpected properties, comparison, novelty), each expanded and critiqued by dedicated agents.

## Result
Demonstrated on a "silk → energy-intensive" seed pair: produced an 8,100-word hypothesis proposing silk + dandelion-pigment biomaterials with predicted tensile strength ~1.5 GPa (vs 0.5–1.0 GPa baseline) and ~30% energy reduction. A second case (graphene + amyloid fibrils) yielded predicted conductivities $10^5$–$10^6$ S/m and self-rated novelty 8/10, feasibility 7/10. No formal benchmarks; evaluation is qualitative + agent self-rating.

## Key terms
multi-agent LLM, knowledge graph, ontological reasoning, random path sampling, hypothesis generation, agent council, critic agent, in-context learning, retrieval-augmented generation, bio-inspired materials, graph traversal, autonomous scientific discovery
