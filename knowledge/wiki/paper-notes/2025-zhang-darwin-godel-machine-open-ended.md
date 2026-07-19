---
type: note
kind: paper-relevance
about: 2025-zhang-darwin-godel-machine-open-ended
canonical: ../../domains/ai-agents/source/2025-zhang-darwin-godel-machine-open-ended.md
---

# Relevance note — Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents

Canonical distillation: [`2025-zhang-darwin-godel-machine-open-ended.md`](../../domains/ai-agents/source/2025-zhang-darwin-godel-machine-open-ended.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card:

## Why it matters here
Directly informs the einstein autonomous-loop architecture: the cycle-discipline + self-improvement-loop rules already mirror DGM's archive-of-stepping-stones design, and DGM provides empirical validation that (a) archive-based open-ended exploration beats hill-climbing on a frozen meta-agent, and (b) self-modification compounds. Also a cautionary tale — DGM's node-114 objective-hacking incident parallels einstein's local-evaluator-drift problem (P9/P14/P17), reinforcing why triple-verify and hidden eval functions matter.

## Open questions / connections
- Can the open-ended exploration loop itself (parent selection, archive curation) be made self-modifiable without exponential compute blowup?
- How to design objectives robust to Goodhart-style hacking when the agent can read and edit its own eval scaffolding? (Hidden eval functions helped but didn't fully prevent it.)
- Extends ADAS (Hu et al. 2025, fixed meta-agent) and concurrent Robeyns et al. 2025 (single agent, no archive); leaves open whether DGM-style self-improvement transfers to non-coding objectives like math optimization (P1-P23).
- Connection to quality-diversity (MAP-Elites, Faldor 2025) — would behavioral-descriptor binning beat the current score $\times$ 1/children selection rule?
