---
type: note
kind: paper-relevance
about: 2025-cai-training-free-group-relative-policy
canonical: ../../domains/ai-agents/source/2025-cai-training-free-group-relative-policy.md
---

# Relevance note — Training-Free Group Relative Policy Optimization

Canonical distillation: [`2025-cai-training-free-group-relative-policy.md`](../../domains/ai-agents/source/2025-cai-training-free-group-relative-policy.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
Directly relevant to the self-improvement-loop and council-dispatch rules — the paper formalizes "learned experiential knowledge as token prior" with an explicit ops grammar (Add/Delete/Modify/Keep), which is essentially what `knowledge/wiki/findings/` + experience selection does manually here. Suggests a concrete mechanism to operationalize the autonomous-loop branch: each cycle's failure/success findings become an indexed experience library that conditions the next council dispatch, with semantic advantage replacing the missing scalar reward signal on hard problems.

## Open questions / connections
- Does semantic-advantage distillation work when there is *no* ground truth (their no-GT variant kept gains) — directly applicable to Einstein Arena problems where verifier drift makes scalar reward unreliable; aligns with triple-verify rule.
- Library curation: at 48 experiences after 100 samples, how does retrieval/ranking scale to wiki-sized $|E|$? Paper doesn't address; the wiki's qmd-based retrieval would be the analog.
- Capability prerequisite: QwQ-32B actually *regressed* on web tasks with the same recipe (27.5→25.5%) — suggests the method only compounds for sufficiently strong base models, with implications for which Einstein cycles benefit.
- Connects to Self-Refine (Madaan 2023), Reflexion (Shinn 2023), Agent KB (Tang 2025); extends them by tying experience updates to *group-relative* semantic comparison rather than single-trajectory reflection.
