---
type: source
kind: paper
title: Less can be more for predicting properties with large language models
authors: Nawaf Alampara, Santiago Miret, K. Jablonka
year: 2024
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2406.17295
source_local: ../raw/2024-alampara-less-can-more-predicting.pdf
topic: general-knowledge
cites:
---

# Less can be more for predicting properties with large language models

**Authors:** Nawaf Alampara, Santiago Miret, K. Jablonka  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2406.17295

## One-line
Large language models systematically fail to learn from coordinate (geometric) information in coordinate-category data such as crystal structures, even though they readily learn the categorical (atom-type) component.

## Key claim
Across model scales (up to 70B parameters), dataset scales (up to 2M structures), and nine text representations, LLMs exhibit a positive **Coordinate-Category Cliff** ($L_{\text{coord},\alpha} > L_{\text{cat},\alpha}$): error on coordinate-dominated tasks is consistently and significantly higher than on category-dominated tasks, and the behavior mirrors that of n-gram baselines — implying LLMs effectively ignore coordinate structure.

## Method
Synthetic coordinate-category datasets with a tunable hypothetical potential $E = \alpha E_{\text{category}} + (1-\alpha) E_{\text{coordinate}}$, $\alpha \in (0,1)$, used to sweep from purely positional to purely categorical labels. BERT and instruction-tuned LLaMA (7B/13B/70B) are finetuned across nine text representations (Composition, Atom Sequence ±, SLICES, Local-Env, Crystal-Text-LLM, CIF P1, CIF Symmetrized, Z-Matrix) inside the **MatText** benchmarking framework, with cross-validation, attention-mask token-type analysis, and n-gram comparison. Real materials tasks (shear/bulk modulus, formation energy, dielectric, GVRH, phonons, bandgap, perovskites) are evaluated against MatBench GNN baselines (CGCNN, SchNet, DimeNet).

## Result
The CC-Cliff is positive on every synthetic and real dataset; SLICES (no coordinates) matches or beats CIF P1 (full coordinates); RT order-of-magnitude tokenization gives no consistent gain; scaling data 30K→2M and model 7B→70B produces RMSE changes inside the random-fluctuation band. On MatBench, a clear **"GNN–LM wall"** separates GNN approaches (lower MAE) from LM approaches (higher MAE) across six properties. Attention analysis shows numeric tokens receive far less attention than atomic-symbol tokens, and no dedicated number-feature heads emerge from pretraining.

## Why it matters here
General background; no direct arena tie. The negative result on geometric/coordinate learning is a useful caution if the Einstein agent ever considers an LLM-based surrogate for coordinate-heavy problems (sphere packing, kissing, Heilbronn-style point configurations) — specialized geometric optimizers / GNN-style inductive biases dominate the LM route at fixed budget.

## Open questions / connections
- Are there architectural modifications (e.g., explicit positional encodings for $\mathbb{R}^3$, equivariant attention, MACE-style tensor messages) that close the CC-Cliff without abandoning the LM stack?
- How does the cliff scale with dataset "diversity volume" (convex-hull area in ChgNet embedding PCA) — observed correlation is non-monotonic and unexplained.
- Connects to the broader question of when text-serialization of geometric objects is information-preserving but model-inefficient — relevant when designing prompts that include coordinate dumps.

## Key terms
large language models, coordinate-category data, CC-Cliff, MatText, materials property prediction, GNN-LM wall, n-gram models, SLICES, CIF, Z-matrix, inductive bias, geometric learning, attention analysis, BERT, LLaMA
