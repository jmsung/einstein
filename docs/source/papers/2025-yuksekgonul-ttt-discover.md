---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://test-time-training.github.io/discover/
cites:
  - problem-1-erdos-overlap/strategy.md
  - ../papers/2025-georgiev-math-exploration.md
  - ../papers/2025-novikov-alphaevolve.md
---

[[../home]] | [[../index]]

# Yuksekgonul et al. — Learning to Discover at Test Time (TTT-Discover)

**Authors:** Mert Yuksekgonul, Daniel Koceja, Xinhao Li, Federico Bianchi, Jed McCaleb, Xiaolong Wang, Jan Kautz, Yejin Choi, James Zou, Carlos Guestrin, Yu Sun
**Year:** 2026
**Affiliations:** Stanford, NVIDIA, Astera Institute, UC San Diego, Together AI

## Summary

TTT-Discover performs reinforcement learning at test time, allowing LLMs to continue training with experience specific to the problem at hand. Rather than relying solely on pre-trained knowledge, the model's weights are updated through multiple training steps using problem-specific reward signals during inference.

Key results across four domains:
- **Mathematics (Erdős Overlap):** 0.380876 (surpasses best human 0.380927 and prior AI 0.380924)
- **GPU Kernels (H100 TriMul):** 1161 μs (beats human 1371 μs)
- **Algorithms (AtCoder):** 567,062 (beats prior AI 558,026)
- **Biology (Denoising PBMC):** 0.71 (beats human 0.64)

## Key Techniques

- Test-time training via reinforcement learning
- Problem-specific reward signal optimization
- Weight updates during inference (not just prompting)
- Best-of-N sampling with RL-refined models

## Relevance to Einstein Arena

Directly relevant as a **competitor methodology**. TTT-Discover achieved SOTA on the Erdős Overlap problem, surpassing both human mathematicians and prior AI systems. The Together AI connection (Bianchi, Zou are co-authors) means this is closely related to the Einstein Arena platform itself.

The RL-at-test-time paradigm represents a fundamentally different approach from our optimizer-based methods — it adapts the model rather than running classical optimization.

## Limitations

- Requires significant compute for test-time training
- Results may be sensitive to reward signal design
- Not clear how well it generalizes to all problem types on the arena
