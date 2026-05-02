---
type: home
author: human
drafted: 2026-05-02
status: seed
---

# einstein-wiki — math wisdom from solving Einstein Arena problems

This wiki is a math knowledge base built by human + agent through the practice of solving Einstein Arena problems. The arena is the gym; math wisdom is the goal. The wiki + agent code is the public artifact.

## Start here

- **[`problems/_inventory.md`](problems/_inventory.md)** — concept-coverage compass across 23 problems (the project's compass)
- **[`personas/_synthesis.md`](personas/_synthesis.md)** — the 12 stances drawn from the great mathematicians *(coming in Goal 4)*
- **[`index.md`](index.md)** — full catalog

## What's here

| Section | What lives there |
|---|---|
| [`concepts/`](concepts/) | WHAT-IS — durable mental models (LP duality, equioscillation, Cohn–Elkies bound, modular forms, basin rigidity, parameterization selection, …) |
| [`techniques/`](techniques/) | HOW-TO — concrete methods (parallel tempering, mpmath ulp polish, Remez exchange, SDP flag algebra, compute router, …) |
| [`personas/`](personas/) | Embodied mathematician perspectives — Gauss, Riemann, Tao, Conway, Cohn, Razborov, Polya, Hilbert, Grothendieck, Atiyah, Wiles, … and `_synthesis.md` (the 12 stances) |
| [`findings/`](findings/) | Specific Q→A pages with cites |
| [`problems/`](problems/) | One short index page per arena problem + the inventory matrix |
| [`questions/`](questions/) | Open math questions awaiting research |

## How knowledge gets in

```
external artifact → /wiki-ingest <url>
                       ├──→ ../raw/<type>/<stem>.<ext>     (gitignored, local)
                       └──→ ../source/<type>/<stem>.md     (in git, distilled)

questions / findings / concepts → /wiki-learn or /wiki-query --file-back
                                  → wiki/<category>/<slug>.md
                                    (with frontmatter author: agent|human|hybrid)
```

`raw/` is gitignored; `source/` is canonical. Wiki/ pages are synthesized — by either human OR agent, with mandatory attribution and the same quality bar regardless of author.

## Operating principles

1. **Math wisdom is the goal**, not arena rank. Submission is verification only.
2. **Failure is a finding** — every dead-end is a wiki entry with the why.
3. **Wiki-first lookup** — query the wiki before paraphrasing from training.
4. **Attribution is mandatory** — `author: agent | human | hybrid` on every page.
5. **Compute routing** before launching — local M5 / local MPS / Modal cloud, per workload.
6. **Triple-verify** every score before trusting (fast eval + exact reimpl + cross-check).
7. **No external posts** — the wiki is the publication channel.

See [`CLAUDE.md`](CLAUDE.md) for the full machine-readable contract; [`../.claude/rules/`](../.claude/rules/) for behavioral rules.

## Status

Pilot — reborn 2026-05-02 from `mb/wiki/`. Conventions provisional; will tighten as patterns clarify.
