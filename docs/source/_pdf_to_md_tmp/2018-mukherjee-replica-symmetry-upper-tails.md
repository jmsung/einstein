arXiv:1812.09841v3[math.PR]31Mar2019

REPLICA SYMMETRY IN UPPER TAILS OF MEAN-FIELD HYPERGRAPHS

SOMABHA MUKHERJEE AND BHASWAR B. BHATTACHARYA

Abstract. Given a sequence of s-uniform hypergraphs {Hn}n≥1, denote by Tp(Hn) the number of edges in the random induced hypergraph obtained by including every vertex in Hn independently with probability p ∈ (0, 1). Recent advances in the large deviations of low complexity non-linear functions of independent Bernoulli variables can be used to show that tail probabilities of Tp(Hn) are precisely approximated by the so-called ‘mean-ﬁeld’ variational problem, under certain assumptions on the sequence {Hn}n≥1. In this paper, we study properties of this variational problem for the upper tail of Tp(Hn), assuming that the mean-ﬁeld approximation holds. In particular, we show that the variational problem has a universal replica symmetric phase (where it is uniquely minimized by a constant function), for any sequence of regular s-uniform hypergraphs, which depends only on s. We also analyze the associated variational problem for the related problem of estimating subgraph frequencies in a converging sequence of dense graphs. Here, the variational problems themselves have a limit which can be expressed in terms of the limiting graphon.

1. Introduction

Given a s-uniform hypergraph H = (V (H),E(H)) with vertex set V (H) and hyperedge set E(H) (which is a collection of s-element subsets of V (H)) and p ∈ (0,1) ﬁxed, construct a random sub-hypergraph of H as follows: sample each vertex in V (H) with probability p and consider the induced sub-hypergraph of H on the set of sampled vertices. Denote by Tp(H) the number of edges in this random sub-hypergraph, which can be written, more formally, as

Tp(H) :=

Xv, (1.1)

e∈E(H) v∈e

where X1,X2,... ,X|V (H)| are i.i.d. Ber(p). (Note that E(Tp(H)) = |E(H)|ps.) Numerous celebrated problems in combinatorial probability can be re-formulated in terms of (1.1), for some choice of H.

- (1) Subgraphs in Erdo˝s-Re´nyi random graphs: The number of copies of a ﬁxed graph F = (V (F),E(F)) in the Erd˝os-Re´nyi random graph G(n,p) can be formulated in terms of (1.1) as follows: Consider the hypergraph Hn(F) (to be referred to as the F-counting hypergraph) with vertex set of Hn(F) as the edge set of the complete graph Kn, and edge set of Hn(F) as the collection of the edge sets of all copies of F in Kn. Then Hn(F) is a |E(F)|-uniform regular hypergraph1 and Tp(Hn(F)) is precisely the number of copies of F in G(n,p).
- (2) Arithmetic progressions in a random set: Given r ≥ 1, deﬁne the r-AP counting hypergraph Hn(r) as the hypergraph with vertex set [n] := {1,2,... ,n} and edge set the set of all r term arithmetic progressions in [n]. Then Tp(Hn(r)) is the number of r-term arithmetic progressions in a random subset of [n], where every element is included in the subset independently with probability p.


![image 1](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile1.png>)

1A hypergraph H = (V (H),E(H)) is said to be d-regular if every vertex v ∈ V (H) is incident on exactly d hyperedges in E(H).

1

(3) Estimating motif frequencies in large graphs: Eﬃciently counting motifs in a large graph such as the number of edges or triangles (more generally, subgraph counts) is an important statistical and computational problem [21]. One natural strategy to reduce storage and computational costs is to randomly sample subsets of vertices, where natural estimates of subgraph counts are often of the form (1.1) above (see Section 1.2 for details).

Concentration inequalities for Tp(Hn), for a sequence of hypergraphs {Hn}n≥1, are well-known (see [18, 27] and the references therein). In this paper, we study the precise large deviations upper tail probabilities of Tp(Hn), in the ﬁxed p ∈ (0,1) regime, which involves determining the exact asymptotics of

log P(Tp(Hn) ≥ rs|E(Hn)|), for 0 < p < r < 1. (1.2) Note that Tp(Hn) is a random multi-linear polynomial indexed by Hn, and establishing its upper tail asymptotics falls in the framework of non-linear large deviations, introduced in the seminal paper of Chatterjee and Dembo [12]. Here, they studied the large deviations of a general random function f(X1,X2,... ,Xn), where f : {0,1}n → R and X1,X2,... ,Xn are i.i.d. Ber(p), and came up with a notion of complexity of the gradient of the function (along with additional smoothness properties), under which the tail probabilities of f(X1,X2,... ,Xn) (and the associated Gibbs measure on {0,1}n) can be well-approximated by the so-called ‘mean-ﬁeld’ variational problem, which is an entropic variational problem over the set of product measures on the hypercube {0,1}n. Thereafter, Eldan [17] obtained an improved set of conditions, which involved computing the Gaussian width of the gradient of the function, under which the above reduction holds. Similar results for Gibbs measures beyond the hypercube were obtained by [4, 28], and recently by Austin [2] for very general product spaces.

These results can be used to obtain various suﬃcient conditions on a sequence of hypergraphs

{Hn}n≥1 for which the probability in (1.2) can be approximated by the corresponding mean-ﬁeld variational problem. This motivates the following abstract deﬁnition:

- Deﬁnition 1.1. (Mean-ﬁeld hypergraphs) Given a s-uniform hypergraph H and p ∈ (0,1), the upper-tail mean ﬁeld variational problem for Tp(H) is deﬁned as:


 

 

|V (H)|

1 |V (H)|

Ip(xv) : t(H,x) ≥ rs|E(H)|

φH(r,p) = inf

, (1.3)

![image 2](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile2.png>)

x∈[0,1]|V (H)|





v=1

where

- – 0 < p < r < 1,
- – Ip(x) = xlog xp + (1 − x)log 11−−xp, is the relative entropy of Ber(x) with respect to Ber(p); and

![image 3](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile3.png>)

![image 4](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile4.png>)

- – t(H,x) = e∈E(H) v∈e xv, for x = x1,... ,x|V (H)| ∈ [0,1]|V (H)|.


Moreover, a sequence {Hn}n≥1 of s-uniform hypergraphs is said to be mean-ﬁeld (for the upper tail problem) if

1

|V(Hn)| log P(Tp(Hn) ≥ rs|E(Hn)|) −φHn(r,p)

![image 5](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile5.png>)

= 1, (1.4) for all 0 < p < r < 1.

lim

![image 6](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile6.png>)

n→∞

The mean-ﬁeld condition has been established for several natural hypergraph sequences. For example, it follows from results in the landmark paper of Chatterjee and Varadhan [14], that

for any ﬁxed graph F, the F-counting hypergraph Hn(F) deﬁned above is mean-ﬁeld. In this case, the associated variational problems {φHn(F)(r,p)}n≥1 themselves have a limit, which can be expressed as an optimization problem in the space of graphons (the continuum limit of graphs [22]). Lubetzky and Zhao [23] analyzed these variational problems, and identiﬁed the precise region of replica symmetry (set of all points (p,r) where the optimization problem is uniquely minimized by the constant function r) for regular graphs F. The validity of (1.4) for the number of arithmetic progressions in a random set, and properties of the associated variational problem was established in [8]. Recently, Dembo and Lubetzky [16] derived the large deviations for subgraph counts in the uniform random graph model G(n,m) (the uniform distribution over graphs with n vertices and m edges). Here, the variational problem in the rate function coincide with those studied in statistical physics in the context of constrained random graphs, where symmetry breaking conﬁgurations are often attained by block (‘multi-podal’) graphons (see [19, 20, 25] and the references therein).

For a general hypergraph sequence the results in [12, 17] can be applied to obtain diﬀerent suﬃcient conditions on {Hn}n≥1 for which the approximation 1.4 holds. For instance, Brie¨t and Gopi [11] computed the Gaussian-width a general multilinear polynomial, which combined with [17, Theorem 5] gives the following suﬃcient condition for a sequence of s-uniform hypergraphs {Hn}n≥1 to be mean-ﬁeld:2

|E(Hn)| |V (Hn)|

and ∆1(Hn) = O |E(Hn)| |V (Hn)|

, (1.5)

∆2(Hn) ≪

![image 7](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile7.png>)

![image 8](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile8.png>)

2− 1

![image 9](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile9.png>)

2⌈ s−1

![image 10](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile10.png>)

2 ⌉ log |V (H)|

![image 11](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile11.png>)

where ∆1(Hn) and ∆2(Hn) are the maximum degree and the maximum co-degree of Hn, respectively.3 These assumptions are satisﬁed for a variety of hypergraphs, from dense s-uniform hypergraphs (where E(Hn) = Θ(|V (Hn)|s)) to much sparser hypergraphs such as the r-AP counting hypergraph (where E(Hn) = Θ(|V (Hn)|2). The condition in (1.5) can be signiﬁcantly improved for graphs (2-uniform hypergraphs), where the mean-ﬁeld condition has been extensively studied and well-understood [4, 17]. In this case, a suﬃcient condition for sequence of graphs {Gn}n≥1 to be mean-ﬁeld is

|E(Gn)| ≫ |V (Gn)| and ∆1(Gn) = O |E(Gn)| |V (Gn)|

, (1.6)

![image 12](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile12.png>)

that is, the graph Gn is not ‘too sparse’ (number of edges is much larger than the number of vertices) and not ‘too irregular’ (maximum degree is of the same order as the average degree). In the appendix (Proposition A.1), we show that

|E(Hn)| ≫ |V (Hn)|s−1 and ∆1(Hn) = O |E(Hn)| |V (Hn)|

, (1.7)

![image 13](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile13.png>)

is another simple suﬃcient condition for a sequence of s-uniform hypergraphs to be mean-ﬁeld for the upper tail problem. The conditions in (1.5) and (1.7) are, in general, incomparable. However,

![image 14](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile14.png>)

- 2The ﬁrst condition in (1.5) controls the Gaussian width of the gradient of the function x → t(H,x) [11, Corollary 6.1], while the second condition controls the Lipschitz constant. To verify the mean-ﬁeld condition using [17, Theorem 5], one also needs to check a few technical conditions related to the continuity of the variational problem, all of which can be easily veriﬁed when (1.5) holds.
- 3For a s-uniform hypergraph H, the degree of a vertex v ∈ V (H) (to be denoted by dH(v)) is the number of hyperedges in H containing v, and the maximum degree ∆1(H) := maxv∈V(H) dH(v). Similarly, for u, v ∈ H, the co-degree of u, v (denoted by dH(u, v)) is the number of hyperedges in H containing both u and v, and the maximum co-degree ∆2(H) := maxu,v∈V(H) dH(u, v).


there are cases where (1.7) improves upon (1.5) (see Example 3 in Appendix A). Moreover, (1.7) recovers the condition for graphs (1.6) as a special case.

- Remark 1.1. In the approximation (1.4) one can often allow the sparsity parameter p = p(n), to go to zero with n, at appropriate rates. Determining the optimal dependence on the sparsity parameter for a speciﬁc sequence of hypergraphs is, in general, a challenging problem. For example, for upper tails of subgraphs in the Erd˝os-Re´nyi random graph G(n,p), Chatterjee and Dembo [12, Theorem 1.2] established the validity of (1.4), using their notion of gradient complexity, for certain regimes of the sparsity parameter p. The dependence on p was later improved by Eldan [17], and, very recently, Cook and Dembo [15] and Augeri [1], independently and simultaneously, established (1.4) for cycle counts in G(n,p), under almost optimal sparsity conditions. The associated variational problems in the sparse regime was precisely analyzed in [7, 24].


In this paper, we study asymptotic properties of the variational problem (1.3) for a sequence suniform hypergraphs {Hn}n≥1 in the ﬁxed p ∈ (0,1) regime, assuming the mean-ﬁeld approximation (1.4) holds. The following is the summary of our results:

- (1) In the ﬁxed p regime, it is notoriously diﬃcult to solve the variational problem (1.3) explicitly for a general sequence of hypergraphs. Instead, one searches for the region of replica

symmetry, that is, the set of (p,r) for which the variational problem φHn(p,r) is uniquely minimized by the constant vector (r,r,... ,r) ∈ (0,1)|V (Hn)| (recall 0 < p < r < 1). We show in Theorem 1.1 that any sequence of regular s-uniform hypergraphs has a (universal) region of replica symmetry, which depends only on s, but not on the speciﬁc choice of the hypergraphs. Moreover, in a sense to be made precise below, the replica symmetry region we identify for regular s-uniform hypergraphs is tight.

- (2) We also analyze the variational problem arising in the motif frequency estimation problem, for a converging sequence of dense graphs (Section 1.2). In this case, the variational problems themselves have a limit which can be expressed, using the limiting graphon, as an optimization problem over the space of functions from [0,1] → [0,1] (Theorem 1.2), giving the exact Bahadur slope [3] of the corresponding estimate.


- 1.1. Replica Symmetry for Regular Hypergraphs. We begin with the following theorem, which identiﬁes the precise region of universal replica symmetry for regular s-uniform hypergraphs. To this end, recall the deﬁnition of the mean-ﬁeld variational problem φH(r,p) from (1.3).


- Theorem 1.1. Fix 0 < p < r < 1. Then the following hold:


- (a) (Replica Symmetry) Suppose {Hn}n≥1 is a sequence of regular s-uniform hypergraphs. If the point (rs,Ip(r)) lies on the convex minorant of the function x  → Ip(x1s), then φHn(r,p) = Ip(r). Moreover, if {Hn}n≥1 is a sequence of mean-ﬁeld, regular s-uniform hypergraphs, then

![image 15](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile15.png>)

lim

n→∞

1 |V (Hn)|

![image 16](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile16.png>)

log P Tp(Hn) ≥ rs E(Tp(Hn)) = −Ip(r).

- (b) (Replica Symmetry Breaking) If the point (rs,Ip(r)) does not lie on the convex minorant of x  → Ip(x1s), then there exists a sequence of mean-ﬁeld, regular s-uniform hypergraphs {Hn}n≥1 (depending on p and r) such that φHn(r,p) < Ip(r), and


![image 17](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile17.png>)

1 |V (Hn)|

log P Tp(Hn) ≥ rs E(Tp(Hn)) > −Ip(r).

liminf

![image 18](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile18.png>)

n→∞

The proof of this theorem is given in Section 2. It shows that the variational problem (1.3) has a region of replica symmetry for any regular s-uniform hypergraph, which is determined by the

convex minorant of the function x → Ip(x1s), and this region is tight over the class of all regular s-uniform hypergraphs: For a regular s-uniform hypergraph H denote by

![image 19](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile19.png>)

R(H) := {(p,r) : 0 < p < r < 1 and φH(r,p) = Ip(r)}, (1.8) the set of all points where replica symmetry is preserved. Then the theorem above can be re-stated as:

R(H) = Cs,

H∈Hs

where Hs is the collection of all regular s-uniform hypergraphs and Cs is the set of all (p,r) such that 0 < p < r < 1 and (rs,Ip(r)) lies on the convex minorant of the function x → Ip(x1s).4 On the other hand, in Example 2, we construct a sequence of irregular graphs which exhibit symmetry breaking everywhere, showing that the regularity assumption on the hypergraphs in Theorem 1.1 is necessary for obtaining a universal region of symmetry.

![image 20](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile20.png>)

- Remark 1.2. For a speciﬁc sequence of hypergraphs the region of replica symmetry might be


larger. For instance, if Hn is the sequence of complete s-uniform hypergraph on n vertices, it is easy to check that replica symmetry is preserved for all 0 < p < r < 1. Another example is the replica symmetry region in the upper tails of subgraphs in the Erd˝os-Renyi random graph G(n,p). To this end, given a ﬁxed connected graph F = (V (F),E(F)), recall the deﬁnition of the F-counting hypergraph Hn(F) from above: the vertex set of Hn(F) is the edge set of the complete graph Kn, and the edge set of Hn(F) is the collection of the edge sets of all copies of F in Kn. Then Tp(Hn(F)) = N(F,G(n,p)), the number of copies of F in G(n,p). Lubetzky and Zhao [23] studied the replica symmetry region in the upper tail variational problem for N(F,G(n,p)). It follows from their results that R(Hn(F)) ⊇ C∆(F), where ∆(F) is the maximum degree of F.5 On the other hand, Theorem 1.1 above shows that R(Hn(F)) ⊇ C|E(F)|, since Hn(F) is a regular |E(F)|-uniform hypergraph. (Note that C∆(F) ⊃ C|E(F)|, unless ∆(F) = |E(F)|, in which case F is a star-graph and the two regions are the same.)

- 1.2. Subgraphs in Dense Graphs. In this section, we explore the application of the general framework introduced above, in counting subgraphs of vertex-percolated graphs. Given 0 < p < 1 and a graph G = (V (G),E(G)) the vertex-percolated graph G[p] is the random induced subgraph G[S],6 where S is obtained by including every element of V (G) independently with probability


p. For a ﬁxed graph H = (V (H),E(H)), denote by Tp(H,G) the number of copies of the graph H = (V (H),E(H)) in G[p]. More formally,

1 |Aut(H)|

auaub(G), (1.9)

Xu

Tp(H,G) :=

![image 21](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile21.png>)

(a,b)∈E(H)

u∈V (G)|V (H)|

where:

- – X1,X2,··· ,X|V (G)| are i.i.d. Ber(p) and Xu := j |V=1(H)| Xuj,
- – A(G) = ((auv(G))) is the adjacency matrix of G,


![image 22](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile22.png>)

4Note that Theorem 1.1 does not construct a regular s-uniform hypergraph H for which R(H) = Cs, since the symmetry breaking construction depends on p and r. We are only able to obtain such a construction when rs is

restricted to be on the concave part of the function x → Ip(xs1 ) (see Example 1 for details). 5This is the exact replica symmetric region when F is D-regular, that is, R(Hn(F)) = CD ([23, Theorem 1.1]). 6Given a graph G = (V (G), E(G)) and S ⊆ V (G), G[S] denotes the induced subgraph of G on the set S.

![image 23](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile23.png>)

- – V (G)|V (H)| is the set of all |V (H)|-tuples u = (u1,··· ,u|V (H)|) ∈ V (G)|V (H)| with distinct indices.7 Thus, the cardinality of V (G)|V (H)| is (|V(G|V)|−|(GV)|(!H)|)!,

![image 24](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile24.png>)

- – Aut(H) is the automorphism group of H, that is, the group of permutations σ of the vertex set V (H) such that (x,y) ∈ E(H) if and only if (σ(x),σ(y)) ∈ E(H).


Note that

p|V(H)| |Aut(H)|

auaub(G) = p|V(H)|N(H,G), (1.10)

E(Tp(H,G)) =

![image 25](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile25.png>)

u∈V (G)|V (H)| (a,b)∈E(H)

where N(H,G) is the number of copies of H in G.

- Remark 1.3. As mentioned before, the statistic (1.9) arises in the problem of estimating motif frequencies in large graphs [21]. Here, given a large graph Gn, the goal is to eﬃciently (without storing or searching over the entire graph) estimate motif frequencies (subgraph counts) of Gn, by making local queries on Gn. Klusowski and Wu [21] proposed the subgraph sampling model, where one has access to the random induced subgraph Gn[S], where S ⊂ V (Gn) is obtained by


sampling each vertex in V (Gn) independently with probability p. In this model, by (1.10) above,

1

p|V(H)|Tp(H,Gn) is an unbiased estimate of the subgraph count N(H,Gn).

![image 26](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile26.png>)

The large deviation tail probabilities for Tp(H,Gn) can be derived using the general theory described above. To see this, note that Tp(H,Gn) can be rewritten as (1.1) by deﬁning the |V (H)|uniform hypergraph which has vertex set V (Gn) and a hyperedge for every copy of H in Gn.8 In this section, we show that the large deviation variational problem for Tp(H,Gn) itself has a limit, when Gn is a converging sequence of dense graphs. We begin with some preliminaries on graph limit theory. The formal statement of the result is given in Section 1.2.1.

- 1.2.1. Graph Limit Theory Preliminaries. The theory of graph limits developed by Lov´asz and coauthors [22] has received phenomenal attention over the last few years. It connects various topics such as graph homomorphisms, Szemeredi’s regularity lemma, and quasirandom graphs, and has found many interesting applications in statistical physics, extremal graph theory, statistics and related areas (see [5, 6, 13, 25, 26, 29, 30] and the references therein). Here we recall the basic deﬁnitions about the convergence of graph sequences. If F and G are two graphs, denote


the homomorphism density of F into G by t(F,G) := ||Vhom((G)||F,GV(F))||, where |hom(F,G)| denotes the number of homomorphisms of F into G.

![image 27](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile27.png>)

To deﬁne the continuous analogue of graphs, consider W to be the space of all measurable functions from [0,1]2 into [0,1] that satisfy W(x,y) = W(y,x), for all x,y. For a simple graph F with V (F) = {1,2,... ,|V (F)|}, let

t(F,W) = ˆ

W(xi,xj)dx1dx2 ··· dx|V(F)|. (1.11)

[0,1]|V (F)| (i,j)∈E(F)

- Deﬁnition 1.2. [9, 10, 22] A sequence of graphs {Gn}n≥1 is said to converge to W ∈ W, if for every ﬁnite simple graph F,


lim

t(F,Gn) = t(F,W). (1.12)

n→∞

![image 28](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile28.png>)

7For a set S, the set SN denotes the N-fold cartesian product S × S × · · · × S. 8Technically this is a ‘multi-hypergraph’, because a subset of V (H) vertices might contain several copies of H in Gn. However, the general theory can be easily modiﬁed to include hypergraphs with multiple edges.

The limit objects, that is, the elements of W, are called graph limits or graphons. A ﬁnite simple graph G = (V (G),E(G)) can also be represented as a graphon in a natural way: Deﬁne WG(x,y) = 1{(⌈|V (G)|x⌉,⌈|V (G)|y⌉) ∈ E(G)}, that is, partition [0,1]2 into |V (G)|2 squares of side length 1/|V (G)|, and let WG(x,y) = 1 in the (i,j)-th square if (i,j) ∈ E(G), and 0 otherwise. Observe that t(F,WG) = t(F,G) for every simple graph F and therefore the constant sequence G converges to the graph limit WG. It turns out that the notion of convergence in terms of subgraph densities outlined above can be suitably metrized using the so-called cut distance (see Section 3 for details).

- 1.2.2. Large Deviations of Subgraph Counts in Vertex-Percolated Dense Graphs. Consider a sequence of graphs {Gn}n≥1 converging to a graphon W ∈ W and a ﬁxed graph H. In this case, the limit of the upper tail large deviation probability for Tp(H,Gn) can be described as a variational problem in the space of graphons. To this end, given a measurable function h : [0,1]  → [0,1], a ﬁxed graph H, and graphon W ∈ W, deﬁne


|V (H)|

t(H,W,h) := ˆ

W(xi,xj)

h(xi) dx1 ··· dx|V(H)|. (1.13)

i=1

(i,j)∈E(H)

[0,1]|V (H)|

(Note that when h := 1 is the constant function 1, t(H,W,h) = t(H,W), as deﬁned in (1.11).)

- Theorem 1.2. Suppose {Gn}n≥1 is a sequence of graphs converging to a graphon W and H = (V (H),E(H)) is a ﬁxed graph satisfying t(H,W) > 0. Then, for 0 < p < r < 1,


1 |V (Gn)|

log P(Tp(H,Gn) ≥ r|V(H)|N(H,Gn)) = −ψ2(H,W,r,p), (1.14) with

lim

![image 29](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile29.png>)

n→∞

ˆ 1

Ip(h(x))dx : t(H,W,h) ≥ r|V(H)|t(H,W) , (1.15) where the inﬁmum is taken over the set of all measurable functions h : [0,1]  → [0,1].

ψ2(H,W,r,p) := inf

h:[0,1] →[0,1]

0

The proof of this result and various examples are given in Section 3. Note that the assumption

t(H,W) > 0 implies that the limiting density of H in Gn is non-vanishing, and ensures, among other things, that the mean-ﬁeld assumptions are satisﬁed. This also gives the exact Bahadur slope

[3] of the unbiased estimate p|V1(H)|Tp(H,Gn) (recall Remark 1.3) for the subgraph count N(H,Gn), in the subgraph-sampling model (see Remark 3.1 for details).

![image 30](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile30.png>)

2. Proof of Theorem 1.1

Proof of Replica-Symmetry: The proof for the replica symmetry case relies on the following lemma.

- Lemma 2.1. For any s-uniform d-regular hypergraph H = (V (H),E(H)), and x = (x1,x2,


... ,x|V (H)|) ∈ [0,1]|V (H)|, |E(1H)|t(H,x) ≤ |V(1H)| v |V=1(H)| xsv, where t(H,x) is as in Deﬁnition 1.1. Proof. Note that it suﬃces to show t(H,x) ≤ ds

![image 31](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile31.png>)

![image 32](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile32.png>)

|V (H)| v=1 xsv, for x ∈ [0,1]|V (H)|, since |E(H)| =

![image 33](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile33.png>)

d s|V (H)|. To this end, deﬁne the function,

![image 34](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile34.png>)

|V (H)|

d s

xsv − t(H,x),

η(x) =

![image 35](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile35.png>)

v=1

This is a smooth function on the compact set [0,1]|V (H)|, and hence the minimum of η(·) is attained at some point z ∈ [0,1]|V (H)|. Therefore, to prove the lemma, it suﬃces to show that η(z) ≥ 0.

To show this, let S := {v ∈ V (H) : zv ∈ (0,1)}. Then, ∂z∂

η(z) = 0, for all v ∈ S. This implies, dzvs−1 =

![image 36](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile36.png>)

v

zu, for all v ∈ S. (2.1)

e∈E(H):v∈e u∈e\{v}

Hence, using (2.1),

 d −

 dzvs −

zu

zu

|V (H)|

1 s

1 s

η(z) =

 ≥ 0,

 =

![image 37](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile37.png>)

![image 38](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile38.png>)

e∈E(H):v∈e u∈e

e∈E(H):v∈e u∈e

v=1

v∈V (H)\S:zv=1

where the last step uses e∈E(H):v∈e u∈e zu ≤ |{e ∈ E(H) : v ∈ e}| = d , for all v ∈ V (H).

To show replica symmetry, suppose (rs,Ip(r)) lies on the convex minorant the function Jp(x) := Ip(x1s). Let Jˆp denote the convex minorant of the function Jp. Note that Jˆp is increasing on the interval [ps,1], and Jp ≥ Jˆp on [0,1]. Hence, for x ∈ [0,1]|V (H)| such that |E(1H)|t(H,x) ≥ rs,

![image 39](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile39.png>)

![image 40](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile40.png>)

|V (H)|

|V (H)|

|V (H)|

1 |V (H)|

1 |V (H)|

1 |V (H)|

Jˆp (xsv) (using Jp ≥ Jˆp)

Jp (xsv) ≥

Ip(xv) =

![image 41](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile41.png>)

![image 42](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile42.png>)

![image 43](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile43.png>)

v=1

v=1

v=1

xsv

≥ Jˆp 

|V (H)|

 1 |V (H)|

 (Jensen’s inequality)

![image 44](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile44.png>)

v=1

≥ Jˆp (rs) (using Lemma 2.1) = Ip(r), (2.2)

The proof of replica symmetry now follows, since there is equality everywhere in (2.2), if xv = r, for all v ∈ V (H).

Proof of Replica Symmetry Breaking: Here, suppose (rs,Ip(r)) does not lie on the convex minorant of the function x → Ip(x1s). Then there exist 0 ≤ r1 < r < r2 ≤ 1 such that the point (rs,Ip(r)) lies strictly above the line segment joining (r1s,Ip(r1)) and (r2s,Ip(r1)), that is, there exists

![image 45](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile45.png>)

- 0 < λ < 1 such that


λr1s + (1 − λ)r2s = rs and λIp(r1) + (1 − λ)Ip(r2) < Ip(r). By continuity, λ′Ip(r1)+(1−λ′)Ip(r2) < Ip(r) for all λ′ in a neighborhood of λ, which means, there exists 0 < λ0 < 1 such that

λ0r1s + (1 − λ0)r2s > rs and λ0Ip(r1) + (1 − λ0)Ip(r2) < Ip(r). Therefore, choose M large enough so that Mλ0 ≥ 1, and

Cp M

1 M

λ0r1s + (1 − λ0)r2s −

> rs and λ0Ip(r1) + (1 − λ0)Ip(r2) +

< Ip(r), where Cp := log(1/p) + log(1/q) (with q := 1 − p). (Note, this choice of M depends on p and r.)

![image 46](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile46.png>)

![image 47](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile47.png>)

Now, let Hn be the disjoint union of M complete s-uniform hypergraphs on ⌈Mn ⌉ vertices each. This is a dense hypergraph, that is |E(Hn)| = Θ(ns), and, hence, satisﬁes assumptions (1.5), which implies that {Hn}n≥1 is a sequence of mean-ﬁeld, regular s-uniform hypergraphs. Assuming that

![image 48](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile48.png>)

the vertices of Hn are labelled {1,2,... ,M⌈Mn ⌉}, deﬁne x = (x1,x2,... ,x|V (Hn)|) ∈ [0,1]|V (Hn)| as xj = where K = ⌊Mλ0⌋. Then using λ0 − M1 ≤ MK ≤ λ0, r1 ≤ 1, and t(H,x) as in Deﬁnition 1.1,

![image 49](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile49.png>)

- r1 for j ∈ {1,2,... ,K⌈Mn ⌉},

![image 50](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile50.png>)

- r2 for j ∈ {K⌈Mn ⌉ + 1,K⌈Mn ⌉ + 2,... ,M⌈Mn ⌉},


![image 51](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile51.png>)

![image 52](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile52.png>)

![image 53](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile53.png>)

![image 54](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile54.png>)

![image 55](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile55.png>)

r1s + ⌈Mn ⌉

K ⌈Mn ⌉ s

r1s M

1 M ⌈Mn ⌉

t(Hn,x) |E(Hn)|

(M − K)r2s ≥ λ0r1s + (1 − λ0)r2s −

![image 56](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile56.png>)

![image 57](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile57.png>)

=

![image 58](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile58.png>)

![image 59](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile59.png>)

![image 60](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile60.png>)

s

![image 61](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile61.png>)

s

> rs. On the other hand, the entropy satisﬁes,

|V (Hn)|

1 |V (Hn)|

n M − K

n M

1 M⌈Mn ⌉

n M

Ip(r1) + M

Ip(r2)

Ip(xu) =

K

![image 62](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile62.png>)

![image 63](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile63.png>)

![image 64](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile64.png>)

![image 65](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile65.png>)

![image 66](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile66.png>)

![image 67](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile67.png>)

u=1

K M

K M

=

Ip(r1) + 1 −

Ip(r2)

![image 68](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile68.png>)

![image 69](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile69.png>)

Ip(r2) M

(using λ0 − M1 ≤ MK ≤ λ0) ≤ λ0Ip(r1) + (1 − λ0)Ip(r2) +

≤ λ0Ip(r1) + (1 − λ0)Ip(r2) +

![image 70](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile70.png>)

![image 71](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile71.png>)

![image 72](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile72.png>)

Cp M

(recall Cp = log(1/p) + log(1/q)) < Ip(r),

![image 73](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile73.png>)

which completes the proof of Theorem 1.1. ✷

Note that in the construction above the hypergraphs {Hn}n≥1 which break symmetry at (p,r), depend on p and r. Whether it is possible to obtain a sequence of regular, mean-ﬁeld s-uniform hypergraphs not depending on p and r, which breaks symmetry whenever (rs,Ip(r)) does not lie on the convex minorant of x → Ip(x1s), remains open. In the example below, we construct a sequence of regular, mean-ﬁeld s-uniform hypergraphs (not depending on p and r) which breaks symmetry whenever the point (rs,Ip(r)) lies on the concave part of x → Ip(x1s).9

![image 74](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile74.png>)

![image 75](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile75.png>)

- Example 1. Assume that the point (rs,Ip(r)) lies on the strictly concave part of the curve of Jp(x) = Ip(x1s). Hence, there exist two points a,b in a neighborhood of rs such that


![image 76](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile76.png>)

a + b 2

- 1

![image 77](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile77.png>)

- 2


- 1

![image 78](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile78.png>)

- 2


= rs and Jp(rs) >

Jp(a) +

Jp(b). (2.3)

![image 79](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile79.png>)

Let n = 2N be even, and let Hn be the disjoint union of two complete s-uniform hypergraphs with N vertices each, and vertices labelled labelled {1,2,··· ,N} and {N +1,N +2,··· ,2N}, respectively.

Deﬁne x = (x1,x2,... ,xn) ∈ [0,1]n as: x1 = ··· = xN := a1s and xN+1 = ··· xn := b1s. It is easy to check that x := (x1,··· ,xn) belongs to the constraint space of (1.3), and by (2.3),

![image 80](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile80.png>)

![image 81](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile81.png>)

n i=1 Ip(xi) = 21Jp(a) + 12Jp(b) < Ip(r), which shows replica-symmetry-breaking.

- 1 n


![image 82](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile82.png>)

![image 83](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile83.png>)

![image 84](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile84.png>)

![image 85](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile85.png>)

9If s ≥ 1, the function Jp(x) = Ip(x1s ) is convex if and only if p ≥ p0(s) := s−1+se−s/1(s−1) . On the other hand, if 0 < p < p0(s), then the function Jp(x) has exactly two inﬂection points (both to the right of x = ps), with a region of concavity in the middle (see [23, Lemma A.1] for details).

![image 86](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile86.png>)

![image 87](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile87.png>)

3. Proof of Theorem 1.2

We begin with a few deﬁnitions from graph limit theory. The notion of graph convergence in terms of subgraph densities in Deﬁnition 1.2 can be metrized using the cut-metric, which we recall below:

- Deﬁnition 3.1. [22] The cut-distance between 2 graphons W1,W2 ∈ W, is deﬁned as


ˆ

(W1(x,y) − W2(x,y)) f(x)g(y)dxdy . (3.1)

||W1 − W2|| := sup

[0,1]2

f,g:[0,1]→[−1,1]

The cut-metric between 2 graphons W1,W2 ∈ W, is deﬁned as δ (W1,W2) := inf

||W1ψ − W2|| ,

ψ

with the inﬁmum taken over all measure-preserving bijections ψ : [0,1] → [0,1], and W1ψ(x,y) := W1(ψ(x),ψ(y)), for x,y ∈ [0,1].

Hereafter, we assume that {Gn}n≥1 is a sequence of graphs converging to a graphon W, which is equivalent to δ (WGn,W) → 0 [9, Theorem 3.8]. Now, for a ﬁxed graph H, deﬁne the multihypergraph MGn(H) with vertex set V (Gn) and a hyperedge for every copy of H in Gn. The assumption t(H,W) > 0 implies that |E(MGn(H))| = Θ(N(H,Gn)) = Θ(|V (Gn)||V (H)|), and

∆2(MGn(H)) = Θ |V (Gn)||V (H)|−2 and ∆1(MGn(H)) = Θ |V (Gn)||V (H)|−1 ,

that is, the sequence {MGn(H)}n≥1 satisﬁes assumption (1.5). Therefore, {MGn(H)}n≥1 is meanﬁeld, and by Deﬁnition 1.1, for every 0 < p < r < 1:

1

|V(Gn)| log P Tp(H,Gn) ≥ r|V(H)|N(H,Gn) −ψGn(r,p,H)

![image 88](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile88.png>)

= 1. where

lim

![image 89](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile89.png>)

n→∞

 

Ip(xv) : N(H,Gn,x) ≥ r|V(H)|N(H,Gn)  

|V (Gn)|

1 |V (Gn)|

ψGn(r,p,H) =

inf

. (3.2)

![image 90](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile90.png>)

x∈[0,1]|V (Gn)|



v=1

with

- – x = (x1,x2,... ,x|V (Gn)|) ∈ [0,1]|V (Gn)| and xu := j |V=1(H)| xuj, and
- – N(H,Gn,x) = |Aut1(H)| u∈V (G


n)|V(H)| xu (a,b)∈E(H) aua,ub(Gn). The argument above shows that to prove Theorem 1.2, it suﬃces to prove that the limit of (3.2) equals (1.15). To this end, suppose {Gn}n≥1 is a sequence of graphs such that limn→∞ δ (WGn,W) =

![image 91](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile91.png>)

0. Then it follows from [9, Lemma 5.3] that there exists a permutation σ : [|V (Gn)|] → [|V (Gn)|] such that ||WGσ

n − W|| → 0, where Gσn is a graph obtained by relabelling the vertices of Gn by σ. Moreover, the variational problem (3.2) is invariant under vertex permutations, that is, ψGn(r,p,H) = ψGσ

n(r,p,H). This implies, to derive the limit of (3.2), we can, without loss of generality, assume ||WGn − W|| → 0.

We begin with the following lemma, which follows by a telescoping argument identical to the proof of [9, Theorem 3.7]. We omit the details.

- Lemma 3.1. Let Gn be a sequence of graphs such that ||WGn − W|| → 0. Then, for any ﬁxed graph H = (V (H),E(H)),


 

W(xi,xj)

|V (H)|

ˆ

lim

sup

fi(xi) dxi = 0,

WGn(xi,xj) −



n→∞

f1,···,f|V (H)|

i=1

(i,j)∈E(H)

(i,j)∈E(H)

[0,1]|V (H)|

where the supremum runs over all measurable functions f1,··· ,f|V(H)| : [0,1]  → [0,1].

Given a function h : [0,1]  → [0,1] and a graphon W ∈ W, recall the deﬁnition of t(H,W,h) from (1.13). Also, denote by Tn the class of all functions h : [0,1]  → [0,1], which are constant on the intervals |V a(−G1

n)|, |V (Ga

n)| , for every 1 ≤ a ≤ |V (Gn)|. Then, recalling (3.2), ψGn(H,r,p) =

![image 92](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile92.png>)

![image 93](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile93.png>)

ˆ 1

Ip(h(x))dx : t(H,WGn,h) − R(H,Gn,h) ≥ r|V(H)| (t(H,WGn) − R (H,Gn)) , (3.3) where

inf

h∈Tn

0

|V (H)|

ˆ ui

![image 94](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile94.png>)

|V (Gn)|

R (H,Gn,h) =

h(y)dy,

auaub(Gn)

ui−1 |V (Gn)|

i=1

![image 95](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile95.png>)

u∈[|V (Gn)|]|V (H)| [|V (Gn)|]|V (H)| (a,b)∈E(H)

and R(H,Gn) = R(H,Gn,1), which is R(H,Gn,h), when h is the constant function 1. The adjustment by R(H,Gn,h) is required to move from the sum over all indices [|V (Gn)|]|V (H)| in t(H,WGn,h) to the sum over distinct indices [|V (Gn)|]|V (H)| in N(H,Gn,x) (recall (3.2)). (Note that R (H,Gn,h) = 0 if H is a clique.) However, the asymptotic contribution of this adjustment is small:

|V (H)| 2

1 |V (Gn)||V (H)|

[V (Gn)]|V (H)| [V (Gn)]|V (H)| ≤

sup

R(H,Gn,h) ≤

. (3.4)

![image 96](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile96.png>)

![image 97](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile97.png>)

|V (Gn)|

h:[0,1] →[0,1]

Lemma 3.2. If Gn is a sequence of graphs such that ||WGn −W|| → 0, then for every ﬁxed graph H and 0 < p < r < 1,

{ψGn(H,r,p) − An(H,r,p)} = 0, (3.5) where An(H,r,p) := infh∈Tn

lim

n→∞

´ 1

0 Ip(h(x))dx : t(H,W,h) ≥ r|V(H)|t(H,W) . Proof. Fix r ∈ (p,1). For each n ≥ 1, choose hn ∈ Tn such that

t(H,W,hn) ≥ r|V(H)|t(H,W) and ˆ 1

1 n

. (3.6)

Ip(hn(x))dx < An(H,r,p) +

![image 98](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile98.png>)

0

By Lemma 3.1, t(H,WGn,hn) − t(H,W,hn) → 0 and t(H,WGn) → t(H,W), as n → ∞. Then there exists ε ∈ (0,r/p) such that, by (3.4),

r|V(H)|t(H,W) (r − εp)|V (H)|

t(H,W) 2

t(H,WGn,hn) − R(H,Gn,hn) > t(H,W,hn) − ε and

,

< t(H,WGn) <

![image 99](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile99.png>)

![image 100](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile100.png>)

for all large n. Now, deﬁne ε′ := p|V(H)2|tε(H,W). Then t(H,WGn,hn) − R(H,Gn,hn) > r|V(H)|t(H,W) − ε (by (3.6)) > (r − εp)|V(H)|t(H,WGn) − ε

![image 101](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile101.png>)

> (r − εp)|V(H)|t(H,WGn) − ε′p|V(H)|t(H,WGn) ≥ (r/p − ε)|V(H)| − ε′ p|V(H)| (t(H,WGn) − R(H,Gn)) ,

by choosing ε small enough so that (r/p − ε)|V (H)| − ε′ > 0. This implies, recalling (3.3) and (3.6),

ψGn (H,rε,p) ≤ ˆ 1

1 n

. (3.7)

Ip(hn(x))dx < An(H,r,p) +

![image 102](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile102.png>)

0

1

![image 103](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile103.png>)

where rε = (r/p − ε)|V(H)| − ε′

|V(H)| p. Note that rε → r, as ε → 0, and by arguments similar to the proof of [12, Lemma 5.8], it follows that

ψGn (H,rε,p) ≥ ψGn(H,r,p) + o(1), where the o(1)-term depends on p,r,H, and ε, but not on n, and goes to zero as ε → 0. This implies limsupn→∞ {ψGn(H,r,p) − An(H,r,p)} ≤ 0. The other direction can be proved similarly.

Next, let Q denote the class of all measurable functions h : [0,1]  → [0,1], such that h is continuous at every irrational point in [0,1]. Then deﬁne

LW(H,r,p) := inf

h∈Q

ˆ 1

Ip(h(x))dx : t(H,W,h) ≥ r|V(H)|t(H,W) .

0

Note that Tn ⊂ Q, for each n ≥ 1, which gives liminfn→∞ An(H,r,p) ≥ LW(H,r,p). Now, ﬁxing ε > 0, choose h ∈ Q such that

t(H,W,h) ≥ r|V(H)|t(H,W) and ˆ 1

Ip(h(x))dx < LW(H,r,p) + ε. (3.8) For n ≥ 1, deﬁne

0

|V (Gn)|

a − 1 |V (Gn)|

a |V (Gn)|

h(y) 1 x ∈

hn(x) =

sup

,

.

![image 104](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile104.png>)

![image 105](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile105.png>)

y∈ |V a(−G1n)|,|V (Gan)|

a=1

![image 106](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile106.png>)

![image 107](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile107.png>)

Clearly, hn ≥ h, and hence, t(H,W,hn) ≥ r|V(H)|t(H,W), for all n ≥ 1. Moreover, since hn ∈ Tn, An(H,r,p) ≤ ˆ 1

Ip(hn(x))dx, for all n ≥ 1. (3.9)

0

Now, since hn(x) → h(x) for every irrational x ∈ [0,1], and Ip is a bounded, continuous function on [0,1], limn→∞

´ 1 0 Ip(hn(x))dx =

´ 1

0 Ip(h(x))dx, by the dominated convergence theorem. Hence, by taking limits in (3.9) and using (3.8), we have limsupn→∞ An(H,r,p) < LW(H,r,p) + ε. Finally, since ε > 0 is arbitrary, by (3.5), we get

lim

ψGn(H,r,p) = LW(H,r,p). (3.10)

n→∞

Therefore, to complete the proof of Theorem 1.2, it suﬃces to show LW(H,r,p) = ψ2(H,W,r,p) (recall (1.15)). Clearly, ψ2(H,W,r,p) ≤ LW(H,r,p). For the other direction, let ε ∈ (0,r/p) and take a measurable function h : [0,1]  → [0,1] such that

t(H,W,h) ≥ r|V(H)|t(H,W) and ˆ 1

Ip(h(x))dx < ψ2(H,W,r,p) + ε (3.11)

0

By standard measure theoretic arguments, there exists a continuous function g : [0,1]  → [0,1] such that:

´ 1 0 Ip(h(x))dx + ε and

´ 1 0 Ip(g(x))dx <

t(H,W,g) ≥ t(H,W,h) − ε|V (H)|p|V(H)|t(H,W) ≥ (r|V(H)| − (εp)|V (H)|)t(H,W), where the last step uses (3.11). Hence, deﬁning rε = (r|V(H)| − (εp)|V (H)|)

1

|V(H)|, gives

![image 108](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile108.png>)

Ip(g(x))dx < ˆ 1

LW(H,rε,p) ≤ ˆ 1

Ip(h(x))dx + ε < ψ2(H,W,r,p) + 2ε (3.12)

0

0

where the last step uses (3.11). Finally, since rε → r, as ε → 0, by arguments similar to the proof of [12, Lemma 5.8],

LW(H,rε,p) ≥ LW(H,r,p) + o(1), where the o(1)-term goes to zero as ε → 0. This combined with (3.12) shows that LW(H,r,p) = ψ2(H,W,r,p), which completes the proof of Theorem 1.2. ✷

- Remark 3.1. By arguments similar to the proof of Theorem 1.2, an analogous variational problem

can be established for the two-sided tail probability. More precisely, if {Gn}n≥1 is a sequence of graphs converging in cut-metric to a graphon W ∈ W, and H = (V (H),E(H)) is a ﬁxed graph satisfying t(H,W) > 0, then for any ﬁxed ε > 0, it follows that

lim

n→∞

1 |V (Gn)|

![image 109](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile109.png>)

log P

1 p|V(H)|

![image 110](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile110.png>)

Tp(H,Gn) − N(H,Gn) ≥ ε = −γ2(H,W,ε,p), where

γ2(H,W,ε,p) := inf

h:[0,1] →[0,1]

ˆ 1

0

Ip(h(x))dx :

t(H,W,h) p|V (H)| − t(H,W) ≥ ε ,

![image 111](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile111.png>)

is the exact Bahadur slope [3] of p|V1(H)|Tp(H,Gn), the estimate of N(H,Gn) in the subgraph sampling model described in Remark 1.3.

![image 112](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile112.png>)

The variational problem in (1.15) reduces to a ﬁnite dimensional optimization problem, if the limiting graphon W is a block function (constant on ﬁnitely many blocks). These functions are dense in the space of graphons and arise naturally as limits of stochastic block models.

- Remark 3.2. (Block Graphons) Suppose {Gn}n≥1 is a sequence of graphs converging in cut-metric to the following K-block graphon:


K

W(x,y) :=

i=1

K

bij1{x ∈ Ai and y ∈ Aj},

j=1

- where B := ((bij))1≤i,j≤K is a non-zero K × K symmetric matrix with entries in [0,1], and A1,A2,... ,AK form a measurable partition of [0,1], with λ(Ai) > 0, for all 1 ≤ i ≤ K (here λ(·) denotes the Lebesgue measure on [0,1]). Then, for any ﬁxed graph H = (V (H),E(H)), the homomorphism density


t(H,W) =

buaub

(u1,...,u|V (H)|)∈[K]|V (H)| (a,b)∈E(H)

|V (H)|

λ(Aui).

i=1

Further, for x = (x1,x2,... ,xK) ∈ [0,1]K, deﬁne

t(H,W,x) :=

buaub

(u1,...,u|V (H)|)∈[K]|V (H)| (a,b)∈E(H)

|V (H)|

λ(Aui)xui.

i=1

Then the RHS of (1.15) becomes,

K

λ(Ai)Ip(xi) : t(H,W,x) ≥ r|V(H)|t(H,W) , (3.13)

inf

x=(x1,x2,...,xK)∈[0,1]K

i=1

which is a ﬁnite dimensional optimization problem with K variables. To see (3.13), note that for any h : [0,1] → [0,1] in the constraint space of (1.15), the vector x ∈ [0,1]K deﬁned by

1 λ(Ai)

ˆ

xi :=

h(z)dz, for 1 ≤ i ≤ K,

![image 113](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile113.png>)

Ai

belongs to the constraint space of (3.13). Then by the convexity of Ip(·),

K

λ(Ai)Ip(xi) ≤ ˆ 1

Ip(h(z))dz,

0

i=1

which shows that (3.13) is at most the RHS of (1.15). Conversely, for some x in the constraint space of (3.13), the function h(z) := Ki=1 xi1{z ∈ Ai} belongs to the constraint space of (1.15) and

´ 1 0 Ip(h(z))dz = Ki=1 λ(Ai)Ip(xi). Hence, the RHS of (1.15) is equal to (3.13).

We conclude with an example of a sequence of non-regular graphs which exhibits replica symmetry breaking, for all 0 < p < r < 1.

- Example 2. (Bipartite Graphs) Consider the sequence of complete bipartite graphs Km,n, with m/(m + n) → α ∈ (0,1). In this case, the limiting graphon W is a two-block function with block sizes α and (1 − α), with 0 on the diagonal blocks and 1 on the oﬀ-diagonal blocks. Then by Theorem 1.2, for 0 < p < r < 1,


1 m + n

log P(Tp(K2,Km,n) ≥ r2mn) → −ψ2(K2,W,r,p). In this case, W is 2-block, hence, by Remark 3.2,

![image 114](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile114.png>)

αIp(x) + (1 − α)Ip(y) : xy ≥ r2 . (3.14)

ψ2(K2,W,r,p) = inf

(x,y)∈[0,1]2

- • α = 21: Then any (x,y) in the constraint space of (3.14) satisﬁes x+2y ≥

![image 115](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile115.png>)

![image 116](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile116.png>)

√xy ≥ r, and by the convexity of Ip and the fact that it is increasing on the interval (p,1), it follows that

![image 117](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile117.png>)

- 1

![image 118](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile118.png>)

- 2Ip(x) + 12Ip(y) ≥ Ip (r), showing replica symmetry, for all values of 0 < p < r < 1.


![image 119](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile119.png>)

- • α = 12: In this case, the graph sequence Km,n is irregular. Note that (3.14) equals the minimum of the function:


![image 120](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile120.png>)

r2 x

, over x ∈ r2,1 .

g(x) := αIp(x) + (1 − α)Ip

![image 121](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile121.png>)

Note that g is diﬀerentiable on r2,1 and g′ (r) = 0, showing replica-symmetry-breaking for all values of 0 < p < r < 1.

References

- [1] F. Augeri. Nonlinear large deviation bounds with applications to traces of Wigner matrices and cycles counts in Erd˝s-Re´nyi graphs. arXiv:1810.01558, 2018.
- [2] T. Austin. The structure of low-complexity Gibbs measures on product spaces. arXiv preprint arXiv:1810.07278, 2018.
- [3] R. R. Bahadur. Rates of convergence of estimates and test statistics. The Annals of Mathematical Statistics, 38(2):303–324, 1967.
- [4] A. Basak and S. Mukherjee. Universality of the mean-ﬁeld for the Potts model. Probability Theory and Related Fields, 168(3-4):557–600, 2017.
- [5] S. Bhamidi, G. Bresler, and A. Sly. Mixing time of exponential random graphs. Ann. Appl. Probab., 21(6):2146– 2170, 2011.
- [6] S. Bhamidi, S. Chakraborty, S. Cranmer, and B. Desmarais. Weighted exponential random graph models: Scope and large network limits. Journal of Statistical Physics, 173(3-4):704–735, 2018.
- [7] B. B. Bhattacharya, S. Ganguly, E. Lubetzky, and Y. Zhao. Upper tails and independence polynomials in random graphs. Advances in Mathematics, 319(313–347), 2017.
- [8] B. B. Bhattacharya, S. Ganguly, X. Shao, and Y. Zhao. Upper tails for arithmetic progressions in a random set. International Mathematics Research Notices, to appear, 2018.
- [9] C. Borgs, J. T. Chayes, L. Lova´sz, V. T. S´os, and K. Vesztergombi. Convergent sequences of dense graphs. I. Subgraph frequencies, metric properties and testing. Adv. Math., 219(6):1801–1851, 2008.
- [10] C. Borgs, J. T. Chayes, L. Lova´sz, V. T. S´os, and K. Vesztergombi. Convergent sequences of dense graphs II. Multiway cuts and statistical physics. Ann. of Math. (2), 176(1):151–219, 2012.
- [11] J. Brie¨t and S. Gopi. Gaussian width bounds with applications to arithmetic progressions in random settings. International Mathematics Research Notices, to appear, 2018.
- [12] S. Chatterjee and A. Dembo. Nonlinear large deviations. Adv. Math., 299:396–450, 2016.
- [13] S. Chatterjee and P. Diaconis. Estimating and understanding exponential random graph models. The Annals of Statistics, 41(5):2428–2461, 2013.
- [14] S. Chatterjee and S. R. S. Varadhan. The large deviation principle for the Erd˝s-Re´nyi random graph. European J. Combin., 32(7):1000–1017, 2011.
- [15] N. Cook and A. Dembo. Large deviations of subgraph counts for sparse Erd˝s-Re´nyi graphs. arXiv:1809.11148, 2018.
- [16] A. Dembo and E. Lubetzky. A large deviation principle for the Erd˝s–Re´nyi uniform random graph. Electronic Communications in Probability, 23, 2018.
- [17] R. Eldan. Gaussian-width gradient complexity, reverse log-Sobolev inequalities and nonlinear large deviations. Geom. Funct. Anal., to appear, 2018.
- [18] S. Janson and A. Rucin´ski. Upper tails for counting objects in randomly induced subhypergraphs and rooted random graphs. Arkiv f¨or matematik, 49(1):79–96, 2011.
- [19] R. Kenyon, C. Radin, K. Ren, and L. Sadun. Multipodal structure and phase transitions in large constrained graphs. Journal of Statistical Physics, 168(2):233–258, 2017.
- [20] R. Kenyon, C. Radin, K. Ren, and L. Sadun. The phases of large networks with edge and triangle constraints. Journal of Physics A: Mathematical and Theoretical, 50(43):435001, 2017.
- [21] J. M. Klusowski and Y. Wu. Counting motifs with graph sampling. In Proceedings of the 31st Conference On Learning Theory, volume 75, pages 1966–2011, 2018.
- [22] L. Lova´sz. Very large graphs. In Current developments in mathematics, 2008, pages 67–128. Int. Press, Somerville, MA, 2009.
- [23] E. Lubetzky and Y. Zhao. On replica symmetry of large deviations in random graphs. Random Structures Algorithms, 47(1):109–146, 2015.
- [24] E. Lubetzky and Y. Zhao. On the variational problem for upper tails in sparse random graphs. Random Structures Algorithms, 50(3):420–436, 2017.
- [25] C. Radin, K. Ren, and L. Sadun. A symmetry breaking transition in the edge/triangle network model. Annales de l’Institut Henri Poincar´e D, 5(2):251–286, 2018.
- [26] C. Radin and M. Yin. Phase transitions in exponential random graphs. The Annals of Applied Probability, 23(6):2458–2471, 2013.
- [27] L. Warnke. Upper tails for arithmetic progressions in random subsets. Israel J. Math., 221:317–365, 2017.
- [28] J. Yan. Nonlinear large deviations: Beyond the hypercube. arXiv preprint arXiv:1703.08887, 2017.


- [29] M. Yin. A detailed investigation into near degenerate exponential random graphs. Journal of Statistical Physics, 164(1):241–253, 2016.
- [30] M. Yin, A. Rinaldo, and S. Fadnavis. Asymptotic quantization of exponential random graphs. The Annals of Applied Probability, 26(6):3251–3285, 2016.


Appendix A. A Simple Mean-Field Condition

In this section we derive a simple suﬃcient condition for a sequence of s-uniform hypergraphs to be mean-ﬁeld for the upper tail problem (recall Deﬁnition 1.1), using the framework of non-linear large deviations developed in [17]. To this end, we need a few deﬁnitions: The Lipschitz constant of a function h : {0,1}n  → R, is deﬁned as:

|∂ih(y)|, where

Lip(h) = max

i∈[n],y∈{0,1}n

∂ih(y) = h(y1,... ,yi−1,1,yi+1,... ,yn) − h(y1,... ,yi−1,0,yi+1,... ,yn), denotes the discrete partial derivative of h(y) with respect to the i-th coordinate. The Gaussianwidth of a set A ⊆ Rn is deﬁned as:

aTZ ,

GW(A) = E sup

a∈A

where Z follows the standard n−dimensional Gaussian distribution Nn(0,In). Finally, the gradientcomplexity of h is deﬁned as:

D(h) = GW ({∇h(y) : y ∈ {0,1}n} ∪ {0}) , where ∇h(y) := (∂1h(y),··· ,∂nh(y))⊤.

For x ∈ [0,1], deﬁne the function:

fn(x) := |V (Hn)| |E(Hn)|

t(Hn,x), (A.1)

![image 122](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile122.png>)

where t(Hn,x) is as in Deﬁnition 1.1. It follows from [17, Theorem 5] that a sequence of s-uniform hypergraph {Hn}n≥1 is mean-ﬁeld for the upper tail problem if

Lip(fn) = O(1) and D(fn) = o(|V (Hn)|). (A.2) In [11, Corollary 6.1] it was proved that the above conditions are satisﬁed whenever (1.5) holds. The ﬁrst condition in (1.5) ensures D(fn) = o(|V (Hn)|), while the second condition implies Lip(fn) = O(1). In the following proposition, we derive another easy suﬃcient condition for (A.2) to hold, in terms of the number of hyperdges in Hn. As a special case, this recovers the mean-ﬁeld condition for graphs (1.6).

Proposition A.1. A sequence of s-uniform hypergraphs {Hn}n≥1 is mean-ﬁeld for the upper tail problem if

|E(Hn)| ≫ |V (Hn)|s−1 and ∆1(Hn) = O |E(Hn)| |V (Hn)|

![image 123](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile123.png>)

where ∆1(Hn) denotes the maximum degree of the hypergraph Hn. Proof. Recall the deﬁnition of fn(·) from (A.1). Note that,

|V (Hn)| |E(Hn)|

{e ∈ E(Hn) : v ∈ e} = |V (Hn)| |E(Hn)|

Lip(fn) ≤

max

![image 124](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile124.png>)

![image 125](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile125.png>)

v∈V (Hn)

, (A.3)

∆1(Hn).

The second condition in (A.3) then implies that Lip(fn) = O(1).

Therefore, it suﬃces to show D(fn) = o(|V (Hn)|) (recall (A.2)). Note that for a standard |V (Hn)|−dimensional Gaussian vector Z and y ∈ {0,1}|V (Hn)|,

|∇fn(y)TZ| =

∂vfn(y)Zv

v∈V (Hn)

= |V (Hn)| |E(Hn)|

![image 126](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile126.png>)

Zv

v∈V (Hn)

yu

e∈E(Hn):v∈e u∈e\{v}

= |V (Hn)| |E(Hn)|

![image 127](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile127.png>)

Zv

v∈V (Hn)

1 A {v} ∈ E(Hn)

A⊆V (Hn)\{v}

yu

u∈A

= |V (Hn)| |E(Hn)|

yu ,

CA

![image 128](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile128.png>)

u∈A

A⊆V (Hn):|A|=s−1

where CA := v/∈A Zv · 1(A {v} ∈ E(Hn)). By the Cauchy-Schwarz inequality,

|V (Hn)|s+12 |E(Hn)|

CA2 = |V (Hn)|s+12 |E(Hn)|

√

![image 129](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile129.png>)

![image 130](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile130.png>)

![image 131](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile131.png>)

![image 132](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile132.png>)

|∇fn(y)TZ| ≤

C⊤C,

![image 133](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile133.png>)

![image 134](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile134.png>)

A⊆V (Hn):|A|=s−1

- where C is the column vector of length |Vs(−H1n)| , having entries CA indexed by subsets A of V (Hn)


having size s−1. Note that C = MZ, where M = ((MA,v)) is the |Vs(−H1n)| ×n matrix with entries MA,v := 1{v ∈/ A,A {v} ∈ E(Hn)}, where A varies over the set of all subsets of V (Hn) having size s − 1, and v ∈ V (Hn). Hence,

|V (Hn)|s+12 |E(Hn)|

E √

![image 135](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile135.png>)

![image 136](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile136.png>)

Z⊤M⊤MZ

D(fn) ≤

![image 137](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile137.png>)

|V (Hn)|s+12 |E(Hn)|

![image 138](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile138.png>)

![image 139](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile139.png>)

E(Z⊤M⊤MZ)

≤

![image 140](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile140.png>)

= |V (Hn)|s+12 |E(Hn)|

![image 141](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile141.png>)

![image 142](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile142.png>)

trace [M⊤M]

![image 143](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile143.png>)

= |V (Hn)|s+12 |E(Hn)|

![image 144](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile144.png>)

![image 145](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile145.png>)

1 v ∈/ A,A {v} ∈ E(Hn)

![image 146](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile146.png>)

v∈V (Hn) A⊆V (Hn):|A|=s−1

√s|V (Hn)|s+12 |E(Hn)|

= |V (Hn)|s+12 |E(Hn)|

![image 147](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile147.png>)

![image 148](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile148.png>)

![image 149](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile149.png>)

![image 150](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile150.png>)

= o(|V (Hn)|),

dHn(v) =

![image 151](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile151.png>)

![image 152](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile152.png>)

![image 153](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile153.png>)

v∈V (Hn)

by the ﬁrst condition in (A.3).

In general, the conditions in Proposition A.1 and those in (1.5) are incomparable. The maximum co-degree condition in (1.5) holds for many sparse hypergraphs, such as the r-AP counting hypergraph. On the other hand, Proposition A.1 requires very high edge-density, but allows for larger co-degrees, as illustrated in the example below. To this end, for a ﬁnite set T and a positive integer s ≥ 1, denote by Ts the set of all subsets of T with cardinality s.

- Example 3. Fix s ≥ 3, and take (s − 1)−2 < a < (s − 1)−1. For j ∈ {1,2,... ,⌈na⌉}, suppose Tj := {(j − 1)⌈n1−a⌉ + 1,(j − 1)⌈n1−a⌉ + 2,... ,j⌈n1−a⌉},


and let Fn(j) be the hypergraph with vertex set Tj and hyperedge set Tsj . Note that

Fn(1),Fn(2),... ,Fn(⌈na⌉), is a collection of ⌈na⌉ disjoint copies of the complete s-uniform hypergraph on ⌈n1−a⌉ vertices. Next, deﬁne the hypergraph Dn = (V (Dn),E(Dn)) with vertex set V (Dn) := {1′,2′,... ,n′} and hyperedge set

V (Dn)\{1′,2′} s − 2

E(Dn) := B {1′,2′} : B ∈

,

the collection of all s-element subsets of V (Dn) containing 1′ and 2′. Finally, let Hn be the sequence of hypergraphs obtained by taking the disjoint union of

Fn(1),Fn(2),... ,Fn(⌈na⌉) and Dn. Note that |E(Hn)| = ⌈na⌉|E(Fn(1))| + ns−−22 = Θ(ns−a(s−1)). Moreover, ∆1(Hn) ≤ max{n(1−a)(s−1),ns−2} = O(n(1−a)(s−1)),

and ∆2(Hn) ns−2. Now, it is easy to check that condition (A.3) is satisﬁed. On the other hand, using a > (s − 1)−2,

s−2−a(s−1)+ 1

|E(Hn)| |V (Hn)|

![image 154](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile154.png>)

2⌈ s−1

2 ⌉ ≪ ns−2,

n

![image 155](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile155.png>)

![image 156](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile156.png>)

2− 1

![image 157](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile157.png>)

2⌈ s−1 2 ⌉

![image 158](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile158.png>)

showing that the ﬁrst condition in (1.5) is not satisﬁed.

For the case s = 2 (which corresponds to graphs), (1.5) always implies (A.3). To see this note that for any sequence of non-empty graphs {Gn}n≥1, ∆2(Gn) = 1. Therefore, the ﬁrst condition in (1.5) is equivalent to |E(Gn)| ≫ |V (Gn)|32 log |V (Gn)|, which implies |E(Gn)| ≫ |V (Gn)|, the ﬁrst condition in (A.3). For an example where (A.3) holds, but (1.5) does not, consider a sequence {Gn}n≥1 of d-regular graphs on n vertices, with 1 ≪ d = O(√n). In this case, condition (A.3) is trivially satisﬁed (note that |E(Gn)| = nd2 ≫ n), but the ﬁrst condition in (1.5) does not hold, since

![image 159](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile159.png>)

![image 160](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile160.png>)

![image 161](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile161.png>)

![image 162](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile162.png>)

nd 2 ≪ n23 log n.

![image 163](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile163.png>)

|E(Gn)| =

![image 164](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile164.png>)

![image 165](<2018-mukherjee-replica-symmetry-upper-tails_images/imageFile165.png>)

Department of Statistics, University of Pennsylvania, Philadelphia, USA, somabha@wharton.upenn.edu Department of Statistics, University of Pennsylvania, Philadelphia, USA, bhaswar@wharton.upenn.edu

