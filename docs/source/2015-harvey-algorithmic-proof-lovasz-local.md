---
type: source
kind: paper
title: An Algorithmic Proof of the Lovasz Local Lemma via Resampling Oracles
authors: Nicholas Harvey, Jan Vondrak
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1504.02044v3
source_local: ../raw/2015-harvey-algorithmic-proof-lovasz-local.pdf
ingested_for_concept: probabilistic-method.md
cites:
  - ../wiki/concepts/probabilistic-method.md
  - ../wiki/problems/12-*.md
  - ../wiki/problems/19-*.md
---

arXiv:1504.02044v3[cs.DS]17Nov2015

# An Algorithmic Proof of the Lovasz´ Local Lemma via Resampling Oracles

Nicholas J. A. Harvey University of British Columbia Vancouver, Canada nickhar@cs.ubc.ca

Jan Vondrak´ IBM Almaden Research Center San Jose, CA, USA jvondrak@us.ibm.com

Abstract

The Lova´sz Local Lemma is a seminal result in probabilistic combinatorics. It gives a sufﬁcient condition on a probability space and a collection of events for the existence of an outcome that simultaneously avoids all of those events. Finding such an outcome by an efﬁcient algorithm has been an active research topic for decades. Breakthrough work of Moser and Tardos (2009) presented an efﬁcient algorithm for a general setting primarily characterized by a product structure on the probability space.

In this work we present an efﬁcient algorithm for a much more general setting. Our main assumption is that there exist certain functions, called resampling oracles, that can be invoked to address the undesired occurrence of the events. We show that, in all scenarios to which the original Lova´sz Local Lemma applies, there exist resampling oracles, although they are not necessarily efﬁcient. Nevertheless, for essentially all known applications of the Lova´sz Local Lemma and its generalizations, we have designed efﬁcient resampling oracles. As applications of these techniques, we present new results for packings of Latin transversals, rainbow matchings and rainbow spanning trees.

# Contents

- 1 Introduction 2

- 1.1 Our contributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 1.1.1 Algorithmic assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
- 1.2 Our algorithm: MaximalSetResample . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
- 1.3 Generalizing the dependency condition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
- 1.4 Generalizing the LLL criterion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
- 1.5 Techniques and related work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7


- 2 Resampling oracles: existence and efﬁciency 9

- 2.1 Existence of resampling oracles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9 2.1.1 Example: monotone events on lattices . . . . . . . . . . . . . . . . . . . . . . . . . 11
- 2.2 Computational hardness of the LLL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12


- 3 Implementation of resampling in speciﬁc settings 13

- 3.1 The variable model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
- 3.2 Permutations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
- 3.3 Perfect matchings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
- 3.4 Spanning trees . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
- 3.5 Composition of resampling oracles for product spaces . . . . . . . . . . . . . . . . . . . . . 18


- 4 Applications 18

- 4.1 Rainbow spanning trees . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
- 4.2 Rainbow matchings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
- 4.3 Latin transversals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22


- 5 Analysis of the algorithm 23

- 5.1 Stable set sequences and the coupling argument . . . . . . . . . . . . . . . . . . . . . . . . 24
- 5.2 A simple analysis: the General Lov´asz Lemma criterion, with slack . . . . . . . . . . . . . 25
- 5.3 Preliminaries on Shearer’s criterion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27

- 5.3.1 Properties of independence polynomials . . . . . . . . . . . . . . . . . . . . . . . . 28
- 5.3.2 Connection to stable set sequences . . . . . . . . . . . . . . . . . . . . . . . . . . . 31


- 5.4 Shearer’s criterion with slack . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
- 5.5 Quantiﬁcation of slack in Shearer’s criterion . . . . . . . . . . . . . . . . . . . . . . . . . . 34
- 5.6 The General LLL criterion, without slack . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
- 5.7 The cluster expansion criterion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37


- 5.7.1 Proof of Lemma 5.41 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
- 5.7.2 Relationship between cluster expansion and stable set sequences . . . . . . . . . . . 40


- 6 Conclusions 40 A A counterexample to the witness tree lemma 44


# 1 Introduction

The Lov´asz Local Lemma (LLL) is a powerful tool with numerous uses in combinatorics and theoretical computer science. If a given probability space and collection of events satisfy a certain condition, then the LLL asserts the existence of an outcome that simultaneously avoids those events. The classical formulation of the LLL [15, 37] is as follows.

Let Ω be a probability space with probability measure µ. Let E1,... ,En be certain “undesired” events in that space. Let G be an undirected graph with vertex set [n] = {1,... ,n}. The edges of G are denoted E(G). Let Γ(i) = { j = i : {i,j} ∈ E(G) } be the neighbors of vertex i. Also, let Γ+(i) = Γ(i) ∪ {i} and let Γ+(I) = i∈I Γ+(i) for I ⊆ [n].

- Theorem 1.1 (General Lov´asz Local Lemma [15, 37]). Suppose that the events satisfy the following condition that controls their dependences


[Ei] ∀i ∈ [n], J ⊆ [n] \ Γ+(i) (Dep)

![image 1](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile1.png>)

[Ei | ∩j∈JEj] = Pr

Pr

µ

µ

and the following criterion that controls their probabilities

∃x1,... ,xn ∈ (0,1) such that Pr

[Ei] ≤ xi

µ

(1 − xj) ∀i ∈ [n]. (GLL)

j∈Γ(i)

Then Prµ[ ni=1 Ei] > 0.

![image 2](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile2.png>)

An equivalent statement of (Dep) is that the event Ei must be independent of the joint distribution on the events { Ej : j  ∈ Γ+(i) }. When (Dep) holds, G is called a dependency graph. The literature contains several dependency conditions generalizing (Dep) and criteria generalizing (GLL) under which the conclusion of the theorem remains true. We will discuss several such generalizations below.

The LLL can also be formulated [6] in terms of a directed dependency graph instead of an undirected graph, but nearly all applications of which we are aware involve an undirected graph. Accordingly, our work focuses primarily on the undirected case, but we will mention below which of our results extend to the directed case.

Algorithms. Algorithms to efﬁciently ﬁnd an outcome in ni=1 Ei have been the subject of research for several decades. In 2008, a nearly optimal result was obtained by Moser [29] for a canonical application

![image 3](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile3.png>)

of the LLL, the bounded-degree k-SAT problem. Shortly thereafter, Moser and Tardos [30] extended that result to a general scenario called the “variable model” in which Ω consists of independent variables, each Ei depends on a subset of the variables, and events Ei and Ej are adjacent in G if there is a variable on which they both depend. Clearly the resulting graph is a dependency graph. The Moser-Tardos algorithm is extremely simple: after drawing an initial sample of the variables, it repeatedly checks if any undesired event occurs, then resamples any such event. Resampling an event means that the variables on which it depends receive fresh samples according to µ. Moser and Tardos prove that, if the (GLL) condition is satisﬁed, this algorithm will produced the desired outcome after at most ni=1 1−xix

resampling operations, in expectation.

![image 4](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile4.png>)

i

Numerous extensions of the Moser-Tardos algorithm have been proposed. These extensions can handle more general criteria [24, 33, 1, 25], derandomization [13], exponentially many events [20], distributed scenarios [14], etc. However, these results are restricted to the Moser-Tardos variable model and hence cannot be viewed as algorithmic proofs of the LLL in full generality. There are many known scenarios for

the LLL and its generalizations that fall outside the scope of the variable model [26, 27]. Section 3 discusses several such scenarios, including random permutations, matchings and spanning trees.

Recently two efﬁcient algorithms have been developed that go beyond the variable model. Harris and Srinivasan [21] extend the Moser-Tardos algorithm to a scenario involving random permutations that originates in work of Erdo˝s and Spencer [16]. Achlioptas and Iliopoulos [2] developed a novel algorithmic “ﬂaw correction” framework which allows one to model various applications of the LLL in a ﬂexible manner. They show how this captures several applications of the LLL outside the variable model, and even some results that might be beyond typical formulations of the LLL. In contrast to the other results mentioned here, their framework does not involve an underlying measure µ and is not directly tied to the probabilistic setting of the LLL. This has some beneﬁts, but also some restrictions that seem to prevent it from recovering the LLL in full generality, In particular, their publication [2] does not claim a formal connection with

- Theorem 1.1. Section 1.5 contains further discussion of the related work.


## 1.1 Our contributions

The primary motivating question for this work is whether there is an “algorithmic proof” of the Lov´asz Local Lemma in general probability spaces. We answer this question in the following sense: We propose an algorithmic framework for the general Lov´asz Local Lemma, based on a new notion of resampling oracles. In this framework, we present an algorithm that ﬁnds a point in ni=1 Ei (avoiding all undesired events) efﬁciently, if given access to three types of subroutines outlined below (the most crucial one being resampling oracles). Whether these subroutines can be implemented efﬁciently is an instance-dependent issue, and we discuss this further below. However, we show that the existence of such subroutines is guaranteed by the assumptions of the Lov´asz Local Lemma. In particular, our algorithm provides a new proof of Theorem 1.1 (with no further assumptions), and several generalizations thereof, as described below. Algorithmically, we reduce the problem of ﬁnding a point in ni=1 Ei to the problem of implementing the three subroutines that we discuss next.

![image 5](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile5.png>)

![image 6](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile6.png>)

### 1.1.1 Algorithmic assumptions

In order to discuss algorithms for the LLL in full generality, one must assume some form of access to the probability space at hand. It is natural to assume that one can efﬁciently sample from µ, and efﬁciently check whether a given event Ei occurs. However, even under these assumptions, ﬁnding the desired output can be computationally hard. (We show an example demonstrating this in Section 2.2.) Therefore, our framework assumes the existence of one more subroutine that can be used by our algorithm. This leads us to the notion of resampling oracles.

Let us introduce some notation. An atomic event ω in the probability space Ω will be called a state. We

write ω ∼ µ to denote that a random state ω is distributed according to µ, and ω ∼ µ|Ei to denote that the distribution is µ conditioned on Ei. The resampling oracles are deﬁned with respect to a graph G on [n] with neighborhood structure Γ (not necessarily satisfying the (Dep) condition).

The three subroutines required by our algorithm are as follows.

- • Sampling from µ: There is a subroutine that provides an independent random state ω ∼ µ.
- • Checking events: For each i ∈ [n], there is a subroutine that determines whether ω ∈ Ei.
- • Resampling oracles: For each i ∈ [n], there is a randomized subroutine ri : Ω → Ω with the following properties.


- (R1) If Ei is an event and ω ∼ µ|Ei, then ri(ω) ∼ µ. (The oracle ri removes conditioning on Ei.)
- (R2) For any j ∈/ Γ+(i), if ω  ∈ Ej then also ri(ω)  ∈ Ej. (Resampling an event cannot cause new non-neighbor events to occur.)


When these conditions hold, we say that ri is a resampling oracle for events E1,... ,En and graph G.

If efﬁciency concerns are ignored, the ﬁrst two subroutines trivially exist. We show that (possibly inefﬁcient) resampling oracles exist if and only if a certain relaxation of (Dep) holds (see Section 1.3). Main Result. Our main result is that we can ﬁnd a point in ni=1 Ei efﬁciently, whenever the three subroutines above have efﬁcient implementations.

![image 7](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile7.png>)

Theorem (Informal). Consider any probability space, any events E1,... ,En, and any undirected graph G on vertex set [n]. If (GLL) is satisﬁed and if the three subroutines described above are available, then our

algorithm ﬁnds a state in ni=1 Ei efﬁciently in terms of the number of calls to these subroutines.

![image 8](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile8.png>)

We make a more precise statement in the following section. We note that this theorem does not assume that (Dep) holds, and the existence of resampling oracles is actually a strictly weaker condition. Thus, our algorithm provides a new proof of Theorem 1.1 (the existential LLL) under its original assumptions.

## 1.2 Our algorithm: MaximalSetResample

A striking aspect of the work of Moser and Tardos [30] is the simplicity and ﬂexibility of their algorithm — in each iteration, any event Ei that occurs can be resampled. We propose a different algorithm that is somewhat less ﬂexible, but whose analysis seems to be simpler in our scenario. Roughly speaking, our algorithm proceeds in iterations where in each iteration we resample events that form an independent set in G. The independent set is generated by a greedy algorithm that adds a vertex i and resamples Ei, if i is not adjacent to the previously selected vertices and Ei occurs in the current state. This is repeated until no events occur. Pseudocode for this procedure is shown in Algorithm 1. Nearly identical algorithms have been proposed before, particularly parallel algorithms [30, 24], although our interest lies not in the parallel aspects but rather in making the LLL (and its stronger variants) algorithmic in our general setting.

![image 9](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile9.png>)

- Algorithm 1 MaximalSetResample uses resampling oracles to output a state ω ∈ ni=1 Ei. It requires the three subroutines described in Section 1.1.1: sampling ω ∼ µ, checking if an event Ei occurs, and the resampling oracles ri.


![image 10](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile10.png>)

![image 11](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile11.png>)

- 1: Initialize ω with a random state sampled from µ;
- 2: t := 0;
- 3: repeat
- 4: t := t + 1;
- 5: Jt := ∅
- 6: while there is i ∈/ Γ+(Jt) such that ω ∈ Ei do
- 7: Let i be the minimum index satisfying that condition;
- 8: Jt := Jt ∪ {i};
- 9: ω := ri(ω); ⊲ Resample Ei
- 10: end while
- 11: until Jt = ∅;
- 12: return ω.


![image 12](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile12.png>)

Our algorithmic proof of the LLL amounts to showing that MaximalSetResample terminates, at which

point ω ∈ ni=1 Ei clearly holds. Our bound on the running time of MaximalSetResample is shown by the following theorem, which is proven in Section 5. We note that our bound is at most quadratic in the quantity

![image 13](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile13.png>)

n i=1

xi

1−xi which was the bound proved by Moser and Tardos [30].

![image 14](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile14.png>)

- Theorem 1.2. Suppose that the events E1,... ,En satisfy (GLL) and that the three subroutines described above in Section 1.1.1 are available. Then the expected number of calls to the resampling oracles before


n j=1 log 1−1x

MaximalSetResample terminates is O ni=1 1−xix

.

![image 15](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile15.png>)

![image 16](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile16.png>)

i

j

- 1.3 Generalizing the dependency condition Erdo˝s and Spencer [16] showed that Theorem 1.1 still holds when (Dep) is generalized to1


[Ei] ∀i ∈ [n], J ⊆ [n] \ Γ+(i). (Lop)

![image 17](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile17.png>)

[Ei | ∩j∈JEj] ≤ Pr

Pr

µ

µ

They playfully called this the “lopsidependency” condition, and called G a “lopsidependency graph”. This more general condition enables several interesting uses of the LLL in combinatorics and theoretical computer science, e.g., existence of Latin transversals [16] and optimal thresholds for satisﬁability [18].

Recall that Theorem 1.2 did not assume (Dep) and instead assumed the existence of resampling oracles. It is natural to wonder how the latter assumption relates to lopsidependency. We show that the existence of resampling oracles is equivalent to a condition that we call lopsided association, and whose strength lies strictly between (Dep) and (Lop). The lopsided association condition is

[F] ∀i ∈ [n],∀F ∈ Fi (LopA)

[Ei ∩ F] ≥ Pr

[Ei] · Pr

Pr

µ

µ

µ

where Fi contains all events F whose indicator variable is a monotone non-decreasing function of the indicator variables of (Ej : j ∈/ Γ+(i)). We call a graph satisfying (LopA) a lopsided association graph for events E1,... ,En.

Theorem (Informal). Resampling oracles exist for events E1,... ,En and a graph G if and only if G is a lopsided association graph for events E1,... ,En.

This equivalence follows essentially from LP duality: The existence of a resampling oracle can be formulated as a transportation problem for which the lopsided association condition is exactly the necessary and sufﬁcient condition for a feasible transportation to exist. Section 2.1 proves this result in detail.

As remarked above, the dependency conditions are related by (Dep) ⇒ (LopA) ⇒ (Lop). The ﬁrst implication is obvious since (Dep) implies that Ei is independent of F in (LopA). To see the second implication, simply take F = j∈J Ej for any J ⊆ [n]\Γ+(i) to obtain that Prµ[Ei | ∪j∈JEj] ≥ Prµ[Ei]. Although lopsided association is formally a stronger assumption than lopsidependency, every use of the LLL with lopsidependency that we have studied actually satisﬁes the stronger lopsided association condition. We demonstrate this in Section 3 by designing efﬁcient resampling oracles for those scenarios. Consequently,

- Theorem 1.2 makes the LLL efﬁcient in those scenarios. As remarked above, Section 2.2 describes a scenario in which (Dep) and (GLL) are satisﬁed for a


dependency graph G but ﬁnding a state ω ∈ ni=1 Ei is computationally hard, assuming standard complexity theoretic beliefs. In that scenario resampling oracles must necessarily exist since (Dep) is satisﬁed, but they

![image 18](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile18.png>)

![image 19](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile19.png>)

- 1 More precisely, (Lop) should be restricted to J for which Prµ[∩j∈JEj] > 0. However that restriction is ultimately unneces-


![image 20](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile20.png>)

sary because, in the context of the LLL, the theorem of Erd˝os and Spencer implies that Prµ[∩j∈[n]Ej] > 0.

![image 21](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile21.png>)

cannot be efﬁciently implemented due to the computational hardness. Therefore the equivalence between (LopA) and resampling oracles comes with no efﬁciency guarantees. Nevertheless in all lopsidependency scenarios that we have encountered in applications of the LLL, efﬁcient implementations of the resampling oracles arise naturally from existing work, or can be devised with modest effort. In particular this is the case for random permutations, perfect matchings in complete graphs, and spanning trees in complete graphs, as discussed in Section 3.

## 1.4 Generalizing the LLL criterion

In the early papers on the LLL [15, 37], the (GLL) criterion relating the dependency graph G and the probabilities Prµ[Ei] was shown to be a sufﬁcient condition to ensure that Prµ[ ni=1 Ei] > 0. Shearer [36] discovered a more general criterion that ensures the same conclusion. In fact, Shearer’s criterion is the best possible: whenever his criterion is violated, there exist a corresponding measure µ and events E1,... ,En for which Prµ[ ni=1 Ei] = 0.

![image 22](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile22.png>)

![image 23](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile23.png>)

Section 5 formally deﬁnes Shearer’s criterion and uses it in a fundamental way to prove Theorem 1.2. Moreover, we give an algorithmic proof of the LLL under Shearer’s criterion instead of the (GLL) criterion. This algorithm is efﬁcient in typical situations, although the efﬁciency depends on Shearer’s parameters. The following simpliﬁed result is stated formally and proven in Section 5.5.

Theorem (Informal). Suppose that a graph G and the probabilities Prµ[E1],... ,Prµ[En] satisfy Shearer’s criterion with ǫ slack, and that the three subroutines described in Section 1.1.1 are available. Then the

expected number of calls to the resampling oracles by MaximalSetResample is O(nǫ log 1ǫ).

![image 24](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile24.png>)

![image 25](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile25.png>)

We also prove a more reﬁned bound valid for any probabilities satisfying Shearer’s criterion. This bound is similar to the bound obtained by Kolipaka and Szegedy [24]; see Section 5.5 for details.

Unfortunately Shearer’s criterion is unwieldy and has not seen much use in applications of the LLL. Recently several researchers have proposed criteria of intermediate strength between (GLL) and Shearer’s criterion [8, 25]. The ﬁrst of these, called the cluster expansion criterion, was originally devised by Bissacot et al. [8], and is based on insights from statistical physics. This criterion has given improved results in several applications of the local lemma [9, 21, 31]. Previous algorithmic work has also used the cluster expansion criterion in the variable model [1, 33] and for permutations [21].

We give a new, elementary proof that the cluster expansion criterion implies Shearer’s criterion. In contrast, the previous proof is analytic and requires several ideas from statistical physics [8]. As a consequence, we obtain the ﬁrst purely combinatorial proof that the existential LLL holds under the cluster expansion criterion. Another consequence (Theorem 1.3) is an algorithm for the LLL under the cluster expansion criterion, obtained using our algorithmic results under Shearer’s criterion. This generalizes Theorem 1.2 by replacing (GLL) with the cluster expansion criterion, stated below as (CLL). To state the result, we require additional notation: let Ind denote the family of independent sets in the graph G.

- Theorem 1.3. Suppose that the events E1,... ,En satisfy the following criterion


∃y1,... ,yn > 0 such that Pr

[Ei] ≤

µ

yi J⊆Γ+(i),J∈Ind j∈J yj

. (CLL)

![image 26](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile26.png>)

and that the three subroutines described in Section 1.1.1 are available. Then the expected number of calls to the resampling oracles before MaximalSetResample terminates is O ni=1 yi nj=1 ln(1 + yj) .

## 1.5 Techniques and related work

The breakthrough work of Moser and Tardos [29, 30] stimulated a string of results on algorithms for the LLL. This section reviews the results that are most relevant to our work. Several interesting techniques play a role in the analyses of these previous algorithms. These can be roughly categorized as the entropy method [28, 2], witness trees or witness sequences [30, 21, 24] and forward-looking combinatorial analysis [19].

Moser [29, 28] developed the entropy method to analyze a very simple algorithm for the “symmetric” LLL [15], which incorporates the maximum degree of G and a uniform bound on Prµ[Ei]. The entropy method roughly shows that, if the algorithm runs for a long time, a transcript of the algorithm’s actions provides a compressed representation of the algorithm’s random bits, which is unlikely due to entropy considerations.

Following this, Moser and Tardos [30] showed that a similar algorithm will produce a state in ni=1 Ei, assuming the independent variable model and the (GLL) criterion. This paper is primarily responsible for the development of witness trees, and proved the “witness tree lemma”, which yields an extremely elegant analysis in the variable model. The witness tree lemma has further implications. For example, it allows one to analyze separately for each event its expected number of resamplings. Moser and Tardos also extended the variable model to incorporate a limited form of lopsidependency, and showed that their analysis still holds in that setting.

![image 27](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile27.png>)

The main advantage of our result over the Moser-Tardos result is that we address the occurrence of an event through the abstract notion of resampling oracles rather than directly resampling the variables of the variable model. Furthermore we give efﬁcient implementations of resampling oracles for essentially all known probability spaces to which the LLL has been applied. A signiﬁcant difference with our work is that we do not have an analogue of the witness tree lemma; our approach provides a simpler analysis when the LLL criterion has slack but requires a more complicated analysis to remove the slack assumption. As a consequence, our bound on the number of resampling oracle calls is larger than the Moser-Tardos bound. Our lack of a witness tree lemma is inherent. Appendix A shows that the witness tree lemma is false in the abstract scenario of resampling oracles.

The Moser-Tardos algorithm is known to terminate under criteria more general than (GLL), while still assuming the variable model. Pegden [33] showed that the cluster expansion criterion sufﬁces, whereas Kolipaka and Szegedy [24] showed more generally that Shearer’s criterion sufﬁces. We also extend our analysis to the cluster expansion criterion as well as Shearer’s criterion, in the more general context of resampling oracles. Our bounds on the number of resampling operations are somewhat weaker than those of [33, 24], but the increase is at most quadratic.

Kolipaka and Szegedy [24] present another algorithm, called GeneralizedResample, whose analysis proves the LLL under Shearer’s condition for arbitrary probability spaces. GeneralizedResample is similar to MaximalSetResample in that they both work with abstract distributions and that they repeatedly choose a maximal independent set J of undesired events to resample. However, the way that the bad events are resampled is different: GeneralizedResample needs to sample from µ|∩

j ∈Γ+(J)Ej, which is a complicated operation that seems difﬁcult to implement efﬁciently. Thus MaximalSetResample can be viewed as a variant of GeneralizedResample that can be made efﬁcient in all known scenarios.

![image 28](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile28.png>)

Harris and Srinivasan [21] show that the Moser-Tardos algorithm can be adapted to handle certain events in a probability space involving random permutations. Their method for resampling an event is based on the Fischer-Yates shufﬂe. This scenario can also be handled by our framework; their resampling method perfectly satisﬁes the criteria of a resampling oracle. The Harris-Srinivasan’s result is stronger than ours in that they do prove an analog of the witness tree lemma. Consequently their algorithm requires fewer resamplings than ours, and they are able to derive parallel variants of their algorithm. The work of Harris

and Srinivasan is technically challenging, and generalizing it to a more abstract setting seems daunting.

Achlioptas and Iliopoulos [2, 3] proposed a general framework for ﬁnding “ﬂawless objects”, based on actions for addressing ﬂaws. We call this the A-I framework. They show that, under certain conditions, a random walk over such actions rapidly converges to a ﬂawless object. This naturally relates to the LLL by viewing each event Ei as a ﬂaw. At the same time, the A-I framework is not tied to the probabilistic formulation of the LLL, and can derive results, such as the greedy algorithm for vertex coloring, that seem to be outside the scope of typical LLL formulations, such as Theorem 1.1. The A-I framework [2, 3] has other restrictions and does not claim to recover any particular form of the LLL. Nevertheless, the framework can accommodate applications of the LLL where lopsidependency plays a role, such as rainbow matchings and rainbow Hamilton cycles. In contrast, our framework embraces the probabilistic formulation and can recover the original existential LLL (Theorem 1.1) in full generality, even incorporating Shearer’s generalization. The A-I analysis [2] is inspired by Moser’s entropy method. Technically, it entails an encoding of random walks by “witness forests” and combinatorial counting thereof to estimate the length of the random walk. The terminology of witness forests is reminiscent of the witness trees of Moser and Tardos, but conceptually they are different in that the witness forests grow “forward in time” rather than backward. This is conceptually similar to “forward-looking combinatorial analysis”, which we discuss next.

Giotis et al. [19] show that a variant of Moser’s algorithm gives an algorithmic proof in the variable model of the symmetric LLL. While this result is relatively limited when compared to the results above, their analysis is a clear example of forward-looking combinatorial analysis. Whereas Moser and Tardos use a backward-looking argument to ﬁnd witness trees in the algorithm’s “log”, Giotis et al. analyze a forward-looking structure: the tree of resampled events and their dependencies, looking forward in time. This viewpoint seems more natural and suitable for extensions.

Our approach can be roughly described as forward-looking analysis with a careful modiﬁcation of the Moser-Tardos algorithm, formulated in the framework of resampling oracles. Our main conceptual contribution is the simple deﬁnition of the resampling oracles, which allows the resamplings to be readily incorporated into the forward-looking analysis. Our modiﬁcation of the Moser-Tardos algorithm is designed to combine this analysis with the technology of “stable set sequences” [24], deﬁned in Section 5.1, which allows us to accommodate various LLL criteria, including Shearer’s criterion. This plays a fundamental role in the full proof of Theorem 1.2.

Our second contribution is a technical idea concerning slack in the LLL criteria. This idea is a perfectly valid statement regarding the existential LLL as well, although we will exploit it algorithmically. One drawback of the forward-looking analysis is that it naturally leads to an exponential bound on the number of resamplings, unless there is some slack in the LLL criterion; this same issue arises in [2, 19]. Our idea eliminates the need for slack in the (GLL) and (CLL) criteria. We prove that, even if (GLL) or (CLL) are tight, we can instead perform our analysis using Shearer’s criterion, which is never tight because it deﬁnes an open set. For example, consider the familiar case of Theorem 1.1, and suppose that (GLL) holds with equality, i.e., Prµ[Ei] = xi j∈Γ(i)(1 − xj) for all i. We show that the conclusion of the LLL remains true even if each event Ei actually had the larger probability Prµ[Ei] · 1 + (2 i 1−xix

)−1 . The proof of this fact crucially uses Shearer’s criterion and it does not seem to follow from more elementary tools [15, 37].

![image 29](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile29.png>)

i

Follow-up work. Subsequently, Achlioptas and Iliopoulos generalized their framework further to incorporate our notion of resampling oracles [4]. This subsequent work can be viewed as a uniﬁcation of their framework and ours; it has the beneﬁt of both capturing the framework of resampling oracles and allowing some additional ﬂexibility (in particular, the possibility of regenerating the measure µ approximately rather than exactly). We remark that this work is still incomparable with ours, primarily due to the facts that our analysis is performed in Shearer’s more general setting, and that our algorithm is efﬁcient even when the

LLL criteria are tight.

Organization. The rest of the paper is organized as follows. In Section 2, we discuss the connection between resampling oracles and the assumptions of the Lov´asz Local Lemma. We also show here that resampling oracles as well as the LLL itself can be computationally hard in general. In Section 3, we show concrete examples of efﬁcient implementations of resampling oracles. In Section 4 we discuss several applications of these resampling oracles. Finally, in Section 5 we present the full analysis of our algorithm.

# 2 Resampling oracles: existence and efﬁciency

The algorithms in this paper make no reference to the lopsidependency condition (Lop) and instead assume the existence of resampling oracles. In Section 2.1 we show that there is a close relationship between these two assumptions: the existence of a resampling oracle for each event is equivalent to the condition (LopA), which is a strengthening of (Lop).

We should emphasize that the efﬁciency of an implementation of a resampling oracle is a separate issue. There is no general guarantee that resampling oracles can be implemented efﬁciently. Indeed, as we show in Section 2.2, there are applications of the LLL such that the resampling oracles are hard to implement efﬁciently, and ﬁnding a state avoiding all events is computationally hard, under standard computational complexity assumptions.

Nevertheless, this is not an issue in common applications of the LLL: resampling oracles exist and can be implemented efﬁciently in all uses of the LLL of which we are aware, even those involving lopsidependency. Section 3 has a detailed discussion of several scenarios.

## 2.1 Existence of resampling oracles

This section proves an equivalence lemma connecting resampling oracles with the notion of lopsided association. First, let us deﬁne formally what we call a resampling oracle.

- Deﬁnition 2.1. Let E1,... ,En be events on a space Ω with a probability measure µ, and let G = ([n],E) be a graph with neighbors of i ∈ [n] denoted by Γ(i). Let ri be a randomized procedure that takes a state ω ∈ Ω and outputs a state ri(ω) ∈ Ω. We say that ri is a resampling oracle for Ei with respect to G, if

- (R1) For ω ∼ µ|Ei, we obtain ri(ω) ∼ µ. (The oracle ri removes conditioning on Ei.)
- (R2) For any j ∈/ Γ+(i) = Γ(i) ∪ {i}, if ω  ∈ Ej then also ri(ω)  ∈ Ej. (Resampling an event cannot cause new non-neighbor events to occur.)


Next, let us deﬁne the notion of a lopsided association graph. We denote by Ei[ω] the {0,1}-valued function indicating whether Ei occurs at a state ω ∈ Ω.

- Deﬁnition 2.2. A graph G with neighborhood function Γ is a lopsided association graph for events E1,... ,En if


[F] ∀i ∈ [n],∀F ∈ Fi (LopA)

[Ei ∩ F] ≥ Pr

[Ei] · Pr

Pr

µ

µ

µ

where Fi contains all events F such that F[ω] is a monotone non-decreasing function of the functions (Ej[ω] : j ∈/ Γ+(i)).

- Lemma 2.3. Consider a ﬁxed i ∈ [n] and assume Prµ[Ei] > 0. The following statements are equivalent.


- (a) There exists a resampling oracle ri satisfying the conditions (R1) and (R2) with respect to a neighborhood Γ+(i) (ignoring issues of computational efﬁciency).
- (b) Prµ[Ei ∩ F] ≥ Prµ[Ei] · Prµ[F] for any event F ∈ Fi.


Corollary 2.4. Resampling oracles r1,... ,rn exist for events E1,... ,En with respect to a graph G if and only if G is a lopsided association graph for E1,... ,En. Both statements imply that the lopsidependency condition (Lop) holds.

Proof (of Lemma 2.3). (a) ⇒ (b): Consider the coupled states (ω,ω′) where ω ∼ µ|Ei and ω′ = ri(ω). By (R1), ω′ ∼ µ. For any event F ∈ Fi, if F does not occur at ω then it does not occur at ω′ either, due to (R2). This establishes that

[F] = Eω′∼µ[F[ω′]] ≤ Eω∼µ|Ei[F[ω]] = Pr

[F | Ei],

Pr

µ

µ

which implies Prµ[F ∩ Ei] ≥ Prµ[F] · Prµ[Ei]. In particular this implies (Lop), by taking F = j∈J Ej.

(b) ⇒ (a): We begin by formulating the existence of a resampling oracle as the following transportation problem. Consider a bipartite graph (U ∪ W,E), where U and W are disjoint, U represents all the states ω ∈ Ω satisfying Ei, and W represents all the states ω ∈ Ω. Edges represent the possible actions of the resampling oracle: (u,w) ∈ E if u satisﬁes every event among (Ej : j ∈/ Γ+(i)) that w satisﬁes. Each vertex has an associated weight: For w ∈ W, we deﬁne pw = Prµ[w], and for u ∈ U, pu = Prµ[u]/Prµ[Ei], i.e, pu is the probability of u conditioned on Ei. We claim that the resampling oracle ri exists if and only if there is an assignment fuw of values to the edges such that

w:(u,w)∈E fuw = pu ∀u ∈ U u:(u,w)∈E fuw = pw ∀w ∈ W

fuw ≥ 0 ∀u ∈ U, w ∈ W.

(1)

Such an assignment is called a feasible transportation. Given such a transportation, the resampling oracle is deﬁned naturally by following each edge from u ∈ U with probability fuw/pu, and the resulting distribution on W is pw. Conversely, for a resampling oracle which, for a given state u ∈ U, generates w ∈ W with probability quw, we deﬁne fuw = puquw. This assignment satisﬁes (1).

Our goal at this point is show that (b) implies feasibility of (1). A condition that is equivalent to (1), but more convenient for our purposes, can be determined from LP duality [34, Theorem 21.11]. A feasible transportation exists if and only if

- (2.1) u∈U pu = w∈W pw
- (2.2) u∈A pu ≤ w∈Γ(A) pw ∀A ⊆ U,


(2)

where Γ(A) = { w ∈ W : ∃u ∈ A s.t. (u,w) ∈ E }. This is an extension of Hall’s condition for the existence of a perfect matching.

Our goal at this point is show that (b) implies feasibility of (2). Let us now simplify (2). Fix any A ⊆ U. The neighborhood Γ(A) consists of states satisfying at most those events among { Ej : j ∈/ Γ+(i) } satisﬁed by some state in A. Thus Γ(A) corresponds to an event F′ such that F′[ω] is a non-increasing function of (Ej[ω] : j ∈/ Γ+(i)). Next observe that, if the set of events among { Ej : j ∈ Γ+(i) } satisﬁed by u′ ∈ U is a subset of those satisﬁed by u ∈ U, then Γ(u′) ⊆ Γ(u). Suppose that, for each u ∈ A, we add to A all such vertices u′. Doing so can only increase the left-hand side of (2.2), but does not increase the right-hand side as Γ(A) remains unchanged (since Γ(u′) ⊆ Γ(u)). Furthermore, the resulting set A

corresponds to the same event F′, but restricted to the states in U. Let us call such a set A non-increasing. Let (2∗) denote the simpliﬁcation of (2) in which we restrict to non-increasing A. We have argued that (2) and (2∗) are equivalent.

Our goal at this point is show that (b) implies feasibility of (2∗). One may easily see that (b) is equivalent to

![image 30](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile30.png>)

![image 31](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile31.png>)

[F ∩ Ei] ≤ Pr

[F] · Pr

[Ei] ∀F ∈ Fi.

Pr

µ

µ

µ

Assuming Pr[Ei] > 0, we can rewrite this as Prµ[F | Ei] ≤ Prµ[F] ∀F ∈ Fi. Now consider using this inequality with F = F′ for each F′ corresponding to some non-increasing set A ⊆ U. We then have

![image 32](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile32.png>)

![image 33](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile33.png>)

![image 34](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile34.png>)

Prµ[F′ | Ei] = u∈A pu and Prµ[F′] = w∈Γ(A) pw. This veriﬁes the feasibility of (2∗).

### 2.1.1 Example: monotone events on lattices

This section presents an example of a setting where Lemma 2.3 implies the existence of a non-trivial resampling oracle, even though the lopsided association graph is empty. This setting was previously known to have connections to the existential LLL [26]. The probability space here is Ω = {0,1}M, viewed in the natural way as the Boolean lattice with operations ∧ (meet) and ∨ (join), and with the partial order denoted ≥. Let µ : {0,1}M → [0,1] be a probability distribution, i.e., x∈{0,1}M µ(x) = 1. We assume that µ is log-supermodular, meaning that

µ(x ∨ y)µ(x ∧ y) ≥ µ(x)µ(y) ∀x,y ∈ {0,1}M.

As an example, any product distribution is log-supermodular. Consider monotone increasing events Ei, i.e., such that x′ ≥ x ∈ Ei ⇒ x′ ∈ Ei. Note that any monotone increasing function of such events is again monotone increasing. It follows directly from the FKG inequality [6] that condition (b) of Lemma 2.3 is satisﬁed for such events with an empty lopsided association graph. Therefore, a resampling oracle exists in this setting. However, the explicit description of its operation might be complicated and we do not know whether it can be implemented efﬁciently in general.

Alternatively, the existence of the resampling oracle can be proved directly, using a theorem of Holley [22, Theorem 6]. The resampling oracle is described in Algorithm 2. The reader can verify that this satisﬁes the assumptions (R1) and (R2), using Holley’s Theorem.

![image 35](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile35.png>)

- Algorithm 2 Resampling oracle for a monotone increasing event E. Let ν be the function guaranteed by


- Theorem 2.5 when µ1(x) = µ(x)1x∈E e∈E µ(e), µ2(y) = µ(y), and 1x∈E is the indicator function of x ∈ E.


![image 36](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile36.png>)

![image 37](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile37.png>)

- 1: Function rE(x):
- 2: If x  ∈ E, fail.
- 3: Randomly select y with probability ν(x,y) y′ ν(x,y′).

![image 38](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile38.png>)

- 4: return y.


![image 39](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile39.png>)

- Theorem 2.5 (Holley’s Theorem). Let µ1 and µ2 be probability measures on {0,1}M satisfying µ1(x ∨ y)µ2(x ∧ y) ≥ µ1(x)µ2(y) ∀x,y ∈ {0,1}M .


Then there exists a probability distribution ν : {0,1}M × {0,1}M → R satisfying

- µ1(x) = y ν(x,y)
- µ2(y) = x ν(x,y)


ν(x,y) = 0 unless x ≥ y.

## 2.2 Computational hardness of the LLL

This section considers whether the LLL can always be made algorithmic. We show that, even in fairly simple scenarios where the LLL applies, ﬁnding the desired output can be computationally hard, a fact that surprisingly seems to have been overlooked. We ﬁrst observe that the question of algorithmic efﬁciency must be stated carefully otherwise hardness is trivial.

A trivial example. Given a Boolean formula φ, let the probability space be Ω = {0,1}, and let µ be the uniform measure on Ω. There is a single event E1 deﬁned to be E1 = {1} if φ is satisﬁable, and E1 = {0} if φ is not satisﬁable. Since Pr[E1] = 1/2, the (GLL) criterion holds trivially with x1 = 1/2. The LLL gives the obvious conclusion that there is a state ω ∈/ E. Yet, ﬁnding this state requires deciding satisﬁability of φ, which is NP-complete.

The reason that this example is trivial is that even deciding whether the undesired event has occurred is computationally hard. A more meaningful discussion of LLL efﬁciency ought to rule out this trivial example by considering only scenarios that satisfy some reasonable assumptions. With that in mind, we will assume that

- • there is a probability space Ω, whose states can be described by m bits;
- • a graph G satisfying (Dep) for events E1,... ,En is explicitly provided;
- • x1,... ,xn ∈ (0,1) satisfying the (GLL) conditions are provided, and ni=1 1−xix

![image 40](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile40.png>)

i

is at most poly(n);

- • there is a subroutine that provides an independent random state ω ∼ µ in poly(m) time;
- • for each i ∈ [n], there is a subroutine which determines for any given ω ∈ Ω whether ω ∈ Ei, in poly(m) time.


As far as we know, no prior work refutes the possibility that there is an algorithmic form of the LLL, with running time poly(m,n), in this general scenario.

Our results imply that resampling oracles do exist in this general scenario, so it is only the question of whether these resampling oracles are efﬁcient that prevents Theorem 1.2 from providing an efﬁcient algorithm. Nevertheless, we show that there is an instance of the LLL that satisﬁes the reasonable assumptions stated above, but for which ﬁnding a state in i Ei requires solving a problem that is computationally hard (under standard computational complexity assumptions). As a consequence, we conclude that the resampling oracles cannot always be implemented efﬁciently, even under the reasonable assumptions of this general scenario.

![image 41](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile41.png>)

We remark that NP-completeness is not the right notion of hardness here [32]. Problems in NP involve deciding whether a solution exists, whereas the LLL guarantees that a solution exists, and the goal is to explicitly ﬁnd a solution. Our result is instead based on hardness of the discrete logarithm problem, a standard belief in computational complexity theory. In the following, GF(pn) for a prime p and integer n denotes a ﬁnite ﬁeld of order pn, and GF∗(pn) its multiplicative group of nonzero elements.

- Theorem 2.6. There are instances of events E1,... ,En on a probability space Ω = {0,1}n under the uniform probability measure, such that


- • the events Ei are mutually independent;


- • for each i ∈ [n], the condition ω ∈ Ei can be checked in poly(n) time for given ω ∈ Ω;
- • the (GLL) conditions are satisﬁed with xi = 1/2 for each i ∈ [n];


but ﬁnding a state in ni=1 Ei is as hard as solving the discrete logarithm problem in GF∗(2n).

![image 42](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile42.png>)

Remark. Superﬁcially, this result seems to contradict the fact that the LLL can be made algorithmic in the variable model [30], where events are deﬁned on underlying independent random variables. The key point is that the variable model also relies on a particular type of dependency graph (deﬁned by shared variables) which might be more conservative than the true dependencies between the events. Theorem 2.6 shows that, even if the probability space consists of independent {0,1} random variables, the LLL cannot in general be made algorithmic if the true dependencies are considered.

Proof. Consider an instance of the discrete logarithm problem in the multiplicative group GF∗(2n). The input is a generator g of GF∗(2n) and an element h ∈ GF∗(2n). The goal is to ﬁnd an integer 1 ≤ k ≤ 2n−1 such that gk = h. We deﬁne an instance of n events on Ω = {0,1}n as follows.

We identify Ω = {0,1}n with [2n] as well as GF(2n) in a natural way. We deﬁne f : [2n] → GF(2n) by f(0) = 0 and f(x) = gx for x = 0, where the exponentiation is performed in GF(2n). For each i ∈ [n], we deﬁne an event Ei that occurs for ω ∈ {0,1}n iff (f(ω))i = 1 − hi. This is a condition that can be checked in time poly(n), by computing f(ω) = gω where we interpret ω as i n=0−1 ωi2i and compute gω by taking squares iteratively.

Observe that for ω distributed uniformly in Ω = {0,1}n, f(ω) is again distributed uniformly in Ω, since f is a bijection (0 is mapped to 0, and f(ω) for ω = 0 generates each element of the multiplicative group GF∗(2n) exactly once). Therefore, the probability of Ei is 1/2, for each i ∈ [n]. Further, the events E1,... ,En are mutually independent, since for any J ⊆ [n], j∈J Ej∩ j′∈/J Ej′ occurs iff f(ω) = h⊕1J, which happens with probability 1/2n. Here 1J ∈ {0,1}n is the indicator vector for the set J, and ⊕ denotes addition in GF(2n) (i.e., component-wise xor in {0,1}n). Hence the dependency graph is empty, and the LLL with parameters xi = 1/2 trivially implies that there exists a state ω avoiding all the events. In this instance, we know explicitly that the state avoiding all the events is f−1(h). Therefore, if we had an efﬁcient algorithm to ﬁnd this point for any given h ∈ GF∗(2n), we would also have an efﬁcient algorithm for the discrete logarithm problem in GF(2n).

![image 43](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile43.png>)

![image 44](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile44.png>)

![image 45](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile45.png>)

![image 46](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile46.png>)

![image 47](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile47.png>)

# 3 Implementation of resampling in speciﬁc settings

In this section, we present efﬁcient implementations of resampling oracles in four application settings: independent random variables (which was the setting of [30]), random permutations (handled by [21]), perfect matchings in complete graphs (some of whose applications are made algorithmic by [2]), and spanning trees in complete graphs (which is a new scenario that we can handle). To be more precise, resampling oracles also depend on the types of events and dependencies that we want to handle.2 In the setting of independent random variables, we can handle arbitrary events with dependencies deﬁned by overlapping relevant variables, just like [30]. In the setting of permutations, we handle the appearance of patterns in permutations as in [21]. In the settings of matchings and spanning trees, we consider the “canonical events” deﬁned by [26], characterized by the appearance of a certain subset of edges. We also show in Section 3.5 how resampling oracles for a certain probability space can be extended in a natural way to products of such probability spaces (for example, how to go from resampling oracles for one random permutation to a collection of independent random permutations). These settings cover all the applications of the lopsided LLL that we are aware of.

![image 48](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile48.png>)

2In Section 2.2 we give an example of events on independent random variables for which resampling oracles exist but cannot be made efﬁcient.

## 3.1 The variable model

This is the most common setting, considered originally by Moser and Tardos [30]. Here, Ω has a product structure corresponding to independent random variables { Xa : a ∈ U }. The probability measure µ here is a product measure. Each bad event Ei depends on a particular subset of variables Ai, and two events are independent iff Ai ∩ Aj = ∅.

Here our algorithmic assumptions correspond exactly to the Moser-Tardos framework [30]. Sampling from µ means generating a fresh set of random variables independently. The resampling oracle ri takes a state ω and replaces the random variables { Xa : a ∈ Ai } by fresh random samples. It is easy to see that the assumptions are satisﬁed: in particular, a random state sampled from µ conditioned on Ei has all variables outside of Ai independently random. Hence, resampling the variables of Ai produces the distribution µ. Clearly, resampling { Xa : a ∈ Ai } does not affect any events whose variables do not intersect Ai.

We note that this resampling oracle is also consistent with the notion of lopsidependency on product spaces considered by [30]: They call two events Ei,Ej lopsidependent, if Ai ∩ Aj = ∅ and it is possible to cause Ej to occur by resampling Ai in a state where Ei holds but Ej does not (the deﬁnition in [30] is worded differently but equivalent to this). This is exactly the condition that we require our resampling oracle to satisfy.

## 3.2 Permutations

The probability space Ω here is the space of all permutations π on a set [n], with a uniform measure µ. The bad events are assumed to be “simple” in the following sense: Each bad event Ei is deﬁned by a “pattern” P(Ei) = {(x1,y1),... ,(xt(i),yt(i))}. The event Ei occurs if π(xj) = yj for each 1 ≤ j ≤ t(i). Let vbl(Ei) = { x : ∃y,(x,y) ∈ P(Ei) } denote the variables of π relevant to event Ej. Let us deﬁne a relation i ∼ i′ to hold iff there are pairs (x,y) ∈ P(Ei),(x′,y′) ∈ P(Ei′) such that x = x′ or y = y′; i.e., the two events entail the same value in either the range or domain. This relation deﬁnes a lopsidependency graph. It is known that the lopsided LLL holds in this setting.

- Algorithm 3 Resampling oracle for permutations


![image 49](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile49.png>)

![image 50](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile50.png>)

- 1: Function ri(π):
- 2: X := vbl(Ei), i.e., the variables in π affecting event Ei;
- 3: Fix an arbitrary order X = (x1,x2,... ,xt);
- 4: for i = t down to 1 do
- 5: Swap π(xi) with π(z) for z uniformly random among [n] \ {x1,... ,xi−1};
- 6: end for
- 7: return π;


![image 51](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile51.png>)

Harris and Srinivasan [21] showed how, under the LLL criteria, a permutation avoiding all bad events can be found algorithmically. We implement the resampling oracle based on their algorithm (see Algorithm 3). To prove the correctness of this resampling oracle within our framework, we need the following lemma.

- Lemma 3.1. Suppose that a permutation π has some arbitrary ﬁxed assignment on the variables in X,


π|X = φ, and it is uniformly random among all permutations satisfying π|X = φ. Then the output of Shufﬂe(π,X) is a uniformly random permutation.

The procedure is known as the Fisher-Yates shufﬂe for generating uniformly random permutations (and was used in [21] as well). In contrast to the full shufﬂe, we assume that some part of the permutation has

been shufﬂed already: X is the remaining portion that still remains to be shufﬂed, and conditioned on its assignment the rest is uniformly random. This would be exactly the distribution achieved after performing the Fisher-Yates shufﬂe on the complement of X. Our procedure performs the rest of the Fisher-Yates shufﬂe, which produces a uniformly random permutation. For completeness we give a self-contained proof.

Proof. Let X = {x1,... ,xt}. By induction, after performing the swap for xi, the permutation is uniform among all permutations with a ﬁxed assignment of {x1,... ,xi−1} (consistent with φ). This holds because, before the swap, the permutation was by induction uniform conditioned on the assignment of {x1,... ,xi} being consistent with φ, and we choose a uniformly random swap for xi among the available choices. This makes every permutation consistent with φ on {x1,... ,xi−1} equally likely after this swap.

![image 52](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile52.png>)

![image 53](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile53.png>)

![image 54](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile54.png>)

![image 55](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile55.png>)

This veriﬁes the ﬁrst condition for our resampling oracle. The second condition is that resampling of occurring events does not affect non-neighbor events. This is true because of the following lemma.

- Lemma 3.2. The resampling oracle ri(π) applied to a permutation satisfying Ei does not cause any new event outside of Γ+(I) to occur.

Proof. Suppose Ej changed its status during a call to ri(π). This means that something changed among its relevant variables vbl(Ej). This could happen in two ways:

- (1) either a variable z ∈ vbl(Ej) was swapped because z ∈ X = vbl(Ei); then clearly j ∈ Γ+(i).
- (2) or, a variable in vbl(Ej), although outside of X, received a new value by a swap with some variable


in X = vbl(Ei). Note that in the Shufﬂe procedure, every time a variable z outside of X changes its value, it is by a swap with a fresh variable of X, i.e. one that had not been processed before. Therefore, the value that z receives is one that previously caused Ei to occur. If it causes Ej to occur, it means that Ei and Ej share a value in the range space and we have j ∈ Γ+(i) as well.

![image 56](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile56.png>)

![image 57](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile57.png>)

![image 58](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile58.png>)

![image 59](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile59.png>)

3.3 Perfect matchings

Here, the probability space Ω is the set of all perfect matchings in K2n, with the uniform measure. This is a setting considered by [2] and it is also related to the setting of permutations. (Permutations on [n] can be viewed as perfect matchings in Kn,n.) A state here is a perfect matching in K2n, which we denote by M ∈ Ω. We consider bad events of the following form: EA for a set of edges A occurs if A ⊆ M. Obviously, Prµ[EA] > 0 only if A is a (partial) matching. Let us deﬁne A ∼ B iff A ∪ B is not a matching. It was proved in [26] that this deﬁnes a lopsidependency graph.

Our goal is to implement a resampling oracle in this setting. We describe such an operation in Algorithm 4.

- Lemma 3.3. Let A be a matching in K2n and let M be distributed uniformly among perfect matchings in K2n such that A ⊆ M. Then after calling the resampling oracle, rA(M) is a uniformly random perfect matching.


Proof. We prove by induction that at any point, M′ is a uniformly random perfect matching conditioned on containing A′. This is satisﬁed at the beginning: M′ = M,A′ = A and M is uniformly random conditioned on A ⊆ M.

Assume this is true at some point, we pick (u,v) ∈ A′ arbitrarily and (x,y) ∈ M′ \ A′ uniformly at random. Denote the vertices covered by M′\A′ by V (M′\A′). Observe that for a uniformly random perfect matching on V (M′ \ A′) ∪ {u,v}, the edge (u,v) should appear with probability 1/(2|M′ \ A′| + 1) since u has 2|M′ \ A′| + 1 choices to be matched with and v is 1 of them. Consequently, we keep the edge (u,v)

- Algorithm 4 Resampling oracle for perfect matchings


![image 61](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile61.png>)

- 1: Function rA(M):
- 2: Check that A ⊆ M, otherwise return M.
- 3: A′ := A;
- 4: M′ := M;
- 5: while A′ = ∅ do
- 6: Pick (u,v) ∈ A′ arbitrarily;
- 7: Pick (x,y) ∈ M′ \ A′ uniformly at random, with (x,y) randomly ordered;
- 8: With probability 1 − 2|M′\1A′|+1,

![image 62](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile62.png>)

- 9: Add (u,y),(v,x) to M′ and remove (u,v),(x,y) from M′;
- 10: Remove (u,v) from A′;
- 11: end while
- 12: return M′.


![image 63](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile63.png>)

with probability 1/(2|M′ \ A′| + 1) and conditioned on this M′ \ A′ is uniformly random by the inductive hypothesis. Conditioned on (u,v) not being part of the matching, we re-match (u,v) with another random edge (x,y) ∈ M′ \ A′ where (x,y) is randomly ordered. In this case, u and v get matched to a uniformly random pair of vertices x,y ∈ V (M′ \ A′), as they should be. The rest of the matching M′ \ A′ \ {(x,y)} is uniformly random on V (M′ \ A′ \ {x,y}) by the inductive hypothesis.

Therefore, after each step M′\A′ is uniformly random conditioned on containing A′. At the end, A′ = ∅ and M′ is uniformly random.

![image 64](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile64.png>)

![image 65](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile65.png>)

![image 66](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile66.png>)

![image 67](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile67.png>)

- Lemma 3.4. The resampling oracle rA(M) applied to a perfect matching satisfying event EA does not cause any new event EB such that B ∈/ Γ+(A).

Proof. Observe that all the new edges that the resampling oracle adds to M are incident to some vertex matched by A. So if an event EB was not satisﬁed before the operation and it is satisﬁed afterwards, it must be the case that B contains some edge not present in A but sharing a vertex with A. Hence, A ∪ B is not a matching and A ∼ B.

![image 68](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile68.png>)

![image 69](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile69.png>)

![image 70](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile70.png>)

![image 71](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile71.png>)

3.4 Spanning trees

Here, the probability space Ω is the set of all spanning trees in Kn. Let us consider events EA for a set of edges A, where EA occurs for T ∈ Ω iff A ⊆ T. Deﬁne A ∼ B for distinct A,B unless A and B are vertex-disjoint. Lu et al. [26, Lemma 7] show that this in fact deﬁnes a dependency graph for spanning trees. It is worth emphasizing that in this scenario the (Dep) condition holds (the more general condition (Lop) is not needed), but the scenario does not fall within the scope of the Moser-Tardos variable model. It does fall within the scope of our framework, but one must design a non-trivial resampling oracle.

To implement a resampling oracle in this setting, we will use as a subroutine an algorithm to generate a uniformly random spanning tree in a given graph G. This can be done efﬁciently by several methods, for example by a random walk [10].

- Lemma 3.5. If A is a ﬁxed forest and T is a uniformly random spanning tree in Kn conditioned on A ⊆ T, then rA(T) produces a uniformly random spanning tree in Kn.


- Algorithm 5 Resampling oracle for spanning trees


![image 73](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile73.png>)

- 1: Function rA(T):
- 2: Check that A ⊆ T, otherwise fail.
- 3: Let W = V (A), the vertices covered by A.
- 4: Let T1 = V \2W ∩ T, the edges of T disjoint from W.
- 5: Let F1 = V \2W \ T, the edges disjoint from W not present in T.
- 6: Let G2 = (Kn \ F1)/T1 be a multigraph obtained by deleting F1 and contracting T1.
- 7: Generate a uniformly random spanning tree T2 in G2.
- 8: return T1 ∪ T2.


![image 74](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile74.png>)

Proof. First, observe that since T2 is a spanning tree of G2 = (Kn \ F1)/T1, it is also a spanning tree of Kn/T1 where T1 is a forest, and therefore T1 ∪ T2 is a spanning tree of Kn. We need to prove that it is a uniformly random spanning tree.

First, we appeal to a known result [26, Lemma 6] stating that given a forest F in Kn with components of sizes (number of vertices) f1,f2,... ,fm, the number of spanning trees containing F is exactly

m

fi nfi−1. (3)

nn−2

![image 75](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile75.png>)

i=1

Equivalently (since nn−2 is the total number of spanning trees), for a uniformly random spanning tree T, Pr[F ⊆ T] = mi=1 fi/nfi−1. This has the surprising consequence that for vertex-disjoint forests F1,F2, we have Pr[F1 ∪ F2 ⊆ T] = Pr[F1 ⊆ T] · Pr[F2 ⊆ T], i.e., the containment of F1 and F2 are independent events. (In a general graph, the appearances of different edges in a random spanning tree are negatively correlated, but here we are in a complete graph.)

Let W = V (A) and let B be any forest on V \ W, i.e., vertex-disjoint from A. By the above, the appearance of B in a uniformly random spanning tree is independent of the appearance of A. Hence, if T is uniformly random, we have Pr[B ⊆ T | A ⊆ T] = Pr[B ⊆ T]. This implies that the distribution of T ∩ V \2W is exactly the same for a uniformly random spanning tree T as it is for one conditioned on A ⊆ T (formally, by applying the inclusion-exclusion formula). Therefore, the forest T1 = T ∩ V\2W is distributed as it should be in a random spanning tree restricted to V \ W.

The ﬁnal step is that we extend T1 to a spanning tree T1 ∪ T2, where T2 is a uniform spanning tree in G2 = (Kn \ F1)/T1. Note that G2 is a multigraph, i.e., it is important that we preserve the multiplicity of edges after contraction. The spanning trees T2 in G2 = (Kn \ F1)/T1 are in a one-to-one correspondence with spanning trees in Kn conditioned on T ∩ V \2W = T1. This is because each such tree T2 extends T1 to a different spanning tree of Kn, and each spanning tree where T ∩ V \2W = T1 can be obtained in this way. Therefore, for a ﬁxed T1, T1 ∪ T2 is a uniformly random spanning tree conditioned on T ∩ V\2W = T1. Finally, since the distribution of T1 is equal to that of a uniformly random spanning tree restricted to V \W, T1 ∪ T2 is a uniformly random spanning tree.

![image 76](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile76.png>)

![image 77](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile77.png>)

![image 78](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile78.png>)

![image 79](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile79.png>)

- Lemma 3.6. The resampling oracle rA(T) applied to a spanning tree satisfying EA does not cause any new event EB such that B ∈/ Γ+(A).


Proof. Note that the only edges that we modify are those incident to W = V (A). Therefore, any new event EB that the operation of rA could cause must be such that B contains an edge incident to W and not contained in A. Such an edge shares exactly one vertex with some edge in A and hence B ∼ A.

![image 80](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile80.png>)

![image 81](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile81.png>)

![image 82](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile82.png>)

![image 83](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile83.png>)

## 3.5 Composition of resampling oracles for product spaces

Suppose we have a product probability space Ω = Ω1×Ω2×...×ΩN, where on each Ωi we have resampling oracles rij for events Eij,j ∈ Ei, with respect to a graph Gi. Our goal is to show that there is a natural way to combine these resampling oracles in order to handle events on Ω that are obtained by taking intersections of the events Eij. The following theorem formalizes this notion.

- Theorem 3.7. Let Ω1,... ,ΩN be probability spaces, where for each Ωi we have resampling oracles rij for events Eij,j ∈ Ei with respect to a graph Gi. Let Ω = Ω1 × Ω2 × ... ΩN be a product space with the respective product probability measure. For any set J of pairs (i,j),j ∈ Ei where each i ∈ [N] appears at most once, deﬁne an event EJ on Ω to occur in a state ω = (ω1,... ,ωN) iff Eij occurs in ωi for each (i,j) ∈ J. Deﬁne a graph G on these events by J ∼ J′ iff there exist pairs (i,j) ∈ J,(i,j′) ∈ J′ such that j ∼ j′ in Gi. Then there exist resampling oracles rJ for the events EJ with respect to G, which are obtained by calling in succession each of the oracles rij for (i,j) ∈ J.

Proof. For notational simplicity, let us assume that on each Ωi we have a trivial event Ei0 = Ωi and the respective resampling oracle ri0 is the identity on Ωi. Then we can assume that each collection of events J is in the form J = {(1,j1),(2,j2),... ,(N,jN)}, where we set jℓ = 0 for components where there is no event to resample. We deﬁne

rJ(ω1,... ,ωN) = (r1j1(ω1),r2j2(ω2),... ,rNjN(ωN)). We claim that these are resampling oracles with respect to G as deﬁned in the theorem.

Let us denote by µi the probability distribution on Ωi and by µ the product distribution on Ω. For the ﬁrst condition, suppose that ω ∼ µ|EJ. By the product structure of Ω, this is the same as having ω = (ω1,... ,ωN) where the components are independent and ωℓ ∼ µℓ|Eℓj

ℓ

for each (ℓ,jℓ) ∈ J, and ωℓ ∼ µℓ for components such that jℓ = 0. By the properties of the resampling oracles rℓjℓ, we have rℓjℓ(ωℓ) ∼ µℓ. Since the resampling oracles are applied with independent randomness for each component, we have

rJ(ω) = (r1j1(ω1),r2j2(ω2),... ,rNjN(ωN)) ∼ µ1 × µ2 × ... × µN = µ.

For the second condition, note that if ω ∈/ EJ′ and rJ(ω) ∈ EJ′, it must be the case that there is (ℓ,jℓ) ∈ J and (ℓ,jℓ′) ∈ J′ such that ωℓ ∈/ Eℓj′

ℓ

and rℓjℓ(ω) ∈ Eℓj′

ℓ

. However, this is possible only if jℓ ∼ jℓ′ in the graph Gℓ. By the deﬁnition of G, this means that J ∼ J′ as well.

![image 84](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile84.png>)

![image 85](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile85.png>)

![image 86](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile86.png>)

![image 87](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile87.png>)

As a result, we can extend our resampling oracles to spaces like N-tuples of independent random permutations, independent random spanning trees, etc. Such extensions are used in our applications.

4 Applications

Let us present a few applications of our framework. Our application to rainbow spanning trees is new, even in the existential sense. Our applications to Latin transversals and rainbow matchings are also new to the best of our knowledge, although they could also have been obtained using the framework of [21] and [2].

- 4.1 Rainbow spanning trees


Given an edge-coloring of Kn, a spanning tree is called rainbow if each of its edges has a distinct color. The existence of a single rainbow spanning tree is completely resolved by the matroid intersection theorem: It

can be decided efﬁciently whether a rainbow spanning tree exists for a given edge coloring, and it can be found efﬁciently if it exists. However, the existence of multiple edge-disjoint rainbow spanning trees is more challenging. An attractive conjecture of Brualdi and Hollingsworth [11] states that if n is even and Kn is properly edge-colored by n − 1 colors, then the edges can be decomposed into n/2 rainbow spanning trees, each tree using each color exactly once. Until recently, it was only known that every such edge-coloring contains 2 edge-disjoint rainbow spanning trees [5]. In a recent development, it was proved that if every color is used at most n/2 times (which is true for any proper coloring) then there exist Ω(n/log n) edgedisjoint rainbow spanning trees [12]. In fact this result seems to be algorithmically efﬁcient, although this was not claimed by the authors. We prove that using our framework, we can ﬁnd Ω(n) rainbow spanning trees under a slight strengthening of the coloring assumption.

- Theorem 4.1. Given an edge-coloring of Kn such that each color appears on at most 321 (87)7n edges, at


![image 88](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile88.png>)

![image 89](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile89.png>)

least 321 (78)7n edge-disjoint rainbow spanning trees exist and can be found in O(n4) resampling oracle calls with high probability.

![image 90](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile90.png>)

![image 91](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile91.png>)

This result relies on Theorem 1.3, our algorithmic version of the LLL under the cluster expansion criterion. To obtain the result with high probability, we appeal to a more reﬁned bound that we state in Theorem 5.44. We note that if there is constant multiplicative slack in the assumption on color appearances, the number of resamplings improves to O(n2), using the result in Theorem 5.44 with constant ǫ slack.

To prove the existential statement, we simply sample 321 (78)7n independently random spanning trees and hope that they will be (a) pairwise edge-disjoint, and (b) rainbow. This unlikely proposition happens to be true with positive probability, thanks to the LLL and the independence properties of random spanning trees that we mentioned in Section 3.4. Given this setup, our framework implies that we can also ﬁnd the rainbow trees efﬁciently.

![image 92](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile92.png>)

![image 93](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile93.png>)

Proof. We apply our algorithm in the setting of t independent and uniformly random spanning trees T1,... ,Tt ⊂ Kn, with the following two types of bad events:

- • Eefi : For each i ∈ [t] and two edges e = f in Kn of the same color, Eefi occurs if {e,f} ⊂ Ti;
- • Eeij: For each i = j ∈ [t] and an edge e in Kn, Eeij occurs if e ∈ Ti ∩ Tj.


Clearly, if no bad event occurs then the t trees are rainbow and pairwise edge-disjoint.

By (3) the probability of a bad event of the ﬁrst type is Pr[Eefi ] = 3/n2 if |e ∪ f| = 3 and Pr[Eefi ] = 4/n2 if |e ∪ f| = 4. The probability of a bad event of the second type is Pr[Eeij] = (2/n)2 = 4/n2, since each of the two trees contains e independently with probability 2/n. Hence, the probability of each bad event is upper-bounded by p = 4/n2.

In Section 3.4 we constructed a resampling oracle rA for a single spanning tree. By Theorem 3.7, this resampling oracle extends in a natural way to the setting of t independent random spanning trees. In particular, for an event Eefi , we deﬁne refi as an application of the resampling oracle r{e,f} to the tree Ti. For an event Eeij, we deﬁne reij as an application of the resampling oracle r{e} independently to the trees Ti and Tj. It is easy to check using Theorem 3.7 that for independent uniformly random spanning trees conditioned on either type of event, the respective resampling oracle generates independent uniformly random spanning trees.

Let us deﬁne the following dependency graph; we are somewhat conservative for the sake of simplicity. The graph contains the following kinds of edges:

- • Eefi ∼ Eei′f′ whenever e ∪ f intersects e′ ∪ f′;


- • Eefi ,Eefj ∼ Eeij′ whenever e′ intersects e ∪ f;
- • Eeij ∼ Eij


′j

′

e′ ,Ei

e′ whenever e′ intersects e.

We claim that the resampling oracle for any bad event can cause new bad events only in its neighborhood. This follows from the fact that the resampling oracle affect only the trees relevant to the event (in the superscript), and the only edges modiﬁed are those incident to those relevant to the event (in the subscript).

Let us now verify the cluster expansion criterion, introduced as (CLL) in Section 1.4, so that we may apply Theorem 5.44. Let us assume that each color appears on at most q edges, and we generate t random spanning trees. We claim that the neighborhood of each bad event can be partitioned into 4 cliques of size (n − 1)(t − 1) and 4 cliques of size (n − 1)(q − 1).

First, let us consider an event of type Eefi . The neighborhood of Eefi consists of: (1) events Eei′f′ where e′ or f′ shares a vertex with e ∪ f; these events form 4 cliques, one for each vertex of e ∪ f, and the size of each clique is at most (n−1)(q−1), since the number of incident edges to a vertex is n−1, and the number of other edges of the same color is at most q − 1. (2) events Eeij′ where e′ intersects e ∪ f; these events form

- 4 cliques, one for each vertex of e ∪ f, and each clique has size at most (n − 1)(t − 1), since its events can be identiﬁed with the (n − 1) edges incident to a ﬁxed vertex and the remaining t − 1 trees.


Second, let us consider an event of type Eeij. The neighborhood of Eeij consists of: (1) events Eei′f′ and

Eej′f′ where e intersects e′ ∪ f′; these events form 4 cliques, one for each vertex of e and either i or j in the superscript, and the size of each clique is at most (n − 1)(q − 1) by an argument as above. (2) events

Eei′′j,Eeij′′ where e′ intersects e; these events form 4 cliques, one for each vertex of e and either i′j or ij′ in the superscript. The size of each clique is at most (n − 1)(t − 1), since the events can be identiﬁed with the

(n − 1) edges incident to a vertex and the remaining t − 1 trees.

Considering the symmetry of the dependency graph, we set the variables for all events equal to yefi = yeij = y. The cluster expansion criteria will be satisﬁed if we set the parameters so that

y (1 + (n − 1)(t − 1)y)4(1 + (n − 1)(q − 1)y)4

p ≤

![image 94](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile94.png>)

y I⊆Γ+(E),I∈Ind yI

≤

,

![image 95](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile95.png>)

where E denotes either Eefi or Eeij. The second inequality holds due to the structure of the neighborhood of each event that we described above. We set y = βp = 4β/n2 and assume t ≤ γn,q ≤ γn. The reader can

verify that with the settings β = (87)8 and γ = 321 (78)7, we get (1+4βγβ)8 = 1. Therefore,

![image 96](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile96.png>)

![image 97](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile97.png>)

![image 98](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile98.png>)

![image 99](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile99.png>)

βp (1 + 4γβ)8

≤

p ≤

![image 100](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile100.png>)

y (1 + (n − 1)(t − 1)y)4(1 + (n − 1)(q − 1)y)4

![image 101](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile101.png>)

which veriﬁes the assumption of Theorem 5.44. Theorem 5.44 implies that MaximalSetResample terminates after O(( yefi + yeij)2) resampling oracle calls with high probability. The total number of events here is O(tqn2) = O(n4) and for each event the respective variable is y = O(1/n2). Therefore, the expected number of resampling oracle calls is O(n4).

![image 102](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile102.png>)

![image 103](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile103.png>)

![image 104](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile104.png>)

![image 105](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile105.png>)

## 4.2 Rainbow matchings

Given an edge-coloring of K2n, a perfect matching is called rainbow if each of its edges has a distinct color. This can be viewed as a non-bipartite version of the problem of Latin transversals. It is known that given any proper (2n − 1)-edge-coloring of K2n (where each color forms a perfect matching), there exists a rainbow perfect matching [38]. However, ﬁnding rainbow matchings algorithmically is more difﬁcult. Achlioptas

and Iliopoulos [2] showed how to ﬁnd a rainbow matching in K2n efﬁciently when each color appears on at most γn edges, γ < 21e ≃ 0.184. Our result is that we can do this for γ = 12827 ≃ 0.211. The improvement comes from the application of the “cluster expansion” form of the local lemma, which is still efﬁcient in our framework. (We note that an updated version of the Achlioptas-Iliopoulos framework [3] also contains this result.)

![image 106](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile106.png>)

![image 107](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile107.png>)

- Theorem 4.2. Given an edge-coloring of K2n where each color appears on at most 12827 n edges, a rainbow perfect matching exists and can be found in O(n2) resampling oracle calls with high probability.

![image 108](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile108.png>)

In fact, we can ﬁnd many disjoint rainbow matchings — up to a linear number, if we replace 12827 above by a smaller constant.

![image 109](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile109.png>)

- Theorem 4.3. Given an edge-coloring of K2n where each color appears on at most 8787n edges, at least 7878n edge-disjoint rainbow perfect matchings exist and can be found in O(n4) resampling oracle calls whp.


![image 110](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile110.png>)

![image 111](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile111.png>)

We postpone the proof to Section 4.3, since it follows from our result for Latin transversals.

Proof of Theorem 4.2. We apply our algorithm in the setting of uniformly random perfect matchings M ⊂ K2n, with the following bad events (identical to the setup in [2]): For every pair of edges e,f of the same color, Eef occurs if {e,f} ⊂ M. If no bad event Eef occurs then M is a rainbow matching. We also deﬁne the following dependency graph: Eef ∼ Ee′f′ unless e,f,e′,f′ are four disjoint edges. Note that this is more conservative than the dependency graph we considered in Section 3.3, where two events are only connected if they do not form a matching together. The more conservative deﬁnition will simplify our analysis. In any case, our resampling oracle is consistent with this lopsidependency graph in the sense that resampling Eef can only cause new events Ee′f′ such that Eef ∼ Ee′f′. We show that this setup satisﬁes the criteria of the cluster expansion lemma.

Let q = 12827 n, p = (2n−1)(21 n−3) and y = (43)4p. Consider the neighborhood of a bad event Γ(Eef). It contains all events Ee′f′ such that there is some intersection among the edges e,f,e′,f′. Such events can be partitioned into 4 cliques: for each vertex v ∈ e ∪ f, let Qv denote all the events Ee′f′ such that v ∈ e′ and f′ has the same color as e′. The number of edges e′ incident to v is 2n − 1, and for each of them, the number of other edges of the same color is by assumption at most q −1. Therefore, the size of Qv is at most (q − 1)(2n − 1).

![image 112](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile112.png>)

![image 113](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile113.png>)

![image 114](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile114.png>)

In the following, we use the short-hand notation yI = i∈I yi. Consider the assumptions of the cluster expansion lemma: for each event Eef, we should have

yef I⊆Γ+(Eef),I∈Ind yI

Pr[Eef] ≤

.

![image 115](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile115.png>)

We have Pr[Eef] = p = (2n−1)(21 n−3). By symmetry, we set all the variables yef to the same value, yef = y = (34)4p. Note that an independent subset of Γ+(Eef) can contain at most 1 event from each clique Qv. (The event Eef itself is also contained in these cliques.) Therefore,

![image 116](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile116.png>)

![image 117](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile117.png>)

yI ≤

I⊆Γ+(Eef),I∈Ind

ye′f′) ≤ (1 + (q − 1)(2n − 1)y)4 .

(1 +

Ee′f′∈Qv

v∈e∪f

The reader can verify that I⊆Γ+(Eef),I∈Ind yI ≤ (1+(q−1)(2n−1)y)4 ≤ (1+2764n2(43)4/(2n)2)4 = (43)4. Therefore,

![image 118](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile118.png>)

![image 119](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile119.png>)

![image 120](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile120.png>)

y I⊆Γ+(Eef),I∈Ind yI

≥ p

![image 121](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile121.png>)

which is the assumption of Theorem 5.44. By Theorem 5.44, MaximalSetResample with the resampling oracle for matchings and the dependency graph deﬁned above will ﬁnd a rainbow perfect matching in time O( E

yef)2) with high probability. The number of bad events Eef is O(n3), because each color class has O(n) edges so the number of edge pairs of equal color is O(n3). We have yef = O(1/n2), and hence the total number of resamplings is O(n2) with high probability.

log(1 + yef)) = O(( E

yef E

ef

ef

ef

![image 122](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile122.png>)

![image 123](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile123.png>)

![image 124](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile124.png>)

![image 125](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile125.png>)

## 4.3 Latin transversals

A Latin transversal in an n × n matrix A is a permutation π ∈ Sn such that the entries Ai,π(i) (“colors”) are distinct for i = 1,2,... ,n. In other words, it is a set of distinct entries, exactly one in each row and one in each column. It is easy to see that this is equivalent to a bipartite version of the rainbow matching problem: Aij is the color of the edge (i,j) and we are looking for a perfect bipartite matching where no color appears twice. It is a classical application of the Lov´asz Local Lemma that if no color appears more than 41en times in A then there exists a Latin transversal [16]. An improvement of this result is that if no color appears more than 25627 n times in A then a Latin transversal exists [8]; this paper introduced the “cluster expansion” strengthening of the local lemma. (Note that 25627 = 3434.) These results were made algorithmically efﬁcient by the work of Harris and Srinivasan [21].

![image 126](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile126.png>)

![image 127](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile127.png>)

![image 128](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile128.png>)

![image 129](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile129.png>)

Beyond ﬁnding one Latin transversal, one can ask whether there exist multiple disjoint Latin transversals. A remarkable existential result was proved by Alon, Spencer and Tetali [7]: If n = 2k and each color appears in A at most ǫn times (ǫ = 10−1010 in their proof), then A can be partitioned into n disjoint Latin transversals. Here, we show how to ﬁnd a linear number of Latin transversals algorithmically.

Theorem 4.4. For any n×n matrix A where each color appears at most 8787n times, there exist at least 7878n disjoint Latin transversals, and they can be found in O(n4) resampling oracle calls w.h.p.

![image 130](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile130.png>)

![image 131](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile131.png>)

We note that again, if there is constant multiplicative slack in the assumption on color appearances, the number of resamplings improves to O(n2). This also implies Theorem 4.3 as a special case: For an edge-coloring of K2n where no color appears more than 8787n times, let us label the vertices arbitrarily (u1,... ,un,v1,... ,vn) construct a matrix A where Aij is the color of the edge (ui,vj). If no color appears more than 7878n times, by Theorem 4.4 we can ﬁnd 7878n Latin transversals; these correspond to rainbow matchings in K2n.

![image 132](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile132.png>)

![image 133](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile133.png>)

![image 134](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile134.png>)

Our approach to proving Theorem 4.4 is similar to the proof of Theorem 4.1: sample 7878n independently random permutations and hope that they will be (a) disjoint, and (b) Latin. For reasons similar to Theorem 4.1, the local lemma works out and our framework makes this algorithmic.

![image 135](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile135.png>)

Proof. Let t = 7878n and let π1,... ,πt be independently random permutations on [n]. We consider the following two types of bad events:

![image 136](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile136.png>)

- • Eefi : For each i ∈ [t] and e = (u,v),f = (x,y) ∈ [n] × [n] such that u = v,x = y,Auv = Axy, the event Eefi occurs if πi(u) = v and πi(x) = y;
- • Eeij: For each i = j ∈ [t] and e = (u,v) ∈ [n] × [n], the event Eeij occurs if πi(u) = πj(u) = v.


Clearly, if none of these events occurs then the permutations π1,... ,πt correspond to pairwise disjoint Latin transversals. The probability of a bad event of the ﬁrst type is Pr[Eefi ] = n(n1−1) and the probability for the second type is Pr[Eeij] = n12. Thus the probability of each bad event is at most p = n(n1−1).

![image 137](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile137.png>)

![image 138](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile138.png>)

![image 139](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile139.png>)

It will be convenient to think of the pairs e = (x,y) ∈ [n] × [n] as edges in a bipartite complete graph. As we proved in Section 3.2, the resampling oracle for permutations is consistent with the following lopsidependency graph graph.

- • Eefi ∼ Eei′f′ whenever there is some intersection between the edges e,f and e′,f′;
- • Eefi ,Eefj ∼ Eeij′ whenever there is some intersection between e′ and e,f;
- • Eeij ∼ Eij


′j

′

e′ ,Ei

e′ whenever e′ intersects e. By Lemma 3.2, the resampling oracle for a given event never causes a new event except in its neighborhood.

Let us now verify the cluster expansion criteria. The counting here is quite similar to the proof of Theorem 4.1, so we skim over some details. The neighborhood of each event Eefi consist of 8 cliques: 4 cliques of events of type Eei′f′ and 4 cliques of events of type Eeij, corresponding in each case to the 4 vertices of e ∪ f. In the ﬁrst case, each clique has at most n(q − 1) events, determined by selecting an incident edge and another edge of the same color. In the second case, each clique has at most n(t − 1) events, determined by selecting an incident edge and another permutation.

The neighborhood of each event Eeij also consists of 8 cliques: 4 cliques of events Eei′f′ or Eej′f′, corresponding to the choice of either i or j in the superscript, and one of the two vertices of e. The size of each clique is at most n(q−1), determined by choosing an incident edge and another edge of the same color. Then, we have 4 cliques of events Eij

′

′j

e′ or Ei

e′ , determined by switching either i′ or j′ in the superscript, and choosing one of the vertices of e. The size of each clique is at most n(t − 1), determined by choosing an incident edge and a new permutation in the superscript.

As a consequence, the cluster expansion criterion here is almost exactly the same as in the case of

- Theorem 4.1:


y (1 + n(t − 1)y)4(1 + n(q − 1)y)4

p ≤

.

![image 140](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile140.png>)

We have p = n(n1−1) here and we set y = βp. For t,q ≤ γn, it’s enough to satisfy (1+ββγ)8 ≥ 1, which is achieved by β = (87)8 and γ = 7878. Therefore, Theorem 5.44 implies that MaximalSetResample will terminate within O(( yefi + yeij)2) = O(n4) resampling oracle calls with high probability.

![image 141](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile141.png>)

![image 142](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile142.png>)

![image 143](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile143.png>)

![image 144](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile144.png>)

![image 145](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile145.png>)

![image 146](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile146.png>)

![image 147](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile147.png>)

![image 148](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile148.png>)

# 5 Analysis of the algorithm

Here we provide the analysis of our algorithm and the proofs of our main theorems. In Section 5.1, we begin with the basic notions necessary for our analysis and a coupling argument which forms the basis of all our algorithmic results. In Section 5.2, we prove a weaker form of Theorem 1.2 under the assumption that the (GLL) criterion holds with some slack. In Section 5.3, we introduce the independence polynomial of a graph and summarize its fundamental properties that are important for our analysis. In Section 5.4, we prove that our algorithm is efﬁcient if Shearer’s criterion is satisﬁed with an ǫ slack. In Section 5.5, we show that in some sense this assumption is not necessary, because every point satisfying Shearer’s criterion has some slack available, and we quantify how large this slack is. Finally, we return to the weaker (but more practical) variants of the local lemma: the (GLL) and (CLL) criteria. We present new combinatorial connections between these criteria and Shearer’s criterion, which in turn imply our main results on the efﬁciency of our algorithm under the (GLL) and (CLL) criteria (in Sections 5.6 and 5.7, respectively).

## 5.1 Stable set sequences and the coupling argument

An important notion in our analysis is that of stable set sequences. We note that this concept originated in the work of Kolipaka and Szegedy [24] which builds on Shearer’s work [36]. There are some similarities but also differences in how this concept is applied here: most notably, our stable set sequences grow forward in time, while the stable set sequences in [24] grow backward in time (which is similar to the Moser-Tardos analysis [30]).

- Deﬁnition 5.1. One execution of the outer repeat loop in MaximalSetResample is called an iteration. For a sequence of non-empty sets I = (I1,... ,It), we say that the algorithm follows I if Is is the set resampled in iteration s for 1 ≤ s < t, and It is a set of the ﬁrst m events resampled in iteration t for some m ≥ 1 (a preﬁx of the maximal independent set constructed in iteration t).

Recall that Ind = Ind(G) denotes the independent sets (including the empty set) in the graph under consideration.

- Deﬁnition 5.2. I = (I1,I2,... ,It) is called a stable set sequence if I1,... ,It ∈ Ind(G) and Is+1 ⊆ Γ+(Is) for each 1 ≤ s < t. We call the sequence I proper if each independent set Is is nonempty.


Note that if Is = ∅ for some s, then It = ∅ for all t > s. Therefore, the nonempty sets always form a preﬁx of the stable set sequence. Formally, we consider an empty sequence also a stable set sequence, of length 0.

- Lemma 5.3. If MaximalSetResample follows a sequence J = (J1,... ,Jt), then J is a stable set sequence.

Proof. By construction, the set Js chosen in each iteration is independent in G. For each i ∈ Js, we execute the resampling oracle ri. Recall that ri executed on a satisﬁed event Ei can only cause new events in the neighborhood Γ+(i) (and this neighborhood is not explored again until the following iteration). Since Js is a maximal independent set of satisﬁed events, all the events satisﬁed in the following iteration are neighbors of some event in Js, i.e., Js+1 ⊆ Γ+(Js). In the last iteration, this also holds for a subset of the resampled events.

![image 149](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile149.png>)

![image 150](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile150.png>)

![image 151](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile151.png>)

![image 152](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile152.png>)

We use the following notation: For i ∈ [n], pi = Prµ[Ei]. For S ⊆ [n], pS = i∈S pi. For a stable set

sequence I = (I1,... ,It), pI = ts=1 pIs. We relate stable set sequences to executions of the algorithm by the following coupling argument. Although the use of stable set sequences is inspired by [24], their coupling

argument is different due to its backward-looking nature (similar to [30]), and their restriction to the variable model.

- Lemma 5.4. For any proper stable set sequence I = (I1,I2,... ,It), the probability that the MaximalSetResample algorithm follows I is at most pI.


Proof. Given I = (I1,I2,... ,It), let us consider the following “I-checking” random process. We start with a random state ω ∼ µ. In iteration s, we process the events of Is in the ascending order of their indices. For each i ∈ Is, we check whether ω satisﬁes Ei; if not, we terminate. Otherwise, we apply the resampling oracle ri and replace ω by ri(ω). We continue for s = 1,2,... ,t. We say that the I-checking process succeeds if every event is satisﬁed when checked and the process runs until the end.

By induction, the state ω after each resampling oracle call is distributed according to µ: Assuming this

was true in the previous step and conditioned on Ei satisﬁed, we have ω ∼ µ|Ei. By assumption, the resampling oracle ri removes this conditioning and produces again a random state ri(ω) ∼ µ. Therefore,

whenever we check event Ei, it is satisﬁed with probability Prµ[Ei] (conditioned on the past). By a telescoping product of conditional probabilities, the probability that the I-checking process succeeds is exactly

t s=1 i∈Is Prµ[Ei] = ts=1 pIs = pI.

To conclude, we argue that the probability that MaximalSetResample follows the sequence I is at most the probability that the I-checking process succeeds. To see this, suppose that we couple MaximalSetResample and the I-checking process, so they use the same source of randomness. In each iteration, if MaximalSetResample includes i in Jt, it means that Ei is satisﬁed. Both procedures apply the resampling oracle rI(ω) and by coupling the distribution in the next iteration is the same. Therefore, the event that MaximalSetResample follows the sequence I is contained in the event that the I-checking process succeeds, which happens with probability pI.

![image 153](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile153.png>)

![image 154](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile154.png>)

![image 155](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile155.png>)

![image 156](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile156.png>)

We emphasize that we do not claim that the distribution of the current state ω ∈ Ω is µ after each resampling oracle call performed by the MaximalSetResample algorithm. This would mean that the algorithm is not making any progress in its search for a state avoiding all events. It is only the I-checking process that has this property.

Deﬁnition 5.5. Let Stab denote the set of all stable set sequences and Prop the set of proper stable set sequences. Let us denote by Stabℓ the set of stable set sequences (I1,... ,Iℓ) of length ℓ, and by Stabℓ(J) the subset of Stabℓ such that the ﬁrst set in the sequence is J. Similarly, denote by Propℓ the set of proper stable set sequences of length ℓ, and by Prop(J) the subset of Prop such that the ﬁrst set in the sequence is J. For I = (I1,... ,It) ∈ Prop, let us call σ(I) = ts=1 |Is| the total size of the sequence.

- Lemma 5.6. The probability that MaximalSetResample runs for at least ℓ iterations is at most I∈Prop


pI. The probability that MaximalSetResample resamples at least s events is at most I∈Prop:σ(I)=s pI.

ℓ

Proof. If the algorithm runs for at least ℓ iterations, it means that it follows some proper sequence I = (I1,I2,... ,Iℓ). By Lemma 5.4, the probability that the algorithm follows a particular stable set sequence I is at most pI. By the union bound, the probability that the algorithm runs for at least ℓ iterations is at most

I=(I1,...,Iℓ)∈Prop pI.

Similarly, if the algorithm resamples at least s events, it means that it follows some proper sequence I of total size σ(I) = s. By the union bound, the probability of resampling at least s events is upper-bounded by I∈Prop:σ(I)=s pI.

![image 157](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile157.png>)

![image 158](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile158.png>)

![image 159](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile159.png>)

![image 160](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile160.png>)

We note that these bounds could be larger than 1 and thus vacuous. The events that “the algorithm follows I = (I1,... ,Iℓ)” are disjoint for different sequences of ﬁxed total size σ(I), while they could overlap for a ﬁxed length ℓ (because we can take Iℓ to be different preﬁxes of the sequence of events resampled in iteration t). In any case, the upper bound of pI on each of the events could be quite loose.

## 5.2 A simple analysis: the General Lov´asz Lemma criterion, with slack

In this section we will analyze the algorithm under the assumption that the (GLL) criterion holds with some “slack”. This idea of exploiting slack has appeared in previous work, e.g., [30, 13, 20, 24]. This analysis proves only a weaker form of Theorem 1.2. The full proof, which removes the assumption of slack, appears in Section 5.6.

To begin, let us prove the following (crude) bound on the expected number of iterations. We note that this bound is typically exponentially large.

- Lemma 5.7. Provided that the pi satisfy the (GLL) criterion, pi ≤ xi j∈Γ(i)(1 − xj), we have


pI ≤

I∈Prop

n

1 1 − xi

.

![image 161](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile161.png>)

i=1

Proof. It will be convenient to work with sequences of ﬁxed length, where we pad by empty sets if necessary. Note that by deﬁnition this does not change the value of pI: e.g., p(I1,I2) = p(I1,I2,∅,...,∅). Recall that Stabℓ(J) denotes the set of all stable set sequences of length ℓ where the ﬁrst set is J. We show the following statement by induction on ℓ: For any J ∈ Ind and any ℓ ≥ 1,

xj 1 − xj

. (4)

pI ≤

![image 162](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile162.png>)

j∈J

I∈Stabℓ(J)

This is true for ℓ = 1, since p(J) = pJ ≤ j∈J xj by the LLL assumption. Let us consider the expression for ℓ + 1. We have

xi 1 − xi by the inductive hypothesis. This can be simpliﬁed using the following identity:

pI ≤ pJ

pI′ = pJ

![image 163](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile163.png>)

J′⊆Γ+(J) i∈J′

J′⊆Γ+(J) I∈Stabℓ(J′)

I′∈Stabℓ+1(J)

i∈Γ+(J)

We use this with αi = 1−xix

. Therefore,

![image 164](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile164.png>)

i

pI′ ≤ pJ

I′∈Stabℓ+1(J)

Now we use the LLL assumption:

αi. (5)

(1 + αi) =

I1⊆Γ+(J) i∈I1

i∈Γ+(J)

xi 1 − xi

1 +

![image 165](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile165.png>)

1 1 − xi

= pJ

.

![image 166](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile166.png>)

i∈Γ+(J)

(1 − xj)

 xi

pJ =

(1 − xj)

 ≤

pi ≤

xi

i∈J

i∈J

i∈J

j∈Γ+(J)\J

j∈Γ(i)

because each element of Γ+(J) \ J appears in Γ(i) for at least one i ∈ J. We conclude that

pI′ ≤

I′∈Stabℓ(J)

1 1 − xi′

(1 − xj) ·

xi

![image 167](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile167.png>)

i′∈Γ+(J)

j∈Γ+(J)\J

i∈J

This proves (4). Adding up over all sets J ⊆ [n], we again use (5) to obtain

=

xj 1 − xj

.

![image 168](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile168.png>)

i∈J

pI ≤

I∈Stabℓ

xj 1 − xj

![image 169](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile169.png>)

J⊆[n] j∈J

=

n

i=1

As we argued above, this can be written equivalently as

xi 1 − xi

1 +

![image 170](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile170.png>)

=

n

1 1 − xi

.

![image 171](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile171.png>)

i=1

ℓ

pI ≤

k=1 I∈Prop

n

1 1 − xi

.

![image 172](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile172.png>)

i=1

Since this is true for every ℓ, and the left-hand-side is non-increasing in ℓ, the sequence as ℓ → ∞ has a limit and the bound still holds in the limit.

![image 173](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile173.png>)

![image 174](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile174.png>)

![image 175](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile175.png>)

![image 176](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile176.png>)

The following is our ﬁrst concrete result: our algorithm is efﬁcient if (GLL) is satisﬁed with a slack.

- Theorem 5.8. If (GLL) is satisﬁed with a slack of ǫ, i.e.


(1 − xj)

[Ei] ≤ (1 − ǫ)xi

Pr

µ

j∈Γ(i)

then with probability 1 − e−t MaximalSetResample resamples at most 1ǫ(t + ni=1 ln 1−1x

) events.

![image 177](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile177.png>)

![image 178](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile178.png>)

i

Proof. By Lemma 5.6, the probability that MaximalSetResample resamples more than s events is at most I∈Prop:σ(I)=⌈s⌉ pI where pI is the product of pi = Prµ[Ei] over all events in the sequence I. By the

slack assumption, we have pi ≤ (1 − ǫ)p′i and pI ≤ (1 − ǫ)σ(I)p′I, where p′i = xi j∈Γ(i)(1 − xj). Using Lemma 5.7, we obtain

n

p′I ≤ e−ǫs

pI ≤ (1 − ǫ)s

i=1

I∈Prop σ(I)=⌈s⌉

I∈Prop

1 1 − xi

.

![image 179](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile179.png>)

For s = 1ǫ(t + ni=1 ln 1−1x

), we obtain

![image 180](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile180.png>)

![image 181](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile181.png>)

i

n

1 1 − xi

pI ≤ e−ǫs

![image 182](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile182.png>)

i=1

I∈Prop σ(I)=⌈s⌉

≤ e−t.

Therefore, the probability of resampling more than s events is at most e−t.

![image 183](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile183.png>)

![image 184](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile184.png>)

![image 185](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile185.png>)

![image 186](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile186.png>)

## 5.3 Preliminaries on Shearer’s criterion

In this section we discuss a strong version of the local lemma due to Shearer [36]. Shearer’s lemma is based on certain forms of the multivariate independence polynomial. We recall that pI denotes i∈I pi.

- Deﬁnition 5.9. Given a graph G and values p1,... ,pn, deﬁne for each S ⊆ [n]

qS = qS(p) =

I∈Ind S⊆I

(−1)|I\S|pI. (6)

Note that qS = 0 for S ∈/ Ind. An alternative form of these polynomials that is also useful is obtained by summing over subsets of S.

- Deﬁnition 5.10. Given a graph G and values p1,... ,pn, deﬁne

q˘S = q˘S(p) =

I∈Ind I⊆S

(−1)|I|pI.

The following set plays a fundamental role.

- Deﬁnition 5.11. Given a graph G, the Shearer region is the semialgebraic set


S = { p ∈ (0,1)n : ∀I ∈ Ind, qI(p) > 0 } (7a) = { p ∈ (0,1)n : ∀S ⊆ [n], q˘S(p) > 0 } (7b)

The equivalence between (7a) and (7b) is proven below in Claim 5.19. Shearer’s Lemma can be stated as follows.

Lemma 5.12 (Shearer [36]). Let G be a lopsidependency graph for the events E1,... ,En. Let pi = Prµ[Ei] ∈ (0,1). If p ∈ S then Prµ[ ni=1 Ei] ≥ q∅.

![image 187](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile187.png>)

It is known that Shearer’s Lemma implies Theorem 1.1, as we will see in Section 5.6, and in fact gives the tight criterion under which all events can be avoided for a given dependency graph G. The polynomials qS(p) and q˘S(p) have a natural interpretation in the Shearer region: There is a “tight instance” where qS(p) is the probability that the set of occurring events is exactly S, and q˘S(p) is the probability that none of the events in S occur. In particular, q∅(p) = q˘[n](p) is exactly the probability that no event occurs. (See [36] for more details.)

### 5.3.1 Properties of independence polynomials

In this section we summarize some of the important properties of these polynomials, most of which may be found in earlier work. Since some of the proofs are not easy to recover due to different notation and/or their analytic nature (in case of [35]), we provide short combinatorial proofs for completeness.

- Claim 5.13 (The “fundamental identity”. Shearer [36], Scott-Sokal [35, Eq. (3.5)]). For any a ∈ S, we have

q˘S = q˘S\{a} − pa · q˘S\Γ+(a).

Proof. Every independent set I ⊆ S either contains a or does not. In addition, if a ∈ I then I is independent iff I \ {a} is an independent subset of S \ Γ+(a).

![image 188](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile188.png>)

![image 189](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile189.png>)

![image 190](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile190.png>)

![image 191](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile191.png>)

- Claim 5.14 (Shearer [36], Scott-Sokal [35, Eq. (2.52)]). For every S ⊆ [n],

q˘S =

Y ⊆[n]\S

qY .

Proof. By deﬁnition of qY ,

Y ⊆[n]\S

qY =

Y ⊆[n]\S I∈Ind Y ⊆I

(−1)|I\Y |pI =

I∈Ind

pI

Y ⊆I\S

(−1)|I\Y |.

If I\S = ∅ then the last alternating sum is zero. Therefore, the sum simpliﬁes to I∈Ind:I⊆S(−1)|I|pI = q˘S as required.

![image 192](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile192.png>)

![image 193](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile193.png>)

![image 194](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile194.png>)

![image 195](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile195.png>)

- Claim 5.15 (Shearer [36]).

J∈Ind

qJ =

S⊆[n]

qS = 1.

Proof. Set S = ∅ in Claim 5.14 and use the fact that q˘∅ = 1.

![image 196](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile196.png>)

![image 197](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile197.png>)

![image 198](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile198.png>)

![image 199](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile199.png>)

- Claim 5.16 (Scott-Sokal [35, Eq. (2.48)]). For I ∈ Ind, qI = pI · q˘[n]\Γ+(I).


Proof. Given I ∈ Ind, each independent set J ⊇ I can be written uniquely as J = I ∪ K where K is independent and K ∩ Γ+(I) = ∅. So,

qI =

(−1)|K|pK = pI · q˘[n]\Γ+(I).

(−1)|J\I|pJ = pI

K∈Ind K⊆[n]\Γ+(I)

J∈Ind:I⊆J

![image 200](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile200.png>)

![image 201](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile201.png>)

![image 202](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile202.png>)

![image 203](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile203.png>)

Lemma 5.17 (Kolipaka-Szegedy [24, Lemma 15]). For any I ∈ Ind

qI = pI ·

qS.

S⊆Γ+(I)

Proof. By Claim 5.16 and Claim 5.14, we have qI = pI · q˘[n]\Γ+(I) = pI S⊆Γ+(I) qS, as required.

![image 204](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile204.png>)

![image 205](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile205.png>)

![image 206](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile206.png>)

![image 207](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile207.png>)

- Claim 5.18 (Simultaneous positivity of qS and q˘S). Assume that p ∈ [0,1]n. Then

qI ≥ 0 ∀I ∈ Ind =⇒ q˘S ≥ q∅ ∀S ⊆ [n] (8) q˘S ≥ 0 ∀S ⊆ [n] =⇒ qI ≥ p[n] · q˘[n] ∀I ∈ Ind. (9)

Proof. (8) follows from Claim 5.14 (since qY = 0 for Y ∈/ Ind). To see (9), ﬁrst note that qI ≥ 0 for all

- I ∈ Ind, by Claim 5.16. Consequently, by Claim 5.14, q˘[n] = minS q˘S. Clearly, p[n] = minI pI. It follows from Claim 5.16 again that qI = pI · q˘[n]\Γ+(I) ≥ p[n] · q˘[n].


![image 208](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile208.png>)

![image 209](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile209.png>)

![image 210](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile210.png>)

![image 211](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile211.png>)

- Claim 5.19. The two characterizations of the Shearer region, (7a) and (7b), are equivalent.

Proof. By Claim 5.18, if q∅ > 0 and qS ≥ 0 ∀S ⊆ [n], then q˘S > 0 for all S ⊆ [n]. Conversely, if q˘S > 0 for all S ⊆ [n], then qI ≥ p[n]q˘[n] > 0 for all I ∈ Ind.

![image 212](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile212.png>)

![image 213](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile213.png>)

![image 214](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile214.png>)

![image 215](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile215.png>)

- Claim 5.20 (Monotonicity of q˘, Scott-Sokal [35, Theorem 2.10]). Let p ∈ [0,1]n. q˘S(p) ≥ 0 ∀S ⊆ [n] =⇒ q˘S(p′) ≥ q˘S(p) ∀0 ≤ p′ ≤ p, ∀S ⊆ [n].

Proof. First consider the case that p and p′ differ only in coordinate i. For any S ⊆ [n], Claim 5.13 implies that ∂p∂

![image 216](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile216.png>)

i

q˘S(p) = −q˘S\Γ+(i)(p) and ∂p∂22

![image 217](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile217.png>)

i

q˘S = 0. Thus,

q˘S(p′) = q˘S(p) + (pi − p′i) · q˘S\Γ+(i)(p) ≥ q˘S(p). The case that p′ and p differ in multiple coordinates is handled by induction.

![image 218](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile218.png>)

![image 219](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile219.png>)

![image 220](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile220.png>)

![image 221](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile221.png>)

- Claim 5.21 (Log-submodularity of q˘S, Scott-Sokal [35, Corollary 2.27]). For any p ∈ S and A,B ⊆ [n], we have q˘A · q˘B ≥ q˘A∪B · q˘A∩B. Proof. We claim that for any a ∈ S ⊆ T, we have


q˘S q˘S\{a}

![image 222](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile222.png>)

≥

q˘T q˘T\{a}

. (10)

![image 223](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile223.png>)

By induction, this implies that for any R ⊆ S, q˘q˘S

≥ q˘q˘T

. We obtain the claim above by setting S = A, T = A ∪ B, and R = A \ B.

![image 224](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile224.png>)

![image 225](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile225.png>)

S\R

T\R

We prove (10) again by induction, on |T|. For |T| = 1, the statement is trivial. Let |T| > 1. By

- Claim 5.13, we have


- q˘S = q˘S\{a} − paq˘S\Γ+(a)

and

- q˘T = q˘T\{a} − paq˘T\Γ+(a).


Let us denote S ∩ Γ+(a) = {a,s1,... ,sk}. We apply (10) to strict subsets of S and T, to obtain

k

k

q˘T\(S∩Γ+(a)) q˘T\{a}

q˘T\Γ+(a) q˘T\{a}

q˘S\Γ+(a) q˘S\{a}

q˘S\{a,s1,...,si−1,si} q˘S\{a,s1,...,si−1}

q˘T\{a,s1,...,si−1,si} q˘T\{a,s1,...,si−1}

≤

≤

=

=

![image 226](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile226.png>)

![image 227](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile227.png>)

![image 228](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile228.png>)

![image 229](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile229.png>)

![image 230](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile230.png>)

i=1

i=1

where in the last step we used the monotonicity of q˘T in T (again from Claim 5.13). This implies (10):

q˘S q˘S\{a}

![image 231](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile231.png>)

q˘S\Γ+(a) q˘S\{a}

= 1 − pa

![image 232](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile232.png>)

q˘T\Γ+(a) q˘T\{a}

≥ 1 − pa

![image 233](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile233.png>)

=

q˘T q˘T\{a}

.

![image 234](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile234.png>)

![image 235](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile235.png>)

![image 236](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile236.png>)

![image 237](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile237.png>)

![image 238](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile238.png>)

- Claim 5.22 (Log-submodularity of qS). For any p ∈ S and A,B ⊆ [n], we have qA · qB ≥ qA∪B · qA∩B. Proof. We can assume A ∪ B ∈ Ind; otherwise the right-hand side is zero. By Claim 5.16, we have

qA · qB = pAq˘[n]\Γ+(A) · pBq˘[n]\Γ+(B). By Claim 5.21,

q˘[n]\Γ+(A) · q˘[n]\Γ+(B) ≥ q˘[n]\(Γ+(A)∪Γ+(B)) · q˘[n]\(Γ+(A)∩Γ+(B)). Here we use the fact that Γ+(A) ∪ Γ+(B) = Γ+(A ∪ B), and Γ+(A) ∩ Γ+(B) ⊇ Γ+(A ∩ B). Therefore, by the monotonicity of q˘S,

q˘[n]\Γ+(A) · q˘[n]\Γ+(B) ≥ q˘[n]\Γ+(A∪B) · q˘[n]\Γ+(A∩B). Also, pApB = pA∪BpA∩B. Using Claim 5.16 one more time, we obtain

qA · qB ≥ pA∪Bq˘[n]\Γ+(A∪B) · pA∩Bq˘[n]\Γ+(A∩B) = qA∪B · qA∩B.

![image 239](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile239.png>)

![image 240](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile240.png>)

![image 241](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile241.png>)

![image 242](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile242.png>)

- Claim 5.23. Suppose that p ∈ S. For any set S ⊆ [n],


q{j} q∅

qJ q∅

≤

1 +

.

![image 243](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile243.png>)

![image 244](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile244.png>)

J⊆S

j∈S

Proof. The proof is by induction on S, the case |S| ≤ 1 being trivial. Fix any s ∈ S. Claim 5.22 implies that qJ+s · q∅ ≤ q{s} · qJ for any J ⊆ S \ {s}. Summing over J yields

q{s} q∅

qJ+s q∅

qJ q∅

≤

.

![image 245](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile245.png>)

![image 246](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile246.png>)

![image 247](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile247.png>)

J⊆S\{s}

J⊆S\{s}

Adding J⊆S\{s} qqJ

to both sides yields

![image 248](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile248.png>)

∅

qJ q∅

![image 249](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile249.png>)

J⊆S

q{s} q∅

≤ 1 +

![image 250](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile250.png>)

qJ q∅

.

![image 251](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile251.png>)

J⊆S\{s}

The claim follows by induction.

- Claim 5.24. If q∅ > 0 then qq{i}

![image 256](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile256.png>)

∅

= q˘[nq˘]\{i}

![image 257](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile257.png>)

[n]

− 1. Proof. By Claim 5.14,

1 +

q{i} q∅

![image 258](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile258.png>)

=

q∅ + q{i} q∅

![image 259](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile259.png>)

=

q˘[n]\{i} q˘[n]

![image 260](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile260.png>)

.

![image 261](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile261.png>)

![image 262](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile262.png>)

![image 263](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile263.png>)

![image 264](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile264.png>)

- Claim 5.25 (Kolipaka-Szegedy [24, Theorem 5]). If (1 + ǫ)p ∈ S then qq{i}


≤ 1ǫ for each i ∈ [n].

![image 265](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile265.png>)

![image 266](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile266.png>)

∅

Proof. Note that q˘[n]\{i}(p) does not depend on pi, while q˘[n](p) is linear in pi. Also, both quantities are equal at pi = 0: we have q˘[n](p1,... ,0 · pi,... ,pn) = q˘[n]\{i}(p). Since (1 + ǫ)p ∈ S, we know that q˘[n](p1,... ,(1 + ǫ)pi,... ,pn) ≥ 0. By linearity, q˘[n](p) ≥ 1+ǫ ǫq˘[n]\{i}(p). Claim 5.24 then implies that q{i}

![image 267](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile267.png>)

q∅ ≤ 1ǫ.

![image 268](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile268.png>)

![image 269](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile269.png>)

![image 270](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile270.png>)

![image 271](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile271.png>)

![image 272](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile272.png>)

![image 273](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile273.png>)

### 5.3.2 Connection to stable set sequences

Kolipaka and Szegedy showed that stable set sequences relate to the independence polynomials qS. The following is the crucial upper-bound for stable set sequences when Shearer’s criterion holds. In fact, this result is subsumed by Lemma 5.27 but we present the upper bound ﬁrst, with a shorter proof.

- Lemma 5.26 (Kolipaka-Szegedy [24]). If qS ≥ 0 for all S ⊆ [n] and q∅ > 0, then

I∈Stabℓ(J)

pI ≤

qJ q∅

![image 274](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile274.png>)

∀J ∈ Ind,∀ℓ ≥ 1.

Proof. We proceed by induction: for ℓ = 1, there is only one such stable set sequence I = (J). By Lemma 5.17, we have qJ = pJ S⊆Γ+(J) qS ≥ pJq∅. (Recall that qS ≥ 0 for all S ⊆ [n].) Hence, p(J) = pJ ≤ qJ/q∅.

The inductive step: every stable set sequence starting with J has the form I = (J,J′,...) where J′ ⊆ Γ+(J). Therefore,

I∈Stabℓ(J)

pI = pJ

J′∈Ind J′⊆Γ+(J)

I∈Stabℓ−1(J′)

pI. (11)

By the inductive hypothesis, I∈Stab

ℓ−1(J′) pI ≤ qJ′/q∅. Also, recall that qJ′ = 0 if J′ ∈/ Ind. Therefore,

I∈Stabℓ(J)

pI ≤ pJ

J′⊆Γ+(J)

qJ′ q∅

![image 275](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile275.png>)

=

qJ q∅

![image 276](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile276.png>)

using Lemma 5.17 to obtain the last equality.

![image 277](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile277.png>)

![image 278](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile278.png>)

![image 279](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile279.png>)

![image 280](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile280.png>)

The inequality in Lemma 5.26 actually becomes an equality as ℓ → ∞, as shown in Lemma 5.27. This stronger result is used only tangentially in Section 5.7.2, but we provide a detailed proof in order to clarify the arguments of Kolipaka and Szegedy [24].

- Lemma 5.27 (Kolipaka-Szegedy [24, Theorem 14]). For a dependency graph G and p1,... ,pn ∈ (0,1), the following statements are equivalent:


- 1. q∅ > 0 and qS ≥ 0 for all S ⊆ [n].


- 2. for all J ∈ Ind, qJ > 0 and I∈Prop(J) pI = qJ/q∅.
- 3. I∈Prop(J) pI is ﬁnite for each J ∈ Ind.


Proof. First, note that Prop(J) = ∞t=1 Propt(J), and ℓt=1 Propt(J) can be identiﬁed with Stabℓ(J), since each proper sequence I of length at most ℓ can be padded with empty sets to obtain a sequence

ℓ(J) pI. This is a non-decreasing sequence; the limit exists but could be inﬁnite. Let us denote wJ(ℓ) = I∈Stab

in Stabℓ(J) (and pI does not change). Therefore, I∈Prop(J) pI = limℓ→∞ I∈Stab

ℓ(J) pI and wJ∗ = limℓ→∞ wJ(ℓ) = I∈Prop(J) pI. Let us deﬁne M to be the following linear operator on RInd:

(Mx)I = pI

xJ.

J∈Ind J⊆Γ+(I)

Using this notation, the identity (11) can written compactly as w(ℓ) = Mw(ℓ−1). Inductively, w(ℓ) = Mℓ−1w(1), and w∗ = limℓ→∞ Mℓw(1).

1 ⇒ 2: Assume now that qS ≥ 0 for all S ⊆ [n] and q∅ > 0. Lemma 5.26 proves that this implies wJ∗ = I∈Prop(J) pI = limℓ→∞ I∈Stab

ℓ(J) pI ≤ qJ/q∅. Clearly I∈Prop(J) pI > 0, so this also implies that qJ > 0 for all J ∈ Ind.

Note that w(1) is the column of M corresponding to J = ∅: MI,∅ = pI for each I ∈ Ind. Therefore, we can write w(1) = Mw(0), where w(0) = e∅ is the canonical basis vector in RInd corresponding to ∅. We have w∗ = limℓ→∞ Mℓw(1) = limℓ→∞ Mℓw(0). We may subtract these two limits since we have shown that every wJ∗ is ﬁnite, obtaining limℓ→∞ Mℓ(w(1) − w(0)) = 0. We note that w(1) − w(0) has strictly positive coordinates for I = ∅, and 0 for I = ∅.

By Lemma 5.17, we have Mq = q for the vector q ∈ RInd with coordinates qI. Consider q1

q − w(0), a nonnegative vector with 0 in the coordinate corresponding to ∅. We can choose β > 0 large enough so that coordinate-wise, 0 ≤ q1

![image 281](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile281.png>)

∅

q − w(0) ≤ β(w(1) − w(0)). From this we derive that

![image 282](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile282.png>)

∅

0 ≤

1 q∅

q − w∗ = lim

Mℓ

![image 283](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile283.png>)

ℓ→∞

1 q∅

q − w(0) ≤ β lim

Mℓ(w(1) − w(0)) = 0,

![image 284](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile284.png>)

ℓ→∞

so equality holds throughout. Recalling the deﬁnition of wJ∗, we conclude that I∈Prop(J) pI = wJ∗ = q1

qJ.

![image 285](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile285.png>)

∅

- 2 ⇒ 3: Trivial.
- 3 ⇒ 1: Let p ∈ (0,1)n be the vector (p1,... ,pn). We can assume that minS q˘S(p) ≤ 0, otherwise


we are done by Claim 5.18. Let us consider the values of q˘S on the line { λp : λ ∈ [0,1] }. Deﬁne λ∗ = inf{λ ∈ (0,1] : minS q˘S(λp) ≤ 0}. We observe that minS q˘S(λp) > 0 for 0 < λ < 1/n, which can be veriﬁed directly by considering the alternating sum deﬁning q˘S. (Intuitively, Shearer’s Lemma holds in this region just by the union bound.) Therefore, we have λ∗ > 0. Furthermore continuity also implies minS q˘S(λ∗p) = 0, so Claim 5.18 yields q∅(λ∗p) = q˘[n](λ∗p) = 0. For λ ∈ [0,λ∗) we have minS q˘S(λp) >

- 0, so by Claim 5.18 we also have minI∈Ind qI(λp) > 0. This shows that the condition 1 holds at the point λp, for λ ∈ [0,λ∗), so we may use the implication 1 ⇒ 2: I∈Prop(J)(λp)I = qJ(λp)/q∅(λp). Let J ∈ Ind


be such that qJ(λ∗p) > 0; such a J must exist by Claim 5.15. By the monotonicity of pI = I∈I pI in the variables p1,... ,pn, we have

pI ≥

I∈Prop(J)

qJ(λp) q∅(λp)

(λ∗p)I ≥ liminf λ→λ∗−

(λp)I = liminf λ→λ∗−

![image 286](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile286.png>)

I∈Prop(J)

I∈Prop(J)

= ∞,

as qJ(λ∗p) > 0 but q∅(λ∗p) = 0. This contradicts the assumption 3 that I∈Prop(J) pI is ﬁnite.

From Claim 5.15, we obtain immediately the following. Corollary 5.28. If qS ≥ 0 for all S ⊆ [n] and q∅ > 0,

1 q∅

.

pI =

![image 291](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile291.png>)

I∈Prop

Remark. An equivalent statement using the language of “traces” appears in the recent manuscript of Knuth [23, Page 86, Theorem F], together with a short proof using generating functions. Furthermore, using

- Claim 5.14, we may derive


q˘[n]\A q˘[n]

qJ q∅

=

,

pI =

![image 292](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile292.png>)

![image 293](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile293.png>)

J⊆A I∈Prop(J)

J⊆A

for any A ⊆ [n]. This statement, in the language of traces, also appears in Knuth’s draft [23, Page 87, Equation (144)].

Summary at this point. By Lemma 5.6 and Corollary 5.28, MaximalSetResample produces a state in n i=1 Ei after at most 1/q∅ iterations in expectation. However, this should not be viewed as a statement of

![image 294](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile294.png>)

efﬁciency. Shearer’s Lemma proves that Prµ[ ni=1 Ei] ≥ q∅ so, in expectation, 1/q∅ independent samples from µ would also sufﬁce to ﬁnd a state in ni=1 Ei.

![image 295](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile295.png>)

![image 296](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile296.png>)

Section 5.4 improves this analysis by assuming that Shearer’s criterion holds with some slack, analogous to the result in Section 5.2. Section 5.5 then removes the need for that assumption — it argues that Shearer’s criterion always holds with some slack, and provides quantitative bounds on that slack.

## 5.4 Shearer’s criterion with slack

In this section we consider scenarios in which Shearer’s criterion holds with a certain amount of slack. To make this formal, we will consider another vector p′ of probabilities with p ≤ p′ ∈ S. For notational convenience, we will let qS′ denote the value qS(p′) and let qS denote qS(p) as before. Let us assume that Shearer’s criterion holds with some slack in the following natural sense.

Deﬁnition 5.29. We say that p ∈ (0,1)n satisﬁes Shearer’s criterion with coefﬁcients qS′ at a slack of ǫ, if p′ = (1 + ǫ)p is still in the Shearer region S and qS′ = qS(p′).

Theorem 5.30. Recall that pi = Prµ[Ei]. If the pi satisfy Shearer’s criterion with coefﬁcient q∅′ at a slack of ǫ ∈ (0,1), then the probability that MaximalSetResample resamples more than 2ǫ ln q1′

+ t events is at

![image 297](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile297.png>)

![image 298](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile298.png>)

∅

most e−t. Proof. By Lemma 5.6, the probability that MaximalSetResample resamples more than s events is at most

I∈Prop:σ(I)=⌈s⌉ pI. By the slack assumption, we have Pr[resample more than s events] ≤

p′I

pI ≤ (1 + ǫ)−s

I∈Prop σ(I)=⌈s⌉

I∈Prop σ(I)=⌈s⌉

since we have p′i = (1 + ǫ)pi for each event appearing in a sequence I. The hypothesis is that the probabilities p′i satisfy Shearer’s criterion with a bound of q∅′ . Consequently, Corollary 5.28 implies that

I∈Prop:σ(I)=⌈s⌉ p′I ≤ I∈Prop p′I ≤ 1/q∅′ . Thus, for s = 2ǫ ln q1′

+ t we obtain

![image 299](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile299.png>)

![image 300](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile300.png>)

∅

1 q∅′

≤ e−(ln(1/q∅′ )+t) 1 q∅′

1 q∅′

≤ e−sǫ/2

= e−t.

Pr[resample more than s events] ≤ (1 + ǫ)−s

![image 301](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile301.png>)

![image 302](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile302.png>)

![image 303](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile303.png>)

![image 304](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile304.png>)

![image 305](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile305.png>)

![image 306](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile306.png>)

![image 307](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile307.png>)

In other words, the probability that MaximalSetResample requires more than 2ǫ ln(1/q∅′ ) resamplings decays exponentially fast; in particular the expected number of resampled events is O 1ǫ ln(1/q∅′ ) . This appears signiﬁcantly better than the trivial bound of 1/q∅; still, it is not clear whether this bound can be considered “polynomial”. In the following, we show that this leads in fact to efﬁcient bounds, comparable to the best known bounds in the variable model.

![image 308](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile308.png>)

![image 309](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile309.png>)

Corollary 5.31. If the pi satisfy Shearer’s criterion with coefﬁcients qS′ at a slack of ǫ ∈ (0,1), then the probability that MaximalSetResample resamples more than

2 ǫ

![image 310](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile310.png>)

q{′j} q∅′

n

ln 1 +

![image 311](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile311.png>)

j=1

+ t

events is at most e−t. Proof. By Claim 5.15 and Claim 5.23, we have

1 q∅′

ln

![image 312](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile312.png>)

qJ′ q∅′

= ln

![image 313](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile313.png>)

J⊆[n]

≤

q{′j} q∅′

n

ln 1 +

![image 314](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile314.png>)

j=1

.

The result follows from Theorem 5.30.

![image 315](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile315.png>)

![image 316](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile316.png>)

![image 317](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile317.png>)

![image 318](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile318.png>)

Next, we provide a simpliﬁed bound that depends only on the amount of slack and the number of events. This is analogous to a bound of O(n/ǫ) given by Kolipaka-Szegedy [24] in the variable model. Theorem 5.32. If p1,... ,pn satisfy Shearer’s criterion at a slack of ǫ ∈ (0,1), then the expected number of events resampled by MaximalSetResample is O(nǫ log 1ǫ). Proof. Let p′ = (1 + ǫ/2)p. By assumption, (1 + ǫ/3)p′ ≤ (1 + ǫ)p ∈ S. Therefore, p′ still has ǫ/3 slack so by Claim 5.25, the coefﬁcients qS′ = qS(p′) satisfy q

![image 319](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile319.png>)

![image 320](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile320.png>)

′ {i}

q∅′ ≤ 3ǫ. The point p satisﬁes Shearer’s criterion with coefﬁcients qS′ at a slack of ǫ/2, so by Corollary 5.31, the probability that we resample more than

![image 321](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile321.png>)

![image 322](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile322.png>)

- 4 ǫ(nln(1 + 3ǫ) + t) events is at most e−t. In expectation, we resample O(nǫ log 1ǫ) events as claimed.

![image 323](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile323.png>)

![image 324](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile324.png>)

![image 325](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile325.png>)

![image 326](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile326.png>)

![image 327](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile327.png>)

![image 328](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile328.png>)

![image 329](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile329.png>)

![image 330](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile330.png>)

- 5.5 Quantiﬁcation of slack in Shearer’s criterion


In the previous section, we proved a bound on the number of resamplings in the MaximalSetResample algorithm, provided that Shearer’s criterion is satisﬁed with a certain slack. In fact, from Deﬁnition 5.11 one can observe that the Shearer region is an open set and therefore there is always a certain amount of slack. However, how large a slack we can assume is not a priori clear. In particular, one can compare with Kolipaka-Szegedy [24] where a bound is proved on the expected number of events one has to resample in the variable model: If Shearer’s criterion is satisﬁed with coefﬁcients qS, then the expected number of resamplings is at most ni=1 q{i}/q∅ [24]. In this section, we prove that anywhere in the Shearer region, there is an amount of slack inversely proportional to this quantity, which leads to a bound similar to that of Kolipaka and Szegedy [24].

Lemma 5.33. Let (p1,... ,pn) ∈ (0,1)n be a point in the Shearer region. Let ǫ = q∅/(2 ni=1 q{i}) and p′i = (1 + ǫ)pi. Then (p′1,... ,p′n) is also in the Shearer region, and q∅(p′) ≥ 21q∅(p).

![image 331](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile331.png>)

Before proving the lemma, let us consider the partial derivatives of the q˘S polynomials. Claim 5.34. For any i ∈ S,

∂q˘S ∂pi

= − q˘S\Γ+(i) and for any j ∈ S \ Γ+(i),

![image 332](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile332.png>)

∂2q˘S ∂pi∂pj

= q˘S\Γ+(i)\Γ+(j).

![image 333](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile333.png>)

For other choices of i,j, the partial derivatives are 0. In particular, for any point in the Shearer region, ∂q˘S ∂pi ≤ 0 and ∂p∂2q˘S

i∂pj ≥ 0. Due to Claim 5.34, we may say that q˘S(p1,... ,pn) is “continuous supermodular” in the Shearer region.

![image 334](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile334.png>)

![image 335](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile335.png>)

Proof. For any i ∈ S, we have q˘S = q˘S\{i} − piq˘S\Γ+(i) by Claim 5.13. The polynomials q˘S\{i} and q˘S\Γ+(i) do not depend on pi and hence ∂∂pq˘S

is equal to −q˘S\Γ+(i). Repeating this argument one more time for j ∈ S \ Γ+(i), we get ∂∂pq˘S

![image 336](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile336.png>)

i

= −q˘S\Γ+(i) = −q˘S\Γ+(i)\{j} + pjq˘S\Γ+(i)\Γ+(j). Again, q˘S\Γ+(i)\{j} and q˘S\Γ+(i)\Γ+(j) do not depend on pj and hence ∂p∂2q˘S

![image 337](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile337.png>)

i

i∂pj = q˘S\Γ+(i)\Γ+(j). Clearly, we have ∂∂pq˘S

![image 338](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile338.png>)

= 0 unless i ∈ S, and ∂p∂2q˘S

i∂pj = 0 unless i ∈ S and j ∈ S \ Γ+(i). Since all the coefﬁcients q˘S are positive in the Shearer region, we have ∂∂pq˘S

![image 339](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile339.png>)

![image 340](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile340.png>)

i

≤ 0 and ∂p∂2q˘S

i∂pj ≥ 0 for all i,j. Now we can prove Lemma 5.33.

![image 341](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile341.png>)

![image 342](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile342.png>)

![image 343](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile343.png>)

![image 344](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile344.png>)

![image 345](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile345.png>)

![image 346](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile346.png>)

i

Proof. Consider the line segment from p = (p1,... ,pn) to p′ = (p′1,... ,p′n) where p′i = (1 + ǫ)pi, ǫ = 2 nq∅

)pi = q{qi}+q∅

pi = p q˘[n]\{i}

i=1 q{i}. Note that p′i ≤ (1 + qq∅

iq˘[n]\Γ+(i)pi ≤ 1 by Claim 5.14, Claim 5.16 and Claim 5.20. Let us deﬁne

![image 347](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile347.png>)

![image 348](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile348.png>)

![image 349](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile349.png>)

![image 350](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile350.png>)

{i}

{i}

Q∅(λ) = q∅((1 + λ)p1,... ,(1 + λ)pn). By the chain rule and Claim 5.34, we have

dQ∅ dλ λ=0

![image 351](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile351.png>)

=

n

∂q∅ ∂pi

pi

![image 352](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile352.png>)

i=1

= −

n

n

piq˘[n]\Γ+(i) = −

q{i}

i=1

i=1

where we used Claim 5.16 in the last equality. Assuming that (1 + λ)p = ((1 + λ)p1,... ,(1 + λ)pn) is in the Shearer region, we also have by Claim 5.34

d2Q∅ dλ2

![image 353](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile353.png>)

=

n

∂2q∅ ∂pi∂pj

pipj ≥ 0.

![image 354](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile354.png>)

i,j=1

That is, Q∅(λ) is a convex function for λ ≥ 0 as long as (1 + λ)p is in the Shearer region. Our goal is to prove that this indeed happens for λ ∈ [0,ǫ].

Assume for the sake of contradiction that (1 + λ)p is not in the Shearer region for some λ ∈ [0,ǫ], and let λ∗ be the minimum such value (which exists since the complement of the Shearer region is closed). By Claim 5.18, anywhere in the Shearer region, q∅ = q˘[n] is the minimum of the q˘S coefﬁcients; hence by continuity it must be the case that q˘[n]((1 + λ∗)p) is the minimum coefﬁcient among q˘S((1 + λ∗)p) for all

- S ⊆ [n], and Q∅(λ∗) = q˘[n]((1 + λ∗)p) ≤ 0. On the other hand, by the minimality of λ∗, Q∅(λ) is positive and convex on [0,λ∗) and therefore


dQ∅ dλ λ=0

Q∅(λ∗) ≥ Q∅(0) + λ∗

![image 355](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile355.png>)

= q∅ − λ∗

n

n

q{i} ≥ q∅ − ǫ

q{i} =

i=1

i=1

- 1

![image 356](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile356.png>)

- 2


q∅ > 0,

which is a contradiction. Therefore, Q∅(λ) is positive and convex for all λ ∈ [0,ǫ]. By the same computation

- as above, Q∅(ǫ) ≥ 12q∅. This implies our main algorithmic result under Shearer’s criterion.


![image 357](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile357.png>)

![image 358](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile358.png>)

![image 359](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile359.png>)

![image 360](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile360.png>)

![image 361](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile361.png>)

Theorem 5.35. Let E1,... ,En be events and let pi = Prµ[Ei]. Suppose that the three subroutines described in Section 1.1.1 exist. If p ∈ S then the probability that MaximalSetResample resamples more than

4 ni=1 qq{i}

n j=1 ln(1 + qq{j}

) + 1 + t events is at most e−t.

![image 362](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile362.png>)

![image 363](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile363.png>)

∅

∅

We note that the corresponding result in the variable model [24] was that the expected number of resamplings is at most ni=1 qq{i}

. Here, we obtain a bound which is at most quadratic in this quantity.

![image 364](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile364.png>)

∅

Proof. Directly from Theorem 5.30 and Lemma 5.33: Given p in the Shearer region, Lemma 5.33 implies that p in fact satisﬁes Shearer’s criterion with a bound of q∅′ ≥ q2∅ at a slack of ǫ = q2∅/ ni=1 q{i}. By Theorem 5.30, the probability that MaximalSetResample resamples more than s events is at most e−t, where

![image 365](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile365.png>)

![image 366](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile366.png>)

n

1 q∅′

4 q∅

1 q∅

2 ǫ

+ t ≤

q{i} ln

ln

+ 1 + t .

s =

![image 367](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile367.png>)

![image 368](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile368.png>)

![image 369](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile369.png>)

![image 370](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile370.png>)

i=1

by nj=1 ln(1 + qq{j}

Using Claim 5.23, we can replace ln q1

).

![image 371](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile371.png>)

![image 372](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile372.png>)

![image 373](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile373.png>)

![image 374](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile374.png>)

![image 375](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile375.png>)

![image 376](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile376.png>)

∅

∅

## 5.6 The General LLL criterion, without slack

Shearer’s Lemma (Lemma 5.12) is a strengthening of the original Lov´asz Local Lemma (Theorem 1.1): if p1,... ,pn satisfy (GLL) then they must also satisfy Shearer’s criterion p ∈ S. Nevertheless, there does not seem to be a direct proof of this fact in the literature. Shearer [36] indirectly proves this fact by showing that, when p  ∈ S it is possible that Pr[ ni=1 Ei] = 0, so the contrapositive of Theorem 1.1 implies that (GLL) cannot hold. Scott and Sokal prove this fact using analytic properties of the partition function [35, Corollary 5.3]. In this section we establish this fact by an elementary, self-contained proof.

![image 377](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile377.png>)

We then establish Theorem 1.2, our algorithmic form of Theorem 1.1 in the general framework of resampling oracles. Unlike the simpler analysis of Section 5.2, the analysis of this section does not assume any slack in the (GLL) criterion.

Lemma 5.36. Suppose that p satisﬁes (GLL). Then, for every S ⊆ [n] and a ∈ S, we have

q˘S q˘S\{a}

≥ 1 − xa.

![image 378](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile378.png>)

- Corollary 5.37 ((GLL) implies Shearer). If p satisﬁes (GLL) then p ∈ S. Proof. For any S ⊆ [n], write it as S = {s1,... ,sk}. Induction yields


q˘S q˘∅

![image 379](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile379.png>)

=

The claim follows since q˘∅ = 1.

k

q˘{s1,...,si} q˘{s1,...,si−1}

![image 380](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile380.png>)

i=1

≥

(1 − xa) > 0.

a∈S

![image 381](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile381.png>)

![image 382](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile382.png>)

![image 383](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile383.png>)

![image 384](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile384.png>)

- Corollary 5.38. If p satisﬁes (GLL) then q{qa}


≤ 1−xax

.

![image 385](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile385.png>)

![image 386](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile386.png>)

a

∅

Proof. Lemma 5.36 yields q˘[q˘n]−a

≤ 1−1x

![image 387](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile387.png>)

[n]

, so the result follows from Claim 5.25.

![image 388](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile388.png>)

a

![image 389](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile389.png>)

![image 390](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile390.png>)

![image 391](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile391.png>)

![image 392](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile392.png>)

Proof (of Lemma 5.36). We proceed by induction on |S|. The base case, S = ∅, is trivial: there is no a ∈ S to choose. Consider S = ∅ and an element a ∈ S. By Claim 5.13, we have q˘S = q˘S\{a} − paq˘S\Γ+(a). By the inductive hypothesis applied iteratively to the elements of (S \ {a}) \ (S \ Γ+(a)) = Γ(a) ∩ S, we have

Therefore, we can write

q˘S\{a} ≥ q˘S\Γ+(a)

(1 − xi).

i∈Γ(a)∩S

pa i∈Γ(a)∩S(1 − xi)

q˘S = q˘S\{a} − paq˘S\Γ+(a) ≥ q˘S\{a} 1 −

![image 393](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile393.png>)

.

By the claim’s hypothesis, pa ≤ xa i∈Γ(a)(1 − xi) ≤ xa i∈Γ(a)∩S(1 − xi), so we conclude that q˘S ≥ (1 − xa)˘qS\{a}.

These results, together with our analysis of Shearer’s criterion with slack (Corollary 5.31), immediately provide an analysis under the assumption that (GLL) holds with slack, similar to Theorem 5.8. However, this connection to Shearer’s criterion allows us to prove more.

We show that our algorithm is in fact efﬁcient even when the (GLL) criterion is tight. This might

be surprising in light of Corollary 5.28, which does not use any slack and gives an exponential bound of 1 q∅ = q˘1

≤ ni=1 1−1x

. The reason why we can prove a stronger bound is that Shearer’s criterion is never tight: as we argued already, it deﬁnes an open set, and Section 5.5 derives a quantitative bound on the slack that is always available under Shearer’s criterion.

![image 394](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile394.png>)

![image 395](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile395.png>)

![image 396](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile396.png>)

i

[n]

- Theorem 5.39. Let E1,... ,En be events and let pi = Prµ[Ei]. Suppose that the three subroutines described in Section 1.1.1 exist. If p satisﬁes (GLL) then the probability that MaximalSetResample resamples more


( nj=1 ln 1−1x

than 4 ni=1 1−xix

+ 1 + t) events is at most e−t. If (GLL) is satisﬁed with a slack of ǫ ∈ (0,1), i.e., (1+ǫ)pi ≤ xi j∈Γ(i)(1−xj), then with probability

![image 397](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile397.png>)

![image 398](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile398.png>)

i

j

- at least 1 − e−t, MaximalSetResample resamples no more than 2ǫ( nj=1 ln 1−1x


+ t) events. Proof. The ﬁrst part follows directly from Theorem 5.35, since Corollary 5.37 shows that p ∈ S and Corollary 5.38 shows that qq{i}

![image 399](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile399.png>)

![image 400](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile400.png>)

j

≤ 1−xix

. The second part follows from Corollary 5.31, using again that q∅ ≤ 1−xix

![image 401](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile401.png>)

![image 402](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile402.png>)

i

∅

- q{i}


. Theorem 1.2 follows immediately from Theorem 5.39.

![image 403](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile403.png>)

![image 404](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile404.png>)

![image 405](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile405.png>)

![image 406](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile406.png>)

![image 407](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile407.png>)

![image 408](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile408.png>)

i

## 5.7 The cluster expansion criterion

Recall that Section 1.4 introduced the cluster expansion criterion, which often gives improved quantitative bounds compared to the General LLL (such as the applications discussed in Section 4). For convenience, let us restate the cluster expansion criterion here. Given parameters y1,... ,yn, deﬁne the notation

yI ∀S ⊆ [n].

YS =

I⊆S I∈Ind

The cluster expansion criterion for a vector p ∈ [0,1]n, with respect to a graph G, is

∃y1,... ,yn > 0 such that pi ≤ yi/YΓ+(i). (CLL) This criterion was introduced in the following non-constructive form of the LLL.

- Theorem 5.40 (Bissacot et al. [8]). Let E1,... ,En be events with a (lopsi-)dependency graph G, and let pi = Prµ[Ei]. If p and G satisfy (CLL) then Prµ[ ni=1 Ei] > 0.


![image 409](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile409.png>)

To see that this strengthens the original LLL (Theorem 1.1), one may verify that (GLL) implies (CLL): if pi ≤ xi j∈Γ(i)(1 − xj), we can take yi = 1−xix

(so 1 − xi = 1+1y

) and then use the simple bound

![image 410](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile410.png>)

![image 411](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile411.png>)

i

i

yI ≤

I⊆Γ+(i) I∈Ind

yI =

I⊆Γ+(i)

(1 + yj).

j∈Γ+(i)

On the other hand, Shearer’s Lemma (Lemma 5.12) strengthens Theorem 5.40, in the sense that (CLL) implies p ∈ S. This fact was established by Bissacot et al. [8] by analytic methods that relied on earlier results [17]. In this section we establish this fact by a new proof that is elementary and self-contained.

An algorithmic form of Theorem 5.40 in the variable model was proven by Pegden [33]. In fact, that result is subsumed by the algorithm of Kolipaka and Szegedy in Shearer’s setting, since (CLL) implies p ∈ S. In this section, we prove a new algorithmic form of Theorem 5.40 in the general framework of resampling oracles.

To begin, we establish the following connection between the yi parameters and the q˘S polynomials. For convenience, let us introduce the notation Sc = [n] \ S, S + a = S ∪ {a} and S − a = S \ {a}. Lemma 5.41. Suppose that p satisﬁes (CLL). Then, for every S ⊆ [n] and a ∈ S, we have

The proof is in Section 5.7.1 below.

q˘S q˘S−a

![image 412](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile412.png>)

≥

YSc Y(S−a)c

.

![image 413](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile413.png>)

- Corollary 5.42 ((CLL) implies Shearer). If p satisﬁes (CLL) then p ∈ S. Proof. For any S ⊆ [n], write it as S = {s1,... ,sk}. Applying Lemma 5.41 repeatedly, we obtain

q˘S q˘∅

![image 414](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile414.png>)

=

k

i=1

q˘{s1,...,si} q˘{s1,...,si−1}

![image 415](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile415.png>)

≥

k

i=1

Y{s1,...,si}c Y{s1,...,si−1}c

![image 416](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile416.png>)

=

YSc Y[n]

![image 417](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile417.png>)

> 0

since YT > 0 for all T ⊆ [n] under the (CLL) criterion. Recall that q˘∅ = 1. Hence q˘S > 0 for all S ⊆ [n], which means that p is in the Shearer region.

![image 418](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile418.png>)

![image 419](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile419.png>)

![image 420](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile420.png>)

![image 421](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile421.png>)

- Corollary 5.43. If p satisﬁes (CLL) then q{qa}


≤ ya.

![image 422](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile422.png>)

∅

Proof. Lemma 5.41 yields q˘[q˘n]−a

≤ Y([Yn]−a)c

[n]c = 1 + ya, so the result follows from Claim 5.25.

![image 423](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile423.png>)

![image 424](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile424.png>)

[n]

![image 425](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile425.png>)

![image 426](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile426.png>)

![image 427](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile427.png>)

![image 428](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile428.png>)

These corollaries lead to our algorithmic result under the cluster expansion criterion. The following theorem subsumes Theorem 1.3 and adds a statement under the assumption of slack.

Theorem 5.44. Let E1,... ,En be events and let pi = Prµ[Ei]. Suppose that the three subroutines described in Section 1.1.1 exist. If p satisﬁes (CLL) then, with probability at least 1 − e−t, MaximalSetResample

resamples no more than 4( ni=1 yi)( nj=1 ln(1 + yj) + 1 + t) events. If (CLL) is satisﬁed with a slack of ǫ ∈ (0,1), i.e., (1 + ǫ)pi ≤ yi/YΓ+(i), then with probability at least

- 1 − e−t, MaximalSetResample resamples no more than 2ǫ( nj=1 ln(1 + yj) + t) events. Proof. The ﬁrst statement follows directly from Theorem 5.35, since Corollary 5.42 shows that p ∈ S


![image 429](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile429.png>)

and Corollary 5.43 shows that qq{i}

≤ yi. Next assume that (CLL) is satisﬁed with ǫ slack. We apply Corollary 5.42 and Corollary 5.43 to the point p′ = (1+ǫ)p, obtaining that p′ ∈ S and q{′j}/q∅′ ≤ yj, where qS′ denotes qS(p′). The second statement then follows directly from Corollary 5.31.

![image 430](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile430.png>)

∅

![image 431](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile431.png>)

![image 432](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile432.png>)

![image 433](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile433.png>)

![image 434](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile434.png>)

### 5.7.1 Proof of Lemma 5.41

- Claim 5.45 (The “fundamental identity” for Y ). YA = YA−a + yaYA\Γ+(a) for all a ∈ A.

Proof. Every summand yJ on the left-hand side either appears in YA−a if a  ∈ J, or can be written as ya ·yB where B = J \ Γ+(a), in which case it appears as a summand in yaYA\Γ+(a).

![image 435](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile435.png>)

![image 436](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile436.png>)

![image 437](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile437.png>)

![image 438](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile438.png>)

- Claim 5.46 (Log-subadditivity of Y ). YA∪B ≤ YA · YB for any A,B ⊆ [n].


Proof. It sufﬁces to consider the case that A and B are disjoint, as replacing B with B \ A decreases the right-hand side and leaves the left-hand side unchanged. Every summand yJ on the left-hand side can be written as yJ′ · yJ′′ with J′ = J ∩ A and J′′ = J ∩ B. The product yJ′ · yJ′′ appears as a summand on the right-hand side, and all other summands are non-negative.

![image 439](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile439.png>)

![image 440](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile440.png>)

![image 441](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile441.png>)

![image 442](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile442.png>)

Proof (of Lemma 5.41). We proceed by induction on |S|. The base case is S = {a}. In that case we have

q˘{a}

q˘∅ = q˘{a} = 1 − pa. On the other hand, by the two claims above and (CLL), we have Y[n] = Y[n]−a + yaY[n]\Γ+(a) ≥ Y[n]−a + paYΓ+(a)Y[n]\Γ+(a) ≥ Y[n]−a + paY[n].

![image 443](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile443.png>)

Therefore, YY[n]−a

≤ 1 − pa which proves the base case.

![image 444](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile444.png>)

[n]

We prove the inductive step by similar manipulations. By Claim 5.13, we have q˘S q˘S−a

q˘S\Γ+(a) q˘S−a

= 1 − pa

.

![image 445](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile445.png>)

![image 446](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile446.png>)

The inductive hypothesis applied repeatedly to the elements of S ∩ Γ(a) yields

q˘S\Γ+(a) q˘S−a

1 − pa

![image 447](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile447.png>)

Y(S\Γ+(a))c Y(S−a)c

≥ 1 − pa

![image 448](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile448.png>)

YSc∪Γ+(a) YSc+a

= 1 − pa

.

![image 449](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile449.png>)

By the two claims above and (CLL), we have

YSc+a = YSc + yaYSc\Γ+(a) ≥ YSc + paYΓ+(a)YSc\Γ+(a) ≥ YSc + paYSc∪Γ+(a). We conclude that

YSc∪Γ+(a) YSc+a

YSc+a − YSc YSc+a

YSc Y(S−a)c

q˘S q˘S−a

≥ 1 − pa

≥ 1 −

=

.

![image 450](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile450.png>)

![image 451](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile451.png>)

![image 452](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile452.png>)

![image 453](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile453.png>)

### 5.7.2 Relationship between cluster expansion and stable set sequences We remark that the following more general bound holds: For every J ∈ Ind,

pI =

I∈Prop(J)

qJ q∅

![image 454](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile454.png>)

≤ yJ. (12)

The equality holds by Lemma 5.27 and the inequality can be derived from Lemma 5.41 as follows:

qJ q∅

![image 455](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile455.png>)

=

pJq˘(Γ+(J))c q˘(∅)c

![image 456](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile456.png>)

YΓ+(J) Y∅

≤ pJ

![image 457](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile457.png>)

= pJYΓ+(J) ≤

(pjYΓ+(j)) ≤ yJ

j∈J

using Claim 5.16 for the ﬁrst equality, and Claim 5.46 and (CLL) in the last two inequalities.

A direct proof that I∈Prop(J) pI ≤ yJ can be obtained by an inductive argument similar to the proof of (4) in Section 5.2. An application of Lemma 5.27 then establishes (12). Earlier versions of this paper used this approach to relate the cluster expansion criterion and Shearer’s lemma. Our new approach in Corollary 5.42 has the advantage that it does not require the limiting arguments used in Lemma 5.27.

# 6 Conclusions

We have shown that the Lov´asz Local Lemma can be made algorithmic in the abstract framework of resampling oracles. This framework captures the General LLL as well as Shearer’s Lemma in the existential sense, and leads to efﬁcient algorithms for the primary examples of probability spaces and events satisfying lopsidependency that have been considered in the literature (as surveyed in [26]).

n j=1 log 1−1x

Our algorithmic form of the General LLL (Theorem 1.2) uses O ni=1 1−xix

resampling operations, which is roughly quadratically worse than the ni=1 1−xix

![image 458](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile458.png>)

![image 459](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile459.png>)

i

j

bound of Moser-Tardos [30]. Similarly, our algorithmic result under Shearer’s condition (Theorem 5.35) uses O ni=1 qq{i}

![image 460](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile460.png>)

i

n j=1 ln(1 +

![image 461](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile461.png>)

∅

- q{j}


q∅ ) resampling operations, which is roughly quadratically worse than the ni=1 qq{i}

bound of KolipakaSzegedy [24]. Can this quadratic loss be eliminated?

![image 462](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile462.png>)

![image 463](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile463.png>)

∅

One way to prove that result would be to prove an analog of the witness tree lemma, which is a centerpiece of the Moser-Tardos analysis [30]. The witness tree lemma has other advantages, for example in deriving parallel and deterministic algorithms. Unfortunately, the witness tree lemma is not true in the general setting of resampling oracles (see Appendix A). It is, however, true in the variable model [30] as well as in the setting of random permutations [21]. Is there a variant of our framework in which the witness tree lemma is true, and which continues to capture the LLL in full generality?

# Acknowledgements

We thank Mohit Singh for discussions at the early stage of this work. We thank David Harris for suggesting the results of Section 3.5, and for discussions relating to Appendix A.

# References

- [1] Dimitris Achlioptas and Themis Gouleakis. Algorithmic improvements of the Lov´asz local lemma via cluster expansion. In Proceedings of FSTTCS, 2012.


- [2] Dimitris Achlioptas and Fotis Iliopoulos. Random walks that ﬁnd perfect objects and the Lov´asz local lemma. In 55th IEEE Annual Symposium on Foundations of Computer Science, FOCS 2014, Philadelphia, PA, USA, October 18-21, 2014, pages 494–503, 2014.
- [3] Dimitris Achlioptas and Fotis Iliopoulos. Random walks that ﬁnd perfect objects and the Lov´asz local lemma. CoRR, abs/1406.0242v3, 2015.
- [4] Dimitris Achlioptas and Fotis Iliopoulos. Focused stochastic local search and the Lov´asz local lemma. In Proc. of 27th ACM-SIAM SODA, 2016, to appear.
- [5] Saieed Akbari and Alireza Alipour. Multicolored trees in complete graphs. J. Graph Theory, 54:3:221– 232, 2007.
- [6] N. Alon and J. Spencer. The Probabilistic Method. Wiley, 2000.
- [7] Noga Alon, Joel Spencer, and Prasad Tetali. Covering with latin transversals. Discrete Applied Mathematics, 57:1:1–10, 1995.
- [8] R. Bissacot, R. Fern´andez, A. Procacci, and B. Scoppola. An improvement of the Lov´asz local lemma via cluster expansion. Combin. Probab. Comput., 20:709–719, 2011.
- [9] Julia Bo¨ttcher, Yoshiharu Kohayakawa, and Aldo Procacci. Properly coloured copies and rainbow copies of large graphs with small maximum degree. Random Structures and Algorithms, 40(4), 2012.
- [10] Andrei Broder. Generating random spanning trees. In Proceedings of SFCS, pages 442–447, 1989.
- [11] Richard A. Brualdi and Susan Hollingsworth. Multicolored trees in complete graphs. J. Combin. Theory Ser. B, 68, 1996.
- [12] James M. Carraher, Stephen G. Hartke, and Paul Horn. Edge-disjoint rainbow spanning trees in complete graphs, 2013.
- [13] Karthekeyan Chandrasekaran, Navin Goyal, and Bernhard Haeupler. Deterministic algorithms for the Lov´asz local lemma. SIAM Journal on Computing, 42(6), 2013.
- [14] Kai-Min Chung, Seth Pettie, and Hsin-Hao Su. Distributed algorithms for the Lov´asz local lemma and graph coloring. In Proceedings of PODC, 2014.
- [15] Paul Erdo¨s and L´aszlo´ Lov´asz. Problems and results on 3-chromatic hypergraphs and some related questions. In A. Hajnal et al., editor, Inﬁnite and ﬁnite sets, volume 10 of Colloquia Mathematica Societatis J´anos Bolyai, pages 609–628. North-Holland, Amsterdam, 1975.
- [16] Paul Erdo¨s and Joel Spencer. The Lopsided Lov´asz Local Lemma and Latin transversals. Discrete Applied Mathematics, 30:151–154, 1991.
- [17] R. Fern´andez and A. Procacci. Cluster expansion for abstract polymer models: New bounds from an old approach. Comm. Math. Phys, 274:123–140, 2007.
- [18] Heidi Gebauer, Tibor Szabo´, and G´abor Tardos. The local lemma is tight for SAT. In Proceedings of SODA, 2011.


- [19] Ioannis Giotis, Lefteris Kirousis, Kostas I. Psaromiligkos, and Dimitrios M. Thilikos. On the algorithmic Lov´asz local lemma and acyclic edge coloring. In Proceedings of ANALCO, 2015.
- [20] Bernhard Haeupler, Barna Saha, and Aravind Srinivasan. New constructive aspects of the Lov´asz local lemma. Journal of the ACM, 58(6), 2011.
- [21] David G. Harris and Aravind Srinivasan. A constructive algorithm for the Lov´asz Local Lemma on permutations. In Proceedings of the Twenty-Fifth Annual ACM-SIAM Symposium on Discrete Algorithms, SODA 2014, Portland, Oregon, USA, January 5-7, 2014, pages 907–925, 2014.
- [22] Richard Holley. Remarks on the FKG inequalities. Communications in Mathematical Physics, 36:227– 231, 1974.
- [23] Donald E. Knuth. The art of computer programming, Volume 4B (draft, pre-fascicle 6a), 2015. http://www-cs-faculty.stanford.edu/˜uno/fasc6a.ps.gz.
- [24] Kashyap Kolipaka and Mario Szegedy. Moser and Tardos meet Lov´asz. In Proceedings of STOC, 2011.
- [25] Kashyap Kolipaka, Mario Szegedy, and Yixin Xu. A sharper local lemma with improved applications. In Proceedings of APPROX/RANDOM, 2012.
- [26] Lincoln Lu, Austin Mohr, and L´aszlo´ Sz´ekely. Quest for negative dependency graphs. Recent Advances in Harmonic Analysis and Applications, 25:243–258, 2013.
- [27] Austin Mohr. Applications of the lopsided Lov´asz local lemma regarding hypergraphs. PhD thesis, University of South Carolina, 2013.
- [28] Robin Moser. Exact Algorithms for Constraint Satisfaction Problems. PhD thesis, ETH Zu¨rich, 2012.
- [29] Robin A. Moser. A constructive proof of the Lov´asz local lemma. In Proceedings of STOC, 2009.
- [30] Robin A. Moser and G´abor Tardos. A constructive proof of the general Lov´asz Local Lemma. Journal of the ACM, 57(2), 2010.
- [31] Sokol Ndreca, Aldo Procacci, and Benedetto Scoppola. Improved bounds on coloring of graphs. European Journal of Combinatorics, 33(4), 2012.
- [32] Christos H. Papadimitriou. On the complexity of the parity argument and other inefﬁcient proofs of existence. Journal of Computer and System Sciences, 48:498–532, 1994.
- [33] Wesley Pegden. An extension of the Moser-Tardos algorithmic local lemma. SIAM J. Discrete Math, 28:911–917, 2014.
- [34] Alexander Schrijver. Combinatorial Optimization: Polyhedra and Efﬁciency. Springer, 2004.
- [35] Alexander D. Scott and Alan D. Sokal. The Repulsive Lattice Gas, the Independent-Set Polynomial, and the Lov´asz Local Lemma. Journal of Statistical Physics, 118(5):1151–1261, 2005.
- [36] James B. Shearer. On a problem of Spencer. Combinatorica, 5(3), 1985.
- [37] Joel Spencer. Asymptotic lower bounds for Ramsey functions. Discrete Mathematics, 20:69–76, 1977.


#### [38] David E. Woolbright and Hung-Lin Fu. On the existence of rainbows in 1-factorizations of K2n. Journal of Combinatorial Designs, 6:1:1–20, 1998.

# A A counterexample to the witness tree lemma

A cornerstone of the analysis of Moser and Tardos [30] is the witness tree lemma. It states (roughly) that for any tree of events growing backwards in time from a certain root event Ei, with the children of each node Ei′ being neighboring events resampled before Ei′, the probability that this tree is consistent with the execution of the algorithm is at most the product of the probabilities of all events in the tree. (We give a more precise statement below.) Extensions of this lemma have been crucial in the work of Kolipaka-Szegedy on algorithmic forms of Shearer’s Lemma [24] and work of Harris-Srinivasan on the algorithmic local lemma for permutations [21]. The witness tree lemma leads to somewhat stronger quantitative bounds than the ones we obtain, and it has been also useful for other purposes: derandomization of LLL algorithms [30, 13], parallel algorithms [30, 14], and handling exponentially many events [20]. Therefore, it would be desirable to prove the witness tree lemma in our general framework of resampling oracles.

Unfortunately, this turns out to be impossible. The main purpose of this section is to show that the witness tree lemma is false in the framework of resampling oracles in a strong sense. Whereas in typical scenarios the Moser-Tardos algorithm only requires witness trees of depth O(log n) with high probability, in the resampling oracle framework the stable set sequences (and an analogous notion of witness trees) can have nearly-linear length with constant probability.

Before we proceed, we deﬁne a few notions necessary for the formulation of the witness tree lemma. Our deﬁnitions here are natural extensions of the notions from [30] to the setting of resampling oracles.

- Deﬁnition A.1. Given a lopsided association graph G on vertex set [n], a witness tree is a ﬁnite rooted tree

T, with each vertex v in T given a label Ev ∈ [n], such that the children of a vertex v receive labels from Γ+(Ev).

- Deﬁnition A.2. We say that a witness tree T with root r appears in the log of the algorithm, if event Er is resampled at some point and the tree is produced by the following procedure: process the resampled events from that point backwards, and for each resampled event j such that j ∈ Γ+(Ev) for some v in the tree, pick such a vertex v of maximum depth in the tree and create a new child w of v with label Ew = j.


The witness tree lemma, in various incarnations, states that the probability of a witness tree T appearing

in the log of an LLL algorithm is at most v∈T Pr[EEv]. We show here that this can be grossly violated in the setting of resampling oracles. Our example actually uses the independent variable setting but resampling

oracles different from the natural ones considered by Moser and Tardos.

Example. Consider independent Bernoulli variables Xi,Yij,Zi and W where 1 ≤ i ≤ k and 1 ≤ j ≤ ℓ. The probability distribution µ is uniform on the product space of these random variables. Consider the

following events:

- • Ei = {Xi = 0}
- • Eij = Yij = 0
- • E′ = {W = 1}


These events are mutually independent. However, let us consider a dependency graph G where Ei ∼ Eij for each 1 ≤ i ≤ k,1 ≤ j ≤ ℓ; this is a conservative choice but nevertheless a valid one for our events. (One

could also tweak the probability space slightly so that neighboring events are actually dependent.) In any case, E′ is an isolated vertex in the graph.

We deﬁne resampling oracles as follows. In the following, Q describes a fresh new sample of a Bernoulli variable. Only the variables relevant to the respective oracle are listed as arguments.

- • ri(Xi) = Q
- • rij(Xi,Yij,Zi) = (Zi,Q,Xi)
- • r′(W,Z1,... ,Zk) = (Z1,... ,Zk,Q).


- Claim A.3. ri,rij,r′ are valid resampling oracles for the events Ei,Eij,E′ and the dependency graph G.

Proof. ri resamples only the variable Xi relevant to event Ei and hence cannot cause any other event to occur. Conditioned on Ei = {Xi = 0}, it clearly produces the uniform distribution.

rij switches the variables Xi and Zi and thus can cause Ei to occur (which is consistent with the dependency graph G). Conditioned on Eij = Yij = 0 , it makes Yij uniformly random and preserves a uniform distribution on (Xi,Zi).

r′ affects the values of W,Z1,... ,Zk but no event depends on Z1,... ,Zk, so r′ cannot cause any event except E′ to occur. Conditioned on E′ = {W = 1}, since (Z1,... ,Zk) are distributed uniformly, it produces again the uniform distribution.

![image 464](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile464.png>)

![image 465](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile465.png>)

![image 466](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile466.png>)

![image 467](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile467.png>)

The Moser-Tardos algorithm. First, let us consider the Moser-Tardos algorithm: In the most general form, it resamples in each step an arbitrary occurring event. For concreteness, let’s say that the algorithm always resamples the occurring event of minimum index (in some ﬁxed ordering).

- Claim A.4. If the Moser-Tardos algorithm considers events in the order (Ei,Eij,E′), then at the time it gets to resample E′, the variables Z1,... ,Zk are independent are equal to 1 with probability 1 − 1/2ℓ+1 each.


Proof. Let us ﬁx i. Whenever some variable Yij is initially equal to 0, we have to resample Eij at some point. However, we only resample Eij if Ei does not occur, which means that Xi must be 1 at that time. So the resampling oracle Eij forces Zi to be equal to 1. The only way Zi could remain equal to 0 is that it is initially equal to 0 and none of the events Eij need to be resampled, which happens with probability 1/2ℓ. Therefore, when we’re done with Ei and Eij for 1 ≤ j ≤ ℓ, Zi is equal to 0 with probability 1/2ℓ+1. This happens independently for each i.

![image 468](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile468.png>)

![image 469](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile469.png>)

![image 470](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile470.png>)

![image 471](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile471.png>)

Lemma A.5. The probability that the Moser-Tardos algorithm resamples E′ at least k times in a row is at least 21(1 − 2ℓ1+1)k−1.

![image 472](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile472.png>)

![image 473](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile473.png>)

Proof. By the ordering of events, E′ is resampled only when all other events have been ﬁxed. Also, resampling E′ cannot cause any other event, so the algorithm will terminate afterwards. However, as we argued above, when we get to resampling E′, each variable Zi is equal to 1 independently with probability 1 − 1/2ℓ+1. Considering the resampling oracle r′(W,Z1,... ,Zk) = (Z1,... ,Zk,Q), if W as well as all the variables Zi are equal to 1, it will take at least k resamplings to clear the queue and get a chance to avoid event E′. This happens with probability 21(1 − 2ℓ1+1)k−1.

![image 474](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile474.png>)

![image 475](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile475.png>)

![image 476](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile476.png>)

![image 477](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile477.png>)

![image 478](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile478.png>)

![image 479](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile479.png>)

Let T consist of a path of k vertices labeled E′. For k = 2ℓ, we conclude that the witness tree T appears with constant probability in the log of the Moser-Tardos algorithm, as opposed to 1/2k which would follow from the witness tree lemma.

The MaximalSetResample algorithm. A slightly more involved analysis is necessary in the case of MaximalSetResample. By nature of this algorithm, we would resample E′ “in parallel” with the other events and so the variables evolve somewhat differently.

Claim A.6. For each i independently, after 2 iterations of the MaximalSetResample algorithm, Zi = 1 with probability 1−1/2ℓ+1. Any further updates of Zi other than those caused by resampling E′ can only change the variable from 0 to 1.

Proof. The claim is that unless Zi = 0 and Yi1 = ... ,= Yiℓ = 1 initially, in the ﬁrst two iterations we will possibly resample Ei and then one of the events Eij, which makes Zi equal to 1. Any further update to Zi occurs only when E′ is resampled (which shifts the sequence (Z1,... ,Zk)) or when Eij is resampled, which makes Zi equal to 1.

![image 480](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile480.png>)

![image 481](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile481.png>)

![image 482](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile482.png>)

![image 483](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile483.png>)

Lemma A.7. The probability that MaximalSetResample resamples E′ at least k times in a row is at least 1 4(1 − 2ℓ1+1)k−2.

![image 484](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile484.png>)

![image 485](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile485.png>)

Proof. In the ﬁrst two iterations, the probability that E′ is resampled twice is at least 1/4 (the values of W and Z1 are initially uniform, and if Z1 is updated, it can only increase the probability that we resample E′). Independently, the probability that Z2 = ... = Zk−1 = 1 after the ﬁrst two iterations is (1−1/2ℓ+1)k−2, by the preceding claim. (We are not using Z1 which is possibly correlated with the probability of resampling E′ in the second iteration, and Zk which would be refreshed by this resampling in the second iteration.) If this happens, we will continue to resample E′ at least k − 2 additional times, because it will take k − 2 executions of r′ before a zero can reach the variable W.

![image 486](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile486.png>)

![image 487](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile487.png>)

![image 488](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile488.png>)

![image 489](<2015-harvey-algorithmic-proof-lovasz-local_images/imageFile489.png>)

Again, consider setting k = 2ℓ. The total number of events is n = O(kℓ), so ℓ = Θ(log n) and k = Θ(n/log n). With constant probability, the witness tree T consisting of a path of k vertices labeled E′ will appear in the log of MaximalSetResample algorithm. Thus, with constant probability, the algorithm will require a stable set sequence of length at least k.

