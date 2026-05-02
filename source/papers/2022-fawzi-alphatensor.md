---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://www.nature.com/articles/s41586-022-05172-4
source_local: sources/2022-fawzi-alphatensor.pdf
cites:
  - ../papers/2023-romera-paredes-funsearch.md
  - ../papers/2025-novikov-alphaevolve.md
---

[[../home]] | [[../index]]

# Fawzi et al. — Discovering Faster Matrix Multiplication Algorithms with Reinforcement Learning (AlphaTensor)

**Authors:** Alhussein Fawzi, Matej Balog, Aja Huang, Thomas Hubert, Bernardino Romera-Paredes, Mohammadamin Barekatain, Alexander Novikov, Francisco J. R. Ruiz, Julian Schrittwieser, Grzegorz Swirszcz, David Silver, Demis Hassabis, Pushmeet Kohli
**Year:** 2022 (Nature 610:47–53, 6 October 2022)

## Summary

DeepMind's first major scientific-discovery RL system. AlphaTensor casts matrix multiplication as a **single-player tensor-decomposition game**: the state is the residual tensor, actions are rank-1 outer-product subtractions, and the goal is to drive the tensor to zero in as few moves as possible — exactly the bilinear rank of the matrix multiplication tensor.

Headline results:
- New decomposition for **4×4 matrix multiplication in F_2**: rank 47 (down from Strassen's 49 over reals; first improvement in 50 years for this size)
- New best ranks for many sizes ⟨m, n, p⟩ with 2 ≤ m,n ≤ 5 — later subsumed by Smirnov / Kauers-Moosbauer / AlphaEvolve, but at the time SOTA
- Demonstration that AlphaZero-style RL can navigate enormous combinatorial spaces (factor space ~10^33) and discover provably correct algorithms

This paper is the methodological *predecessor of FunSearch and AlphaEvolve* in the DeepMind scientific-discovery lineage. AlphaTensor uses pure RL on a fixed game; FunSearch uses LLM-mediated evolutionary search; AlphaEvolve combines both.

## Key Techniques

- **Tensor-decomposition game** — single-player MDP with rank-1 actions
- **AlphaZero-style MCTS + neural network** — policy/value network guides search
- **Synthetic training data** — random tensors with known low-rank decompositions
- **Symmetrization** — exploit the symmetry of the matrix-mult tensor for sample efficiency
- **Modular-arithmetic decompositions** — F_2 setting where 4×4 rank dropped to 47
- **Provable correctness** — every decomposition is verified post-hoc, no probabilistic guarantee

## Relevance to Einstein Arena

### Methodological precursor

AlphaTensor is the canonical example of "RL discovers provably-correct algorithms in extremal-combinatorics-style spaces." Several arena problems (Heilbronn P15/P16, packing P14/P17, kissing P6/P22) admit similar formulations: state = current configuration, action = local move, score = exact provable objective. The AlphaZero-style architecture is one possible engine, though FunSearch / AlphaEvolve / agent-driven search have largely supplanted it for problems where LLMs help.

### Cross-cutting — RL vs. evolutionary search

Reading AlphaTensor and FunSearch back-to-back highlights the design tradeoff: pure RL (no LLM) is more sample-efficient when the action space is small and well-defined; LLM-driven evolution is more flexible when the search space is "code." Arena problems span both regimes. This paper anchors the pure-RL end.

### Direct connection
FunSearch (2023) and AlphaEvolve (2025) cite AlphaTensor as the lineage anchor. The same DeepMind team produced all three.

## Limitations

- Compute-heavy — AlphaTensor's training was substantial GPU-weeks per problem
- Many headline ranks have been beaten (Smirnov / Kauers-Moosbauer / AlphaEvolve)
- Single-game formulation requires hand-crafting the action space; not directly portable to arena problems without adaptation
- F_2 results don't translate to real-arithmetic ranks for some sizes

## See Also

- [[2023-romera-paredes-funsearch]] — successor with LLMs in the loop
- [[2025-novikov-alphaevolve]] — combines RL + LLM evolutionary search
