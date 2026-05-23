---
type: source
kind: paper
title: Some remarks on hypergraph matching and the Füredi-Kahn-Seymour conjecture
authors: Nikhil Bansal, David G. Harris
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2011.07097v3
source_local: ../raw/2020-bansal-some-remarks-hypergraph-matching.pdf
topic: author-sweep
cites:
---

arXiv:2011.07097v3[math.CO]8Mar2022

Some remarks on hypergraph matching and the Fu¨redi-Kahn-Seymour conjecture

Nikhil Bansal∗ David G. Harris†

Abstract A classic conjecture of F¨uredi, Kahn and Seymour (1993) states that any hypergraph with

non-negative edge weights w(e) has a matching M such that e∈M(|e| − 1 + 1/|e|)w(e) ≥ w∗, where w∗ is the value of an optimum fractional matching. We show the conjecture is true for

rank-3 hypergraphs, and is achieved by a natural iterated rounding algorithm. While the general conjecture remains open, we give several new improved bounds. In particular, we show that the iterated rounding algorithm gives e∈M(|e| − δ(e))w(e) ≥ w∗, where δ(e) = |e|/(|e|2 + |e| − 1), improving upon the baseline guarantee of e∈M |e|w(e) ≥ w∗.

# 1 Introduction

Let H = (V,E) be a hypergraph with vertex set V and edge set E, where each edge e ∈ E is a subset of V ; for simplicity, we assume throughout that ∅ ∈/ E. We deﬁne the rank of H to be the largest size of any edge in E. We deﬁne Ek to be the set of edges of cardinality k; we call these k-edges for brevity. For a vertex v, we deﬁne the edge-neighborhood N(v) = {e : v ∈ e} to be the edges containing v, and Nk(v) = N(v) ∩ Ek to be the k-edges containing v. Likewise, for an edge e, we deﬁne the (exclusive) edge-neighborhood N(e) = {f : e = f,e ∩ f = ∅} = v∈e N(v) \ {e} and Nk(e) = N(e) ∩ Ek.

A matching M of H is a collection of pairwise disjoint edges; equivalently, it is an independent set of the line graph of H. A fractional matching of H is a function x : E → [0,1] satisfying the condition

x(e) ≤ 1 for all vertices v ∈ V. (1)

e∈N(v)

In other words, viewing x(e) as the fractional extent to which an edge is picked, the total fraction of edges containing any vertex v is at most 1. Clearly, if x takes on integral values, then it corresponds to a matching. We say that x is a basic fractional matching if it is an extreme point of the fractional matching polytope given by the constraints (1).

Given a non-negative weight function w : E → R≥0 on the edges, we deﬁne the weight of a fractional matching x by

w(x) =

w(e)x(e).

e∈E

![image 1](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile1.png>)

∗University of Michigan, Ann Arbor. bansal@gmail.com. Supported in part by the NWO VICI grant 639.023.812. †University of Maryland, College Park. davidgharris29@gmail.com

Given the fundamental role of matchings in combinatorics, optimization and computer science, there has been quite some interest in understanding the integrality gap between the weight of the integral and fractional matchings.

The FKS Conjecture. With the aim of exactly pinning down the integrality gap, Fu¨redi, Kahn & Seymour conjectured a ﬁne-grained relation between integral and fractional matchings [7]. This is particularly powerful for settings where the edges have diﬀerent sizes. There are two formulations of the conjecture. The original version was stated in the primal form below. As shown in [1], the dual version is equivalent to the primal version, both algorithmically and combinatorially.

- Conjecture 1.1 (FKS conjecture [7]). Let H be a hypergraph with fractional matching x. (Primal) For any weight function w : E → R≥0, there exists a matching M with


(|e| − 1 + 1/|e|)w(e) ≥ w(x). (2)

e∈M

(Dual) There is a probability distribution Ω over matchings of H, such that when M is drawn from Ω, every edge e ∈ E satisﬁes

x(e) |e| − 1 + 1/|e|

Pr(e ∈ M) ≥

. (3)

![image 2](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile2.png>)

This conjecture was shown for a number of special cases in [7], including uniform hypergraphs where all the edges have the same size. The factor k − 1 + 1/k for edges of size k is optimal for inﬁnitely many values of k (it is tight for projective planes).

The fractional matching LP can easily be solved eﬃciently, while ﬁnding or approximating a maximum-weight matching is intractable even for rank-3 hypergraphs [8]. Thus, the FKS conjecture is closely related to approximation algorithms for matchings. A number of recent papers [4, 1] have shown weakened versions of Conjecture 1.1; most recently, [1] showed the following:

- Proposition 1.2 ([1]). For a hypergraph H with fractional matching x, there is a probability distribution Ω over matchings of H, such that when M is drawn from Ω, every edge e ∈ E satisﬁes


x(e) |e| − (|e| − 1)x(e)

Pr(e ∈ M) ≥

.

![image 3](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile3.png>)

As x(e) can be arbitrarily small for a particular edge, the denominator can be arbitrarily close to |e|, and in particular this gives the following.

- Corollary 1.3 ([1]). For a hypergraph H = (V,E) with fractional matching x and weight function


- w : E → R≥0, there is a matching M with


|e|w(e) ≥ w(x).

e∈M

To better situate the FKS conjecture, let us note a more general result for independent sets in graphs, based on constructions in [1, 5].

Theorem 1.4. Let G = (V,E) be a graph and λ : V → R≥0 be a non-negative function. There is a probability distribution Ω over independent sets I of G, such that when I is drawn from Ω, every vertex v ∈ V satisﬁes

λ(v) λ(v) + vu∈E λ(u)

Pr(v ∈ I) ≥

.

![image 4](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile4.png>)

Proof. For each vertex v, draw an independent Exponential random variable Xv with rate λ(v). Place v into I if Xv < Xu for all neighbors u of v. The claim follows directly from the standard properties of the minimum of exponential random variables.

![image 5](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile5.png>)

![image 6](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile6.png>)

![image 7](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile7.png>)

![image 8](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile8.png>)

Setting λ(v) = 1 for all v in Theorem 1.4 gives one version of the well-known Caro-Wei theorem where each vertex v goes into the independent set with probability 1/(deg(v) + 1). Indeed,

- Theorem 1.4 should be thought of as a fractional version of the Caro-Wei theorem. To see how


- Theorem 1.4 implies Proposition 1.2, note that for any edge e of H, the sum of x(e) over neighboring edges f is given by


x(f) ≤

x(f) ≤ |e|(1 − x(e)).

v∈e f∈N(v)\{e}

f∈N(e)

Thus, applying Theorem 1.4 to the line graph G of H with λ(e) = x(e), we get

x(e) x(e) + f∈N(e) x(f)

≥

Pr(e ∈ M) ≥

![image 9](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile9.png>)

x(e) x(e) + |e|(1 − x(e))

=

![image 10](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile10.png>)

x(e) |e| − (|e| − 1)x(e)

. (4)

![image 11](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile11.png>)

In this sense, the results of Proposition 1.2 and Corollary 1.3 are essentially only using crude degree statistics of the line graph of H. The FKS conjecture asks whether it is possible to take advantage of underlying matching structure to improve over this bound.

For example, suppose that (wishfully speaking) we were guaranteed that x(e) ∈ {0} ∪ [1/|e|,1] for all e. In this case, (4) would imply the bound in (3) and hence the FKS conjecture. While such a property is too much to hope for in general, it suﬃces to have a lower bound on x(e) in a certain average sense. As we discuss shortly, this argument was used already in [7] to show the FKS conjecture for uniform hypergraphs.

# 2 Iterative rounding and our results

Chan & Lau [6] described an iterative rounding procedure to turn the existential bounds of [7] for uniform hypergraphs into an eﬀective algorithm. We will extend this approach to cover nonuniform hypergraphs (see Proposition 2.3 below for the formal statement). Roughly speaking, this algorithm is based on the “local-ratio” technique [3]. Given an instance H the algorithm solves the fractional matching LP and considers a suitable edge e. It modiﬁes the weight of neighbors of e and removes e to obtain a smaller hypergraph H′ and recursively applies the algorithm to H′.

Consider a hypergraph H = (V,E), where in addition each edge has a weight w(e) as well as an associated “discount factor” g(e) ∈ (0,1]. For concreteness, one can think of g(e) = 1/|e|. We

can use the following FindMatching algorithm to obtain a high-weight matching for H. Algorithm 1: FindMatching(H,g,w)

![image 12](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile12.png>)

![image 13](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile13.png>)

- 1 if H has no edges, then return ∅ and terminate.
- 2 if there is some edge e ∈ H with w(e) ≤ 0 then return FindMatching(H \ {e},g,w)
- 3 Solve the fractional matching LP to get a basic fractional matching x maximizing w(x).
- 4 if there is some edge e ∈ H with f∈N(e) g(f)x(f) ≤ 1 − g(e)x(e) then

![image 14](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile14.png>)

- 5 Choose an arbitrary such edge e
- 6 Deﬁne new weight function w′ by

w′(f) =

w(f) − w(e)g(f)/g(e) if f ∈ N(e) w(f) if f ∈/ N(e)

- 7 Set M′ ← FindMatching(H \ {e},g,w′)
- 8 if M′ ∩ N(e) = ∅ then

![image 15](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile15.png>)

- 9 return M = M′ ∪ {e}

![image 16](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile16.png>)

- 10 else

![image 17](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile17.png>)

- 11 return M = M′

![image 18](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile18.png>)

![image 19](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile19.png>)

- 12 Output “ERROR” and terminate


![image 20](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile20.png>)

Note that while the earlier algorithm [6] used identical discount factors everywhere, ours can be diﬀerent for each edge. Proposition 2.3 below analyzes the quality of the solution returned by the algorithm, in terms of the discount factors. The following deﬁnitions are critical for our analysis.

- Deﬁnition 2.1. A basic fractional matching x is stuck for g if it satisﬁes the condition

∀e ∈ E

f∈N(e)

g(f)x(f) > 1 − g(e)x(e). (5)

- Deﬁnition 2.2. Discount factor g is good for H if no non-empty subgraph of H has a basic fractional matching that is stuck for g.


- Proposition 2.3. Algorithm FindMatching(H,g,w) runs in polynomial time, and outputs either ERROR or a matching of H. In the former case, g is not good for H. In the latter case, the matching M satisﬁes


w(f)/g(f) ≥ w∗

f∈M

where w∗ is the maximum weight of any fractional matching of H.

Proof. Each iteration of FindMatching clearly runs in polynomial time. Each subproblem has its edge count reduced by one, so there are at most |E| iterations in total. Since we only add e to M if N(e) ∩ M′ = ∅, the output M is clearly a matching. We now show the two properties by induction on |E|. The base case where E = ∅ are clear in both cases.

For the induction step, observe that if the algorithm reaches line 12, then the fractional matching

- x is evidently stuck for g. Otherwise, suppose that the recursive call on hypergraph H \ {e} at line 2 or 7 terminates in ERROR. By induction hypothesis, there is a basic fractional matching x′ which is stuck for g for some H′ = (V,E′) with E′ ⊆ E \ {e}; this shows the ﬁrst claim.


The induction step for the second claim is clear if some edge e has w(e) ≤ 0. Otherwise, let M′ = FindMatching(H \ {e},g,w′) where e is the edge chosen at line 5, and let F = M′ ∩ N(e). We calculate:

w(f)/g(f) =

f∈M′

w′(f)/g(f) +

f∈M′

f∈F

g(f)w(e)/g(e) g(f)

=

![image 21](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile21.png>)

w′(f)/g(f) + |F|w(e)/g(e). (6)

f∈M′

The restriction of x to H \ {e} is also a fractional matching. So by the induction hypothesis and using the deﬁnition of w′, we have

w′(f)/g(f) ≥ max

w′(x′) ≥

w′(f)x(f)

fractional matchings x′

f∈M′

f∈E\{e}

w(f)x(f) − w(e)

=

f∈E

g(f)x(f)/g(e) + x(e) ,

f∈N(e)

The criterion for choosing e at line 5 ensures that f∈N(e) g(f)x(f) ≤ 1 − g(e)x(e). Since w(e) > 0, substituting this bound into the above formula gives:

f∈M′

Together with (6), this implies

w′(f)/g(f) ≥ w(x) − w(e)/g(e).

w(f)/g(f) ≥ w(x) + (|F| − 1)w(e)/g(e).

f∈M′

Now, if F = ∅, then M = M′ ∪ {e}, and so

w(f)/g(f) = w(e)/g(e) +

f∈M

w(f)/g(f) ≥ w(e)/g(e) + w(x) − w(e)/g(e) = w(x).

f∈M′

Otherwise, if |F| > 0, then M = M′ and so

w(f)/g(f) =

f∈M

w(f)/g(f) ≥ w(x) + (|F| − 1)w(e)/g(e) ≥ w(x).

f∈M′

In either case, it holds that f∈M w(f)/g(f) ≥ w(x) = w∗.

![image 22](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile22.png>)

![image 23](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile23.png>)

![image 24](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile24.png>)

![image 25](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile25.png>)

## 2.1 Our results

Given Proposition 2.3, we make the following conjecture which would, in particular, show the FKS conjecture:

- Conjecture 2.4. If we set g(e) = |e|−1+11 /|e| for all edges e of H, then g is good for H.


![image 26](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile26.png>)

It was already shown in [6] that Conjecture 2.4 holds for uniform hypergraphs. As some further evidence for Conjecture 2.4, and the FKS conjecture, we show the following:

- Theorem 2.5. If H has rank 3, then Conjecture 2.4 holds for H.


We prove Theorem 2.5 in Section 3. In Section 3, we also prove a number of bounds for what we call bi-uniform hypergraphs, i.e., hypergraphs which have two possible edge sizes. We consider general hypergraphs in Section 4, and while we are not able to show Conjecture 2.4, we can show the following result which is strictly stronger than Corollary 1.3:

- Theorem 2.6. Let h : N → R be any function satisfying the following conditions for all k ≥ 2:


- (A1) h(k + 1) ≤ h(k)
- (A2) 0 ≤ h(k) ≤ 1/(k − 1 + 1/k)
- (A3) h(k + 1) ≤ 1 − (k − 1)h(k)


The discount factor deﬁned by g(e) = h(|e|) for all edges e is good for any hypergraph H. In particular, there is a probability distribution over matchings M with Pr(e ∈ M) ≥ h(|e|) for all e.

We prove Theorem 2.6 in Section 4. Notice that h(k) = 1/k satisﬁes each of the conditions (A1), (A2), (A3) with some slack, which will allow us to obtain improved bounds of the form h(k) = 1/(k − δ(k)) for some functions δ(k) > 0. There is no single optimal choice for the function h, and we give some sample bounds in the following corollary.

- Corollary 2.7. Let H = (V,E) be a hypergraph.


- 1. If H has rank r, the following is good for H:

g(e) = hr(|e|) for hr(k) =

(−1)r−k(k − 2)! (r − 2)!(r + 1/r − 1)

![image 27](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile27.png>)

+

r−k

i=1

(−1)i+1(k − 2)! (k − 2 + i)!

![image 28](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile28.png>)

.

- 2. With no restriction on rank, the following is good for H:

g(e) = h∞(|e|) for h∞(k) =

∞

i=1

(−1)i+1(k − 2)! (k − 2 + i)!

![image 29](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile29.png>)

- 3. With no restriction on rank, the following is good for H:


1 k − δ(k)

k k2 + k − 1

g(e) = h˜∞(|e|) for h˜∞(k) =

,where δ(k) :=

.

![image 30](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile30.png>)

![image 31](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile31.png>)

The proof of Corollary 2.7 appears in Appendix A. In order to compare and illustrate these bounds, let us denote the function corresponding to

the FKS conjecture by

h∗(k) = 1/(k − 1 + 1/k)

Figure 1 shows the baseline value 1/k in Corollary 1.3, the conjectured function h∗(k), and the values h∞(k),h˜∞(k) from Corollary 2.7.

![image 32](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile32.png>)

![image 33](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile33.png>)

![image 34](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile34.png>)

![image 35](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile35.png>)

![image 36](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile36.png>)

![image 37](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile37.png>)

![image 38](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile38.png>)

![image 39](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile39.png>)

k 1/k h∗(k) h∞(k) h˜∞(k)

![image 40](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile40.png>)

![image 41](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile41.png>)

![image 42](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile42.png>)

- 2 0.5000 0.6667 0.6321 0.6250

![image 43](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile43.png>)

![image 44](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile44.png>)

![image 45](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile45.png>)

![image 46](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile46.png>)

![image 47](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile47.png>)

![image 48](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile48.png>)

![image 49](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile49.png>)

![image 50](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile50.png>)

- 3 0.3333 0.4286 0.3679 0.3667

![image 51](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile51.png>)

![image 52](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile52.png>)

![image 53](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile53.png>)

![image 54](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile54.png>)

![image 55](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile55.png>)

![image 56](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile56.png>)

![image 57](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile57.png>)

![image 58](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile58.png>)

- 4 0.2500 0.3077 0.2642 0.2639

![image 59](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile59.png>)

![image 60](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile60.png>)

![image 61](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile61.png>)

![image 62](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile62.png>)

![image 63](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile63.png>)

![image 64](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile64.png>)

![image 65](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile65.png>)

![image 66](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile66.png>)

- 5 0.2000 0.2381 0.2073 0.2071

![image 67](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile67.png>)

![image 68](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile68.png>)

![image 69](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile69.png>)

![image 70](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile70.png>)

![image 71](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile71.png>)

![image 72](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile72.png>)

![image 73](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile73.png>)

![image 74](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile74.png>)

- 6 0.1667 0.1935 0.1709 0.1708

![image 75](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile75.png>)

![image 76](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile76.png>)

![image 77](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile77.png>)

![image 78](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile78.png>)

![image 79](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile79.png>)

![image 80](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile80.png>)

![image 81](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile81.png>)

![image 82](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile82.png>)

- 7 0.1429 0.1628 0.1455 0.1455

![image 83](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile83.png>)

![image 84](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile84.png>)

![image 85](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile85.png>)

![image 86](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile86.png>)

![image 87](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile87.png>)

![image 88](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile88.png>)

![image 89](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile89.png>)

![image 90](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile90.png>)

- 8 0.1250 0.1404 0.1268 0.1268

![image 91](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile91.png>)

![image 92](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile92.png>)

![image 93](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile93.png>)

![image 94](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile94.png>)

![image 95](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile95.png>)

![image 96](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile96.png>)

![image 97](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile97.png>)

![image 98](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile98.png>)

- 9 0.1111 0.1233 0.1124 0.1124

![image 99](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile99.png>)

![image 100](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile100.png>)

![image 101](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile101.png>)

![image 102](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile102.png>)

![image 103](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile103.png>)

![image 104](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile104.png>)

![image 105](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile105.png>)

![image 106](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile106.png>)

- 10 0.1000 0.1099 0.1009 0.1009 20 0.0500 0.0525 0.0501 0.0501


![image 107](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile107.png>)

![image 108](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile108.png>)

![image 109](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile109.png>)

![image 110](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile110.png>)

![image 111](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile111.png>)

![image 112](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile112.png>)

![image 113](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile113.png>)

![image 114](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile114.png>)

![image 115](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile115.png>)

![image 116](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile116.png>)

![image 117](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile117.png>)

![image 118](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile118.png>)

![image 119](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile119.png>)

![image 120](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile120.png>)

![image 121](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile121.png>)

Figure 1: Table showing k along with a few approximation factors from the diﬀerent results. Terms are rounded to four decimal places for readability.

To help parse these expressions, we record a few observations.

- • We have hk(k) = h∗(k) = k−1+11 /k, matching the known bound for k-uniform hypergraphs.

![image 122](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile122.png>)

- • As hr(k) is given by an alternating sum, the values hk+2i(k) are decreasing in i, and the values hk+1+2i(k) are increasing in i. They both converge to h∞(k). For any ﬁxed k, the least value hr(k) is attained for r = k + 1 which equals hk+1(k) = k2/(k3 − 1), that is,

hr(k) ≥ k2/(k3 − 1) > 1/k.

- • A simple calculation shows that h˜∞(k) = hk+3(k) ≤ h∞(k) ≤ h∗(k). While h∞(k) is always larger than h˜∞(k), they are quite close asymptotically. More speciﬁcally,

h∗(k) = k−1 + k−2 − O(k−4), h∞(k),h˜∞(k) = k−1 + k−3 − O(k−4).

- • The value h∞(k) can be computed in closed form as h∞(k) = (−1)k(Dk−2−(k−2)!/e), where Dn is the number of derangements on n letters and e = 2.718... is the base of the natural logarithm. For example, h∞(3) = 1/e,h∞(4) = 1 − 2/e, etc.


Intuition. Before the formal proofs of Theorem 2.5 and Theorem 2.6, let us provide a high-level overview. The idea is to show that if the algorithm gets stuck for some fractional solution x, then x cannot be a basic solution to the LP deﬁning the matching. This involves combining the inequalities (5) suitably to obtain a contradiction to some property of a basic solution.

Let us start with the simpler case of k-uniform hypergraphs (where the FKS conjecture is already known) and show that the algorithm does not get stuck for g(e) = h∗(k) = 1/(k−1+1/k). Consider some basic solution x to the LP, and let V ′ be the set of tight vertices v with f∈N(v) x(f) = 1, and let E′ be the set of edges with x(e) > 0. As x is a basic solution, we have |E′| ≤ |V ′|. We will show that if we assume that the algorithm is stuck, then the inequalities

h∗(k) x(e) +

x(f) > 1 (7)

f∈N(e)

can be combined to derive |V ′| < |E′|, a contradiction.

Indeed, as x is feasible we have f∈N(v) x(f) ≤ 1 for each v; summing over the vertices v in an edge e gives f |f ∩ e|x(f) ≤ k, and thus kx(e) + f∈N(e) x(f) ≤ k. Together with (7), this gives

(k − 1)x(e) < k − 1/h∗(k) = 1 − 1/k,

or equivalently x(e) < 1/k. On the other hand, as H is k-uniform and the vertices in V ′ are all tight, summing over e ∈ E′ gives

x(e) = |V ′|.

x(e) ≥

k

x(e) =

v∈V e∈N(v)

e∈E′

v∈V ′ e∈N(v)

Together this implies |V ′| ≤ k e∈E′ x(e) < |E′|. This is the desired contradiction, which is essentially the proof given in [7].

Non-uniform edges. The computations for non-uniform edges sizes get more involved. To explain, let us divide the edges into two groups: the edges Ek of size k, and edges E>k of size strictly larger than k. Suppose that we use discount factors given by g(e) = h∗(k) for k-edges and g(e) = 1/|e| (the baseline value) for the larger edges.

If all the k-edges were “self-interacting,” that is, had no neighbors in E>k, then we could use the argument above for uniform hypergraphs. On the other hand, suppose that an edge e ∈ Ek has only neighbors outside Ek. Then, for this edge e, we could calculate

g(f)x(f) ≤

f∈N(e)

x(f)/|f| ≤

f∈N(e)

k k + 1

k k + 1

(1 − x(e)) ≤

x(f)/(k + 1) ≤

,

![image 123](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile123.png>)

![image 124](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile124.png>)

f∈N(e)

so that the condition (5) forces x(e) to be large. Consequently, x is not stuck for g (it can make progress on edge e).

In Theorem 2.6, we track the amount of self-interaction for the k-edges, showing that we always can ﬁnd some k-edge where x(e) is large enough not to get stuck.

In Theorem 2.5, we track this more carefully: we not only keep track of the self-interaction among 2-edges, but we also keep track of the self-interaction among 3-edges. Since the hypergraph has only two edge sizes, the amounts of these self-interactions can be related to each other.

Before we show Theorems 2.5 and 2.6, we next record some simple observations and deﬁnitions to analyze FindMatching and stuck fractional matchings.

## 2.2 Simple bounds for stuck fractional matchings

For a fractional matching x, we say that a vertex v is tight if e∋v x(e) = 1. We say that x is reduced if x(e) ∈ (0,1) for all edges e. We deﬁne B ⊆ V to be the set of all tight vertices. For any

set of edges L ⊆ E, we deﬁne B(L) = e∈L e ∩ B.

- Proposition 2.8. If x is reduced, then for any edge-set L ⊆ E, there holds |L| ≤ |B(L)|.


Proof. Let us consider the restriction of the fractional matching LP to the edges in L, i.e., all the values x(e) for e ∈/ L are held ﬁxed. This LP can be described as:

∀v ∈ V

x(e) ≤ 1 −

x(f) (8)

e∈L∩N(v)

f∈N(v)\L

where we emphasize that the terms on the RHS are viewed as ﬁxed constants.

If v ∈/ B, then the constraint (8) is not tight. If v ∈ B \ B(L), then the LHS of (8) is zero. Thus, when restricting our attention to the variables x(e) for e ∈ L, the LP has at most one tight non-trivial constraint for each v ∈ B(L). Since we are assuming that x(e) ∈ (0,1) for all e, it has a fractional variable for each e ∈ L. Since x is a basic LP solution, the number of fractional variables |L| is at most the number of tight constraints |B(L)|.

![image 125](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile125.png>)

![image 126](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile126.png>)

![image 127](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile127.png>)

![image 128](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile128.png>)

- Proposition 2.9. If a basic fractional matching x is stuck for g, then H has no singleton edges.

Proof. Suppose that e = {v} is such an edge. On the other hand, since x is a fractional matching, we have f∈N(v) x(f) ≤ 1. Since N(e) = N(v) \ {e}, this implies

f∈N(e)

g(f)x(f) =

f∈N(v)\{e}

g(f)x(f) ≤

f∈N(v)\{e}

x(f) ≤ 1 − x(e) ≤ 1 − g(e)x(e),

a contradiction.

![image 129](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile129.png>)

![image 130](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile130.png>)

![image 131](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile131.png>)

![image 132](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile132.png>)

- Proposition 2.10. If g is not good for H, then there is some non-empty subgraph H′ = (V,E′) with a reduced basic fractional matching x which is stuck for g.


Proof. Suppose that E′ ⊆ E has minimal size such that some basic fractional matching x on hypergraph H′ = (V,E′) is stuck for g and E′ is non-empty. We claim that N(e) = ∅ for all e ∈ E′. For, if N(e) = ∅, then edge e would satisfy

0 =

g(f)x(f) > 1 − g(e)x(e),

f∈N(e)

which is a contradiction since the RHS is non-negative.

So we may assume that |E′| > 1. We claim now that x is reduced. For, suppose that x(e) = 0 for some edge e. If we deﬁne the non-empty edge set E′′ = E′ \{e}, we see that every edge e′′ ∈ E′′ still satisﬁes

g(f)x(f) > 1 − g(e)x(e′′).

g(f)x(f) =

f∈E′′∩N(e′′)

f∈E′∩N(e′′)

Thus, the restriction of x to H′′ = (V,E′′) is also stuck. This contradicts minimality of E′.

Finally, suppose that x(e) = 1 for some edge e. Since N(e) = ∅, there must be some edge e′ ∈ N(e); but then necessarily x(e′) = 0, which we have already ruled out.

![image 133](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile133.png>)

![image 134](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile134.png>)

![image 135](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile135.png>)

![image 136](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile136.png>)

# 3 Bounds for bi-uniform hypergraphs

Let us consider a hypergraph H with a reduced basic fractional matching x where all edges have sizes k,ℓ where k < ℓ. We use discount factors given by

g(e) =

- p for |e| = k
- q for |e| = ℓ


for values p,q. We may assume p ≥ q as k < ℓ. Most of the steps in the argument hold more generally for arbitrary edge sizes; we later specialize to k = 2,p = h∗(2) = 2/3,ℓ = 3,q = h∗(3) = 3/7 to obtain Theorem 2.5.

For any edge e and any integer i ∈ {k,ℓ} we deﬁne ai(e) =

x(f).

f∈Ni(e)

We will adopt the following notation throughout this section: we use e to denote a k-edge and f to denote a ℓ-edge. For a vertex v, let x(v) denote the total x-value of edges containing v. We begin with the following upper bounds on x(e) and x(f).

- Proposition 3.1. If x is stuck for g, then all edges e ∈ Ek,f ∈ Eℓ satisfy


kp − 1 − (p − q)aℓ(e) (k − 1)p

x(e) <

![image 137](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile137.png>)

ℓq − 1 + (p − q)ak(f) (ℓ − 1)q

and x(f) <

.

![image 138](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile138.png>)

Proof. The condition (5) for x being stuck implies that

1 − pak(e) − qaℓ(e) < px(e) ∀e ∈ Ek and 1 − pak(f) − qaℓ(f) < qx(f) ∀f ∈ Eℓ. As the total x-value for each vertex is at most 1, we have the bounds:

ak(e) + aℓ(e) ≤ k(1 − x(e)) ∀e ∈ Ek and ak(f) + aℓ(f) ≤ ℓ(1 − x(f)) ∀f ∈ Eℓ.

Eliminating aℓ(f) from the inequalities for f, and eliminating ak(e) from the inequalities for e gives the two claimed bounds.

![image 139](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile139.png>)

![image 140](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile140.png>)

![image 141](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile141.png>)

![image 142](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile142.png>)

For an ℓ-edge f, let nk(f) = |Nk(f)| denote the number of k-edges (possibly zero) incident to f. Then Proposition 3.1 above implies the following upper bound on x(f) in terms of nk(f). Proposition 3.2. If x is stuck for g, then for any f ∈ Eℓ,

(p − q)2 (k − 1)(ℓ − 1)pq

x(f) 1 + nk(f)

![image 143](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile143.png>)

ℓq − 1 (ℓ − 1)q

(kp − 1)(p − q) (k − 1)(ℓ − 1)pq

<

+ nk(f)

.

![image 144](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile144.png>)

![image 145](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile145.png>)

Proof. Consider any k-edge e incident to f. Then by the bound on x(e) in Proposition 3.1,

kp − 1 − (p − q)x(f) (k − 1)p

x(e) <

,

![image 146](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile146.png>)

where we use that aℓ(e) ≥ x(f) as f is adjacent to e (and that p ≥ q). As this holds for every e ∈ Nk(f), we get

kp − 1 − (p − q)x(f) (k − 1)p

.

ak(f) =

x(e) < nk(f)

![image 147](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile147.png>)

e∈N(f)

If we substitute this upper bound for ak(f) into the bound of Proposition 3.1 for x(f), we get x(f) <

ℓq − 1 (ℓ − 1)q

p − q (ℓ − 1)q

kp − 1 − (p − q)x(f) (k − 1)p which, upon rearranging, is equivalent to the stated inequality.

· nk(f)

+

![image 148](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile148.png>)

![image 149](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile149.png>)

![image 150](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile150.png>)

![image 151](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile151.png>)

![image 152](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile152.png>)

![image 153](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile153.png>)

![image 154](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile154.png>)

Let us now consider the sum S =

(kx(e) − 1) +

(ℓx(f) − 1).

e∈Ek

f∈Eℓ

Our strategy is to show upper and lower bounds for S, under the assumption that x is basic, reduced, and stuck for g. We then argue that these bounds are contradictory, and hence the desired matching exists. We show the lower bound and upper bound on S in turn.

Lower bound. First, as x(v) ≤ 1 for any vertex v, and

- Proposition 2.8 gives


kx(e) +

ℓx(f) =

e∈Ek

f∈Eℓ

v

x(v),

x(v) − |E| ≥

S =

v∈V

x(v) − |E| = |B| − |E| ≥ 0. (9)

v∈B

Upper bound. By the bound on x(e) in Proposition 3.1, we have S ≤

k2p − k (k − 1)p

k(p − q) (k − 1)p

− 1 −

(ℓx(f) − 1).

aℓ(e) +

![image 155](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile155.png>)

![image 156](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile156.png>)

e∈Ek

f∈Eℓ

Writing

this gives

x(f) =

aℓ(e) =

e∈Ek

e∈Ek f∈Nℓ(e)

S ≤

e∈Ek

k2p − k (k − 1)p

− 1 +

![image 157](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile157.png>)

x(f)

1 =

f∈Eℓ

e∈Nk(f)

x(f)nk(f),

f∈Eℓ

f∈Eℓ

k(p − q) (k − 1)p

ℓ − nk(f)

![image 158](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile158.png>)

x(f) − 1 . (10)

Putting together the bounds on S, we can now conclude our desired contradiction as follows.

Lemma 3.3. Let T = p((pk−−q1))kℓ. Suppose that p ≤ h∗(k) and for every integer n ∈ {0,... ,⌊T⌋} it holds that

![image 159](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile159.png>)

pq(k − 1)(ℓ − 1) + n(p − q)2 p(k − 1)ℓ − kn(p − q)

p(k − 1)(qℓ − 1) + n(p − q)(pk − 1) p(k − 1)

≥

(11)

![image 160](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile160.png>)

![image 161](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile161.png>)

Then, there cannot be a reduced basic fractional matching x which is stuck for g.

Proof. If we examine upper bound (10), we see that the term (kk2−p−1)kp − 1 is non-positive since p ≤ h∗(k). We also must have S ≥ 0 from (9). Now, if Eℓ = ∅ (and there are no summands f), then in fact H is a k-uniform hypergraph. We have already shown that x cannot be stuck in this case since p ≤ h∗(k). So, there must be an edge f ∈ Eℓ for which the corresponding summand in (10) is non-negative. For this edge f, let us denote n = nk(f), i.e.

![image 162](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile162.png>)

k(p − q) (k − 1)p

x(f) − 1 ≥ 0. (12) Since x(f) ≥ 0, we clearly must have

(ℓ − n

![image 163](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile163.png>)

p(k − 1)ℓ (p − q)k

n ≤

= T, and then (12) is equivalent to

![image 164](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile164.png>)

p(k − 1) p(k − 1)ℓ − (p − q)kn

x(f) ≥

. Substituting this lower bound for x(f) into the bound of Proposition 3.2, we conclude

![image 165](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile165.png>)

p(k − 1) p(k − 1)ℓ − (p − q)kn

![image 166](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile166.png>)

(p − q)2 (k − 1)(ℓ − 1)pq

1 + n

![image 167](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile167.png>)

ℓq − 1 (ℓ − 1)q

<

![image 168](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile168.png>)

(kp − 1)(p − q) (k − 1)(ℓ − 1)pq

+ n

. (13)

![image 169](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile169.png>)

With some algebraic simpliﬁcations, this inequality is precisely what is ruled out by (11) for the given value n.

![image 170](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile170.png>)

![image 171](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile171.png>)

![image 172](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile172.png>)

![image 173](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile173.png>)

Proof of Theorem 2.5. Now, let H = (V,E) be a rank-3 hypergraph. Assume for contradiction that Theorem 2.5 fails for H. Then by Proposition 2.10 there is a subgraph H′ of H with a reduced basic fractional matching x stuck for g. The subgraph H′ also has rank at most 3, and by

- Proposition 2.9 has no singleton edges. Thus, H′ is a bi-uniform hypergraph with k = 2,ℓ = 3.


Now consider Lemma 3.3 for our desired bounds for p = h∗(k) = 2/3 and q = h∗(ℓ) = 3/7. The condition p ≤ h∗(k) is obviously satisﬁed. Here, T = 4.2, and we just need to verify (11) at the values n = 0,1,2,3,4, which is easily done. This shows Theorem 2.5.

(Note that (11) is false for some non-integer values n in the relevant range, in particular, is it false for n ∈ (0,0.8).)

Other edge sizes. We cannot show Conjecture 2.4 for other values of k,ℓ. Nonetheless, if we set p = h∗(k), we can still obtain non-trivial bounds on q. For instance, for ℓ = k + 1, we have the following crisp estimate:

- Theorem 3.4. If ℓ = k + 1, then no basic fractional matching x can be stuck with


1 k + 1/k

1 k − 1 + 1/k

p = h∗(k) =

, q =

.

![image 174](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile174.png>)

![image 175](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile175.png>)

Note that this q is quite close to h∗(k + 1) = k+1/1(k−1). In particular, h∗(k + 1) − q = k−4 + O(k−5).

![image 176](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile176.png>)

Proof. Plugging the bounds for p and q into Lemma 3.3 gives T = k4k−21. It can be routinely checked that (11) holds for all real numbers n ∈ [0,T]. For example, it is a rational inequality that can be

![image 177](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile177.png>)

veriﬁed using an algorithm for decidability of real-closed ﬁelds. We used Mathematica’s Reduce command to check this.

![image 178](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile178.png>)

![image 179](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile179.png>)

![image 180](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile180.png>)

![image 181](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile181.png>)

The proof of Theorem 3.4 did not use the integrality of n, which was critical in proving Theorem 2.5. For ﬁxed values k,ℓ, we can obtain better bounds compared to Theorem 3.4. For example, for k = 3, ℓ = 4, we can set p = h∗(3) = 3/7 and numerically optimize q to satisfy Lemma 3.3 (trying all possible integer values of n) to obtain q = 0.30508; by contrast, Theorem 3.4 would give p = h∗(3),q = 0.3. Similarly, for k = 4,ℓ = 5, we can set p = h∗(4) = 4/13, and q = 0.23656; by contrast, Theorem 3.4 gives p = h∗(4), and q = 0.23529.

# 4 Proof of Theorem 2.6

Recall here that we are setting g(e) = h(|e|) where h satisﬁes the bounds (A1), (A2), (A3). Throughout this section, we assume for contradiction that H is a minimal counter-example, i.e., H is non-empty and there is a basic fractional matching x of H which is stuck for g.

In light of Proposition 2.10, we assume that x is reduced. By Proposition 2.9, H then has no singleton edges, and so let k ≥ 2 be the size of the smallest edge in E.

We deﬁne p = h(k),q = h(k + 1). By properties (A1), (A2), (A3), we have that

1 k − 1 + 1/k

q ≤ 1 − (k − 1)p, 0 ≤ q ≤ p ≤

. (14)

![image 182](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile182.png>)

Let us write E>k,N>k(v),N>k(e) to denote the respective sets of edges with strictly more than k vertices. Let V ′ denote the set of vertices v with Nk(v) = ∅. We also deﬁne B′ = B(Ek) = B ∩V ′ and nk(v) = |Nk(v)| ≥ 1 for all v ∈ V ′. For each vertex v and edge e, deﬁne

y(v) =

x(f), y(e) =

f∈N>k(v)

|f ∩ e|x(f),

y(v) =

v∈e

f∈N>k(e)

so that y(v) is the x-value of the edges containing v which have size strictly larger than k, and y(e) is the sum of y(v) over all v ∈ e.

Consider the sum

S =

x(e).

e∈Ek

Our strategy is to compute upper and lower bounds on S. We then combine them and argue that they cannot both hold simultaneously, and hence the counter-example H is impossible.

Lower bound. This is straightforward. As each edge in Ek has cardinality exactly k and all its vertices are in V ′, we can use double-counting to get:

1 k v∈V ′

1 k v∈B′

x(e) ≥

(1 − y(v))/k. (15)

S =

x(e) =

![image 183](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile183.png>)

![image 184](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile184.png>)

v∈B′

e∈Nk(v)

e∈Nk(v)

Upper bound. First, we claim that every edge e ∈ Ek satisﬁes

x(e) < (kp − 1 − (p − q)y(e))/(p(k − 1)). (16) To show this, note that since x is stuck, the condition (5) and the fact that g(e) = p implies

1 − px(e) <

g(f)x(f) ≤ p

x(f) + q

x(f)

f∈N(e)

f∈Nk(e)

f∈N>k(e)

≤ p

|f ∩ e|x(f) + q

|f ∩ e|x(f)

f∈Nk(e)

f∈N>k(e)

≤ p(k − kx(e) − y(e)) + qy(e),

where the second inequality uses that q = h(k + 1) ≥ g(f) for all f ∈ N>k(e). (16) then follows upon rearranging the above inequality.

We then sum inequality (16) over the edges e ∈ Ek to obtain:

|Ek|(kp − 1) − (p − q) e∈E

y(e) p(k − 1)

kp − 1 − (p − q)y(e) p(k − 1)

k

=

S <

![image 185](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile185.png>)

![image 186](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile186.png>)

e∈Ek

|Ek|(kp − 1) − (p − q) e∈E

k v∈e y(v) p(k − 1)

|Ek|(kp − 1) − (p − q) v∈V ′ y(v)nk(v) p(k − 1)

=

=

.

![image 187](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile187.png>)

![image 188](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile188.png>)

By Proposition 2.8 we have |Ek| ≤ |B′|. Noting that p−q ≥ 0,p ≥ 1/k and B′ ⊆ V ′, we thus have:

|B′|(kp − 1) − (p − q) v∈B′ y(v)nk(v) p(k − 1)

S <

=

![image 189](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile189.png>)

kp − 1 − y(v)nk(v)(p − q) p(k − 1)

. (17)

![image 190](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile190.png>)

v∈B′

Putting them together. We now combine the upper bound inequality (17) with the lower bound inequality (15) to get:

(1 − y(v))/k ≤ S <

v∈B′

v∈B′

kp − 1 − y(v)nk(v)(p − q) p(k − 1)

.

![image 191](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile191.png>)

In particular, one of the summands on the LHS must be smaller than the corresponding summand on the RHS. Thus, there must exist some vertex v ∈ B′ with

1 − y(v) < k

kp − 1 − y(v)nk(v)(p − q) p(k − 1)

![image 192](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile192.png>)

. (18)

Since v ∈ B′, we have nk(v) ≥ 1. Also, the ﬁrst condition in (14) implies p−q ≥ kp−1 ≥ 0. Thus, the right side above is at most

k(kp − 1) p(k − 1)

1 − y(v)

. (19)

![image 193](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile193.png>)

The second condition in (14) is equivalent to kp((kpk−−1)1) ≤ 1; thus, (19) is at most 1 −y(v). Thus, this is a contradiction to the existence of H, completing the proof of Theorem 2.6.

![image 194](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile194.png>)

# 5 Acknowledgments

Thanks to Rico Zenklusen for some helpful explanations about their paper [1]. Thanks to the journal reviewers for useful suggestions and revisions.

# A Proof of Corollary 2.7

- Proposition A.1. For any value r, let us extend the deﬁnition of function hr by setting


hr(k) =

i+1(k−2)!

(−1)r−k(k−2)!

(r−2)!(r+1/r−1) + i r=1−k (−1)

(k−2+i)! if 2 ≤ k ≤ r 0 if k > r

![image 195](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile195.png>)

![image 196](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile196.png>)

This function hr satisﬁes properties (A1)–(A3).

Proof. Let us ﬁx r and write h = hr for brevity. Properties (A1)–(A3) can be easily checked for k ≥ r (noting that h(r) = r−1+11 /r). We claim that (A3) holds with equality k = 2,... ,r − 1, i.e.,

![image 197](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile197.png>)

h(k + 1) = 1 − (k − 1)h(k). (20)

To verify this, we calculate

r−k−1

(−1)i+1(k + 1 − 2)! (k + 1 − 2 + i)!

(−1)r−(k+1)((k + 1 − 2)! (r − 2)!(r + 1/r − 1)

h(k + 1) + h(k)(k − 1) =

+

![image 198](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile198.png>)

![image 199](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile199.png>)

i=1

r−k

(−1)i+1(k − 2)! (k − 2 + i)!

(−1)r−k(k − 1)(k − 2)! (r − 2)!(r + 1/r − 1)

+ (k − 1)

+

![image 200](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile200.png>)

![image 201](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile201.png>)

i=1

r−k

r−k−1

(−1)i+1(k − 2)! (k − 2 + i)!

(−1)i+1(k + 1 − 2)! (k + 1 − 2 + i)!

+ (k − 1)

=

![image 202](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile202.png>)

![image 203](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile203.png>)

i=1

i=1

r−k−1

r−k−1

(−1)j(k − 1)! (k − 1 + j)!

(−1)i+1(k − 1)! (k − 1 + i)!

substituting j = i − 1

+

=

![image 204](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile204.png>)

![image 205](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile205.png>)

j=0

i=1

r−k−1

=

i=1

(−1)i+1(k − 1)! + (−1)i(k − 1)! (k − 1 + i)!

![image 206](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile206.png>)

(−1)0(k − 1)! (k − 1 + 0)!

+

= 1,

![image 207](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile207.png>)

where the second equality follows as the ﬁrst and third terms in the ﬁrst equality cancel.

We now turn to verifying property (A2) for k = 2,... ,r − 1. To do so, we show the stronger inequality for k ≤ r:

1 k

1 k − 1 + 1/k

≤ h(k) ≤

. (21)

![image 208](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile208.png>)

![image 209](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile209.png>)

We show (21) by induction on k. The base case k = r is clear since h(r) = r−1+11 /r, . For

![image 210](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile210.png>)

the induction step, note that by (20) we have h(k) = 1−(hk−(k1)+1). By the induction hypothesis, this implies

![image 211](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile211.png>)

1 − k+1/1(k+1) k − 1

1 − k+11 k − 1

![image 212](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile212.png>)

![image 213](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile213.png>)

≤ h(k) ≤

. Now observe that

![image 214](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile214.png>)

![image 215](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile215.png>)

1 − k+1/1(k+1) k − 1

1 k

![image 216](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile216.png>)

≥

![image 217](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile217.png>)

![image 218](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile218.png>)

and

1 − k+11 k − 1

![image 219](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile219.png>)

≤

![image 220](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile220.png>)

1 k − 1 + 1/k

![image 221](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile221.png>)

for k ≥ 2,

which concludes the proof of property (A2).

Finally, for property (A1), we need to show that h(k + 1) ≤ h(k); by (20), it suﬃces to show that 1 − h(k)(k − 1) ≤ h(k), which holds since h(k) ≥ 1/k.

![image 222](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile222.png>)

![image 223](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile223.png>)

![image 224](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile224.png>)

![image 225](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile225.png>)

- Proposition A.2. The function h = h∞ satisﬁes properties (A1)–(A3).


Proof. For any value k, the sum deﬁning h∞(k) is an alternating series whose terms decrease monotonically, hence h∞(k) = limr→∞ hr(k). Properties (A1)–(A3) are deﬁned in terms of nonstrict inequalities; since each hr(k) individually satisﬁes these properties, by continuity their limit satisﬁes them as well.

![image 226](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile226.png>)

![image 227](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile227.png>)

![image 228](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile228.png>)

![image 229](<2020-bansal-some-remarks-hypergraph-matching_images/imageFile229.png>)

Propositions A.1 and A.2, combined with Theorem 2.6, imply Corollary 2.7 parts (1) and (2). To show Corollary 2.7 part (3), observe that h˜∞(k) ≤ h∞(k) for all k.

# References

- [1] Anegg, G., Angelidakis, H., Zenklusen, R.: Simpler and stronger approaches for non-uniform hypergraph matching and the Fu¨redi, Kahn, and Seymour conjecture. Proc. 4th SIAM Symposium on Simplicity in Algorithm (SOSA), pp. 196-203 (2021)
- [2] Bansal, N., Gupta, A., Li, J., Mestre, J., Nagarajan, V., Rudra, A: When LP is the cure for your matching woes: improved bounds for stochastic matchings. Algorithmica 63(4), pp. 733–762 (2012)
- [3] Bar-Yehuda, R., Bendel, K., and Freund, A., Rawitz, D.: Local ratio: a uniﬁed framework for approxmation algorithms. ACM Computing Surveys 36(4), pp. 422–463 (2004)
- [4] Brubach, B., Sankararaman, K. A., Srinivasan A., Xu, P.: Algorithms to approximate columnsparse packing problems. ACM Transactions on Algorithms 16(1), Article #10 (2020)
- [5] Bruggmann, S., Zenklusen, R.: An optimal monotone contention resolution scheme for bipartite matchings via a polyhedral viewpoint. Mathematical Programming 191(2), pp. 795–845 (2022)
- [6] Chan, Y., Lau, L.: On linear and semideﬁnite programming relaxations for hypergraph matching. Mathematical Programming 135(1-2), pp. 123–148 (2012)
- [7] Fu¨redi, Z., Kahn, J., Seymour, P.: On the fractional matching polytope of a hypergraph. Combinatorica 13(2), pp. 167–180 (1993)
- [8] Kahn, V.: Maximum bounded 3-dimensional matching is MAX SNP-complete. Information Processing Letters 37(1), pp. 27–35 (1991)


