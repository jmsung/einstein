---
type: source
kind: paper
title: Sets of integers with no large sum-free subset
authors: Sean Eberhard, B. Green, Freddie Manners
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1301.4579
source_local: ../raw/2013-eberhard-sets-integers-large-sum-free.pdf
topic: general-knowledge
cites:
---

# Sets of integers with no large sum-free subset

**Authors:** Sean Eberhard, B. Green, Freddie Manners  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1301.4579

## One-line
Settles Erdős's 1965 question by constructing, for every $\varepsilon>0$, a set of $n$ integers whose largest sum-free subset has size at most $(\tfrac{1}{3}+\varepsilon)n$, proving $\sigma = \lim f(n)/n = 1/3$.

## Key claim
$\sigma := \lim_{n\to\infty} f(n)/n = 1/3$, where $f(n)$ is the largest $k$ such that every $n$-element set of nonzero integers contains a sum-free subset of size $k$. Equivalently: for every $\varepsilon>0$ there is a finite set $A$ such that every $A'\subset A$ with $|A'|\ge(\tfrac{1}{3}+\varepsilon)|A|$ contains distinct $x,y,z$ with $x+y=z$.

## Method
A "local-to-global" weight-function construction on $\mathbb{Z}/Q\mathbb{Z}\times[0,1]$: a Lipschitz weight $w$ encodes the only obstructions to the $1/3$ bound (mod-$Q$ and real-interval). $A\subset\{1,\dots,N\}$ is built by Bernoulli sampling with density $\propto w$, and the arithmetic regularity lemma of Green–Tao (twice) reduces sum-free analysis on $A$ to a continuous problem. The weight is built by an iterative "near-solution → nearer-solution" scheme (Lemma 5.2) whose driver is a structure theorem: open sets with $\mu(A-A)\le(4-\varepsilon)\mu(A)$ have density $\ge \tfrac{1}{2}+c\varepsilon$ on a long progression — proved via regularity + Brunn–Minkowski + a stability version of Kemperman's theorem.

## Result
$f(n) = \tfrac{1}{3}n + o(n)$ (the $o(n)$ is ineffective due to double regularity-lemma use). Side theorem of independent interest (Theorem 4.1 / 6.1 / 6.4): if $A\subset\{1,\dots,N\}$ has $|A-A|\le 4|A|-\varepsilon N$ (or $|A-A|\le(4-\varepsilon)|A|$ via Freiman modelling), then $A$ has density $\ge \tfrac{1}{2}+\tfrac{1}{5}\varepsilon$ on an arithmetic progression of length $\gg_\varepsilon N$. Continuous analog (Theorem 6.2): same for open $A\subset[0,1]$ with bound $\tfrac{1}{2}+\tfrac{1}{7}\varepsilon$.

## Why it matters here
General background on additive combinatorics; no direct arena tie. Relevant if any Einstein problem reduces to sum-free density or small-doubling structure ($|A-A|<4|A|$) — the "doubling-<4 ⇒ dense on a progression" structure theorem is a reusable extremal-combinatorics tool that complements Plünnecke/Freiman-type wiki content.

## Open questions / connections
- Effective $o(n)$ rate: can the dual use of the arithmetic regularity lemma in §4 be replaced by elementary arguments, giving quantitative bounds on $f(n) - n/3$?
- Two-set generalization: extend Theorem 4.1 / 6.2 to $|A-B|<|A|+|B|+2\sqrt{|A||B|}-\varepsilon$ (needs a two-set arithmetic regularity lemma, not yet in the literature).
- Lower bound: is $f(n)\ge \tfrac{n}{3}+\omega(n)$ with $\omega(n)\to\infty$? Best known is Bourgain's $\tfrac{1}{3}(n+2)$.
- Sharper constants: optimal value of $c$ in "density $\tfrac{1}{2}+c\varepsilon$" — paper achieves $\tfrac{1}{4}-\eta$, true optimum unknown.

## Key terms
sum-free sets, Erdős, additive combinatorics, arithmetic regularity lemma, Green–Tao, Gowers $U^2$-norm, small doubling, Brunn–Minkowski, Kemperman theorem, Freiman isomorphism, Plünnecke–Ruzsa, sumset
