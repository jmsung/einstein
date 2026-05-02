# Council dispatch — pick personas; each writes a QUESTION

When starting a hard problem (recon phase), dispatch a council of mathematician personas. The council's job is **not to solve the problem** — it's to write the right questions.

**Why:** A persona producing "the answer" is just generating plausible markdown. A persona producing "the question Tao would ask if he were stuck on this" is genuinely useful — it forces the gap-detect loop. Questions are the artifact even if the answer takes longer.

**How to apply:**

1. **Parse problem category** from `mb/tracking/<problem>/strategy.md` and `wiki/problems/_inventory.md`. Categories: sphere_packing, kissing_number, autocorrelation, discrete_geometry, packing, extremal_graph, sieve_theory, uncertainty, combinatorics, …

2. **Read each persona's wiki page** (`wiki/personas/<name>.md`) BEFORE dispatching. The page is the seed — without reading it, you're just pattern-matching on the name.

3. **Spawn 3–5 personas in parallel** as research subagents, seeded with:
   - Problem statement
   - Top-3 SOTA solutions (downloaded via arena API)
   - The persona's wiki page (stance + heuristics + when-stuck-I-ask)
   - Existing relevant findings (from `wiki/findings/`)
   - Instruction: **write 2–3 questions, not a solution**

4. **Check specialist triggers** (in each persona's frontmatter): if the problem matches the persona's `trigger.categories`, also dispatch them.

5. **Each persona's output** lands in `wiki/questions/<YYYY-MM-DD>-<problem>-<persona>-<slug>.md` with frontmatter `author: agent`, `asked_by: <persona>`, `status: open`.

6. **Synthesize**: read all the questions; group by approach; rank by expected impact. Pick the top 3 to research first via [self-improvement-loop](self-improvement-loop.md).

7. **Wall-clock budget**: 10–15 min per persona. If any reports a high-confidence breakthrough candidate, escalate to deep research immediately (do not wait for full council to return).

**Default core council** (always runs): Gauss, Riemann, Tao, Conway, Euler, Poincaré, Erdős, Noether, Cohn, Razborov.

**Bench** (triggered): Viazovska (sphere_packing, kissing), Szemerédi (regularity), Turán (graph_density), Ramanujan (modular_forms, hidden_structure), Archimedes (discrete_geometry, packing), Hilbert (functional_analysis, autocorrelation, uncertainty).

**Meta-coaches** (always available, dispatched when *stuck on protocol* not *stuck on math*): Polya (heuristics), Hadamard (inverse framing), Grothendieck (right framework), Atiyah (cross-field), Wiles (depth/persistence).

**Cost budget**: ~$X tokens per problem for the full council. Run ONCE per problem during recon, not on every iteration. Re-dispatch only if the problem category shifts or new evidence arrives.

See also: [wiki/personas/](../../wiki/personas/), [self-improvement-loop](self-improvement-loop.md), [ask-the-question-first](ask-the-question-first.md).
