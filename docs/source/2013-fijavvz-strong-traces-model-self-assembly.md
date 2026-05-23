---
type: source
kind: paper
title: Strong Traces Model of Self-Assembly Polypeptide Structures
authors: Gavsper Fijavvz, Tomavz Pisanski, Jernej Rus
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1308.4024
source_local: ../raw/2013-fijavvz-strong-traces-model-self-assembly.pdf
topic: general-knowledge
cites:
---

# Strong Traces Model of Self-Assembly Polypeptide Structures

**Authors:** Gavsper Fijavvz, Tomavz Pisanski, Jernej Rus  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1308.4024

## One-line
Introduces "strong traces" — closed double-walks on a graph without nontrivial vertex repetitions — as the correct combinatorial model for routing a single polypeptide chain through the edge-skeleton of a target polyhedral nanostructure.

## Key claim
Every connected graph admits a strong trace (Thm 2.4), hence every connected graph can in principle be assembled from a single coiled-coil polypeptide chain; furthermore $G$ admits an *antiparallel* strong trace iff $G$ has a spanning tree $T$ with every component of $G - E(T)$ having an even number of edges, and a *parallel* strong trace iff $G$ is Eulerian.

## Method
The core technique is a duality between double traces and combinatorial graph embeddings $(\Pi,\lambda)$ on surfaces: a double trace $W$ is "strong" iff every vertex figure $F_{v,W}$ (the 2-regular graph on $E(v)$ recording $W$-consecutiveness) is a single cycle, equivalently $W$ is the unique facial walk of a 1-face embedding. Existence then follows from the Edmonds–Pisanski 1-face embedding theorem; the parallel case is handled by a local swap argument that merges two vertex-figure cycles into one without changing edge directions.

## Result
- Thm 2.4 / 2.5: every connected $G$ has a strong trace (constructive via 1-face embedding).
- Prop 3.4: $G$ admits a $d$-stable trace iff $\delta(G) > d$, recovering Sabidussi/Eggleton–Skilton ($d=1$) and Klavžar–Rus ($d=2$).
- Thm 4.1/4.2: antiparallel strong trace $\Leftrightarrow$ 1-face *orientable* embedding $\Leftrightarrow$ Xuong-type spanning-tree parity condition.
- Thm 5.3/5.4: parallel $d$-stable trace iff $G$ is Eulerian and $\delta(G) > d$.

## Why it matters here
General background; no direct arena tie — Einstein Arena problems are continuous-geometry / extremal-analysis (sphere packing, autocorrelation, kissing) rather than polyhedral self-assembly routing. Tangentially informs any future discrete-combinatorics problem involving Eulerian-type traversals or graph embeddings on surfaces.

## Open questions / connections
- Problem 4.6: characterize graphs admitting antiparallel $d$-stable traces for $d > 1$ (the surface-embedding correspondence breaks; pseudo-surfaces appear).
- Choice problem: among many strong traces of a fixed graph (40 for the cube), which maximizes self-assembly yield? Initial-vertex dependence on physical/chemical properties is open.
- Extends Tarry (1895), Ore (1951), Sabidussi, Eggleton–Skilton, Thomassen (1990), and Xuong (1979) on double-tracings and maximum-genus embeddings.

## Key terms
strong trace, double trace, d-stable trace, Eulerian graph, 1-face embedding, rotation system, signature, vertex figure, antiparallel trace, parallel trace, maximum genus, Xuong spanning tree, polypeptide self-assembly, coiled-coil, Steinitz theorem
