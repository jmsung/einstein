<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine
authors: [Wenyi Wang, Piotr Piekos, Nanbo Li, Firas Laakom, Yimeng Chen, Mateusz Ostaszewski, Mingchen Zhuge, Jurgen Schmidhuber]
year: 2025
source_url: https://arxiv.org/abs/2510.21614
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine

**Authors:** Wenyi Wang, Piotr Piekos, Nanbo Li, Firas Laakom, Yimeng Chen, Mateusz Ostaszewski, Mingchen Zhuge, Jurgen Schmidhuber  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2510.21614

## One-line
Selects which self-modifying coding agent to expand by estimating the aggregate benchmark success of its *entire descendant lineage* (clade) instead of its own immediate score, approximating the Gödel Machine.

## Key claim
Greedy "best-current-score" selection (used by DGM, SICA) is weakly correlated with long-run self-improvement potential (Metaproductivity-Performance Mismatch); a clade-aggregated estimator (CMP) raises the Pearson correlation with empirical metaproductivity from ~0.28-0.44 to 0.78 (SWE-Verified-60) and 0.63 (Polyglot). Theorem 1: under their restricted setting (Assumption 1: terminal-only utility, repeatable trials, unit-cost modifications), access to a true CMP oracle suffices to implement the Gödel Machine.

## Method
Cast self-improvement as tree search over agents; each node tracks $n^C_{\text{success}}(a), n^C_{\text{failure}}(a)$ aggregated over its clade $C(a)$. Estimator $\widehat{\mathrm{CMP}}(a) = n^C_{\text{success}}(a) / (n^C_{\text{success}}(a) + n^C_{\text{failure}}(a))$. Expansion/evaluation are decoupled (vs DGM/SICA which couple them); both use Thompson sampling on $\mathrm{Beta}(\tau(1+n_s), \tau(1+n_f))$ with monotone-in-$t$ scheduler $\tau$; new arms (expansions) added when $|T_t| \le N_t^\alpha$ (UCB-Air rule, $\alpha = 0.6$); final agent chosen by $\epsilon$-percentile of utility posterior via regularized incomplete beta $I_\epsilon$. Async implementation parallelizes across CPUs.

## Result
On SWE-bench Verified, HGM reaches 56.67% vs DGM's 53.33% / SICA's 50%, with 2.38× fewer CPU-hours. On Polyglot it dominates both baselines. The HGM-discovered agent (optimized on SWE-Verified with GPT-5-mini), evaluated on SWE-bench Lite with GPT-5, matches the best officially-checked human-engineered coding agents — i.e. transfers under simultaneous dataset + model shift.

## Key terms
Gödel Machine, self-improving agent, clade metaproductivity, CMP, Thompson sampling, UCB-Air, infinite-armed bandit, tree search, Darwin Gödel Machine, SICA, SWE-bench, coding agent, meta-learning, Schmidhuber, lineage-aggregated credit assignment
