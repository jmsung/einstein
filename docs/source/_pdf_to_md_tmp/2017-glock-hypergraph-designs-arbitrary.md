arXiv:1706.01800v2[math.CO]3Mar2020

HYPERGRAPH F-DESIGNS FOR ARBITRARY F

STEFAN GLOCK, DANIELA KUHN,¨ ALLAN LO AND DERYK OSTHUS

Abstract. We solve the existence problem for F-designs for arbitrary r-uniform hypergraphs F. In particular, this shows that, given any r-uniform hypergraph F, the trivially necessary divisibility conditions are suﬃcient to guarantee a decomposition of any suﬃciently large complete r-uniform hypergraph G = Kn(r) into edge-disjoint copies of F, which answers a question asked e.g. by Keevash. The graph case r = 2 forms one of the cornerstones of design theory and was proved by Wilson in 1975. The case when F is complete corresponds to the existence of block designs, a problem going back to the 19th century, which was ﬁrst settled by Keevash.

More generally, our results extend to F-designs of quasi-random hypergraphs G and of hypergraphs G of suitably large minimum degree. Our approach builds on results and methods we recently introduced in our new proof of the existence conjecture for block designs.

1. Introduction

- 1.1. Background. A hypergraph G is a pair (V,E), where V = V (G) is the vertex set of G and the edge set E is a set of subsets of V . We often identify G with E, in particular, we let


|G| := |E|. We say that G is an r-graph if every edge has size r. We let Kn(r) denote the complete r-graph on n vertices.

Let G and F be r-graphs. An F-decomposition of G is a collection F of copies of F in G such that every edge of G is contained in exactly one of these copies. (Throughout the paper, we always assume that F is non-empty without mentioning this explicitly.) More generally, an (F,λ)-design of G is a collection F of distinct copies of F in G such that every edge of G is contained in exactly λ of these copies. Such a design can only exist if G satisﬁes certain divisibility conditions (e.g. if F is a graph triangle and λ = 1, then G must have even vertex degrees and the number of edges must be a multiple of three). If F is complete, such designs are also referred to as block designs.

The question of the existence of such designs goes back to the 19th century. The ﬁrst general result was due to Kirkman [17], who proved the existence of Steiner triple systems (i.e. triangle decompositions of complete graphs) under the appropriate divisibility conditions. In a groundbreaking series of papers which transformed the area, Wilson [32, 33, 34, 35] solved the existence problem in the graph setting (i.e. when r = 2) by showing that the trivially necessary divisibility conditions imply the existence of (F,λ)-designs in Kn(2) for suﬃciently large n. More generally, the existence conjecture postulated that the necessary divisibility conditions are also suﬃcient to ensure the existence of block designs with given parameters in Kn(r).

Answering a question of Erd˝os and Hanani [10], Ro¨dl [27] was able to give an approximate solution to the existence conjecture by constructing near optimal packings of edge-disjoint copies of Kf(r) in Kn(r), i.e. packings which cover almost all the edges of Kn(r). (For this, he introduced his now famous Ro¨dl nibble method, which has since had a major impact in many areas.) More recently, Kuperberg, Lovett and Peled [22] were able to prove probabilistically the existence of

![image 1](<2017-glock-hypergraph-designs-arbitrary_images/imageFile1.png>)

Date: 4th March 2020. This preprint has been merged with ‘The existence of designs via iterative absorption’ (arXiv:1611.06827v1)

into a single paper ‘The existence of designs via iterative absorption: hypergraph F-designs for arbitrary F’ (arXiv:1611.06827v3). The research leading to these results was partially supported by the EPSRC, grant nos. EP/N019504/1 (D. Ku¨hn) and EP/P002420/1 (A. Lo), by the Royal Society and the Wolfson Foundation (D. Ku¨hn) as well as by the European Research Council under the European Union’s Seventh Framework Programme (FP/2007–2013) / ERC Grant Agreement no. 306349 (S. Glock and D. Osthus).

1

non-trivial designs for a large range of parameters (but their result requires that λ is comparatively large). Apart from this, progress for r ≥ 3 was mainly limited to explicit constructions for rather restrictive parameters (see e.g. [7, 31]).

In a recent breakthrough, Keevash [15] proved the existence of (Kf(r),λ)-designs in Kn(r) for arbitrary (but ﬁxed) r,f and λ, provided n is suﬃciently large. In particular, his result implies the existence of Steiner systems for any admissible range of parameters as long as n is suﬃciently large compared to f (Steiner systems are block designs with λ = 1). The approach in [15] involved randomised algebraic constructions and yielded a far-reaching generalisation to block designs in quasirandom r-graphs. This in turn was extended in [12], where we developed a nonalgebraic approach based on iterative absorption, which additionally yielded resilience versions and the existence of block designs in hypergraphs of large minimum degree. This naturally raises the question of whether F-designs also exist for arbitrary r-graphs F. Here, we answer this aﬃrmatively, by building on methods and results from [12].

- 1.2. F-designs in quasirandom hypergraphs. We now describe the degree conditions which are trivially necessary for the existence of an F-design in an r-graph G. For a set S ⊆ V (G) with 0 ≤ |S| ≤ r, the (r − |S|)-graph G(S) has vertex set V (G) \ S and contains all (r − |S|)-subsets of V (G) \ S that together with S form an edge in G. (G(S) is often called the link graph of S.) Let δ(G) and ∆(G) denote the minimum and maximum (r − 1)-degree of an r-graph G, respectively, that is, the minimum/maximum value of |G(S)| over all S ⊆ V (G) of size r−1. For a (non-empty) r-graph F, we deﬁne the divisibility vector of F as Deg(F) := (d0,... ,dr−1) ∈ Nr,


where di := gcd{|F(S)| : S ∈ V (iF) }, and we set Deg(F)i := di for 0 ≤ i ≤ r − 1. Note that d0 = |F|. So if F is the Fano plane, we have Deg(F) = (7,3,1).

Given r-graphs F and G, G is called (F,λ)-divisible if Deg(F)i | λ|G(S)| for all 0 ≤ i ≤ r − 1

and all S ∈ V (iG) . Note that G must be (F,λ)-divisible in order to admit an (F,λ)-design. For simplicity, we say that G is F-divisible if G is (F,1)-divisible. Thus F-divisibility of G is

necessary for the existence of an F-decomposition of G.

As a special case, the following result implies that (F,λ)-divisibility is suﬃcient to guarantee the existence of an (F,λ)-design when G is complete and λ is not too large. This answers a question asked e.g. by Keevash [15].

In fact, rather than requiring G to be complete, it suﬃces that G is quasirandom in the following sense. An r-graph G on n vertices is called (c,h,p)-typical if for any set A of (r − 1)subsets of V (G) with |A| ≤ h we have | S∈A G(S)| = (1 ± c)p|A|n. Note that this is what one would expect in a random r-graph with edge probability p.

Theorem 1.1 (F-designs in typical hypergraphs). For all f,r ∈ N with f > r and all c,p ∈ (0,1] with

- q + r
- r


c ≤ 0.9(p/2)h/(qr4q), where q := 2f · f! and h := 2r

,

there exist n0 ∈ N and γ > 0 such that the following holds for all n ≥ n0. Let F be any r-graph on f vertices and let λ ∈ N with λ ≤ γn. Suppose that G is a (c,h,p)-typical r-graph on n vertices. Then G has an (F,λ)-design if it is (F,λ)-divisible.

The main result in [15] is also stated in the setting of typical r-graphs, but additionally requires that c ≪ 1/h ≪ p,1/f and that λ = O(1) and F is complete. The case when F is complete and λ is bounded is also a special case of our recent result on designs in supercomplexes (see Theorem 1.4 in [12]). Previous results in the case when r ≥ 3 and F is not complete are very sporadic – for instance Hanani [13] settled the problem if F is an octahedron (viewed as a 3-uniform hypergraph) and G is complete.

As a very special case, Theorem 1.1 resolves a conjecture of Archdeacon on self-dual embeddings of random graphs in orientable surfaces: as proved in [2], a graph has such an embedding if it has a decomposition into K := K4(2) and K′ := K5(2). Suppose G is a (c,h,p)-typical 2-graph on n vertices with an even number of edges and 1/n ≪ c ≪ 1/h ≪ p (which almost surely holds for the binomial random graph Gn,p if we remove at most one edge). Now remove a suitable

number of copies of K from G to ensure that the leftover G′ satisﬁes 16 | |G′|. Let F be the vertex-disjoint union of K and K′. Since Deg(F)1 = 1, G′ is F-divisible. Thus we can apply

- Theorem 1.1 to obtain an F-decomposition of G′. If the number of edges is odd, a similar argument yields self-dual embeddings in non-orientable surfaces.

In Section 8, we will deduce Theorem 1.1 from a more general result on F-decompositions in supercomplexes G (Theorem 3.8). (The condition of G being a supercomplex is considerably less restrictive than typicality.) Moreover, the F-designs we obtain will have the additional property that |V (F′) ∩ V (F′′)| ≤ r for all distinct F′,F′′ which are included in the design. It is easy to see that with this additional property the bound on λ in Theorem 1.1 is best possible up to the value of γ.

We can also deduce the following result which yields ‘near-optimal’ F-packings in typical r-graphs which are not divisible. (An F-packing in G is a collection of edge-disjoint copies of F in G.)

- Theorem 1.2. For all f,r ∈ N with f > r and all c,p ∈ (0,1] with


- q + r
- r


c ≤ 0.9ph/(qr4q), where q := 2f · f! and h := 2r

,

there exist n0,C ∈ N such that the following holds for all n ≥ n0. Let F be any r-graph on f vertices. Suppose that G is a (c,h,p)-typical r-graph on n vertices. Then G has an F-packing F such that the leftover L consisting of all uncovered edges satisﬁes ∆(L) ≤ C.

- 1.3. F-designs in hypergraphs of large minimum degree. Once the existence question is settled, a next natural step is to seek F-designs and F-decompositions in r-graphs of large minimum degree. Our next result gives a bound on the minimum degree which ensures an F-decomposition for ‘weakly regular’ r-graphs F. These are deﬁned as follows.


Deﬁnition 1.3 (weakly regular). Let F be an r-graph. We say that F is weakly (s0,... ,sr−1)regular if for all 0 ≤ i ≤ r − 1 and all S ∈ V (iF) , we have |F(S)| ∈ {0,si}. We simply say that F is weakly regular if it is weakly (s0,... ,sr−1)-regular for suitable si’s.

So for example, cliques, the Fano plane and the octahedron are all weakly regular but a 3-uniform tight or loose cycle is not. Theorem 1.4 (F-decompositions in hypergraphs of large minimum degree). Let F be a weakly regular r-graph on f vertices. Let

r! 3 · 14rf2r

c⋄F :=

.

![image 2](<2017-glock-hypergraph-designs-arbitrary_images/imageFile2.png>)

There exists an n0 ∈ N such that the following holds for all n ≥ n0. Suppose that G is an r-graph on n vertices with δ(G) ≥ (1 − c⋄F)n. Then G has an F-decomposition if it is F-divisible.

Note that Theorem 1.4 implies that every packing of edge-disjoint copies of F into Kn(r) with overall maximum degree at most c⋄Fn can be extended into an F-decomposition of Kn(r) (provided Kn(r) is F-divisible).

An analogous (but signiﬁcantly worse) constant c⋄F for r-graphs F which are not weakly regular immediately follows from the case p = 1 of Theorem 1.1. These results lead to the concept of the ‘decomposition threshold’ δF of a given r-graph F.

- Deﬁnition 1.5 (Decomposition threshold). Given an r-graph F, let δF be the inﬁmum of all δ ∈ [0,1] with the following property: There exists n0 ∈ N such that for all n ≥ n0, every F-divisible r-graph G on n vertices with δ(G) ≥ δn has an F-decomposition.


By Theorem 1.4, we have δF ≤ 1 − c⋄F whenever F is weakly regular. As noted in [12], for all r,f,n0 ∈ N, there exists an r-graph Gn on n ≥ n0 vertices with δ(Gn) ≥ (1 − br flogr−f1)n such that Gn does not contain a single copy of Kf(r), where br > 0 only depends on r. (This can be seen by adapting a construction from [19] which is based on a result from [29].)

![image 3](<2017-glock-hypergraph-designs-arbitrary_images/imageFile3.png>)

Previously, the only positive result for the hypergraph case r ≥ 3 was due to Yuster [36], who showed that if T is a linear r-uniform hypertree, then every T-divisible r-graph G on n vertices with minimum vertex degree at least (2r1−1 + o(1)) r− n1 has a T-decomposition. This is asymptotically best possible for nontrivial T. Moreover, the result implies that δT ≤ 1/2r−1.

![image 4](<2017-glock-hypergraph-designs-arbitrary_images/imageFile4.png>)

For the graph case r = 2, much more is known about the decomposition threshold: the results in [4, 11] establish a close connection between δF and the fractional decomposition threshold δF∗ (which is deﬁned as in Deﬁnition 1.5, but with an F-decomposition replaced by a fractional F-decomposition). In particular, the results in [4, 11] imply that δF ≤ max{δF∗ ,1−1/(χ(F)+1)} and that δF = δF∗ if F is a complete graph.

Together with recent results on the fractional decomposition threshold for cliques in [3, 8], this gives the best current bounds on δF for general F. It would be very interesting to establish a similar connection in the hypergraph case.

Also, for bipartite graphs the decomposition threshold was completely determined in [11]. It would be interesting to see if this can be generalised to r-partite r-graphs. On the other hand, even the decomposition threshold of a graph triangle is still unknown (a beautiful conjecture of Nash-Williams [24] would imply that the value is 3/4).

- 1.4. Counting. An approximate F-decomposition of Kn(r) is a set of edge-disjoint copies of F in Kn(r) which together cover almost all edges of Kn(r). Given good bounds on the number of

approximate F-decompositions of Kn(r) whose set of leftover edges forms a typical r-graph, one can apply Theorem 1.1 to obtain corresponding bounds on the number of F-decompositions

in Kn(r) (see [15, 16] for the clique case). Such bounds on the number of approximate Fdecompositions can be achieved by considering either a random greedy F-removal process or an associated F-nibble removal process.

- 1.5. Outline of the paper. As mentioned earlier, our main result (Theorem 3.8) actually concerns F-decompositions in so-called supercomplexes. We will deﬁne supercomplexes in Section 3 and derive Theorems 1.1, 1.2 and 1.4 from Theorem 3.8 in Section 8. The deﬁnition of a supercomplex G involves mainly the distribution of cliques of size f in G (where f = |V (F)|). The notion is weaker than usual notions of quasirandomness. This has two main advantages: ﬁrstly, our proof is by induction on r, and working with this weaker notion is essential to make the induction proof work. Secondly, this allows us to deduce Theorems 1.1, 1.2 and 1.4 from a single statement.


However, Theorem 3.8 applies only to F-decompositions of a supercomplex G for weakly regular r-graphs F (which allows us to deduce Theorem 1.4 but not Theorem 1.1). To deal with this, in Section 8 we ﬁrst provide an explicit construction which shows that every r-graph F can be ‘perfectly’ packed into a suitable weakly regular r-graph F∗. In particular, F∗ has an F-decomposition. The idea is then to apply Theorem 3.8 to ﬁnd an F∗-decomposition in G. Unfortunately, G may not be F∗-divisible. To overcome this, in Section 9 we show that we can remove a small set of copies of F from G to achieve that the leftover G′ of G is now F∗-divisible (see Lemma 8.4 for the statement). This now implies Theorem 1.1 for F-decompositions, i.e. for λ = 1. However, by repeatedly applying Theorem 3.8 in a suitable way, we can actually allow λ to be as large as required in Theorem 1.1.

It thus remains to prove Theorem 3.8 itself. We achieve this via the iterative absorption method. The idea is to iteratively extend a packing of edge-disjoint copies of F until the set H of uncovered edges is very small. This ﬁnal set can then be ‘absorbed’ into an r-graph A we set aside at the beginning of the proof (in the sense that A ∪ H has an F-decomposition). This iterative approach to decompositions was ﬁrst introduced in [18, 21] in the context of Hamilton decompositions of graphs. (Absorption itself was pioneered earlier for spanning structures e.g. in [20, 28], but as remarked e.g. in [15], such direct approaches are not feasible in the decomposition setting.)

This approach relies on being able to ﬁnd a suitable approximate F-decomposition in each iteration, whose existence we derive in Section 5. The iteration process is underpinned by a so-called ‘vortex’, which consists of an appropriate nested sequence of vertex subsets of G (after

each iteration, the current set of uncovered edges is constrained to the next vertex subset in the sequence). These vortices are discussed in Section 6. The ﬁnal absorption step is described in Section 7.

As mentioned earlier, the current proof builds on the framework introduced in [12]. In fact, several parts of the argument in [12] can either be used directly or can be straightforwardly adapted to the current setting. In particular, this applies to the Cover down lemma (Lemma 6.9), which is the key result that allows the iteration to work. Thus in the current paper we concentrate on the parts which involve signiﬁcant new ideas (e.g. the absorption process). For details of the parts which can be straightforwardly adapted, we refer to the appendix. Altogether, this illustrates the versatility of our framework and we thus believe that it can be developed in further settings.

As a byproduct of the construction of the weakly regular r-graph F∗ outlined above, we prove the existence of resolvable clique decompositions in complete partite r-graphs G (see Theorem 8.1). The construction is explicit and exploits the property that all square submatrices of so-called Cauchy matrices over ﬁnite ﬁelds are invertible. We believe this construction to be of independent interest. A natural question leading on from the current work would be to obtain such resolvable decompositions also in the general (non-partite) case. For decompositions of

Kn(2) into Kf(2), this is due to Ray-Chaudhuri and Wilson [26]. For recent progress see [9, 23].

2. Notation

- 2.1. Basic terminology. We let [n] denote the set {1,... ,n}, where [0] := ∅. Moreover, let [n]0 := [n] ∪ {0} and N0 := N ∪ {0}. As usual, ni denotes the binomial coeﬃcient, where we set ni := 0 if i > n or i < 0. Moreover, given a set X and i ∈ N0, we write Xi for the collection of all i-subsets of X. Hence, Xi = ∅ if i > |X|. If F is a collection of sets, we deﬁne

- F := f∈F f. We write A ∪· B for the union of A and B if we want to emphasise that A and


B are disjoint.

We write X ∼ B(n,p) if X has binomial distribution with parameters n,p, and we write bin(n,p,i) := ni pi(1 − p)n−i. So by the above convention, bin(n,p,i) = 0 if i > n or i < 0.

We say that an event holds with high probability (whp) if the probability that it holds tends to 1 as n → ∞ (where n usually denotes the number of vertices).

We write x ≪ y to mean that for any y ∈ (0,1] there exists an x0 ∈ (0,1) such that for all x ≤ x0 the subsequent statement holds. Hierarchies with more constants are deﬁned in a similar way and are to be read from the right to the left. We will always assume that the constants in our hierarchies are reals in (0,1]. Moreover, if 1/x appears in a hierarchy, this implicitly means that x is a natural number. More precisely, 1/x ≪ y means that for any y ∈ (0,1] there exists an x0 ∈ N such that for all x ∈ N with x ≥ x0 the subsequent statement holds.

We write a = b ± c if b − c ≤ a ≤ b + c. Equations containing ± are always to be interpreted from left to right, e.g. b1 ± c1 = b2 ± c2 means that b1 − c1 ≥ b2 − c2 and b1 + c1 ≤ b2 + c2.

When dealing with multisets, we treat multiple appearances of the same element as distinct elements. In particular, two subsets A,B of a multiset can be disjoint even if they both contain a copy of the same element, and if A and B are disjoint, then the multiplicity of an element in the union A∪B is obtained by adding the multiplicities of this element in A and B (rather than just taking the maximum).

- 2.2. Hypergraphs and complexes. Let G be an r-graph. Note that G(∅) = G. For a set


- S ⊆ V (G) with |S| ≤ r and L ⊆ G(S), let S ⊎ L := {S ∪ e : e ∈ L}. Clearly, there is a natural bijection between L and S ⊎ L.


For i ∈ [r−1]0, we deﬁne δi(G) and ∆i(G) as the minimum and maximum value of |G(S)| over all i-subsets S of V (G), respectively. As before, we let δ(G) := δr−1(G) and ∆(G) := ∆r−1(G). Note that δ0(G) = ∆0(G) = |G(∅)| = |G|.

For two r-graphs G and G′, we let G − G′ denote the r-graph obtained from G by deleting all edges of G′. We write G1 + G2 to mean the vertex-disjoint union of G1 and G2, and t · G to mean the vertex-disjoint union of t copies of G.

Let F and G be r-graphs. An F-packing in G is a set F of edge-disjoint copies of F in G. We let F(r) denote the r-graph consisting of all covered edges of G, i.e. F(r) = F′∈F F′.

A multi-r-graph G consists of a set of vertices V (G) and a multiset of edges E(G), where each e ∈ E(G) is a subset of V (G) of size r. We will often identify a multi-r-graph with its edge set. For S ⊆ V (G), let |G(S)| denote the number of edges of G that contain S (counted with multiplicities). If |S| = r, then |G(S)| is called the multiplicity of S in G. We say that G is F-divisible if Deg(F)|S| divides |G(S)| for all S ⊆ V (G) with |S| ≤ r − 1. An F-decomposition of G is a collection F of copies of F in G such that every edge e ∈ G is covered precisely once. (Thus if S ⊆ V (G) has size r, then there are precisely |G(S)| copies of F in F in which S forms an edge.)

- Deﬁnition 2.1. A complex G is a hypergraph which is closed under inclusion, that is, whenever

e′ ⊆ e ∈ G we have e′ ∈ G. If G is a complex and i ∈ N0, we write G(i) for the i-graph on V (G) consisting of all e ∈ G with |e| = i. We say that a complex is empty if ∅ ∈/ G(0), that is, if G does not contain any edges.

Suppose G is a complex and e ⊆ V (G). Deﬁne G(e) as the complex on vertex set V (G) \ e containing all sets e′ ⊆ V (G) \ e such that e ∪ e′ ∈ G. Clearly, if e ∈/ G, then G(e) is empty. Observe that if |e| = i and r ≥ i, then G(r)(e) = G(e)(r−i). We say that G′ is a subcomplex of

- G if G′ is a complex and a subhypergraph of G. For a set U, deﬁne G[U] as the complex on U ∩ V (G) containing all e ∈ G with e ⊆ U.


Moreover, for an r-graph H, let G[H] be the complex on V (G) with edge set G[H] := {e ∈ G :

e r ⊆ H},

and deﬁne G − H := G[G(r) − H]. So for i ∈ [r − 1], G[H](i) = G(i). For i > r, we might have G[H](i) G(i). Moreover, if H ⊆ G(r), then G[H](r) = H. Note that for an r1-graph H1 and an r2-graph H2, we have (G[H1])[H2] = (G[H2])[H1]. Also, (G − H1) − H2 = (G − H2) − H1, so we may write this as G − H1 − H2.

If G1 and G2 are complexes, we deﬁne G1 ∩ G2 as the complex on vertex set V (G1) ∩ V (G2)

containing all sets e with e ∈ G1 and e ∈ G2. We say that G1 and G2 are i-disjoint if G(1i) ∩G(2i) is empty.

For any hypergraph H, let H≤ be the complex on V (H) generated by H, that is,

H≤ := {e ⊆ V (H) : ∃e′ ∈ H such that e ⊆ e′}. For an r-graph H, we let H↔ denote the complex on V (H) that is induced by H, that is,

H↔ := {e ⊆ V (H) :

e r ⊆ H}.

Note that H↔(r) = H and for each i ∈ [r − 1]0, H↔(i) is the complete i-graph on V (H). We let Kn denote the the complete complex on n vertices.

3. Decompositions of supercomplexes

- 3.1. Supercomplexes. We prove our main decomposition theorem for so-called ‘supercomplexes’, which were introduced in [12]. The crucial property appearing in the deﬁnition is that of ‘regularity’, which means that every r-set of a given complex G is contained in roughly the same number of f-sets (where f = |V (F)|). If we view G as a complex which is induced by some r-graph, this means that every edge lies in roughly the same number of cliques of size f. It turns out that this set of conditions is appropriate even when F is not a clique.


A key advantage of the notion of a supercomplex is that the conditions are very ﬂexible, which will enable us to ‘boost’ their parameters (see Lemma 3.5 below). The following deﬁnitions are the same as in [12].

- Deﬁnition 3.1. Let G be a complex on n vertices, f ∈ N and r ∈ [f − 1]0, 0 ≤ ε,d,ξ ≤ 1. We say that G is


- (i) (ε,d,f,r)-regular, if for all e ∈ G(r) we have |G(f)(e)| = (d ± ε)nf−r;
- (ii) (ξ,f,r)-dense, if for all e ∈ G(r), we have |G(f)(e)| ≥ ξnf−r;
- (iii) (ξ,f,r)-extendable, if G(r) is empty or there exists a subset X ⊆ V (G) with |X| ≥ ξn


such that for all e ∈ Xr , there are at least ξnf−r (f − r)-sets Q ⊆ V (G) \ e such that

Q∪e

r \ {e} ⊆ G(r). We say that G is a full (ε,ξ,f,r)-complex if G is

- • (ε,d,f,r)-regular for some d ≥ ξ,
- • (ξ,f + r,r)-dense,
- • (ξ,f,r)-extendable.


We say that G is an (ε,ξ,f,r)-complex if there exists an f-graph Y on V (G) such that G[Y ] is a full (ε,ξ,f,r)-complex. Note that G[Y ](r) = G(r) (recall that r < f).

- Deﬁnition 3.2. (supercomplex) Let G be a complex. We say that G is an (ε,ξ,f,r)-supercomplex

if for every i ∈ [r]0 and every set B ⊆ G(i) with 1 ≤ |B| ≤ 2i, we have that b∈B G(b) is an (ε,ξ,f − i,r − i)-complex.

In particular, taking i = 0 and B = {∅} implies that every (ε,ξ,f,r)-supercomplex is also an (ε,ξ,f,r)-complex. Moreover, the above deﬁnition ensures that if G is a supercomplex and b,b′ ∈ G(i), then G(b) ∩ G(b′) is also a supercomplex (cf. Proposition 4.4).

The following examples from [12] demonstrate that the deﬁnition of supercomplexes generalises the notion of typicality.

- Example 3.3. Let 1/n ≪ 1/f and r ∈ [f−1]. Then the complete complex Kn is a (0,0.99/f!,f,r)supercomplex.
- Example 3.4. Suppose that 1/n ≪ c,p,1/f, that r ∈ [f − 1] and that G is a (c,2r f+r r ,p)typical r-graph on n vertices. Then G↔ is an (ε,ξ,f,r)-supercomplex, where


ε := 2f−r+1c/(f − r)! and ξ := (1 − 2f+1c)p2r(f+rr)/f!.

As mentioned above, the following lemma allows us to ‘boost’ the regularity parameters (and thus deduce results with ‘eﬀective’ bounds). It is an easy consequence of our Boost lemma (Lemma 5.2). The key to the proof is that we can (probabilistically) choose some Y ⊆ G(f) so that the parameters of G[Y ] in Deﬁnition 3.1(i) are better than those of G, i.e. the resulting distribution of f-sets is more uniform.

- Lemma 3.5 ([12]). Let 1/n ≪ ε,ξ,1/f and r ∈ [f − 1] with 2(2√e)rε ≤ ξ. Let ξ′ :=


![image 5](<2017-glock-hypergraph-designs-arbitrary_images/imageFile5.png>)

0.9(1/4)(f+fr)ξ. If G is an (ε,ξ,f,r)-complex on n vertices, then G is an (n−1/3,ξ′,f,r)-complex. In particular, if G is an (ε,ξ,f,r)-supercomplex, then it is a (2n−1/3,ξ′,f,r)-supercomplex.

- 3.2. The main complex decomposition theorem. The statement of our main complex decomposition theorem involves the concept of ‘well separated’ decompositions. This did not appear in [12], but is crucial for our inductive proof to work in the context of F-decompositions.


- Deﬁnition 3.6 (well separated). Let F be an r-graph and let F be an F-packing (in some r-graph G). We say that F is κ-well separated if the following hold:


- (WS1) for all distinct F′,F′′ ∈ F, we have |V (F′) ∩ V (F′′)| ≤ r.
- (WS2) for every r-set e, the number of F′ ∈ F with e ⊆ V (F′) is at most κ. We simply say that F is well separated if (WS1) holds.


For instance, any Kf(r)-packing is automatically 1-well separated. Moreover, if an F-packing F is 1-well separated, then for all distinct F′,F′′ ∈ F, we have |V (F′) ∩ V (F′′)| < r. On the other hand, if F is not complete, we cannot require |V (F′) ∩ V (F′′)| < r in (WS1): this would make it impossible to ﬁnd an F-decomposition of Kn(r). The notion of being well-separated is a natural relaxation of this requirement, we discuss this in more detail after stating Theorem 3.8.

We now deﬁne F-divisibility and F-decompositions for complexes G (rather than r-graphs G).

- Deﬁnition 3.7. Let F be an r-graph and f := |V (F)|. A complex G is F-divisible if G(r) is F-divisible. An F-packing in G is an F-packing F in G(r) such that V (F′) ∈ G(f) for all F′ ∈ F. Similarly, we say that F is an F-decomposition of G if F is an F-packing in G and F(r) = G(r).


Note that this implies that every copy F′ of F used in an F-packing in G is ‘supported’ by a clique, i.e. G(r)[V (F′)] ∼= Kf(r).

We can now state our main complex decomposition theorem.

- Theorem 3.8 (Main complex decomposition theorem). For all r ∈ N, the following is true.


(∗)r Let 1/n ≪ 1/κ,ε ≪ ξ,1/f and f > r. Let F be a weakly regular r-graph on f vertices and let G be an F-divisible (ε,ξ,f,r)-supercomplex on n vertices. Then G has a κ-well separated F-decomposition.

We will prove (∗)r by induction on r in Section 8. We do not make any attempt to optimise the values that we obtain for κ.

We now motivate Deﬁnitions 3.6 and 3.7. This involves the following additional concepts, which are also convenient later.

Deﬁnition 3.9. Let f := |V (F)| and suppose that F is a well separated F-packing. We let F≤ denote the complex generated by the f-graph {V (F′) : F′ ∈ F}. We say that well separated

F-packings F1,F2 are i-disjoint if F1≤,F2≤ are i-disjoint (or equivalently, if |V (F′) ∩ V (F′′)| < i for all F′ ∈ F1 and F′′ ∈ F2).

Note that if F is a well-separated F-packing, then the f-graph {V (F′) : F′ ∈ F} is simple. Moreover, observe that (WS2) is equivalent to the condition ∆r(F≤(f)) ≤ κ. Furthermore, if F is a well separated F-packing in a complex G, then F≤ is a subcomplex of G by Deﬁnition 3.7. Clearly, we have F(r) ⊆ F≤(r), but in general equality does not hold. On the other hand, if F is an F-decomposition of G, then F(r) = G(r) which implies F(r) = F≤(r).

We now discuss (WS1). During our proof, we will need to ﬁnd an F-packing which covers a given set of edges. This gives rise to the following task of ‘covering down locally’.

(⋆) Given a set S ⊆ V (G) of size 1 ≤ i ≤ r − 1, ﬁnd an F-packing F which covers all edges

- of G that contain S. (This is crucial in the proof of Lemma 6.9. Moreover, a two-sided version of this involving


sets S, S′ is needed to construct parts of our absorbers, see Section 7.1.)

A natural approach to achieve (⋆) is as follows: Let T ∈ V (iF) . Suppose that by using the main theorem inductively, we can ﬁnd an F(T)-decomposition F′ of G(S). We now wish to obtain F by ‘extending’ F′ as follows: For each copy F′ of F(T) in F′, we deﬁne a copy F⊳′ of F by ‘adding S back’, that is, F⊳′ has vertex set V (F′) ∪ S and S plays the role of T in F⊳′. Then F⊳′ covers all edges e with S ⊆ e and e \ S ∈ F′. Since F′ is an F(T)-decomposition of G(S), the union of all F⊳′ would indeed cover all edges of G that contain S, as desired. There are two issues with this ‘extension’ though. Firstly, it is not clear that F⊳′ is a subgraph of G. Secondly, for distinct F′,F′′ ∈ F′, it is not clear that F⊳′ and F⊳′′ are edge-disjoint. Deﬁnition 3.7 (and the succeeding remark) allows us to resolve the ﬁrst issue. Indeed, if F′ is an F(T)-decomposition of the complex G(S), then from V (F′) ∈ G(S)(f−i), we can deduce V (F⊳′) ∈ G(f) and thus that F⊳′ is a subgraph of G(r).

We now consider the second issue. This does not arise if F is a clique. Indeed, in that case

F(T) is a copy of Kf(r−−ii), and thus for distinct F′,F′′ ∈ F′ we have |V (F′) ∩ V (F′′)| < r − i. Hence |V (F⊳′) ∩ V (F⊳′′)| < r − i + |S| = r, i.e. F⊳′ and F⊳′′ are edge-disjoint. If however F is not a clique, then F′,F′′ ∈ F′ can overlap in r − i or more vertices (they could in fact have the same

vertex set), and the above argument does not work. We will show that under the assumption

- that F′ is well separated, we can overcome this issue and still carry out the above ‘extension’. (Moreover, the resulting F-packing F will in fact be well separated itself, see Deﬁnition 6.10 and Proposition 6.11). For this it is useful to note that F(T) is an (r − i)-graph, and thus we already have |V (F′) ∩ V (F′′)| ≤ r − i if F′ is well separated.


The reason why we also include (WS2) in Deﬁnition 3.6 is as follows. Suppose we have already found a well separated F-packing F1 in G and now want to ﬁnd another well separated F-packing F2 such that we can combine F1 and F2. If we ﬁnd F2 in G − F1(r), then F1(r) and

- F2(r) are edge-disjoint and thus F1 ∪ F2 will be an F-packing in G, but it is not necessarily well


separated. We therefore ﬁnd F2 in G−F1(r) −F1≤(r+1). This ensures that F1 and F2 are (r+1)disjoint, which in turn implies that F1 ∪ F2 is indeed well separated, as required. But in order

to be able to construct F2, we need to ensure that G − F1(r) − F1≤(r+1) is still a supercomplex, which is true if ∆(F1(r)) and ∆(F1≤(r+1)) are small (cf. Proposition 4.5). The latter in turn is ensured by (WS2) via Fact 4.3.

Finally, we discuss why we prove Theorem 3.8 for weakly regular r-graphs F. Most importantly, the ‘regularity’ of the degrees will be crucial for the construction of our absorbers (most notably in Lemma 7.22). Beyond that, weakly regular graphs also have useful closure properties (cf. Proposition 4.2): they are closed under taking link graphs and divisibility is inherited by link graphs in a natural way.

We prove Theorem 3.8 in Sections 5–7 and 8.1. As described in Section 1.5, we generalise this to arbitrary F via Lemma 8.2 (proved in Section 8.2) and Lemma 8.4 (proved in Section 9): Lemma 8.2 shows that for every given r-graph F, there is a weakly regular r-graph

- F∗ which has an F-decomposition. Lemma 8.4 then complements this by showing that every F-divisible r-graph G can be transformed into an F∗-divisible r-graph G′ by removing a sparse F-decomposable subgraph of G.


4. Tools

- 4.1. Basic tools. We will often use the following ‘handshaking lemma’ for r-graphs: Let G be an r-graph and 0 ≤ i ≤ k ≤ r − 1. Then for every S ∈ V (iG) we have


−1

r − i r − k

- (4.1) |G(T)|.


|G(S)| =

T∈(V(kG)): S⊆T

- Proposition 4.1. Let F be an r-graph. Then there exist inﬁnitely many n ∈ N such that Kn(r) is F-divisible.

Proof. Let p := i r=0−1 Deg(F)i. We will show that for every a ∈ N, if we let n = r!ap + r − 1 then Kn(r) is F-divisible. Clearly, this implies the claim. In order to see that Kn(r) is F-divisible, it is suﬃcient to show that p | nr−−ii for all i ∈ [r − 1]0. It is easy to see that this holds for the above choice of n.

The following proposition shows that the class of weakly regular uniform hypergraphs is closed under taking link graphs.

- Proposition 4.2. Let F be a weakly regular r-graph and let i ∈ [r−1]. Suppose that S ∈ V (iF) and that F(S) is non-empty. Then F(S) is a weakly regular (r − i)-graph and Deg(F(S))j = Deg(F)i+j for all j ∈ [r − i − 1]0.


Proof. Let s0,... ,sr−1 be such that F is weakly (s0,... ,sr−1)-regular. Note that since F is nonempty, we have sj > 0 for all j ∈ [r−1]0 (and the si’s are unique). Consider j ∈ [r−i−1]0. For all

- T ∈ V (Fj(S)) , we have |F(S)(T)| = |F(S ∪T)| ∈ {0,si+j}. Hence, F(S) is weakly (si,... ,sr−1)regular. Since F is non-empty, we have Deg(F) = (s0,... ,sr−1), and since F(S) is non-empty too by assumption, we have Deg(F(S)) = (si,... ,sr−1). Therefore, Deg(F(S))j = Deg(F)i+j


- for all j ∈ [r − i − 1]0.


We now list some useful properties of well separated F-packings.

Fact 4.3. Let G be a complex and F an r-graph on f > r vertices. Suppose that F is a κ-well separated F-packing (in G) and F′ is a κ′-well separated F-packing (in G). Then the following hold.

- (i) ∆(F≤(r+1)) ≤ κ(f − r).
- (ii) If F(r) and F′(r) are edge-disjoint and F and F′ are (r + 1)-disjoint, then F ∪ F′ is a (κ + κ′)-well separated F-packing (in G).
- (iii) If F and F′ are r-disjoint, then F ∪F′ is a max{κ,κ′}-well separated F-packing (in G).


- 4.2. Some properties of supercomplexes. The following properties of supercomplexes were proved in [12].


- Proposition 4.4 ([12]). Let G be an (ε,ξ,f,r)-supercomplex and let B ⊆ G(i) with 1 ≤ |B| ≤ 2i for some i ∈ [r]0. Then b∈B G(b) is an (ε,ξ,f − i,r − i)-supercomplex.
- Proposition 4.5 ([12]). Let f,r′ ∈ N and r ∈ N0 with f > r and r′ ≥ r. Let G be a complex on n ≥ r2r+1 vertices and let H be an r′-graph on V (G) with ∆(H) ≤ γn. Then the following hold:


- (i) If G is (ε,d,f,r)-regular, then G − H is (ε + 2rγ,d,f,r)-regular.
- (ii) If G is (ξ,f,r)-dense, then G − H is (ξ − 2rγ,f,r)-dense.
- (iii) If G is (ξ,f,r)-extendable, then G − H is (ξ − 2rγ,f,r)-extendable.
- (iv) If G is an (ε,ξ,f,r)-complex, then G − H is an (ε + 2rγ,ξ − 2rγ,f,r)-complex.
- (v) If G is an (ε,ξ,f,r)-supercomplex, then G − H is an (ε + 22r+1γ,ξ − 22r+1γ,f,r)supercomplex.


Corollary 4.6 ([12]). Let 1/n ≪ ε,γ,ξ,p,1/f and r ∈ [f − 1]. Let

f+r r

ξ′ := 0.95ξp2r(f+rr) ≥ 0.95ξp(8f) and γ′ := 1.1 · 2r

γ.

![image 6](<2017-glock-hypergraph-designs-arbitrary_images/imageFile6.png>)

(f − r)!

Suppose that G is an (ε,ξ,f,r)-supercomplex on n vertices and that H ⊆ G(r) is a random subgraph obtained by including every edge of G(r) independently with probability p. Then whp the following holds: for all L ⊆ G(r) with ∆(L) ≤ γn, G[H △ L] is a (3ε + γ′,ξ′ − γ′,f,r)supercomplex.

- 4.3. Rooted Embeddings. We now prove a result (Lemma 4.7) which allows us to ﬁnd edgedisjoint embeddings of graphs with a prescribed ‘root embedding’. Let T be an r-graph and suppose that X ⊆ V (T) is such that T[X] is empty. A root of (T,X) is a set S ⊆ X with |S| ∈ [r − 1] and |T(S)| > 0.


For an r-graph G, we say that Λ: X → V (G) is a G-labelling of (T,X) if Λ is injective. Our aim is to embed T into G such that the roots of (T,X) are embedded at their assigned position. More precisely, given a G-labelling Λ of (T,X), we say that φ is a Λ-faithful embedding of (T,X) into G if φ is an injective homomorphism from T to G with φ↾X = Λ. Moreover, for a set S ⊆ V (G) with |S| ∈ [r − 1], we say that Λ roots S if S ⊆ Im(Λ) and |T(Λ−1(S))| > 0, i.e. if Λ−1(S) is a root of (T,X).

The degeneracy of T rooted at X is the smallest D such that there exists an ordering v1,... ,vk of the vertices of V (T) \ X such that for every ℓ ∈ [k], we have

|T[X ∪ {v1,... ,vℓ}](vℓ)| ≤ D, i.e. every vertex is contained in at most D edges which lie to the left of that vertex in the ordering.

We need to be able to embed many copies of (T,X) simultaneously (with diﬀerent labellings) into a given host graph G such that the diﬀerent embeddings are edge-disjoint. In fact, we need a slightly stronger disjointness criterion. Ideally, we would like to have that two distinct embeddings intersect in less than r vertices. However, this is in general not possible because of the desired rooting. We therefore introduce the following concept of a hull. We will ensure that the hulls are edge-disjoint, which will be suﬃcient for our purposes. Given (T,X) as above, the

hull of (T,X) is the r-graph T′ on V (T) with e ∈ T′ if and only if e ∩ X = ∅ or e ∩ X is a root of (T,X). Note that T ⊆ T′ ⊆ KV(r()T) − KX(r), where KZ(r) denotes the complete r-graph with vertex set Z. Moreover, the roots of (T′,X) are precisely the roots of (T,X).

- Lemma 4.7. Let 1/n ≪ γ ≪ ξ,1/t,1/D and r ∈ [t]. Suppose that α ∈ (0,1] is an arbitrary scalar (which might depend on n) and let m ≤ αγnr be an integer. For every j ∈ [m], let Tj be an r-graph on at most t vertices and Xj ⊆ V (Tj) such that Tj[Xj] is empty and Tj has degeneracy


at most D rooted at Xj. Let G be an r-graph on n vertices such that for all A ⊆ Vr−(G1) with |A| ≤ D, we have | S∈A G(S)| ≥ ξn. Let O be an (r + 1)-graph on V (G) with ∆(O) ≤ γn. For every j ∈ [m], let Λj be a G-labelling of (Tj,Xj). Suppose that for all S ⊆ V (G) with |S| ∈ [r − 1], we have that

- (4.2) |{j ∈ [m] : Λj roots S}| ≤ αγnr−|S| − 1.

Then for every j ∈ [m], there exists a Λj-faithful embedding φj of (Tj,Xj) into G such that the following hold:

- (i) for all distinct j,j′ ∈ [m], the hulls of (φj(Tj),Im(Λj)) and (φj′(Tj′),Im(Λj′)) are edgedisjoint;
- (ii) for all j ∈ [m] and e ∈ O with e ⊆ Im(φj), we have e ⊆ Im(Λj);
- (iii) ∆( j∈[m] φj(Tj)) ≤ αγ(2−r)n.


Note that (i) implies that φ1(T1),... ,φm(Tm) are edge-disjoint. We also remark that the Tj do not have to be distinct; in fact, they could all be copies of a single r-graph T. Proof. For j ∈ [m] and a set S ⊆ V (G) with |S| ∈ [r − 1], let

root(S,j) := |{j′ ∈ [j] : Λj′ roots S}|.

We will deﬁne φ1,... ,φm successively. Once φj is deﬁned, we let Kj denote the hull of (φj(Tj),Im(Λj)). Note that φj(Tj) ⊆ Kj and that Kj is not necessarily a subgraph of G.

Suppose that for some j ∈ [m], we have already deﬁned φ1,... ,φj−1 such that K1,... ,Kj−1 are edge-disjoint, (ii) holds for all j′ ∈ [j − 1], and the following holds for Gj := j′∈[j−1] Kj′, all i ∈ [r − 1] and all S ∈ V (iG) :

- (4.3) |Gj(S)| ≤ αγ(2−i)nr−i + (root(S,j − 1) + 1)2t. Note that (4.3) together with (4.2) implies that for all i ∈ [r − 1] and all S ∈ V(iG) , we have
- (4.4) |Gj(S)| ≤ 2αγ(2−i)nr−i.

We will now deﬁne a Λj-faithful embedding φj of (Tj,Xj) into G such that Kj is edge-disjoint from Gj, (ii) holds for j, and (4.3) holds with j replaced by j + 1. For i ∈ [r − 1], deﬁne BADi := {S ∈ V (iG) : |Gj(S)| ≥ αγ(2−i)nr−i}. We view BADi as an i-graph. We claim that for all i ∈ [r − 1],

- (4.5) ∆(BADi) ≤ γ(2−r)n.


Consider i ∈ [r − 1] and suppose that there exists some S ∈ Vi−(G1) such that |BADi(S)| > γ(2−r)n. We then have that

1 r − i + 1

|Gj(S ∪ {v})| ≥ r−1

|Gj(S)| =

|Gj(S ∪ {v})|

![image 7](<2017-glock-hypergraph-designs-arbitrary_images/imageFile7.png>)

v∈BADi(S)

v∈V (G)\S

≥ r−1|BADi(S)|αγ(2−i)nr−i ≥ r−1γ(2−r)nαγ(2−i)nr−i = r−1αγ(2−r+2−i)nr−(i−1).

This contradicts (4.4) if i − 1 > 0 since 2−r + 2−i < 2−(i−1). If i = 1, then S = ∅ and we have |Gj| ≥ r−1αγ(2−r+2−1)nr, which is also a contradiction since |Gj| ≤ m r t ≤ r t αγnr and 2−r + 2−1 < 1 (as r ≥ 2 if i ∈ [r − 1]). This proves (4.5).

We now embed the vertices of Tj such that the obtained embedding φj is Λj-faithful. First, embed every vertex from Xj at its assigned position. Since Tj has degeneracy at most D rooted

at Xj, there exists an ordering v1,... ,vk of the vertices of V (Tj)\Xj such that for every ℓ ∈ [k], we have

- (4.6) |Tj[Xj ∪ {v1,... ,vℓ}](vℓ)| ≤ D.


Suppose that for some ℓ ∈ [k], we have already embedded v1,... ,vℓ−1. We now want to deﬁne φj(vℓ). Let U := {φj(v) : v ∈ Xj ∪ {v1,... ,vℓ−1}} be the set of vertices which have already been used as images for φj. Let A contain all (r−1)-subsets S of U such that φ−j 1(S)∪{vℓ} ∈ Tj. We need to choose φj(vℓ) from the set ( S∈A G(S)) \ U in order to complete φj to an injective homomorphism from Tj to G. By (4.6), we have |A| ≤ D. Thus, by assumption, | S∈A G(S)| ≥ ξn.

For i ∈ [r − 1], let Oi consist of all vertices x ∈ V (G) such that there exists some S ∈ i− U1 such that S ∪ {x} ∈ BADi (so BAD1 = O11 ). We have

(4.5)

|U| i − 1

t i − 1

γ(2−r)n.

|Oi| ≤

≤

∆(BADi)

Let Or consist of all vertices x ∈ V (G) such that S ∪ {x} ∈ Gj for some S ∈ r U−1 . By (4.4), we have that |Or| ≤ r |−U1| ∆(Gj) ≤ r− t1 2αγ(2−(r−1))n ≤ r− t1 γ(2−r)n. Finally, let Or+1 be the set of all vertices x ∈ V (G) such that there exists some S ∈ Ur such that S ∪ {x} ∈ O. By assumption, we have |Or+1| ≤ |Ur| ∆(O) ≤ r t γn.

Crucially, we have

r+1

|Oi| ≥ ξn − t − 2tγ(2−r)n > 0.

|

G(S)| − |U| −

i=1

S∈A

Thus, there exists a vertex x ∈ V (G) such that x ∈/ U ∪ O1 ∪ ··· ∪ Or+1 and S ∪ {x} ∈ G for all S ∈ A. Deﬁne φj(vℓ) := x.

Continuing in this way until φj is deﬁned for every v ∈ V (Tj) yields an injective homomorphism from Tj to G. By deﬁnition of Or+1, (ii) holds for j. Moreover, by deﬁnition of Or, Kj is edge-disjoint from Gj. It remains to show that (4.3) holds with j replaced by j+1. Let i ∈ [r−1]

and S ∈ V (iG) . If S ∈/ BADi, then we have |Gj+1(S)| ≤ |Gj(S)| + r t−−ii ≤ αγ(2−i)nr−i + 2t, so (4.3) holds. Now, assume that S ∈ BADi. If S ⊆ Im(Λj) and |Tj(Λ−j 1(S))| > 0, then root(S,j) = root(S,j −1)+1 and thus |Gj+1(S)| ≤ |Gj(S)|+ r t−−ii ≤ αγ(2−i)nr−i +(root(S,j − 1)+1)2t+ r t−−ii ≤ αγ(2−i)nr−i+(root(S,j)+1)2t and (4.3) holds. Suppose next that S  ⊆ Im(Λj). We claim that S  ⊆ V (φj(Tj)). Suppose, for a contradiction, that S ⊆ V (φj(Tj)). Let ℓ := max{ℓ′ ∈ [k] : φj(vℓ′) ∈ S}. (Note that the maximum exists since (S ∩V (φj(Tj)))\Im(Λj) is not empty.) Hence, x := φj(vℓ) ∈ S. Recall that when we deﬁned φj(vℓ), φj(v) had already been deﬁned for all v ∈ Xj ∪ {v1,... ,vℓ−1} and hence S \ {x} ⊆ U. But since S ∈ BADi, we have x ∈ Oi, in contradiction to x = φj(vℓ). Thus, S  ⊆ V (φj(Tj)) = V (Kj), which clearly implies that |Gj+1(S)| = |Gj(S)| and (4.3) holds. The last remaining case is if S ⊆ Im(Λj) but |Tj(Λ−j 1(S))| = 0. But then S is not a root of (φj(Tj),Im(Λj)) and thus not a root of (Kj,Im(Λj)). Hence |Kj(S)| = 0 and therefore |Gj+1(S)| = |Gj(S)| as well.

Finally, if j = m, then the fact that (4.3) holds with j replaced by j + 1 together with (4.2) implies that ∆( j∈[m] φj(Tj)) ≤ 2αγ(2−(r−1))n ≤ αγ(2−r)n.

5. Approximate F-decompositions

The majority of the edges which are covered during our iterative absorption procedure are covered by ‘approximate’ F-decompositions of certain parts of G, i.e. F-packings which cover almost all the edges in these parts. For cliques, the existence of such packings was ﬁrst proved by Ro¨dl [27], introducing what is now called the ‘nibble’ technique. Here, we derive a result on approximate F-decompositions which is suitable for our needs (Lemma 5.3).

We will derive the F-nibble lemma (Lemma 5.3) from the special case when F is a clique. This in turn was derived in [12] from a result in [1] which allows us to assume that the leftover of an approximate clique decomposition has appropriately bounded maximum degree.

- Lemma 5.1 (Boosted nibble lemma, [12]). Let 1/n ≪ γ,ε ≪ ξ,1/f and r ∈ [f − 1]. Let G be a complex on n vertices such that G is (ε,d,f,r)-regular and (ξ,f + r,r)-dense for some d ≥ ξ.


- Then G contains a Kf(r)-packing K such that ∆(G(r) − K(r)) ≤ γn. Crucially, we do not need to assume that ε ≪ γ in Lemma 5.1. The reason for this is the so-


called Boost lemma from [12], which allows us to ‘boost’ the regularity parameters of a suitable complex and which is an important ingredient in the proof of both Lemma 5.1 and Lemma 5.3.

- Lemma 5.2 (Boost lemma, [12]). Let 1/n ≪ ε,ξ,1/f and r ∈ [f − 1] such that 2(2√e)rε ≤ ξ.

![image 8](<2017-glock-hypergraph-designs-arbitrary_images/imageFile8.png>)

Let ξ′ := 0.9(1/4)(f+fr)ξ. Suppose that G is a complex on n vertices and that G is (ε,d,f,r)regular and (ξ,f + r,r)-dense for some d ≥ ξ. Then there exists Y ⊆ G(f) such that G[Y ] is (n−(f−r)/2.01,d/2,f,r)-regular and (ξ′,f + r,r)-dense.

We now prove an F-nibble lemma which allows us to ﬁnd κ-well separated approximate Fdecompositions in supercomplexes.

- Lemma 5.3 (F-nibble lemma). Let 1/n ≪ 1/κ ≪ γ,ε ≪ ξ,1/f and r ∈ [f − 1]. Let F be an r-graph on f vertices. Let G be a complex on n vertices such that G is (ε,d,f,r)-regular and (ξ,f + r,r)-dense for some d ≥ ξ. Then G contains a κ-well separated F-packing F such that ∆(G(r) − F(r)) ≤ γn.

Let F be an r-graph on f vertices. Given a collection K of edge-disjoint copies of Kf(r), we deﬁne the K-random F-packing F as follows: For every K ∈ K, choose a random bijection from V (F) to V (K) and let FK be a copy of F on V (K) embedded by this bijection. Let

- F := {FK : K ∈ K}. Clearly, if K is a Kf(r)-decomposition of a complex G, then the K-random F-packing F is a


1-well separated F-packing in G. Moreover, writing p := 1 − |F|/ fr , we have |F(r)| = |F||K| = |F||G(r)|/ fr = (1−p)|G(r)|, and for every e ∈ G(r), we have P(e ∈ G(r)−F(r)) = p. As turns out, the leftover G(r) − F(r) behaves essentially like a p-random subgraph of G(r) (cf. Lemma 5.4). Our strategy to prove Lemma 5.3 is thus as follows: We apply Lemma 5.1 to G to obtain a Kf(r)-packing K1 such that ∆(G(r) − K1(r)) ≤ γn. The leftover here is negligible, so assume for the moment that K1 is a Kf(r)-decomposition. We then choose a K1-random F-packing F1 in G and continue the process with G − F1(r). In each step, the leftover decreases by a factor of p. Thus after logp γ steps, the leftover will have maximum degree at most γn.

- Lemma 5.4. Let 1/n ≪ ε ≪ ξ,1/f and r ∈ [f − 1]. Let F be an r-graph on f-vertices with p := 1 − |F|/ fr ∈ (0,1). Let G be an (ε,d,f,r)-regular and (ξ,f + r,r)-dense complex on n


vertices for some d ≥ ξ. Suppose that K is a Kf(r)-decomposition of G. Let F be the K-random F-packing in G. Then whp the following hold for G′ := G − K≤(r+1) − F(r).

- (i) G′ is (2ε,p(fr)−1d,f,r)-regular;
- (ii) G′ is (0.9p(f+rr)−1ξ,f + r,r)-dense;
- (iii) ∆(G′(r)) ≤ 1.1p∆(G(r)).


Since the assertions follow easily from the deﬁnitions, we omit the proof here. We refer to Appendix A for the details.

Proof of Lemma 5.3. Let p := 1 − |F|/ fr . If F = Kf(r), then we are done by Lemma 5.1. We may thus assume that p ∈ (0,1). Choose ε′ > 0 such that 1/n ≪ ε′ ≪ 1/κ ≪ γ,ε ≪

p,1−p,ξ,1/f. We will now repeatedly apply Lemma 5.1. More precisely, let ξ0 := 0.9(1/4)(f+fr)ξ and deﬁne ξj := (0.5p)j(f+rr)ξ0 for j ≥ 1. For every j ∈ [κ]0, we will ﬁnd Fj and Gj such that the following hold:

- (a)j Fj is a j-well separated F-packing in G and Gj ⊆ G − Fj(r);
- (b)j ∆(Lj) ≤ jε′n, where Lj := G(r) − Fj(r) − G(jr);
- (c)j Gj is (2(r+1)jε′,dj,f,r)-regular and (ξj,f + r,r)-dense for some dj ≥ ξj;
- (d)j Fj≤ and Gj are (r + 1)-disjoint;
- (e)j ∆(G(jr)) ≤ (1.1p)jn.


First, apply Lemma 5.2 to G in order to ﬁnd Y ⊆ G(f) such that G0 := G[Y ] is (ε′,d/2,f,r)regular and (ξ0,f + r,r)-dense. Hence, (a)0–(e)0 hold with F0 := ∅. Also note that Fκ will be a κ-well separated F-packing in G and ∆(G(r)−Fκ(r)) ≤ ∆(Lκ)+∆(G(κr)) ≤ κε′n+(1.1p)κn ≤ γn, so we can take F := Fκ.

Now, assume that for some j ∈ [κ], we have found Fj−1 and Gj−1 and now need to ﬁnd Fj and Gj. By (c)j−1, Gj−1 is (

√

![image 9](<2017-glock-hypergraph-designs-arbitrary_images/imageFile9.png>)

ε′,dj−1,f,r)-regular and (ξj−1,f + r,r)-dense for some dj−1 ≥ ξj−1. Thus, we can apply Lemma 5.1 to obtain a Kf(r)-packing Kj in Gj−1 such that ∆(L′j) ≤ ε′n, where L′j := G(jr−)1 − Kj(r). Let G′j := Gj−1 − L′j. Clearly, Kj is a Kf(r)-decomposition of G′j. Moreover, by (c)j−1 and Proposition 4.5 we have that G′j is (2(r+1)(j−1)+rε′,dj−1,f,r)-regular and (0.9ξj−1,f +r,r)-dense. By Lemma 5.4, there exists a 1-well separated F-packing Fj′ in G′j such that the following hold for Gj := G′j − Fj′(r) − Kj≤(r+1) = G′j − Fj′(r) − Fj′≤(r+1):

- (i) Gj is (2(r+1)(j−1)+r+1ε′,p(fr)−1dj−1,f,r)-regular;
- (ii) Gj is (0.81p(f+rr)−1ξj−1,f + r,r)-dense;
- (iii) ∆(G(jr)) ≤ 1.1p∆(G′j(r)).


Let Fj := Fj−1 ∪ Fj′ and Lj := G(r) − Fj(r) − G(jr). Note that Fj(−r)1 ∩ Fj′(r) = ∅ by (a)j−1. Moreover, Fj−1 and Fj′ are (r + 1)-disjoint by (d)j−1. Thus, Fj is (j − 1 + 1)-well separated by Fact 4.3(ii). Moreover, using (a)j−1, we have

Gj ⊆ Gj−1 − Fj′(r) ⊆ G − Fj(−r)1 − Fj′(r), thus (a)j holds. Observe that Lj\Lj−1 ⊆ L′j. Thus, we clearly have ∆(Lj) ≤ ∆(Lj−1)+∆(L′j) ≤ jε′n, so (b)j holds. Moreover, (c)j follows directly from (i) and (ii), and (e)j follows from (e)j−1 and (iii). To see (d)j, observe that Fj≤−1 and Gj are (r + 1)-disjoint by (d)j−1 and since Gj ⊆ Gj−1, and Fj′≤ and Gj are (r + 1)-disjoint by deﬁnition of Gj. Thus, (a)j–(e)j hold and the proof is completed.

6. Vortices

A vortex is best thought of as a sequence of nested ‘random-like’ subsets of the vertex set of a supercomplex G. In our approach, the ﬁnal set of the vortex has bounded size.

The main results of this section are Lemmas 6.3 and 6.4, where the ﬁrst one shows that vortices exist, and the latter one shows that given a vortex, we can ﬁnd an F-packing covering all edges which do not lie inside the ﬁnal vortex set. We now give the formal deﬁnition of what it means to be a ‘random-like’ subset.

- Deﬁnition 6.1. Let G be a complex on n vertices. We say that U is (ε,µ,ξ,f,r)-random in G if there exists an f-graph Y on V (G) such that the following hold:


- (R1) U ⊆ V (G) with |U| = µn ± n2/3;
- (R2) there exists d ≥ ξ such that for all x ∈ [f − r]0 and all e ∈ G(r), we have that |{Q ∈ G[Y ](f)(e) : |Q ∩ U| = x}| = (1 ± ε)bin(f − r,µ,x)dnf−r;
- (R3) for all e ∈ G(r) we have |G[Y ](f+r)(e)[U]| ≥ ξ(µn)f;
- (R4) for all h ∈ [r]0 and all B ⊆ G(h) with 1 ≤ |B| ≤ 2h we have that b∈B G(b)[U] is an (ε,ξ,f − h,r − h)-complex.


Having deﬁned what it means to be a ‘random-like’ subset, we can now deﬁne what a vortex is.

- Deﬁnition 6.2 (Vortex). Let G be a complex. An (ε,µ,ξ,f,r,m)-vortex in G is a sequence


- U0 ⊇ U1 ⊇ ··· ⊇ Uℓ such that (V1) U0 = V (G); (V2) |Ui| = ⌊µ|Ui−1|⌋ for all i ∈ [ℓ]; (V3) |Uℓ| = m; (V4) for all i ∈ [ℓ], Ui is (ε,µ,ξ,f,r)-random in G[Ui−1]; (V5) for all i ∈ [ℓ − 1], Ui \ Ui+1 is (ε,µ(1 − µ),ξ,f,r)-random in G[Ui−1].


As shown in [12], a vortex can be found in a supercomplex by repeatedly taking random subsets.

- Lemma 6.3 ([12]). Let 1/m′ ≪ ε ≪ µ,ξ,1/f such that µ ≤ 1/2 and r ∈ [f − 1]. Let G be an (ε,ξ,f,r)-supercomplex on n ≥ m′ vertices. Then there exists a (2√ε,µ,ξ − ε,f,r,m)-vortex in

![image 10](<2017-glock-hypergraph-designs-arbitrary_images/imageFile10.png>)

- G for some µm′ ≤ m ≤ m′.

The following is the main lemma of this section. Given a vortex in a supercomplex G, it allows us to cover all edges of G(r) except possibly some from inside the ﬁnal vortex set (see Lemma 7.13 in [12] for the corresponding result in the case when F is a clique).

- Lemma 6.4. Let 1/m ≪ 1/κ ≪ ε ≪ µ ≪ ξ,1/f and r ∈ [f − 1]. Assume that (∗)k is true


for all k ∈ [r − 1]. Let F be a weakly regular r-graph on f vertices. Let G be an F-divisible (ε,ξ,f,r)-supercomplex and U0 ⊇ U1 ⊇ ··· ⊇ Uℓ an (ε,µ,ξ,f,r,m)-vortex in G. Then there exists a 4κ-well separated F-packing F in G which covers all edges of G(r) except possibly some inside Uℓ.

The proof of Lemma 6.4 consists of an ‘iterative absorption’ procedure, where the key ingredient is the Cover down lemma (Lemma 6.9). Roughly speaking, given a supercomplex G and a ‘random-like’ subset U ⊆ V (G), the Cover down lemma allows us to ﬁnd a ‘partial absorber’

- H ⊆ G(r) such that for any sparse L ⊆ G(r), H ∪ L has an F-packing which covers all edges




- of H ∪ L except possibly some inside U. Together with the F-nibble lemma (Lemma 5.3), this allows us to cover all edges of G except possibly some inside U whilst using only few edges inside


- U. Indeed, set aside H as above, which is reasonably sparse. Then apply the Lemma 5.3 to


- G − G(r)[U] − H to obtain an F-packing Fnibble with a very sparse leftover L. Combine H and L to ﬁnd an F-packing Fclean whose leftover lies inside U.


Now, if U0 ⊇ U1 ⊇ ··· ⊇ Uℓ is a vortex, then U1 is ‘random-like’ in G and thus we can cover all edges which are not inside U1 by using only few edges inside U1 (and in this step we forbid edges inside U2 from being used.) Then U2 is still ‘random-like’ in the remainder of G[U1], and hence we can iterate until we have covered all edges of G except possibly some inside Uℓ. The proof of Lemma 6.4 is very similar to that of Lemma 7.13 in [12], thus we omit it here. The details can be found in Appendix B.

We record the following easy tools from [12] for later use.

- Fact 6.5 ([12]). The following hold.


- (i) If G is an (ε,ξ,f,r)-supercomplex, then V (G) is (ε/ξ,1,ξ,f,r)-random in G.
- (ii) If U is (ε,µ,ξ,f,r)-random in G, then G[U] is an (ε,ξ,f,r)-supercomplex.


- Proposition 6.6 ([12]). Let 1/n ≪ ε ≪ µ1,µ2,1−µ2,ξ,1/f and r ∈ [f −1]. Let G be a complex on n vertices and let U ⊆ V (G) be of size ⌊µ1n⌋ and (ε,µ1,ξ,f,r)-random in G. Then there exists U˜ ⊆ U of size ⌊µ2|U|⌋ such that

- (i) U˜ is (ε + |U|−1/6,µ2,ξ − |U|1/6,f,r)-random in G[U] and
- (ii) U \ U˜ is (ε + |U|−1/6,µ1(1 − µ2),ξ − |U|1/6,f,r)-random in G.


- Proposition 6.7 ([12]). Let 1/n ≪ ε ≪ µ,ξ,1/f such that µ ≤ 1/2 and r ∈ [f − 1]. Suppose


- that G is a complex on n vertices and U is (ε,µ,ξ,f,r)-random in G. Suppose that L ⊆ G(r)


√ε,f,r)-random in G − L − O.

and O ⊆ G(r+1) satisfy ∆(L) ≤ εn and ∆(O) ≤ εn. Then U is still (√ε,µ,ξ −

![image 11](<2017-glock-hypergraph-designs-arbitrary_images/imageFile11.png>)

![image 12](<2017-glock-hypergraph-designs-arbitrary_images/imageFile12.png>)

- 6.1. The Cover down lemma. Recall that the Cover down lemma allows us to replace a given leftover L with a new leftover which is restricted to some small set of vertices U. We now provide the formal statement.


- Deﬁnition 6.8. Let G be a complex on n vertices and H ⊆ G(r). We say that G is (ξ,f,r)-dense with respect to H if for all e ∈ G(r), we have |G[H ∪ {e}](f)(e)| ≥ ξnf−r.


Lemma 6.9 (Cover down lemma). Let 1/n ≪ 1/κ ≪ γ ≪ ε ≪ ν ≪ µ,ξ,1/f and r ∈ [f − 1] with µ ≤ 1/2. Assume that (∗)i is true for all i ∈ [r − 1] and that F is a weakly regular r-graph on f vertices. Let G be a complex on n vertices and suppose that U is (ε,µ,ξ,f,r)-random in G. Let G˜ be a complex on V (G) with G ⊆ G˜ such that G˜ is (ε,f,r)-dense with respect to

- G(r) − G(r)[U¯], where U¯ := V (G) \ U. Then there exists a subgraph H∗ ⊆ G(r)−G(r)[U¯] with ∆(H∗) ≤ νn such that for any L ⊆ G˜(r)


with ∆(L) ≤ γn and H∗∪L being F-divisible and any (r+1)-graph O on V (G) with ∆(O) ≤ γn, there exists a κ-well separated F-packing in G˜[H∗ ∪ L] − O which covers all edges of H∗ ∪ L except possibly some inside U.

Roughly speaking, the proof of the Cover down lemma proceeds as follows. Suppose that we have already chosen H∗ and that L is any sparse (leftover) r-graph. For an edge e ∈ H∗ ∪ L, we refer to |e ∩ U| as its type. Since L is very sparse, we can greedily cover all edges of L in a ﬁrst step. In particular, this covers all type-0-edges. We will now continue and cover all

type-1-edges. Note that every type-1-edge contains a unique S ∈ V (rG−)1\U . For a given set S ∈ V (rG−)1\U , we would like to cover all remaining edges of H∗ that contain S simultaneously. Assuming a suitable choice of H∗, this can be achieved as follows. Let LS be the link graph of S after the ﬁrst step. Let T ∈ Vr−(F1) be such that F(T) is non-empty. By Proposition 4.2, LS will be F(T)-divisible. Thus, by (∗)1, LS has a κ-well separated F(T)-decomposition FS′ . Proposition 6.11 below implies that we can extend FS′ to a κ-well separated F-packing FS which covers all edges that contain S.

However, in order to cover all type-1-edges, we need to obtain such a packing FS for every

S ∈ V (rG−)1\U , and these packings are to be r-disjoint for their union to be a κ-well separated F-packing again. The real diﬃculty thus lies in choosing H∗ in such a way that the link graphs

LS do not interfere too much with each other, and then to choose the decompositions FS′ sequentially. We would then continue to cover all type-2-edges using (∗)2, etc., until we ﬁnally cover all type-(r−1)-edges using (∗)r−1. The only remaining edges are then type-r-edges, which are contained in U, as desired.

Proving the Cover down lemma for cliques presented one of the main challenges in [12]. However, with Proposition 6.11 in hand, the proof carries over to general (weakly regular) F without signiﬁcant modiﬁcations, and is thus omitted here. The full proof of the Cover down lemma (Lemma 6.9) can be found in Appendix D.

We now show how the notion of well separated F-packings allows us to ‘extend’ a decomposition of a link complex to a packing which covers all edges that contain a given set S (cf. the discussion in Section 3.2).

- Deﬁnition 6.10. Let F be an r-graph, i ∈ [r−1] and assume that T ∈ V (iF) is such that F(T)


is non-empty. Let G be a complex and S ∈ V (iG) . Suppose that F′ is a well separated F(T)packing in G(S). We then deﬁne S ⊳ F′ as follows: For each F′ ∈ F′, let F⊳′ be an (arbitrary) copy of F on vertex set S ∪ V (F′) such that F⊳′(S) = F′. Let

S ⊳ F′ := {F⊳′ : F′ ∈ F′}.

The following proposition is crucial and guarantees that the above extension yields a packing which covers the desired set of edges. It replaces Fact 10.1 of [12] in the proof of the Cover down lemma. It is also used in the construction of so-called ‘transformers’ (see Section 7.1).

- Proposition 6.11. Let F, r, i, T, G, S be as in Deﬁnition 6.10. Let L ⊆ G(S)(r−i). Suppose that F′ is a κ-well separated F(T)-decomposition of G(S)[L]. Then F := S ⊳ F′ is a κ-well separated F-packing in G and {e ∈ F(r) : S ⊆ e} = S ⊎ L.


In particular, if L = G(S)(r−i), i.e. if F′ is a κ-well separated F(T)-decomposition of G(S), then F is a κ-well separated F-packing in G which covers all r-edges of G that contain S.

Proof. We ﬁrst check that F is an F-packing in G. Let f := |V (F)|. For each F′ ∈ F′, we have V (F′) ∈ G(S)[L](f−i) ⊆ G(S)(f−i). Hence, V (F⊳′) ∈ G(f). In particular, G(r)[V (F⊳′)] is a clique and thus F⊳′ is a subgraph of G(r). Suppose, for a contradiction, that for distinct F′,F′′ ∈ F′, F⊳′ and F⊳′′ both contain e ∈ G(r). By (WS1) we have that |V (F′)∩V (F′′)| ≤ r −i, and thus we must have e = S ∪ (V (F′) ∩ V (F′′)). Since V (F′) ∩ V (F′′) ∈ G(S)[L], we have e \ S ∈ G(S)[L](r−i), and thus e \ S belongs to at most one of F′ and F′′. Without loss of generality, assume that e\S ∈/ F′. Then we have e\S ∈/ F⊳′(S) and thus e ∈/ F⊳′, a contradiction. Thus, F is an F-packing in G.

We next show that F is κ-well separated. Clearly, for distinct F′,F′′ ∈ F′, we have |V (F⊳′) ∩

- V (F⊳′′)| ≤ r − i + |S| = r, so (WS1) holds. To check (WS2), consider e ∈ V (rG) . Let e′ be an (r −i)-subset of e\S. By deﬁnition of F, we have that the number of F⊳′ ∈ F with e ⊆ V (F⊳′) is at most the number of F′ ∈ F′ with e′ ⊆ V (F′), where the latter is at most κ since F′ is κ-well separated.


Finally, we check that {e ∈ F(r) : S ⊆ e} = S ⊎ L. Let e be any r-set with S ⊆ e. By

- Deﬁnition 6.10, we have e ∈ F(r) if and only if e\S ∈ F′(r−i). Since F′ is an F(T)-decomposition of G(S)[L](r−i) = L, we have e \ S ∈ F′(r−i) if and only if e \ S ∈ L. Thus, e ∈ F(r) if and only if e ∈ S ⊎ L.

7. Absorbers

In this section we show that for any (divisible) r-graph H in a supercomplex G, we can ﬁnd an ‘exclusive’ absorber r-graph A (as discussed in Section 1.5, one may think of H as a potential leftover from an approximate F-decomposition and A will be set aside earlier to absorb H into an F-decomposition). The following deﬁnition makes this precise. The main result of this section is Lemma 7.2, which constructs an absorber provided that F is weakly regular.

- Deﬁnition 7.1 (Absorber). Let F, H and A be r-graphs. We say that A is an F-absorber for


- H if A and H are edge-disjoint and both A and A∪H have an F-decomposition. More generally, if G is a complex and H ⊆ G(r), then A ⊆ G(r) is a κ-well separated F-absorber for H in G if A and H are edge-disjoint and there exist κ-well separated F-packings F◦ and F• in G such that


- F◦(r) = A and F•(r) = A ∪ H.


Lemma 7.2 (Absorbing lemma). Let 1/n ≪ 1/κ ≪ γ,1/h,ε ≪ ξ,1/f and r ∈ [f − 1]. Assume that (∗)i is true for all i ∈ [r − 1]. Let F be a weakly regular r-graph on f vertices, let G be an (ε,ξ,f,r)-supercomplex on n vertices and let H be an F-divisible subgraph of G(r) with |H| ≤ h. Then there exists a κ-well separated F-absorber A for H in G with ∆(A) ≤ γn.

We now brieﬂy discuss the case r = 1. For the case F = Kf(1), a construction of an F-absorber for any F-divisible r-graph H in a supercomplex G is given in [12]. It is easy to see that this absorber is 1-well separated. Essentially the same construction also works if F contains some isolated vertices. Thus, for the remainder of this section, we will assume that r ≥ 2.

The building blocks of our absorbers will be so-called ‘transformers’, ﬁrst introduced in [4]. Roughly speaking, a transformer T can be viewed as transforming a given leftover graph H into a new leftover H′ (where we set aside T and H′ earlier).

- Deﬁnition 7.3 (Transformer). Let F be an r-graph, G a complex and assume that H,H′ ⊆ G(r). A subgraph T ⊆ G(r) is a κ-well separated (H,H′;F)-transformer in G if T is edge-disjoint from both H and H′ and there exist κ-well separated F-packings F and F′ in G such that F(r) = T∪H and F′(r) = T ∪ H′.


Our ‘Transforming lemma’ (Lemma 7.5) guarantees the existence of a transformer for H and

- H′ if H′ is obtained from H by identifying vertices (modulo deleting some isolated vertices from H′). To make this more precise, given a multi-r-graph H and x,x′ ∈ V (H), we say that x and x′


are identiﬁable if |H({x,x′})| = 0, that is, if identifying x and x′ does not create an edge of size less than r. For multi-r-graphs H and H′, we write H H′ if there is a sequence H0,... ,Ht of multi-r-graphs such that H0 ∼= H, Ht is obtained from H′ by deleting isolated vertices, and for every i ∈ [t], there are two identiﬁable vertices x,x′ ∈ V (Hi−1) such that Hi is obtained from Hi−1 by identifying x and x′.

If H and H′ are (simple) r-graphs and H H′, we just write H H′ to indicate the fact that during the identiﬁcation steps, only vertices x,x′ ∈ V (Hi−1) with Hi−1({x}) ∩ Hi−1({x′}) = ∅ were identiﬁed (i.e. if we did not create multiple edges).

Clearly, is a reﬂexive and transitive relation on the class of multi-r-graphs, and is a reﬂexive and transitive relation on the class of r-graphs.

It is easy to see that H H′ if and only if there is an edge-bijective homomorphism from H to H′ (see Proposition 7.4(i)). Given r-graphs H,H′, a homomorphism from H to H′ is a map φ: V (H) → V (H′) such that φ(e) ∈ H′ for all e ∈ H. Note that this implies that φ↾e is injective for all e ∈ H. We let φ(H) denote the subgraph of H′ with vertex set φ(V (H)) and edge set {φ(e) : e ∈ H}. We say that φ is edge-bijective if |H| = |φ(H)| = |H′|. For two r-graphs H and H′, we write H φ H′ if φ is an edge-bijective homomorphism from H to H′.

We now record a few simple observations about the relation for future reference.

- Proposition 7.4. The following hold.


- (i) H H′ if and only if there exists φ such that H φ H′.
- (ii) Let H1,H1′,... ,Ht,Ht′ be r-graphs such that H1,... ,Ht are vertex-disjoint and H1′,... ,Ht′ are edge-disjoint and Hi ∼= Hi′ for all i ∈ [t]. Then

H1 + ··· + Ht H1′ ∪· ··· ∪· Ht′.

- (iii) If H H′ and H is F-divisible, then H′ is F-divisible.


- 7.1. Transformers. The following lemma guarantees the existence of a transformer from H to H′ if F is weakly regular and H H′. The proof relies inductively on the assertion of the main complex decomposition theorem (Theorem 3.8).


- Lemma 7.5 (Transforming lemma). Let 1/n ≪ 1/κ ≪ γ,1/h,ε ≪ ξ,1/f and 2 ≤ r < f.


Assume that (∗)i is true for all i ∈ [r − 1]. Let F be a weakly regular r-graph on f vertices, let G be an (ε,ξ,f,r)-supercomplex on n vertices and let H,H′ be vertex-disjoint F-divisible subgraphs of G(r) of order at most h and such that H H′. Then there exists a κ-well separated (H,H′;F)-transformer T in G with ∆(T) ≤ γn.

A key operation in the proof of Lemma 7.5 is the ability to ﬁnd ‘localised transformers’. Let i ∈ [r − 1] and let S ⊆ V (H), S′ ⊆ V (H′) and S∗ ⊆ V (F) be sets of size i. For an (r − i)-graph L in the link graph of both S and S′, we can view an F(S∗)-decomposition FL of L (which exists by (∗)r−i) as a localised transformer between S ⊎ L and S′ ⊎ L. Indeed, similarly to the situation described in Sections 3.2 and 6.1, we can extend FL ‘by adding S back’ to obtain an F-packing F which covers all edges of S ⊎ L. By ‘mirroring’ this extension, we can also obtain an F-packing F′ which covers all edges of S′ ⊎ L (see Deﬁnition 7.8 and Proposition 7.9). To make this more precise, we introduce the following notation.

- Deﬁnition 7.6. Let V be a set and let V1,V2 be disjoint subsets of V having equal size. Let φ: V1 → V2 be a bijection. For a set S ⊆ V \ V2, deﬁne φ(S) := (S \ V1) ∪ φ(S ∩ V1). Moreover, for an r-graph R with V (R) ⊆ V \ V2, we let φ(R) be the r-graph on φ(V (R)) with edge set {φ(e) : e ∈ R}.


The following facts are easy to see.

- Fact 7.7. Suppose that V , V1, V2 and φ are as above. Then the following hold for every r-graph


- R with V (R) ⊆ V \ V2:


- (i) φ(R) ∼= R;


- (ii) if R = R1 ∪···· ∪· Rk, then φ(R) = φ(R1)∪···· ∪· φ(Rk) and thus φ(R1) = φ(R)−φ(R2)− ··· − φ(Rk).


The following deﬁnition is a two-sided version of Deﬁnition 6.10.

- Deﬁnition 7.8. Let F be an r-graph, i ∈ [r − 1] and assume that S∗ ∈ V (iF) is such that


- F(S∗) is non-empty. Let G be a complex and assume that S1,S2 ∈ V (iG) are disjoint and that a bijection φ: S1 → S2 is given. Suppose that F′ is a well separated F(S∗)-packing in
- G(S1) ∩ G(S2). We then deﬁne S1 ⊳ F′ ⊲ S2 as follows: For each F′ ∈ F′ and j ∈ {1,2}, let Fj′ be a copy of F on vertex set Sj ∪ V (F′) such that Fj′(Sj) = F′ and such that φ(F1′) = F2′. Let


F1 := {F1′ : F′ ∈ F′}; F2 := {F2′ : F′ ∈ F′};

S1 ⊳ F′ ⊲ S2 := (F1,F2). The next proposition is proved using its one-sided counterpart, Proposition 6.11. As in

- Proposition 6.11, the notion of well separatedness (Deﬁnition 3.6) is crucial here.
- Proposition 7.9. Let F, r, i, S∗, G, S1, S2 and φ be as in Deﬁnition 7.8. Suppose that L ⊆ G(S1)(r−i) ∩ G(S2)(r−i) and that F′ is a κ-well separated F(S∗)-decomposition of (G(S1) ∩


- G(S2))[L]. Then the following holds for (F1,F2) = S1 ⊳ F′ ⊲ S2:


- (i) for j ∈ [2], Fj is a κ-well separated F-packing in G with {e ∈ Fj(r) : Sj ⊆ e} = Sj ⊎ L;
- (ii) V (F1(r)) ⊆ V (G) \ S2 and φ(F1(r)) = F2(r).


Proof. Let j ∈ [2]. Since (G(S1) ∩ G(S2))[L] ⊆ G(Sj), we can view Fj as Sj ⊳ F′ (cf. Deﬁnition 6.10). Moreover, since (G(S1) ∩ G(S2))[L](r−i) = L = G(Sj)[L](r−i), we can conclude that F′ is a κ-well separated F(S∗)-decomposition of G(Sj)[L]. Thus, by Proposition 6.11, Fj is a κ-well separated F-packing in G with {e ∈ Fj(r) : Sj ⊆ e} = Sj ⊎ L.

Moreover, we have V (F1(r)) ⊆ F′∈F′ V (F1′) ⊆ V (G) \ S2 and by Fact 7.7(ii) φ(F1(r)) = φ(

˙

˙

˙

F2′ = F2(r).

F1′) =

φ(F1′) =

F′∈F′

F′∈F′

F′∈F′

We now sketch the proof of Lemma 7.5. Given Proposition 7.9, the details are very similar to the proof of Lemma 8.5 in [12] and thus omitted here. The full proof of Lemma 7.5 can be found in Appendix C.

Suppose for simplicity that H′ is simply a copy of H, i.e. H′ = φ(H) where φ is an isomorphism from H to H′. We aim to construct an (H,H′;F)-transformer. In a ﬁrst step, for every edge e ∈ H, we introduce a set Xe of |V (F)| − r new vertices and let Fe be a copy of F such that

- V (Fe) = e ∪ Xe and e ∈ Fe. Let T1 := e∈H Fe[Xe] and R1 := e∈H Fe − T1 − H. Clearly, {Fe : e ∈ H} is an F-decomposition of H ∪R1 ∪T1. By Fact 7.7(ii), we also have that {φ(Fe) : e ∈ H} is an F-decomposition of H′ ∪ φ(R1) ∪ T1. Hence, T1 is an (H ∪ R1,H′ ∪ φ(R1);F)transformer. Note that at this stage, it would suﬃce to ﬁnd an (R1,φ(R1);F)-transformer T1′, as then T1 ∪ T1′ ∪ R1 ∪ φ(R1) would be an (H,H′;F)-transformer. The crucial diﬀerence now to the original problem is that every edge of R1 contains at most r −1 vertices from V (H). On the other hand, every edge in R1 contains at least one vertex in V (H) as otherwise it would belong to T1. We view this as Step 1 and will now proceed inductively. After Step i, we will have an r-graph Ri and an (H ∪ Ri,H′ ∪ φ(Ri);F)-transformer Ti such that every edge e ∈ Ri satisﬁes 1 ≤ |e ∩ V (H)| ≤ r − i. Thus, after Step r we can terminate the process as Rr must be empty and thus Tr is an (H,H′;F)-transformer.


In Step i + 1, where i ∈ [r − 1], we use (∗)i inductively as follows. Let Ri′ consist of all edges of Ri which intersect V (H) in r − i vertices. We decompose Ri′ into ‘local’ parts. For every edge e ∈ Ri′, there exists a unique set S ∈ Vr(−Hi) such that S ⊆ e. For each S ∈ Vr(−Hi) , let LS := Ri′(S). Note that the ‘local’ parts S ⊎ LS form a decomposition of Ri′. The problem

of ﬁnding Ri+1 and Ti+1 can be reduced to ﬁnding a ‘localised transformer’ between S ⊎ LS and φ(S) ⊎ LS for every S, as described above. At this stage, by Proposition 4.2, LS will automatically be F(S∗)-divisible, where S∗ ∈ Vr(−Fi) is such that F(S∗) is non-empty. If we were given an F(S∗)-decomposition FS′ of LS, we could use Proposition 7.9 to extend FS′ to an F-packing FS which covers all edges of S ⊎ LS, and all new edges created by this extension intersect S (and V (H)) in at most r − i − 1 vertices, as desired. It is possible to combine these localised transformers with Ti and Ri in such a way that we obtain Ti+1 and Ri+1.

Unfortunately, (G(S) ∩ G(φ(S)))[LS] might not be a supercomplex (one can think of LS as

some leftover from previous steps) and so FS′ may not exist. However, by Proposition 4.4, we have that G(S) ∩ G(φ(S)) is a supercomplex. Thus we can (randomly) choose a suitable i-

subgraph AS of (G(S) ∩ G(φ(S)))(i) such that AS is F(S∗)-divisible and edge-disjoint from LS. Instead of building a localised transformer for LS directly, we will now build one for AS and one for AS ∪ LS, using (∗)i both times to ﬁnd the desired F(S∗)-decomposition. These can then be combined into a localised transformer for LS.

- 7.2. Canonical multi-r-graphs. Roughly speaking, the aim of this section is to show that


any F-divisible r-graph H can be transformed into a canonical multigraph Mh which does not depend on the structure of H. However, it turns out that for this we need to move to a ‘dual’ setting, where we consider ∇H which is obtained from H by applying an F-extension operator ∇. This operator allows us to switch between multi-r-graphs (which arise naturally in the construction but are not present in the complex G we are decomposing) and (simple) r-graphs (see e.g. Fact 7.15).

Given a multi-r-graph H and a set X of size r, we say that ψ is an X-orientation of H if ψ is a collection of bijective maps ψe: X → e, one for each e ∈ H. (For r = 2 and X = {1,2}, say, this coincides with the notion of an oriented multigraph, e.g. by viewing ψe(1) as the tail and ψe(2) as the head of e, where parallel edges can be oriented in opposite directions.)

Given an r-graph F and a distinguished edge e0 ∈ F, we introduce the following ‘extension’ operators ∇˜ (F,e0) and ∇(F,e0).

Deﬁnition 7.10 (Extension operators ∇˜ and ∇). Given a (multi-)r-graph H with an e0orientation ψ, let ∇˜ (F,e0)(H,ψ) be obtained from H by extending every edge of H into a copy of F, with e0 being the rooted edge. More precisely, let Ze be vertex sets of size |V (F) \ e0| such that Ze ∩ Ze′ = ∅ for all distinct (but possibly parallel) e,e′ ∈ H and V (H) ∩ Ze = ∅ for all e ∈ H. For each e ∈ H, let Fe be a copy of F on vertex set e ∪ Ze such that ψe(v) plays the role of v for all v ∈ e0 and Ze plays the role of V (F) \ e0. Then ∇˜ (F,e0)(H,ψ) := e∈H Fe. Let ∇(F,e0)(H,ψ) := ∇˜ (F,e0)(H,ψ) − H.

Note that ∇(F,e0)(H,ψ) is a (simple) r-graph even if H is a multi-r-graph. If F, e0 and ψ are clear from the context, or if we only want to motivate an argument before giving the formal proof, we just write ∇˜H and ∇H.

Fact 7.11. Let F be an r-graph and e0 ∈ F. Let H be a multi-r-graph and let ψ be any e0-orientation of H. Then the following hold:

- (i) ∇˜ (F,e0)(H,ψ) is F-decomposable;
- (ii) ∇(F,e0)(H,ψ) is F-divisible if and only if H is F-divisible.


The goal of this subsection is to show that for every h ∈ N, there is a multi-r-graph Mh such that for any F-divisible r-graph H on at most h vertices, we have (7.1) ∇(∇(H + t · F) + s · F) ∇Mh

for suitable s,t ∈ N. The multigraph Mh is canonical in the sense that it does not depend on H, but only on h. The beneﬁt is, very roughly speaking, that it allows us to transform any given leftover r-graph H into the empty r-graph, which is trivially decomposable, and this will enable us to construct an absorber for H. Indeed, to see that (7.1) allows us to transform H into the empty r-graph, let

H′ := ∇(∇(H + t · F) + s · F) = ∇∇H + t · ∇∇F + s · ∇F

and observe that the r-graph T := ∇H + t · ∇˜F + s · F ‘between’ H and H′ can be chosen in such a way that

T ∪ H = ∇˜ H + t · ∇˜F + s · F,

T ∪ H′ = ∇˜ (∇H) + t · (∇˜(∇F) ∪· F) + s · ∇˜F, i.e. T is an (H,H′;F)-transformer (cf. Fact 7.11(i)). Hence, together with (7.1) and Lemma 7.5, this means that we can transform H into ∇Mh. Since Mh does not depend on H, we can also transform the empty r-graph into ∇Mh, and by transitivity we can transform H into the empty graph, which amounts to an absorber for H (the detailed proof of this can be found in Section 7.3).

We now give the rigorous statement of (7.1), which is the main lemma of this subsection.

- Lemma 7.12. Let r ≥ 2 and assume that (∗)i is true for all i ∈ [r − 1]. Let F be a weakly regular r-graph and e0 ∈ F. Then for all h ∈ N, there exists a multi-r-graph Mh such that for any F-divisible r-graph H on at most h vertices, we have


∇(F,e0)(∇(F,e0)(H + t · F,ψ1) + s · F,ψ3) ∇(F,e0)(Mh,ψ2) for suitable s,t ∈ N, where ψ1 and ψ2 can be arbitrary e0-orientations of H + t · F and Mh, respectively, and ψ3 is an e0-orientation depending on these.

The above graphs ∇(∇(H + t · F) + s · F) and ∇Mh will be part of our F-absorber for H. We therefore need to make sure that we can actually ﬁnd them in a supercomplex G. This requirement is formalised by the following deﬁnition.

Deﬁnition 7.13. Let G be a complex, X ⊆ V (G), F an r-graph with f := |V (F)| and e0 ∈ F. Suppose that H ⊆ G(r) and that ψ is an e0-orientation of H. By extending H with a copy of ∇(F,e0)(H,ψ) in G (whilst avoiding X) we mean the following: for each e ∈ H, let Ze ∈ G(f)(e) be such that Ze ∩ (V (H) ∪ X) = ∅ for every e ∈ H and Ze ∩ Ze′ = ∅ for all distinct e,e′ ∈ H. For each e ∈ H, let Fe be a copy of F on vertex set e ∪ Ze (so Fe ⊆ G(r)) such that ψe(v) plays the role of v for all v ∈ e0 and Ze plays the role of V (F) \ e0. Let H∇ := e∈H Fe − H and F := {Fe : e ∈ H} be the output of this.

For our purposes, the set |V (H) ∪ X| will have a small bounded size compared to |V (G)|. Thus, if the G(f)(e) are large enough (which is the case e.g. in an (ε,ξ,f,r)-supercomplex), then the above extension can be carried out simply by picking the sets Ze one by one.

- Fact 7.14. Let (H∇,F) be obtained by extending H ⊆ G(r) with a copy of ∇(F,e0)(H,ψ) in G.


- Then H∇ ⊆ G(r) is a copy of ∇(F,e0)(H,ψ) and F is a 1-well separated F-packing in G with


- F(r) = H ∪ H∇ such that for all F′ ∈ F, |V (F′) ∩ V (H)| ≤ r.


For a partition P = {Vx}x∈X whose classes are indexed by a set X, we deﬁne VY := x∈Y Vx for every subset Y ⊆ X. Recall that for a multi-r-graph H and e ∈ V(rH) , |H(e)| denotes the multiplicity of e in H. For multi-r-graphs H,H′, we write H P H′ if P = {Vx′}x′∈V (H′) is a partition of V (H) such that

(I1) for all x′ ∈ V (H′) and e ∈ H, |Vx′ ∩ e| ≤ 1; (I2) for all e′ ∈ V (rH′) , e∈(Ve′

r ) |H(e)| = |H′(e′)|.

Given P, deﬁne φP : V (H) → V (H′) as φP(x) := x′ where x′ is the unique x′ ∈ V (H′) such that x ∈ Vx′. Note that by (I1), we have |{φP(x) : x ∈ e}| = r for all e ∈ H. Further, by (I2), there exists a bijection ΦP : H → H′ between the multi-edge-sets of H and H′ such that for every edge e ∈ H, the image ΦP(e) is an edge consisting of the vertices φP(x) for all x ∈ e. It is easy to see that H H′ if and only if there is some P such that H P H′.

The extension operator ∇ is well behaved with respect to the identiﬁcation relation in the following sense: if H H′, then ∇H ∇H′. More precisely, let H and H′ be multi-r-graphs and suppose that H P H′. Let φP and ΦP be deﬁned as above. Let F be an r-graph and

e0 ∈ F. For any e0-orientation ψ′ of H′, we deﬁne an e0-orientation ψ of H induced by ψ′ as follows: for every e ∈ H, let e′ := ΦP(e) be the image of e with respect to P . We have that φP↾e: e → e′ is a bijection. We now deﬁne the bijection ψe: e0 → e as ψe := φP↾e−1 ◦ψe′′, where ψe′′ : e0 → e′. Thus, the collection ψ of all ψe, e ∈ H, is an e0-orientation of H. It is easy to see that ψ satisﬁes the following.

- Fact 7.15. Let F be an r-graph and e0 ∈ F. Let H,H′ be multi-r-graphs and suppose that


H H′. Then for any e0-orientation ψ′ of H′, we have ∇(F,e0)(H,ψ) ∇(F,e0)(H′,ψ′), where ψ is induced by ψ′.

We now deﬁne the multi-r-graphs which will serve as the canonical multi-r-graphs Mh in

- (7.1). For r ∈ N, let Mr contain all pairs (k,m) ∈ N20 such that rm−i r− k−1−i i is an integer for all i ∈ [r − 1]0.


![image 13](<2017-glock-hypergraph-designs-arbitrary_images/imageFile13.png>)

- Deﬁnition 7.16 (Canonical multi-r-graph). Let F∗ be an r-graph and e∗ ∈ F∗. Let V ′ :=

V (F∗) \ e∗. If (k,m) ∈ Mr, deﬁne the multi-r-graph M(F

∗,e∗)

k,m on vertex set [k] ∪· V ′ such that for every e ∈ [k]∪rV′ , the multiplicity of e is

|M(F

∗,e∗)

k,m (e)| =

 



0 if e ⊆ [k];

m r−|e∩[k]|

![image 14](<2017-glock-hypergraph-designs-arbitrary_images/imageFile14.png>)

k−|e∩[k]|

r−1−|e∩[k]| if |e ∩ [k]| > 0,|e ∩ V ′| > 0; 0 if e ⊆ V ′,e ∈/ F∗; m r

![image 15](<2017-glock-hypergraph-designs-arbitrary_images/imageFile15.png>)

k

r−1 if e ⊆ V ′,e ∈ F∗.

We will require the graph F∗ in Deﬁnition 7.16 to have a certain symmetry property with respect to e∗, which we now deﬁne. We will prove the existence of a suitable (F-decomposable) symmetric r-extender in Lemma 7.23.

- Deﬁnition 7.17 (symmetric r-extender). We say that (F∗,e∗) is a symmetric r-extender if F∗ is an r-graph, e∗ ∈ F∗ and the following holds:


(SE) for all e′ ∈ V (Fr ∗) with e′ ∩ e∗ = ∅, we have e′ ∈ F∗.

Note that if (F∗,e∗) is a symmetric r-extender, then the operators ∇˜ (F∗,e∗),∇(F∗,e∗) are labelling-invariant, i.e. ∇˜ (F∗,e∗)(H,ψ1) ∼= ∇˜(F∗,e∗)(H,ψ2) and ∇(F∗,e∗)(H,ψ1) ∼= ∇(F∗,e∗)(H,ψ2) for all e∗-orientations ψ1,ψ2 of a multi-r-graph H. We therefore simply write ∇˜ (F∗,e∗)H and ∇(F∗,e∗)H in this case.

To prove Lemma 7.12 we introduce so called strong colourings. Let H be an r-graph and C a set. A map c: V (H) → C is a strong C-colouring of H if for all distinct x,y ∈ V (H) with |H({x,y})| > 0, we have c(x) = c(y), that is, no colour appears twice in one edge. For α ∈ C, we let c−1(α) denote the set of all vertices coloured α. For a set C′ ⊆ C, we let

c⊆(C′) := {e ∈ H : C′ ⊆ c(e)}. We say that c is m-regular if |c⊆(C′)| = m for all C′ ∈ r− C1 . For example, an r-partite r-graph H trivially has a strong |H|-regular [r]-colouring.

Fact 7.18. Let H be an r-graph and let c be a strong m-regular [k]-colouring of H. Then |c⊆(C′)| = rm−i r− k−1−i i for all i ∈ [r − 1]0 and all C′ ∈ [ki] .

![image 16](<2017-glock-hypergraph-designs-arbitrary_images/imageFile16.png>)

- Lemma 7.19. Let (F∗,e∗) be a symmetric r-extender. Suppose that H is an r-graph and suppose that c is a strong m-regular [k]-colouring of H. Then (k,m) ∈ Mr and


∗,e∗)

∇(F∗,e∗)H M(F

k,m . Proof. By Fact 7.18, (k,m) ∈ Mr, thus M(F

∗,e∗)

∗,e∗)

k,m is deﬁned. Recall that M(F

k,m has vertex set [k] ∪ V ′, where V ′ := V (F∗) \ e∗. Let V (H) ∪ e∈H Ze be the vertex set of ∇(F∗,e∗)H as in Deﬁnition 7.10, with Ze = {ze,v : v ∈ V ′}. We deﬁne a partition P of V (H) ∪ e∈H Ze as follows: for all i ∈ [k], let Vi := c−1(i). For all v ∈ V ′, let Vv := {ze,v : e ∈ H}. We now claim

that ∇(F∗,e∗)H P M(F

∗,e∗)

k,m .

- Clearly, P satisﬁes (I1) because c is a strong colouring of H. For a set e′ ∈ [k]∪rV′ , deﬁne Se′ := {e′′ ∈ ∇(F∗,e∗)H : e′′ ⊆ Ve′}.


Since ∇(F∗,e∗)H is simple, in order to check (I2), it is enough to show that for all e′ ∈ [k]∪rV′ , we have |Se′| = |M(F

∗,e∗)

k,m (e′)|. We distinguish three cases.

- Case 1: e′ ⊆ [k]

In this case, |M(F

∗,e∗)

k,m (e′)| = 0. Since Ve′ ⊆ V (H) and (∇(F∗,e∗)H)[V (H)] is empty, we have Se′ = ∅, as desired.

- Case 2: e′ ⊆ V ′

In this case, Se′ consists of all edges of ∇(F∗,e∗)H which play the role of e′ in Fe∗ for some e ∈ H. Hence, if e′ ∈/ F∗, then |Se′| = 0, and if e′ ∈ F∗, then |Se′| = |H|. Fact 7.18 applied with i = 0 yields |H| = mr r− k1 , as desired.

![image 17](<2017-glock-hypergraph-designs-arbitrary_images/imageFile17.png>)

- Case 3: |e′ ∩ [k]| > 0 and |e′ ∩ V ′| > 0


We claim that |Se′| = |c⊆(e′ ∩[k])|. In order to see this, we deﬁne a bijection π: c⊆(e′ ∩[k]) → Se′ as follows: for every e ∈ H with e′ ∩ [k] ⊆ c(e), deﬁne

π(e) := (e ∩ c−1(e′ ∩ [k])) ∪ {ze,v : v ∈ e′ ∩ V ′}. We ﬁrst show that π(e) ∈ Se′. Note that e ∩ c−1(e′ ∩ [k]) is a subset of e of size |e′ ∩ [k]| and {ze,v : v ∈ e′ ∩ V ′} is a subset of Ze of size |e′ ∩ V ′|. Hence, π(e) ∈ V (Fre∗) and |π(e) ∩ e| = |e′ ∩ [k]| > 0. Thus, by (SE), we have π(e) ∈ Fe∗ ⊆ ∇(F∗,e∗)H. (This is in fact the crucial point where we need (SE).) Moreover,

π(e) ⊆ c−1(e′ ∩ [k]) ∪ {ze,v : v ∈ e′ ∩ V ′} ⊆ Ve′∩[k] ∪ Ve′∩V′ = Ve′.

Therefore, π(e) ∈ Se′. It is straightforward to see that π is injective. Finally, for every e′′ ∈ Se′, we have e′′ = π(e), where e ∈ H is the unique edge of H with e′′ ∈ Fe∗. This establishes our claim that π is bijective and hence |Se′| = |c⊆(e′ ∩ [k])|. Since 1 ≤ |e′ ∩ [k]| ≤ r − 1, Fact 7.18 implies that

k − |e′ ∩ [k]| r − 1 − |e′ ∩ [k]|

m r − |e′ ∩ [k]|

∗,e∗)

= |M(F

|Se′| = |c⊆(e′ ∩ [k])| =

k,m (e′)|, as required.

![image 18](<2017-glock-hypergraph-designs-arbitrary_images/imageFile18.png>)

Next, we establish the existence of suitable strong regular colourings. As a tool we need the following result about decompositions of very dense multi-r-graphs (which we will apply with r − 1 playing the role of r). We omit the proof as it is essentially the same as that of Corollary 8.16 in [12].

- Lemma 7.20. Let r ∈ N and assume that (∗)r is true. Let 1/n ≪ 1/h,1/f with f > r, let F be


a weakly regular r-graph on f vertices and assume that Kn(r) is F-divisible. Let m ∈ N. Suppose that H is an F-divisible multi-r-graph on [h] with multiplicity at most m − 1 and let K be the complete multi-r-graph on [n] with multiplicity m. Then K − H has an F-decomposition.

The next lemma guarantees the existence of a suitable strong regular colouring. For this, we apply Lemma 7.20 to the shadow of F. For an r-graph F, deﬁne the shadow Fsh of F to be the (r − 1)-graph on V (F) where an (r − 1)-set S is an edge if and only if |F(S)| > 0. We need the following fact.

Fact 7.21. If F is a weakly (s0,... ,sr−1)-regular r-graph, then Fsh is a weakly (s′0,... ,s′r−2)regular (r − 1)-graph, where s′i := sr−i

si for all i ∈ [r − 2]0. Proof. Let i ∈ [r − 2]0. For every T ∈ V (iF) , we have |Fsh(T)| = sr−i

![image 19](<2017-glock-hypergraph-designs-arbitrary_images/imageFile19.png>)

r−1

|F(T)| since every edge of F which contains T contains r − i edges of Fsh which contain T, but each such edge of Fsh is contained in sr−1 such edges of F. This implies the claim.

![image 20](<2017-glock-hypergraph-designs-arbitrary_images/imageFile20.png>)

r−1

- Lemma 7.22. Let r ≥ 2 and assume that (∗)r−1 holds. Let F be a weakly regular r-graph. Then for all h ∈ N, there exist k,m ∈ N such that for any F-divisible r-graph H on at most h vertices, there exists t ∈ N such that H + t · F has a strong m-regular [k]-colouring.


Proof. Let f := |V (F)| and suppose that F is weakly (s0,... ,sr−1)-regular. Thus, for every

- S ∈ Vr−(F1) , we have


sr−1 if S ∈ Fsh; 0 otherwise.

|F(S)| =

- (7.2)

By Proposition 4.1, we can choose k ∈ N such that 1/k ≪ 1/h,1/f and such that Kk(r−1) is Fsh-divisible. Let G be the complete multi-(r − 1)-graph on [k] with multiplicity m′ := h + 1 and let m := sr−1m′.

Let H be any F-divisible r-graph on at most h vertices. By adding isolated vertices to H if necessary, we may assume that V (H) = [h]. We ﬁrst deﬁne a multi-(r − 1)-graph H′ on [h] as follows: For each S ∈ r [−h]1 , let the multiplicity of S in H′ be |H′(S)| := |H(S)|. Clearly, H′ has multiplicity at most h. Observe that for each S ⊆ [h] with |S| ≤ r − 1, we have

- (7.3) |H′(S)| = (r − |S|)|H(S)|.

Note that since H is F-divisible, we have that sr−1 | |H(S)| for all S ∈ r [−h]1 . Thus, the multiplicity of each S ∈ r [−h]1 in H′ is divisible by sr−1. Let H′′ be the multi-(r − 1)-graph on [h] obtained from H′ by dividing the multiplicity of each S ∈ r [−h]1 by sr−1. Hence, by (7.3), for all S ⊆ [h] with |S| ≤ r − 1, we have

|H′′(S)| = |H′(S)| sr−1

![image 21](<2017-glock-hypergraph-designs-arbitrary_images/imageFile21.png>)

=

r − |S|

![image 22](<2017-glock-hypergraph-designs-arbitrary_images/imageFile22.png>)

- (7.4) sr−1 |H(S)|.

For each S ∈ r [−k]1 with S  ⊆ [h], we set |H′′(S)| := |H(S)| := 0. Then (7.4) still holds. We claim that H′′ is Fsh-divisible. Recall that by Fact 7.21,

Fsh is weakly (

r sr−1

![image 23](<2017-glock-hypergraph-designs-arbitrary_images/imageFile23.png>)

s0,... ,

r − i sr−1

![image 24](<2017-glock-hypergraph-designs-arbitrary_images/imageFile24.png>)

si,... ,

2 sr−1

![image 25](<2017-glock-hypergraph-designs-arbitrary_images/imageFile25.png>)

sr−2)-regular.

Let i ∈ [r − 2]0 and let S ∈ [hi] . We need to show that |H′′(S)| ≡ 0 mod Deg(Fsh)i, where Deg(Fsh)i = sr−i

![image 26](<2017-glock-hypergraph-designs-arbitrary_images/imageFile26.png>)

r−1

si. Since H is F-divisible, we have |H(S)| ≡ 0 mod si. Together with (7.4), we deduce that |H′′(S)| ≡ 0 mod sr−i

![image 27](<2017-glock-hypergraph-designs-arbitrary_images/imageFile27.png>)

r−1

si. Hence, H′′ is Fsh-divisible. Therefore, by Lemma 7.20 (with k,m′,r − 1,Fsh playing the roles of n,m,r,F) and our choice of k, G − H′′ has an Fshdecomposition F into t edge-disjoint copies F1′,... ,Ft′ of Fsh.

We will show that t is as required in Lemma 7.22. To do this, let F1,... ,Ft be vertex-disjoint copies of F which are also vertex-disjoint from H. We will now deﬁne a strong m-regular [k]-colouring c of

H+ := H ∪

j∈[t]

Fj.

Let c0 be the identity map on V (H) = [h], and for each j ∈ [t], let

- (7.5) cj : V (Fj) → V (Fj′) be an isomorphism from Fjsh to Fj′


(recall that V (Fjsh) = V (Fj)). Since H,F1,... ,Ft are vertex-disjoint and V (H)∪ j∈[t] V (Fj′) ⊆ [k], we can combine c0,c1,... ,ct to a map

c: V (H+) → [k],

i.e. for x ∈ V (H+), we let c(x) := cj(x), where either j is the unique index for which x ∈ V (Fj) or j = 0 if x ∈ V (H). For every edge e ∈ H+, we have e ⊆ V (H) or e ⊆ V (Fj) for some j ∈ [t], thus c↾e is injective. Therefore, c is a strong [k]-colouring of H+.

It remains to check that c is m-regular. Let C ∈ r [−k]1 . Clearly, |c⊆(C)| = tj=0 |c⊆j (C)|. Since every cj is a bijection, we have

|c⊆0 (C)| = |{e ∈ H : c−0 1(C) ⊆ e}| = |H(c−0 1(C))| = |H(C)| and

sr−1 if c−j 1(C) ∈ Fjsh (7.5⇔) C ∈ Fj′; 0 otherwise.

|c⊆j (C)| = |Fj(c−j 1(C))| (7.2=)

Thus, we have |c⊆(C)| = |H(C)| + sr−1|J(C)|, where

J(C) := {j ∈ [t] : C ∈ Fj′}. Now crucially, since F is an Fsh-decomposition of G − H′′, we have that |J(C)| is equal to the multiplicity of C in G − H′′, i.e. |J(C)| = m′ − |H′′(C)|. Thus,

|c⊆(C)| = |H(C)| + sr−1|J(C)| (7.4=) sr−1(|H′′(C)| + |J(C)|) = sr−1m′ = m, completing the proof.

Before we can prove Lemma 7.12, we need to show the existence of a symmetric r-extender F∗ which is F-decomposable. For some F we could actually take F∗ = F (e.g. if F is a clique). For general (weakly regular) r-graphs F, we will use the Cover down lemma (Lemma 6.9) to ﬁnd F∗. At ﬁrst sight, appealing to the Cover down lemma may seem rather heavy handed, but a direct construction seems to be quite diﬃcult.

- Lemma 7.23. Let F be a weakly regular r-graph, e0 ∈ F and assume that (∗)i is true for all i ∈ [r − 1]. There exists a symmetric r-extender (F∗,e∗) such that F∗ has an F-decomposition


- F with e∗ ∈ F′ ∈ F and e∗ plays the role of e0 in F′. Proof. Let f := |V (F)|. By Proposition 4.1, we can choose n ∈ N and γ,ε,ν,µ > 0 such


that 1/n ≪ γ ≪ ε ≪ ν ≪ µ ≪ 1/f and such that Kn(r) is F-divisible. By Example 3.3, Kn is a (0,0.99/f!,f,r)-supercomplex. By Fact 6.5(i) and Proposition 6.6, there exists U ⊆ V (Kn) of size ⌊µn⌋ which is (ε,µ,0.9/f!,f,r)-random in Kn. Let U¯ := V (Kn) \ U. Using (R2) of Deﬁnition 6.1, it is easy to see that Kn is (ε,f,r)-dense with respect to Kn(r) − Kn(r)[U¯] (see Deﬁnition 6.8). Thus, by the Cover down lemma (Lemma 6.9), there exists a subgraph H∗ of Kn(r) − Kn(r)[U¯] with ∆(H∗) ≤ νn and the following property: for all L ⊆ Kn(r) such that ∆(L) ≤ γn and H∗ ∪ L is F-divisible, H∗ ∪ L has an F-packing which covers all edges except possibly some inside U.

Let F′ be a copy of F with V (F′) ⊆ U¯. Let Gnibble := Kn − H∗ − F′. By Proposition 4.5(v), Gnibble is a (22r+2ν,0.8/f!,f,r)-supercomplex. Thus, by Lemma 5.3, there exists an F-packing Fnibble in G(nibbler) such that ∆(L) ≤ γn, where L := G(nibbler) − Fnibble(r) . Clearly, H∗ ∪ L = Kn(r) − Fnibble(r) − F′ is F-divisible. Thus, there exists an F-packing F∗ in H∗ ∪ L which covers all edges of H∗ ∪L except possibly some inside U. Let F := {F′} ∪Fnibble ∪F∗. Let F∗ := F(r) and let e∗ be the edge in F′ which plays the role of e0.

Clearly, F is an F-decomposition of F∗ with e∗ ∈ F′ ∈ F and e∗ plays the role of e0 in F′. It remains to check (SE). Let e′ ∈ V (K

(r) n )

r with e′ ∩ e∗ = ∅. Since e∗ ⊆ U¯, e′ cannot be inside U. Thus, e′ is covered by F and we have e′ ∈ F∗.

Note that |V (F∗)| is quite large here, in particular 1/|V (F∗)| ≪ 1/f for f = |V (F)|. This means that G being an (ε,ξ,f,r)-supercomplex does not necessarily allow us to extend a given subgraph H of G(r) to a copy of ∇(F∗,e∗)H as described in Deﬁnition 7.13. Fortunately, this will in fact not be necessary, as F∗ will only serve as an abstract auxiliary graph and will not appear as a subgraph of the absorber. (This is crucial since otherwise we would not be able to prove our main theorems with explicit bounds, let alone the bounds given in Theorem 1.4.)

We are now ready to prove Lemma 7.12.

Proof of Lemma 7.12. Given F and e0, we ﬁrst apply Lemma 7.23 to obtain a symmetric r-extender (F∗,e∗) such that F∗ has an F-decomposition F with e∗ ∈ F′ ∈ F and e∗ plays the

role of e0 in F′. For given h ∈ N, let k,m ∈ N be as in Lemma 7.22. Clearly, we may assume that there exists an F-divisible r-graph on at most h vertices. Together with Lemma 7.19, this implies that (k,m) ∈ Mr. Deﬁne

∗,e∗)

Mh := M(F

k,m .

Now, let H be any F-divisible r-graph on at most h vertices. By Lemma 7.22, there exists t ∈ N such that H + t · F has a strong m-regular [k]-colouring. By Lemma 7.19, we have

∇(F∗,e∗)(H + t · F) Mh. Let ψ1 be any e0-orientation of H + t · F. Observe that since e∗ plays the role of e0 in F′, ∇(F∗,e∗)(H + t · F) can be decomposed into a copy of ∇(F,e0)(H + t · F,ψ1) and s copies of F (where s = |H + t · F| · |F \ {F′}|). Hence, we have

∇(F,e0)(H + t · F,ψ1) + s · F ∇(F∗,e∗)(H + t · F)

by Proposition 7.4(ii). Thus, ∇(F,e0)(H +t·F,ψ1)+s·F Mh by transitivity of . Finally, let ψ2 be any e0-orientation of Mh. By Fact 7.15, there exists an e0-orientation ψ3 of ∇(F,e0)(H + t · F,ψ1) + s · F such that

∇(F,e0)(∇(F,e0)(H + t · F,ψ1) + s · F,ψ3) ∇(F,e0)(Mh,ψ2).

- 7.3. Proof of the Absorbing lemma. As discussed at the beginning of Section 7.2, we can now combine Lemma 7.5 and Lemma 7.12 to construct the desired absorber by concatenating transformers between certain auxiliary r-graphs, in particular the extension ∇Mh of the canonical multi-r-graph Mh. It is relatively straightforward to ﬁnd these auxiliary r-graphs within a given supercomplex G. The step when we need to ﬁnd ∇Mh is the reason why the deﬁnition of a supercomplex includes the notion of extendability. Proof of Lemma 7.2. If H is empty, then we can take A to be empty, so let us assume that


- H is not empty. In particular, G(r) is not empty. Recall also that we assume r ≥ 2. Let e0 ∈ F and let Mh be as in Lemma 7.12. Fix any e0-orientation ψ of Mh. By Lemma 7.12, there exist t1,t2,s1,s2,ψ1,ψ2,ψ1′ ,ψ2′ such that


- (7.6) ∇(F,e0)(∇(F,e0)(H + t1 · F,ψ1) + s1 · F,ψ1′ ) ∇(F,e0)(Mh,ψ);
- (7.7) ∇(F,e0)(∇(F,e0)(t2 · F,ψ2) + s2 · F,ψ2′ ) ∇(F,e0)(Mh,ψ). We can assume that 1/n ≪ 1/ℓ where ℓ := max{|V (Mh)|,t1,t2,s1,s2}.

Since G is (ξ,f + r,r)-dense, there exist disjoint Q1,1,... ,Q1,t1,Q2,1,... ,Q2,t2 ∈ G(f) which are also disjoint from V (H). For i ∈ [2] and j ∈ [ti], let Fi,j be a copy of F with V (Fi,j) = Qi,j. Let H1 := H ∪ j∈[t1] F1,j and H2 := j∈[t

2] F2,j and for i ∈ [2], deﬁne

Fi := {Fi,j : j ∈ [ti]}. So H1 is a copy of H + t1 · F and H2 is a copy of t2 · F. In fact, we will from now on assume (by redeﬁning ψi and ψi′) that for i ∈ [2], we have

- (7.8) ∇(F,e0)(∇(F,e0)(Hi,ψi) + si · F,ψi′) ∇(F,e0)(Mh,ψ).


For i ∈ [2], let (Hi′,Fi′) be obtained by extending Hi with a copy of ∇(F,e0)(Hi,ψi) in G (cf. Deﬁnition 7.13). We can assume that H1′ and H2′ are vertex-disjoint by ﬁrst choosing H1′ whilst avoiding V (H2) and subsequently choosing H2′ whilst avoiding V (H1′). (To see that this is possible we can e.g. use the fact that G is (ε,d,f,r)-regular for some d ≥ ξ.)

There exist disjoint Q′1,1,... ,Q′1,s1,Q′2,1,... ,Q′2,s2 ∈ G(f) which are also disjoint from V (H1′)∪ V (H2′). For i ∈ [2] and j ∈ [si], let Fi,j′ be a copy of F with V (Fi,j′ ) = Q′i,j. For i ∈ [2], let

Hi′′ := Hi′ ∪

Fi,j′ ;

j∈[si]

Fi′′ := {Fi,j′ : j ∈ [si]}.

Since Hi′′ is a copy of ∇(F,e0)(Hi,ψi) + si · F, we can assume (by redeﬁning ψi′) that

- (7.9) ∇(F,e0)(Hi′′,ψi′) ∇(F,e0)(Mh,ψ).

For i ∈ [2], let (Hi′′′,Fi′′′) be obtained by extending Hi′′ with a copy of ∇(F,e0)(Hi′′,ψi′) in G (cf. Deﬁnition 7.13). We can assume that H1′′′ and H2′′′ are vertex-disjoint.

Since G is (ξ,f,r)-extendable, it is straightforward to ﬁnd a copy M′ of ∇(F,e0)(Mh,ψ) in G(r) which is vertex-disjoint from H1′′′ and H2′′′.

Since Hi′′′ is a copy of ∇(F,e0)(Hi′′,ψi′), by (7.9) we have Hi′′′ M′ for i ∈ [2]. Using

Fact 7.11(ii) repeatedly, we can see that both H1′′′ and H2′′′ are F-divisible. Together with Proposition 7.4(iii), this implies that M′ is F-divisible as well.

Let T1 := (H1 − H) ∪ H1′′ and T2 := H2 ∪ H2′′. For i ∈ [2], let Fi,1 := Fi′ ∪ Fi′′ and Fi,2 := Fi ∪ Fi′′′. We claim that F1,1,F1,2,F2,1,F2,2 are 2-well separated F-packings in G such that

- (7.10) F1(,r1) = T1 ∪ H, F1(,r2) = T1 ∪ H1′′′, F2(,r2) = T2 ∪ H2′′′ and F2(,r1) = T2.


(In particular, T1 is a 2-well separated (H,H1′′′;F)-transformer in G and T2 is a 2-well separated (H2′′′,∅;F)-transformer in G.) Indeed, we clearly have that F1,F2,F1′′,F2′′ are 1-well separated F-packings in G, where F1(r) = H1 −H, F2(r) = H2, and for i ∈ [2], Fi′′(r) = Hi′′ − Hi′. Moreover, by Fact 7.14, for i ∈ [2], Fi′ and Fi′′′ are 1-well separated F-packings in G with Fi′(r) = Hi ∪ Hi′ and Fi′′′(r) = Hi′′ ∪ Hi′′′. Note that

T1 ∪ H = H1 ∪ H1′′ = (H1 ∪ H1′) ∪· (H1′′ − H1′) = F1′(r) ∪· F1′′(r) = F1(,r1);

- T1 ∪ H1′′′ = (H1 − H) ∪· (H1′′ ∪ H1′′′) = F1(r) ∪· F1′′′(r) = F1(,r2);
- T2 ∪ H2′′′ = H2 ∪· (H2′′ ∪ H2′′′) = F2(r) ∪· F2′′′(r) = F2(,r2); T2 = H2 ∪ H2′′ = (H2 ∪ H2′) ∪· (H2′′ − H2′) = F2′(r) ∪· F2′′(r) = F2(,r1).


To check that F1,1, F1,2, F2,1 and F2,2 are 2-well separated F-packings, by Fact 4.3(ii) it is now enough to show for i ∈ [2] that Fi′ and Fi′′ are (r + 1)-disjoint and that Fi and Fi′′′ are (r + 1)-disjoint. Note that for all F′ ∈ Fi′ and F′′ ∈ Fi′′, we have V (F′) ⊆ V (Hi′) and V (F′′) ∩ V (Hi′) = ∅, thus V (F′) ∩ V (F′′) = ∅. For all F′ ∈ Fi and F′′ ∈ Fi′′′, we have V (F′) ⊆ V (Hi) and |V (F′′) ∩ V (Hi)| ≤ |V (F′′) ∩ V (Hi′′)| ≤ r by Fact 7.14, thus |V (F′) ∩ V (F′′)| ≤ r. This completes the proof of (7.10).

Let

Or := H1 ∪ H1′′ ∪ H2 ∪ H2′′; Or+1,3 := F1≤,1(r+1) ∪ F1≤,2(r+1) ∪ F2≤,1(r+1) ∪ F2≤,2(r+1).

By Fact 4.3(i), ∆(Or+1,3) ≤ 8(f − r). Note that H1′′′,M′ ⊆ G(r) − (Or ∪ H2′′′). Thus, by Proposition 4.5(v) and Lemma 7.5, there exists a (κ/3)-well separated (H1′′′,M′;F)-transformer

- T3 in G − (Or ∪ H2′′′) − Or+1,3 with ∆(T3) ≤ γn/3. Let F3,1 and F3,2 be (κ/3)-well separated F-packings in G − (Or ∪ H2′′′) − Or+1,3 such that F3(,r1) = T3 ∪ H1′′′ and F3(,r2) = T3 ∪ M′.


Similarly, let Or+1,4 := Or+1,3∪F3≤,1(r+1)∪F3≤,2(r+1). By Fact 4.3(i), ∆(Or+1,4) ≤ (8+2κ/3)(f − r). Note that H2′′′,M′ ⊆ G(r) −(Or ∪H1′′′ ∪T3). Using Proposition 4.5(v) and Lemma 7.5 again, we can ﬁnd a (κ/3)-well separated (H2′′′,M′;F)-transformer T4 in G − (Or ∪ H1′′′ ∪ T3) − Or+1,4 with ∆(T4) ≤ γn/3. Let F4,1 and F4,2 be (κ/3)-well separated F-packings in G − (Or ∪ H1′′′ ∪ T3) − Or+1,4 such that of F4(,r1) = T4 ∪ H2′′′ and F4(,r2) = T4 ∪ M′.

Let

A := T1 ∪· H1′′′ ∪· T3 ∪· M′ ∪· T4 ∪· H2′′′ ∪· T2;

F◦ := F1,2 ∪ F3,2 ∪ F4,1 ∪ F2,1; F• := F1,1 ∪ F3,1 ∪ F4,2 ∪ F2,2.

Clearly, A ⊆ G(r), and ∆(A) ≤ γn. Moreover, A and H are edge-disjoint. Using (7.10), we can check that

F◦(r) = F1(,r2) ∪· F3(,r2) ∪· F4(,r1) ∪· F2(,r1) = (T1 ∪ H1′′′) ∪· (T3 ∪ M′) ∪· (T4 ∪ H2′′′) ∪· T2 = A; F•(r) = F1(,r1) ∪· F3(,r1) ∪· F4(,r2) ∪· F2(,r2) = (H ∪ T1) ∪· (H1′′′ ∪ T3) ∪· (M′ ∪ T4) ∪· (H2′′′ ∪ T2) = A ∪ H.

By deﬁnition of Or+1,3 and Or+1,4, we have that F1,2,F3,2,F4,1,F2,1 are (r + 1)-disjoint. Thus, F◦ is a (2·κ/3+4)-well separated F-packing in G by Fact 4.3(ii). Similarly, F• is a (2·κ/3+4)well separated F-packing in G. So A is indeed a κ-well separated F-absorber for H in G.

8. Proof of the main theorems

- 8.1. Main complex decomposition theorem. We can now deduce our main decomposition result for supercomplexes. The main ingredients for the proof of Theorem 3.8 are Lemma 6.3 (to ﬁnd a vortex), Lemma 7.2 (to ﬁnd absorbers for the possible leftovers in the ﬁnal vortex set), and Lemma 6.4 (to cover all edges outside the ﬁnal vortex set).


Proof of Theorem 3.8. We proceed by induction on r. The case r = 1 forms the base case of the induction and in this case we do not rely on any inductive assumption. Suppose that r ∈ N and that (∗)i is true for all i ∈ [r − 1].

We may assume that 1/n ≪ 1/κ ≪ ε. Choose new constants κ′,m′ ∈ N and γ,µ > 0 such that

1/n ≪ 1/κ ≪ γ ≪ 1/m′ ≪ 1/κ′ ≪ ε ≪ µ ≪ ξ,1/f and suppose that F is a weakly regular r-graph on f > r vertices.

Let G be an F-divisible (ε,ξ,f,r)-supercomplex on n vertices. We are to show the existence of a κ-well separated F-decomposition of G. By Lemma 6.3, there exists a (2√ε,µ,ξ−ε,f,r,m)vortex U0,U1,... ,Uℓ in G for some µm′ ≤ m ≤ m′. Let H1,... ,Hs be an enumeration of all spanning F-divisible subgraphs of G[Uℓ](r). Clearly, s ≤ 2(mr). We will now ﬁnd edge-disjoint subgraphs A1,... ,As of G(r) and √κ-well separated F-packings F1,◦,F1,•,... ,Fs,◦,Fs,• in G such that for all i ∈ [s] we have that

![image 28](<2017-glock-hypergraph-designs-arbitrary_images/imageFile28.png>)

![image 29](<2017-glock-hypergraph-designs-arbitrary_images/imageFile29.png>)

- (A1) Fi,(r◦) = Ai and Fi,(r•) = Ai ∪ Hi;
- (A2) ∆(Ai) ≤ γn;
- (A3) Ai[U1] is empty;
- (A4) Fi,≤•,G[U1],F1≤,◦,... ,Fi≤−1,◦,Fi≤+1,◦,... ,Fs,≤◦ are (r + 1)-disjoint.


Suppose that for some t ∈ [s], we have already found edge-disjoint A1,... ,At−1 together with

- F1,◦,F1,•,... ,Ft−1,◦,Ft−1,• that satisfy (A1)–(A4) (with t − 1 playing the role of s). Let


Tt := (G(r)[U1] − Ht) ∪

Ai;

i∈[t−1]

(Fi,≤◦(r+1) ∪ Fi,≤•(r+1)).

Tt′ := G(r+1)[U1] ∪

i∈[t−1]

Clearly, ∆(Tt) ≤ µn+sγn ≤ 2µn by (V2) and (A2). Also, ∆(Tt′) ≤ µn+2s√κ(f −r) ≤ 2µn by (V2) and Fact 4.3(i). Thus, applying Proposition 4.5(v) twice we see that Gabs,t := G − Tt − Tt′ is still a (√µ,ξ/2,f,r)-supercomplex. Moreover, Ht ⊆ G(abs,tr) by (A3). Hence, by Lemma 7.2, there exists a √κ-well separated F-absorber At for Ht in Gabs,t with ∆(At) ≤ γn. Let Ft,◦ and Ft,• be √κ-well separated F-packings in Gabs,t ⊆ G such that Ft,(r◦) = At and Ft,(r•) = At ∪ Ht. Clearly, At is edge-disjoint from A1,... ,At−1. Moreover, (A3) holds since G(abs,tr) [U1] = Ht and At is edge-disjoint from Ht, and (A4) holds with t playing the role of s due to the deﬁnition of Tt′.

![image 30](<2017-glock-hypergraph-designs-arbitrary_images/imageFile30.png>)

![image 31](<2017-glock-hypergraph-designs-arbitrary_images/imageFile31.png>)

![image 32](<2017-glock-hypergraph-designs-arbitrary_images/imageFile32.png>)

![image 33](<2017-glock-hypergraph-designs-arbitrary_images/imageFile33.png>)

Let A∗ := A1 ∪ ··· ∪ As and T∗ := i∈[s](Fi,≤◦(r+1) ∪ Fi,≤•(r+1)). We claim that the following hold:

- (A1′) for every F-divisible subgraph H∗ of G[Uℓ](r), A∗ ∪ H∗ has an s√κ-well separated Fdecomposition F∗ with F∗≤ ⊆ G[T∗];

![image 34](<2017-glock-hypergraph-designs-arbitrary_images/imageFile34.png>)

- (A2′) ∆(A∗) ≤ εn and ∆(T∗) ≤ 2s√κ(f − r) ≤ εn;

![image 35](<2017-glock-hypergraph-designs-arbitrary_images/imageFile35.png>)

- (A3′) A∗[U1] and T∗[U1] are empty. For (A1′), we have that H∗ = Ht for some t ∈ [s]. Then F∗ := Ft,• ∪ i∈[s]\{t} Fi,◦ is an


F-decomposition of A∗ ∪ H∗ = (At ∪ Ht) ∪ i∈[s]\{t} Ai by (A1) and since Ht,A1,... ,As are pairwise edge-disjoint. By (A4) and Fact 4.3(ii), F∗ is s√κ-well separated. We clearly have F∗≤ ⊆ G and F∗≤(r+1) ⊆ T∗. Thus F∗≤ ⊆ G[T∗] and so (A1′) holds. It is straightforward to check that (A2′) follows from (A2) and Fact 4.3(i), and that (A3′) follows from (A3) and (A4).

![image 36](<2017-glock-hypergraph-designs-arbitrary_images/imageFile36.png>)

Let Galmost := G − A∗ − T∗. By (A2′) and Proposition 4.5(v), Galmost is an (√ε,ξ/2,f,r)supercomplex. Moreover, since A∗ must be F-divisible, we have that Galmost is F-divisible. By (A3′), U1,... ,Uℓ is a (2√ε,µ,ξ − ε,f,r,m)-vortex in Galmost[U1]. Moreover, (A2′) and Proposition 6.7 imply that U1 is (ε1/5,µ,ξ/2,f,r)-random in Galmost and U1 \ U2 is (ε1/5,µ(1 − µ),ξ/2,f,r)-random in Galmost. Hence, U0,U1,... ,Uℓ is still an (ε1/5,µ,ξ/2,f,r,m)-vortex in Galmost. Thus, by Lemma 6.4, there exists a 4κ′-well separated F-packing Falmost in Galmost which covers all edges of G(almostr) except possibly some inside Uℓ. Let H∗ := (G(almostr) − Falmost(r) )[Uℓ]. Since H∗ is F-divisible, A∗ ∪ H∗ has an s√κ-well separated F-decomposition F∗ with F∗≤ ⊆ G[T∗] by (A1′). Clearly,

![image 37](<2017-glock-hypergraph-designs-arbitrary_images/imageFile37.png>)

![image 38](<2017-glock-hypergraph-designs-arbitrary_images/imageFile38.png>)

![image 39](<2017-glock-hypergraph-designs-arbitrary_images/imageFile39.png>)

G(r) = G(almostr) ∪· A∗ = Falmost(r) ∪· H∗ ∪· A∗ = Falmost(r) ∪· F∗(r),

and Falmost and F∗ are (r +1)-disjoint. Thus, by Fact 4.3(ii), Falmost ∪F∗ is a (4κ′ +s√κ)-well separated F-decomposition of G, completing the proof.

![image 40](<2017-glock-hypergraph-designs-arbitrary_images/imageFile40.png>)

- 8.2. Resolvable partite designs. Perhaps surprisingly, it is much easier to obtain decompositions of complete partite r-graphs than of complete (non-partite) r-graphs. In fact, we can obtain (explicit) resolvable decompositions (sometimes referred to as Kirkman systems or large sets of designs) in the partite setting using basic linear algebra. We believe that this result and the corresponding construction are of independent interest. Here, we will use this result to show that for every r-graph F, there is a weakly regular r-graph F∗ which is F-decomposable (see


- Lemma 8.2). Let G be a complex. We say that a Kf(r)-decomposition K of G is resolvable if K can be


partitioned into Kf(r−1)-decompositions of G, that is, K≤(f) can be partitioned into sets Y1,... ,Yt such that for each i ∈ [t], Ki := {G(r−1)[Q] : Q ∈ Yi} is a Kf(r−1)-decomposition of G. Clearly, K1,... ,Kt are r-disjoint.

Let Kn×k be the complete k-partite complex with each vertex class having size n. More precisely, Kn×k has vertex set V1 ∪ ···· ∪· Vk such that |Vi| = n for all i ∈ [k] and e ∈ Kn×k if and only if e is crossing, that is, intersects with each Vi in at most one vertex. Since every subset of a crossing set is crossing, this deﬁnes a complex.

Theorem 8.1. Let q be a prime power and 2f ≤ q. Then for every r ∈ [f − 1], Kq×f has a resolvable Kf(r)-decomposition.

Let us ﬁrst motivate the proof of Theorem 8.1. Let F be the ﬁnite ﬁeld of order q. Assume that each class of Kq×f is a copy of F. Suppose further that we are given a matrix A ∈ F(f−r)×f with the property that every (f − r) × (f − r)-submatrix is invertible. Identifying Kq(f×)f with Ff in the obvious way, we let K be the set of all Q ∈ Kq(f×)f with AQ = 0. Fixing the entries of r coordinates of Q (which can be viewed as ﬁxing an r-set) transforms this into an equation A′Q′ = b′, where A′ is an (f −r)×(f −r)-submatrix of A. Thus, there exists a unique solution, which will translate into the fact that every r-set of Kq×f is contained in exactly one f-set of K, i.e. we have a Kf(r)-decomposition.

There are several known classes of matrices over ﬁnite ﬁelds which have the desired property that every square submatrix is invertible. We use so-called Cauchy matrices, introduced by

Cauchy [6], which are very convenient for our purposes. For an application of Cauchy matrices to coding theory, see e.g. [5].

- Let F be a ﬁeld and let x1,... ,xm,y1,... ,yn be distinct elements of F. The Cauchy matrix


generated by (xi)i∈[m] and (yj)j∈[n] is the m×n-matrix A ∈ Fm×n deﬁned by ai,j := (xi −yj)−1. Obviously, every submatrix of a Cauchy matrix is itself a Cauchy matrix. For m = n, it is well known that the Cauchy determinant is given by the following formula (cf. [30]):

(xj − xi)(yi − yj) 1≤i,j≤n(xi − yj)

det(A) = 1≤i<j≤n

. In particular, every square Cauchy matrix is invertible.

![image 41](<2017-glock-hypergraph-designs-arbitrary_images/imageFile41.png>)

Proof of Theorem 8.1. Let F be the ﬁnite ﬁeld of order q. Since 2f ≤ q, there exists a Cauchy matrix A ∈ F(f−r+1)×f. Let ˆa be the ﬁnal row of A and let A′ ∈ F(f−r)×f be obtained from A by deleting ˆa.

We assume that the vertex set of Kq×f is F×[f]. Hence, for every e ∈ Kq×f, there are unique 1 ≤ i1 < ··· < i|e| ≤ f and x1,... ,x|e| ∈ F such that e = {(xj,ij) : j ∈ [|e|]}. Let

  

   ∈ F|e|.

x1 . x|e|

Ie := {i1,... ,i|e|} ⊆ [f] and xe :=

- Clearly, Q ∈ Kq(f×)f is uniquely determined by xQ.


Deﬁne Y ⊆ Kq(f×)f as the set of all Q ∈ Kq(f×)f which satisfy A′ · xQ = 0. Moreover, for each x∗ ∈ F, deﬁne Yx∗ ⊆ Y as the set of all Q ∈ Y which satisfy aˆ·xQ = x∗. Clearly, {Yx∗ : x∗ ∈ F} is a partition of Y . Let K := {Kq(r×)f[Q] : Q ∈ Y } and Kx∗ := {Kq(r×−f1)[Q] : Q ∈ Yx∗} for each x∗ ∈ F. We claim that K is a Kf(r)-decomposition of Kq×f and that Kx∗ is a Kf(r−1)decomposition of Kq×f for each x∗ ∈ F.

For I ⊆ [f], let AI be the (f − r + 1) × |I|-submatrix of A obtained by deleting the columns

which are indexed by [f] \ I. Similarly, for I ⊆ [f], let A′I be the (f − r) × |I|-submatrix of A′ obtained by deleting the columns which are indexed by [f] \ I. Finally, for a vector x ∈ Ff and

- I ⊆ [f], let xI ∈ F|I| be the vector obtained from x by deleting the coordinates not in I. Observe that for all e ∈ Kq×f and Q ∈ Kq(f×)f, we have


e ⊆ Q if and only if xQI

- (8.1) = xe.


e

Consider e ∈ Kq(r×)f. By (8.1), the number of Q ∈ Y containing e is equal to the number of x ∈ Ff such that A′ · x = 0 and xIe = xe, or equivalently, the number of x′ ∈ Ff−r satisfying A′I

· x′ = 0. Since A′[f]\I

· xe + A′[f]\I

is an (f − r) × (f − r)-Cauchy matrix, the equation A′[f]\I

- e


e

e

· xe has a unique solution x′ ∈ Ff−r, i.e. there is exactly one Q ∈ Y which contains e. Thus, K is a Kf(r)-decomposition of Kq×f.

· x′ = −A′I

e

e

Now, ﬁx x∗ ∈ F and e ∈ Kq(×r−f1). By (8.1), the number of Q ∈ Yx∗ containing e is equal to the number of x ∈ Ff such that A′ · x = 0, ˆa · x = x∗ and xIe = xe, or equivalently, the number of x′ ∈ Ff−(r−1) satisfying AIe ·xe+A[f]\Ie·x′ =

0 x∗

. Since A[f]\Ie is an (f −r+1)×(f −r+1)Cauchy matrix, this equation has a unique solution x′ ∈ Ff−r+1, i.e. there is exactly one Q ∈ Yx∗ which contains e. Hence, Kx∗ is a Kf(r−1)-decomposition of Kq×f.

Our application of Theorem 8.1 is as follows.

- Lemma 8.2. Let 2 ≤ r < f. Let F be any r-graph on f vertices. There exists a weakly regular r-graph F∗ on at most 2f · f! vertices which has a 1-well separated F-decomposition. Proof. Choose a prime power q with f! ≤ q ≤ 2f!. Let V (F) = {v1,... ,vf}. By Theorem 8.1, there exists a resolvable Kf(r)-decomposition K of Kq×f. Let the vertex classes of Kq×f be


V1,... ,Vf. Let K1,... ,Kq be a partition of K into Kf(r−1)-decompositions of Kq×f. (We will only need K1,... ,Kf!.) We now construct F∗ with vertex set V (Kq×f) as follows: Let π1,... ,πf!

be an enumeration of all permutations on [f]. For every i ∈ [f!] and Q ∈ Ki≤(f), let Fi,Q be a copy of F with V (F) = Q such that for every j ∈ [f], the unique vertex in Q ∩ Vπi(j) plays the role of vj. Let

F∗ :=

Fi,Q;

i∈[f!],Q∈Ki≤(f)

F := {Fi,Q : i ∈ [f!],Q ∈ Ki≤(f)}. Since K1,... ,Kf! are r-disjoint, we have |V (F′) ∩ V (F′′)| < r for all distinct F′,F′′ ∈ F. Thus,

- F is a 1-well separated F-decomposition of F∗.


We now show that F∗ is weakly regular. Let i ∈ [r −1]0 and S ∈ V (Fi ∗) . If S is not crossing, then |F∗(S)| = 0, so assume that S is crossing. If i = r − 1, then S plays the role of every (r − 1)-subset of V (F) exactly k times, where k is the number of permutations on [f] that map [r − 1] to [r − 1]. Hence,

|F∗(S)| = |F|rk = |F| · r!(f − r + 1)! =: sr−1. If i < r − 1, then S is contained in exactly ci := r− f−1−i i qr−1−i crossing (r − 1)-sets. Thus, |F∗(S)| =

sr−1ci r − i

=: si. Therefore, F∗ is weakly (s0,... ,sr−1)-regular.

![image 42](<2017-glock-hypergraph-designs-arbitrary_images/imageFile42.png>)

- 8.3. Proofs of Theorems 1.1, 1.2 and 1.4. We now prove our main theorems which guarantee F-decompositions in r-graphs of high minimum degree (for weakly regular r-graphs F, see Theorem 1.4), and F-designs in typical r-graphs (for arbitrary r-graphs F, see Theorem 1.1). We will also derive Theorem 1.2.


We ﬁrst prove the minimum degree version (for weakly regular r-graphs F). Instead of directly proving Theorem 1.4 we actually prove a stronger ‘local resilience version’. Let Hr(n,p) denote the random binomial r-graph on [n] whose edges appear independently with probability p.

Theorem 8.3 (Resilience version). Let p ∈ (0,1] and f,r ∈ N with f > r and let

r!p2r(f+rr) 3 · 14rf2r

.

c(f,r,p) :=

![image 43](<2017-glock-hypergraph-designs-arbitrary_images/imageFile43.png>)

Then the following holds whp for H ∼ Hr(n,p). For every weakly regular r-graph F on f vertices and any r-graph L on [n] with ∆(L) ≤ c(f,r,p)n, H △ L has an F-decomposition whenever it is F-divisible.

The case p = 1 immediately implies Theorem 1.4. Proof. Choose n0 ∈ N and ε > 0 such that 1/n0 ≪ ε ≪ p,1/f and let n ≥ n0, c′ :=

1.1 · 2r f+r r (f − r)!

c(f,r,p), ξ := 0.99/f!, ξ′ := 0.95ξp2r(f+rr), ξ′′ := 0.9(1/4)(f+fr)(ξ′ − c′).

![image 44](<2017-glock-hypergraph-designs-arbitrary_images/imageFile44.png>)

Recall that the complete complex Kn is an (ε,ξ,f,r)-supercomplex (cf. Example 3.3). Let H ∼ Hr(n,p). We can view H as a random subgraph of Kn(r). By Corollary 4.6, the following holds whp for all L ⊆ Kn(r) with ∆(L) ≤ c(f,r,p)n:

Kn[H △ L] is a (3ε + c′,ξ′ − c′,f,r)-supercomplex. Note that c′ ≤ p

2r(f+rr)

2.7(2√e)rf!. Thus, 2(2√e)r·(3ε+c′) ≤ ξ′−c′. Lemma 3.5 now implies that Kn[H△ L] is an (ε,ξ′′,f,r)-supercomplex. Hence, if H △ L is F-divisible, it has an F-decomposition by Theorem 3.8.

![image 45](<2017-glock-hypergraph-designs-arbitrary_images/imageFile45.png>)

![image 46](<2017-glock-hypergraph-designs-arbitrary_images/imageFile46.png>)

![image 47](<2017-glock-hypergraph-designs-arbitrary_images/imageFile47.png>)

Next, we derive Theorem 1.1. As indicated previously, we cannot apply Theorem 3.8 directly, but have to carry out two reductions. As shown in Lemma 8.2, we can ‘perfectly’ pack any given r-graph F into a weakly regular r-graph F∗. We also need the following lemma, which we will prove later in Section 9. It allows us to remove a sparse F-decomposable subgraph L from an F-divisible r-graph G to achieve that G−L is F∗-divisible. Note that we do not need to assume that F∗ is weakly regular.

- Lemma 8.4. Let 1/n ≪ γ ≪ ξ,1/f∗ and r ∈ [f∗ − 1]. Let F be an r-graph. Let F∗ be an r-graph on f∗ vertices which has a 1-well separated F-decomposition. Let G be an r-graph on n


vertices such that for all A ⊆ Vr−(G1) with |A| ≤ fr∗−−11 , we have | S∈A G(S)| ≥ ξn. Let O be an (r + 1)-graph on V (G) with ∆(O) ≤ γn. Then there exists an F-divisible subgraph D ⊆ G with ∆(D) ≤ γ−2 such that the following holds: for every F-divisible r-graph H on V (G) which is edge-disjoint from D, there exists a subgraph D∗ ⊆ D such that H ∪ D∗ is F∗-divisible and D − D∗ has a 1-well separated F-decomposition F such that F≤(r+1) and O are edge-disjoint.

In particular, we will apply this lemma when G is F-divisible and thus H := G − D is Fdivisible. Then L := D − D∗ is a subgraph of G with ∆(L) ≤ γ−2 and has a 1-well separated F-decomposition F such that F≤(r+1) and O are edge-disjoint. Moreover, G − L = H ∪ D∗ is F∗-divisible.

We can deduce the following corollary from the case F = Kr(r) of Lemma 8.4. Corollary 8.5. Let 1/n ≪ γ ≪ ξ,1/f and r ∈ [f − 1]. Let F be an r-graph on f vertices.

- Let G be an r-graph on n vertices such that for all A ⊆ Vr−(G1) with |A| ≤ fr−−11 , we have


| S∈A G(S)| ≥ ξn. Then there exists a subgraph D ⊆ G with ∆(D) ≤ γ−2 such that the following holds: for any r-graph H on V (G) which is edge-disjoint from D, there exists a subgraph D∗ ⊆ D

such that H ∪ D∗ is F-divisible.

In particular, using H := G − D, there exists a subgraph L := D − D∗ ⊆ G with ∆(L) ≤ γ−2 such that G − L = H ∪ D∗ is F-divisible. Proof. Apply Lemma 8.4 with F,Kr(r) playing the roles of F∗,F.

We now prove the following theorem, which immediately implies the case λ = 1 of Theorem 1.1. Theorem 8.6. Let 1/n ≪ γ,1/κ ≪ c,p,1/f and r ∈ [f − 1], and

- q + r
- r


c ≤ ph/(qr4q), where h := 2r

- (8.2) and q := 2f · f!.


Let F be any r-graph on f vertices. Suppose that G is a (c,h,p)-typical F-divisible r-graph on n vertices. Let O be an (r + 1)-graph on V (G) with ∆(O) ≤ γn. Then G has a κ-well separated F-decomposition F such that F≤(r+1) and O are edge-disjoint.

Proof. By Lemma 8.2, there exists a weakly regular r-graph F∗ on f∗ ≤ q vertices which has a 1-well separated F-decomposition.

By Lemma 8.4 (with 0.5p(fr∗−−11) playing the role of ξ), there exists a subgraph L ⊆ G with ∆(L) ≤ γ−2 such that G − L is F∗-divisible and L has a 1-well separated F-decomposition Fdiv such that Fdiv≤(r+1) and O are edge-disjoint. By Fact 4.3(i), ∆(Fdiv≤(r+1)) ≤ f − r. Let

G′ := G↔ − L − Fdiv≤(r+1) − O. By Example 3.4, G↔ is an (ε,ξ,f∗,r)-supercomplex, where ε := 2f∗−r+1c/(f∗ − r)! and ξ := (1 − 2f∗+1c)p2r(f∗r+r)/f∗!. Observe that assumption (8.2) now guarantees that 2(2√e)rε ≤ ξ. Thus, by Lemma 3.5, G↔ is a (γ,ξ′,f∗,r)-supercomplex, where ξ′ := 0.9(1/4)(f∗r+r)ξ. By Proposition 4.5(v), we have that G′ is a (√γ,ξ′/2,f∗,r)-supercomplex. Moreover, G′ is F∗divisible. Thus, by Theorem 3.8, G′ has a (κ − 1)-well separated F∗-decomposition F∗. Since

![image 48](<2017-glock-hypergraph-designs-arbitrary_images/imageFile48.png>)

![image 49](<2017-glock-hypergraph-designs-arbitrary_images/imageFile49.png>)

- F∗ has a 1-well separated F-decomposition, we can conclude that G′ has a (κ−1)-well separated


F-decomposition Fcomplex. Let F := Fdiv ∪ Fcomplex. By Fact 4.3(ii), F is a κ-well separated F-decomposition of G. Moreover, F≤(r+1) and O are edge-disjoint.

It remains to derive Theorem 1.1 from Theorem 8.6 and Corollary 8.5.

- Proof of Theorem 1.1. Choose a new constant κ ∈ N such that 1/n ≪ γ ≪ 1/κ ≪ c,p,1/f.

Suppose that G is a (c,h,p)-typical (F,λ)-divisible r-graph on n vertices. Split G into two

subgraphs G′1 and G′2 which are both (c + γ,h,p/2)-typical (a standard Chernoﬀ-type bound shows that whp a random splitting of G yields the desired property).

By Corollary 8.5 (applied with G′2,0.5(p/2)(fr−−11) playing the roles of G,ξ), there exists a subgraph L∗ ⊆ G′2 with ∆(L∗) ≤ κ such that G2 := G′2 −L∗ is F-divisible. Let G1 := G′1 ∪L∗ = G − G2. Clearly, G1 is still (F,λ)-divisible. By repeated applications of Corollary 8.5, we can ﬁnd edge-disjoint subgraphs L1,... ,Lλ of G1 such that Ri := G1 − Li is F-divisible and ∆(Li) ≤ κ for all i ∈ [λ]. Indeed, suppose that we have already found L1,... ,Li−1. Then ∆(L1 ∪ ··· ∪ Li−1) ≤ λκ ≤ γ1/2n (recall that λ ≤ γn). Thus, by Corollary 8.5, there exists a subgraph Li ⊆ G′1 − (L1 ∪ ··· ∪ Li−1) with ∆(Li) ≤ κ such that G1 − Li is F-divisible.

Let G′′2 := G2 ∪ L1 ∪ ··· ∪ Lλ. We claim that G′′2 is F-divisible. Indeed, let S ⊆ V (G) with

|S| ≤ r−1. We then have that |G′′2(S)| = |G2(S)|+ i∈[λ] |(G1−Ri)(S)| = |G2(S)|+λ|G1(S)|− i∈[λ] |Ri(S)| ≡ 0 mod Deg(F)|S|. Since G′1 and G′2 are both (c + γ,h,p/2)-typical and ∆(L∗ ∪ L1 ∪ ··· ∪ Lλ) ≤ 2γ1/2n, we

have that each of G2, G′′2, R1,... ,Rλ is (c + γ1/3,h,p/2)-typical (and they are F-divisible by construction).

Using Theorem 8.6 repeatedly, we can thus ﬁnd κ-well separated F-decompositions F1,... ,Fλ−1

of G2, a κ-well separated F-decomposition F∗ of G′′2, and for each i ∈ [λ], a κ-well separated F-decomposition Fi′ of Ri. Moreover, we can assume that all these decompositions are pairwise (r+1)-disjoint. Indeed, this can be achieved by choosing them successively: Let O consist of the (r+1)-sets which are covered by the decompositions we have already found. Then by Fact 4.3(i) we have that ∆(O) ≤ 2λ · κ(f − r) ≤ γ1/2n. Hence, using Theorem 8.6, we can ﬁnd the next κ-well separated F-decomposition which is (r + 1)-disjoint from the previously chosen ones.

Then F := F∗ ∪ i∈[λ−1] Fi ∪ i∈[λ] Fi′ is the desired (F,λ)-design. Indeed, every edge of G1−(L1∪···∪Lλ) is covered by each of F1′,... ,Fλ′ . For each i ∈ [λ], every edge of Li is covered by F∗ and each of F1′,... ,Fi′−1,Fi′+1,... ,Fλ′ . Finally, every edge of G2 is covered by each of F1,... ,Fλ−1 and F∗.

Finally, we also prove Theorem 1.2, which is an immediate consequence of Theorem 8.6 and Corollary 8.5.

- Proof of Theorem 1.2. Apply Corollary 8.5 (with G,0.5p(fr−−11) playing the roles of G,ξ) to ﬁnd a subgraph L ⊆ G with ∆(L) ≤ C such that G − L is F-divisible. It is easy to see that


- G − L is (1.1c,h,p)-typical. Thus, we can apply Theorem 8.6 to obtain an F-decomposition F of G − L.


9. Achieving divisibility It remains to show that we can turn every F-divisible r-graph G into an F∗-divisible r-graph

- G′ by removing a sparse F-decomposable subgraph of G, that is, to prove Lemma 8.4. Note that in Lemma 8.4, we do not need to assume that F∗ is weakly regular. On the other hand, our argument heavily relies on the assumption that F∗ is F-decomposable.


We ﬁrst sketch the argument. Let F∗ be F-decomposable, let bk := Deg(F∗)k and hk := Deg(F)k. Clearly, we have hk | bk. First, consider the case k = 0. Then b0 = |F∗| and h0 = |F|. We know that |G| is divisible by h0. Let 0 ≤ x < b0 be such that |G| ≡ x mod b0. Since h0 divides |G| and b0, it follows that x = ah0 for some 0 ≤ a < b0/h0. Thus, removing a

edge-disjoint copies of F from G yields an r-graph G′ such that |G′| = |G| − ah0 ≡ 0 mod b0, as desired. This will in fact be the ﬁrst step of our argument.

We then proceed by achieving Deg(G′)1 ≡ 0 mod b1. Suppose that the vertices of G′ are ordered v1,... ,vn. We will construct a degree shifter which will ﬁx the degree of v1 by allowing the degree of v2 to change, whereas all other degrees are unaﬀected (modulo b1). Step by step, we will ﬁx all the degrees from v1,... ,vn−1. Fortunately, the degree of vn will then automatically be divisible by b1. For k > 1, we will proceed similarly, but the procedure becomes more intricate. It is in general impossible to shift degree from one k-set to another one without aﬀecting the degrees of any other k-set. Roughly speaking, the degree shifter will contain a set of 2k special ‘root vertices’, and the degrees of precisely 2k k-subsets of this root set change, whereas all other k-degrees are unaﬀected (modulo bk). This will allow us to ﬁx all the degrees of k-sets in G′ except the ones inside some ﬁnal (2k − 1)-set, where we use induction on k as well. Fortunately, the remaining k-sets will again automatically satisfy the desired divisibility condition (cf. Lemma 9.5).

The proof of Lemma 8.4 divides into three parts. In the ﬁrst subsection, we will construct the degree shifters. In the second subsection, we show on a very abstract level (without considering a particular host graph) how the shifting has to proceed in order to achieve overall divisibility. Finally, we will prove Lemma 8.4 by embedding our constructed shifters (using Lemma 4.7) according to the given shifting procedure.

- 9.1. Degree shifters. The aim of this subsection is to show the existence of certain r-graphs which we call degree shifters. They allow us to locally ‘shift’ degree among the k-sets of some host graph G.


Deﬁnition 9.1 (x-shifter). Let 1 ≤ k < r and let F,F∗ be r-graphs. Given an r-graph Tk and distinct vertices x01,... ,x0k,x11,... ,x1k of Tk, we say that Tk is an (x01,... ,x0k,x11,... ,x1k)-shifter with respect to F,F∗ if the following hold:

- (SH1) Tk has a 1-well separated F-decomposition F such that for all F′ ∈ F and all i ∈ [k], |V (F′) ∩ {x0i ,x1i }| ≤ 1;
- (SH2) |Tk(S)| ≡ 0 mod Deg(F∗)|S| for all S ⊆ V (Tk) with |S| < k;
- (SH3) for all S ∈ V (kTk) ,


(−1) i∈[k] ziDeg(F)k mod Deg(F∗)k if S = {xzii : i ∈ [k]}, 0 mod Deg(F∗)k otherwise.

|Tk(S)| ≡

We will now show that such shifters exist. Ultimately, we seek to ﬁnd them as rooted subgraphs in some host graph G. Therefore, we impose additional conditions which will allow us to apply Lemma 4.7.

- Lemma 9.2. Let 1 ≤ k < r, let F,F∗ be r-graphs and suppose that F∗ has a 1-well separated F-decomposition F. Let f∗ := |V (F∗)|. There exists an (x01,... ,x0k,x11,... ,x1k)-shifter Tk with respect to F,F∗ such that Tk[X] is empty and Tk has degeneracy at most fr∗−−11 rooted at X, where X := {x01,... ,x0k,x11,... ,x1k}.


In order to prove Lemma 9.2, we will ﬁrst prove a multigraph version (Lemma 9.4), which is more convenient for our construction. We will then recover the desired (simple) r-graph by applying an operation similar to the extension operator ∇(F,e0) deﬁned in Section 7.2. The diﬀerence is that instead of extending every edge to a copy of F, we will consider an F-decomposition of the multigraph shifter and then extend every copy of F in this decomposition to a copy of F∗ (and then delete the original multigraph).

For a word w = w1 ... wk ∈ {0,1}k, let |w|0 denote the number of 0’s in w and let |w|1 denote the number of 1’s in w. Let We(k) be the set of words w ∈ {0,1}k with |w|1 being even, and let Wo(k) be the set of words w ∈ {0,1}k with |w|1 being odd.

Fact 9.3. For every k ≥ 1, |We(k)| = |Wo(k)| = 2k−1.

- Lemma 9.4. Let 1 ≤ k < r and let F,F∗ be r-graphs such that F∗ is F-decomposable. Let


x01,... ,x0k,x11,... ,x1k be distinct vertices. There exists a multi-r-graph Tk∗ which satisﬁes (SH1)– (SH3), except that F does not need to be 1-well separated.

Proof. Let Sk := V (kF) . For every S∗ ∈ Sk, we will construct a multi-r-graph Tk,S∗ such that x01,... ,x0k,x11,... ,x1k ∈ V (Tk,S∗) and

- (sh1) Tk,S∗ has an F-decomposition F such that for all F′ ∈ F and all i ∈ [k], |V (F′) ∩ {x0i ,x1i }| ≤ 1;
- (sh2) |Tk,S∗(S)| ≡ 0 mod Deg(F∗)|S| for all S ⊆ V (Tk,S∗) with |S| < k;
- (sh3) for all S ∈ V (Tkk,S∗) ,


(−1) i∈[k] zi|F(S∗)| mod Deg(F∗)k if S = {xzii : i ∈ [k]}, 0 mod Deg(F∗)k otherwise.

|Tk,S∗(S)| ≡

Following from this, it easy to construct Tk∗ by overlaying the above multi-r-graphs Tk,S∗. Indeed, there are integers (a′S∗)S∗∈Sk such that S∗∈Sk a′S∗|F(S∗)| = Deg(F)k. Hence, there are positive integers (aS∗)S∗∈Sk such that

- (9.1) aS∗|F(S∗)| ≡ Deg(F)k mod Deg(F∗)k.

Therefore, we take Tk∗ to be the union of aS∗ copies of Tk,S∗ for each S∗ ∈ Sk. Then Tk∗ has the desired properties.

Let S∗ ∈ Sk. It remains to construct Tk,S∗. Let X0 := {x01,... ,x0k} and X1 := {x11,... ,x1k}. We may assume that V (F∗)∩(X0∪X1) = ∅. Let F∗ be an F-decomposition of F∗ and F′ ∈ F∗. Let X = {x1,... ,xk} ⊆ V (F′) be the k-set which plays the role of S∗ in F′, in particular |F′(X)| = |F(S∗)|. We ﬁrst deﬁne an auxiliary r-graph T1,xk as follows: Let F′′ be obtained from F′ by replacing xk with a new vertex xˆk. Then let

T1,xk := (F∗ − F′) ∪· F′′.

Clearly, (F∗ \{F′})∪{F′′} is an F-decomposition of T1,xk. Moreover, observe that for every set S ⊆ V (T1,xk) with |S| < r, we have

|T1,xk(S)| =

 



0 if {xk,xˆk} ⊆ S; |F∗(S)| if {xk,xˆk} ∩ S = ∅; |F∗(S)| − |F′(S)| if xk ∈ S,xˆk ∈/ S; |F′′(S)| = |F′((S \ {xˆk}) ∪ {xk})| if xk ∈/ S,xˆk ∈ S.

- (9.2)


S∗∈Sk

We now overlay copies of T1,xk in a suitable way in order to obtain the multi-r-graph Tk,S∗. The vertex set of Tk,S∗ will be

V (Tk,S∗) = (V (F∗) \ X) ∪· X0 ∪· X1. For every word w = w1 ... wk−1 ∈ {0,1}k−1, let Tw be a copy of T1,xk, where

- (a) for each i ∈ [k − 1], xwi i plays the role of xi (and x1i−wi ∈/ V (Tw));
- (b) if |w|1 is odd, then x0k plays the role of xk and x1k plays the role of xˆk, whereas if |w|1 is even, then x0k plays the role of xˆk and x1k plays the role of xk;
- (c) the vertices in V (T1,xk) \ {x1,... ,xk−1,xk,xˆk} keep their role.


Let

Tk,S∗ :=

Tw.

w∈{0,1}k−1

(Note that if k = 1, then Tk,S∗ is just a copy of T1,xk, where x01 plays the role of xˆ1 and x11 plays the role of x1.) We claim that Tk,S∗ satisﬁes (sh1)–(sh3). Clearly, (sh1) is satisﬁed because each

Tw is a copy of T1,xk which is F-decomposable, and for all w ∈ {0,1}k−1 and all i ∈ [k − 1], |V (Tw) ∩ {x0i ,x1i }| = 1, and since xk ∈/ V (F′′).

We will now use (9.2) in order to determine an expression for |Tk,S∗(S)| (see (9.3)) which will imply (sh2) and (sh3). Call S ⊆ V (Tk,S∗) degenerate if {x0i ,x1i } ⊆ S for some i ∈ [k]. Clearly, if S is degenerate, then |Tw(S)| = 0 for all w ∈ {0,1}k−1. If S ⊆ V (Tk,S∗) is non-degenerate, deﬁne I(S) as the set of all indices i ∈ [k] such that |S∩{x0i ,x1i }| = 1, and deﬁne the ‘projection’ π(S) := (S \ (X0 ∪ X1)) ∪ {xi : i ∈ I(S)}.

Clearly, π(S) ⊆ V (F∗) and |π(S)| = |S|. Note that if S ⊆ V (Tw) and k ∈/ I(S), then S plays the role of π(S) ⊆ V (T1,xk) in Tw by (a). For i ∈ I(S), let zi(S) ∈ {0,1} be such that S ∩ {x0i,x1i } = {xizi(S)}, and let z(S) := i∈I(S) zi(S). We claim that the following holds:

 

(−1)z(S)|F′(π(S))| mod Deg(F∗)|S| if S is non-degenerate

|Tk,S∗(S)| ≡

- (9.3)


and |I(S)| = k; 0 mod Deg(F∗)|S| otherwise.



As seen above, if S is degenerate, then we have |Tk,S∗(S)| = 0. From now on, we assume that S is non-degenerate. Let W(S) be the set of words w = w1 ... wk−1 ∈ {0,1}k−1 such that wi = zi(S) for all i ∈ I(S) \ {k}. Clearly, if w ∈ {0,1}k−1 \ W(S), then |Tw(S)| = 0 by (a). Suppose that w ∈ W(S). If k ∈/ I(S), then S plays the role of π(S) in Tw and hence we have |Tw(S)| = |T1,xk(π(S))| = |F∗(π(S))| by (9.2). It follows that |Tk,S∗(S)| ≡ 0 mod Deg(F∗)|S|, as required.

From now on, suppose that k ∈ I(S). Let We(S) := {w ∈ W(S) : |w|1 + zk(S) is even}; Wo(S) := {w ∈ W(S) : |w|1 + zk(S) is odd}.

- By (b), we know that xzkk(S) plays the role of xk in Tw if w ∈ Wo(S) and the role of xˆk if


- w ∈ We(S). Hence, if w ∈ Wo(S) then S plays the role of π(S) in Tw, and if w ∈ We(S), then S plays the role of (π(S) \ {xk}) ∪ {xˆk} in Tw. Thus, we have


 

|T1,xk(π(S))| (9.2=) |F∗(π(S))| − |F′(π(S))| if w ∈ Wo(S); |T1,xk((π(S) \ {xk}) ∪ {xˆk})| (9.2=) |F′(π(S))| if w ∈ We(S); 0 if w ∈/ W(S).

|Tw(S)| =



It follows that |Tk,S∗(S)| =

|Tw(S)| ≡ (|We(S)| − |Wo(S)|)|F′(π(S))| mod Deg(F∗)|S|.

w∈{0,1}k−1

Observe that

|We(S)| = |{w′ ∈ {0,1}k−|I(S)| : |w′|1 + z(S) is even}|; |Wo(S)| = |{w′ ∈ {0,1}k−|I(S)| : |w′|1 + z(S) is odd}|.

Hence, if |I(S)| < k, then by Fact 9.3 we have |We(S)| = |Wo(S)| = 2k−|I(S)|−1. If |I(S)| = k, then |We(S)| = 1 if z(S) is even and |We(S)| = 0 if z(S) is odd, and for Wo(S), the reverse holds. Altogether, this implies (9.3).

It remains to show that (9.3) implies (sh2) and (sh3). Clearly, (sh2) holds. Indeed, if |S| < k, then S is degenerate or we have |I(S)| < k, and (9.3) implies that |Tk,S∗(S)| ≡ 0 mod Deg(F∗)|S|.

Finally, consider S ∈ V (Tkk,S∗) . If S does not have the form {xzii : i ∈ [k]} for suitable z1,... ,zk ∈ {0,1}, then S is degenerate or |I(S)| < k and (9.3) implies that |Tk,S∗(S)| ≡ 0 mod Deg(F∗)k, as required. Assume now that S = {xzii : i ∈ [k]} for suitable z1,... ,zk ∈ {0,1}. Then S is not degenerate, I(S) = [k], z(S) = i∈[k] zi and π(S) = {x1,... ,xk} = X, in which case (9.3) implies that

|Tk,S∗(S)| ≡ (−1)z(S)|F′(X)| = (−1)z(S)|F(S∗)| mod Deg(F∗)k, as required for (sh3).

Proof of Lemma 9.2. By applying Lemma 9.4 (with x0k and x1k swapping their roles), we can see that there exists a multi-r-graph Tk∗ with x01,... ,x0k,x11,... ,x1k ∈ V (Tk∗) such that the following properties hold:

- • Tk∗ has an F-decomposition {F1,... ,Fm} such that for all j ∈ [m] and all i ∈ [k], we have |V (Fj) ∩ {x0i ,x1i }| ≤ 1;
- • |Tk∗(S)| ≡ 0 mod Deg(F∗)|S| for all S ⊆ V (Tk∗) with |S| < k;
- • for all S ∈ V (T


∗ k ) k ,

|Tk∗(S)| ≡

(−1) i∈[k−1] zi+(1−zk)Deg(F)k mod Deg(F∗)k if S = {xzii : i ∈ [k]}, 0 mod Deg(F∗)k otherwise.

Let f := |V (F)|. For every j ∈ [m], let Zj be a set of f∗−f new vertices, such that Zj∩Zj′ = ∅ for all distinct j,j′ ∈ [m] and Zj ∩V (Tk∗) = ∅ for all j ∈ [m]. Now, for every j ∈ [m], let Fj∗ be a copy of F∗ on vertex set V (Fj) ∪ Zj such that Fj ∪ {Fj} is a 1-well separated F-decomposition of Fj∗. In particular, we have that

- (a) (Fj∗ − Fj)[V (Fj)] is empty;
- (b) Fj is a 1-well separated F-decomposition of Fj∗ − Fj such that for all F′ ∈ Fj, |V (F′) ∩ V (Fj)| ≤ r − 1.


Let

˙

(Fj∗ − Fj).

Tk :=

j∈[m]

We claim that Tk is the desired shifter. First, observe that Tk is a (simple) r-graph since (Fj∗ −Fj)[V (Fj)] is empty for every j ∈ [m] by (a). Moreover, since F1,... ,Fm are r-disjoint by (b), Fact 4.3(iii) implies that F := F1∪···∪Fm is a 1-well separated F-decomposition of Tk, and for each j ∈ [m], all F′ ∈ Fj and all i ∈ [k], we have |V (F′) ∩ {x0i ,x1i }| ≤ |V (Fj) ∩ {x0i ,x1i}| ≤ 1. Thus, (SH1) holds.

Moreover, note that for every j ∈ [m], we have |(Fj∗ − Fj)(S)| ≡ −|Fj(S)| mod Deg(F∗)|S| for all S ⊆ V (Tk) with |S| ≤ r − 1. Thus,

−|Fj(S)| = −|Tk∗(S)| mod Deg(F∗)|S|

|Tk(S)| ≡

j∈[m]

for all S ⊆ V (Tk) with |S| ≤ r − 1. Hence, (SH2) clearly holds. If S = {xzii : i ∈ [k]} for suitable z1,... ,zk ∈ {0,1}, then

|Tk(S)| ≡ −|Tk∗(S)| ≡ (−1) i∈[k]ziDeg(F)k mod Deg(F∗)k and (SH3) holds. Thus, Tk is indeed an (x01,... ,x0k,x11,... ,x1k)-shifter with respect to F,F∗.

Finally, to see that Tk has degeneracy at most fr∗−−11 rooted at X, consider the vertices of V (Tk) \ X in an ordering where the vertices of V (T∗

k ) \ X precede all the vertices in sets Zj, for j ∈ [m]. Note that Tk[V (Tk∗)] is empty by (a), i.e. a vertex in V (Tk∗) \ X has no ‘backward’ edges. Moreover, if z ∈ Zj for some j ∈ [m], then |Tk({z})| = |Fj∗({z})| ≤ fr∗−−11 .

- 9.2. Shifting procedure. In the previous section, we constructed degree shifters which allow us to locally change the degrees of k-sets in some host graph. We will now show how to combine these local shifts in order to transform any given F-divisible r-graph G into an F∗-divisible r-graph. It turns out to be more convenient to consider the shifting for ‘r-set functions’ rather than r-graphs. We will then recover the graph theoretical statement by considering a graph as an indicator set function (see below).


Let φ : Vr → Z. (Think of φ as the multiplicity function of a multi-r-graph.) We extend φ to φ : k∈[r]

V k → Z by deﬁning for all S ⊆ V with |S| = k ≤ r,

0

- (9.4) φ(S′).

Thus for all 0 ≤ i ≤ k ≤ r and all S ∈ Vi ,

r − i k − i

φ(S) =

S′∈(Vk):S⊆S′

- (9.5) φ(S′).


φ(S) :=

S′∈(Vr):S⊆S′

For k ∈ [r − 1]0 and b0,... ,bk ∈ N, we say that φ is (b0,... ,bk)-divisible if b|S| | φ(S) for all S ⊆ V with |S| ≤ k.

If G is an r-graph with V (G) ⊆ V , we deﬁne 1G: Vr → Z as

1 if S ∈ G; 0 if S ∈/ G.

1G(S) :=

and extend 1G as in (9.4). Hence, for a set S ⊆ V with |S| < r, we have 1G(S) = |G(S)|. Thus,

- (9.5) corresponds to the handshaking lemma for r-graphs (cf. (4.1)). Clearly, if G and G′ are edge-disjoint, then we have 1G + 1G′ = 1G∪G′. Moreover, for an r-graph F, G is F-divisible if and only if 1G is (Deg(F)0,... ,Deg(F)r−1)-divisible.

As mentioned before, our strategy is to successively ﬁx the degrees of k-sets until we have ﬁxed the degrees of all k-sets except possibly the degrees of those k-sets contained in some ﬁnal vertex set K which is too small as to continue with the shifting. However, as the following lemma shows, divisibility is then automatically satisﬁed for all the k-sets lying inside K. For this to work it is essential that the degrees of all i-sets for i < k are already ﬁxed.

Lemma 9.5. Let 1 ≤ k < r and b0,... ,bk ∈ N be such that k r−−ii bi ≡ 0 mod bk for all i ∈ [k]0. Let φ : Vr → Z be a (b0,... ,bk−1)-divisible function. Suppose that there exists a subset K ⊆ V of size 2k − 1 such that if S ∈ Vk with φ(S)  ≡ 0 mod bk, then S ⊆ K. Then φ is (b0,... ,bk)divisible. Proof. Let K be the set of all subsets T′′ of K of size less than k. We ﬁrst claim that for all T′′ ∈ K, we have

T′∈(Kk): T′′⊆T′

- (9.6) φ(T′) ≡ 0 mod bk.

Indeed, suppose that |T′′| = i < k, then we have

T′∈(Kk): T′′⊆T′

φ(T′) ≡

T′∈(Vk): T′′⊆T′

φ(T′) (9.5=)

r − i k − i

φ(T′′) mod bk.

Since φ is (b0,... ,bk−1)-divisible, we have φ(T′′) ≡ 0 mod bi, and since k r−−ii bi ≡ 0 mod bk, the claim follows.

- Let T ∈ Kk . We need to show that φ(T) ≡ 0 mod bk. To this end, deﬁne the function


f : K → Z as

f(T′′) :=

(−1)|T′′| if T′′ ⊆ K \ T; 0 otherwise.

We claim that for all T′ ∈ Kk , we have

T′′ T′

f(T′′) =

1 if T′ = T; 0 otherwise.

- (9.7)


Indeed, let T′ ∈ Kk , and set t := |T′ \ T|. We then check that (using |K| < 2k in the ﬁrst equality)

t

t j

1 if t = 0; 0 if t > 0.

(−1)|T′′| =

(−1)j

f(T′′) =

=

T′′ T′

j=0

T′′⊆(K\T)∩T′

We can now conclude that

  

  

(9.6≡) 0 mod bk,

φ(T) (9.7=)

φ(T′)

f(T′′) =

f(T′′)

φ(T′)

T′′ T′

T′′∈K

T′∈(Kk)

T′∈(Kk): T′′⊆T′

as desired.

We now deﬁne a more abstract version of degree shifters, which we call adapters. They represent the eﬀect of shifters and will ﬁnally be replaced by shifters again.

Deﬁnition 9.6 (x-adapter). Let V be a vertex set and k,r,b0,... ,bk,hk ∈ N be such that k < r and hk | bk. For distinct vertices x01,... ,x0k,x11,... ,x1k in V , we say that τ : Vr → Z is an (x01,... ,x0k,x11,... ,x1k)-adapter with respect to (b0,... ,bk;hk) if τ is (b0,... ,bk−1)-divisible and for all S ∈ Vk ,

(−1) i∈[k] zihk mod bk if S = {xzii : i ∈ [k]}, 0 mod bk otherwise.

τ(S) ≡

Note that such an adapter τ is (b0,... ,bk−1,hk)-divisible.

Fact 9.7. If T is an x-shifter with respect to F,F∗, then 1T is an x-adapter with respect to (Deg(F∗)0,... ,Deg(F∗)k;Deg(F)k).

The following deﬁnition is crucial for the shifting procedure. Given some function φ, we intend to add adapters in order to obtain a divisible function. Every adapter is characterised by a tuple

- x consisting of 2k distinct vertices, which tells us where to apply the adapter. All these tuples are contained within a multiset Ω, which we call a balancer. Ω is capable of dealing with any input function φ in the sense that there is a multisubset of Ω which tells us where to apply the adapters in order to make φ divisible. Moreover, as we ﬁnally want to replace the adapters by shifters (and thus embed them into some host graph), there must not be too many of them.


Deﬁnition 9.8 (balancer). Let r,k,b0,... ,bk ∈ N with k < r and let U,V be sets with U ⊆ V . Let Ωk be a multiset containing ordered tuples x = (x1,... ,x2k), where x1,... ,x2k ∈ U are distinct. We say that Ωk is a (b0,... ,bk)-balancer for V with uniformity r acting on U if for any hk ∈ N with hk | bk, the following holds: let φ: Vr → Z be any (b0,... ,bk−1,hk)-divisible function such that S ⊆ U whenever S ∈ Vk and φ(S)  ≡ 0 mod bk. There exists a multisubset Ω′ of Ωk such that φ+τΩ′ is (b0,... ,bk)-divisible, where τΩ′ := x∈Ω′ τx and τx is any x-adapter with respect to (b0,... ,bk;hk).

For a set S ∈ Vk , let degΩ

(S) be the number of x = (x1,... ,x2k) ∈ Ωk such that |S ∩ {xi,xi+k}| = 1 for all i ∈ [k]. Furthermore, we denote ∆(Ωk) to be the maximum value of degΩ

k

(S) over all S ∈ Vk .

k

The following lemma shows that these balancers exist, i.e. that the local shifts performed by the degree shifters guaranteed by Lemma 9.2 are suﬃcient to obtain global divisibility (for which we apply Lemma 9.5).

Lemma 9.9. Let 1 ≤ k < r. Let b0,... ,bk ∈ N be such that k r−−ss bs ≡ 0 mod bk for all s ∈ [k]0.

- Let U be a set of n ≥ 2k vertices and U ⊆ V . Then there exists a (b0,... ,bk)-balancer Ωk for V with uniformity r acting on U such that ∆(Ωk) ≤ 2k(k!)2bk. Proof. We will proceed by induction on k. First, consider the case when k = 1. Write


- U = {v1,... ,vn}. Deﬁne Ω1 to be the multiset containing precisely b1 − 1 copies of (vj,vj+1) for all j ∈ [n − 1]. Note that ∆(Ω1) ≤ 2b1.


We now show that Ω1 is a (b0,b1)-balancer for V with uniformity r acting on U. Let φ :

- V r → Z be (b0,h1)-divisible for some h1 ∈ N with h1 | b1, such that v ∈ U whenever v ∈ V


and φ({v})  ≡ 0 mod b1. Let m0 := 0. For each j ∈ [n − 1], let 0 ≤ mj < b1 be such that (mj−1 − mj)h1 ≡ φ({vj}) mod b1. Let Ω′ ⊆ Ω1 consist of precisely mj copies of (vj,vj+1) for all j ∈ [n − 1]. Let τ := x∈Ω′ τx, where τx is an x-adapter with respect to (b0,b1;h1), and let φ′ := φ + τ. Clearly, φ′ is (b0)-divisible. Note that, for all j ∈ [n − 1],

τ({vj}) ≡ mj−1τ(vj−1,vj)({vj}) + mjτ(vj,vj+1)({vj}) mod b1

- (9.8) ≡ (−mj−1 + mj)h1 ≡ −φ({vj}) mod b1,

implying that φ′({vj}) ≡ 0 mod b1 for all j ∈ [n − 1]. Moreover, for all v ∈ V \ U, we have φ({v}) ≡ 0 mod b1 by assumption and τ({v}) ≡ 0 mod b1 since no element of Ω1 contains v. Thus, by Lemma 9.5 (with {vn} playing the role of K), φ′ is (b0,b1)-divisible, as required.

We now assume that k > 1 and that the statement holds for smaller k. Again, write U = {v1,... ,vn}. For every ℓ ∈ [n], let Uℓ := {vj : j ∈ [ℓ]}. We construct Ωk inductively. For each ℓ ∈ {2k,... ,n}, we deﬁne a multiset Ωk,ℓ as follows. Let Ωk−1,ℓ−1 be a (b1,... ,bk)-balancer for

- V \ {vℓ} with uniformity r − 1 acting on Uℓ−1 and ∆(Ωk−1,ℓ−1) ≤ 2k−1(k − 1)!2bk.


(Indeed, Ωk−1,ℓ−1 exists by our induction hypothesis with r − 1,k − 1,b1,... ,bk,Uℓ−1,V \ {vℓ} playing the roles of r,k,b0,... ,bk,U,V .) For each v = (vj1,... ,vj2k−2) ∈ Ωk−1,ℓ−1, let

- (9.9) v′ := (vℓ,vj1,... ,vjk−1,vjv,vjk,... ,vj2k−2) ∈ Uℓ × Uℓ2−k1−1,


such that jv ∈ {ℓ − 2k + 1,... ,ℓ} \ {ℓ,j1,... ,j2k−2} (which exists since ℓ ≥ 2k). We let Ωk,ℓ := {v′ : v ∈ Ωk−1,ℓ−1}. Now, deﬁne

n

Ωk,ℓ.

Ωk :=

ℓ=2k

Claim 1: ∆(Ωk) ≤ 2k(k!)2bk Proof of claim: Consider any S ∈ Vk . Clearly, if S  ⊆ U, then degΩ

(S) = 0, so assume that S ⊆ U. Let i0 be the largest i ∈ [n] such that vi ∈ S.

k

First note that for all ℓ ∈ {2k,... ,n}, we have degΩ

(S \ {v}) ≤ k∆(Ωk−1,ℓ−1).

(S) ≤

degΩ

k−1,ℓ−1

k,ℓ

v∈S

On the other hand, we claim that if ℓ < i0 or ℓ ≥ i0 + 2k, then degΩ

(S) = 0. Indeed, in the ﬁrst case, we have S  ⊆ Uℓ which clearly implies that degΩ

k,ℓ

(S) = 0. In the latter case, for any v ∈ Ωk−1,ℓ−1, we have jv ≥ ℓ − 2k + 1 > i0 and thus |S ∩ {vℓ,vjv}| = 0, which also implies degΩk,ℓ(S) = 0. Therefore,

k,ℓ

n

(S) ≤ 2k2∆(Ωk−1,ℓ−1) ≤ 2k(k!)2bk,

degΩ

(S) =

degΩ

k,ℓ

k

ℓ=2k

as required. −

We now show that Ωk is indeed a (b0,... ,bk)-balancer on V with uniformity r acting on U. The key to this is the following claim, which we will apply repeatedly.

Claim 2: Let 2k ≤ ℓ ≤ n. Let φℓ: Vr → Z be any (b0,... ,bk−1,hk)-divisible function for some hk ∈ N with hk | bk. Suppose that if φℓ(S)  ≡ 0 mod bk for some S ∈ Vk , then S ⊆ Uℓ. Then there exists Ω′k,ℓ ⊆ Ωk,ℓ such that φℓ−1 := φℓ + τΩ′

is (b0,... ,bk−1,hk)-divisible and if φℓ−1(S)  ≡ 0 mod bk for some S ∈ Vk , then S ⊆ Uℓ−1.

k,ℓ

:= v′∈Ω′k,ℓ τv′ and τv′ is an arbitrary v′-adapter

is as in Deﬁnition 9.8, i.e. τΩ′

(Here, τΩ′

k,ℓ

k,ℓ

with respect to (b0,... ,bk;hk).) Proof of claim: Deﬁne ρ : Vr\{−v1ℓ} → Z such that for all S ∈ Vr\{−v1ℓ} ,

ρ(S) := φℓ(S ∪ {vℓ}).

It is easy to check that this identity transfers to smaller sets S, that is, for all S ⊆ V \{vℓ}, with |S| ≤ r − 1, we have ρ(S) = φℓ(S ∪ {vℓ}), where ρ(S) and φℓ(S ∪ {vℓ}) are as deﬁned in (9.4).

Hence, since φℓ is (b0,... ,bk−1,hk)-divisible, ρ is (b1,... ,bk−1,hk)-divisible. Moreover, for all S ∈ Vk\{−v1ℓ} with ρ(S)  ≡ 0 mod bk, we have S ⊆ Uℓ−1.

Recall that Ωk−1,ℓ−1 is a (b1,... ,bk)-balancer for V \ {vℓ} with uniformity r − 1 acting on Uℓ−1. Thus, there exists a multiset Ω′ ⊆ Ωk−1,ℓ−1 such that

- (9.10) ρ + τΩ′ is (b1,... ,bk)-divisible.


Let Ω′k,ℓ ⊆ Ωk,ℓ be induced by Ω′, that is, Ω′k,ℓ := {v′ : v ∈ Ω′} (see (9.9)). Let v′ ∈ Ω′k,ℓ and let τv′ be any v′-adapter with respect to (b0,... ,bk;hk). As noted after Deﬁnition 9.6, τv′ is (b0,... ,bk−1,hk)-divisible. Crucially, if S ∈ Vk and vℓ ∈ S, then τv′(S) ≡ τv(S \ {vℓ}) mod bk. Indeed, let x01,... ,x0k−1,x11,... ,x1k−1 be such that v = (x01,... ,x0k−1,x11,... ,x1k−1) and thus v′ = (vℓ,x01,... ,x0k−1,vjv,x11,... ,x1k−1). Then by Deﬁnition 9.6, as vℓ ∈ S, we have

(−1)0+ i∈[k−1] zihk mod bk if S \ {vℓ} = {xzii : i ∈ [k − 1]}, 0 mod bk otherwise,

τv′(S) ≡

≡ τv(S \ {vℓ}) mod bk. Let τΩ′

. Note that for all S  ⊆ Uℓ, we have τΩ′

(S) = 0 by (9.9). Moreover, if S ∈ Vk and vℓ ∈ S, then τΩ′

:= v′∈Ω′k,ℓ τv′ and φℓ−1 := φℓ+τΩ′

k,ℓ

k,ℓ

k,ℓ

(S) ≡ τΩ′(S \ {vℓ}) mod bk by the above.

k,ℓ

Clearly, φℓ−1 is (b0,... ,bk−1,hk)-divisible. Now, consider any S ∈ Vk with S  ⊆ Uℓ−1. If S  ⊆ Uℓ, then

(S) ≡ 0 + 0 ≡ 0 mod bk. If S ⊆ Uℓ, then since S  ⊆ Uℓ−1 we must have vℓ ∈ S, and so

φℓ−1(S) = φℓ(S) + τΩ′

k,ℓ

(S) ≡ ρ(S \ {vℓ}) + τΩ′(S \ {vℓ}) (9.10≡ ) 0 mod bk. This completes the proof of the claim. −

φℓ−1(S) = φℓ(S) + τΩ′

k,ℓ

Now, let hk ∈ N with hk | bk and let φ: Vr → Z be any (b0,... ,bk−1,hk)-divisible function such that S ⊆ U whenever S ∈ Vk and φ(S)  ≡ 0 mod bk. Let φn := φ and note that U = Un. Thus, by Claim 2, there exists Ω′k,n ⊆ Ωk,n such that φn−1 := φn + τΩ′

is (b0,... ,bk−1,hk)-

k,n

divisible and if φn−1(S)  ≡ 0 mod bk for some S ∈ Vk , then S ⊆ Un−1. Repeating this step ﬁnally yields some Ω′k ⊆ Ωk such that φ∗ := φ + τΩ′

is (b0,... ,bk−1,hk)-divisible and such that

k

S ⊆ U2k−1 whenever S ∈ Vk and φ(S)  ≡ 0 mod bk. By Lemma 9.5 (with U2k−1 playing the role of K), φ∗ is then (b0,... ,bk)-divisible. Thus Ωk is indeed a (b0,... ,bk)-balancer.

- 9.3. Proof of Lemma 8.4. We now prove Lemma 8.4. For this, we consider the balancers Ωk guaranteed by Lemma 9.9. Recall that these consist of suitable adapters, and that Lemma 9.2 guarantees the existence of shifters corresponding to these adapters. It remains to embed these shifters in a suitable way, which is achieved via Lemma 4.7. The following fact will help us to verify the conditions of Lemma 9.9.


Fact 9.10. Let F be an r-graph. Then for all 0 ≤ i ≤ k < r, we have k r−−ii Deg(F)i ≡ 0 mod Deg(F)k.

Proof. Let S be any i-set in V (F). By (4.1), we have that r − i k − i |F(S)| =

|F(T)| ≡ 0 mod Deg(F)k,

T∈(V(kF)): S⊆T

and this implies the claim.

Proof of Lemma 8.4. Let x01,... ,x0r−1,x11,... ,x1r−1 be distinct vertices (not in V (G)). For k ∈ [r − 1], let Xk := {x01,... ,x0k,x11,... ,x1k}. By Lemma 9.2, for every k ∈ [r − 1], there exists an (x01,... ,x0k,x11,... ,x1k)-shifter Tk with respect to F,F∗ such that Tk[Xk] is empty and Tk has degeneracy at most fr∗−−11 rooted at Xk. Note that (SH1) implies that

- (9.11) |Tk({x0i ,x1i})| = 0 for all i ∈ [k].


We may assume that there exists t ≥ maxk∈[r−1] |V (Tk)| such that 1/n ≪ γ ≪ 1/t ≪ ξ,1/f∗. Let Deg(F) = (h0,h1,... ,hr−1) and let Deg(F∗) = (b0,b1,... ,br−1). Since F∗ is F-decomposable and thus F-divisible, we have hk | bk for all k ∈ [r − 1]0.

By Fact 9.10, we have k r−−ii bi ≡ 0 mod bk for all 0 ≤ i ≤ k < r. For each k ∈ [r − 1] with hk < bk, we apply Lemma 9.9 to obtain a (b0,... ,bk)-balancer Ωk for V (G) with uniformity r acting on V (G) such that ∆(Ωk) ≤ 2k(k!)2bk. For values of k for which we have hk = bk, we let Ωk := ∅. For every k ∈ [r − 1] and every v = (v1,... ,v2k) ∈ Ωk, deﬁne the labelling Λv: Xk → V (G) by setting Λv(x0i ) := vi and Λv(x1i ) := vi+k for all i ∈ [k].

For technical reasons, let T0 be a copy of F and let X0 := ∅. Let Ω0 be the multiset containing b0/h0 copies of ∅, and for every v ∈ Ω0, let Λv : X0 → V (G) be the trivial G-labelling of (T0,X0). Note that T0 has degeneracy at most fr∗−−11 rooted at X0. Note also that Λv does not root any set S ⊆ V (G) with |S| ∈ [r − 1].

We will apply Lemma 4.7 in order to ﬁnd faithful embeddings of the Tk into G. Let Ω := r−1 k=0 Ωk. Let α := γ−2/n.

Claim 1: For every k ∈ [r − 1] and every S ⊆ V (G) with |S| ∈ [r − 1], we have |{v ∈ Ωk : Λv roots S}| ≤ r−1αγnr−|S|. Moreover, |Ωk| ≤ r−1αγnr.

Proof of claim: Let k ∈ [r−1] and S ⊆ V (G) with |S| ∈ [r−1]. Consider any v = (v1,... ,v2k) ∈ Ωk and suppose that Λv roots S, i.e. S ⊆ {v1,... ,v2k} and |Tk(Λ−v1(S))| > 0. Note that if we had {x0i ,x1i } ⊆ Λ−v1(S) for some i ∈ [k] then |Tk(Λ−v1(S))| = 0 by (9.11), a contradiction. We deduce that |S ∩ {vi,vi+k}| ≤ 1 for all i ∈ [k], in particular |S| ≤ k. Thus there exists S′ ⊇ S with |S′| = k and such that |S′ ∩ {vi,vi+k}| = 1 for all i ∈ [k]. However, there are at most nk−|S| sets S′ with |S′| = k and S′ ⊇ S, and for each such S′, the number of v = (v1,... ,v2k) ∈ Ωk with |S′ ∩ {vi,vi+k}| = 1 for all i ∈ [k] is at most ∆(Ωk). Thus, |{v ∈ Ωk : Λv roots S}| ≤ nk−|S|∆(Ωk) ≤ nr−1−|S|2k(k!)2bk ≤ r−1αγnr−|S|. Similarly, we have |Ωk| ≤ nk∆(Ωk) ≤ r−1αγnr. −

Claim 1 implies that for every S ⊆ V (G) with |S| ∈ [r − 1], we have |{v ∈ Ω : Λv roots S}| ≤ αγnr−|S| − 1,

and we have |Ω| ≤ b0/h0 + k r−=11 |Ωk| ≤ αγnr. Therefore, by Lemma 4.7, for every k ∈ [r − 1]0 and every v ∈ Ωk, there exists a Λv-faithful embedding φv of (Tk,Xk) into G, such that, letting Tv := φv(Tk), the following hold:

- (a) for all distinct v1,v2 ∈ Ω, the hulls of (Tv1,Im(Λv1)) and (Tv2,Im(Λv2)) are edgedisjoint;
- (b) for all v ∈ Ω and e ∈ O with e ⊆ V (Tv), we have e ⊆ Im(Λv);
- (c) ∆( v∈Ω Tv) ≤ αγ(2−r)n.


Note that by (a), all the graphs Tv are edge-disjoint. Let D :=

Tv.

v∈Ω

- By (c), we have ∆(D) ≤ γ−2. We will now show that D is as desired. For every k ∈ [r − 1] and v ∈ Ωk, we have that Tv is a v-shifter with respect to F,F∗ by


deﬁnition of Λv and since φv is Λv-faithful. Thus, by Fact 9.7,

- (9.12) 1Tv is a v-adapter with respect to (b0,... ,bk;hk).


Claim 2: For every Ω′ ⊆ Ω, v∈Ω′ Tv has a 1-well separated F-decomposition F such that F≤(r+1) and O are edge-disjoint.

Proof of claim: Clearly, for every v ∈ Ω0, Tv is a copy of F and thus has a 1-well separated F-decomposition Fv = {Tv}. Moreover, for each k ∈ [r − 1] and all v = (v1,... ,v2k) ∈ Ωk, Tv has a 1-well separated F-decomposition Fv by (SH1) such that for all F′ ∈ Fv and all i ∈ [k], |V (F′) ∩ {vi,vi+k}| ≤ 1.

In order to prove the claim, it is thus suﬃcient to show that for all distinct v1,v2 ∈ Ω, Fv1 and Fv2 are r-disjoint (implying that F := v∈Ω′ Fv is 1-well separated by Fact 4.3(iii)) and that for every v ∈ Ω, Fv≤(r+1) and O are edge-disjoint.

To this end, we ﬁrst show that for every v ∈ Ω and F′ ∈ Fv, we have that |V (F′)∩Im(Λv)| < r and every e ∈ V (rF′) belongs to the hull of (Tv,Im(Λv)). If v ∈ Ω0, this is clear since Im(Λv) = ∅ and F′ = Tv, so suppose that v = (v1,... ,v2k) ∈ Ωk for some k ∈ [r − 1]. (In particular, hk < bk.) By the above, we have |V (F′) ∩ {vi,vi+k}| ≤ 1 for all i ∈ [k]. In particular, |V (F′) ∩ Im(Λv)| ≤ k < r, as desired. Moreover, suppose that e ∈ V (rF′) . If e ∩ Im(Λv) = ∅, then e belongs to the hull of (Tv,Im(Λv)), so suppose further that S := e∩Im(Λv) is not empty. Clearly, |S ∩ {vi,vi+k}| ≤ |V (F′) ∩ {vi,vi+k}| ≤ 1 for all i ∈ [k]. Thus, there exists S′ ⊇ S with |S′| = k and |S′ ∩ {vi,vi+k}| = 1 for all i ∈ [k]. By (SH3) (and since hk < bk), we have that |Tv(S′)| > 0, which clearly implies that |Tv(S)| > 0. Thus, e ∩ Im(Λv) = S is a root of (Tv,Im(Λv)) and therefore e belongs to the hull of (Tv,Im(Λv)).

Now, consider distinct v1,v2 ∈ Ω and suppose, for a contradiction, that there is e ∈ V (rG) such that e ⊆ V (F′) ∩ V (F′′) for some F′ ∈ Fv1 and F′′ ∈ Fv2. But by the above, e belongs to the hulls of both (Tv1,Im(Λv1)) and (Tv2,Im(Λv2)), a contradiction to (a).

Finally, consider v ∈ Ω and e ∈ O. We claim that e ∈/ Fv≤(r+1). Let F′ ∈ Fv and suppose, for a contradiction, that e ⊆ V (F′). By (b), we have e ⊆ Im(Λv). On the other hand, by the above, we have |V (F′) ∩ Im(Λv)| < r, a contradiction. −

Clearly, D is F-divisible by Claim 2. We will now show that for every F-divisible r-graph H on V (G) which is edge-disjoint from D, there exists a subgraph D∗ ⊆ D such that H ∪ D∗ is F∗-divisible and D − D∗ has a 1-well separated F-decomposition F such that F≤(r+1) and O are edge-disjoint.

Let H be any F-divisible r-graph on V (G) which is edge-disjoint from D. We will inductively prove that the following holds for all k ∈ [r − 1]0:

is (b0,... ,bk)-divisible, where Dk∗ := v∈Ω∗k Tv.

SHIFTk there exists Ω∗k ⊆ Ω0 ∪ ··· ∪ Ωk such that 1H∪D∗

k

We ﬁrst establish SHIFT0. Since H is F-divisible, we have |H| ≡ 0 mod h0. Since h0 | b0, there exists some 0 ≤ a < b0/h0 such that |H| ≡ ah0 mod b0. Let Ω∗0 be the multisubset of Ω0 consisting of b0/h0 − a copies of ∅. Let D0∗ := v∈Ω∗

Tv. Hence, D0∗ is the edge-disjoint union of b0/h0 − a copies of F. We thus have |H ∪ D0∗| ≡ ah0 + |F|(b0/h0 − a) ≡ ah0 + b0 − ah0 ≡ 0 mod b0. Therefore, 1H∪D∗

0

is (b0)-divisible, as required.

0

Suppose now that SHIFTk−1 holds for some k ∈ [r−1], that is, there is Ω∗k−1 ⊆ Ω0∪···∪Ωk−1 such that 1H∪D∗

Tv. Note that Dk∗−1 is Fdivisible by Claim 2. Thus, since both H and Dk∗−1 are F-divisible, we have 1H∪D∗

is (b0,... ,bk−1)-divisible, where Dk∗−1 := v∈Ω∗

k−1

k−1

(S) = |(H ∪ Dk∗−1)(S)| ≡ 0 mod hk for all S ∈ V(kG) . Hence, 1H∪D∗

k−1

is in fact (b0,... ,bk−1,hk)divisible. Thus, if hk = bk, then 1H∪D∗

k−1

is (b0,... ,bk)-divisible and we let Ω′k := ∅. Now, assume that hk < bk. Recall that Ωk is a (b0,... ,bk)-balancer and that hk | bk. Thus, there exists a multisubset Ω′k of Ωk such that the function 1H∪D∗

k−1

τv is (b0,... ,bk)-divisible,

+ v∈Ω′

k−1

k

where τv is any v-adapter with respect to (b0,... ,bk;hk). Recall that by (9.12) we can take τv = 1Tv. In both cases, let

Ω∗k := Ω∗k−1 ∪ Ω′k ⊆ Ω0 ∪ ··· ∪ Ωk; Dk′ :=

Tv;

v∈Ω′k

Tv = Dk∗−1 ∪ Dk′ .

Dk∗ :=

v∈Ω∗k

is (b0,... ,bk)-divisible, as required. Finally, SHIFTr−1 implies that there exists Ω∗r−1 ⊆ Ω such that 1H∪D∗ is (b0,... ,br−1)-

# + 1D′

= 1H∪D∗

and hence 1H∪D∗

τv = 1D′

Thus, v∈Ω′

k−1

k

k

k

k

Tv. Clearly, D∗ ⊆ D, and we have that H ∪ D∗ is F∗-divisible. Finally, by Claim 2,

divisible, where D∗ := v∈Ω∗

r−1

D − D∗ =

Tv

v∈Ω\Ω∗r−1

has a 1-well separated F-decomposition F such that F≤(r+1) and O are edge-disjoint, completing the proof.

References

- [1] N. Alon and R. Yuster, On a hypergraph matching problem, Graphs and Combinatorics 21 (2005), 377–384.
- [2] D. Archdeacon, Self-dual embeddings of complete multipartite graphs, J. Graph Theory 18 (1994), 735–749.
- [3] B. Barber, D. Ku¨hn, A. Lo, R. Montgomery and D. Osthus, Fractional clique decompositions of dense graphs and hypergraphs, J. Combinatorial Theory Ser. B, to appear.
- [4] B. Barber, D. Ku¨hn, A. Lo and D. Osthus, Edge-decompositions of graphs with high minimum degree, Adv. Math. 288 (2016), 337–385.
- [5] J. Bl¨mer, M. Kalfane, R. Karp, M. Karpinski, M. Luby, D. Zuckerman, An XOR-based erasure-resilient coding scheme, TR-95-048, International Computer Science Institute, 1995.
- [6] A.L. Cauchy, Exercices d’analyse et de physique mathematique 2, 2nd edition, Bachelier, Paris, 1841.
- [7] C.J. Colbourn and J.H. Dinitz, Handbook of Combinatorial Designs, 2nd edition, CRC Press, 2006.
- [8] F. Dross, Fractional triangle decompositions in graphs with large minimum degree, SIAM J. Discr. Math. 30

(2016), 36–42.

- [9] P. Dukes and A. Ling, Asymptotic existence of resolvable graph designs, Canad. Math. Bull. 50 (2007), 504–518.
- [10] P. Erd˝s and H. Hanani, On a limit theorem in combinatorial analysis, Publicationes Mathematicae Debrecen 10 (1963), 10–13.
- [11] S. Glock, D. Ku¨hn, A. Lo, R. Montgomery and D. Osthus, On the decomposition threshold of a given graph, arXiv:1603.04724, 2016.
- [12] S. Glock, D. Ku¨hn, A. Lo and D. Osthus, The existence of designs via iterative absorption, arXiv:1611.06827, 2016.
- [13] H. Hanani, Decomposition of hypergraphs into octahedra, Annals of the New York Academy of Sciences, 319

(1979) 260–264.

- [14] S. Janson, T.  Luczak, and A. Rucin´ski, Random graphs, Wiley-Interscience Series in Discrete Mathematics and Optimization. Wiley-Interscience, New York, 2000.
- [15] P. Keevash, The existence of designs, arXiv:1401.3665, 2014.
- [16] P. Keevash, Counting designs, J. European Math. Soc., to appear.
- [17] T.P. Kirkman, On a problem in combinatorics, Cambridge Dublin Math. J. 2 (1847), 191–204.
- [18] F. Knox, D. Ku¨hn and D. Osthus, Edge-disjoint Hamilton cycles in random graphs, Random Structures Algorithms 46 (2015), 397–445.
- [19] A. Kostochka, D. Mubayi and J. Verstrae¨te, On independent sets in hypergraphs, Random Structures Algorithms 44 (2014), 224–239.
- [20] M. Krivelevich, Triangle factors in random graphs, Combin. Probab. Comput. 6 (1997), 337–347.
- [21] D. Ku¨hn and D. Osthus, Hamilton decompositions of regular expanders: A proof of Kelly’s conjecture for large tournaments, Adv. Math. 237 (2013), 62–146.
- [22] G. Kuperberg, S. Lovett and R. Peled, Probabilistic existence of regular combinatorial objects, arXiv:1302.4295, 2013. (Extended abstract version appeared in STOC 2012.)
- [23] S. Lovett, S. Rao and A. Vardy, Probabilistic existence of large sets of designs, arXiv:1704.07964, 2017.
- [24] C.St.J.A. Nash-Williams, An unsolved problem concerning decomposition of graphs into triangles, In: Combinatorial Theory and its Applications III, pages 1179–1183, North Holland, 1970.


- [25] R. Raman, The power of collision: randomized parallel algorithms for chaining and integer sorting, In: Foundations of software technology and theoretical computer science (Bangalore, 1990), volume 472 of Lecture Notes in Comput. Sci., pages 161–175, Springer, Berlin, 1990.
- [26] D.R. Ray-Chaudhuri and R.M. Wilson, The existence of resolvable designs, in: A Survey of Combinatorial Theory, pages 361–375, North-Holland, Amsterdam, 1973.
- [27] V. Ro¨dl, On a packing and covering problem, European J. Comb. 5 (1985), 69–78.
- [28] V. Ro¨dl, A. Rucin´ski and E. Szemere´di, A Dirac-type theorem for 3-uniform hypergraphs, Combin. Probab. Comput. 15 (2006), 229–251.
- [29] V. Ro¨dl and E. Sinˇajova´,ˇ Note on independent sets in Steiner systems, Random Structures Algorithms 5

(1994), 183–190.

- [30] S. Schechter, On the inversion of certain matrices, Mathematical Tables and Other Aids to Computation 13

(1959), 73–77.

- [31] L. Teirlinck, Non-trivial t-designs without repeated blocks exist for all t, Discrete Math. 65 (1987), 301–311.
- [32] R.M. Wilson, An existence theory for pairwise balanced designs I. Composition theorems and morphisms, J. Combinatorial Theory Ser. A 13 (1972), 220–245.
- [33] R.M. Wilson, An existence theory for pairwise balanced designs II. The structure of PBD-closed sets and the existence conjectures, J. Combinatorial Theory Ser. A 13 (1972), 246–273.
- [34] R.M. Wilson, An existence theory for pairwise balanced designs III. Proof of the existence conjectures, J. Combinatorial Theory Ser. A 18 (1975), 71–79.
- [35] R.M. Wilson, Decompositions of complete graphs into subgraphs isomorphic to a given graph, In Proc. of the Fifth British Combinatorial Conference (Univ. Aberdeen, Aberdeen, 1975), pages 647–659, Congressus Numerantium, No. XV, Utilitas Math., Winnipeg, Man., 1976.
- [36] R. Yuster, Decomposing hypergraphs with simple hypertrees, Combinatorica 20 (2000), 119–140.


Appendix A. Additional tools We gather a few more tools which we use in the appendix.

Proposition A.1 ([12]). Let f,r′ ∈ N and r ∈ N0 with f > r. Let L be an r′-graph on n vertices with ∆(L) ≤ γn. Then every e ∈ V (rL) that does not contain any edge of L is contained in at most 2rγnf−r f-sets of V (L) that contain an edge of L.

Fact A.2 ([12]). If G is an (ε,ξ,f,r)-supercomplex, then for all distinct e,e′ ∈ G(r), we have |G(f)(e) ∩ G(f)(e′)| ≥ (ξ − ε)(n − 2r)f−r.

Proposition A.3 ([12]). Let 1/n ≪ ε,ξ,1/f and r ∈ [f − 1]. Suppose that G is an (ε,ξ,f,r)supercomplex on n vertices. Let Yused be an f-graph on V (G) with ∆r(Yused) ≤ εnf−r. Then

- G − Yused is a (2r+2ε,ξ − 22r+1ε,f,r)-supercomplex.


Using (WS2), we can deduce that there are many f-disjoint F-decompositions of a supercomplex. This will be an important tool in the proof of the Cover down lemma (Lemma 6.9), where we will ﬁnd many candidate F-decompositions and then pick one at random.

Corollary A.4. Let 1/n ≪ ε ≪ ξ,1/f and r ∈ [f − 1] and assume that (∗)r is true. Let F be a weakly regular r-graph on f vertices. Suppose that G is an F-divisible (ε,ξ,f,r)-supercomplex on n vertices. Then the number of pairwise f-disjoint 1/ε-well separated F-decompositions of G is at least ε2nf−r.

Proof. Suppose that F1,... ,Ft are f-disjoint 1/ε-well separated F-decompositions of G, where t ≤ ε2nf−r. Let Yused := j∈[t] Fj≤(f). By (WS2), we have ∆r(Yused) ≤ t/ε ≤ εnf−r. Thus, by Proposition A.3, G − Yused is an F-divisible (2r+2ε,ξ − 22r+1ε,f,r)-supercomplex and thus has a 1/ε-well separated F-decomposition Ft+1 by (∗)r, which is f-disjoint from F1,... ,Ft.

A.1. Probabilistic tools.

- Lemma A.5 (see [14, Corollary 2.3, Corollary 2.4, Remark 2.5 and Theorem 2.8]). Let X be the sum of n independent Bernoulli random variables. Then the following hold.

- (i) For all t ≥ 0, P(|X − EX| ≥ t) ≤ 2e−2t2/n.
- (ii) For all 0 ≤ ε ≤ 3/2, P(|X − EX| ≥ εEX) ≤ 2e−ε2EX/3.
- (iii) If t ≥ 7EX, then P(X ≥ t) ≤ e−t.


- Lemma A.6 ([12]). Let 1/n ≪ p,α,1/a,1/B. Let I be a set of size at least αna and let (Xi)i∈I be a family of Bernoulli random variables with P(Xi = 1) ≥ p. Suppose that I can be partitioned into at most Bna−1 sets I1,... ,Ik such that for each j ∈ [k], the variables (Xi)i∈Ij are independent. Let X := i∈I Xi. Then we have


P(|X − EX| ≥ n−1/5EX) ≤ e−n1/6. Lemma A.6 can be conveniently applied in the following situation: We are given an r-graph

- H on n vertices and H′ is a random subgraph of H, where every edge of H survives (i.e. lies in H′) with some probability ≥ p.


Corollary A.7 ([12]). Let 1/n ≪ p,1/r,α. Let H be an r-graph on n vertices with |H| ≥ αnr. Let H′ be a random subgraph of H, where each edge of H survives (i.e. lies in H′) with some probability ≥ p. Moreover, suppose that for every matching M in H, the edges of M survive independently. Then we have

P(||H′| − E|H′|| ≥ n−1/5E|H′|) ≤ e−n1/6.

When we apply Corollary A.7, it will be clear that for every matching M in H, the edges of M survive independently, and we will not discuss this explicitly.

We will also use the following simple result.

- Proposition A.8 (Jain, see [25, Lemma 8]). Let X1,... ,Xn be Bernoulli random variables such that, for any i ∈ [n] and any x1,... ,xi−1 ∈ {0,1},


P(Xi = 1 | X1 = x1,... ,Xi−1 = xi−1) ≤ p. Let B ∼ B(n,p) and X := X1 + ··· + Xn. Then P(X ≥ a) ≤ P(B ≥ a) for any a ≥ 0.

We now use Lemma A.6 to prove Lemma 5.4, which states that the random F-packing derived from a clique packing yields a quasirandom leftover.

- Proof of Lemma 5.4. For e ∈ G(r), we let Ke be the unique element of K≤(f) with e ⊆ Ke.


Let Gind := G−K≤(r+1). G′(r) is a random subgraph of G(indr) , where for any I ⊆ G(r), the events {e ∈ G′(r)}e∈I are independent if the sets {Ke}e∈I are distinct. Since ∆(K≤(r+1)) ≤ f − r, Proposition 4.5 implies that Gind is (1.1ε,d,f,r)-regular and (ξ − ε,f + r,r)-dense.

For e ∈ G(r), let Qe := Gind(f)(e) and Q˜e := G(indf+r)(e). Thus, |Qe| = (d ± 1.1ε)nf−r and |Q˜e| ≥ 0.95ξnf. Let Q′e be the random subgraph of Qe consisting of all Q ∈ Qe with Qr∪e \{e} ⊆ G′(r). Similarly, let Q˜′e be the random subgraph of Q˜e consisting of all Q ∈ Q˜e with Qr∪e \{e} ⊆ G′(r). Note that if e ∈ G′(r), then Q′e = G′(f)(e). Moreover, note that by deﬁnition of Gind, we have

- (A.1) |(e ∪ Q) ∩ K| ≤ r for all Q ∈ Qe,K ∈ K.


Consider Q ∈ Qe. By (A.1), the Ke′ with e′ ∈ Qr∪e \ {e} are all distinct, hence we have P(Q ∈ Q′e) = p(fr)−1. Thus, E|Q′e| = p(fr)−1|Qe|.

Deﬁne an auxiliary graph Ae on vertex set Qe where QQ′ ∈ Ae if and only if there exists

- K ∈ K≤(f) \ {Ke} such that |(e ∪ Q) ∩ K| = r and |(e ∪ Q′) ∩ K| = r. Using (A.1), it is easy to see that if Y is an independent set in Ae, then the events {Q ∈ Q′e}Q∈Y are independent.


Claim 1: Qe can be partitioned into 2 fr 2nf−r−1 independent sets in Ae.

Proof of claim: It is suﬃcent to prove that ∆(Ae) ≤ fr 2nf−r−1. Fix Q ∈ V (Ae). There are f r −1 r-subsets e′ of e∪Q other than e. For each of these, Ke′ is the unique K ∈ K≤(f) \{Ke} which contains e′. Each choice of Ke′ has fr r-subsets e′′. If we want e ∪ Q′ to contain e′′, then since e′′ = e, we have |e ∪ e′′| ≥ r + 1 and thus there are at most nf−r−1 possibilities for Q′. −

By Lemma A.6, we thus have P(|Q′e| = (1 ± n−1/5)E|Q′e|) ≤ e−n1/6. We conclude that with probability at least 1−e−n1/6 we have |Q′e| = (p(fr)−1d±2ε)nf−r. Together with a union bound, this implies that whp G′ is (2ε,p(fr)−1d,f,r)-regular, which proves (i).

A similar argument shows that whp G′ is (0.9p(f+rr)−1ξ,f + r,r)-dense.

To prove (iii), let S ∈ Vr−(G1) . Clearly, we have E|G′(r)(S)| = p|G(r)(S)|. If |G(r)(S)| = 0, then we clearly have |G(r)(S)| ≤ 1.1p∆(G(r)), so assume that S ⊆ e ∈ G(r). Since e is contained in at least 0.5ξnf−r f-sets in G, and every r-set e′ = e is contained in a most nf−(r+1) of these, we can deduce that |G(r)(S)| ≥ 0.5ξn. Deﬁne the auxiliary graph AS with vertex set G(r)(S) such that e1e2 ∈ AS if and only if KS∪e1 = KS∪e2. Again, we have ∆(AS) ≤ f − r and thus G(r)(S) can be partitioned into f − r + 1 sets which are independent in AS. By Lemma A.6, we thus have P(|G′(r)(S)| = (1 ± n−1/5)p|G(r)(S)|) ≤ e−n1/6. Using a union bound, we conclude that whp ∆(G′(r)) ≤ 1.1p∆(G(r)).

Finally, we consider subcomplexes obtained by taking a random subset of the vertex set of G.

Corollary A.9 ([12]). Let 1/n ≪ γ ≪ µ ≪ ε ≪ ξ,1/f and r ∈ [f − 1]. Let G be an (ε,ξ,f,r)supercomplex on n vertices. Suppose that U is a random subset of V (G) obtained by including every vertex from V (G) independently with probability µ. Then whp for any W ⊆ V (G) with |W| ≤ γn, G[U △ W] is a (2ε,ξ − ε,f,r)-supercomplex.

A.2. Greedy coverings and divisibility. The following lemma allows us to extend a given collection of r-sets into suitable r-disjoint f-cliques.

- Lemma A.10 ([12]). Let 1/n ≪ γ ≪ α,1/s,1/f and r ∈ [f − 1]. Let G be a complex on n vertices and let L ⊆ G(r) satisfy ∆(L) ≤ γn. Suppose that L decomposes into L1,... ,Lm with 1 ≤ |Lj| ≤ s. Suppose that for every j ∈ [m], we are given some candidate set Qj ⊆


e∈Lj G(f)(e) with |Qj| ≥ αnf−r. Then there exists Qj ∈ Qj for each j ∈ [m] such that, writing Kj := (Qj ⊎ Lj)≤, we have that Kj and Kj′ are r-disjoint for all distinct j,j′ ∈ [m], and ∆( j∈[m] Kj(r)) ≤

√γn.

![image 50](<2017-glock-hypergraph-designs-arbitrary_images/imageFile50.png>)

- Corollary A.11. Let 1/n ≪ γ ≪ α,1/f and r ∈ [f − 1]. Suppose that F is an r-graph on f vertices. Let G be a complex on n vertices and let H ⊆ G(r) with ∆(H) ≤ γn and |G(f)(e)| ≥ αnf−r for all e ∈ H. Then there is a 1-well separated F-packing F in G that covers

all edges of H and such that ∆(F(r)) ≤

√γn.

![image 51](<2017-glock-hypergraph-designs-arbitrary_images/imageFile51.png>)

Proof. Let e1,... ,em be an enumeration of H. For j ∈ [m], deﬁne Lj := {ej} and Qj := G(f)(e). Apply Lemma A.10 to obtain K1,... ,Km. For each j ∈ [m], let Fj be a copy of F with V (Fj) = Kj and such that ej ∈ Fj. Then F := {F1,... ,Fm} is as desired.

We can combine Lemma 5.3 and Corollary A.11 to deduce the following result. It allows us to make an r-graph divisible by deleting a small fraction of edges (even if we are forbidden to delete a certain set of edges H). Note that the result has a similar ﬂavour as Corollary 8.5, but the assumptions are diﬀerent.

- Corollary A.12. Let 1/n ≪ γ,ε ≪ ξ,1/f and r ∈ [f − 1]. Let F be an r-graph on f vertices. Suppose that G is a complex on n vertices which is (ε,d,f,r)-regular for some d ≥ ξ and (ξ,f + r,r)-dense. Let H ⊆ G(r) satisfy ∆(H) ≤ εn. Then there exists L ⊆ G(r) − H such that ∆(L) ≤ γn and G(r) − L is F-divisible.


Proof. We clearly have |G(f)(e)| ≥ 0.5ξnf−r for all e ∈ H. Thus, by Corollary A.11, there exists an F-packing F0 in G which covers all edges of H and satisﬁes ∆(F0(r)) ≤

√εn. By

![image 52](<2017-glock-hypergraph-designs-arbitrary_images/imageFile52.png>)

Proposition 4.5(i) and (ii), G′ := G − F0(r) is still (2r+1√ε,d,f,r)-regular and (ξ/2,f + r,r)dense. Thus, by Lemma 5.3, there exists an F-packing Fnibble in G′ such that ∆(L) ≤ γn, where

![image 53](<2017-glock-hypergraph-designs-arbitrary_images/imageFile53.png>)

- L := G′(r) − Fnibble(r) = G(r) − F0(r) − Fnibble(r) ⊆ G(r) − H. Clearly, G(r) − L is F-divisible (in fact, F-decomposable).


Appendix B. Vortices

Here, we prove Lemma 6.4, which states that given a vortex in a supercomplex, we can cover all edges which do not lie in the ﬁnal vortex set. As sketched in Section 6, we achieve this by alternately applying the F-nibble lemma (Lemma 5.3) and the Cover down lemma (Lemma 6.9). Recall that the Cover down down lemma guarantees the existence of a suitable ‘cleaning graph’ or ‘partial absorber’ which allows us to ‘clean’ the leftover of an application of the F-nibble lemma in the sense that the new leftover is guaranteed to lie in the next vortex set. For technical reasons, we will in fact ﬁnd all cleaning graphs ﬁrst (one for each vortex set) and set them aside even before the ﬁrst nibble.

- B.1. Existence of cleaners. The aim of this subsection is to apply the Cover down lemma to each ‘level’ i of the vortex to obtain a ‘cleaning graph’ Hi (playing the role of H∗) for each i ∈ [ℓ] (see Lemma B.2). Let G be a complex and U0 ⊇ U1 ⊇ ··· ⊇ Uℓ a vortex in G. We say that H1,... ,Hℓ is a (γ,ν,κ,F)-cleaner (for the said vortex) if the following hold for all i ∈ [ℓ]:


(C1) Hi ⊆ G(r)[Ui−1] − G(r)[Ui+1], where Uℓ+1 := ∅; (C2) ∆(Hi) ≤ ν|Ui−1|; (C3) Hi and Hi+1 are edge-disjoint, where Hℓ+1 := ∅; (C4) whenever L ⊆ G(r)[Ui−1] is such that ∆(L) ≤ γ|Ui−1| and Hi ∪ L is F-divisible and O is an (r+1)-graph on Ui−1 with ∆(O) ≤ γ|Ui−1|, there exists a κ-well separated F-packing F in G[Hi ∪ L][Ui−1] − O which covers all edges of Hi ∪ L except possibly some inside Ui.

Note that (C1) and (C3) together imply that H1,... ,Hℓ are edge-disjoint. The following proposition will be used to ensure (C3).

- Proposition B.1 ([12]). Let 1/n ≪ ε ≪ µ,ξ,1/f and r ∈ [f −1]. Let ξ′ := ξ(1/2)(8f+1). Let G be a complex on n vertices and let U ⊆ V (G) of size µn and (ε,µ,ξ,f,r)-random in G. Suppose that H is a random subgraph of G(r) obtained by including every edge of G(r) independently with probability 1/2. Then with probability at least 1 − e−n1/10,


- (i) U is (√ε,µ,ξ′,f,r)-random in G[H] and

![image 54](<2017-glock-hypergraph-designs-arbitrary_images/imageFile54.png>)

- (ii) G is (√ε,f,r)-dense with respect to H − G(r)[U¯], where U¯ := V (G) \ U.


![image 55](<2017-glock-hypergraph-designs-arbitrary_images/imageFile55.png>)

The following lemma shows that cleaners exist.

- Lemma B.2. Let 1/m ≪ 1/κ ≪ γ ≪ ε ≪ ν ≪ µ,ξ,1/f be such that µ ≤ 1/2 and r ∈ [f − 1]. Assume that (∗)i is true for all i ∈ [r − 1] and that F is a weakly regular r-graph on f vertices. Let G be a complex and U0 ⊇ U1 ⊇ ··· ⊇ Uℓ an (ε,µ,ξ,f,r,m)-vortex in G. Then there exists a (γ,ν,κ,F)-cleaner.


Proof. For i ∈ [ℓ], deﬁne Ui′ := Ui \ Ui+1, where Uℓ+1 := ∅. For i ∈ [ℓ − 1], let µi := µ(1 − µ), and let µℓ := µ. By (V4) and (V5), we have for all i ∈ [ℓ] that Ui′ is (ε,µi,ξ,f,r)-random in G[Ui−1].

Split G(r) randomly into G0 and G1, that is, independently for every edge e ∈ G(r), put e into G0 with probability 1/2 and into G1 otherwise. We claim that with positive probability, the following hold for every i ∈ [ℓ]:

- (i) Ui′ is (√ε,µi,ξ(1/2)(8f+1),f,r)-random in G[Gi mod 2][Ui−1];

![image 56](<2017-glock-hypergraph-designs-arbitrary_images/imageFile56.png>)

- (ii) G[Ui−1] is (√ε,f,r)-dense with respect to Gi mod 2[Ui−1] − G(r)[Ui−1 \ Ui′].


![image 57](<2017-glock-hypergraph-designs-arbitrary_images/imageFile57.png>)

- By Proposition B.1, the probability that (i) or (ii) do not hold for i ∈ [ℓ] is at most e−|Ui−1|1/10 ≤


|Ui−1|−2. Since ℓi=1 |Ui−1|−2 < 1, we deduce that with positive probability, (i) and (ii) hold for all i ∈ [ℓ].

Therefore, there exist G0,G1 satisfying the above properties. For every i ∈ [ℓ], we will ﬁnd Hi using the Cover down lemma (Lemma 6.9). Let i ∈ [ℓ]. Apply Lemma 6.9 with the following objects/parameters:

object/parameter G[Gi mod 2][Ui−1] Ui′ G[Ui−1] F |Ui−1| κ γ √ε ν µi ξ(1/2)(8f+1) f r playing the role of G U G˜ F n κ γ ε ν µ ξ f r

![image 58](<2017-glock-hypergraph-designs-arbitrary_images/imageFile58.png>)

![image 59](<2017-glock-hypergraph-designs-arbitrary_images/imageFile59.png>)

![image 60](<2017-glock-hypergraph-designs-arbitrary_images/imageFile60.png>)

![image 61](<2017-glock-hypergraph-designs-arbitrary_images/imageFile61.png>)

![image 62](<2017-glock-hypergraph-designs-arbitrary_images/imageFile62.png>)

![image 63](<2017-glock-hypergraph-designs-arbitrary_images/imageFile63.png>)

![image 64](<2017-glock-hypergraph-designs-arbitrary_images/imageFile64.png>)

![image 65](<2017-glock-hypergraph-designs-arbitrary_images/imageFile65.png>)

![image 66](<2017-glock-hypergraph-designs-arbitrary_images/imageFile66.png>)

![image 67](<2017-glock-hypergraph-designs-arbitrary_images/imageFile67.png>)

![image 68](<2017-glock-hypergraph-designs-arbitrary_images/imageFile68.png>)

![image 69](<2017-glock-hypergraph-designs-arbitrary_images/imageFile69.png>)

![image 70](<2017-glock-hypergraph-designs-arbitrary_images/imageFile70.png>)

![image 71](<2017-glock-hypergraph-designs-arbitrary_images/imageFile71.png>)

![image 72](<2017-glock-hypergraph-designs-arbitrary_images/imageFile72.png>)

![image 73](<2017-glock-hypergraph-designs-arbitrary_images/imageFile73.png>)

![image 74](<2017-glock-hypergraph-designs-arbitrary_images/imageFile74.png>)

![image 75](<2017-glock-hypergraph-designs-arbitrary_images/imageFile75.png>)

![image 76](<2017-glock-hypergraph-designs-arbitrary_images/imageFile76.png>)

![image 77](<2017-glock-hypergraph-designs-arbitrary_images/imageFile77.png>)

![image 78](<2017-glock-hypergraph-designs-arbitrary_images/imageFile78.png>)

![image 79](<2017-glock-hypergraph-designs-arbitrary_images/imageFile79.png>)

![image 80](<2017-glock-hypergraph-designs-arbitrary_images/imageFile80.png>)

![image 81](<2017-glock-hypergraph-designs-arbitrary_images/imageFile81.png>)

![image 82](<2017-glock-hypergraph-designs-arbitrary_images/imageFile82.png>)

![image 83](<2017-glock-hypergraph-designs-arbitrary_images/imageFile83.png>)

![image 84](<2017-glock-hypergraph-designs-arbitrary_images/imageFile84.png>)

![image 85](<2017-glock-hypergraph-designs-arbitrary_images/imageFile85.png>)

Hence, there exists

Hi ⊆ Gi mod 2[Ui−1] − Gi mod 2[Ui−1 \ Ui′] ⊆ Gi mod 2[Ui−1] − G(r)[Ui+1] with ∆(Hi) ≤ ν|Ui−1| and the following ‘cleaning’ property: for all L ⊆ G(r)[Ui−1] with ∆(L) ≤ γ|Ui−1| such that Hi ∪ L is F-divisible and all (r + 1)-graphs O on Ui−1 with ∆(O) ≤ γ|Ui−1|, there exists a κ-well separated F-packing F in G[Hi ∪ L][Ui−1] − O which covers all edges of Hi ∪ L except possibly some inside Ui′ ⊆ Ui. Thus, (C1), (C2) and (C4) hold.

Since G0 and G1 are edge-disjoint, (C3) holds as well. Thus, H1,... ,Hℓ is a (γ,ν,κ,F)cleaner.

- B.2. Obtaining a near-optimal packing. Recall that Lemma 6.4 guarantees an F-packing covering all edges except those in the ﬁnal set Uℓ of a vortex. We prove this by applying successively the F-nibble lemma (Lemma 5.3) and the deﬁnition of a cleaner to each set Ui in the vortex.


- Proof of Lemma 6.4. Choose new constants γ,ν > 0 such that 1/m ≪ 1/κ ≪ γ ≪ ε ≪ ν ≪ µ ≪ ξ,1/f.


Apply Lemma B.2 to obtain a (γ,ν,κ,F)-cleaner H1,... ,Hℓ. Note that by (V4) and Fact 6.5(ii), G[Ui] is an (ε,ξ,f,r)-supercomplex for all i ∈ [ℓ], and the same holds for i = 0 by assumption. Let Hℓ+1 := ∅ and Uℓ+1 := ∅.

For i ∈ [ℓ]0 and Fi∗, deﬁne the following conditions:

- (FP1∗)i Fi∗ is a 4κ-well separated F-packing in G − Hi+1 − G(r)[Ui+1];
- (FP2∗)i Fi∗ covers all edges of G(r) that are not inside Ui;
- (FP3∗)i for all e ∈ G(r)[Ui], |Fi∗≤(f)(e)| ≤ 2κ;
- (FP4∗)i ∆(Fi∗(r)[Ui]) ≤ µ|Ui|. Note that (FP1∗)0–(FP4∗)0 hold trivially with F0∗ := ∅. We will now proceed inductively


until we obtain Fℓ∗ satisfying (FP1∗)ℓ–(FP4∗)ℓ. Clearly, taking F := Fℓ∗ completes the proof (using (FP1∗)ℓ and (FP2∗)ℓ).

Suppose that for some i ∈ [ℓ], we have found Fi∗−1 such that (FP1∗)i−1–(FP4∗)i−1 hold. Let

Gi := G[Ui−1] − (Fi∗−(r1) ∪ Hi+1 ∪ G(r)[Ui+1]) − Fi∗≤−1(r+1). We now intend to ﬁnd Fi such that:

- (FP1) Fi is a 2κ-well separated F-packing in Gi;
- (FP2) Fi covers all edges from G(r)[Ui−1] − Fi∗−(r1) that are not inside Ui;
- (FP3) ∆(Fi(r)[Ui]) ≤ µ|Ui|. We ﬁrst observe that this is suﬃcient for Fi∗ := Fi∗−1 ∪Fi to satisfy (FP1∗)i–(FP4∗)i. Note that Fi(r) and Fi∗−(r1) are edge-disjoint, and Fi and Fi∗−1 are (r+1)-disjoint by deﬁnition of Gi. Together with (FP1∗)i−1 this implies that Fi∗ is a well separated F-packing in G − Hi+1 − G(r)[Ui+1]. Let e ∈ G(r). If e  ⊆ Ui−1, then |Fi≤(f)(e)| = 0 and hence |Fi∗≤(f)(e)| = |Fi∗≤−1(f)(e)| ≤ 4κ. If


e ⊆ Ui−1, then we have |Fi∗≤(f)(e)| = |Fi∗≤−1(f)(e)| + |Fi≤(f)(e)| ≤ 4κ by (FP3∗)i−1 and (FP1). Thus, Fi∗ is 4κ-well separated and (FP1∗)i holds.

Clearly, (FP2∗)i−1 and (FP2) imply (FP2∗)i. Moreover, observe that Fi∗≤−1(r)[Ui] is empty by (FP1∗)i−1. Thus, (FP3∗)i holds since Fi is 2κ-well separated, and (FP3) implies (FP4∗)i.

It thus remains to show that Fi satisfying (FP1)–(FP3) exists. We will obtain Fi as the union of two packings, one obtained from the F-nibble lemma (Lemma 5.3) and one using (C4). Let Gi,nibble := G[Ui−1] − (Fi∗−(r1) ∪ Hi ∪ G(r)[Ui]) − Fi∗≤−1(r+1). Recall that G[Ui−1] is an (ε,ξ,f,r)supercomplex. In particular, it is (ε,d,f,r)-regular for some d ≥ ξ, and (ξ,f +r,r)-dense. Note that by (FP4∗)i−1, (C2) and (V2) we have

∆(Fi∗−(r1)[Ui−1] ∪ Hi ∪ G(r)[Ui]) ≤ µ|Ui−1| + ν|Ui−1| + µ|Ui−1| ≤ 3µ|Ui−1|.

Moreover, ∆(Fi∗≤−1(r+1)) ≤ 4κ(f − r) ≤ µ|Ui−1| by Fact 4.3(i). Thus, Proposition 4.5(i) and (ii) imply that Gi,nibble is still (2r+3µ,d,f,r)-regular and (ξ/2,f + r,r)-dense. Since µ ≪ ξ, we can apply Lemma 5.3 to obtain a κ-well separated F-packing Fi,nibble in Gi,nibble such that

∆(Li,nibble) ≤ 12γ|Ui−1|, where Li,nibble := G(i,nibbler) − Fi,nibble(r) . Since by (FP2∗)i−1, G(r) − Fi∗−(r1) − Fi,nibble(r) = G(r)[Ui−1] − Fi∗−(r1) − Fi,nibble(r)

![image 86](<2017-glock-hypergraph-designs-arbitrary_images/imageFile86.png>)

= (G(i,nibbler) ∪ Hi ∪ G(r)[Ui]) − Fi,nibble(r)

= Hi ∪ G(r)[Ui] ∪ Li,nibble,

we know that Hi ∪ G(r)[Ui] ∪ Li,nibble is F-divisible. By (C1) and (C3), we know that Hi+1 ∪ G(r)[Ui+1] ⊆ G(r)[Ui] − Hi. Moreover, by (C2) and Proposition 4.5(v) we have that G[Ui] − Hi is a (2µ,ξ/2,f,r)-supercomplex. We can thus apply Corollary A.12 (with G[Ui] − Hi, Hi+1 ∪ G(r)[Ui+1], 2µ playing the roles of G,H,ε) to ﬁnd an F-divisible subgraph Ri of G(r)[Ui] − Hi containing Hi+1 ∪ G(r)[Ui+1] such that ∆(Li,res) ≤ 21γ|Ui|, where Li,res := G(r)[Ui] − Hi − Ri.

![image 87](<2017-glock-hypergraph-designs-arbitrary_images/imageFile87.png>)

Let Li := Li,nibble ∪ Li,res. Clearly, Li ⊆ G(r)[Ui−1] and ∆(Li) ≤ γ|Ui−1|. Note that

- (B.1) Hi ∪ Li = (Hi ∪· (G(r)[Ui] − Hi) ∪· Li,nibble) − Ri = G(r) − Fi∗−(r1) − Fi,nibble(r) − Ri


is F-divisible. Moreover, ∆(Fi∗≤−1(r+1) ∪Fi,nibble≤(r+1)) ≤ 5κ(f −r) by Fact 4.3(i). Thus, by (C4) there exists a κ-well separated F-packing Fi,clean in

Gi,clean := G[Hi ∪ Li][Ui−1] − Fi∗≤−1(r+1) − Fi,nibble≤(r+1) which covers all edges of Hi ∪ Li except possibly some inside Ui.

We claim that Fi := Fi,nibble ∪ Fi,clean is the desired packing. Since Fi,nibble(r) and Fi,clean(r) are edge-disjoint and Fi,nibble and Fi,clean are (r +1)-disjoint, we have that Fi is a 2κ-well separated F-packing by Fact 4.3(ii). Moreover, it is easy to see from (C1) that Gi,nibble ⊆ Gi. Crucially, since Ri was chosen to contain Hi+1 ∪ G(r)[Ui+1], we have from (FP2∗)i−1 that

(B.1)

⊆ G(r)[Ui−1] − Ri − Fi∗−(r1) ⊆ G(r)[Ui−1] − (Fi∗−(r1) ∪ Hi+1 ∪ G(r)[Ui+1]) and thus Gi,clean ⊆ Gi as well. Hence, (FP1) holds.

Hi ∪ Li

Clearly, Fi covers all edges of G(r)[Ui−1] − Fi∗−(r1) that are not inside Ui, thus (FP2) holds.

Finally, since Fi,nibble(r) [Ui] is empty, we have ∆(Fi(r)[Ui]) ≤ ∆(Hi∪Li) ≤ ν|Ui−1|+γ|Ui−1| ≤ µ|Ui|, as needed for (FP3).

Appendix C. Transformers

Here, we prove Lemma 7.5, which guarantees a transformer from H to H′ if H H′. As indicated in Section 7.1, a key step in the argument is the ability to construct ‘localised transformers’ between graphs S1 ⊎ L and S2 ⊎ L. This is achieved by the following lemma.

- Lemma C.1. Let 1/n ≪ γ′ ≪ γ,1/κ,ε ≪ ξ,1/f and 1 ≤ i < r < f. Assume that (∗)r−i is


true. Let F be a weakly regular r-graph on f vertices and assume that S∗ ∈ V(iF) is such that F(S∗) is non-empty. Let G be an (ε,ξ,f,r)-supercomplex on n vertices, let S1,S2 ∈ G(i) with S1 ∩ S2 = ∅, and let φ: S1 → S2 be a bijection. Moreover, suppose that L is an F(S∗)-divisible subgraph of G(S1)(r−i) ∩ G(S2)(r−i) with |V (L)| ≤ γ′n.

Then there exist T,R ⊆ G(r) such that the following hold:

- (TR1) V (R) ⊆ V (G) \ S2 and |e ∩ S1| ∈ [i − 1] for all e ∈ R (so if i = 1, then R must be empty since [0] = ∅);
- (TR2) T is a (κ + 1)-well separated ((S1 ⊎ L) ∪ φ(R),(S2 ⊎ L) ∪ R;F)-transformer in G;
- (TR3) |V (T ∪ R)| ≤ γn.


Proof. We may assume that γ′ ≪ γ ≪ 1/κ,ε. Choose µ > 0 with γ′ ≪ µ ≪ γ ≪ 1/κ,ε. We split the argument into two parts. First, we will establish the following claim, which is the essential part and relies on (∗)r−i.

Claim 1: There exist T,Rˆ 1,A,R1,A∪L ⊆ G(r) and κ-well separated F-packings Fˆ1,Fˆ2 in G such that the following hold:

- (tr1) V (R1,A ∪ R1,A∪L) ⊆ V (G) \ S2 and |e ∩ S1| ∈ [i − 1] for all e ∈ R1,A ∪ R1,A∪L;
- (tr2) Tˆ, S1⊎L, S2 ⊎L, R1,A, φ(R1,A), R1,A∪L, φ(R1,A∪L) are pairwise edge-disjoint subgraphs of G(r);
- (tr3) Fˆ1(r) = Tˆ ∪ (S1 ⊎ L) ∪ R1,A∪L ∪ φ(R1,A) and Fˆ2(r) = Tˆ ∪ (S2 ⊎ L) ∪ R1,A ∪ φ(R1,A∪L);
- (tr4) |V (Tˆ ∪ R1,A ∪ R1,A∪L)| ≤ 2µn.


Proof of claim: By Corollary A.9 and Lemma A.5(i), there exists a subset U ⊆ V (G) with 0.9µn ≤ |U| ≤ 1.1µn such that G′ := G[U ∪ S1 ∪ S2 ∪ V (L)] is a (2ε,ξ − ε,f,r)-supercomplex. By Proposition 4.4, G′′ := G′(S1)∩G′(S2) is a (2ε,ξ −ε,f −i,r−i)-supercomplex. Clearly, L ⊆ G′′(r−i) and ∆(L) ≤ γ′n ≤

√γ′|U|. Thus, by Proposition 4.5(v), G′′−L is a (3ε,ξ−2ε,f−i,r−i)supercomplex. By Corollary A.12, there exists H ⊆ G′′(r−i) −L such that A := G′′(r−i) −L−H is F(S∗)-divisible and ∆(H) ≤ γ′n. In particular, by Proposition 4.5(v) we have that

![image 88](<2017-glock-hypergraph-designs-arbitrary_images/imageFile88.png>)

- (i) G′′[A] is an F(S∗)-divisible (3ε,ξ/2,f − i,r − i)-supercomplex;
- (ii) G′′[A ∪ L] is an F(S∗)-divisible (3ε,ξ/2,f − i,r − i)-supercomplex.


Recall that F being weakly regular implies that F(S∗) is weakly regular as well (see Proposition 4.2). By (i) and (∗)r−i, there exists a κ-well separated F(S∗)-decomposition FA of G′′[A]. By Fact 4.3(i), ∆(FA≤(r−i+1)) ≤ κf. Thus, by (ii), Proposition 4.5(v) and (∗)r−i, there also exists a κ-well separated F(S∗)-decomposition FA∪L of G′′[A ∪ L] − FA≤(r−i+1). In particular, FA and FA∪L are (r − i + 1)-disjoint.

We deﬁne

(F1,A,F2,A) := S1 ⊳ FA ⊲ S2,

(F1,A∪L,F2,A∪L) := S1 ⊳ FA∪L ⊲ S2. By Proposition 7.9(i), for j ∈ [2], Fj,A is a κ-well separated F-packing in G′ ⊆ G with {e ∈ Fj,A(r) : Sj ⊆ e} = Sj ⊎ A and Fj,A∪L is a κ-well separated F-packing in G′ ⊆ G with {e ∈ Fj,A(r)∪L : Sj ⊆ e} = Sj ⊎ (A ∪ L).

For j ∈ [2], let

Tj,A := {e ∈ Fj,A(r) : |e ∩ Sj| = 0}, Tj,A∪L := {e ∈ Fj,A(r)∪L : |e ∩ Sj| = 0},

Rj,A := {e ∈ Fj,A(r) : |e ∩ Sj| ∈ [i − 1]}, Rj,A∪L := {e ∈ Fj,A(r)∪L : |e ∩ Sj| ∈ [i − 1]}.

By Deﬁnition 7.8, we have that T1,A = T2,A and T1,A∪L = T2,A∪L. We thus set

TA := T1,A = T2,A and TA∪L := T1,A∪L = T2,A∪L. Moreover, we have

- (C.1) φ(R1,A) = R2,A and φ(R1,A∪L) = R2,A∪L.


Note that R1,A,R2,A,R1,A∪L,R2,A∪L are empty if i = 1. Crucially, since FA and FA∪L are (r − i + 1)-disjoint, it is easy to see (by contradiction) that TA and TA∪L are edge-disjoint, and that for j ∈ [2], Rj,A and Rj,A∪L are edge-disjoint. Further, since A and L are edge-disjoint, we clearly have for j ∈ [2] that Sj ⊎L and Sj ⊎A are edge-disjoint. Using this, it is straightforward to see that

(†) S1 ⊎ L, S2 ⊎ L, S1 ⊎ A, S2 ⊎ A, TA, TA∪L, R1,A, R2,A, R1,A∪L, R2,A∪L are pairwise

edge-disjoint subgraphs of G(r). Observe that for j ∈ [2], we have

- (C.2) Fj,A(r) = (Sj ⊎ A) ∪· Rj,A ∪· TA;
- (C.3) Fj,A(r)∪L = (Sj ⊎ (A ∪ L)) ∪· Rj,A∪L ∪· TA∪L. Deﬁne


Tˆ := (S1 ⊎ A) ∪ (S2 ⊎ A) ∪ TA ∪ TA∪L;

Fˆ1 := F1,A∪L ∪ F2,A; Fˆ2 := F1,A ∪ F2,A∪L.

We now check that (tr1)–(tr4) hold. First note that by (†) we clearly have T,Rˆ 1,A,R1,A∪L ⊆ G(r). Moreover, since FA and FA∪L are (r−i+1)-disjoint, we have that F1,A∪L and F2,A are r-disjoint and thus Fˆ1 is a κ-well separated F-packing in G by Fact 4.3(iii). Similarly, Fˆ2 is a κ-well separated F-packing in G.

To check (tr1), note that V (R1,A) ⊆ V (F1(,Ar) ) ⊆ V (G) \ S2 and V (R1,A∪L) ⊆ V (F1(,Ar)∪L) ⊆

- V (G) \ S2 by Proposition 7.9(ii). Moreover, for all e ∈ R1,A ∪ R1,A∪L, we have |e ∩ S1| ∈ [i − 1] by deﬁnition. Hence, (tr1) holds. Clearly, (C.1) and (†) imply (tr2). Crucially, by (C.1)–(C.3) we have that


- Fˆ1(r) = F1(,Ar)∪L ∪· F2(,Ar) = Tˆ ∪ (S1 ⊎ L) ∪ R1,A∪L ∪ φ(R1,A);
- Fˆ2(r) = F1(,Ar) ∪· F2(,Ar)∪L = Tˆ ∪ (S2 ⊎ L) ∪ R1,A ∪ φ(R1,A∪L).


Thus, (tr3) is satisﬁed. Finally, |V (Tˆ ∪ R1,A ∪ R1,A∪L)| ≤ |V (G′)| ≤ 2µn, proving the claim.

−

The transformer Tˆ almost has the required properties, except that to satisfy (TR2) we would have needed R1,A∪L and φ(R1,A∪L) to be on the ‘other side’ of the transformation. In order to resolve this, we carry out an additional transformation step. (Since R1,A and R1,A∪L are empty if i = 1, this additional step is vacuous in this case.)

Claim 2: There exist T′,R′ ⊆ G(r) and 1-well separated F-packings F1′,F2′ in G − Fˆ1≤(r+1) − Fˆ2≤(r+1) such that the following hold:

- (tr1′) V (R′) ⊆ V (G) \ S2 and |e ∩ S1| ∈ [i − 1] for all e ∈ R′;
- (tr2′) T′, R′, φ(R′), Tˆ, S1 ⊎ L, S2 ⊎ L, R1,A, φ(R1,A), R1,A∪L, φ(R1,A∪L) are pairwise edgedisjoint r-graphs;
- (tr3′) F1′(r) = T′ ∪ R1,A∪L ∪ R′ and F2′(r) = T′ ∪ φ(R1,A∪L) ∪ φ(R′);
- (tr4′) |V (T′ ∪ R′)| ≤ 0.7γn.


Proof of claim: Let H′ := Tˆ ∪ R1,A ∪ φ(R1,A) ∪ (S1 ⊎ L) ∪ (S2 ⊎ L). Clearly, ∆(H′) ≤ 5µn.

Let W := V (R1,A∪L) ∪ V (φ(R1,A∪L)). By (tr4), we have that |W| ≤ 4µn. Similarly to the beginning of the proof of Claim 1, by Corollary A.9 and Lemma A.5(i), there exists a

subset U′ ⊆ V (G) with 0.4γn ≤ |U′| ≤ 0.6γn such that G′′′ := G[U′ ∪ W] is a (2ε,ξ − ε,f,r)supercomplex. Let n˜ := |U′ ∪ W|. Note that

√µn˜ and ∆(Fˆj≤(r+1)) ≤ κ(f − r) for j ∈ [2] by Fact 4.3(i). Thus, by Proposition 4.5(v),

∆(H′) ≤ 5µn ≤

![image 89](<2017-glock-hypergraph-designs-arbitrary_images/imageFile89.png>)

G˜ := G′′′ − H′ − Fˆ1≤(r+1) − Fˆ2≤(r+1) is still a (3ε,ξ − 2ε,f,r)-supercomplex. For every e ∈ R1,A∪L, let

Qe := {Q ∈ G˜(f)(e) ∩ G˜(f)(φ(e)) : Q ∩ (S1 ∪ S2) = ∅}.

By Fact A.2, for every e ∈ R1,A∪L ⊆ G˜(r), we have that |G˜(f)(e) ∩ G˜(f)(φ(e))| ≥ 0.5ξn˜f−r. Thus, we have that |Qe| ≥ 0.4ξn˜f−r. Since ∆(R1,A∪L ∪φ(R1,A∪L)) ≤ 4µn ≤

√µn˜, we can apply Lemma A.10 (with |R1,A∪L|,2,{e,φ(e)},Qe playing the roles of m,s,Lj,Qj) to ﬁnd for every e ∈ R1,A∪L some Qe ∈ Qe such that, writing Ke := (Qe ⊎ {e,φ(e)})≤, we have that

![image 90](<2017-glock-hypergraph-designs-arbitrary_images/imageFile90.png>)

- (C.4) Ke and Ke′ are r-disjoint for distinct e,e′ ∈ R1,A∪L.

For each e ∈ R1,A∪L, let F˜e,1 and F˜e,2 be copies of F with V (F˜e,1) = e∪Qe and V (F˜e,2) = φ(e)∪Qe and such that e ∈ F˜e,1 and φ(F˜e,1) = F˜e,2. Clearly, we have that φ(e) ∈ F˜e,2. Moreover, since e ⊆ V (R1,A∪L) ⊆ V (G) \ S2 by (tr1) and Qe ∩ (S1 ∪ S2) = ∅, we have V (F˜e,1) ⊆ V (G) \ S2. Let

- (C.5) F1′ := {F˜e,1 : e ∈ R1,A∪L};
- (C.6) F2′ := {F˜e,2 : e ∈ R1,A∪L}.

By (C.4), F1′ and F2′ are both 1-well separated F-packings in G˜ ⊆ G − Fˆ1≤(r+1) − Fˆ2≤(r+1). Moreover, V (F1′(r)) ⊆ V (G) \ S2 and φ(F1′(r)) = F2′(r). Let

- (C.7) T′ := F1′(r) ∩ F2′(r);
- (C.8) R′ := F1′(r) − T′ − R1,A∪L.

We clearly have T′,R′ ⊆ G(r) and now check (tr1′)–(tr4′). Note that no edge of T′ intersects

S1 ∪ S2. For (tr1′), we ﬁrst have that V (R′) ⊆ V (F1′(r)) ⊆ V (G) \ S2. Now, consider e′ ∈ R′. There exists e ∈ R1,A∪L with e′ ∈ F˜e,1 and thus e′ ⊆ e ∪ Qe. If we had e′ ∩ S1 = ∅, then e′ ⊆ (e \ S1) ∪ Qe. Since φ(F˜e,1) = F˜e,2, it follows that e′ ∈ T′, a contradiction to (C.8). Hence, |e′ ∩S1| > 0. Moreover, by (tr1) we have |e′ ∩S1| ≤ |(e ∪Qe) ∩S1| = |e ∩S1| ≤ i −1. Therefore, |e′ ∩ S1| ∈ [i − 1] and (tr1′) holds.

In order to check (tr3′), observe ﬁrst that by (C.8) and (C.5), we have F1′(r) = T′∪· R1,A∪L∪· R′. Hence, by Fact 7.7(ii), we have

- (C.9) F2′(r) = φ(F1′(r)) = φ(T′) ∪· φ(R1,A∪L) ∪· φ(R′) = T′ ∪· φ(R1,A∪L) ∪· φ(R′),


so (tr3′) is satisﬁed.

We now check (tr2′). Note that T′,R′,φ(R′) ⊆ G˜(r) ⊆ G(r) − H′. Thus, by (tr2), it is enough to check that T′,R′,φ(R′),R1,A∪L,φ(R1,A∪L) are pairwise edge-disjoint. Recall that no edge of T′ intersects S1 ∪ S2. Moreover, for every e ∈ R′ ∪ R1,A∪L, we have |e ∩ S1| ∈ [i − 1] and e∩S2 = ∅, and for every e ∈ φ(R′)∪φ(R1,A∪L), we have |e∩S2| ∈ [i−1] and e∩S1 = ∅. Since R′ and R1,A∪L are edge-disjoint by (C.8) and φ(R′) and φ(R1,A∪L) are edge-disjoint by (C.9), this implies that T′,R′,φ(R′),R1,A∪L,φ(R1,A∪L) are indeed pairwise edge-disjoint, proving (tr2′).

Finally, we can easily check that |V (T′ ∪ R′)| ≤ n˜ ≤ 0.7γn. −

We now combine the results of Claims 1 and 2. Let T := Tˆ ∪ R1,A∪L ∪ φ(R1,A∪L) ∪ T′; R := R1,A ∪ R′;

- F1 := Fˆ1 ∪ F2′;
- F2 := Fˆ2 ∪ F1′.


Clearly, (tr1) and (tr1′) imply that (TR1) holds. Moreover, (tr2′) implies that T is edge-disjoint from both (S1 ⊎ L) ∪ φ(R) and (S2 ⊎ L) ∪ R. Using (tr3) and (tr3′), observe that

T ∪ (S1 ⊎ L) ∪ φ(R) = Tˆ ∪ R1,A∪L ∪ φ(R1,A∪L) ∪ T′ ∪ (S1 ⊎ L) ∪ φ(R1,A) ∪ φ(R′)

= (Tˆ ∪ (S1 ⊎ L) ∪ R1,A∪L ∪ φ(R1,A)) ∪· (T′ ∪ φ(R1,A∪L) ∪ φ(R′))

= Fˆ1(r) ∪· F2′(r) = F1(r). Similarly, F2(r) = Fˆ2(r) ∪· F1′(r) = T ∪ (S2 ⊎ L) ∪ R. In particular, by Fact 4.3(ii) we can see

- that F1 and F2 are (κ + 1)-well separated F-packings in G. Thus, T is a (κ + 1)-well separated ((S1⊎L)∪φ(R),(S2⊎L)∪R;F)-transformer in G, so (TR2) holds. Finally, we have |V (T ∪R)| ≤ 4µn + 0.7γn ≤ γn by (tr4) and (tr4′).


So far, our maps φ: S1 → S2 were bijections. When φ is an edge-bijective homomorphism from H to H′, φ is in general not injective. In order to still have a meaningful notion of ‘mirroring’

- as before, we introduce the following notation. Deﬁnition C.2. Let V be a set and let V1,V2 be disjoint subsets of V , and let φ: V1 → V2 be


- a map. For a set S ⊆ V \ V2, deﬁne φ(S) := (S \ V1) ∪ φ(S ∩ V1). Let r ∈ N and suppose that


- R is an r-graph with V (R) ⊆ V and i ∈ [r]0. We say that R is (φ,V,V1,V2,i)-projectable if the following hold:


- (Y1) for every e ∈ R, we have that e ∩ V2 = ∅ and |e ∩ V1| ∈ [i] (so if i = 0, then R must be empty since [0] = ∅);
- (Y2) for every e ∈ R, we have |φ(e)| = r;
- (Y3) for every two distinct edges e,e′ ∈ R, we have φ(e) = φ(e′).


Note that if φ is injective and e ∩ V2 = ∅ for all e ∈ R, then (Y2) and (Y3) always hold. If

- R is (φ,V,V1,V2,i)-projectable, then let φ(R) be the r-graph on φ(V (R) \ V2) with edge set {φ(e) : e ∈ R}. For an r-graph P with V (P) ⊆ V \V2 that satisﬁes (Y2), let Pφ be the r-graph on V (P) ∪ V1 that consists of all e ∈ V \rV2 such that φ(e) = φ(e′) for some e′ ∈ P.


The following facts are easy to see.

- Proposition C.3 ([12]). Let V,V1,V2,φ,R,r,i be as above and assume that R is (φ,V,V1,V2,i)projectable. Then the following hold:


- (i) R φ(R);
- (ii) every subgraph of R is (φ,V,V1,V2,i)-projectable;
- (iii) for all e′ ∈ φ(R), we have e′ ∩ V1 = ∅ and |e′ ∩ V2| ∈ [i];
- (iv) assume that for all e ∈ R, we have |e ∩ V1| = i, and let S contain all S ∈ Vi1 such that S is contained in some edge of R, then


R =

˙

(S ⊎ R(S)) and φ(R) =

S∈S

˙

(φ(S) ⊎ R(S)).

S∈S

We can now prove the Transforming lemma by combining many localised transformers.

- Proof of Lemma 7.5. We can assume that 1/κ ≪ γ ≪ 1/h,ε. Choose new constants κ′ ∈ N and γ2,... ,γr,γ2′ ... ,γr′ > 0 such that


1/n ≪ 1/κ ≪ γr ≪ γr′ ≪ γr−1 ≪ γr′−1 ≪ ··· ≪ γ2 ≪ γ2′ ≪ γ ≪ 1/κ′,1/h,ε ≪ ξ,1/f.

Let φ: V (H) → V (H′) be an edge-bijective homomorphism from H to H′. Extend φ as in

Deﬁnition C.2 with V (H),V (H′) playing the roles of V1,V2. Since φ is edge-bijective, we have that

- (C.10) φ↾S is injective whenever S ⊆ e for some e ∈ H.

For every e ∈ H, we have |G(f)(e) ∩ G(f)(φ(e))| ≥ 0.5ξnf−r by Fact A.2. It is thus easy to ﬁnd for each e ∈ H some Qe ∈ G(f)(e) ∩ G(f)(φ(e)) with Qe ∩ (V (H) ∪ V (H′)) = ∅ such that Qe ∩ Qe′ = ∅ for all distinct e,e′ ∈ H. For each e ∈ H, let F˜e,1 and F˜e,2 be copies of F with V (F˜e,1) = e ∪ Qe and V (F˜e,2) = φ(e) ∪ Qe and such that e ∈ F˜e,1 and φ(F˜e,1) = F˜e,2. Clearly, we have that φ(e) ∈ F˜e,2. For j ∈ [2], deﬁne Fr,j∗ := {F˜e,j : e ∈ H}. Clearly, Fr,∗1 and Fr,∗2 are both 1-well separated F-packings in G. Deﬁne

- (C.11) Tr∗ := Fr,∗(1r) ∩ Fr,∗(2r), Rr∗ := Fr,∗(1r) − Tr∗ − H.


Let γ1 := γ. Furthermore, let κr := 1 and recursively deﬁne κi := κi+1+ hi κ′ for all i ∈ [r−1]. Given i ∈ [r − 1]0 and Ti∗+1,Ri∗+1,Fi∗+1,1,Fi∗+1,2, we deﬁne the following conditions:

- (TR1∗)i Ri∗+1 is (φ,V (G),V (H),V (H′),i)-projectable;
- (TR2∗)i Ti∗+1,Ri∗+1,φ(Ri∗+1),H,H′ are edge-disjoint subgraphs of G(r);
- (TR3∗)i Fi∗+1,1 and Fi∗+1,2 are κi+1-well separated F-packings in G with Fi∗+1(r),1 = Ti∗+1 ∪H ∪Ri∗+1 and Fi∗+1(r),2 = Ti∗+1 ∪ H′ ∪ φ(Ri∗+1);
- (TR4∗)i |V (Ti∗+1 ∪ Ri∗+1)| ≤ γi+1n.


We will ﬁrst show that the above choices of Tr∗,Rr∗,Fr,∗1,Fr,∗2 satisfy (TR1∗)r−1–(TR4∗)r−1. We will then proceed inductively until we obtain T1∗,R1∗,F1∗,1,F1∗,2 satisfying (TR1∗)0–(TR4∗)0, which will then easily complete the proof.

Claim 1: Tr∗,Rr∗,Fr,∗1,Fr,∗2 satisfy (TR1∗)r−1–(TR4∗)r−1.

Proof of claim: (TR4∗)r−1 clearly holds. To see (TR1∗)r−1, consider any e′ ∈ Rr∗. There exists e ∈ H such that e′ ∈ F˜e,1. In particular, e′ ⊆ e ∪ Qe. If e′ ⊆ V (H), then e′ = e ∈ H, and if e′ ∩ V (H) = ∅, then e′ ∈ F˜e,2 since φ(F˜e,1) = F˜e,2 and thus e′ ∈ Tr∗. Hence, by deﬁnition of Rr∗, we must have |e′ ∩ V (H)| ∈ [r − 1]. Clearly, e′ ∩ V (H′) ⊆ (e ∪ Qe) ∩ V (H′) = ∅, so (Y1) holds. Moreover, e′ ∩V (H) ⊆ e, so φ↾e′∩V(H) is injective by (C.10), and (Y2) holds. Let e′,e′′ ∈ Rr∗ and suppose that φ(e′) = φ(e′′). We thus have e′\V (H) = e′′\V (H) = ∅. Since the Qe’s were chosen to be vertex-disjoint, we must have e′,e′′ ⊆ e ∪ Qe for some e ∈ H. Hence, (e′ ∪ e′′) ∩ V (H) ⊆ e and so φ↾(e′∪e′′)∩V (H) is injective by (C.10). Since φ(e′ ∩ V (H)) = φ(e′′ ∩ V (H)) by assumption, we have e′ ∩ V (H) = e′′ ∩ V (H), and thus e′ = e′′. Altogether, (Y3) holds, so (TR1∗)r−1 is satisﬁed. In particular, φ(Rr∗) is well-deﬁned. Observe that

φ(Rr∗) = Fr,∗(2r) − Tr∗ − H′.

Clearly, Tr∗,Rr∗,φ(Rr∗),H,H′ are subgraphs of G(r). Using Proposition C.3(iii), it is easy to see that they are indeed edge-disjoint, so (TR2∗) holds. Moreover, note that Fr,∗1 and Fr,∗2 are 1-well separated F-packings in G with Fr,∗(1r) = Tr∗ ∪ H ∪ Rr∗ and Fr,∗(2r) = Tr∗ ∪ H′ ∪ φ(Rr∗), so Tr∗ satisﬁes (TR3∗)r−1. −

Suppose that for some i ∈ [r − 1], we have already found Ti∗+1,Ri∗+1,Fi∗+1,1,Fi∗+1,2 such that

(TR1∗)i–(TR4∗)i hold. We will now ﬁnd Ti∗,Ri∗,Fi,∗1,Fi,∗2 such that (TR1∗)i−1–(TR4∗)i−1 hold. To this end, let

Ri := {e ∈ Ri∗+1 : |e ∩ V (H)| = i}.

- By Proposition C.3(ii), Ri is (φ,V (G),V (H),V (H′),i)-projectable. Let Si be the set of all


- S ∈ V(iH) such that S is contained in some edge of Ri. For each S ∈ Si, let LS := Ri(S). By


Proposition C.3(iv), we have that Ri =

˙

˙

- (C.12) (φ(S) ⊎ LS).


(S ⊎ LS) and φ(Ri) =

S∈Si

S∈Si

We intend to apply Lemma C.1 to each pair S,φ(S) with S ∈ Si individually. For each S ∈ Si, deﬁne

VS := (V (G) \ (V (H) ∪ V (H′))) ∪ S ∪ φ(S). Claim 2: For every S ∈ Si, LS ⊆ G[VS](S)(r−i) ∩ G[VS](φ(S))(r−i) and |V (LS)| ≤ 1.1γi+1|VS|.

Proof of claim: The second assertion clearly holds by (TR4∗)i. To see the ﬁrst one, let e′ ∈ LS = Ri(S). Since Ri ⊆ Ri∗+1 ⊆ G(r), we have e′ ∈ G(S)(r−i). Moreover, φ(S) ∪ e′ ∈ φ(Ri) ⊆ φ(Ri∗+1) ⊆ G(r) by (C.12). Since Ri∗+1 is (φ,V (G),V (H),V (H′),i)-projectable, we have that e′ ∩ (V (H) ∪ V (H′)) = ∅. Thus, S ∪ e′ ⊆ VS and φ(S) ∪ e′ ⊆ VS. −

Let S∗ ∈ V (iF) be such that F(S∗) is non-empty. Claim 3: For every S ∈ Si, LS is F(S∗)-divisible.

Proof of claim: Consider b ⊆ V (LS) with |b| < r − i. We have to check that Deg(F(S∗))|b| | |LS(b)|. By (TR3∗)i, both Ti∗+1 ∪ H ∪ Ri∗+1 and Ti∗+1 ∪ H′ ∪ φ(Ri∗+1) are necessarily F-divisible. Clearly, H′ does not contain an edge that contains S. Note that by (TR1∗)i and Proposition C.3(iii), φ(Ri∗+1) does not contain an edge that contains S either, hence |Ti∗+1(S ∪ b)| = |(Ti∗+1 ∪ H′ ∪ φ(Ri∗+1))(S ∪ b)| ≡ 0 mod Deg(F)|S∪b|. Moreover, since H is F-divisible, we have |(Ti∗+1 ∪ Ri∗+1)(S ∪ b)| ≡ |(Ti∗+1 ∪ H ∪ Ri∗+1)(S ∪ b)| ≡ 0 mod Deg(F)|S∪b|. Thus, we have Deg(F)|S∪b| | |Ri∗+1(S ∪ b)|. Moreover, |Ri∗+1(S ∪ b)| = |Ri(S ∪ b)| = |LS(b)|. Hence, Deg(F)|S∪b| | |LS(b)|, which proves the claim as Deg(F)|S∪b| = Deg(F(S∗))|b| by Proposition 4.2. −

We now intend to apply Lemma C.1 for every S ∈ Si in order to deﬁne TS,RS ⊆ G(r) and κ′-well separated F-packings FS,1,FS,2 in G such that the following hold:

- (TR1′) RS is (φ,V (G),V (H),V (H′),i − 1)-projectable;
- (TR2′) TS,RS,φ(RS),S ⊎ LS,φ(S) ⊎ LS are edge-disjoint;
- (TR3′) FS,(r1) = TS ∪ (S ⊎ LS) ∪ φ(RS) and FS,(r2) = TS ∪ (φ(S) ⊎ LS) ∪ RS;
- (TR4′) |V (TS ∪ RS)| ≤ γi′+1n. We also need to ensure that all these graphs and packings satisfy several ‘disjointness properties’ (see (a)–(c)), and we will therefore choose them successively. Recall that Pφ (for a given r-graph P) was deﬁned in Deﬁnition C.2. Let S′ ⊆ Si be the set of all S′ ∈ Si for which TS′,RS′ and FS′,1,FS′,2 have already been deﬁned such that (TR1′)–(TR4′) hold. Suppose that next we want to ﬁnd TS, RS, FS,1 and FS,2. Let


PS := Ri∗+1 ∪

RS′,

S′∈S′

MS := Ti∗+1 ∪ Ri∗+1 ∪ φ(Ri∗+1) ∪

(TS′ ∪ RS′ ∪ φ(RS′)),

S′∈S′

OS := Fi∗≤+1(,r1+1) ∪ Fi∗≤+1(,r2+1) ∪

FS≤′(,1r+1) ∪ FS≤′(,2r+1),

S′∈S′

GS := G[VS] − ((MS ∪ PSφ) − ((S ⊎ LS) ∪ (φ(S) ⊎ LS))) − OS. Observe that (TR4∗)i and (TR4′) imply that

|V (MS ∪ PS)| ≤ |V (Ti∗+1 ∪ Ri∗+1 ∪ φ(Ri∗+1))| +

S′∈S′

- h
- i


γi′+1n ≤ γin.

≤ 2γi+1n + 2

|V (TS′ ∪ RS′ ∪ φ(RS′))|

In particular, |V (PSφ)| ≤ |V (PS) ∪ V (H)| ≤ γin + h. Moreover, by Fact 4.3(i), (TR3∗)i and

- (TR3′), we have that ∆(OS) ≤ (2κi+1 + 2 hi κ′)(f − r). Thus, by Proposition 4.5(v) GS is still a (2ε,ξ/2,f,r)-supercomplex. Moreover, note that LS ⊆ GS(S)(r−i) ∩ GS(φ(S))(r−i) and |V (LS)| ≤ 1.1γi+1|VS| by Claim 2 and that LS is F(S∗)-divisible by Claim 3.

Finally, by deﬁnition of Si, S is contained in some e ∈ Ri. Since Ri satisﬁes (Y2) by (TR1∗)i, we know that φ↾e is injective. Thus, φ↾S : S → φ(S) is a bijection. We can thus apply Lemma C.1 with the following objects/parameters:

object/parameter GS i S φ(S) φ↾S LS 1.1γi+1 γi′+1 2ε |VS| ξ/2 f r F S∗ κ′/2 playing the role of G i S1 S2 φ L γ′ γ ε n ξ f r F S∗ κ

![image 91](<2017-glock-hypergraph-designs-arbitrary_images/imageFile91.png>)

![image 92](<2017-glock-hypergraph-designs-arbitrary_images/imageFile92.png>)

![image 93](<2017-glock-hypergraph-designs-arbitrary_images/imageFile93.png>)

![image 94](<2017-glock-hypergraph-designs-arbitrary_images/imageFile94.png>)

![image 95](<2017-glock-hypergraph-designs-arbitrary_images/imageFile95.png>)

![image 96](<2017-glock-hypergraph-designs-arbitrary_images/imageFile96.png>)

![image 97](<2017-glock-hypergraph-designs-arbitrary_images/imageFile97.png>)

![image 98](<2017-glock-hypergraph-designs-arbitrary_images/imageFile98.png>)

![image 99](<2017-glock-hypergraph-designs-arbitrary_images/imageFile99.png>)

![image 100](<2017-glock-hypergraph-designs-arbitrary_images/imageFile100.png>)

![image 101](<2017-glock-hypergraph-designs-arbitrary_images/imageFile101.png>)

![image 102](<2017-glock-hypergraph-designs-arbitrary_images/imageFile102.png>)

![image 103](<2017-glock-hypergraph-designs-arbitrary_images/imageFile103.png>)

![image 104](<2017-glock-hypergraph-designs-arbitrary_images/imageFile104.png>)

![image 105](<2017-glock-hypergraph-designs-arbitrary_images/imageFile105.png>)

![image 106](<2017-glock-hypergraph-designs-arbitrary_images/imageFile106.png>)

![image 107](<2017-glock-hypergraph-designs-arbitrary_images/imageFile107.png>)

![image 108](<2017-glock-hypergraph-designs-arbitrary_images/imageFile108.png>)

![image 109](<2017-glock-hypergraph-designs-arbitrary_images/imageFile109.png>)

![image 110](<2017-glock-hypergraph-designs-arbitrary_images/imageFile110.png>)

![image 111](<2017-glock-hypergraph-designs-arbitrary_images/imageFile111.png>)

![image 112](<2017-glock-hypergraph-designs-arbitrary_images/imageFile112.png>)

![image 113](<2017-glock-hypergraph-designs-arbitrary_images/imageFile113.png>)

![image 114](<2017-glock-hypergraph-designs-arbitrary_images/imageFile114.png>)

![image 115](<2017-glock-hypergraph-designs-arbitrary_images/imageFile115.png>)

![image 116](<2017-glock-hypergraph-designs-arbitrary_images/imageFile116.png>)

![image 117](<2017-glock-hypergraph-designs-arbitrary_images/imageFile117.png>)

![image 118](<2017-glock-hypergraph-designs-arbitrary_images/imageFile118.png>)

![image 119](<2017-glock-hypergraph-designs-arbitrary_images/imageFile119.png>)

![image 120](<2017-glock-hypergraph-designs-arbitrary_images/imageFile120.png>)

![image 121](<2017-glock-hypergraph-designs-arbitrary_images/imageFile121.png>)

![image 122](<2017-glock-hypergraph-designs-arbitrary_images/imageFile122.png>)

![image 123](<2017-glock-hypergraph-designs-arbitrary_images/imageFile123.png>)

This yields TS,RS ⊆ G(Sr) and κ′/2-well separated F-packings FS,1,FS,2 such that (TR2′)–

- (TR4′) hold, V (RS) ⊆ V (GS) \ φ(S) and |e ∩ S| ∈ [i − 1] for all e ∈ RS. Note that the latter implies that RS is (φ,V (G),V (H),V (H′),i − 1)-projectable as V (H) ∩ V (GS) = S and


- V (H′) ∩ V (GS) = φ(S), so (TR1′) holds as well. Moreover, using (TR2∗)i and (TR2′) it is easy to see that our construction ensures that


- (a) H,H′,Ti∗+1,Ri∗+1,φ(Ri∗+1),(TS)S∈Si,(RS)S∈Si,(φ(RS))S∈Si are pairwise edge-disjoint;
- (b) for all distinct S,S′ ∈ Si and all e ∈ RS, e′ ∈ RS′, e′′ ∈ Ri∗+1 − Ri we have that φ(e), φ(e′) and φ(e′′) are pairwise distinct;
- (c) for any j,j′ ∈ [2] and all distinct S,S′ ∈ Si, FS,j is (r +1)-disjoint from Fi∗+1,j′ and from FS′,j′.


Indeed, (a) holds by the choice of MS, (b) holds by deﬁnition of PSφ, and (c) holds by deﬁnition of OS. Let

Ti∗ := Ti∗+1 ∪ Ri ∪ φ(Ri) ∪

TS;

S∈Si

Ri∗ := (Ri∗+1 − Ri) ∪

RS;

S∈Si

- Fi,∗1 := Fi∗+1,1 ∪ S∈Si

FS,2;

- Fi,∗2 := Fi∗+1,2 ∪ S∈Si


FS,1.

Using (TR3∗)i, (TR3′), (a) and (C.12), it is easy to check that both Fi,∗1 and Fi,∗2 are F-packings in G. We check that (TR1∗)i−1–(TR4∗)i−1 hold. Using (TR4∗)i and (TR4′), we can conﬁrm that

|V (Ti∗ ∪ Ri∗)| ≤ |V (Ti∗+1 ∪ Ri∗+1 ∪ φ(Ri∗+1))| +

≤ 2γi+1n +

- h
- i


γi′+1n ≤ γin,

|V (TS ∪ RS)|

S∈Si

so (TR4∗)i−1 holds.

In order to check (TR1∗)i−1, i.e. that Ri∗ is (φ,V (G),V (H),V (H′),i − 1)-projectable, note that (Y1) and (Y2) hold by (TR1∗)i, the deﬁnition of Ri and (TR1′). Moreover, (Y3) is implied by (TR1∗)i, (TR1′) and (b).

Moreover, (TR2∗)i−1 follows from (a). Finally, we check (TR3∗)i−1. Observe that Ti∗ ∪ H ∪ Ri∗ = Ti∗+1 ∪ Ri ∪ φ(Ri) ∪

TS ∪ H ∪ (Ri∗+1 − Ri) ∪

RS

S∈Si

S∈Si

(C.12= ) (Ti∗+1 ∪ H ∪ Ri∗+1) ∪

(TS ∪ (φ(S) ⊎ LS) ∪ RS),

S∈Si

Ti∗ ∪ H′ ∪ φ(Ri∗) = Ti∗+1 ∪ Ri ∪ φ(Ri) ∪

TS ∪ H′ ∪ (φ(Ri∗+1) − φ(Ri)) ∪

φ(RS)

S∈Si

S∈Si

(C.12= ) (Ti∗+1 ∪ H′ ∪ φ(Ri∗+1)) ∪

(TS ∪ (S ⊎ LS) ∪ φ(RS)).

S∈Si

Thus, by (TR3∗)i and (TR3′), Fi,∗1 is an F-decomposition of Ti∗ ∪ H ∪ Ri∗ and Fi,∗2 is an Fdecomposition of Ti∗ ∪ H′ ∪ φ(Ri∗). Moreover, by (c) and Fact 4.3(ii), Fi,∗1 and Fi,∗2 are both (κi+1 + hi κ′)-well separated in G. Since κi+1 + hi κ′ = κi, this establishes (TR3∗)i−1.

Finally, let T1∗,R1∗,F1∗,1,F1∗,2 satisfy (TR1∗)0–(TR4∗)0. Note that R1∗ is empty by (TR1∗)0 and (Y1). Moreover, T1∗ ⊆ G(r) is edge-disjoint from H and H′ by (TR2∗)0 and ∆(T1∗) ≤ γ1n by (TR4∗)0. Most importantly, F1∗,1 and F1∗,2 are κ1-well separated F-packings in G with

F1∗,(1r) = T1∗∪H and F1∗,(2r) = T1∗∪H′ by (TR3∗)0. Therefore, T1∗ is a κ1-well separated (H,H′;F)transformer in G with ∆(T1∗) ≤ γ1n. Recall that γ1 = γ and note that κ1 ≤ 2hκ′ ≤ κ. Thus, T1∗ is the desired transformer.

Appendix D. Covering down

Here, we prove the Cover down lemma (Lemma 6.9). Our proof proceeds by induction on the ‘type’ of the edges to be covered. In order to carry out the induction step we will actually prove a signiﬁcantly stronger result, the ‘Cover down lemma for setups’ (Lemma D.21), from which Lemma 6.9 immediately follows. In each step, some edges will be covered via an inductive argument, and the remaining ones via the ‘Localised cover down lemma’ (Lemma D.7).

- D.1. Systems and focuses.


- Deﬁnition D.1. Given i ∈ N0, an i-system in a set V is a collection S of distinct subsets of V of size i. A subset of V is called S-important if it contains some S ∈ S, otherwise we call it

S-unimportant. We say that U = (US)S∈S is a focus for S if for each S ∈ S, US is a subset of V \ S.

- Deﬁnition D.2. Let G be a complex and S an i-system in V (G). We call G r-exclusive with respect to S if every e ∈ G with |e| ≥ r contains at most one element of S. Let U be a focus for

S. If G is r-exclusive with respect to S, the following functions are well-deﬁned: For r′ ≥ r, let Er′ denote the set of S-important r′-sets in G. Deﬁne τr′ : Er′ → [r′ − i]0 as τr′(e) := |e ∩ US|, where S is the unique S ∈ S contained in e. We call τr′ the type function of G(r′), S, U.

- Deﬁnition D.3. Let G be a complex and S an i-system in V (G). Let U be a focus for S and suppose that G is r-exclusive with respect to S. For i′ ∈ {i + 1,... ,r − 1}, we deﬁne T as the


set of all i′-subsets T of V (G) which satisfy S ⊆ T ⊆ e \ US for some S ∈ S and e ∈ G(r). We call T the i′-extension of S in G around U.

Clearly, T is an i′-system in V (G). Moreover, note that for every T ∈ T , there is a unique

- S ∈ S with S ⊆ T because G is r-exclusive with respect to S. We let T↾S := S denote this element. (On the other hand, we may have |T | < |S|.) Note that U′ := {UT↾S : T ∈ T } is a focus for T as T ∩ UT↾S = ∅ for all T ∈ T .


The following proposition contains some basic properties of i′-extensions, which are straightforwardly checked using the deﬁnitions (see also Step 1 in the proof of Lemma 10.22 in [12]).

- Proposition D.4. Let 0 ≤ i < i′ < r. Let G be a complex and S an i-system in V (G). Let U be a focus for S and suppose that G is r-exclusive with respect to S. Let T be the i′-extension


of S in G around U. For r′ ≥ r, let τr′ be the type function of G(r′), S, U. Then the following hold for

G′ := G − {e ∈ G(r) : e is S-important and τr(e) < r − i′} :

- (i) G′ is r-exclusive with respect to T ;
- (ii) for all e ∈ G with |e| ≥ r, we have e ∈/ G′ ⇔ e is S-important and τ|e|(e) < |e| − i′;
- (iii) for r′ ≥ r, the T -important elements of G′(r′) are precisely the elements of τr−′1(r′ − i′).


Let Zr,i be the set of all quadruples (z0,z1,z2,z3) ∈ N40 such that z0 + z1 < i, z0 + z3 < i and z0 + z1 + z2 + z3 = r. Clearly, |Zr,i| ≤ (r + 1)3, and Zr,i = ∅ if i = 0.

Deﬁnition D.5. Let V be a set of size n, let S be an i-system in V and let U be a focus for S. We say that U is a µ-focus for S if each US ∈ U has size µn ± n2/3. For all S ∈ S, z = (z0,z1,z2,z3) ∈ Zr,i and all (z1 + z2 − 1)-sets b ⊆ V \ S, deﬁne

JS,zb := {S′ ∈ S : |S ∩ S′| = z0,b ⊆ S′ ∪ US′,|US′ ∩ S| ≥ z3}, JS,z,b 1 := {S′ ∈ JS,zb : |b ∩ S′| = z1}, JS,z,b 2 := {S′ ∈ JS,zb : |b ∩ S′| = z1 − 1,|US ∩ (S′ \ b)| ≥ 1}.

We say that U is a (ρsize,ρ,r)-focus for S if

- (F1) each US has size ρsizeρn ± n2/3;
- (F2) |US ∩ US′| ≤ 2ρ2n for distinct S,S′ ∈ S;
- (F3) for all S ∈ S, z = (z0,z1,z2,z3) ∈ Zr,i and (z1 + z2 − 1)-sets b ⊆ V \ S, we have


- |JS,z,b 1| ≤ 26rρz2+z3−1ni−z0−z1,
- |JS,z,b 2| ≤ 29rρz2+z3+1ni−z0−z1+1.


The sets S′ in JS,z,b 1 and JS,z,b 2 are those which may give rise to interference when covering the edges containing S. (F3) ensures that there are not too many of them. The next lemma states that a suitable random choice of the US yields a (ρsize,ρ,r)-focus.

- Lemma D.6 ([12]). Let 1/n ≪ ρ ≪ ρsize,1/r and i ∈ [r − 1]. Let V be a set of size n, let S be an i-system in V and let U′ = (US′ )S∈S be a ρsize-focus for S. Let U = (US)S∈S be a random focus obtained as follows: independently for all pairs S ∈ S and x ∈ US′ , retain x in US with probability ρ. Then whp U is a (ρsize,ρ,r)-focus for S.


The following ‘Localised cover down lemma’ allows us to simultaneously cover all S-important edges of an i-system S provided that the associated focus U satisﬁes (F1)–(F3) and all Simportant edges are ‘localised’ in the sense that their links are contained in the respective focus set (or, equivalently, their type is maximal).

Lemma D.7 (Localised cover down lemma). Let 1/n ≪ ρ ≪ ρsize,ξ,1/f and 1 ≤ i < r < f. Assume that (∗)r−i is true. Let F be a weakly regular r-graph on f vertices and S∗ ∈ V (iF) such that F(S∗) is non-empty. Let G be a complex on n vertices and let S = {S1,... ,Sp} be an i-system in G such that G is r-exclusive with respect to S. Let U = {U1,... ,Up} be a (ρsize,ρ,r)focus for S. Suppose further that whenever Sj ⊆ e ∈ G(r), we have e \ Sj ⊆ Uj. Finally, assume that G(Sj)[Uj] is an F(S∗)-divisible (ρ,ξ,f − i,r − i)-supercomplex for all j ∈ [p].

Then there exists a ρ−1/12-well separated F-packing F in G covering all S-important r-edges. Proof. Recall that by Proposition 4.2, F(S∗) is a weakly regular (r − i)-graph. We will use (∗)r−i together with Corollary A.4 in order to ﬁnd many F(S∗)-decompositions of G(Sj)[Uj] and then pick one of these at random. Let t := ρ1/6(0.5ρρsizen)f−r and κ := ρ−1/12. For all

j ∈ [p], deﬁne Gj := G(Sj)[Uj]. Consider Algorithm D.8 which, if successful, outputs a κ-well separated F(S∗)-decomposition Fj of Gj for every j ∈ [p].

![image 124](<2017-glock-hypergraph-designs-arbitrary_images/imageFile124.png>)

Algorithm D.8 for j from 1 to p do

![image 125](<2017-glock-hypergraph-designs-arbitrary_images/imageFile125.png>)

for all z = (z0,z1,z2,z3) ∈ Zr,i, deﬁne Tzj as the (z1 + z2)-graph on Uj containing all Z1 ∪· Z2 ⊆ Uj with |Z1| = z1,|Z2| = z2 such that for some j′ ∈ [j − 1] with |Sj ∩ Sj′| = z0 and some K′ ∈ Fj≤′(f−i), we have Z1 ⊆ Sj′, Z2 ⊆ K′ and |K′ ∩ Sj| = z3

if there exist κ-well separated F(S∗)-decompositions Fj,1,... ,Fj,t of Gj− z∈Zr,i Tzj which are pairwise (f − i)-disjoint then

pick s ∈ [t] uniformly at random and let Fj := Fj,s else

return ‘unsuccessful’ end if

end for

![image 126](<2017-glock-hypergraph-designs-arbitrary_images/imageFile126.png>)

Claim 1: If Algorithm D.8 outputs F1,... ,Fp, then F := j∈[p] F˜j is a packing as desired, where F˜j := Sj ⊳ Fj.

Proof of claim: Since z1+z2 > r−i, we have G(jr−i) = (Gj− z∈Zr,i Tzj)(r−i). Hence, Fj is indeed an F(S∗)-decomposition of Gj. Thus, by Proposition 6.11, F˜j is a κ-well separated F-packing in G covering all r-edges containing Sj. Therefore, F covers all S-important r-edges of G. By Fact 4.3(iii) it suﬃces to show that F˜1,... ,F˜p are r-disjoint.

To this end, let j′ < j and suppose, for a contradiction, that there exist K˜ ∈ F˜j≤(f) and K˜′ ∈ F˜j≤′(f) such that |K˜ ∩K˜ ′| ≥ r. Let K := K˜ \Sj and K′ := K˜′ \Sj′. Then K ∈ Fj≤(f−i) and

- K′ ∈ Fj≤′(f−i) and |(Sj ∪ K) ∩ (Sj′ ∪ K′)| ≥ r. Let z0 := |Sj ∩ Sj′| and z3 := |Sj ∩ K′|. Hence, we have |K ∩ (Sj′ ∪ K′)| ≥ r − z0 − z3. Choose X ⊆ K such that |X ∩ (Sj′ ∪ K′)| = r − z0 − z3 and let Z1 := X ∩ Sj′ and Z2 := X ∩ K′. We claim that z := (z0,|Z1|,|Z2|,z3) ∈ Zr,i. Clearly, we have z0 + |Z1| + |Z2| + z3 = r. Furthermore, note that z0 + z3 < i. Indeed, we clearly have z0 + z3 = |Sj ∩ (Sj′ ∪ K′)| ≤ |Sj| = i, and equality can only hold if Sj ⊆ Sj′ ∪ K′ = K˜′, which is impossible since G is r-exclusive. Similarly, we have z0 + |Z1| < i. Thus, z ∈ Zr,i. But this implies that Z1 ∪ Z2 ∈ Tzj, in contradiction to Z1 ∪ Z2 ⊆ K. −


In order to prove the lemma, it is thus suﬃcient to prove that with positive probability, ∆(Tzj) ≤ 22rfκρ1/2|Uj| for all j ∈ [p] and z ∈ Zr,i. Indeed, this would imply that ∆( z∈Z

Tzj) ≤ (r + 1)322rfρ1/2−1/12|Uj|, and by Proposition 4.5(v), Gj − z∈Zr,i Tzj would be a (ρ1/12,ξ/2,f − i,r − i)-supercomplex. By Corollary A.4 and since |Uj| ≥ 0.5ρρsizen, the number of pairwise (f − i)-disjoint κ-well separated F(S∗)-decompositions in Gj − z∈Zr,i Tzj is

r,i

- at least ρ2/12|Uj|(f−i)−(r−i) ≥ t, so the algorithm would succeed. In order to analyse ∆(Tzj), we deﬁne the following variables. Suppose that 1 ≤ j′ < j ≤ p,


′

that z = (z0,z1,z2,z3) ∈ Zr,i and b ⊆ Uj is a (z1 + z2 − 1)-set. Let Y b,j

j,z denote the random indicator variable of the event that each of the following holds:

- (a) there exists some K′ ∈ Fj≤′(f−i) with |K′ ∩ Sj| = z3;
- (b) there exist Z1 ⊆ Sj′, Z2 ⊆ K′ with |Z1| = z1, |Z2| = z2 such that b ⊆ Z1 ∪ Z2 ⊆ Uj;
- (c) |Sj ∩ Sj′| = z0.


We say that v ∈ Uj1\b is a witness for j′ if (a)–(c) hold with Z1 ∪· Z2 = b ∪· v. For all j ∈ [p], z = (z0,z1,z2,z3) ∈ Zr,i and (z1 + z2 − 1)-sets b ⊆ Uj, let Xj,zb := j j′−=11 Yj,zb,j′.

Claim 2: For all j ∈ [p], z = (z0,z1,z2,z3) ∈ Zr,i and (z1 + z2 − 1)-sets b ⊆ Uj, we have |Tzj(b)| ≤ 22rfκXj,zb .

Proof of claim: Let j,z and b be ﬁxed. Clearly, if v ∈ Tzj(b), then by Algorithm D.8, v is a witness for some j′ ∈ [j − 1]. Conversely, we claim that for each j′ ∈ [j − 1], there are at most

′

22rfκ witnesses for j′. Clearly, this would imply that |Tzj(b)| ≤ 22rfκ|{j′ ∈ [j − 1] : Y b,j

j,z =

- 1}| = 22rfκXj,zb .

Fix j′ ∈ [j − 1]. If v is a witness for j′, then there exists Kv ∈ Fj≤′(f−i) such that (a)–(c) hold with Z1∪· Z2 = b∪· v and Kv playing the role of K′. By (b) we must have v ⊆ Z1∪Z2 ⊆ Sj′ ∪Kv. Since |Sj′ ∪ Kv| = f, there are at most f witnesses v′ for j′ such that Kv can play the role of

Kv′. It is thus suﬃcient to show that there are at most 22rκ K′ ∈ Fj≤′(f−i) such that (a)–(c) hold.

Note that for any possible choice of Z1,Z2,K′, we must have |b ∩ Z2| ∈ {z2,z2 − 1} and b ∩ Z2 ⊆ Z2 ⊆ K′ by (b). For any Z2′ ⊆ b with |Z2′| ∈ {z2,z2 − 1} and any Z3 ∈ Szj

3

, there can

be at most κ K′ ∈ Fj≤′(f−i) with Z2′ ⊆ K′ and K′ ∩ Sj = Z3. This is because Fj′ is a κ-well separated F(S∗)-decomposition and |Z2′ ∪Z3| ≥ z2 −1+z3 ≥ r −i. Hence, there can be at most

- 2|b| z i


κ ≤ 22rκ possible choices for K′. − The following claim thus implies the lemma.

3

Claim 3: With positive probability, we have Xj,zb ≤ ρ1/2|Uj| for all j ∈ [p], z = (z0,z1,z2,z3) ∈ Zr,i and (z1 + z2 − 1)-sets b ⊆ Uj. Proof of claim: Fix j,z,b as above. We split Xj,zb into two sums. For this, let

Jj,zb := {j′ ∈ [j − 1] : |Sj ∩ Sj′| = z0,b \ Sj′ ⊆ Uj′,|Uj′ ∩ Sj| ≥ z3},

- Jj,z,b 1 := {j′ ∈ Jj,zb : |b ∩ Sj′| = z1},
- Jj,z,b 2 := {j′ ∈ Jj,zb : |b ∩ Sj′| = z1 − 1,|Uj ∩ (Sj′ \ b)| ≥ 1}.


Since U is a (ρsize,ρ,r)-focus for S, (F3) implies that

- (D.1) |Jj,z,b 1| ≤ 26rρz2+z3−1ni−z0−z1,
- (D.2) |Jj,z,b 2| ≤ 29rρz2+z3+1ni−z0−z1+1.

Note that if Y b,j

′

j,z = 1, then j′ ∈ Jj,z,b 1 ∪ Jj,z,b 2. Hence, we have Xj,zb = Xj,z,b 1 + Xj,z,b 2, where Xj,z,b 1 := j′∈Jj,z,b 1 Y b,j

′

j,z and Xj,z,b 2 := j′∈Jj,z,b 2 Y b,j

′

j,z . We will bound Xj,z,b 1 and Xj,z,b 2 separately.

For j′ ∈ Jj,z,b 1 ∪ Jj,z,b 2, deﬁne

Kj,zb,j′ := {K′ ∈

Uj′ f − i

- (D.3) : b ⊆ Sj′ ∪ K′,|K′ ∩ Uj| ≥ z2,|K′ ∩ Sj| = z3}.


′

′

j,z = 1, then Fj≤′,k(f−i) ∩ Kb,j

Note that if Y b,j

j,z = ∅. Recall that the candidates Fj′,1,... ,Fj′,t in Algorithm D.8 from which Fj′ was chosen at random are (f − i)-disjoint. We thus have

′

′

|{k ∈ [t] : Fj≤′,k(f−i) ∩ Kb,j

|Kb,j

j,z = ∅}| t ≤

j,z | t

′

P(Y b,j

j,z = 1) ≤

.

![image 127](<2017-glock-hypergraph-designs-arbitrary_images/imageFile127.png>)

![image 128](<2017-glock-hypergraph-designs-arbitrary_images/imageFile128.png>)

This upper bound still holds if we condition on variables Yj,zb,j′′, j′′ = j′. We thus need to bound |Kb,j

′

j,z | in order to bound Xj,z,b 1 and Xj,z,b 2. Step 1: Estimating Xj,z,b 1 Consider j′ ∈ Jj,z,b 1. For all K′ ∈ Kb,j

′

j,z , we have b \ Sj′ ⊆ K′ and |b ∩ K′| = |b| − |b ∩ Sj′| = z2 − 1, and the sets b ∩ K′, K′ ∩ Sj, (K′ \ b) ∩ (Uj ∩ Uj′) are disjoint. Moreover, we have |(K′ \ b) ∩ (Uj ∩ Uj′)| = |(K′ \ b) ∩ Uj| ≥ |K′ ∩ Uj| − |b ∩ K′| ≥ 1. We can thus count

|Sj| z3 · |Uj ∩ Uj′| · |Uj′|f−i−(z2−1)−1−z3 ≤ 2i · 2ρ2n · (2ρρsizen)f−i−z2−z3.

′

|Kb,j

j,z | ≤

- Let ρ˜1 := ρz0+z1−i+5/3ρsizen1+z0+z1−i ∈ [0,1]. In order to apply Proposition A.8, let j1,... ,jm be an enumeration of Jj,z,b 1. We then have for all k ∈ [m] and all y1,... ,yk−1 ∈ {0,1} that

P(Yj,zb,jk = 1 | Yj,zb,j1 = y1,... ,Yj,zb,jk−1 = yk−1) ≤

|Kj,zb,jk| t ≤

![image 129](<2017-glock-hypergraph-designs-arbitrary_images/imageFile129.png>)

2i · 2ρ2n · (2ρρsizen)f−i−z2−z3 ρ1/6(0.5ρρsizen)f−r

![image 130](<2017-glock-hypergraph-designs-arbitrary_images/imageFile130.png>)

= 22f−r+1−z2−z3ρ11/6(ρρsize)z0+z1−in1+z0+z1−i ≤ ρ˜1.

- Let B1 ∼ Bin(|Jj,z,b 1|,ρ˜1) and observe that

7EB1 = 7|Jj,z,b 1|ρ˜1

(D.1)

≤ 7 · 26rρz2+z3−1ni−z0−z1 · ρz0+z1−i+5/3ρsizen1+z0+z1−i

= 7 · 26rρr−i+2/3ρsizen ≤ 0.5ρ1/2|Uj|. Thus,

P(Xj,z,b 1 ≥ 0.5ρ1/2|Uj|)

Proposition A.8

≤ P(B1 ≥ 0.5ρ1/2|Uj|)

Lemma A.5(iii)

≤ e−0.5ρ1/2|Uj|.

Step 2: Estimating Xj,z,b 2 Consider j′ ∈ Jj,z,b 2. This time, since |b ∩ Sj′| = z1 − 1, we have |K′ ∩ b| = |b \ Sj′| = z2 for

all K′ ∈ Kj,zb,j′. Thus, we count

|Kb,j

′

j,z | ≤

|Sj| z3 · |Uj′|f−i−z2−z3 ≤ 2i · (2ρρsizen)f−i−z2−z3.

Let ρ˜2 := ρz0+z1−i−1/5ρsizenz0+z1−i ∈ [0,1]. In order to apply Proposition A.8, let j1,... ,jm be an enumeration of Jj,z,f 2. We then have for all k ∈ [m] and all y1,... ,yk−1 ∈ {0,1} that

P(Yj,zb,jk = 1 | Yj,zb,j1 = y1,... ,Yj,zb,jk−1 = yk−1) ≤

|Kj,zb,jk| t ≤

![image 131](<2017-glock-hypergraph-designs-arbitrary_images/imageFile131.png>)

2i · (2ρρsizen)f−i−z2−z3 ρ1/6(0.5ρρsizen)f−r

![image 132](<2017-glock-hypergraph-designs-arbitrary_images/imageFile132.png>)

= 22f−r−z2−z3ρ−1/6(ρρsizen)z0+z1−i ≤ ρ˜2.

- Let B2 ∼ Bin(|Jj,z,b 2|,ρ˜2) and observe that




(D.2)

7EB2 = 7|Jj,z,b 2|ρ˜2

≤ 7 · 29rρz2+z3+1ni−z0−z1+1 · ρz0+z1−i−1/5ρsizenz0+z1−i

= 7 · 29rρr−i+4/5ρsizen ≤ 0.5ρ1/2|Uj|. Thus,

Lemma A.5(iii)

Proposition A.8

≤ e−0.5ρ1/2|Uj|. Hence,

≤ P(B2 ≥ 0.5ρ1/2|Uj|)

P(Xj,z,b 2 ≥ 0.5ρ1/2|Uj|)

P(Xj,zb ≥ ρ1/2|Uj|) ≤ P(Xj,z,b 1 ≥ 0.5ρ1/2|Uj|) + P(Xj,z,b 2 ≥ 0.5ρ1/2|Uj|) ≤ 2e−0.5ρ1/2|Uj|. Since p = |S| ≤ ni, a union bound easily implies Claim 3. −

This completes the proof of Lemma D.7.

- D.2. Partition pairs. We now develop the appropriate framework to be able to state the Cover down lemma for setups (Lemma D.21). Recall that we will consider (and cover) r-sets separately according to their type. The type of an r-set e naturally imposes constraints on the type of an f-set which covers e. We will need to track and adjust the densities of r-sets with respect to f-sets for each pair of types separately. This gives rise to the following concepts of partition pairs and partition regularity (see Section D.3).


Let X be a set. We say that P = (X1,... ,Xa) is an ordered partition of X if the Xi are disjoint subsets of X whose union is X. We let P(i) := Xi and P([i]) := (X1,... ,Xi). If P = (X1,... ,Xa) is an ordered partition of X and X′ ⊆ X, we let P[X′] denote the ordered partition (X1 ∩ X′,... ,Xa ∩ X′) of X′. If {X′,X′′} is a partition of X, P′ = (X1′,... ,Xa′ ) is an ordered partition of X′ and P′′ = (X1′′,... ,Xb′′) is an ordered partition of X′′, we let

P′ ⊔ P′′ := (X1′,... ,Xa′ ,X1′′,... ,Xb′′). Deﬁnition D.9. Let G be a complex and let f > r ≥ 1. An (r,f)-partition pair of G is a pair (Pr,Pf), where Pr is an ordered partition of G(r) and Pf is an ordered partition of G(f), such that for all E ∈ Pr and Q ∈ Pf, every Q ∈ Q contains the same number C(E,Q) of elements from E. We call C : Pr × Pf → [ fr ]0 the containment function of the partition pair. We say that (Pr,Pf) is upper-triangular if C(Pr(ℓ),Pf(k)) = 0 whenever ℓ > k.

C(E,Q) = fr . If (Pr,Pf) is an (r,f)-partition pair of G and G′ ⊆ G is a subcomplex, we deﬁne

Clearly, for every Q ∈ Pf, E∈P

r

(Pr,Pf)[G′] := (Pr[G′(r)],Pf[G′(f)]). Clearly, (Pr,Pf)[G′] is an (r,f)-partition pair of G′.

Example D.10. Suppose that G is a complex and U ⊆ V (G). For ℓ ∈ [r]0, deﬁne Eℓ := {e ∈ G(r) : |e ∩ U| = ℓ}. For k ∈ [f]0, deﬁne Qk := {Q ∈ G(f) : |Q ∩ U| = k}. Let Pr := (E0,... ,Er) and Pf := (Q0,... ,Qf). Then clearly (Pr,Pf) is an (r,f)-partition pair of G, where the containment function is given by C(Eℓ,Qk) = kℓ fr−−kℓ . In particular, C(Eℓ,Qk) = 0 whenever ℓ > k or k > f − r + ℓ. We say that (Pr,Pf) is the (r,f)-partition pair of G, U.

The partition pairs we use are generalisations of the above example. More precisely, suppose

- that G is a complex, S is an i-system in V (G) and U is a focus for S. Moreover, assume that G is r-exclusive with respect to S. For r′ ≥ r, let τr′ denote the type function of G(r′), S, U. As in the above example, if Eℓ := τr−1(ℓ) for all ℓ ∈ [r − i]0 and Qk := τf−1(k) for all k ∈ [f − i]0, then


every Q ∈ Qk contains exactly kℓ fr−−ii−−kℓ elements from Eℓ. However, we also have to consider S-unimportant edges and cliques. It turns out that it is useful to assume that the unimportant

edges and cliques are partitioned into i parts each, in an upper-triangular fashion. More formally, for r′ ≥ r, let Dr′ denote the set of S-unimportant r′-sets of G and assume

that Pr∗ is an ordered partition of Dr and Pf∗ is an ordered partition of Df. We say that (Pr∗,Pf∗) is admissible with respect to G, S, U if the following hold:

- (P1) |Pr∗| = |Pf∗| = i;
- (P2) for all S ∈ S, h ∈ [r −i]0 and B ⊆ G(S)(h) with 1 ≤ |B| ≤ 2h and all ℓ ∈ [i], there exists D(S,B,ℓ) ∈ N0 such that for all Q ∈ b∈B G(S ∪ b)[US](f−i−h), we have that

|{e ∈ Pr∗(ℓ) : ∃b ∈ B: e ⊆ S ∪ b ∪ Q}| = D(S,B,ℓ);

- (P3) (Pr∗ ⊔ {G(r) \ Dr},Pf∗ ⊔ {G(f) \ Df}) is an upper-triangular (r,f)-partition pair of G. Note that for i = 0, S = {∅} and U = {U} for some U ⊆ V (G), the pair (∅,∅) trivially


satisﬁes these conditions. Also note that (P2) can be viewed as an analogue of the containment function (from Deﬁnition D.9) which is suitable for dealing with supercomplexes.

Assume that (Pr∗,Pf∗) is admissible with respect to G, S, U. Deﬁne

Pr := Pr∗ ⊔ (τr−1(0),... ,τr−1(r − i)), Pf := Pf∗ ⊔ (τf−1(0),... ,τf−1(f − i)).

Pf∗(1) . . . Pf∗(i) τf−1(0) τf−1(1) . . . . . . τf−1(f − r) . . . . . . τf−1(f − i) Pr∗(1) ∗

![image 133](<2017-glock-hypergraph-designs-arbitrary_images/imageFile133.png>)

![image 134](<2017-glock-hypergraph-designs-arbitrary_images/imageFile134.png>)

![image 135](<2017-glock-hypergraph-designs-arbitrary_images/imageFile135.png>)

![image 136](<2017-glock-hypergraph-designs-arbitrary_images/imageFile136.png>)

![image 137](<2017-glock-hypergraph-designs-arbitrary_images/imageFile137.png>)

![image 138](<2017-glock-hypergraph-designs-arbitrary_images/imageFile138.png>)

![image 139](<2017-glock-hypergraph-designs-arbitrary_images/imageFile139.png>)

![image 140](<2017-glock-hypergraph-designs-arbitrary_images/imageFile140.png>)

![image 141](<2017-glock-hypergraph-designs-arbitrary_images/imageFile141.png>)

![image 142](<2017-glock-hypergraph-designs-arbitrary_images/imageFile142.png>)

![image 143](<2017-glock-hypergraph-designs-arbitrary_images/imageFile143.png>)

![image 144](<2017-glock-hypergraph-designs-arbitrary_images/imageFile144.png>)

![image 145](<2017-glock-hypergraph-designs-arbitrary_images/imageFile145.png>)

![image 146](<2017-glock-hypergraph-designs-arbitrary_images/imageFile146.png>)

![image 147](<2017-glock-hypergraph-designs-arbitrary_images/imageFile147.png>)

![image 148](<2017-glock-hypergraph-designs-arbitrary_images/imageFile148.png>)

![image 149](<2017-glock-hypergraph-designs-arbitrary_images/imageFile149.png>)

![image 150](<2017-glock-hypergraph-designs-arbitrary_images/imageFile150.png>)

![image 151](<2017-glock-hypergraph-designs-arbitrary_images/imageFile151.png>)

![image 152](<2017-glock-hypergraph-designs-arbitrary_images/imageFile152.png>)

![image 153](<2017-glock-hypergraph-designs-arbitrary_images/imageFile153.png>)

![image 154](<2017-glock-hypergraph-designs-arbitrary_images/imageFile154.png>)

![image 155](<2017-glock-hypergraph-designs-arbitrary_images/imageFile155.png>)

![image 156](<2017-glock-hypergraph-designs-arbitrary_images/imageFile156.png>)

![image 157](<2017-glock-hypergraph-designs-arbitrary_images/imageFile157.png>)

![image 158](<2017-glock-hypergraph-designs-arbitrary_images/imageFile158.png>)

![image 159](<2017-glock-hypergraph-designs-arbitrary_images/imageFile159.png>)

![image 160](<2017-glock-hypergraph-designs-arbitrary_images/imageFile160.png>)

![image 161](<2017-glock-hypergraph-designs-arbitrary_images/imageFile161.png>)

![image 162](<2017-glock-hypergraph-designs-arbitrary_images/imageFile162.png>)

![image 163](<2017-glock-hypergraph-designs-arbitrary_images/imageFile163.png>)

![image 164](<2017-glock-hypergraph-designs-arbitrary_images/imageFile164.png>)

![image 165](<2017-glock-hypergraph-designs-arbitrary_images/imageFile165.png>)

![image 166](<2017-glock-hypergraph-designs-arbitrary_images/imageFile166.png>)

![image 167](<2017-glock-hypergraph-designs-arbitrary_images/imageFile167.png>)

![image 168](<2017-glock-hypergraph-designs-arbitrary_images/imageFile168.png>)

![image 169](<2017-glock-hypergraph-designs-arbitrary_images/imageFile169.png>)

![image 170](<2017-glock-hypergraph-designs-arbitrary_images/imageFile170.png>)

. . . 0 ∗ Pr∗(i) 0 0 ∗

![image 171](<2017-glock-hypergraph-designs-arbitrary_images/imageFile171.png>)

![image 172](<2017-glock-hypergraph-designs-arbitrary_images/imageFile172.png>)

![image 173](<2017-glock-hypergraph-designs-arbitrary_images/imageFile173.png>)

![image 174](<2017-glock-hypergraph-designs-arbitrary_images/imageFile174.png>)

![image 175](<2017-glock-hypergraph-designs-arbitrary_images/imageFile175.png>)

![image 176](<2017-glock-hypergraph-designs-arbitrary_images/imageFile176.png>)

![image 177](<2017-glock-hypergraph-designs-arbitrary_images/imageFile177.png>)

![image 178](<2017-glock-hypergraph-designs-arbitrary_images/imageFile178.png>)

![image 179](<2017-glock-hypergraph-designs-arbitrary_images/imageFile179.png>)

![image 180](<2017-glock-hypergraph-designs-arbitrary_images/imageFile180.png>)

![image 181](<2017-glock-hypergraph-designs-arbitrary_images/imageFile181.png>)

![image 182](<2017-glock-hypergraph-designs-arbitrary_images/imageFile182.png>)

![image 183](<2017-glock-hypergraph-designs-arbitrary_images/imageFile183.png>)

τr−1(0) 0 0 0 ∗ ∗ 0 0 0 . . . 0 0 0 0 ∗ ∗ 0 0 . . . 0 0 0 0 0 ∗ ∗ 0

![image 184](<2017-glock-hypergraph-designs-arbitrary_images/imageFile184.png>)

![image 185](<2017-glock-hypergraph-designs-arbitrary_images/imageFile185.png>)

![image 186](<2017-glock-hypergraph-designs-arbitrary_images/imageFile186.png>)

![image 187](<2017-glock-hypergraph-designs-arbitrary_images/imageFile187.png>)

![image 188](<2017-glock-hypergraph-designs-arbitrary_images/imageFile188.png>)

![image 189](<2017-glock-hypergraph-designs-arbitrary_images/imageFile189.png>)

![image 190](<2017-glock-hypergraph-designs-arbitrary_images/imageFile190.png>)

![image 191](<2017-glock-hypergraph-designs-arbitrary_images/imageFile191.png>)

![image 192](<2017-glock-hypergraph-designs-arbitrary_images/imageFile192.png>)

![image 193](<2017-glock-hypergraph-designs-arbitrary_images/imageFile193.png>)

![image 194](<2017-glock-hypergraph-designs-arbitrary_images/imageFile194.png>)

![image 195](<2017-glock-hypergraph-designs-arbitrary_images/imageFile195.png>)

![image 196](<2017-glock-hypergraph-designs-arbitrary_images/imageFile196.png>)

![image 197](<2017-glock-hypergraph-designs-arbitrary_images/imageFile197.png>)

![image 198](<2017-glock-hypergraph-designs-arbitrary_images/imageFile198.png>)

![image 199](<2017-glock-hypergraph-designs-arbitrary_images/imageFile199.png>)

![image 200](<2017-glock-hypergraph-designs-arbitrary_images/imageFile200.png>)

![image 201](<2017-glock-hypergraph-designs-arbitrary_images/imageFile201.png>)

![image 202](<2017-glock-hypergraph-designs-arbitrary_images/imageFile202.png>)

![image 203](<2017-glock-hypergraph-designs-arbitrary_images/imageFile203.png>)

![image 204](<2017-glock-hypergraph-designs-arbitrary_images/imageFile204.png>)

![image 205](<2017-glock-hypergraph-designs-arbitrary_images/imageFile205.png>)

![image 206](<2017-glock-hypergraph-designs-arbitrary_images/imageFile206.png>)

![image 207](<2017-glock-hypergraph-designs-arbitrary_images/imageFile207.png>)

![image 208](<2017-glock-hypergraph-designs-arbitrary_images/imageFile208.png>)

![image 209](<2017-glock-hypergraph-designs-arbitrary_images/imageFile209.png>)

![image 210](<2017-glock-hypergraph-designs-arbitrary_images/imageFile210.png>)

![image 211](<2017-glock-hypergraph-designs-arbitrary_images/imageFile211.png>)

![image 212](<2017-glock-hypergraph-designs-arbitrary_images/imageFile212.png>)

![image 213](<2017-glock-hypergraph-designs-arbitrary_images/imageFile213.png>)

![image 214](<2017-glock-hypergraph-designs-arbitrary_images/imageFile214.png>)

![image 215](<2017-glock-hypergraph-designs-arbitrary_images/imageFile215.png>)

![image 216](<2017-glock-hypergraph-designs-arbitrary_images/imageFile216.png>)

![image 217](<2017-glock-hypergraph-designs-arbitrary_images/imageFile217.png>)

![image 218](<2017-glock-hypergraph-designs-arbitrary_images/imageFile218.png>)

![image 219](<2017-glock-hypergraph-designs-arbitrary_images/imageFile219.png>)

![image 220](<2017-glock-hypergraph-designs-arbitrary_images/imageFile220.png>)

![image 221](<2017-glock-hypergraph-designs-arbitrary_images/imageFile221.png>)

![image 222](<2017-glock-hypergraph-designs-arbitrary_images/imageFile222.png>)

![image 223](<2017-glock-hypergraph-designs-arbitrary_images/imageFile223.png>)

![image 224](<2017-glock-hypergraph-designs-arbitrary_images/imageFile224.png>)

![image 225](<2017-glock-hypergraph-designs-arbitrary_images/imageFile225.png>)

![image 226](<2017-glock-hypergraph-designs-arbitrary_images/imageFile226.png>)

![image 227](<2017-glock-hypergraph-designs-arbitrary_images/imageFile227.png>)

![image 228](<2017-glock-hypergraph-designs-arbitrary_images/imageFile228.png>)

τr−1(r − i) 0 0 0 0 0 0 ∗ ∗

![image 229](<2017-glock-hypergraph-designs-arbitrary_images/imageFile229.png>)

![image 230](<2017-glock-hypergraph-designs-arbitrary_images/imageFile230.png>)

![image 231](<2017-glock-hypergraph-designs-arbitrary_images/imageFile231.png>)

![image 232](<2017-glock-hypergraph-designs-arbitrary_images/imageFile232.png>)

![image 233](<2017-glock-hypergraph-designs-arbitrary_images/imageFile233.png>)

![image 234](<2017-glock-hypergraph-designs-arbitrary_images/imageFile234.png>)

![image 235](<2017-glock-hypergraph-designs-arbitrary_images/imageFile235.png>)

![image 236](<2017-glock-hypergraph-designs-arbitrary_images/imageFile236.png>)

![image 237](<2017-glock-hypergraph-designs-arbitrary_images/imageFile237.png>)

![image 238](<2017-glock-hypergraph-designs-arbitrary_images/imageFile238.png>)

![image 239](<2017-glock-hypergraph-designs-arbitrary_images/imageFile239.png>)

![image 240](<2017-glock-hypergraph-designs-arbitrary_images/imageFile240.png>)

![image 241](<2017-glock-hypergraph-designs-arbitrary_images/imageFile241.png>)

![image 242](<2017-glock-hypergraph-designs-arbitrary_images/imageFile242.png>)

![image 243](<2017-glock-hypergraph-designs-arbitrary_images/imageFile243.png>)

![image 244](<2017-glock-hypergraph-designs-arbitrary_images/imageFile244.png>)

![image 245](<2017-glock-hypergraph-designs-arbitrary_images/imageFile245.png>)

Figure 1. The above table sketches the containment function of an (r, f)-partition pair induced by (Pr∗, Pf∗) and U. The cells marked with ∗ and the shaded subtable will play an important role later on.

It is not too hard to see that (Pr,Pf) is an (r,f)-partition pair of G. Indeed, Pr clearly is a partition of G(r) and Pf is a partition of G(f). Suppose that C is the containment function of (Pr∗ ⊔ {G(r) \ Dr},Pf∗ ⊔ {G(f) \ Df}). Then C′ as deﬁned below is the containment function of (Pr,Pf):

- • For all E ∈ Pr∗ and Q ∈ Pf∗, let C′(E,Q) := C(E,Q).
- • For all ℓ ∈ [r − i]0 and Q ∈ Pf∗, let C′(τr−1(ℓ),Q) := 0.
- • For all E ∈ Pr∗ and k ∈ [f − i]0, deﬁne C′(E,τf−1(k)) := C(E,{G(f) \ Df}).
- • For all ℓ ∈ [r − i]0, k ∈ [f − i]0, let


f − i − k r − i − ℓ

k ℓ

C′(τr−1(ℓ),τf−1(k)) :=

- (D.4) .

We say that (Pr,Pf) as deﬁned above is induced by (Pr∗,Pf∗) and U. Finally, we say that (Pr,Pf) is an (r,f)-partition pair of G, S, U, if

- • (Pr([i]),Pf([i])) is admissible with respect to G, S, U;
- • (Pr,Pf) is induced by (Pr([i]),Pf([i])) and U.


The next proposition summarises basic properties of an (r,f)-partition pair of G, S, U.

Proposition D.11 ([12]). Let 0 ≤ i < r < f and suppose that G is a complex, S is an i-system in V (G) and U is a focus for S. Moreover, assume that G is r-exclusive with respect to S. Let (Pr,Pf) be an (r,f)-partition pair of G, S, U with containment function C. Then the following hold:

- (P1′) |Pr| = r + 1 and |Pf| = f + 1;
- (P2′) for i < ℓ ≤ r + 1, Pr(ℓ) = τr−1(ℓ − i − 1), and for i < k ≤ f + 1, Pf(k) = τf−1(k − i − 1);
- (P3′) (Pr,Pf) is upper-triangular;
- (P4′) C(Pr(ℓ),Pf(k)) = 0 whenever both ℓ > i and k > f − r + ℓ;
- (P5′) (P2) holds for all ℓ ∈ [r + 1], with Pr playing the role of Pr∗.
- (P6′) if i = 0, S = {∅} and U = {U} for some U ⊆ V (G), then the (unique) (r,f)-partition pair of G, S, U is the (r,f)-partition pair of G, U (cf. Example D.10);
- (P7′) for every subcomplex G′ ⊆ G, (Pr,Pf)[G′] is an (r,f)-partition pair of G′, S, U.


- D.3. Partition regularity.


- Deﬁnition D.12. Let G be a complex on n vertices and (Pr,Pf) an (r,f)-partition pair of G with a := |Pr| and b := |Pf|. Let A = (aℓ,k) ∈ [0,1]a×b. We say that G is (ε,A,f,r)-regular with respect to (Pr,Pf) if for all ℓ ∈ [a], k ∈ [b] and e ∈ Pr(ℓ), we have


- (D.5) |(Pf(k))(e)| = (aℓ,k ± ε)nf−r,


where we view Pf(k) as a subgraph of G(f). If E ⊆ Pr(ℓ) and Q ⊆ Pf(k), we will often write A(E,Q) instead of aℓ,k.

For A ∈ [0,1]a×b with 1 ≤ t ≤ a ≤ b, we deﬁne

- • min\(A) := min{aj,j : j ∈ [a]} as the minimum value on the diagonal,
- • min\t(A) := min{aj,j+b−a : j ∈ {a − t + 1,... ,a}} and
- • min\\t(A) := min{min\(A),min\t(A)}.


Note that min\\r−i+1(A) is the minimum value of the entries in A that correspond to the entries marked with ∗ in Figure 1.

- Deﬁnition D.13. We say that A ∈ [0,1]a×b is diagonal-dominant if aℓ,k ≤ ak,k/2(a − ℓ) for all 1 ≤ ℓ < k ≤ min{a,b}.


Lemma D.14 ([12]). Let 1/n ≪ ε ≪ ξ,1/f and r ∈ [f − 1]. Suppose that G is a complex on n vertices and (Pr,Pf) is an upper-triangular (r,f)-partition pair of G with |Pr| ≤ |Pf| ≤ f + 1. Let A ∈ [0,1]|Pr|×|Pf| be diagonal-dominant with d := min\(A) ≥ ξ. Suppose that G is (ε,A,f,r)regular with respect to (Pr,Pf) and (ξ,f + r,r)-dense. Then there exists Y ∗ ⊆ G(f) such that G[Y ∗] is (2fε,d,f,r)-regular and (0.9ξ(ξ/4(f + 1))(f+fr),f + r,r)-dense.

The following concept of a setup turns out to be the appropriate generalisation of Deﬁnition 6.1 to i-systems and partition pairs.

Deﬁnition D.15 (Setup). Let G be a complex on n vertices and 0 ≤ i < r < f. We say that S,U,(Pr,Pf) form an (ε,µ,ξ,f,r,i)-setup for G if there exists an f-graph Y on V (G) such that the following hold:

- (S1) S is an i-system in V (G) such that G is r-exclusive with respect to S; U is a µ-focus for S and (Pr,Pf) is an (r,f)-partition pair of G, S, U;
- (S2) there exists a matrix A ∈ [0,1](r+1)×(f+1) with min\\r−i+1(A) ≥ ξ such that G[Y ] is (ε,A,f,r)-regular with respect to (Pr,Pf)[G[Y ]] = (Pr,Pf[Y ]);
- (S3) every S-unimportant e ∈ G(r) is contained in at least ξ(µn)f S-unimportant Q ∈

G[Y ](f+r), and for every S-important e ∈ G(r) with e ⊇ S ∈ S, we have |G[Y ](f+r)(e)[US]| ≥ ξ(µn)f;

- (S4) for all S ∈ S, h ∈ [r − i]0 and all B ⊆ G(S)(h) with 1 ≤ |B| ≤ 2h we have that b∈B G(S ∪ b)[US] is an (ε,ξ,f − i − h,r − i − h)-complex.


Moreover, if (S1)–(S4) are true and A is diagonal-dominant, then we say that S,U,(Pr,Pf) form a diagonal-dominant (ε,µ,ξ,f,r,i)-setup for G.

Note that (S4) implies that G(S)[US] is an (ε,ξ,f − i,r − i)-supercomplex for every S ∈ S, but is stronger in the sense that B is not restricted to US. The following observation shows that Deﬁnition D.15 does indeed generalise Deﬁnition 6.1. (Recall that the partition pair of G,U was deﬁned in Example D.10.) We will use it to derive the Cover down lemma from the more general Cover down lemma for setups.

Proposition D.16 ([12]). Let G be a complex on n vertices and suppose that U ⊆ V (G) is (ε,µ,ξ,f,r)-random in G. Let (Pr,Pf) be the (r,f)-partition pair of G,U. Then {∅},{U},(Pr,Pf) form an (ε,µ,µξ,f,r,˜ 0)-setup for G, where µ˜ := (min {µ,1 − µ})f−r.

The following lemma shows that we can (probabilistically) sparsify a given setup so that the resulting setup is diagonal-dominant.

- Lemma D.17 ([12]). Let 1/n ≪ ε ≪ ν ≪ µ,ξ,1/f and 0 ≤ i < r < f. Let ξ′ := ν8f·f+1. Let G be a complex on n vertices and suppose that


S,U,(Pr,Pf) form an (ε,µ,ξ,f,r,i)-setup for G. Then there exists a subgraph H ⊆ G(r) with ∆(H) ≤ 1.1νn and the following property: for all

- L ⊆ G(r) with ∆(L) ≤ εn and all (r+1)-graphs O on V (G) with ∆(O) ≤ εn, the following holds for G′ := G[H △ L] − O:


S,U,(Pr,Pf)[G′] form a diagonal-dominant (√ε,µ,ξ′,f,r,i)-setup for G′. We also need a similar result which ‘sparsiﬁes’ the neighbourhood complexes of an i-system.

![image 246](<2017-glock-hypergraph-designs-arbitrary_images/imageFile246.png>)

- Lemma D.18 ([12]). Let 1/n ≪ ε ≪ µ,β,ξ,1/f and 1 ≤ i < r < f. Let ξ′ := 0.9ξβ(8f). Let G be a complex on n vertices and let S be an i-system in G such that G is r-exclusive with respect to S. Let U be a µ-focus for S. Suppose that

G(S)[US] is an (ε,ξ,f − i,r − i)-supercomplex for every S ∈ S.

Then there exists a subgraph H ⊆ G(r) with ∆(H) ≤ 1.1βn and the following property: for all L ⊆ G(r) with ∆(L) ≤ εn and all (r+1)-graphs O on V (G) with ∆(O) ≤ εn, the following holds for G′ := G[H △ L] − O:

G′(S)[US] is a (√ε,ξ′,f − i,r − i)-supercomplex for every S ∈ S.

![image 247](<2017-glock-hypergraph-designs-arbitrary_images/imageFile247.png>)

The ﬁnal tool that we need is the following lemma. Given a setup in a supercomplex G and an i′-extension T of the respective i-system S, it allows us to ﬁnd a new focus U′ for T and a suitable partition pair which together form a new setup in the complex G′ (which is the complex we look at after all edges with type less than r − i′ have been covered).

The idea is to choose U′ randomly. The proof of Lemma D.19 follows the lines of Claim 4 and Step 2 in the proof of Lemma 10.22 in [12]. In particular, (ii) and (iii) below correspond to (10.11) and (10.12), respectively, and (i) holds using Lemma D.6.

- Lemma D.19. Let 1/n ≪ ε ≪ ρ ≪ µ,ξ,1/f and 0 ≤ i < i′ < r < f. Let G be a complex on n vertices and suppose that S,U,(Pr,Pf) form an (ε,µ,ξ,f,r,i)-setup for G. For r′ ≥ r, let τr′ be the type function of G(r′), S, U. Let T be the i′-extension of S in G around U, and let


G′ := G − {e ∈ G(r) : e is S-important and τr(e) < r − i′}. Then there exist U′,Pr′,Pf′ with the following properties:

- (i) U′ is a (µ,ρ,r)-focus for T such that UT ⊆ UT↾S for all T ∈ T ;
- (ii) T ,U′,(Pr′,Pf′ ) form a (1.1ε,ρµ,ρf−rξ,f,r,i′)-setup for G′;
- (iii) G′(T)[UT] is a (1.1ε,0.9ξ,f − i′,r − i′)-supercomplex for every T ∈ T .


- D.4. Proof of the Cover down lemma. In this subsection, we state and prove the Cover down lemma for setups and deduce the Cover down lemma (Lemma 6.9).


Deﬁnition D.20. Let F and G be r-graphs, let S be an i-system in V (G), and let U be a focus for S. We say that G is F-divisible with respect to S,U, if for all S ∈ S and all T ⊆ V (G) \ S with |T| ≤ r − i − 1 and |T \ US| ≥ 1, we have Deg(F)i+|T| | |G(S ∪ T)|.

Note that if G is F-divisible, then it is F-divisible with respect to any i-system and any associated focus.

Recall that a setup for G was deﬁned in Deﬁnition D.15, and G being (ξ,f,r)-dense with respect to H ⊆ G(r) in Deﬁnition 6.8. We will prove the Cover down lemma for setups by induction on r − i. We will deduce the Cover down lemma by applying this lemma with i = 0.

Lemma D.21 (Cover down lemma for setups). Let 1/n ≪ 1/κ ≪ γ ≪ ε ≪ ν ≪ µ,ξ,1/f and 0 ≤ i < r < f. Let F be a weakly regular r-graph on f vertices. Assume that (∗)ℓ is true for all ℓ ∈ [r − i − 1]. Let G be a complex on n vertices and suppose that S,U,(Pr,Pf) form an (ε,µ,ξ,f,r,i)-setup for G. For r′ ≥ r, let τr′ denote the type function of G(r′), S, U. Then the following hold.

- (i) Let G˜ be a complex on V (G) with G ⊆ G˜ such that G˜ is (ε,f,r)-dense with respect to

G(r) − τr−1(0). Then there exists a subgraph H∗ ⊆ G(r) − τr−1(0) with ∆(H∗) ≤ νn such that for any L∗ ⊆ G˜(r) with ∆(L∗) ≤ γn and H∗ ∪ L∗ being F-divisible with respect to S,U and any (r+1)-graph O∗ on V (G) with ∆(O∗) ≤ γn, there exists a κ-well separated F-packing in G˜[H∗ ∪ L∗] − O∗ which covers all edges of L∗, and all S-important edges of H∗ except possibly some from τr−1(r − i).

- (ii) If G(r) is F-divisible with respect to S,U and the setup is diagonal-dominant, then there exists a 2κ-well separated F-packing in G which covers all S-important r-edges except possibly some from τr−1(r − i).


Before proving Lemma D.21, we show how it implies the Cover down lemma (Lemma 6.9). Note that we only need part (i) of Lemma D.21 to prove Lemma 6.9. (ii) is used in the inductive proof of Lemma D.21 itself.

Proof of Lemma 6.9. Let S := {∅}, U := {U} and let (Pr,Pf) be the (r,f)-partition pair of G,U. By Proposition D.16, S,U,(Pr,Pf) form a (ε,µ,µf−rξ,f,r,0)-setup for G. We can thus apply Lemma D.21(i) with µf−rξ playing the role of ξ. Recall that all r-edges of G are S-important. Moreover, let τr denote the type function of G(r), S, U. We then have τr−1(0) = G(r)[U¯] and τr−1(r) = G(r)[U], where U¯ := V (G) \ U.

Proof of Lemma D.21. The proof is by induction on r − i. For i = r − 1, we will prove the statement directly. For i < r−1, we assume that the statement is true for all i′ ∈ {i+1,... ,r−1}. We will ﬁrst prove (i) using (ii) inductively, and then derive (ii) from (i) (for the same value of r − i).

Proof of (i). If i < r − 1, choose new constants ν1,ρ1,β1,... ,νr−i−1,ρr−i−1,βr−i−1 such that 1/n ≪ 1/κ ≪ γ ≪ ε ≪ ν1 ≪ ρ1 ≪ β1 ≪ ··· ≪ νr−i−1 ≪ ρr−i−1 ≪ βr−i−1 ≪ ν ≪ µ,ξ,1/f. For every ℓ ∈ [r − i − 1], let

- (D.6) Gℓ := G − {e ∈ G(r) : e is S-important and τr(e) < ℓ}.

For every i′ ∈ {i+1,... ,r−1}, let T i′ be the i′-extension of S in G around U. By Proposition D.4, the following hold for all i′ ∈ {i + 1,... ,r − 1}:

(I) Gr−i′ is r-exclusive with respect to T i′; (II) the elements of τr−1(r − i′) are precisely the T i′-important elements of G(rr−)i′.

By Lemma D.19, for every i′ ∈ {i + 1,... ,r − 1}, there exist Ui′, Pri′, Pfi′ such that the following hold:

- (a) Ui′ is a (µ,ρr−i′,r)-focus for T i′ such that UT ⊆ UT↾S for all T ∈ T i′;
- (b) T i′,Ui′,(Pri′,Pfi′) form a (1.1ε,ρr−i′µ,ρfr−−ir′ξ,f,r,i′)-setup for Gr−i′;
- (c) Gr−i′(T)[UT] is a (1.1ε,0.9ξ,f − i′,r − i′)-supercomplex for every T ∈ T i′.


(I) allows us to consider the type function τr−i′,r of G(rr−)i′,T i′,Ui′. Step 1: Reserving subgraphs In this step, we will ﬁnd a number of subgraphs of G(r) − τr−1(0) whose union will be the

r-graph H∗ we seek in (i). Let G˜ be a complex as speciﬁed in (i). Let β0 := ε. Let H0 be a subgraph of G(r) − τr−1(0) with ∆(H0) ≤ 1.1β0n such that for all e ∈ G˜(r), we have

|G˜[H0 ∪ {e}](f)(e)| ≥ 0.9β

(fr)

- (D.7) 0 nf−r.


(H0 will be used to greedily cover L∗.) That such a subgraph exists can be seen by a probabilistic argument: let H0 be obtained by including every edge of G(r) − τr−1(0) with probability β0. Clearly, whp ∆(H0) ≤ 1.1β0n. Also, since G˜ is (ε,f,r)-dense with respect to G(r) − τr−1(0) by assumption, we have for all e ∈ G˜(r) that

(fr)−1 0 εnf−r.

(fr)−1 0 |G˜[(G(r) − τr−1(0)) ∪ {e}](f)(e)| ≥ β

E|G˜[H0 ∪ {e}](f)(e)| = β

Using Corollary A.7 and a union bound, it is then easy to see that whp H0 satisﬁes (D.7) for all e ∈ G˜(r).

Step 1.1: Deﬁning ‘sparse’ induction graphs Hℓ. Consider ℓ ∈ [r − i − 1] and let i′ := r − ℓ. Let ξℓ := ν8

f·f+1

ℓ . By (b) and Lemma D.17 (with Gℓ,3βℓ−1,νℓ,ρℓµ,ρfℓ−rξ,i′ playing the roles of G,ε,ν,µ,ξ,i), there exists a subgraph Hℓ ⊆ Gℓ(r)

with ∆(Hℓ) ≤ 1.1νℓn and the following property: for all L ⊆ G(ℓr) with ∆(L) ≤ 3βℓ−1n and every (r + 1)-graph O on V (Gℓ) with ∆(O) ≤ 3βℓ−1n, the following holds for G′ := Gℓ[Hℓ △ L] − O:

- (D.8) T i′,Ui′,(Pri′,Pfi′)[G′] form a diagonal-dominant ( 3βℓ−1,ρℓµ,ξℓ,f,r,i′)-setup for G′.

![image 248](<2017-glock-hypergraph-designs-arbitrary_images/imageFile248.png>)

Step 1.2: Deﬁning ‘localised’ cleaning graphs Jℓ. Again, consider ℓ ∈ [r − i − 1] and let i′ := r − ℓ. Let

- (D.9) G∗ℓ := Gℓ − {e ∈ G(ℓr) : e is T i′-important and τℓ,r(e) < ℓ}.

We claim that G∗ℓ(T)[UT] = Gℓ(T)[UT] for every T ∈ T i′. Indeed, consider any T ∈ T i′ and e ∈ Gℓ(T)[UT]. Hence, e ⊆ UT and e∪T ∈ Gℓ. We need to show that e∪T ∈ G∗ℓ, i.e. that there is no T i′-important r-subset e′ of e∪T with τℓ,r(e′) < ℓ. However, if e′ ∈ e∪rT is T i′-important, then |e ∪ T| ≥ |e′| = r and since Gℓ is r-exclusive with respect to T i′ by (I), we must have T ⊆ e′. As e′ \ T ⊆ e ⊆ UT, we deduce that τℓ,r(e′) = |e′ ∩ UT| = |e′ \ T| = r − i′ = ℓ.

Hence, by (c), for every T ∈ T i′, G∗

ℓ(T)[UT] is a (1.1ε,0.9ξ,f − i′,r − i′)-supercomplex. Thus, by Lemma D.18 (with G∗ℓ,3νℓ,ρℓµ,βℓ,0.9ξ playing the roles of G,ε,µ,β,ξ), there exists a subgraph Jℓ ⊆ G∗ℓ(r) with ∆(Jℓ) ≤ 1.1βℓn and the following property: for all L ⊆ G∗ℓ(r) with ∆(L) ≤ 3νℓn and every (r + 1)-graph O on V (G∗ℓ) with ∆(O) ≤ 3νℓn, the following holds for G∗ := G∗ℓ[Jℓ △ L] − O:

G∗(T)[UT] is a (√3νℓ,0.81ξβ(8

![image 249](<2017-glock-hypergraph-designs-arbitrary_images/imageFile249.png>)

f )

- (D.10) ℓ ,f − i′,r − i′)-supercomplex for every T ∈ T i′.


We have deﬁned subgraphs H0,H1,... ,Hr−i−1,J1,... ,Jr−i−1 of G(r) − τr−1(0). Note that

they are not necessarily edge-disjoint. Let H0∗ := H0 and for all ℓ ∈ [r −i−1] deﬁne inductively Hℓ′ := Hℓ∗−1 ∪ Hℓ, Hℓ∗ := Hℓ∗−1 ∪ Hℓ ∪ Jℓ = Hℓ′ ∪ Jℓ, H∗ := Hr∗−i−1.

Clearly, ∆(Hℓ∗) ≤ 2βℓn for all ℓ ∈ [r − i − 1]0 and ∆(Hℓ′) ≤ 2νℓn for all ℓ ∈ [r − i − 1]. In particular, ∆(H∗) ≤ 2βr−i−1n ≤ νn, as desired.

Step 2: Covering down

Let L∗ be any subgraph of G˜(r) with ∆(L∗) ≤ γn such that H∗∪L∗ is F-divisible with respect to S,U, and let O∗ ⊆ G˜(r+1) with ∆(O∗) ≤ γn. We need to ﬁnd a κ-well separated F-packing F in G˜[H∗ ∪ L∗] − O∗ which covers all edges of L∗, and covers all S-important edges of H∗ except possibly some from τr−1(r − i). We will do so by inductively showing that the following holds for all ℓ ∈ [r − i].

(#)ℓ There exists a (3ℓ√κ)-well separated F-packing Fℓ∗−1 in G˜[Hℓ∗−1 ∪ L∗] − O∗ covering all

![image 250](<2017-glock-hypergraph-designs-arbitrary_images/imageFile250.png>)

edges of L∗, and all S-important e ∈ Hℓ∗−1 with τr(e) < ℓ. Clearly, (#)r−i establishes (i).

Claim 1: (#)1 is true.

Proof of claim: Let H0′ := H0 ∪ L∗ = H0∗ ∪ L∗. By (D.7) and Proposition A.1, for all e ∈ L∗ we have that

(fr) 0 nf−r.

|(G˜[H0′] − O∗)(f)(e)| ≥ |G˜[H0 ∪ e](f)(e)| − 2rγnf−r ≥ 0.8β

By Corollary A.11, there is a 1-well separated F-packing F0∗ in G˜[H0′] − O∗ covering all edges of L∗. Since H0∗ does not contain any edges from τr−1(0), F0∗ satisﬁes (#)1. −

If i = r − 1, we can take F0∗ and complete the proof of (i). So assume that i < r − 1 and that Lemma D.21 holds for larger values of i.

Suppose that for some ℓ ∈ [r − i − 1], Fℓ∗−1 satisﬁes (#)ℓ. Let i′ := r − ℓ > i. We will now ﬁnd a 3√κ-well separated F-packing Fℓ in G[Hℓ∗] − Fℓ∗−(r1) − Fℓ∗≤−1(r+1) − O∗ such that Fℓ covers all edges of Hℓ∗ − Fℓ∗−(r1) that belong to τr−1(ℓ).

![image 251](<2017-glock-hypergraph-designs-arbitrary_images/imageFile251.png>)

Then Fℓ∗ := Fℓ∗−1 ∪ Fℓ covers all edges of L∗ and all S-important e ∈ Hℓ∗ with τr(e) < ℓ + 1. By Fact 4.3(ii), Fℓ∗ is (3ℓ√κ + 3√κ)-well separated, implying that (#)ℓ+1 is true.

![image 252](<2017-glock-hypergraph-designs-arbitrary_images/imageFile252.png>)

![image 253](<2017-glock-hypergraph-designs-arbitrary_images/imageFile253.png>)

Crucially, by (II), all the edges of τr−1(ℓ) that we seek to cover in this step are T i′-important. We will obtain Fℓ as the union of Fℓ◦ and Fℓ†, where

(COV1) Fℓ◦ is 2√κ-well separated F-packing in G[Hℓ∗] − Fℓ∗−(r1) − Fℓ∗≤−1(r+1) − O∗ which covers all T i′-important edges of Hℓ∗ − Fℓ∗−(r1) except possibly some from τℓ,r−1(ℓ); (COV2) Fℓ† is a √κ-well separated F-packing in G[Hℓ∗]−Fℓ∗−(r1) −Fℓ◦(r) −Fℓ∗≤−1(r+1)−Fℓ◦≤(r+1) −O∗ which covers all T i′-important edges of Hℓ∗ − Fℓ∗−(r1) − Fℓ◦(r).

![image 254](<2017-glock-hypergraph-designs-arbitrary_images/imageFile254.png>)

![image 255](<2017-glock-hypergraph-designs-arbitrary_images/imageFile255.png>)

Since Fℓ† and Fℓ◦ are (r + 1)-disjoint, Fℓ := Fℓ◦ ∪ Fℓ† is 3√κ-well separated by Fact 4.3(ii). Clearly, Fℓ covers all T i′-important edges of Hℓ∗ − Fℓ∗−(r1), as required. We will obtain Fℓ◦ by using (ii) of this lemma inductively, and Fℓ† by an application of the Localised cover down lemma (Lemma D.7).

![image 256](<2017-glock-hypergraph-designs-arbitrary_images/imageFile256.png>)

Recall that F-divisibility with respect to T i′,Ui′ was deﬁned in Deﬁnition D.20. Let Hℓ′′ := Hℓ′ − Fℓ∗−(r1).

Claim 2: Hℓ′′ is F-divisible with respect to T i′,Ui′.

Proof of claim: Let T ∈ T i′ and b′ ⊆ V (G)\T with |b′| ≤ r−i′ −1 and |b′ \UT| ≥ 1. We have to show that Deg(F)i′+|b′| | |Hℓ′′(T ∪b′)|. Let S := T↾S and b := b′∪(T \S). Hence, |b| = |b′|+i′−i. Clearly, b ⊆ V (G)\S, |b| ≤ r−i−1 and |b\US| ≥ |T \S| ≥ 1. Hence, since H∗∪L∗ is F-divisible with respect to S,U by assumption, we have Deg(F)i+|b| | |(H∗ ∪ L∗)(S ∪ b)|, and this implies that Deg(F)i+|b| | |((H∗ ∪ L∗) − Fℓ∗−(r1))(S ∪ b)|. It is thus suﬃcient to show that

Hℓ′′(T ∪ b′) = ((H∗ ∪ L∗) − Fℓ∗−(r1))(S ∪ b).

Clearly, we have T ∪b′ = S∪b and Hℓ′′ ⊆ H∗−Fℓ∗−(r1). Conversely, observe that every e ∈ H∗∪L∗ that contains T ∪ b′ and is not covered by Fℓ∗−1 must belong to Hℓ′′. Indeed, since e contains T, we have that τr(e) ≤ r − i′ = ℓ, so e ∈ Hℓ∗. Moreover, by (#)ℓ we must have τr(e) ≥ ℓ. Hence, τr(e) = ℓ. But since |b′ \ UT| ≥ 1, we have τℓ,r(e) < ℓ. By (D.9), e ∈/ Jℓ. Thus,

e ∈ Hℓ′ − Fℓ∗−(r1) = Hℓ′′. Hence, Hℓ′′(T ∪ b′) = ((H∗ ∪ L∗) − Fℓ∗−(r1))(S ∪ b). This implies the claim. −

Let L′ℓ := Hℓ′′ △ Hℓ. So Hℓ′′ = Hℓ △ L′ℓ. Claim 3: L′ℓ ⊆ G(ℓr) and ∆(L′ℓ) ≤ 3βℓ−1n.

Proof of claim: Suppose, for a contradiction, that there is e ∈ Hℓ′′ △ Hℓ with e ∈/ G(ℓr). Since Hℓ ⊆ G(ℓr), we must have e ∈ Hℓ′′ = Hℓ′ − Fℓ∗−(r1). Thus, since e is not covered by Fℓ∗−1, (#)ℓ implies that e is S-unimportant or τr(e) ≥ ℓ, both contradicting e ∈/ G(ℓr).

In order to see the second part, observe that L′ℓ = ((Hℓ∗−1 ∪ Hℓ) − Fℓ∗−(r1)) △ Hℓ ⊆ Hℓ∗−1 ∪ L∗ since Fℓ∗−(r1) ⊆ L∗ ∪ Hℓ∗−1. Thus, ∆(L′ℓ) ≤ ∆(Hℓ∗−1) + ∆(L∗) ≤ 3βℓ−1n. −

Note that Claim 3 implies that Hℓ′′ ⊆ G(ℓr). Let Gℓ,ind := Gℓ[Hℓ′′] − Fℓ∗≤−1(r+1) − O∗. By Fact 4.3(i) and (#)ℓ, we have that ∆(Fℓ∗≤−1(r+1)∪O∗) ≤ (3ℓ√κ)(f −r)+γn ≤ 2γn. Thus, by (D.8) and Claim 3, T i′,Ui′,(Pri′,Pfi′)[Gℓ,ind] form a diagonal-dominant ( 3βℓ−1,ρℓµ,ξℓ,f,r,i′)-setup for Gℓ,ind. We can thus apply Lemma D.21(ii) inductively with the following objects/parameters.

![image 257](<2017-glock-hypergraph-designs-arbitrary_images/imageFile257.png>)

![image 258](<2017-glock-hypergraph-designs-arbitrary_images/imageFile258.png>)

object/parameter Gℓ,ind n 3βℓ−1 ρℓµ ξℓ i′ T i′ Ui′ (Pri′, Pfi′)[Gℓ,ind] √κ f r F playing the role of G n ε µ ξ i S U (Pr, Pf) κ f r F

![image 259](<2017-glock-hypergraph-designs-arbitrary_images/imageFile259.png>)

![image 260](<2017-glock-hypergraph-designs-arbitrary_images/imageFile260.png>)

![image 261](<2017-glock-hypergraph-designs-arbitrary_images/imageFile261.png>)

![image 262](<2017-glock-hypergraph-designs-arbitrary_images/imageFile262.png>)

![image 263](<2017-glock-hypergraph-designs-arbitrary_images/imageFile263.png>)

![image 264](<2017-glock-hypergraph-designs-arbitrary_images/imageFile264.png>)

![image 265](<2017-glock-hypergraph-designs-arbitrary_images/imageFile265.png>)

![image 266](<2017-glock-hypergraph-designs-arbitrary_images/imageFile266.png>)

![image 267](<2017-glock-hypergraph-designs-arbitrary_images/imageFile267.png>)

![image 268](<2017-glock-hypergraph-designs-arbitrary_images/imageFile268.png>)

![image 269](<2017-glock-hypergraph-designs-arbitrary_images/imageFile269.png>)

![image 270](<2017-glock-hypergraph-designs-arbitrary_images/imageFile270.png>)

![image 271](<2017-glock-hypergraph-designs-arbitrary_images/imageFile271.png>)

![image 272](<2017-glock-hypergraph-designs-arbitrary_images/imageFile272.png>)

![image 273](<2017-glock-hypergraph-designs-arbitrary_images/imageFile273.png>)

![image 274](<2017-glock-hypergraph-designs-arbitrary_images/imageFile274.png>)

![image 275](<2017-glock-hypergraph-designs-arbitrary_images/imageFile275.png>)

![image 276](<2017-glock-hypergraph-designs-arbitrary_images/imageFile276.png>)

![image 277](<2017-glock-hypergraph-designs-arbitrary_images/imageFile277.png>)

![image 278](<2017-glock-hypergraph-designs-arbitrary_images/imageFile278.png>)

![image 279](<2017-glock-hypergraph-designs-arbitrary_images/imageFile279.png>)

![image 280](<2017-glock-hypergraph-designs-arbitrary_images/imageFile280.png>)

![image 281](<2017-glock-hypergraph-designs-arbitrary_images/imageFile281.png>)

![image 282](<2017-glock-hypergraph-designs-arbitrary_images/imageFile282.png>)

![image 283](<2017-glock-hypergraph-designs-arbitrary_images/imageFile283.png>)

![image 284](<2017-glock-hypergraph-designs-arbitrary_images/imageFile284.png>)

![image 285](<2017-glock-hypergraph-designs-arbitrary_images/imageFile285.png>)

![image 286](<2017-glock-hypergraph-designs-arbitrary_images/imageFile286.png>)

![image 287](<2017-glock-hypergraph-designs-arbitrary_images/imageFile287.png>)

Since G(ℓ,indr) = Hℓ′′ is F-divisible with respect to T i′,Ui′ by Claim 2, there exists a 2√κ-well separated F-packing Fℓ◦ in Gℓ,ind covering all T i′-important edges of Hℓ′′ except possibly some from τℓ,r−1(r − i′) = τℓ,r−1(ℓ). Note that Hℓ∗ − Hℓ′ ⊆ Jℓ and that every T i′-important edge of Jℓ lies in τℓ,r−1(ℓ). Thus Fℓ◦ does indeed cover all T i′-important edges of Hℓ∗ − Fℓ∗−(r1) except possibly some from τℓ,r−1(ℓ), as required for (COV1).

![image 288](<2017-glock-hypergraph-designs-arbitrary_images/imageFile288.png>)

We will now use Jℓ to cover the remaining T i′-important edges of Hℓ∗. Let Jℓ′ := Hℓ∗ −Fℓ∗−(r1) − Fℓ◦(r). Let Si∗′ ∈ V(iF′ ) be such that F(Si∗′) is non-empty.

Claim 4: Jℓ′(T)[UT] is F(Si∗′)-divisible for every T ∈ T i′.

Proof of claim: Let T ∈ T i′ and b′ ⊆ UT with |b′| ≤ r − i′ − 1. We have to show that Deg(F(Si∗′))|b′| | |Jℓ′(T)[UT](b′)|. Note that for every e ∈ Jℓ′ ⊆ G∗ℓ(r) containing T, we have τℓ,r(e) = r − i′. Thus, Jℓ′(T)[UT] is identical with Jℓ′(T) except for the diﬀerent vertex sets. It is thus suﬃcient to show that Deg(F(Si∗′))|b′| | |Jℓ′(T ∪ b′)|. By Proposition 4.2, we have that Deg(F(Si∗′))|b′| = Deg(F)i′+|b′|. Let S := T↾S and b := b′ ∪ (T \ S). By assumption, H∗ ∪ L∗ is F-divisible with respect to S,U. Thus, since S ∈ S, |b| ≤ r −i−1 and |b\US| ≥ |T \S| ≥ 1, we have that Deg(F)i+|b| | |(H∗ ∪L∗)(S ∪b)|. This implies that Deg(F)i+|b| | |((H∗ ∪L∗) −Fℓ∗−(r1) − Fℓ◦(r))(S ∪ b)|. It is thus suﬃcient to prove that Jℓ′(T ∪ b′) = ((H∗ ∪ L∗) − Fℓ∗−(r1) − Fℓ◦(r))(S ∪ b). Clearly, Jℓ′ ⊆ H∗ − Fℓ∗−(r1) − Fℓ◦(r) by deﬁnition. Conversely, observe that every e ∈ (H∗ ∪ L∗) −

- Fℓ∗−(r1) − Fℓ◦(r) that contains T ∪ b′ must belong to Jℓ′. Indeed, since L∗ ⊆ Fℓ∗−(r1), we have e ∈ H∗,

and since e contains T, we have τr(e) ≤ ℓ. Hence, e ∈ Hℓ∗ and thus e ∈ Jℓ′. This implies the claim. −

Let L′′ℓ := Jℓ′ △ Jℓ. So Jℓ′ = Jℓ △ L′′ℓ. Claim 5: L′′ℓ ⊆ G∗ℓ(r) and ∆(L′′ℓ) ≤ 3νℓn.

Proof of claim: Suppose, for a contradiction, that there is e ∈ Jℓ′ △ Jℓ with e ∈/ G∗ℓ(r). By (D.6) and (D.9), the latter implies that e is S-important with τr(e) < ℓ or T i′-important with τℓ,r(e) <

ℓ. However, since Jℓ ⊆ G∗ℓ(r), we must have e ∈ Jℓ′ − Jℓ and thus e ∈ Hℓ′ and e ∈/ Fℓ∗−(r1) ∪ Fℓ◦(r). In particular, e ∈ Hℓ′′. Now, if e was S-important with τr(e) < ℓ, then e ∈ Hℓ′ −Hℓ ⊆ Hℓ∗−1. But then e would be covered by Fℓ∗−1, a contradiction. So e must be T i′-important with τℓ,r(e) < ℓ. But since e ∈ Hℓ′′, e would be covered by Fℓ◦ unless τℓ,r(e) = ℓ, a contradiction.

In order to see the second part, observe that

L′′ℓ = ((Hℓ′ ∪ Jℓ) − Fℓ∗−(r1) − Fℓ◦(r)) △ Jℓ ⊆ Hℓ′ ∪ L∗ since Fℓ∗−(r1) ∪ Fℓ◦(r) ⊆ Hℓ′ ∪ L∗. Thus, ∆(L′′ℓ) ≤ ∆(Hℓ′) + ∆(L∗) ≤ 3νℓn. −

Note that Claim 5 implies that Jℓ′ ⊆ G∗ℓ(r). Let

Gℓ,clean := G∗ℓ[Jℓ′] − Fℓ∗≤−1(r+1) − Fℓ◦≤(r+1) − O∗. By (#)ℓ, (COV1) and Fact 4.3(i), we have that

∆(Fℓ∗≤−1(r+1) ∪ Fℓ◦≤(r+1) ∪ O∗) ≤ (3ℓ√κ)(f − r) + (2√κ)(f − r) + γn ≤ 2γn. Thus, by (D.10), Claim 4 and Claim 5, Gℓ,clean(T)[UT] is an F(Si∗′)-divisible (ρℓ,β(8

![image 289](<2017-glock-hypergraph-designs-arbitrary_images/imageFile289.png>)

![image 290](<2017-glock-hypergraph-designs-arbitrary_images/imageFile290.png>)

f)+1

ℓ ,f − i′,r − i′)-supercomplex for every T ∈ T i′. Moreover, whenever there are T ∈ T (i′) and e ∈

- G(ℓ,cleanr) ⊆ G∗ℓ(r) with T ⊆ e, then |(e \ T) ∩ UT| = τℓ,r(e) = ℓ = |e \ T| and thus e \ T ⊆ UT. By (I), Gℓ,clean ⊆ Gℓ is r-exclusive with respect to T i′, and by (a), Ui′ is a (µ,ρℓ,r)-focus for


T i′. We can therefore apply the Localised cover down lemma (Lemma D.7) with the following objects/parameters.

![image 291](<2017-glock-hypergraph-designs-arbitrary_images/imageFile291.png>)

![image 292](<2017-glock-hypergraph-designs-arbitrary_images/imageFile292.png>)

![image 293](<2017-glock-hypergraph-designs-arbitrary_images/imageFile293.png>)

![image 294](<2017-glock-hypergraph-designs-arbitrary_images/imageFile294.png>)

![image 295](<2017-glock-hypergraph-designs-arbitrary_images/imageFile295.png>)

![image 296](<2017-glock-hypergraph-designs-arbitrary_images/imageFile296.png>)

![image 297](<2017-glock-hypergraph-designs-arbitrary_images/imageFile297.png>)

![image 298](<2017-glock-hypergraph-designs-arbitrary_images/imageFile298.png>)

![image 299](<2017-glock-hypergraph-designs-arbitrary_images/imageFile299.png>)

![image 300](<2017-glock-hypergraph-designs-arbitrary_images/imageFile300.png>)

![image 301](<2017-glock-hypergraph-designs-arbitrary_images/imageFile301.png>)

![image 302](<2017-glock-hypergraph-designs-arbitrary_images/imageFile302.png>)

f )+1

ℓ i′ Gℓ,clean T i′ Ui′ r f F Si∗′ playing the role of n ρ ρsize ξ i G S U r f F S∗

object/parameter n ρℓ µ β(8

![image 303](<2017-glock-hypergraph-designs-arbitrary_images/imageFile303.png>)

![image 304](<2017-glock-hypergraph-designs-arbitrary_images/imageFile304.png>)

![image 305](<2017-glock-hypergraph-designs-arbitrary_images/imageFile305.png>)

![image 306](<2017-glock-hypergraph-designs-arbitrary_images/imageFile306.png>)

![image 307](<2017-glock-hypergraph-designs-arbitrary_images/imageFile307.png>)

![image 308](<2017-glock-hypergraph-designs-arbitrary_images/imageFile308.png>)

![image 309](<2017-glock-hypergraph-designs-arbitrary_images/imageFile309.png>)

![image 310](<2017-glock-hypergraph-designs-arbitrary_images/imageFile310.png>)

![image 311](<2017-glock-hypergraph-designs-arbitrary_images/imageFile311.png>)

![image 312](<2017-glock-hypergraph-designs-arbitrary_images/imageFile312.png>)

![image 313](<2017-glock-hypergraph-designs-arbitrary_images/imageFile313.png>)

![image 314](<2017-glock-hypergraph-designs-arbitrary_images/imageFile314.png>)

![image 315](<2017-glock-hypergraph-designs-arbitrary_images/imageFile315.png>)

This yields a ρℓ−1/12-well separated F-packing Fℓ† in Gℓ,clean covering all T i′-important edges of G(ℓ,cleanr) = Jℓ′ = Hℓ∗ − Fℓ∗−(r1) − Fℓ◦(r) . Thus Fℓ† is as required in (COV2). As observed before, this completes the proof of (#)ℓ+1 and thus the proof of (i).

Proof of (ii).

Let Y ⊆ G(f) and A ∈ [0,1](r+1)×(f+1) be such that (S1)–(S4) hold. We assume that G(r) is F-divisible with respect to S,U and that A is diagonal-dominant.

Claim 6: G is (ξ − ε,f,r)-dense with respect to G(r) − τr−1(0).

Proof of claim: Let e ∈ G(r) and let ℓ′ ∈ [r+1] be such that e ∈ Pr(ℓ′). Suppose ﬁrst that ℓ′ ≤ i. Then no f-set from Pf(ℓ′) contains any edge from τr−1(0) (as such an f-set is S-unimportant). Recall from (S2) for S,U,(Pr,Pf) that G[Y ] is (ε,A,f,r)-regular with respect to (Pr,Pf[Y ]) and min\\r−i+1(A) ≥ ξ. Thus,

|G[(G(r) − τr−1(0)) ∪ e](f)(e)| ≥ |(Y ∩ Pf(ℓ′))(e)| ≥ (aℓ′,ℓ′ − ε)nf−r ≥ (ξ − ε)nf−r.

If ℓ′ > i + 1, then by (P2′) in Proposition D.11, no f-set from Pf(f − r + ℓ′) contains any edge from τr−1(0). Thus, we have

|G[(G(r) − τr−1(0)) ∪ e](f)(e)| ≥ (aℓ′,f−r+ℓ′ − ε)nf−r ≥ (ξ − ε)nf−r.

If ℓ′ = i + 1, then Pr(ℓ′) = τr−1(0) by (P2′). However, every f-set from τf−1(f − r) = Pf(f − r + ℓ′) that contains e contains no other edge from τr−1(0). Thus,

|G[(G(r) − τr−1(0)) ∪ e](f)(e)| ≥ (aℓ′,f−r+ℓ′ − ε)nf−r ≥ (ξ − ε)nf−r.

−

By Claim 6, we can choose H∗ ⊆ G(r) − τr−1(0) such that (i) holds with G playing the role of G˜. Let

Hnibble := G(r) − H∗.

Recall that by (S2), G[Y ] is (ε,A,f,r)-regular with respect to (Pr,Pf[Y ]), and (S3) implies that G[Y ] is (µfξ,f + r,r)-dense. Let

Gnibble := (G[Y ])[Hnibble].

Using Proposition A.1, it is easy to see that Gnibble is (2r+1ν,A,f,r)-regular with respect to (Pr,Pf)[Gnibble]. Moreover, by Proposition 4.5(ii), Gnibble is (µfξ/2,f + r,r)-dense. Thus, by

Lemma D.14, there exists Y ∗ ⊆ Gnibble(f) such that Gnibble[Y ∗] is (√ν,d,f,r)-regular for d := min\(A) ≥ ξ and (0.45µfξ(µfξ/8(f + 1))(f+fr),f + r,r)-dense. Thus, by Lemma 5.3 there is a κ-well separated F-packing Fnibble in Gnibble[Y ∗] such that ∆(Lnibble) ≤ γn, where Lnibble := Gnibble[Y ∗](r) − Fnibble(r) = Hnibble − Fnibble(r) . Since G(r) is F-divisible with respect to S,U, we clearly have that H∗ ∪Lnibble = G(r) −Fnibble(r) is F-divisible with respect to S,U. By Fact 4.3(i), we have that ∆(Fnibble≤(r+1)) ≤ κ(f − r) ≤ γn. Thus, by (i), there exists a κ-well separated Fpacking F∗ in G[H∗ ∪ Lnibble] − Fnibble≤(r+1) which covers all edges of Lnibble, and all S-important edges of H∗ except possibly some from τr−1(r − i). But then, by Fact 4.3(ii), Fnibble ∪ F∗ is a 2κ-well separated F-packing in G which covers all S-important r-edges except possibly some from τr−1(r − i), completing the proof.

![image 316](<2017-glock-hypergraph-designs-arbitrary_images/imageFile316.png>)

This completes the proof of Lemma D.21.

Stefan Glock, Daniela Ku¨hn, Allan Lo, Deryk Osthus School of Mathematics University of Birmingham Edgbaston Birmingham B15 2TT UK

E-mail addresses: [sglock,d.kuhn,s.a.lo,d.osthus]@bham.ac.uk

