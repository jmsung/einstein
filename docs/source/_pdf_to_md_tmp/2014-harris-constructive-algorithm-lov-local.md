## A CONSTRUCTIVE ALGORITHM FOR THE LOVASZ´ LOCAL LEMMA ON PERMUTATIONS1

DAVID G. HARRIS2 AND ARAVIND SRINIVASAN3

# arXiv:1612.02663v1[cs.DS]8Dec2016

Abstract. While there has been signiﬁcant progress on algorithmic aspects of the Lov´asz Local Lemma (LLL) in recent years, a noteworthy exception is when the LLL is used in the context of random permutations. The breakthrough algorithm of Moser & Tardos only works in the setting of independent variables, and does not apply in this context. We resolve this by developing a randomized polynomial-time algorithm for such applications. A noteworthy application is for Latin transversals: the best-known general result here (Bissacot et al., improving on Erdo˝s and Spencer), states that any n × n matrix in which each entry appears at most (27/256)n times, has a Latin transversal. We present the ﬁrst polynomial-time algorithm to construct such a transversal. We also develop RNC algorithms for Latin transversals, rainbow Hamiltonian cycles, strong chromatic number, and hypergraph packing.

In addition to eﬃciently ﬁnding a conﬁguration which avoids bad-events, the algorithm of Moser & Tardos has many powerful extensions and properties. These include a well-characterized distribution on the output distribution, parallel algorithms, and a partial resampling variant. We show that our algorithm has nearly all of the same useful properties as the Moser-Tardos algorithm, and present a comparison of this aspect with recent works on the LLL in general probability spaces.

1. Introduction

Recent years have seen substantial progress in developing algorithmic versions of the Lov´sz Local Lemma (LLL) and some of its generalizations, starting with the breakthrough work of Moser & Tardos [32]: see, e.g., [18, 20, 26, 33]. However, one major relative of the LLL that has eluded constructive versions, is the “lopsided” version of the LLL (with the single exception of the CNF-SAT problem [32]). A natural setting for the lopsided LLL is where we have one or many random permutations [14, 28, 31]. This approach has been used for Latin transversals [9, 14, 38], hypergraph packing [29], certain types of graph coloring [10], and in proving the existence of certain error-correcting codes [25]. However, current techniques do not give constructive versions in this context. We develop a randomized polynomial-time algorithm to construct such permutation(s) whose existence is guaranteed by the lopsided LLL, leading to several algorithmic applications in combinatorics. Furthermore, since the appearance of the conference version of this work [21], related works including [1, 22, 27] have been published; we make a comparison to these in Sections 1.2 and 6.3, detailing which of our contributions do not appear to follow from the frameworks of [1, 22, 27].

1.1. The Lopsided Lova´sz Local Lemma and random permutations. Suppose we want to select permutations π1,...,πN, where each πk is a permutation on the set [nk] = {1,...,nk}. In addition we have a set B of “bad events.” We want to select permutations π such that no bad event is true. The lopsided version of the Lov´sz Local Lemma (LLL) can be used to prove that such permutations exist, under suitable conditions.

We suppose that that the family of bad events B consists of atomic bad-events. That is, each bad event B ∈ B is a set of tuples B = {(k1,x1,y1),...,(kr,xr,yr)}; it is true iﬀ we have (πk

(x1) = y1)∧···∧(πk

(xr) = yr). (Complex bad-events can usually be decomposed into atomic bad-events, so this does not lose much generality.) We will assume that no bad-event contains two tuples (k,x,y),(k,x,y ) where y = y , or two tuples (k,x,y),(k,x ,y) where x = x ; such a bad-event would have probability zero, and could be ignored.

1

r

1This is an extended version of a paper which appeared in the Proc. ACM-SIAM Symposium on Discrete Algorithms, (SODA) 2014.

- 2Department of Applied Mathematics, University of Maryland, College Park, MD 20742. Research supported in part by

NSF Awards CNS-1010789 and CCF-1422569. Email: davidgharris29@hotmail.com.

- 3Department of Computer Science and Institute for Advanced Computer Studies, University of Maryland, College Park,


MD 20742. Research supported in part by NSF Awards CNS-1010789 and CCF-1422569, and by a research award from Adobe, Inc. Email: srin@cs.umd.edu.

1

To apply the Lopsided Local Lemma in this setting, we need to deﬁne a dependency graph with respect to these bad events. We connect two bad events B,B by an edge iﬀ they overlap in one slice of the domain or range of a permutation; namely, iﬀ there are some k,x,y1,y2 with (k,x,y1) ∈ B,(k,x,y2) ∈ B or there are some k,x1,x2,y with (k,x1,y) ∈ B,(k,x2,y) ∈ B . We write this B ∼ B ; note that B ∼ B. The following notation will be useful: for pairs (x1,y1),(x2,y2), we write (x1,y1) ∼ (x2,y2) if x1 = x2 or y1 = y2 (or both). Thus, another way to write B ∼ B is that “there are (k,x,y) ∈ B, (k,x ,y ) ∈ B with (x,y) ∼ (x ,y )”. We will use the following notation at various points: we write (k,x,∗) to mean any (or all) triples of the form (k,x,y), and similarly for (k,∗,y), or (x,∗) etc. Therefore, yet another way to write the condition B ∼ B is that there are (k,x,∗) ∈ B,(k,x,∗) ∈ B or (k,∗,y) ∈ B,(k,∗,y) ∈ B .

Now suppose we select each πk uniformly at random and independently. This deﬁnes a probability space Ω, to which we can apply the lopsided LLL. One can show that the probability of avoiding a bad event B can only be increased by avoiding other bad events B  ∼ B [29]. Thus, in the language of the lopsided LLL, the relation ∼ deﬁnes a negative-dependence graph among the bad-events. (See [28, 29, 31] for a study of the connection between negative dependence, random injections/permutations, and the lopsided LLL.) Hence, the standard lopsided-LLL criterion is as follows:

Theorem 1.1 ([29]). Suppose that there is some assignment µ : B → [0,∞) such that for all bad-events B ∈ B we have

µ(B) ≥ PΩ(B)

(1 + µ(B )).

B ∼B

Then the random process of selecting each πk uniformly at random and independently has a positive probability of selecting permutations that avoid all the bad-events.

Remark: The condition of Theorem 1.1 about the existence of such a µ is equivalent to the more-familiar LLL formulation “there exists x : B → [0,1) such that for all B ∈ B, PΩ(B) ≤ x(B) B ∼B:B =B(1−x(B ))”: just set µ(B) = x(B)/(1 − x(B)).

The “positive probability” of Theorem 1.1 is however typically exponentially small, as is standard for the LLL. As mentioned above, a variety of papers have used the framework of Theorem 1.1 for proving the existence of various combinatorial structures. Unfortunately, the algorithms for the LLL, such as MoserTardos resampling [32], do not apply in this setting. The problem is that such algorithms have a more restrictive notion of when two bad-events are dependent; namely, that they share variables. (The MoserTardos algorithm allows for a restricted type of dependence called lopsidependence: two bad-events which share a variable but always agree on that value, are counted as independent. This is not strong enough to generate permutations.) So we do not have an eﬃcient algorithm to generate such permutations, we can merely show that they exist.

We develop an algorithmic analogue of the LLL for permutations. The necessary conditions for our Swapping Algorithm are the same as for the LLL (Theorem 1.1); however, we will construct such permutations in randomized polynomial (typically linear or near-linear) time. Our setting is far more complex than in similar contexts such as those of [32, 20, 33], and requires many intermediate results ﬁrst. The main complication is that when we encounter a bad event involving “πk(x) = y”, and perform our algorithm’s random swap associated with it, we could potentially be changing any entry of πk. In contrast, when we resample a variable in [32, 20, 33], all the changes are conﬁned to that variable. There is a further technical issue: the current witness-tree-based algorithmic versions of the LLL such as [32, 20], identify, for each bad-event B in the witness-tree τ, some necessary event occurring with probability at most PΩ(B). This is not the proof we employ here; there are signiﬁcant additional terms (“(nk − A0k)!/n!” – see the proof of Lemma 3.1) that are gradually “discharged” over time.

We also develop RNC versions of our algorithms. Going from serial to parallel is fairly direct in [32]; our main bottleneck here is that when we resample an “independent” set of bad events, they could still inﬂuence each other.

(Note: we distinguish in this paper between the probability of events which occur in our algorithm, which we denote simply by P, and the probabilities of events within the space Ω, which we denote by PΩ.)

- 1.2. Comparison with other LLLL algorithms. Building on an earlier version of this work [21], there have been several papers which have developed generic frameworks for variations of the Moser-Tardos algorithm applied to other probability spaces. In [1], Achlioptas & Iliopoulos gave an algorithm which is


based on a compression analysis for a random walk; this was improved for permutations and matchings by Kolmogorov [27]. In [22], Harvey & Vondr´k gave a probabilistic analysis similar to the parallel MoserTardos algorithm. These frameworks both include the permutation LLL as well as some other combinatorial applications. These papers give much simpler proofs that the Swapping Algorithm terminates quickly.

The Moser-Tardos algorithm has many other powerful properties and extensions, beyond the fact that it eﬃciently ﬁnds a conﬁguration avoiding bad-events. These properties include a well-characterized distribution on the output distribution at the end of the resampling process, a corresponding eﬃcient parallel (RNC) algorithm, a partial-resampling variant (as developed in [20]), and an arbitrary (even adversarial) choice of which bad-event to resample. All of these properties follow from the Witness Tree Lemma we show for our Swapping Algorithm. The more generalized LLLL frameworks of [1, 22] have a limited ability to show such extensions.

We will discuss the relationship between this paper and the other LLLL frameworks further in Section 6.3. As one example of the power of our proof method, we develop a parallel Swapping Algorithm in Section 7; we emphasize that such a parallel algorithm cannot be shown using the results of [1] or [22]. A second example is provided by Theorem 8.2, results such as which we do not see how to develop using the frameworks of [1, 22, 27].

One of the main goals of our paper is to provide a model for what properties a generalized LLLL algorithm should have. In our view, there has been signiﬁcant progress toward this goal but there remain many missing pieces toward a true generalization of the Moser-Tardos algorithm. We will discuss this more in a concluding section, Section 9.

- 1.3. Applications. We present algorithmic applications for four classical combinatorial problems: Latin transversals, rainbow Hamiltonian cycles, strong chromatic number, and edge-disjoint hypergraph packing. In addition to the improved bounds, we wish to highlight that our algorithmic approach can go beyond Theorem 1.1: as we will see shortly, one of our (asymptotically-optimal) algorithmic results on Latin transversals, could not even have been shown non-constructively using the lopsided LLL prior to this work.

The study of Latin squares and the closely-related Latin transversals is a classical area of combinatorics, going back to Euler and earlier [12]. Given an m × n matrix A with m ≤ n, a transversal of A is a choice of m elements from A, one from each row and at most one from any column. Perhaps the major open problem here is: given an integer s, under what conditions will A have an s-transversal: a transversal in which no value appears more than s times [9, 13, 14, 36, 37, 38]? The usual type of suﬃcient condition sought here is an upper bound ∆ on the number of occurrences of any given value in A. That is, we ask: what is the maximum ∆ such that any m × n matrix A in which each value appears at most ∆ times, is guaranteed to have an s-transversal? We denote this quantity by L(s;m,n). The case s = 1 is perhaps most studied, and 1-transversals are also called Latin transversals. The case m = n is also commonly studied (and includes Latin squares as a special case), and we will also focus on these. It is well-known that L(1;n,n) ≤ n−1 [37]. In perhaps the ﬁrst application of the lopsided LLL to random permutations, Erd˝s & Spencer essentially proved a result very similar to Theorem 1.1, and used it to show that L(1;n,n) ≥ n/(4e) [14]. (Their paper shows that L(1;n,n) ≥ n/16; the n/(4e) lower-bound follows easily from their technique.) To our knowledge, this is the ﬁrst Ω(n) lower-bound on L(1;n,n). Alon asked if there is a constructive version of this result [4]. Building on [14] and using the connections to the LLL from [34, 35], Bissacot et al. showed non-constructively that L(1;n,n) ≥ (27/256)n [9]. Our result makes these results constructive.

The lopsided LLL has also been used to study the case s > 1 [38]. Here, we prove a result that is asymptotically optimal for large s, except for the lower-order O(√s) term: we show (algorithmically) that L(s;n,n) ≥ (s − O(√s)) · n. An interesting fact is that this was not known even non-constructively before: Theorem 1.1 roughly gives L(s;n,n) ≥ (s/e) · n. We also give faster serial and perhaps the ﬁrst RNC algorithms with good bounds, for the strong chromatic number. Strong coloring is quite well-studied [5, 8, 16, 23, 24], and is in turn useful in covering a matrix with Latin transversals [7].

- 1.4. Outline. In Section 2 we introduce our Swapping Algorithm, a variant of the Moser-Tardos resampling algorithm. In it, we randomly select our initial permutations; as long as some bad-event is currently true, we perform certain random swaps to randomize (or resample) them.


Section 3 introduces the key analytic tools to understand the behavior of the Swapping Algorithm, namely the witness tree and the witness subdag. The construction for witness trees follows [32]; it provides an explanation or history for the random choices used in each resampling. The witness subdag is a related

concept, which is new here; it provides a history not for each resampling, but for each individual swapping operation performed during the resamplings.

In Section 4, we show how these witness subdags may be used to deduce partial information about the permutations. As the Swapping Algorithm proceeds in time, the witness subdags can also be considered to evolve over time. At each stage of this process, the current value of the witness subdags provides information about the current values of the permutations. In Section 5, we use this process to make probabilistic predictions for certain swaps made by the Swapping Algorithm: namely, whenever the witness subdags change, the swaps must be highly constrained so that the permutations still conform to them. We calculate the probability that the swaps satisfy these constraints.

Section 6 puts the analyses of Sections 3, 4, 5 together, to prove that our Swapping Algorithm terminates in polynomial time under the same conditions as those of Theorem 1.1; also, as mentioned in Section 1.2, Section 6.3 discusses certain contributions that our approach leads to that do not appear to follow from [1, 22, 27].

In Section 7, we introduce a parallel (RNC) algorithm corresponding to the Swapping Algorithm. This is similar in spirit to the Parallel Resampling Algorithm of Moser & Tardos. In the latter algorithm, one repeatedly selects a maximal independent set (MIS) of bad-events which are currently true, and resamples

- them in parallel. In our setting, bad-events which are “independent” in the LLL sense (that is, they are not connected via ∼), may still inﬂuence each other; a great deal of care must be taken to avoid these conﬂicts.

- Section 8 describes a variety of combinatorial problems to which our Swapping Algorithm can be applied,

including Latin transversals, strong chromatic number, and hypergraph packing. Finally, we conclude in

- Section 9 with a discussion of future goals for the construction of a generalized LLL algorithm.


2. The Swapping Algorithm We will analyze the following Swapping Algorithm algorithm to ﬁnd a satisfactory π1,...,πN:

- (1) Generate the permutations π1,...,πN uniformly at random and independently.
- (2) While there is some true bad-event:


(3) Choose some true bad-event B ∈ B arbitrarily. For each permutation that is involved in B, we perform a swapping of all the relevant entries. (We will describe the swapping subroutine “Swap” shortly.) We refer to this step as a resampling of the bad-event B.

Each permutation involved in B is swapped independently, but if B involves multiple entries from a single permutation, then all such entries are swapped simultaneously. For example, if B consisted of triples (k1,x1,y1),(k2,x2,y2),(k2,x3,y3), then we would perform Swap(π1;x1) and Swap(π2;x2,x3), where the “Swap” procedure is given next.

The swapping subroutine Swap(π;x1,...,xr) for a permutation π : [t] → [t] as follows: Repeat the following for i = 1,...,r:

- • Select x i uniformly at random among [t] − {x1,...,xi−1}.
- • Swap entries xi and x i of π.


Note that at every stage of this algorithm all the πk are permutations, and if this algorithm terminates,

- then the πk must avoid all the bad-events. So our task will be to show that the algorithm terminates in polynomial time. We measure time in terms of a single iteration of the main loop of the Swapping Algorithm:


each time we run one such iteration, we increment the time by one. We will use the notation πkT to denote the value of permutation πk after time T. The initial sampling of the permutation (after Step (1)) generates πk0.

The swapping subroutine seems strange; it would appear more natural to allow x i to be uniformly selected among [t]. However, the swapping subroutine is nothing more than than the Fisher-Yates Shuﬄe for generating uniformly-random permutations. If we allowed x i to be chosen from [t] then the resulting permutation would be biased. The goal is to change πk in a minimal way to ensure that πk(x1),...,πk(xr) and πk−1(y1),...,πk−1(yr) are adequately randomized.

There are alternative methods for generating random permutations, and many of these can replace the Swapping subroutine without changing our analysis. We discuss a variety of such equivalencies in Appendix A; these will be used in various parts of our proofs. We note that one class of algorithms that has a very diﬀerent behavior is the commonly used method to generate random reals ri ∈ [0,1], and then form the

permutation by sorting these reals. When encountering a bad-event, one would resample the aﬀected reals ri. In our setting, where the bad-events are deﬁned in terms of speciﬁc values of the permutation, this is not a good swapping method because a single swap can drastically change the permutation. When bad-events are deﬁned in terms of the relative rankings of the permutation (e.g. a bad event is π(x1) < π(x2) < π(x3)), then this is a better method and can be analyzed in the framework of the ordinary Moser-Tardos algorithm.

3. Witness trees and witness subdags

To analyze the Swapping Algorithm, following the Moser-Tardos approach [32], we introduce the concept of an execution log and a witness tree. The execution log consists of listing every resampled bad-event, in the order that they are resampled. We form a witness tree to justify the resampling at time t. We start with the resampled bad-event B corresponding to time t, and create a single node in our tree labeled by this event. We move backward in time; for each bad-event B we encounter, we add it to the witness tree if B ∼ B for some event B already in the tree: we choose such a B that has the maximum depth in the current tree (breaking ties arbitrarily), and make B a child of this B (there could be many nodes labeled B ). If B  ∼ B for all B in the current tree, we ignore this B and keep moving backward in time. To make this discussion simpler we say that the root of the tree is at the “top” and the deep layers of the tree are at the “bottom”. The top of the tree corresponds to later events, the bottom of the tree to the earliest events.

For the remainder of this section, the dependence on the “justiﬁed” bad-event at time t at the root of the tree will be understood; we will omit it from the notation.

We will use the term “witness tree” in two closely-related senses in the following proof. First, when we run the Swapping Algorithm, we produce a witness tree τˆT; this is a random variable. Second, we might want to ﬁx some labeled tree τ, and discuss hypothetically under what conditions it could be produced or what properties it has; in this sense, τ is a speciﬁc object. We will always use the notation τˆT to denote the speciﬁc witness tree produced by running the Swapping Algorithm, corresponding to resampling time T. We write τˆ as short-hand for τˆT where T is understood from context (or irrelevant).

If τ is a witness tree, we say that τ appears iﬀ τˆT = τ for some T ≥ 0. The critical lemma that allows us to analyze the behavior of this algorithm is the Witness Tree Lemma:

- Lemma 3.1 (Witness Tree Lemma). Let τ be a witness tree, with nodes labeled B1,...,Bs. The probability that τ was produced as the witness tree corresponding any any resampling time t ≥ 0, is at most


P(τ appears) ≤ PΩ(B1)···PΩ(Bs)

Note that the probability of the event B within the space Ω can be computed as follows: if B contains r1,...,rN elements from each of the permutations 1,...,N, (and B is not impossible) then we have

(nN − rN)! nN!

(n1 − r1)! n1!

...

PΩ(B) =

This lemma is superﬁcially similar to the corresponding lemma in Moser-Tardos [32]. However, the proof will be far more complex, and we will require many intermediate results ﬁrst. The main complication is that when we encounter a bad-event involving πk(x) = y, and we perform the random swap associated with it, then we could potentially be changing any entry of πk. By contrast, in the usual Moser-Tardos algorithm, when we resample a variable, all the changes are conﬁned to that variable. However, as we will see, the witness tree will leave us with enough clues about which swap was actually performed that we will be able

- to narrow down the possible impact of the swap. The analysis in the next sections can be very complicated. We have two recommendations to make these


proofs easier. First, the basic idea behind how to form and analyze these trees comes from [32]; the reader should consult that paper for results and examples which we omit here. Second, one can get most of the intuition behind these proofs by considering the situation in which there is a single permutation, and the bad-events all involve just a single element; that is, every bad-event has the form π(xi) = yi. In this case, the witness subdags (deﬁned later) are more or less equivalent to the witness tree. (The main point of the witness subdag concept is, in eﬀect, to reduce bad-events to their individual elements.) When reading the following proofs, it is a good idea to keep this special case in mind. In several places, we will discuss how certain results simplify in that setting.

The following proposition is the main reason the witness tree encodes suﬃcient information about the sequence of swaps:

### Proposition 3.2. Suppose that at some time t0 we have πt

### k (X) = Y , and at some later time t2 > t0 we have πt

0

k (X) = Y . Then there must have occurred at some intermediate time t1 some bad-event including (k,X,∗) or (k,∗,Y ). Proof. Let t1 ∈ [t0,t2 − 1] denote the earliest time at which we had πt

2

1+1(X) = Y ; this must be due to encountering some bad-event including the elements (k,x1,y1),...,(k,xr,yr) (and possibly other elements from other permutations). Suppose that πk(X) = Y was ﬁrst caused by swapping entry xi, which at that time had πk(xi) = y i, with some x .

After this swap, we have πk(xi) = y and πk(x ) = y i. Evidently x = X or xi = X. In the second case, the bad event at time t1 included (k,X,∗) as desired and we are done.

So suppose x = X and y i = Y . So at the time of the swap, we had πk(xi) = Y . The only earlier swaps in this resampling were with x1,...,xi−1; so at the beginning of time t1, we must have had πt

k (xj) = Y for some j ≤ i. This implies that yj = Y , so that the bad-event at time t1 included (k,∗,Y ) as desired.

1

To explain some of the intuition behind Lemma 3.1, we note that Proposition 3.2 implies Lemma 3.1 for a singleton witness tree. Corollary 3.3. Suppose that τ is a singleton node labeled by B. Then P(τ appears) ≤ PΩ(B).

Proof. Suppose τˆT = τ. We claim that B must have been true of the initial conﬁguration. For suppose that (k,x,y) ∈ B but in the initial conﬁguration we have πk(x) = y. At some later point in time t ≤ T, the event B must become true. By Proposition 3.2, then there is some time t < t at which we encounter a bad-event B including (k,x,∗) or (k,∗,y). This bad-event B occurs earlier than B, and B ∼ B. Hence, we would have placed B below B in the witness tree τˆT.

In proving Lemma 3.1, we will not need to analyze the interactions between the separate permutations, but rather we will be able to handle each permutation in a completely independent way. For a permutation πk, we deﬁne the witness subdag for permutation πk; this is a relative of the witness tree, but which only includes the information for a single permutation at a time.

- Deﬁnition 3.4 (witness subdags). For a permutation πk, a witness subdag for πk is deﬁned to be a directed acyclic simple graph, whose nodes are labeled with pairs of the form (x,y). If a node v is labeled by (x,y), we write v ≈ (x,y). This graph must in addition satisfy the following properties:

- (1) If any pair of nodes overlaps in a coordinate, that is, we have v ≈ (x,y) ∼ (x ,y ) ≈ v , then nodes v,v must be comparable (that is, either there is a path from v to v or vice-versa).
- (2) Every node of G has in-degree at most two and out-degree at most two.


We also may label the nodes with some auxiliary information, for example we will record that the nodes of a witness subdag correspond to bad-events or nodes in a witness tree τ.

We will use the same terminology as for witness trees: vertices on the “bottom” are close to the source nodes of G (appearing earliest in time), and vertices on the “top” are close to the sink nodes of G (appear latest in time).

The witness subdags that we will be interested in are derived from witness trees in the following manner.

- Deﬁnition 3.5 (Projection of a witness tree). For a witness tree τ, we deﬁne the projection of τ onto


permutation πk which we denote Projk(τ), as follows. Suppose we have a node v ∈ τ which is labeled by some bad-event B = (k1,x1,y1),...,(kr,xr,yr). For

each i with ki = k, we create a corresponding node v i ≈ (xi,yi) in the graph Projk(τ). We also include some auxiliary information indicating that these nodes came from bad event B, and in particular that all such nodes are part of the same bad-event.

The edges of Projk(τ) are formed follows. For each node v ∈ Projk(τ), labeled by (x,y) and corresponding to v ∈ τ, we ﬁnd the node wx ∈ τ (if any) which satisﬁes the following properties:

- (P1) The depth of wx is smaller than the depth of v
- (P2) wx is labeled by some bad-event B which contains (k,x,∗)
- (P3) Among all vertices satisfying (P1), (P2), the depth of wx is maximial


If this node wx ∈ τ exists, then it corresponds to a node w x ∈ Projk(τ) labeled (k,x,∗); we construct an edge from v to w x. Note that, since the levels of the witness tree are independent under ∼, there can be at most one such wx and at most one such w x.

We similary deﬁne a node wy satisfying:

- (P1’) The depth of wy is smaller than the depth of v
- (P2’) wy is labeled by some bad-event B which contains (k,y,∗)
- (P3’) Among all vertices satisfying (P1), (P2), the depth of wy is maximial


If this node exists, we create an edge from v to the corresponding w y ∈ Projk(τ) labeled (k,∗,y).

Note that since edges in Projk(τ) correspond to strictly smaller depth in τ, the graph Projk(τ) is acyclic. Also, note that it is possible that wx = wy; in this case we only add a single edge to Projk(τ).

Expository Remark: In the special case when each bad-event contains a single element, the witness subdag is a “ﬂattening” of the tree structure. Each node in the tree corresponds to a node in the witness subdag, and each node in the witness subdag points to the next highest occurrence of the domain and range variables.

Basically, the projection of τ onto k tells us all of the swaps of πk that occur. It also gives us some of the temporal information about these swaps that would have been available from τ. If there is a path from v to v in Projk(τ), then we know that the swap corresponding to v must come before the swap corresponding to v . It is possible that there are a pair of nodes in Projk(τ) which are incomparable, yet in τ there was enough information to deduce which event came ﬁrst (because the nodes would have been connected through some other permutation). So Projk(τ) does discard some information from τ, but it turns out that we will not need this information.

To prove Lemma 3.1, we will prove (almost) the following claim: Let G be a witness subdag for permutation πk; suppose the nodes of G are labeled with bad-events B1,...,Bs. Then the probability that there is some T > 0 such that G = Projk(ˆτT), is at most

- (1) P(G = Projk(ˆτT) for some T > 0) ≤ Pk(B1)···Pk(Bs)


where, for a bad-event B we deﬁne Pk(B) in a similar manner to PΩ(B); namely that if the bad-event B contains rk elements from permutation k, then we deﬁne Pk(B) = (n

k−rk)!

nk! .

Unfortunately, proving this directly runs into technical complications regarding the order of conditioning. It is simpler to just sidestep these issues. However, the reader should bear in mind (1) as the informal motivation for the analysis in Section 4.

4. The conditions on a permutation πk∗ over time

In Section 4, we will ﬁx a value k∗, and we will describe conditions that πkt∗ must satisfy at various times t during the execution of the Swapping Algorithm. In this section, we are only analyzing a single permutation k∗. To simplify notation, the dependence on k∗ will be hidden henceforth; we will discuss simply π,Proj(τ), and so forth.

This analysis can be divided into three phases.

- (1) We deﬁne the future-subgraph at time t, denoted Gt. This is a kind of graph which encodes necessary conditions on πt, in order for τ to appear, that is, for τˆT = τ for some T > 0. Importantly, these

conditions, and Gt itself, are independent of the precise value of T. We deﬁne and describe some structural properties of these graphs.

- (2) We analyze how a future-subgraph Gt imposes conditions on the corresponding permutation πt, and how these conditions change over time.
- (3) We compute the probability that the swapping satisﬁes these conditions.


We will prove (1) and (2) in Section 4. In Section 5 we will put this together to prove (3) for all the permutations.

- 4.1. The future-subgraph. Suppose we have ﬁxed a target graph G, which could hypothetically have been produced as the projection of τˆT onto k∗. We begin the execution of the Swapping Algorithm and see if, so


far, it is still possible that G = Projk∗(ˆτT), or if G has been disqualiﬁed somehow. Suppose we are at time t of this process; we will show that certain swaps must have already occurred at past times t < t, and certain other swaps must occur at future times t > t.

We deﬁne the future-subgraph of G at time t, denoted Gt, which tells us all the future swaps that must occur.

Deﬁnition 4.1 (The future-subgraph). We deﬁne the future-subgraphs Gt inductively. Initially G0 = G. When we run the Swapping Algorithm, as we encounter a bad-event (k1,x1,y1),...,(kr,xr,yr) at time t, we form Gt+1 from Gt as follows:

- (1) Suppose that ki = k∗, and Gt contains a source node v labeled (xi,yi). Then Gt+1 = Gt − v.
- (2) Suppose that ki = k∗, and Gt has a source labeled (xi,y ) where y = yi or (x ,yi) where x = xi. Then, as will be shown in Proposition 4.2, we can immediately conclude G is impossible; we set Gt+1 = ⊥, and we can abort the execution of the Swapping Algorithm.
- (3) Otherwise, we set Gt+1 = Gt.


- Proposition 4.2. For any time t ≥ 0, let τˆ≥Tt denote the witness tree built for the event at time T, but only


using the execution log from time t onwards. Then if Proj(ˆτT) = G we also have Proj(ˆτ≥Tt) = Gt.

Note that if Gt = ⊥, the latter condition is obviously impossible; in this case, we are asserting that whenever Gt = ⊥, it is impossible to have Proj(ˆτT) = G. Proof. We omit T from the notation, as usual. We prove this by induction on t. When t = 0, this is obviously true as τˆ≥0 = τˆ and G0 = G.

Suppose we have Proj(ˆτ) = G; at time t we encounter a bad-event B = (k1,x1,y1),...,(kr,xr,yr). By inductive hypothesis, Proj(ˆτ≥t) = Gt.

Suppose ﬁrst that τˆ≥t+1 does not contain any bad-events B ∼ B. Then, by our rule for building the witness tree, we have τˆ≥t = τˆ≥t+1. Hence we have Gt = Proj(ˆτ≥t+1). When we project this graph onto permutation k, there cannot be any source node labeled (k,x,y) with (x,y) ∼ (xi,yi) as such node would be labeled with B ∼ B. Hence, according to our rules for updating Gt, we have Gt+1 = Gt. So in this case we have τˆ≥t = τˆ≥t+1 and Gt = Gt+1 and Proj(ˆτ≥t) = Gt; it follows that Proj(ˆτ≥t+1) = Gt+1 as desired.

Next, suppose τˆ≥t+1 does contain B ∼ B. Then bad-event B will be added to τˆ≥t, placed below any such B . When we project τˆ≥t, then for each i with ki = k∗ we add a node (xi,yi) to Proj(ˆτ≥t). Each such node is necessarily a source node; if such a node (xi,yi) had a predecessor (x ,y ) ∼ (xi,yi), then the node (x ,y ) would correspond to an event B ∼ B placed below B. Hence we see that Proj(ˆτ≥t) is obtained from Proj(ˆτ≥t) by adding source nodes (xi,yi) for each (k∗,xi,yi) ∈ B.

So Proj(ˆτ≥t) = Proj(ˆτ≥t+1) plus the addition of source nodes for each (k∗,xi,yi). By inductive hypothesis, Gt = Proj(ˆτ≥t), so that Gt = Proj(ˆτ≥t+1) plus source nodes for each (k∗,xi,yi). Now our rule for updating Gt+1 from Gt is to remove all such source nodes, so it is clear that Gt+1 = Proj(ˆτ≥t+1), as desired.

Note that in this proof, we assumed that Proj(ˆτ) = G, and we never encountered the case in which Gt+1 = ⊥. This conﬁrms our claim that whenever Gt+1 = ⊥ it is impossible to have Proj(ˆτ) = G.

By Proposition 4.2, the witness subdag G and the future-subgraphs Gt have a similar shape; they are all produced by projecting witness trees of (possibly truncated) execution logs. Note that if G = Proj(τ) for some tree τ, then for any bad-event B ∈ τ, either B is not represented in G, or all the pairs of the form (k∗,x,y) ∈ B are represented in G and are incomparable there.

The following structural decomposition of a witness subdag G will be critical.

- Deﬁnition 4.3 (Alternating paths). Given a witness subdag G, we deﬁne an alternating path in G to be a simple path which alternately proceeds forward and backward along the directed edges of G. For a vertex v ∈ G, the forward (respectively backward) path of v in G, is the maximal alternating path which includes v and all the forward (respectively backward) edges emanating from v. Because G has in-degree and out-degree at most two, every vertex v has a unique forward and backward path (up to reﬂection); this justiﬁes our reference to “the” forward and backward path. These paths may be even-length cycles.

Note that if v is a source node, then its backward path contains just v itself. This is an important type of alternating path which should always be taken into account in our deﬁnitions.

One type of alternating path, which is referred to as the W-conﬁguration, plays a particularly important role.

- Deﬁnition 4.4 (The W-conﬁguration). Suppose v ≈ (x,y) has in-degree at most one, and the backward path contains an even number of edges, terminating at vertex v ≈ (x ,y ). We refer to this alternating path


- as a W-conﬁguration. (See Figure 1.) Any W-conﬁguration can be written (in one of its two orientations) as a path of vertices labeled


(x0,y1),(x1,y1),(x1,y2),...,(xs,ys),(xs,ys+1);

here the vertices (x1,y1),...,(xs,ys) are at the “base” of the W-conﬁguration. Note here that we have written the path so that the x-coordinate changes, then the y-coordinate, then x, and so on. When written this way, we refer to (x0,ys+1) as the endpoints of the W-conﬁguration.

If v ≈ (x,y) is a source node, then it deﬁnes a W-conﬁguration with endpoints (x,y). This should not be considered a triviality or degeneracy, rather it will be the most important type of W-conﬁguration.

(x0,y1)

(x4,y5)

(x1,y1)

(x ,y )

Figure 1. The vertices labeled (x0,y1),(x1,y1),...,(x4,y5) form a W-conﬁguration of length 9 with endpoints (x0,y5). Note that the vertex (x ,y ) is not part of this Wconﬁguration.

- 4.2. The conditions on πkt∗ encoded by Gt. At any t, the future-subgraph Gt gives certain necessary conditions on π in order for some putative τ to appear. Proposition 4.5 describes a certain set of conditions that plays a key role in the analysis.


- Proposition 4.5. For any graph G and integers t ≤ T, the following condition is necessary to have G =


Proj(ˆτ≥Tt):

For every W-conﬁguration in Gt with endpoints (x0,ys+1), we must have πt(x0) = ys+1, where πt denotes the value of the permutation at time t.

For example, if v ≈ (x,y) is a source node of Gt, then πt(x) = y.

Proof. We prove this by induction on s. The base case is s = 0; in this case we have a source node (x,y). Suppose πt(x) = y. In order for τˆT to contain some bad-event containing (k∗,x,y), we must at some point t > t have πt (x) = y; let t be the minimal such time. By Proposition 3.2, we must encounter a bad-event containing (k∗,x,∗) or (k∗,∗,y) at some intervening time t < t . If this bad-event contains (k∗,x,y) then necessarily πt (x) = y contradicting minimality of t . So there is a bad-event (k∗,x, = y) or (k∗, = x,y) earlier than the earliest occurrence of π(x) = y. This event (k∗,x, = y) or (k∗, = x,y) projects to a source node (x, = y) or ( = x,y) in Gt. But then (x,y) cannot also be a source node of Gt.

We now prove the induction step. Suppose we have a W-conﬁguration with base (x1,y1),...,(xs,ys), and suppose the endpoints of this W-conﬁguration are vertices v,v labeled (x0,y1 and (xs,ys+1) respectively.

At some future time t ≥ t we must encounter a bad-event B involving some subset of the source nodes, say that B includes (xi

### ) for 1 ≤ r ≤ s. As these were necessarily source nodes, we had πt (xi

### ,yi

### ),...,(xi

### ,yi

1

1

r

r

### ,...,πt (xi

### . After the swaps, these source nodes are removed and so the updated Gt +1 has r + 1 new W-conﬁgurations, whose length is all smaller than s. By inductive hypothesis, the updated permutation πt +1 must then satisfy πt +1(x0) = yi

### ) = yi

### ) = yi

1

1

r

r

### ,πt +1(xi

### ,...,πt +1(xi

### ) = yi

) = ys+1.

1

1

2

r

By Proposition A.2, we may suppose without loss of generality that the resampling of the bad event ﬁrst swaps xi

### in that order. Let π denote the result of these swaps; there may be additional swaps to other elements of the permutation, but we must have πt +1(xi

### ,...,xi

1

r

### ) for l = 1,...,r. In this case, we see that evidently xi

### ) = π (xi

l

l

### , and so on, until eventually xi

### swapped with xi

### , then xi

### swapped with xi

1

2

2

3

### was swapped with x = (πt )−1ys+1. At this point, we have π (x ) = yi

### . Later swaps during time t may swap x with some other x, where (x,y) ∈ B. Thus, at time t +1 we either have πt +1(x ) = yi

r

1

1

### or πt +1(x) = yi

where (x,y) ∈ B. Recall that πt +1(x0) = yi−1; thus either x = x0 or x = x0.

1

In the latter case, (x0,y) ∈ B. Thus implies that, when we encounter the bad-event B at time t , there is a source node labeled (x0,y) ∈ Gt . This node (x0,y) would also be a node in the graph Gt; thus v has two in-neighbors in Gt labeled (x0,y) and (x1,y1), which contradicts that it is part of a W-conﬁguration of Gt.

Thus, we conclude that x = x0. This implies that we must have (πt )−1ys = x = x0; that is, that πt (x0) = ys. This in turn implies that πt(x0) = ys+1. For, by Proposition 3.2, otherwise we would have

encountered a bad-event involving (x0,∗) or (∗,ys+1); these would imply an additional in-neighbor of either v or v respectively, which contradicts that it is part of a W-conﬁguration of Gt.

- Proposition 4.5 can be viewed equally as a deﬁnition:


Deﬁnition 4.6 (Active conditions of a future-subgraph). We refer to the conditions implied by Proposition 4.5 as the active conditions of the graph Gt. More formally, we deﬁne

Active(G) = {(x,y) | (x,y) are the end-points of a W-conﬁguration of G}

We also deﬁne Atk to be the cardinality of Active(Gt), that is, the number of active conditions of permutation πk at time t. (The subscript k may be omitted in context, as usual.)

When we remove source nodes (x1,y1),...,(xr,yr) from Gt, the new active conditions of Gt+1 are related to (x1,y1),...,(xr,yr) in a particular way.

- Lemma 4.7. Suppose G is a future-subgraph with source nodes v1 ≈ (x1,y1),...,vr ≈ (xr,yr). Let H = G − v1 − ··· − vr denote the graph obtained from G by removing these source nodes. Then there is a set Z ⊆ {(x1,y1),...,(xr,yr)} with the following properties:


- (1) There is an injective function f : Z → Active(H), with the property that (x,y) ∼ f((x,y)) for all (x,y) ∈ Z
- (2) |Active(H)| = |Active(G)| − (r − |Z|)


Expository remark: We have recommended bearing in mind the special case when each bad-event consists of a single element. In this case, we would have r = 1; and the stated theorem would be that either |Active(H)| = |Active(G)| − 1; OR we have |Active(H)| = |Active(G)| and (x1,y1) ∼ (x 1,y 1) ∈ Active(H).

Intuitively, we are saying that every node (x,y) we are removing is either explicitly constrained in an “independent way” by some new condition in the graph H (corresponding to Z), or it is almost totally unconstrained. We will never have the bad situation in which a node (x,y) is constrained, but in some implicit way depending on the previous swaps.

Proof. Let Hi denote the graph G − v1 − ··· − vi. We will recursively build up set Zi and functions fi : Zi → Active(H), where Zi ⊆ {(x1,y1),...,(xi,yi)}, and which satisfy the given conditions up to stage i.

Now, suppose we remove the source node vi from Hi−1. Observe that (xi,yi) ∈ Active(Hi−1), but (unless there is some other vertex with the same label in G), (xi,yi)  ∈ Active(Hi). Thus, the most obvious change when we remove vi is that we destroy the active condition (xi,yi). This may add or subtract other active conditions as well.

We will need to update Zi−1,fi−1. Most importantly, fi−1 may have mapped (xj,yj) for j < i, to an active condition of Hi−1 which is destroyed when vi is removed. In this case, we must re-map this to a new active condition. Note that we cannot have fi−1(xj,yj) = (xi,yi) for j < i, as xi = xj and yi = yj.

There are now a variety of cases depending on the forward-path of vi in Hi−1.

- (1) This forward path consists of a cycle, or the forward path terminates on both sides in forwardedges. This is the easiest case. Then no more active conditions of Hi−1 are created or destroyed. We update Zi = Zi−1,fi = fi−1. One active condition is removed, in net, from Hi−1; hence |Active(Hi)| = |Active(Hi−1)| − 1.
- (2) This forward path contains a forward edge on one side and a backward edge on the other. For example, suppose the path has the form (X1,Y1),(X1,Y2),(X2,Y2),...,(Xs,Ys+1), where the vertices (X1,Y1),...,(Xs,Ys) are at the base, and the node (X1,Y1) has out-degree 1, and the node (Xs,Ys+1) has in-degree 1. Suppose that (xi,yi) = (Xj,Yj) for some j ∈ {1,...,s}. (See Figure 2.) In this case, we do not destroy any W-conﬁgurations, but we create a new W-conﬁguration with endpoints (Xj,Ys+1) = (xi,Ys+1).


We now update Zi = Zi−1 ∪ {(xi,yi)}. We deﬁne fi = fi−1 plus we map (xi,yi) to the new active condition (xi,Ys+1). In net, no active conditions were added or removed, and |Active(Hi)| = |Active(Hi−1)|.

(X2,Y3) (X4,Y5)

(X2,Y2)

Figure 2. When we remove (X2,Y2), we create a new W-conﬁguration with endpoints (X2,Y5).

- (3) This forward path was a W-conﬁguration (X0,Y1),(X1,Y1),...,(Xs,Ys),(Xs,Ys+1) with the pairs (X1,Y1),...,(Xs,Ys) on the base, and we had (xi,yi) = (Xj,Yj). This is the most complicated situation; in this case, we destroy the original W-conﬁguration with endpoints (X0,Ys+1) but create two new W-conﬁgurations with endpoints (X0,Yj) and (Xj,Ys+1). We update Zi = Zi−1∪{(xi,yi)}. We will set fi = fi−1, except for a few small changes as follows.


Now, suppose fi−1(xl,yl) = (X0,Ys+1) for some l < i; so either xl = X0 or yl = Ys+1. If it is the former, we set fi(xl,yl) = (X0,Yj),fi(xi,yi) = (Xj,Ys+1). If it is the latter, we set fi(xl,yl) = (Xj,Ys+1),fi(xi,yi) = (X0,Yj).. If (fi−1)−1(X0,Ys+1) = ∅ then we simply set fi(xi,yi) = (X0,Yj).

In any case, fi is updated appropriately, and in the net no active conditions are added or removed, so we have |Active(Hi)| = |Active(Hi−1)|.

5. The probability that the swaps are all successful

In the previous sections, we determined necessary conditions for the permutations πt, depending on the graphs Gt. In this section, we ﬁnish by computing the probability that the swapping subroutine causes the permutations to, in fact, satisfy all such conditions.

- Proposition 5.1 states the key randomness condition satisﬁed by the swapping subroutine. The basic


intuition behind this is as follows: suppose π : [n] → [n] is a ﬁxed permutation with π(x) = y, and we call π = Swap(π;x1,...,xr). Then π (x1) has a uniform distribution over [n]. Similarly, π −1(y1) has a uniform distribution over [n]. However, the joint distribution is not uniform — there is essentially only one degree of freedom for the two values. In general, any subset of the variables π (x1),...,π (xr),π −1(y1),...,π−1(yr) will have the uniform distribution, as long as the subset does not simultaneously contain π (xi),π −1(yi) for some i ∈ [r].

- Proposition 5.1. Suppose n,r,s,q are non-negative integers obeying the following constraints:


- (1) 0 ≤ s ≤ min(q,r)
- (2) q + (r − s) ≤ n


Let π be a ﬁxed permutation of [n], and let x1,...,xr ∈ [n] be distinct, and let yi = π(xi) for i = 1,...,r. Let (x 1,y 1),...,(x q,y q) be a given list with the following properties:

- (3) All x are distinct; all y are distinct
- (4) For i = 1,...,s we have xi = x i or yi = y i.


Let π = Swap(π;x1,...,xr). Then the probability that π satisﬁes all the constraints (x ,y ) is at most

(n − r)!(n − q)! n!(n − q − r + s)!

P(π (x 1) = y 1 ∧ ··· ∧ π (x q) = y q) ≤

Expository remark: Consider the special case when each bad-event contains a single element. In that case, we have r = 1. There are two possibilities for s; either s = 0 in which case this probability on the right is 1 − q/n (i.e. the probability that π (x1) = y 1,...,y q); or s = 1 in which case this probability is 1/n (i.e. the probability that π (x1) = y 1).

Proof. Deﬁne the function g(n,r,s,q) = n(!(n−n−r)!(q−nr−+qs)!)!. We will prove this proposition by induction on s,r. There are a few cases we handle separately:

- (1) Suppose s > 0 and x1 = x 1. Then, in order to satisfy the desired conditions, we must swap x1 to x = π−1(y 1); this occurs with probability 1/n. The subsequent r − 1 swaps starting with the permutation π(x1 x ) must now satisfy the conditions π (x 2) = y 2,...,π (xq) = y q. We claim that we have (xi,π(x1 x )xi) ∼ (x i,y i) for i = 2,...,s. If x = x2,...,xs, this is immediately clear. Otherwise, suppose x = xj. If xj = x j, then we again still have (xj,π(x1 x )xj) ∼ (x j,y j). If yj = y j, then this implies that y 1 = yj = y j, which contradicts that the y j = y 1 .

So we apply the induction hypothesis to π(x1 x ); in the induction, we subtract one from n,q,r,s. This gives

P(π (x 1) = y 1 ∧ ··· ∧ π(x q) = y q) ≤ n1g(n − 1,r − 1,s − 1,q − 1) = g(n,r,s,q) as desired.

- (2) Similarly, suppose s > 0 and suppose y1 = y 1. By Proposition A.3, we would obtain the same distribution if we executed (π )−1 = Swap(π−1;y1,...,yr). Hence we have

P(π (x 1) = y 1 ∧ ··· ∧ π(x q) = y q) = P((π )−1(y 1) = x 1 ∧ ··· ∧ (π )−1(y q) = x q)

Now, the right-hand side has swapped the roles of x1/y1; in particular, it now falls under the previous case (1) already proved, and so the right-hand side is at most g(n,r,s,q) as desired.

- (3) Suppose s = 0 and that there is some i ∈ [r],j ∈ [q] with (xi,yi) ∼ (x j,y j). By Proposition A.2, we

can assume without loss of generality that (x1,y1) ∼ (x 1,y 1). So, in this case, we are really in the case with s = 1. This is covered by case (1) or case (2), which have already shown. Thus, we have that

P(π (x 1) = y 1 ∧ ··· ∧ π(x q) = y q) ≤ g(n,r,1,q) =

g(n,r,0,q)

n − q − r + 1 ≤ g(n,r,s,q) Here, we are using our hypothesis that n ≥ q + (r − s) = q + r.

- (4) Finally, suppose s = 0 and x1,...,xr are distinct from x 1,...,x q and y1,...,yq are distinct from y 1,...,y q. In this case, a necessary (although not suﬃcient) condition to have π (x 1) = y 1,...,π(x q) = y q is that there are some y 1,...,y r , distinct from each other and distinct from y 1,...,y q, with the property that π (xi) = y i for j = 1,...,r. By the union bound, we have


P(π (x 1) = y 1 ∧ ··· ∧ π(x q) = y q) ≤

y 1 ,...,y r

P(π (x1) = y 1 ∧ ··· ∧ π(xr) = y r )

For each individual summand, we apply the induction hypothesis; the summand has probability at most g(n,r,r,q). As there are (n−q)!/(n−q−r)! possible values for y 1,...,y r , the total probability is at most (n − q)!/(n − q − r)! × g(n,r,r,q) = g(n,r,s,q).

We apply Proposition 5.1 to upper-bound the probability that the Swapping Algorithm successfully swaps when it encounters a bad event.

- Proposition 5.2. Suppose we encounter a bad-event B at time t containing elements (k,x1,y1), ..., (k,xr,yr) from permutation k (and perhaps other elements from other permutations). Then the probability


that πkt+1 satisﬁes all the active conditions of its future-subgraph, conditional on all past events and all other swappings at time t, is at most

(nk − Atk+1)! (nk − Atk)!

P(πkt+1 satisﬁes Active(Gtk+1)) ≤ Pk(B)

.

Recall that we have deﬁned Atk to be the number of active conditions in the future-subgraph corresponding to permutation πk at time t, and we have deﬁned Pk(B) = (n

k−r)! nk! .

Expository remark: Consider the special case when each bad-event consists of a single element. In this case, we would have Pk(B) = 1/n. The stated theorem is now: either At+1 = At, in which case the probability that π satisﬁes its swapping condition is 1/n; or At+1 = At −1; in which case the probability that π satisﬁes its swapping condition is 1 − At+1/n.

Proof. Let H denote the future-subgraph Gk,t+1 after removing the source nodes corresponding to the pairs (x1,y1),...,(xr,yr). Using the notation of Lemma 4.7, we set s = |Z| and q = Atk+1. We have Active(H) = {(x 1,y 1),...,(x q,y q)}.

For each (x,y) ∈ Z, we have y = πt(x), and there is an injective function f : Z → Active(H) and (x,y) ∼ f((x,y)). By Proposition A.2, we can assume without loss of generality Z = {(x1,y1),...,(xs,ys)} and f(xi,yi) = (x i,y i). In order to satisfy the active conditions on Gk,t+1, the swapping must cause πt+1(x i) = y i for i = 1,...,q.

By Lemma 4.7, we have Atk = Atk+1 + (r − s) = q + (r − s). Note that Atk ≤ n. So all the conditions of k−r)! nk! × (n

t+1 k )!

(nk−q−r+s)! = (nk−r)!(nk−A

k−q)!

- Proposition 5.1 are satisﬁed. Thus this probability is at most (n


nk!(nk−Atk)! . We have ﬁnally all the pieces necessary to prove Lemma 3.1.

Lemma 3.1. Let τ be a witness tree, with nodes labeled B1,...,Bs. The probability that τ appears is at most

P(τ appears) ≤ PΩ(B1)···PΩ(Bs)

Proof. The Swapping Algorithm, as we have deﬁned it, begins by selecting the permutations uniformly at random. One may also consider ﬁxing the permutations to some arbitrary (not random) value, and allowing the Swapping Algorithm to execute from that point onward. We refer to this as starting at an arbitrary state of the Swapping Algorithm. We will prove the following by induction on τ : The probability, starting

- at an arbitrary state of the Swapping Algorithm, that the subsequent swaps would produce the subtree τ , is at most


N

nk! (nk − |Active(Projk(τ ))|)!

- (2) P(ˆτT = τ for some T ≥ 0) ≤ B∈τ


PΩ(B) ×

.

k=1

When τ = ∅, the RHS of (2) is equal to one so this is vacuously true. To show the induction step, note that in order for τ to be produced as the witness tree for some T ≥ 0, it must be that some B is resampled, where some node v ∈ τ is labeled by B. Suppose we condition on that v is the ﬁrst such node, resampled at time t. A necessary condition to have τˆT = τ for some T ≥ t is that πt+1 satisﬁes all the active conditions on Gt+1. By Proposition 5.2, the probability that πt+1 satisﬁes these conditions is at most k Pk(B)(nk−A

t+1 k )!

(nk−Atk)! .

Next, if this event occurs, then subsequent resamplings must cause τˆ≥Tt+1 = τ − v. To bound the probability of this, we use the induction hypothesis. Note that the induction hypothesis gives a bound conditional on any starting conﬁguration of the Swapping Algorithm, so we may multiply these probabilities. Thus

N

(nk − Atk+1)! (nk − Atk)! ×

nk! (nk − |Active(Projk(τ − v))|)!

P(ˆτT = τ for some T > 0) ≤

PΩ(B) ×

Pk(B)

B∈τ −v

k=1

k

(nk − Atk+1)! (nk − Atk)!

nk! (nk − |Active(Projk(τ − v))|)!

=

### PΩ(B)

B∈τ

k

nk! (nk − Atk)!

as Atk+1 = |Active(Projk(τ − v))| completing the induction argument.

=

### PΩ(B)

B∈τ

k

We now consider the necessary conditions to produce the entire witness tree τ, and not just fragments of it. First, the original permutations πk0 must satisfy the active conditions of the respective witness subdags Projk(τ). For each permutation k, this occurs with probability (nk−A

0 k)!

nk! . Next, the subsequent sampling must be compatible with τ; by (2) this has probability at most B∈τ PΩ(B) × Nk=1

nk!

(nk−A0k)!. Again, note that the bound in (2) is conditional on any starting position of the Swapping Algorithm, hence we may multiply these probabilities. In total we have

P(ˆτT = τ for some T ≥ 0) ≤

k

(nk − A0k)! nk! ×

B∈τ

N

nk! (nk − A0k)!

PΩ(B) ×

=

k=1

### PΩ(B).

B∈τ

We note one counter-intuitive aspect to this proof. The natural way of proving this lemma would be to identify, for each bad-event B ∈ τ, some necessary event occurring with probability at most PΩ(B). This is the general strategy in Moser-Tardos [32] and related constructive LLL variants such as [20], [1], [22]. This is

not the proof we employ here; there is an additional factor of (nk − A0k)!/n! which is present for the original permutation and is gradually “discharged” as active conditions disappear from the future-subgraphs.

6. The constructive LLL for permutations

Now that we have proved the Witness Tree Lemma, the remainder of the analysis is essentially the same as for the Moser-Tardos algorithm [32]. Using arguments and proofs from [32] with our key lemma, we can now easily show our key theorem:

- Theorem 6.1. Suppose there is some assignment of weights µ : B → [0,∞) which satisﬁes, for every B ∈ B the condition


µ(B) ≥ PΩ(B)

(1 + µ(B ))

B ∼B

Then the Swapping Algorithm terminates with probability one. The expected number of iterations in which we resample B is at most µ(B).

In the “symmetric” case, this gives us the well-known LLL criterion:

Corollary 6.2. Suppose each bad-event B ∈ B has probability at most p, and is dependent with at most d bad-events. Then if ep(d + 1) ≤ 1, the Swapping Algorithm terminates with probability one; the expected number of resamplings of each bad-event is O(1).

Some extensions of the LLL, such as the Moser-Tardos distribution bounds shown in [18], the observation of Pegden regarding independent sets in the dependency graph [33], or the partial-resampling of [20], follow almost immediately here. There are a few extensions which require slightly more discussion:

- 6.1. Lopsidependence. As in [32], it is possible to slightly restrict the notion of dependence. Two badevents which share the same valuation of a variable are not forced to be dependent. We can re-deﬁne the relation ∼ on bad-events as follows: for B,B ∈ B, we have B ∼ B iﬀ


- (1) B = B , or
- (2) there is some (k,x,y) ∈ B,(k,x ,y ) ∈ B with either x = x ,y = y or x = x ,y = y .


In particular, bad-events which share the same triple (k,x,y), are not caused to be dependent.

Proving that the Swapping Algorithm still works in this setting requires only a slight change in our deﬁnition of Projk(τ). Now, the tree τ may have multiple copies of any given triple (k,x,y) on a single level. When this occurs, we create the corresponding nodes v ≈ (x,y) ∈ Projk(τ); edges are added between such nodes in an arbitrary (but consistent) way. The remainder of the proof remains as before.

- 6.2. LLL for injective functions. The analysis of [29] considers a slightly more general setting for the LLL, in which we select random injections fk : [mk] → [nk], where mk ≤ nk. In fact, our Swapping Algorithm can be extended to this case. We simply deﬁne a permutation πk on [nk], where the entries πk(mk + 1),...,πk(nk) are “dummies” which do not participate in any bad-events. The LLL criterion for the extended permutation πk is exactly the same as the corresponding LLL criterion for the injection fk. Because all of the dummy entries have the same behavior, it is not necessary for the Swapping Algorithm to keep track of the dummy entries exactly; they are needed only for the analysis.


6.3. Comparison with the approaches of Achlioptas & Iliopoulos and Harvey & Vondra´k. Achlioptas & Iliopoulos [1] and Harvey & Vondr´k [22] gave generic frameworks for analyzing variants of the Moser-Tardos algorithm, applicable to diﬀerent types of combinatorial conﬁgurations. These frameworks can include vertex-colorings, permutations, Hamiltonian cycles of graphs, spanning trees, matchings, and other settings. For the case of permutations, both of these frameworks give a version of the Swapping Algorithm and show that it terminates under the same conditions as we do, which in turn are the same conditions as the LLL (Theorem 1.1).

The key diﬀerence between our approach and [1, 22] is that they enumerate the entire history of all resamplings to the permutations. In contrast, our proof is based on the Witness Tree Lemma; this is a much more succinct structure that ignores most of the resamplings, and only enumerates the few resamplings that

are necessary to justify a single item in the execution log. Their proofs are much simpler than ours; a major part of the complexity of our proof lies in the need to argue that the bad-events which were ignored by the witness tree do not aﬀect the probabilities. (The ignored bad-events do interact with the variables we need to track for the witness tree, but do so in a “neutral” way.)

If our only goal is to prove that the Swapping Algorithm terminates in polynomial time, then the other two frameworks give a better and simpler approach. However, the Witness Tree Lemma allows much more precise estimates for many types of events. The main reason for this precision is the following: suppose we want to show that some event E has a low probability of occurring during or after the execution of the Swapping Algorithm. The proof strategy of Moser & Tardos is to take a union-bound over all witness trees that correspond to this event. In this case, we are able to show a probability bound which is proportional to the total weight of all such witness trees. This can be a relatively small number as only the witness trees connected to E are relevant. Our analysis, which is also based on witness trees, is able to show similar types of bounds.

However, the analysis of Achlioptas & Iliopoulos and Harvey & Vondr´k is not based on witness trees, but the much larger set of full execution logs. The number of possible execution logs can be exponentially larger than the number of witness trees. It is very ineﬃcient to take a union bound over all such logs. Hence, Achlioptas & Iliopoulos and Harvey & Vondr´k give bounds which are exponentially weaker (in a certain technical sense) than the ones we provide.

Many properties of the Swapping Algorithm depend on the ﬁne degree of control provided by the Witness Tree Lemma, and it seems diﬃcult to obtain them from the alternate LLLL approaches. We list a few of these properties here.

The LLL criterion without slack. As a simple example of the problems caused by taking a union bound over execution logs, suppose that we satisfy the LLL criterion without slack, say epd = 1; here, as usual, p and d are bounds respectively on the probability of any bad event and the degree of any bad event in the dependency graph. In this case, we show that the expected time for our Swapping Algorithm to terminate is O(m). In contrast, in Achlioptas & Iliopoulous or Harvey & Vondr´k, they require satisfying the LLL criterion with slack ep(1 + )d = 1, and achieve a termination time of O(m/ ). They require this slack term in order to damp the exponential growth in the number of execution logs. (Harvey & Vondr´k show that if the symmetric LLL criterion is satisﬁed without slack, then the Shearer criterion [35] is satisﬁed with slack = O(1/m). Thus, they would achieve a running time of O(m2) without slack.)

Arbitrary choice of which bad-event to resample. The Swapping Algorithm as we have stated it is actually under-determined, in that the choice of which bad-event to resample is arbitrary. In contrast, in both Achlioptas & Iliopoulos and Harvey & Vondr´k, there is a ﬁxed priority on the bad-events. (The work of [27] has shown that this restriction can be removed in certain special cases of the Achlioptas & Iliopoulous setting, including for random permutations and matchings.) This freedom can be quite useful. For example, in Section 7 we consider a parallel implementation of our Swapping Algorithm. We will select which bad-events to resample in a quite complicated and randomized way. However, the correctness of the parallel algorithm will follow from the fact that it simulates some serial implementation of the Swapping Algorithm.

The Moser-Tardos distribution. The Witness Tree Lemma allows us to analyze the so-called “MoserTardos (MT) distribution,” ﬁrst discussed by [18]. The LLL and its algorithms ensure that bad-events

- B cannot possibly occur. In other words, we know that the conﬁguration produced by the LLL has the property that no B ∈ B is true. In many applications of the LLL, we may wish to know more about such conﬁgurations, other than they exist.


There are a variety of reasons we might want this; we give two examples for the ordinary, variablebased LLL. Suppose that we have some weights for the values of our variables, and we deﬁne the objective function on a solution i w(Xi); in this case, if we are able to estimate the probability that a variable Xi takes on value j in the output of the LLL (or Moser-Tardos algorithm), then we may be able to show that conﬁgurations with a good objective function exist. A second example is when the number of bad-events becomes too large, perhaps exponentially large. In this case, the Moser-Tardos algorithm cannot test them all. However, we may still be able to ignore a subset of the bad events, and argue that the probability that they are true at the end of the Moser-Tardos algorithm is small even though they were never checked.

The Witness Tree Lemma gives us an extremely powerful result concerning this MT distribution, which carries over to the Swapping Algorithm.

## Proposition 6.3. Let E ≡ πk

(x1) = y1 ∧ ··· ∧ πk

(xr) = yr. Then the probability that E is true in the output of the Swapping Algorithm, is at most PΩ(E) B ∼E(1 + µ(B )). Proof. See [18] for the proof of this for the ordinary MT algorithm; the extension to the Swapping Algorithm is straightforward.

1

r

Bounds on the depth of the resampling process. One key requirement for parallel variants of the Moser-Tardos algorithm appears to be that the resampling process has logarithmic depth. This is equivalent to showing that there are no deep witness trees. This follows easily from the Witness Tree Lemma, along the same lines as in the original paper of Moser & Tardos, but appears to be very diﬃcult in the other LLLL frameworks.

Partial resampling. In [20], a partial resampling variant of the Moser-Tardos algorithm was developed. In this variant, one only resamples a small, random subset of the variables (or, in our case, permutation elements) which determine a bad-event. To analyze this variant, [20] developed an alternate type of witness tree, which only records the variables which were actually resampled. Ignoring the other variables can drastically prunes the space of witness trees. Again, this does not seem to be possible in other LLLL frameworks in which the full execution log must be recorded. We will see an example of this in Theorem 8.2; we do not know of any way to show results such as Theorem 8.2 using the frameworks of either Achlioptas & Iliopoulos or Harvey & Vondr´k.

7. A parallel version of the Swapping Algorithm

The Moser-Tardos resampling algorithm for the ordinary LLL can be transformed into an RNC algorithm by allowing a slight slack in the LLL’s suﬃcient condition [32]. The basic idea is that in every round, we select a maximal independent set of bad-events to resample. Using the known distributed/parallel algorithms for MIS, this can be done in RNC; the number of resampling rounds is then shown to be logarithmic whp (“with high probability”), in [32].

In this section, we will describe a parallel algorithm for the Swapping Algorithm, which runs along the same lines. However, everything is more complicated than in the case of the ordinary LLL. In the MoserTardos algorithm, events which are not connected to each other cannot aﬀect each other in any way. For the permutation LLL, such events can interfere with each other, but do so rarely. Consider the following example. Suppose that at some point we have two active bad-events, “πk(1) = 1” and “πk(2) = 2” respectively, and so we decide to resample them simultaneously (since they are not connected to each other, and hence constitute an independent set). When we are resampling the bad-event πk(1) = 1, we may swap 1 with 2; in this case, we are automatically ﬁxing the second bad-event as well. The sequential algorithm, in this case, would only swap a single element. The parallel algorithm should likewise not perform a second swap for the second bad-event, or else it would be over-sampling. Avoiding this type of conﬂict is quite tricky.

Let n = n1+···+nK; since the output of the algorithm will be the contents of the permutations π1,...,πk, this algorithm should be measured in terms of n, and we must show that this algorithm runs in logO(1) n time. We will make the following assumptions in this section. First, we assume that |B|, the total number of potential bad-events, is polynomial in n. This assumption can be relaxed if we have the proper kind of “separation oracle” for B. Next, we assume that every element B ∈ B has size |B| ≤ M = logO(1) n; this holds in many cases.

We describe the following Parallel Swapping Algorithm:

- (1) In parallel, generate the permutations π1,...,πN uniformly at random.
- (2) We proceed through a series of rounds while there is some true bad-event. In round i (i = 1,2,...,) do the following:


(3) Let Vi,1 ⊆ B denote the set of bad-events which are currently true at the beginning of round i. We will attempt to ﬁx the bad-events in Vi,1 through a series of sub-rounds. This may introduce new bad-events, but we will not ﬁx any newly created bad-events until round i + 1. We repeat the following for j = 1,2,... as long as Vi,j = ∅:

- (4) Let Ii,j be a maximal independent set (MIS) of bad-events in Vi,j.
- (5) For each true bad-event B ∈ Ii,j, choose the swaps corresponding to B. Namely, if we have some bad-event B involving triples (k1,x1,y1),...,(kr,xr,yr), then we select each


zl ∈ [nk

], which is the element to be swapped with πk

(xl) according to procedure Swap.

l

l

Do not perform the indicated swaps at this time though! We refer to (k1,x1),...,(kr,xr) as the swap-sources of B and the (k1,z1), ..., (kr,zr) as the swap-mates of B.

- (6) Select a random ordering ρi,j of the elements of Ii,j. Consider the graph Gi,j whose vertices correspond to elements of Ii,j: add an edge connecting B with B if ρi,j(B) < ρi,j(B ) and one of the swap-mates of B is a swap-source of B . Generate I i,j ⊆ Ii,j as the lexicographically-ﬁrst MIS (LFMIS) of the resulting graph Gi,j, with respect to the vertex-ordering ρi,j.
- (7) For each permutation πk, enumerate all the transpositions (x z) corresponding to elements of I i,j, arranged in order of ρi,j. Say these transpositions are, in order (x1,z1),...(xl,zl), where l ≤ n. Compute, in parallel for all πk, the composition π k = πk(xl zl)...(x1 z1).
- (8) Update Vi,j+1 from Vi,j by removing all elements which are either no longer true for the current permutation, or are connected via ∼ to some element of I i,j.


Most of the steps of this algorithm can be implemented using standard parallel algorithms. For example, step (1) can be performed simply by having each element of [nk] choose a random real and then executing a parallel sort. The independent set Ii,j can be found in time in polylogarithmic time using [6, 30].

The diﬃcult step to parallelize is in selecting the LFMIS I i,j. In general, the problem of ﬁnding the LFMIS is P-complete [11], hence we do not expect a generic parallel algorithm for this. However, what saves us it that the ordering ρi,j and the graph Gi,j are constructed in a highly random fashion.

This allows us to use the following greedy algorithm to construct I i,j, the LFMIS of Gi,j:

(1) Let H1 be the directed graph obtained by orienting all edges of Gi,j in the direction of ρi,j. Repeat the following for s = 1,2,...,:

- (2) If Hs = ∅ terminate.
- (3) Find all source nodes of Hs. Add these to I i,j.
- (4) Construct H s+1 by removing all source nodes and all successors of source nodes from H s.


The output of this algorithm is the LFMIS I i,j. Each step can be implemented in parallel time O(1). The number of iterations of this algorithm is the length of the longest directed path in G i,j. So it suﬃces it show that, whp, all directed paths in G i,j have length at most polylogarithmic in n.

- Proposition 7.1. Let I ⊆ B be an an arbitrary independent set of true bad-events, and suppose all elements


of B have size ≤ M. Let G = Gi,j be the graph constructed in Step (6) of the Parallel Swapping Algorithm. Then whp, every directed path in G has length O(M + log n).

Proof. One of the main ideas below is to show that for the typical B1,...,Bl ∈ I, where l = 5(M + log n), the probability that B1,...,Bl form a directed path is small. Suppose we select B1,...,Bl ∈ I uniformly at random without replacement. Let us analyze how these could form a directed path in G. (We may assume |I| > l or otherwise the result holds trivially.)

First, it must be the case that ρ(B1) < ρ(B2) < ··· < ρ(Bl). This occurs with probability 1/l!. Next, it must be that the swap-mates of Bs overlap the swap-sources of Bs+1, for s = 1,...,l − 1. Now, Bs has O(M) swap-mates; each such swap-mate can overlap with at most one element of I, since I is an independent set. Conditional on having chosen B1,...,Bs, there are a remaining |I| − s choices for Bs+1. This gives that the probability of having Bs with an edge to Bs+1, conditional on the previous events, is at most |IM|−s. (The fact that swap-mates are chosen randomly does not give too much of an advantage here.)

Putting this all together, the total probability that there is a directed path on B1,...,Bl is P(directed path B1,...,Bl) ≤

Ml−1(|I| − l)! (|I| − 1)!l!

Since the above was for a random B1,...,Bl, the probability that there is some such path (of length l) is at most

Ml−1(|I| − l)! (|I| − 1)!l!

|I|! (|I| − l)! ×

P(some directed path) ≤

Ml−1 (l/e)l ≤ n−Ω(1),

Ml−1 l! ≤ n ×

= |I| ×

since l = 5(M + log n).

So far, we have shown that each sub-round of the Parallel Swapping Algorithm can be executed in parallel time logO(1) n. Next, we show that whp that number of sub-rounds corresponding to any round is bounded by logO(1) n.

- Proposition 7.2. Suppose |B| = nO(1) and all elements B ∈ B have size |B| ≤ M. Then whp, we have Vi,j = ∅ for some j = O(M log2 n). Proof. We will ﬁrst show the following: Let B ∈ I, where I is an arbitrary independent set of B. Then with


probability at least 1 − 2M1lnn we have B ∈ I as well, where I is the LFMIS associated with I.

Observe that if there is no B ∈ I such that ρ(B ) < ρ(B) and such that a swap-mate of B overlaps with a swap-source of B, then B ∈ I (this is not a necessary condition). We will analyze the ordering ρ using the standard trick, in which each element B ∈ I chooses a rank W(B) ∼ Uniform[0,1], independently and identically. The ordering ρ is then formed by sorting in increasing ordering of W. In this way, we are able to avoid the dependencies induced by the rankings. For the moment, let us suppose that the rank W(B) is ﬁxed at some real value w. We will then count how many B ∈ I satisfy W(B ) < w and a swap-mate of B

overlaps a swap-source of B.

So, let us consider some swap-source s of B in permutation k, and consider some B j ∈ I which has r j other elements in permutation k. For l = 1,...,r j, there are nk −l+1 possible choices for the lth swap-mate from B j, and hence the total expected number of swap-mates of B which overlap s is at most

r j

1 nk − l + 1

E[ # swap-mates of B j overlapping s] ≤

l=1

r j+1

1 nk − l + 1

≤

dl

l=1

nk nk − r j

= ln(

)

Next, sum over all B j ∈ I. Observe that since I is an independent set, we must have r j ≤ nk − 1. Thus,

nk nk − r j

E[ # swap-mates of some B j overlapping s] ≤

ln(

)

j

nk nk − j r j

≤ ln(

) by concavity ≤ lnnk ≤ lnn

Thus, summing over all swap-sources of B, the total probability that there is some B with ρ(B ) ≤ B and for which a swap-mate overlaps a swap-source of B, is at most w|B|lnn ≤ wM lnn. By Markov’s inequality, we have

P(B ∈ I | W(B) = w) ≥ 1 − wM lnn Integrating over w, we have that B ∈ I with probability at least

1 2M lnn

P(B ∈ I ) ≥ 1 −

Now, using this fact, we show that Vi,j is decreasing quickly in size. For, suppose B ∈ Vi,j. So B ∼ B

for some B ∈ Ii,j, as Ii,j is a maximal independent set (possibly B = B ). We will remove B from Vi,j+1 if B ∈ I i,j, which occurs with probability at least 1 − 2M1lnn. As B was an arbitrary element of Vi,j, this shows that E |Vi,j+1| | Vi,j ≤ (1 − 2M1lnn)|Vi,j|.

For j = Ω(M log2 n), this implies that

1 2M lnn

2 n)|Vi,1| ≤ n−Ω(1) This in turn implies that Vi,j = ∅ with high probability, for j = Ω(M log2 n).

)Ω(M log

E |Vi,j| ≤ (1 −

To ﬁnish the proof, we must show that the number of rounds is itself bounded whp. We begin by showing that Witness Tree Lemma remains valid in the parallel setting.

- Proposition 7.3. When we execute this parallel swapping algorithm, we may generate an “execution log” according to the following rule: suppose that we resample B in round i,j and B in round i ,j . Then we place B before B iﬀ:

- (1) i < i ; OR
- (2) i = i AND j < j ; OR
- (3) i = i and j = j and ρi,j(B) < ρi ,j (B )


that is, we order the resampled bad-events lexicographically by round, sub-round, and then rank ρ.

Given such an execution log, we may also generate witness trees in the same manner as the sequential algorithm.

Now let τ be any witness tree; we have P(τ appears) ≤

B∈τ

PΩ(B)

Proof. Observe that the choice of swaps for a bad-event B at round i, subround j, and rank ρi,j(B), is only aﬀected by the events in earlier rounds / subrounds as well as other B ∈ Ii,j with ρi,j(B ) < ρi,j(B).

Thus, we can view this parallel algorithm as simulating the sequential algorithm, with a particular rule for selecting the bad-event to resample. Namely, we keep track of the sets Vi and Ii,j as we do for the parallel algorithm, and within each sub-round we resample the bad-event in Ii,j with the minimum value of ρi,j(B).

This is why it is critical in step (6) that we select I i,j to be the lexicographically-ﬁrst MIS; this means that the presence of B ∈ I i,j cannot be aﬀected with B with ρ(B ) > ρ(B).

- Proposition 7.4. Let B be any resampling performed at the ith round of the Parallel Swapping Algorithm

(that is, B ∈ I i,j for some integer j > 0) Then the witness tree corresponding to the resampling of B has height exactly i.

Proof. First, note that if we have B ∼ B in the execution log, where B occurs earlier in time, and the witness tree corresponding to B has height i, then the witness tree corresponding to B must have height i + 1. So it will suﬃce to show that if B ∈ I i,j, then we must have B ∼ B for some B ∈ I i−1,j .

At the beginning of round i, it must be the case that πi makes the bad-event B true. By Proposition 3.2, either the bad-event B was already true at the beginning of round i − 1, or some bad-event B ∼ B was resampled at round i − 1. If it is the latter, we are done.

So suppose B was true at the beginning of round i − 1. So B was an element of Vi−1,1. In order for B to have been removed from Vi−1, then either we had B ∼ B ∈ I i−1,j , in which case we are also done, or after some sub-round j the event B was no longer true. But again by Proposition 3.2, in order for B to become true again at the beginning of round i, there must have been some bad-event B ∼ B encountered later in round i − 1.

This gives us the key bound on the running time of the Parallel Swapping Algorithm. We give only a sketch of the proof, since the argument is identical to that of [32].

- Proposition 7.5. Suppose that > 0 and that there is some assignment of weights µ : B → [0,∞) which satisﬁes, for every B ∈ B, the condition


µ(B) ≥ (1 + )PΩ(B)

(1 + µ(B ))

B ∼B

O(1)(n B µ(B)) rounds.

Then, whp, the Parallel Swapping Algorithm terminates after log

Proof. Consider the event that for some B ∈ B, that B is resampled after i rounds of the Parallel Swapping Algorithm. In this case, τˆ has height i. As shown in [32], the sum, over all witness trees of some height h, of the product of the probabilities of the constituent events in the witness trees, is decreasing exponentially in h. So, for any ﬁxed B, the probability that this occurs is exponentially small; this remains true after taking a union-bound over the polynomial number of B ∈ B.

We can put this analysis all together to show:

- Theorem 7.6. Suppose |B| = nO(1) and that for all B ∈ B we have |B| ≤ logO(1) n. Suppose also that > 0 and that there is some assignment of weights µ : B → [0,∞) which satisﬁes, for every B ∈ B, the condition

µ(B) ≥ (1 + )PΩ(B)

B ∼B

(1 + µ(B ))

Then, whp, the Parallel Swapping Algorithm terminates after log

O(1)(n B µ(B)) time.

Proof. The number of rounds, the number of sub-rounds per round, and the running time of each sub-round, are all polylogarithmic in n whp.

8. Algorithmic Applications

The LLL for permutations plays a role in diverse combinatorial constructions. Using our algorithm, nearly all of these constructions become algorithmic. We examine a few selected applications now.

- 8.1. Latin transversals. Suppose we have an n × n matrix A. The entries of this matrix come from a set


- C which are referred to as colors. A Latin transversal of this matrix is a permutation π ∈ Sn, such that no color appears twice among the entries A(i,π(i)); that is, there are no i = j with A(i,π(i)) = A(i ,π(i )). A typical question in this area is the following: suppose each color c appears at most ∆ times in the matrix. How large can ∆ be so as to guarantee the existence of a Latin transversal?


In [14], a proof using the probabilistic form of the Lov´sz Local Lemma for permutations was given, showing that ∆ ≤ n/(4e) suﬃces. This was the ﬁrst application of the LLL to permutations. This bound was subsequently improved by [9] to the criterion ∆ ≤ (27/256)n; this uses a variant of the probabilistic Local Lemma which is essentially equivalent to Pegden’s variant on the constructive Local Lemma. Using our algorithmic LLL, we can almost immediately transform the existential proof of [9] into a constructive algorithm. To our knowledge, this is the ﬁrst polynomial-time algorithm for constructing such a transversal.

- Theorem 8.1. Suppose ∆ ≤ (27/256)n. Then there is a Latin transversal of the matrix. Furthermore, the Swapping Algorithm selects such a transversal in polynomial time.

Proof. For any quadruples i,j,i ,j with A(i,j) = A(i ,j ), we have a bad-event (i,j),(i ,j ). Such an event has probability n(n1−1). We give weight µ(B) = α to every bad event B, where α is a scalar to be determined.

This bad-event can have up to four types of neighbors (i1,j1,i 1,j 1), which overlap on one of the four coordinates i,j,i ,j ; as discussed in [9], all the neighbors of any type are themselves neighbors in the dependency graph. Since these are all the same, we will analyze just the ﬁrst type of neighbor, one which shares the same value of i, that is i1 = i. We now may choose any value for j1 (n choices). At this point, the color A(i1,j1) is determined, so there are ∆ − 1 remaining choices for i 1,j 1.

By Lemma 3.1 and Pegden’s criterion [33], a suﬃcient condition for the convergence of the Swapping Algorithm is that

α ≥

1 n(n − 1)

(1 + n(∆ − 1)α)4 Routine algebra shows that this has a positive real root α when ∆ ≤ (27/256)n.

In [38], Szab´ considered a generalization of this question: suppose that we seek a transversal, such that no color appears more than s times. When s = 1, this is asking for a Latin transversal. Szab´ gave similar criteria “∆ ≤ γsn” for s a small constant. Such bounds can be easily obtained constructively using the permutation LLL as well.

By combining the permutation LLL with the partial resampling approach of [20], we can provide asymptotically optimal bounds for large s:

- Theorem 8.2. Suppose ∆ ≤ (s−c√s)n, where c is a suﬃciently large constant. Then there is a transversal of the matrix in which each color appears no more than s times. This transversal can be constructed in polynomial time. Proof. For each set of s appearances of any color, we have a bad event. We use the partial resampling


framework, to associate the fractional hitting set which assigns weight r s −1 to any r appearances of a color, where r = √s .

We ﬁrst compute the probability of selecting a given r-set X. From the fractional hitting set, this has probability r s −1. In addition, the probability of selecting the indicated cells is (n−n!r)!. So we have p ≤ r s −1(n−n!r)!.

Next, we compute the dependency of the set X. First, we may select another X which overlaps with X

in a row or column; the number of such sets is 2rn r ∆−1 . Next, we may select any other r-set with the same color as X (this is the dependency due to in the partial resampling framework; see [20] for more details).

The number of such sets is ∆r . So the LLL criterion is satisﬁed if

−1(n − r)! n! × 2rn

s r

∆ r − 1

∆ r ≤ 1

e ×

+

Simple calculus now shows that this can be satisﬁed when ∆ ≤ (s − O(√s))n. Also, it is easy to detect a true bad-event and resample it in polynomial time, so this gives a polynomial-time algorithm.

Our result depends on the Swapping Algorithm in a fundamental way — it does not follow from Theorem 1.1 (which would roughly require ∆ ≤ (s/e)n). Hence, prior to this paper, we would not have been able to even show the existence of such transversals; here we provide an eﬃcient algorithm as well. To see that our bound is asymptotically optimal, consider a matrix in which the ﬁrst s+1 rows all contain a given color,

- a total multiplicity of ∆ = (s + 1)n. Then the transversal must contain that color at least s + 1 times.


## 8.2. Rainbow Hamiltonian cycles and related structures. The problem of ﬁnding Hamiltonian cycles

in the complete graph Kn, with edges of distinct colors, was ﬁrst studied in [19]. This problem is typically phrased in the language of graphs and edges, but we can rephrase it in the language of Latin transversals, with the additional property that the permutation π has full cycle. How often can a color appear in the matrix A, for this to be possible? In [2], it was shown that such a transversal exists if each color appears at most ∆ = n/32 times.1 This proof is based on applying the non-constructive Lova´sz Local Lemma to the probability space induced by a random choice of full-cycle permutation. This result was later generalized in [17], to show the following result: if each color appears at most ∆ ≤ c0n times for a certain constant c0 > 0, then not only is there a full-cycle Latin transversal, but there are also cycles of each length 3 ≤ k ≤ n. The constant c0 was somewhat small, and this result was also non-constructive. Theorem 8.3 uses the Swapping Algorithm to construct Latin transversals with essentially arbitrary cycle structures; this generalizes [17] and [2] quite a bit.

- Theorem 8.3. Suppose that each color appears at most ∆ ≤ 0.027n times in the matrix A, and n is suﬃciently large. Let τ be any permutation on n letters, whose cycle structure contains no ﬁxed points nor swaps (2-cycles). Then there is a Latin transversal π which is conjugate to τ (i.e., has the same cycle structure); furthermore the Swapping Algorithm ﬁnds it in polynomial time. Also, the Parallel Swapping Algorithm ﬁnds it in time logO(1) n.


Proof. We cannot apply the Swapping Algorithm directly to the permutation π, because we will not be able to control its cycle structure. Rather, we will set π = σ−1τσ, and apply the Swapping Algorithm to σ.

A bad-event is that A(x,π(x)) = A(x ,π(x )) for some x = x . Using the fact that τ has no ﬁxed points or 2-cycles, we can see that this is equivalent to one of the following two situations: (A) There are i,i ,x,y,x ,y such that σ(x) = i,σ(y) = τ(i),σ(x ) = i ,σ(y ) = τ(i ), and x,y,x ,y are distinct, and i,i ,τ(i),τ(i ) are distinct, and A(x,y) = A(x ,y ) or (B) There are i,x,y,z with σ(x) = i,σ(y) = τ(i),σ(z) = τ2(i), and all of x,y,z are distinct, and A(x,y) = A(y,z). We will refer to the ﬁrst type of bad-event as an event of type A led by i (such an event is also led by i ); we will refer to the second type of bad-event as type B led by i.

Note that in an A-event, the color is repeated in distinct column and rows, and in a B-event the column of one coordinate is the row of another. So, to an extent, these events are mutually exclusive. Much of the complexity of the proof lies in balancing the two conﬁgurations. To a ﬁrst approximation, the worst case occurs when A-events are maximized and B-events are impossible. This intuition should be kept in mind during the following proof.

1The terminology used for rainbow Hamilton cycles is slightly diﬀerent from that of Latin transversals. In the context of Hamilton cycles, one often assumes that the matrix A is symmetric. Furthermore, since A(x, y) and A(y, x) always have the same color, one only counts this as a single occurrence of that color. Thus, for example, in [2], the stated criterion is that the matrix A is symmetric and a color appears at most ∆/64 times.

We will deﬁne the function µ as follows. Each event of type A is assigned the same weight µA, and each event of type B is assigned weight µB. The event of type A has probability (n − 4)!/n! and each event of type B has probability (n − 3)!/n!. In the following proof, we shall need to compare the relative magnitude of µA,µB. In order to make this concrete, we set

µA = 2.83036n−4,µB = 1.96163n−3

(In deriving this proof, we left these constant coeﬃcients undetermined until the end of the computation, and we then veriﬁed that all desired inequalities held.)

Now, to apply Pegden’s criterion [33] for the convergence of the Swapping Algorithm, we will need to analyze the independent sets of neighbors each bad-event can have in the dependency graph. In order to keep track of this neighborhood structure, it will be convenient to deﬁne the following sums. We let t denote the sum of µ(X) over all bad-events X involving some ﬁxed term σ(x). Let s denote the sum of µ(X) over all bad-events X (of type either A or B) led by some ﬁxed value i, and let b denote the sum of µ(X) over B-events X alone. Recall that each bad-event of type A is led by i and also by i .

We now examine how to compute the term t. Consider a ﬁxed value x; we will enumerate all the badevents that involve σ(x). These correspond to color-repetitions involving either row or column x in the matrix A. Let ci (respectively ri) denote the number of occurrences of color i in column (respectively row) x of the matrix, excluding A(x,y) itself.

We can have a color repetition of the form A(y,x) = A(x,y ) where y = y ; or we can have repetitions of the form A(x,y) = A(x ,y ) or A(y,x) = A(y ,x ), where x = x ,y = y (but possibly x = y). The total number of repetitions of the ﬁrst type is v1 ≤ i ciri. The total number of repetitions of the second type is at most v2 ≤ i ci(∆ − ci − ri). The total number of repetitions of the third type is at most v3 ≤ i ri(∆ − ci − ri).

For a repetition of the ﬁrst type, this must correspond to an B-event, in which σ(y) = i,σ(x) = τ(i),σ(y ) = τ2(i) for some i. For a repetition of the second type, if x = y this correspond to an Aevent in which σ(x) = i,σ(y) = τ(i),σ(x ) = i ,σ(y ) = τ(i ) for some i,i or alternatively if x = y it correspond to a B-event in which σ(x) = i,σ(y) = τ(i),σ(y ) = τ2(i) for some i. A similar argument holds for the third type of repetition.

Summing all these cases, we have

t ≤ v1nµB + v2(max(n2µA + nµB)) + v3(max(n3µA + nµB)) ≤ v1nµB + v2n2µA + v3n2µA ≤

(cjrjnµB + cj(∆ − cj − rj)n2µA + rj(∆ − cj − rj)n2µA)

j

Observe that the the RHS is maximized when there are n distinct colors with cj = 1 and n distinct colors with rj = 1. For, suppose that a color has (say) cj > 1. If we decrement cj by 1 while adding a new color with cj = 1, this changes the RHS by (−1 + 2(cj + rj) − ∆)n2µA + (−1 + ∆ − rj)nµB ≥ 0.

This gives us

t ≤ 2n3∆µA

Similarly, let us consider s. Given i, we choose some y with σ(y) = τ(i). Now, we again list all color repetitions A(x,y) = A(x ,y ) or A(x,y) = A(y,z). The number of the former is at most j cj(∆ − cj − rj) and the number of the latter is at most j cjrj. As before, this is maximized when each color appears once in the column, leading to

s ≤ n3∆µA For term b, the worst case is when each color appears ∆/2 times in the row and column of y; this yields

b ≤ n2(∆/2)µB

Now consider a ﬁxed bad-event A, with parameters i,i ,x,y,x ,y , and let us count the sum over all independent sets of neighbors, of µ. This could have one or zero children involving σ(x) and similarly for σ(y),σ(x ),σ(y ); this gives a total contribution of (1 + t)4. The children could also overlap on i; the total set of possibilities is either zero children, a B-child led by i − 2, a B-child led by i − 2 and a child led by i, a child led by i − 1, a child led by i − 1 and a child led by i + 1, a child led by i, a child led by i + 1. There is

an identical factor for the contributions of bad-events led by i − 2,...,i + 1. In total, the criterion for A is that we must have

(n − 4)! n!

(1 + t)4(1 + b + sb + s + s2 + s + s)2 Applying the same type of analysis to an event of type B gives us the criterion:

µA ≥

(n − 3)! n!

(1 + t)3(1 + b + sb + sb + s + s2 + s2 + s + s2 + s)

µB ≥

Putting all these constraints together gives a complicated system of polynomial equations, which can be solved using a symbolic algebra package. Indeed, the stated values of µA,µB satisfy these conditions when ∆ ≤ 0.027n and n is suﬃciently large.

Hence the Swapping Algorithm terminates, resulting in the desired permutation π = σ−1τσ. It is easy to see that the Parallel Swapping Algorithm works as well.

We note that for certain cycle structures, namely the full cycle σ = (123...n−1 n) and n/2 transpositions σ = (12)(34)...(n − 1 n), one can apply the LLLL directly to the permutation π. This gives a qualitatively similar condition, of the form ∆ ≤ cn, but the constant term is slightly better than ours. For some of these settings, one can also apply a variant of the Moser-Tardos algorithm to ﬁnd such permutations [1]. However, these results do not apply to general cycle structures, and they do not give parallel algorithms.

- 8.3. Strong chromatic number of graphs. Suppose we have a graph G, with a given partition of the


vertices into k blocks each of size b, i.e., V = V1 ··· Vk. We would like to b-color the vertices, such that every block has exactly b colors, and such that no edge has both endpoints with the same color (i.e., it is a proper vertex-coloring). This is referred to as a strong coloring of the graph. If this is possible for any such partition of the vertices into blocks of size b, then we say that the graph G has strong chromatic number b.

A series of papers [5, 8, 16, 23] have provided bounds on the strong chromatic number of graphs, typically in terms of their maximum degree ∆. In [24], it is shown that when b ≥ (11/4)∆ + Ω(1), such a coloring exists; this is the best bound currently known. Furthermore, the constant 11/4 cannot be improved to any number strictly less than 2. The methods used in most of these papers are highly non-constructive, and do not provide algorithms for generating such colorings.

In this section, we examine two routes to constructing strong colorings. The ﬁrst proof, based on [3], builds up the coloring vertex-by-vertex, using the ordinary LLL. The second proof uses the permutation LLL to build the strong coloring directly. The latter appears to be the ﬁrst RNC algorithm with a reasonable bound on b.

We ﬁrst develop a related concept to the strong coloring known as an independent transversal. In an independent transversal, we choose a single vertex from each block, so that the selected vertices form an independent set of the graph.

Proposition 8.4. Suppose b ≥ 4∆. Then G has an independent transversal, which can be found in expected time O(n∆).

Furthermore, let v ∈ G be any ﬁxed vertex. Then G has an independent transversal which includes v, which can be found in expected time O(n∆2).

Proof. Use the ordinary LLL to select a single vertex uniformly from each block. See [9], [20] for more details. This shows that, under the condition b ≥ 4∆, an independent transversal exists and is found in expected time O(n∆).

To ﬁnd an independent transversal including v, we imagine assigning a weight 1 to vertex v and weight zero to all other vertices. As described in [20], the expected weight of the independent transversal returned by the Moser-Tardos algorithm, is at least Ω(w(V )/∆), where w(V ) is the total weight of all vertices. This implies that that vertex v is selected with probability Ω(1/∆). Hence, after running the Moser-Tardos algorithm for O(∆) separate independent executions, one ﬁnds an independent transversal including v.

Using this as a building block, we can form a strong coloring by gradually adding colors:

- Theorem 8.5. Suppose b ≥ 5∆. Then G has a strong coloring, which can be found in expected time


- O(n2∆2).


Proof. (This proof is almost identical to the proof of Theorem 5.3 of [3]). We maintain a partial coloring of the graph G, in which some vertices are colored with {1,...,b} and some vertices are uncolored. Initially all vertices are uncolored. We require that in a block, no vertices have the same color, and no adjacent vertices have the same color.

Now, suppose some color is partially missing from the strong coloring; say without loss of generality there is a vertex w missing color 1. In each block i = 1,...,k, we will select some vertex vi to have color 1. If the block does not have such a vertex already, we will simply assign vi to have color 1. If the block i already had some vertex ui with color 1, we will swap the colors of vi and ui (if vi was previously uncolored, then ui will become uncolored).

We need to ensure three things. First, the vertices v1,...,vk must form an independent transversal of G. Second, if we select vertex vi and swap its color with ui, this cannot cause ui to have any conﬂicts with its neighbors. Third, we insist of selecting w itself for the independent traversal.

A vertex ui will have conﬂicts with its neighbors if vi currently has the same color as one of the neighbors of ui. In each block, there are at least b−∆ possible choices of vi that avoid that; we must select an independent transversal among these vertices, which also includes the designated vertex w. By Proposition 8.4, this can be done in time O(n2∆2) as long as b ≥ 4∆.

Whenever we select the independent transversal v1,...,vk, the total number of colored vertices increases by at least one: for, the vertex w becomes colored while it was not initially, and in every other block the number of colored vertices does not decrease. So, after n iterations, the entire graph has a strong coloring; the total time is O(n2∆2).

The algorithm based on the ordinary LLL is slow and is inherently sequential. Using the permutation LLL, one can obtain a more direct and faster construction; however, the hypothesis of the theorem will need to be slightly stronger.

- Theorem 8.6. Suppose we have a given graph G of maximum degree ∆, whose vertices are partitioned into blocks of size b. Then if b ≥ 25627 ∆, it is possible to strongly color graph G in expected time O(n∆). If


- b ≥ (25627 + )∆ for some constant > 0, there is an RNC algorithm to construct such a strong coloring. Proof. We will use the permutation LLL. For each block, we assume the vertices and colors are identiﬁed with the set [b]. Then any proper coloring of a block corresponds to a permutation of Sb. When we discuss the color of a vertex v, we refer to πk(v) where k is the block containing vertex v.


For each edge f = u,v ∈ G and any color c ∈ [1,...b], we have a bad-event that both u and v have color c. (Note that we cannot specify simply that u and v have the same color; because we have restricted ourselves to atomic bad-events, we must list every possible color c with a separate bad event.)

Each bad-event has probability 1/b2. We give weight µ(B) = α to every bad event, where α is a scalar to be determined.

Now, each such event (u,v,c) is dependent with four other types of bad-events:

- (1) An event u,v ,c where v is connected to vertex u;
- (2) An event u ,v,c where u is connected to vertex v;
- (3) An event u ,v ,c where u is in the block of u and v is connected to u ;
- (4) An event u ,v ,c where v is in the block of v and u is connected to v


There are b∆ neighbors of each type. For any of these four types, all the neighbors are themselves connected to each other. Hence an independent set of neighbors of the bad-event (u,v,c) can contain one or zero of each of the four types of bad-events.

Using Lemma 3.1 and Pegden’s criterion [33], a suﬃcient condition for the convergence of the Swapping Algorithm is that

α ≥ (1/b2) · (1 + b∆α)4 When b ≥ 25627 ∆, this has a real positive root α∗ (which is a complicated algebraic expression). Further-

more, in this case the expected number of swaps of each permutation is ≤ b2∆α∗ ≤ 25681 ∆. So the Swapping Algorithm terminates in expected time O(n∆). A similar argument applies to the parallel Swapping Algo-

rithm.

- 8.4. Hypergraph packing. In [29], the following packing problem was considered. Suppose we are given two r-uniform hypergraphs H1,H2 and an integer n. Is it possible to ﬁnd two injections φi : V (Hi) → [n]


with the property that φ1(H1) is edge-disjoint to φ2(H2)? (That is, there are no edges e1 ∈ H1,e2 ∈ H2 with {φ1(v) | v ∈ e1} = {φ2(v) | v ∈ e2}. ). A suﬃcient condition on H1,H2,n was given using the LLLL. We achieve this algorithmically as well:

- Theorem 8.7. Suppose that H1,H2 have m1,m2 edges respectively. Suppose that each edge of Hi intersects with at most di other edges of Hi, and suppose that


n r

(d1 + 1)m2 + (d2 + 1)m1 <

e

Then the Swapping Algorithm ﬁnds injections φi : V (Hi) → [n] such that φ1(H1) is edge-disjoint to φ2(H2).

Suppose further that r ≤ logO(1) n and

(1 − ) nr e

(d1 + 1)m2 + (d2 + 1)m1 <

O(1) n time and using poly(m1,m2,n) processors.

Then the Parallel Swapping Algorithm ﬁnds such injections with high probability in log

Proof. [29] proves this fact using the LLLL, and the proof immediately applies to the Swapping Algorithm as well. We review the proof brieﬂy: we may assume without loss of generality that the vertex set of H1 is [n] and the vertex set of H2 has cardinality n and that φ1 is the identity permutation; then we only need to select the bijection φ2 : H2 → [n]. For each pair of edges e1 = {u1,...,ur} ∈ H1,e2 = {v1,...,vr} ∈ H2, and each ordering σ ∈ Sr, there is a separate bad-event φ2(v1) = uσ1 ∧···∧φ2(vr) = uσr. Now observe that the LLL criterion is satisﬁed for these bad-events, under the stated hypothesis.

The proof for the Parallel Swapping Algorithm is almost immediate. There is one slight complication: the total number of atomic bad-events is m1m2r!, which could be super-polynomial for r = Θ(log n). However, it is easy to see that the total number of bad-events which are true at any one time is at most m1m2; namely, for each pair of edges e1,e2, there may be at most one σ such that φ2(v1) = uσ1 ∧ ··· ∧ φ2(vr) = uσr. It is not hard to see that Theorem 7.6 still holds under this condition.

9. Conclusion

The original formulation of the LLLL [14] applies in a natural way to general probability spaces. There has been great progress over the last few years in developing constructive algorithms, which ﬁnd in polynomial time the combinatorial structures in these probability spaces whose existence is guaranteed by the LLL. These algorithms have been developed in great generality, encompassing the Swapping Algorithm as a special case.

However, the Moser-Tardos algorithm has uses beyond simply ﬁnding a object which avoids the badevents. In many ways, the Moser-Tardos algorithm is more powerful than the LLL. We have already seen problems that feature its extensions: e.g., Theorem 8.2 requires the use of the Partial Resampling variant of the Moser-Tardos algorithm, and Proposition 8.4 requires the use of the Moser-Tardos distribution (albeit in the context of the original Moser-Tardos algorithm, not the Swapping Algorithm).

While the algorithmic frameworks of Achlioptas & Iliopoulous and Harvey & Vondr´k achieve the main goal of a generalized constructive LLL algorithm, they do not match the full power of the Moser-Tardos algorithm. However, our analysis shows that the Swapping Algorithm matches nearly all of the additional features of the Moser-Tardos algorithm. In our view, one main goal of our paper is to serve as a roadmap to the construction of a true generalized LLL algorithm. Behind all the diﬃcult technical analysis, there is the underlying theme: even complicated probability spaces such as permutations can be reduced to “variables” (the domain and range elements of the range) which interact in a somewhat “independent” fashion.

Encouragingly, there has been progress toward this goal. For example, one main motivation of [1, 22] was to generalize the Swapping Algorithm. Then, Kolmogorov noticed in [27] that our Swapping Algorithm had a certain nice property, namely the ability to select the resampled bad-event in an arbitrary fashion, that the analysis of [1] lacked; this led to the work of [27] which partially generalized that property (which Kolmogorov refers to as commutativity).

At the current time, we do not even know how to deﬁne a truly generalized LLL algorithm, let alone analyze it. But we hope that we have at least provided an example approach toward such an algorithm.

10. Acknowledgments

We would like to thank the anonymous reviewers of the conference and journal versions of this paper, for their helpful comments and suggestions.

Appendix A. Symmetry properties of the swapping subroutine

In the following series of propositions, we show a variety of symmetry properties of the swapping subroutine. This analysis will use simple results and notations of group theory. We let Sl denote the symmetric group on l letters, which we identify with the set of permutations of [l]. We let (a b) denote the permutation (of whatever dimension is appropriate) that swaps a/b and is the identity otherwise. We write multiplications on the right, so that στ denotes the permutation which maps x to σ(τ(x)). Finally, we will sometimes write σx instead of the more cumbersome σ(x).

- Proposition A.1. The swapping subroutine is invariant under permutations of the domain or range, namely that for any permutations τ,σ we have

P(Swap(π;x1,...,xr) = σ) = P(Swap(πτ;τ−1x1,...,τ−1xr) = στ) and

P(Swap(π;x1,...,xr) = σ) = P(Swap(τπ;x1,...,xr = τσ) Proof. We prove this by induction on r. The following equivalence will be useful. We can view a single call to Swap as follows: we select a random x 1 and swap x1 with x 1; let π = π · (x1 x 1) denote the permutation after this swap. Now consider the permutation on n−1 letters obtained by removing x1 from the range and π (x1) from the range of π ; we use the notation π − (x1,∗) to denote this restriction of range/domain. We then recursively call Swap(π − (x1,∗),x2,...,xr).

Now, in order to have Swap(πτ;τ−1x1,...,τ−1xr) = στ we must ﬁrst swap τ−1x1 with x 1 = τ−1π−1στx1; this occurs with probability 1/n. Then we would have

P(Swap(πτ;τ−1x1,...,τ−1xr) = στ)

= n1P(Swap(πτ(τ−1x1 τ−1π−1σx1) − (τ−1x1,∗);τ−1x2,...,τ−1xr) = στ − (τ−1x1,∗))

= n1P(Swap(πτ(τ−1x1 τ−1π−1σx1)τ−1 − (x1,∗);τ−1τx2,...,τ−1τxr) = σττ−1 − (x1,∗))

by inductive hypothesis

= n1P(Swap(π(x1 π−1σx1)τ−1 − (x1,∗);x2,...,xr) = σ − (x1,∗))

= P(Swap(π;x1,x2,...,xr) = σ) A similar argument applies for permutation of the range (i.e., post-composition by τ). Also, the order in which we perform the swaps is irrelevant:

- Proposition A.2. Let π ∈ Sn be ﬁxed, and let x1,...,xr ∈ [n] be ﬁxed as well. Let ρ : [r] → [r] be a permutation on r letters; then for any permutation σ ∈ Sn we have


P(Swap(π;x1,...,xr) = σ) = P(Swap(π;xρ(1),...,xρ(r) = σ)

Proof. We will prove this by induction on r. We assume ρ(1) = 1 or else this follows immediately from induction.

We have:

- P(Swap(π;xρ(1),...,xρ(r)) = σ)


= n1P(Swap(π(xρ(1) π−1σxρ(1));xρ(2),...,xρ(r)) = σ)

= n1P(Swap(π(xρ(1) π−1σxρ(1));x1,x2,...,xρ(1)−1,xρ(1)+1,...,xr) = σ) by I.H.

= n(n1−1)P(Swap(π(xρ(1) π−1σxρ(1))(x1 (π(xρ(1) π−1σxρ(1))−1)σx1)x2,...,xρ(1)−1,xρ(1)+1,...,xr) = σ)

= n(n1−1)P(Swap(π(xρ(1) π−1σxρ(1))(x1 (xρ(1) π−1σxρ(1))π−1σx1)x2,...,xρ(1)−1,xρ(1)+1,...,xr) = σ)

At this point, consider the following simple fact about permutations: for any a1,a2,b1,b2 ∈ [l] with a1 = a2,b1 = b2, we have

(a2 b2)(a1 (a2 b2)b1) = (a1 b1)(a2 (a1 b1)b2)

This fact is simple to prove by case analysis considering which of the letters a1,a2,b1,b2 are equal to each other.

We now apply this fact using a1 = x1,a2 = xρ(1),b1 = π−1σa1,b2 = π−1σa2; this gives us P(Swap(π;xρ(1),...,xρ(r)) = σ)

= n(n1−1)P(Swap(π(x1 π−1σx1)(xρ(1) (x1 π−1σx1)π−1σxρ(1));x2,...,xρ(1)−1,xρ(1)+1,...,xr) = σ)

= n1P(Swap(π(x1 π−1σx1);xρ(1),x2,...,xρ(1)−1,xρ(1)+1,...,xr) = σ)

= n1P(Swap(π(x1 π−1σx1);x2,...,xr) = σ) by I.H.

= P(Swap(π;x1,...,xr) = σ)

In our analysis and algorithm, we will seek to maintain the symmetry between the “domain” and “range” of the permutation. The swapping subroutine seems to break this symmetry, inasmuch as the swaps are all based on the domain of the permutation. However, this symmetry-breaking is only superﬁcial as shown in

- Proposition A.3.


Proposition A.3. Deﬁne the alternate swapping subroutine, which we denote Swap2(π;y1,...,yr) as follows:

- (1) Suppose π is a permutation of [n]. Repeat the following for i = 1,...,r:
- (2) Select y i uniformly at random among [n] − {y1,...,yi−1}.
- (3) Swap entries π−1(yi) and π−1(y i) of the permutation π.


More compactly:

Swap2(π;y1,...,yr) = Swap(π−1,y1,...,yr)−1

Then the algorithms Swap and Swap2 induce the same distribution, namely that if π(x1) = y1,...,π(xr) = yr, then for any permutation σ we have

P(Swap(π;x1,...,xr) = σ) = P(Swap2(π;y1,...,yr) = σ)

Proof. A similar recursive deﬁnition applies to Swap2 as for Swap: we select x 1 uniformly at random, swap x1/x 1, and then call Swap2(π(x1 x 1) − (∗,y1);y2,...,yr). The main diﬀerence is that we remove the image point (∗,y1) instead of the domain point (x1,∗).

Now, in order to have Swap2(π;y1,...,yr) = σ we must ﬁrst swap x1 with x 1 = π−1σx1; this occurs with probability 1/n. Next, we recursively call Swap2 on the permutation π(x1x 1) − (∗,y1) yielding: P(Swap2(π;y1,...,yr) = σ) = n1P(Swap2(π(x1x 1) − (∗,y1);y2,...,yr) = σ − (∗,y1))

= n1P(Swap(π(x1 x 1) − (∗,y1);(x1 x 1)π−1y2,...,(x1 x 1)π−1yr) = σ − (∗,y1))

by inductive hypothesis

= n1P(Swap(π − (x1,y1);x2,...,xr) = σ(x1 x 1) − (x1,y1))

by Proposition A.1, when we pre-compose with (x1 x 1)

= n1P(Swap((σx1 σx 1)π − (x1,∗);x2,...,xr) = (σx1 σx 1)σ(x1 x 1) − (x1,∗)

by Proposition A.1; when we post-compose with (σx1 σx 1)

= n1P(Swap(π(x1 x 1) − (x1,∗);x2,...,xr) = σ − (x1,∗)

= P(Swap(π;x1,...,xr) = σ)

References

- [1] Achlioptas, D., Iliopoulos, F.: Random walks that ﬁnd perfect objects and the Lovasz Local Lemma. Foundations of Computer Science (2014).
- [2] Albert, M., Frieze, A., Reed, B.: Multicoloured Hamilton Cycles. The Electronic Journal of Combinatorics 2-1, R10. (1995)
- [3] Aharoni, R., Berger, E., Ziv, R.: Independent systems of representatives in weighted graphs. Combinatorica 27.3, pp. 253-267 (2007).
- [4] Alon, N.: Probabilistic proofs of existence of rare events. Springer Lecture Notes in Mathematics No. 1376 (J. Lindenstrauss and V. D. Milman, Eds.), Springer-Verlag, pp. 186-201 (1988).


- [5] Alon, N.: The strong chromatic number of a graph. Random Structures and Algorithms 3-1, pp. 1-7 (1992).
- [6] Alon, N., Babai, L., Itai, A.: A fast and simple randomized parallel algorithm for the maximal independent set problem. J. Algorithms 7(4): 567-583 (1986).
- [7] Alon, N., Spencer, J., Tetali, P.: Covering with Latin transversals. Discrete Applied Math. 57, pp. 1-10 (1995).
- [8] Axenovich, M., Martin, R.: On the strong chromatic number of graphs. SIAM J. Discrete Math 20-3, pp. 741-747 (2006).
- [9] Bissacot, R., Fernandez, R., Procacci, A., Scoppola, B.: An improvement of the Lov´asz Local Lemma via cluster expansion. Combinatorics, Probability and Computing 20-5, pp. 709-719 (2011).
- [10] Bottcher, J., Kohayakawa, Y., Procacci, A.: Properly coloured copies and rainbow copies of large graphs with small maximum degree. Random Structures and Algorithms 40-4, pp. 425-436 (2012).
- [11] Cook, S.: A Taxonomy of problems with fast parallel algorithms. Information and Control 64, pp. 2-22 (1985).
- [12] De´nes, J., Keedwell, A. D.: Latin squares and their applications. Akade´miai Kiado´, Budapest & English Universities Press

(1974).

- [13] Erd˝os, P., Hickerson, D. R., Norton, D. A., Stein, S. K.: Has every Latin square of order n a partial Latin transversal of size n − 1? Amer. Math. Monthly 95, pp. 428430 (1988).
- [14] Erd˝os, P., Spencer, J.: Lopsided Lova´sz Local Lemma and Latin transversals. Discrete Applied Math 30, pp. 151-154

(1990).

- [15] Esperet, L., Parreau, A.: Acyclic edge-coloring using entropy compression. European Journal of Combinatorics 34-6, pp. 1019-1027 (2013).
- [16] Fellows, M.: Transversals of vertex partitions in graphs. SIAM J. Discrete Math 3-2, pp. 206-215 (1990).
- [17] Freize, A., Krivelevich, M.: On rainbow trees and cycles. The Electronic Journal of Combinatorics 15-1, R. 59 (2008)
- [18] Haeupler, B., Saha, B., Srinivasan, A.: New constructive aspects of the Lov´asz Local Lemma. Journal of the ACM 58

(2011).

- [19] Hahn, G., Thomassen, C.: Path and cycle sub-Ramsey numbers and an edge-colouring conjecture. Discrete Mathematics 62-1, pp. 29-33 (1986)
- [20] Harris, D., Srinivasan, A.: The Moser-Tardos framework with partial resampling. Proc. IEEE Symp. Foundations of Computer Science, pp. 469–478 (2013).
- [21] Harris, D., Srinivasan, A.: A constructive algorithm for the Lov´asz Local Lemma on permutations. Proc. ACM-SIAM Symposium on Discrete Algorithms, pp. 907-925 (2014).
- [22] Harvey, N., Vondr´ak, J.: An algorithmic proof of the Lopsided Lov´asz Local Lemma via resampling oracles. IEEE Symposium on Foundations of Computer Science, pp. 1327-1346 (2015)
- [23] Haxell, P.: On the strong chromatic number. Combinatorics, Probability, and Computing 13-6, pp. 857-865 (2004).
- [24] Haxell, P.: An improved bound for the strong chromatic number. Journal of Graph Theory 58-2, pp. 148-158 (2008).
- [25] Keevash, P., Ku, C.: A random construction for permutation codes and the covering radius. Designs, Codes and Cryptography 41-1, pp. 79-86 (2006).
- [26] Kolipaka, K., Szegedy, M.: Moser and Tardos meet Lov´asz. Proc. ACM Symposium on Theory of Computing, pp. 235-244

(2011).

- [27] Kolmogorov, V.: Commutativity in the random walk formulation of the Lov´asz Local Lemma. Arxiv 1506.08547 (2015).
- [28] Lu, L., Mohr, A., Sze´ke´ly, L.: Quest for negative dependency graphs. Recent Advances in Harmonic Analysis and Applications pp. 243-258 (2013).
- [29] Lu, L., Sze´ke´ly, L.: Using Lov´asz Local Lemma in the space of random injections. The Electronic Journal of Combinatorics 13-R63 (2007).
- [30] Luby, M.: A simple parallel algorithm for the maximal independent set problem. SIAM J. Comput. 15(4):1036-1053 (1986).
- [31] Mohr, A.: Applications of the Lopsided Lova´sz Local Lemma regarding hypergraphs. PhD Thesis, University of South Carolina (2013).
- [32] Moser, R., Tardos, G.: A constructive proof of the general Lova´sz Local Lemma. Journal of the ACM 57-2, pp. 11:1-11:15

(2010).

- [33] Pegden, W.: An extension of the Moser-Tardos algorithmic Local Lemma. SIAM Journal of Discrete Math 28-2, pp. 911-917

(2014).

- [34] Scott, A., Sokal, A.: The repulsive lattice gas, the independent-set polynomial, and the Lov´asz Local Lemma. J. Stat. Phys. 118, No. 5-6, pp. 11511261 (2005).
- [35] Shearer, J. B.: On a problem of Spencer. Combinatorica 5, 241-245 (1985).
- [36] Shor, P. W.: A lower bound for the length of a partial transversal in a Latin square. J. Combin. Theory Ser. A. 33, pp. 1-8 (1982).
- [37] Stein, S. K.: Transversals of Latin squares and their generalizations. Paciﬁc J. Math. 59, pp. 567-575 (1975).
- [38] Szab´o, S.: Transversals of rectangular arrays. Acta Math. Univ. Comenianae, Vol. 37, pp. 279-284 (2008).


