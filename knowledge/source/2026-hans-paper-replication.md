<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
domains: [ai-agents, ai-ml, ai-verification]
title: "Coding-agents can replicate scientific machine learning papers"
authors: [Atharva Hans, Ilias Bilionis]
year: 2026
arxiv: 2607.02134
source_url: https://arxiv.org/abs/2607.02134
drive_file_id: 15p61MmsjQn_prkvfvSfwQ7YPWR_jZ0mG
text_source: pdf
ingested_by: claude-opus-4-8
---

# Coding-agents can replicate scientific machine learning papers

**Authors:** Atharva Hans, Ilias Bilionis (School of Mechanical Engineering, Purdue University)  ·  **Year:** 2026  ·  **Venue:** arXiv:2607.02134  ·  **Source:** https://arxiv.org/abs/2607.02134

## One-line
Paper-replication is a coding-agent skill that turns each computational claim in a scientific-ML paper into a tracked target with recorded evidence, forcing the agent to reconstruct the method, run experiments, tie outputs to provenance and to the paper's claims, and pass validation before it can declare completion.

## Key claim
A coding agent *can* be prompted to replicate a paper's computational claims from paper materials alone, but a bare prompt doesn't preserve progress or check that generated evidence actually supports the claims. Structuring replication as claim-targets-with-evidence plus a completion gate makes agent-driven replication auditable and reliably complete.

## Method
- **Paper-replication workflow (implemented as a coding-agent skill):** select paper claims (e.g., "relative MSE < 5%", "95% predictive credible interval covers the test data") as targets; for each, record the target, reconstruct the paper's method, run computational experiments, link generated outputs to provenance and to comparisons with the paper's claims, record where the matched evidence appears in the replication report, and pass validation checks before completion.
- Built on general coding agents (Codex, Claude Code) that inspect files, edit code, run commands, and iterate on failures.

## Key results
- Evaluated over **12 independent runs (3 per paper) across 4 scientific-ML papers**, one coding-agent interface/model/reasoning setting.
- **All 12 workspaces pass the completion gate; all 158 recorded targets are matched with report coverage.**
- Repeated runs still differ in how papers are divided into targets and in numerical fidelity — completion does not imply identical decomposition or exact reproduction.

## Why it matters
A concrete pattern for making agentic replication/verification trustworthy: bind claims to evidence and gate completion on validation, rather than trusting an agent's self-report. Directly transferable to any "reproduce/verify this artifact" agent task. Noted limitations (4 papers, 3 runs each, single agent/model/setting, no skill-ablation) bound the strength of the "coding-agents can replicate" claim.
