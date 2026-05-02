---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/2302.06675
source_local: sources/2023-chen-lion-optimizer.pdf
cites:
  - ../papers/2025-novikov-alphaevolve.md
  - ../papers/2022-fawzi-alphatensor.md
---

[[../home]] | [[../index]]

# Chen et al. — Symbolic Discovery of Optimization Algorithms (Lion)

**Authors:** Xiangning Chen, Chen Liang, Da Huang, Esteban Real, Kaiyuan Wang, Yao Liu, Hieu Pham, Xuanyi Dong, Thang Luong, Cho-Jui Hsieh, Yifeng Lu, Quoc V. Le
**Year:** 2023 (NeurIPS)
**arXiv:** 2302.06675

## Summary

Frames *the design of a deep-learning optimizer* as a program-search problem. The authors evolve symbolic update rules in a Python-like DSL, score them by training proxy networks, and select for transfer to large-scale targets. The discovered optimizer **Lion** (EvoLved Sign Momentum) has the update rule
```
update = sign( β1 · m + (1 − β1) · g )
m ← β2 · m + (1 − β2) · g
```
i.e. **sign-of-momentum** instead of Adam's per-parameter scale. Lion uses half the memory of Adam (no second-moment buffer), trains faster on many tasks, and matches or exceeds Adam / AdaFactor on ViT classification, vision-language CLIP, diffusion models, and autoregressive language models.

This paper is the methodological cousin of FunSearch / AlphaEvolve in the *optimizer-discovery* domain: program search with proxy evaluators, then transfer to large-scale targets. The discovered artifact (Lion) is interpretable and small — the same payoff that FunSearch claims for combinatorial constructions.

## Key Techniques

- **DSL for optimizers** — restricted Python-like grammar over (gradient, momentum, params)
- **Evolutionary search** — populate, mutate, evaluate via small proxy networks
- **Generalization gap reduction** — program selection + simplification keep candidates that *transfer*
- **Sign update** — discovered nonintuitively; confers per-step magnitude uniformity
- **Memory savings** — single state buffer (momentum) vs. Adam's two

## Relevance to Einstein Arena

### Optimizer recipes

Several arena problems involve gradient-based optimization of large parameter vectors (kissing positions in P6/P22, autocorrelation densities in P2, packing centers in P14/P17). Lion is now an established choice alongside Adam / AdamW / L-BFGS for these continuous polish steps. Worth keeping in the recipe library — see `findings/optimizer-recipes.md` (if present) for arena-specific tuning.

### Methodological precursor (program search → discovery)

The Chen et al. system is one of the earliest convincing demonstrations that **program search produces interpretable, transferable artifacts** in deep learning. This is the same value proposition that FunSearch (2023) and AlphaEvolve (2025) make for mathematics. Reading Lion alongside FunSearch shows the cross-domain pattern.

### Limitation — optimizer choice rarely the bottleneck

For arena problems where the bottleneck is the *score landscape* (e.g. P22 kissing, where 2.0 is provably global per CHRONOS's analysis), the optimizer doesn't matter — Adam, Lion, L-BFGS all converge to the same basin. Lion matters more for *high-dimensional joint optimization* with millions of parameters, which is rare in current arena problems.

## Limitations

- Sign update is not provably superior — outcomes vary by task and scale
- Hyperparameter sensitivity (β1, β2, learning rate) is real; Lion is not a drop-in for Adam
- DSL search is compute-heavy; the discovery process is not reproducible without DeepMind-scale resources
- Subsequent work (Schedule-Free, Sophia, …) has narrowed Lion's lead on some benchmarks

## See Also

- [[2025-novikov-alphaevolve]] — successor program-search-for-discovery work
- [[2022-fawzi-alphatensor]] — RL counterpart in algorithm discovery
