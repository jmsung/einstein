---
type: source
kind: paper
title: Coding-agents can replicate scientific machine learning papers
authors: Atharva Hans, Ilias Bilionis
year: 2026
author: agent
drafted: 2026-07-05
ingested_at: 2026-07-05
status: distilled
source_type: arxiv
source_url: https://arxiv.org/abs/2607.02134
source_local: ../raw/2026-hans-paper-replication.pdf
distilled_from_hash: abc74823d062
topic: agent-harness-engineering
cites:
---

# Coding-agents can replicate scientific machine learning papers

**Authors:** Atharva Hans, Ilias Bilionis (Purdue) · **Year:** 2026 · arXiv:2607.02134

## Abstract

Introduces **Paper-replication**: a workflow (implemented as a coding-agent skill) that
turns each selected paper claim into a *target* with recorded evidence, and makes
completion depend on **workspace state + external validation checks rather than the
agent's final message**. Evaluated on 12 runs across 4 SciML papers (PIFT, PINN-I/II,
SINDy): all 12 pass the completion gate, all 158 targets matched with report coverage.

## Key contributions

- Defines paper replication as a **target-level evidence contract** for a coding agent —
  each target links a generated output to method reconstruction, a successful run,
  provenance, comparison evidence, and report coverage before it can be marked matched.
- A persistent **replication workspace**: reproduction matrix (targets + status), task
  ledger (one active target at a time), specification files (method reconstruction),
  run + provenance records (command, seed, hashes), comparison evidence, report coverage,
  completion gate.
- **Validation checks run OUTSIDE the agent** before a claim can be marked matched —
  "the agent's final message is not enough evidence" (motivated by intrinsic
  self-correction limits, Huang et al. 2024: an LM cannot reliably judge/repair its own
  reasoning without external feedback).
- **Hash checks detect copied paper-provided assets** — anti-cheat: a target can't be
  passed by reusing the paper's own figure/table/rendered page instead of reconstructing.

## Methods

Targets come in four claim types, each with a claim-specific acceptance rule: **numeric**
(discrepancy ≤ recorded tolerance), **distributional** (compare summary statistics /
intervals, not identical samples), **structural** (sparsity, ordering, regime transition,
attractor structure), **visual** (reference vs candidate image comparison, only when the
claim is inherently visual). Failed runs are *replaced, not overwritten* — the workspace
preserves the trial-and-correction path. Completion gate passes only when every recorded
target has accepted evidence, no target remains active, and the replication-report PDF exists.

## Why interesting for einstein

Direct external corroboration of the meta-layer thesis in
[`findings/gates-compound-discretion-decays`](../wiki/findings/gates-compound-discretion-decays.md)
("a rule is advice the agent can rationalize past; a gate is not") and the capture-gate
`Stop` hook. Their **"completion = workspace evidence + external checks, not final
message"** is exactly the einstein capture-gate + triple-verify design, independently
arrived at from the SciML-replication direction. The reproduction-matrix/task-ledger split
mirrors `docs/agent/` (cycle-log + skill-library). Strong candidate cite for the
methodology paper's harness section (§harness), and a design reference for hardening the
autonomous loop's completion criteria.

## Limitations / open questions

- Even in a *completed* workspace, repeated runs vary in target decomposition, paper-anchored
  numeric fidelity, elapsed replication time, number of intermediate executions, and the
  acceptance rules chosen — the replication *process itself* is not tightly reproducible.
- Scope limited to SciML papers with computational claims; author code is disallowed in
  their setting (agent must infer + implement the method), narrowing generality.
- Hash checks catch verbatim copies but not transformed/adversarial reuse of paper assets.
