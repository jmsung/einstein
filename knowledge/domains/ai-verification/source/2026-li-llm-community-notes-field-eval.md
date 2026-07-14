<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-verification
domains: [ai-verification, ai-agents, ai-nlp]
title: "AI Fact-Checking in the Wild: A Field Evaluation of LLM-Written Community Notes on X"
authors: [Haiwen Li, Michiel A. Bakker]
year: 2026
source_url: https://arxiv.org/abs/2604.02592
drive_file_id: 10i5JlhN-tnYLOAIgiSoXHCiDqk8MwIi8
text_source: pdf
ingested_by: agent
---
# AI Fact-Checking in the Wild: A Field Evaluation of LLM-Written Community Notes on X

**Authors:** Haiwen Li, Michiel A. Bakker (MIT)  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2604.02592

## One-line
The first field evaluation of an LLM fact-checking pipeline deployed live on a social media platform — over three months on X's Community Notes "AI writer" feature it wrote 1,614 notes on 1,597 tweets, and judged by 108,169 ratings from 42,521 real raters, its notes were rated more helpful than human-written notes across the political spectrum.

## Key claim
LLM-written Community Notes can achieve *broader cross-ideological acceptance* than human notes — the exact standard Community Notes is designed to reward (a "bridging" criterion that only shows notes rated helpful by raters with differing viewpoints). This matters because it shows LLMs can be broadly *helpful*, not merely factually correct, and can scale fact-checking to match the volume of misinformation that human contributors cannot. The authors frame LLMs and humans as complementary (LLMs synthesize widely-available info at scale; humans handle novel/niche/fast-moving events), competing within one rating system so the best note wins regardless of origin.

## Method
Real-world A/B-style comparison via X's AI-writer API over a three-month period. The **note-writing pipeline**: retrieve a flagged post + its multimodal context (text, images, video thumbnails, quoted/replied posts) → use **Grok-4-fast** (chosen for X-native search + video understanding) for web and X-native evidence research → **GPT-5-mini** decides whether a note is warranted (spam safeguard) → GPT-5-mini writes the note per Community Notes guidelines → URL-validity, length, and ClaimOpinion quality checks before submission. Because LLM and human notes differ in submission timing and rating exposure, direct note-level comparison is confounded; the authors run two complementary analyses: (1) a **rating-level** linear mixed-effects model of individual ratings (coded Helpful=1.0, Somewhat=0.5, Not=0.0) as a function of AI authorship × rater ideology factor (linear + quadratic), with note and rater random intercepts; (2) a **note-level equal-exposure** analysis restricted to raters who evaluated all notes on the same post, plus robustness specs (tweet random effects, clustered OLS, categorical ideology groups).

## Result
- **Cross-ideological helpfulness:** LLM notes get higher %-helpful and lower %-unhelpful ratings than human notes across *all* ideology groups (left, neutral, right). AI coefficient at ideology center = **0.104 (p < 0.001)** vs a human baseline of ~78.5% helpful from centrists → ≈ **+10 percentage points**. A negative quadratic interaction means the advantage is largest among moderates and narrows toward both extremes, steeper on the right. Estimates hold across all four model specifications.
- **Equal-exposure note-level:** among raters who saw all notes on a post, LLM notes score significantly higher on helpfulness — confirming the advantage isn't a rating-count artifact.
- **Topic heterogeneity:** strongest LLM advantage on health/medicine claims and conspiracy/pseudoscience (abundant authoritative sources); minimal advantage on AI-generated-content posts (needs detection tooling the pipeline lacks — e.g., reverse image search, SynthID could be added).
- **Style/sourcing:** LLM notes are longer (35.8 vs 26.9 words) and cite more URLs (1.51 vs 1.23). LLM notes lean on mainstream/authoritative sources (reuters 7.7%, wikipedia 7.2%, snopes 3.9%, bbc 4.2%); human notes lean on platform-native content (x.com 18.7% vs 4.2% for LLM).

## Limitations / open questions
- **Timing confound:** LLM notes can only be written *after* enough users flag a post, so they're submitted later and accumulate fewer ratings; the Community Notes algorithm penalizes low-rating notes, deflating aggregate LLM scores. The equal-exposure analysis controls for this but it complicates raw platform metrics.
- Results characterize *one specific* pipeline (Grok-4-fast + GPT-5-mini); other AI-writer implementations may differ in relative strengths and overall performance.
- No AI-generated-content detection capability in the current pipeline.

## Key terms
LLM fact-checking, X Community Notes, AI writer, bridging / cross-ideological consensus, rater ideology factor, linear mixed-effects model, equal-exposure analysis, note helpfulness (matrix factorization), multimodal note writing, agentic search pipeline, content moderation at scale, human–AI complementarity
