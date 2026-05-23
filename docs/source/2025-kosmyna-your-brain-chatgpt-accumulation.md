---
type: source
kind: paper
title: "Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task"
authors: Nataliya Kosmyna, Eugene Hauptmann, Ye Yuan, Jessica Situ, Xiangwen Liao, Ashly Vivian Beresnitzky, Iris Braunstein, Pattie Maes
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2506.08872
source_local: ../raw/2025-kosmyna-your-brain-chatgpt-accumulation.pdf
topic: general-knowledge
cites:
---

# Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task

**Authors:** Nataliya Kosmyna, Eugene Hauptmann, Ye Yuan, Jessica Situ, Xiangwen Liao, Ashly Vivian Beresnitzky, Iris Braunstein, Pattie Maes  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2506.08872

## One-line
EEG + NLP study of 54 participants writing SAT essays with ChatGPT, a search engine, or unaided, showing LLM users develop weaker neural connectivity, weaker essay ownership, and worse recall over 4 sessions.

## Key claim
Brain connectivity scales inversely with external tool support: Brain-only > Search > LLM across alpha, beta, theta, and delta bands (dDTF), and LLM users in session 4 (LLM-to-Brain) show persistent under-engagement of alpha/beta networks plus impaired ability to quote their own essays — evidence of accumulated "cognitive debt" from repeated LLM use.

## Method
Three groups (LLM / Search Engine / Brain-only, $n=18$ each) wrote SAT-style essays across 3 sessions; 18 participants returned for a 4th session with swapped condition (LLM→Brain, Brain→LLM). Brain activity measured via 32-channel Enobio EEG, analyzed via dynamic Directed Transfer Function (dDTF) across alpha/beta/theta/delta bands; essays scored by human teachers + an AI judge, with NLP analysis covering NER, n-grams, ontology, and latent embeddings, plus post-session interviews.

## Result
Total significant dDTF sums (Brain-only group, alpha band): Sessions 2 ≈ 0.825, S3 ≈ 0.506, S4 ≈ 0.242, S1 ≈ 0.057 — peak engagement at S2–S3. LLM group's total dDTF was substantially lower across all bands until session 4, when Brain-to-LLM participants showed network-wide spikes (e.g., low delta total 2.894 in S4 vs 0.902 in S1). LLM users reported low essay ownership and reduced quoting ability; LLM-to-Brain (S4) participants exhibited weaker connectivity than the never-LLM Brain group, consistent with carryover deficit. NER/n-gram/ontology homogeneity was highest within the LLM group.

## Why it matters here
General background; no direct arena tie. Relevant only as a meta-cautionary signal for the agent's own self-improvement loop — heavy reliance on LLM-generated wiki content without independent re-derivation may produce the same kind of "ownership decay" and reduced recall the paper documents in humans.

## Open questions / connections
- Does cognitive debt accumulate analogously in an agent that copies LLM-derived findings without triple-verification or re-derivation from sources?
- Would the Brain-to-LLM session-4 connectivity spike correspond, in agent terms, to the value of writing failure findings *before* querying LLM completions on the next problem?
- Connects to existing concerns in `wiki-first-lookup.md` and `triple-verify.md`: skipping independent verification compounds drift — the human analog is documented here.

## Key terms
cognitive debt, cognitive offloading, EEG, dynamic Directed Transfer Function, dDTF, alpha band, beta band, neural connectivity, LLM essay writing, ChatGPT, NER, n-grams, essay ownership, learning sciences
