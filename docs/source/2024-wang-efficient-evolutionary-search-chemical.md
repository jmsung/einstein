---
type: source
kind: paper
title: Efficient Evolutionary Search Over Chemical Space with Large Language Models
authors: Haorui Wang, Marta Skreta, C. Ser, Wenhao Gao, Lingkai Kong, Felix Streith-Kalthoff, Chenru Duan, Yuchen Zhuang, Yue Yu, Yanqiao Zhu, Yuanqi Du, Alán Aspuru-Guzik, K. Neklyudov, Chao Zhang
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2406.16976
source_local: ../raw/2024-wang-efficient-evolutionary-search-chemical.pdf
topic: general-knowledge
cites:
---

# Efficient Evolutionary Search Over Chemical Space with Large Language Models

**Authors:** Haorui Wang, Marta Skreta, C. Ser, Wenhao Gao, Lingkai Kong, Felix Streith-Kalthoff, Chenru Duan, Yuchen Zhuang, Yue Yu, Yanqiao Zhu, Yuanqi Du, Alán Aspuru-Guzik, K. Neklyudov, Chao Zhang  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2406.16976

## One-line
Replaces the random crossover/mutation operators in a molecular genetic algorithm with chemistry-aware LLM (GPT-4 / BioT5 / MoleculeSTM) prompts to cut the number of oracle calls needed to find high-fitness molecules.

## Key claim
On 26 black-box molecular-optimization tasks (PMO + TDC), MOLLEO — Graph-GA with LLM-driven operators — beats Graph-GA, REINVENT, GP-BO, Augmented Memory, and DST in top-10 AUC across single- and multi-objective settings; e.g. JNK3 top-10 AUC rises from $0.773$ (Graph-GA) to $0.790$ (GPT-4), and `scaffold_hop` from $0.565$ to $0.971$.

## Method
Build on Graph-GA (Jensen 2019): sample two parents proportional to fitness, but route CROSSOVER through GPT-4 prompted with both parents + their objective scores, or route MUTATION through BioT5 (SELFIES seq2seq fine-tuned on chemistry) or MoleculeSTM (contrastive text–molecule encoder with gradient-descent latent editing, $x_{t+1} = x_t - \alpha \nabla_{x_t} L(x_t)$ where $L = -\cos(E_M^c(A_{gc}(x_t)), E_T^c(\text{prompt})) + \lambda\|x_t - x_0\|^2$). A Tanimoto-similarity filter to the top-fitness incumbent prunes LLM offspring, since LLMs do not reliably improve fitness without selection pressure. Multi-objective uses either weighted sum $\arg\max \sum_i w_i F_i(m)$ or Pareto-frontier selection with hypervolume metric.

## Result
LLM operators preserve substructure (Tanimoto $0.43$ GPT-4 / $0.76$ MolSTM to parent vs $\sim 0.12$ to random) while moving toward objective. On expensive oracles (docking against 3pbl/2rgp/3eml at 1000-call budget) LLM overhead is dominated by oracle cost; on cheap oracles GPT-4 adds wall-clock. Prompt phrasing matters — Spearman-$\rho$-selected prompt lifts MolSTM JNK3 top-10 AUC from $0.643$ to $0.730$. Improvements transfer when MOLLEO operators are dropped into Augmented Memory, Genetic GFN, and JANUS, not just Graph-GA.

## Why it matters here
General background; no direct arena tie — none of the 23 Einstein Arena problems are molecular. The transferable lesson for the agent is structural: replacing **random** GA operators with **task-conditioned LLM operators + a similarity filter to the incumbent** is a recipe that may apply to combinatorial-search problems in the arena (e.g. P9 Sidon-set perturbations, P11 Hardin–Sloane configurations), and the Pareto-hypervolume framing is reusable for any multi-criterion polish.

## Open questions / connections
- Does an LLM crossover beat random crossover on geometric/combinatorial search spaces (point configurations, autocorrelation sequences) where SMILES has no analogue?
- The "filter LLM proposals by similarity to current best" trick generalizes — does it help basin-hopping when the proposer is a stochastic neural sampler?
- Cost regime: LLM operators only pay off when the oracle is much more expensive than the LLM call — what's the breakeven for arena evaluators (cheap) vs full triple-verify (expensive)?

## Key terms
evolutionary algorithm, genetic algorithm, Graph-GA, crossover, mutation, LLM operator, GPT-4, BioT5, MoleculeSTM, SMILES, SELFIES, black-box optimization, Pareto frontier, hypervolume, Tanimoto similarity, molecular optimization, oracle budget, multi-objective optimization
