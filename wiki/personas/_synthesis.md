---
type: persona
author: agent
drafted: 2026-05-02
cites:
  - wiki/personas/polya.md
  - wiki/personas/tao.md
  - wiki/personas/hilbert.md
  - wiki/personas/grothendieck.md
  - wiki/personas/hadamard.md
  - wiki/personas/erdos.md
  - wiki/personas/cohn.md
  - wiki/personas/noether.md
  - wiki/personas/riemann.md
  - wiki/personas/gauss.md
  - wiki/personas/euler.md
  - wiki/personas/ramanujan.md
  - wiki/personas/atiyah.md
  - wiki/personas/archimedes.md
---

# The 12 Stances — Synthesis

Twenty-one mathematicians; one set of stances. Read the persona pages for
the embodied voice; this page is the cross-cut. These are the *moves* the
council reaches for, abstracted from any one mathematician.

The stances are roughly ordered by where they belong in the math-solving
protocol: stances 1–2 belong to **Understand**, 3–9 to **Plan / Carry
out**, 10–11 to **Look back**, 12 is structural across all steps.

---

## 1. Restate the problem until you own it (Polya)

Most "stuck" is "haven't really read the problem yet." The first move on
every hard problem is to restate it in your own words: name the unknown,
list the data, list the conditions. If you can't restate it without the
original statement in front of you, you don't own it. Polya's *Understand*
step. The act of restating often resolves the problem before any
optimizer runs.

**Personas embodying this**: Polya (primary). All the meta-coaches
(Hadamard, Grothendieck, Wiles) implicitly. Tao writes blog posts as
exercises in restatement.

---

## 2. Specialize first (Polya, Tao)

Try n=2, 3, 4 by hand before launching any optimizer. Patterns visible at
n=4 propagate to general structure; patterns invisible at n=4 may not
exist at n=594 either. Specialization is fast, free, and almost always
generates an insight that survives. The agent's most-skipped step before
launching compute.

**Personas embodying this**: Polya, Tao, Gauss (small-case tabulation),
Euler (count exhaustively at small n), Archimedes (draw the picture).

---

## 3. Generalize second (Hilbert, Grothendieck)

After specialization yields a pattern, ask whether the right framework
makes it obvious. Hilbert axiomatizes — the cleanest statement is the
right statement. Grothendieck rises the sea — find the abstraction in
which the problem dissolves. Generalization comes *after* specialization,
not before; premature generalization produces hollow theorems.

**Personas embodying this**: Hilbert (axiomatization), Grothendieck
(framework change), Atiyah (right category).

---

## 4. Inverse framing (Hadamard, Erdős)

When forward search saturates, pretend the answer exists and reason about
its properties. What symmetries must it have? What scaling? What
asymptotics? Reverse-engineering constrains the candidate space. Erdős
does this probabilistically: pretend a random object solves the problem,
compute the expectation, derandomize. Hadamard does it analytically:
pretend the extremizer exists, list its properties, recognize it.

**Personas embodying this**: Hadamard (primary, *Psychology of
Invention*), Erdős (probabilistic existence), Cohn (LP dual: pretend the
upper bound is achievable, certificate it).

---

## 5. Dual reformulation (Cohn–Elkies, von Neumann)

Every primal problem has a dual. Sphere packing has the Cohn-Elkies LP
dual; max-flow has min-cut; the original primal often hides the structure
that the dual makes obvious. The dual gives the upper bound; the primal
gives the lower bound; optimality is when they meet. When stuck on the
primal, write the dual.

**Personas embodying this**: Cohn (LP duality), Hilbert (Rayleigh
quotient as eigenvalue dual), Razborov (flag-algebra SDP dual), Riemann
(potential-theoretic dual via complex analysis).

---

## 6. Symmetry / invariant first (Klein, Noether, Weyl)

Identify the symmetry group before optimizing. The optimum often lives in
a G-fixed subspace, or in a fundamental domain modulo G. Quotient out
redundant gauge (translation, rotation, scaling); restrict to the
G-invariant subspace if the optimum is forced to be symmetric. Noether's
theorem links continuous symmetry to conserved quantities; Erlangen-style
classification by invariants applies to discrete cases.

**Personas embodying this**: Noether (primary), Conway (lattice
automorphism groups), Archimedes (container symmetry), Riemann (modular
group symmetry).

---

## 7. Compute aggressively, by hand and tabulation (Gauss, Euler, Ramanujan)

Compute small cases prolifically. Tabulate. The pattern emerges from the
data, not from contemplation. Gauss wrote the table of primes by hand and
saw the asymptotic; Euler computed thousands of partition values; Ramanujan
filled notebooks with q-series identities recognized by stare-and-shape.
The agent's analog: triple-verify scores, log every experiment, build
OEIS-style sequence tables for SOTA values.

**Personas embodying this**: Gauss, Euler, Ramanujan (all three
prolifically); Conway (catalog as method).

---

## 8. Cross-pollinate fields (Atiyah)

When one field is stuck, translate to another. Algebra ↔ analysis ↔
geometry ↔ physics. The Atiyah-Singer index theorem is the prototype: an
analytic count equals a topological count. Combinatorial problems often
yield to harmonic analysis; analytic problems to representation theory;
discrete-geometry problems to algebraic constructions.

**Personas embodying this**: Atiyah (primary), Tao (additive
combinatorics × harmonic analysis), Razborov (extremal combinatorics ×
SDP), Cohn (sphere packing × modular forms).

---

## 9. Identify the obstruction (Tao, Atiyah)

Name the *single phenomenon* preventing the bound from improving. Not
"the optimizer keeps returning the same value" — that's a symptom. The
obstruction is the underlying structural reason. Once named, the
obstruction is half-solved: the agent can either remove it (parameterization
change) or prove it's load-bearing (lower bound). Without naming, every
"failure" looks the same.

**Personas embodying this**: Tao (primary, "what is the obstruction?"),
Atiyah (cross-field obstructions), Riemann (singularity structure as
obstruction).

---

## 10. Two minds, dialectical (Tao)

Run two minds in parallel: one looking for proofs, one looking for
counterexamples. One arguing the bound holds, one arguing it doesn't.
Dialectic is more productive than monologue — the bound proof and the
counterexample search inform each other. When one stalls, the other
provides a new angle. This is also Tao's blog method: write half-arguments
publicly so the absence of a counterexample is itself evidence.

**Personas embodying this**: Tao (primary), Polya (proof and
counter-search loop), Erdős (probabilistic upper bound vs explicit
lower bound).

---

## 11. Look back (Polya — most skipped)

After any result — success or failure — ask: what was the key idea? Does
it generalize? Where else does this apply? Update or create the
corresponding wiki concept. *This is the only step that compounds.*
Without Look Back, every solve produces a single answer; with Look Back,
each solve produces a reusable concept that strengthens the next solve.
The single most-skipped step in research practice.

**Personas embodying this**: Polya (primary, *How to Solve It* step 4),
Wiles (descent ascent: after the breakthrough, verify each layer).
Riemann's notebooks are the historical record of this practice.

---

## 12. Failure is a finding (Riemann's notebooks, Tao's blog)

Every dead end becomes a `findings/dead-end-<slug>.md` with the *why*.
Not "it didn't improve" — that's a symptom — but the structural reason.
Tomorrow's breakthrough sits on yesterday's articulated obstruction.
Riemann's posthumous notebooks are full of failed approaches *with
reasons*; Tao's blog institutionalizes the practice; Wiles's seven-year
silence was layered with failure logs.

**Personas embodying this**: Riemann (notebooks), Tao (blog), Wiles
(descent strategy with explicit failure annotations), Hadamard
(*Psychology of Invention* documents others' failures), Polya (*Look
back* step generates failure findings as a byproduct).

---

## How the protocol invokes the stances

The math-solving-protocol (`.claude/rules/math-solving-protocol.md`)
runs these stances in roughly this order, but the council dispatch step
(step 3) selects which mathematician's voice to load *for which stance*
based on the problem category. The stances are universal; the personas
are domain-specialized embodiments.

A typical hard-problem session invokes:
- Stance 1 (restate) — always, by Polya
- Stance 2 (specialize) — always, by Polya / Tao / Gauss
- Stance 6 (symmetry) — always, by Noether / Archimedes
- Stance 9 (obstruction) — once stuck, by Tao
- Stances 4 / 5 / 8 (inverse / dual / cross-field) — when stuck on math
- Stances 3 / 11 (generalize / look back) — after the breakthrough
- Stance 12 (failure log) — at every dead end

The 5 meta-coach personas (Polya, Hadamard, Grothendieck, Atiyah, Wiles)
are dispatched for stance-level questions; the 16 domain personas are
dispatched for math-domain questions. The synthesis is here so the agent
can ask "which stance am I in?" before asking "which persona do I
load?".

*Last updated: 2026-05-02*
