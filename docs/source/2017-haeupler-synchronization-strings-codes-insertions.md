---
type: source
kind: paper
title: "Synchronization strings: codes for insertions and deletions approaching the Singleton bound"
authors: Bernhard Haeupler, Amirbehshad Shahrasbi
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1704.00807
source_local: ../raw/2017-haeupler-synchronization-strings-codes-insertions.pdf
topic: general-knowledge
cites:
---

# Synchronization strings: codes for insertions and deletions approaching the Singleton bound

**Authors:** Bernhard Haeupler, Amirbehshad Shahrasbi  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1704.00807

## One-line
Introduces "synchronization strings" — a combinatorial indexing primitive that reduces insertion/deletion errors to ordinary half-errors, yielding near-MDS insdel codes that approach the Singleton bound.

## Key claim
For every $\varepsilon > 0$ and $\delta \in (0,1)$, there exist explicit insdel codes over a constant-size alphabet $|\Sigma| = f(\varepsilon)$ with rate $> 1 - \delta - \varepsilon$ that uniquely and efficiently decode any $\delta n$ insertions/deletions in linear encoding and quadratic decoding time.

## Method
A synchronization string $S$ is an infinite sequence over a finite alphabet with the $\varepsilon$-synchronization property: any two neighboring intervals of total length $\ell$ require $\geq (1-\varepsilon)\ell$ insdel ops to transform one into the other. Existence is proved via Lovász local lemma; derandomization uses $O(\log\log n / \log(1/\varepsilon))$-wise independent strings via Naor–Naor small-bias spaces over alphabet $O(\varepsilon^{-6})$. Attaching $S$ symbol-by-symbol to any Hamming ECC (e.g., Guruswami–Indyk expander codes) transforms it black-box into an insdel code; decoding uses minimum relative-suffix-distance (RSD) or global longest-common-subsequence matching.

## Result
$k$ synchronization errors reduce to at most $(1+\varepsilon)k$ half-errors using constant-size alphabet polynomial in $1/\varepsilon$. Streaming RSD decoder gives $(5+\varepsilon)k$ reduction; global LCS-based decoder achieves the $(1+\varepsilon)k$ near-MDS bound. Linear-time error-free decoders exist for deletion-only and insertion-only channels with $\leq \varepsilon n \delta / (1-\varepsilon)$ misdecodings. This closes a 50-year gap: prior insdel codes (Schulman–Zuckerman 1999; Guruswami–Li 2016) achieved only $\Omega(\delta^5)$ rate or $1 - O(\sqrt{\delta})$ rate, polynomially far from optimal.

## Why it matters here
General background; no direct arena tie. Could inform any Einstein Arena problem involving combinatorial string structures with non-self-similarity constraints, derandomization via $k$-wise independence, or Lovász local lemma constructions — but the direct application (insdel coding) is outside the current 23-problem scope.

## Open questions / connections
- Can an improved relative-suffix pseudo-distance (RSPD) variant achieve near-MDS via a single-pass minimum-distance decoder (vs. requiring global LCS)?
- Tightening the alphabet bit size from near-linear in $1/\varepsilon$ to the existential logarithmic-in-$1/\varepsilon$ bound while preserving linear encoding/decoding.
- Extends Thue's non-repetitive-sequence tradition (1912) and the Spielman/Guruswami–Indyk expander-code line; connects to derandomized Lovász local lemma (Chandrasekaran–Goyal–Haeupler 2013; Moser–Tardos 2010).

## Key terms
synchronization strings, insertion-deletion codes, insdel codes, Singleton bound, near-MDS codes, edit distance, Lovász local lemma, k-wise independence, relative suffix distance, expander codes, Guruswami-Indyk, Levenshtein, derandomization, self-matching property
