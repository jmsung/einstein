---
type: source
kind: paper
title: "The Secret Sharer: Evaluating and Testing Unintended Memorization in Neural Networks"
authors: Nicholas Carlini, Chang Liu, Ú. Erlingsson, Jernej Kos, D. Song
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1802.08232
source_local: ../raw/2018-carlini-secret-sharer-evaluating-testing.pdf
topic: general-knowledge
cites:
---

# The Secret Sharer: Evaluating and Testing Unintended Memorization in Neural Networks

**Authors:** Nicholas Carlini, Chang Liu, Ú. Erlingsson, Jernej Kos, D. Song  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1802.08232

## One-line
A testing methodology that quantifies how much a generative sequence model unintentionally memorizes rare training-data sequences by inserting random "canaries" and measuring their relative perplexity rank.

## Key claim
Generative neural sequence models memorize unique, out-of-distribution training sequences (e.g., a single inserted SSN or credit-card number) well before overtraining, and these secrets can be efficiently extracted via black-box queries; only differentially-private training (DP-SGD/DP-RMSProp) reliably eliminates the effect, while dropout, early-stopping, and weight decay do not.

## Method
Insert a canary $s[\hat r]$ drawn from a randomness space $\mathcal{R}$ into training data, then define **exposure** $= \log_2|\mathcal{R}| - \log_2 \mathrm{rank}_\theta(s[\hat r])$, where rank orders all $|\mathcal{R}|$ candidate fills by model log-perplexity $\mathrm{Px}_\theta$. Rank is approximated either by sampling or by fitting a skew-normal to the empirical perplexity distribution and integrating its tail. A separate shortest-path-style extraction algorithm uses exposure to recover the actual secret given partial context.

## Result
On a PTB character-LSTM, a single inserted 9-digit SSN is recoverable by greedy/beam search after standard training. Exposure rises sharply with batch size, model capacity, and canary repetitions; it is largely unaffected by optimizer choice, shuffling, or bagging. DP-RMSProp drives exposure to $\approx 1$ (no memorization) even at huge nominal $\varepsilon$ (e.g., $\varepsilon = 10^9$), with only ~10% test-loss penalty vs non-private baseline — empirical privacy far exceeds the analytic $\varepsilon$ bound.

## Why it matters here
General background; no direct arena tie. Tangentially relevant only as a methodological reminder that **rare/outlier training data leaves disproportionate fingerprints** — analogous in spirit to how a single canary configuration can dominate optimizer behavior; otherwise unrelated to sphere packing, autocorrelation, or extremal combinatorics.

## Open questions / connections
- Extending exposure/extraction beyond generative models (e.g., to classifiers, regressors) — open.
- Gap between empirical exposure-measured privacy and analytic DP $\varepsilon$ bound (orders of magnitude) — tightening proofs (Erlingsson et al., Feldman et al.) remains active.
- White-box variants using internal activations/weights rather than only output logits — not explored here.

## Key terms
unintended memorization, canary, exposure metric, log-perplexity, rank, generative sequence model, LSTM, differential privacy, DP-SGD, membership inference, Penn Treebank, skew-normal extrapolation
