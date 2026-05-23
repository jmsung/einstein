arXiv:1711.06216v2[math.CO]17Apr2019

ON THE PROBABILITY OF NONEXISTENCE IN BINOMIAL SUBSETS

FRANK MOUSSET, ANDREAS NOEVER, KONSTANTINOS PANAGIOTOU, AND WOJCIECH SAMOTIJ

Abstract. Given a hypergraph Γ = (Ω, X) and a sequence p = (pω)ω∈Ω of values in (0, 1), let Ωp be the random subset of Ω obtained by keeping every vertex ω independently with probability pω. We investigate the general question of deriving ﬁne (asymptotic) estimates for the probability that Ωp is an independent set in Γ, which is an omnipresent problem in probabilistic combinatorics. Our main result provides a sequence of upper and lower bounds on this probability, each of which can be evaluated explicitly in terms of the joint cumulants of small sets of edge indicator random variables. Under certain natural conditions, these upper and lower bounds coincide asymptotically, thus giving the precise asymptotics of the probability in question. We demonstrate the applicability of our results with two concrete examples: subgraph containment in random (hyper)graphs and arithmetic progressions in random subsets of the integers.

1. Introduction

Let Γ = (Ω,X) be a hypergraph and, given a sequence p = (pω)ω∈Ω ∈ (0,1)Ω, let Ωp be a random subset of Ω formed by including every ω ∈ Ω independently with probability pω. What is the probability that Ωp is an independent set in Γ? This very general question arises in many diﬀerent settings.

- Example 1. Let F be a graph and let n be a positive integer. Deﬁne Ω as the edge set E(Kn) = [n]

2 of the complete graph with vertex set [n] = {1,...,n} and let X be the collection of the edge sets of all copies of F in Kn. Fix some p ∈ (0,1) and deﬁne p by setting pω = p for every ω ∈ Ω. Then we are asking for the probability that the Erdős–Rényi random graph Gn,p is F-free, that is, does not contain F as a (not necessarily induced) subgraph.

- Example 2. An arithmetic progression of length r ∈ N (an r-AP for short) is a subset of the integers of the form {a + kb : k ∈ [r]}, where b = 0. Let Ω = [n] and let X be the set of all r-APs in [n]. Given p ∈ (0,1), we deﬁne p by setting pω = p for every ω ∈ Ω. Then we are asking for the probability that the p-random subset [n]p of [n] is r-AP-free.
- Example 3. Let Ω be a ﬁnite set of points in the plane. Include a triple {i,j,k} in X if the points


i,j,k lie on a common line. Now we are asking for the probability that the random subset Ωp of points is in general position.

It is not hard to ﬁnd other natural examples that provide further motivation for studying this question. It is convenient to introduce some notation. Given Γ = (Ω,X) and p ∈ (0,1)Ω, we shall ﬁx an (abritrary) ordering of the elements of X as γ1,...,γN. We then let Xi denote the indicator variable of the event that γi ⊆ Ωp and set X = X1 + ··· + XN. Thus, X counts the number of edges of Γ that are fully contained in Ωp and our goal is to compute the probability that X = 0. Of course, these notations all depend on the given pair (Γ,p), but we shall always suppress this dependence as it will be clear from the context.

Most of the time, we will be interested in the case where Γ = Γ(n) and p = p(n) (and hence also X = X(n)) depend on some parameter n that tends to inﬁnity and ask:

What are the asymptotics of the probability P[X = 0] as n → ∞?

![image 1](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile1.png>)

Date: April 18, 2019.

Research supported in part by the Israel Science Foundation grants 1147/14 (FM, WS), 1028/16 (FM) and 1147/14 (FM), the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation program (grant agreement no. 772606) (KP), and the ERC Starting Grant 633509 (FM). .

1

The above question can also be viewed as a computational problem: we want to derive closed formulas that are asymptotic to P[X = 0], at least for various ranges of the density parameter p.

For technical convenience, we shall exclude the border case where pω ∈ {0,1} for some ω. That case can always be addressed by changing Γ or by a continuity argument.

- 1.1. The Harris and Janson inequalities. The main reason why computing P[X = 0] is challenging is that the random variables X1,...,XN are usually not independent. However, this is not to say that there is no structure at all: each random variable Xi is a non-decreasing function on the product space {0,1}Ω. An important inequality that applies in this case is the Harris inequality:


- Theorem 4 (Harris inequality [10]). Let Ω be a ﬁnite set and let X and Y be random variables deﬁned on a product probability space over {0,1}Ω. If X and Y are both non-decreasing (or nonincreasing), then

E[XY ] ≥ E[X]E[Y ]. If X is non-decreasing and Y is non-increasing, then

E[XY ] ≤ E[X]E[Y ].

In our setting, for every V ⊆ [N], the random variable i∈V (1 − Xi) is non-increasing, so we easily deduce from Harris’s inequality that

P[X = 0] = E



i∈[N]

(1 − Xi)

 ≥

i∈[N]

(1 − E[Xi]). (1)

Note that (1) would be true with equality if X1,...,XN were independent. An upper bound on P[X = 0] is given by Janson’s inequality, which states that the reverse of (1) holds up to a multiplicative error term that is an explicit function of the pairwise dependencies between the indicator random variables X1,...,XN. Formally, we write i ∼ j if i = j and γi ∩ γj = ∅, and deﬁne the sum of joint moments

∆2 =

i∼j

E[XiXj]. (2)

- Theorem 5 (Janson’s inequality [2, 15]). For all Γ and p as above, P[X = 0] ≤ exp − E[X] + ∆2 .


To compare this with (1), we will now assume that the individual probabilities of Xi = 1 are not too large, say E[Xi] ≤ 1 − ε for some positive constant ε. In this case, we may use the inequality 1 − x ≥ exp(−x − x2/ε) for x ∈ [0,1 − ε] to obtain from (1)

P[X = 0] ≥

(1 − E[Xi]) ≥ exp(− E[X] − δ1/ε), (3)

i∈[N]

where

E[Xi]2. (4)

δ1 =

i∈[N]

Combining this lower bound with the upper bound given by Janson’s inequality, we get the approximation

P[X = 0] = exp − E[X] + O(δ1 + ∆2) . (5)

If δ1 + ∆2 = o(1), then (5) gives the correct asymptotics of P[X = 0]. The condition ∆2 = o(1) in particular requires that the pairwise correlations between the indicator variables Xi vanish asymptotically in a well-deﬁned sense. This rather strict requirement is not satisﬁed in many natural settings, including the ones presented in Examples 1–3 for certain choices of p. It is therefore an important question to obtain better approximations of P[X = 0] in cases when the pairwise dependencies among the Xi are not negligible. This is the starting point of our investigations.

- 1.2. Triangles in random graphs. Even though our results will be phrased in the general framework introduced above and are thus widely applicable, we believe that it is useful to keep in mind the following well-studied instance of the problem that will serve as a guiding example.

Example 6. Assume p = p(n) ∈ (0,1) and let X = X(n) denote the number of triangles in Gn,p, as in Example 1 with F = K3. Since each triangle has three edges, we have E[Xi] = p3 for all i. Thus E[X] = n3 p3 and δ1 = O(n3p6). Moreover, we have ∆2 = O(n4p5), because if two distinct triangles intersect, then their union is the graph with 4 vertices and 5 edges. Thus (5) implies that as long as p = o(n−4/5), we have

P[X = 0] = exp − n3p3/6 + o(1) .

Extending this result, Wormald [25] and later Stark and Wormald [23] obtained asymptotic expressions for P[X = 0] even when p = Ω(n−4/5) and thus (5) no longer gives an asymptotic bound. In particular, it was shown by Stark and Wormald in [23] that if p = o(n−7/11), then

P[X = 0] = exp −

n3p3 6

![image 2](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile2.png>)

+

n4p5 4

![image 3](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile3.png>)

−

7n5p7 12

![image 4](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile4.png>)

+

n2p3 2

![image 5](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile5.png>)

−

3n4p6 8

![image 6](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile6.png>)

+

27n6p9 16

![image 7](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile7.png>)

+ o(1) .

One goal of this paper is to give a simple interpretation of the individual terms in this formula. Indeed, we will formulate a general result from which the above formula may be obtained by a few short calculations. More precisely, we will prove a generalisation of (5) that takes into account the k-wise dependencies between the variables Xi for all k ≥ 2.

- 1.3. Joint cumulants, clusters, dependency graphs. Let A = {Z1,...,Zm} be a ﬁnite set of real-valued random variables. The joint moment of the variables in A is


∆(A) = E[Z1 ···Zm]. (6) The joint cumulant of the variables is

κ(A) =

(|π| − 1)!(−1)|π|−1

π∈Π(A)

∆(P), (7)

P∈π

where Π(A) denotes the set of all partitions of A into non-empty sets. In particular, κ({X}) = E[X], κ({X,Y }) = E[XY ] − E[X]E[Y ], κ({X,Y,Z}) = E[XY Z] − E[X]E[Y Z] − E[Y ]E[XZ] − E[Z]E[XY ]

+ 2 E[X]E[Y ]E[Z].

The joint cumulant κ(A) can be regarded as a measure of the mutual dependence of the variables in A. For example, κ({X,Y }) is simply the covariance of X and Y , and so κ({X,Y }) = 0 if X and Y are independent. More generally, the following holds.

Proposition 7. Let A be a ﬁnite set of real-valued random variables. If A can be partitioned into two subsets A1 and A2 such that all variables in A1 are independent of all variables in A2, then κ(A) = 0.

In fact, Proposition 7 remains valid when one replaces the independence assumption with the weaker assumption that ∆(B1 ∪ B2) = ∆(B1)∆(B2) for all B1 ⊆ A1 and B2 ⊆ A2. An elegant proof of Proposition 7 can be found in [1]. The proposition motivates the deﬁnition of the following notion.

Deﬁnition 8 (decomposable, cluster). A set A of random variables is decomposable if there exists a partition A = A1 ∪ A2 such that the variables in A1 are independent of the variables in A2. A non-decomposable set is also called a cluster.

In our setting, the notion of a cluster has a natural combinatorial interpretation. Given Γ = (Ω,X) and p ∈ (0,1)Ω, we deﬁne the dependency graph GΓ as the graph on the vertex set [N] whose edges are all pairs {i,j} such that i ∼ j, that is, γi ∩ γj = ∅. It is then clear that a set V ⊆ [N] induces a connected subgraph in GΓ if and only if the set of random variables {Xi : i ∈ V } is a

cluster (this is one reason why it is convenient to assume pω ∈/ {0,1} for all ω ∈ Ω). In particular, the joint cumulant κ({Xi : i ∈ V }) vanishes unless GΓ[V ] is connected.

Motivated by this, we shall write Ck for the collection of all k-element subsets V ⊆ [N] such that GΓ[V ] is connected, and deﬁne

κ({Xi : i ∈ V }) and ∆k =

κk =

V ∈Ck

∆({Xi : i ∈ V }). (8)

V ∈Ck

Note that this deﬁnition of ∆k is consistent with the deﬁnition of ∆2 given by (2). Moreover, it follows from (7) and Harris’s inequality that |κk| ≤ Kk∆k for some Kk depending only on k.

- 1.4. Our main result. Let Γ = (Ω,X) and p ∈ (0,1)Ω be as above. Given a subset V ⊆ [N], we write


(V ) \ V for the external neighbourhood of V in the dependency graph and let λ(V ) =

∂(V ) = NG

Γ

E[Xi |

Xj = 1]

j∈V

i∈∂(V )

be the expected number of external neighbours i of V in the dependency graph such that γi ⊆ Ωp, conditioned on γj ⊆ Ωp for all j ∈ V . For all k ∈ N, we deﬁne

Λk(Γ,p) = max λ(V ) : V ⊆ [N] and 1 ≤ |V | ≤ k .

It can be intuitively helpful to think of Λk(Γ,p) as a measure of (non)expansion of the dependency graph GΓ.

- Theorem 9. For every n ∈ N, let Γ(n) = (Ω(n),X(n)) be a hypergraph and let p(n) ∈ (0,1)Ω(n). Assume that for every constant k ∈ N,


pω(n) = 0 and limsup

lim

max

Λk(Γ(n),p(n)) < ∞.

n→∞

ω∈Ω(n)

n→∞

Let X(n) denote the number of edges of Γ(n) that are fully contained in Ω(n)p(n). Then, for every constant k ∈ N,

P[X(n) = 0] = exp − κ1 + κ2 − ··· + (−1)kκk + O(δ1 + ∆k+1) as n → ∞, where δ1, κ1,...,κk, and ∆k+1 are deﬁned as above.

The condition max{pω(n) : ω ∈ Ω(n)} = o(1) implies κk = ∆k + o(∆k) for every ﬁxed k, as can be seen from the deﬁnition (7) of κk. In such cases, the ﬁrst-order behaviour of κk is thus given by ∆k. However, this does not mean that we can then replace κi by ∆i in the formula for P[X(n) = 0] given by Theorem 9, because the lower-order terms in the κi can be non-negligible, see e.g. the proof of Corollary 15 below.

The fact that κ1 = E[X] shows that the case k = 1 of Theorem 9 gives (a slight weakening of) Janson’s inequality (5). Unlike (5), Theorem 9 requires the additional assumptions maxω∈Ω(n) pω(n) = o(1) and Λk(Γ(n),p(n)) = O(1) for all constant k. Both conditions are perhaps not strictly necessary. As we will see further below, the latter condition implies that ∆k+1 = O(∆k) for all constant k, which gives at least an indication of the type of assumption that is involved.

It is natural to ask under which conditions Theorem 9 can give asymptotically sharp bounds. While computing the ﬁrst error term δ1 is generally straightforward, it is not so obvious how one should estimate ∆k+1. Here we will focus on the rather common situation where each edge of Γ(n) has bounded size and there is some p(n) ∈ (0,1) such that pω(n) = p(n) for all ω ∈ Ω(n). We then write simply Ωp instead of Ωp. This is the situation that we encounter in all of our applications.

For every Ω′ ⊆ Ω, deﬁne the j-th codegree of Ω′ by

dj(Ω′) = |{γ ∈ X : Ω′ ⊆ γ and |γ| = |Ω′| + j}|, and let

dj(Ω′)pj;

D(Γ,p) = max

max

∅ =Ω′⊆Ω

j≥1

one can think of this as a weighted maximum codegree of Γ. The following is a specialised version of Theorem 9 that gives an easily veriﬁable condition ensuring ∆k+1 = o(1) for some constant k.

- Theorem 10. Let r be a ﬁxed positive integer. For every n ∈ N, let Γ(n) = (Ω(n),X(n)) be a hypergraph whose edges all have size at most r and let p(n) be a real number in (0,1). Assume

lim

n→∞

p(n) = 0 and limsup

n→∞

D(Γ(n),p(n)) < ∞.

Let X(n) denote the number of edges of Γ(n) that are fully contained in Ω(n)p(n). Then, for every constant k ∈ N,

P[X(n) = 0] = exp − κ1 + κ2 − ··· + (−1)kκk + O(δ1 + ∆k+1) as n → ∞, where δ1, κ1,...,κk, and ∆k+1 are deﬁned as above.

Moreover, if D(Γ(n),p(n)) ≤ |Ω(n)|−ε for some positive ε, then there is a positive integer k = k(ε,r) such that ∆k+1 = o(1).

Let us brieﬂy illustrate the applicability of this result by considering again the example of triangle-free random graphs.

Example 6 (continuing from p.3). The hypergraph Γ of triangles in Kn is 3-uniform, so we can choose r = 3 in Theorem 10. One easily veriﬁes that D(Γ,p) ≤ p+np2. We recall from our earlier discussion that δ1 ≤ n3p6. Therefore Theorem 10 implies that for every ﬁxed positive integer k and all p = o(n−1/2), we have

P[X = 0] = exp − κ1 + κ2 − ··· + (−1)kκk + O(∆k+1) + o(1) . Moreover, if p ≤ n−1/2−ε for some positive constant ε, then there exists a constant k such that

P[X = 0] = exp − κ1 + κ2 − ··· + (−1)kκk + o(1) , i.e., the asymptotics of P[X = 0] are given by a ﬁnite formula that we could in principle compute by analysing the ﬁnitely many possible ‘shapes’ of clusters formed by at most k triangles in Kn.

We shall derive both of the above theorems from a more general result, Theorem 11 below, which has the advantage that it can be applied in certain non-sparse settings. Its disadvantage lies in the fact that the error terms are somewhat less transparent. For a set A of random variables, we deﬁne

δ(A) = ∆(A) · max{E[X] : X ∈ A}. Given k ∈ N, we set

δk =

V ∈Ck

δ({Xi : i ∈ V }), (9)

analogously to (8), and

ρk = max

V ⊆[N] 1≤|V |≤k

P[Xi = 1 for some i ∈ V ∪ ∂(V )]. (10)

Observe that this deﬁnition of δk generalises (4).

- Theorem 11. For every k ∈ N and ε > 0, there is a K = K(k,ε) such that the following holds. Let Γ = (Ω,X) be a hypergraph and let p ∈ (0,1)Ω. If ρk+1 ≤ 1 − ε, then


log P[X = 0] + κ1 − κ2 + κ3 − ··· + (−1)k+1κk ≤ K · (δ1,K + ∆k+1,K), where

K

K

δi and ∆k+1,K =

∆i.

δ1,K =

i=1

i=k+1

We will derive Theorems 9 and 10 from Theorem 11 in Section 2. The proof of Theorem 11, which is the main part of this paper, will be presented in Section 3.

- 1.5. Application: random graphs and hypergraphs. A fundamental question studied by the random graphs community, raised already in the seminal paper of Erdős and Rényi [8], is to


determine the probability that Gn,p contains no copies of a given ‘forbidden’ graph F (as in Example 1). The classical result of Bollobás [5], proved independently by Karoński and Ruciński [16], determines this probability asymptotically for every strictly balanced1 F, but only for p such that the expected number of copies of F in Gn,p is constant. (In the case when F is a tree or a cycle, this was done earlier by Erdős and Rényi [8] and in the case when F is a complete graph, by Schürger [22].) It was later proved by Frieze [9] that the same estimate remains valid as long as the expected number of copies of F in Gn,p is o(nε) for some positive constant ε that depends only on F. Wormald [25] and later Stark and Wormald [23] obtained asymptotic formulas for signiﬁcantly larger ranges of p in the special case where F is a triangle. Prior to those papers and the present work, the strongest result of this form (i.e., determining the probability of being F-free asymptotically) for a general graph F followed from Harris’s and Janson’s inequalities, see (5). Finally, we remark that for several special graphs F, the probability that Gn,p is F-free can be computed very precisely either when p = 1/2 or, in some cases, even for all suﬃciently large p = o(1) using the known precise structural characterisations of F-free graphs, see [4, 11, 17, 18, 19].

Using Theorem 10, we can answer this question for a large class of graphs and a wide range of densities. We will take a rather general point of view and consider the analogous problem in random r-uniform hypergraphs, where instead of just avoiding a single graph F, our goal is to avoid every graph in some ﬁnite family F. Let Gn,p(r) denote the random r-uniform hypergraph (r-graph for short) on n vertices containing every possible edge (r-element subset of the vertices) with probability p, independently of other edges. In particular, G(2)n,p is simply the binomial random graph Gn,p. Given a family F = {F1,...,Ft} of r-graphs, we consider the problem of determining the probability that G(n,pr) is F-free, that is, it simultaneously avoids all copies of all r-graphs in F.

Since removing isomorphic duplicates from F does not aﬀect the probability that we are interested in, we can assume that the r-graphs in F are pairwise non-isomorphic. Similarly, we can assume that no hypergraph in F has isolated vertices.

We encode this problem in a hypergraph Γ = (Ω,X) by proceeding similarly as we did in

Example 1. That is, we let Ω = [nr] be the edge set of Kn(r), the complete r-graph with vertex set [n], and we let X be the collection of edge sets of subhypergraphs of Kn(r) that are isomorphic to one of the r-graphs in F. The probability that Gn,p is F-free is then precisely the probability that the p-random subset Ωp contains no edges of Γ.

Note that the maximal size of an edge in Γ is bounded from above by the largest number of edges of an r-graph in F, which does not depend on n. By applying Theorem 10 to this hypergraph, we can therefore get the asymptotics for the probability that Gn,p(r) is F-free in a certain range of p. To quantify this range, given an r-graph F, deﬁne

m∗(F) = min

eF − eH vF − vH

: H ⊆ F with vH < vF and eH > 0 ,

![image 8](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile8.png>)

where we use the convention min∅ = ∞ and where vG and eG denote, respectively, the numbers of vertices and edges in a (hyper)graph G. For a family F of r-graphs, we then set

m∗(F) = min{m∗(F) : F ∈ F} and d(F) = min{eF/vF : F ∈ F}. It is easy to see that δ1 ≤ |F| · max{nv

: F ∈ F} and thus δ1 = o(1) if np2d(F) = o(1).

p2e

F

F

Moreover, for any non-empty set Ω′ of edges in Kn(r) whose union forms an r-graph H with eH > 0 edges, we have

F−eH : H ⊆ F ∈ F and vH < vF} . It follows that D(Γ,p) = (npm

F−vHpe

dj(Ω′)pj = O max{nv

max

j≥1

∗(F))Θ(1). Theorem 10 then immediately implies the following result.

![image 9](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile9.png>)

1A graph F is strictly balanced if eF /vF > eH/vH for every proper non-empty subgraph H of F.

- Corollary 12. Let F be a ﬁnite family of r-uniform hypergraphs and assume that p = p(n) ∈ (0,1) satisﬁes

npm

∗(F) = o(1) and np2d(F) = o(1). (11) Then, for every constant k ∈ N, we have

P G(n,pr) is F-free = exp − κ1 + κ2 − ··· + (−1)kκk + O(∆k+1) + o(1) as n → ∞. Moreover, if npm

∗(F) ≤ n−ε for some positive ε, then there is a positive integer k = k(ε,F) such that ∆k+1 = o(1).

The conditions in (11) can be further simpliﬁed under certain natural assumptions on the family F. Recall that the r-density of an r-graph F with at least two edges is

mr(F) = max

eH − 1 vH − r

![image 10](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile10.png>)

: H ⊆ F with eH > 1

and that F is r-balanced if this maximum is achieved with H = F, that is, if mr(F) = (eF − 1)/(vF − r). Observe that for every F with at least two edges, we have

mr(F) ≥

eF − 1 vF − r

![image 11](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile11.png>)

≥ m∗(F).

We claim that if F is r-balanced, then in fact mr(F) = m∗(F). Indeed, writing αK = (eK − 1)/(vK − r), we see that for every H ⊆ F with vH < vF and eH > 1,

eF − eH vF − vH

![image 12](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile12.png>)

=

αF(vF − r) − αH(vH − r) (vF − r) − (vH − r)

![image 13](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile13.png>)

≥ mr(F),

since mr(F) = αF ≥ αH (as F is r-balanced) and this inequality continues to hold if eH = 1. Thus m∗(F) ≥ mr(F) and so m∗(F) = mr(F).

Another simpliﬁcation is possible in the important special case r = 2. In this case, the second condition in (11) follows from the ﬁrst condition, since 2eF/vF ≥ (eF −1)/(vF −2) for every graph F and consequently m∗(F) ≤ 2d(F) for every family of graphs F.

- Corollary 13. Let F be a ﬁnite family of 2-balanced graphs with at least two edges each and let

p = p(n) ∈ (0,1) be such that p = o(n−1/m

2(F)) for every F ∈ F. Then, for every ﬁxed k ∈ N, we have

P [Gn,p is F-free] = exp − κ1 + κ2 − ··· + (−1)kκk + O(∆k+1) + o(1) . as n → ∞. Moreover, if p ≤ n−1/m

2(F)−ε for some positive ε and all F ∈ F, then there is a positive integer k = k(ε,F) such that ∆k+1 = o(1).

Of course, neither Corollary 12 nor Corollary 13 would be particularly useful if one could not compute the values κk for at least several small integers k. In Section 4, we outline a general approach for doing so and perform the calculations for two special cases.

- Corollary 14. If p = o(n−4/5), then the probability that Gn,p is simultaneously K3-free and C4-free is asymptotically

exp −

n3p3 6

![image 14](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile14.png>)

−

n4p4 8

![image 15](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile15.png>)

+

n6p7 4

![image 16](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile16.png>)

+

- 2n5p6

![image 17](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile17.png>)

- 3


.

- Corollary 15. If p = o(n−7/11), then the probability that Gn,p is triangle-free is asymptotically


n3p3 6

exp −

+

![image 18](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile18.png>)

n4p5 4

7n5p7 12

−

+

![image 19](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile19.png>)

![image 20](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile20.png>)

n2p3 2

3n4p6 8

−

+

![image 21](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile21.png>)

![image 22](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile22.png>)

27n6p9 16

![image 23](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile23.png>)

.

As mentioned above, Corollary 15 was obtained independently by Stark and Wormald [23]. It extends a result of Wormald [25] that applies to a smaller range of p. However, the derivation of

- Corollary 15 from Theorem 10 is very short compared to the proofs in [23] and [25].


- 1.6. Application: arithmetic progressions. As a second application, we will estimate the

probability that [n]p, the p-random subset of [n], is r-AP-free, i.e., does not contain any arithmetic progression of length r. As in Example 2, we encode this problem in the hypergraph Γ = (Ω,X) on Ω = [n] whose edge set is the collection X of r-APs in [n].

Since any two distinct integers are contained at most r2 = O(1) common r-APs, it is easy to see that δ1 = O(n2p2r) and D(Γ,p) = O(p + npr−1). Therefore, Theorem 10 has the following corollary.

- Corollary 16. Let r ≥ 3 be a ﬁxed integer and assume p = p(n) ∈ (0,1) satisﬁes p = o(n−1/(r−1)). Then, for every ﬁxed k ∈ N, we have

P [n]p is r-AP-free = exp − κ1 + κ2 − ··· + (−1)kκk + O(∆k+1) + o(1)

as n → ∞. Moreover, if p = o(n−1/(r−1)−ε) for some positive constant ε, then there exists a positive integer k = k(ε,r) such that ∆k+1 = o(1).

In Section 4, we will perform the necessary calculations to determine the precise asymptotics of P[[n]p is r-AP-free] for p = o(n−4/7).

- Corollary 17. If p = o(n−4/7), then the probability that [n]p is 3-AP-free is asymptotically


exp −

n2p3 4

![image 24](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile24.png>)

+

7n3p5 24

![image 25](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile25.png>)

.

- 1.7. Related work and open problems. Janson’s inequality was ﬁrst proved (by Svante Janson himself) during the 1987 conference on random graphs in Poznań, in response to Bollobás’s announcement of his estimate [6] for the chromatic number of random graphs, which requires a strong upper bound on the probability that a random graph contains no large cliques. A related estimate was found, during the same conference, by Łuczak. Janson’s original proof was based on the analysis of the moment-generating function of X, whereas Łuczak’s proof used martingales. Both of these arguments can be found in [14]. Our proof of Theorem 11 is inspired by a subsequent proof of Janson’s inequality that was found soon afterwards by Boppana and Spencer [7]; it uses only the Harris inequality. Somewhat later, Janson [12] showed that his proof actually gives bounds for the whole lower tail, and not just for the probability P[X = 0]. Around the same time, Suen [24] proved a correlation inequality that is very similar to Janson’s. Suen’s inequality gives a slightly weaker estimate (which was later sharpened by Janson [13]), but is applicable in a much more general context. Another generalisation of Janson’s inequality was obtained recently by Riordan and Warnke [20].


In [25], Wormald proved that if p = o(n−2/3), then

n4p5 4

7n5p7 12

n3p3 6

P[Gn,p is K3-free] = exp −

+ o(1) , (12)

+

−

![image 26](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile26.png>)

![image 27](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile27.png>)

![image 28](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile28.png>)

whereas for Gn,m with m = d n2 and d = o(n−2/3), we have P[Gn,m is K3-free] = exp −

n3d3 6

+ o(1) .

![image 29](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile29.png>)

These results were strengthened recently by Stark and Wormald [23], who obtained the approximation in Corollary 15 (which implies (12)) and also

n2d3 2

n4d6 8

n3d3 6

P[Gn,m is K3-free] = exp −

+

−

+ o(1) ,

![image 30](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile30.png>)

![image 31](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile31.png>)

![image 32](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile32.png>)

where m = d n2 , which holds when d = o(n−7/11). In fact, they were able to obtain a more general result, which states that in the range where Corollary 13 is applicable, the probability that Gn,p or Gn,m is F-free is approximated by the exponential of the ﬁrst few terms of a power series in n and p (resp. d) whose terms depend only on F. However, the way in which these terms are computed is rather implicit. In contrast, in the setting of binomial random subsets such as Gn,p, our Theorem 9 explains what these terms are.

While our results (and our methods) apply only to binomial subsets (e.g., Gn,p and not Gn,m), the results for Gn,p could conceivably be transferred to Gn,m using the identity

P[Gn,p is F-free] · P[e(Gn,p) = m | Gn,p is F-free] P[e(Gn,p) = m]

P[Gn,m is F-free] =

.

![image 33](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile33.png>)

It was shown by Stark and Wormald [23] that the conditional probability in the right-hand side can be computed explicitly for a carefully chosen p of the same order of magnitude as d. However, this is not at all an easy task.

It would be interesting to establish a similar relationship in the more abstract and general setting of random induced subhypergraphs. If this was possible, Theorem 9 could be used to count independent sets of a given (suﬃciently small) cardinality in general hypergraphs. In some sense, this would complement the counting results that can be obtained with the so-called hypergraph container method developed by Balogh, Morris, and Samotij [3] and by Saxton and Thomason [21]. Whereas the container method applies to somewhat large independent sets, which exhibit a ‘global’ structure, our Theorem 9 would yield estimates on the number of smaller independent sets that only exhibit ‘local’ structure. In particular, the container method can be used to estimate the probability that Gn,p is F-free whenever p = ω(n−1/m

2(F)) for every nonbipartite graph F. For p in this range, Gn,p conditioned on being F-free is approximately (χ(F) − 1)-partite with very high probability. On the other hand, our method (and the method of [23]) applies whenever p = o(n−1/m

2(F)), provided that F is 2-balanced. For p in this range, the edges of Gn,p conditioned on being F-free are still distributed very uniformly with probability close to one.

2. Proofs of Theorems 9 and 10

In this section, we will show that Theorem 11 implies Theorems 9 and 10. To prove Theorem 9, we need the following lemma, which also clariﬁes the deﬁnition of Λk.

- Lemma 18. For every hypergraph Γ = (Ω,X), every p ∈ (0,1)Ω, and every positive integer k, we have


∆k+1/∆k ≤ Λk(Γ,p) and δk+1/δk ≤ Λk(Γ,p).

Proof. For every V ∈ Ck+1 there exist at least two distinct i ∈ V such that V \ {i} ∈ Ck. Indeed, every connected graph with at least two vertices has at least two non-cut vertices. Therefore for each V ∈ Ck+1 we can make a canonical choice of a set V − ⊂ V such that V − ∈ Ck and

max{E[Xi] : i ∈ V } = max {E[Xi] : i ∈ V −}. (13)

Denoting by iV the unique element in V \ V −, we have iV ∈ ∂(V −) because GΓ[V ] is connected. Moreover,

∆({Xi : i ∈ V }) = ∆({Xi : i ∈ V −}) · E[Xi

|

Xi = 1] and, analogously,

V

i∈V −

It follows that

δ({Xi : i ∈ V }) = δ({Xi : i ∈ V −}) · E[Xi

V

|

Xi = 1]

i∈V −

∆k+1 ≤

=

∆({Xi : i ∈ V −})

E[Xj |

V −∈Ck

j∈∂(V −)

Xi = 1]

i∈V −

∆({Xi : i ∈ V −}) · λ(V −) ≤ ∆k · Λk(Γ,p)

V −∈Ck

and, similarly, δk+1 ≤ δk · Λk(Γ,p).

- Proof of Thm. 9 from Thm. 11. Assume that Γ(n) = (Ω(n),X(n)) and p(n) = (pω(n))ω∈Ω(n) are as in the statement of the theorem.


Fix any k ∈ N and ε ∈ (0,1) and let K = K(k,ε) be as given by Theorem 11. We verify that Γ(n) and p(n) satisfy the assumption of Theorem 11 for all suﬃciently large n. For this, consider

some nonempty V ⊆ [N] of size at most k + 1. Since p = o(1), we have i∈V E[Xi] ≤ (1 − ε)/2 for all suﬃciently large n. Additionally, if i ∈ ∂(V ), then γi intersects j∈V γj. Therefore,

E[Xi] ≤ λ(V ) · max{pω(n) : ω ∈

j∈V

i∈∂(V )

γj} ≤ (1 − ε)/2.

By the union bound, this implies ρk+1 = max

P[Xi = 1 for some i ∈ V ∪ ∂(V )] ≤ 1 − ε.

V ⊆[N] 1≤|V |≤k+1

Therefore, Theorem 11 yields |log P[X = 0] + κ1 − κ2 + ··· + (−1)k+1κk| ≤ K · (δ1,K + ∆k+1,K).

Using Lemma 18 and our assumption that Λi(Γ(n),p(n)) = O(1) for all constant i (in particular, for all 1 ≤ i ≤ K), we get

K

K · δ1,K = K ·

i=1

which completes the proof.

δi = O(δ1) and K · ∆k+1,K = K ·

K

∆i = O(∆k+1),

i=k+1

- Lemma 19. For all positive integers k and r, there exist k′ = k′(k,r) and K = K(k,r) such that, for every p ∈ (0,1) and every hypergraph Γ = (Ω,X) with all edges of size at most r,


′

∆k′/∆k ≤ K · max{D(Γ,p),D(Γ,p)k

}.

Proof. Deﬁne D(j) = max∅ =Ω′⊆Ω dj(Ω′) for every j ≥ 1 and note that then D(Γ,p) = maxj≥1 D(j)pj. It is convenient to also deﬁne D(0) = 1.

We choose k′ = 2rk. Note that if V ∈ Ck′, then there is an ordering of the elements of V as i1,...,ik′ such that the set {i1,...,iℓ} belongs to Cℓ for all ℓ ∈ [k′]. For every ℓ, let jℓ = |γi

)|. Since |γi| ≤ r for all i, there are at most 2rk − 1 edges of Γ that are completely contained in γi

∪ ··· ∪ γi

\ (γi

ℓ−1

ℓ

1

. Therefore, by our choice of k′, at least one of jk+1,...,jk′ must be nonzero. Since there are at most 2rℓ choices for the intersection of γi

∪ ··· ∪ γi

k

1

, it then follows that

and γi

∪···∪γi

ℓ−1

ℓ

1

k′

∆k′/∆k ≤

ℓ=k+1

0≤jk+1,...,jk′≤r jk+1+···+jk′≥1

2rℓD(j

ℓ)pj

′

≤ K · max {D(Γ,p),D(Γ,p)k

}

ℓ

for an appropriate choice of K.

- Proof of Thm. 10 from Thm. 9. Suppose that Γ(n) = (Ω(n),X(n)) and p(n) ∈ (0,1) are as in the statement of the theorem. Deﬁne the sequence p(n) = (pω(n))ω∈Ω(n) by pω(n) = p(n) for all ω ∈ Ω(n). For every V ⊆ [N], we have | i∈V γi| ≤ r|V |, and so


E Xi |

λ(V ) =

j∈V

i∈∂(V )

Xj = 1

dj(Ω′)p(n)j

≤ 2r|V| +

max

j≥1

∅ =Ω′⊆ i∈V γi

≤ 2r|V| 1 + D(Γ(n),p(n)) .

Using our assumption on D(Γ(n),p(n)), this implies Λk(Γ(n),p(n)) = O(1) for every ﬁxed k ∈ N. Since we also assume p(n) → 0, Theorem 9 implies the ﬁrst statement of Theorem 10.

To see the second statement, assume D(Γ(n),p(n)) ≤ |Ω(n)|−ε for a positive ε. By Lemma 19, iterated 2r/ε times, we ﬁnd that there are k = k(ε,r) and K = K(ε,r) such that ∆k ≤ K · |Ω(n)|−2r · ∆1. Since ∆1 ≤ |Ω(n)|rp(n), we obtain ∆k ≤ K · |Ω(n)|−r · p(n) = o(1).

3. Proof of Theorem 11

Let Γ and p be as in the statement of the theorem. We start the proof by establishing some notational conventions. Given a subset V ⊆ [N], we use the abbreviations

XV =

i∈V

![image 34](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile34.png>)

Xi and XV =

(1 − Xi).

i∈V

Note that these are the indicator variables for the events ‘γi ⊆ Ωp for all i ∈ V ’ and ‘γi Ωp for all i ∈ V ’, respectively. Besides being positively correlated by Harris’s inequality, the variables XV satisfy the stronger FKG lattice condition

E[XU]E[XV ] ≤ E[XU∪V ]E[XU∩V ] for all U,V ⊆ X. (14)

To see that this is true, rewrite (14) using E[XW] = ω∈ W pω, take logarithms of both sides, and note that

log pω

ω∈ i∈U∪V γi

log pω

log pω −

log pω +

=

ω∈( i∈U γi)∩( i∈V γi)

ω∈ i∈V γi

ω∈ i∈U γi

log pω,

log pω −

log pω +

≥

ω∈ i∈U∩V γi

ω∈ i∈V γi

ω∈ i∈U γi

since log pω < 0 for all ω ∈ Ω and i∈U∩V γi ⊆ i∈U γi ∩ i∈V γi. We will also use the notation

E[XP]

µπ =

P∈π

whenever π is a set of subsets of [N] (usually a partition of some subset of [N]). Thus for a non-empty subset V ⊆ [N], the value

κ(V ) =

(−1)|π|−1(|π| − 1)!µπ (15)

π∈Π(V )

is the joint cumulant of {Xi : i ∈ V }. For the sake of brevity, we will from now on write κ(V ) instead of the more cumbersome κ({Xi : i ∈ V }).

Recall that we denote by ∂(V ) the external neighbourhood of V in the dependency graph, that is,

(V ) \ V for every non-empty subset V ⊆ [N]. We deﬁne

∂(V ) = NG

Γ

ρV = P[Xi = 1 for some i ∈ V ∪ ∂(V )], (16) so that ρk+1 = max {ρV : V ⊆ [N] and 1 ≤ |V | ≤ k + 1}. Moreover, we set

I(V ) = [N] \ (V ∪ ∂(V )).

Neglecting the distinction between an index i and the variable Xi, we may say that ∂(V ) contains the variables outside of V that are dependent on V and I(V ) contains those that are independent of V . As above, we write Ci for the collection of all i-element sets V ⊆ [N] such that GΓ[V ] is connected. We will also write Ci(ℓ) for the subset of Ci comprising all A ∈ Ci with maxA = ℓ.

Assume that k ∈ N and ε > 0 are such that ρk+1 ≤ 1 − ε. Note that this implies, in particular, that E[Xi] ≤ 1 − ε for all i ∈ [N]. Then we need to show that, for some K = K(k,ε),

where

log P[X = 0] +

(−1)i+1κi ≤ K · (δ1,K + ∆k+1,K),

i∈[k]

δ1,K =

K

K

δi and ∆k+1,K =

∆i.

i=1

i=k+1

V U

Figure 1. The set U attaches to V , i.e., U ֒→ V , but not vice-versa.

To do so, we ﬁrst write out the probability that X = 0 using the chain rule: P[X = 0] =

![image 35](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile35.png>)

![image 36](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile36.png>)

1 − E[Xℓ | X[ℓ−1] = 1] .

P[Xℓ = 0 | X[ℓ−1] = 1] =

ℓ∈[N]

ℓ∈[N]

![image 37](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile37.png>)

Note that by the Harris inequality, E[Xℓ | X[ℓ−1] = 1] ≤ E[Xℓ] ≤ 1 − ε . Taking logarithms of both sides of the above equality and using the fact that |log(1 − x) + x| ≤ x2/ε for x ∈ [0,1 − ε], we get

![image 38](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile38.png>)

E[Xℓ | X[ℓ−1] = 1] ≤

log P[X = 0] +

ℓ∈[N]

E[Xℓ | X[ℓ−1] = 1]2/ε.

![image 39](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile39.png>)

ℓ∈[N]

![image 40](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile40.png>)

Hence, using again E[Xℓ | X[ℓ−1] = 1] ≤ E[Xℓ], log P[X = 0] +

![image 41](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile41.png>)

E[Xℓ | X[ℓ−1] = 1] ≤

ℓ∈[N]

E[Xℓ]2/ε = δ1/ε. (17)

ℓ∈[N]

Thus, our main goal becomes estimating the sum

![image 42](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile42.png>)

E[Xℓ | X[ℓ−1] = 1]. (18)

ℓ∈[N]

We shall do this by approximating (18) by an expression involving the quantities

(−1)|V|−1 E[XV ] E[XS\I(V) | XS∩I(V) = 1]

. (19)

q(V,S) =

![image 43](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile43.png>)

![image 44](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile44.png>)

![image 45](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile45.png>)

This ratio is well-deﬁned for all V,S ⊆ [N] because E[XS\I(V) | XS∩I(V) = 1] ≥ E[XS\I(V )] > 0,

![image 46](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile46.png>)

![image 47](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile47.png>)

![image 48](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile48.png>)

which is a consequence of the Harris inequality and the assumption that pω < 1 for all ω ∈ Ω. The relationship between (18) and (19) is made precise in the following lemma:

- Lemma 20. Let k ∈ N and ε > 0 be such that ρk+1 ≤ 1 − ε. Then


![image 49](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile49.png>)

E[Xℓ | X[ℓ−1] = 1] −

q(V,[ℓ − 1]) ≤ ∆k+1/ε.

ℓ∈[N]

ℓ∈[N] i∈[k] V ∈Ci(ℓ)

We postpone the proof of Lemma 20 to Section 3.1 and instead show how it implies the assertion of the theorem. Before we can do this, we need several additional deﬁnitions.

- Deﬁnition 21 (Attachment). Given subsets U,V ⊆ [N], we say that U attaches to V , in symbols


- U ֒→ V , if every connected component of GΓ[U ∪ V ] contains a vertex of V (see Figure 1). We state the following simple facts for future reference:


- (i) We have ∅ ֒→ V for every V ⊆ [N].
- (ii) If i ∈ ∂(V ), then {i} ֒→ V .
- (iii) If U ֒→ V and W ֒→ V then also U ∪ W ֒→ V .
- (iv) If V ∈ C|V| and U ֒→ V , then U ∪ V ∈ C|U∪V|.


P

W

V

Figure 2. A partition in ΠCV (W). Note that V is the union of components of the subgraph induced by the part P containing it. If the dashed edge were in GΓ, then the partition would no longer be in ΠCV (W).

- Deﬁnition 22. Suppose that ∅ = V ⊆ W ⊆ [N]. We deﬁne


ΠCV (W) ⊆ Π(W) to be the set of all partitions π of W that contain a part P ∈ π such that V ⊆ P and V is the union of connected components of GΓ[P] (see Figure 2).

Next, for ∅ = V ⊆ W ⊆ [N], we deﬁne κV (W) =

π∈ΠCV (W)

(−1)|π|−1(|π| − 1)!µπ. (20)

Note that this is very similar to the deﬁnition (15) of κ(W), except that we sum over ΠCV (W) instead of Π(W). For every k ∈ N and all V,S ⊆ [N] with V = ∅, we set

κ(Vk)(S) =

(−1)|W|−1κV (W). (21)

V ⊆W⊆V ∪S W֒→V |W|≤k

Certainly, this is a very complicated deﬁnition, whose meaning is far from clear at this point. However, it serves as a convenient ‘bridge’ between q(V,[ℓ − 1]) and the values κi, as shown by the following two lemmas:

- Lemma 23. Let k ∈ N and ε > 0 be such that ρk+1 ≤ 1 − ε. Then there is some K = K(k,ε) such that

ℓ∈[N] i∈[k] V ∈Ci(ℓ)

q(V,[ℓ − 1]) − κ(Vk)([ℓ − 1]) ≤ K · (δ1,K + ∆k+1,K).

- Lemma 24. For every k ∈ N, we have


κ(Vk)([ℓ − 1]) =

ℓ∈[N] i∈[k] V ∈Ci(ℓ)

(−1)i+1κi.

i∈[k]

Theorem 11 is an easy consequence of Lemmas 20, 23, and 24. Indeed, assume k ∈ N and ε > 0 are such that ρk+1 ≤ 1 − ε. It follows from (17), the above three lemmas, and the triangle inequality that

log P[X = 0] +

(−1)i+1κi ≤ δ1/ε + ∆k+1/ε + K′ · (δ1,K′ + ∆k+1,K′)

i∈[k]

for some K′ = K′(k,ε). The assertion of the theorem now follows simply by observing that the right-hand side above is at most K · (δ1,K + ∆k+1,K) for K = K′ + 1/ε.

- 3.1. Proof of Lemma 20. We derive Lemma 20 from the following auxiliary lemma, which will also be used in the proof of Lemma 23.


- Lemma 25. Assume that V,S ⊆ [N] are disjoint. Then for every non-negative integer k,


(−1)k · E[XV | XS = 1] ≤ (−1)k+|V |−1

![image 50](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile50.png>)

q(V ∪ U,S). (22)

U⊆S,U֒→V |U|≤k

Proof. We claim that it suﬃces to prove that for every integer k ≥ 0, (−1)k · E XV XS ≤

(−1)k+|U| E XV∪U E XS∩I(V∪U) . (23)

![image 51](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile51.png>)

![image 52](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile52.png>)

U⊆S,U֒→V 0≤|U|≤k

Indeed, (23) implies (22) because

E XS∩I(V∪U) = P XS = 1 · E XS\I(V∪U) | XS∩I(V∪U) = 1 −1 and because deﬁnition (19) gives

![image 53](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile53.png>)

![image 54](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile54.png>)

![image 55](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile55.png>)

![image 56](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile56.png>)

(−1)|V|+|U|−1 E[XV ∪U] E[XS\I(V∪U) | XS∩I(V∪U) = 1]

.

q(V ∪ U,S) =

![image 57](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile57.png>)

![image 58](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile58.png>)

![image 59](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile59.png>)

We prove (23) by induction on k. When k = 0, the inequality simpliﬁes to E[XV XS] ≤ E[XV ]E[XS∩I(V)],

![image 60](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile60.png>)

![image 61](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile61.png>)

![image 62](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile62.png>)

![image 63](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile63.png>)

which holds because XS ≤ XS∩I(V) and because XV and XS∩I(V) are independent. Assume now that k ≥ 1 and that (23) holds for all k′ with 0 ≤ k′ < k. It follows from the Bonferroni inequalities that

′|XU′. (24)

(−1)k · XS∩∂(V) ≤ (−1)k ·

(−1)|U

![image 64](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile64.png>)

U′⊆S∩∂(V ) |U′|≤k

![image 65](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile65.png>)

Since S and V are disjoint and ∂(V )∪I(V ) = [N]\V , then multiplying (24) through by XV XS∩I(V) and taking expectations yields

′| E[XV∪U′XS∩I(V)] (25)

(−1)k+|U

(−1)k · E[XV XS] ≤

![image 66](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile66.png>)

![image 67](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile67.png>)

U′⊆S∩∂(V ) |U′|≤k

Observe that for every U′ ⊆ S∩∂(V ), the sets V ∪U′ and S∩I(V ) are disjoint. In particular, if U′ is non-empty, then we may appeal to the induction hypothesis (with k ← k − |U′|) to bound each term in the right-hand side of (25) as follows. As S ∩I(V )∩I(V ∪U′ ∪U′′) = S ∩I(V ∪U′ ∪U′′),

′| · E[XV∪U′XS∩I(V)] ≤

(−1)k+|U

![image 68](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile68.png>)

(−1)k+|U

U′′⊆S∩I(V ) U′′֒→V ∪U′ 0≤|U′′|≤k−|U′|

′|+|U′′| E[XV∪U′∪U′′]E[XS∩I(V∪U′∪U′′)]. (26)

![image 69](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile69.png>)

Finally, observe that every non-empty U ⊆ S such that U ֒→ V can be partitioned into a nonempty U′ ⊆ S∩∂(V ) and an U′′ ⊆ S∩I(V ) such that U′′ ֒→ (V ∪U′) in a unique way. Indeed, one sets U′ = U ∩ ∂(V ) and U′′ = U \ U′; this is the only such partition. Since ∅ ֒→ V by deﬁnition, then bounding each term in (25) that corresponds to a non-empty U′ using (26) and rearranging the sum gives (23).

Proof of Lemma 20. Fix ℓ ∈ [N] and assume k ∈ N and ε > 0 are such that ρk+1 ≤ 1−ε. Invoking Lemma 25 with V = {ℓ} and S = [ℓ − 1] twice, ﬁrst with k ← k − 1 and then with k ← k, to get

![image 70](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile70.png>)

both an upper and a lower bound on E[Xℓ | X[ℓ−1]], we obtain

![image 71](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile71.png>)

E[Xℓ | X[ℓ−1] = 1] −

q(U ∪ {ℓ},[ℓ − 1])

U⊆[ℓ−1],U֒→{ℓ} |U|≤k−1

≤

q(U ∪ {ℓ},[ℓ − 1]) . (27)

U⊆[ℓ−1],U֒→{ℓ} |U|=k

Since the sets U ∪ {ℓ} with U ⊆ [ℓ − 1], U ֒→ {ℓ}, and |U| = i − 1 are precisely the elements of Ci(ℓ), we can rewrite the above inequality as

![image 72](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile72.png>)

E[Xℓ | X[ℓ−1] = 1] −

|q(V,[ℓ − 1])|. (28)

q(V,[ℓ − 1]) ≤

V ∈Ck+1(ℓ)

i∈[k] V ∈Ci(ℓ)

It follows from deﬁnition (19) and Harris’s inequality that

E[XV ] E[XS\I(V) | XS∩I(V) = 1]

|q(V,S)| =

![image 73](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile73.png>)

![image 74](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile74.png>)

![image 75](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile75.png>)

E[XV ] 1 − P[Xi = 1 for some i ∈ S \ I(V ) | XS∩I(V) = 1]

E[XV ] 1 − ρV

,

=

≤

![image 76](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile76.png>)

![image 77](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile77.png>)

![image 78](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile78.png>)

Since ρV ≤ ρk+1 ≤ 1 − ε for all V with |V | = k + 1, summing (28) over all ℓ ∈ [N] yields

![image 79](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile79.png>)

E[Xℓ | X[ℓ−1] = 1] −

q(V,[ℓ − 1]) ≤ ∆k+1/ε,

ℓ∈[N]

ℓ∈[N] i∈[k] V ∈Ci(ℓ)

which is precisely the assertion of the lemma.

- 3.2. Proof of Lemma 23 – preliminaries. The goal of this subsection is to derive a recursive formula for κV (W), stated in Lemma 30 below, which will be used in the proof of Lemma 23.


- Deﬁnition 26. Suppose that ∅ = V ⊆ W ⊆ [N]. We deﬁne ΠV (W) and Π֒V→(W) as follows:

- (1) ΠV (W) is the set of all partitions of W that contain V as a part;
- (2) Π֒V→(W) is the set of all partitions π ∈ ΠV (W) such that P ֒→ V for every part P ∈ π.


Since by now we have deﬁned several diﬀerent classes of partitions of a set W, it is a good moment to pause and convince ourselves that

Π֒V→(W) ⊆ ΠV (W) ⊆ ΠCV (W) ⊆ Π(W). As a ﬁrst step towards the promised recursive formula, we give an alternative expression for κV (W).

- Deﬁnition 27 (Degree of a part in a partition). For a partition π of a subset of [N] and any part P ∈ π, let dπ(P) denote the number of parts P′ ∈ π \{P} such that GΓ contains an edge between P′ and P. We call dπ(P) the degree of P in π. Lemma 28. If ∅ = V ⊆ W ⊆ [N], then


where

(−1)|π|−1χV (π)µπ,

κV (W) =

π∈ΠV (W)

χV (π) =

1 if |π| = 1 dπ(V )(|π| − 2)! if |π| ≥ 2.

Proof. Given a π ∈ ΠCV (W), let P denote the part of π containing V . Deﬁne a map f : ΠCV (W) → ΠV (W) as follows. If P = V , then let f(π) = π. Otherwise, let f(π) be the partition obtained

C

V P

Figure 3. A set C in CutV (P). Every element of CutV (P), except for P itelf, is a cutset in GΓ(V ∪ P) that disconnects V from some vertices in P.

from π by splitting P into V and P \ V . Clearly, κV (W) =

(−1)|π|−1(|π| − 1)!µπ

π∈ΠCV (W)

′|−1(|π′| − 1)!µπ′.

(−1)|π

=

π∈ΠV (W) π′∈f−1(π)

Observe that every π ∈ ΠV (W) has exactly |π| − dπ(V ) preimages via f. One of them is π itself and there are |π|−1−dπ(V ) additional partitions obtained from π by merging V with some other part Q ∈ π such that GΓ contains no edges between V and Q. In particular, there is one preimage of size |π| and there are |π| − 1 − dπ(V ) preimages of size |π| − 1. Furthermore, note that µπ′ = µπ for every π′ ∈ f−1(π). Indeed, for every Q ∈ π with no edges of GΓ between Q and

- V , we have E[XV ] · E[XQ] = E[XV XQ] = E[XV ∪Q].


It follows that κV (W) =

(−1)|π|−1 (|π| − 1)! − (|π| − 1 − dπ(V )) · (|π| − 2)! µπ

π∈ΠV (W)

(−1)|π|−1χV (π)µπ,

=

π∈ΠV (W)

as claimed.

Our next lemma is the main result of this subsection and the essential combinatorial ingredient of the proof of Lemma 23. Stating it requires the following deﬁnition (illustrated in Figure 3). Deﬁnition 29 (CutV (P)). Suppose that V ⊆ [N] is non-empty and P ⊆ [N] is disjoint from V and satisﬁes P ֒→ V . Then we write CutV (P) for the collection of all sets C ⊆ [N] satisfying ∂(V ) ∩ P ⊆ C ⊆ P and C ֒→ V .

- Lemma 30. Suppose that ∅ = V ⊆ W ⊆ [N] and W ֒→ V . Then


(−1)|π|−1(|π| − 1)!

κV (W) = E[XV ]

π∈Π֒V→(W)

P∈π P =V

κC(P). (29)

C∈CutV (P)

Proof. Denote the right hand side of (29) by rV (W). We need to show κV (W) = rV (W). Let us ﬁrst rewrite the inner sum in (29). To this end, ﬁx some non-empty P ⊆ W \V such that P ֒→ V . By the deﬁnition of κC(P), see (20),

(−1)|π|−1(|π| − 1)!µπ. (30)

κC(P) =

C∈CutV (P) π∈ΠCC(P)

C∈CutV (P)

We may write this double sum more compactly as follows. For brevity, let ∂P(V ) := ∂(V ) ∩ P. Denote by Π˜V (P) the set of all partitions π ∈ Π(P) such that some Q ∈ π contains all neighbours

of V in P, that is, such that ∂P(V ) ⊆ Q for some Q ∈ π. We claim that

(−1)|π|−1(|π| − 1)!µπ. (31)

κC(P) =

π∈Π˜V (P)

C∈CutV (P)

Indeed, this follows from (30) because, letting

Q(V,P) = {(C,π) : C ∈ CutV (P) and π ∈ ΠCC(P)},

the projection p2: Q(V,P) ∋ (C,π)  → π ∈ Π(P) is a bijection between Q(V,P) and Π˜V (P). This is because for every (C,π) ∈ Q(V,P), C is the union of those connected components of GΓ(Q) that intersect ∂P(V ). Furthermore, observe that the right-hand side of (31) is simply the joint cumulant of the set

P(V)}, which is obtained from P by replacing {Xi : i ∈ ∂P(V )} with the single variable X∂

PV = {Xi : i ∈ P \ ∂P(V )} ∪ {X∂

P(V). Therefore, it follows from (31) that

(−1)|π|−1(|π| − 1)!

rV (W) = E[XV ]

π∈Π֒V→(W)

P∈π P =V

κ(PV ). (32)

Let Π′V (W) be the set of all partitions in ΠV (W) whose every part, except possibly V itself, contains a neighbour of V . We claim that the product in the right-hand side of (32) is zero for every π ∈ Π′V (W) \ Π֒V→(W) and hence we may replace Π֒V→(W) with Π′V (W) in the range of summation in (32). Indeed, if π ∈ Π′V (W) \ Π֒V→(W), then there is a P ∈ π \ {V } such that ∂P(V ) = ∅ but P ֒→ V . In particular, some connected component of GΓ[P] is disjoint from ∂P(V ) and hence κ(PV ) = 0. Expanding κ(PV ) again, we obtain

(−1)|π|−1(|π| − 1)!

rV (W) = E[XV ]

π∈Π′V (W)

P∈π P =V

′|−1(|π′| − 1)!µπ′. (33)

(−1)|π

π′∈Π˜V (P)

Let us write P to denote the set of all pairs (π,π∗) ∈ Π′V (W) × ΠV (W) obtained as follows. Choose an arbitrary partition π ∈ Π′V (W) and reﬁne every P ∈ π \ {V } by replacing it by some πP ∈ Π˜V (P), so that ∂P(V ) is contained in a single part of πP; ﬁnally, let π∗ be the resulting partition of W.

Suppose that (π,π∗) ∈ P. Enumerate the parts of π as V,P1,...,Pt and suppose that π∗ was obtained from π by reﬁning each Pj into ij + 1 parts, so that |π∗| = t + 1 + i1 + ... + it. Then, letting

f(π,π∗) = ft(i1,...,it) := (−1)tt!

j∈[t]

∗|−1t!

ij! = (−1)|π

(−1)i

ij!,

j

j∈[t]

we may rewrite (33) as

f(π,π∗)µπ∗. (34)

rV (W) =

(π,π∗)∈P

Fix some π∗ ∈ ΠV (W) and note that π∗ contains dπ∗(V ) parts other than V that intersect ∂(V ). Let us write s = |π∗|, t = dπ∗(V ), and π∗ = {V,P1∗,...,Ps∗−1}, so that P1∗,...,Pt∗ are the parts intersecting ∂(V ). Fix an arbitrary permutation σ of [s − 1] such that σ(1) ∈ [t]. Such a σ can be used to deﬁne a π such that (π,π∗) ∈ P in the following way. Consider the sequence Pσ∗ = (Pσ∗(1),...,Pσ∗(s−1)). For every i ∈ [t], let Pi be the union of Pi∗ and all the Pj∗, with

- j ∈ [s − 1] \ [t], for which Pi∗ is the right-most element among P1∗,...,Pt∗ that is to the left of Pj∗


in Pσ∗. (Since σ(1) ∈ [t], then each Pj∗ with j ∈ [s − 1] \ [t] has one of P1∗,...,Pt∗ left of it.) A moment’s thought reveals that each partition π with (π,π∗) ∈ P is obtained this way from exactly

|f(π,π∗)| permutations σ. It follows that rV (W) =

∗|−1µπ∗

(−1)|π

|f(π,π∗)|

π∈Π′V (W) (π,π∗)∈P

π∗∈ΠV (W)

∗|−1µπ∗ · |{σ ∈ Sym(|π∗| − 1) : σ(1) ∈ {1,...,dπ∗(V )}}|

(−1)|π

=

π∗∈ΠV (W)

∗|−1µπ∗ · χV (π∗),

(−1)|π

=

π∗∈ΠV (W)

where χV (π∗) is as deﬁned in Lemma 28. By Lemma 28, we conclude that rV (W) = κV (W), as required.

- 3.3. Proof of Lemma 23. For V,S ⊆ [N] and k ∈ N such that |V | ≤ k, we deﬁne


κ(Uk−|V|)(S ∩ I(V ))

κ˜(Vk)(S) = (−1)|V|−1 E[XV ]

0≤i≤k−|V | U⊆S,U֒→V 1≤|U|≤k−|V |

i

(35)

and

q(k)(V,S) = (−1)|V|−1 E[XV ]

q(U,S ∩ I(V ))

0≤i≤k−|V | U⊆S,U֒→V 1≤|U|≤k−|V |

i

. (36)

Our proof of Lemma 23 consists of three steps. First, in Lemma 31, we show that q(V,S) ≈ q(k)(V,S). Second, in Lemma 32, we show that κ(Vk)(S) ≈ κ˜(Vk)(S). Finally, the fact that q(k)(V,S) and κ˜V(k)(S) satisfy similar recurrences (given the above approximate equalities) allows us to prove that also q(V,S) ≈ κ(Vk)(S). Lemma 23 then follows easily. The precise deﬁnition of ‘≈’ above will be expressed by the following quantities. For integers k and K satisfying 1 ≤ k ≤ K, deﬁne

∆k(V ) =

E[XU∪V ] and ∆k,K(V ) =

U֒→V |U∪V |=k

K

∆i(V ), (37)

i=k

and

E[XU∪V ]max{E[Xi] : i ∈ U ∪ V }. (38)

δk,K(V ) =

U֒→V k≤|U∪V |≤K

- Lemma 31. Let ε > 0 and k ∈ N be such that ρk ≤ 1 − ε. Then there exists K = K(k,ε) such that for all V,S ⊆ [N] with 1 ≤ |V | ≤ k,


|q(V,S) − q(k)(V,S)| ≤ K · δ1,K(V ) + ∆k+1,K(V ) . Proof. Fix V and S as in the statement of the lemma and set

![image 80](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile80.png>)

ρ = P[Xi = 1 for some i ∈ S \ I(V ) | XS∩I(V) = 1]. Then by deﬁnition

(−1)|V|−1 E[XV ] E[XS\I(V) | XS∩I(V) = 1]

q(V,S) =

=

![image 81](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile81.png>)

![image 82](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile82.png>)

![image 83](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile83.png>)

(−1)|V|−1 E[XV ] 1 − ρ

. (39)

![image 84](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile84.png>)

Since, by Harris’s inequality and |V | ≤ k, we have 0 ≤ ρ ≤ ρV ≤ ρk ≤ 1 − ε, then (39) and the identity (1 − ρ)−1 = 1 + ρ + ... + ρk−|V| + ρk−|V|+1(1 − ρ)−1 yield

q(V,S) − (−1)|V|−1 E[XV ] · (1 + ρ + ··· + ρk−|V |) ≤ ε−1 E[XV ]ρkV−|V |+1. (40)

We now observe that

E[XV ]ρkV−|V |+1 ≤ E[XV ]

E[Xi]

i∈V ∪∂(V )

k−|V |+1

k−|V |+1

E[Xi

# = E[XV ]

]

j

j=1

i1,...,ik−|V |+1

and note that if i1,...,ik−|V |+1 are distinct elements of ∂(V ), then

k−|V |+1

] ≤ E[XV∪{i

E[Xi

E[XV ]

1,...,ik−|V|+1}]

j

j=1

by Harris’s inequality; if, on the other hand, either ij ∈ V for some j or some two ij are equal, then Harris’s inequality and the fact that |E[Xi]| ≤ 1 for each i imply the stronger bound

k−|V |+1

E[Xi

E[XV ]

]

j

j=1

1,...,ik−|V|+1}] · max{E[Xi] : i ∈ V ∪ {i1,...,ik−|V|+1}}. In particular, the right-hand side of (40) is bounded from above by

≤ E[XV∪{i

ε−1 · (k − |V | + 1)! · ∆k+1(V ) + ε−1 · kk−|V |+1 · δ1,k(V ), which yields

q(V,S) − (−1)|V|−1 E[XV ] · (1 + ρ + ··· + ρk−|V |) ≤ K1 · ∆k+1(V ) + δ1,k(V ) (41) for some constant K1 that depends only on k and ε.

We claim that there is a constant K2 = K2(k,ε) such that, for all 0 ≤ i ≤ k − |V |, E[XV ] · ρi −

i

(V ) . (42)

(V ) + ∆k+1,K

≤ K2 · δ1,K

q(U,S ∩ I(V ))

2

2

U⊆S,U֒→V 1≤|U|≤k−|V |

Observe that (41) and (42) imply that |q(V,S) − q(k)(V,S)| ≤ K · δ1,K(V ) + ∆k+1,K(V ) for some K = K(k,ε), giving the assertion of the lemma. It thus remains to prove (42). We ﬁrst consider the case i = 1. By the Bonferroni inequalities, for every positive j, (−1)j−1 · ρ ≤ (−1)j−1 ·

′|−1 E[XU′ | XS∩I(V) = 1].

(−1)|U

![image 85](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile85.png>)

U′⊆S\I(V ) 1≤|U′|≤j

Applying Lemma 25 with k ← j − |U′|, V ← U′, and S ← S ∩ I(V ), we get that for each

- U′ ⊆ S \ I(V ) with 1 ≤ |U′| ≤ j,


′| E[XU′ | XS∩I(V) = 1] ≤

(−1)j−1q(U′ ∪ U′′,S ∩ I(V )).

(−1)j−|U

![image 86](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile86.png>)

U′′⊆S∩I(V ),U′′֒→U′ |U′′|≤j−|U′|

Next, observe that any non-empty U ⊆ S with U ֒→ V of size at most j can be written uniquely as the disjoint union of U′ and U′′, where U′ ⊆ V ∪ ∂(V ) and U′′ ⊆ I(V ) and U′′ ֒→ U′. The previous two inequalities then imply that

(−1)j−1 · ρ ≤ (−1)j−1 ·

q(U,S ∩ I(V )). (43)

U⊆S,U֒→V 1≤|U|≤j

Invoking (43) twice, ﬁrst with j ← k − |V | and then with j ← k − |V | + 1, to get both an upper and a lower bound on ρ, we obtain

q(U,S ∩ I(V )) ≤

ρ −

U⊆S,U֒→V 1≤|U|≤k−|V |

q(U,S ∩ I(V ))

U⊆S,U֒→V |U|=k−|V |+1

ε−1 E[XU],

≤

U⊆S,U֒→V |U|=k−|V |+1

(44)

where the last inequality uses the deﬁnition of q(U,S ∩ I(V )) and the assumption that ρk ≤ 1 − ε, see the discussion below (39).

Finally, we show how to deduce (42) from (44). Let y =

q(U,S ∩ I(V )),

U⊆S,U֒→V 1≤|U|≤k−|V |

so that the left-hand side of (42) is E[XV ] · |ρi − yi|, and observe that, as in (44), |y| ≤ z :=

ε−1 E[XU].

U֒→V 1≤|U|≤k−|V |

Fix an i ∈ {1,...,k − |V |}. Since |ρ| ≤ 1, then

|ρi − yi| ≤ |ρ − y| ·

- i−1
- j=0


|ρjyi−1−j| ≤ (1 + z)i−1 · |ρ − y|,

which together with (44) implies that E[XV ] · |ρi − yi| ≤ (1 + z)i−1 E[XV ]

ε−1 E[XU].

U֒→V |U|=k−|V |+1

Note that for pairwise disjoint U1,...,Uj ⊆ [N], Harris’s inequality gives j

E[XU

] ≤ E[XU

1∪...∪Uj]

ℓ

ℓ=1

and if U1,...,Uj ⊆ [N] are not pairwise disjoint, then the stronger FKG lattice condition (14) implies that

j

1∪...∪Uj] · max{E[Xi] : i ∈ U1 ∪ ... ∪ Uj}. In particular, using a similar reasoning as used for deriving the bound (41) from (40), we obtain (1 + z)i−1 E[XV ]

E[XU

] ≤ E[XU

ℓ

ℓ=1

ε−1 E[XU] ≤ K4 · δ1,ik(V ) + ∆k+1,ik+1(V )

U֒→V |U|=k−|V |+1

for suﬃciently large K4 = K4(k,ε). This shows (42) and hence the lemma.

- Lemma 32. For every k ∈ N there exists some K = K(k) such that, for all V,S ⊆ [N] with 1 ≤ |V | ≤ k, we have


|κ(Vk)(S) − κ˜(Vk)(S)| ≤ K · δ1,K(V ) + ∆k+1,K(V ) . Proof. Fix k, S, and V as in the statement of the lemma and let x =

κU(k−|V |)(S ∩ I(V )),

U⊆S,U֒→V 1≤|U|≤k−|V |

so that

κ˜(Vk)(S) = (−1)|V|−1 E[XV ](1 + x + x2 + ··· + xk−|V |). (45)

Using the deﬁnition (21), we may rewrite x =

(−1)|W|−1κU(W). (46)

U⊆S,U֒→V 1≤|U|≤k−|V |

U⊆W⊆U∪(S∩I(V )) W֒→U,|W|≤k−|V |

Recalling from Deﬁnition 29 that

CutV (W) = {U ⊆ W : U ֒→ V and ∂(V ) ∩ W ⊆ U}, we may switch the order of summation in (46) to obtain x =

(−1)|W|−1κU(W).

W⊆S,W֒→V 1≤|W|≤k−|V |

U∈CutV (W)

For the sake of brevity, write

(−1)|W|−1κU(W).

f(W) =

U∈CutV (W)

We may now rewrite (45) as

κ˜(Vk)(S) = (−1)|V|−1 E[XV ]

k−|V |

f(W1) · ... · f(Wi). (47)

i=0 W1,...,Wi⊆S

W1,...,Wi֒→V 1≤|W1|,...,|Wi|≤k−|V |

Consider ﬁrst the total contribution κ˜1 to the right-hand side of (47) coming from terms corresponding to W1,...,Wi ⊆ S \ V that are pairwise disjoint and whose union has size at most

- k − |V |. Each such term may be regarded as a partition of the set W = V ∪ W1 ∪ ... ∪ Wi, which satisﬁes V ⊆ W ⊆ S and |W| ≤ k; this partition {V,W1,...,Wi} belongs to Π֒V→(W). Conversely, given a W with these properties, every partition π ∈ Π֒V→(W) corresponds to exactly (|π| − 1)! such terms; this is the number of ways to order the elements of π \ {V } as W1,...,Wi. Therefore,


κ˜1 = (−1)|V|−1 E[XV ]

f(P).

(|π| − 1)!

π∈Π֒V→(W)

P∈π P =V

V ⊆W⊆V ∪S W֒→V,|W|≤k

In particular, Lemma 30 gives κ˜1 = (−1)|V|−1

(−1)|W|−|V|κV (W) = κ(Vk)(S).

V ⊆W⊆V ∪S W֒→V,|W|≤k

Every term in the right-hand side of (47) corresponding to W1,...,Wi that is not included in κ˜1 either satisﬁes |V ∪ W1 ∪ ... ∪ Wi| > k or the sets V,W1,...,Wi are not pairwise disjoint. Let κ˜2 = κ˜(Vk)(S) − κ˜1 denote the total contribution of these terms. Since for every W, Harris’s inequality implies

|f(W)| ≤

|π|!µπ ≤ |W||W| E[XW],

|κU(W)| ≤

U⊆W

π∈Π(W)

there is a constant K1 that depends only on k such that

|κ˜2| ≤ K1 E[XV ]

W1,...,Wi

- i
- j=1


E[XW

],

j

where the sum ranges over all i ≤ k − |V | and W1,...,Wi ⊆ S, each of size at most k − |V | and attaching to V , such that either |V ∪W1 ∪...∪Wi| > k or the sets V,W1,...,Wi are not pairwise disjoint. An argument analogous to the one given at the end of the proof of Lemma 31, employing Harris’s inequality and the stronger FKG lattice condition (14), gives

|κ˜2| ≤ K · δ1,K(V ) + ∆k+1,K(V ) for some K that depends only on k.

- Lemma 33. Let k ∈ N be such that ρk ≤ 1 − ε. Then there exists K = K(k,ε) such that for all V,S ⊆ [N] with 1 ≤ |V | ≤ k, we have


|q(V,S) − κ(Vk)(S)| ≤ K · δ1,K(V ) + ∆k+1,K(V ) .

Proof. We prove the lemma by complete induction on k. To this end, let k ≥ 0 and suppose that the statement holds for all k′ ∈ N with k′ < k. By the triangle inequality

|q(V,S) − κ(Vk)(S)| ≤ |q(V,S) − q(k)(V,S)|

+ |q(k)(V,S) − κ˜(Vk)(S)|

+ |κ˜(Vk)(S) − κ(Vk)(S)|. Lemmas 31 and 32 imply that

|q(V,S) − q(k)(V,S)| + |κ˜(Vk)(S) − κ(Vk)(S)| ≤ K1 · δ1,K

(V )

(V ) + ∆k+1,K

1

1

for some suﬃciently large K1 = K1(k,ε) and thus it suﬃces to show that there is some K2 = K2(k,ε) such that

|q(k)(V,S) − κ˜(Vk)(S)| ≤ K2 · δ1,K

(V ) . (48) To this end, observe ﬁrst that since k−|V | < k, then the induction hypothesis states that there

(V ) + ∆k+1,K

2

2

is a constant K′ = K′(k,ε) such that

q(U,S ∩ I(V )) − κU(k−|V |)(S ∩ I(V )) ≤ K′ · δ1,K′(U) + ∆k−|V |+1,K′(U) (49) for all U such that 1 ≤ |U| ≤ k − |V |. Let

κU(k−|V |)(S ∩ I(V ))

x =

U⊆S,U֒→V 1≤|U|≤k−|V |

and, as in the proof of Lemma 31, y =

q(U,S ∩ I(V )).

U⊆S,U֒→V 1≤|U|≤k−|V |

Observe that

ε−1 E[XU],

|y| ≤ z :=

U֒→V 1≤|U|≤k−|V |

as in the proof of Lemma 31, and that (49) implies that |x − y| ≤ w := K′ ·

δ1,K′(U) + ∆k−|V |+1,K′(U) . (50)

U֒→V 1≤|U|≤k−|V |

For any i ≥ 1, we have

|xi − yi| ≤ |x − y| ·

- i−1
- j=0


|xjyi−1−j| ≤ |x − y| · (|x| + |y|)i−1 ≤ w(2z + w)i−1.

It follows that

|q(k)(V,S) − κ˜(Vk)(S)| ≤

E[XV ] · w(2z + w)i−1. (51)

1≤i≤k−|V |

Similarly as in the proofs of Lemmas 31 and 32, one sees that the FKG lattice condition (14) implies that the right hand side of (51) is bounded from above by K2 · δ1,K

(V ) , provided K2 = K2(k,ε) is suﬃciently large, as claimed.

(V ) + ∆k+1,K

2

2

Proof of Lemma 23. It follows from Lemma 33 that there is K1 = K1(k,ε) such that

ℓ∈[N] i∈[k] V ∈Ci(ℓ)

q(V,[ℓ − 1]) − κ(Vk)(S)

(V ) . (52)

(V ) + ∆k+1,K

K1 · δ1,K

≤

1

1

ℓ∈[N] i∈[k] V ∈Ci(ℓ)

But if we choose K suﬃciently large then the right-hand side is at most K · δ1,K + ∆k+1,K , as required.

- 3.4. Proof of Lemma 24. Fix an integer k and an ℓ ∈ [N]. Recalling (21), we rewrite the ℓth term of the sum from the statement of the lemma as follows:


κ(Vk)([ℓ − 1]) =

(−1)|W|−1κV (W).

i∈[k] V ∈Ci(ℓ) V ⊆W⊆V ∪[ℓ−1] W֒→V |W|≤k

i∈[k] V ∈Ci(ℓ)

It follows from Deﬁnition 21 that if V is connected then W ֒→ V if and only if W is connected. Therefore, changing the order of the last two sums in the right-hand side of the above identity yields

κ(Vk)([ℓ − 1]) =

(−1)|W|−1κV (W), (53)

i∈[k] W∈Ci(ℓ) V ∈CW

i∈[k] V ∈Ci(ℓ)

where CW denotes the collection of all connected sets V ⊆ W satisfying max V = max W. We claim that for each W ∈ Ci(ℓ),

κ(W) =

V ∈CW

κV (W). (54)

Observe ﬁrst that establishing this claim completes the proof of the lemma. Indeed, substituting (54) into (53) and summing over all ℓ gives

κ(Vk)([ℓ − 1]) =

(−1)|W|−1κ(W)

i∈[k] ℓ∈[N] W∈Ci(ℓ)

ℓ∈[N] i∈[k] V ∈Ci(ℓ)

(−1)i−1

κ(W) =

=

W∈Ci

i∈[k]

(−1)i−1κi.

i∈[k]

Therefore, we only need to prove the claim. To this end, ﬁx a W ∈ Ci(ℓ). Recalling (15) and (20), it clearly suﬃces to show that {ΠCV (W) : V ∈ CW} is a partition of Π(W). Obviously, ΠCV (W) ⊆ Π(W) for each V ∈ CW. Conversely, given an arbitrary π ∈ Π(W), let P ∈ π be the part containing max W and let V be the connected component of max W in GΓ[P]. Clearly,

- V ∈ CW and π ∈ ΠCV (W). Moreover, the connected component of maxW in GΓ[P] is the only set V with this property, and so the sets ΠCV (W) and ΠCU(W) are disjoint for distinct U,V ∈ CW.


4. Computations

The goal of this section is to carry out the necessary computations for proving Corollaries 14, 15, and 17.

- 4.1. Corollaries 14 and 15. Assume that F = {F1,...,Ft} is a collection of pairwise nonisomorphic r-graphs without isolated vertices and let the associated hypergraph Γ = (Ω,X) be


deﬁned as in Section 1.5. To prove Corollaries 14 and 15, we need to compute the quantities κk for small values of k. This can be done using the following general approach: We ﬁrst enumerate all ‘isomorphism types’ of clusters in Ck. Then we compute the joint cumulant for each isomorphism type. Finally we multiply each value with the size of the respective isomorphism class. This is made more precise as follows.

- Deﬁnition 34. An F-complex is a non-empty set of subgraphs of Kn, each of which is isomorphic to a graph in F. An F-complex B is irreducible if it cannot be written as the union of two Fcomplexes B1 and B2 where every graph in B1 is edge-disjoint from every graph in B2. The set of all irreducible F-complexes of cardinality k is denoted by Ck(F). The underlying graph GB of an F-complex B is the subgraph of Kn formed by taking the union of (the edge sets of) the graphs in B.

Note that there is a natural bijection φ between the sets V ⊆ [N] of size k and the F-complexes of size k: φ maps V = {i1,...,ik} to the F-complex B = {G1,...,Gk}, where Gj is the subgraph of Kn spanned by the edges in γi

j

(recall that γi

j

is a set of edges in Kn and that we assume that none of the graphs in F have isolated vertices). Note also that φ|C

k

is a bijection between Ck and Ck(F). We can therefore write κ(B) for the joint cumulant of {Xi : i ∈ φ−1(B)} without ambiguity, obtaining

κk =

B∈Ck(F)

κ(B).

Using (7) we easily express κ(B) in terms of GB: κ(B) =

π∈Π(B)

(|π| − 1)!(−1)|π|−1

B′∈π

pe

G

B′

. (55)

- Deﬁnition 35. Let B1 and B2 be F-complexes. A map f : V (GB


) is a homomorphism from B1 to B2 if for every graph H ∈ B1, the graph f(H) (with vertex set f(V (H)) and edge set {{f(u),f(v)} : {u,v} ∈ E(H)}) belongs to B2. If f is bijective and both f and f−1 are homomorphisms, then f is an isomorphism. We denote by Aut(B) the group of automorphisms of B, that is of isomorphisms from B to B.

) → V (GB

2

1

It is easy to see that κ assigns equal values to isomorphic F-complexes. The following simple lemma can then be used to compute the values κk. In the sequel, we will denote by ni the falling factorial n(n − 1)···(n − i + 1).

![image 87](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile87.png>)

Lemma 36. Let Ck(F)/∼= be the set of isomorphism types of F-complexes in Ck(F). Then

nvG

B

![image 88](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile88.png>)

.

κ(B) =

κ(B) ·

![image 89](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile89.png>)

|Aut(B)|

[B]∈Ck(F)/∼=

B∈Ck(F)

Proof. For each isomorphism type [B], there are nvG

ways to place the vertices of GB into Kn; this way, every element of Ck(F) isomorphic to B is counted once for every automorphism of B.

B

![image 90](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile90.png>)

- Proof of Corollary 14. Suppose that F = {K3,C4} and that p = o(n−4/5). Since both K3 and C4 are 2-balanced and


min m2(K3),m2(C4) = min{2,3/2} ≥ 5/4, we can apply Corollary 13, which states that the probability that Gn,p is simultaneously K3-free and C4-free is

exp − κ1 + κ2 − κ3 + O(∆4) + o(1) .

Figure 4 shows all seven non-isomorphic irreducible F-complexes of size at most two. Using Lemma 36, the contribution to κk from a given F-complex B of size k is

nvG

B

![image 91](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile91.png>)

κ(B) ·

.

![image 92](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile92.png>)

|Aut(B)|

- For the complexes shown in Figure 4, we can easily calculate |Aut(B)| manually; going through the ﬁgure from the top left to the bottom right, we obtain the values


6,8,4,4,4,2,2. Therefore

n4p4 8

n3p3 6

![image 93](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile93.png>)

![image 94](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile94.png>)

+

κ1 =

![image 95](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile95.png>)

![image 96](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile96.png>)

| | |
|---|---|


Figure 4. The irreducible {K3,C4}-complexes of size at most two. Copies of K3 are represented by the grey triangles and copies of C4 by the hatched or dotted 4-cycles.

and, since p = o(n−4/5), κ2 =

n4(p5 − p6) 4

n6(p7 − p8) 4

n5(p6 − p8) 4

n5(p6 − p7) 2

n4(p5 − p7) 2

![image 97](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile97.png>)

![image 98](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile98.png>)

![image 99](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile99.png>)

![image 100](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile100.png>)

![image 101](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile101.png>)

+

+

+

+

![image 102](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile102.png>)

![image 103](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile103.png>)

![image 104](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile104.png>)

![image 105](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile105.png>)

![image 106](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile106.png>)

n6p7 4

- 3n5p6

![image 107](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile107.png>)

![image 108](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile108.png>)

- 4


![image 109](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile109.png>)

=

+

+ o(1).

![image 110](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile110.png>)

When calculating κ3, we ﬁrst observe that the underlying graphs of the third F-complex and the ﬁfth F-complex in Figure 4 each contain a C4 that is not already part of the complex and that the graph of the bottom right F-complex contains a triangle that is not a part of the complex. Let κ′3 denote the contribution of the two F-complexes of size three that are obtained from one of these three complexes of size two by adding the ‘extra’ C4 or K3. Then

n4(p5 − 2p8 − p9 + 2p10) 4

n5(p6 − 3p10 + 2p12) 12

n5p6 12

![image 111](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile111.png>)

![image 112](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile112.png>)

![image 113](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile113.png>)

κ′3 =

+

=

+ o(1).

![image 114](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile114.png>)

![image 115](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile115.png>)

![image 116](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile116.png>)

On the other hand, the contribution of every other F-complex of to κ3 is at most in the order of (p + np2 + n2p3) · κ2, because, except in the two cases mentioned above, the graph of a complex of size three is obtained from the graph of a complex of size two by adding either a new edge, or a new vertex and two new edges, or two new vertices and three new edges. Using the assumption p = o(n−4/5), we get

(p + np2 + n2p3) · κ2 = O(n6p8 + n5p7 + n7p9 + n8p10) = o(1), and therefore

n5p6 12

![image 117](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile117.png>)

+ o(1).

κ3 =

![image 118](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile118.png>)

Since the F-complexes accounted for by κ′3 are ‘complete’ (in the sense that their graphs do not contain either a K3 or a C4 that is not already a part of the complex), a similar reasoning shows that

∆4 ≤ O (p + np2 + n2p3) · κ′3 + O (1 + p + np2 + n2p3) · (κ3 − κ′3) = o(1). Since our assumption on p implies that max{κ1,κ2,κ3} = o(n), we can replace ni by ni in the expressions for κ1,κ2,κ3, incurring only an additive error of o(1). Thus the probability that Gn,p with p = o(n−4/5) is simultaneously triangle-free and C4-free is asymptotically

![image 119](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile119.png>)

n4p4 8

n6p7 4

- 2n5p6

![image 120](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile120.png>)

- 3


n3p3 6

−

+

+

, as claimed.

exp −

![image 121](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile121.png>)

![image 122](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile122.png>)

![image 123](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile123.png>)

- Proof of Corollary 15. Suppose that F = {K3} and p = o(n−7/11). Since K3 is 2-balanced and m2(K3) = 2 ≥ 11/7, we can apply Corollary 13, which tells us that the probability that Gn,p is triangle-free is


exp − κ1 + κ2 − κ3 + κ4 + O(∆5) + o(1) .

In Figure 5 we see representations of all isomorphism types of irreducible F-complexes of size up to four. Generating a similar list of complexes of size ﬁve would most likely require the help of a computer.

Figure 5. The irreducible {K3}-complexes of size at most four. The four complexes in the bottom row are negligible when p = o(n−7/11).

By Lemma 36, the contribution to κk from the isomorphism type of an F-complex B of size k is

nvG

B

![image 124](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile124.png>)

.

κ(B) ·

![image 125](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile125.png>)

|Aut(B)|

- For the complexes shown in Figure 5, it is not too diﬃcult to calculate |Aut(B)| by hand. In fact, since the automorphism group of K3 comprises all 3! permutations of V (K3), automorphisms of {K3}-complexes are simply automorphisms of the 3-uniform hypergraphs involved2. For example, the leftmost F-complex in the second row has exactly two automorphisms: the trivial one, and the unique automorphism exchanging the vertices belonging to exactly one triangle. Under our assumptions on p, we have κk = ∆k + o(1) for k ∈ {3,4}. This is the case because |κk − ∆k| = O(p∆k) and


p∆3 ≤ O(n5p8 + n4p7) = o(1) and p∆4 ≤ p · O(1 + p + p2n) · ∆3 = o(1), as can be seen by looking at Figure 5.

Now we just work through the ﬁgure row by row (from the top left to the bottom right) and in this order, we compute (using the ﬁrst row)

- κ1 =

n3p3 6

![image 126](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile126.png>)

![image 127](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile127.png>)

,

- κ2 =

n4(p5 − p6) 4

![image 128](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile128.png>)

![image 129](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile129.png>)

,

- κ3 = ∆3 + o(1) =


n5p7 2

n5p7 12

n4p6 6

![image 130](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile130.png>)

![image 131](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile131.png>)

![image 132](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile132.png>)

+ o(1), and (using the other rows)

+

+

![image 133](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile133.png>)

![image 134](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile134.png>)

![image 135](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile135.png>)

n6p9 2

n6p9 6

n6p9 2

n6p9 2

![image 136](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile136.png>)

![image 137](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile137.png>)

![image 138](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile138.png>)

![image 139](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile139.png>)

+

+

+

+

κ4 = ∆4 + o(1) =

![image 140](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile140.png>)

![image 141](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile141.png>)

![image 142](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile142.png>)

![image 143](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile143.png>)

n6p9 48

n4p6 24 + O(n5p8) + o(1).

![image 144](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile144.png>)

![image 145](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile145.png>)

+

![image 146](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile146.png>)

![image 147](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile147.png>)

![image 148](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile148.png>)

2But for general F, it is wrong to think of an F-complex isomorphism as a hypergraph isomorphism.

The term O(n5p8) represents the contribution of the four complexes in the bottom row of Figure 5, which is o(1), as p = o(n−7/11). Finally, we have

∆5 = O(p∆4 + np2∆4 + n5p8 + n5p9) = O(n4p7 + n5p8 + n6p10 + n7p11) = o(1),

since the graph of an F-complex of size ﬁve must be obtained by adding either a new edge or a new vertex and two new edges to one of the graphs in Figure 5, or else it must be isomorphic to one of the ﬁrst three graphs in the bottom row of Figure 5 (as the graphs of the remaining complexes of size four contain only triangles that are already in the complex).

Finally, κ1 = n3p3/6 = (n3 − 3n2)p3/6 + o(1) and, since max{κ2,κ3,κ4} = o(n), we may replace the falling factorials ni in the remaining expressions by ni. Adding up the terms in −κ1 + κ2 − κ3 + κ4, we obtain that the probability that Gn,p with p = o(n−7/11) is triangle-free is asymptotically

![image 149](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile149.png>)

![image 150](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile150.png>)

n3p3 6

n4p5 4

7n5p7 12

n2p3 2

3n4p6 8

27n6p9 16

, as claimed.

exp −

+

−

+

−

+

![image 151](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile151.png>)

![image 152](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile152.png>)

![image 153](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile153.png>)

![image 154](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile154.png>)

![image 155](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile155.png>)

![image 156](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile156.png>)

- 4.2. Corollary 17. It only remains to prove Corollary 17.


Proof of Corollary 17. Let Γ be the hypergraph of r-APs in [n], as deﬁned in Section 1.6, and assume that p = o(n−4/7). Then by Corollary 16 with r = 3 and k = 2,

P[X = 0] = exp − κ1 + κ2 + O(∆3) + o(1) . It remains to calculate κ1, κ2, and ∆3. For i ∈ [n], the number of 3-APs containing i is f(i) =

n 2

+ min {i,n − i} + O(1),

![image 157](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile157.png>)

where min {i,n − i} counts the 3-APs that have i as their midpoint, and n/2 counts the others. Thus the total number of 3-APs in [n] is

n

n2 4

1 3

f(i) =

+ O(n),

![image 158](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile158.png>)

![image 159](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile159.png>)

i=1

and therefore (using np3 = o(1))

n2p3 4

+ o(1).

κ1 =

![image 160](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile160.png>)

If {i,j} is an edge in the dependency graph, then |γi ∩ γj| is either 1 or 2. The number of pairs γi,γj intersecting in two elements is at most n2 32 2, so the contribution of these pairs to κ2 is O(n2p4), which is o(1) by our assumption on p. The number of pairs {γi,γj} with i = j and |γi ∩ γj| ≥ 1 is precisely ni=1 f(2i) and hence the number M of pairs with |γi ∩ γj| = 1 satisﬁes

n

n

- 1

![image 161](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile161.png>)

- 2


f(i) 2

+ O(n2) =

f(i)2 + O(n2).

M =

i=1

i=1

Since

n

n

f(i)2 =

i=1

i=1

= 2

⌊n/2⌋

n/2 + min{i,n − i} 2 + O(n2) = 2

i=1

n3 3

7n3 12

(n/2)3 3

+ O(n2) =

+ O(n2)

−

![image 162](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile162.png>)

![image 163](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile163.png>)

![image 164](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile164.png>)

(n/2 + i)2 + O(n2)

and n2p4 = o(1), we have

7n3p5 24

κ2 = M(p5 − p6) + O n2(p4 − p6) =

+ o(1).

![image 165](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile165.png>)

Lastly, we claim that ∆3 = O(n4p7) = o(1). Since any two distinct numbers are contained in at most three 3-APs, we have |C3| = O(n4). Moreover, let C3∗ be the family of all {i,j,k} ∈ C3 such that |γi ∪ γj ∪ γk| < 7. A simple case analysis shows that

∆({Xi : i ∈ V }) = O(n2p5 + n3p6) = o(1).

V ∈C3∗

On the other hand, ∆({Xi : i ∈ V }) = p7 for every V ∈ C3 \ C3∗. Thus, ∆3 ≤ |C3|p7 +

∆({Xi : i ∈ V }) = O(n4p7 + n2p4 + n3p6) = o(1)

V ∈C3∗

and we conclude that the probability that [n]p is 3-AP-free is asymptotically exp −

n2p3 4

7n3p5 24

, as claimed.

+

![image 166](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile166.png>)

![image 167](<2017-mousset-probability-nonexistence-binomial-subsets_images/imageFile167.png>)

Acknowledgement. This project was started during the workshop of the research group of Angelika Steger in Buchboden in February 2014. We are grateful to the anonymous referee for their careful reading of this paper and many helpful suggestions; in particular, for pointing out a mistake in an earlier version of the paper.

References

- [1] C. Ahlbach, J. Usatine, and N. Pippenger. A combinatorial interpretation of the joint cumulant. arXiv:1211.0652 [math.CO].
- [2] N. Alon and J. H. Spencer. The Probabilistic Method. Wiley Series in Discrete Mathematics and Optimization. John Wiley & Sons, Inc., Hoboken, NJ, fourth edition, 2016.
- [3] J. Balogh, R. Morris, and W. Samotij. Independent sets in hypergraphs. J. Amer. Math. Soc., 28:669–709, 2015.
- [4] J. Balogh, R. Morris, W. Samotij, and L. Warnke. The typical structure of sparse Kr+1-free graphs. Trans. Amer. Math. Soc., 368:6439–6485, 2016.
- [5] B. Bollobás. Threshold functions for small subgraphs. Math. Proc. Cambridge Philos. Soc., 90:197–206, 1981.
- [6] B. Bollobás. The chromatic number of random graphs. Combinatorica, 8:49–55, 1988.
- [7] R. Boppana and J. Spencer. A useful elementary correlation inequality. J. Combin. Theory Ser. A, 50:305–307, 1989.
- [8] P. Erdős and A. Rényi. On the evolution of random graphs. Magyar Tud. Akad. Mat. Kutató Int. Közl., 5:17–61, 1960.
- [9] A. Frieze. On small subgraphs of random graphs. In Random graphs (Poznań, 1989), volume 2, pages 67–90. Wiley, New York, 1992.
- [10] T. E. Harris. A lower bound for the critical probability in a certain percolation process. Proc. Cambridge Philos. Soc., 56:13–20, 1960.
- [11] C. Hundack, H. J. Prömel, and A. Steger. Extremal graph problems for graphs with a color-critical vertex. Combin. Probab. Comput., 2:465–477, 1993.
- [12] S. Janson. Poisson approximation for large deviations. Random Structures Algorithms, 1:221–229, 1990.
- [13] S. Janson. New versions of Suen’s correlation inequality. In Proceedings of the Eighth International Conference on Random Structures and Algorithms (Poznan, 1997), volume 13, pages 467–483, 1998.
- [14] S. Janson, T. Łuczak, and A. Ruciński. An exponential bound for the probability of nonexistence of a speciﬁed subgraph in a random graph. In Random graphs ’87 (Poznań, 1987), pages 73–87. Wiley, Chichester, 1990.
- [15] S. Janson, T. Łuczak, and A. Rucinski. Random graphs. Wiley-Interscience Series in Discrete Mathematics and Optimization. Wiley-Interscience, New York, 2000.
- [16] M. Karoński and A. Ruciński. On the number of strictly balanced subgraphs of a random graph. In Graph theory (Łagów, 1981), volume 1018 of Lecture Notes in Math., pages 79–83. Springer, Berlin, 1983.
- [17] D. Osthus, H. J. Prömel, and A. Taraz. For which densities are random triangle-free graphs almost surely bipartite? Combinatorica, 23:105–150, 2003. Paul Erdős and his mathematics (Budapest, 1999).
- [18] H. J. Prömel and A. Steger. The asymptotic number of graphs not containing a ﬁxed color-critical subgraph. Combinatorica, 12:463–473, 1992.
- [19] Hans Jürgen Prömel and Angelika Steger. On the asymptotic structure of sparse triangle free graphs. J. Graph Theory, 21(2):137–151, 1996.
- [20] O. Riordan and L. Warnke. The Janson inequalities for general up-sets. Random Structures Algorithms, 46:391– 395, 2015.
- [21] D. Saxton and A. Thomason. Hypergraph containers. Invent. Math., 201:925–992, 2015.
- [22] K. Schürger. Limit theorems for complete subgraphs of random graphs. Period. Math. Hungar., 10:47–53, 1979.


- [23] D. Stark and N. Wormald. The probability of nonexistence of a subgraph in a moderately sparse random graph. Combin. Probab. Comput, 27(4):672–715, 2018.
- [24] W.-C. S. Suen. A correlation inequality and a Poisson limit theorem for nonoverlapping balanced subgraphs of a random graph. Random Structures Algorithms, 1:231–242, 1990.
- [25] N. C. Wormald. The perturbation method and triangle-free random graphs. In Proceedings of the Seventh International Conference on Random Structures and Algorithms (Atlanta, GA, 1995), volume 9, 1996.


Frank Mousset, School of Mathematical Sciences, Tel Aviv University, Tel Aviv 6997801, Israel E-mail address: moussetfrank@gmail.com

Andreas Noever, Department of Computer Science, ETH Zurich, 8092 Zurich, Switzerland E-mail address: andreas.noever@gmail.com

Konstantinos Panagiotou, Institute of Mathematics, University of Munich, D-80333 Munich, Ger-

many E-mail address: kpanagio@math.lmu.de Wojciech Samotij, School of Mathematical Sciences, Tel Aviv University, Tel Aviv 6997801,

Israel E-mail address: samotij@tauex.tau.ac.il

