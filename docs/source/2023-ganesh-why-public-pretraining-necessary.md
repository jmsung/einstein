---
type: source
kind: paper
title: Why Is Public Pretraining Necessary for Private Model Training?
authors: Arun Ganesh, Mahdi Haghifam, Milad Nasr, Sewoong Oh, T. Steinke, Om Thakkar, Abhradeep Thakurta, Lun Wang
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2302.09483
source_local: ../raw/2023-ganesh-why-public-pretraining-necessary.pdf
topic: general-knowledge
cites:
---

# Why Is Public Pretraining Necessary for Private Model Training?

**Authors:** Arun Ganesh, Mahdi Haghifam, Milad Nasr, Sewoong Oh, T. Steinke, Om Thakkar, Abhradeep Thakurta, Lun Wang  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2302.09483

## One-line
Constructs a synthetic loss landscape proving that public pretraining is provably necessary (not just helpful) for differentially-private optimization to achieve low excess risk.

## Key claim
There exist data distributions where neither $n_{\text{pub}}=p$ public samples alone nor $n_{\text{priv}}=p^2$ $(\varepsilon,\delta)$-DP private samples alone can achieve excess population loss $o(1)$, yet public-pretraining-then-private-finetuning achieves $O(1/p)$ excess loss — a provable separation in sample complexity.

## Method
Concatenates two known mean-estimation lower bounds into a single non-convex loss $\ell((\theta_1,\theta_2);(d_1,d_2)) = \ell_1(\theta_1;d_1) + p\cdot q(\theta_1)\cdot\ell_2(\theta_2;d_2)$ on $\mathbb{R}^{p^4}\times\mathbb{R}^p$, where $q$ is a "basin-activation" function that gates the second term to be active only inside a basin $S\subset\mathbb{R}^{p^4}$. The first coordinates encode a high-dimensional ($p^4$) private mean-estimation lower bound (Lemma 1.2, [BST14, SU17]); the second encode a low-dimensional mean-estimation problem solvable only with many samples (Lemma 1.3). Public data is needed to enter the right basin; private data is then needed to optimize within it. Extended to OOD public data via a point-distribution trick that hides $\tau_2$ from the public set.

## Result
**Theorem 2.1**: For any $p\geq 1$ and $\delta=o(1/p^2)$: (i) any $(1,\delta)$-DP $\mathcal A_{\text{priv}}$ on $p^2$ samples has worst-case excess loss $\Omega(1)$; (ii) any non-private $\mathcal A_{\text{pub}}$ on $p$ samples has worst-case excess loss $\Omega(1)$; (iii) one full-batch GD step on the $p$ public samples followed by DP-SGD on the $p^2$ private samples achieves $O(1/p)$ excess loss. Theorem 2.2 extends this to OOD public data. Theorem D.1 shows a quadratic, constrained version of the same separation. Empirically validated on CIFAR-10 (low-noise epochs are best spent in pretraining, not post-training) and LibriSpeech (publicly-pretrained-then-privately-finetuned models live in the same loss-landscape basin as fully-public models, while fully-private models land in a different basin).

## Why it matters here
General background; no direct arena tie. The framing — "selection between basins is the hard phase; convex optimization inside a basin is the easy phase" — is a useful mental model for any non-convex landscape including the multistart / basin-hopping work on P11, P15, P17, but the privacy mechanism itself is orthogonal to the Einstein Arena problem set.

## Open questions / connections
- Can the two-phase (basin-selection then basin-polish) decomposition be made rigorous for *deterministic* non-convex optimization landscapes (not just DP)? Connects to multistart vs. polish tradeoff in our optimizer work.
- The DP-selection lower bound of [SU17] ($n=\Omega(\sqrt{k}\log d)$ for top-$k$ of $d$ coins) is the underlying combinatorial primitive; its reduction to non-convex optimization via [GTU22] is structurally similar to "basin = arm" framings.
- Privacy-budget scheduling across training rounds (more budget early, less late) remains an open practical question — relates to annealing schedules in SA / parallel tempering.

## Key terms
differential privacy, DP-SGD, public pretraining, transfer learning, non-convex optimization, basin selection, two-phase optimization, mean estimation lower bound, sample complexity separation, hypothesis selection, loss landscape, out-of-distribution pretraining, fine-tuning, [SU17] selection lower bound, Polyak-Lojasiewicz
