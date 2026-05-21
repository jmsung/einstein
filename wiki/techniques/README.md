# techniques/

**HOW-TO** — concrete methods. Procedures, recipes, code patterns that the agent (or human) can apply.

Each technique page has frontmatter:

```yaml
---
type: technique
author: agent | human | hybrid
drafted: YYYY-MM-DD
related_concepts: [lp-duality.md, equioscillation.md, ...]
related_problems: [P2, P3, ...]
compute_profile: [local-cpu | local-mps | modal-gpu]
cost_estimate: "minutes / hours / GPU-hours"
hit_rate: "<n_top3> / <n_tried>"   # populated as we use it
---
```

Body structure:
1. **TL;DR** — what it does, when to use
2. **When to apply** — preconditions; signals you should reach for it
3. **Procedure** — numbered steps, code snippets where helpful
4. **Pitfalls** — known failure modes
5. **Compute profile** — local CPU / MPS / Modal recommendation
6. **References** — papers, repos, prior implementations

Distinct from `concepts/` — techniques are *how to do something*; concepts are *what something is*. Parallel tempering is a technique; sphere packing is a concept.
