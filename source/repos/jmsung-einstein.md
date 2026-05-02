---
type: source
provenance: repos
author: agent
drafted: 2026-05-02
level: 4
source_type: code_repository
source_url: https://github.com/jmsung/einstein
cites:
  - ../blog/2026-togetherai-einstein-arena.md
  - ../papers/2025-novikov-alphaevolve.md
  - ../personas/_synthesis.md
  - findings/verification-patterns.md
  - findings/gpu-modal-compute.md
  - strategy.md
---

[[../home]] | [[../index]]

# Sung — JSAgent: An AI Agent for Hard Mathematical Optimization

**Author:** Jongmin Sung
**Year:** 2026
**Language:** Python (3.13+)
**License:** MIT
**Created:** 2026-03-30

## Summary

JSAgent is the public-facing codebase for the einstein project — an AI agent that solves hard mathematical optimization problems on Einstein Arena. The repository shares the full methodology openly: techniques, findings, per-problem deep dives, and a discovery timeline for attribution clarity.

JSAgent was cited in the Together AI blog post by Bianchi, Kwon, and Zou as a top-performing agent. The repository serves dual purpose: active competition solver and open knowledge contribution to the community.

As of 2026-04-21, JSAgent holds **#1 on 4 problems** (P2 First Autocorrelation, P7 Prime Number Theorem, P14 Circle Packing, P18 Circles in Rectangle) and **top-3 on 12 problems** across the 21-problem arena.

## Key Architecture

### Mathematician Council
A multi-agent research system with 10 core personas (Gauss, Riemann, Tao, Conway, Euler, Poincare, Erdos, Noether, Cohn, Razborov) plus 6 conditional specialists (Viazovska, Szemeredi, Turan, Ramanujan, Archimedes, Hilbert). Each researches independently; a synthesis step ranks ideas by impact.

### Adaptive Optimizer
Problem-agnostic optimization loop: load best solution → select strategies (knowledge-weighted) → run candidates → verify → update weights → loop. Ships with general strategies (hill climbing, Nelder-Mead, L-BFGS-B, perturbation) plus problem-specific plugins (Riemannian GD, Dinkelbach, memetic tabu).

### Knowledge Layer
Structured knowledge base tracking which strategies work for which problem categories. Cross-problem transfer means new problems benefit from solved-problem priors.

### Triple Verification
Every score verified three ways: fast evaluator, exact reimplementation, cross-check with different method. Disagreement → rejection.

### GPU Strategy
Bottleneck classification before scaling: math-limited → research, sequential-compute → CPU, parallel-compute → PyTorch on A100/H100 if ≥3x speedup, low GPU util → custom Triton kernels.

## Public Documentation

- `docs/timeline.md` — Discovery timeline with dated breakthroughs
- `docs/methodology.md` — Optimizer taxonomy, general techniques
- `docs/findings/` — Arena mechanics, float64 polish, verification, optimization recipes
- `docs/arena.md` — Platform overview and API reference
- Per-problem deep dives in `docs/` (one file per problem)

## Citation

```bibtex
@misc{jsagent2026,
  author       = {Sung, Jongmin},
  title        = {JSAgent: An AI Agent for Hard Mathematical Optimization},
  year         = {2026},
  publisher    = {GitHub},
  url          = {https://github.com/jmsung/einstein}
}
```

## Relevance to Einstein Project

This IS the einstein project's public repository. The reference page serves as:
1. A snapshot of the public methodology description and current standings
2. The canonical citation for external references
3. A record of the open knowledge mission and repository structure

## Limitations

- Arena status table is auto-updated by cron — snapshot here may be stale
- README describes the architecture at a high level; internal implementation details live in per-problem strategy docs and findings

*Last updated: 2026-04-21*
