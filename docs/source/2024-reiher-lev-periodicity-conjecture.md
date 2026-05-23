---
type: source
kind: paper
title: On Lev's periodicity conjecture
authors: Christian Reiher
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2408.15174v2
source_local: ../raw/2024-reiher-lev-periodicity-conjecture.pdf
topic: general-knowledge
cites: 
---

# On Lev's periodicity conjecture

**Authors:** Christian Reiher  ·  **Year:** 2024  ·  **Source:** http://arxiv.org/abs/2408.15174v2

## One-line
Resolves Lev's 20-year-old conjecture by classifying all sum-free subsets of $\mathbb{F}_3^n$ with density above $1/6$, pinning down the maximal aperiodic sum-free set size at $\tfrac{1}{2}(3^{n-1}+1)$.

## Key claim
A subset $A \subseteq V$ of a finite ternary vector space with $|A| > \tfrac{1}{6}|V|$ is maximal sum-free **iff** it is *primitive* (a recursively defined family built from hyperplane-halves $W$ and primitive subsets $X \subseteq C(U)$); consequently every aperiodic maximal sum-free $A \subseteq \mathbb{F}_3^n$ (with $n \neq 2$) satisfies $|A| \leq \tfrac{1}{2}(3^{n-1}+1)$, and this is tight.

## Method
Induction on $\dim V$ combined with Kneser's addition theorem (used via Lemma 3.3: if $2|A|+2|B|+|C| > 2|G|$ and $(A+B)\cap C = \emptyset$, then $A+B$ is a union of cosets of some subgroup $K$). The proof factors through a recursive structural definition of "primitive" sets, a quadruple-sum lemma ($0 \notin 4A$ for dense sum-free $A$, established via the $n=4$ base case in $\mathbb{F}_3^4$), and a "$5/6$-density inside an affine subspace" extraction (Lemma 2.7) that forces enough structure for Propositions 3.4/3.9 to apply.

## Result
Theorem 1.4: maximal sum-free $\Leftrightarrow$ primitive whenever $|A| > |V|/6$. Lemma 1.3 gives the cardinality formula $|A| = \tfrac{1}{6}(|V| + 3|\mathrm{Sym}(A)|)$ for primitive $A$, so aperiodic ($\mathrm{Sym}(A)=\{0\}$) forces $|A| = \tfrac{1}{2}(3^{n-1}+1)$. Lev's optimal construction (using $X = -U$ with $\dim U = 0$) is shown to be unique up to the recursive structure. Concluding remarks tabulate $t(\mathbb{F}_p^n)$ for $p=2,3$ and $p \equiv 1,2 \pmod 3$ with $p \geq 11$, leaving $p=5$ for $n \geq 4$ as the only fully open case.

## Why it matters here
General background on additive combinatorics in ternary spaces — directly informs cap-set–adjacent reasoning and the use of Kneser's theorem as a structural tool; the recursive "primitive set" construction is a clean template for *certified-maximal* extremal configurations relevant to discrete-combinatorics arena problems. No direct arena-problem tie identified, but the Kneser-via-Lemma-3.3 pattern and the $0 \notin 4A$ density lemma are reusable for sum/difference-set arguments.

## Open questions / connections
- $t(\mathbb{F}_5^n)$ for $n \geq 4$ — no conjecture exists; the analogous classification is wide open.
- Extends Davydov–Tombak (1989) on $\mathbb{F}_2^n$ to the ternary regime; the recursive primitive-set definition may generalize to $\mathbb{F}_p^n$ for other primes.
- The $0 \notin 4A$ phenomenon (Lemma 2.3 / Proposition 4.5) for dense sum-free sets — does it extend to higher iterated sums in other groups, and is there a Fourier-analytic proof avoiding the $n=4$ computer-style base case?

## Key terms
sum-free sets, Lev periodicity conjecture, ternary vector spaces, $\mathbb{F}_3^n$, maximal sum-free, aperiodic, primitive sets, Kneser theorem, additive combinatorics, hyperplane covering, symmetry group, Davydov-Tombak, cap sets, quadruple sums
