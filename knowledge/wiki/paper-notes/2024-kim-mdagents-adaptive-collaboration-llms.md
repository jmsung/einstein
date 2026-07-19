---
type: note
kind: paper-relevance
about: 2024-kim-mdagents-adaptive-collaboration-llms
canonical: ../../domains/ai-agents/source/2024-kim-mdagents-adaptive-collaboration-llms.md
---

# Relevance note — MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making

Canonical distillation: [`2024-kim-mdagents-adaptive-collaboration-llms.md`](../../domains/ai-agents/source/2024-kim-mdagents-adaptive-collaboration-llms.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The framework's structure — complexity triage → recruit specialist council → multi-round consensus with moderator → final synthesis — is directly analogous to einstein's council-dispatch + math-solving-protocol rules, and could inform how the autonomous loop adaptively sizes its persona council per problem complexity.

## Open questions / connections
- Can a complexity classifier reliably triage Einstein Arena problems by category (sphere_packing vs combinatorics vs uncertainty) the way moderator triages MDM cases?
- Moderator + external-knowledge contributed +11.8% — is the analogous lever for math personas the wiki-first retrieval step, and is it the dominant gain there too?
- Static vs flexible conversation patterns (Table 1) — current council-dispatch is static (3-5 personas, one shot); does adding rounds + early-stopping like MDT help on hard arena problems?
