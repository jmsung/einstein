---
type: note
kind: paper-relevance
about: 2025-wang-huxley-g-del-machine-human-level
canonical: ../../domains/ai-agents/source/2025-wang-huxley-g-del-machine-human-level.md
---

# Relevance note — Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine

Canonical distillation: [`2025-wang-huxley-g-del-machine-human-level.md`](../../domains/ai-agents/source/2025-wang-huxley-g-del-machine-human-level.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The relevant transferable idea is the **lineage / clade-aggregated credit assignment** principle: when scoring a node whose *value* is its capacity to seed good descendants (e.g. an exploration root in basin-hopping, a parameterization in a search tree, a council-question), aggregate over its subtree rather than scoring the node alone. Also: Thompson-sampling + UCB-Air-style arm-widening as a scheduler for "when to spawn a new candidate vs evaluate an existing one" — directly applicable to the autonomous loop's expand-vs-evaluate decisions.

## Open questions / connections
- Extends Schmidhuber's Gödel Machine (2003) by replacing intractable formal-proof acceptance with a sampled clade statistic — at the cost of Assumption 1's terminal-only utility (no intermediate reward).
- The CMP estimator is biased by which agents the evaluation policy probes; the paper notes asynchronous execution introduces an "easy tasks finish first" bias that fades after ~50 evaluations — a caution for any clade-aggregated metric on partially-observed trees.
- Open: how to extend CMP-style credit assignment beyond binary success indicators (e.g. continuous arena scores with verifier drift, as in P14/P17).
- Could the "decouple expansion from evaluation; let unpromising arms be early-stopped" rule generalize to the council-dispatch protocol (early-stop personas whose questions aren't seeding findings)?
