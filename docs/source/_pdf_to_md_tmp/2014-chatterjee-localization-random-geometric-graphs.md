# arXiv:1401.7577v7[math.PR]2Jul2019

## LOCALIZATION IN RANDOM GEOMETRIC GRAPHS WITH TOO MANY EDGES

SOURAV CHATTERJEE AND MATAN HAREL

Abstract. We consider a random geometric graph G(χn,rn), given by connecting two vertices of a Poisson point process χn of intensity n on the d-dimensional unit torus whenever their distance is smaller than the parameter rn. The model is conditioned on the rare event that the number of edges observed, E , is greater than (1+δ)E( E ), for some ﬁxed δ > 0. This article proves that upon conditioning, with high probability there exists a ball of diameter rn which contains a clique of at least 2δE( E )(1 − ε) vertices, for any given ε > 0. Intuitively, this region contains all the “excess” edges the graph is forced to contain by the conditioning event, up to lower order corrections. As a consequence of this result, we prove a large deviations principle for the upper tail of the edge count of the random geometric graph. The rate function of this large deviation principle turns out to be non-convex.

1. Introduction

The random geometric graph is a simple stochastic model, ﬁrst studied in [20] in 1972, for generating a graph: given the parameters n and r, consider a Poisson point process of intensity n on the d-dimensional unit torus, equipped with a translation-invariant metric inherited from a norm  ⋅  on Euclidean space (which may not be the Euclidean norm), and declare an edge between any two vertices that are at distance ≤ r from each other.

Unlike the well-known Erdős–Rényi random graph, the random geometric graph’s deﬁnition leads to strong dependence between edges: if three vertices form a “V” shaped graph, they are far more likely to have the third edge of the triangle than if no assumption were made on the other edges, as a consequence of the triangle inequality.

Many properties of this graph model have been studied. The classic monograph of Mathew Penrose [33] studies results pertaining to many graphtheoretical functions of random geometric graphs, including (but not limited to) laws of large numbers and central limit theorems for subgraph counts, independence number, and chromatic number, as well as many properties connected to the giant component. Many of the results presented in this

2010 Mathematics Subject Classiﬁcation. 60F10, 05C80, 60D05. Key words and phrases. Random geometric graph, Poisson point process, large devia-

tion, localization. Research partially supported by ERC AG “COMPASP” and NSF grant DMS-1005312.

1

monograph have been improved and generalized by Penrose and others in the years since its initial publication. Besides this, there have been investigations into other probabilistic features, such as threshold functions for cover times and mixing times [4] and thresholds for monotone graph functions [18]. This list is far from comprehensive, of course, and the random geometric graph remains an active object of research.

The random geometric graph is also closely related to the random connection continuum percolation model. In that model, the vertex set is given by an (almost surely inﬁnite) Poisson point process of ﬁxed intensity on Rd, and two points are connected with some probability that varies (and usually decreases) with their distance. In particular, the special case in which the radius of connection is deterministically ﬁxed at 1 was the model that initiated the study of this kind of random geometry, in the seminal paper of Gilbert [17]. The properties of interest in this model are the existence of an inﬁnite connected component, as well as the behavior of the subset of Rd that is at distance at most 1 from one of the vertices of the graph (the so-called “Poisson blob”) and its complement (the “vacant set”). Continuum percolation is treated in detail in a book-length monograph by Meester and Roy [29], as well as in the book by Grimmett [19].

Most of the work done on random geometric graphs is concerned with either the behavior of a typical graph — the graph we are likely to see for a given r as n goes to inﬁnity — or typical deviations from that behavior — that is, central limit theorems. In this paper, we are concerned with the behavior of the model conditioned on a rare event. Speciﬁcally, we will study the random geometric graph conditioned on having many more edges than is expected (a formal description will follow). The large deviation regime of the upper tail of any subgraph count of the random geometric graph is not well understood, though some bounds are available: Janson [24] established concentration inequalities for U-statistics, a general class of statistics which includes the subgraph counts we are interested in. These upper bounds work in very general settings, but are not tight, even up to constants in the exponent. Large deviation principles have been proven for functionals of random point processes in which the contribution of any particular vertex is uniformly bounded [38], but no such bound is known for functionals with possibly large inﬂuence, such as the edge count of the graph.

As motivation for this detailed study, we consider the problem in a more familiar context: the “infamous upper tail” [25] of the triangle count T in the Erdős–Rényi random graph, G(n,p). After many years of development of increasingly strong bounds, the ﬁrst breakthrough was made by Kim and Vu [27] and Janson et al. [26] independently, who proved that, for any δ > 0 and whenever p  (logn) n,

exp[−c(δ)n2p2 log(1 p)]≤ P[T >(1 + δ)E[T]]≤ exp[−C(δ)n2p2],

where c(⋅) and C(⋅) depend only on δ. Recently, there has been renewed interest in these type of tail estimates. In 2010, Chatterjee [8] and Demarco and Kahn [12] (in independent works) established the correct order of the upper tail of triangles and other small cliques by adding the missing logarithmic term to the upper bound, without providing good control of the leading-order constants. The work of Chatterjee and Dembo [10] on nonlinear large deviations proved that the upper tail probability can be described in terms of a continuous variational problem when p is vanishing suﬃciently slowly — namely, when n−1 42 p 1. Generalizations and expansions of the approach by Eldan [14] established the variational equivalence for n−1 18 logn p 1; Cook and Dembo [11] proved the result for n−1 3 p 1, and Augeri [1] did the same for n−1 2(logn)2 p 1. Lubetzky and Zhao [28] solved the variational problem for triangles (Bhattacharya, Ganguly, Lubetzky and Zhao [5] did the same for more general subgraphs), which thus calculated both the order and the leading-order constant for the upper tail question in a certain regime of sparse Erdős–Rényi random graphs. The main results and ideas from this body of work are summarized in the survey article [9]. Recently, Harel, Mousset, and Samotij [21] used a combinatorial approach to prove that the upper tail probability of the subgraph count of any ﬁxed, regular graph can be expressed in terms of the solution of a discrete variational problem for nearly all values of p where localization is believed to hold. Unfortunately, all the papers described above are only valid for functions of independent Bernoulli random variables, and are therefore not applicable to the problem we are studying here.

In this work, we use the properties the random geometric graph inherits from the geometry of Rd to evaluate the upper tail large deviation rate function. In addition, we provide a “structure theorem” to describe the graph-theoretical structure of the model conditioned on having too many edges. Speciﬁcally, we show that such a conditional model exhibits localization. Heuristically, this phenomenon can be described as a scenario in which a small number of vertices will contribute almost all the extra edges that we require the graph to exhibit, while the edge count of the “bulk” of the graph will remain largely unchanged, in some weak sense. Furthermore, we will show that the geometry of the localized region has the shape of a ball in the given norm (we will make these two statements more precise at the end of the next section). Outside of the aforementioned works of Lubetzky and Zhao [28], Bhattacharya et al. [5], and Harel, Mousset and Samotij [21] in the Erdős–Rényi model, this work is the only (as far as the authors are aware) to establish that the large deviation regime of a subgraph count is (weakly) equivalent to planting a combinatorial structure in the usual, unconditional graph.

The fact that large deviation events may be dominated by conﬁgurations with a small number of very large contributions was known relatively early

in the history of large deviation theory: a survey by Nagaev [31], summarizing a series of papers written in the Soviet Union in the 1960’s and 70’s, includes this observation for sums of i.i.d. random variables with stretchedexponential tails. In our context, the natural combinatorial structure for creating many edges with a small number of edges is a “giant clique”. The clique number, the (typical) size of the largest clique of the random geometric graph, falls under the general class of scan statistics, and has been shown to focus on two values with high probability for certain values of r (see [32], [30]); however, these works do not explore the large deviation regime. Our work uses techniques from large deviations, concentration inequalities, convex analysis, and geometric measure theory. A key component in the proof is a technique for proving localization that has previously appeared in [40] and [7].

2. Definitions and Main Results

Let χn be a Poisson Point Process of intensity n on the d-dimensional unit torus Td =[0,1]d. For any S ⊂ Td, we denote the restriction of χn to S by χn(S). Let N ∶= χn . Recall that N is a Poisson random variable with mean n, and conditional on N, χn is just a set of N points, each chosen independently and uniformly at random. Let rn be a positive sequence that decreases to 0 as n → ∞, and  ⋅  be some norm on Rd that induces a translation-invariant metric on Td. We deﬁne the random geometric graph G(χn,rn)∶=(V,E), where V = χn ={v1,...,vN}, enumerated arbitrarily, and E is the set of unordered pairs {i,j} such that vi − vj ≤ rn. Figure 1 shows a particular instance of G(χ150,0.1).

Letting 1i,j be the indicator that there is an edge between vi and vj, we can calculate the expected value of E , the number of edges in the graph:

E( E )= E

1i,j = E

E(11,2 N) 

N 2

1≤i<j≤N

n2 2 ⋅ P( v1 − v2 ≤ rn).

=

Denoting Lebesgue measure on both Rd and Td by λ(⋅), we deﬁne ν ∶= λ x ∈ Rd ∶ x ≤ 1

to be the volume of the unit ball in the norm  ⋅ . Then,by translation invariance of the metric induced on Td, P( v1 − v2 ≤ rn) is simply νrnd, as long as rn is suﬃciently small (to ensure the ball on the torus has the same measure as the one in Rd)

ν ⋅ n2rnd 2

µn ∶= E( E )=

.

We can also compute the variance of E :

- (2.1) Var( E )= E[Var( E N)]+ Var(E[ E N])

= E E

1≤i<j≤N,1≤i′<j′≤n

(1i,j − νrnd)(1i′,j′ − νrnd) N

+(νrnd)2Var

N 2

=

n2 2

νrnd − ν2rn2d + n3 +

n2 2

ν2rn2d

= µn 1 + 2νnrnd ,

where we note that (i,j)≠(i′,j′) implies that the indicators 1i,j and 1i′,j′ are

conditionallyµ2n, and E concentratesindependent.aroundThis impliesits meanthat,by asChebyshev’slong as µn inequality.→∞, Var( E ) 

For the rest of the article, we suppose the existence of a ﬁxed constant δ∗ > 0 such that, for all suﬃciently large n,

- (2.2) n(δ∗−2) d ≤ rn ≤ n−δ∗ d . The lower bound ensures that the expected number of edges grows as a

positive power of n; the upper bound excludes the possibility of rn = n−o(1) — that is, bounded above and below by nε and n−ε, respectively, for any ﬁxed ε > 0 and n ≥ n0, for some n0 depending on ε. We will reuse the notation no(1) throughout the paper in this sense, and we will allow the (implicit) ε to depend on any ﬁxed parameter other than n. We deﬁne the parameter p as

- (2.3) p ∶= lim n→∞

logµn logn

,

implicitly assuming that the limit exists. This ensures that µn = f(n)np, where f(n)= no(1). Notice that

- (2.4) δ∗ ≤ p ≤ 2 − δ∗ ,


thanks to (2.2). We will say the random geometric graph is admissible if rn satisﬁes (2.2) and the limit above exists.

The following theorem is the main result of the paper:

- Theorem 2.1. Let G(χn,rn) be an admissible random geometric graph model on Td with respect to some norm  ⋅ . Deﬁne


τn ∶= ν ⋅(rn 2)d ,

that is, τn is the volume of a ball of diameter rn. Fix δ > 0 and ε > 0, and let Fn(ε) be the event that there exists a ball B of diameter rn such that

- (1) any convex set S ⊂ B satisﬁes


χn(S)  √2δµn −

λ(S) τn  < ε,

![image 1](<2014-chatterjee-localization-random-geometric-graphs_images/imageFile1.png>)

Figure 1. An instance of the random geometric graph G(χ150,0.1), with respect to the Euclidean norm. The graph has 148 vertices and 343 edges. The gray area is the white unit square translated, to show periodicity

- (2) for any convex set S′ ⊂ Bc such that diam(S′)≤ rn and λ(S′)> ετn,


χn(S′)  √2δµn < ε ⋅

λ(S′) τn

. Then

P Fn(ε)  E >(1 + δ)µn = 1.

lim

n→∞

As a consequence of Theorem 2.1, we prove that the upper tail of the edge count of random geometric graphs satisﬁes a large deviation principle. Recall that a sequence of non-negative random variables Xn satisﬁes an upper tail large deviation principle with speed s(n) and rate function I(x) if, for any closed set F ⊂(0,∞),

Xn − E[Xn] E[Xn]

∈ F ≤− inf

I(x),

1 s(n)

logP

limsup

x∈F

n→∞

and for any open set G ⊂[0,∞),

Xn − E[Xn] E[Xn]

∈ G ≥− inf

I(x).

1 s(n)

logP

liminf

n→∞

x∈G

(For more on large deviation principles and their applications, see e.g. [13].) The following theorem gives the upper tail large deviation principle for the number of edges in a random geometric graph.

- Theorem 2.2. Let G(χn,rn) be an admissible random geometric graph model on the d-dimensional torus, with the same assumptions as in Theorem 2.1. Deﬁne


√2x,

2 − p 2

I(x)∶= 

√µn logn and rate function I(x).

where p is deﬁned as in (2.3). Then E satisﬁes an upper tail large deviation principle with speed s(n)=

There are several important features to the two main theorems of this paper: ﬁrst, both describe models in which the number of edges signiﬁcantly exceeds its mean. The lower tail of the edge count — i.e. events of the form { E <(1−δ)µn} — is likely to satisfy Poisson-like statistics. Its large deviation principle is expected to hold with speed µn, and no special combinatorial structure like the “giant clique” of Theorem 2.1 should appear.

Before we go on, let us comment on the precise properties of the giant clique given by our two main theorems. Since the rate function of Theorem 2.2 is strictly increasing, we know that, conditional on { E >(1+δ)µn}, the event

 (1 + δ′)µn > E >(1 + δ)µn

occurs with high probability (i.e. probability at least 1 − ε) for any δ′ > δ and n suﬃciently large. Now, if we set S = B in the ﬁrst stipulation of

- Theorem 2.1, we see that the ball B of diameter rn makes up a clique of at least √2δµn(1−ε) vertices — and therefore at least δµn(1−2ε) edges. Since ε and δ′ − δ are arbitrarily close to zero, we ﬁnd that the clique in B has


δµn + o(µn) edges, whereas the rest of the graph has µn + o(µn) edges. This formalizes our earlier claim that ‘almost all extra edges in the conditional model are between points in B.’

- Theorem 2.1 also gives information about the internal geometry of the


giant clique. If we pick S to be a proper convex subset of the ball B, we ﬁnd that χn(S)  proportional to √2δµn times the density of S in B (again, up to lower order corrections). We restricted S to be convex in order to preclude pathological sets, such as sets which are sparse but of large measure (e.g. generalized Cantor sets) or have boundaries that take up a large amount of space. It should be possible to replace convexity with a weaker assumption. That being said, probing the Poisson point process χn with convex S ⊂ B is enough to establish that the conditional process, restricted to B, is distributed roughly uniformly, up to errors that vanish in comparison to √µn.

Finally, we would like to say that there are no other large cliques in G(χn,rn) conditioned on { E >(1+δ)µn}; unfortunately, Theorem 2.1 does not provide this result. Instead, we can only be sure that every other clique outside of the “exceptional” set B has o(

√µn) vertices, that is, much smaller than the largest clique.

3. The s-Graded Model

Henceforth in the manuscript, we will suppress the subscript n and write χ, µ, τ and r instead of χn, µn, τn and rn.

We now present an approximation of the random geometric model which allows us to replace the Poisson point process with a sequence of independent Poisson random variables. To do this, we ﬁrst discretize space, and then produce a semi-metric on the resulting “cells” that approximates the norm  ⋅  on the unit torus. We call this the s-graded model.

For a positive integer s, deﬁne

m ∶= s r , so that

s r − 1 ≤ m ≤

s r

. This deﬁnition and (2.3) imply that

- (3.1) md = n2−p+o(1),

where the constant in the o(1) depends on s. Let T ={1,2,...,m}d. Pick I =(i1,i2,...,id)∈ T, and deﬁne

AI = 

i1 − 1 m

,

i1 m × ⋅⋅⋅ × 

id − 1 m

,

id m

.

The AI’s partition the unit torus into md cubes (ignoring sets of measure 0), each of volume 1 md, and therefore, XI = χ(AI)  is a Poisson random variable of mean

- (3.2) D ∶=

n md

. We now deﬁne a semi-metric on T, induced by the norm on torus:

- (3.3) ρ(I,J)= inf x∈AoI,y∈AoJ


m x − y

where the circles indicate the interiors of the sets. Note that the ρ(⋅,⋅) is always an integer. Moreover, ρ(I,J)= z if z is the smallest integer such that some point in AoI and some point in AoJ are less than z away, measured in units of 1 m, the side length of the cubes. We force the points to be in the interior to prevent “trivialities”, such as two adjacent cells being distance 0, since they share a boundary. Note that ρ(⋅,⋅) does not satisfy the triangle inequality, and hence is only a semi-metric. To see this, consider T5 under the Euclidean norm, and the cells A1 = A(1,...,1), A2 = A(2,...,2) and A3 = A(3,...,3). Since A1 and A2 share a corner, ρ(A1,A2) = 1, and the same holds for ρ(A2,A3). However, ρ(A1,A3)=

√5 > 1 + 1 = ρ(A1,A2)+ ρ(A2,A3). But

ρρ(doesK,J)+satisfyCd, wherea modiﬁedCd dependstriangleonlyinequalityon the ofdimensionthe formandρ(I,Jchoice)≤ ρof(I,Knorm,)+ though we never make explicit use of this fact.

We are now ready to deﬁne the s-graded random geometric graph. Let Gs(χ,r)=(V,Es) have the same vertex set as the original graph. For each

vertex v, let Iv be the index in T such that v ∈ AIv; there is ambiguity on the boundary of the AI’s, but that set has Lebesgue measure 0, and therefore it has no vertices of χ, almost surely. We say (v,w)∈ Es whenever ρ(Iv,Iw)≤ s. Heuristically, the s-graded model allows every point to wander inside a cubical “cage” of side-length 1 m, and connects any two points that might be connected after we allow this mobility. In this framework, it is clear that Es becomes smaller as s decreases. In fact, for suﬃciently large s, Es is identical to E; unfortunately, this s will be random. In formulating

- Theorem 3.1, the main theorem of this section (which is proved in Section


- 5), we will let s be an arbitrary positive integer, and discuss its asymptotic properties as n goes to inﬁnity. Later, in Sections 6 and 7, we will take s to suﬃciently large, and show that the resulting approximation is good enough for our purposes.


Having deﬁned the s-graded model, we now need to compute several quantities related to it, as we did for the random geometric graph in Section 2. We will denote s-graded model variables with tildes, to distinguish them from similar variables deﬁned by the continuous geometry of the Td. We will say Gs(χ,r)=(V,Es) is admissible whenever the random geometric graph G(χ,r) is admissible.

The major beneﬁt of the s-graded model is that its edge count is very simple to express in terms of XI, the number of points in each AI:

Es =

XI 2  +

- 1

- 2 J ∶0<ρ(I,J)≤s


- (3.4) XIXJ


I∈T

=

XJ − 1 .

- 1

- 2 I∈T


XI

J ∶ρ(I,J)≤s

This random variable is deﬁned in terms of i.i.d. random variables, which eases the analysis greatly. The geometric relations that deﬁne the edge count are now completely encoded by ρ. Finally, each XI only appears in ﬁnitely many terms in this expression (i.e. the number of terms involving XI is uniformly bounded in n). The “ﬁnite range” nature of the representation will play a major role in the proof presented.

We quantify this fact as follows: for any I ∈ T, let

N˜I ∶={J ∶ ρ(I,J)≤ s}.

Thanks to translation invariance of ρ, the cardinality of this set is independent of the choice of I. Using this parameter, we can compute the expected

number of edges in the s-graded random geometric graph easily:

- (3.5) µ˜s ∶= E( Es )

=

I∈T

E

XI 2  +

- 1

- 2 J ∶0<ρ(I,J)≤s


E(XI)E(XJ) 

=

N ˜I mdD2 2 =

N ˜I n2 2md

,

where we recall that D is the mean of XI, and the deﬁning relation (3.2). The variance of Es is also straightforward to calculate from the above representation, though the exact formula is messy. Instead, we produce an upper bound: the variance of Es can be thought of as the sum of (E[QI ⋅ QI′]− E[QI]2), where QI is the summand in (3.4) and I,I′ ∈ T. This quantity is maximized when I = I′, and is zero if the two terms are independent. Thus, we ﬁnd that

Var[ Es ]≤

I∈T

S ˜I ⋅ E

XI 2  +

- 1

- 2 J ∶0<ρ(I,J)≤s


XIXJ −

N ˜I D2 2

2

,

where

S˜I ∶={J ∶ N˜I ∩ N˜J ≠ }. A straightforward (if elaborate) computation can show that this implies that

- (3.6) Var[ Es ]≤ 16 S ˜I N ˜I 2md ⋅ max{D3,D2}.

In Lemma 5.1 below, we will show that both N ˜I and S ˜I are uniformly bounded in n. Together with (3.5) and (3.2), this implies that, for any s,

Var[ Es ]  µ˜2s, and hence Es concentrates around its mean by Chebyshev’s inequality.

As before, we are interested in conditioning the s-graded model on the event { Es >(1 + δ˜)µ˜s}. Following Theorem 2.1, we expect that such conditional measures will be concentrated on conﬁgurations with many points on sets of diameter s and maximal cardinality. We call a set of indices a maximal clique set if it is a subset of T with diameter ≤ s that achieves the maximal cardinality of all such sets. We deﬁne

- (3.7) τ˜s ∶= max{ I ∶ I ⊂ T,diam(I)≤ s},

i.e. τ˜s is the cardinality of a maximal clique set. Clearly τ˜s is increasing in s, and

- (3.8) τ˜s ≥ τ˜1 ≥ 2d,


as the diameter of the set {I = (η1,...,ηn) ∶ ηi ∈ {1,2}} under the semimetric ρ(⋅,⋅) is exactly 1, as all the AI’s share a corner. We will also need an approximate notion of this geometric object: we say a set is a ε˜-almost maximal clique set if its diameter is bounded above by s, and its cardinality is at least (1 − ε˜)τ˜s.

We can now state the equivalent to Theorem 2.1 for the s-graded model:

- Theorem 3.1. Let s be a positive integer. Consider Gs(χ,r), an admissible s-graded random geometric graph. For any δ˜ > 0, deﬁne the event Ln(δ˜) by


Ln(δ˜)∶={ Es >(1 + δ˜)µ˜s}.

For any ε˜> 0, let Gn,δ˜(ε˜) be the event there exists a pair of sets B and C in T such that

- (1) B is a ε˜-almost maximal clique set,
- (2) for all I ∈ B, τ ˜sXI

(2δ˜µ˜s)1 2

− 1 < ε,˜

- (3) C satisﬁes

C < ε˜⋅ τ˜s and

I∈C

XI < ε˜⋅(2δ˜µ˜s)1 2, and

- (4) for all J ∈(B ∪ C)c, τ˜sXJ


< ε.˜

(2δ˜µ˜s)1 2

There is a universal constant ε˜0 > 0 such that the following is true. Take any ε˜ ∈(0,ε˜0), any positive integer s, and any three numbers 0 < δ˜0 ≤ δ˜ ≤ ∆˜0. Then there is an integer n0 depending only on s, ε˜, δ˜0 and ∆˜0, such that whenever n ≥ n0,

P[Gn,δ˜(ε˜)c ∩ Ln(δ˜)]

≤ 3exp −(2δ˜µ˜s)1 2 log (2δ˜µ˜s)1 2

τ˜s ⋅ D  − 1 +(ε˜ 10)10 2 .

Because of its technical nature, Theorem 3.1 warrants a short explanation. It turns out that it is possible to show that, for some η > 0

P[Ln(δ˜)]≥ exp −(2δ˜µ˜s)1 2 log (2δ˜µ˜s)1 2 τ˜s ⋅ D  − 1 − Cnp 2−η .

This bound comes from explicitly “planting" a maximal clique set where every cell includes exactly  (2δ˜µ˜s)1 2 τ ˜s vertices; we will not prove this fact, but Lemma 6.5 will show a very similar computation for the edge count of the random geometric graph. In Lemma 5.1 below, we will show that N ˜I is uniformly bounded in n for any s > 0. Together with the fact that δ˜ is uniformly bounded above and below in n, this implies that (2δ˜µ˜s)1 2 = np 2+o(1) np 2−η. Therefore, Theorem 3.1 shows that, with high probability, the event Gn,δ˜(ε˜) occurs in the conditional s-graded model.

The event Gn,δ˜(ε˜) produces a set B, which is very close to a maximal clique set, in which each XI is very close to 2δ˜µ˜s τ ˜s — the value we would expect if we were to spread the 2δ˜µ˜s vertices required to make a “giant” clique evenly among the τ˜s elements of a maximal clique set. In addition,

we allow for an “exceptional" set C, where some XI’s may be much larger than this average amount. However, this exceptional set is made up of few

indices, and includes few vertices of χ, when compared with 2δ˜µ˜s. Outside of these two sets, every XJ is at most ε˜ 2δ˜µ˜s τ ˜s — a lower order quantity when compared to the bounds on XI,I ∈ B.

When this event ﬁres, the conditional s-graded model has a clique with approximately δ˜µ˜s edges. We also know that the vertices are distributed roughly uniformly. Finally, we get a quantitative estimate on the probability that the edge count of the s-graded model exceeds its mean without the desired structure occurring. Note that the constants and 10th power of ε˜ that appears in the quantitative bound are somewhat arbitrary — we made

- no attempts to optimize them.


Suppose that ε˜<(2˜τs)−1. In this case Gn,δ˜(ε˜) would require B ≥ τ˜s − 1 2 and C ≤ 1 2 — i.e. C is empty and B is a true maximal clique set. Thus,

- Theorem 3.1 can be used to show that the s-graded model conditioned on


oL(n1())δ˜)edges.will includeUnfortunately,a maximalthecliquequantitativeset housingestimatea cliqueonoftheatprobabilityleast δ˜µ˜s(1of− Gn,δ˜(ε˜)c ∩ Ln(δ˜) in this case is not suﬃciently good to deduce Theorem

- 2.1. This is the reason for the introduction of the ε˜-almost maximal clique sets, which allow us to deduce a stronger upper bound on the probability


that Gn,δ˜(ε˜) does not occur — at the price of dealing with more ﬂexible geometric constructions.

4. Outline of the Proof

Before embarking on a proper proof, we sketch the main ideas required. We recall that δ∗ > 0 is a ﬁxed positive number and that p is given by limn→∞ logµ logn. We will deﬁne

δ∗ 25

a ∶=

.

Later, we will also pick two positive real numbers α,β as some quantities depending on p and a. All of these quantities will be ﬁxed throughout the paper. We further note that, for any admissible graph, r → 0 as n →∞. For the remainder of the paper, we will take the statement “n is suﬃciently large” to imply that r is suﬃciently small.

We begin by carefully analyzing the s-graded model. We order the indices

I by the size of XI, the point counts of the AI’s. Explicitly, we pick a bijection from T to {1,2,...,md} such that

X1 ≥ X2 ≥⋅⋅⋅≥ Xmd . For notational convenience, we set

q =(2δ˜µ˜s)1 2, w = τ˜s ⋅ D.

Picking a as above, we set M = D ⋅ na, and let TM be the greatest I such that XI ≥ M. We deﬁne

I ={1,2,...,TM}, ordered by size as above,

to be the set of indices whose associated point counts XI exceed their mean (corrected for integrality) by a ﬁxed polynomial factor. Furthermore, deﬁne

YI ∶= XI (log(XI D)− 1)+ D , and

Q(I)∶=

XI 2  +

2 q2 I∈I

- 1

- 2 J∈N˜


XIXJ ,

I∩I J≠I

and

V (I)∶=

1 q I∈I

XI.

The ﬁrst quantity is an appropriately chosen convex function of the XI’s, while the second is a scaled version of the number of edges with both end-

points in the AI’s associated with I, and the third controls the number of vertices in I.

Let ξ > 0 be a ﬁxed constant independent of n. Consider the event

Hξ = Q(I)≥ 1 −

YI ≤ log(q w)− 1 + ξ .

ξ logn

1 q I∈I

The main probabilistic analysis of this paper occurs in two sections: the ﬁrst uses large deviation estimates to control sums of i.i.d. random variables, and the second employs concentration inequalities for more complicated functions. Together, this work allows us to show that, for suﬃciently large values of n and small values of ξ,

q w − 1 + ξ 2 .

P[Hξc ∩ Ln(δ˜)]≤ 3exp −q log

It turns out that, if we set ξ ≤(ε˜ 10)10, any I ⊂ T that satisﬁes both the quadratic lower bound and the convex upper bound that deﬁne Hξ (as well as a mild bound on TM and V (I)) contains in it a ε˜-almost maximal clique set B and an exceptional set C that satisfy the four stipulations of Gn,δ˜(ε˜)! This nontrivial statement implies Gn,δ˜(ε˜)c ⊂ Hξc, whenever ξ ≤(ε˜ 10)10 – and, in particular, {Gn,δ˜(ε˜)c∩Ln(δ˜)}⊂{Hξc∩Ln(δ˜)}. This proves Theorem

- 3.1. The proof of the above implication is not straightforward, and we will de-


duce it in several steps. We emphasize that this is a completely deterministic property of conﬁgurations that satisfy a certain set of inequalities. The next two paragraphs sketch the argument used to prove this implication.

Set TV to be

TV ∶= min k ∶ V ({1,...,k})> 1 −

and T ∶={1,...,TV }.

2ξ logn

Careful use of minimality and Jensen’s inequality proves that

V (T)≤ 1 + φ(TV ), Q(T)≥ 1 − ψ(TV ), where φ(⋅) and ψ(⋅) are explicit functions, bounded above by 1 (logn)1 2, that are non-increasing in their arguments. One of the diﬃculties we encounter is that we do not have good upper bounds on TV , and thus must have bounds that improve whenever the parameter grows.

We set TP to be the greatest integer I smaller than TV that satisﬁes XI > ξq τ ˜s. Setting P ={1,2,...,TP}, we now have a set of indices whose associated XI’s are commensurate with q. We proceed to show that the diameter of P cannot exceed s without violating either the lower bound on Q(T) or the upper bound on V (T). Together with technical estimates that force TP ≥ τ˜s(1 − ξ1 3), we ﬁnd that P is an ξ1 3-almost maximal clique set. Moreover, a quantitative version of Jensen’s inequality allows us to break P into B and C, the required sets. Finally, we can show that XTP+1 vanishes suﬃciently quickly to completes the proof of Theorem 3.1.

We then move on to proving that Theorem 3.1 implies Theorem 2.1. To do so, we ﬁrst show that we can approximate any convex subset S of a ball of diameter r from both the inside and the outside by a union of AI’s using the tools of geometric measure theory. Next, we use the classical isodiametric inequality to show that the AI’s associated with a s−1 20-almost maximal clique set approximate a ball of diameter r, in the sense of the Hausdorﬀ metric.

Next, we ﬁx ε > 0, and show that, for suﬃciently large s and δ˜ ∈[(1 − ε 16)δ,δ], the event Gn,δ˜(s−1 20) will imply Fn(ε). We then apply Theorem 3.1 with δ˜ as above and ε˜= s−1 20 to get an upper bound on the probability of {Fn(ε)c ∩ Ln(δ˜)}. Combining this bound with a good lower bound on the probability of { E >(1 + δ)µ} (to be derived directly from the Poisson point process) and a well-known correlation inequality gives Theorem 2.1.

The ﬁnal section of the paper proves the large deviation principle of Theorem 2.2. We use the ﬁrst stipulation of Theorem 2.1 and the s-graded model to compute the upper bound.

5. Analysis of the s-Graded Model In this section we analyze the s-graded model and prove Theorem 3.1.

δAt˜0 ≤theδ˜ ≤very∆˜0. Webeginning,will ﬁgurelet outus nowthe universalﬁx a positiveconstantintegerε˜0 slater.and Throughout,numbers 0 < whenever we say “n suﬃciently large”, we will mean “n ≥ n0 for some n0 that depends only on s, ε˜, δ˜0, and ∆˜0”.

- 5.1. Controlling the Natural Parameters of the s-Graded Model. The geometric properties of the s-graded model are not quite comparable to those of the random geometric graph; most obviously, the s-graded model has a discrete geometry induced by the semi-metric ρ(⋅,⋅) on T. We begin with a very useful lemma, which tells us that the parameters of the s-graded model


are close to their appropriate equivalents on Td. To do so, we deﬁne three operators: ﬁrst, let U send a set of indices to the union of their associated AI’s — that is, for any I ⊂ T,

- (5.1) U(I)∶= I∈I

AI .

InandtheO(otherK) todirection,be the maximalwe must(resp.be moreminimal)careful.subsetsLet K ⊂ofTTd, suchwe deﬁnethatR(K)

- (5.2) U(R(K))⊂ K and K K′ ⊂ U(O(K)) ,

where K′ is some subset of K of Lebesgue measure 0; this modiﬁcation allows us to not deal with certain trivialities. We note that R(K) may be empty, and O(K) may be T, even when K or T K are nonempty. Alternatively, we may deﬁne O(K) by

O(K)∶={I ∈ T ∶ λ(K ∩ U(I))> 0}.

We recall several deﬁnitions: µ = E( E ), µ˜s = E( Es ) and τ = ν(r 2)d. We set N ˜I to be the number of indices satisfying ρ(I,J) ≤ s, and S˜I = {J ∶ N˜I ∩ N˜J ≠ }. Finally, τ˜s is the cardinality of a maximal clique set (as deﬁned in (3.7)).

- Lemma 5.1. We have E ⊂ Es, and there exist constants C, s0, and n0 depending only on the dimension and the chosen norm of the torus, such that, if s ≥ s0 and n ≥ n0, then


µ ≤ µ˜s ≤ µ 1 +

C s

and

mdτ ≤ τ˜s ≤ mdτ 1 +

C s

Furthermore, N ˜I , S ˜I , and τ˜s are uniformly bounded in n.

In this section, we will only use this lemma to establish that certain quantities are uniform in n; in Section 6, we will strongly use the fact that the estimates become tight as s grows.

Proof. Pick an arbitrary I and consider U(N˜I). By deﬁnition of ρ(⋅,⋅) and s, this set includes a ball of radius r around any point in AI. Therefore, any pair (v,w)∈ E must also be in Es, giving the ﬁrst stipulation. Since this inclusion holds for any conﬁguration of the underlying Poisson Point process, this also gives µ ≤ µ˜s.

Now, deﬁne ς to be the diameter of the unit cube under the norm  ⋅  that is,

- (5.3) ς ∶= sup x,y∈[0,1]d


x − y .

Fix I, and let x and y be two ﬁxed points in AI and U(N˜I), respectively. Letting J be an index for which y ∈ AJ, we pick arbitrary points z and w in AI and AJ, respectively. Then the triangle inequality for  ⋅  implies that

x − y ≤ x − z + z − w + w − z ≤ z − w +

2ς m

,

where we bound the ﬁrst and last terms by ς m using scaling of the norm. Since z and w are arbitrary, we can take an inﬁmum over all choices of z and

- w in A○I and A○J, respectively, and conclude that


(s + 2ς)r s − r

s + 2ς m ≤

x − y ≤

,

where we use that m ≥ s r − 1, by deﬁnition. Therefore, U(N˜I) is contained in a ball of radius r(1 + 3ς s) around any point in AI, for suﬃciently large value of s and n (recalling that r is vanishing in n). Since each AI is of measure of m−d, we deduce that

d

N ˜I = mdλ U(N˜I) ≤ νmdrd 1 +

≤ νmdrd 1 +

6dς s

3ς s

,

where the ﬁnal inequality follows because (1 + x)d ≤ 1 +(2d)x for all sufﬁciently small x. Substituting this into the deﬁnition of µ˜s produces the desired inequality on µ˜s. Repeating a similar analysis will show that the set U {J ∶ N˜I ∩ N˜J ≠ }  is a subset of some ball of radius 2r(1+3ς s), and thus

S ˜I ≤ νmd(2r)d 1 +

6dς s

.

Next, we wish to control τ˜s. For the lower bound, let B ⊂ Td be an Barbitrary)> 0 forballevery(inI ⋅ ∈ O) (ofBdiameter). Therefore,r. Consider O(B). By minimality, λ(AI ∩

x − y  ≤ r ,

max

inf

x∈AoI,y∈AoJ

I,J∈O(B)

which implies, by the deﬁnition of ρ(⋅,⋅), that the diameter O(B) is at most s. Meanwhile, by inclusion, and the fact that λ(AI)= 1 md for every I,

O(B) > mdλ(B)= mdτ , completing the lower bound.

For the upper bound, pick any W ⊂ T such that λ(U(W))≥ τ 1 +

C s

Applying the isodiametric inequality for ﬁnite dimensional normed spaces [6, p. 93] and choosing C and s0 suﬃciently large gives

diam(U(W))≥ r 1 +

C s

1 d

≥ r 1 +

4ς s − r

.

This implies that the diameter of W is at least s + 1. Therefore, any set W of diameter at most s must satisfy λ(U(W))< τ(1 + c S), and

W = md ⋅ λ(U(W))≤ mdτ 1 +

C s

, as required.

The uniform bounds on N ˜I , S ˜I , and τ˜s follow from md ≤ sd rd and the above formulae.

An immediate corollary to this theorem is that, assuming (2.3), µ˜s = np+o(1).

- 5.2. Large Deviation Estimates. The probabilistic bounds we need in this work are divided into two parts. The ﬁrst involves good control on the deviation of sums of i.i.d. random variables. Our main tools here will be Chernoﬀ bounds, as well as exact lower bounds.


Recall from Section 4 that q =(2δ˜µ˜s)1 2, w = τ˜s ⋅ D, and Ln(δ˜)={ Es > (1 + δ˜)µ˜s}. By our assumptions on δ˜, (3.2), (3.5), and Lemma 5.1, we have that q = np 2+o(1) and w = np−1+o(1). Since p 2 > p − 1 for any admissible s-graded model, we can increase n to ensure that q > 3w. We will assume this inequality for the rest of the paper.

We begin by recalling some classical bounds on the Poisson distribution (for proof, see [13, pg. 35], for example):

- Lemma 5.2. Let XI be a Poisson random variable with mean D. Then, for any t > D,


P[XI ≥ t]≤ exp(−t[log(t D)− 1]− D), and for any t < D,

P[XI ≤ t]≤ exp(−t[log(t D)− 1]− D).

These bounds, which are given by explicitly computing exponential moment generating functions, are tight up to polynomial factors, and will be very important in the nearly exact computations we do in the proceeding lemmas.

We now deﬁne a random ordering of T according to the XI. Speciﬁcally, we pick a bijection from T to {1,2,...,md} such that

X1 ≥ X2 ≥⋅⋅⋅≥ Xmd .

This bijection is not unique, as each XI is integer-valued, and there may be many I’s whose associated XI’s are equal. However, all the statements will be true independently of the particular choice of bijection. Next, ﬁx a = δ∗ 25, and deﬁne M by

- (5.4) M ∶= D ⋅ na .


The number M is deﬁned so to be a threshold of density for XI — if XI < M, we say it is in the bulk of the graph. We expect that, even conditional on

Ln(δ˜), most indices I will be in the bulk. To formalize this, we let

TM ∶= max{I ∶ XI ≥ M}. The next proposition controls the tail of TM: Proposition 5.3. Let

α = min{1 − p 2 − a 2, p 2 − a 2}. Let A be the event {TM ≥ nα}. Then, for all suﬃciently large n, P[A ]≤ exp −np 2+a 3 .

The number α will remain ﬁxed to the value above for the remainder of the paper. We note that α < 2 − p for any admissible s-graded model, and therefore nα md (using (3.1)). Thus, we ﬁnd that, with very high probability, the complement of the bulk takes up a vanishing proportion of T.

Proof. The event A implies the existence of some W ⊂ T such that, for all I ∈ W, XI > M, and W > nα . By the union bound,

md nα  ⋅ P[XI > M]nα .

P[A ]≤ 

Using the upper tail bound in Lemma 5.2 and the brutal bound mk < mk, this implies that

P[A ] md(nα+1) ⋅ exp(−nαM [log(M D)− 1]) ≤ exp(d(nα + 1)logm − nα+a D ) .

Since logm is bounded above by C logn for some uniform constant C (by Lemma 5.1), we can increase n to ensure that

nα+a ⋅ D 2

P[A ]≤ exp −

. If D ≤ 1, then the ceiling function is 1 and α = p 2 − a 2. Increasing n until

- np 2+a 2 2 > np 2+a 3 completes this case. If D > 1, then we bound D by D itself. By deﬁnition,


Dnα+a = nmin{3p 2−1+a 2,p 2+a 2}+o(1).

In the case p ≥ 1, the exponent is always minimized by the second choice. This completes the proof.

The second estimate of this section will be used to control the behavior of the elements outside the bulk. Deﬁne

YI = XI log(XI D)− 1 + D ,

with the convention that 0 ⋅ log0 = 0. Note that YI = I (XI), where I is the rate function of a Poisson random variable of mean D. This implies

that YI ≥ 0 and vanishes only at D. I is a convex function, and thus we

can bound the sum of the YI’s by a function of the sum of the XI’s, using Jensen’s inequality. Furthermore, P[YI > t] should vanish as exp(−t), by “inverting” the rate function. We formalize this notion in the lemma below:

Lemma 5.4. For any D, and any positive λ < 1,

1 + λ 1 − λ

E[exp(λYI)]≤

.

Proof. The function I (x) = x[log(x D)− 1]+ D is not invertible, but is piecewise invertible. First, let

g1(x)∶[0,D]→[0,D] be a function such that (I ○ g1)(x)= x. Note that this function is decreasing, with g1(0)= D and g1(D)= 0. For any

- x > D, we say that g1(x)=−∞. We deﬁne g2, the second inverse, similarly, except its domain is deﬁned to be (D,∞). This inverse is strictly increasing. Thus,


P[YI ≥ t]= P[XI ≤ g1(t)]+ P[XI ≥ g2(t)]. By appealing to the two bounds of Lemma 5.2, we ﬁnd that both the probabilities above are bounded above by exp(−t); in fact, if t > D, the ﬁrst probability is identically zero. Regardless, it will suﬃce to use the bound P[YI > t]< 2e−t. Thus, for any λ < 1,

∞ 1

E[exp(λYI)]= 1 +

P YI >

logt λ

dt ≤ 1 + 2

∞ 1

t−1 λdt

1 + λ 1 − λ

=

, as required.

We now uses the lemma to control the upper tail of the sum of the YI’s over any suﬃciently small subset of T. We will only apply the proposition below on the set {1,2,...,TM} (which will be small with good probability from Proposition 5.3), but it is actually more straightforward to consider the existence of a subset with bad properties, in order to avoid conditional probabilities.

Proposition 5.5. Let YI as above, and α as in Proposition 5.3. Deﬁne the event

Bξ ∶= ∃W ⊂ T, W ≤ nα such that

YI > q(log(q w)− 1)+ ξq .

I∈W

Then, for all suﬃciently large n, P[Bξ]≤ exp(−q[log(q w)− 1 + ξ 2]).

Proof. Set t = q(log(q w)− 1 + ξ). Fix W ⊂ T with cardinality at most nα. By Chebyshev’s inequality

### exp(λYI) n

α

YI > t ≤

P

exp(λt) ≤ 

I∈W

1 + λ 1 − λ

nα

⋅ e−λt , where the second inequality is Lemma 5.4.

We now set λ = 1 − nα t, noting that, for suﬃciently large n, λ > 0 (since nα << q). This turns the above estimate into

⋅ e−t+nα

YI > t ≤(2t nα)n

α

P

I∈W

≤ exp(−t + Cnα logn) . The ﬁnal step is to apply the union bound:

nα

md

k  ⋅ e−t+Cnαlogn ≤ nα

P[B]≤

k=1

md nα ⋅ e−t+Cnαlogn

≤ md(nα+1) ⋅ e−t+Cnαlogn .

Recalling Lemma 5.1, we see that the combinatorial term in the ﬁnal inequality is bounded above by exp(Cnα logn) for some (probably diﬀerent) C. Since q >> nα logn, the entire positive contribution can be bounded above by ξq 2. This completes the proof.

- 5.3. Concentration Inequalities. This section will prove concentration of the edge count of the random geometric graph restricted to the bulk. Explicitly, let


XˆI ∶= XI ⋅ 1XI<M and Eˆs be the deﬁne analogously with Es by replacing XI with its truncated version (recall that M = D ⋅ na). In other words, Eˆs is the version of the edge count of Gs obtained after deleting all vertices lying in AI’s that satisfy XI ≥ M.

For the rest of the paper, ﬁx

β = p − 2a. Consider the event

C =  Eˆs − µ˜s > nβ . We control the probability of C in two regimes. We begin by assuming that D < logn.

Our strategy for proving an upper bound on C in this regime relies on Talagrand’s convex concentration inequality [39, Theorem 4.1.1]. First, let

us deﬁne the setting: let Ω = ∏Ni=1 Ωi, where Ωi are all probability spaces and the measure P on Ω is the product measure. For a set A ⊂ Ω, deﬁne the set

UA(x)∶={{si}∈{0,1}N ∶ ∃y ∈ A,si = 0  ⇒ xi = yi}.

Let VA(x) be the convex hull of UA(x), and dc(A,x) is the 2 distance of VA(x) to the origin. For any set A, we denote At be the t blowup of A with respect to this metric, i.e.

At ∶={x ∈ Ω ∶ dc(A,x)≤ t}. We can now state the inequality:

- Theorem 5.6 (Talagrand’s Inequality [39]). If Ω, P[⋅], A and At are as above, then

P[A](1 − P[At])≤ e−t2 4 .

We will not apply this theorem directly; instead, we use a corollary of this theorem frequently used in discrete settings [3, Theorem 7.7.1]. To do so, we consider a random variable X deﬁned on the space Ω, and a function f from the natural numbers to the natural numbers. We say that f is a witness function for X if, whenever X(ω)≥ t, there exists I ⊂[n] with I ≤ f(t), such that every ω′ that agrees with ω in all i ∈ I has X(ω′)≥ t. Furthermore, we assume that X(ω) is K-Lipschitz with respect to the Hamming distance — that is, X(ω)− X(ω′)  ≤ K whenever ω and ω′ diﬀer in at most one coordinate.

- Theorem 5.7 ([3]). Let Ω be a product space, and X a real valued function on Ω with Lipschitz constant K with respect to the Hamming distance. If f is witness function for X as above, then, for any b and t,


P[X > b + tK f(b)]P[X ≤ b]≤ exp(−t2 4). With this preliminary complete, we will prove the following lemma:

Lemma 5.8. Let C be as above, and assume that D < logn. Then, for all suﬃciently large n,

P[C]≤ exp −n2β−p−6a . Proof. Thanks to our assumption on D, M < na logn. We now apply Theorem 5.7 to X = Eˆs , considered as a function of the XI’s. Since each coordinate is bounded above by na logn, X is Lipschitz with K ≤ N˜I n2a log2 n. The function f(w)= 2w is a witness function for Eˆs ; to see this, note that

Eˆs is the edge count of the s-graded geometric random graph, after we remove any XI with very high density. As such, we can “witness” the existence of w edges by ﬁnding at most 2w vertices; the ﬂexibility of the setup allows us to pick these vertices judiciously, avoiding all the isolated ones. Finding 2w vertices will require at most 2w distinct coordinates, if each one of them vertices lies in a distinct AI. Note that this bound may be very loose – whenever 2w > md, we can easily just check every AI to witness Eˆs > w.

We apply the theorem with b = µ˜s + nβ logn and t =

nβ(1 − 1 logn) N ˜I n2a log2 n ⋅[2˜µs + 2nβ logn]1 2

. We deduce that

n2β [1 − 1 logn]2 8 N ˜I 2n4a log4 n[µ˜s + nβ logn]

P[C]⋅ P[ Eˆs ≤ µ˜s + nβ logn]≤ exp −

- (5.5) ≤ exp −n2β−p−5a ,


where the ﬁnal inequality holds for suﬃciently large n, using the fact that µ˜s = np+o(1) >> nβ logn and the fact that N ˜I is uniformly bounded in n.

To complete the proof, we must show that P[ Eˆs ≤ µ˜s + nβ logn] is not

too small. Since the mean of Eˆs is strictly smaller than the mean of Es , it is enough to show that

P[ Eˆs − E[ Eˆs ]≥ nβ logn]< ε.

XWeˆI will ∑J∈N˜produceI a very crude bound on the variance of Eˆs : let ZˆI =

XˆJ − 1 . Then clearly, Var[ Eˆs ]=

E Z ˆI − E[ZˆI]  ZˆJ − E[ZˆJ]  

I,J

S ˜I ⋅ E Z ˆI − E[ZˆI] 2

≤

I

A straightforward computation will show that, for some constant C independent of n,

E Z ˆI − E[ZˆI] 2 ≤ C(D2 + D4).

Since D < logn and S ˜I is uniformly bounded in n (from Lemma 5.1), this implies that Var[ Eˆs ]< np+o(1), and Chebyshev’s inequality gives that

P[ Eˆs − E[ Eˆs ]≥ nβ logn]≤ np−2β+o(1). For any admissible value of p, this function vanishes as n increases, and P[ Eˆs ≤ µ˜s + nβ logn]> 1 − ε. Substituting this into (5.5) gives us

P[C]≤ exp −n2β−p−6a , completing the proof.

Next, assume that D ≥ logn. In this regime, we replace Talagrand’s inequality with the celebrated Azuma–Hoeﬀding inequality:

Theorembe a martingale5.9 (Azuma–Hoeﬀdingsequence with Zk −inequalityZk−1 < ck for[2, 22])all k..LetThen{Z0,Z1,...,Zn}

t2 2∑nk=1 c2k

P[ Zn − Z0 > t]≤ 2exp −

.

We wish to prove the following lemma, bounding the probability of the event C:

- Lemma 5.10. Assume that D ≥ logn. Then, for all n suﬃciently large,


n2β mdD3n6a

P[C]≤ exp −

.

We note that a naive application of Azuma–Hoeﬀding to the martingale given by conditioning on the value of XˆI would give a bound on the probability of C which depends on the fourth power of D−1, not the third as in the lemma — an inferior bound. Thus, we need to be more careful in this analysis.

Proof. We partition AI into sets of measure 1 n; formally, let {FI,t}, for 1natural n for everyt ≤ Dt ≤  beDa −collection1, and of disjoint subsets of AI such that λ(FI,t)=

FI,t = AI .

t

Note that the measure of the ﬁnal FI,t will be strictly smaller than 1 n, unless D is an integer. We deﬁne WI,t = χ(FI,t) .

Clearly, ∑t WI,t = XI. Deﬁne Es as (yet another!) truncation of Es . Speciﬁcally, let WI,t = WI,t ⋅ 1WI,t<na 2, and deﬁne Es by replacing each XI in the deﬁnition of Es by ∑t WI,t. Note that Es is a function of md D independent random variables. Letting F′ be the σ-algebra generated by the ﬁrst WI,t’s (enumerated arbitrarily), we once again have a martingale sequence Z′ = E Es F′ . We also have that

Z′ − Z′ −1 ≤ N˜I ⋅ D n2a . Thus, Azuma–Hoeﬀding implies that

P Es − µ˜s > nβ 2 ≤ P Es − E[ Es ]> nβ 2

n2β 8md D 3 N ˜I 2n4a

≤ 2exp −

,

where the ﬁrst line follows since µ˜s > E[ Es ]. Using the uniform bound on N ˜I , we deduce that

n2β+o(1)

P Es − µ˜s > nβ 2 ≤ exp −

- mdD3n4a

≤ exp −

n2β

- mdD3n5a


. By partitioning,

- (5.6) P[C]≤ P[ Es − µ˜s > nβ 2]+ P[C, Es − µ˜s < nβ 2].


### The second event on the righthand side implies the event

E ∶={ Eˆs − Es > nβ 2}.

The lemma will follow if we can produce a good upper bound on the probability of the event E .

The diﬀerence between the random variables E ˆs and Es is given by conﬁgurations in which at least WI,t is larger than na 2. In fact,

WI,t ⋅ 1WI,t>na 2 ⋅

XJ ⋅ 1XJ< D na .

Eˆs − Es <

(I,t)

J∶ρ(I,J)≤s

While the random variables in the expression above are far from independent, we can replace the second sum over the XJ’s by N ˜I ⋅ D na, the upper bound imposed on it by the indicator random variables involved. Therefore,

Cnβ Dna

WI,t ⋅ 1WI,t>na 2 >

P[E ]≤ P

(I,t)

To bound this ﬁnal probability, we can directly bound the exponential moment of WI,t ⋅ 1WI,t>na 2:

ek k! ≤ 1 + exp(−na).

E exp WI,t ⋅ 1WI,t>na 2  ≤ 1 +

k>na 2

The ﬁrst inequality follows because WI,t is a Poisson random variable of mean

- 1 (or possibly less than 1, if we pick the small WI,t in each I), while the second can deduced by using Stirling’s approximation and explicitly summing.


Applying a Chernoﬀ strategy, we ﬁnd that

d(D+1) ⋅ exp −

Cnβ Dna ≤(1 + exp(−na))m

Cnβ Dna

WI,t ⋅ 1WI,t>na 2 >

P

.

(I,t)

Using the standard approximation (1 + x)≤ ex, we ﬁnd that the prefactor is bounded by 2 for all n suﬃciently large.

Substituting the bounds into (5.6) gives

n2β mdD3n5a + 2exp −

Cnβ Dna

P[C]≤ exp −

.

The ﬁrst term vanishes like exp(−n1−9a+o(1)), whereas the second vanishes as exp(−n1−7a+o(1)). Therefore, we conclude that

n2β mdD3n6a

P[C]≤ exp −

,

- as required.


- 5.4. Reducing to Deterministic Inequalities. The ﬁnal probabilistic step of this proof involves bounding the probability of a rather complicated set of simultaneous inequalities. Luckily, instead of dealing with the event


itself, we will control it using the events A , Bξ, and C, whose probability we controlled previously.

Recall that

V (W)=

1 q I∈W

XI

We also recall from the outline that, for any W ⊂ T, we set 2 q2 I∈W

- (5.7) Q(W)∶=


XI 2  +

- 1

- 2 J∈N˜


XIXJ .

I∩W J≠I

This counts the number of edges with both endpoints in AI’s with I ∈ W, normalized b q2 2; this choice will avoid many unnecessary factors in our later analysis. This immediately implies that, for any W ⊂ T,

Q(W)≤[V (W)]2 .

Using this notation, we can formulate Jensen’s inequality in the following way:

## Lemma 5.11. For any W ⊂ T,

q w + logV (W)− log

YI ≥ V (W) log

W τ˜s  − 1 .

1 q I∈W

Proof. This is a direct application of Jensen’s inequality to the convex function YI = XI log(XI D)− 1 + D. It implies that

qV (W) W D  − 1 + D W .

YI ≥ qV (W) log

I∈W

Dividing through by q, using the deﬁnition of w, and ignoring the positive additive term D W q gives the bound above.

We now begin the part of the analysis where we will obtain the universal constant ε˜0 in the statement of Theorem 3.1. For that, we ﬁrst introduce a parameter ξ > 0. We will eventually deﬁne ε˜ in terms of ξ. In the following, wherever we say “ξ suﬃciently small”, we mean “ξ ≤ ξ0 for some universal constant ξ0”. The meaning of “n suﬃciently large” will remain as it is.

Recal that TM ∶= max{I ∶ XI ≥ M}, and let I ∶={1,2,...,TM}. Given ξ > 0 and a constant C which does not depend on n, we deﬁne Hξ to be the

event that the following four inequalities hold:

- (5.8) TM < nα , 1 q I∈I

- (5.9) YI ≤ log(q w)− 1 + ξ ,
- (5.10) V (I)< C,

Q(I)≥ 1 −

ξ logn

- (5.11) .


Proposition 5.12. Deﬁne Hξ as above. Then, for all n suﬃciently large and ξ suﬃciently small,

P[Hξc ∩ Ln(δ˜)]≤ 3exp(−q[log(q w)− 1 + ξ 2]).

Proof. Suppose that A c ∩ Bξc ∩ Cc ∩ Ln(δ˜) implies Hξ. If this were true, then the union bound would imply that

P[Hξc ∩ Ln(δ˜)]≤ P[A ]+ P[Bξ]+ P[C].

The righthand side of the proposition above can be expressed as e−np 2+o(1). Therefore, for all suﬃciently large n, Proposition 5.3 implies that

P[A ]⋅ exp(q[log(q w)− 1 + ξ 2])≤ exp −np 2+a 3 + np 2+o(1) < 1,

where the ﬁnal inequality follows because the ﬁrst exponent is larger than p 2 for all admissible values of p. Similar analysis of exponents and Lemma 5.8 tell us that, if D < logn and n is large,

P[C]⋅ exp(q[log(q w)− 1 + ξ 2]≤ exp −n2β−p−6a + np 2+o(1) < 1.

When D > logn, P[C]< exp(−n1−10a−o(1)) by Lemma 5.10, and, for all n suﬃciently large,

P[C]⋅ exp(q[log(q w)− 1 + ξ 2])≤ exp −n1−10a + np 2+o(1) < 1.

Finally, Proposition 5.5 bounds the probability of Bξ by the righthand side. We conclude that, if A c ∩ Bξc ∩ Cc ∩ Ln(δ˜) implies Hξ,

P[Hξc ∩ Ln(δ˜)]≤ 3exp(−q[log(q w)− 1 + ξ 2]). For the remainder of this proof, we condition on the event A c ∩ Bξc ∩ Cc ∩ Ln(δ˜). The event A c automatically implies (5.8). With this bound on TM, (5.9) is immediate from Bξc. Next, we apply Lemma 5.11 to the sum of the YI’s over I ∈ I to deduce that

w ⋅ TM  − 1 + V (I)logV (I)≤ log(q w)− 1 + ξ . If V (I)≤ 1, we have a (much better than needed!) bound on V (I). Otherwise, V (I)logV (I) is positive, and we conclude that

V (I) log

qτ˜s

log(q w)− 1 + ξ log(qτ˜s (w ⋅ TM))− 1

V (I)≤

.

By (5.8) and the deﬁnitions of the variables q, w and α,

- (5.12)

qτ˜s

w ⋅ TM ≥ na 2+o(1) . Therefore, the denominator grows at least as a constant multiple of logn. Meanwhile, q w ≤ n1−p 2+o(1). This proves (5.10).

For the ﬁnal stipulation, we use the event Ln(δ˜)∩ Cc. By Cc,

- (5.13) (q2 2)⋅ Q(Ic)− µ˜s ≤ nβ . By the occurrence of Ln(δ˜),

q2 2

Q(I)+ Q(Ic) +

I∈I J∈N˜I∩Ic

XIXJ ≥(1 + δ˜)µ˜s ,

where the ﬁrst term counts edges with both endpoints either in or outside the bulk, whereas the sum counts the number of edges with exactly one endpoint in the bulk. Using the upper bound on Q(Ic) given by (5.13), we deduce that

- (5.14) Q(I)+

2 q2 I∈I J∈N˜

I∩Ic

XIXJ ≥ 1 −

2nβ q2

.

By deﬁnition, XJ ≤ M whenever J ∈ I, and therefore 2 q2 I∈I J∈N˜

I∩Ic

XIXJ ≤

2 N ˜I M

q ⋅ V (I). Recalling (5.4), we see that

M q = nmax{a−p 2+o(1),p 2−1+a+o(1)}.

The exponent is always negative, and therefore, for any admissible s-graded model, M q < ξ (2C logn) for suﬃciently large n. By (5.10) and Lemma 5.1, V (I) and N ˜I are uniformly bounded in n. Similarly, we can increase

(whichn suﬃcientlyis possibleto ensurethanksthatto (the2nβdeﬁnition) q2 is alsoofboundedβ). Substitutingabove bytheξ (2logboundsn) into (5.14) shows that A c ∩ Bξc ∩ Cc ∩ Ln(δ˜) implies Hξ, completing the proof.

5.5. Controlling the Linear Sum. The rest of the section is dedicated to analyzing conﬁgurations in Hξ. We will condition on this event — i.e. assume that the four inequalities in the deﬁnition hold, and show that subsets with certain properties exist. We emphasize that the statement will hold for any positive integer s, asymptotically in n. The number ξ will be chosen to be suﬃciently small for certain estimates to hold.

Deﬁne TV by

- (5.15) TV ∶= min k ∶ V ({1,...,k})> 1 −


2ξ logn

.

A priori, the set T ∶={1,2,...,TV } may include some elements of the bulk. The next lemma proves that not only are all these indices away from bulk, but, in fact, restricting our attention to T does not force us to ignore too many edges.

Lemma 5.13. Deﬁne T as above, and assume that Hξ holds. Then, for all n suﬃciently large and ξ suﬃciently small, the following holds:

τ˜s 1 − ξ1 2 ≤ TV ≤ TM.

Q(T)≥ 1 − ψ(TV ) and

1 −

logn ≤ V (T)≤ 1 + φ(TV ) where

2ξ

C[log(x τ ˜s)+ ξ] logn

φ(x)= min

2 x

,

and

C[1 + log(x τ ˜s)] logn

C′ x  +

ψ(x)= min

ξ logn for some constants C and C′ independent of n.

,

The exact forms of φ and ψ are chosen to make the proof more transparent. The important feature of the functions are that φ and ψ decrease for large x, providing better bounds whenever TV is large. Since we have no a priori bound for this cardinality, this will be crucial for later analysis. Furthermore, for any positive x and suﬃciently large value of n,

- (5.16) max{ψ(x),φ(x)}≤

1 √logn

. Proof. Since Q(I)≥ 1 − ξ logn (by (5.11)), we know that V (I)≥ Q(I)≥ 1 − ξ logn,

which immediately implies TV ≤ TM. Since YI ≥ 0, the upper bound (5.9) in the deﬁnition of Hξ can be applied to elements of T. Applying Lemma 5.11 to this set, we deduce that

- (5.17) V (T) log


q w + logV (T)− log

τ˜s  − 1 ≤ log

q w + ξ − 1.

TV

By deﬁnition, V (T) is at least 1 − 2ξ logn. Noting that log 1 −

−4ξ logn for all suﬃciently large n, we can conclude that

2ξ logn ≥

2ξ log(q w) logn +

τ˜s  ≤ ξ +

− 1 −

Cξ logn

2ξ logn

TV

log

.

We recall that q w ≤ n1−p 2+o(1), and therefore there exists a constant C such that

τ˜s  ≤ Cξ . Inverting the negative logarithm gives

−log

TV

TV ≥ τ˜s exp(−Cξ)≥ τ˜s(1 − Cξ)≥ τ˜s(1 − ξ1 2),

where the ﬁnal inequality holds for all suﬃciently small ξ, as required.

We prove the upper bound on V (T) by proving a bound that holds for all values of TV , and then improving it in the case TV < logn. We observe that the deﬁnition of the ordering of the XI’s implies that XTV is equal to the minimum of the set {X1,X2,...,XTV }, and thus

V (T) TV

XTV q ≤

- (5.18)


. Furthermore, by minimality of TV ,

V (T  {XTV })≤ 1 −

2ξ logn

.

Recall that τ˜s ≥ 2d (from (3.8)) and therefore, TV >(1 − ξ1 2)τ˜s implies that TV ≥ 2 for any ξ suﬃciently small. Since V (T)= V (T  {XTV })+ XTV q, we deduce that

1 −(2ξ) (logn) 1 − 1 TV ≤ 1 +

V (T)≤

TV −

2

2ξ logn

. Ignoring the negative contribution 2ξ logn gives the desired bound.

- 2 TWheneverV for all suﬃcientlyTV ≥ lognlarge, an explicitn. Thus,computationto completewillthe showboundthaton Vφ(TT)V,)=we may assume that TV < logn. We now return to (5.17). If V (T)≤ 1, we are done. Otherwise, V (T)logV (T) is positive, and thus


log(q w)− 1 + ξ log(q w)− log(TV τ ˜s)− 1

V (T)≤

log(TV τ ˜s)+ ξ log(q w)− log(TV τ ˜s)− 1 ≤ 1 +

= 1 +

C[log(TV τ ˜s)+ ξ] logn

,

where we use the upper bound TV ≤ TM and (5.12) to ensure that the denominator is bounded below by [(a 3)logn − 1]>(a 4)logn for all suﬃcently large n. This gives half the desired upper bound on V (T) under the assumption TV < logn.

The loewr bound on Q(T) will follow a similar strategy. We begin by noting that an algebraic manipulation will prove that, for any set W ⊂ T,

V (W) q

XJ −

Q(W)=

1 q2 I∈W

XI

.

J∈N˜I∩W

Let Z = I T, and observe that

Q(I)− Q(T)≤

1 q2 ⋅

XJ −

XI

XI

XJ

I∈I

I∈T

J∈N˜I∩I

J∈N˜I∩T

1 q2 ⋅

XJ +

=

XI

XI

XJ

I∈Z

I∈T

J∈N˜I∩I

J∈N˜I∩Z

We decompose the ﬁrst sum into

XJ =

XJ +

XI

XI

XI

XJ

I∈Z

I∈Z

I∈Z

J∈N˜I∩I

J∈N˜I∩Z

J∈N˜I∩T

=

XJ +

XI

XI

XJ ,

I∈Z

I∈T

J∈N˜I∩Z

J∈N˜I∩Z

where we can ﬂip the order of summation in the ﬁnal equality thanks to the symmetry of ρ. Substituting this in, we ﬁnd that

- (5.19) Q(I)− Q(T)≤


2 q2 I∈I

XI

XJ .

J∈N˜I∩Z

By ordering of the XI’s, we have that XI ≤ XTV for any I ∈ Z. Therefore, 1 q J∈N˜

N ˜I V (T)

XJ ≤

,

TV

I∩Z

where we reuse (5.18). Substituting this into (5.19), we see that

2 N ˜I V (I)⋅ V (T) TV

Q(I)− Q(T)≤

.

Thanks to Hξ, V (I) is uniformly bounded in n (by (5.10)) and Q(I) ≥ 1 − ξ logn (by (5.11)). The uniform bound on N ˜I from Lemma 5.1 proves half of the lower bound on Q(T).

Again, if TV ≥ logn, ψ(TV )= C′ TV + ξ logn for all suﬃciently large n. Thus, we may assume that TV < logn for the rest of the proof. Suppose that we were given the bound V (Z)≤ C[1 + log(TV τ ˜s)] logn. From (5.19), we konw that

C 1 + log Tτ˜V

Q(I)− Q(T)≤ 2V (I)⋅ V (Z)≤

s

,

logn

where we use (5.10) to replace V (I) by a uniform constant. Thus, it is suﬃcient to prove the upper bound on V (Z).

To do so, we return to (5.11), and apply Lemma 5.11 to T without ignoring the contibution of elements of Z. This allows us to deduce that

- (5.20)


V (T) log

τ˜s  − 1 +

q w + logV (T)− log

YI ≤ log(q w)− 1 + ξ .

1 q I∈Z

TV

Thanks to the upper bound on TV , we know that the bracketed term is positive and increasing in V (T). Since V (T)≥ 1 − 2ξ logn, some careful calculations imply that, for all suﬃciently large n and suﬃciently small ξ,

τ˜s  − 1 ≥ log(q w)− 1 − log

q w + logV (T)− log

V (T) log

TV

TV

τ˜s −

3ξ log(q w) logn

3ξ logn −

.

Substituting this into (5.20) gives that 1 q I∈Z

3ξ log(q w) logn ≤ Cξ + log

YI ≤ ξ +

3ξ logn + log

τ˜s  +

TV

TV τ˜s

,

for some uniform C and all suﬃciently large n. Another application of Lemma 5.11 — this time, to Z — implies that

qτ˜s w ⋅ TM  + V (Z)(logV (Z)− 1)≤ Cξ + log

V (Z)log

TV τ˜s

,

where we bound Z by TM. The function x[log(x)−1] is bounded below by −1 for any positive x; applying this bound to V (Z)[logV (Z)− 1] and rearranging the previous inequality algebraically, we ﬁnd that, for all suﬃciently large n

###  + 1 log[qτ˜s (w ⋅ TM)]

 + 1 (a 3)⋅ logn ≤

### Cξ + log Tτ˜V

C 1 + log Tτ˜V

Cξ + log Tτ˜V

≤

V (Z)≤

s

s

s

, where use (5.12) to get the penultimate bound. This completes the proof.

logn

Recall that, for any W ⊂ T, Q(W)≤ V (W)2. In a sense, the content of Lemma 5.13 is that this bound is nearly right for T. To make this precise, we deﬁne

PI(W)∶=

1 q J∈W,ρ(I,J)>s

XJ . Note that the sum is over indices whose distance exceeds s. Corollary 5.14. Assume Hξ holds, and that TV and T are deﬁned as above. Then, for all n suﬃciently large and ξ suﬃciently small,

XIPI(T)≤ 3φ(TV )+ ψ(TV ), where φ(⋅) and ψ(⋅) are deﬁned as in Lemma 5.13.

1 q I∈T

Proof. We observe that V (T)2 − Q(T)=

V (T) q

XIPI(T)+

1 q I∈T

,

where the additive factor of V (T) q comes from the fact that n2 − 2 n2 = n. By Lemma 5.13, we conclude that

XIPI(T)≤ V (T)2 − Q(T)

1 q I∈T

≤(1 + φ(TV ))2 −(1 − ψ(TV ))≤ 3φ(TV )+ ψ(TV ). This completes the proof.

- 5.6. Removing Lower Order Terms. Before proceeding, consider the situation in which we assume that both φ and ψ vanish, and that ξ = 0. This


implies that PI(TV ) must be zero for every I ≤ TV , since the sum in Corollary 5.14 is made up of non-negative terms. Thus, T would have diameter

- at most s. Thanks to the lower bound on TV in Lemma 5.13, the set would be a maximal clique set!


Of course, φ, ψ, and ξ are nonzero, so we cannot apply this argument to T directly. We further truncate the set to deal with this diﬃculty. Deﬁne

- (5.21) TP ∶= max k ≤ TV ∶ Xk ≥


ξq τ˜s

,

where we set TP = 0 if the set on the right is empty. We denote the set {1,...,TP} by P. The following lemma establishes bounds on V (P) and the sum of the YI’s in P. At the end of this section, we will use these bounds to deduce some geometric properties of P.

- Lemma 5.15. Assume that Hξ holds, and deﬁne TP and P as above. Then, for suﬃciently small ξ and suﬃciently large n,


1 − ξ1 2 < V (P)≤ 1 + φ(TV ) and

YI < V (P)(log(q w)− 1)+ ξ1 2 .

1 q I∈P

The stipulation on the sum of the YI’s in P is a slight (but essential) improvement on the naive inclusion bound given by (5.9) in the deﬁnition of Hξ. Proof. The upper bound on V (P) follows from the inclusion P ⊂ T and Lemma 5.13. Deﬁne

L1 ∶= I ∈ T ∶ XI <

ξq τ˜s log(TV ) and

L2 ∶= I ∈ T ∶

≤ XI <

ξq τ˜s log(TV )

ξq τ˜s

.

Clearly, L1,L2 and P form a partition of T. Proving the lemma is tantamount to proving good upper bounds on V (L1) and V (L2), as well as good lower bounds on the sum of the YI’s in both sets.

To bound V (L1), we ﬁrst need to bound PI(L1) from below for any I ∈ T. The worst case scenario is that the distance restriction removes the N ˜I largest elements of L1. Therefore,

ξ N ˜I τ˜s log(TV )

XJ > V (L1)−

PI(L1)≥ V (L1)−

1 q

N ˜I max J∈L1

.

Since PI(W)≤ PI(W′) whenever W ⊂ W′, we see that Corollary 5.14 implies that

XIPI(L1)≤ 3φ(TV )+ ψ(TV ).

1 q I∈T

Replacing PI(L1) with its minimum and recalling that N ˜I and τ˜s are uniformly bounded in n (by Lemma 5.1), we see that

V (T)< 3φ(TV )+ ψ(TV ).

V (L1)−

Cξ log(TV )

Using the (very suboptimal) lower bound of 1 2 for V (T) (which follows from Lemma 5.13 and n suﬃciently large), we conclude that

- (5.22) V (L1)< 6φ(TV )+ 2ψ(TV )+

Cξ log(TV )

.

for some C independent of n. Repeating this analysis with L2 yields the inequality

V (L2)< 6φ(TV )+ 2ψ(TV )+ Cξ . Since both φ(x) and ψ(x) are bounded above by 1 (logn)1 2 (from (5.16)) and TV >(1 − ξ1 2)τ˜s (by Lemma 5.13), we get

- (5.23) max{V (L1), V (L2)}< Cξ. Combining the previous bounds and the lower bound on V (T) from Lemma

- 5.13, we ﬁnd that, for all suﬃciently small values of ξ,


- (5.24) V (P)= V (T)− V (L1)− V (L2)

≥ 1 − 2Cξ −

2ξ logn ≥ 1 − ξ1 2 .

This establishes the lower bound on V (P). We now turn to bounding ∑I∈P YI. Suppose that

- (5.25)


YI > V (Li)(log(q w)− 1)− 2ξ2 3. We observe that (5.24) and Lemma 5.13 imply that

1 q I∈L

i

V (P)+(2ξ) logn ≥ 1 − V (L1)− V (L2).

By inclusion, we may apply (5.9) to T, partition the elements into P, L1, and L2 and substitute the above bounds to get the following set of deductions

YI ≤(log(q w)− 1)+ ξ −

1 q I∈P

1 q I∈L

YI <(1 − V (L1)− V (L2))(log(q w)− 1)+ 4ξ2 3 + ξ < V (P)(log(q w)− 1)+

1∪L2

logn (log(q w)− 1)+ 5ξ2 3 < V (P)(log(q w)− 1)+ ξ1 2 ,

2ξ

where the ﬁnal inequality holds for suﬃciently small ξ. Thus, we only need to show (5.25).

By applying Lemma 5.11 to Li, we know that 1 q I∈L

YI ≥ V (Li)(log(q w)− 1)+ V (Li)logV (Li)− V (Li)log( Li ),

- (5.26)


i

where we ignored the positive term V (Li)logτ˜s. Using (5.23), we ﬁnd that V (Li)logV (Li) is bounded below by Cξ log[Cξ]>−ξ2 3.

Controlling V (L1)log( L1 ) is quite straightforward: since inclusion implies that L1 ≤ TV , we can use (5.22) to see that, for suﬃciently large n,

log(TV ) ≤ max

V (L1)log( L1 )≤ 6φ(TV )+ 2ψ(TV )+

Cξ log(TV )

2≤x≤TM{logx ⋅(6φ(x)+ 2ψ(x))}+ Cξ,

where we use the fact that 2 ≤ τ˜s(1 − ξ1 2) ≤ TV ≤ TM. Recalling the deﬁnitions of φ and ψ, we have that

6C[log(x τ ˜s)+ ξ] logn

6φ(x)+ 2ψ(x)= min

12 x

,

2C[1 + log(x τ ˜s)] logn

2C′ x  +

+ min

ξ logn

,

,

and thus, it can be shown that, for some (diﬀerent) uniform constant C,

logx(1 + logx) logn

logx ⋅(6φ(x)+ 2ψ(x))≤ C ⋅ min

logx x  +

ξ logx logn

,

.

We wish to prove a uniform, x-independent bound on the minimum above (for any x ≥ 2). The ﬁrst function in the minimum is increasing; meanwhile, the second function in the minimum is larger than the ﬁrst one on [2,e] (for all suﬃciently large n), and is a decreasing function of x on (e,∞). Thus, for any 2 ≤ x ≤ TM, the minimum is bounded above by logy(1+logy) logn for any y that satisﬁes (1+logy) logn ≥ 1 y. The value y = logn is one such

value. Combining the two estimates gives

C[loglogn +(loglogn)2] logn +

logx ⋅(6φ(x)+ 2ψ(x))≤

ξ logx logn

. Thus, we ﬁnd that

- (5.27)


C[loglogn +(loglogn)2] logn +

log(x)⋅(6φ(x)+ 2ψ(x))≤

ξ logTM logn

max

.

2≤x≤TM

Using (5.8) to bound TM, we deduce that, for all suﬃciently large n, V (L1)log( L1 )< Cξ for some uniform constant C; this, in turn, is bounded by ξ2 3 for all sufﬁciently small ξ.

To control V (L2)log( L2 ), we must be slightly more careful. For any I ∈ L2, we know that

PI(L2)≥

1 q J∈L

XJ

min

J∈L2

2,ρ(I,J)>s

≥

ξ τ˜s log(TV ) ≥

J∈L2,ρ(I,J)>s

ξ( L2 − N˜I ) τ˜s log(TV )

,

where we use the lower bound deﬁning L2. By inclusion, PI(L2)< PI(T), and Corollary 5.14 allows us to conclude that

ξ( L2 − N˜I ) τ˜s log(TV )

 ≤

V (T) 

XIPI(L2)

1 q I∈T

≤ 3φ(TV )+ ψ(TV ). Solving for L2 , we deduce that

τ˜s ξ ⋅ log(TV )⋅(6φ(TV )+ 2ψ(TV )),

L2 ≤ N˜I +

where we bound V (T) from below by 1 2 by Lemma 5.13. Referring back to (5.27), we see that

Cτ˜s ⋅[loglogn +(loglogn)2] ξ logn +

L2 ≤ N˜I +

τ˜s logTM logn

.

Using (5.8) and Lemma 5.1 to bound N ˜I and τ˜s from above, this proves that L2 is uniformly bounded in n. Appealing to (5.23) a ﬁnal time,

V (L2)log( L2 )< Cξ < ξ2 3. This completes the proof.

As promised, we now show that P has the desired geometric properties:

- Lemma 5.16. For all n suﬃciently large and ξ suﬃciently small, diam(P)≤ s and TP > τ˜s 1 − ξ1 3 ,

that is - the set P is a ξ1 3-almost maximal clique set. Proof. Assume that there exists a pair of indices I∗,J∗ ∈ P such that ρ(I∗,J∗)> s. Then,

1 q I∈T

XIPI(T)≥

XI∗XJ∗ q2 ≥

ξ2 τ˜s2

,

where the ﬁnal bound is from the deﬁnition of P. By Corollary 5.14, we know the lefthand quantity cannot exceed 3φ(TV )+ψ(TV ), which is bounded above by 4 (logn)1 2 - a clear contradiction for all suﬃciently large n. Thus, the diameter P is at most s.

Combining Lemmas 5.11 and 5.15 gives V (P)(log(q w)− 1)+ V (P) logV (P)− log

TP

τ˜s < V (P)(log(q w)− 1)+ ξ1 2 ,

and therefore

TP > τ˜s ⋅ V (P)exp −

ξ1 2 V (P)

 > τ˜s ⋅ V (P) 1 −

ξ1 2 V (P)

using the standard estimate e−x ≥ 1−x. Combining this with the lower bound on V (P) from Lemma 5.15 forces

TP > τ˜s(1 − ξ1 3)

for all suﬃciently large values of n and small values of ξ.

5.7. Convex Analysis. We are nearly done with the proof: all that remains is to show that, for most I ∈ P, XI is close to q τ ˜s, and then to formally prove the theorem. The essential additional information we are now armed with is an upper bound on TP — namely τ˜s, as P has diameter at most s, and τ˜s is the largest possible cardinality for such a set of indices.

- Lemma 5.17. Let P be as above, and assume that Hξ holds. Deﬁne


q − 1 < ξ1 5 and C = P B. Then, for all suﬃciently large n and ξ suﬃciently small,

B ∶= I ∶ 

XIτ˜s

B >(1 − 10ξ1 10)τ˜s, C < 9ξ1 10τ˜s, and V (C)< 10ξ1 10.

Proof. We consider the Taylor expansion of YI around the value q τ ˜s. Explicitly, we let f(x)= x(log(x D)− 1)+ D, and by Taylor’s theorem,

f′′(L(XI)) 2

2

q τ˜s + f′

YI = f(XI)= f

XI −

q τ˜s +

XI −

q τ˜s

q τ˜s

explicitlywhere L(XandI) simplifyingis some numberalgebraically,betweenweXIseeandthatq τ ˜s. Diﬀerentiating f(x)

2

YI = D −

q τ˜s + XI log(q w)+

XI −

1 2L(XI)

q τ˜s

.

Next, we sum over P and use the upper bound on ∑I∈P YI from Lemma 5.15 to deduce that

2

q τ˜s + XI log(q w)+

D −

XI −

1 2L(XI)

1 q I∈P

q τ˜s

≤ V (P)(log(q w)− 1)+ ξ1 2 . We ignore the positive term D on the lefthand side. From Lemma 5.16, the diameter of P is at most s, and hence TP ≤ τ˜s. Thus,

2

XI −

τ˜s − V (P)+ ξ1 2 ≤ 2ξ1 2 , where the ﬁnal inequality follows thanks to the lower bound on V (P) from

≤

1 q I∈P

1 2L(XI)

q τ˜s

TP

- (5.28)


- Lemma 5.15. Now, deﬁne


- W1 ∶= I ∈ P ∶ XI ≥(1 + ξ1 5)q τ ˜s

and

- W2 ∶= I ∈ P ∶ XI ≤(1 − ξ1 5)q τ ˜s .


We recall that C = P B = W1 ∪ W2. On W1, the function 1 L(XI) is bounded below by 1 XI. Thus, (5.28) implies that

2

W1 q ⋅ min

XI −

≤ 2ξ1 2 .

- 1

- 2XI


q τ˜s

I∈W1

The function x (x − q τ ˜s)2 (2x) is strictly increasing on the interval [(q τ ˜s)(1 + ξ1 5),∞), and always convex. Using the ﬁrst fact, we ﬁnd that

ξ2 5 2˜τs ⋅(1 + ξ1 5)

 ≤ 2ξ1 2.

W1 ⋅ 

This implies that W1 < 5ξ1 10τ˜s. To control V (W1), we apply (the standard version of) Jensen’s inequality to the convex function x  (x − q τ ˜s)2 (2x). Algebraically manipulating the resulting expression gives

2

2

V (W1)−

≤

XI −

≤ 2ξ1 2,

1 2V (W1)

1 q I∈W

- 1

- 2XI


q τ˜s

W1 τ˜s

1

where the ﬁnal bound follows from (5.28). Since the lefthand side is increasing in V (W1) whenever V (W1)≥ W1 τ ˜s, we can conclude that

V (W1)≤ W1 τ ˜s + 2ξ1 4 < 6ξ1 10.

For W2, we can bound 1 L(XI) from below by τ˜s q. A ﬁnal appeal to (5.28) gives that

2

< 2ξ1 2 .

W2 q ⋅ min

XI −

τ ˜s 2q

q τ˜s

I∈W2

We can bound the minimum from below by assuming that some XI realizes the upper bound that deﬁnes W2. In this case, it is immediate that W2 ≤ 4ξ1 10τ˜s. Finally, XI ≤ q τ ˜s for each I ∈ W2, and therefore, V (W2)< 4ξ1 10. Putting these terms together, we ﬁnd that

V (C)= V (W1)+ V (W2)< 10ξ1 10. We also see that

C = W1 + W2 < 9ξ1 10τ˜s. The lower bound on B follows from

B = TP − C > τ˜s(1 − ξ1 3)− 9ξ1 10τ˜s > τ˜s 1 − 10ξ1 10 , where the penultiamte inequality was proved in Lemma 5.16.

We have completed the proof of the diﬃcult assertion in Theorem 3.1; all that is left is to ensure the second stipulation holds. Proof of Theorem 3.1. We recall the deﬁnition of Gn,δ˜(ε˜): there must a pair of sets B and C such that

- a)B is ε˜-almost maximal clique set such that I ∈ B implies τ ˜sXI

q − 1 < ε,˜

- b) C satisﬁes C < ε˜τ˜s and V (C)< ε,˜


and

c) whenever J ∈(B ∪ C)c,

ε˜⋅ q τ˜s

XJ <

.

We set ξ =(ε˜ 10)10. Then, whenever Hξ holds, the sequence of assertions given by Lemmas 5.13, 5.15, 5.16 and 5.17 assure us that, for n sufﬁciently large and ε˜ suﬃciently small (interpreted according to our stated conventions), the sets B and C of Lemma 5.17 satisfy the ﬁrst and second conditions of Gn,δ˜(ε˜).

To show the ﬁnal condition holds, we must show that all elements of T P

are small. If TV > TP, then XTP+1 < ξq τ ˜s < εq˜ τ ˜s. This implies the upper bound holds for every element outside of P, thanks to the ordering of the

elements. We are left with the scenario in which TV = TP. By deﬁnition (recall

- (5.15) and (5.21)), this means that P = T, and therefore TV ≤ τ˜s. Formally,


it is still possible that XTV +1 ≥ ξq τ ˜s. By Lemma 5.11 and Lemma 5.13, we deduce that

τ˜s  − 1 ≥ 1 −

YI ≥ V (T) log(q w)+ log(V (T))− log

1 q I∈T

TV

log(q w)− 1 −

2ξ logn

3ξ logn

,

where the contribution of the term including the logarithm of TV is nonnegative and thus can be safely ignored. Note that, since we assumed q > 3w, the righthand side above is positive for all suﬃciently large n. Therefore,

- (5.9) implies that 1


YI ≤[log(q w)− 1 + ξ]− 1 −

log(q w)− 1 −

3ξ logn 4ξ log(q w)

2ξ logn

q I∈I T

logn + ξ ≤ Cξ .

As before, the ﬁnal inequality follows because log(q w)≤ C logn for some C. Suppose XTV +1 ≥ εq˜ τ ˜s = 10ξ1 10q τ ˜s. Then we ﬁnd that YTV +1 = XTV +1 (log(XTV +1 D)− 1)+ D

≥ ξq log(q w)+ log(10ξ1 10)− 1 + D .

If we divide through by q, we ﬁnd that this expression still grows with n, whereas the earlier upper bound is uniformly bounded. This is a contradiction, and we get the upper bound XTV +1 < εq˜ τ ˜s.

The above computation implies that any conﬁguration in H(ε˜ 10)10 is also

in Gn,δ˜(ε˜). Taking complements and intersecting with Ln(δ˜), we conclude that

P[Gn,δ˜(ε˜)c ∩ Ln(δ˜)]

≤ P[H(cε˜ 10)10 ∩ Ln(δ˜)]≤ 3exp(−q[log(q w)− 1 +(ε˜ 10)10 2]), where the ﬁnal inequality is Proposition 5.12.

6. Moving from Discrete to Continuous

This section has three parts: ﬁrst, we prove several estimates that show the discrete setting of the s-graded model approximates the continuous geometry of Td. We then prove a proposition relating the random geometric graph structural event Fn(ε) with Gn,δ˜(ε˜), given by the structure theorem 3.1 on the s-graded model, with appropriately chosen parameters. The second part is probabilistic, where we ﬁnd a tight lower bound on the event that the number of edges in the random geometric graph exceeds its mean. We then assume Theorem 3.1 and deduce Theorem 2.1 by choosing δ˜ and ε˜judiciously and employing a correlation inequality.

- 6.1. Geometric Lemmas. Recall that (as in (5.2)), for any K ⊂ Td, we deﬁne R(K) and O(K) to be the maximal (resp. minimal) subsets of T such that


- (6.1) U(R(K))⊂ K and K K′ ⊂ U(O(K)) ,


where K′ is some subset of K of Lebesgue measure 0. Recall that λ(⋅) will be used to denote Lebesgue measure of sets. We begin by showing that this operation does not alter the measure of convex subsets S of diameter at most

- r by very much. Formally:


Proposition 6.1. Fix ε > 0, and let S be a convex subset of diameter at most 2r. Then, there exists an s0 that depends only on ε, the dimension, and the choice of norm, such that whenever s > s0, the inner hull R(S) satisﬁes

ε2τ

64 < λ U(R(S)) ≤ λ(S) Similarly, the corresponding inequality

λ(S)−

ε2τ

λ(S)≤ λ U(O(S)) < λ(S)+

64 hold for the outer hull O(S).

Note that, for any ﬁxed S, this result follows from the continuity of Lebesgue measure. The essential part of this proposition is that the choice of s0 is uniform for all convex subsets S that satisfy the assumptions of the proposition.

Instead of proving the proposition directly, we consider the following minor modiﬁcation:

- Lemma 6.2. Let S be a convex set as in Proposition 6.1. Deﬁne (∂S)l ∶={y ∶ ∂S − y ≤ l} ,


- where B −x is shorthand for infb∈B b−x for any set B. Then there exists an s0, depending on ε, the dimension, and the norm, such that s > s0 implies


ε2τ 64

λ (∂S)ς m <

, where ς is the diameter of a unit square (as in (5.3)). This lemma implies Proposition 6.1, since

S ⊂ U(R(S))∪(∂S)ς m and

U(O(S))⊂ S ∪(∂S)ς m . Taking the Lebesgue measure of both sides and using subadditivity gives the two nontrivial bounds in Proposition 6.1.

Proof of Lemma 6.2. Heuristically, the volume of (∂S)ς m should be commensurate with the product of ς m with the surface area of S. Since S has diameter at most 2r and is a convex set (and therefore its boundary cannot be too convoluted), this surface area ought to be bounded above by Crd−1. To formalize this loose heuristic, we turn to the tools of geometric measure theory. Although this approach is standard in that ﬁeld, we include a detailed proof for completeness.

Consider a function f ∶ Rd → R that is Lipschitz with respect to the Euclidean distance, and a Borel set A. The Euclidean coarea formula [15, pg. 248] states that, with the functions as above,

∞ −∞

Hd−1 A ∩ f−1(y) dy ,

Df(x) 2dx =

A

where  ⋅ 2 is the Euclidean norm, and Hd−1 is the Hausdorﬀ measure on the surface (eﬀectively the surface area) and Df is the gradient of f, which exists since f is almost everywhere diﬀerentiable.

The natural choice for our analysis is f(x) = ∂S − x . We begin by proving that f is Lipshitz with respect to the Euclidean norm. We recall the classical fact that all norms are equivalent in ﬁnite dimensional space, i.e. there exists two positive constants c and C such that, for all x and y,

c x − y ≤ x − y 2 ≤ C x − y . Pick two points x and y, and let a ∈ ∂S be the point such that f(x)= x−a (this point exists because ∂S is closed). Then

f(y)− f(x)≤ y − a − x − a ≤ x − y ≤ C x − y 2 . Similarly, f(x)− f(y)≤ C x − y 2.

Thus, f is diﬀerentiable almost everywhere. Pick an x where the function is diﬀerentiable, and let a be as before. Then, for any t ∈(0,1),

f(x + t(a − x))≤ f(x)− t a − x ,

by the properties of norms. Subtracting f(x) from both sides, dividing by t and letting t → 0, we get

a − x,Df ≤− a − x ,

where  ⋅,⋅  is the Euclidean inner product (or in this case, the directional derivative). Applying the Cauchy-Schwarz inequality, we conclude that

a − x ≤ a − x 2 Df 2 , which implies, by the equivalence of norms, that

a − x

a − x 2 ≥ c. Letting A ={x ∶ f(x)≤ ς m}, we apply the Euclidean coarea formula to deduce that

Df 2 ≥

Hd−1 ({y ∶ ∂S − y = z})dz ,

- (6.2) λ (∂S)ς m ≤ C


ς m 0

- where C is some (possibly diﬀerent) universal constant. Note that, for sufﬁciently small z and T convex, the set {y ∶ ∂T − y = z} has two connected components: one inside T and the other outside of it. We wish to show that both are boundaries of convex sets. The outer one is the boundary of the aﬃne sum of S and the ball of radius z, which is known to be convex. The internal one is the boundary of


S(z) ∶={x ∶ x ∈ S, ∂S − x ≥ z}.

We claim that this set is also convex: it if it weren’t, we could ﬁnd x,y ∈ S(z) such that w = tx +(1 − t)y ∈ S(z) for some t ∈(0,1). Let v be the minimal length vector such that w + v ∈ ∂S. Then, since v < z by deﬁnition, we can ﬁnd an ε suﬃciently small such that w +(1 + ε)v ∈ S, while x +(1 + ε)v,

- y +(1 + ε)v are both in S, contradicting convexity of S. We complete the proof using Cauchy’s surface area formula [37, pg. 55]:


for any convex S,

Hd−1(∂S)= Cd

λd−1 S u⊥ du

u∈Sd−1

where Sd−1 is the d − 1-dimensional unit ball in Rd, λd−1 is the d − 1dimensional Lebesgue measure, S u⊥ is the projection of S onto the d − 1

dimensional subspace perpendicular to u, and Cd is a constant used to ensure the Hausdorﬀ and Lebesgue measures are compatible.

We apply this formula to the two convex sets (S)z and S(z) (discussed

above)y = z}whose. The boundariesprojection ofgiveeitherthe twoset ontoconnecteda d −components1-dimensionalof subset{y ∶ ∂Shas− diameter at most 2(r+z), and therefore, by the triangle inequality, is included in some ball of diameter 4(r + z). Thus, inclusion implies that

λd−1  (S)z u⊥ ≤ Cd(r + z)d−1 and λd−1 S(z) u⊥ ≤ Cd(r + z)d−1 for some constant Cd. Substituting this into (6.2) gives

r+(ς m) r

ud−1du = C[(r + ς m)d − rd]. Increasing s, we can ensure that [1+ς (rm)]d < 1+(2dς) (rm), and therefore, λ (∂S)ς m ≤

λ (∂S)ς m ≤ C

Crd−1 m ≤

Cτ rm <

Cτ s − r

, where the value of C may change from one inequality to the next. Increasing

- s, we get the desired result.


Next, we prove a lemma that proves that almost maximal clique sets are, essentially, discretized versions of balls of diameter r:

Lemma 6.3. Fix ε > 0. Then there exists s0 such that, for any s > s0, r suﬃciently small, and s−1 20-almost maximal clique set B in the s-graded

model, there exists a set of indices H ⊂ T with H < ε ⋅ τ˜s and B, a ball of diameter r in Td, such that

B ⊂ U(B ∪ H) and U(B)⊂(B)εr.

The choice of the term s−1 20 is somewhat arbitrary — the above result will follow for any function which vanishes as s grows. We framed the lemma as we did since the function s−1 20 is used in the proof of Theorem 2.1 below.

Proof. To prove this lemma, we go through the abstract framework of Hausdorﬀ convergence of subsets of a metric space. Consider an abstract metric space X imbued with metric ι, and, for any S ⊂ X, deﬁne the l-fattening of S as before, using the metric ι to measure distance. For any two A,B ⊂ X, the Hausdorﬀ distance is deﬁned as

ιH(A,B)∶= inf{l ∶ A ⊂(B)l, B ⊂(A)l}. If X is compact in the topology deﬁned by ι, the space of closed subsets of X makes a compact space with respect to this metric [36, page 294].

Recall that Ts ={1,2,...,m}d is a set of indices, where we add the subscript s to emphasize the dependence on this variable. Let {Bs}s≥2 be a sequence of s−1 20-almost maximal clique sets, where Bs ⊂ Ts. Deﬁne A to be some ball of radius r(1 + 2ς) in Td. For any set S of diameter of at most r(1 + 2ς), there exists a translate of S which lies completely in A – this can be done by simply translating any point of S to the center of A. Thus, there is a translate of U(Bs) that is a subset of A, since

2ς m ≤ r 1 +

diam(U(Bs))≤ r +

s − r < r(1 + 2ς), whenever s is suﬃciently large and r suﬃciently small.

2ς

Let A˜ and B˜s be the sets A and the translate of U(Bs) that are inside

- A, scaled by 1 r and embedded in Rd (which is possible as long as r is suﬃciently small to not “notice” the torroidal geometry of Td). Thus, A˜ is a ball of radius 1 + 2ς. By Lemma 5.1, we know that


τ(1 − s−1 20) rd =

ν(1 − s−1 20) 2d

, and λ(B˜s)≥

diam(B˜s)≤ 1 +

C s

, with the ﬁnal inequality being the deﬁnition of τ.

Since all the B˜s are closed sets embedded in a single compact metric space (namely, A˜), we can extract a subsequence B˜sk which converges to some set B˜ in the Hausdorﬀ metric. Passing to the limit, we see that B˜ must have diameter of at most 1 and measure at least ν 2d. Quoting the isodiametric inequality again [6, pg 94],

d

diamB˜ 2

λ(B˜)≤ ν

.

where equality holds if and only if B˜ is a ball of diameter 1. This implies that B˜ is, in fact, the ball of diameter 1 (up to sets of measure zero). Indeed, if

we take an arbitrary subsequence of {B˜s}, we can extract a convergent subsubsequence whose limit will have diameter 1 and measure ν 2d — meaning any sub-subsequential limit is some ball of diameter 1. Letting B be the set of all balls of diameter in A, we ﬁnd that

ιH(B˜s,B˜)= 0.

lim

### inf

s→∞

B˜∈B

Therefore, there is an s0, such that, for any s > s0, there exists some ball B˜ ∈ B such that

ιH(B˜s,B˜)< ε (16d).

Scaling by r, we ﬁnd that, for any s > s0, there is a ball B of diameter r in Td, such that

B ⊂(U(Bs))εr (16d) and U(Bs)⊂(B)εr (16d). The second statement implies the required inclusion of U(B) in a (B)εr. For the other direction, we note that (U(Bs))εr (16d) ⊂(B)εr 8d. Set H = O(Bεr 8d)  Bs. Since (B)εr 8d is convex, we can use Proposition 6.1 and

- Lemma 5.1 to ensure that


d

O (B)εr 8d  ≤ md ⋅ τ 1 +

+ ε2 64 < τ˜s(1 + ε 2)

ε 4d

where the ﬁnal inequality holds for suﬃciently large s and suﬃciently small ε. Bs has cardinality at least τ˜s(1−s−1 20); if s0 is suﬃciently large to ensure s−1 20 < ε 2, we ﬁnd that H < ετ˜s, and inclusion guarantees that

B ⊂ U(Bs ∪ H). This completes the proof.

- 6.2. Relating the s-Graded Model and Random Geometric Graph Structure Theorems. Using the geometric information derived in the previous section, we wish to prove the following proposition:


Proposition 6.4. There is some ε0 > 0 such that the following holds for any ε < ε0. Take any δ > 0 and δ˜ ∈[(1−ε 16)δ,δ]. Let Fn(ε) and Gn,δ˜(s−1 20) be the events described in Theorems 2.1 and 3.1, respectively. Then, there exist n0 and s0 depending only on ε and δ, such that if n ≥ n0 and s ≥ s0, then

Gn,δ˜(s−1 20)⊂ Fn(ε). Proof. Set ε˜= s−1 20 and s0 and n0 to be the suﬃciently large to ensure that

- Lemma 5.1 holds for any s > s0 and n ≥ n0 (further conditions on s may be


imposed on later in the proof). Assume Gn,δ˜(ε˜) occurs, and let B and C be the sets described in Theorem 3.1. Then, by deﬁnition,

- (6.3)

τ ˜sXI q − 1 < ε˜ ∀I ∈ B,

- (6.4) C < ε˜⋅ τ˜s and I∈C


XI < εq,˜

and

- (6.5) XI <

εq˜ τ˜s ∀I ∈ B ∪ C.

Since the above bounds are in terms of q, whereas Fn(ε) is deﬁned using √2δµ, we begin by bounding √2δµ q from above and below. δ˜ ≤ δ by deﬁnition, and µ ≥ µ˜s(1 + C s)−1 by Lemma 5.1. Therefore,

√2δµ

q =

δµ δ˜µ˜s ≥ 1 +

C s

−1 2

≥(1 − ε˜),

where the ﬁnal inequality holds for all s suﬃciently large. Similarly, µ ≤ µ˜s and δ˜ > δ(1 − ε 16) implies that

√2δµ

q =

δµ δ˜µ˜s ≤ 1 −

ε 16

−1 2

≤ 1 + ε 8,

Putting this together, we see that, for all suﬃciently large s,

- (6.6) (1 − ε˜)≤

√2δµ

q ≤ 1 + ε 8.

We now set s to be suﬃciently large so that, when we apply Lemma 6.3 to B to produce B, a ball of radius r, and H ⊂ T with B ⊂ U(B∪H), we can be certain that H <(ε 8)⋅ τ˜s and that B ⊂(B)(νε2r) (d⋅2d+3) (the slightly odd constants are chosen to make later computations simpler). We also require that ε˜ < ε2 16. Our goal is to show that B will satisfy the conditions of Fn(ε).

For any S ⊂ Td, it is straightforward to see that

I∈R(S)

XI ≤ χ(S) ≤

I∈O(S)

XI .

To prove the ﬁrst condition of Fn(ε), it is suﬃcient to show that, for any convex S ⊂ B,

I∈R(S)

XI > 

λ(S) τ − ε 2δµ and

I∈O(S)

XI < 

λ(S)

τ + ε 2δµ. For the upper bound, we use Proposition 6.1 and Lemma 5.1 to see that

O(S) = mdλ(U(O(S)))< 

λ(S) τ +

ε2 64

mdτ ≤ 

λ(S) τ +

ε2 64

τ ˜s. We also know that, for any W ⊂ T,

- (6.7) I∈W


W (1 + ε˜) τ˜s

XI ≤

XI + W ⋅ max

XI < ε˜+

I ∈C

I∈C

q,

using (6.3), (6.4), and (6.5). Applying this to O(S) gives that

λ(S) τ +

ε2 64 (1 + ε˜) q

XI < ε˜+ 

I∈O(S)

λ(S) τ +

1 + ε˜ 1 − ε˜

ε2 64 ⋅

≤ 

ε˜ 1 − ε˜ + 

2δµ,

where the ﬁnal inequality is (6.6). Since λ(S) τ ≤ 1 (as S ⊂ B) and ε˜< ε2 16, the righthand side is smaller than [λ(S) τ+ε]

√2δµ for all ε suﬃciently small,

- as required.


To get a lower bound on the sum of the XI’s in R(S), we observe that S ⊂ B implies that R(S)⊂ B ∪ H, and therefore,

R(S)∩ B ≥ R(S) − H

ε ⋅ τ˜s 8 ≥ 

λ(S) τ −

ε2 64

mdτ −

> 

λ(S

ε2 64(1 + ε˜)

(1 + ε˜)τ −

−

ε 8

τ ˜s,

using Proposition 6.1 and Lemma 5.1. By deﬁnition, XI ≥[q(1 − ε˜)] τ˜s for any I ∈ B, and therefore

XI >

XI

I∈R(S)

I∈R(S)∩B

1 − ε˜ 1 + ε˜

λ(S) τ −

ε2 64 −

>

ε 4

q

1 − ε˜ (1 + ε˜)(1 + ε 8)

λ(S) τ −

ε2 64 −

>

ε 4

2δµ.

Reusing the bounds λ(S)≤ τ and ε˜ < ε2 16 gives that, for all ε suﬃciently small, the ﬁnal lower bound is smaller than [λ(S) τ − ε]

√2δµ, as required.

Next, let S′ be a convex set disjoint from B with diameter at most r and λ(S′)> ετ. A slightly more involved version of (6.7) gives that

XI + O(S′)∩ B ⋅ max

XI + O(S′)∩(B ∪ C)c ⋅ max

XI <

### XI

I∈B

I∈(B∪C)c

I∈C

I∈O(S′)

O(S′)∩ B ⋅(1 + ε˜) τ˜s +

O(S′)∩(B ∪ C)c ⋅ ε˜ τ˜s

≤ ε˜+

q.

Since S′ ∩ B = , we know that U(R(S′))∩ B = . We have assumed above that B ⊂(B)(νε2r) (d⋅2d+3), and therefore

U(R(S′)∩ B)⊂(B)(νε2r) (d⋅2d+3) B.

Taking the measure of both sides and multiplying by md to get cardinality bounds, we ﬁnd that

d

νε2 d2d+3

ε2mdτ

R(S′)∩ B ≤ mdrd 1 +

4 ≤ ε2τ˜s 4. Thus,

− 1 <

O(S′)∩ B ≤ O(S′)  R(S′) + R(S′)∩ B ≤(ε2 32 + ε2 4)τ˜s <(ε2 2)τ˜s,

using Proposition 6.1 to bound the diﬀerence between the inner and outer hulls of the convex set S′. Bounding O(S′)∩(B ∪ C)c by O(S′) , using inequality (6.6) to move from q to √2δµ, and appealing to Proposition 6.1 one ﬁnal time, we ﬁnd that

λ(S′) τ +

ε2(1 + ε˜) 2 + 

ε2 32

XI < ε˜+

ε ˜ q

I∈O(S′)

√2δµ τ

λ(S′)⋅

2ε2τ 3λ(S′)

ε2τ 32λ(S′)

ε ˜ (1 − ε˜)−1 ⋅

≤ 

+

+ 1 +

ετ˜ λ(S′)

.

Since λ(S′)> ετ by assumption, and ε˜ < ε2 16, the product of bracketed term and (1−ε˜)−1 is bounded by ε for all suﬃciently small values of ε. This completes the proof.

- 6.3. Theorem 3.1 implies Theorem 2.1. The next lemma establishes a lower bound on the event { E >(1 + δ)µ} — the conditioning event in Theorem 2.1


- Lemma 6.5. Fix δ > 0, and let Hn(δ)∶={ E >(1 + δ)µ}. Then, setting


- z = max{p 4,3p 4 − 1 2}, there exists n0 such that n > n0 implies that


√2δµ

P[Hn(δ)]≥ exp − 2δµ log

n ⋅ τ  − 1 − Cnz logn , where C is an absolute constant independent of n and δ. Proof. Fix B, a ball of diameter r, and let H′ be the event that there are

- at least √2δµ + nz vertices in B. Since the number of vertices in B is a Poisson random variable of mean nτ, we can get very straightforward lower bounds on the probability of H′:


P[H′]≥ P[Poisson(nτ)=  2δµ + nz ]

√2δµ+nz

exp(−nτ)⋅(nτ)

√2δµ + nz )!

=

( 

. By Stirling’s approximation, it follows that, for suﬃciently large n, P[H′]≥ exp −nτ −  2δµ + 2nz log

√2δµ + nz

nτ  − 1 − C logn ,

nforz logsomen <<universal constant C. Thanks to our judicious choice of z, nτ <<

√2δµ; therefore, by increasing n we can ﬁnd a C independent of n that guarantees

- (6.8) P[H′]≥ exp − 2δµ log

√2δµ

n ⋅ τ  − 1 − Cnz logn .

If H′ occurs, there exists a clique with at least δµ+nz√δµ edges in it (since 0 < z < p 2, this quantity is a lower bound for the number of edges in a clique of √2δµ+nz vertices for all suﬃciently large n). Conditional on H′, Hn(δ) occurs if the number of edges with at most one endpoint in B exceeds µ−nz√δµ. Let E ′ be the number of edges with no endpoints in B. Letting 1i,j be the indicator of an edge between vertices i and j, we can see that

E( E ′)= E

N 2

E(11,2 ⋅ 1v1,v2 ∈B N) 

=

n2 2

P({ v1 − v2 ≤ r}∩{v1,v2 ∈ B}),

where N is the total number of point in the torus, as before, and the probability measure in the second equality is given by the uniform process. For notational convenience, let 1Bi,j be the indicator of the event { vi − vj ≤ r}∩{vi,vj ∈ B}, and µB be its expectation under the measure of the uniform process (by symmetry, this is independent of the indices i and j). If v1 is at a distance greater than r from B, the second condition holds trivially. For a ﬁxed B, the probability that v1 is within distance r of B is a constant multiple of rd. Thus,

µB ≥(1 − Crd)νrd ,

for some C that depends only on the norm and the dimension. Thus, the expected value of E ′ is bounded below by µ(1−Crd). Therefore, by deﬁnition of z, we have the inequality

- (6.9) µ − δµ ⋅ nz ≤ E[ E ′]−


√δµ ⋅ nz 4 We now need a variance estimate for E ′:

Var( E ′)= E(Var( E ′ N))+ Var(E( E ′ N)).

We have already calculated the expectation of E ′ given N above; since µB does not depend on N, we deduce that

Var(E( E ′ N))=(µB)2Var

N 2

.

A standard calculation will show that the variance of N2 is n3+n2 2. Meanwhile,

µB ≤ P( v1 − v2 ≤ r)= νrd . Combining these facts gives

Var(E( E ′ N))≤ Cr2dn3 ,

for some universal constant C.

Next, we estimate the expression E(Var( E ′ N)). We can write this variance as

Var( E ′ N)= E

[1Bi,j − µB] 

2

N .

1≤i<j≤N

We now decompose this sum into three sums by distributing the square: one sum over pairs of the form (i,j),(k,l) with four distinct indices, one with pairs of the form (i,j),(i,k) where one index repeats, and the ﬁnal over perfect squares of terms involving (i,j). The expectation of the ﬁrst one is zero, as the event that i,j form an edge with both endpoints outside of B is completely independent of the same event occurring over distinct vertices k,l. For a ﬁxed choice of (i,j) and (i,k), we can bound

E[1Bi,j ⋅ 1Bi,k]≤ P[ vi − vj ≤ r, vi − vk ≤ r]=(νrd)2 ,

where the ﬁrst inequality follows by removing the requirement that the vertices lie outside of B, and thus increasing the probability. There are N(N −1)(N −2) ways to choose a pair of indices that overlap in exactly one entry. Thus,

(1Bi,j − µB)(1Bi,k − µB)= 1Bi,j ⋅ 1Bi,k −(µB)2 ≤ C′r2dN3 ,

for some universal constant C′. Again, this overestimates the value of this sum dramatically, but is suﬃcient for our purposes. Finally, the contribution

of terms of the form (1Bi,j − µB)2 to the sum is exactly N2 (µB − µ2B), which is bounded above by C′′rdN2. Combining these results, taking expectations over N, and then adding the contribution of the variance of the expectation from before, we conclude that

- (6.10) Var( E ′)≤ C′′′(rdn2 + r2dn3),


for yet another universal constant C′′′. rdn2 grows as np+o(1), while r2dn3 grows as n2p−1+o(1). Thus, the variance of E ′ is np+o(1) if p ≤ 1, and n2p−1+o(1) when p > 1.

By Chebyshev’s inequality and (6.9),

√δµ ⋅ nz 4 ≤

P[ E ′ < µ − δµ ⋅ nz]≤ P E ′ < E[ E ′]−

16Var( E ′) δµ ⋅ n2z

.

Regardless of the value of p, this quantity vanishes as n−p 2+o(1), and therefore, with probability 1−ε, E ′ exceeds µ−

√δµ⋅nz for all suﬃciently large n.

To conclude, we note that

P[Hn(δ)] P[Hn(δ) H′]⋅ P[H′] ≥ P[ E ′ ≥ µ − 2δµ ⋅ nz]⋅ P[H′] ≥(1 − ε)P[H′].

Substituting (6.8) completes the proof.

Proof of Theorem 2.1. Fix δ,ε ∈(0,1). In this proof, whenever we say “s suﬃciently large”, we mean “s ≥ s0 for some s0 that depends only on δ and ε, and the universal constant ε˜0 from Theorem 3.1”, and whenever we say “n suﬃciently large”, we mean “n ≥ n0 for some n0 that depends only on ε, δ, and our choice of s”.

Let δ˜0 =(1 − ε 16)δ and ∆˜0 = δ. Deﬁne δ˜ to satisfy δ˜µ˜s = δµ(1 − 1 (logn)2).

Although δ˜ will depend on n, we have that δ˜0 ≤ δ˜ ≤ ∆˜0 for s and n suﬃciently large (where we use Lemma 5.1 to bound µ µ ˜s from above and below). This allows us to apply Theorem 3.1. We also deﬁne

Dn ∶=  Es − E >(1 + δ˜)µ˜s −(1 + δ)µ =  Es − E > µ˜s − µ −

δµ (logn)2

.

The deﬁnitions are chosen in such a way that {Dn ∩Hn(δ)} imply the event Ln(δ˜).

Let Fn(ε) be the event described in the statement of Theorem 2.1 i.e. the existence of a ball B housing the giant clique. Our goal is to prove that

P[Fn(ε)c Hn(δ)]= 0.

lim

n→∞

By Proposition 6.4, Gn,δ˜(s−1 20) implies the event Fn(ε) whenever δ˜ ∈[(1 − ε 16)δ,δ], n and s are suﬃciently large, and ε is suﬃciently small. Then, taking complements, we ﬁnd that

P[Fn(ε)c Hn(δ)]≤ P[Fn(ε)c ∩ Dn Hn(δ)]+ P[Dnc Hn(δ)]

P[Gn,δ˜(s−1 20)c ∩ Dn ∩ Hn(δ)] P[Hn(δ)]

+ P[Dnc Hn(δ)]

≤

P[Gn,δ˜(s−1 20)c ∩ Ln(δ˜)] P[Hn(δ)]

≤

+ P[Dnc Hn(δ)]

We begin with the second term. To analyze it, we will use an instance of the celebrated FKG correlation inequality. First stated in the context of ﬁnite lattice systems [16], we will use a version that ﬁrst appears in [23]. There is a natural partial ordering on conﬁgurations of χ: we say ω ω′ if ω ⊂ ω′ i.e. every point of ω is also in ω′. An event A is increasing with respect to this ordering if ω ω′ and ω ∈ A implies ω′ ∈ A. Heuristically, A is increasing adding points to the conﬁguration only makes A more likely to occur.

- Lemma 6.6 (The FKG Inequality [23]). Let A and B increasing events. Then


P[A B]≥ P[A]. It is clear that Hn(δ) is an increasing event. In addition, we can write

Es − E as a sum over pairs of points in the Poisson Point Process whose distance exceeds r, but whose corresponding indices satisfy ρ(I,J)≤ s. Thus, Dn is also an increasing event, and Lemma 6.6 allows us to deduce that

P[Dn Hn(δ)]≥ P[Dn]. Taking complements, we ﬁnd that

P[Gn,δ˜(s−1 20)c ∩ Ln(δ˜)] P[Hn(δ)]

P[Fn(ε)c Hn(δ)]≤

+ P[Dnc]

It’simplyeasyDnto, andsee thattherefore,{ Es >theµ˜s−unionδµ [2bound(logn)tells2]} andus that{ E < µ+δµ [2(logn)2]} P[Dnc]≤ P Es ≤ µ˜s −

δµ 2log2 n + P E ≥ µ +

δµ 2log2 n

. Recalling (2.1) and (3.6), we can see that

Var[ E = µ(1 + 2νnrd)= max np+o(1),n2p−1+o(1)},

Var[ Es ]≤ 16 S ˜I N ˜I 2md ⋅ max{D2,D3}= max{np+o(1),n2p−1+o(1)}, where we use the fact that nrd = np−1+o(1) (which follows from (2.3)) for the ﬁrst line, and equations (3.1), (3.2), and the bounds on S ˜I and N ˜I from Lemma 5.1 to get control of the variance of Es . Thus, Chebyshev’s inequality gives that

4log4 n(Var[ E ]+ Var[ Es ])

δ2µ2 = nmax{−p,−1}+o(1). As n grows, this vanishes for all admissible p.

P[Dnc]≤

To complete the proof, we must show that, for s suﬃciently large,

### P[Gn,δ˜(s−1 20)c ∩ Ln(δ˜)] P[Hn(δ)]

= 0

lim

n→∞

as n grows. We will now use Theorem 3.1, which holds since δ˜ is bounded above and below by δ(1 − ε 16) and δ, respectively. Reusing the convention q =(2δ˜µ˜s)1 2 and w = τ˜s ⋅ D, the quantitative bound of Theorem 3.1 and Lemma 6.5 gives us

P[Gn,δ˜(s−1 20)c ∩ Ln(δ˜)] P[Hn(δ)]

10

≤ exp −q log

q w − 1 −

q 2

1 10 ⋅ s1 20

√2δµ

+ 2δµ log

n ⋅ τ  − 1 + Cnz logn .

Here, the choice δ˜µ˜s = δµ(1 − 1 (logn)2) becomes essential. Careful algebra will show that the ﬁrst order terms — i.e. those of order √2δµ⋅logn — will cancel perfectly. In fact,

√2δµ

√2δµ q

n ⋅ τ  − 1 − q log

q w − 1 = q log

w nτ  + q log

2δµ log

√2δµ enτ

+( 2δµ − q)log

.

By the choice of δ˜, √2δµ q = (1 − 1 (logn)2)−1 2, and hence, the bound log(1 − x)≥−2x for all suﬃciently small x implies that

√2δµ

q  =−

log 1 −

 ≤

- 1

- 2


1 (logn)2

1 (logn)2

log

,

for all suﬃciently large n. Similarly, √2δµ−q ≤ 2q (logn)2 for all suﬃciently large n and s. Since √2δµ enτ = n(2−p) 2+o(1) (which follows from (2.3)), we conclude that

√2δµ

3 − p 2logn

n ⋅ τ  − 1 − q log

q w − 1 ≤ q log

w nτ  +

2δµ log

.

Recalling that w (nτ)= τ˜s (mdτ), we are left with

P[Gn,δ˜(s−1 20)c ∩ Ln(δ˜)] P[Hn(δ)]

≤

3 − p

- (6.11) 2logn + Cnz logn .


τ ˜s mdτ  −

1 2 ⋅ 1010s1 2 +

exp q log

From Lemma 5.1, we can see that τ˜s (mdτ)≤(1 + C s), and thus, for suﬃciently large values of s,

τ ˜s mdτ  −

1 2 ⋅ 1010s1 2 ≤

C s −

1 2 ⋅ 1010s1 2 ≤−

1 4 ⋅ 1010s1 2

log

.

For all suﬃciently large s and n, we now see that the bracketed term of (6.11) will be negative. Since z < p 2, we now see that the exponent approaches negative inﬁnity as n grows, and we deduce that

P[Gn,δ˜(s−1 20)c ∩ Ln(δ˜)] P[Hn(δ)]

= 0, as required.

lim

n→∞

7. Proof of the Upper Tail Large Deviation Principle We now prove Theorem 2.2, which claims that the function I(x)∶= 

√2x

2 − p 2

is the upper tail rate function for the random variable E with speed s(n)= √µlogn. Recall that we restrict our attention to subsets of the interval (0,∞), as our result only holds for events in which E exceeds its expectation.

Instead of proving Theorem 2.2 directly, we will prove the following proposition instead: Proposition 7.1. Recall that, for any δ > 0,

E − µ µ > δ .

Hn(δ)={ E >(1 + δ)µ}= 

Then, for any δ > 0 ﬁxed, (7.1) lim

logP[Hn(δ)]

√µlogn =−I(δ).

n→∞

The equivalence of this proposition to Theorem 2.2 is standard, but its proof is straightforward and we include it for completeness.

Proof that Proposition 7.1 implies Theorem 2.2. Pick F to be a closed subset of (0,∞), and let aF > 0 be its leftmost endpoint. Since I(x) is increasing, its inﬁmum over F occurs at aF. Furthermore, F ⊂[aF,∞), and therefore, for any ε > 0 satisfying (aF − ε)> 0,

E − µ µ ∈ F ≤ P

E − µ µ ∈(aF − ε,∞) = P[Hn(aF − ε)].

P

Taking the logarithm, dividing by √µlogn, applying (7.1) and letting ε go to zero gives the upper bound for F.

Next, take G open in (0,∞) and pick b ∈ G. For some ε > 0, we know that (b − ε,b]∈ G. Therefore,

E − µ µ ∈(b − ε,b] = P[Hn(b − ε)]− P[Hn(b)].

E − µ µ ∈ G ≥ P

P

Applying (7.1) twice, we deduce that, for any ε˜> 0, there is an n suﬃciently large to ensure that

E − µ µ ∈ G ≥ exp(−(1 + ε˜)⋅ I(b − ε)⋅

√µlogn) − exp(−(1 − ε˜)⋅ I(b)⋅

P

√µlogn) .

Picking ε˜ suﬃciently small (as a function of ε) ensures that the second term is smaller than half the ﬁrst term. Taking logarithms, dividing by √µlogn,

µand) µtaking∈ G}, andε to zeroestablishesestablishesTheoremthe lower2.2. bound on the probability of {( E − Proof of Proposition 7.1. The statement that, for any ε > 0, there exists n suﬃciently large to ensure that

logP[Hn(δ)]

√µlogn >−(1 + ε)I(δ)

is a direct consequence of Lemma 6.5. Thus, it will be suﬃcient an upper bound on the probability of Hn(δ).

Fix ε > 0. For an arbitrary pair of events A and B, assume that, conditional on A, the event B occurs with probability at least 1 − ε. This implies that

P[A]≤ 

P[B].

1 1 − ε

By Theorem 2.1, there exists a suﬃcient large n such that conditioning on H√n2(δµδ)(1implies− ε) withthatprobabilitythe randomatgeometricleast 1 − εgraph. Thishasmeansa cliquethat,offorsizeanyats,leastthe s-graded model includes a maximal clique set P ⊂ T with at least as many vertices as the clique of the random geometric graph. Since every maximal clique set has τ˜s indices, there can be at most mdτ˜s distinct maximal clique sets; this is an egregious overcount, but we have no need for ﬁner control. Thus, by the union bound, the probability that there exists a maximal clique set with √2δµ(1−ε) vertices is bounded above by mdτ˜s times the probability that a single one has the same property. The number of vertices in a maximal clique set is distributed as a Poisson random variable of mean τ˜s ⋅ D = w. Therefore, the chain of implication allows us to conclude that

mdτ˜s 1 − ε

P Poisson(w)> 2δµ(1 − ε)  . Let v ∶=

P[Hn(δ)]≤ 

√2δµ(1 − ε). Applying the Chernoﬀ bounds of Poisson random variables (see Lemma 5.2) to the right-hand side above gives

mdτ˜s 1 − ε

exp −v log

- v

- w − 1 − w


P[Hn(δ)]≤ 

√µ w

≤ exp −(1 − 2ε) 2δµlog

,

where the second inequality follows for all suﬃciently large n by noting that all the missing terms vanish in comparison to √µ ⋅ logn, and can therefore be absorbed at the cost of changing ε to 2ε. By the deﬁnitions of µ, p and w,

√µ

w = n(2−p) 2+o(1) . Therefore, for any η > 0, there exists an n suﬃciently large to ensure that

2 − p 2 + η √2δ . Since ε and η are arbitrary, we conclude the desired upper bound.

logP[Hn(δ)]≤−(1 − 2ε) 

1 √µlogn

Acknowledgment. The authors thank Mathew Penrose for many helpful comments. They would also like to thank the anonymous referees for their thorough reports, which greatly improved this manuscript, and helped correct several errors that were pointed out in previous versions.

References

- [1] Augeri, F. (2018). Nonlinear large deviation bounds with applications to traces of Wigner matrices and cycles counts in Erdos-Renyi graphs. Preprint. Available at https://arxiv.org/abs/1810.01558.
- [2] Azuma, K. (1967). Weighted sums of certain dependent random variables. Tohoku Math. J., Second Series, 19(3), 357–367.
- [3] Alon, N. and Spencer, J. H. (2008) The Probabilistic Method. John Wiley and Sons, Hoboken, New Jersey.
- [4] Avin, C. and Ercal, G. (2007). On the cover time and mixing time of random geometric graphs. Theoretical Computer Science, 380(1), 2–22 .
- [5] Bhattacharya, B. B., Ganguly, S., Lubetzky, E. and Zhao, Y. (2017). Upper tails and independence polynomials in random graphs. Advances in Mathematics, 319, 313-347.
- [6] Burago, Y. D. and Zalgaller, V. A. (1998). Geometric Inequalities. Leningrad.
- [7] Chatterjee, S. (2017). A note about the uniform distribution on the intersection of a simplex and a sphere. Journal of Topology and Analysis, 9(04), 717-738.
- [8] Chatterjee, S. (2012). The missing log in large deviations for triangle counts. Random Structures and Algorithms, 40(4), 437–451.
- [9] Chatterjee, S. (2016). An introduction to large deviations for random graphs. Bull. Amer. Math. Soc., 53(4), 617–642.
- [10] Chatterjee, S. and Dembo, A. (2016). Nonlinear large deviations. Advances in Mathematics, 299, 396-450.
- [11] Cook, N. A. and Dembo, A. (2018). Large deviations of subgraph counts for sparse Erdos–Renyi graphs. Preprint. Available at https://arxiv.org/abs/1809.11148.
- [12] Demarco, B. and Kahn, J. (2012). Upper tails for triangles. Random Structures and Algorithms, 40(4), 452–459.
- [13] Dembo, A. and Zeitouni, O. (2010). Large Deviations Techniques and Applications. (Vol 38). Springer, New York.
- [14] Eldan, R. (2018) Gaussian-width gradient complexity, reverse log-Sobolev inequalities and nonlinear large deviations Geometric and Functional Analysis, 28(6), 1548–1596.
- [15] Federer, H. (1996). Geometric Measure Theory. Springer, Berlin.
- [16] Fortuin, C. M., Kasteleyn, P. W., and Ginibre, J. (1971). Correlation Inequalities on Some Partially Ordered Sets. Communications in Mathematical Physics, 22, 89–103.
- [17] Gilbert, E. N. (1961). Random Plane Networks. Journal of the Society of Industrial and Applied Mathematics, 9(4),533–543.
- [18] Goel, A., Rai, S., and Krishnamachari B. (2005). Monotone properties of random geometric graphs have sharp thresholds. Annals of Applied Probability, 15(4), 2535– 2552.
- [19] Grimmett, G. (1999). Percolation. Springer, Berlin.
- [20] Hafner, R. (1972). The assymptotic distribution of clumping. Computing, 10(4), 335–351.
- [21] Harel, M., Mousset, F., and Samotij, W. (2019). Upper tails via high moments and entropic stability. Preprint. Available at https://arxiv.org/abs/1904.08212.
- [22] Hoeﬀding, W. (1963). Probability inequalities for sums of bounded random variables. J. Amer. Stat. Assoc., 58, 13–30.
- [23] Janson, S. (1984). Bounds on the distributions of extremal values of a scanning process. Stochastic Processes and Applications, 18, 313-328.
- [24] Janson, S. (2004). Large deviations for sums of partly dependent random variables. Random Structures and Algorithms, 24(3), 234–248.
- [25] Janson, S. and Ruciński, A. (2002). The infamous upper tail. Random Structures and Algorithms, 20(3), 317–342.
- [26] Janson, S., Oleszkiewicz, K., and Rucinski, A. (2004). Upper tails for subgraph counts in random graphs. Israel Journal of Mathematics, 142, 61—92.


- [27] Kim, J.H. and Vu, V.H. (2000). Concentration of multivariate polynomials and its applications. Combinatorica, 20(3), 417– 434.
- [28] Lubetzky, E. and Zhao, Y. (2017). On the variational problem for upper tails in sparse random graphs. Random Structures and Algorithms, 50(3), 420-436.
- [29] Meester, R. and Roy, R. (1996). Continuum Percolation. (Vol. 119) Cambridge University Press, Cambridge.
- [30] Muller, T. (2006). Two-point concentration in random geometric graphs. Combinatorica, 28(5), 529–545.
- [31] Nagaev, S. V. (1979). Large deviations of sums of independent random variables. The Annals of Probability 7(5),745–789.
- [32] Penrose, M. D. (2002). Focusing of the scan statistic and geometric clique number. Advances in Applied Probability, 739–753.
- [33] Penrose, M. (2003). Random Geometric Graphs. (Vol. 5) Oxford University Press, Oxford.
- [34] Penrose, M. D. and Yukich, J.E. (2003). Weak laws of large numbers in geometric probability. The Annals of Applied Probability, 13(1), 277–303.
- [35] Penrose, M. D. and Yukich, J. E. (2005). Normal approximation in geometric probability. Stein’s Method and Applications, Lecture Note Series, Institute for Mathematical Sciences, National University of Singapore,5, 37–58.
- [36] Petersen, P. (2006). Riemannian Geometry. (Vol. 171). Springer, New York.
- [37] Klain, D. A., and Rota, G. C. (1997). Introduction to Geometric Probability Cambridge University Press, Cambridge.
- [38] Schreiber, T. and Yukich, J. E. (2005). Large deviations for functionals of spatial point processes with applications to random packing and spatial graphs. Stochastic Processes and Their Applications, 115(8), 1332–1356.
- [39] Talagrand, M. (1996). Concentration of measures and isoperimetric inequalities in product spaces. Publications Mathematiques de l’I.H.E.S., 81(1),73–205.
- [40] Talagrand, M. (2003). Spin Glasses: A Challenge for Mathematicians. Springer, Berlin.


Department of Statistics Stanford University Email: souravc@stanford.edu

Department of Mathematics Tel Aviv University Email: mataharel8@tauex.tau.ac.il

