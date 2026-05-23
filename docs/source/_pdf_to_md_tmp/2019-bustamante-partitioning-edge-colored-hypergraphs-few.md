arXiv:1903.04471v2[math.CO]9Jul2020

# Partitioning edge-coloured hypergraphs into few monochromatic tight cycles*

Sebastián Bustamante Jan Corsten Nóra Frankl Alexey Pokrovskiy Jozef Skokan

10th July 2020

Conﬁrming aconjectureof Gyárfás, we prove that, for all naturalnumbersk and r, the vertices of every r-edge-coloured complete k-uniform hypergraph can be partitioned into a bounded number (independent of the size of the hypergraph) of monochromatic tight cycles. We further prove that, for all natural numbersp andr, the vertices of everyr-edge-colouredcomplete graph can be partitioned into a bounded number of p-th powers of cycles, settling a problem of Elekes, Soukup, Soukup and Szentmiklóssy. In fact we prove a common generalisation of both theorems which further extends these results to all host hypergraphs of bounded independence number.

## 1 Introduction and main results

A conjecture of Lehel states that the vertices of any 2-edge-coloured complete graph on n verticescanbe partitionedinto two monochromaticcycles of diﬀerentcolours. Heresingle vertices and edges are considered cycles. This conjecture ﬁrst appeared in [2], where it was also proved for some special types of colourings of Kn. Łuczak, Rödl and Szemerédi [14] proved Lehel’s conjecture for all suﬃciently large n using the regularity method. In [1], Allen gave an alternative proof, which gave a better bound on n. Finally, Bessy and Thomassé [3] proved Lehel’s conjecture for all integers n ≥ 1.

For colourings with more than two colours (all colourings in this paper are edgecolourings), Erdős, Gyárfás and Pyber [7] proved that the vertices of every r-coloured complete graph can be partitioned into O(r2 logr) monochromatic cycles and conjectured that r cycles should always suﬃce. Their conjecture was refuted by Pokrovskiy [15], who showed that, for every r ≥ 3, there exist inﬁnitely many r-coloured complete graphs

![image 1](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile1.png>)

∗Published in SIAM J. Discrete Math. 34 (2020), no. 2, 1460–1471, DOI: 10.1137/19M1269786, © 2020. This manuscript version is made available under the CC-BY-NC-ND 4.0 license.

which cannot be vertex-partitioned into r monochromatic cycles. Pokrovskiy also proposed the following alternative version of Erdős, Gyárfás and Pyber conjecture, which is still widely open.

Conjecture 1.1 (Pokrovskiy [15]). In every r-edge-coloured complete graph, there are r vertex-disjoint monochromatic cycles covering all but cr vertices, where cr is a constant depending only on r.

The best-known result for general r is due to Gyárfás, Ruszinkó, Sárközy and Szemerédi [10], who showed that the vertices of every large enough r-coloured complete graph can be partitioned into at most 100r logr monochromatic cycles.

Similar partitioning problems have been considered for other graphs, for example, powers of cycles. Given a graph H and a natural number p, the p-th power of H is the graph obtained from H by putting an edge between any two vertices whose distance is at most p in H. Grinshpun and Sárközy [8] proved that the vertices of every two-coloured complete graph can be partitioned into at most 2cp logp monochromatic p-th powers of cycles, where c is an absolute constant. They conjectured that a much smaller number of pieces should suﬃce, which was conﬁrmed by Sárközy [20]. For more than two colours not much is known. Elekes, D. Soukup, L. Soukup and Szentmiklóssy [6] proved an analogue of the result of Grinshpun and Sárközy for inﬁnite graphs and multiple colours and asked whether it is true for ﬁnite graphs.

Problem 1.2 (Elekes et al. [6, Problem 6.4]1). Prove that for every r,p ∈ N, there is some c = c(r,p) such that the vertices of every r-edge-coloured complete graph can be partitioned into at most c monochromatic p-th powers of cycles.

We shall prove a substantial generalisation of this problem, see Corollary 1.5.

Another possible generalisation is to study questions about monochromatic partitions for hypergraphs. A k-uniform hypergraph (k-graph) consists of a vertex setV and a set of k-element subsets ofV. The loosek-uniform cycle of lengthm is thek-graph consisting of m(k − 1) cyclically ordered vertices and m edges, each edge formed of k consecutive vertices, so that consecutive edges intersect in exactly one vertex. The tight k-uniform cycle of length m is the k-graph with m cyclically ordered vertices in which any k consecutive vertices form an edge. Loose and tight paths are deﬁned in a similar way. For technical reasons we consider single vertices both as tight and loose cycles and paths.

Questions about monochromatic partitions for hypergraphs were ﬁrst studied by Gyárfás and Sárközy [11] who showed that for every k, r ∈ N, there is some c = c(k,r) so that the vertices of every r-edge-coloured complete k-graph can be partitioned into at most c loose cycles. Later, Sárközy [19] showed that c(k,r) can be be chosen to be 50rk log(rk). Gyárfás conjectured that a similar result can be obtained for tight cycles.

Conjecture 1.3 (Gyárfás [9]). For everyk,r ∈ N, there is somec = c(k,r) so that the vertices of every r-edge-coloured complete k-graph can be partitioned into at most c monochromatic tight cycles.

![image 2](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile2.png>)

- 1The problem is phrased diﬀerently in [6] but this version is stronger, as Elekes et al. explain below the problem.


We shall prove this conjecture and a generalisation in which we allow the host- hypergraph to be any k-graph with bounded independence number (i.e. without a large set of vertices containing no edges).

- Theorem 1.4. For every k,r,α ∈ N, there is some c = c(k,r,α) such that the vertices of every r-edge-coloured k-graph G with independence number α(G) ≤ α can be partitioned into at most c monochromatic tight cycles.


We note that a similar result for graphs was obtained by Sárközy [18], and for loose cycles in hypergraphs by Gyárfás and Sárközy [12].

As a corollary we obtain the following extension of Theorem 1.4 top-th powers of tight cycles. Here thep-th power of ak-uniform tight cycle is thek-graph obtained by replacing every edge of the (k + p − 1)-uniform tight cycle by the complete k-graph on k + p − 1 vertices.

Corollary 1.5. For every k,r,p,α ∈ N, there is some c = c(k,r,p,α) such that the vertices of every r-edge-coloured k-graph G with α(G) ≤ α can be partitioned into at most c monochromatic p-th powers of tight cycles.

Since Corollary 1.5 follows from Theorem 1.4 easily, we present its short proof here.

Proof of Corollary 1.5. For positive integers k,r,s1, . . .,sr, let Rr(k)(s1, . . .,sr) denote the rcolour Ramsey number fork-graphs, that is the smallest positive integern, so that in every

r-colouring of the complete k-graph on n vertices, there is some i ∈ [r] and si distinct vertices which induce a monochromatic clique in colour i.

Let f (k,r,α) be the smallest c for which Theorem 1.4 is true and let (k,r,p,α) be the smallestc for which Corollary 1.5 is true. We will show that (k,r,p,α) ≤ f (k+p−1,r,α˜), where α˜ = Rr(k+)1 (k +p − 1, . . .,k + p − 1,α + 1)−1. Suppose now we are given an r-edgecoloured k-graph G with α(G) ≤ α. Deﬁne a (k + p − 1)-graph H on the same vertex-set whose edges are the monochromatic cliques of sizek+p−1 inG. By construction we have α(H) ≤ α˜ and thus, by Theorem 1.4, there are at most f (k + p − 1,r,α˜) monochromatic tight cycles partitioning V(H). To conclude, note that a tight cycle in H corresponds to a p-th power of a tight cycle in G.

In the next section, we shall prove Theorem 1.4.

## 2 The proof of Theorem 1.4

The proof of Theorem 1.4 combines the absorption method introduced in [7] and the regularity method. For the complete host k-graph G, the proof of Theorem 1.4 can be summarised as follows.

First, we ﬁnd a monochromatic k-graph H0 ⊂ G with the following special property: There is some B ⊂ V(H0), so that for every B′ ⊂ B there is a tight cycle in H0 with vertices V(H0) \ B′. This is explained in Section 2.3. We then greedily remove vertex-disjoint

monochromatic tight cycles from V(G) \ V(H0) until the set of leftover vertices R is very small in comparison to B. Finally, in Section 2.4, we show that the leftover vertices can be absorbed by H0. More precisely, we show that there are constantly many vertex-disjoint tight cycles with vertices in R∪B which cover all of R. This is the crucial part of the paper and also the place where we use tools from the hypergraph regularity method (introduced in Section 2.2).

In order to prove the main theorem for hostk-graphs with bounded independence number, we need to iterate the above process a few times. Here the main diﬃculty is to show that the iteration process stops after constantly many steps. This will be shown in Section 2.5. We start with some basic notation about hypergraphs.

### 2.1 Notation

For a set of vertices V and a natural number k ≥ 2, let Vk denote the set of all k-element subsets of V. Given a subset E ⊂ Vk , H = (V,E) is called a k-uniform hypergraph (kgraph). We sometimes use the notation H = (V(H),E(H)). The density of a k-graph H with n vertices is given by d(H) = |E(H)|/ nk .

Let H be a k-graph. Given some e ⊂ V(H) with 1 ≤ |e| ≤ k, we deﬁne its degree of e by deg(e) := |f ∈ E(H) : e ⊂ f |. If |e| = 1 for some ∈ V(H) we simply write deg( ) for deg({ }) and if |e| = k − 1, we call deg(e) co-degree. Given a partition P = {V1, . . .,Vt} of V, we say that H is P-partite if |e ∩ Vi| ≤ 1 for every e ∈ E(H) and every i ∈ [t]. The k-graph H is s-partite if it is P-partite for some partition P of V with s parts. We denote by K(k)(P) the complete P-partite k-graph. Furthermore, given some 2 ≤ j ≤ k − 1 and a

- j-graph H, we deﬁne K(k)(H) to be the set of all k-cliques in H(j), seen as a k-graph on V. Given a k-graph H and ℓ ≤ k distinct vertices 1, . . ., ℓ ∈ V(H), we deﬁne the link-


graph LkH( 1, . . ., ℓ) as the (k −ℓ)-graph on V(H) \ { 1, . . ., ℓ} with edges {e ∈ Vk(−Hℓ) : e ∪ { 1, . . ., l} ∈ E(H)}. If, in addition, disjoint sets V1, . . .,Vk−ℓ ⊂ V(H) \ { 1, . . ., ℓ} are given, we denote by LkH( 1, . . ., ℓ;V1, . . .,Vk−ℓ) the (k −ℓ)-partite (k −ℓ)-graph with parts V1, . . .,Vk−ℓ and edges {e ∈ K(k−ℓ)(V1, . . .,Vk−ℓ) : e ∪ { 1, . . ., ℓ} ∈ E(H)}. If there is no danger of confusion, we drop the subscript H.

### 2.2 Finding short paths

The goal of this section is to prove the following lemma, which allows us to ﬁnd in any dense k-graph G, a dense subgraph H ⊂ G in which any two non-isolated (k − 1)-sets are connected by a short path of a given prescribed length. For this, we need to use basic tools from hypergraph regularity, but the reader may use Lemma 2.1 as a black box if she would like to avoid it.

Before stating the lemma, we need to introduce some notation. Fix some k ≥ 2 and a partition P = {V1, . . .,Vk}. We call a tight path in K(k)(P) positively oriented if its vertex sequence (u1, . . .,um) travels through P in cyclic order, i.e. there is some j ∈ [k] such that ui ∈ Vi+j for every i ∈ [m], where we identify k + 1 ≡ 1. In this subsection, we will

only consider positively oriented tight cycles. In particular, given some e ∈ K(k−1)(P), the ordering of e in a tight path starting at e is uniquely determined.

Lemma 2.1. For every d > 0, there are constants δ = δ(d) > 0 and γ = γ(d) > 0, such that the following is true for every partition P = {V1, . . .,Vk} and every P-partite k-graph G of density at least d. There is a P-partite sub-k-graph H ⊂ G of density at least δ such that for every set S = S1 ∪ . . . ∪ Sk with Si ⊂ Vi and |Si| ≤ γ |Vi| and any two e, f ∈ K(k−1)(P) which are disjoint from S and have positive co-degree, there is a positively oriented tight path of length ℓ ∈ {k + 2, . . ., 2k + 1} in H which starts at e, ends at f and avoids S.

Note that the length of the cycle in Lemma 2.1 is uniquely determined by the types of e and f . The type of e ∈ K(k−1)(P), denoted by tp (e), is the unique index i ∈ [k] such that e ∩ Vi = ∅. Given two (k − 1)-sets e, f ∈ K(k−1)(P), the type of (e, f ) is given by tp (e, f ) := tp (f ) − tp (e)(mod k). It is easy to see that every tight path in K(k)(P) which starts ate and ends at f has length ℓk+tp (e, f ) for some ℓ ≥ 0. In particular, in Lemma 2.1, we have ℓ = k + tp(e, f ) if tp(e, f ) ≥ 2 and ℓ = 2k + tp(e, f ) otherwise.

#### 2.2.1 Hypergraph regularity

We will now introduce the basic concepts of hypergraph regularity in order to state a simple consequence of the strong hypergraph regularity lemma which guarantees a dense regular complex in every large enough k-graph.

For technical reasons, we want to see a 1-graph on some vertex-setV as a partition ofV in what follows. We call H(k) = (H(1), . . .,H(k)) a k-complex if H(j) is a j-graph for every j ∈ [k] and H(j) underlies H(j+1), i.e. H(j+1) ⊂ K(j+1)(H(j)) for every j ∈ [k − 1]. Note that, in particular, H(j) is H(1)-partite for every j ∈ [k]. We call H(k) s-partite if H(1) consists of s parts.

Now, given some j-graph H(j) and some underlying (j − 1)-graph H(j−1), we deﬁne the density of H(j) w.r.t. H(j−1) by

H(j) ∩ K(j)(H(j−1)) K(j)(H(j−1))

d H(j)|H(j−1) =

.

![image 3](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile3.png>)

We are now ready to deﬁne regularity. Deﬁnition 2.2.

- • Let r, j ∈ N with j ≥ 2, ε,dj > 0, and H(j) be a j-partite j-graph and H(j−1) be an underlying (j-partite) (j − 1)-graph. We call H(j) (ε,dj,r)-regular w.r.t. H(j−1) if for all Q1(j−1), . . .,Qr(j−1) ⊂ E(H(j−1)), we have


i∈[r] K(j) Qi(j−1) ≥ ε K(j) H(j−1) =⇒ d H(j) i∈[r] Qi(j−1) − dj ≤ ε.

We simply say (ε, ∗,r)-regular for (ε, d H(j)|H(j−1) ,r)-regular and (ε,d)-regular for (ε,d, 1)-regular.

- • Let j,s ∈ N with s ≥ j ≥ 2, ε,dj > 0, and H(j) be an s-partite j-graph and H(j−1) be an underlying (s-partite) (j − 1)-graph. We call H(j) (ε,dj)-regular w.r.t. H(j−1) if H(j)[V1, . . .,Vj] is (ε,dj)-regular w.r.t. H(j−1)[Vi1, . . .,Vij] for all 1 ≤ i1 < . . . < ij ≤ s, where {V1, . . .,Vs} is the vertex partition of V(H(j)).
- • Let k,r ∈ N, ε,εk,d2, . . .,dk > 0, and H(k) = (H1, . . .,Hk) be a k-partite k-complex. We callH(k) (d2, . . .,dk,ε,εk,r)-regular, ifH(j) is (ε,dj)-regular with respecttoH(j−1) for every j = 2, . . .,k − 1 and H(k) is (εk,dk,r)-regular w.r.t. H(k−1).


The following theorem is a direct consequence of the strong hypergraph regularity lemma as stated in [17] (with the exception that we allow for an initial partition of not necessarily equal sizes).

- Theorem 2.3. For all integers k ≥ 2, constants εk > 0, and functions ε : (0, 1) → (0, 1) and r : (0, 1) → N, there exists some δ = δ(k,ε,εk,r) > 0 such that the following is true. For every partition P = {V1, . . .,Vk} of some set V and every P-partite k-graph G(k) of density d ≥ 2εk, there are sets Ui ⊂ Vi with |Ui| ≥ δ |Vi| for every i ∈ [k] and constants d2, . . .,dk−1 ≥ δ and dk ≥ d/2 for which there exists some (d2, . . .,dk,ε(δ),εk,r(δ))-regular


- k-complex H(k), so that H(1) = {U1, . . .,Uk}.


We will use the following special case of the extension lemma in [5, Lemma 5] to ﬁnd short tight paths between almost any two (k − 1)-sets in a regular complex. Fix a (d2, . . .,dk,ε,εk)-regular complex H(k) = (P,H(2), . . .,H(k)), where P = {V1, . . .,Vk}. Let Hi(k−1) ⊂ H(k−1) denote the edges of type i and note that the dense counting lemma for complexes [5, Lemma 6] implies that

Hi(k−1)

0

k−1

= (1 ± ε)

j=2

(k−j1)

|Vi| .

d

j

i∈[k]\i0

×Hi(k−1)

Given some β > 0, we call a pair (e, f ) ∈ Hi(k−1)

β-typical for H(k) if the number of tight paths of length ℓ := k + tp (i1,i2) in H(k) which start at e and end at f is

2

1

k

(1 ± β)

j=2

(kj−−11)−(k−j1) j

dℓ

|Vi| ,

i∈{i1,...,i2}

where {i1, . . .,i2} is understood in cyclic ordering. Note here that the number of j-sets in a k-uniform tight path of length ℓ which are contained in an edge is ℓ kj−−11 + k−j 1 . However, 2 k−j 1 of these are contained in e (the ﬁrst k − 1 vertices) or f (the last k − 1 vertices), which are already ﬁxed in our example.

- Lemma 2.4. Let k,r,n0 ∈ N, β,d2, . . .,dk,ε,εk > 0 and suppose that 1/n0 ≪ 1/r,ε ≪ min{εk,d2, . . .,dk−1} ≤ εk ≪ β,dk, 1/k.


Then the following is true for all integers n ≥ n0, for all indices i1,i2 ∈ [k] and every (d2, . . .,dk,ε,εk,r)-regular complex H(k) = H(1), . . .,H(k) with |Vi| ≥ n0 for all i ∈ [k],

where H(1) = {V1, . . .,Vk}. All but at most β Hi(k−1)

1

are β-typical for H(k).

Hi(k−1)

2

× Hi(k−1)

pairs (e, f ) ∈ Hi(k−1)

2

1

Combining Theorem 2.3 and Lemma 2.4 gives Lemma 2.1. Proof-sketch of Lemma 2.1. Apply Theorem 2.3 with suitable constants and delete all e ∈ H(k−1) of small co-degree. Let e ∈ Hi(k−1)

and f ∈ Hi(k−1)

for some i1,i2 ∈ [k] and deﬁne

2

1

- X = (k−1) ∈ Hi(k−1)

1+1 : e ∪ (k−1) ∈ H(k) and

- Y = (k−1) ∈ Hi(k−1)


2−1 : f ∪ (k−1) ∈ H(k) .

LetX˜ ⊂ X andY˜ ⊂ Y be the sets of all those edges in X andY avoidingS. By Lemma 2.4 at least one pair in X˜ ×Y˜ must be typical and by a counting argument not all of the promised paths can touch S.

### 2.3 Absorption Method

The idea of the absorption method is to ﬁrst cover almost every vertex by vertex-disjoint monochromatic tight cycles and then absorb the leftover using a suitable absorption lemma.

- Lemma 2.5. For all k,r,α ∈ N and every γ > 0, there is some c = c(k,r,α,γ) so that the following is true for every r-coloured k-graph G on n vertices with α(G) ≤ α. There is a collection of at most c vertex-disjoint monochromatic tight cycles whose vertices cover all but at most γn vertices.


Deﬁnition 2.6. LetG be a hypergraph, χ be a colouring of E(G) and A,B ⊂ V(G) disjoint subsets. A is called an absorber for B if there is a monochromatic tight cycle with vertices A ∪ B′ for every B′ ⊂ B.

Lemma 2.7. For every k,r,α ∈ N, there is some β = β(k,r,α) > 0 such that the following is true for every k-graph G with α(G) ≤ α. In every r-colouring of E(G) there are disjoint sets A,B ⊂ V(G) with |B| ≥ β|V(G)| such that A absorbs B.

The following hypergraphwill function as our absorber. A very similar hypergraphwas used by Gyárfás and Sárközy to absorb loose cycles [11, 12]. See Figure 1 for an example.

Deﬁnition 2.8. The (k-uniform) crown of order t, Tt(k), is a tight cycle with n = t(k − 1) vertices 0, . . ., n−1 (the base) and additional verticesu0, . . .,ut−1 (the rim). Furthermore, for eachi = 0, . . .,t −1, we add thek edges {ui, (k−1)i+j, . . ., (k−1)i+j+k−2}, j = 0, . . .,k−1.

- Figure 1: A 3-uniform crown of order 4. The edges of the tight cycle are red and the remaining edges are blue.


It is easy to see that the base of a crown is an absorber for the rim. To prove Lemma 2.7, we therefore only need to show that we can always ﬁnd monochromatic crowns of linear size. Both this and Lemma 2.5 are consequences of the following theorem of Cooley, Fountoulakis, Kühn, and Osthus [5] (see also [13] and [4]).

Theorem 2.9. For everyr,k, ∆ ∈ N, there is someC = C(r,k, ∆) > 0 so that the following is true for all k-graphs H1, . . .,Hr with at most n vertices and maximum degree at most ∆, and every N ≥ Cn. In every edge-colouring of KN(k) with colours c1, . . .,cr, there is some i ∈ [r] for which there is a ci-monochromatic copy of Hi.

Proof of Lemma 2.7. Suppose k,r,α and G are given as in the theorem and that E(G) is coloured with r colours. Let N = |V(G)|, ∆ := max 2k, k α−1 and c = 1/((k − 1)C) where C = C(r + 1,k, ∆) is given by Theorem 2.9. Furthermore, let n = V(TcN(k)) = N/C. Consider now the (r + 1)-colouring of E KN(k) in which every edge in E(G) receives the same colour as in G and every other edge receives colour r + 1. Let Hr+1 = Kα(k+)1 and Hi = TcN(k) for all i ∈ [t], and note that ∆(Hi) ≤ ∆ for all i ∈ [r + 1]. By choice of ∆, there is no monochromaticHr+1 in colourr +1 and hence, since N ≥ Cn, there is a monochromatic copy of Hi for some i ∈ [r]. Therefore, there is a monochromatic crown of size c|V(G)| and its base is an absorber for its rim.

Proof of Lemma 2.5. Applying Theorem 2.9 with r + 1 colours, uniformity k, maximum degree ∆ = max{k, k α−1 }, andH1 = . . . = Hr being tight cycles onn/(CThm 2.9(r +1,k, ∆))

vertices and Hr+1 = Kα(k+)1 gives the following. There exist some ε = ε(r,k,α) so that in every r-coloured k-graph G on n vertices with α(G) ≤ α, there is a monochromatic tight

cycle on at least εn vertices.2 By iterating this process i times, we ﬁnd i vertex-disjoint monochromatic tight cycles covering all but (1 − ε)in vertices. This ﬁnishes the proof, since (1 − ε)i → 0 as i → ∞.

- 2.4 Absorption Lemma In this section we prove a suitable absorption lemma for our approach.


Lemma 2.10. For every ε > 0 and k,r ∈ N, there is some γ = γ(k,r,ε) > 0 and some c = c(k,r,ε) such thatthefollowingis true. LetH beak-partitek-graph with partsB1, . . .,Bk such that |B1| ≥ . . . ≥ |Bk−1| ≥ |Bk|/γ and |Lk( ;B1, . . .,Bk−1)| ≥ ε|B1| · · ··|Bk−1| for every

∈ Bk. Then, in every r-colouring of E(H), there are c vertex-disjoint monochromatic tight cycles covering Bk.

Note that it is enough to cover all but a bounded number of vertices, since we allow single vertices as tight cycles. We will make use of this in the proof and frequently remove few vertices.

We will use the following theorem of Pósa [16].

Theorem 2.11 (Pósa). In every graph G, there is a collection of at most α(G) cycles whose vertices partition V(G).

We further need the following simple but quite technical lemma, which states that, given a ground set X and a collection F of subsets of X of linear size, we can group almost all of these subsets into groups of size 4 which have a large common intersection. We will apply this lemma when X is the edge-set of a hypergraph G and F is a collection of subgraphs of G.

Lemma 2.12. For every ε > 0 there is some δ = δ(ε) > 0 and some C = C(ε) > 0 such that the following is true for every m ∈ N. Let X be set of size m and F ⊂ 2X be a family of subsets such that |F| ≥ εm for every F ∈ F . Then there is some G ⊂ F of size |G| ≤ C and a partition P of F \G into sets of size 4 such that i 4=1 Bi ≥ δm for every {B1,B2,B3,B4} ∈ P.

We will prove the lemma with δ(ε) = e4/26 and C(ε) = 8/ε2 + 2/ε.

Proof. Deﬁne a graph G on F by {F1, F2} ∈ E(G) if and only if |F1 ∩ F2| ≥ (ε/2)2m. We claim that α(G) ≤ 2/ε. Suppose for contradiction that there is an independent set I of size

2/ε + 1. Then we have |F0 \ F∈I\{F0} F| ≥ εm/2 for every F0 ∈ I and hence | F∈I F| > m, a contradiction.

Since every graph has a matching of size at least (G)−α(G), we ﬁnd a matching P1 in

- G of all but at most 2/ε vertices of G (i.e. F ∈ F). Let G1 = F \ V(P1) and note that P1 is a partition of F \ G1 into sets of size 2. Let F1 = {F1 ∩ F2 : {F1, F2} ∈ P1} and iterate the process once more.


u1,1 u1,2 u2,1 u2,2 u3,1 u3,2 u1,1 u1,2

v1 v2 v3

(a) Link graphs

u1,1 u1,2 u2,1 u2,2 u3,1 u3,2 u1,1 u1,2

![image 4](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile4.png>)

![image 5](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile5.png>)

![image 6](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile6.png>)

![image 7](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile7.png>)

![image 8](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile8.png>)

v1 v2 v3

(b) Tight Cycle

- Figure 2: A sketch of Observation 2.13 fork = t = 3. Figure (a) shows the link graphs of 1 (blue), 2 (red) and 3 (green). The colours are for demonstration purposes only and are not related to the given edge-colouring. Figure (b) shows the resulting


tight cycle. In both ﬁgures, we identify the ends (u1,1 and u1,2) to simplify the drawing.

Proof of Lemma 2.10. By choosing γ small enough, we may assume that |B1|, . . ., |Bk−1| are suﬃciently large for the following arguments. First we claim that it suﬃces to prove

the lemma for r = 1. Indeed, partition Bk = Bk,1 ∪ . . . ∪ Bk,r so that for each i ∈ [r] and ∈ Bk,i, we have |Lki( ;B1, . . .,Bk−1)| ≥ ε/r·|B1| · · · |Bk−1| and delete all edges containing whose colour is not i. (Here we denote by Lki(·) the link graph with respect to Gi, the

graph with all edges of colour i.) Next, for each j ∈ [k − 1], partition Bj = Bj,1 ∪ . . . ∪ Bj,r into sets of equal sizes so that | Lki( ;B1,i, . . .,Bk−1,i)| ≥ ε/(2r) · |B1,i| · · · |Bk−1,i|. Such a partition can be found for example by choosing one uniformly at random and applying the probabilistic method). Finally, we can apply the one-colour result (with ε′ = ε/(2r)) for each i ∈ [r].

Fix ε > 0, k ≥ 2 and a k-partite k-graph H with parts B1, . . .,Bk as in the statement of the lemma. Choose constants γ,δ1,δ2,δ3 > 0 so that 0 < γ ≪ δ3 ≪ δ2 ≪ δ1 ≪ ε, 1/k. We begin with a simple but important observation.

Observation 2.13. Let 1, . . ., t ∈ Bk be distinct vertices and C be a tight cycle in K(k−1) (B1, . . .,Bk−1) with vertex-sequence (u1,1, . . .,u1,k−1, . . .,ut,1, . . .,ut,k−1). Denote by es,i the edge in C starting at us,i and suppose that

![image 9](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile9.png>)

2Here, we treat non-edges as colour r + 1 again.

- (i) es,i ∈ Lk( s;B1, . . .,Bk−1) for every s ∈ [t] and every i ∈ [k − 1] and
- (ii) es,1 ∈ Lk( s−1;B1, . . .,Bk−1) for every s ∈ [t] (here 0 := t).


Then, (u1,1, . . .,u1,k−1, 1, . . .,ut,1, . . .,ut,k−1, t) is the vertex-sequence of a tight cycle in H.

The proof of Observation 2.13 follows readily from the deﬁnition of the link graphs. See Figure 2 for an overview. We will now proceed in three steps. For simplicity, we write

- H := LkH( ;B1, . . .,Bk−1) for ∈ Bk.


- Step 1 (Divide into blocks). By Lemma 2.12, there is some C = C(ε) ∈ N and a partition P of all but C graphs from {H : ∈ Bk} into blocks H of size 4 with e(H) := | H∈H E(H)| ≥ δ1|B1| · · · |Bk−1| for every H ∈ P. Remove the C leftover vertices from Bk.

Think of every block H now as a (k − 1)-graph with edges E(H) := H∈H E(H). By applying Lemma 2.1 (withk−1 instead ofk), for each H ∈ P, we ﬁnd a subgraph H′ ⊂ H such that e(H′) ≥ δ2 |B1| · · · |Bk−1| with the same property as in Lemma 2.1. By deleting all the edges of H \ H′ we may assume that H itself has this property.

- Step 2 (Cover blocks by paths). Deﬁne an auxiliary graph G with V(G) = P and {H1, H2} ∈ E(G) if and only if e(H1 ∩ H2) ≥ δ3|B1| · · · |Bk−1|. Similarly as in the proof of Lemma 2.12, we conclude that α(G) ≤ 2/δ2, and hence V(G) can be covered by 2/δ2 vertex-disjoint paths using Theorem 2.11.
- Step 3 (Lift to tight cycles). This step is the crucial part of the argument. To make it easier to follow the proof, Figure 3 provides an example for k = t = 4.


We will ﬁnd in each path of blocks an auxiliary tight cycle in K(k−1)(B1, . . .,Bk−1) of the desired form to apply Observation 2.13. Let P = (H1, . . ., Ht) be one of the paths. Choose disjoint edges e0 = x1(0), . . .,xk(0−)1 ∈ E(H1) and et = x1(t), . . .,xk(t−)1 ∈ E(Ht). For each s ∈ [t −1], further choose two edges es = x1(s), . . .,xk(s−)1 ∈ E(Hs)∩E(Hs+1) and es′ = 1 (s), . . ., k (s−)1 ∈ E(Hs) ∩ E(Hs+1) so that all chosen edges are pairwise disjoint. We identify xi(0) = i (0) and xi(s) = i (s) for every i ∈ [k − 1], and e0 = e0′ and et = et′. Assume without loss of generality, that xi(s) ∈ Bi for every i ∈ [k − 1] and all s = 0, . . .,t.

By construction, every block H has the property guaranteed in Lemma 2.1. Therefore, for every s ∈ [t], there is a tight path Ps ⊂ Hs of length 2k − 3 which starts at (x2(s−1), . . .,xk(s−−11)), ends at (x1(s), . . .,xk(s−)2) and (internally) avoids all previously used vertices.3 Similarly, there is for everys ∈ [t] a tight pathQs ⊂ Hs of length 2k−3 which starts at and ( 1 (s), . . ., k (s−)2), ends at ( 2 (s−1), . . ., k (s−−11)) and (internally) avoids all previously used vertices.

Let U ⊂ Bk be the set of vertices for which H ∈ Hi for some i ∈ [t]. To ﬁnish the proof, we want to apply Observation 2.13 to cover U. Label U = { 1, . . ., 4t} so that

![image 10](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile10.png>)

3Note that the number of previously used vertices in Vj is at most γ|Vj| for every j ∈ [k − 1] since every tight cycle in G uses the same number of vertices from each part.

###### H1 H2 H3 H4

e3

e1

e2

- x1(1)

- x2(1)

- x3(1)

y1(1) y2(1)

- y3(1)






x1(2) x2(2) x3(2)

x1(3) x2(3) x3(3)

e0

e4

x1(0) = y1(0) x2(0) = y2(0) x3(0) = y3(0)

x1(4) = y1(4) x2(4) = y2(4) x3(4) = y3(4)

e3′

e1′

e2′

- y1(2)
- y2(2)
- y3(2)


- y1(3)
- y2(3)
- y3(3)


v1,v2,v15,v16 v3,v4,v13,v14 v5,v6,v11,v12 v7,v8,v9,v10

(a) A path of blocks.

e0 e4

- (x1(0),x2(0),x3(0)) (x1(1),x2(1),x3(1))

e1 P1

(x1(2),x2(2),x3(2))

e2 P2

(x1(3),x2(3),x3(3))

e3 P3

(x1(4),x2(4),x3(4))

P4

- (y1(0),y2(0),y3(0)) (y1(1),y2(1),y3(1)) Q1 e1′


= =

(y1(2),y2(2),y3(2)) Q2 e2′

(y1(3),y2(3),y3(3)) Q3 e3′

(y1(4),y2(4),y3(4)) Q4

e0′ e4′

(b) Edge sequence of the auxiliary 3-uniform tight cycle.

v1 ∗ ∗ ∗ v2 x1(1) x2(1) x3(1) v3 ∗ ∗ ∗ v4 x1(2) x2(2) x3(2) v5 ∗ ∗ ∗ v6 x1(3) x2(3) x3(3) v7 ∗ ∗ ∗ v8

x3(0) x1(4)

| |
|---|


x2(0) x2(4)

x1(0) v16 ∗ ∗ ∗ v15 y3(1) y2(1) y1(1) v14 ∗ ∗ ∗ v13 y3(2) y2(2) y1(2) v12 ∗ ∗ ∗ v11 y3(3) y2(3) y1(3) v10 ∗ ∗ ∗ v9

x3(4)

(c) Vertex sequence of the resulting tight cycle.

- Figure 3: Finding a tightcycle in a pathof blocks whenk = t = 4. In Figure (c), ∗ represents an internal vertex of a path Pi or Qi.


H 2i+1,H 2i+2,H 4t−2i,H 4t−2i−1 ∈ Hi for all i = 0, . . .,t − 1. Consider now the tight cycle C in Kk−1 (B1, . . .,Bk−1) with edge sequence

e0′ = e0,P1,e1,P2,e2, . . .,Pt,et = et′,Qt, . . .,e1,Q1,e0′ = e0 (1)

and relabel V(C) so that it’s vertex sequence is (u1,1, . . .,u1,k−1, . . .,ut,1, . . .,u4t,k−1) (i.e. u1,i = xi(0) for i ∈ [k − 1], u2,1, . . .,u2,k−1 are the internal vertices of P14, u3,i = xi(1) for all i ∈ [3] and so on). By construction, C has the desired properties to apply Observation 2.13, ﬁnishing the proof. Note that it is important here that every block Hi has size 4 since we cover 2 vertices of every block “going forwards” and 2 vertices “going backwards”.

### 2.5 Proof of Theorem 1.4.

Fix α,r,n ∈ N and a k-graph G with α(G) ≤ α. Choose constants 0 < β,γ,ε ≪ max{α,r,k}−1 so that γ = γ(r,ε) works for Lemma 2.10 and β = β(α,r) works for

![image 11](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile11.png>)

4Note that all Pi and Qi have 3k − 5 vertices and hence k − 1 internal vertices.

Lemma 2.7. The proof proceeds in α steps (the initial k − 1 steps are done at the same time). No eﬀort is made to calculate the exact number of cycles we use, we only care that it is bounded (i.e. independent of n).

Step 1, ..., k-1. By Lemma 2.7, there is some B ⊂ [n] of size βn with an absorber Ak−1 ⊂ [n]. Partition B into k − 1 sets B1(k−1), . . .,Bk(k−−11) of equal sizes. By Lemma 2.5, there is a bounded number of vertex-disjoint monochromatic tight cycles in [n] \ (B ∪ Ak−1) so that the set Rk−1 of uncovered vertices in [n] \ (B ∪ Ak−1) satisﬁes |Rk−1| ≤ γ |B1(k−1)|. Let Rk′−1 ⊂ Rk−1 be the set of vertices with | Lk( ;B1(k−1), . . .,Bk(k−−11))| < ε|B1(k−1)| · · · |Bk(k−−11)| and letRk′′−1 = Rk−1\Rk′−1. ByLemma2.10 we can ﬁnd a bounded number of vertex-disjoint cycles in B1(k−1) ∪ . . . ∪ Bk(k−−11) ∪ Rk′′−1 covering Rk′′−1. Remove them and let Bi(k) ⊂ Bi(k−1) be the set of leftover vertices for every i ∈ [k − 1].

Step j (j = k, . . .,α). In each step j, we will deﬁne disjoint sets B1(j+1), . . .,Bj(j+1),R′j+1,Aj. Fix some j ∈ {k, . . .,α} now and suppose we have built disjoint sets B1(j), . . .,B(j−j)1,R′j and absorbers A2, . . .,Aj−1. By Lemma 2.7 there is some B(jj) ⊂ R′j of size β|R′j| with an absorber Aj ⊂ R′j. By Lemma 2.5, there is a bounded number of monochromatic tight cycles in R′j \(Aj ∪B(jj)) so that the set Rj+1 of uncovered vertices in R′j \(Aj ∪B(jj)) satisﬁes |Rj+1| ≤ γ |B(jj)|. Let R′j+1 ⊂ Rj+1 be the set of vertices with | Lk( ;Bt(j)

, . . .,Bt(j)

)| < ε Bt(j)

1

k−1

· · · Bt(j)

for all 1 ≤ t1 < . . . < tk−1 ≤ j and let R′′j+1 = Rj+1 \ R′j+1. By ( k j

1

k−1

applications of) Lemma 2.10 we can ﬁnd a bounded number of vertex-disjoint cycles in B1(j) ∪ . . . ∪ B(jj) ∪ R′′j covering R′′j . Remove them and let Bi(j+1) ⊂ Bi(j) be the set of leftover vertices for every i ∈ [j].

In the end we are left with disjoint sets B1 := B1(α+1), . . .,Bα := Bα(α+1),Bα+1 := Rα′ +1 and

corresponding absorbers Ak−1, . . .,Aα (Ak−1 absorbs B1(α+1), . . .,Bk(α−+11)). All other vertices are covered by a bounded number of cycles.

We will show now that Rα′ +1 = ∅, which ﬁnishes the proof. In order to do so, we assume

the contrary and ﬁnd an independent set of size α + 1. Note that every vertex in B(jj) \ Bj must be part of a tight cycle of our disjoint collection of tight cycles with one part in

Rj+1 and hence B(jj) \ Bj ≤ Rj+1 ≤ γ B(jj) . It follows that Bj ≥ (1 − γ) B(ji) for every 1 ≤ j ≤ i ≤ α and we conclude

, . . .,Bi(i−1)

Lk ;Bi1, . . .,Bik−1 ≤ Lk ;Bi(i−1)

1

k−1

· · · Bi(i−1)

≤ ε Bi(i−1)

1

k−1 ≤ ε(1 −γ)−(k−1) Bi1 · · · Bik−1 ≤ 2ε Bi1 · · · Bik−1

for every i ∈ {k, . . .,α + 1}, 1 ≤ i1 < . . . < ik−1 < i and ∈ Bi. By the following lemma, there is an independent set of size α + 1, a contradiction.

Lemma 2.14. For all k,m ∈ N there is some ε = ε(k,m) > 0 such that the following is true for every k-graph H and all non-empty, disjoint sets B1, . . .,Bm ⊂ V(H). If

Lk( ;Bi1, . . .,Bik−1) ≤ ε Bi1 · · · Bik−1 for all i ∈ {k, . . .,m}, 1 ≤ i1 < . . . < ik−1 < i and

∈ Bi, then there is an independent transversal, i.e. an independent set { 1, . . ., m} with i ∈ Bi for all i ∈ [m].

We will prove the lemma for ε(k,m) = m−(k−1)2. Proof. Let δ = m−(k−1) and ε = δk−1. Choose m ∈ Bm arbitrarily and assume now that

m, . . ., j+1 are chosen for some j ∈ [m − 1]. Given s ∈ {2, . . .,k − 1} and i = (i1, . . .,ik) with 1 ≤ i1 < . . . < is−1 < is = j < is+1 < . . . < ik ≤ m, deﬁne

Bj(s, i) := u ∈ Bj : Lk ik, . . ., is+1,u;Bis−1, . . .,Bi1 ≥ ε/δk−s Bi1 · · · Bis−1 . Furthermore, given i = (i1, . . .,ik) with j = i1 < i2 < . . . < ik ≤ m, deﬁne

![image 12](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile12.png>)

![image 13](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile13.png>)

Bj(1, i) := N ik, . . ., i2;Bi1 , the neighbourhood of { i2, . . ., ik} in Bi1. Note that, by choice of m, . . ., j+1, we have

Bj(s, i) < δ Bj for everys ∈ {2, . . .,k − 1} and Bj(1, i) < ε/δk−2 Bj = δ Bj . Since there

![image 14](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile14.png>)

![image 15](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile15.png>)

are at most mk−−11 < 1/δ choices for (s, i), we can choose some j ∈ Bj \ s,i Bj(s, i). Clearly, at the end of this process, { 1, . . ., m} will be independent.

![image 16](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile16.png>)

## References

- [1] P. Allen, Covering two-edge-colouredcomplete graphs with two disjoint monochromatic cycles, Combin. Probab. Comput. 17 (2008), no. 4, 471–486.
- [2] J. Ayel, Sur l’existence de deux cycles supplémentaires unicolores, disjoints et de couleurs diﬀérentes dans un graphe complet bicolore, Theses, Université Joseph-Fourier - Grenoble I, May 1979.
- [3] S. Bessy and S. Thomassé, Partitioning a graph into a cycle and an anticycle, a proof of lehel’s conjecture, J. Combin. Theory Ser. B 100 (2010), no. 2, 176–180.
- [4] D. Conlon, J. Fox, and B. Sudakov, Ramsey numbers of sparse hypergraphs, Random Structures & Algorithms 35 (2009), no. 1, 1–14.
- [5] O. Cooley, N. Fountoulakis, D. Kühn, and D. Osthus, Embeddings and Ramsey numbers of sparse κ-uniform hypergraphs, Combinatorica 29 (2009), no. 3, 263–297.
- [6] M. Elekes, D. T. Soukup, L. Soukup, and Z. Szentmiklóssy, Decompositions of edgecolored inﬁnite complete graphs into monochromatic paths, Discrete Math. 340 (2017), no. 8, 2053–2069.


- [7] P. Erdős, A. Gyárfás, and L. Pyber, Vertex coverings by monochromatic cycles and trees, J. Combin. Theory Ser. B 51 (1991), no. 1, 90–95.
- [8] A. Grinshpun and G. N. Sárközy, Monochromatic bounded degree subgraph partitions, Discrete Math. 339 (2016), no. 1, 46–53.
- [9] A. Gyárfás, Vertex covers by monochromatic pieces — a survey of results and problems, Discrete Math. 339 (2016), no. 7, 1970–1977.
- [10] A. Gyárfás, M. Ruszinkó, G. N. Sárközy, and E. Szemerédi, An improved bound for the monochromatic cycle partition number, J. Combin. Theory Ser. B 96 (2006), no. 6, 855–873.
- [11] A. GyárfásandG.N. Sárközy, Monochromaticpathand cyclepartitionsinhypergraphs, Electron. J. Combin. 20 (2013), no. 1, P18.
- [12] , Monochromatic loose-cycle partitions in hypergraphs, Electron. J. Combin. 21

![image 17](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile17.png>)

(2014), no. 2, P2–36.

- [13] Y. Ishigami, Linear Ramsey Numbers for Bounded-Degree Hypergraphs, Electr. Notes Discrete Math. 29 (2007), 47–51.
- [14] T. Łuczak, V. Rödl, and E. Szemerédi, Partitioning two-coloured complete graphs into two monochromatic cycles, Combin. Probab. Comput. 7 (1998), no. 4, 423–436.
- [15] A. Pokrovskiy, Partitioning edge-coloured complete graphs into monochromatic cycles and paths, J. Combin. Theory Ser. B 106 (2014), 70–97.
- [16] L. Pósa, On the circuits of ﬁnite graphs, Magyar Tud. Akad. Mat. Kutató Int. Közl 8

(1963), 355–361.

- [17] V. Rödl and M. Schacht, Regular Partitions of Hypergraphs: Regularity Lemmas, Combin. Probab. Comput. 16 (2007), no. 06.
- [18] G. N. Sárközy, Monochromatic cycle partitions of edge-colored graphs, J. Graph Theory 66 (2011), no. 1, 57–64.
- [19] , Improved monochromatic loose cycle partitions in hypergraphs, Discrete Math. 334 (2014), 52–62.

![image 18](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile18.png>)

- [20] , Monochromatic cycle power partitions, Discrete Math. 340 (2017), no. 2, 72– 80.


![image 19](<2019-bustamante-partitioning-edge-colored-hypergraphs-few_images/imageFile19.png>)

