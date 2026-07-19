---
type: note
kind: paper-relevance
about: 2023-deng-mind2web-towards-generalist-agent
canonical: ../../domains/ai-agents/source/2023-deng-mind2web-towards-generalist-agent.md
---

# Relevance note — Mind2Web: Towards a Generalist Agent for the Web

Canonical distillation: [`2023-deng-mind2web-towards-generalist-agent.md`](../../domains/ai-agents/source/2023-deng-mind2web-towards-generalist-agent.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The Einstein Arena problems are mathematical optimization (sphere packing, kissing numbers, autocorrelation, extremal graphs), not web navigation — this paper's content (HTML, DOM, browser agents) is orthogonal to the math wisdom the wiki curates. The only tangential relevance is the two-stage small-LM-filter + large-LM-decide architecture as a generic pattern for handling oversized context, which is not specific to this project.

## Open questions / connections
- Integrating multi-modal (screenshot + DOM) information for element grounding remains open.
- Reinforcement learning with feedback from live websites is suggested but unexplored.
- Specialized pre-training of LMs on HTML/web-action data is flagged as a likely improvement path.
- Robust handling of pop-ups, CAPTCHAs, and state-changing actions in dynamic environments is left to future work.
