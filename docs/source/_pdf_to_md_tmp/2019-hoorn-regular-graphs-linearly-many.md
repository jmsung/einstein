arXiv:1904.02212v3[math.CO]14Apr2021

Regular graphs with many triangles are structured

Pim van der Hoorn1, Gabor Lippner2, and Elchanan Mossel3,4 1TU Eindhoven, Department of Mathematic and Computer Science 2Northeastern University, Department of Mathematics 3MIT, Department of Mathematics 4MIT Institute for Data Systems and Society April 16, 2021

Abstract

We compute the leading asymptotics of the logarithm of the number of d-regular graph having at least a ﬁxed positive fraction c of the maximum possible number of triangles, and provide a strong structural description of almost all such graphs.

When d is constant, we show that such graphs typically consist of many disjoint d + 1cliques and an almost triangle-free part. When d is allowed to grow with n, we show that such graphs typically consist of d + o(d) sized almost cliques together with an almost triangle-free part.

This conﬁrms a conjecture of Collet and Eckmann from 2002 and considerably strengthens their observation that the triangles cannot be totally scattered in typical instances of regular graphs with many triangles.

# 1 Introduction

It is easy to see that a d-regular graph on n nodes cannot have more than Tmax = Tmax(n, d) =

d

n 3

2 triangles, and that this value is achieved exactly if the graph is a disjoint union of d+1cliques. In this paper we prove a strong, almost sure structural stability result for this extremal problem: Let 0 < c ≤ 1 and let Gd,c(n) denote the set of d-regular graphs on n labeled nodes that contain at least c · Tmax triangles. We show that, for constant d and large n, almost all graphs in Gd,c(n) consist of a disjoint union of d + 1 cliques and an almost triangle-free part.

![image 1](<2019-hoorn-regular-graphs-linearly-many_images/imageFile1.png>)

This result may not seem surprising at ﬁrst, and especially for c close to 1 it seems quite natural to expect. However we would like to emphasize that it also holds for very small positive c. In that regime the required number of triangles could easily be arranged in such a way that no vertex has more than 1 triangle in its neighborhood. However, as it turns out, such graphs only constitute a vanishing fraction of elements of Gd,c(n).

The study of Gd,c(n) has been initiated by Collet and Eckmann [6], who proved

log Gd,c(n) log Gd(n) ≤ 1 −

log Gd,c(n) log Gd(n) ≤ lim sup

2d d + 1 ≤ lim inf

c 3

1 − c

, (1)

![image 2](<2019-hoorn-regular-graphs-linearly-many_images/imageFile2.png>)

![image 3](<2019-hoorn-regular-graphs-linearly-many_images/imageFile3.png>)

![image 4](<2019-hoorn-regular-graphs-linearly-many_images/imageFile4.png>)

![image 5](<2019-hoorn-regular-graphs-linearly-many_images/imageFile5.png>)

n→∞

n→∞

where Gd(n) is the set of all d-regular graphs on n labeled nodes. They conjectured that this limit exists. Using a heuristic counting argument they concluded that the triangles should be clustered in a “typical” element of Gd,c(n).

In this paper we prove their conjecture and ﬁnd the correct limiting value

log Gd,c(n) log Gd(n)

d − 1 d + 1

= 1 − c ·

lim

. (2)

![image 6](<2019-hoorn-regular-graphs-linearly-many_images/imageFile6.png>)

![image 7](<2019-hoorn-regular-graphs-linearly-many_images/imageFile7.png>)

n→∞

Furthermore we prove that the observation that triangles are clustered in typical elements of Gd,c(n) hold in a very strong sense: for almost all graphs in the class, almost all triangles are contained in d + 1-cliques.

- 1.1 Probabilistic context


While our methods are purely combinatorial, the results are more conveniently stated in the language of random graphs. What is the probability that a random graph has a lot more triangles than expected? This is a typical question in the ﬁeld of large deviations, the theory that studies the tail behavior of random variables or, stated diﬀerently, the behavior of random objects conditioned on a parameter being far from its expectation. For example, one of the earliest results of this ﬂavor, Crame´r’s Theorem states that for i.i.d. variables X ∼ X1, X2, . . . there exists a “rate function” I(x) depending on the distribution of X such that

P

N

1

Xi ≥ Nx ≈ e−N·I(x).

- 1.1.1 Upper tail interpretation

In random graphs, the question about the upper tail for triangles in G(n, p) has been long studied for a constant factor of deviation from the mean [11]. More precisely, let t(G(n, p)) denote the triangle density in the Erd˝s-Re´nyi random graph, normalized so that E [t(G(n, p))] = p3. One would like to understand the asymptotic behavior of

r(n, p, δ) = −log P t(G(n, p) > (1 + δ)p3

The dense case (p a constant) has been reduced to an analytic variational problem by Chatterjee and Varadhan [5] using methods from graph limits. However, the solution of this variational problem is only known in certain parameter ranges (see [18] for details). In the sparse (p = o(1)) regime the asymptotics r(n, p, δ) ≈ n2p2 log(1/p) have been determined in a long series of papers by many authors [23, 16, 12, 10, 3, 8]. The variational methods were extended to (part of) the sparse regime in [4] and using this, Lubetzky and Zhao [19] found the exact asymptotics of r(n, p,δ) in the n−1/42 log n ≤ p ≪ 1 range. Recently, Cook and Dembo [7] and Augeri [2] extended it to the range n−1/2 ≪ p ≪ 1, and Harel, Mousset and Samotij [9] to all n−1 log n ≪ p ≪ 1.

In the case of random regular graphs Gd(n) have been studied much less. Kim, Sudakov, and Vu [15] obtained that the distribution of small subgraphs of Gd(n) is asymptotically Poisson in the sparse case, implying an asymptotic formula for the tail probability P(T(Gd(n)) > (1 + δ)E[T(Gd(n))]), where T(G) denotes the number of triangles in the graph G. The expected number of triangles in Gd(n) is ﬁnite. This means that the “standard” regime for large deviations - exceeding the expected value by a constant factor - in this case is not interesting.

- 1.1.2 Maximum entropy random graphs with triangles


In this note we are interested in the more extreme tail probability P T(Gd(n)) > c d2 n/3 . The reason for analyzing this tail probability originated from a related problem of ﬁnding

random graph models that maximize entropy under speciﬁc constraints.

Let Pn be some probability distribution on the set G(n) of graphs on n labeled nodes. Then the entropy of Pn is deﬁned as

E[Pn] =

−Pn(G) log (Pn(Gn)) . (3)

G∈G(n)

Now let G∗(n) denote the set of graphs on n labeled nodes with some additional properties, for instance speciﬁed edge or triangle densities. Then, in order to study the structure of ”typical” graphs with these constraints, one wants to ﬁnd the uniform distribution on G∗(n). This corresponds to ﬁnding the distribution P∗n that maximizes the entropy E[Pn] subject to the constraint that P∗n = 0 outside G∗(n).

It turns out that in many cases, computing the rate function also comes down to solving an optimization problem involving entropy. For example, Chatterjee and Dembo [4] showed that, up to lower order terms, the rate function corresponding to the large deviation result for subgraph counting can be expressed as the solution to a speciﬁc entropy related optimization problem. For large deviations of triangles, let Gn denote the set of undirected graphs on n

nodes with edges weights gij ∈ [0, 1], then the rate function is obtained, up to lower order terms, as

r(n, p, δ) = inf Ip(G) : G ∈ Gn, t(G) > (1 + δ)p3 .

where t(G) = n−3 1≤i,j,k≤n gijgjkgki and Ip(G) is the so-called relative entropy of the weighted graph G

gij p

gij log

Ip(G) =

![image 8](<2019-hoorn-regular-graphs-linearly-many_images/imageFile8.png>)

1≤i<j≤n

1 − gij 1 − p

+ (1 − gij) log

.

![image 9](<2019-hoorn-regular-graphs-linearly-many_images/imageFile9.png>)

In the case of dense graphs, such optimizations problems can be used to establish structural results for constrained random graphs. In the case of edge and triangle densities, a collection of research by Kenyon, Radin and co-authors [21, 20, 13, 14] showed that the limits of dense maximal entropy random graphs with given edge and triangle densities have a bipodal structure, at least in a narrow range just above the average. This means that the graph is split into two components with speciﬁc inter- and intra-component connection probabilities.

Recently, some techniques have been extended to solve the problem of ﬁnding maximum entropy sparse graphs with a given power-law degree distribution [22]. However, the degree distribution is a relatively global characteristic and hence is not expected to inﬂuence graph structures that much. A natural extension of this problem is therefore to include a constraint related to triangles, try to ﬁnd the corresponding maximum entropy solutions and see what this tells us about the structure of such graphs. A key motivation for this kind of question is the work by Krioukov [17], which hinted to the fact that triangle constraints might enforce the resulting maximum entropy solution to have some geometric component.

- 1.2 Results


Motivated by the question “can local constraints induce global (geometric) behavior?”, we study the random d-regular graph Gd(n) conditioned on having at least a positive fraction of the maximum possible number of triangles. (For d ﬁxed this just means linearly many triangles, in n.) With respect to the previous section, our setting is related to the entropy maximization problem with local and global constraints, i.e. where each node must have degree exactly d and must be incident to at least t triangles on average.

Let Tmax = Tmax(n, d) = d2 n/3 be the maximum number of triangles an n vertex dregular graph can have. Let Gd,c(n) denote the set of d-regular graphs on n labeled nodes that contain at least c · Tmax triangles. We compute the leading asymptotics of |Gd,c(n)| for ﬁxed c, as n → ∞, where d is either a constant or can grow with n as long as log d = o(log n). We provide a structural description of a “typical” element of Gd,c(n). We then extend these results to case of k-cliques in d-regular graphs.

- 1.2.1 Number of d-regular graph with many triangles


The dependence of d on n will be suppressed from the notation. We always assume d = o(n). We will emphasize when constant d is assumed.

- Theorem 1.1. For a ﬁxed 0 < c < 1 we have


−O

log|Gd,c(n)|

d − 1 d + 1 ≤ c

1 log nd ≤

log d log d+1n

2 log d+1n − 1 − c ·

+ O

![image 10](<2019-hoorn-regular-graphs-linearly-many_images/imageFile10.png>)

![image 11](<2019-hoorn-regular-graphs-linearly-many_images/imageFile11.png>)

![image 12](<2019-hoorn-regular-graphs-linearly-many_images/imageFile12.png>)

![image 13](<2019-hoorn-regular-graphs-linearly-many_images/imageFile13.png>)

dn

![image 14](<2019-hoorn-regular-graphs-linearly-many_images/imageFile14.png>)

![image 15](<2019-hoorn-regular-graphs-linearly-many_images/imageFile15.png>)

![image 16](<2019-hoorn-regular-graphs-linearly-many_images/imageFile16.png>)

![image 17](<2019-hoorn-regular-graphs-linearly-many_images/imageFile17.png>)

1 log nd

![image 18](<2019-hoorn-regular-graphs-linearly-many_images/imageFile18.png>)

![image 19](<2019-hoorn-regular-graphs-linearly-many_images/imageFile19.png>)

The part dn2 log d+1n is related to log|Gd(n)|, where Gd(n) denotes the set of d-regular graphs on n nodes. In particular, using the results in [1], one can show that

![image 20](<2019-hoorn-regular-graphs-linearly-many_images/imageFile20.png>)

![image 21](<2019-hoorn-regular-graphs-linearly-many_images/imageFile21.png>)

log|Gd(n)| dn

lim

= 1

![image 22](<2019-hoorn-regular-graphs-linearly-many_images/imageFile22.png>)

2 log d+1n

n→∞

![image 23](<2019-hoorn-regular-graphs-linearly-many_images/imageFile23.png>)

![image 24](<2019-hoorn-regular-graphs-linearly-many_images/imageFile24.png>)

The O(1/ log(n/d)) terms are o(1) as long as d = o(n). The c log d/log(n/d) term on the right hand side is only o(1) if log d = o(log n). Unfortunately, for d polynomial in n we do not get a sharp logarithmic rate.

- 1.2.2 Structure of d-regular graph with many triangles

For ﬁxed d, it turns out, perhaps not so surprisingly, that in most elements of Gd,c(n), most of the triangles cluster into (disjoint) d+1-cliques. To make this statement precise, let us call a node bad if it is not part of a d + 1-clique but it is incident to at least one triangle.

- Theorem 1.2. Let d be ﬁxed and 0 < c < 1. With high probability a uniformly randomly chosen element of Gd,c(n) has less than logloglognnn bad nodes. Thus, the number of triangles that are not part of a d + 1-clique is sublinear.

![image 25](<2019-hoorn-regular-graphs-linearly-many_images/imageFile25.png>)

In Section 2.2 we prove a slightly more general result where we consider the case where a uniformly randomly chosen element of Gd,c(n) has less than εnn bad nodes, with εn → 0, such that εn log n → ∞.

Note that Theorem 1.2 hints at a graph structure similar to the bipodal case, where instead of two components, we now have a linear in n number of cliques and some remaining larger graph with a sub-linear number of triangles.

We prove a similar result for the 1 ≪ d ≪ n case. Here, however, we cannot expect

- d + 1-cliques to appear, as it is possible to construct families of examples with the correct leading logarithmic growth rate, that don’t have any cliques. Instead, we introduce a notion of a pseudo-clique, which turns out to be a very dense subgraph of size d + o(d) with the property that diﬀerent pseudo-cliques must be disjoint. (See the explanation at the beginning of Section 2.2.2 for details.) It turns out that a typical element of the ensemble consists of a collection of these pseudo-cliques together with an almost triangle-free part.


- Theorem 1.3. Let 1 ≪ d ≪ n and ﬁx 0 < c < 1. With high probability, almost all triangles of a uniformly randomly chosen element of Gd,c(n) are contained in pseudo-cliques.

1.2.3 d-regular graph with many k-cliques

As a corollary to our methods, we also obtain similar results for regular graphs with many k-cliques. Let Gd,c,k(n) denote the set of d-regular graphs on n nodes that contain at least c · Tk,max = c k− d1 n/k subgraphs isomorphic to Kk. As a natural extension of terminology, we call nodes bad if they are not part of a d + 1-clique but are incident to a k clique.

- Theorem 1.4. For k ≥ 3 and ﬁxed 0 < c < 1 we have




log|Gd,c,k(n)| (d/2)n log n − 1 − c ·

d − 1 d + 1

![image 26](<2019-hoorn-regular-graphs-linearly-many_images/imageFile26.png>)

![image 27](<2019-hoorn-regular-graphs-linearly-many_images/imageFile27.png>)

= O(log d/log n)

Furthermore, for d ﬁxed, almost all elements of Gd,tk,k(n) will have at most εn bad nodes.

# 2 Proofs

- 2.1 The number of regular graphs with a given number of triangles


The proof of Theorem 1.1 consist of establishing a lower and upper bound on log |Gd,c(n)|. More precisely, we will show that

d − 1 d + 1

−O (dn) ≤ log |Gd,c(n)| − 1 − c ·

![image 28](<2019-hoorn-regular-graphs-linearly-many_images/imageFile28.png>)

n d + 1 ≤ c

dn 2

dn 2

log

![image 29](<2019-hoorn-regular-graphs-linearly-many_images/imageFile29.png>)

![image 30](<2019-hoorn-regular-graphs-linearly-many_images/imageFile30.png>)

![image 31](<2019-hoorn-regular-graphs-linearly-many_images/imageFile31.png>)

log d + O(dn).

The theorem then follows after dividing by dn2 log d+1n and letting n → ∞. Proof of Theorem 1.1 (Lower bound). To establish a lower bound we construct a family of elements in Gd,c(n) by letting

![image 32](<2019-hoorn-regular-graphs-linearly-many_images/imageFile32.png>)

![image 33](<2019-hoorn-regular-graphs-linearly-many_images/imageFile33.png>)

c · n d + 1

b = c · Tmax · d+13 −1 =

,

![image 34](<2019-hoorn-regular-graphs-linearly-many_images/imageFile34.png>)

taking b disjoint d + 1-cliques and an arbitrary m = n − (d + 1)b = (1 − c)n node d-regular graph. Clearly, these graphs will have at least c · Tmax triangles.

The number of d-regular graphs on m nodes satisﬁes

|Gd(m)| ∼ e1/4

m − 1 d

m m

2 dm 2

![image 35](<2019-hoorn-regular-graphs-linearly-many_images/imageFile35.png>)

m(m − 1) md

−1

for any d = d(m) ≤ m − 2, as m → ∞, see [1]. Using the standard (a/b)b ≤ ab ≤ (ea/b)b bounds, it is easy to obtain

- 1

![image 36](<2019-hoorn-regular-graphs-linearly-many_images/imageFile36.png>)

- 2


m

log|Gd(m)| ≥

d + 1 − dm − O(1). (4) The size of our family of graphs thus satisﬁes

dmlog

![image 37](<2019-hoorn-regular-graphs-linearly-many_images/imageFile37.png>)

n d+1

n−(d+1)

d+1 · · · n−(b−d+11)(d+1) b! |Gd(m)| =

n! m!b!(d + 1)!b |Gd(m)|.

|Gd,c(n)| =

![image 38](<2019-hoorn-regular-graphs-linearly-many_images/imageFile38.png>)

![image 39](<2019-hoorn-regular-graphs-linearly-many_images/imageFile39.png>)

Again a simple computation using the |log k!−(k log k−k+1/2 log k)| ≤ O(1) approximation, and noting that n = m + b(d + 1) = (1 − c)n + b(d + 1), gives

- 1

![image 40](<2019-hoorn-regular-graphs-linearly-many_images/imageFile40.png>)

- 2


- 1

![image 41](<2019-hoorn-regular-graphs-linearly-many_images/imageFile41.png>)

- 2


log|Gd,c(n)| ≥ n log n − n +

log n − (mlog m − m +

log m) − b((d + 1) log(d + 1) − (d + 1) +

- 1

![image 42](<2019-hoorn-regular-graphs-linearly-many_images/imageFile42.png>)

- 2


- 1

![image 43](<2019-hoorn-regular-graphs-linearly-many_images/imageFile43.png>)

- 2


log(d + 1)) − (b log b − b +

log b)

d 2

d 2

m log m −

mlog d − dm

+

![image 44](<2019-hoorn-regular-graphs-linearly-many_images/imageFile44.png>)

![image 45](<2019-hoorn-regular-graphs-linearly-many_images/imageFile45.png>)

- 1 − c

![image 46](<2019-hoorn-regular-graphs-linearly-many_images/imageFile46.png>)

- 2


m d + 1

m d + 1 −

cn d + 1

m d + 1 − O(dn)

= cn log

+

dnlog

log

![image 47](<2019-hoorn-regular-graphs-linearly-many_images/imageFile47.png>)

![image 48](<2019-hoorn-regular-graphs-linearly-many_images/imageFile48.png>)

![image 49](<2019-hoorn-regular-graphs-linearly-many_images/imageFile49.png>)

![image 50](<2019-hoorn-regular-graphs-linearly-many_images/imageFile50.png>)

(1 − c) · d 2

c d + 1

m d + 1 − O(dn)

= c −

+

n log

![image 51](<2019-hoorn-regular-graphs-linearly-many_images/imageFile51.png>)

![image 52](<2019-hoorn-regular-graphs-linearly-many_images/imageFile52.png>)

![image 53](<2019-hoorn-regular-graphs-linearly-many_images/imageFile53.png>)

2c d + 1

d 2

m d + 1 − O(dn)

+ 1 − c

=

n log

![image 54](<2019-hoorn-regular-graphs-linearly-many_images/imageFile54.png>)

![image 55](<2019-hoorn-regular-graphs-linearly-many_images/imageFile55.png>)

![image 56](<2019-hoorn-regular-graphs-linearly-many_images/imageFile56.png>)

d − 1 d + 1

m d + 1 − O (dn)

d 2

= 1 − c ·

n log

![image 57](<2019-hoorn-regular-graphs-linearly-many_images/imageFile57.png>)

![image 58](<2019-hoorn-regular-graphs-linearly-many_images/imageFile58.png>)

![image 59](<2019-hoorn-regular-graphs-linearly-many_images/imageFile59.png>)

d − 1 d + 1

n d + 1 − O (dn).

d 2

= 1 − c ·

n log

![image 60](<2019-hoorn-regular-graphs-linearly-many_images/imageFile60.png>)

![image 61](<2019-hoorn-regular-graphs-linearly-many_images/imageFile61.png>)

![image 62](<2019-hoorn-regular-graphs-linearly-many_images/imageFile62.png>)

We have used b = nd−+1m = dcn+1 and hence log b = log dm+1 + O(1), and similarly log m = log n + O(1).

![image 63](<2019-hoorn-regular-graphs-linearly-many_images/imageFile63.png>)

![image 64](<2019-hoorn-regular-graphs-linearly-many_images/imageFile64.png>)

![image 65](<2019-hoorn-regular-graphs-linearly-many_images/imageFile65.png>)

![image 66](<2019-hoorn-regular-graphs-linearly-many_images/imageFile66.png>)

![image 67](<2019-hoorn-regular-graphs-linearly-many_images/imageFile67.png>)

![image 68](<2019-hoorn-regular-graphs-linearly-many_images/imageFile68.png>)

![image 69](<2019-hoorn-regular-graphs-linearly-many_images/imageFile69.png>)

We now need to prove a matching upper bound on |Gd,c(n)|. We do this by uncovering the edges of such graphs in a suitably chosen order, and recording whether in each step a new triangle is created. We will deﬁne a function

φ : Gd,c(n) → {0, 1}nd/2 that will record which edges of G create triangles when added in this order.

We use an approach inspired by the conﬁguration model. Let us denote by Gd∗(n) (respectively, Gd,c∗ (n)) the set of d-regular graphs (respectively, d-regular graphs with at least c·Tmax triangles) on n labeled nodes, where additionally the edges leaving each node are assigned labels 1 through d. This means that each edge gets two labels, one from each end.

Given G∗ ∈ Gd,c∗ (n), we deﬁne the a conﬁguration ordering ≺ on the set of edges of G∗ as follows. Let e = (i1j1) and f = (i2j2) be two edges of G∗ with i1 < j1 and i2 < j2. Let us declare e ≺ f if i1 < i2, or if i1 = i2 and the label of e is smaller than the label of f at their common node. Let e1 ≺ e2 ≺ · · · ≺ end/2 denote the edges of G∗ in increasing conﬁguration order. Let G∗[k] denote the subgraph of G∗ consisting of e1, . . . , ek.

Finally deﬁne φ(G∗)(k) = 1 if ek is incident to a triangle in G∗[k] and 0 otherwise. Denoting ek = (ij), it is clear that we have φ(G∗)(k) = 1 if and only if there is a triangle (hij) in G∗ such that h < min(i, j).

For any x ∈ {0, 1}nd/2 let us denote x = nd/j=12 x(j). Then φ(G∗) denotes the total number of edges ek that upon adding to the graph G∗[k − 1] have created at least one new

triangle. Moreover, any vector x ∈ {0, 1}nd/2 describes a proﬁle of which edges revealed a new triangle. The next lemma gives an upper bound on the number of graphs in Gd,c∗ (n) with a given triangle reveal proﬁle.

- Lemma 2.1.

φ−1(x) ≤ (dn)dn/2 ·

d2 n

![image 70](<2019-hoorn-regular-graphs-linearly-many_images/imageFile70.png>)

x

Proof. The idea is to reconstruct a G∗ ∈ φ−1(x) by starting from the empty graph and adding edges 1-by-1, according to the conﬁguration order. Just like in the conﬁguration model, each node starts with d half-edges, labeled 1 through d. First we take the half-edge with label 1 at node 1, and join it to any other half-edge. We can do this in dn − 1 ways. Then, in each subsequent step, we take the smallest node that still has half-edges, pick the one with the smallest label, and match it to any another half-edge. If we didn’t have constraints on triangles, the total number of possible (multi-)graphs we could create this way would be (dn − 1)(dn − 3) · · · 3 · 1, which is an upper bound on |Gd∗(n)|.

In our case, the vector x dictates whether the next edge added has to create a triangle with previously added edges. By the deﬁnition of the conﬁguration order, the number of possible choices for the kth edge is dn−(2k−1), as the starting half-edge is ﬁxed and there are exactly dn−(2k−1) available half-edges at this step. However, when x(k) = 1, the number of choices for the ending half-edge is limited. Suppose the starting half-edge is incident to node j. Then, in order for this edge to create a triangle, the ending half-edge most be incident to one of the current 2nd neighbors of j. There are never more than d2 second neighbors, and thus never more than d3 possible half-edges to choose from.

Thus we get the upper bound |φ−1(x)| ≤

j:x(j)=0

(dn − (2j − 1)) ·

j:x(j)=1

d3

≤ d3 x · (dn)dn/2− x

= (dn)dn/2 ·

d2 n

![image 71](<2019-hoorn-regular-graphs-linearly-many_images/imageFile71.png>)

x

which proves the lemma.

![image 72](<2019-hoorn-regular-graphs-linearly-many_images/imageFile72.png>)

![image 73](<2019-hoorn-regular-graphs-linearly-many_images/imageFile73.png>)

![image 74](<2019-hoorn-regular-graphs-linearly-many_images/imageFile74.png>)

![image 75](<2019-hoorn-regular-graphs-linearly-many_images/imageFile75.png>)

The main idea for the upper bound is now to consider a speciﬁc set of triangle reveal proﬁles x ∈ {0, 1}nd/2, in which at least a cdd−+11 fraction of edges have revealed triangles.

![image 76](<2019-hoorn-regular-graphs-linearly-many_images/imageFile76.png>)

- Proof of Theorem 1.1 (Upper bound). Let us introduce the following short hand notation,


Tc = c ·

dn 2

![image 77](<2019-hoorn-regular-graphs-linearly-many_images/imageFile77.png>)

d − 1 d + 1

![image 78](<2019-hoorn-regular-graphs-linearly-many_images/imageFile78.png>)

, (5)

- as it will come up frequently. Deﬁne L = x ∈ {0, 1}nd2 : x ≥ Tc − 1 .


![image 79](<2019-hoorn-regular-graphs-linearly-many_images/imageFile79.png>)

Then, by Lemma 2.1, and using d2 ≤ n, we see that

φ−1(L) ≤ |L|(dn)dn/2

d2 n

![image 80](<2019-hoorn-regular-graphs-linearly-many_images/imageFile80.png>)

Tc−1

≤ 2dn/2(dn)dn/2

d2 n

![image 81](<2019-hoorn-regular-graphs-linearly-many_images/imageFile81.png>)

Tc−1

(6)

To ﬁnish the proof, we will show that Gd,c∗ (n) ≤ dn2 |φ−1(L)|. For this, consider the symmetric group Sn, which acts on Gd,c∗ (n) by permuting the node labels. For σ ∈ Sn and G∗ ∈ Gd,c∗ (n), let us denote by G∗σ the graph obtained by applying σ to the node labels. Furthermore let SnG∗ = {G∗σ : σ ∈ Sn} ⊂ Gd,c∗ (n) denote the orbit of G∗ under the action of Sn. We ﬁnish the proof modulo the following result, which we establish at the end of this section.

![image 82](<2019-hoorn-regular-graphs-linearly-many_images/imageFile82.png>)

- Lemma 2.2. For any G∗ ∈ Gd,c∗ (n) we have


2

SnG∗ ∩ φ−1(L) ≥

dn|SnG∗| In other words, randomly relabeling the nodes of G∗ yields, with not too small probability, a graph whose φ(G∗σ) ≥ Tc − 1.

![image 83](<2019-hoorn-regular-graphs-linearly-many_images/imageFile83.png>)

Summing this inequality over all orbits of the Sn actions yields Gd,c∗ (n) ≤ dn2 |φ−1(L)| as claimed above. Note that |Gd,c∗ (n)| = |Gd,c(n)| · (d!)n. Combining this with (6) we get

![image 84](<2019-hoorn-regular-graphs-linearly-many_images/imageFile84.png>)

Tc−1

|Gd,c(n)| = |Gd,c∗ (n)| (d!)n ≤

|φ−1(L)| (d!)n ≤

(dn)dn/2 (d/e)dn

d2 n

dn 2

dn 2

2dn/2

![image 85](<2019-hoorn-regular-graphs-linearly-many_images/imageFile85.png>)

![image 86](<2019-hoorn-regular-graphs-linearly-many_images/imageFile86.png>)

![image 87](<2019-hoorn-regular-graphs-linearly-many_images/imageFile87.png>)

![image 88](<2019-hoorn-regular-graphs-linearly-many_images/imageFile88.png>)

![image 89](<2019-hoorn-regular-graphs-linearly-many_images/imageFile89.png>)

![image 90](<2019-hoorn-regular-graphs-linearly-many_images/imageFile90.png>)

√

dn

dn 2

n d

2 −Tc+1

![image 91](<2019-hoorn-regular-graphs-linearly-many_images/imageFile91.png>)

2e)dn

dTc−1

![image 92](<2019-hoorn-regular-graphs-linearly-many_images/imageFile92.png>)

=

(

![image 93](<2019-hoorn-regular-graphs-linearly-many_images/imageFile93.png>)

![image 94](<2019-hoorn-regular-graphs-linearly-many_images/imageFile94.png>)

√

n2 2d

dn

n d

2 −Tc

![image 95](<2019-hoorn-regular-graphs-linearly-many_images/imageFile95.png>)

2e)dn

dTc

![image 96](<2019-hoorn-regular-graphs-linearly-many_images/imageFile96.png>)

= (

![image 97](<2019-hoorn-regular-graphs-linearly-many_images/imageFile97.png>)

![image 98](<2019-hoorn-regular-graphs-linearly-many_images/imageFile98.png>)

Thus

d − 1 d + 1

log|Gc,d(n)| ≤ 1 − c ·

![image 99](<2019-hoorn-regular-graphs-linearly-many_images/imageFile99.png>)

d − 1 d + 1

= 1 − c ·

![image 100](<2019-hoorn-regular-graphs-linearly-many_images/imageFile100.png>)

dn 2

n d

dn 2

+ c ·

log

log d + O(dn)

![image 101](<2019-hoorn-regular-graphs-linearly-many_images/imageFile101.png>)

![image 102](<2019-hoorn-regular-graphs-linearly-many_images/imageFile102.png>)

![image 103](<2019-hoorn-regular-graphs-linearly-many_images/imageFile103.png>)

n d + 1

dn 2

dn 2

+ c ·

log

log d + O(dn)

![image 104](<2019-hoorn-regular-graphs-linearly-many_images/imageFile104.png>)

![image 105](<2019-hoorn-regular-graphs-linearly-many_images/imageFile105.png>)

![image 106](<2019-hoorn-regular-graphs-linearly-many_images/imageFile106.png>)

![image 107](<2019-hoorn-regular-graphs-linearly-many_images/imageFile107.png>)

![image 108](<2019-hoorn-regular-graphs-linearly-many_images/imageFile108.png>)

![image 109](<2019-hoorn-regular-graphs-linearly-many_images/imageFile109.png>)

![image 110](<2019-hoorn-regular-graphs-linearly-many_images/imageFile110.png>)

We are thus left to prove Lemma 2.2. For this we ﬁrst show that for a uniform random

permutation σ, the expected value of φ(G∗σ) is at least c · dn2((dd+1)−1). Then the lemma will follow from a standard Markov-inequality argument.

![image 111](<2019-hoorn-regular-graphs-linearly-many_images/imageFile111.png>)

- Lemma 2.3. Let σ be a uniformly random permutation. Then E[ φ(G∗σ) ] ≥ Tc.


Proof. Let Xe(σ) be the indicator variable that the edge e of G∗ creates a triangle when it is added in the lexicographic order of G∗σ. Then φ(G∗σ) = e Xe(σ) and so

E [ φ(G∗σ) ] =

e

E[Xe(σ)] =

e

P (Xe(σ) = 1)

Let e = (ij) and let e be incident to exactly te triangles in G∗. Let v1, v2, . . . , vte denote the third nodes of these triangles. Then Xe(σ) is 1 if at least one of these triangles is formed

- at the moment when e is added, which is equivalent to at least one of these nodes preceding both i and j in the σ-order. That is, min(σ(v1), σ(v2), . . . , σ(vte)) < min(σ(i),σ(j)). Then Xe(σ) = 0 if and only if either i or j has the smallest σ value among i, j, v1, v2, . . . , vte. Since the σ-order of these nodes is a uniformly random permutation on te + 2 elements, we get P(Xe(σ) = 0) = 2/(te + 2) and hence P (Xe(σ) = 1) = 1 − 2/(te + 2).


Thus, since te ≤ d − 1, we get

te te + 2 ≥

te d + 1 ≥ Tc, (7)

2 te + 2

E [ φ(G∗σ) ] =

1 −

=

P(Xe(σ) = 1) =

![image 112](<2019-hoorn-regular-graphs-linearly-many_images/imageFile112.png>)

![image 113](<2019-hoorn-regular-graphs-linearly-many_images/imageFile113.png>)

![image 114](<2019-hoorn-regular-graphs-linearly-many_images/imageFile114.png>)

e

e

e

e

where the last inequality follows from e te being 3 times the total number of triangles in

- G∗, which is in turn at least c · n3 d2 . This ﬁnishes the proof of the lemma. Proof of Lemma 2.2. By simple algebraic considerations


![image 115](<2019-hoorn-regular-graphs-linearly-many_images/imageFile115.png>)

![image 116](<2019-hoorn-regular-graphs-linearly-many_images/imageFile116.png>)

![image 117](<2019-hoorn-regular-graphs-linearly-many_images/imageFile117.png>)

![image 118](<2019-hoorn-regular-graphs-linearly-many_images/imageFile118.png>)

![image 119](<2019-hoorn-regular-graphs-linearly-many_images/imageFile119.png>)

SnG∗ ∩ φ−1(L) |SnG∗|

= |{σ ∈ Sn : φ(G∗σ) ∈ L}| |Sn|

. (8)

![image 120](<2019-hoorn-regular-graphs-linearly-many_images/imageFile120.png>)

![image 121](<2019-hoorn-regular-graphs-linearly-many_images/imageFile121.png>)

This is obvious when G∗ has no automorphisms (that is, when SnG∗ is in bijection with Sn), but it also holds in the general case since the stabilizers of diﬀerent elements of the orbit SnG∗ are conjugate and hence have the same cardinality.

Consider a uniformly random permutation σ ∈ Sn. By (8) it is enough to show that with probability at least dn2 we have φ(G∗σ) ∈ L, which is equivalent to φ(G∗σ) ≥ Tc − 1.

![image 122](<2019-hoorn-regular-graphs-linearly-many_images/imageFile122.png>)

Observe that φ(G∗σ) cannot be bigger than dn2 . Hence, using Lemma 2.3 Tc ≤ E [|φ(G∗σ)|] ≤ (Tc − 1) P (|φ(G∗σ)| < Tc − 1) +

![image 123](<2019-hoorn-regular-graphs-linearly-many_images/imageFile123.png>)

dn 2

P(|φ(G∗σ)| ≥ Tc − 1) ≤ Tc − 1 +

![image 124](<2019-hoorn-regular-graphs-linearly-many_images/imageFile124.png>)

(9)

dn 2

P(|φ(G∗σ)| ≥ Tc − 1) ,

![image 125](<2019-hoorn-regular-graphs-linearly-many_images/imageFile125.png>)

from which we conclude that

2 dn

P( φ(G∗σ) ≥ Tc − 1) ≥

.

![image 126](<2019-hoorn-regular-graphs-linearly-many_images/imageFile126.png>)

![image 127](<2019-hoorn-regular-graphs-linearly-many_images/imageFile127.png>)

![image 128](<2019-hoorn-regular-graphs-linearly-many_images/imageFile128.png>)

![image 129](<2019-hoorn-regular-graphs-linearly-many_images/imageFile129.png>)

![image 130](<2019-hoorn-regular-graphs-linearly-many_images/imageFile130.png>)

- 2.2 The structure of regular graphs with a given number of triangles


A simple extension of the methods of the proof of Theorem 1.1 yields a strong structural description of a typical graph with at least c · Tmax triangles:

For d ﬁxed: 1 − o(1) fraction of all triangles are contained in d + 1-cliques. For 1 ≪ d ≪ n: 1 − o(1) fraction of all triangles are contained in pseudo-cliques. Moreover,

these pseudo-cliques are non-overlapping.

We will treat the two cases separately, but the following lemma will be useful for both. As before, we let te denote the number of triangles the edge e is incident to. We say the edge

- e is δ-bad if 1 ≤ te ≤ d − 1 − δd.


- Lemma 2.4. Let ε, δ > 0 ﬁxed. Let Gd,cε,δ ⊂ Gd,c denote the subset of graphs where at least ε(d/2)n edges are δ-bad. Then


d − 1 d + 1 −

εδd 3d + 3

n d

εδd 3d + 3

dn 2

dn 2

log|Gd,cε,δ(n)| ≤ 1 − c

log d + O(dn). Proof. If e is bad, then 1 ≤ te ≤ d − 1 − δd, so

log

+ c +

![image 131](<2019-hoorn-regular-graphs-linearly-many_images/imageFile131.png>)

![image 132](<2019-hoorn-regular-graphs-linearly-many_images/imageFile132.png>)

![image 133](<2019-hoorn-regular-graphs-linearly-many_images/imageFile133.png>)

![image 134](<2019-hoorn-regular-graphs-linearly-many_images/imageFile134.png>)

![image 135](<2019-hoorn-regular-graphs-linearly-many_images/imageFile135.png>)

![image 136](<2019-hoorn-regular-graphs-linearly-many_images/imageFile136.png>)

d − 1 − te d + 1 ≥

te d + 1

te d + 1

te d + 1

te te + 2 ·

te d + 1

1 3 ·

δd d + 1

te te + 2 −

te te + 2

=

+

=

+

+

.

![image 137](<2019-hoorn-regular-graphs-linearly-many_images/imageFile137.png>)

![image 138](<2019-hoorn-regular-graphs-linearly-many_images/imageFile138.png>)

![image 139](<2019-hoorn-regular-graphs-linearly-many_images/imageFile139.png>)

![image 140](<2019-hoorn-regular-graphs-linearly-many_images/imageFile140.png>)

![image 141](<2019-hoorn-regular-graphs-linearly-many_images/imageFile141.png>)

![image 142](<2019-hoorn-regular-graphs-linearly-many_images/imageFile142.png>)

![image 143](<2019-hoorn-regular-graphs-linearly-many_images/imageFile143.png>)

![image 144](<2019-hoorn-regular-graphs-linearly-many_images/imageFile144.png>)

![image 145](<2019-hoorn-regular-graphs-linearly-many_images/imageFile145.png>)

![image 146](<2019-hoorn-regular-graphs-linearly-many_images/imageFile146.png>)

Suppose more than ε(d/2)n edges of G∗ ∈ Gd,c∗ (n) are bad. Combining the above with (7) we get that for a uniformly random permutation σ ∈ Sn

εδd2n 6d + 6 ≥ Tc +

εδd2n 6d + 6

te te + 2 ≥

te d + 1

E[|φ(G∗σ)|] =

+

.

![image 147](<2019-hoorn-regular-graphs-linearly-many_images/imageFile147.png>)

![image 148](<2019-hoorn-regular-graphs-linearly-many_images/imageFile148.png>)

![image 149](<2019-hoorn-regular-graphs-linearly-many_images/imageFile149.png>)

![image 150](<2019-hoorn-regular-graphs-linearly-many_images/imageFile150.png>)

e

e

Hence, by the same computation as in (9) we get

εδd2n 6d + 6 − 1 ≥

2 dn

P |φ(G∗σ)| ≥ Tc +

. Now let

![image 151](<2019-hoorn-regular-graphs-linearly-many_images/imageFile151.png>)

![image 152](<2019-hoorn-regular-graphs-linearly-many_images/imageFile152.png>)

εδd2n 6d + 6 − 1 .

Lε,δ = x ∈ {0, 1}nd2 : |x| ≥ Tc +

![image 153](<2019-hoorn-regular-graphs-linearly-many_images/imageFile153.png>)

![image 154](<2019-hoorn-regular-graphs-linearly-many_images/imageFile154.png>)

By the previous considerations, for any G∗ ∈ G∗ε,δd,c(n) we get that

SnG∗ ∩ φ−1(Lε,δ) |SnG∗|

= |{σ ∈ Sn : φ(G∗σ) ∈ Lε,δ}| |Sn|

2 dn

≥

![image 155](<2019-hoorn-regular-graphs-linearly-many_images/imageFile155.png>)

![image 156](<2019-hoorn-regular-graphs-linearly-many_images/imageFile156.png>)

![image 157](<2019-hoorn-regular-graphs-linearly-many_images/imageFile157.png>)

Summing the inequality SnG∗ ∩ φ−1(Lε,δ) ≥ dn2 |Sn| over the orbits of the Sn action in G∗ε,δd,c(n) we obtain the estimate

![image 158](<2019-hoorn-regular-graphs-linearly-many_images/imageFile158.png>)

dn

|G∗ε,δd,c(n)| ≤

2 |φ−1(Lε,δ)|, which, combined with Lemma 2.1, yields

![image 159](<2019-hoorn-regular-graphs-linearly-many_images/imageFile159.png>)

|Gd,cε,δ(n)| = |G∗ε,δc,d(n)|

|φ−1(Lε,δ)| (d!)n

dn 2

(d!)n ≤

![image 160](<2019-hoorn-regular-graphs-linearly-many_images/imageFile160.png>)

![image 161](<2019-hoorn-regular-graphs-linearly-many_images/imageFile161.png>)

![image 162](<2019-hoorn-regular-graphs-linearly-many_images/imageFile162.png>)

2n 6d+6 −1

Tc+ εδd

d2 n

(dn)dn/2 (d/e)dn

![image 163](<2019-hoorn-regular-graphs-linearly-many_images/imageFile163.png>)

dn 2

2dn/2

≤

![image 164](<2019-hoorn-regular-graphs-linearly-many_images/imageFile164.png>)

![image 165](<2019-hoorn-regular-graphs-linearly-many_images/imageFile165.png>)

![image 166](<2019-hoorn-regular-graphs-linearly-many_images/imageFile166.png>)

√

dn

n d

dn 2

2 −Tc+1

![image 167](<2019-hoorn-regular-graphs-linearly-many_images/imageFile167.png>)

2e)dn

dTc−1

![image 168](<2019-hoorn-regular-graphs-linearly-many_images/imageFile168.png>)

(

=

![image 169](<2019-hoorn-regular-graphs-linearly-many_images/imageFile169.png>)

![image 170](<2019-hoorn-regular-graphs-linearly-many_images/imageFile170.png>)

2 −Tc− εδd6d+62n

√

n2 2d

dn

n d

2n

dTc+εδd

![image 171](<2019-hoorn-regular-graphs-linearly-many_images/imageFile171.png>)

![image 172](<2019-hoorn-regular-graphs-linearly-many_images/imageFile172.png>)

2e)dn

![image 173](<2019-hoorn-regular-graphs-linearly-many_images/imageFile173.png>)

6d+6 ·

= (

. Taking log of both sides ﬁnishes the proof.

![image 174](<2019-hoorn-regular-graphs-linearly-many_images/imageFile174.png>)

![image 175](<2019-hoorn-regular-graphs-linearly-many_images/imageFile175.png>)

![image 176](<2019-hoorn-regular-graphs-linearly-many_images/imageFile176.png>)

![image 177](<2019-hoorn-regular-graphs-linearly-many_images/imageFile177.png>)

![image 178](<2019-hoorn-regular-graphs-linearly-many_images/imageFile178.png>)

![image 179](<2019-hoorn-regular-graphs-linearly-many_images/imageFile179.png>)

![image 180](<2019-hoorn-regular-graphs-linearly-many_images/imageFile180.png>)

- 2.2.1 Fixed d

Let us say that a node in G is bad if it’s not in a d + 1-clique, but it is in a triangle. The following statement is a (very) slight strengthening of Theorem 1.2.

Theorem 2.5. Let ε > 0 and d ﬁxed. Among all d-regular graphs with at least c · Tmax triangles, the proportion of those where more than εn nodes are bad goes to 0 as n → ∞. This remains true even if ε → 0, as long as ε log n → ∞.

We will make use of the following simple observation, whose proof we omit.

Lemma 2.6. Let G be a d-regular graph. If all edges incident to a node v are incident to exactly d − 1 triangles, then v is part of a d + 1-clique.

Proof of Theorem 2.5. Let us set δ = 1/d and call 1/d-bad edges simply “bad”. Suppose now that more than εn nodes of G are bad. Each bad node, by deﬁnition, is adjacent to at least two bad edges, so there are at least εn bad edges. Thus G ∈ G

2ε

![image 181](<2019-hoorn-regular-graphs-linearly-many_images/imageFile181.png>)

d , d1

![image 182](<2019-hoorn-regular-graphs-linearly-many_images/imageFile182.png>)

d,c (n). Then, Lemma 2.4 combined with Theorem 1.1 and the fact that d = O(1) gives

log |G

2ε

![image 183](<2019-hoorn-regular-graphs-linearly-many_images/imageFile183.png>)

d , d1

![image 184](<2019-hoorn-regular-graphs-linearly-many_images/imageFile184.png>)

d,c (n)| |Gd,c(n)|

![image 185](<2019-hoorn-regular-graphs-linearly-many_images/imageFile185.png>)

= −

2ε d

![image 186](<2019-hoorn-regular-graphs-linearly-many_images/imageFile186.png>)

1 dd

![image 187](<2019-hoorn-regular-graphs-linearly-many_images/imageFile187.png>)

![image 188](<2019-hoorn-regular-graphs-linearly-many_images/imageFile188.png>)

3d + 3

dn 2

![image 189](<2019-hoorn-regular-graphs-linearly-many_images/imageFile189.png>)

log n + O(dn log d) = −

ε 3d + 3

![image 190](<2019-hoorn-regular-graphs-linearly-many_images/imageFile190.png>)

n log n + O(n),

so indeed

lim

n→∞

|G

2ε

![image 191](<2019-hoorn-regular-graphs-linearly-many_images/imageFile191.png>)

d , d1

![image 192](<2019-hoorn-regular-graphs-linearly-many_images/imageFile192.png>)

d,c (n)| |Gd,c(n)|

![image 193](<2019-hoorn-regular-graphs-linearly-many_images/imageFile193.png>)

= 0,

- as long as ε log n → ∞, proving that with high probability a graph conditioned on having at least c · Tmax triangles has o(n) bad nodes, hence consists almost completely of d + 1-cliques and a triangle-free part.


![image 194](<2019-hoorn-regular-graphs-linearly-many_images/imageFile194.png>)

![image 195](<2019-hoorn-regular-graphs-linearly-many_images/imageFile195.png>)

![image 196](<2019-hoorn-regular-graphs-linearly-many_images/imageFile196.png>)

![image 197](<2019-hoorn-regular-graphs-linearly-many_images/imageFile197.png>)

- 2.2.2 Growing d


An immediate generalization of Theorem 2.5 cannot hold for the d ≫ 1 case, because one can exhibit a family of d-regular graphs with c · Tmax triangles that contain no cliques at all, yet have the optimal, (1 − c)(d/2)n log d+1n , logarithmic growth rate. Such a family can be built, for example, by taking the disjoint union of many copies of H, together with a random d-regular graph, where H is Kd+2 minus a perfect matching. Realizing the required c · Tmax triangles takes up only slightly more space this way than using copies of Kd+1, and the resulting decrease in the size of the random part is small enough that it doesn’t aﬀect the logarithmic growth rate. One can push this even further, and use disjoint d + o(d) size components (these still contain roughly d3 triangles each), and a large random d-regular part of the appropriate size.

![image 198](<2019-hoorn-regular-graphs-linearly-many_images/imageFile198.png>)

We will show in this section, that a typical graph in the ensemble does, in fact, resemble an element of this last family. The main reason the previous argument fails for d ≫ 1 is because now we cannot choose δ to be too small in Lemma 2.4, otherwise the gain will be less in magnitude than the error term O(dn log d). Nevertheless, if log d/log n is small, then the gap between the main term and the error term allows us to choose both ε and δ to be small, which will be enough to learn something about the typical graphs in the ensemble. In particular, we can choose

1/2

log d log dn2

ε = δ2 = (3c)2/3 ·

. (10)

![image 199](<2019-hoorn-regular-graphs-linearly-many_images/imageFile199.png>)

![image 200](<2019-hoorn-regular-graphs-linearly-many_images/imageFile200.png>)

Then Lemma 2.4 implies that in a typical d-regular graph with at least c · Tmax triangles, most edges are incident to 0 or almost d triangles. As it turns out, this implies a structural description similar to that of Theorem 2.5. Let us ﬁrst informally explain the result. We call a subgraph H ⊂ G a dense spot if |H| ≤ d + 1 and degH(x) = d(1 − O(δ)) for all x ∈ H. Dense spots satisfy the following simple, combinatorial observations:

- • Two dense spots are either disjoint, or they intersect in d(1 − O(δ)) nodes.
- • Intersection is transitive: if H1 ∩ H2 = ∅ and H2 ∩ H3 = ∅ then H1 ∩ H3 = ∅.
- • The union of a maximal, pairwise intersecting, family of dense spots has size d(1+O(δ)). We call these pseudo-cliques.


- • It follows that any two pseudo-cliques must be disjoint. The following is a restatement of Theorem 1.3.


Theorem 2.7. Let 1 ≪ d ≪ n. Let δ as in (10), and assume δ < 1/16. With high probability, a random d-regular graph with at least c·Tmax triangles contains (1+O(δ))cn/d pseudo-cliques. These pseudo-cliques contain 1 − O((ε + δ)/c) fraction of all triangles.

Remark 2.8. Theorem 2.7 is the strongest when log d = o(log n), as in this case both ε and δ are o(1). However, when d = nβ then δ = (3c)1/3 1− β2β

1/4

, so we still get a non-trivial

![image 201](<2019-hoorn-regular-graphs-linearly-many_images/imageFile201.png>)

structural result when β is small enough. Proof. We set ε and δ according to (10). Then, a careful calculation using Lemma 2.4 shows that we have

|Gd,cε,δ(n)| |Gd,c(n)|

lim

= 0,

![image 202](<2019-hoorn-regular-graphs-linearly-many_images/imageFile202.png>)

n→∞

so it is enough to consider a graph G ∈ Gd,c(n)\Gε,δd,c(n). The graph G then has, by deﬁnition, less than ε(d/2)n edges that are δ-bad. Let us call a δ-bad edge bad for brevity, and other

edges good. Let us start by removing all edges with te = 0 from G, and denote the remaining graph by G′. Removing such edges doesn’t change the te value of the remaining edges. Let us call a node v ∈ G′ bad, if it is incident to at least δd bad edges. Then, since ε = δ2, it follows that G′ cannot have more than δn bad nodes.

The total number of triangles that are incident to either a bad edge or a bad node is at

most ε(d/2)n · d + δn d2 = O(ε + δ) · Tmax. We will show that the rest of the triangles are concentrated in pseudo-cliques.

Deﬁnition 2.9. A subgraph H ⊂ G is a dense spot if |H| ≤ d + 1 and each node x ∈ H has degH(x) ≥ (1 − 4δ)d.

- Claim 2.10. Let H1, H2 be dense spots. Then they are either disjoint, or |H1∩H2| ≥ (1−8δ)d. This follows from the fact the nodes in the intersection must have degree ≤ d.
- Claim 2.11. Let H1, H2, H3 be dense spots. If H1∩H2 = ∅ and H2∩H3 = ∅ then H1∩H3 = ∅, since otherwise we would have d + 1 ≥ |H2| ≥ |H2 ∩ H1| + |H2 ∩ H3| ≥ 2d(1 − 8δ) which contradicts δ < 1/16.


Deﬁnition 2.12. A subgraph K ⊂ G is a pseudo-clique if there is a maximal family H of pairwise intersecting dense spots such that K = ∪H∈HH.

Claim 2.13. By deﬁnition, any dense spot H is either disjoint from, or fully contained in, a pseudo clique K. Furthermore, any two distinct pseudo-cliques are disjoint.

Lemma 2.14. If K is a pseudo-clique then |K| ≤ 11−−138δδ (d + 1) = (1 + O(δ))d.

![image 203](<2019-hoorn-regular-graphs-linearly-many_images/imageFile203.png>)

Proof of Lemma 2.14. Let H ⊂ K be one of the dense spots in K. For any node x ∈ H we have degH(x) ≥ (1 − 4δ)d. But deg(x) = d, thus the total number of edges going between H and K \ H is at most |H| · 4δd ≤ 4δd(d + 1). However, each node y ∈ K \ H is contained in a dense spot H′, and thus degH′(y) ≥ (1 − 4δ)d. Since |H′ \ H| ≤ 8δd + 1 ≤ 9δd, we get that

- at least (1 − 13δ)d edges go from y to H. Hence |K \ H|(1 − 13δ)d ≤ 4δd(d + 1),


from which

1 − 8δ 1 − 13δ

4δ(d + 1) 1 − 13δ ≤

|K| ≤ |H| +

(d + 1) as claimed.

![image 204](<2019-hoorn-regular-graphs-linearly-many_images/imageFile204.png>)

![image 205](<2019-hoorn-regular-graphs-linearly-many_images/imageFile205.png>)

![image 206](<2019-hoorn-regular-graphs-linearly-many_images/imageFile206.png>)

![image 207](<2019-hoorn-regular-graphs-linearly-many_images/imageFile207.png>)

![image 208](<2019-hoorn-regular-graphs-linearly-many_images/imageFile208.png>)

![image 209](<2019-hoorn-regular-graphs-linearly-many_images/imageFile209.png>)

To ﬁnish the proof of Theorem 2.7, we need to show that any triangle that’s only incident to good edges and good nodes is contained in a pseudo-clique. We will show slightly more: that a good edge connecting good nodes is in a pseudo-clique.

Consider a good edge uv in G′, where both u and v are good nodes. Since we already removed the edges with no triangles, tuv ≥ d − δd. In particular u and v share at least d − δd common neighbors. Each of u and v may be incident to at most δd bad edges. That means that the subset H0 of common neighbors of u and v that are connected to both of them via

good edges has size |H0| ≥ d−3δd. Let H = H0∪{u, v}. We claim H is a dense spot. Clearly |H| ≤ 1 + deg(u) = d + 1, and by construction, degH(u), degH(v) ≥ (1 − 3δ)d ≥ (1 − 4δ)d. What remains to show is that for any node x ∈ H0 we have degH(x) ≥ (1−4δ)d. But xu is a good edge, hence x and u have at least (1 − δ)d common neighbors, or equivalently, at most δd of u’s neighbors are not connected to x. Thus x is connected to at least (1− 4δ)d nodes in

- H, proving that indeed H is a dense spot. So the uv edge is contained in a dense spot, and thus in a pseudo-clique.


![image 210](<2019-hoorn-regular-graphs-linearly-many_images/imageFile210.png>)

![image 211](<2019-hoorn-regular-graphs-linearly-many_images/imageFile211.png>)

![image 212](<2019-hoorn-regular-graphs-linearly-many_images/imageFile212.png>)

![image 213](<2019-hoorn-regular-graphs-linearly-many_images/imageFile213.png>)

- 2.3 k-cliques


We can easily extend the above results from triangles to k-cliques. Let Gd,c,k(n) denote the set of d-regular graphs on n nodes that contain at least c · k− d1 nk subgraphs isomorphic to Kk. (The maximum possible number of subgraphs isomorphic to Kk is clearly k− d1 nk .)

![image 214](<2019-hoorn-regular-graphs-linearly-many_images/imageFile214.png>)

![image 215](<2019-hoorn-regular-graphs-linearly-many_images/imageFile215.png>)

Proof of Theorem 1.4. The idea is a simple reduction the the k = 3 case. Clearly, each G ∈ Gd,c,k(n) has at least

k 3 d−2 k−3

n k

n 3

c · k− d1

= c · d2

= c · Tmax

![image 216](<2019-hoorn-regular-graphs-linearly-many_images/imageFile216.png>)

![image 217](<2019-hoorn-regular-graphs-linearly-many_images/imageFile217.png>)

![image 218](<2019-hoorn-regular-graphs-linearly-many_images/imageFile218.png>)

triangles, so Gd,tk,k(n) ⊂ Gd,c(n), which implies the upper bound of the theorem. On the other hand, the family of graphs constructed in Theorem 1.1 contain

b

d + 1 k

n d + 1

= c ·

![image 219](<2019-hoorn-regular-graphs-linearly-many_images/imageFile219.png>)

d + 1 k

= c ·

d k − 1

n k

![image 220](<2019-hoorn-regular-graphs-linearly-many_images/imageFile220.png>)

k-cliques, so this family is contained in Gd,c,k(n), implying the lower bound of the theorem. Finally, the structural statement follows directly from Theorem 2.5.

![image 221](<2019-hoorn-regular-graphs-linearly-many_images/imageFile221.png>)

![image 222](<2019-hoorn-regular-graphs-linearly-many_images/imageFile222.png>)

![image 223](<2019-hoorn-regular-graphs-linearly-many_images/imageFile223.png>)

![image 224](<2019-hoorn-regular-graphs-linearly-many_images/imageFile224.png>)

Acknowledgements The authors thank Dmitri Krioukov for useful discussions on the related topic of sparse maximum entropy graphs with given number of triangles, which lead us to the upper tail problem. Pim van der Hoorn and Gabor Lippner were supported by ARO grant W911NF1610391, Gabor Lippner was also supported by NSF grant DMS 1800738, and Elchanan Mossel was supported by NSF grant DMS-1737944 and ONR grant N00014-17-12598.

# References

- [1] L. Anita and N. Wormald. Asymptotic enumeration of graphs by degree sequence, and the degree sequence of a random graph. arXiv, 2017.
- [2] Fanny Augeri. Nonlinear large deviation bounds with applications to traces of wigner matrices and cycles counts in erdo¨s-renyi graphs. arXiv preprint arXiv:1810.01558, 2018.
- [3] Sourav Chatterjee. The missing log in large deviations for triangle counts. Random Structures & Algorithms, 40(4):437–451, 2012.
- [4] Sourav Chatterjee and Amir Dembo. Nonlinear large deviations. Advances in Mathematics, 299:396–450, 2016.
- [5] Sourav Chatterjee and S.R.S. Varadhan. The large deviation principle for the erdo˝s-re´nyi random graph. European Journal of Combinatorics, 32(7):1000 – 1017, 2011. Homomorphisms and Limits.
- [6] P. Collet and J. P. Eckmann. The number of large graphs with a positive density of triangles. Journal of Statistical Physics, 109(5):923–943, 2002.
- [7] Nicholas A Cook and Amir Dembo. Large deviations of subgraph counts for sparse erdo˝s–re´nyi graphs. arXiv preprint arXiv:1809.11148, 2018.
- [8] B. DeMarco and J. Kahn. Upper tails for triangles. Random Structures & Algorithms, 40(4):452–459, aug 2011.


- [9] Matan Harel, Frank Mousset, and Wojciech Samotij. Upper tails via high moments and entropic stability. arXiv preprint arXiv:1904.08212, 2019.
- [10] Svante Janson, Krzysztof Oleszkiewicz, and Andrzej Rucin´ski. Upper tails for subgraph counts in random graphs. Israel Journal of Mathematics, 142(1):61–92, 2004.
- [11] Svante Janson and Andrzej Rucin´ski. The infamous upper tail. Random Structures & Algorithms, 20(3):317–342, 2002.
- [12] Svante Janson and Andrzej Rucin´ski. The deletion method for upper tail estimates. Combinatorica, 24(4):615–640, 2004.
- [13] Richard Kenyon, Charles Radin, Kui Ren, and Lorenzo Sadun. Bipodal structure in oversaturated random graphs. International Mathematics Research Notices, page rnw261, 2016.
- [14] Richard Kenyon, Charles Radin, Kui Ren, and Lorenzo Sadun. The phases of large networks with edge and triangle constraints. Journal of Physics A: Mathematical and Theoretical, 50(43):435001, 2017.
- [15] Jeong Han Kim, Benny Sudakov, and Van Vu. Small subgraphs of random regular graphs. Discrete Mathematics, 307(15):1961–1967, 2007.
- [16] Jeong Han Kim and Van H Vu. Divide and conquer martingales and the number of triangles in a random graph. Random Structures & Algorithms, 24(2):166–174, 2004.
- [17] Dmitri Krioukov. Clustering implies geometry in networks. Physical review letters, 116(20):208302, 2016.
- [18] Eyal Lubetzky and Yufei Zhao. On replica symmetry of large deviations in random graphs. Random Structures & Algorithms, 47(1):109–146, 2015.
- [19] Eyal Lubetzky and Yufei Zhao. On the variational problem for upper tails in sparse random graphs. Random Structures & Algorithms, 50(3):420–436, 2017.
- [20] Charles Radin, Kui Ren, and Lorenzo Sadun. The asymptotics of large constrained graphs. Journal of Physics A: Mathematical and Theoretical, 47(17):175001, 2014.
- [21] Charles Radin and Lorenzo Sadun. Phase transitions in a complex network. Journal of Physics A: Mathematical and Theoretical, 46(30):305002, 2013.
- [22] Pim van der Hoorn, Gabor Lippner, and Dmitri Krioukov. Sparse maximum-entropy random graphs with a given power-law degree distribution. Journal of Statistical Physics, 173(3):806–844, Nov 2018.
- [23] Van H Vu. A large deviation result on the number of small subgraphs of a random graph. Combinatorics, Probability and Computing, 10(1):79–94, 2001.


