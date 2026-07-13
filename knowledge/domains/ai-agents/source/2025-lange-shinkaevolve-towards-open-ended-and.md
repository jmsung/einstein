<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution"
authors: [Robert Tjarko Lange, Yuki Imajuku, Edoardo Cetin]
year: 2025
doi: 10.48550/arXiv.2509.19349
source_url: https://doi.org/10.48550/arXiv.2509.19349
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution

## TL;DR
ShinkaEvolve is an open-source (Apache 2.0) LLM-driven evolutionary program-optimization framework that matches or beats closed systems like AlphaEvolve while using orders-of-magnitude fewer evaluations — e.g. a new state-of-the-art circle-packing solution in only 150 samples versus thousands.

## Key findings
- **Three core algorithmic innovations** drive the sample efficiency: (1) an adaptive parent-sampling strategy balancing exploration/exploitation, (2) code-embedding novelty rejection sampling, and (3) a bandit-based LLM ensemble selection that adapts which model proposes mutations.
- **Parent sampling**: programs in island subpopulations are selected by either power-law ranking (α controls exploitation; α=0 → uniform, α→∞ → hill-climbing) or a "weighted" scheme combining a sigmoid performance score sᵢ=σ(λ·(F(Pᵢ)−α₀)) (α₀ = median fitness) with a novelty term hᵢ=1/(1+N(Pᵢ)) favoring programs with fewer offspring. Ablation: weighted sampling consistently beats both random search and hill-climbing (hill-climbing plateaus early).
- **Novelty rejection sampling**: mutable code is embedded (text-embedding-3-small); proposals with max cosine similarity > 0.95 to archive members are escalated to an LLM-as-novelty-judge. Ablation shows embedding-based rejection gives substantial gains; the LLM judge adds only marginal benefit.
- **Bandit LLM ensemble**: a UCB1 variant selects among GPT, Gemini, Claude, DeepSeek models. The reward is relative — rᵢᵘ = exp(max(rᵢ−rᵢᵇ,0))−1 where rᵢᵇ is the max of parent/initial fitness — promoting bold high-reward mutations over safe minor ones. Beats both single-LLM and fixed-uniform ensembles.
- **Mutation operators**: diff-based SEARCH/REPLACE edits, full rewrites (with immutable EVOLVE-BLOCK markers), and crossover; invalid patches trigger Reflexion-style resampling. A periodic **meta-scratchpad** summarizes recent winners into prompt guidance every T generations.
- **Results across 4 domains**: (1) *Circle packing* (26 circles, maximize Σradii) — beats AlphaEvolve in <150 evals, sum 2.6360; (2) *AIME 2024 agent scaffolds* — evolves a 7-call (3 generate + 3 review + 1 synthesis) multi-persona scaffold on gpt-4.1-nano that generalizes across years (esp. unseen 2025) and across base LLMs (gpt-4.1-mini/gpt-4.1/o4-mini); (3) *ALE-Bench LITE* competitive programming — improves ALE-Agent solutions ~2.3% on 10 tasks, reaching 2nd-place-equivalent on ahc039; (4) *MoE load-balancing loss* — discovers a new LBL augmenting the global-batch loss with an entropy-scaled minimum-usage regularizer that rescues under-specialized ("dead") experts, validated on 556M→2.7B-parameter MoE training.

## Methods (brief)
LLM agents act as mutation operators over an archive of evaluated programs organized into parallel island subpopulations with occasional migration. Each candidate is executed, scored on a scalar fitness plus exposed public metrics and textual feedback, and stored for future prompting. Validation used relaxed vs. exact verification (circle packing), three independent runs per candidate (AIME), and public→private test-set submission (ALE-Bench).

## Limitations
Fixed hyperparameter configs with no automatic exploration-exploitation control; requires manually specified objective functions and well-defined numerical fitness, limiting open-endedness. On ALE-Bench it tended to stay close to the seed solution (potential overfitting to initialization), and the MoE LBL was evolved and tested on similar architectures with limited training budget.

## Citations of interest
- Novikov et al. 2025 (AlphaEvolve) — the closed-source coding agent ShinkaEvolve benchmarks against and borrows diff/island mechanics from.
- Romera-Paredes et al. 2024 (FunSearch, *Nature*) — foundational LLM program-search with island models.
- Hu et al. 2024 (Automated Design of Agentic Systems) — basis for the AIME agent-scaffold task.
- Imajuku et al. 2025 (ALE-Bench / ALE-Agent) — benchmark and seed solutions for the competitive-programming experiments.
- Shinn et al. 2024 (Reflexion) — verbal-feedback resampling used for invalid patch recovery.
- Auer et al. 2002 (UCB1) — bandit algorithm underlying the adaptive LLM selection.
