---
type: source
kind: paper
title: OpenAI gpt-5 disproves a discrete-geometry conjecture (unit-distance bound)
authors: OpenAI
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: openai-release
source_url: https://openai.com/index/model-disproves-discrete-geometry-conjecture/
source_local: ../raw/2026-openai-gpt5-unit-distance-disproof.pdf
topic: agentic-harness
cites: 
---

# OpenAI gpt-5 disproves a discrete-geometry conjecture (unit-distance bound)

**Authors:** OpenAI  ·  **Year:** 2026  ·  **Source:** https://openai.com/index/model-disproves-discrete-geometry-conjecture/

## One-line
An autonomous LLM produces a number-theoretic construction that disproves Erdős's 1946 unit-distance conjecture, showing $\nu(n) \geq n^{1+\delta}$ for some absolute $\delta > 0$ and infinitely many $n$.

## Key claim
**Theorem 1.1:** There exists an absolute constant $\delta > 0$ and infinitely many $n$ with $\nu(n) \geq n^{1+\delta}$, where $\nu(n)$ is the maximum number of unit-distance pairs in an $n$-point planar set. This refutes the conjectured bound $\nu(n) \leq n^{1+C/\log\log n}$ from [Erd46], which had been widely believed and supported by recent results on generic norms.

## Method
The construction is a high-dimensional analogue of Erdős's square-grid lower bound, replacing $\mathbb{Q}(i)$ with $K = L(i)$ for $L$ a totally real number field of growing degree. **Arithmetic part:** Hajir–Maire-style unramified pro-3 class field tower over a cyclic cubic base $F$, with Golod–Shafarevich ($r > d^2/4$) keeping the tower infinite while Chebotarev-selected primes $q_b$ (with Frobenius in the Frattini subgroup) are forced to split completely in every layer; bounded root discriminant gives class numbers $h(K_j) \leq H^{f_j}$ via Minkowski. **Geometric part:** Norm-one elements $u = \alpha/c(\alpha)$ from class-group pigeonhole over $2^m$ ideal choices ($m = tf$) embed into a Minkowski lattice $\Lambda \subset \mathbb{C}^f$; averaging over cosets of a polydisc window and projecting one complex coordinate yields the planar set, with injectivity from the field-embedding structure.

## Result
Concretely: with $t = \lceil (\ell-1)^2/100 \rceil$ split primes and $\log H = O(\ell \log \ell)$, the surplus $\gamma = t \log 2 - \log H > 0$ for large $\ell$. The construction gives $\nu(P_j) \geq \tfrac{1}{2} n_j e^{\gamma f_j/2}$ with packing bound $n_j \leq e^{B f_j}$ where $B = 2\log(4RD)$, yielding $\delta = \gamma/(4B) > 0$. The exponent $\delta$ is small and unspecified but absolute; this is an existential infinitely-often statement, not a universal $n$ bound. Compatible with the upper bound $\nu(n) = O(n^{4/3})$ of Spencer–Szemerédi–Trotter [SST84], which remains the best known.

## Why it matters here
General background; no direct arena tie. The paper is notable methodologically — an LLM (gpt-5) autonomously produced a research-level disproof of a 70-year-old conjecture using class field towers — and as evidence that **autonomous mathematical reasoning at conjecture-disproof scale is now possible**, directly relevant to the einstein agent's self-improvement thesis. The combinatorial-geometry content touches problems in the [[discrete_geometry]] / [[packing]] families but the techniques (number-field class towers) are far from current arena workloads.

## Open questions / connections
- Can $\delta$ be made explicit / quantitatively larger, narrowing the gap to the $O(n^{4/3})$ upper bound?
- Does the construction generalize to higher dimensions $\mathbb{R}^d$, refuting analogous conjectures for unit distances in $d \geq 3$?
- Refutes the [EF97] stronger conjecture $k \leq n^{o(1)}$ for $k$-equidistant point sets: average degree $n^{\Omega(1)}$ along this sequence forces a min-degree-$k$ subgraph with $k = n^{\Omega(1)}$.
- How tight is the Hajir–Maire–Ramakrishna [HMR21] tower-cutting machinery here — could other split-prescription problems benefit from the same Frattini-trivial Frobenius trick?
- Methodologically: what does an "AI-written prompt → internal model → AI grading → human verification" pipeline look like as a reproducible research workflow?

## Key terms
unit distance problem, Erdős conjecture, $\nu(n)$ bound, Golod-Shafarevich inequality, class field tower, Hajir-Maire method, unramified pro-3 extension, Frattini subgroup, Chebotarev density theorem, Shafarevich relation rank, totally real cubic field, CM field, Minkowski lattice embedding, conductor-discriminant formula, root discriminant, autonomous LLM mathematics, gpt-5, Spencer-Szemerédi-Trotter, Kővári-Sós-Turán, planar discrete geometry
