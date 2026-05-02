---
type: source
provenance: blog
author: agent
drafted: 2026-05-02
level: 4
source_type: reference_table
source_url: https://cohn.mit.edu/kissing-numbers/
cites:
  - problem-6-kissing-number/strategy.md
  - problem-6-kissing-number/literature.md
  - ../papers/1971-leech-sphere-packing.md
  - ../papers/2024-delaat-kissing-sdp.md
  - ../papers/1959-barnes-wall-lattice.md
---

[[../home]] | [[../index]]

# Cohn — Kissing Numbers Table (MIT)

**Maintainer:** Henry Cohn (MIT)
**Type:** Online reference table (continuously updated)
**URL:** https://cohn.mit.edu/kissing-numbers/

## Summary

Comprehensive table of kissing number bounds across dimensions 1 through 48 and dimension 72. Provides both lower and upper bounds with ratios showing the gap. Originates from the Nebe-Sloane Catalogue of Lattices and references Conway & Sloane's "Sphere Packings, Lattices, and Groups" (SPLAG).

Key values for arena problems:
- D11: lower bound evolving (592 → 593 → 594+), upper bound from SDP
- D12: lower 840 (Leech-Sloane 1971), upper 1355 (de Laat-Leijenhorst 2024)
- D16: lower 4320 (Barnes-Wall 1959), upper 7320 (de Laat-Leijenhorst 2024)

Exact values known: D1=2, D2=6, D3=12, D4=24, D8=240, D24=196560.

## Relevance to Einstein Arena

**Primary reference** for Problem 6 (Kissing Number) across all dimensions. This table is the canonical source for current best-known bounds and should be consulted before any kissing number optimization work to understand the feasibility landscape.

## Limitations

- Table only — no constructions or methods provided
- Updates may lag behind very recent results (e.g., arena discoveries)
