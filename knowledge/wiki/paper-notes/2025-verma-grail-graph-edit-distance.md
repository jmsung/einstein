---
type: note
kind: paper-relevance
about: 2025-verma-grail-graph-edit-distance
canonical: ../../domains/ai-agents/source/2025-verma-grail-graph-edit-distance.md
---

# Relevance note — GRAIL: Graph Edit Distance and Node Alignment Using LLM-Generated Code

Canonical distillation: [`2025-verma-grail-graph-edit-distance.md`](../../domains/ai-agents/source/2025-verma-grail-graph-edit-distance.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Closest relevance is *methodological*: this is a concrete, recent template for **LLM-driven program search as combinatorial-optimization heuristic discovery** — the same FunSearch substrate the einstein autonomous-loop agent's design implicitly inherits, and a worked example of "evolve a *bounded* objective so you don't need ground truth", which mirrors the project's triple-verify upper-bound-as-loss stance for hard problems.

## Open questions / connections
- Extends FunSearch (Romera-Paredes et al. 2024 *Nature*) from cap-sets/bin-packing to a labeled-graph matching problem — does the same recipe transfer to sphere-packing / kissing / autocorrelation arena problems where an admissible upper bound exists?
- The submodularity proof for "min over a pool of upper-bound heuristics" is reusable: any arena problem where each candidate solution is a verified upper bound (or lower bound) could plug into the same greedy program-portfolio framework.
- Open: how to discover programs when no closed-form upper bound is available, and how to add human-in-the-loop refinement of LLM-emitted code (raised in the conclusion).
