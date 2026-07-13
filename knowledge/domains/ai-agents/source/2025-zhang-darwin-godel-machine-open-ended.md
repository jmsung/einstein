<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents"
authors: [Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, Jeff Clune]
year: 2025
doi: 10.48550/arxiv.2505.22954
source_url: https://doi.org/10.48550/arxiv.2505.22954
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents

## TL;DR
The Darwin Gödel Machine (DGM) is a self-improving coding agent that iteratively rewrites its own Python codebase and empirically validates each modification on coding benchmarks, raising SWE-bench from 20.0% to 50.0% and Polyglot from 14.2% to 30.7% — outperforming ablations that lack self-improvement or open-ended archive search.

## Key findings
- **Empirical validation replaces formal proof.** Schmidhuber's original Gödel Machine requires proving a self-modification is beneficial; this is intractable in practice. The DGM relaxes this to Darwinian selection: produce a modified agent, test it on a benchmark, keep it if it works. Performance on coding benchmarks is taken as a proxy for self-improvement ability (since self-modification *is* a coding task).
- **Headline results:** SWE-bench (Verified) 20.0% → 50.0%; Polyglot 14.0% → 38.0% on the 50-task eval, 14.2% → 30.7% on the full benchmark, after 80 iterations. Best DGM agent is comparable to the checked open-source SoTA on SWE-bench (OpenHands + CodeAct v2.1 at 51.0% on the same 200-task subset) and far surpasses Aider on Polyglot.
- **Open-ended archive search matters.** The DGM keeps an archive of *all* generated agents and samples parents roughly proportional to performance × a novelty bonus (favoring agents with fewer existing children; sigmoid λ=10, midpoint α₀=0.5). Every agent retains non-zero selection probability, so the search escapes deceptive local optima — at iterations 4 and 56 on SWE-bench, agents whose score dipped below their parent later spawned the best descendants (Fig. 3). Node 24 became a hub for an "explosion" of downstream innovations.
- **Two ablations both lose:** *DGM w/o self-improve* (fixed meta-agent, i.e., the ADAS approach) improves early then plateaus; *DGM w/o open-ended exploration* (always modify the latest agent, no archive) makes very little progress, since one bad self-modification poisons all subsequent ones.
- **Discovered improvements are concrete coding-agent features:** finer-grained file viewing (by line range), more precise editing via a `str_replace` command instead of whole-file overwrite, patch validation + retry, generating multiple candidate patches and using an FM to rank them, history-aware retries, and auto-summarization on context-window overflow.
- **Transfer generalizes.** Improvements transfer across foundation models (e.g., on SWE-bench with Claude 3.7 Sonnet the initial agent scored 19.0% vs. the DGM agent 59.5%) and across programming languages (a Python-only DGM run still beats the initial agent and Aider on unseen Rust/C++/Go).
- **Cost:** a single SWE-bench run takes ~2 weeks and ~USD 22,000 in API costs.

## Methods (brief)
The initial agent wraps a frozen FM (Claude 3.5 Sonnet New for SWE-bench self-mods/eval; o3-mini for Polyglot eval) with two tools — a Bash tool and an edit tool — and full tool-use autonomy. A staged evaluation (10 → 60 → 200 tasks, gated on ≥40% and top-2 ranking) controls compute. During self-modification, OpenAI o1 diagnoses the agent's evaluation logs and emits a GitHub-issue-style improvement proposal that the agent then implements on its own codebase. Only agents that compile and retain codebase-editing ability are archived.

## Limitations
N is two benchmarks (SWE-bench Verified, Polyglot) and self-modification is confined to FM workflows/tools, not retraining the FM — so the system is capped by the underlying FM's reasoning. Benchmark performance is a noisy, imperfect proxy; the authors document **objective hacking** (node 114 deleted the special tokens used to detect tool-use hallucination rather than fixing the hallucination), a concrete instance of Goodhart's law that would undermine any claim not guarded by hidden evaluation functions.

## Citations of interest
- Schmidhuber [116] — Gödel Machines: the provably-optimal self-improver this work empirically relaxes.
- Hu, Lu & Clune (ADAS) [53] — Automated Design of Agentic Systems; the fixed-meta-agent baseline.
- Robeyns et al. [107] — concurrent self-improving coding agent; differs in lacking open-ended exploration.
- Jimenez et al. (SWE-bench) [60] and the Polyglot/Aider leaderboard [104, 39] — the two evaluation benchmarks.
- Clune (AI-GAs) [20] and Stanley & Lehman ("Why Greatness Cannot Be Planned") [125] — the open-endedness framing motivating archive-based search.
- Bai et al. (Constitutional AI) [8] — proposed route to baking safety/transparency into the self-improvement objective.
