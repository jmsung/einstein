---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/2503.11061
source_local: sources/2025-ellenberg-generative-math.pdf
cites:
  - ../papers/2023-romera-paredes-funsearch.md
  - ../papers/2025-novikov-alphaevolve.md
  - ../papers/2025-georgiev-math-exploration.md
---

[[../home]] | [[../index]]

# Ellenberg, Fraser-Taliente, Harvey, Srivastava & Sutherland — Generative Modeling for Mathematical Discovery

**Authors:** Jordan S. Ellenberg, Cristofero S. Fraser-Taliente, Thomas R. Harvey, Karan Srivastava, Andrew V. Sutherland
**Year:** 2025 (Adv. Theor. Math. Phys.)
**arXiv:** 2503.11061

## Summary

A **practitioner-oriented reimplementation of FunSearch** designed for working mathematicians: requires no machine-learning expertise, no high-performance computing access, and uses third-party LLM APIs (OpenAI, Anthropic, Google) instead of an in-house model. Adapting it to a new problem requires modifying a small Python segment plus selecting an LLM.

The authors benchmark their implementation on three different problems (combinatorial and number-theoretic) and report metrics that practitioners can use to plan applications:
- Iteration counts to convergence
- LLM-call cost vs. problem difficulty
- Quality of discovered programs vs. baseline (Strassen-style hand-written heuristics)

Headline qualitative finding: **funsearch successfully learns in a variety of combinatorial and number-theoretic settings, and in some contexts learns principles that generalize beyond the problem originally trained on** — i.e., the discovered Python heuristics are transferable across related problems.

The paper is the natural reference if you want to *run* FunSearch yourself on an arena problem rather than reading about the original DeepMind system.

## Key Techniques

- **Plug-in LLM backend** — abstract over OpenAI / Anthropic / Google APIs; swap models per cost-quality budget
- **Single-file evolve block** — minimal Python harness, drop-in for new problems
- **Asynchronous distributed sampling** — parallelize across many LLM calls without expensive infrastructure
- **Benchmark suite** — three reference problems with metrics (iterations, cost, success rate)
- **Cross-problem transfer** — same harness applied unchanged to multiple problems

## Relevance to Einstein Arena

### Direct practitioner reference

This is the closest thing to a "how to run FunSearch on an arena problem" guide. If we want to deploy a FunSearch-style agent against any of P1, P2, P6, P14–P19, P22, this paper is the implementation blueprint. JSAgent's evolutionary loop architecture overlaps significantly.

### Methodology comparison

Where AlphaEvolve is a closed DeepMind system and the original FunSearch paper describes pre-Codey/Gemini infrastructure, this paper validates the *core idea* using commodity LLMs available to anyone. This matters because the arena assumes contestants have access to *standard* LLM APIs, not bespoke DeepMind models.

### Open-source spirit
The paper aligns with the JSAgent / open-knowledge mission of the broader Einstein Arena project — making mathematical discovery via LLMs reproducible without privileged compute.

## Limitations

- Performance lags AlphaEvolve on direct comparisons (when DeepMind's data is available)
- Third-party LLMs vary widely in usefulness; results depend on model choice
- Three benchmarks is a thin evaluation; arena-specific transfer is not validated
- Closed evaluation loop only — no hooks for human-in-the-loop refinement

## See Also

- [[2023-romera-paredes-funsearch]] — original FunSearch paper
- [[2025-novikov-alphaevolve]] — successor system at DeepMind
- [[2025-georgiev-math-exploration]] — adjacent benchmark for mathematical exploration
