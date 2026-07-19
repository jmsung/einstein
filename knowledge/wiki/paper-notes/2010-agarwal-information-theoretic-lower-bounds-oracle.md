---
type: note
kind: paper-relevance
about: 2010-agarwal-information-theoretic-lower-bounds-oracle
canonical: ../../domains/sci-math/source/2010-agarwal-information-theoretic-lower-bounds-oracle.md
---

# Relevance note — Information-Theoretic Lower Bounds on the Oracle Complexity of Stochastic Convex Optimization

Canonical distillation: [`2010-agarwal-information-theoretic-lower-bounds-oracle.md`](../../domains/sci-math/source/2010-agarwal-information-theoretic-lower-bounds-oracle.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — the Einstein problems are deterministic convex/SDP/LP relaxations, not stochastic optimization. The packing-set + Fano reduction technique could conceivably inform information-theoretic lower bounds on LP-bound iteration counts, but the stochastic-oracle setting is not the project's compute regime.

## Open questions / connections
- Extension of the strongly convex lower bound from $B_\infty(r)$ to arbitrary convex compact sets remains open.
- Memory-constrained and distributed-optimization oracle complexity left as future work.
- Connects to statistical minimax theory (Has'minskii, Yang–Barron, Yu's Assouad/Fano/Le Cam) — same packing+Fano machinery, different metric.
