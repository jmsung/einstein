# concepts/

**WHAT-IS** — durable mental models. Definitions, principles, and frames that recur across multiple problems.

A concept earns a page when:
- It appears in 2+ problems (cross-problem reuse signal), OR
- A finding is cited by 3+ other pages (promotion threshold)

Each concept page has frontmatter:

```yaml
---
type: concept
author: agent | human | hybrid
drafted: YYYY-MM-DD
related_problems: [P2, P3, P4, ...]
related_techniques: [parallel-tempering.md, ...]
related_findings: [...]
cites: [source/papers/..., wiki/findings/...]
---
```

Body structure:
1. **TL;DR** — 1-2 sentences
2. **What it is** — definition with notation
3. **When it applies** — problem family / structural conditions
4. **Why it works** — intuition, then formal statement
5. **Classic examples** — 1-3 with cites
6. **Related** — concepts/techniques cross-links

Distinct from `techniques/` — concepts are *what something is*; techniques are *how to do something*. Cohn–Elkies bound is a concept; LP cutting-plane warm-start is a technique.
