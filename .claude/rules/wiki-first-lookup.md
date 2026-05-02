# Wiki-first lookup for in-scope claims

When answering a math/optimizer/arena question whose subject is plausibly already in this wiki, **query the wiki before paraphrasing from training**. Cite what you find. If the wiki has nothing useful, say so explicitly before falling back.

**Why:** This wiki is the project's source of truth for math wisdom — concepts, techniques, personas, findings. Skipping it costs precision (the wiki distillation has the right framing for *this* problem family) and feeds drift back into the repo via agents that re-derive the same answer differently every session. The whole point of the self-improvement loop is that the wiki *compounds* — bypassing it breaks compounding.

**How to apply:**

In-scope subjects (query first):

- Math concepts: LP duality, equioscillation, Cohn–Elkies, modular forms, Sidon sets, basin rigidity, parameterization selection, …
- Optimizer techniques: parallel tempering, mpmath polish, Remez exchange, SDP flag algebra, basin hopping, …
- Mathematician personas and their stances
- Per-problem prior work: any of the 23 arena problems
- Cross-problem findings: what we learned from previous solves
- Tools: HiGHS LP, Modal, MPS, qmd

Lookup paths:

```bash
qmd query "<question>" -c einstein-wiki -n 5         # synthesis pages
qmd query "<question>" -c einstein-wiki-source -n 5  # raw distillations
# qmd doesn't multi-collection — query each in turn
```

Or, when faster: `grep`/`find` against `wiki/` and `source/`, or read a specific path the user references.

After the lookup:

- **Hit found:** answer from it, cite the path (e.g. `wiki/concepts/equioscillation.md`). Don't paraphrase a paper's abstract when the distillation is already the better framing.
- **Empty or low relevance:** say "the wiki has nothing on this" explicitly before falling back to training. Offer to ingest via `/wiki-ingest` if the topic warrants it. **File the question** in `wiki/questions/` per the [self-improvement-loop](self-improvement-loop.md).
- **Conflict with training:** trust the wiki for "what is this thing in our context"; trust training for general background. The wiki was made deliberately; training was scraped.

Out-of-scope subjects (general programming, language syntax, common ML terms) — answer from training as usual.

**Triggering pattern:** every time the agent is about to answer a math question or recommend a technique, the FIRST tool call should be a wiki search, not a code or training-data answer.
