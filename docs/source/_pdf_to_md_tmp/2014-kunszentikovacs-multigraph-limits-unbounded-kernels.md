arXiv:1406.7846v2[math.CO]28Oct2021

Multigraph limits, unbounded kernels, and Banach space decorated graphs

David´ Kunszenti-Kovacs´ ∗ Alfr´ed R´enyi Institute of Mathematics, Budapest, Hungary Laszl´ o´ Lovasz´ † Alfr´ed R´enyi Institute of Mathematics Institute of Mathematics, Eo¨tv¨os Lor´and University, Budapest, Hungary Balazs´ Szegedy‡ Alfr´ed R´enyi Institute of Mathematics, Budapest, Hungary

October 29, 2021

Abstract

We present a construction that allows us to deﬁne a limit object of Banach space decorated graph sequences in a generalized homomorphism density sense. This general functional analytic framework provides a universal language for various combinatorial limit notions. In particular it makes it possible to assign limit objects to multigraph sequences that are convergent in the sense of node-and-edge homomorphism numbers, and it generalizes the limit theory for graph sequences with compact decorations.

# Contents

- 1 Introduction 2
- 2 Decorated graphs and graphons 3

- 2.1 Decorated graphs and graphons . . . . . . . . . . . . . . . . . . . . . . . . . 3
- 2.2 Homomorphism densities . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
- 2.3 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
- 2.4 The jumble norm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
- 2.5 Counting Lemma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
- 2.6 The Weak Regularity Lemma . . . . . . . . . . . . . . . . . . . . . . . . . . 15


- 3 Convergence of Banach space valued graphons 17


- 3.1 Dense sets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
- 3.2 Moment sequences . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
- 3.3 Measure preserving transformations . . . . . . . . . . . . . . . . . . . . . . 20
- 3.4 Limit graphon . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
- 3.5 W-random decorated graphs . . . . . . . . . . . . . . . . . . . . . . . . . . 23


![image 1](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile1.png>)

∗Research supported by ERC Advanced Research Grant No. 227701, the Bolyai Research Grant of the Hungarian Academy of Sciences and ERC Consolidator Grant No. 648017.

†Research supported by ERC Advanced Research Grant No. 227701 and ERC Synergy Grant No. 810115.

‡Research supported by ERC Consolidator Grant No. 617747 and the Hungarian National Excellence Grant 2018-1.2.1-NKP-00008.

- 4 Convergence of multigraphs 24

- 4.1 Multigraphs as Banach decorated graphs . . . . . . . . . . . . . . . . . . . . 24
- 4.2 W-random multigraphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
- 4.3 Node-convergence vs. node-and-edge convergence . . . . . . . . . . . . . . . 30
- 4.4 Node-and-edge vs. sample convergence and exchangeability . . . . . . . . . 31


- 5 Concluding remarks 33


# 1 Introduction

The motivation for this paper was to provide a framework for a theory of convergence and limits of graphs with unbounded edge multiplicities, along the lines of the limit theory for dense simple graphs developed by Borgs, Chayes, Lov´asz, So´s and Vesztergombi [2, 3] and Lov´asz and Szegedy [10]. Key elements of this theory are the notions of cut distance and subgraph densities, the deﬁnitions of convergence and limit objects, the Regularity Lemma (in its weak form due to Frieze and Kannan [5]), along with the Counting Lemma.

In the paper [11] (posted on the Arxiv, but not published; see also [9], Section 17.1), the second and third authors worked out a theory of convergence and limits of simple graphs whose edges are decorated by points from some compact space. (Ordinary simple graphs can be considered as complete graphs with edges decorated by elements of a two-point space.) One could say that the theory of undecorated simple graphs extends to this case in a rather straightforward manner (at least as soon as the appropriate formulations are found). Edge-weighted graphs and multigraphs ﬁt in this framework, provided the edge weights/multiplicities are bounded (but for unbounded multiplicities or edge weights one has to do more, as we shall see). We note that this paper took the approach of deﬁning convergence via weak convergence of the distribution of samples, and this gives a link to exchangeability and Aldous’ representation theorem. It turns out that whilst sampling convergence is equivalent to homomorphism convergence notions for compact decorations, this does not longer hold if the compactness condition is waived (see Section 4.4).

A limit theory for convergence of multigraphs was worked out by Kolossva´ry and Ra´th [7], and essentially the same results can be derived from the limit theory of compact decorated graphs using the one-point compactiﬁcation of the set of integers to encode the edge multiplicities. The limit objects can be described by functions on [0,1]2 whose values are probability distributions on nonnegative integers.

Let us describe in a few words the general framework for graph convergence theories. We start with deﬁning the number of occurrences of a “small” graph F in a “big” graph G. In the case of simple graphs, one can use the number of homomorphisms (adjacencypreserving maps) hom(F,G) from F to G. One also needs the (normalized) homomorphism density

hom(F,G) |V (G)||V (F)|

. (1)

t(F,G) =

![image 2](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile2.png>)

A key notion in these theories is that of convergence of a graph sequence, which is deﬁned by specifying an appropriate family of test graphs, and then saying that a sequence of graphs (G1,G2,... ) is convergent, if t(F,Gn) is convergent for every test graph F. In the theory of convergence of simple graphs, the family of simple graphs is the right (in a sense, only reasonable) choice for test graphs. The limiting values of these densities can be represented by limit objects called graphons, which in the case of simple graphs are symmetric measurable functions [0,1]2 → [0,1].

The motivation of this paper is to work out a limit theory for convergence of multigraphs. Whether or not the results of Kolossva´ry and Ra´th [7] can be viewed as a solution

of the problem of multigraph convergence depends on how we deﬁne homomorphisms between two multigraphs F and G.

One natural deﬁnition is that of node-and-edge homomorphism: this is a pair of maps ϕ : V (F) → V (G) and ψ : E(F) → E(G) such that if e ∈ E(G) connects i and j, then ψ(e) connects ϕ(i) and ϕ(j). A diﬀerent deﬁnition is that of a node-homomorphism: a map V (F) → V (G) such that the multiplicity of the image of an edge is not less than the multiplicity of the edge. If both F and G consist of two nodes connected by two edges, then the number of node-homomorphisms F → G is 2, while the number of node-and-edge homomorphisms is 8.

In this paper, we consider node-and-edge homomorphisms, and for two multigraphs, we denote by hom(F,G) their number. We deﬁne homomorphism densities and convergence based on this deﬁnition. The results of Kolossva´ry and Ra´th are based on nodehomomorphisms. It turns out that these two notions of convergence are not equivalent (see Section 2.3, and also [9], Chapter 17).

In fact, we consider a more general model, namely a limit theory of graphs whose edges are decorated by elements from a Banach space, and where the test graphs are decorated from the pre-dual space. This will include the convergence theory of compact decorated graphs as well. Along the way, we show that with a modiﬁed notion of cut distance (which we call “jumble distance”) one can state a prove an appropriate Weak Regularity Lemma and a Counting Lemma.

Recently Borgs, Chayes, Cohn and Zhao [1] developed a theory for Lp-graphons (unbounded symmetric functions in the space Lp([0,1]2) for some 2 < p < ∞), and graph sequences convergent to them. They prove appropriate versions of the Regularity and Counting Lemmas. Not every graph has a ﬁnite density in such a kernel, and accordingly, they limit the set of test-graphs to simple graphs with degrees bounded by p. Their setup is more general than ours in the sense that we work with a more restricted family of unbounded kernels, namely kernels in L = 1≤p<∞ Lpsym([0,1]2). On the other hand, we allow arbitrary multigraphs as test graphs (more generally, decorating by elements of a Banach space). So the two theories don’t seem to contain each other (but perhaps a common generalization is possible).

Using random graphs generated by Banach space valued graphons, we show that every element of the space of limit objects that we deﬁne arises as a limit of a convergent sequence of decorated graphs, and that this space is closed under our convergence notion.

Although we do not in this paper investigate the question of uniqueness of Banach space graphons (we refer to [8] by the ﬁrst author for details on that subject), we remark here that Examples 4.9 and 4.11 do show that indeterminacies in the Stieltjes/Hamburger moment problems are an extra natural obstacle to uniqueness for unbounded graphons, beyond the usual weak isomorphism equivalence (see, e.g., [9, Sections 7.3 and 10.7]).

# 2 Decorated graphs and graphons

## 2.1 Decorated graphs and graphons

If X is any set, an X-decorated graph is a graph where every edge ij is decorated by an element Xij ∈ X. An X-decorated graph will be denoted by (G,g), where G is a simple graph (possibly with loops), and g : E(G) → X. We will see several examples in Section

- 2.3 how decorations can be used to express weights, multiple edges, and more. In our setup, we will consider decorations by elements of Banach spaces. Let B be a


separable Banach space, let Z denote its dual. The elements of B act on Z as bounded linear functionals in the canonical way, and vice versa; the action of b ∈ B on z ∈ Z will be denoted by b,z . We will use “small” B-decorated graphs to probe “large” Z-decorated

graphs.

Let (G,g) be an X-decorated graph, where G is a graph with m edges, and X is a Banach space. We deﬁne

g p =

1 m

![image 3](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile3.png>)

e∈E(G)

g(e) pX

1/p

, g ∞ = max

e∈E(G)

g(e) X, and Πg =

e∈E(G)

g(e) X.

Clearly Πg ≤ g m1 .

To deﬁne “decorated graphons” we need to become more technical. We set L = 1≤p<∞ Lpsym([0,1]2). For b ∈ B and W : [0,1]2 → Z, let the function b,W : [0,1]2 → R

be deﬁned by

b,W (x,y) := b,W(x,y) .

- Deﬁnition 2.1. A function W : [0,1]2 → Z is called weak-* measurable if for any b ∈ B, the function b,W is measurable.
- Deﬁnition 2.2. A symmetric weak-* measurable function W : [0,1]2 → Z is called


a Z-graphon if the function (x,y)  → W(x,y) Z lies in L. Note that this function is measurable, since B is separable, and for a countable dense subset F ⊂ B we have

| f,W(x,y) | f B

.

W(x,y) Z = sup

![image 4](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile4.png>)

f∈F\{0}

Let the space of Z-graphons be denoted by WZ. We set

W p := W(.,.) Z p.

(i.e., we take the Z-norm of W(x,y) for every x,y ∈ [0,1], and then take the Lp-norm of the resulting function).

Also, if W is a Z-graphon, then b,W ∈ L. Indeed,

b,W p ≤ b B W(.,.) Z p = b B W p < ∞. (2)

Note that the above measurability notion is not one usually encountered when looking at Banach space valued functions, for the simple reason that generally a predual B may not exist to the range space Z of the functions at hand. The two usual notions are weak and strong/Bochner measurability, and we shall brieﬂy hint at why weak-* measurability is instead the correct notion for our purposes. Recall that a function W : [0,1]2 → Z is called weakly measurable if for any b ∈ Z′, the function b,W is measurable. Note that unless B is reﬂexive (which in our applications it typically will not be), weak-* measurability is strictly weaker due to the natural identiﬁcation of B with a subspace of Z′. A function W : [0,1]2 → Z is called Bochner measurable if it equals to the limit of a sequence of measurable functions with countable range almost everywhere. This in turn is by the Pettis measurability theorem equivalent to being weakly measurable and essentially separably valued (i.e., one may obtain a separable range by deleting a nullset from the domain). Note that whenever Z is separable, Bochner and weak measurability are equivalent.

As will become clear in the next section, the homomorphism densities which will be at the core of our convergence notion can be deﬁned just as well using Z′ instead of B. Also, our aim is to deﬁne a space of graphons that acts as a closure of the space of decorated graphs, and so is as small as possible. This indicates that we should opt for the

strongest possible measurability restrictions, favouring strong or weak measurability. However, (norm) closed balls in Z are not compact with respect to the weak topology, unless we have reﬂexivity and B = Z′ anyway. Therefore, if we wish to use Z-decorated graphs and test with elements from Z′, we might after the limit transition end up with something Z′′-valued, which again brings us to a range with a predual. In addition, there would also be some – related – issues deﬁning the stepping operators (Section 2.6), as weak/Pettis integrability does not follow from weak measurability even for bounded functions. For more details on the subtleties of measurability and integrability of Banach space valued functions, we refer to [13].

## 2.2 Homomorphism densities

For every B-decorated simple loopless graph F = (F,f) and Z-decorated completely looped complete graph G = (G,g), we deﬁne

hom(F,G) =:

f(e),g(ϕ(e)) .

ϕ:V (F)→V (G) e∈E(F)

Loops in G are unavoidable if we want to allow non-injective vertex maps, whereas not having loops on F conforms with the classical theory, and avoids having to cope with an extra component for the limit object (a “diagonal”). The homomorphism density t(F,G) is deﬁned by (1). Note that we can write

t(F,G) = E

f(e),g(ϕ(e)) , (3)

e∈E(F)

where the expectation is taken over uniform random maps ϕ : V (F) → V (G).

In the deﬁnition of the homomorphism number between ﬁnite graphs, it is sometimes convenient to restrict the summation to injective mappings. For every B-decorated graph

- F = (F,f) with k nodes and Z-decorated graph G = (G,g) with n nodes, we deﬁne

inj(F,G) =:

ϕ:V (F)֒→V (G) e∈E(F)

f(e),g(ϕ(e)) ,

and

tinj(F,G) =

inj(F,G) n(n − 1)... (n − k + 1)

![image 5](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile5.png>)

. We need some elementary estimates, summarized in the following lemma. Lemma 2.3. Let F = (F,f) be a B-decorated graph with k nodes and l edges, and let

- G = (G,g) be a Z-decorated graph with n nodes. Then


n n − 1

Πf g ll( for n ≥ 2), and assuming n ≥ 2 and g(u,u) = 0 ∈ Z for all u ∈ V (G),

|t(F,G)| ≤ Πf g ll, |tinj(F,G)| ≤

![image 6](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile6.png>)

k(k − 1) n − 1

Πf g ll. Proof. Let ϕ be a random map V (F) → V (G), then

|tinj(F,G) − t(F,G)| ≤

![image 7](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile7.png>)

|t(F,G)| ≤ E

| f(e),g(ϕ(e)) | ≤ E

e∈E(F)

e∈E(F)

f(e) B g(ϕ(e) Z

= ΠfE

e∈E(F)

g(ϕ(e)) Z .

Here ϕ(e) is uniform over all pairs in V (G) × V (G). Using H¨older’s Inequality,

1/l

E g(ϕ(e) lZ

= Πf g ll.

|t(F,G)| ≤ Πf

e∈E(F)

The second inequality follows by analogue computation, with the only modiﬁcation being that working with injective maps, ϕ(e) will be uniform on the oﬀ-diagonal elements of V (G) × V (G), hence the additional n2/n(n − 1) = n/(n − 1) factor.

For the third inequality, we shall make use of the fact that injective maps are counted both in hom(F,G) and inj(F,G), so a number of terms will cancel despite the diﬀerent normalization. Also, by the Bernoulli inequality

  = nk−1 n −

 1 −

k−1

k(k − 1) 2

j n

(n)k ≥ nk

.

![image 8](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile8.png>)

![image 9](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile9.png>)

j=0

Therefore we have

nk (n)k

1 nk

hom(F,G) −

inj(F,G)

|t(F,G) − tinj(F,G)| =

![image 10](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile10.png>)

![image 11](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile11.png>)

  

   −

nk − (n)k (n)k

1 nk

f(e),g(ϕ(e))

inj(F,G)

=

![image 12](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile12.png>)

![image 13](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile13.png>)

ϕ:V (F)→V (G) ϕ not injective

e∈E(F)

  

   +

nk − (n)k nk |tinj(F,G)|

1 nk

≤

f(e),g(ϕ(e))

![image 14](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile14.png>)

![image 15](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile15.png>)

e∈E(F)

ϕ:V (F)→V (G) ϕ not injective

  

   +

1 nk

k(k − 1) 2(n − 1)

Πf g ll

≤

f(e),g(ϕ(e))

![image 16](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile16.png>)

![image 17](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile17.png>)

ϕ:V (F)→V (G) ϕ not injective

e∈E(F)

For the ﬁrst term, an argument identical to the previous leads to

   ≤

  

nk − (n)k nk

- 1 nk


1/l

Eninj g(ϕ(e) lZ

,

Πf

f(e),g(ϕ(e))

![image 18](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile18.png>)

![image 19](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile19.png>)

e∈E(F)

ϕ:V (F)→V (G) ϕ not injective

e∈E(F)

where the expectation is taken over all non-injective maps. It remains to investigate the distribution of ϕ(e). Note that since the distribution under all maps would be uniform on V (G) × V (G), whereas under injective maps uniform on the oﬀ-diagonal elements, we see that for non-injective maps, we have ϕ(e) = (u,v) ∈ V (G) × V (G) with probability

nk − (n)k n−n1 nk − (n)k ·

1 n2

![image 20](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile20.png>)

if u = v; nk

![image 21](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile21.png>)

![image 22](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile22.png>)

1 n2

nk − (n)k ·

if u = v.

![image 23](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile23.png>)

![image 24](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile24.png>)

However g(u,u) = 0 ∈ B for all u ∈ V (G), meaning

nk − (n)k n−n1 nk − (n)k

![image 25](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile25.png>)

g ll < g ll,

Eninj g(ϕ(e) lZ ≤

![image 26](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile26.png>)

and so

k(k − 1) 2(n − 1)

k(k − 1) 2n

Πf g ll, and the conclusion follows.

Πf g ll +

|t(F,G) − tinj(F,G)| ≤

![image 27](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile27.png>)

![image 28](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile28.png>)

![image 29](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile29.png>)

![image 30](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile30.png>)

![image 31](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile31.png>)

![image 32](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile32.png>)

Another type of decoration we consider is L-decoration, given by a map w : E(F) → L (so every edge ij is decorated by a function wij ∈ L). In this case, a “homomorphism density” can be deﬁned for a single graph: for an L-decorated graph (F,w) on V (F) = [k], we deﬁne

wij(xi,xj)dx1 ... dxk.

t(F,w) :=

ij∈E(F)

[0,1]V (F)

This integral is well deﬁned: if m = |E(F)|, then by H¨older’s Inequality,

[0,1]V (F)

wij(xi,xj) dx1 ... dxk ≤

ij∈E(F)

ij∈E(F)

wij m, (4)

which is ﬁnite.

Most of the time we need the following special case. Consider a B-decorated graph F = (F,f) on [k] and a Z-graphon W. Then wij = fij,W deﬁnes an L-decoration of F, and the previous deﬁnition specializes to

t(F,W) := t(F,w) =

f(ij),W(xi,xj) dx1 ... dxk.

ij∈E(F)

[0,1]V (F)

Finally, as a variation on the above, but without the dependence of the second variable on what simple graph F we chose. For any F-decorated graph F and s ∈ LF we may deﬁne

t(F,s) :=

sfij(xi,xj)dx1 ... dxk.

ij∈E(F)

[0,1]V (F)

We can think of getting information about a Z-graphon W by “probing” it with various “small” B-decorated graphs F. It is often natural to restrict the decoration of our test graphs to a subset F ⊆ B, for which homomorphism numbers of F-decorated graphs carry special combinatorial information. The family F will be countable in our examples. We usually assume that the set F is generating in B (meaning that lin F = B – this is sometimes also called total or fundamental). In this case, the values t(F,W) carry the same information about W if we restrict f to F-decorations than if we allow all B-decorations. If B is ﬁnite dimensional, then any basis can be chosen for F, but the choice of the basis does not actually matter, as illustrated by the examples in the next section.

![image 33](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile33.png>)

## 2.3 Examples

A large variety of examples comes from compact decorated graphs, i.e., K-decorated graphs where K is a compact Hausdorﬀ space. To capture convergence of K-decorated graphs, we need to consider C(K)-decorated graphs (where B = C(K) is the space of continuous real functions on K, with the supremum norm). The dual space Z = R(K) is the set of Radon measures on the Borel sets of K. This contains probability measures concentrated on a single point, and thus K-decorated graphs can be thought of as special Z-decorated graphs. We are also interested in selecting a “nice” countable generating set F ⊆ B. It is interesting to note that diﬀerent choices of F carry diﬀerent combinatorial information.

Many examples of K-decorated graphs with combinatorial signiﬁcance were discussed in [11] and also in [9], Chapter 17, and we only mention them brieﬂy.

- Example 2.4 (Simple graphs). Let K = {0,1} be the discrete space with two elements corresponding to “non-edge” and “edge”. The space B consists of all maps {0,1} → R, i.e., of all pairs (f(0),f(1)) of real numbers. Clearly, the dual space Z can also be identiﬁed with R2.

A natural generating subset F consists of the pairs (1,1) and (0,1). Homomorphism density corresponds to that for simple graphs. Every probability distribution on K can be represented by a number between 0 and 1, which is the probability of the element “edge”. So every symmetric measurable function W : [0,1]2  → [0,1] deﬁnes a Z-graphon.

One may, however, take another basis in B, namely the pairs (0,1) and (1,0). Then again F-decorated graphs can be thought of as simple graphs, and hom(F,G) counts the number of maps that preserve both adjacency and non-adjacency.

- Example 2.5 (Bounded multigraphs and multi-test-graphs). Let G be a multigraph with edge multiplicities at most d. Then G can be thought of as a K-decorated graph, where K = {0,1,... ,d}. This can be modeled with B ∼= Z ∼= Rd+1.

An interesting basis in B consists of the functions F = {1,x,... ,xd}. We can represent an F-decorated graph by a multigraph with edge multiplicities at most d, where an edge decorated by xi is represented by i parallel edges. The advantage of this is that hom(F,G) is then the number of node-and-edge homomorphisms of F into G as multigraphs, and so t(F,G) is the node-and-edge homomorphism density.

Taking the standard basis {e0,e1,... ,ed} in B, we can represent an edge label ei by i parallel edges. In this case, hom(F,G) counts multiplicity-preserving homomorphisms of F into G.

As a third possibility, we can consider the basis vectors fi = e0 +···+ei (i = 0,... ,d). Representing an edge label fi by i parallel edges, hom(F,G) counts node-homomorphisms of F into G.

This shows that in the case of bounded edge-multiplicities, diﬀerent ways of counting homomorphisms between multigraphs are essentially equivalent, they diﬀer in a simple basis transformation in the space B.

- Example 2.6 (Bounded weighted graphs and multi-test-graphs). This example is a rather straightforward extension of the previous one. Let K ⊆ R be a bounded closed interval. Let F be the collection of monomial functions x  → xj for j ∈ N on K (we denote by N the set of nonnegative integers, and by N∗, the set of positive integers). The linear hull of F is dense in B = C(K). It is natural to consider an F-decorated graph F as a multigraph, and then t(F,G) is the weighted homomorphism number as deﬁned e.g. in [9].

Compact decorations do not utilize the full strength of the general theory developed below. We discuss a couple of examples of this kind, and will return to these examples in Section 4.

- Example 2.7 (Multigraphs and simple test-graphs). Let us consider multigraphs with unbounded edge-multiplicity, and simple graphs as test-graphs. It turns out that in this case, multigraphs can be thought of as N-decorated simple graphs, and the fact that the edgeweights are nonnegative integers plays no role; so we can take Z = B = R, and consider the basis F = {1} in B. If F is a simple (F-decorated) graph and G is an edge-weighted (complete) graph, then hom(F,G) is the homomorphism number into G as a multigraph.
- Example 2.8 (Multigraphs and multi-test-graphs). Consider multigraphs with unbounded edge-multiplicity, and multigraphs as test-graphs. We have already seen that homomorphisms of a multigraph into another can be deﬁned in diﬀerent ways. In the bounded case, these notions turned out to be essentially the same, but in the unbounded case, the correspondence is more subtle.


We sketch the idea how to ﬁt convergence according to node-and-edge homomorphism densities into our framework. Let B = R[X] be the space of polynomials in one variable, and let Z be the space of real sequences with ﬁnite support. For f ∈ B and a = (a1,a2,... ) ∈ Z, let us deﬁne

∞

aif(i).

f,a =

i=0

We encode a multigraph F by decorating each edge e ∈ E(F) with multiplicity m by the polynomial Xm, to get an edge-decorated simple graph F. We encode a “target” multigraph G by labeling each edge e ∈ E(F) with multiplicity m by sequence em with a single 1 in the m-th position, to get an edge-decorated complete graph G. Then hom( F, G) = hom(F,G).

The problem with this construction is that B and Z are not Banach spaces, and our theory needs the Banach space structure. We will describe how to work around this in Section 4.1.

## 2.4 The jumble norm

The classical cut-norm, which plays a key role in the limit theory of bounded graphons, is unfortunately not well suited for this general setting that allows for unbounded functions. We introduce a variant that serves this goal better.

Deﬁnition 2.9. Let the jumble-norm on the function space L be deﬁned by

1 λ(S)λ(T)

u(x,y)dxdy

u ⊠ := sup

![image 34](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile34.png>)

![image 35](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile35.png>)

S,T⊆[0,1]

S×T

(To motivate the name, we note that Thomason [14] uses this normalization in the deﬁnition of “jumble graphs”, a version of quasirandom graphs.)

Also, let

W ⊠ := sup

f,W

.

⊠

f∈B\{0} f B=1

We remark that this can also be written as

1 λ(S)λ(T)

sup

![image 36](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile36.png>)

![image 37](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile37.png>)

S,T⊆[0,1]

S×T

W(x,y)dxdy

,

Z

W is the unique element z ∈ Z such that for any f ∈ B one has f,z =

where the integral is to be taken in the weak-* sense, i.e.,

S×T

f,W (cf. [13, Chap. XII., Prop. 3.3]).

S×T

We note that for every u ∈ L (in fact, for every u ∈ L2([0,1]2), the supremum in the deﬁnition above is ﬁnite. Indeed,

1 λ(S)λ(T)

![image 38](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile38.png>)

![image 39](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile39.png>)

S×T

1 λ(S)λ(T) S×T

u(x,y)dxdy =

,u

![image 40](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile40.png>)

![image 41](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile41.png>)

1 λ(S)λ(T) S×T 2

≤

![image 42](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile42.png>)

![image 43](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile43.png>)

u 2 = u 2. (5)

A fortiori, we obtain W ⊠ ≤ W 2.

Let us also compare the jumble norm with the cut norm

u := sup

S,T⊆[0,1]

S×T

u(x,y)dxdy .

It is easy to see that

u ≤ u ⊠ ≤ u 1/2 u 1∞/2, showing that for bounded kernels the two norms deﬁne the same topology.

In the case of stepfunctions, the sets attaining the supremum in the deﬁnition can be chosen in a special way.

- Lemma 2.10. Let P = {S1,... ,Sk} be a measurable partition of [0,1], and u : [0,1]2 → R


a stepfunction with steps in P × P. Then there exist T1 = αi=1 Sai and T2 = βj=1 Sbj such that

1 λ(T1)λ(T2)

u .

u ⊠ =

![image 44](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile44.png>)

![image 45](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile45.png>)

T1×T2

Proof. First note that since u is a stepfunction, given any Q1,Q2 ⊆ [0,1], the value of

k j1,j2=1 λ(Q1 ∩ Sj1)λ(Q2 ∩ Sj2)u|(Q1∩Sj1)×(Q2∩Sj2)

1 λ(Q1)λ(Q2)

u =

![image 46](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile46.png>)

![image 47](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile47.png>)

![image 48](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile48.png>)

k j=1 λ(Q1 ∩ Sj) kj=1 λ(Q2 ∩ Sj)

Q1×Q2

=: F (λ(Qi ∩ Sj))1≤j≤k,i∈{1,2} depends only on the 2k variables

  ,

 

  ×

 

k

k

[0,λ(Sj)]

[0,λ(Sj)]

(λ(Qi ∩ Sj))1≤j≤k,i∈{1,2} ∈

j=1

j=1

and this dependence is continuous. By compactness there then exist some αi,j ∈ [0,λ(Sj)] (1 ≤ j ≤ k,i ∈ {1,2}) at which F attains its maximum. Since the Lebesgue measure on [0,1] is non-atomic, there actually exist measurable subsets Ri,j ⊂ Sj with λ(Ri,j) = αi,j for 1 ≤ j ≤ k,i ∈ {1,2}. Letting Ri := kj=1 Ri,j (i ∈ {1,2}), we obtain

1 λ(R1)λ(R2)

u ⊠ =

u . (6)

![image 49](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile49.png>)

![image 50](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile50.png>)

R1×R2

Now assume that for some 1 ≤ ℓ ≤ k

0 < λ(R1,ℓ) < λ(Sℓ). Let R1′ := R1\Sℓ and R1′′ := R1∪Sℓ, and set a := R′

1×R2 u, d := λ(R2) > 0, c := dλ(R1′ ) ≥ 0 and b := {x

0}×R2 u(x0,·) for some x0 ∈ Sℓ. Note that the value of b is well-deﬁned since u is a stepfunction. We may, without loss of generality, assume that a ≥ 0. If we were to have a > 0,b < 0, then the integral of u over R1′ × R2 and R1,ℓ × R2 would have diﬀerent signs, so at least one of the choices R1′ or R1,ℓ instead of R1 would lead to a strictly larger value than u ⊠, which is a contradiction. Hence we may assume b ≥ 0 as well. Let now Sℓ′ be any subset of Sℓ of measure α. With the notation

1 λ(R1′ ∪ Sℓ′)λ(R2)

N(α) :=

![image 51](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile51.png>)

![image 52](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile52.png>)

(R′1∪Sℓ′)×R2

a + bα √c + dα

u =

![image 53](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile53.png>)

![image 54](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile54.png>)

we have that

bdα + (2bc − ad) 2(c + dα)3/2

N′(α) =

,

![image 55](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile55.png>)

i.e., if bd > 0, the function N is strictly monotone decreasing until its minimum, then strictly monotone increasing, and hence if N(0) < N(λ(R1∩Sℓ)), then also N(λ(R1∩Sℓ)) < N(λ(Sℓ)). If bd = 0, then at least one of N(0) ≥ N(λ(R1 ∩ Sℓ)) and N(λ(R1 ∩ Sℓ)) ≤ N(λ(Sℓ)) is true.

But note that

1 λ(R1′ )λ(R2)

u ,

N(0) =

![image 56](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile56.png>)

![image 57](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile57.png>)

R′1×R2

1 λ(R1)λ(R2)

N(λ(R1 ∩ Sℓ)) =

u ,

![image 58](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile58.png>)

![image 59](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile59.png>)

R1×R2

and

1 λ(R1′′)λ(R2)

u .

N(λ(Sℓ)) =

![image 60](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile60.png>)

![image 61](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile61.png>)

R′′1×R2

This means that we may choose R1 so that it contains either all of Sℓ, or none of it, whilst still satisfying (6). Iterating for all of the Si we obtain the desired T1, and repeating for R2 yields us T2.

![image 62](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile62.png>)

![image 63](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile63.png>)

![image 64](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile64.png>)

![image 65](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile65.png>)

The next lemma shows how weighted integrals can be estimated in terms of the jumble norm.

- Lemma 2.11. Let u ∈ L2([0,1]2) and f,g ∈ L3([0,1]). Then


u(x,y)f(x)g(y)dxdy ≤ 8 u ⊠ f 3 g 3.

[0,1]2

Proof. First, we prove the stronger inequality

u(x,y)f(x)g(y)dxdy ≤ 2 u ⊠ f 3 g 3 (7)

[0,1]2

∞

∞

(s ≤ g(x))ds, we have

(t ≤ f(x))dt and g(x) =

for the case when f,g ≥ 0. Writing f(x) =

0

0

∞

∞

u(x,y)f(x)g(y)dxdy =

u(x,y) (f(x) ≥ t) (g(y) ≥ s)dxdy dtds

0 [0,1]2

0

[0,1]2

∞

∞

![image 66](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile66.png>)

≤

u ⊠ λ{x : f(x) ≥ t}λ{y : g(y) ≥ s}dtds

0

0

∞

∞

![image 67](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile67.png>)

![image 68](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile68.png>)

λ{x : f(x) ≥ t}dt

λ{y : g(y) ≥ s} ds .

= u ⊠

0

0

To estimate the integrals on the right, let h denote the monotone decreasing reordering of f. Then, using H¨older’s Inequality,

∞

0

![image 69](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile69.png>)

λ{x : f(x) ≥ t}dt =

0

- 1

![image 70](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile70.png>)

- 2


≤

∞

![image 71](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile71.png>)

h−1(t)dt =

1

h(x2)dx =

1

1 √y 3/2

![image 72](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile72.png>)

![image 73](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile73.png>)

0

h 3 = 21/3 f 3.

0

- 1

![image 74](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile74.png>)

- 2√y


h(y)dy

![image 75](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile75.png>)

Using a similar estimate for g, then repeating for the function −u we obtain (7).

In the general case, let f+ and g+ denote the positive parts, and f− and g− the negative parts of the functions f and g, respectively, so that f = f+ − f− and g = g+ − g−. Then

u(x,y)f(x)g(y)dxdy

[0,1]2

≤

u(x,y)f+(x)g+(y)dxdy +

u(x,y)f+(x)g−(y)dxdy

[0,1]2

[0,1]2

+

u(x,y)f−(x)g+(y)dxdy +

u(x,y)f−(x)g−(y)dxdy

[0,1]2

[0,1]2

Each term can be estimated by (7), and using the trivial facts that f+ 3, f− 3 ≤ f 3 and g+ 3, g− 3 ≤ g 3, the lemma follows.

![image 76](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile76.png>)

![image 77](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile77.png>)

![image 78](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile78.png>)

![image 79](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile79.png>)

Remark 2.12. A more careful computation would improve the factor of 8 to 4. One can strengthen the lemma in other ways as well. First, instead of the L3-norms on the right side, we could use the Lp-norm for any p > 2 (but not p = 2). Second, for f ∈ Lp[0,1] (p > 2) we can introduce the functional

∞

K(f) :=

0

![image 80](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile80.png>)

λ{x : |f(x)| ≥ t}dt.

It is not hard to see that K(.) is a norm on Lp(0,1) for p > 2 (it is in fact the Lorentz norm on the larger space L2,1), and it satisﬁes

- p − 1

![image 81](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile81.png>)

- p − 2


(p−1)/p

K(f) ≤ 2−1/p

f p.

In terms of the norm K, the conclusion of Lemma 2.11 can be strengthened (with the same proof):

u(x,y)f(x)g(y)dxdy ≤ 4 u ⊠K(f)K(g).

[0,1]2

## 2.5 Counting Lemma

Our next goal is to prove appropriate generalizations of the Counting Lemma from bounded kernels to unbounded ones (see Lemma 10.24 in [9]). It is clear that

(w − w′) ≤ w − w′ ⊠. The following lemma generalizes this inequality to densities of other graphs.

|t(K2,w) − t(K2,w′)| =

[0,1]2

- Lemma 2.13. Let F be a simple graph with l ≥ 2 edges, and let w and w′ be L-decorations of F. For a ∈ E(F), deﬁne


Ma := max wa 3l−3, wa′ 3l−3 . Then we have

|t(F,w) − t(F,w′)| ≤ 8

a∈E(F)

wa − wa′ ⊠

Mb.

b∈E(F)\{a}

If we deﬁne w 0 = 1 for every function w, then the lemma remains valid for all graphs F with at least one edge. Proof. Let V (F) = [k]. It suﬃces to show that if w′ is obtained from w by changing the decoration of a single edge a = uv, then

|t(F,w) − t(F,w′)| ≤ 8 wa − wa′ ⊠

Mb.

b∈E(F)\{a}

We may assume that u = 1 and v = 2. Then t(F,w) − t(F,w′) =

wa(x1,x2) − wa′ (x1,x2)

[0,1]k

wij(xi,xj)dx. (8)

ij =e

We can break the product into two parts: ′ =

, ′′ =

.

ij∈E(F),i=1,j>2

ij∈E(F),i,j>1

Let us ﬁx x3,... ,xk, and integrate just with respect to x1 and x2. Then f = ′ depends only on x1 and g = ′′ depends only on x2, and clearly f,g ∈ Lp(0,1) for every p ≥ 1. So we get by Lemma 2.11 that

wa(x1,x2) − wa′ (x1,x2) f(x1)g(x2)dx1 dx2

[0,1]2

≤ 8 wa − wa′ ⊠ f 3 g 3. Integrating this with respect to x3,x4,... , we get by H¨older’s Inequality

 

 

1/3

1

′|wij(xi,xj)|3 dx1

|t(F,w) − t(F,w′)| ≤ 8 wa − wa′ ⊠

0

[0,1]k−2

 

 

1/3

1

′′|wij(xi,xj)|3 dx2

dx3 ... dxk

×

0

  

  

1/3

≤ 8 wa − wa′ ⊠

′|wij(xi,xj)|3dx1 ... dxk

[0,1]k

  

  

1/3

′′|wij(xi,xj)|3dx1 ... dxk

×

[0,1]k

≤ 8 wa − wa′ ⊠

wij 3l−3 ≤ 8 wa − wa′ ⊠

Mb.

ij =e

b =a

This proves the Lemma.

As a special case, we get the following version of the Counting Lemma.

- Corollary 2.14 (Counting Lemma for Unbounded Kernels). Let u,w ∈ L and let F be a simple graph with l ≥ 1 edges. Then

|t(F,u) − t(F,w)| ≤ 8l u − w ⊠ max u 3l−3, w 3l−3 l−1.

As a further corollary, we can estimate the diﬀerence between the homomorphism densities of a decorated graph in two Z-graphons with the help of distances in jumble norm.

- Corollary 2.15. Let F = (F,f) be a B-decorated graph with k nodes and l edges, and let U,W ∈ WZ. Then

|t(F,U) − t(F,W)| ≤ 8l f l∞ U − W ⊠ max U 3l−3, W 3l−3 l−1.

Proof. Let ua := fa,U , wa := fa,W and Ma := max ua 3l−3, wa 3l−3 for a ∈ E(F). Then by Lemma 2.13 we have that

|t(F,U) − t(F,W)| =|t(F,(ua)a∈E(F)) − t(F,(wa)a∈E(F))| ≤8

a∈E(F)

ua − wa ⊠

b∈E(F)\{a}

Mb

≤8l f ∞ U − W ⊠ max f ∞ U 3l−3, f ∞ W 3l−3 l−1

=8l f l∞ U − W ⊠ max U 3l−3, W 3l−3 l−1

![image 86](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile86.png>)

![image 87](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile87.png>)

![image 88](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile88.png>)

![image 89](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile89.png>)

Also, we can directly extract the following from the proof of Lemma 2.13.

- Corollary 2.16. Let F = (F,f) be an F-decorated graph, s,s′ ∈ LF and


Mψ := max sψ 3l−3 , s′ψ 3l−3 for each ψ ∈ F. Then

 

  sfij − s′fij

|t(F,s) − t(F,s′)| ≤ 8

Mfαβ

⊠ αβ∈E(F)\{ij}

ij∈E(F)

We conclude this section with a simpler version of the counting lemma, using the Ll norm, rather than the jumble norm.

- Lemma 2.17. Let F = (F,f) be a B-decorated graph with k nodes and l edges, and let U,W ∈ WZ. Then


|t(F,U) − t(F,W)| ≤ l f l∞ U − W l max U l, W l l−1.

Proof. The proof follows the ideas of Lemma 2.13 and Corollary 2.15, but applies H¨older’s Inequality directly after equation 8.

![image 90](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile90.png>)

![image 91](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile91.png>)

![image 92](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile92.png>)

![image 93](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile93.png>)

## 2.6 The Weak Regularity Lemma

We generalize the Regularity Lemma to our setting, based on the notion of the jumble norm. The proof is a straightforward generalization from the bounded case, but since we work with a diﬀerent norm here, we include it for completeness.

The stepping operator associated with a measurable partition P = {S1,... ,Sk} of [0,1] assigns to every function u ∈ L the stepfunction uP, where

1 λ(Si)λ(Sj)

uP(x,y) =

u(x,y)dxdy for x ∈ Si,y ∈ Sj,

![image 94](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile94.png>)

Si×Sj

with the convention of assigning value 0 whenever one of the sets has measure 0. Also, again using weak-* integrals, the stepping operator can be extended to Z-graphons as

1 λ(Si)λ(Sj)

W(x,y)dxdy for x ∈ Si,y ∈ Sj

WP(x,y) :=

![image 95](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile95.png>)

Si×Sj

We note that by deﬁnition of the weak-* integral, the stepping operator commutes with applying a linear functional: for every W ∈ WZ and f ∈ B, we have

f,W P = f,WP . (9)

Let us summarize some basic properties of this operator; analogues of these for the cut-norm and for bounded functions were proved in [9].

- Proposition 2.18. The stepping operators are contractive in the jumble norm.

Proof. Let u ∈ L and let P be a measurable partition. Let S and T be sets attaining the supremum in the deﬁnition of uP ⊠, which by Lemma 2.10 can be assumed to be unions of partition classes of P. Then

uP ⊠ =

1 λ(S)λ(T)

![image 96](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile96.png>)

S×T

uP(x,y)dxdy =

1 λ(S)λ(T)

![image 97](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile97.png>)

S×T

u(x,y)dxdy ≤ u ⊠.

![image 98](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile98.png>)

![image 99](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile99.png>)

![image 100](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile100.png>)

![image 101](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile101.png>)

It is easy to check that the stepping operator is contractive with respect to the Lpnorm of functions in Lp([0,1]2) for all p ≥ 1. In fact, it is contractive with respect to any “reasonable” norm (cf. Proposition 14.13 in [9]).

The stepfunction uP is the best approximation of u in the L2-norm among all stepfunctions with the same steps. This is no longer true if the L2-norm is replaced by the jumble norm, but it is true up to a factor of 2, as shown by the following straightforward generalization of an observation of Frieze and Kannan [5].

- Proposition 2.19. Let v ∈ L be a stepfunction and let P be the partition of [0,1] that is ﬁner than the partition into the steps of v. Then for any u ∈ L we have


u − uP

. Proof. We have v = vP, and hence by Proposition 2.18,

≤ 2 u − v

⊠

⊠

u − uP ⊠ ≤ u − v ⊠ + v − uP ⊠ = u − v ⊠ + vP − uP ⊠ = u − v ⊠ + (v − u)P) ⊠ ≤ 2 u − v ⊠.

After this preparation, we are able to state the main lemma in this section.

- Lemma 2.20 (Weak Regularity Lemma for Unbounded Kernels). For every sym-

metric function w ∈ L2([0,1]2) and every k ≥ 1 there is a partition P of [0,1] into k measurable sets such that

w − wP ⊠ ≤

4 √log k

![image 106](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile106.png>)

![image 107](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile107.png>)

w 2.

In the case of bounded kernels (or simple graphs), one may require that the partition P is an equipartition (allowing a little larger error). This is, however, no longer true in the unbounded setting: parts where the function is large must be partitioned into more pieces.

Proof. Let

j =

log k 2

![image 108](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile108.png>)

and c =

2j + 2 log k

![image 109](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile109.png>)

> 1. Let S and T be measurable subsets of [0,1] such that

w ⊠ ≤

c λ(S)λ(T)

![image 110](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile110.png>)

![image 111](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile111.png>)

S×T

w = c

w, S×T

![image 112](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile112.png>)

S×T 2

.

Let a := w, S×T / S×T 22. Clearly a ≥ w ⊠/(c S×T 2), and so w − a S×T 22 = w 22 − a2 S×T 22 ≤ w 22 −

1 c2

![image 113](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile113.png>)

w 2

⊠

. (10) Applying this observation repeatedly, we get pairs of sets Si,Ti and real numbers ai

such that for all r = 1,2,... , the “remainder” wr = w − ri=1 ai Si×Ti satisﬁes

wr 22 ≤ w 22 −

r−1

i=0

1 c2

![image 114](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile114.png>)

wi 2

⊠

.

Applying this inequality with r = j, using (5) and c > 1, it follows that

j

i=0

wi 2

⊠ ≤ c2 w 22. Hence there is a 0 ≤ m ≤ j with

wm ⊠ ≤

c √j + 1

![image 115](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile115.png>)

![image 116](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile116.png>)

w 2 =

2√j + 1 log k

![image 117](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile117.png>)

![image 118](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile118.png>)

w 2 ≤

2√2j log k

![image 119](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile119.png>)

![image 120](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile120.png>)

w 2 ≤

2 √log k

![image 121](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile121.png>)

![image 122](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile122.png>)

w 2,

which means that the stepfunction v = mi=1 ai Si×Ti satisﬁes the inequality w − v ⊠ ≤

2 √log k

![image 123](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile123.png>)

![image 124](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile124.png>)

w 2.

The stepfunction v has at most 2j ≤

√

![image 125](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile125.png>)

k steps. It may not be symmetric, but we can replace it by (v(x,y)+v(y,x))/2, which has at most 4j ≤ k steps. By Proposition 2.19, we can replace v by wP (where P is the partition into the steps of v) at the cost of doubling the error.

![image 126](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile126.png>)

![image 127](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile127.png>)

![image 128](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile128.png>)

![image 129](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile129.png>)

- Lemma 2.21 (Weak Regularity Lemma for several Unbounded Kernels). For every t ∈ N∗, ε ∈ (0,∞), u1,u2,... ,ut ∈ L and measurable partition P1 of [0,1] there exists a positive integer q = q(|P1|,t,ε) and a measurable q-partition P2 of [0,1] reﬁning P1 such that


≤ ε ui 2 for each 1 ≤ i ≤ t.

ui − (ui)P2

⊠

1

Proof. Using Lemma 2.20 we obtain measurable partitions R1,... ,Rt of [0,1] into 264⌈

ε2 ⌉

![image 130](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile130.png>)

sets such that for each 1 ≤ i ≤ t we have

ε 2

ui − (ui)Ri

≤

ui 2. Let P2 be the common reﬁnement of P1 and all of the Ri’s. Then |P2| = |P1| ·

![image 131](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile131.png>)

⊠

t

|Ri| = |P1| · 24t⌈1ε⌉ =: q(|P1|,t,ε),

![image 132](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile132.png>)

i=1

and by Proposition 2.19

ui − (ui)P2

≤ 2 ui − (ui)Ri

≤ ε ui 2 for each 1 ≤ i ≤ t.

⊠

⊠

![image 133](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile133.png>)

![image 134](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile134.png>)

![image 135](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile135.png>)

![image 136](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile136.png>)

# 3 Convergence of Banach space valued graphons

## 3.1 Dense sets

In this preliminary section we prove two lemmas which will allow us to use countable “test sets” for certain properties. The ﬁrst lemma lets us prove weak-* measurability using only a countable dense subset of B.

- Lemma 3.1. Let F ⊂ B be a countable dense subset, and let W : [0,1]2 → Z be a function such that f,W is measurable for each f ∈ F. Then W is weak-* measurable.


Proof. Since F is countable and dense in B, for any b ∈ B there exists a sequence (fn) ⊂ F that converges to b in norm. But then b,W is the pointwise limit of the measurable functions fn,W , and hence itself measurable.

![image 137](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile137.png>)

![image 138](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile138.png>)

![image 139](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile139.png>)

![image 140](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile140.png>)

Next we show that when dealing with convergence of homomorphism densities of decorated graphs, it is enough to consider decorations from a generating subset of the original decoration space.

- Lemma 3.2. Let W1,W2 ... ∈ WZ be Z-graphons and F ⊆ B be a generating subset. Assume that the sequence ( Wn p) is bounded by some 0 ≤ cp for each 1 ≤ p < ∞. Then the following are equivalent:


- (i) For every B-decorated graph F, the sequence t(F,Wn) is convergent;
- (ii) For every F-decorated graph F, the sequence t(F,Wn) is convergent.


Proof. Let us assume (ii) holds. Then, by multilinearity with respect to the decoration, the convergence also holds for every lin(F)-decorated graph. Let F = (F,f) be a B-decorated graph with l ≥ 1 edges, and let f1,... ,fm be the elements present in the decoration of F for an appropriate 1 ≤ m ≤ l. For a given k ∈ N∗ and for each 1 ≤ r ≤ m, let frk ∈ lin(F) be such that

1 k

fr − frk ≤

, (11)

![image 141](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile141.png>)

and let Fk denote the decorated graph obtained from F by replacing each fr in its decoration by frk.

Now ﬁx n ∈ N∗. Let s ∈ LB be deﬁned by sf := f,Wn , and let s′ ∈ LB be such that s′f

= frk,Wn for each 1 ≤ r ≤ m, and s′f = sf otherwise. Let

r

dfαβ = max sfαβ 3l−3 , s′f

αβ 3l−3

,

Then we have by deﬁnition t(F,Wn) = t(F,s) and t(Fk,Wn) = t(F,s′), and applying

- Corollary 2.16 we obtain t(F,Wn) − t(Fk,Wn) = |t(F,s) − t(F,s′)|


 

  sfij − s′fij

df

≤ 8

αβ

⊠ αβ∈E(F)\ij

ij∈E(F)

 

  sfij − s′fij

dfαβ

≤ 8

2

αβ∈E(F)\ij

ij∈E(F)

  fij,Wn − fijk,Wn

 

= 8

dfαβ

2

ij∈E(F)

αβ∈E(F)\ij

  Wn

 

≤ 8

dfαβ

![image 142](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile142.png>)

k 2

ij∈E(F)

αβ∈E(F)\ij

 

 c2

Wn k 3l−3

fαβ,Wn 3l−3 +

≤ 8

![image 143](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile143.png>)

![image 144](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile144.png>)

k

αβ∈E(F)\ij

ij∈E(F)

 c2

 

1 k

≤ 8

fαβ +

c3l−3

![image 145](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile145.png>)

![image 146](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile146.png>)

k

ij∈E(F)

αβ∈E(F)\ij

using inequality (11) and pointwise estimates for the weak-* evaluations of Wn. The last line is independent of n and converges to 0 as k goes to inﬁnity. Since the sequences t(Fk,Wn) are convergent for each k, the convergence thus follows for the sequence t(F,Wn).

The other implication obviously holds.

![image 147](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile147.png>)

![image 148](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile148.png>)

![image 149](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile149.png>)

![image 150](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile150.png>)

- 3.2 Moment sequences Let F be a countable generating subset of B. Deﬁnition 3.3. The F-moment sequence of an element z ∈ Z is the family ( f,z : f ∈


- F) of real numbers. The F-moment function sequence of a function U : [0,1]2 → Z is the family ( f,U : f ∈ F) of functions.

Proposition 3.4. A family of measurable symmetric functions uf : [0,1]2 → R (f ∈ F) is the F-moment sequence of a symmetric weak-* measurable function W : [0,1]2 → Z if and only if (uf(x,y) : f ∈ F) is the F-moment sequence of some element of Z for every (x,y) ∈ [0,1]2.

Proof. The “only if” part is trivial. To prove the “if” part, notice that by assumption we may deﬁne W pointwise in a unique way. Indeed, by the deﬁnition of an F-moment sequence, for every (x,y) ∈ [0,1]2 there is a z ∈ Z such that uf(x,y) = f,z for every f ∈ F. Thus element z is uniquely determined; indeed, if z1 and z2 are two such elements, then by linearity g,z1 = g,z2 for every g ∈ lin(F), and then by the density of lin(F) in B we have b,z1 = b,z2 for every b ∈ B, implying that z1 = z2. Thus we can deﬁne W(x,y) = z. Uniqueness of z also implies that W is symmetric.

We have to show that this function W is weak-* measurable as a function [0,1]2 → Z. Let G := linQ F, then G is a dense countable set in B. By linearity, for every g ∈

- G the function g,W is measurable. By Lemma 3.1, the function W is then weak-* measurable.


![image 151](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile151.png>)

![image 152](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile152.png>)

![image 153](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile153.png>)

![image 154](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile154.png>)

Our next lemma says that, under appropriate conditions, the limit of a sequence of F-moment function sequences of Z-graphons is the F-moment function sequence of a Z-graphon.

- Lemma 3.5. Let Wn ∈ WZ (n ∈ N∗) and suppose that there are constants cp > 0 such that Wn p ≤ cp for every 1 ≤ p < ∞. Let un,f = f,Wn for n ∈ N∗ and f ∈ F, and suppose that for every f ∈ F, un,f(x,y) → uf(x,y) for almost all (x,y) ∈ [0,1]2 for some function uf. Then there exists a Z-graphon W such that W p ≤ cp for every 1 ≤ p < ∞, and uf = f,W for all f ∈ F.


Proof. First we note that the condition that Wn p is bounded implies that for almost all points (x,y) ∈ [0,1]2, the sequence Wn(x,y) Z does not tend to inﬁnity. We also know that for almost all (x,y) ∈ [0,1]2, un,f(x,y) → uf(x,y) for all f ∈ F (in particular uf is measurable). Let us call a point (x,y) satisfying these conditions ordinary.

Fix an ordinary point (x,y). We can ﬁnd a subsequence N1 of the indices n for which

Wn(x,y) Z remains bounded, and we can select a further subsequence N2 for which the sequence (Wn(x,y) : n ∈ N2) is weak-* convergent. Let its limit be z ∈ Z. By the deﬁnition of weak-* convergence, this limit satisﬁes

f,z = lim

n∈N2

f,Wn(x,y) = lim

un,f(x,y) = uf(x,y) (12)

n∈N2

for every f ∈ F, and also z Z = sup

b∈B b B=1

≤ sup

b∈B b B=1

lim

b,Wn(x,y)

b,z = sup

n∈N2

b∈B b B=1

liminf

b B Wn(x,y) Z = liminf

n∈N2

n∈N2

Wn(x,y) Z. (13)

Just as in the previous proof, the conditions f,z = uf(x,y) determine the element z ∈ Z uniquely. It follows that inequality (13) holds for any weak-* convergent normbounded subsequence N2. This implies that

z Z ≤ liminf

n∈N

Wn(x,y) Z. (14)

Now Proposition 3.4 applies and yields a symmetric function W : [0,1]2 → Z that is weak-* measurable, and uf = f,W for every f ∈ F. We want to show that W is a Z-graphon.

By the remark about uniqueness above, W(x,y) must be equal to the weak limit z constructed above for every ordinary (x,y), and setting it to 0 at non-ordinary points we hence have

Wn(x,y) Z. (15) This can be written as

W(x,y) Z ≤ liminf

n∈N∗

0 ≤ ( W(x,y) Z)p ≤ liminf

( Wn(x,y) Z)p.

n∈N∗

An application of Fatou’s lemma then yields that ( W Z)p ∈ L1([0,1]2) for every 1 ≤ p < ∞, and its norm is bounded by cpp. This means that

1/p

W p = ( W Z)p 1

≤ cp, showing that W is a Z-graphon with the required norm bounds.

![image 155](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile155.png>)

![image 156](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile156.png>)

![image 157](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile157.png>)

![image 158](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile158.png>)

## 3.3 Measure preserving transformations

- As a last step before turning our attention to proving the existence of a limit graphon for convergent sequences, it will be useful to touch upon the subject of uniqueness of the graphon representation. In other words, to what extent can we expect a graphon to be uniquely determined by the homomorphism densities? In the bounded, real valued case, this question can be fully answered, giving a characterization of all “equivalent” graphons, and this strongly ties into the fact that a number of convergence notions (density convergence, cut distance convergence, sampling convergence) turn out to be equivalent. In this more general setting, however, only partial results are known, and we refer to [8] for details. In this section we shall concentrate on a suﬃcient condition under which two graphons exhibit the same densities, as this will play a pivotal role in the proof of our main theorem.


For a ﬁnite Z-decorated graph G on the vertex set [n], there is a natural way of identifying it with a Z graphon WG that has the exact same densities. Namely, let

WG(x,y) := g⌈nx⌉⌈ny⌉.

Then WG is a stepfunction that essentially corresponds to the adjacency matrix of G, and an easy computation shows that indeed t(F,G) = t(F,WG) for any B-decorated graph F. Now, note that for a ﬁnite graph G, the value of t(F,G) does not change if we replace it by an isomorphic graph G′ (i.e., we relabel its vertices). However, WG = WG, so this immediately shows that two diﬀerent graphons may exhibit the same densities. The relabeling of the vertices of G essentially amounts to a permutation of the 1/n-length intervals corresponding to the steps of WG. Now note that for graphons, the homomorphism densities are deﬁned via integrals, and in general, for any measure preserving map ϕ : [0,1] → [0,1] and any integrable function H : [0,1]k → R, we have that

H =

[0,1]k

H ◦ ϕ,

[0,1]k

where H ◦ ϕ(x1,x2,... ,xk) := H ◦ ϕ⊗k(x1,x2,... ,xk) = H(ϕ(x1),ϕ(x2),... ,ϕ(xk). In particular, for any Z-graphon W and B-decorated graph F we have t(F,W) = t(F,W ◦ϕ). Also, less trivially, we have the following invariance of the jumble norm as well.

- Lemma 3.6. For any u ∈ L we have u ⊠ = u ◦ ϕ ⊠.


Proof. The proof works essentially as the proof for the cut norm in [6, Lemma 5.5]. The result is straightforward for any stepfunction due to Lemma 2.10 and the fact that any measure preserving map is actually a measure preserving bijection between the ﬁnite atomic σ-algebras generated by the steps of non-zero measure of u and u◦ϕ, respectively. For a general u ∈ L, consider an arbitrary ε > 0 and a stepfunction v ∈ L such that

u − v 2 < ε. Then we have the following:

v ⊠ − v ◦ ϕ ⊠ = 0; u − v ⊠ ≤ u − v 2 < ε; u ◦ ϕ − v ◦ ϕ ⊠ ≤ u ◦ ϕ − v ◦ ϕ 2 = (u − v) ◦ ϕ 2 = u − v 2 < ε.

A few applications of the triangle inequality then imply u ⊠ − u ◦ ϕ ⊠ < 2ε.

![image 159](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile159.png>)

![image 160](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile160.png>)

![image 161](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile161.png>)

![image 162](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile162.png>)

## 3.4 Limit graphon

The goal of this section is to prove our main result on the existence of a limit graphon in the Banach space valued case. The proof follows the overall structure of the proof of the corresponding results in [9, 10].

- Theorem 3.7. Let F be a countable generating subset of B and W1,W2,... be Z-graphons satisfying the following conditions:


- (i) for every 1 ≤ p < ∞ there is a cp > 0 such that Wn p ≤ cp for all n;
- (ii) the sequence (t(F,Wn) : n ∈ N∗) is convergent for every F-decorated graph F.


Then there exists a Z-graphon W such that t(F,Wn) → t(F,W) for every B-decorated graph F.

Proof. Let F = {f1,f2,... } and wn,m = fm,Wn . For each k ≥ 1, deﬁne h(k) recursively by h(1) = 1 and h(k) = q h(k−1),k,1/(c2k) , where q is the function in Lemma 2.21. For every k,n ≥ 1, we construct a partition Pn,k of [0,1] so that |Pn,k| = h(k), Pn,k+1 reﬁnes Pn,k, and the stepfunctions un,k,m = (wn,m)Pn,k satisfy

1 k

fm B (m = 1,... ,k). (16)

wn,m − un,k,m

≤

![image 163](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile163.png>)

⊠

Let Pn,k = {Sn,k1 ,... ,Sn,kh(k)}. Let Un,k = (Wn)Pn,k; then (9) implies that un,k,m =

fm,Un,k , and by the contractivity of the stepping operator, Un,k p ≤ cp for all 1 ≤ p < ∞. Note that un,k,m is deﬁned for all n,k and m, but (16) only holds for m ≤ k.

By selecting a subsequence N1 of the indices n, we may assume that for every ﬁxed k and 1 ≤ j ≤ h(k), the sequence λ(Sn,kj ) converges to a value sk,j, and in fact it converges fast enough so that n∈N

|λ(Sn,kj ) − sk,j| < ∞.

1

- At this point, the issue is that even though the measures of the sets of a given index pair (k,j) converge as n tends to inﬁnity, the sets themselves, pertaining to regularity


partitions of diﬀerent functions Wn, have no reason to exhibit any convergent behaviour. This is where the observations and Lemma 3.6 in the previous section become useful: since the homomorphism densities are not inﬂuenced by transforming the graphons via applying measure preserving transformations, nor are the various Lp (condition (i)) or jumble norm (equation 16) bounds, we could try to ﬁnd an appropriate measure preserving transformation ϕn : [0,1] → [0,1] for each n that would “unscramble” the sets Sn,kj and facilitate a natural limit transition for the partitions. More precisely, there exist measure preserving transformations ϕn : [0,1] → [0,1] (n ∈ N∗) such that for every k ∈ N∗ there is a measurable partition Pk = {Sk1,... ,Skh(k)} into intervals for which n∈N

λ(Skj△ϕn(Sn,kj )) < ∞ for every j, and also Pk+1 reﬁnes Pk.

1

Indeed, let gn,k : [0,1] → N∗ be the measurable function deﬁned via gn,k(x) := j whenever x ∈ Sn,kj . Then the sequence (gn,k(x))k∈N∗ corresponds to the sequence of indices of the partition classes x belongs to. Now let

∞

gn,k(x)

.

gn(x) :=

![image 164](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile164.png>)

k m=1(h(m) + 1)

k=1

Note that gn : [0,1] → [0,1] is a measurable function, and so there exists a measure preserving transformation ϕn that yields a monotone increasing rearrangement of gn (e.g., ϕn(x) := λ([gn < gn(x)]) + λ([gn = gn(x)] ∩ [0,x])). As the denominators of the sum were chosen to grow fast enough, this will correspond to the “lexicographic ordering” of the points of [0,1] with regards to the index sequence (gn,k(·)). Thus the partitions ϕn ◦ Pn,k are interval partitions, and the convergence of the sequences λ(Sn,kj )

ﬁnishes the argument.

n∈N1

Since replacing the graphons Wn by Wn ◦ ϕn in the original statement would lead to an equivalent claim, we may without loss of any generality assume that each ϕn is the identity map, and avoid an extra layer of cumbersome notation.

Our next goal is to select a subsequence of the indices n so that the stepfunctions un,k,m converge to some stepfunction with Pk-steps almost everywhere. This is not obvious, as the sequence (un,k,m)n∈N1 may not be uniformly bounded. To prove it, we have to treat “small” partition classes separately.

Let Jk ⊆ [h(k)] be the set of indices j such that λ(Skj) > 0. Let an,k,m,i,j be the value of un,k,m on Ski × Skj (where i,j ∈ [h(k)]). Then we have that

|an,k,m,i,j|λ(Sn,ki )λ(Sn,kj ) ≤ un,k,m 1 = fm,Un,k 1 ≤ fm B Un,k 1 ≤ c1 fm B,

and since λ(Sn,ki ) and λ(Sn,kj ) both converge to a non-zero value, the sequence (an,k,m,i,j)n∈N1 remains bounded. Hence using the usual diagonal method, we can select subsequence N2 ⊆ N1 so that (an,k,m,i,j)n∈N2 tends to some value ak,m,i,j for all m and all i,j ∈ Jk. We deﬁne ak,m,i,j = 0 if i ∈/ Jk or j ∈/ Jk. (Note that λ(Si ×Sj) = 0 in this case.) These values deﬁne a stepfunction uk,m : [0,1]2 → R with Pk-steps.

It is clear that un,k,m(x,y) → uk,m(x,y) for (x,y) ∈ Ski ×Skj for i,j ∈ Jk, provided x is contained in a ﬁnite number of sets Ski△Sn,ki , and y is contained in a ﬁnite number of sets Skj△Sn,kj . Since n λ(Skj△Sn,kj ) < ∞, the Borel-Cantelli Lemma implies that un,k,m → uk,m almost everywhere (n ∈ N2, n → ∞). Lemma 3.5 implies that for every k, the sequence (uk,m)m∈N∗ is the F-moment function sequence of some Z-graphon Uk, and so uk,m = fm,Uk and Uk p ≤ cp for all 1 ≤ p < ∞.

Note that we have a ﬁnite number of steps and limn∈N2 hj=1(k) λ(Skj△Sn,kj ) = 0. Also, whenever i  ∈ Jk or j  ∈ Jk, we have that for each 1 ≤ p < ∞,

→ 0.

un,k,m|Si

n,k×Sn,kj

p

Indeed, if this were not the case for some p, then since the measures of the sets we restrict to tend to zero, the functions un,k,m would not be uniformly bounded in Lq for any q > p. Thus, we have that for every 1 ≤ p < ∞, un,k,m → uk,m in Lp (n ∈ N2, n → ∞).

Now (un,r,m)Pn,k = un,k,m for r ≥ k ≥ m, and we have a ﬁnite (|J(k)|) number of partition class sequences (Sn,kj )n∈N2, each of which satisfy convergence in their measure to that of Skj, and a ﬁnite (|J(k)|2) number of value sequences (an,k,m,i,j)n∈N2 each converging to the corresponding ak,m,i,j. For the rest of the partition classes in Pk, all measures and all assigned function values ak,m,i,j are zero, hence it follows that also (ur,m)Pk = uk,m. So we can apply the Martingale Convergence Theorem to the sequence (uk,m)k∈N∗, and get that uk,m tends to some symmetric function um : [0,1]2 → R both almost everywhere and also in L1 as k → ∞.

Lemma 3.5 implies that the sequence (um)m∈N∗ is the F-moment function sequence of a Z-graphon U such that U p ≤ cp for all 1 ≤ p < ∞. But since the sequence (uk,m)k∈N∗ is bounded in Lp for every 1 < p < ∞ and uk,m → um in L1, it follows that the convergence also holds in Lp for all 1 ≤ p < ∞ (as above, lack of convergence for a given p would imply no uniform boundedness in Lq for q > p).

Next we show that for the subsequence of indices n we selected, we have t(F,ϕ,Wn) → t(F,ϕ,U) for every F-decorated simple graph (F,ϕ). To this end, let ε > 0 be given, and write

|t(F,ϕ,Wn) − t(F,ϕ,U)| ≤|t(F,ϕ,Wn) − t(F,ϕ,Un,k)| + |t(F,ϕ,Un,k) − t(F,ϕ,Uk)|

+ |t(F,ϕ,Uk) − t(F,ϕ,U)|.

We have a q ≥ 1 such that every decoration in (F,ϕ) occurs among {f1,... ,fq}. By the deﬁnition of Pn,k, we have

1 k

fm B

wn,m − un,k,m

≤

![image 165](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile165.png>)

⊠

for every m ≤ q and k ≥ q. This means that

1 k

fm,Wn − fm,Un,k ⊠ ≤

![image 166](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile166.png>)

fm B,

and by the Counting Lemma 2.13, we get that |t(F,ϕ,Wn) − t(F,ϕ,Un,k)| < ε/3 if k is large enough (independently of n).

Since uk,m → um in Lp for every 1 ≤ p < ∞, Lemma 2.17 implies that t(F,ϕ,Uk) → t(F,ϕ,U), and hence |t(F,ϕ,Uk)−t(F,ϕ,U)| < ε/3 if k is large enough. Let us ﬁx k so that both of these inequalities hold. Then, again by Lemma 2.17, we get that t(F,ϕ,Un,k) → t(F,ϕ,Uk), and hence t|(F,ϕ,Un,k) − t(F,ϕ,Uk)| < ε/3 if n is large enough.

This proves that t(F,ϕ,Wn) → t(F,ϕ,U) for n ∈ N2. Since the sequence (t(F,ϕ,Wn)) is convergent, we have t(F,ϕ,Wn) → t(F,ϕ,W) for n ∈ N∗.

Finally, we show that the relation t(F,ϕ,Wn) → t(F,ϕ,W) (n ∈ N∗) holds not only for F-decorations φ but also for B-decorations ϕ. First, it holds for lin(F)-decorations, since t(F,ϕ,W) is multilinear in ϕ (where ϕ is considered as an element in BE(F)). Second, it holds for B-decorations, since these can be approximated by lin(F)-decorations, and t(F,ϕ,W) is continuous in ϕ.

![image 167](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile167.png>)

![image 168](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile168.png>)

![image 169](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile169.png>)

![image 170](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile170.png>)

## 3.5 W-random decorated graphs

Let W be a Z-graphon. For every n ≥ 1, we can generate a W-random Z-decorated graph G(n,W) on node set [n] as follows: we select n independent uniformly distributed points x1,... ,xn from [0,1], and label every pair ij (1 ≤ i < j ≤ n) by W(xi,xj), and label every pair ii (1 ≤ i ≤ n) by 0 ∈ Z.

- Theorem 3.8. For every Z-graphon and every B-decorated graph F, t(F,G(n,W)) → t(F,W) (n → ∞)


with probability 1. As an immediate corollary, we get:

- Corollary 3.9. Every Z-graphon is the limit of a convergent sequence of Z-decorated graphs.


Proof. The proof is similar to the proof for the unweighted case in [10] and in [9], Section 11.2.1, but we have to be somewhat more careful because of the unbounded values that occur.

Let us ﬁx a countable generating set F ∈ B, and an F-decorated graph F = (F,f) on the node set [k]. It is easy to compute the expected injective subgraph densities in G(n,W), where n ≥ k. We can generate a random map [k] → [0,1] by composing a random map x : [n] → [0,1] with a random injective map ϕ : [k] → [n]. This gives us that

t(F,W) = ExEϕ

ij∈E(F)

f(ij),W(xϕ(i),xϕ(j)) = Ex tinj(F,G(n,W)) .

Lemma 2.3 implies that

Ext(F,G(n,W))) → t(F,W) (n → ∞).

This shows that W-random graphs yield a sequence with the desired subgraph densities in expectation. To show that these values are concentrated, we need to estimate the fourth moments (unfortunately, estimating the variance would not be quite enough). Sharper bounds can be obtained based on the theory of U-statistics, but the simpler argument

below will be suﬃcient for us. For ϕ : V (F) → [n], let Xϕ = tϕ(F,G(n,W)) − t(F,W). Then Ex(Xϕ) = 0 if ϕ is injective. Furthermore,

1 n4k ϕ

(t(F,G(n,W)) − t(F,W))4 =

![image 171](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile171.png>)

Xϕ1 ... Xϕ4,

1,...,ϕ4

where ϕ1,... ,ϕ4 range independently over all maps V (F) → [n]. Let us take expectation in x. If the range of any of the ϕi is disjoint from the others,

then the expectation of Xϕi can be taken separately, and if, in addition, ϕi is injective, then this expectation is 0. So only those terms remain in which for every i, the range of

ϕi intersects the range of at least one other ϕj, or ϕi is not injective. This implies that the range of ϕ1 ∪ ··· ∪ ϕ4 has at most 4k − 2 elements, and so the number of such terms O(n4k−2). The expectation of such a term is bounded by 2Πf · W 44||EE((FF))|| , and hence

Ex (t(F,G(n,W)) − t(F,W))4 = O

1 n2

![image 172](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile172.png>)

.

This implies that for every ﬁxed ε > 0, Pr |t(F,G(n,W)) − t(F,W)| > ε = Pr (t(F,G(n,W)) − t(F,W))4 > ε4 ≤

Ex (t(F,G(n,W)) − t(F,W))4 ε4

1 n2

= O

.

![image 173](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile173.png>)

![image 174](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile174.png>)

Hence ∞

n=1

Pr(|t(F,G(n,W)) − t(F,W)| > ε) < ∞,

and so by the Borel-Cantelli Lemma, with probability 1, |t(F,G(n,W))−t(F,W)| ≤ ε if n is large enough. With probability 1, this holds for every ε = 1,1/2,1/3,... simultaneously, which means that

t(F,G(n,W)) → t(F,W). (17) Since there are only a countable number of F-decorated simple graphs, (17) holds, with probability 1, for every F-decorated graph F simultaneously. We can use a similar argument to show that in addition, with probability 1, for each positive integer k, limn→∞ Wn k = W k. Since for any Z-graphon U and any p < k we have

U p ≤ U k+1, it follows that Wn p remains bounded for every p ≥ 1. In this case, (17) also holds for every B-decorated graph by Lemma 3.2, and so we get that, with probability 1, G(n,W) → W as n → ∞.

![image 175](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile175.png>)

![image 176](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile176.png>)

![image 177](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile177.png>)

![image 178](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile178.png>)

# 4 Convergence of multigraphs

The main application of the above theory pertains to sequences of multigraphs where there is no global bound on edge multiplicities, and we are interested in convergence of node-and-edge homomorphism numbers.

## 4.1 Multigraphs as Banach decorated graphs

To capture convergence of multigraphs, we would like to use probability distributions on N to decorate edges, because this would allow us to generate a random multiplicity for the edge. We want ﬁnite node-and-edge densities, and therefore we have to require that these distributions have ﬁnite moments. Such distributions generate the linear space J of signed measures on N having ﬁnite moments. For γ ∈ J , we denote by γ(p) = ∞n=0 γ(n)np its

p-th moment (p ≥ 0). We can also think of signed measures as sequences indexed by N, and then

J = x ∈ RN :

n

|xn|np < ∞ for all p ≥ 0 .

Let J+ = {x ∈ J : xn ≥ 0 ∀n ∈ N}. Note that P(N) = {x ∈ J+ : n xn = 1} consists of those probability distributions on N having ﬁnite moments.

Based on the special case of multigraphs with bounded edge multiplicity, the space J (more exactly, its subset P(N)) seems to be the right set to deﬁne limit graphons of multigraph sequences. However, there are two technical diﬃculties with this. First, there is no good way to turn J into a Banach space with a pre-dual, which we would need to be able to apply the machinery developed above. Second, the moments of distributions on N do not determine the distribution (but they determine subgraph multiplicities). In other words, we cannot (and should not) distinguish between two distributions with the same moments.

The ﬁrst problem will be addressed by introducing a weight function; the second, by taking the factor space J of J , in which two sequences are identiﬁed if they have the same moments.

Let us ﬁx a weight function ρ ∈ J+ (when we speak of a weight function, we assume that ρ(n) > 0 for all n ∈ N). Let the space

Cρ := {f : N → R|f(m)ρ(m) → 0} be equipped with the norm f ρ := f · ρ ∞. The dual of this Banach space is

Jρ := x ∈ RN :

m

|xm| ρ(m)

< ∞

![image 179](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile179.png>)

with the norm

x ρ :=

m

|xm| ρ(m)

.

![image 180](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile180.png>)

We note that Jρ ⊂ J .

Since ρ ∈ J+, we have (p(0),p(1),...) ∈ Cρ for every polynomial p ∈ R[X]; with some abuse of notation, we will denote this sequence by p. Let R denote the linear space of all such sequences, and let Rρ := R · 

ρ

![image 181](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile181.png>)

. Then Rρ is a closed subspace of Cρ, and so its dual Jρ is a factor space of Jρ. The elements of Jρ are equivalence classes of sequences; two of these sequences are equivalent if and only if they have the same moments (see, e.g., [4, Thm. III.10.1]).

We need a lemma about the existence of weight functions ρ. We call a family M of probability distributions on N moment-bounded, if for every p ≥ 1 there is a constant cp > 0 such that

µ(m)mp < cp for all µ ∈ M.

m≥0

Given a weight function ρ ∈ J+, we call the family M ρ-smooth, if for every p ≥ 1 there is a constant c′p > 0 such that

µ(m) ρ(m)p

< c′p for all µ ∈ M.

![image 182](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile182.png>)

m≥0

- Lemma 4.1. A family M of probability distributions is moment-bounded if and only if there exists a weight function ρ ∈ J+, such that M is ρ-smooth.


Proof. The “if” part is easy: Clearly ρ(m) ≤ 1/m if m is large enough (say m ≥ M), and hence for any p ≥ 1 mp ≤ Mp + 1/ρ(m)p. Thus

µ(m) ρ(m)p ≤ Mp + c′p.

µ(m)mp ≤

µ(m)Mp +

![image 183](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile183.png>)

m

m

m

To prove the “only if” direction, note that for every µ ∈ M,

∞

∞

cp+1 s

1 s

mpµ(m) ≤

mp+1µ(m) ≤

.

![image 184](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile184.png>)

![image 185](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile185.png>)

m=s

m=s

Hence for sj = 2jcj2+1, we have

∞

- 1

![image 186](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile186.png>)

- 2j


mj2µ(m) ≤

.

m=sj

Let ρ(m) = m−j for sj ≤ m < sj+1 (0 ≤ j) and ρ(m) = 1 for m ≤ s0. Clearly ρ ∈ J+, and

sj+1−1

sp−1

∞

∞

ρ(m)−pµ(m)

ρ(m)−pµ(m) +

ρ(m)−pµ(m) =

m=sj

m=0

m=0

j=p

sj+1−1

sp

∞

mp2µ(m) +

≤

m=sj

m=0

j=p

∞

∞

∞

mp2µ(m) +

≤

m=sj

m=0

j=p

∞ j=p Letting c′p = cp2 + 1, the lemma is proved.

- 1

![image 187](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile187.png>)

- 2j ≤ cp2 + 1.


≤ cp2 +

mj2µ(m)

mj2µ(m)

![image 188](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile188.png>)

![image 189](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile189.png>)

![image 190](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile190.png>)

![image 191](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile191.png>)

Remark 4.2. Let G be a multigraph on n vertices such that its multiedge distribution µ is ρ-smooth with constants c′p. Then with Z = Jρ equipped with the ρ norm, we have that the corresponding Z-graphon WG satisﬁes

∞

p

1 n2 1≤i≤j≤n

1 n2 1≤i≤j≤n

µ(ℓ) ρ(ℓ)p

1 ρ(gij)

p

δ{gij} ρ

WG pp =

< c′p,

=

=

![image 192](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile192.png>)

![image 193](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile193.png>)

![image 194](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile194.png>)

![image 195](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile195.png>)

ℓ=0

meaning that the constants in the ρ-smoothness translate to the p-th power of the constants for the various Lp-bounds (1 ≤ p < ∞). In particular a sequence (Gn) of ρ-smooth multigraphs will remain uniformly Lp bounded

- as Jρ-decorated graphs (Gn).


Let F := {Xk : k ∈ N} ⊆ R. By deﬁnition, the set F linearly generates R, and hence it is generating in Rρ, which thus is a separable space. We may turn a loopless multigraph F into an F-decorated graph F′ by decorating each edge ij with multiplicity m by Xm.

To each multigraph G = (G,g) (where G is the underlying simple graph and guv is the multiplicity of the edge uv), we can associate a Jρ-decorated complete graph by decorating each edge with multiplicity m by the probability distribution concentrated on m. Through the factor mapping we obtain a Jρ-decorated complete graph G′′. (Note that these measures in Jρ have ﬁnite support, and therefore they are determined by their

moments. So the factor mapping distinguishes the edge-labels in G′′.) For the node-andedge homomorphism density between two multigraphs G = (G,g) and F = (F,f), we have t(F,G) = t(F′,G′′) = t(F′,WG) as deﬁned for F-decorated graphs and Jρ-graphons. This can be expressed in terms of the moments as

Xfij,gϕ(i)ϕ(j)

t(F,G) =

ϕ:V (F)→V (G) ij∈E(F)

gϕ(f(iji))ϕ(j). (18)

=

ϕ:V (F)→V (G) ij∈E(F)

Now we turn to convergence of multigraph sequences. Recall that a sequence of (Gn) of multigraphs is node-and-edge convergent, if t(F,Gn) is a convergent sequence for every multigraph F.

Theorem 4.3. Let (Gn) be a sequence of multigraphs such that for every multigraph

- F, the sequence t(F,Gn) (in the node-and-edge sense) is convergent. Then there exists a weight function ρ ∈ J+ and a Jρ-graphon W such that t(F,Gn) → t(F′,W).


Proof. Let µn denote the edge-multiplicity distribution of Gn, i.e., µn(m) is the probability that uniformly chosen random nodes i and j of Gn are connected by m edges. (Nodes i = j are connected by 0 edges.) Let us observe that every moment of the probability measures µn is uniformly bounded (independently of n). Indeed, let Bp = (K2,p) denote the graph consisting of two nodes connected by p edges (the p-bond), then

m

µn(m)mp = t(Bp,Gn) ≤ cp,

since the sequence (t(Bp,Gn) : n ∈ N) is convergent and hence bounded.

Lemma 4.1 implies that there is a weight function ρ ∈ J+ such that the family M = {µn} is ρ-smooth.

In light of Remark 4.2 we may apply Theorem 3.7 to obtain a Jρ-graphon W such that lim

t(F′,G′′n) = t(F′,W) for every multigraph F.

t(F,Gn) = lim

n→∞

n→∞

![image 196](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile196.png>)

![image 197](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile197.png>)

![image 198](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile198.png>)

![image 199](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile199.png>)

An unpleasant point is that the space Jρ is awkward to deﬁne and work with. One way out would be to ignore that several distributions may have the same moments, and just select one distribution as W(x,y) out of the equivalence class. We don’t know, however, whether this can be done in a measurable way.

A better solution is to encode W(x,y) ∈ Jρ by its moment sequence. Let us call a sequence (a0,a1,... ) of real numbers a N-moment sequence, if there is a probability distribution µ on N such that ap = ∞m=0 µ(m)mp. Deﬁne

∞

π(m)mp,

Wp(x,y) =

m=0

where π ∈ W(x,y) is an arbitrary probability distribution from the equivalence class. By the deﬁnition of equivalence, this is independent of the choice of π, and in fact the sequence (W0(x,y),W1(x,y),... ) uniquely determines the equivalence class. Then for any multigraph F = (F,f),

t(F′,W) = t(F,W0,W1,... ) :=

Wf(ij).

ij∈E(F)

[0,1]V (F)

Thus we get the following corollary to Theorem 4.3:

Corollary 4.4. For every node-end-edge convergent sequence (Gn) of multigraphs there is a sequence (W0,W1,... ) of measurable, symmetric functions L ∋ Wi : [0,1]2 → [0,∞) such that for every (x,y) ∈ [0,1]2, the sequence (W0(x,y),W1(x,y),... ) is an N-moment sequence, and t(F,Gn) → t(F,W1,W2,... ) for every multigraph F.

## 4.2 W-random multigraphs

We have seen how to sample from a Jρ-graphon W; the result is a Jρ-decorated graph. However, in the case of simple graphs, sampling goes one step further, and we get a simple graph rather than a [0,1]-weighted graph. We can make the corresponding step in the case of multigraphs as well: in this case the limit objects are Jρ-graphons, and the ﬁrst sampling, as described in Section 3.5, gives a Jρ-decorated graph G(n,W). For each edge ij (i,j ∈ [n], i = j), we select a representative W′(i,j) from the equivalence class W(i,j), and generate a multiplicity m(i,j) from the distribution W′(i,j), to get a multigraph GR(n,W). Note the unfortunate indeterminacy in selecting the probability distribution W′(i,j); Corollary 4.6 below remains valid even if an adversary selects these distributions.

To describe this more exactly, let G = (G,g) be a Jρ-decorated complete graph. By a randomization of G, we mean a (random) multigraph GR, where the multiplicity Guv of an edge uv is randomly selected from the distribution guv, independently for diﬀerent edges. It will be convenient to assume that guu is concentrated on 0, so Guu = 0.

- Lemma 4.5. Let F be a multigraph with L edges. Then there is a constant c = c(F) > 0 such that if G = (G,g) is a Jρ-decorated complete graph with n nodes and ε > 0, then |t(F,G) − t(F,GR)| ≤ ε with probability at least 1 − c g(4L) 1/(ε4n2).


Proof. The proof is similar in structure to the proof of Theorem 3.8, but the details are diﬀerent. Let F = (F,f), where F is a simple graph with k nodes and l edges, fij is the multiplicity of edge ij, and L = ij fij is the number of edges in the multigraph F. Let

- G = (G,g), and let G have n nodes. Let gu,v(p) = E(Gpu,v) denote the p-th moment of Gu,v. This deﬁnition implies that for every p ≥ 1,


1 n2

1 n2

E(Gpu,v) =

gu,v(p) = g(p) 1. (19)

E( GR pp) =

![image 200](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile200.png>)

![image 201](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile201.png>)

u,v∈V (G)

u,v∈V (G)

Recall that

where

t(F,G) =

1 nk

homϕ(F,G),

![image 202](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile202.png>)

ϕ:V (F)→V (G)

gϕ(f(iji)),ϕ(j) =

E Gfϕij(i),ϕ(j) .

homϕ(F,G) =

ij∈E(F)

ij∈E(F)

Setting Xϕ = homϕ(F,GR)−homϕ(F,G) and using a similar expression for t(F,GR), we have

1 nk

t(F,GR) − t(F,G) =

Xϕ.

![image 203](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile203.png>)

ϕ:V (F)→V (G)

If ϕ is injective, then E homϕ(F,GR) = homϕ(F,G) (the expectation is taken over the randomization of the edge multiplicities), and so E(Xϕ) = 0. This shows that t(F,GR) will be close to t(F,G) in expectation.

To get that they are close with high probability, we need to estimate higher moments. We can write

1 n4k

t(F,GR) − t(F,G) 4 =

![image 204](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile204.png>)

Xϕ

ϕ:V (F)→V (G)

1 n4k ϕ

4

Xϕ1 ... Xϕ4. (20)

=

![image 205](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile205.png>)

1,...,ϕ4

Note that Xϕi is independent (as a random variable) from all Xϕj for which the range of ϕj is disjoint from the range of ϕi. This implies that if we take expectation in (20), only those terms remain where for every i, ϕi is non-injective or its range intersects the range of the other ϕj. Let us also note that if ϕ identiﬁes two adjacent nodes of F, then Xϕ = 0, so to get a non-zero term, all the ϕi must map edges of F onto distinct nodes. Call these terms bad. It is easy to see that this implies that the ranges of ϕ1,... ,ϕ4 cover

- at most 4k − 2 nodes of G, and so the number of bad 4-tuples of maps is bounded by n


4k−2 (4k − 2)4k < (4k)4kn4k−2. For a particular map ϕ, we use the bound

|Xϕ| ≤ homϕ(F,G) + homϕ(F,GR), which gives

homϕs(F,GR)

|Xϕ1 ... Xϕ4| ≤

homϕs(F,G)

S⊆[4] s∈S

s/∈S

Gfϕij

gϕ(fij)

s(i),ϕs(j).

=

s(i),ϕs(j)

S⊆[4] s∈S ij∈E(F)

s/∈S ij∈E(F)

We think of every summand on the right side as a product of 4L terms of the type (gϕ(fij)

s(i),ϕs(j))1/fij and Gϕ(i),ϕ(j), and use the inequality between the geometric mean and the power mean with exponent 4L. We get

|Xϕ1 ... Xϕ4| ≤

2 L

=

![image 206](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile206.png>)

1 4L s∈S

fij gϕ(fij)

![image 207](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile207.png>)

s(i),ϕs(j)

ij∈E(F)

S⊆[4]

4L/fij +

s/∈S ij∈E(F)

4

fij gϕ(fij)

s(i),ϕs(j)

s=1 ij∈E(F)

4L/fij + G4ϕL

s(i),ϕs(j) .

fijG4ϕL

s(i),ϕs(j)

Using the inequality that (gu,v(a))b ≤ gu,v(ab) for a,b ≥ 1, we get

4

2 L

fij gϕ(4L)

s(i),ϕs(j) + G4ϕL

|Xϕ1 ... Xϕ4| ≤

s(i),ϕs(j) .

![image 208](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile208.png>)

s=1 ij∈E(F)

Note that there are no terms here with ϕs(i) = ϕs(j). Furthermore, if ϕ1,... ,ϕ4 gives a bad term, then so does π ◦ ϕ1,... π ◦ ϕ4 for any permutation of V (G). If we average this over all permutations π of V (G), we get every term gu,v(4L) and G4u,vL (u = v) the same number of times:

1 n! π |Xπ◦ϕ1 ... Xπ◦ϕ4| ≤

2 Ln(n − 1)

fij gu,v(4L) + G4u,vL

![image 209](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile209.png>)

![image 210](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile210.png>)

u =v∈V (G) ij∈E(F)

2 L

fij g(4L) 1 + G 44LL

=

![image 211](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile211.png>)

ij∈E(F)

= 2 g(4L) 1 + 2 G 44LL (21) Hence summing over bad terms, we get

|Xϕ1 ... Xϕ4| ≤ 2(4k)4kn4k−2 g(4L) 1 + G 44LL .

bad

Taking the expectation in (20) and using (19) gives E (t(F,GR)−t(F,G))4 =

1 n4k ϕ

E(Xϕ1 ... Xϕ4)

![image 212](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile212.png>)

1,...,ϕ4 bad

2(4k)4k n2

4(4k)4k n2

g(4L) 1. Hence

g(4L) 1 + E( G 44LL) =

≤

![image 213](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile213.png>)

![image 214](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile214.png>)

Pr(|t(F,GR) − t(F,G)| > ε) = Pr((t(F,GR) − t(F,G))4 > ε4) ≤

E((t(F,GR) − t(F,G))4) ε4 ≤

4(4k)4k n2ε4

g(4L) 1, which proves the lemma.

![image 215](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile215.png>)

![image 216](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile216.png>)

![image 217](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile217.png>)

![image 218](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile218.png>)

![image 219](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile219.png>)

![image 220](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile220.png>)

Combining this lemma with Theorem 3.8, we get that every Jρ-decorated graphon is the limit of multigraphs: Corollary 4.6. For every Jρ-graphon W and every multigraph F,

t(F,GR(n,W)) → t(F,W) (n → ∞) with probability 1.

## 4.3 Node-convergence vs. node-and-edge convergence

When looking at sequences of multigraphs, several convergence notions are available. From the combinatorial standpoint, we have convergence of node-and-edge homomorphism densities and convergence of node homomorphism densities. From a more abstract point of view, we have convergence in the compactiﬁcation sense [11, 7, 9], i.e., we take the onepoint compactiﬁcation N of N, and consider multigraphs as graphs decorated with measures from R(N). Alternatively, we have convergence in the weighted Banach space sense introduced in the previous section. As we have seen, the latter convergence notion corresponds to the combinatorial node-and-edge convergence. On the other hand, compactiﬁcation convergence corresponds to convergence in the node-homomorphism sense. To be precise, let G(t) denote the multigraph obtained from the multigraph G by truncating its edgemultiplicities at t. The following proposition characterizes node-convergence [11, 7, 9]:

![image 221](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile221.png>)

![image 222](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile222.png>)

Proposition 4.7. For a sequence of multigraphs (G1,G2,... ), the following are equivalent:

- (i) The sequence is convergent in terms of node-homomorphism densities.
- (ii) The sequence is convergent as N-labeled graphs.

![image 223](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile223.png>)

- (iii) For every t ∈ N, the truncated sequence (G(1t),G(1t),... ) is convergent as a sequence


of multigraphs with bounded edge-multiplicities. Indeed, convergence in the truncated multiplicity sense corresponds to decorating our

test graphs with the truncated polynomials qk(n) := min{nk,kk}. The linear span of the truncated polynomials is the same as the space generated by the characteristic functions

fk := {k} for all k, together with the constant 1 function (which is actually q0). These in turn generate C(N), and thus the three convergence notions are equivalent.

![image 224](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile224.png>)

In the case of graph sequences with uniformly bounded edge multiplicities, convergence in the node-and-edge homomorphism sense is also equivalent. How are the two types of convergence related in the general case? We shall show that these notions are not equivalent in general, but under appropriate conditions they are closely related.

We start with two examples.

- Example 4.8. Let Gn be the multigraph on [n] with cnn2 edges but with o(n2) distinct edges, where (cn) is an arbitrary bounded sequence. This graph sequence is convergent in the node-sense. The truncated graph G(nt) has o(n2) edges, and hence it tends to the identically zero graphon. However, the edge densities t(K2,Gn) = cn do not form a convergent sequence in general, so this sequence is not convergent in the node-and-edge sense.
- Example 4.9. Let σ and τ be two diﬀerent probability distributions on N with ﬁnite moments and having the same moments (such distributions exist, see, e.g., [12]1 ) We consider σ and τ as elements of Jρ for some appropriate weight function ρ. Let [σ] = [τ] =: µ ∈ Jρ denote their equivalence class in the factor space. Let U(x,y) ≡ σ, W(x,y) ≡ τ, and V (x,y) ≡ µ. Then V is a Jρ-graphon. Next, we wish to apply Corollary 4.6 to the


Jρ-graphon V . But as noted before, we may chose which probability distributions from the given equivalence class we wish to use to generate our random multigraphs. Therefore we shall generate one family with the help of U, and one family with the help of W. Consider the random multigraphs Gn = GR(n,[U]) and Hn = GR(n,[W]). We know by Corollary 4.6 that t(F,Gn) → t(F,V ) and t(F,Hn) → t(F,V ) almost surely. This means that merging the two sequences, we get a sequence (G1,H1,G2,H2,G3,H3,... ) that is almost surely convergent in the node-and-edge sense.

On the other hand, there is a j ∈ N such that σj = τj, and then the truncated distributions

 

 

σi, if i ≤ j,

τi, if i ≤ j,

σi, if i ≤ j + 1, 0, otherwise,

τi, if i ≤ j + 1, 0, otherwise,

σi(j+1) =

and τi(j+1) =

i>j

i>j





are diﬀerent. The truncated graphs G(nj+1) can be considered as random graphs GR(n,[U′]) (where U′(x,y) ≡ σ(j+1)), and hence they converge to [U′] almost surely, and simi-

larly H(nj+1) → [W′] almost surely (where W′(x,y) ≡ τ(j+1)). But σ(j+1) and τ(j+1) are diﬀerent distributions with a ﬁnite support, and hence their moments are not the same; this means that t(Bp,[U′]) = t(Bp,[W′]) for an appropriate p ∈ N∗, and hence t(Bp,G(nj+1)) and t(Bp,H(nj+1)) have diﬀerent limits. So the truncated sequence (G(1j+1),H1(j+1),G(2j+1),H(2j+1),G(3j+1),H(3j+1),... ) is not convergent, which implies that (G1,H1,G2,H2,G3,H3,... ) is almost surely not convergent in the compactiﬁcation sense. Proposition 4.10. Suppose the multigraph sequence Gn is convergent in the node sense. If the numbers t(Bp,Gn) are bounded for each p ∈ N, then the graph sequence is also convergent in the node-and-edge sense.

Proof. By Lemma 4.1, we can choose a weight function ρ ∈ J+ such that the family of edge multiplicity distributions is ρ-smooth. All polynomials and all truncated polynomials lie in C(N,ρ). For any polynomial P we have limn→∞ P(n)ρ(n) = 0, and hence they all lie in the closed linear span of the truncated polynomials. Hence the compactiﬁcation limit is also a limit in the multigraph sense.

![image 225](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile225.png>)

![image 226](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile226.png>)

![image 227](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile227.png>)

![image 228](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile228.png>)

## 4.4 Node-and-edge vs. sample convergence and exchangeability

For simple graphs and bounded, [0,1]-valued graphons, it is well known that homomorphism density convergence is equivalent to sample convergence (cf. [9, Section 5.2.4]). In

![image 229](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile229.png>)

1The explicit example given there is as follows: given a ﬁxed integer q ≥ 2, let σ({a}) = e−qqn/n! and τ({a}) = e−qqn n 1! + n (−1)n

m=1(qm−1) whenever a = qn for some n ∈ N∗, and let all other natural numbers have zero measure.

![image 230](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile230.png>)

![image 231](<2014-kunszentikovacs-multigraph-limits-unbounded-kernels_images/imageFile231.png>)

our formalism, following Example 2.4, this means that given a sequence Wn : [0,1]2 → R2 of symmetric measurable functions with Wn(x,y) ∈ (a,b) ∈ R2 |a,b ≥ 0,a + b = 1 , we have that (t(F,Wn))n∈N∗ converges for every simple graph F if and only if the distribution of GR(k,Wn) over the set of simple graphs on k vertices converges in the weak-* (or vague) topology – here equivalent to weak convergence of measures – as n → ∞ for every k ∈ N∗. In more generality, Lov´asz and Szegedy showed ([11, Theorem 2.3]) the same equivalence in the setting of compact decorations, i.e., when B = C(K) for some compact separable topological space K (see Section 2.3). It is thus a natural question to ask what happens in the case of mulitgraphs with unbounded edge multiplicities. Convergence of the samples would provide a connection to exchangeable arrays and Aldous’ representation theorem for these.

The ﬁrst non-trivial hurdle is what topology to choose for the distributions. As GR(k,Wn) now lives on a locally compact, rather than a compact space, weak convergence (from the weak duality with Cb(X)) and weak-* convergence (from the Riesz-Markov duality (C0(X)∗ = M(X)). The second is that the former convergence notion would preserve total measure (i.e. a sequence of probability distributions would have a limit that’s always a probability distribution), but compactness is lost, whereas the latter allows one to make use of weak-* compactness, but a sequence of probability distributions may actually end up with a zero limit. Thirdly, no matter which we choose, even if we assume that the sequences GR(k,Wn) have probability distributions as their limits, the density functions t(F,·) are not bounded (except for zero-decorations), and even less in C0, convergence of distributions does not immediately imply convergence in densities. Issues are also present for the reverse direction, in that unboundedness naturally leads into moment indeterminacy problems. In particular the counter-example from [8, Section 7.3] can be adapted to this setting as well.

Example 4.11. Let σ and τ be two diﬀerent probability distributions on N with ﬁnite moments and having the same moments (as in Example 4.9). Denote their n-th moments by Mn (n ≥ 0). Let further {Si}i∈N and {Tj}j∈N be two partitions of [0,1] into measurable sets such that λ(Si) = σ({i}) and λ(Tj) = τ({j}) for all i,j ∈ N. Consider the functions gσ,gτ : [0,1] → R deﬁned by

gσ(x) := nx whenever x ∈ Snx, gτ(x) := mx whenever x ∈ Tmx,

respectively, and let Wσ,Wτ : [0,1]2 → Jρ be deﬁned by Wσ(x,y) := δ{gσ(x)·gσ(y)} and Wτ(x,y) = δ{gτ(x)·gτ(y)}, respectively, where ρ ∈ J+ is chosen so that Wσ,Wτ both have ﬁnite · p-norms for all 1 ≤ p < ∞ (such a ρ can be guaranteed with arguments similar to the ones used in the proof of Lemma 4.1).

Let F be a multigraph, let the elements of V (F) be denoted by v1,v2,... ,vk, let fij denote the multiplicity of the edge vivj ∈ E(F), and let di denote the degree of vertex vi (with multiplicities). It can then easily be seen that we have

t(F,Wσ) =

=

(gσ(xi) · gσ(xj))fijdx1 ... xk

x1,...,xk∈[0,1] vivj∈E(F)

k

k

gσ(xi)didxi =

Mdi.

i=1 [0,1]

i=1

Similar calculations yield t(F,Wσ) = ki=1 Mdi, and so the two graphons have the exact same node-and-edge homomorphism densities. Yet, GR(2,Wσ) is the random multiedge

where the multiplicity distribution is the distribution of gσ(x)gσ(y), whilst GR(2,Wτ) is the random multiedge where the multiplicity distribution is the distribution of gτ(x)gτ(y), and these two are not equal. To turn this into an actual counter-example with respect to the convergence notions at hand, we shall generate a sequence of multigraphs from each of the graphons. Let us ﬁrst consider Wσ, the other sequence can be obtained in an analoguous way. For each n ∈ N, let σn be the probability distribution obtained from σ by cutting oﬀ it’s tail above n and setting it to zero, i.e., σ|P({1,...,n}) = σn|P({1,...,n}), σn({n + 1,n + 2,...}) = 0, and σn({0}) = σ({0}∪{n+1,n+2,...}). Next, let the probability distribution σn be obtained from σn by choosing some large enough kn ∈ N∗, and letting σn({m}) := ⌊knσn({m})⌋/kn for all m ≥ 1 in such a way that σn − σn TV < 1/n. Finally, letting Wσ,n be the graphon obtained from σn the same way Wσ was constructed from σ, the graphon Wσ,n will be a stepfunction that represents a multigraph Gσ,n on kn vertices. By construction, the total variational distance of σn and σ tends to zero as n → ∞, meaning that GR(k,Wσ,n) will tend in total variation distance to GR(k,Wσ). Note that convergence also holds in L2, and so a fortiori in jumble norm as well. On the other hand, Wσ − Wσ,n 2 will also tend to zero, and by Corollary 2.15, limn→∞ t(F,Wσ,n) = t(F,Wσ). In other words, the multigraph sequences (Gσ,n)n∈N∗ and (Gτ,n)n∈N∗ have the same limit with respect to nodeand-edge densities, but have two diﬀerent limits with respect to convergence of samples or convergence in jumble norm.

We do expect to have settings (as in the previous section) where these convergence notions coincide, but it is beyond the scope of the present paper to go investigate the details.

# 5 Concluding remarks

- 5.1. An almost identical construction as in Section 4 can be used to deﬁne and study convergent sequences of edge-weighted graphs with no universal bound on the weights. In this case we use as a weight function an appropriate function ρ : [0,∞) → R+, and we replace the set of natural numbers used in the previous example by the set of nonnegative reals, summation by integral etc. Caution: one has to distinguish more carefully functions and signed measures (which were interchangeable in the discrete case above). We don’t go into the details of this.
- 5.2. Using a generalized H¨older Inequality, Borgs, Chayes, Cohn and Zhao [1] proved the following inequality stronger than Lemma 2.3 and inequality (4):

t(F,w) ≤

ij∈E(F)

wij ∆(F),

where ∆(F) is the maximum degree in F. We could improve several of our bounds using similar methods. This has not been our goal in this paper, but it remains an interesting open problem to extend our results in this direction.

- 5.3. The theory of simple graph limits is closely related to the characterization of homomorphism functions. Such characterizations are known, among others, for simple graph parameters of the form hom(.,G) (where G is a simple graph with loops, or an edgeweighted graph, or a node-and-edge-weighted graph), and also for parameters of the form t(.,W), where W is (bounded) graphon. Extending these characterizations to the Banach space decorated, or compact decorated, case seems to be a challenging problem.


# Acknowledgements

The authors would like to thank S. Janson and the anonymous referee for their thorough read of the original manuscript. Their valuable comments and suggestions have led to a more self-contained ﬁnal paper.

# References

- [1] C. Borgs, J.T. Chayes, H. Cohn and Y. Zhao: An Lp theory of sparse graph convergence I: limits, sparse random graph models, and power law distributions, Trans. Amer. Math. Soc. 372 (2019), 3019–3062.
- [2] C. Borgs, J.T. Chayes, L. Lov´asz, V.T. So´s and K. Vesztergombi: Convergent Graph Sequences I: Subgraph frequencies, metric properties, and testing, Advances in Math. 219 (2008), 1801–1851.
- [3] C. Borgs, J.T. Chayes, L. Lov´asz, V.T. So´s and K. Vesztergombi: Convergent Graph Sequences II: Multiway Cuts and Statistical Physics, Annals of Math. 176 (2012), 151–219.
- [4] J.B. Conway, A course in Functional analysis (2nd Ed.), Graduate texts in mathematics 96, Springer (1990)
- [5] A. Frieze and R. Kannan: Quick approximation to matrices and applications, Combinatorica 19 (1999), 175–220.
- [6] S. Janson: Graphons, cut norm and distance, couplings and rearrangements, NYJM Monographs 4, New York Journal of Mathematics, State University of New York, University at Albany, Albany, NY, (2013)
- [7] I. Kolossva´ry and B. Ra´th: Multigraph limits and exchangeability, Acta Math. Hung. 130 (2011), 1–34.
- [8] D. Kunszenti-Kov´acs: Uniqueness of Banach space valued graphons, Journal of Mathematical Analysis and Applications 474 (2019), 413–440.
- [9] L. Lov´asz, Large graphs, graph homomorphisms and graph limits, AMS (2012).
- [10] L. Lov´asz and B. Szegedy: Limits of dense graph sequences, J. Combin. Theory B 96

(2006), 933–957.

- [11] L. Lov´asz, B. Szegedy: Limits of compact decorated graphs, http://arxiv.org/abs/1010.5155
- [12] J.-P. Merx, https://www.mathcounterexamples.net/determinacy-of-random-variables/
- [13] K. Musial, Pettis integral, Handbook of Measure Theory I, North Holland, (2002)
- [14] A. Thomason: Pseudorandom graphs, in: Random graphs ’85 North-Holland Math. Stud. 144, North-Holland, Amsterdam, 1987, 307–331.


David´ Kunszenti-Kovacs.´ Alfre´d Re´nyi Institute of Mathematics, Budapest, Hungary. daku@renyi.hu

Laszl´ o´ Lovasz.´ Alfre´d Re´nyi Institute of Mathematics and Institute of Mathematics, Eo¨tv¨os Lor´and University, Budapest, Hungary. laszlo.lovasz@ttk.elte.hu

Balazs´ Szegedy. Alfre´d Re´nyi Institute of Mathematics, Budapest, Hungary. szegedy.balazs@renyi.hu

