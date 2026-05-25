---
type: source
kind: paper
title: Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine
authors: Wenyi Wang, Piotr Piekos, Nanbo Li, Firas Laakom, Yimeng Chen, Mateusz Ostaszewski, Mingchen Zhuge, Jurgen Schmidhuber
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2510.21614
source_local: ../raw/2025-wang-huxley-g-del-machine-human-level.pdf
topic: general-knowledge
cites:
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

## Why it matters here
General background; no direct arena tie. The relevant transferable idea is the **lineage / clade-aggregated credit assignment** principle: when scoring a node whose *value* is its capacity to seed good descendants (e.g. an exploration root in basin-hopping, a parameterization in a search tree, a council-question), aggregate over its subtree rather than scoring the node alone. Also: Thompson-sampling + UCB-Air-style arm-widening as a scheduler for "when to spawn a new candidate vs evaluate an existing one" — directly applicable to the autonomous loop's expand-vs-evaluate decisions.

## Open questions / connections
- Extends Schmidhuber's Gödel Machine (2003) by replacing intractable formal-proof acceptance with a sampled clade statistic — at the cost of Assumption 1's terminal-only utility (no intermediate reward).
- The CMP estimator is biased by which agents the evaluation policy probes; the paper notes asynchronous execution introduces an "easy tasks finish first" bias that fades after ~50 evaluations — a caution for any clade-aggregated metric on partially-observed trees.
- Open: how to extend CMP-style credit assignment beyond binary success indicators (e.g. continuous arena scores with verifier drift, as in P14/P17).
- Could the "decouple expansion from evaluation; let unpromising arms be early-stopped" rule generalize to the council-dispatch protocol (early-stop personas whose questions aren't seeding findings)?

## Key terms
Gödel Machine, self-improving agent, clade metaproductivity, CMP, Thompson sampling, UCB-Air, infinite-armed bandit, tree search, Darwin Gödel Machine, SICA, SWE-bench, coding agent, meta-learning, Schmidhuber, lineage-aggregated credit assignment
