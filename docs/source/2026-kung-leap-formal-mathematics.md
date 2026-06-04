---
type: source
kind: paper
title: "LEAP: Supercharging LLMs for Formal Mathematics with Agentic Frameworks"
authors: Po-Nien Kung, Linfeng Song, Dawsen Hwang, Jinsung Yoon, Chun-Liang Li, Simone Severini, Mirek Olšák, Edward Lockhart, Quoc V Le, Burak Gokturk, Thang Luong, Tomas Pfister, Nanyun Peng
year: 2026
author: agent
drafted: 2026-06-03
ingested_at: 2026-06-03
ingested_by: agent
source_type: arxiv
source_url: https://arxiv.org/abs/2606.03303
source_local: ../raw/2026-kung-leap-formal-mathematics.pdf
source_hash: d12c93ee83b8
topic: agentic-frameworks
tags: [agentic, formal-math, lean, theorem-proving, dag-memoization, llm-as-prover, blueprint-decomposition, verifier-guided-search]
related_problems: [21]
cites:
---

# LEAP: Supercharging LLMs for Formal Mathematics with Agentic Frameworks

**Authors:** Kung, Song, Hwang, Yoon, Li, Severini, Olšák, Lockhart, Le, Gokturk, Luong, Pfister, Peng (Google Cloud AI Research / Google Cloud / Google DeepMind) · **Year:** 2026 · **Source:** https://arxiv.org/abs/2606.03303 · **Code:** https://github.com/google-deepmind/superhuman/tree/main/leap

## Abstract

LEAP (**L**LM-in-Lean **E**nvironment **A**gentic **P**rover) is an agentic framework that lets a *general-purpose* foundation model (Gemini-3.1-pro) achieve state-of-the-art automated formal theorem proving in Lean 4 — without specialized fine-tuning. The system decomposes complex theorems into smaller units, interleaves informal blueprints with formal Lean sketches, and uses the Lean compiler plus an LLM reviewer as twin verifiers to guide proof search. The paper also introduces **Lean-IMO-Bench**, a 60-problem IMO-level Lean benchmark to escape saturated benchmarks like miniF2F / PutnamBench.

## Key contributions

- **Workflow-inspired agentic design.** A general-LLM-only loop matches or beats specialized prover models — the bottleneck is not formal-language comprehension, it's structured iterative interaction with the proof environment.
- **AND-OR DAG proof state with hierarchical memoization.** Intermediate lemmas are stored as shared nodes; any branch can reuse them (anticipatory lemma planning). Monotone refinement: decomposing a goal doesn't restructure the dependency graph.
- **Interleaved informal-formal planning.** Every formal attempt is paired with an informal rationale, so failures are interpretable; the informal blueprint reduces brittleness vs direct code generation.
- **Verification-guided proof search at two levels.** (1) Lean compiler checks syntax + type-correctness with `sorry` placeholders permitted only for proposed subgoals. (2) LLM reviewer judges whether a decomposition actually simplifies the parent goal — prevents the "subgoal syntactically identical to grandparent" failure (Figure 3).
- **Lean-IMO-Bench.** 60 problems (30 Basic, 30 Advanced) spanning algebra, combinatorics, number theory, geometry; built on Luong et al.'s informal IMO-ProofBench and hand-formalized by Lean experts.

## Methods

LEAP processes a theorem by registering it as the root OR node in an AND-OR DAG. For each open goal, a *state reader* retrieves its statement, dependencies, and related lemmas. The agent first attempts **direct formalization**: write informal proof → translate to Lean → submit to compiler. If that fails, it switches to **blueprint decomposition**: draft an informal blueprint, render it as a Lean proof sketch with `sorry` for the proposed lemmas, get the Lean compiler to accept the sketch (proves "main theorem reduces to these lemmas"), then have an LLM reviewer judge whether those lemmas really do simplify the goal. Accepted decompositions become AND nodes; proposed lemmas become child OR nodes. Search is DFS over the DAG with backtracking. LeanSearch (Gao et al. 2024) retrieves relevant lemmas from mathlib.

## Key results

- **Putnam 2025: 100% (12/12)** with rollout=2. Baselines: Gemini-3.1-pro pass@128 = **0%**, Goedel-Prover-V2-32B pass@128 = **0%**, Hilbert (agentic over Goedel) = **33.3%**, Aristotle (closed-source, IMO-2025 gold) = **75%**.
- **Lean-IMO-Bench Basic: 83.3%** overall (Algebra 100, Combinatorics 100, Number Theory 100, Geometry 16.7). Best prior: Aristotle 76.7%.
- **Lean-IMO-Bench Advanced: 56.7%** overall (Algebra 100, Comb 25, NT 100, Geom 12.5). Best prior: Aristotle 20%.
- **Iterative formalization ablation:** giving Gemini-3.1-pro 20 compiler-feedback revision steps boosts Pass@1 from 20.0% → 36.6% on Basic; the same loop *hurts* Goedel-Prover-V2-32B (10.0 → 6.6). Specialized small provers are worse at consuming feedback than general LLMs.
- **DAG memoization ablation:** full DAG vs naive tree → Basic 73.3 → 83.3, Advanced 40.0 → 56.7. Biggest gains on Advanced Algebra (75 → 100) and Advanced NT (66.6 → 100).
- **Compute cost (Putnam 2025):** LLM calls per problem range 46 (b2) → 3.0k (a5); active DAG nodes 8 → 211; proof length 300 → 2000 lines. Total proof for hardest problem ≈ 2k lines of Lean 4.
- **Open-problem case study:** verified a critical subproblem (≈5000 lines Lean 4) of Knuth's Hamiltonian decomposition of even-order directed Cayley graphs $\text{Cay}(\mathbb{Z}_m^3, \{e_1, e_2, e_3\})$ — a 20-page informal proof with parity-dependent intervals and cross-row transitions. Also reproduced Erdős Problem 457 (triangle-free density).

## Limitations / open questions

- **Geometry remains near-zero.** All systems including LEAP fail at olympiad geometry in Lean (Advanced Geometry: LEAP 12.5%, Aristotle 0). Likely needs domain-specific frameworks (analogue: Lean's lack of a strong synthetic-geometry library).
- **Compute is substantial.** 3k LLM calls on the hardest Putnam problem is expensive; future work needs smarter branch prioritization and compute allocation across the DAG.
- **Hybrid general-LLM + specialized-prover.** Authors flag this as a likely better design pattern but defer it — this paper deliberately stays standalone-general to make the methodological point.
- **DFS search is naive.** LLM-as-search-heuristic for branch selection (beyond the local decomposition reviewer) is explicit future work.
- **Closed-source competitors not reproducible.** Aristotle and Numina ran on Putnam 2025 but did not respond to requests for leaderboard access; comparisons rely on their published numbers.
