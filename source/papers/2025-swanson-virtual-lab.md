---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://www.nature.com/articles/s41586-025-09442-9
cites:
  - ../papers/2025-novikov-alphaevolve.md
  - ../papers/2025-georgiev-math-exploration.md
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

## Relevance to Einstein Arena

Relevant as a **methodological parallel** — the Virtual Lab's multi-agent architecture with specialized roles mirrors our mathematician council approach. The PI + specialists + critic pattern validates the value of role-based agent collaboration for scientific discovery.

The James Zou connection (Stanford / Together AI) links this work to the Einstein Arena organizers.

## Limitations

- Applied to biology, not mathematics — direct technique transfer is limited
- Heavy infrastructure requirements (protein folding models)
- Human-in-the-loop required for steering
