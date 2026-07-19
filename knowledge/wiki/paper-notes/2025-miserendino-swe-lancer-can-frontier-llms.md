---
type: note
kind: paper-relevance
about: 2025-miserendino-swe-lancer-can-frontier-llms
canonical: ../../domains/ai-agents/source/2025-miserendino-swe-lancer-can-frontier-llms.md
---

# Relevance note — SWE-Lancer: Can Frontier LLMs Earn $1 Million from Real-World Freelance Software Engineering?

Canonical distillation: [`2025-miserendino-swe-lancer-can-frontier-llms.md`](../../domains/ai-agents/source/2025-miserendino-swe-lancer-can-frontier-llms.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — this is an SWE-agent capabilities benchmark, not a math-optimization or extremal-combinatorics paper. Indirectly informs the einstein agent's own self-improvement loop discipline: triple-verified end-to-end tests as the right grading layer (echoes the repo's own [[triple-verify]] axiom and verifier-mismatch findings on P9/P14/P17), and the empirical lesson that "localizes fast, root-causes poorly" is a known agent failure mode worth watching in council-dispatch synthesis.

## Open questions / connections
- Does pass@k scaling on SWE tasks transfer to math-optimization tasks where verification is cheap but search space is continuous? (Relevant to test-time-compute routing for arena problems.)
- Extends SWE-Bench / SWE-Bench Verified / SWE-Bench Multimodal to commercial, full-stack, manager-level eval; leaves open: how to evaluate "zero-to-one" greenfield SWE work and infrastructure/DevOps tasks (underrepresented in Expensify).
- Grader-hacking robustness: E2E tests resist unit-test hacks (Appendix A7), but no evidence yet on whether agents trained against E2E tests would learn to game Playwright traces themselves.
