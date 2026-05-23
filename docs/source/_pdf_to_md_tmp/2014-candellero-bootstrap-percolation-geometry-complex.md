# arXiv:1412.1301v2[math.PR]22Aug2015

## Bootstrap percolation and the geometry of complex networks∗

##### Elisabetta Candellero† Nikolaos Fountoulakis‡ September 27, 2018

###### Abstract

On a geometric model for complex networks (introduced by Krioukov et al.) we investigate the bootstrap percolation process. This model consists of random geometric graphs on the hyperbolic plane having N vertices, a dependent version of the Chung-Lu model. The process starts with infection rate p = p(N). Each uninfected vertex with at least r ≥ 1 infected neighbors becomes infected, remaining so forever. We identify a function pc(N) = o(1) such that a.a.s. when p pc(N) the infection spreads to a positive fraction of vertices, whereas when p pc(N) the process cannot evolve. Moreover, this behavior is “robust” under random deletions of edges.

### 1 Introduction

Bootstrap percolation is a deterministic process, characterized by a cascade behavior, in which every vertex has two possible states: either infected or uninfected (sometimes also referred to as active or inactive, respectively). A ﬁxed integer r ≥ 1, called the activation threshold, determines the evolution of the process, which occurs in rounds.

Initially, on the graph G = G(V,E) there is a subset A0 ⊆ V which consists of infected vertices (vertices belonging to V \ A0 are uninfected) that can be selected deterministically or at random.

Subsequently, in each round, if an uninfected vertex has at least r infected neighbors, then it also becomes infected and remains so forever. This is repeated until no more vertices become infected. We denote the ﬁnal infected set by Af.

This process was introduced by Chalupa, Leath and Reich [CLR79] in 1979 in the context of magnetic disordered systems and has been re-discovered since then by several authors mainly due to its connections with various physical models.

These processes have been used as models to describe several complex phenomena in diverse areas, from jamming transitions [TBF06] and magnetic systems [SDS02] to neuronal activity [Ami10, ACM14, TE09]. A short survey regarding applications of bootstrap percolation processes can be found in [AL03].

∗Keywords: Random geometric graph, hyperbolic plane, bootstrap percolation, percolation. †Department of Statistics, University of Warwick, Coventry CV4 7AL, UK. Email:

elisabetta.candellero@gmail.com

‡School of Mathematics, University of Birmingham, Birmingham B15 2TT, UK. Email: n.fountoulakis@bham.ac.uk, Research supported by a Marie Curie Career Integration Grant PCIG09GA2011-293619 and an EPSRC Grant (No. EP/K019749/1).

In the present paper, we consider a geometric framework for complex networks that was introduced by Krioukov et al. [KPK+10]. The theory of complex networks has been developed as a unifying mathematical framework that expresses features of a variety of networks: biological networks, large computer networks such as the Internet, the World Wide Web as well as social networks that have been recently developed over these platforms. Experimental evidence (cf. [CL06], [AB02]) has shown that these networks exhibit a few basic characteristics: their degree distribution seems to follow a power-law, they exhibit local clustering and, ﬁnally, the typical distances between vertices are small (this is known as the small world eﬀect). In fact, most of these networks appear to have a degree distribution that has a power-law tail with exponent between 2 and 3 (see [AB02]).

During the last 15 years there has been a continuous eﬀort to develop models of random networks which typically exhibit all the above features simultaneously. Among the most inﬂuential models was the Watts-Strogatz model of small worlds [WS98] and the Barab´si-Albert model [BA99], which is also known as the preferential attachment model. The framework of Krioukov et al. [KPK+10] represents the inherent inhomogeneity of a complex network with the use of the hyperbolic plane. Intuitively, the intrinsic hierarchies that are present in a complex network induce a tree-like structure which is eﬀectively embedded into the hyperbolic plane. The aim of this work is to shed some light on the evolution of a bootstrap percolation process and how this is determined by the geometry of the underlying network.

#### 1.1 Random geometric graphs on the hyperbolic plane and inhomogeneous random graphs

The most common representations of the hyperbolic plane are the upper-half plane representation {z = x + iy : y > 0} as well as the Poincar´e unit disk which is simply the open disk of radius one, that is, {(u,v) ∈ R2 : 1 − u2 − v2 > 0}. Both spaces are equipped with the

hyperbolic metric; in the former case this is y12dy2 whereas in the latter this is 4 (1du−u22+−dvv22)2. It is well-known that the (Gaussian) curvature in both cases is equal to −1 and that the two spaces are isometric. In fact, there are more representations of the hyperbolic plane of curvature −1, which are isometrically equivalent to the above two. We will denote by H2 the class of these spaces.

In this paper, following the deﬁnitions in [KPK+10], we shall be using the native representation of H2. Under this representation, the ground space of H2 is R2 and every point x ∈ R2 whose polar coordinates are (r,θ) has hyperbolic distance from the origin equal to its Euclidean distance, which is equal to r. Alternatively, the native representation can be thought of as a mapping of the Poincar´e disk into R2. Under this representation, a point p in the Poincar´e disk that is at hyperbolic distance r from the origin and angle θ with respect to the horizontal axis is mapped to the point p of Euclidean distance r from the origin of R2, preserving the angle.

We are now ready to give the deﬁnitions of the two basic models introduced in [KPK+10]. Consider the native representation of the hyperbolic plane. Let N be the number of vertices of the random graph. This is the parameter with respect to which we do asymptotics. For some ﬁxed constant ν > 0, let R > 0 satisfy N = νeR/2 . For simplicity, we will omit  ·  as this does not aﬀect our calculations. We select randomly and independently N points from the disk of radius R centered at the origin O, which we denote by DR.

Each of these points is distributed as follows. Assume that a random point u has polar

coordinates (r,θ). The angle θ is uniformly distributed in (0,2π] and the probability density function of r, which we denote by ρN(r), is determined by a parameter α > 0 and is equal to

ρ(r) = ρN(r) =

αcoshsinhαRαr−1, if 0 ≤ r ≤ R 0, otherwise

. (1)

The above distribution is simply the uniform distribution on DR, but on the hyperbolic plane of curvature −α2. With elementary but tedious calculations, it can be shown that the length of a circle of radius r (centered at the origin) on the hyperbolic plane of curvature −α2 is 2π

α sinh(αr), whereas the area of the circle of radius R (centered at the origin) is α2π2(cosh(αR)−

- 1). Hence, when α = 1, the above becomes the uniform distribution.


An alternative way to deﬁne this distribution is as follows. Consider the disk D R of radius R around the origin O of (the native representation of) the hyperbolic plane of curvature −α2. Select N points independently within D R, uniformly at random. Subsequently, the selected points are projected onto DR preserving their polar coordinates. The projections of these points, which we will be denoting by VN, will be the vertex set of the random graph.

Note that the curvature in this case determines the rate of growth of the space. Hence, when α < 1, the N points are distributed on a disk (namely D R) which has smaller area compared to DR. This naturally increases the density of those points that are located closer to the origin. Similarly, when α > 1 the area of the disk D R is larger than that of DR, and most of the N points are signiﬁcantly more likely to be located near the boundary of D R, due to the exponential growth of the volume.

Given the set VN on DR we deﬁne the random graph G(N;α,ν) on VN, where two distinct vertices are joined precisely if they are within (hyperbolic) distance R from each other.

###### 1.1.1 G(N;α,ν) and the Chung-Lu model

The notion of inhomogeneous random graphs was introduced by S¨derberg [S¨d02] but was deﬁned more generally and studied in great detail by Bollob´s, Janson and Riordan in [BJR07]. In its most general setting, there is an underlying compact metric space S equipped with a measure µ on its Borel σ-algebra. This is the space of types of the vertices (deﬁned below). A kernel κ is a bounded real-valued, non-negative function on S ×S, which is symmetric and measurable. The vertices of the random graph can be understood as points in S. If x,y ∈ S, then the corresponding vertices are joined with probability κ(Nx,y) ∧ 1, independently of every other pair (N is the total number of vertices). The points that are the vertices of the graph are approximately distributed according to µ. More speciﬁcally, the empirical distribution function on the N points converges weakly to µ as N → ∞.

Of particular interest is the case where the kernel function can be factorized and can be written κ(x,y) = t(x)t(y); this is called a kernel of rank 1. Here, the function t(x) represents the weight of the type of vertex x and, in fact, it is approximately its expected degree. The special case where t(x) follows a distribution that has a power law tail was considered by Chung and Lu in a series of papers [CL02a], [CL02b] (see also [vdH]).

In the random graph G(N;α,ν) the probability that two vertices are adjacent has this form. The proof of this fact relies on Lemma 2.1, which we will state and prove later. This provides an approximate characterization of what it means for two points u,v to have hyperbolic distance at most R in terms of their relative angle, which we denote by θu,v. For this lemma,

we need the notion of the type of a vertex. For a vertex v ∈ VN, if rv is the distance of v from the origin, that is, the radius of v, then we set tv = R − rv – we call this quantity the type of vertex v. As we shall shortly see, the type of a vertex is approximately exponentially distributed. If we substitute R − t for r in (1), then assuming that t is ﬁxed that expression becomes asymptotically equal to αe−αt. By Lemma 2.1, two vertices u and v of types tu and tv are within distance R (essentially) if and only if θu,v < 2νetu/2etv/2/N. Hence, conditional on their types the probability that u and v are adjacent is proportional to etu/2etv/2/N. If we set t(u) = etu/2, then P(t(u) ≥ x) = P(tu ≥ 2lnx) e−2αlnx = 1/x2α. In other words, the distribution of t(u) has a power-law tail with parameter 2α. Thus, the random graph G(N;α,ν) is a dependent version of the Chung-Lu model that emerges naturally from the hyperbolic geometry of the underlying space. The fact that this is a random geometric graph gives rise to the existence of local clustering, which is missing in the Chung-Lu model. There, most vertices have tree-like neighborhoods.

In fact, it can be shown that the degree of a vertex u in G(N;α,ν) that has type tu is approximately distributed as a Poisson random variable with parameter proportional to etu/2. This is shown only implicitly in Lemma 2.7.

Gugelmann, Panagiotou and Peter [GPP12] showed that the degree of a vertex has a power law with exponent 2α + 1. If α > 1/2, then the exponent of the power law may take any value greater than 2. When 1 > α > 1/2, this exponent is between 2 and 3. They also showed that the average degree is a constant that depends on α and ν, and that the clustering coeﬃcient (the probability of two vertices with a common neighbor to be joined by an edge) of G(N;α,ν) is asymptotically bounded away from 0 with probability 1 − o(1) as N → ∞.

Furthermore, the second author together with Bode and Mu¨ller [BFM15] showed that G(N;α,ν) with high probability has a giant component, that is, a connected component containing a linear number of vertices if 1 > α > 1/2. When α > 1, the size of the largest component is bounded by a function that is sublinear in N. Recently, Kiwi and Mitsche [KM15] showed that in the supercritical regime, the order of the second largest component is bounded by a polylogarithmic function of N a.a.s.

#### 1.2 Results

The main result of this paper regards the size of the ﬁnal set Af of a bootstrap percolation process with activation threshold r ≥ 1 on G(N;α,ν), with 1 > α > 1/2. We shall assume that the initially infected set A0 is a random subset of VN, where each vertex is included independently with probability p. We call p the initial infection rate. We shall be assuming that p does depend on N. In fact, we will identify a critical infection rate (cf. Theorem 1.2) such that when p “crosses” this critical function the evolution of the bootstrap process changes abruptly. This critical density converges to 0 as N grows. Our results imply that a sub-linear initial infection results with high probability in the spread of the infection to a positive fraction of VN.

Our hypothesis is that 1/2 < α < 1, whereby the random graph G(N;α,ν) exhibits power law degree distribution with exponent between 2 and 3. The second author and Amini [AF14] showed a result analogous to Theorem 1.2 for the Chung-Lu model with the exponent of the power law between 2 and 3.

In the present work, we additionally show that this phenomenon is robust under random deletions of the edges of G(N;α,ν). Assuming that we retain each edge independently with

constant (independent of N) probability ρ > 0, we let G(N;α,ν,ρ) denote the resulting random graph. Since the number of edges of G(N;α,ν) is proportional to N with high probability, it follows that if we allow ρ = o(1), then G(N;α,ν,ρ) has only sub-linear components with high probability.

- Remark 1.1 (Notation). We say that a sequence of events EN on the space of graphs incurred by G(N;α,ν,ρ) occurs asymptotically almost surely (a.a.s.) whenever P(EN) → 1 as N → ∞. If XN is a random variable deﬁned on G(N;α,ν,ρ), then we write liminfN→∞ XN > 0 a.a.s., if there exists a real number c > 0 such that XN > c, a.a.s..


For any two functions f,g : N → R+ we write f(N) g(N) to denote that there is a constant C > 0 such that f(N) ≥ Cg(N) eventually as N → ∞. Analogously we write f(N) g(N) if there is a constant c > 0 such that f(N) ≤ cg(N) eventually as N → ∞. Moreover, we write f(N) g(N) if both f(N) g(N) and g(N) f(N) hold simultaneously. Finally, we write f(N) g(N) or f(N) g(N) if f(N)/g(N) → 0 or f(N)/g(N) → ∞ respectively.

Now we can state our main result.

Theorem 1.2. Let r ≥ 2 be an integer, let ρ ∈ (0,1] and 1/2 < α < 1. Consider a bootstrap percolation process on G(N;α,ν,ρ) with activation threshold r and initial infection rate p(N). Then the following hold

- (i) If p(N)N1/2α → ∞, then liminf N→∞

|Af| N

> 0 a.a.s.;

- (ii) if p(N)N1/2α → γ ∈ R+, then liminf N→∞

|Af| N

> 0 with positive probability;

- (iii) if p(N)N1/2α → 0, then |Af| = |A0| a.a.s.


The proof of Theorem 1.2 eﬀectively makes use of a dense core that G(N;α,ν) has. Intuitively, the proof is based on considering the set of vertices appearing “very close” to the circumference of radius R/2α. In fact, if p(N) is large enough, then at least r of such vertices either belong to A0, or will be infected after the ﬁrst round (and hence they will spread the infection throughout the graph). On the other hand, if p(N) N−21α, then a.a.s. the process does not evolve and the ﬁnal set of infected vertices will coincide with the initial set.

When considering the case for G(N;α,ν,ρ), we have that this central core is a dense binomial random graph where each edge is present with probability ρ. The condition on p(N) ensures that the core becomes completely infected even in this case. Thereafter, we apply an inductive argument which shows that with high probability the infection spreads from the core to a positive fraction of VN.

Note that when r = 1 the ﬁnal set of infected vertices is the union of connected components that contain at least one infected vertex at the beginning of the process. Hence, a reformulation of part (i) of Theorem 1.2 for r = 1 implies that the graph G(N;α,ν,ρ) for any 1/2 < α < 1 and any ρ > 0 contains a giant component. In other words, the graph G(N;α,ν) contains a giant component which is robust under random edge deletions. Let 1(G) denote the number of vertices in a largest component of a graph G.

Corollary 1.3. For all ρ ∈ (0,1] we have a.a.s.

1(G(N;α,ν,ρ)) N

liminf

> 0.

N→∞

A further consequence of part (i) of Theorem 1.2 is the existence of an r-core in G(N;α,ν,ρ).

Recall that for any integer r ≥ 2 the r-core of a graph G is the maximum subgraph of minimum degree at least r. This is a well-studied notion in the theory of random graphs and hypergraphs (see for example [PSW96], [Coo04], [CW06]). Let cr(G) denote the number of vertices of the r-core of a graph G.

Theorem 1.4. For all integers r ≥ 2 and all ρ ∈ (0,1] we have a.a.s.

cr(G(N;α,ν,ρ)) N

liminf

> 0.

N→∞

In other words, Theorem 1.4 implies that the r-core of G(N;α,ν) is robust under random edge deletions.

The proof of Theorem 1.2 is based on an inductive argument, and it is spread over Section

- 3 (the base step), and Section 4 (the inductive step). Finally, in Section 5 we show the proofs of Corollary 1.3 and Theorem 1.4.


Acknowledgments. The authors are grateful to Peter M¨rters for suggesting the problem of the robustness of the giant component under random edge deletions.

### 2 Preliminaries

Throughout the paper, we will be working with the notion of the type of a vertex, rather than its distance from the origin: denoting by ru the distance of vertex u from the origin, its type is deﬁned as tu := R − ru.

It is not hard to show that the type of a vertex follows the exponential distribution with parameter α. More speciﬁcally, it follows from (1) that for any c < 1, uniformly over tu < c·R, we have

ρ¯(tu) := ρ(ru) = αe−αtu 1 − o(1) . (2) We will use this asymptotic equality several times in our proofs, a proof of this easy fact can be found in [CF15]. The above expression implies that the probability that tu ≥ R/(2α) + ω(N) is o(1/N), provided that ω(N) → ∞ as N → ∞. Therefore, a.a.s. all vertices have type that is bounded by R/(2α) + ω(N), where ω(N) can be any slowly growing function that tends to inﬁnity.

#### 2.1 Distances on the hyperbolic plane

We will need a general tool that will allow us to deal with distances on the hyperbolic plane (because these characterize whether or not two vertices are adjacent). The following lemma provides an almost characterization for two points u,v to have hyperbolic distance less than R in terms of their types and their relative angles in DR. This is a key lemma whose proof is based on the hyperbolic law of cosines and allows us to estimate the probability that

two vertices are adjacent. More speciﬁcally, assuming that the points have types tu and tv, respectively, this condition is eﬀectively an upper bound on the relative angle θu,v between u and v so that d(u,v) < R.

- Lemma 2.1. For any ε > 0 there exists an N0 > 0 and a c0 > 0 such that for any N > N0 and u,v ∈ DR with tu + tv < R − c0 the following hold.


- • If θu,v < 2(1 − ε)exp 12(tu + tv − R) , then d(u,v) < R.

- • If θu,v > 2(1 + ε)exp 2 1(tu + tv − R) , then d(u,v) > R.


Proof. We begin with the hyperbolic law of cosines:

cosh(d(u,v)) = cosh(R − tu)cosh(R − tv) − sinh(R − tu)sinh(R − tv)cos(θu,v). The right-hand side of the above becomes:

cosh(R − tu)cosh(R − tv) − sinh(R − tu)sinh(R − tv)cos(θu,v)

e(2R−(tu+tv)) 4

1 + e−2(R−tu) 1 + e−2(R−tv) − 1 − e−2(R−tu) 1 − e−2(R−tv) cos(θu,v)

=

e(2R−(tu+tv)) 4

1 − cos(θu,v) + (1 + cos(θu,v)) e−2(R−tu) + e−2(R−tv)

=

+O e−2(2R−(tu+tv)) .

(3)

Therefore,

cosh(d(u,v)) ≤ e(2R−(tu+tv)) 4

1 − cos(θu,v) + 2 e−2(R−tu) + e−2(R−tv) + O e−2(2R−(tu+tv)) .

###### Since tu +tv < R−c0, the last error term is O(N−4). Also, it is a basic trigonometric identity that 1 − cos(θu,v) = 2sin2 θu,v2 . The latter is at most θ

2 u,v

2 . Therefore, the upper bound on θu,v yields:

e(2R−(tu+tv)) 4

cosh(d(u,v)) ≤

e(2R−(tu+tv)) 4

≤

eR 2

= (1 − ε)2

+

θu,v2 2

+ 2 e−2(R−tu) + e−2(R−tv) + O

1 N4

2(1 − ε)2e(tu+tv−R) + 2 e−2(R−tu) + e−2(R−tv) + O (1)

- 1

- 2


e(tu−tv) + e(tv−tu) + O(1).

At this point we choose c0 such that e−c0 < 2ε, hence the above is bounded from above by

eR 2

- 1

- 2


(1 − ε)2

+ ε

eR 2

2e(tu+tv) + O(1) <

,

for N large enough, since tu + tv < R − c0 and tu,tv ≥ 0. Also, since cosh(d(u,v)) > 12ed(u,v), it follows that d(u,v) < R.

To deduce the second part of the lemma, we consider a lower bound on (3) using the lower bound on θu,v:

e(2R−(tu+tv)) 4

cosh(d(u,v)) ≥

(1 − cos(θu,v)) + O(1)

e(2R−(tu+tv)) 4

1 − cos 2(1 + ε)e12(tu+tv−R) + O(1).

≥

Using again that 1 − cos(θ) = 2sin2 2 θ we deduce that 1 − cos 2(1 + ε)e21(tu+tv−R) = 2sin2

- 1

- 2


2(1 + ε)e12(tu+tv−R) .

Since tu + tv < R − c0, it follows that tu + tv − R < −c0. So the latter is

(1 + ε)e12(tu+tv−R) 2

sin (1 + ε)e12(tu+tv−R) ≥

, for N and c0 large enough. Substituting this bound into (4) we have

cosh(d(u,v)) ≥ 2

(1 + ε)e12(tu+tv−R) 2

2

e(tu+tv−R) 2

+ O(1) = (1 + ε)2

+ O(1).

(4)

Thus, if d(u,v) ≤ R, the left-hand side would be smaller than the right-hand side which would lead to a contradiction.

| |
|---|


#### 2.2 Sketch of proof and the setup of the induction argument The proof of Theorem 1.2 relies on an inductive argument which shows

- 1. that if p N−1/(2α), then a.a.s. all vertices of type at least R/2 (which we call the core vertices) become infected;
- 2. how the infection spreads to the remaining vertices.


To implement the second part, we divide the disk DR into homocentric bands and eﬀectively show that if most of the vertices of a band are infected, then this is also the case for the next band. This is the inductive step. The partition is deﬁned as follows. We set t0 := R/2 and for i > 0,

4π ν(1 − ε)4

ti − 2ln

ti = λti−1, (5) where λ := 2α − 1. Since 1/2 < α < 1, we have 0 < λ < 1. We set

B0 := {v ∈ DR : R/2 < tv ≤ R}, and for i > 0

Bi := {v ∈ DR : ti ≤ tv < ti−1}. We shall restrict our analysis to i < T, where the value T will be determined explicitly in Appendix A. In particular, we have the following result whose proof is rather technical and hence deferred to Appendix A.

- Lemma 2.2. The number of bands T is of order O (lnR).


Also, for i ≥ 0 denote by Ci the circle centered at the origin O that has radius R − ti. Hence Bi is delimited by Ci and Ci−1.

We will use some standard concentration inequalities to show that the number of vertices in each band is concentrated around its expected value. Once we have established this, we will condition on the sets of vertices that belong to each band.

Let Ni denote the set of vertices in VN that belong to Bi, and let Ni := |Ni|.

- Claim 2.3. We have E[N0] = Ω(N1−α).

Proof. We use (2) and deduce that

E[N0] ≥ (1 − o(1))Nα

3R/4

t0

e−αtdt = (1 − o(1))N e−αR/2 − e−3αR/4 = Ω(N1−α).

| |
|---|


The next claim deals with i > 0.

- Claim 2.4. Let ε > 0. If T is such that for i < T e−α(ti−1−ti) < ε, (6)


then for any N suﬃciently large and for every 0 < i < T we have (1 − ε)2Ne−αti ≤ E[Ni] ≤ (1 + ε)2Ne−αti. Proof. Note that by (2) (since ti ≤ R/2, for all i > 0) we have uniformly for all i > 0 E[Ni] = (1 − o(1))Nα

ti−1

e−αtdt = (1 − o(1))N e−αti − e−αti−1 . (7)

ti

The upper bound follows trivially. For the lower bound we use (6) which together with (7) imply that for N suﬃciently large

E[Ni] = (1 − o(1))Ne−αti 1 − e−α(ti−1−ti)

which ﬁnishes the proof.

(6) > Ne−αti(1 − ε)2, (8)

| |
|---|


For the sake of completeness, we recall here two classical results that will be used throughout the paper: Chernoﬀ bounds and the bounded-diﬀerences inequality.

Chernoﬀ bounds. Consider a binomial random variable X ∼ Bin(n,p). If EX = np → ∞,

- as n → ∞, then for every constant ≥ 0 we have


(EX − )2 2EX ≥ 1 − exp −

np 4

P(X ≥ ) ≥ 1 − exp −

, (9)

provided that n is large enough. Analogously, we have P(X ≥ 2EX) ≤ exp −

np 8

. (10)

Bounded-diﬀerences inequality (Hoeﬀding-Azuma). Suppose X1,...,Xn is a collection of independent random variables, and f : Rn → R is a real-valued function. Let c1,c2,...,cn satisfy

sup

x1,x2,...,xn,x i

f(x1,x2,...,xi,...,xn) − f(x1,x2,...,x i,...,xn) < ci,

for 1 ≤ i ≤ n. Now, let X := f(X1,X2,...,Xn). Then for every 0 < < 1 we have

2 2(EX)2 n i=1 c2i

P(X < (1 − )EX) ≤ exp −

. (11)

Now we apply all these results to our setting, by showing the next lemma. Lemma 2.5. For any ε > 0 with high probability we have

(1 − ε)3Ne−αti ≤ Ni ≤ (1 + ε)3Ne−αti. (12)

Proof. Applying the Chernoﬀ bound (9), and since T = O (lnR) (by Lemma 2.2), a simple ﬁrst-moment argument shows that with probability 1 − exp −Ω N1−α we have

(1 − ε)E[Ni] ≤ Ni ≤ (1 + ε)E[Ni], for all 0 < i < T. More precisely, for 0 < i < T, deﬁne the event

Ei := (1 − ε)E[Ni] ≤ Ni ≤ (1 + ε)E[Ni] . (13) Since P(Ei) ≥ 1 − e−Ω(N1−α) uniformly for every i < T, then the probability of the event

T−1

E :=

Ei

i=1

is bounded from below by

T−1

P(E) ≥

i=1

1 − e−Ω(N1−α) ≥ 1 −

T−1

e−Ω(N1−α) ≥ 1 − Te−Ω(N1−α). (14)

i=1

Again, using Lemma 2.2, one has P(E) = 1 − o(1). Note that when E occurs, then for any N suﬃciently large, by Claim 2.4 and (13) for all i = 1,...,T we have the statement.

| |
|---|


- Remark 2.6. Throughout the rest of the paper, we will be assuming that the event E has been realized, and hence that (12) holds.


Now we show an intermediate result about the degree distribution of a vertex v ∈ VN conditional on its type. For two random variables X and Y we write X Y to denote that the random variable Y stochastically dominates X.

- Lemma 2.7. Let dv denote the degree of a vertex v conditional on its type tv. There are two constants 0 < H1 < H2 such that for any N suﬃciently large, if tv < R/2α + ω(N), then we have


etv/2 N

etv/2 N

dv Bin N,H2

.

Bin N,H1

Proof. For every vertex u ∈ VN, the probability that u ∼ v (conditional on tv) can be bounded from above using Lemma 2.1 and (2) as follows

P(u ∼ v | tv)

R−tv−C

e(tu+tv)/2 N

ρ¯(tu)dtu + P(tu > R − tv − C | tv),

0

where C > 0 is an arbitrary large constant. On the other hand, a lower bound is given by

P(u ∼ v | tv)

R−tv−C

e(tu+tv)/2 N

ρ¯(tu)dtu.

0

The ﬁrst step of the proof consists in estimating the integral

I1 :=

R−tv−C

e(tu+tv)/2 N

ρ(tu)dtu,

0

and subsequently in showing that the quantity

I2 := P(tu > R − tv − C | tv) satisﬁes

I2 = o(I1), (15) uniformly over tv. We start with the ﬁrst task, where we use (2) and write

I1 = (1 + o(1))

0

etv/2 N

= (1 + o(1))

We can bound I2 similarly:

R−tv−C

e(tu+tv)/2 N

e−αtudtu

R−tv−C

etv/2 N

e−(α−1/2)tudtu α>1/2

.

0

I2

R

e−αtudtu e−α(R−tv−C) e−α(R−tv)eαC

R−tv−C

etv/2 N

2α

.

By direct comparison we see that (15) holds, since α > 1/2.

It is now easy to see that the above must imply that there are two constants 0 < H1 < H2 such that for any N suﬃciently large

etv/2 N

etv/2 N ≤ P(u ∼ v | tv) ≤ H2

.

H1

Therefore, since the (conditional) degree of v is given by

Bin(N,P(u ∼ v | tv)), for any u ∈ VN, then we have the statement. Remark 2.8. Without loss of generality, we can choose the constant H2 such that H2 > 1.

| |
|---|


Of particular interest will be what we call the light degree of a vertex v. This is deﬁned as follows: given a constant C > 0 (that is to be speciﬁed later during our proof, cf. Appendix A), the light degree of vertex v is the number of neighbors of v that have type less than C > 0. To emphasize the dependence on C we denote it by dC(v). Arguing as in the proof of the above lemma we can show the following statement.

- Lemma 2.9. Let C > 0 and let dC(v) be the light degree of a vertex v conditional on its


type tv. There are two constants 0 < H 1 < H 2 that depend on α and C such that for any N suﬃciently large, if tv < R/2α + ω(N), then we have

etv/2 N

Bin N,H 1

etv/2 N

dC(v) Bin N,H 2

.

### 3 Base Step for Induction

In this section we show that under assumption (i) (resp. (ii)) of Theorem 1.2, with high probability (resp. positive probability) all vertices in B0 become infected. This will be the base case for an inductive argument that will eventually show how the infection will spread from B0 to almost every vertex in Bi, for all i < T. Finally, we will show that the number of these vertices is linear a.a.s.

#### 3.1 The bootstrap percolation process inside B0

Let us condition on having N0 vertices in B0, where N0 satisﬁes (12). Note that by the triangle inequality, any two of them are within distance at most R and, therefore, they form a clique.

The random deletion of the edges incurs a random graph on N0 vertices, whose edges appear independently with probability ρ. That is, this subgraph of G(N;α,ν,ρ) is distributed

- as the binomial random graph G(N0,ρ). Since ρ is constant, G(N0,ρ) is connected a.a.s., and it will play the role of the “seed” graph from which the bootstrap process evolves.


Now assume that we infect each vertex independently with probability p = p(N), where pN1/2α = Ω(1) (as in Theorem 1.2(i)–(ii)). Let GC denote the subgraph of G(N;α,ν,ρ) which is induced by the vertices of type less than C together with the vertices of B0. The constant C will be speciﬁed later in our proof. We will show that if p(N) satisﬁes the conditions of Theorem 1.2 (i) and (ii), then B0 becomes infected a.a.s., in the former case or with positive probability, in the latter case, through the subgraph GC. More precisely, having shown this, we will further show that the infection spreads to most of the vertices of type at least C. Clearly, the two stages use disjoint sets of edges and we can expose them separately.

We now proceed with the analysis of the ﬁrst stage. By Lemma 2.9, conditional on the type tv, a vertex v has expected light degree (before the random edge deletions) H 1etv/2 ≤ EdC(v) ≤ H 2etv/2, where H 1,H 2 depend only on α and C. Thus, each vertex v in the set

R 2α − ω(N) ≤ tu ≤

R 2α

D1 := u :

+ ω(N) , (16)

has (conditional) expected light degree

EdC(v) ≥ H 1 exp(tv/2).

Hence, applying (9) we obtain that

etv/2 2 | tv ≤ e−Θ(etv/2),

P dC(v) ≤ H 1

which tends to zero exponentially fast for v ∈ D1, implying that in fact the conditional light degree of a vertex v ∈ D1 is, with high probability,

H 1 2

R 2α − ω(N) N 21αe−ω(N)/2.

- 1

- 2


dC(v) ≥ H 1etv/2/2 ≥

exp

Now assume we are in case (i) of Theorem 1.2, and set ϕ(N) := p(N)N1/2α; hence ϕ(N) is some increasing function growing to inﬁnity. This implies that for any vertex in D1, the (conditional) expected number of its neighbors that have type at most C and are externally infected is at least (up to multiplicative constants)

p(N)ρN 21αe−ω(N)/2 ϕ(N)e−ω(N)/2. Choosing ω(N) such that eω(N) = o(ϕ(N)) one has

ϕ(N)e−ω(N)/2 → ∞, which further implies that as N → ∞ we have

P v ∈ D1 has at least r initially infected neighbors → 1.

Also, it is not hard to see that a.a.s. D1 contains at least r vertices. Let v1,...,vr be an arbitrary collection of those. Conditional on their degrees being as above, the FKG inequality implies that as N → ∞

P v1,...,vr become infected → 1. (The FKG inequality is applied on the product space of initial infections, using the fact that the event that a vertex has at least r initially infected neighbors is increasing.) In other words, the random graph G(N0,ρ) contains at least r vertices which become infected after round 1. Now, Theorem 5.8 in [J LTV12] implies that a.a.s. the bootstrap percolation process in G(N0,ρ) with this initial set of infected vertices results in complete infection of the vertices in B0.

Similarly, now assume we are in case (ii) and set limN→∞ ϕ(N) = γ > 0. It is not hard to show that the set

R 2α ≤ tv ≤

R 2α

D2 := v :

+ ω(N) , (17)

is non-empty with probability which remains bounded away from 0 as N grows. In fact, the number of vertices therein follows asymptotically a Poisson distribution with constant parameter. In particular, looking at what happens asymptotically when N → ∞, we have that with probability bounded away from 0, it contains at least r vertices. Conditional on their degree, the expected number of infected neighbors that have type less than C of anyone of these vertices is

ρϕ(N) → ργ.

Hence, as N → ∞ the probability that a vertex v ∈ D2 has at least r initially infected neighbors of type less than C is bounded from below by some positive constant. Using again the FKG inequality, we deduce that with asymptotically positive probability these vertices become infected after the ﬁrst round, and a.a.s. subsequently infect all vertices in B0.

Therefore, from now in cases (i) and (ii) we will use these vertices as the root of the infection for those vertices that have type at least C.

We will denote by Kr(B0) the connected component induced by the infected vertices containing the (infected) vertices in B0. In our construction, we will inductively “discover” a subgraph of Kr(B0).

In particular, assume that we have discovered a certain set of vertices in Kr(B0) contained in the union ij−=01 Bj. Our inductive step consists in proving that with high probability there are many vertices in Bi which are connected to those in Kr(B0) through at least r edges that are retained after the percolation process.

#### 3.2 The base step starting from B0

In this section we show that the infection spreads from B0 to the external bands by showing that the core is very well connected with vertices in the outer bands. More precisely, we show that with very high probability outer vertices are contained in the disk of radius R of at least r vertices which are located inside B0, and, moreover, at least r of such connections survive the percolation process. Now we proceed with making this approach rigorous.

For i ≥ 1, deﬁne

θ(i) := 2(1 − ε)e21(ti+ti−1−R). (18)

Consider a point u on Bi−1. Lemma 2.1 implies that all points v ∈ Bi with θu,v ≤ θ(i) belong to the disk of radius R that is centered at u. The set of these points is illustrated by the shaded area in Figure 1.

O u

Bi−1

Bi

###### Figure 1: Set of points v ∈ Bi with θu,v ≤ θ(i): by Lemma 2.1, they are all inside the disk of radius R centered at u.

For every i > 0 we set

θ(i) ti

. (19)

Bi :=

Now consider the circle C1 (i.e., the set of points of type t1), divide it into consecutive blocks of angle B1, and discard the (unique, if it exists) remaining block of angle smaller than B1.

In what follows we shall be referring to these blocks as I1(1),I2(1),...,IK(1)

,

1

where the subscript is the index of the block (with K1 := 2π/B1 ) and the superscript denotes the index of the circle.

For each j ∈ {1,...,K1}, corresponding to each block Ij(1) we deﬁne a region (which will be called active area – cf. Figure 2) A(1)j as follows:

A(1)j := {x = (r,θ) : R − t1 < r < R − t0, θ ∈ Ij(1)}.

- A(1)1
- A(1)2
- A(1)3


O

B0

B1

Figure 2: Active areas in B1.

By taking the union over all blocks we deﬁne

K1

A(1)j ,

A(1) :=

j=1

with ri = R − ti, the above can be expressed as A(1) := x = (r,θ) : x ∈ A(1)j , for some j ∈ {1,...,K1} . (20) We color each block Ij(1) according to the following rule:

- (i) black, if for some integer k ≥ r, there are vertices x(0)1 ,x(0)2 ,...,x(0)k in B0 such that Ij(1) is completely contained in the k disks of radius R centered at x(0)1 ,x(0)2 ,...,x(0)k ;


- (ii) white, otherwise.


If a block Ij(1) is black, then any vertex that falls inside A(1)j will be connected to x(0)1 ,x(0)2 ,...,x(0)k . We show the following intermediate result.

- Lemma 3.1. The expected number of black blocks is bounded from below by K1(1 − e−t1).


Proof. If a vertex v ∈ B1 falls inside the active area A(1)j of a black block Ij(1), then v will be connected to at least r vertices in B0. As a consequence, if all vertices in B0 are infected, then vertex v will become infected as well. Moreover, if at least r of these edges incident to v are retained during the percolation process, then vertex v will be added to Kr(B0).

Deﬁne the event

B(1)j := {block Ij(1) is black}.

The probability of B(1)j is the probability of Ij(1) to be completely contained in the disk of k ≥ r vertices in B0. The probability that the disk of a certain vertex in B0 contains Ij(1) is

- at least θ(1)(1 − t−1 1)/(2π). Note that these events are independent. Therefore


θ(1)(1 − t−1 1) 2π ≥ r ≥ 1 − e−N0θ(1)/(4π), (21)

P(B(1)j ) ≥ P Bin N0,

where the second inequality would follow from (9), provided we had N0θ(1) → ∞. Now, to bound this expression for arbitrary i, we use (12). In particular, we have

2ν(1 − ε)4e12(ti+ti−1)−αti−1 ≤ θ(i)Ni−1 ≤ 2ν(1 + ε)3e12(ti+ti−1)−αti−1. Furthermore, from (5) it follows

- 1

- 2


4π 2ν(1 − ε)4

(ti + ti−1) − αti−1 = ln

ti ,

which in turn yields

(1 + ε)34π (1 − ε)4

4πti ≤ θ(i)Ni−1 ≤

ti. (22)

Thus N0θ(1) → ∞. As θ(1)N0 ≥ 4πt1, now (21) implies

P(B(1)j ) ≥ 1 − e−t1.

Denote by S1 the set of all black blocks and by S1 its cardinality. By what argued above, we have that ES1 is bounded from below by the quantity L1, deﬁned as

L1 := K1 1 − e−t1 , (23) which ﬁnishes the proof.

| |
|---|


Let Si be the collection of black blocks that will similarly be deﬁned on Ci, for i ≥ 1. From now on, let Θi denote the total angle that these blocks cover, and set Θ0 = 2π.

We will show that a suﬃcient number of them are black, so that Θi > π/2 a.a.s. (see Appendix A). Below we show this for S1, starting with the following Lemma.

- Lemma 3.2. There is a decreasing function ε1 := ε1(N) = o(1) such that with high probability we have S1 > L1(1 − ε1).


Proof. Note that changing the position of one vertex in B0 aﬀects the number of black blocks on C1 by at most

θ(1) B1

θ(1) θ(1)/t1

2

= 2

= 2t1.

This is the case as the disk of radius R around each vertex in B0 contains at most θ(1)/B1 intervals Ij(1). Hence, by inequality (11) we have

ε21E2S1 N0(2t1)2 ≤ exp −

ε21L21 N0(2t1)2

P S1 < (1 − ε1)ES1 | N0,Θ0 ≤ exp −

. (24)

Now we need to ﬁnd ε1 such that the absolute value of the exponent above tends to inﬁnity. Using the deﬁnitions of L1( 1/B1) and of B1(= θ(1)/t1) (cf. (23) and (19) respectively), this reduces to ﬁnding ε1 such that

ε21 B12N0t21

M1(2)(N) :=

ε21 (θ(1))2N0 → ∞.

Here we recall relation (22) (that is, θ(1)N0 t1), which implies that the above holds if ε1 θ(1)t1. (25)

Now, by (24) we have that the number of black blocks S1 (at this ﬁrst stage) is, with high probability, bounded from below by

L 1 := L1(1 − ε1), (26) for any function ε1 = ε1(N) = o(1) for which (25) holds.

| |
|---|


Now, let Θ1 denote the total angle covered by the blocks in S1. We conclude this section by showing the following result.

- Proposition 3.3. Asymptotically almost surely we have Θ1 > π.


Proof. By deﬁnition, Θ1 ≥ B1L 1 which, by Lemmas 3.1 and 3.2 is bounded from below by

Θ1 ≥ 2π(1 − e−t1)(1 − ε1) > π, (27) provided that N is suﬃciently large.

| |
|---|


### 4 Inductive Step

In this section we show that the infection spreads throughout the graph, and eventually reaches a linear fraction of vertices.

#### 4.1 Black Blocks

Assume that at step i − 1 (for any 2 ≤ i < T − 1) we have a collection of pairwise disjoint black blocks Si−1 each covering an angle equal to Bi−1 (recall its deﬁnition from (19)). The total angle that is covered by these black blocks is equal to Θi−1 = Si−1Bi−1, which we will show to be at least π/2 a.a.s. (see Appendix A).

We need to show that when passing from level i − 1 to level i, we still obtain a suﬃcient number of black blocks. We proceed with the details. First, we consider the projection of the blocks in Si−1 (i.e., the set of black blocks found on Ci−1) onto the outer boundary of Bi (i.e., on the circle Ci), and declare the images of these projections uncolored.

Subsequently, we divide each block (in the projection) into three parts, namely:

- • Parts (1) and (3): the ﬁrst and the last part of the block, both of angle θ(i);
- • Part (2): the remaining (central) part of the block, which has angle Bi−1 − 2θ(i).


Such a subdivision is shown in Figure 3.

θ(i)

O

Bi−1 − 2θ(i)

θ(i)

Ci−1

Ci

Figure 3: Subdivisions of inherited blocks.

Now, we keep only the central part of each block, discarding all the rest which as we will see later is negligible. We denote the collection of all remaining blocks of angle Bi−1 − 2θ(i) by S i−1. Note that |S i−1| = |Si−1| = Si−1. We split each such part into smaller uncolored blocks of angle Bi. Finally, discard the blocks that are leftover (if any). It is now clear that the number of (uncolored) blocks of angle Bi is bounded from below by

|S i−1|

Bi−1 − 2θ(i) Bi

= Si−1

Bi−1 Bi − 2ti . (28)

Recall that Θi−1 is the total angle covered by black blocks on the circle Ci−1, that is, the blocks in Si−1. We denote the blocks in S i−1 by Ij(i), for j = 1,...,Ki, with Ki := Θi−1/Bi .

Analogously to (20), we deﬁne the active area below the circle Ci as

A(i) := x = (r,θ) : ri−1 < r < ri, θ ∈ Ij(i) for some j ∈ {1,...,Ki} .

Given a block Ij(i) we deﬁne the following event:

B(ji) := for some k ≥ r there are vertices x(1i−1),x(2i−1),...,x(ki−1) ∈ Si−1, such that Ij(i) is completely contained in the k disks of radius R, centered at x(1i−1),x(2i−1),...,x(ki−1), AND at least r edges connecting each x(ji−1) with any vertex in Si−2 are retained during the edge percolation process .

Now we color each block Ij(i) black if and only if the event B(ji) is realized. At this point we show a generalization of Lemma 3.1.

- Lemma 4.1. The expected value of black blocks on Ci is bounded from below by


Bi−1

Bi − 2ti (1 − e−cρrti), for some c > 0 that does not depend on i.

Si−1

Proof. By the deﬁnition of the event B(ji), we ﬁrst need to ensure that the interval Ij(i) is contained in the disk of radius R of k ≥ r vertices, belonging to Si−1. We claim that for each vertex in v ∈ Bi−1 this occurs with probability at least (θ(i) − Bi)/(2π) = θ(i)(1 − t−i 1)/(2π). To see this, note that by Lemma 2.1, the intersection of the disk of radius R around v with Ci is an arc I(v) of angle at least 2θ(i). Therefore, I(v) covers a block Ij(i) for a range of the angle of v which is at least 2θ(i) − Bi (as the length of Ij(i) is equal to Bi).

Moreover, at least r edges must be connecting each such vertex with a vertex in Si−2 and are retained after the edge percolation process. Since this last event occurs with probability

- at least ρr, we have that


θ(i)(1 − t−i 1)ρr

P(B(ji)) ≥ P Bin Ni−1,

2π ≥ r | Ni−1 ≥ 1 − e−ctiρr,

which again follows from (9), for some c = c(ε) > 0, uniformly for all i > 0. Denote by Si the collection of black blocks that we end up with, and set Si := |Si|. Thus,

Bi−1

Bi − 2ti (1 − e−cρrti) =: Li, (29) which concludes the proof.

E(Si | Si−1,Ni−1) ≥ Si−1

| |
|---|


At this point we proceed as in Section 3 and show an analogue of Lemma 3.2.

Lemma 4.2. For every i > 0 let εi := (θ(i))1/6. For any 0 < i < T, conditional on Si−1 and Ni−1, with probability at least 1 − exp(−Θ 1/(ti(θ(i))2/3) we have

Si ≥ Li(1 − εi),

where Li is deﬁned in (29). Proof. Analogously to Lemma 3.2, we see that by changing the position of one vertex in Bi−1, one can change the number of blocks in Si by at most

θ(i) Bi

θ(i) θ(i)/ti

2

= 2

= 2ti.

Hence, by (11) we get

ε2i(E(Si | Si−1,Ni−1))2 Ni−1(2ti)2

P Si < (1 − εi)E(Si | Si−1,Ni−1) | Si−1,Ni−1 ≤ exp −

.

We will specify εi so that the absolute value of the above exponent tends to inﬁnity. Recall that

Θi−1 = Si−1Bi−1. (30)

Furthermore, if we demand that for i ≤ T we have Θi−1 > π/2 (see the deﬁnition of T in the next section), then the absolute value of the above exponent is bounded as follows:

(30) ε2iΘ2i−1

ε2iE2(Si | Si−1,Ni−1) Ni−1(2ti)2

ε2i(Si−1)2(Bi−1/Bi)2 Ni−1(2ti)2

Ni−1t2iBi2 ε2i Ni−1(ti)2Bi2

ε2i Ni−1(θ(i))2

=

.

By (22) we get

ε2i Ni−1θ(i)θ(i)

ε2i tiθ(i)

. Hence, analogously to the base case, we get that εi should satisfy

εi tiθ(i). We choose

1/6

εi := θ(i)

, and set

ε2i tiθ(i)

1 ti(θ(i))2/3

Mi(2)(N) :=

, ∀i ≥ 1. (31)

=

(2) i (N))

In other words, we apply Lemma 4.1 and get that with probability at least 1 − e−Θ(M

we have

Si ≥ Li(1 − εi) =: L i,

where Li has been deﬁned in (29). The proof of the fact that Mi(2)(N) → ∞ is deferred to Appendix C, hence the proof of the Lemma is concluded.

| |
|---|


(2)

This in turn implies that conditional on Si−1, with probability at least 1 − e−Θ(M

i (N)), the total length Θi of the set of blocks in Si is bounded from below by

1/6

L iBi = Si−1(Bi−1 − 2Biti)(1 − e−cρrti) 1 − θ(i)

.

By putting together these facts, we deduce the following result.

- Proposition 4.3. For any 1 < i < T, conditional on Θi−1, we have


θ(i) θ(i−1)ti−1 + e−cρrti + θ(i)

Θi ≥ Θi−1 1 − 2

1/6

,

with probability at least 1 − exp −Θ(Mi(2)(N)) . Proof. By Lemma 4.2, with high probability we have

Bi Bi−1

ti (1 − e−cρrti) 1 − θ(i)

Θi = SiBi ≥ L iBi = Si−1Bi−1 1 − 2

θ(i) θ(i−1)ti−1 (1 − e−cρrti) 1 − θ(i)

1/6

= Si−1Bi−1 1 − 2

θ(i) θ(i−1)ti−1 (1 − e−cρrti) 1 − θ(i)

= Θi−1 1 − 2

1/6

θ(i) θ(i−1)ti−1 + e−cρrti + θ(i)

≥ Θi−1 1 − 2

1/6

,

1/6

which concludes the proof.

(32)

| |
|---|


#### 4.2 Proof of Theorem 1.2

###### 4.2.1 Parts (i) and (ii)

Given a small value 0 < ε < 1, we choose a suitable large constant C = C(α,ν,ε) (which will be deﬁned explicitly in Appendix A) and we set

T1 := min{i : ti < C}, T2 := min{i : Θi < π/2}. (33) We take

T := min{T1,T2}. (34)

Let us denote by N i the number of vertices in Bi which belong to Kr(B0). The random variable N i stochastically dominates a binomial random variable. More speciﬁcally, with denoting stochastic domination, conditional on Ni and Θi, we have

N i Bin Ni,

Θi 2π

ρr . (35)

This is the case because each vertex in Bi falls inside A(i) with probability at least Θi/(2π) and, given this, it is connected to at least r of the vertices in A(i−1) with probability at least

ρr. Furthermore, these events are independent for the set of vertices in Bi, whereby (35) follows.

For i < T ≤ T2 (cf. Deﬁnitions (33), (34)), the stochastic inequality (35) implies that

ρr 4

Θi 2π

ρr ≥ Ni

E N i | Ni,Θi ≥ Ni

.

Now, for any value 0 < δ < 1, we can apply a standard Chernoﬀ bound (9), which leads to

ρr

4 | Ni,Θi ≤ e−δ2Niρr/8. (36) Hence conditional on Ei (deﬁned in (13)), for any δ ∈ (0,1), we have that a.a.s.

P N i < (1 − δ)Ni

ρr 4

N i ≥ (1 − δ)Ni

. (37)

Each of these vertices will be connected to the previous band by at least r edges, hence we conclude showing that there is a positive constant κ = κ(α,C,ε,δ,ρ,r) for which

|Kr(B0)| ≥

T−1

N i ≥ κN. (38)

i=0

Let us set

Mi(1)(N) := δ2Niρr/8. Hence, by choosing δ to be an arbitrarily small constant, with probability at least

T−1

1 −

i=1

(1)

(2)

e−M

i (N) + e−M

i (N) , (39)

(where Mi(2)(N) was deﬁned in (31)) we have for 0 < i < T

ρr 4

N i ≥ (1 − δ)Ni

.

Thus, the above implies that

T−1

T−1

T

ρr 4

ρr 4 ≥

ENi(1 − ε)(1 − δ)

N i ≥

Ni(1 − δ)

i=1

i=1

i=1

T−1

ρr 4

Claim 2.4

N(e−αti − e−αti−1)

≥ (1 − ε)3(1 − δ)

i=1

T−1

ρr 4

Ne−αti 1 − e−α(ti−1−ti)

≥ (1 − ε)3(1 − δ)

i=1

T−1

ρr 4

(49)

e−αti.

≥ (1 − ε)4(1 − δ)

N

i=1

Recall from Section 2.2 that λ = 2α − 1. In Appendix A, we show that

T−1

e−αti ≥ eαC/λ. (40)

i=1

Setting, for example,

(1 − ε)4(1 − δ)ρr 4

e−αC/λ,

κ = κ(α,C,ε,δ,ρ,r) :=

we deduce (38), concluding the proof of parts (i) (a.a.s. case) and (ii) (with positive probability case).

4.2.2 Part (iii) In this case it suﬃces to show that if ϕ(N) = p(N)N1/2α = o(1) and r ≥ 2, then

P there exists v ∈ VN has at least r initially infected neighbors = o(1). (41)

The proof is based on the fact that for any vertex the probability of having at least r ≥ 2 infected neighbors after the ﬁrst round is o(N−1).

More precisely, we resort to Lemma 2.7, which states that the degree d(v) of vertex v ∈ VN (conditional on the type) is such that

d(v)

N

Ber

=1

H2etv/2 N

, (42)

where H2 > 0 is as in Lemma 2.7, and Ber(p) denotes a Bernoulli random variable with parameter p. At this point we can distinguish between two cases: either tv ≥ R/10, or tv < R/10, hence divide the set VN into two disjoint sub-sets:

D3 := {v : R/10 ≤ tv ≤ R/2α + ω(N)}, and

D4 := {v : 0 < tv < R/10}. In the ﬁrst case, by Lemma 2.7 we have

H2etv/2 N ≥ 2H2etv/2

P(d(v) ≥ 2H2etv/2 | tv) ≤ P Bin N,

H2etv/2 8

(10)

≤ exp −

= o(N−1).

(43)

Now we proceed as follows: to simplify the notation in the next calculation, denote by in(v)

the number of initially infected neighbors of v. Hence

R/2α+ω(N)

P(in(v) ≥ r | tv)ρ(tv)dtv

P(v ∈ D3 and in(v) ≥ r) =

R/10

R/2α+ω(N)

P(in(v) ≥ r | tv,d(v) ≥ 2H2etv/2)P(d(v) ≥ 2H2etv/2 | tv)ρ(tv)dtv

=

R/10

R/2α+ω(N)

P(in(v) ≥ r | tv,d(v) < 2H2etv/2)P(d(v) < 2H2etv/2 | tv)ρ(tv)dtv

+

R/10

R/2α+ω(N)

P(d(v) ≥ 2H2etv/2 | tv)ρ(tv)dtv

≤

R/10

R/2α+ω(N)

P(in(v) ≥ r | tv,d(v) < 2H2etv/2)ρ(tv)dtv

+

R/10

R/2α+ω(N)

(43) and Lemma 2.7

≤ o(N−1) +

P Bin 2H2etv/2,p(N) ≥ r | tv ρ(tv)dtv.

R/10

Recall that r ≥ 2. Hence we obtain

R/2α+ω(N)

P Bin 2H2etv/2,p(N) ≥ r | tv ρ(tv)dtv

R/10

R/2α+ω(N)

r

e−αtdt

2H2et/2p(N)

R/10

R/2α+ω(N)

e(r/2−α)tdt r≥2 p(N)re(r/2−α)(R/2α+ω(N))

p(N)r

R/10

r

N−1e(r/2−α)ω(N) ϕ(N)rN−1e(r/2−α)ω(N).

p(N)N1/2α

By choosing ω(N) such that

ϕ(N) = o(e−(1/2−α/r)ω(N)), then the above calculation leads to R/2α+ω(N)

r

e−αtdt ϕ(N)rN−1e(r/2−α)ω(N) = o(N−1).

2H2et/2p(N)

R/10

Therefore we have

P(v ∈ D3 and in(v) ≥ r) = o(N−1). Now we take care of the vertices v ∈ D4. For simplicity of notation, we set

m := H2etv/2. (44) By Remark 2.8 we have that for every r ≥ 2

m ≥ H2 > 1. (45)

At this point on (42) we apply Le Cam’s Theorem, and conditional on tv we have

dTV(d(v),Dˆv) ≤ 2N

H2etv/2 N

2

,

where Dˆv denotes a random variable following a Poisson distribution with parameter m, and dTV is the total variation distance. Hence we obtain

H22etv N ≤ 2

H22eR/10 N

dTV(d(v),Dˆv) ≤ 2

= o(1). (46)

This immediately implies that d(v) is, with a very good approximation (as N → ∞), distributed like Dˆv. Furthermore, inequality (10) implies that for every v ∈ D4 we have

P(d(v) ≥ 2H2etv/2 | tv) ≤ exp(−H2eR/20/4). (47) From now on we shall be conditioning on the event that every v ∈ D4 has degree at most 2H2etv/2

tv≤R/10

≤ 2H2eR/20, which by (47) occurs with probability 1 − o N 1 . To simplify the next calculation, set

n := 2H2eR/20. This leads to

n

P(Bin(dv,p(N)) ≥ r | tv) =

P(Bin( ,p(N)) ≥ r | dv =  ,tv)P(dv = | tv)

=r

n

( p(N))r P(Dˆv = ) + P(dv = | tv) − P(Dˆv = )

≤

=r

n

n

H22eR/10 N

(46)

( p(N))r P(Dˆv = ) +

( p(N))r

≤

=r

=r

n

m !

p(N)r re−m

+ nr+1p(N)rH22e−2R/5.

=r

Now it is easy to see that there is a constant K := K(r) > 0 such that for all ∈ N we have

dr dmr

m !

rm

! ≤ K

. Therefore we obtain

∞

dr dmr

m !

P(Bin(dv,p(N)) ≥ r | tv) Kp(N)re−m

+ nr+1p(N)rH22e−2R/5

=r

∞

dr dmr

###### m !

Kp(N)re−m

+ (eR/20)r+1p(N)re−2R/5

=0

= Kp(N)re−mem + e(r+1)R/20p(N)re−2R/5.

Now we show that e(r+1)R/20p(N)re−2R/5 = o(N−1). This is easy to see, since r ≥ 2. In fact we have:

e(r+1)R/20p(N)re−2R/5 N(r+1)/10Nr/2α−r/2αp(N)rN−4/5

= ϕ(N)rNr(1/10−1/2α)+1/10−4/5 α<<1 ϕ(N)rN−2r/5−7/10 r<≥2 ϕ(N)rN−15/10 = o(N−1).

Hence, we can write

P(v ∈ D4 and in(v) ≥ r | tv) ≤ Kp(N)r + o(N−1). By integrating over the types and reasoning similarly as in the case of v ∈ D3 we have P(v ∈ D4 and in(v) ≥ r)

R/10

p(N)re−αtdt + o(N−1) p(N)r + o(N−1).

0

But p(N) N−1/(2α). Moreover, since 1/2 < α < 1 we have 2α < 2. So as r ≥ 2 it follows that 2rα > 1, whereby p(N)r N−1. Hence,

P(v ∈ D4 and in(v) ≥ r) = o(N−1).

The fact that this probability decreases asymptotically faster than N−1 implies that no vertex becomes infected during the ﬁrst round. In other words, |Af| = |A0| a.a.s. which concludes the proof of Theorem 1.2.

- 5 Proof of Corollary 1.3 and Theorem 1.4 In this section we show how to obtain Corollary 1.3 and Theorem 1.4 from Theorem 1.2.


Proof of Corollary 1.3. To show that there is a giant component, it suﬃces to set r = 1, and apply Theorem 1.2 with a high infection rate. In fact, if there is at least one infected vertex in a connected component, then the bootstrap percolation process will eventually infect the whole component. In this case, we can assume that p = p(N) is a positive constant. This implies that a.a.s. at least 1 vertex in B0 is initially infected and as the graph induced by these vertices is complete, it follows that all these vertices become infected during the second round. But by (38), it follows that a.a.s.

|K1(B0)| ≥ κN, for some κ > 0. Hence, the largest component of G(N;α,ν,ρ) has at least κN vertices. Proof of Theorem 1.4. The proof of this theorem is a byproduct of our proof. In fact, Kr(B0) by its construction is a subgraph of minimum degree at least r.

| |
|---|


| |
|---|


- A The deﬁnition of T and the proof of Lemma 2.2 The ﬁrst step to show Lemma 2.2 is given by the following result. Claim A.1. If i ≥ 1 is such that


2 ti

4π (1 − ε)4

1 − α >

ti , (48)

ln

then

ti < αti−1. Therefore

R 2

ti < αi

.

Proof. Recall the deﬁnition of ti from (5) and that λ = 2α − 1. Notice that Condition (48) can be rewritten as

4π ν(1 − ε)4

ti < (1 − α)ti. This condition implies that

2ln

4π ν(1 − ε)4

4π ν(1 − ε)4

ti≤ti−1

ti−1 < (λ + 1 − α)ti−1 = (2α − 1 + 1 − α)ti−1 = αti−1.

ti

< λti−1 + 2ln

ti = λti−1 + 2ln

| |
|---|


Now we make the deﬁnition of T more precise. In particular, recalling Equations (34) and

(33), here we specify the constant C = C(α,ν,ε), which must large enough so that all the following relations are satisﬁed:

e−Cα(1−α) < ε, (49) if x − 2ln

ν(1 − ε)4 4π

4π ν(1 − ε)4

x ≥ λC, then

< x, (50) 2 λC

- 1 − λ

- 2


4π ν(1 − ε)4

ln

, (51) e−cρrλC

λC <

1 8

1 − e−cρr(1−α)C <

, (52)

∞

(1 − η2) 2η

1 16

xe−xdx <

, (53)

(1−η2)

2 C

4 λ

α 1 − α2

2α (1 − α)2(1 + α)

C > max

. (54)

,

Let us see now what some of these conditions imply (the rest will become clear in the next few pages). Claim A.1 implies that

e−α(ti−1−ti) < e−αti−1(1−α).

Thus, (49) implies that for any 1 ≤ i < T we have

ti−1≥C

e−α(ti−1−ti)

< ε. (55)

- Condition (50) is used in order to ensure that for all 1 ≤ i ≤ T we have ti > λit0. Indeed, using (5) we have that for any 1 ≤ i ≤ T

λC ≤ λtT−1 ≤ λti−1 = ti − 2ln

4π ν(1 − ε)4

ti .

But then Condition (50) implies that ti > ν(1−ε)

4

4π , whereby ln ν(1 4−πε)4ti > 0. In turn, ti > λti−1 ≥ λC, for any i ≤ T. (56)

- Condition (51) together with the previous observation (ti > λC, for any i ≤ T) imply that the hypothesis of Claim A.1 holds for all i ≤ T. Hence, T = O(log R) as in Lemma 2.2


Proof of (40) As shown in Proposition 4.3, for all 0 < i < T with probability bounded from below by 1 − exp(−Θ Mi(2)(N) we have

θ(i)

θ(i−1)ti−1 + e−cρrti + θ(i) 1/6 . Now note that if this event is realized for all j ≤ i < T, we deduce that

Θi ≥ Θi−1 1 − 2

- i
- j=2


θ(j) θ(j−1)tj−1 + e−cρrtj + θ(i) 1/6

Θi ≥ Θ1

1 − 2

 1 −

 .

T−1

θ(j) θ(j−1)tj−1 + e−cρrtj + θ(j) 1/6

≥ Θ1

2

j=2

In the next section we use Conditions (52)–(54) to show that for N is suﬃciently large we have

T−1

T−1

T−1

θ(i) θ(i−1)ti−1 <

1 16

1 8

1 8

1/6

e−cρrti <

θ(i)

; and

; and

<

. (57)

i=2

i=2

i=2

Hence, for all 0 ≤ i < T1 (with T1 deﬁned in (33))

3 8

π 2

Θi ≥ Θ1 1 −

>

, (58)

which in turn implies that in relation (34) we have T = min{T1,T2} = T1. Moreover, this occurs with probability at least 1 − Ti=2−1 exp −Θ(Mi(2)(N)) . If T = T1, then (56) implies that

T−1

T−1

T−1

1

1

e−α

e−α

λitT ≥

λiC ≥ e−αC/λ.

e−αti ≥

i=1

i=1

i=1

### B Bounds on the error terms in (57)

Bound on ﬁrst error term Here we show that Ti=2 θ(θi(−i)1)ti−1 < 1/16, when N is large enough. First note that

T

θ(i) θ(i−1)ti−1 =

i=2

T

ti−1e(ti−ti−2)/2 =

i=2

T−1

tie(ti+1−ti−1)/2.

i=1

By Claim A.1, we have ti+1 < αti and ti−1 > ti/α. Thereby, ti+1 − ti−1 < ti(α − 1/α). So we have

T−1

T−1

T

θ(i) θ(i−1)ti−1 ≤

1 α − α tie−

2α 1 − α2

- 1

- 2


ti

ti

2 (α1−α) =

2 (α1−α).

tie−

i=1

i=1

i=2

Now, the last sum can be bounded as follows:

T−1

- 1

- 2


i=1

1 α − α tie−

ti

2 (α1−α) ≤

∞

xe−xdx ≤

- 1

- 2(α1−α)tT−1


∞

xe−xdx.

- 1

- 2(α1−α)λC−1


Let us set η := 21 α 1 − α . Indeed, this is bound holds provided that C is large enough so that for any x > ηλC − 1, the function xe−x is decreasing, namely for x > 1, and, moreover,

η(ti−1 − ti) ≥ 1.

In particular, the former holds if C > λ4 1−αα2, which is implied by Condition (54). Moreover, we have

ti−1 − ti > (1 − α)ti−1 > (1 − α)C So if η(1 − α)C > 1, then η(ti−1 − ti) ≥ 1 and the approximation of the sum by an integral is valid. This condition is C > η(11−α) = (1−α)22α(1+α), which is again implied by (54) Therefore, bounding the sum by the integral is valid.

###### Bound on the second error term Now, we verify that

T

1 8

e−cρrti <

.

j=2

As ti − ti−1 < (α − 1)C, we can write

T

e−cρrtj < e−cρrtT

j=2

∞

e−jcρr(1−α)C.

j=0

Also, as we have shown above tT > λC. Therefore,

e−cρrtT

∞

e−cρrλC 1 − e−cρr(1−α)C

1 8

(52)

e−jcρr(1−α)C <

.

<

j=0

Bound on the third error term Now we need to check that, when N is large enough, we get

T

1/6

θ(i)

< 1/8.

i=2

To show this, we use Claim A.1, which holds by assumption (51). We have that

T

T

T

ti−1<R/2

1/6

e1/12(ti+ti−1−R)

e1/12(ti−R/2)

θ(i)

≤

=

i=2

i=2

i=2

T

T

ti<αit0

e1/12(αi−1)R/2 = e−R/24

eαiR/24

≤

i=1

i=1

≤ e−R/24TeαR/24. Since α < 1 and T = O (lnR) by Lemma 2.2, the bound follows.

### C Proof of (39)

We conclude our proof showing that the sum of the the error terms obtained in (36) and (31) is of order o(1), i.e., that (39) is 1 − o(1).

Since the event Ei (deﬁned in Equation (13)) is realized, the lower bound on Ni given by

(12) implies that there is a constant ξ(1) > 0 such that for N large enough

Mi(1)(N) ≥ ξ(1)N1−α, 0 ≤ i < T. A straightforward calculation gives

T−1

(1)

i (N) ≤ Te−ξ(1)N1−α = o(1),

e−M

i=1

where we used the fact that T = O(lnR).

Now we seek the analogous relation for Mi(2)(N), which was deﬁned in (31). Using the deﬁnition of θ(i) and the fact that ti ≤ R/2 for all i ≥ 0, we see that there is a constant ξ > 0 such that for all 1 ≤ i < T

Claim A.1

≤ ξRe(αiR/2−R/2)/3 ≤ ξRe(α−1)R/6 e(α−1)R/12,

ti(θ(i))2/3 ξRe(ti−R/2)/3

where the last asymptotic inequality holds for large enough N, and the one before the last is due to the fact that α < 1.

Therefore, there is a constant ξ(2) > 0 such that for N suﬃciently large for all 0 < i < T

(31)

Mi(2)(N)

≥ ξ(2)N(1−α)/6. which implies

T−1

(2)

###### i (N) ≤ Te−ξ(2)N(1−α)/6 = o(1).

e−M

i=1

Hence (38) holds with probability bounded from below by

T−1

i=1

T−1

(1)

(2)

1 − e−M

i (N) 1 − e−M

i (N) ≥ 1 −

i=1

(1)

(2)

e−M

i (N) + e−M

i (N) = 1 − o(1).

### References

[AB02] R. Albert and A.-L. Barab´si, Statistical mechanics of complex networks, Reviews of Modern Physics 74 (2002), 47–97.

[ACM14] H. Amini, R. Cont, and A. Minca, Resilience to contagion in ﬁnancial networks, Mathematical Finance (2014), 37 pages.

[AF14] H. Amini and N. Fountoulakis, Bootstrap percolation in power-law random graphs, Journal of Statistical Physics 155 (2014), 72–92.

[AL03] J. Adler and U. Lev, Bootstrap percolation: visualizations and applications, Brazilian Journal of Physics 33 (2003), no. 3, 641–644.

[Ami10] H. Amini, Bootstrap percolation in living neural networks, Journal of Statistical Physics 141 (2010), 459–475.

[BA99] A.-L. Barab´si and R. Albert, Emergence of scaling in random networks, Science

286 (1999), 509–512.

[BFM15] M. Bode, N. Fountoulakis, and T. Mu¨ller, On the largest component of a hyperbolic model of complex networks”, Electronic Journal of Combinatorics, to appear, 43 pages, 2015.

[BJR07] B. Bollob´as, S. Janson, and O. Riordan, The phase transition in inhomogeneous random graphs, Random Structures and Algorithms 31 (2007), 3–122.

[CF15] E. Candellero and N. Fountoulakis, Clustering and the hyperbolic geometry of complex networks, Internet Mathematics, to appear, 51 pages, 2015.

- [CL02a] F. Chung and L. Lu, The average distances in random graphs with given expected degrees, Proc. Natl. Acad. Sci. USA 99 (2002), 15879–15882.
- [CL02b] , Connected components in random graphs with given expected degree sequences, Annals of Combinatorics 6 (2002), 125–145.


[CL06] , Complex graphs and networks, CBMS Regional Conference Series in Mathematics, vol. 107, Published for the Conference Board of the Mathematical Sciences, Washington, DC; by the American Mathematical Society, Providence, RI, 2006.

[CLR79] J. Chalupa, P. L. Leath, and G. R. Reich, Bootstrap percolation on a Bethe lattice, Journal of Physics C: Solid State Physics 12 (1979), L31–L35.

[Coo04] C. Cooper, The cores of random hypergraphs with a given degree sequence, Random Structures Algorithms 25 (2004), no. 4, 353–375.

[CW06] J. Cain and N. Wormald, Encores on cores, Electron. J. Combin. 13 (2006), no. 1, Research Paper 81, 13 pp. (electronic).

[GPP12] L. Gugelmann, K. Panagiotou, and U. Peter, Random hyperbolic graphs: degree sequence and clustering, Proceedings of the 39th International Colloquium on Automata, Languages and Programming (A. Czumaj et al. Eds.), Lecture Notes in Computer Science, vol. 7392, 2012, pp. 573–585.

[J LTV12] S. Janson, T.  Luczak, T. Turova, and T. Vallier, Bootstrap percolation on the random graph Gn,p, Ann. Appl. Probab. 22 (2012), no. 5, 1989–2047.

[KM15] M. Kiwi and D. Mitsche, A bound on the diameter of random hyperbolic graphs, Proceedings of the 12th Workshop on Analytic Algorithmics and Combinatorics, ANALCO (R. Sedgewick and R.D. Ward, Eds.), SIAM, 2015, pp. 26–39.

[KPK+10] D. Krioukov, F. Papadopoulos, M. Kitsak, A. Vahdat, and M. Bogun˜´, Hyperbolic geometry of complex networks, Phys. Rev. E (3) 82 (2010), no. 3, 036106.

[PSW96] B. Pittel, J. Spencer, and N. Wormald, Sudden emergence of a giant k-core in a random graph, J. Combin. Theory Ser. B 67 (1996), no. 1, 111–151.

[SDS02] S. Sabhapandit, D. Dhar, and P. Shukla, Hysteresis in the random-ﬁeld Ising model and bootstrap percolation, Physical Review Letters 88 (2002), no. 19, 197202.

[S¨d02] B. S¨derberg, General formalism for inhomogeneous random graphs, Phys. Rev. E 66 (2002), 066121.

[TBF06] C. Toninelli, G. Biroli, and D. S. Fisher, Jamming percolation and glass transitions in lattice models, Physical Review Letters 96 (2006), no. 3, 035702.

[TE09] T. Tlusty and J.P. Eckmann, Remarks on bootstrap percolation in metric networks, Journal of Physics A: Mathematical and Theoretical 42 (2009), 205004.

[vdH] R. van der Hofstad, Random graphs and complex networks, available at http://www.win.tue.nl/∼rhofstad/.

[WS98] D. J. Watts and S. H. Strogatz, Collective dynamics of “small-world” networks, Nature 393 (1998), 440–442.

