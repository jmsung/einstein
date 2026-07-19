---
type: note
kind: paper-relevance
about: 2026-ye-evaluation-driven-scaling-scientific-discovery
canonical: ../../domains/ai-agents/source/2026-ye-evaluation-driven-scaling-scientific-discovery.md
---

# Relevance note — Evaluation-driven Scaling for Scientific Discovery

Canonical distillation: [`2026-ye-evaluation-driven-scaling-scientific-discovery.md`](../../domains/ai-agents/source/2026-ye-evaluation-driven-scaling-scientific-discovery.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
Directly relevant to einstein arena work: Erdős minimum overlap, autocorrelation inequalities (AC2/AC3), and circle packing in a unit square are sister problems to several arena items (P15/P16 equioscillation/autocorrelation family; packing problems). The discovered programmatic strategies — FFT-conv + L-BFGS-B for autocorrelation, DCT parameterization, AP-backbone + fringe corrections, coarse-to-fine resolution scaling, multi-restart simulated annealing with non-overlapping run distributions — are concrete techniques the agent's optimizer should consider. Also frames a general meta-loop ($C\times L\times K$) that maps onto the agent's own self-improvement loop.

## Open questions / connections
- What is the exact construction (AP backbone + fringe correction pattern) that achieves Erdős $0.380856$, and can it be reproduced/extended to neighboring extremal problems?
- Does the DCT-parameterized AC3 strategy outperform the wiki's current parameterizations on einstein's autocorrelation-family problems?
- Can the $C\times L\times K$ budgeting be ported to the council-dispatch / wiki-loop — i.e. is global width $C$ better spent on persona diversity vs. seed diversity?
- Reward-hacking analysis (§4.3) is directly relevant to einstein's local-evaluator drift findings (P9/P14/P17) — does their hacking detection generalize?
