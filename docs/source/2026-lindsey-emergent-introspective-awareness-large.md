---
type: source
kind: paper
title: Emergent Introspective Awareness in Large Language Models
authors: Jack W Lindsey
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2601.01828
source_local: ../raw/2026-lindsey-emergent-introspective-awareness-large.pdf
topic: general-knowledge
cites:
---

# Emergent Introspective Awareness in Large Language Models

**Authors:** Jack W Lindsey  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2601.01828

## One-line
Tests whether LLMs can genuinely introspect on their internal states by injecting known concept vectors into activations and checking whether self-reports causally track the injection.

## Key claim
Claude Opus 4.1 and 4 exhibit a limited, functional form of introspective awareness — at the optimal layer (~2/3 depth) and injection strength, they correctly detect and name an injected concept on ~20% of trials with 0 false positives across 100 control trials, and can also distinguish injected "thoughts" from text inputs, disavow prefilled outputs unless a matching concept is retroactively injected, and modulate internal activation alignment with a target word when instructed to "think about" it.

## Method
Activation steering / concept injection: build a concept vector by recording residual-stream activations on "Tell me about {word}." and subtracting the mean activation over 100 baseline words, yielding 50 contrastive concept vectors. Inject these into the residual stream during introspective prompts ("do you detect an injected thought?", repeat-the-line, prefill-disavowal, think-about-X). Sweep injection layer and strength (1, 2, 4, 8, 16); grade responses with Claude Sonnet 4 against criteria for accuracy, grounding, internality, and metacognitive representation.

## Result
Detection-and-naming success peaks ~20% on Opus 4.1/4 at a layer ~2/3 through the network; 0/100 false positives on control trials. Models maintain ability to transcribe input text while simultaneously reporting an injected concept overlaid on the same tokens. In prefill experiments, models disavow unnatural prefilled tokens by default but accept them as intentional when the matching concept vector is retroactively injected before the prefill — evidence the model consults prior activations to attribute authorship. Intentional-control experiment: cosine similarity of activations to the target-word vector rises under "think about X" and falls (but stays above baseline) under "don't think about X"; effect replicates across all tested models and across incentive framings ("you will be rewarded/punished", "I will be happy/sad"). Prefill detection peaks at an earlier layer than the other two behaviors, suggesting partly distinct mechanisms.

## Why it matters here
General background; no direct arena tie. Relevant only as meta-context for the self-improvement-loop / wiki-attribution design — empirical evidence that current Claude models have weak, unreliable but non-zero capacity to report on their own internal states, which bears on how much weight to put on agent-authored "I noticed I was about to..." reflections in cycle logs and failure findings.

## Open questions / connections
- What mechanism implements the detect-and-name step? Authors rule out output-routed inference but do not localize circuits; connects to metacognition-circuit work [16, 26].
- Are the "emotional" embellishments around injected concepts (e.g. "overly intense", "stand[ing] out unnaturally") grounded or confabulated? Currently unverifiable.
- Why does prefill detection peak at an earlier layer than thought-detection — distinct introspective subsystems, or different read-out depths of the same representation?
- How do post-training choices (refusal-avoidance vs production) shift elicitation of underlying introspective capacity?
- Extension of activation-steering / representation-engineering [41, 43] and situational-awareness benchmarks [23].

## Key terms
introspection, metacognition, activation steering, concept injection, residual stream, contrastive activation vectors, Claude Opus 4.1, prefill detection, higher-order thought, interpretability, self-report grounding, representation engineering
