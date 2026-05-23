---
type: source
kind: paper
title: Symbolic Regression with a Learned Concept Library
authors: Arya Grayeli, Atharva Sehgal, Omar Costilla-Reyes, Miles D. Cranmer, Swarat Chaudhuri
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2409.09359
source_local: ../raw/2024-grayeli-symbolic-regression-learned-concept.pdf
topic: general-knowledge
cites:
---

# Symbolic Regression with a Learned Concept Library

**Authors:** Arya Grayeli, Atharva Sehgal, Omar Costilla-Reyes, Miles D. Cranmer, Swarat Chaudhuri  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2409.09359

## One-line
LASR augments a genetic-programming symbolic regression algorithm (PySR) with an LLM-induced library of natural-language "concepts" that bias mutation, crossover, and initialization toward physically/mathematically plausible expressions.

## Key claim
On the 100-equation Feynman SRBench benchmark, LASR exactly recovers 72/100 equations vs PySR's 59/100 (and 66 in the abstract's earlier number); the improvement persists even against PySR run for $10^6$ iterations / 10 hours per equation (PySR: 62, LASR at 40 iterations: 72).

## Method
Hierarchical Bayesian model $p(\pi, C \mid D) \propto p(D \mid \pi)\, p(\pi \mid C)\, p(C)$ where $C$ is a latent natural-language concept library and $\pi$ is a program. Alternating maximization: (1) hypothesis evolution — at each genetic step, with probability $p$ (e.g. 0.01–0.10) replace symbolic mutation/crossover/init with an LLM-call conditioned on $l$ concepts sampled from $C$; (2) concept abstraction — zero-shot LLM prompt over Pareto-frontier good + worst-loss bad hypotheses produces new concepts; (3) concept evolution — LLM "crossover" over existing concepts to extend $C$. Backbones tested: gpt-3.5-turbo, llama3-8b.

## Result
Ablations show variable names, concept library, and concept evolution each contribute; removing the library widens the gap further at higher $p$. Cascading $p \in \{1\%, 5\%, 10\%\}$ and backbone size monotonically improves solve rate. Case study: LASR discovers an LLM scaling law $\text{score} = -0.0248/\text{shots} + 0.360124 \cdot \text{train\_steps}^{1/116050.999}$ on BigBench with only 3 free parameters (vs Chinchilla's 5), competitive on held-out MSE. Re-running with different seeds yields syntactically different equally-fitting equations — evidence against memorization.

## Why it matters here
General background; no direct arena tie. The most transferable idea for the einstein autonomous loop is the **three-phase alternating maximization** (concept-directed search / concept abstraction from Pareto frontier / concept evolution) — structurally identical to the repo's gap-detect → distill → wiki-evolve cycle, but with the concept library directly biasing the *next* search step rather than just informing future humans. The Pareto-of-good + worst-loss bad pairing for concept extraction is a directly usable pattern for `concept-extraction`/`failure-is-a-finding` distillation.

## Open questions / connections
- Could the council-dispatch persona prompts be reframed as LASR-style concept-conditioned operators that *mutate candidate solutions*, not just write questions? — closes the gap between persona output and optimizer state.
- LASR's Pareto-frontier-good vs worst-loss-bad concept extraction is a sharper version of the dead-end-finding distillation: pairing positive + negative exemplars in one prompt rather than separately.
- LASR has no triple-verify analogue — it trusts a single MSE; in this repo's setting (P9/P14/P17 verifier drift) the concept extraction would need to condition on agreement across evaluators, not raw fitness.
- Extension to non-SR settings (combinatorial optimization, packing) is unexplored — the "concept" abstraction may or may not survive when hypotheses are configurations rather than expressions.

## Key terms
symbolic regression, LASR, PySR, genetic programming, concept library, LLM-guided evolution, Pareto frontier, concept abstraction, concept evolution, alternating maximization, Feynman equations, SRBench, hierarchical Bayesian program synthesis, scaling laws, zero-shot prompting, Cranmer
