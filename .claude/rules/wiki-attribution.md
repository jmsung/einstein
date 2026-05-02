# Wiki attribution — either author may write; attribution is mandatory

Either human or agent can author wiki pages. The honesty layer is **mandatory frontmatter attribution** on every page. The same quality bar applies regardless of author.

**Why:** A self-improving agent must actually contribute to its memory. Restricting authorship to humans defeats the experiment. But agent-authored content can drift, hallucinate, or low-quality the wiki — so attribution makes the experiment honest. The cycle log measures self-improvement by tracking agent-authored vs human-authored counts. If every page is human-authored, the agent didn't improve. If every page is agent-authored without human review, the human is asleep at the wheel. Healthy mix is the signal.

**How to apply:**

Every page in `wiki/concepts/`, `wiki/techniques/`, `wiki/findings/`, `wiki/personas/`, `wiki/problems/`, `wiki/questions/` MUST have frontmatter:

```yaml
---
type: concept | technique | finding | persona | problem | question
author: agent | human | hybrid
drafted: YYYY-MM-DD
confirmed_by: human         # OPTIONAL — set after human review of an agent-drafted page
cites: [<paths>]            # mandatory if making non-trivial claims
---
```

**Author values:**
- `agent` — drafted by Claude or any subagent in a session, no human edits beyond approval
- `human` — drafted by Jongmin, no agent contribution beyond search/lookup
- `hybrid` — agent-drafted + human-edited, OR human-drafted + agent-extended substantively

**Quality bar (same for all authors):**
1. **Grounded** — claims trace to `source/` or established literature, not "training said so"
2. **Cited** — specific files / URLs / commit hashes, not "as discussed in some paper"
3. **Verifiable** — code can be run, math can be checked, API can be queried
4. **No filler** — every paragraph earns its place; if removing it doesn't lose information, remove it

**Promotion (human-gated):**
- A finding cited by 3+ other pages OR invoked across 3+ problems is a candidate for promotion to `concepts/`
- The agent may *propose* promotion (annotate the finding with `promotion_proposed: true`) but cannot promote
- Human review for promotion: read the finding, read the proposed concept page, decide

**Pages the agent may NOT write directly (without /wiki-learn or /wiki-query --file-back):**
- `wiki/home.md` — narrative front door, human-curated
- `wiki/personas/_synthesis.md` — meta-page, human-curated
- `mb/notes/*` — personal jots, human-only
- `mb/log.md` — private ops history, human-only

The agent CAN write all other wiki pages directly with mandatory attribution. The honesty layer is the receipt.

**Triggering pattern:** every wiki/ file write goes through this attribution check. Frontmatter without `author:` is incomplete and should be flagged.

See also: [self-improvement-loop](self-improvement-loop.md), [wiki/CLAUDE.md](../../wiki/CLAUDE.md), [agent-stance](agent-stance.md) (honest about lack of info).
