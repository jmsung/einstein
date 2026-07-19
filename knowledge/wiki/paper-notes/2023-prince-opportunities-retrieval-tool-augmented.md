---
type: note
kind: paper-relevance
about: 2023-prince-opportunities-retrieval-tool-augmented
canonical: ../../domains/ai-agents/source/2023-prince-opportunities-retrieval-tool-augmented.md
---

# Relevance note — Opportunities for retrieval and tool augmented large language models in scientific facilities

Canonical distillation: [`2023-prince-opportunities-retrieval-tool-augmented.md`](../../domains/ai-agents/source/2023-prince-opportunities-retrieval-tool-augmented.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The retrieval-augmented + tool-calling architecture (vector store of chunked docs, top-N=4 retrieval, ReAct tool dispatch) is structurally the same pattern as this repo's wiki-first lookup + council dispatch + skill-library loop — useful as an external reference for the autonomous-loop branch's design.

## Open questions / connections
- Can fine-tuned open-source models (Vicuna successors) be made reliable enough to emit valid JSON for structured tool calls, closing the gap with GPT-3.5?
- How does retrieval quality scale when the document store contains decades of e-logs rather than curated docs — does top-N=4 chunking still suffice?
- What evaluation protocol distinguishes "relevant + hallucinated" from "irrelevant + truthful" responses systematically (current scoring is human-graded)?
