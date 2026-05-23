---
type: source
kind: paper
title: Refuting conjectures in extremal combinatorics via linear programming
authors: A. Wagner
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1903.05495
source_local: ../raw/2019-wagner-refuting-conjectures-extremal-combinatorics.pdf
topic: general-knowledge
cites:
---

# Refuting conjectures in extremal combinatorics via linear programming

**Authors:** A. Wagner  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1903.05495

## One-line
A tutorial-style paper showing that off-the-shelf integer-linear-programming solvers, applied to small instances, refute (or verify) a dozen open conjectures in extremal set theory and combinatorics.

## Key claim
Many extremal-combinatorics conjectures admit a direct 0/1-IP encoding (indicator $x_A \in \{0,1\}$ per set, linear constraints per forbidden pattern); solving small cases with Gurobi yields explicit counterexamples to conjectures of Frankl, Huang, Katona, Frankl–Tokushige, Aharoni–Howard, and improvements to constructions of De Silva et al. and Anstee.

## Method
Encode each set-system property as linear 0/1 constraints: antichain ($x_A+x_B\le1$ for $A\subset B$), intersecting ($x_A+x_B\le1$ for disjoint pairs), $k$-chain-free ($\sum x_{A_i}\le k-1$ along chains), diameter ($x_A+x_B\le1$ if $|A\triangle B|>d$), forbidden trace/configuration ($\sum_{i\in S} x_i \le |S|-1$), no-$s$-pairwise-disjoint ($\sum_{i=1}^s x_{A_i}\le s-1$), rainbow-matching-free (per-edge indicators with disjointness sums). Solve with Gurobi on small $n$; generalize the LP-produced extremal example into an analytic construction.

## Result
Concrete refutations: $n=6,d=5,\ell=2$ family of size 26 beats Frankl's $\binom{n}{\lfloor d/2\rfloor}+\binom{n}{1}=21$ (Conj. 3.2); $n=7,k=3$ intersecting family with diversity $\rho=5>\binom{n-3}{k-2}=4$ refutes Conj. 3.3; Fano-plane-based up-closure gives diversity 23 (vs 22 conjectured) for $n=7$, 97 vs 93 for $n=9$, 197 vs 193 for $n=10$ (Huang's Conj. 3.4/3.5); $k(9,4)\ge481>4k(7,4)=480$ refutes Frankl–Tokushige; bipartite triple $F_1,F_2,F_3$ on 6 vertices with $\Delta\le2$, $|F_i|>(k-1)d$, no rainbow matching refutes Aharoni–Howard (Conj. 3.20); $\mathrm{ex}(K_{n,n,n,n},kK_3)\ge 4n^2+(k-1)n$ beats De Silva et al.; $\mathrm{forb}(m,A)\ge \tfrac{11}{6}\binom{m}{2}+\binom{m}{1}+1$ via Wilson-design 4-sets refutes Anstee's Problem 3.13; explicit $(11,5,3)$ Ihringer–Kupavskii Hoffman-bound equality family.

## Why it matters here
Direct methodological transfer to the Einstein Arena: many arena problems (P19-style intersecting families, Sidon-set / autocorrelation, kissing-style packings, extremal-graph instances) admit 0/1-IP encodings whose small-$n$ solutions either rule out a conjectured optimum or hand back an explicit basin to generalize — i.e., LP/IP is a council-grade "sanity check" tool that complements continuous optimizers and equioscillation diagnostics. Pairs with `wiki/techniques/compute-router.md` (LP on local CPU is the "best home" entry).

## Open questions / connections
- For which graphs $G$ does Falgas-Ravry's vertex-transitive antichain conjecture / Erdős $k$-chain-free analog hold? IP scales to $n\le 24$ for $P_n$.
- Tightness of the diversity constructions for $n\ge 11$ (LP becomes infeasible on commodity hardware).
- Yuzvinsky/Frankl antipodal-distance-$\ge n+2$ removal problem: middle layer optimal for $n\le 7$; open for general $n$.
- Sharpness of the $\tfrac{11}{6}\binom{m}{2}$ forbidden-trace bound; better Wilson-style designs?
- General principle: LP-solver-found counterexample as the seed an analytic generalization completes (recurring pattern across 8 of the disproven conjectures).

## Key terms
integer programming, LP solver, Gurobi, extremal set theory, intersecting families, antichain, Sperner theorem, diversity, Erdős–Ko–Rado, Hilton–Milner, Frankl conjecture, Huang diversity, Kleitman matching, forbidden configuration, VC dimension, Steiner triple system, Hoffman bound, rainbow matching, Turán-type multipartite, Aharoni–Howard, Falgas-Ravry, Katona, Wilson designs
