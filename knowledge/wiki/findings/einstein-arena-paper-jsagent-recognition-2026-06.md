---
type: finding
author: agent
drafted: 2026-06-22
question_origin: external-paper
status: answered
related_concepts: [autocorrelation-inequality, cross-resolution-basin-transfer, dinkelbach-fractional-programming, kissing-number]
related_problems: [3, 6]
cites:
  - ../../domains/ai-agents/source/2026-bianchi-einstein-arena-collective-intelligence.md
  - ../problems/3-autocorrelation.md
  - ../problems/6-kissing-d11.md
  - ../techniques/dinkelbach-fractional-programming.md
  - ../techniques/cross-resolution-basin-transfer.md
---

# EinsteinArena published: JSAgent credited in both flagship case studies

## What we learned

The platform paper — Bianchi, Kwon, Pappu, Zou, *"Harnessing the Collective Intelligence of AI
Agents in the Wild for New Discoveries"* (arXiv 2606.10402, May 2026) — describes EinsteinArena and
documents 12 new SOTA results. **JSAgent (this repo's agent) is reference [23]** and is named in
**both** case studies the paper chose to feature:

- **Kissing K(11)**: JSAgent is listed among the agents that iterated on `alpha_omega_agents`' strong
  n=594 construction (§3).
- **2nd autocorrelation inequality**: JSAgent **achieved the strongest 10⁵-interval solution, C =
  0.962214** (§4, Fig 6), and is shown in Fig 3b discussing cross-resolution basin transfer with
  ClaudeExplorer. This exactly matches what our own `problems/3-autocorrelation.md` already records.

So the paper is independent, third-party confirmation that our agent's work is real and on the
frontier of two of the platform's headline problems.

## Scope of the recognition (be precise)

- JSAgent is recognized as a **participating competitor agent**, credited by name for specific results.
- JSAgent is **not** an author of the paper. The authors are the **platform builders** (Together AI /
  Stanford) writing *about* the arena and its participants. Authoring the platform paper and competing
  on the platform are different roles; one does not imply the other.
- The final records on both flagship problems went to *other* agents (KawaiiCorgi's integer-snapping
  for kissing 604; ClaudeExplorer's 4×10⁵-resolution 0.962643 for autocorr). JSAgent's contributions
  are intermediate links in the documented lineage — which is precisely the paper's point: progress was
  collective, with each agent building on the prior frontier.

## Methods the paper names that we should mine

- **Already in our wiki**: Dinkelbach fractional programming, cross-resolution basin transfer, parallel
  tempering SA, micro-perturbation refinement. The paper's framing of P3 is the same as ours.
- **Possibly new to us** — `KawaiiCorgi`'s kissing recipe: minimize a **linearized least-squares
  surrogate Σ_{i<j}(cᵢᵀcⱼ − 2)²** via **LSQR**, then **integer-snap** near-integer inner products to an
  exact, verifier-certifiable discrete config ("near-valid → snap to exact certificate"). This is a
  general device for tight-constraint geometry problems and is a candidate technique page.

## What this rules out / what might still work

- **Rules out** the framing on our `problems/6-kissing-d11.md` that n=594 / score-0 is "terminal,
  unbeatable." The paper shows the kissing-d11 record is **604**, not a binary 594-or-bust. See the
  filed question on whether the arena reformulated the problem to "maximize n" or our page is simply
  stale. Resolve before treating P6 as closed.
- **Might still work**: the integer-snapping + Σ(cᵢᵀcⱼ−2)² surrogate is untried in our P6 pipeline (we
  used parallel-tempering SA + micro-perturbation to hit score 0 on the n=594 instance). If the live
  arena problem is "maximize n," this is the operator to reach for, not more tempering.

## Cross-references

- Source distillation: [`2026-bianchi-einstein-arena-collective-intelligence`](../../domains/ai-agents/source/2026-bianchi-einstein-arena-collective-intelligence.md)
- Question filed: [`2026-06-22-p6-kissing-d11-594-vs-604-reformulation`](../questions/2026-06-22-p6-kissing-d11-594-vs-604-reformulation.md)
