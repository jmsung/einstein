<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, bio-protein-design, bio-drug-discovery]
title: "Swanson et al. — The Virtual Lab: AI Agents Design New SARS-CoV-2 Nanobodies"
year: 2025
source_url: https://www.nature.com/articles/s41586-025-09442-9
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

[[../home]] | [[../index]]

# Swanson et al. — The Virtual Lab: AI Agents Design New SARS-CoV-2 Nanobodies

**Authors:** Kyle Swanson, Wesley Wu, Nash Bunn, et al. (James Zou group, Stanford)
**Year:** 2025
**Venue:** Nature, Vol. 646, pp. 716–723

## Summary

The Virtual Lab is an AI-human research collaboration framework where an LLM Principal Investigator agent guides a team of LLM scientist agents (immunology, computational biology, machine learning, and a critic agent) through a series of research meetings. A human researcher provides high-level feedback.

Applied to nanobody design for SARS-CoV-2, the system created a novel computational pipeline incorporating ESM (protein language model), AlphaFold-Multimer, and Rosetta. It designed 92 new nanobodies, with two exhibiting improved binding to JN.1 or KP.3 variants while maintaining strong ancestral binding.

## Key Techniques

- Multi-agent LLM collaboration with role specialization
- PI agent + specialist agents + critic agent architecture
- Human-in-the-loop high-level feedback
- Computational biology pipeline integration (ESM, AlphaFold, Rosetta)

## Limitations

- Applied to biology, not mathematics — direct technique transfer is limited
- Heavy infrastructure requirements (protein folding models)
- Human-in-the-loop required for steering
