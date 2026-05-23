---
type: source
kind: paper
title: An Improved Bound on the Fraction of Correctable Deletions
authors: B. Bukh, V. Guruswami, J. Håstad
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1507.01719
source_local: ../raw/2015-bukh-improved-bound-fraction-correctable.pdf
topic: general-knowledge
cites:
---

# An Improved Bound on the Fraction of Correctable Deletions

**Authors:** B. Bukh, V. Guruswami, J. Håstad  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1507.01719

## One-line
Constructs $k$-ary codes with positive rate that recover from a deletion fraction approaching $1 - 2/(k+\sqrt{k})$, improving the previous $1 - 1/\sqrt{k}$ bound and giving $\sqrt{2}-1 \approx 0.414$ for binary.

## Key claim
For every $k \geq 2$, there exist (in fact, explicit, near-linear-time decodable) codes over $[k]$ of positive rate whose worst-case correctable deletion fraction $p^*(k) \geq 1 - 2/(k+\sqrt{k})$; combined with the trivial Plotkin-style upper bound $p^*(k) \leq 1 - 1/k$, this pins $1 - p^*(k) = \Theta(1/k)$.

## Method
Code concatenation with an inner code built from "oscillating" words $f_A = (1^A 2^A \cdots k^A)^{L/A}$ at geometrically spaced amplitudes $A = R^{l-1}$, exploiting the fact that two such words admit long common subsequences only when their amplitudes (frequencies) are close. A "dirty" variant $(1^a 2^{ca} \cdots k^{ca})^{M/((1+(k-1)c)a)}$ with $c = \sqrt{k}-1)/(k-1)$ sharpens the bound from $1-1/(k+1)$ to $1 - 2/(k+\sqrt{k})$. Outer code is either random (existence), explicit high-rate deletion code from [Guruswami–Wang '15] (constructive), or Reed–Solomon (efficient decoding via list decoding + brute-force inner decoding + pruning by LCS containment).

## Result
**Theorem 3:** alphabet-reduction concatenation produces $C_2 \subseteq [k]^N$ with $\mathrm{LCS}(C_2) \leq (2/(k+\sqrt{k}) + \varepsilon) N$ and span lower bound $\mathrm{span}(s) \geq (k+\sqrt{k})\mathrm{len}(s) - 5\varepsilon k N$ on any common subsequence between distinct codewords. **Theorem 19:** the explicit RS-concatenated code is decodable from a $1 - 2/(k+\sqrt{k}) - O(\varepsilon^{1/3})$ deletion fraction in $N^3 \cdot \mathrm{poly}(\log N)$ time (improvable to $N \cdot \mathrm{poly}(\log N)$ via recursion). Binary case: $p^*(2) \geq \sqrt{2}-1$.

## Why it matters here
General background; no direct arena tie — this is coding theory (worst-case deletion channels), orthogonal to the sphere-packing / autocorrelation / kissing-number problems on Einstein Arena. The "oscillating words at geometric frequencies" trick and span-vs-LCS amplification argument may have weak analogy value for extremal-combinatorics framings, but no current arena problem uses LCS.

## Open questions / connections
- Close the gap $\sqrt{2}-1 \approx 0.414 \leq p^*(2) \leq 1/2$ for binary deletion codes — authors decline to conjecture which endpoint is tight.
- Authors suspect a *new mechanism* (beyond frequency-separation + dirt) is required to reach $p^*(2) = 1/2$, since pushing dirt fraction toward $1/2$ contradicts the "dirt as minority" intuition.
- Extends [Bukh–Zhou], [Bukh–Ma] LCS-amplitude observations; builds on Kiwi–Loebl–Matoušek random-LCS asymptotics $E[\mathrm{LCS}] \sim \sqrt{2/k}\, n$ and Guruswami–Wang high-noise deletion codes.

## Key terms
deletion codes, longest common subsequence, LCS, worst-case deletions, code concatenation, Reed-Solomon list decoding, Plotkin bound, alphabet reduction, oscillating words, span of subsequence, Bukh, Guruswami, Håstad, binary codes, Sudan list decoding
