---
type: note
kind: paper-relevance
about: 2025-zhang-position-intelligent-science-laboratory
canonical: ../../domains/ai-agents/source/2025-zhang-position-intelligent-science-laboratory.md
---

# Relevance note — Position: Intelligent Science Laboratory Requires the Integration of Cognitive and Embodied AI

Canonical distillation: [`2025-zhang-position-intelligent-science-laboratory.md`](../../domains/ai-agents/source/2025-zhang-position-intelligent-science-laboratory.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The Einstein Arena agent is a purely *cognitive* loop on math problems (no wet-lab, no embodiment), so the embodied layer is irrelevant — but the paper's framing of a meta-agent that auto-composes workflows from modular agents and its closed-loop "hypothesis → execute → feedback → update" structure parallel the einstein self-improvement-loop and council-dispatch rules.

## Open questions / connections
- Does the meta-agent's "automatic workflow design" (vs fixed templates) translate to council-dispatch / persona-selection in a math-solving agent — i.e., should persona selection itself be learned rather than hard-coded?
- MCP-style abstraction for wrapping proprietary models (AlphaFold cited as canonical example) — analog for einstein would be wrapping solvers (HiGHS LP, mpmath, CMA-ES) behind a unified call interface.
- Four-level autonomy taxonomy (L0–L3) as a possible self-assessment frame for the einstein cycle-log: where on L0–L3 is the current loop, and what specifically gates L2 → L3?
