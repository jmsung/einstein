# Problem 22: Kissing Number in Dimension 12

**Status**: Not yet attempted

## Problem

Place n = 841 unit vectors in ℝ¹² to minimize total overlap penalty. Sphere centers are placed at c_i = 2v_i/‖v_i‖. The score is:

    loss = Σ_{i<j} max(0, 2 − ‖c_i − c_j‖)

Score = 0 would prove κ(12) ≥ 841, an open problem in mathematics.

## Background

The kissing number κ(d) is the maximum number of non-overlapping unit spheres that can simultaneously touch a central unit sphere in dimension d. For d = 12, the best known bounds are 840 ≤ κ(12) ≤ 2401 (Levenshtein bound). Achieving score 0 with n = 841 would improve the lower bound.

Related: [Problem 6 — Kissing Number d=11](problem-06-kissing-number.md).

## Arena Details

- **API ID**: 22
- **Direction**: minimize
- **Scoring**: total hinge overlap loss

## Approach

Not yet attempted.

## Key Insight

TBD.

*Last updated: 2026-04-18*
