arXiv:1506.01255v1[math.PR]3Jun2015

FIRST PASSAGE PERCOLATION ON RANDOM GRAPHS WITH INFINITE VARIANCE DEGREES

By Enrico Baroni Remco van der Hofstad Julia´ Komjathy´

Eindhoven University of Technology

We prove non-universality results for ﬁrst-passage percolation on the conﬁguration model with i.i.d. degrees having inﬁnite variance. We focus on the weight of the optimal path between two uniform vertices. Depending on the properties of the weight distribution, we use an example-based approach and show that rather diﬀerent behaviors are possible. When the weights are a.s. larger than a constant, the weight and number of edges in the graph grow proportionally to log log n, as for the graph distances. On the other hand, when the continuous-time branching process describing the ﬁrst passage percolation exploration through the graph reaches inﬁnitely many vertices in ﬁnite time, the weight converges to the sum of two i.i.d. random variables representing the explosion times of the processes started from the two sources. This non-universality is in sharp contrast to the setting where the degree sequence has a ﬁnite variance [5].

1. Introduction.

1.1. The model. There is a wide literature on how complex networks appear in many diﬀerent situations as models for, e.g., communication networks [24], gene regulatory networks [7], electric power grids [1], the Internet [11], transportation systems [18], the World-Wide Web [3], citation networks [23] and social networks [2, 22]. All these examples deal with systems composed of many highly connected units. We use graphs denoted by G to model such settings. The ﬁrst mathematical model of such networks is the Erd˝os-Re´nyi graph (see [10]), in which there is a link between any pair of nodes independently with a certain probability, so the nodes have the same number of links on average. In recent years, however (mainly due to a large amount of available data), two characteristics for many of these networks have been observed. The ﬁrst is the so-called “small world phenomenon”, meaning that the graph distances between vertices are small. The second observed phenomenon is that some of the nodes have a large amount of links, and in particular the degrees of the vertices is close to a power-law distribution (see for instance [11]). One of the most studied properties of such, so-called scale-free random graphs, is the spread of information on them.

In particular, we are interested in the following setting: we have a transportation network that transports a ﬂow through the edges of the network. Basically, the behaviour of the ﬂow depends on two factors: the number of edges in the shortest path between the vertices of the network and the passage cost through the edges of it. From a mathematical point of view, this leads us to study distances on random graphs having inﬁnite-variance degrees using ﬁrst-passage percolation, where the weights on edges are given by independent and identically distributed (i.i.d.) random variables.

![image 1](<2015-baroni-first-passage-percolation-random_images/imageFile1.png>)

AMS 2000 subject classiﬁcations: Primary 60J10, 60D05, 37A25 Keywords and phrases: Conﬁguration model, power-law degrees, ﬁrst passage percolation, universality

1

First-passage percolation was ﬁrst introduced by Hammersley and Welsh (see [8]), and is obtained by assigning the collection of i.i.d. random weights (Ye)e∈E to the edges E of the graph G. If u is a ﬁxed vertex in G, then we deﬁne the passage-time from u to a vertex v as

- (1.1) Wn(u,v) := min π: u→v

e∈π

Ye,

where the minimum is taken over all paths of the form π ⊂ E from u to v. Here, we set Wn(u,v) = 0 when u = v, while Wn(u,v) = ∞ when u and v are not connected.

The main object of study in ﬁrst-passage percolation is the ball of radius t in the Wn-metric given by

- (1.2) B(t) = {v ∈ G: Wn(u,v) ≤ t}.

More precisely, in this paper we study the conﬁguration model CMn(D) on n vertices, where each vertex has a number of half-edges given by i.i.d. random variables (Dv)v∈[n], where [n] = {1,... n} distributed as D, with a power-law distribution that satisﬁes

- (1.3)

c1 xτ−1 ≤ 1 − FD(x) = P(D > x) ≤

![image 2](<2015-baroni-first-passage-percolation-random_images/imageFile2.png>)

C1 xτ−1

![image 3](<2015-baroni-first-passage-percolation-random_images/imageFile3.png>)

. We further assume that

- (1.4) P(D ≥ 2) = 1,

and that τ ∈ (2,3), so that the degrees have ﬁnite mean, but inﬁnite variance. We pair these halfedges uniformly at random and without replacement. Condition (1.4) guarantees that almost all the vertices of the graph lie in the same connected component, or, equivalently, the giant component has size close to n (see [20, Proposition 2.1]). All edges are equipped with i.i.d.

weights or lengths with distribution function FY (y) = P(Y ≤ y), where Y is a non-negative random variable having a continous distribution. We assume P(Y ≥ 0) = 1. Let B deﬁned as the random variable D⋆ − 1 through the size-biased distribution of the variable D⋆, i.e.,

P(D⋆ = k) :=

k E[D]

![image 4](<2015-baroni-first-passage-percolation-random_images/imageFile4.png>)

- (1.5) P(D = k), and

P(B = k) := P(D⋆ = k + 1) =

k + 1 E[D]

![image 5](<2015-baroni-first-passage-percolation-random_images/imageFile5.png>)

- (1.6) P(D = k + 1).

Then, with FB(x) := P(B ≤ x), there exist constants 0 < c⋆1 < C1⋆ < ∞ such that (see e.g., [20, Theorem 3.1])

- (1.7)


C1⋆ xτ−2

c⋆1 xτ−2 ≤ 1 − FB(x) = P(B > x) ≤

.

![image 6](<2015-baroni-first-passage-percolation-random_images/imageFile6.png>)

![image 7](<2015-baroni-first-passage-percolation-random_images/imageFile7.png>)

Let hB(s) = ∞k=1 P(B = k)sj be the probability generating function of B.

Notation. We use the following standard concepts and notation. We say that a sequence of random variables converges in probability to a random variable X, and we write Xn →P X if, for every ε > 0, P(|Xn − X| > ε) → 0. Further, we say that Xn converges to X in distribution, and we write Xn →d X, if limn→∞ P(Xn ≤ x) = P(X ≤ x) for every x for which FX(x) = P(X ≤ x) is continous. Finally we say that a sequence En of events holds w.h.p. (with high probability) if limn→∞ P(En) = 1.

The main tool in the proof of typical distances is a connection to continuous-time (agedependent) branching processes:

Definition 1.1 (Age-dependent branching process). We call a branching process age-dependent,

if individuals have random life-lengths with distribution function FY with FY (0) = 0. At death, an individual produces oﬀspring of random size with probability generating function h(s) and all life-lengths and family sizes are independent of each other. We assume that the process starts at time t = 0 with one individual of age 0.

1.2. Previous results. We investigate the total weight of the shortest-weight path between two uniformly chosen vertices, as in (1.1). When Y has exponential distribution with mean 1, then, in [4, Theorem 3.2], the following result was proved for Wn(u,v):

Theorem 1.2 ([4]). Consider the conﬁguration model CMn(D) where the degrees are i.i.d. with distribution function FD satisfying (1.3), and with i.i.d. edge weights Y having exponential distribution with mean 1. Then, the weight Wn(u,v) of the shortest-weight path between two uniformly chosen vertices u and v satisﬁes

- (1.8) Wn(u,v) →d V (1) + V (2),

where V (1),V (2) are independent copies of the explosion time of a continous-time age-dependent branching process with inﬁnite-mean oﬀspring distribution that we deﬁne below.

The ﬁrst of our main results extends Theorem 1.2 to a more general family of edge weights. For this, let (hB,FY ) be a modiﬁed age-dependent branching process where individuals have random life-lengths with distribution FY (t) and, at death, the ﬁrst individual (the root) produces a family of random size with oﬀspring distribution FD and the further generations have oﬀspring distribution FB. Recall that hB(s) denotes the probability generating function of the distribution FB.

Definition 1.3 (Explosive age-dependent process). We say that the branching process (hB,FY ) is explosive if there is a positive probability that Nt = ∞, where Nt denotes the number of individuals alive at some ﬁnite time t > 0. Otherwise, it is called conservative.

The following theorem from [13] shows that for every oﬀspring distribution FB with inﬁnite expectation, there is a weight distribution FY for which the process is explosive:

Theorem 1.4 ([13, Theorem 6]). Given hB such that h′B(1) = ∞, there exists a FY with FY (0) = 0 such that the process (hB,FY ) is explosive.

The next theorem [13, Corollary 4.1], compares the branching process (hB,FY ) to a Markov branching process:

Theorem 1.5 (Comparison to Markov branching processes). If there exists T > 0 and constants β > α > 0 such that αt ≤ FY (t) ≤ βt for 0 ≤ t ≤ T, then the process (hB,FY ) is explosive if and only if h′B(1) = ∞ and

- (1.9)


1

ds s − h(s)

< ∞

![image 8](<2015-baroni-first-passage-percolation-random_images/imageFile8.png>)

1−ε

for some ε > 0.

The condition in (1.9) is necessary and suﬃcient for explosiveness for Markov branching processes, as proved by Harris in [14].

1.3. Our results. The ﬁrst result of our paper is the following theorem:

Theorem 1.6 (Universality class for explosive weights). Consider the conﬁguration model with i.i.d. degrees having distribution function FD satisfying (1.3), and i.i.d. edge weights (Ye)e∈E having distribution FY . Further suppose that (hB,FY ) is explosive. If u and v are two uniformly chosen vertices, then

- (1.10) Wn(u,v) →d V (1) + V (2),

where V (1) and V (2) are two i.i.d. copies of the explosion time of the process (hB,FY ) deﬁned above.

Theorem 1.6 implies that all edge weights for which the age-dependent branching process that approximates the local neighborhoods of vertices is explosive are in the same universality class. We next investigate one class of random edge weights that are in a diﬀerent universality class. For this, it is useful to deﬁne the hopcount as the number of edges in the shortest-weight path:

Definition 1.7. The hopcount Hn(u,v) is the number of edges in the shortest-weight path between u and v.

The next result determines the asymptotic behaviour of the weight and the hopcount in a diﬀerent setting. We now consider the case when the weight is given by Y = c + X such that X is a random variable with inf supp(X) = 0, where c is a constant satisfying c > 0 and supp(X) is the support of the distribution. Without loss of generality, we may assume that c = 1. Then, our result in this setting is the following theorem:

Theorem 1.8 (Universality class for weights with inf supp(X) > 0). Consider the conﬁguration model with i.i.d. degrees from distribution FD satisfying (1.3), and i.i.d. edge weights

- (1.11) Y = 1 + X, where inf supp(X) = 0. Then,
- (1.12)

Wn(u,v) log log n

![image 9](<2015-baroni-first-passage-percolation-random_images/imageFile9.png>)

−→d

2 |log (τ − 2)|

![image 10](<2015-baroni-first-passage-percolation-random_images/imageFile10.png>)

,

Hn(u,v) log log n

![image 11](<2015-baroni-first-passage-percolation-random_images/imageFile11.png>)

−→d

2 |log (τ − 2)|

![image 12](<2015-baroni-first-passage-percolation-random_images/imageFile12.png>)

.

Let us comment on the result in Theorem 1.8. Deﬁne the graph distance Dn(u,v) between two vertices u,v ∈ [n] as the minimal number of edges on a path connecting u and v. In [16, Theorem 3.1], it was shown that

- (1.13) Dn(u,v) log log n


2 |log (τ − 2)|

−→P

.

![image 13](<2015-baroni-first-passage-percolation-random_images/imageFile13.png>)

![image 14](<2015-baroni-first-passage-percolation-random_images/imageFile14.png>)

Then, Theorem 1.8 shows that the shortest path in terms of its number of edges is such that the average additional weight compared to the graph distance vanishes. In other words, there must exist an almost shortest path for which the sum of weights is o(log log n).

1.4. Overview of the proofs of Theorems 1.6–1.8. In this section we present an overview of the proof of our main results.

Overview of the proof of Theorem 1.6. The key ideas in the proof of Theorem 1.6 are the following:

- 1. Perfect coupling to an age-dependent branching process and lower bound on the weight. First we couple the growth of two shortest-weight graphs from u and v respectively, here

denoted as SWGunρ and SWGvnρ, where u and v are uniformly chosen vertices, to two agedependent branching processes. This can be successfully performed until the time that they reach size nρ, where ρ is a small constant. With high probability these two graphs representing the local neighborhoods of u and v, are disjoint trees (see [4, Proposition 4.7]). The lower bound in Theorem 1.6 follows immediately from the coupling because the two shortest-weight graphs are with high probability disjoint. We deﬁne Nt(1) as the number of dead individuals in the age-dependent branching process associated to SWGvnρ (or SWGunρ) at time t, and

(1.14) Vm(1) = min{t: |Nt(1)| = m}.

Also, if n is large enough, Vm(1) is the time for the SWGvm to reach the mth vertex for any m < nρ, where ρ > 0 is a small constant. If V∞(1) = min{t: |Nt(1)| = ∞}, then it coincides with the explosion time of the process that we call V (1).

- 2. Upper bound on the weights


To prove the upper bound Wn(u,v) ≤ Vn(1)ρ + Vn(2)ρ + ε where ε > 0 is some arbitrary small constant, we show that whp there exists a path that connects SWGvnρ to SWGunρ with weight at most ε. Then we use that (Vn(1)ρ ,Vn(2)ρ ) →d (V (1),V (2)). We ﬁnd this path using percolation on the so-called core of the graph consisting of vertices of large degrees. In more detail, we only keep edges with weight less than ε′ and then show that there still remains a path via the high degree vertices from SWGvnρ to SWGunρ that has a number of edges not depending on n. Picking ε′ small enough ﬁnishes the proof.

Overview of the proof of Theorem 1.8. The proof consists in verifying that, with high probability and for all ε > 0,

- (1.15)

2(1 − ε)log log n |log(τ − 2)|

![image 15](<2015-baroni-first-passage-percolation-random_images/imageFile15.png>)

≤ Dn(u,v) ≤ Hn(u,v) ≤ Wn(u,v) ≤

2(1 + ε) |log(τ − 2)|

![image 16](<2015-baroni-first-passage-percolation-random_images/imageFile16.png>)

log log n.

The ﬁrst inequality has been shown in [16, Theorem 1.2], the second and the third are obvious since every path with q edges has weight greater than q for our choice of Y . It remains to prove the upper bound on Wn(u,v):

Proposition 1.9 (Upper bound on weight when inf supp(X) > 0). Consider the conﬁguration model with i.i.d. degrees from distribution FD satisfying (1.3), and i.i.d. edge weights Y = 1 + X with inf supp(X) = 0. If u and v are two uniformly chosen vertices in [n], then, for any ﬁxed ε > 0 and with high probability as n → ∞,

- (1.16)


Wn(u,v) log log n ≤

2(1 + ε) |log(τ − 2)|

.

![image 17](<2015-baroni-first-passage-percolation-random_images/imageFile17.png>)

![image 18](<2015-baroni-first-passage-percolation-random_images/imageFile18.png>)

Theorem 1.8 follows directly from Proposition 1.9 and (1.15).

1.5. Discussions and related problems. We can consider diﬀerent metrics and topologies on the same graph given by various notions of distances, an example being the graph distance Dn(u,v) between two vertices u and v. Another metric is deﬁned by Wn(u,v), while a third one is characterized by the hopcount Hn(u,v). In this last case we deal with a so-called pseudometric, since the triangle inequality does not necessarily hold. A natural question is whether these three metric spaces are similar. The result of this paper is that this is not the case for a large class of graphs, namely, the conﬁguration model with power-law degree exponent τ ∈ (2,3) and i.i.d. edge weights Y = 1 + X with inf supp(X) = 0. It has been proved (see [16, Theorem 1.1]) that the graph distance Dn(u,v) between two uniformly chosen vertices is proportional to log log n. Hence, these distances are ultra small. When the weights are independent and exponentially distributed, the asymptotic distribution for the minimum weight between two randomly chosen vertices is given by Theorem 1.2, see [4] while in the same paper it is shown that Hn(u,v) satisﬁes the following central limit theorem:

- (1.17)


Hn(u,v) − αlog n √α log n

→d Z,

![image 19](<2015-baroni-first-passage-percolation-random_images/imageFile19.png>)

![image 20](<2015-baroni-first-passage-percolation-random_images/imageFile20.png>)

where α = 2(ττ−−12) and Z has a standard normal distribution. In this regard, Theorem 1.8 shows the existence of a diﬀerent behaviour for the hopcount for weight distributions given in (1.11),

![image 21](<2015-baroni-first-passage-percolation-random_images/imageFile21.png>)

and so it shows that there exists diﬀerent universality classes for the hopcount. Thus, in the metric space deﬁned by Hn(u,v), under the hypothesis of Theorem 1.8, typical distances are small but not ultra-small, meaning that the geometry of the graph signiﬁcantly changes when switching from one metric to the other. It would be of interest to investigate the behaviour of Hn(u,v) in the explosive setting, and that of Wn(u,v) for more general edge weights.

The above results are in sharp contrast to the setting where the degree sequence of the conﬁguration model has ﬁnite variance, as investigated in [5] (see also [4] for the setting where the edge weights are exponentially distributed). Indeed, in [5], Bhamidi, the second author and Hooghiemstra show that when the degree sequence is of ﬁnite variance (with an extra logarithmic moment), then ﬁrst passage percolation has only one universality class in the sense that Wn(u,v) − γ log n converges in distribution for some γ > 0, while Hn(u,v) satisﬁes an asymptotic central limit theorem with asymptotic mean and variance proportional to log n (in [5], i.i.d. degrees are a special case, in the more general case, γ and α can depend on n). As we see for τ ∈ (2,3), the weight distribution has at least two universality classes, depending on whether the age-dependent branching process that approximates the local neighborhoods is explosive or not.

Recently, competition models have attracted considerable attention. In [9], the spread of two competing infections on the conﬁguration model with power-law exponent τ ∈ (2,3) and with i.i.d. exponential edge weights have been studied. The result is that one of the infection types will almost surely occupy all but a ﬁnite number of vertices. A natural question is whether these results still hold for passage times satisfying the explosive conditions given in this paper.

In the same graph setting, in [20] we have investigated the competition of two competing infections with ﬁxed, but not necessarily equal, speeds. The faster infection is shown to occupy almost all vertices, while the slower one can occupy only a random subpolynomial fraction of the vertices. More recently, the second and third author show that when the speeds are equal, then coexistence can occur, in the sense that both types can occupy a positive proportion of the graph [19]. It would be of interest to investigate whether this extends to the setting of Theorem

- 1.8.
- 2. Preliminaries. In this section, we give some preliminaries needed in our proofs.


2.1. Conﬁguration model and shortest-weight graphs. We obtain the conﬁguration model CMn(D) (see [6]) on [n] = {1,... ,n} with i.i.d. degree distribution D by the following procedure:

- (1) We assign to each vertex i ∈ [n] an i.i.d. random variable Di ∼ D describing the number of half-edges of that vertex.
- (2) Let |Ln| = ni=1 Di be the total number of half-edges in the graph. If |Ln| is odd, then we

add an extra half-edge to the vertex n. Let Ln = {h1,h2,... ,h|Ln|} be the ordered set of these half-edges.

- (3) We start pairing h1 with hi1, where hi1 is chosen uniformly at random in Ln \ {h1}. At the second step, we pick the ﬁrst unpaired half-edge hi2 and we pair it with a half-edge hi3 chosen uniformly at random in Ln \ {h1,hi2,hi3}. The k-th step consists in picking the ﬁrst half-edge hi2k in Ln \ {h1,hi2,hi3,hi4,... ,hi2k−1} and connecting it to a half-edge


chosen uniformly at random in Ln \ {h1,hi2,hi3,hi4,... ,hi2k}. (Stop) The process ends when there are no more half-edges to pair.

This process allows us to pick an arbitrary half-edge every time we start pairing a half-edge, i.e., the process of pairing is exchangeable. Hence, we can do this in the same order as the edge-weights require it, to get the vertices that are closest, in terms of weight, to u or to v.

We deﬁne the shortest-weight graph SWGvm, starting from vertex v, as follows. We start with a vertex v and we deﬁne SWGv0 = {v}. We deﬁne SWGvm as the ordered sequence {v,v1,y1,e1,v2,e2,y2,... ,vm,em,ym}, where vi are vertices, ei are edges, and yi is the weight of the edge yi deﬁned inductively as follows:

We start with vertex v. Then e1 is the edge with the minimal weight starting from v and v1 is the vertex that is at the other end of the newly paired edge e1, while y1 = Ye1 is the weight on the edge e1. In general, vi is the vertex for which

- (2.1) vi = arg min w∈[n]\{v1,...,vi−1}


Wn(v,w).

Here we note that the minimum is always attained by a vertex vi that is a neighbor of a vertex in {v1,... ,vi−1} that is not in {v1,... ,vi−1} itself. Also, ei is the edge that connects vi to one of the vertices in SWGvi−1 and yi = Yei its weight. This process is generally called “the exploration process” of the neighborhood of v in the graph, in the context of ﬁrst-passage percolation on the conﬁguration model it appears for instance in [4].

2.2. The weighted graph and the age-dependent branching process. Our aim in proving Theorem 1.6 is to give the weight of the shortest-weight path in terms of the explosion time of an age-dependent branching process. Let B˜i stand for the number of edges minus 1 that are incident to vi. In each step of the growth of CMn(D), an arbitrary half-edge is chosen and paired to a uniformly chosen unpaired half-edge. Thus, the probability of picking a half-edge that is incident to a vertex with j other half-edges is proportional to (j + 1)P(D = j), and thus we get the size-biased distribution (1.5) as a natural candidate for the forward degrees of the vertices vi in the exploration process. More precisely, by [4, Prop.4.7], the variables ( Bi)ni=1ρ can be coupled to an i.i.d. sequence of random variables (Bi)ni=2ρ with the size-biased distribution B given in (1.5). We cite this proposition for the reader’s convenience:1

![image 22](<2015-baroni-first-passage-percolation-random_images/imageFile22.png>)

1Be aware of the diﬀerences in notation between [4] and this paper. What we call Bi is called Bi(ind) in [4], and what we call Bi is called Bi in [4].

Proposition 2.1 ([4, Proposition 2.1]). There exists 0 < ρ < 1 such that the random vector ( Bm)nmρ=2 can be coupled to an independent sequence of random variables (Bm)nmρ=2 with probability mass function B given in (1.5) and ( Bm)nmρ=2 = (Bm)nmρ=2 w.h.p.

Proof. See [4, Proposition 4.5] and the proof of Proposition 4.7 in [4, Appendix A.2].

![image 23](<2015-baroni-first-passage-percolation-random_images/imageFile23.png>)

![image 24](<2015-baroni-first-passage-percolation-random_images/imageFile24.png>)

![image 25](<2015-baroni-first-passage-percolation-random_images/imageFile25.png>)

![image 26](<2015-baroni-first-passage-percolation-random_images/imageFile26.png>)

An immediate consequence of Proposition 2.1 is that the SWGvnρ is w.h.p. a tree. We now

consider a modiﬁed age-dependent process deﬁned as follows: ⊲ Start with the root which dies immediately giving rise to D children. ⊲ Each alive oﬀspring lives for a random amount of time, with distribution FY independent

from any other randomness involved.

⊲ When the mth (where m > 1) vertex dies, it leaves behind Bm alive oﬀspring. The process is a modiﬁed age-dependent two-stage process in the sense that the oﬀspring in the ﬁrst generation is diﬀerent from the oﬀspring in second and further generations.

The construction of the SWGvnρ is equivalent to this construction, but then on the graph CMn(D) rather than on the branching process tree. In Theorem 1.6, we assume that (hB,FY ) is s.t. the process is explosive, where hB is the probability generating function of B = D⋆ − 1.

2.3. Bond percolation on conﬁguration model. Bond percolation on any graph is deﬁned as follows (see [17]): we delete every existing edge independently with probability 1 − p. The remaining edges form the percolated graph that we denote by Gp. For the conﬁguration model, this process is equivalent to the following (see [17, Remark 1.1.]): we consider every half-edge independently, and we remove it with probability 1 −

√p, for a ﬁxed p s.t. 0 ≤ p ≤ 1, then we connect it with a new vertex with degree 1. We ﬁnally remove these new vertices, and their incident edges. Since an edge consists of two half-edges, and each survives with probability √p, this is equivalent to randomly deleting an edge with probability 1−p, independently of all other edges, so the two processes are equivalent. In our case p = p(ε0) will be the probability that the weight of an edge is less than ε0, for an appropriately chosen ε0 > 0. So Gp(ε0) consists only of edges of length less than ε0. We consider Gp as a subgraph of G with the same vertices, but with fewer edges.

![image 27](<2015-baroni-first-passage-percolation-random_images/imageFile27.png>)

![image 28](<2015-baroni-first-passage-percolation-random_images/imageFile28.png>)

Janson [17] has shown that the percolated conﬁguration model is equal in distribution to a conﬁguration model with a new degree distribution Dp = Bin(D,√p), except for some extra vertices of degree 1 that are irrelevant to us. In the next lemma, we show that this new degree sequence again satisﬁes a power law:

![image 29](<2015-baroni-first-passage-percolation-random_images/imageFile29.png>)

Lemma 2.2 (Percolation on the CM). Fix p ∈ (0,1]. Let G = CMn(D) be a conﬁguration model with degree distribution satisfying (1.3). Then, Gp can be representeted as a conﬁguration model with degree distribution that again obeys a power-law distribution of the same form of

- (1.3), but with diﬀerent constants c1 and C1.

Before giving the proof, we state a useful lemma about concentration of binomial random variables:

Lemma 2.3 (Concentration of binomial random variables). Let R be a binomial random variable. Then

- (2.2) P(R ≥ 2E[R]) ≤ exp{−E[R]/8},


- (2.3) P(R ≤ E[R]/2) ≤ exp{−E[R]/8}.


Proof. See e.g., [15, Theorem 2.19].

![image 30](<2015-baroni-first-passage-percolation-random_images/imageFile30.png>)

![image 31](<2015-baroni-first-passage-percolation-random_images/imageFile31.png>)

![image 32](<2015-baroni-first-passage-percolation-random_images/imageFile32.png>)

![image 33](<2015-baroni-first-passage-percolation-random_images/imageFile33.png>)

Proof of Lemma 2.2. Let Dp be the degree distribution for vertices in Gp, so that Dp has a Bin(D,√p) distribution. We want to show that there exists two constants c˜1 and C1 such that

![image 34](<2015-baroni-first-passage-percolation-random_images/imageFile34.png>)

- (2.4)

c˜1 kτ−1 ≤ P(Dp > k) ≤

![image 35](<2015-baroni-first-passage-percolation-random_images/imageFile35.png>)

C1 kτ−1

![image 36](<2015-baroni-first-passage-percolation-random_images/imageFile36.png>)

.

The upper bound is obvious since

- (2.5) P(Dp > k) = P(Bin(D,√p) > k) ≤ P(D > k) ≤

![image 37](<2015-baroni-first-passage-percolation-random_images/imageFile37.png>)

C1 kτ−1

![image 38](<2015-baroni-first-passage-percolation-random_images/imageFile38.png>)

so that C1 = C1. For the lower bound, we ﬁrst ﬁx a constant K and consider k ≤ K. We choose c˜1 = c˜1(K) suﬃciently small, so that the lower bound for k ≤ K is trivially satisﬁed. To prove the inequality for k > K, we split

P(Bin(D,√p) > k) ≥ P(Bin(D,√p) > k,D ≥

![image 39](<2015-baroni-first-passage-percolation-random_images/imageFile39.png>)

![image 40](<2015-baroni-first-passage-percolation-random_images/imageFile40.png>)

2k √p

![image 41](<2015-baroni-first-passage-percolation-random_images/imageFile41.png>)

![image 42](<2015-baroni-first-passage-percolation-random_images/imageFile42.png>)

- (2.6) )

≥ P D ≥

2k √p − P Bin(D,√p) ≤ k,D ≥

![image 43](<2015-baroni-first-passage-percolation-random_images/imageFile43.png>)

![image 44](<2015-baroni-first-passage-percolation-random_images/imageFile44.png>)

![image 45](<2015-baroni-first-passage-percolation-random_images/imageFile45.png>)

2k √p

![image 46](<2015-baroni-first-passage-percolation-random_images/imageFile46.png>)

![image 47](<2015-baroni-first-passage-percolation-random_images/imageFile47.png>)

≥

c1√pτ−1 (2k)τ−1 − P Bin(D,√p) ≤ k,D ≥

![image 48](<2015-baroni-first-passage-percolation-random_images/imageFile48.png>)

![image 49](<2015-baroni-first-passage-percolation-random_images/imageFile49.png>)

![image 50](<2015-baroni-first-passage-percolation-random_images/imageFile50.png>)

2k √p

![image 51](<2015-baroni-first-passage-percolation-random_images/imageFile51.png>)

![image 52](<2015-baroni-first-passage-percolation-random_images/imageFile52.png>)

.

Now, by stochastic domination of Bin(m,√p) by Bin(n,√p) when m ≤ n,

![image 53](<2015-baroni-first-passage-percolation-random_images/imageFile53.png>)

![image 54](<2015-baroni-first-passage-percolation-random_images/imageFile54.png>)

- (2.7) P Bin(D,√p) ≤ k,D ≥

![image 55](<2015-baroni-first-passage-percolation-random_images/imageFile55.png>)

2k √p ≤ P Bin

![image 56](<2015-baroni-first-passage-percolation-random_images/imageFile56.png>)

![image 57](<2015-baroni-first-passage-percolation-random_images/imageFile57.png>)

2k √p

![image 58](<2015-baroni-first-passage-percolation-random_images/imageFile58.png>)

![image 59](<2015-baroni-first-passage-percolation-random_images/imageFile59.png>)

,√p ≤ k .

![image 60](<2015-baroni-first-passage-percolation-random_images/imageFile60.png>)

By Lemma 2.2,

- (2.8) P Bin(D,√p) ≤ k,D ≥

![image 61](<2015-baroni-first-passage-percolation-random_images/imageFile61.png>)

2k √p ≤ e−k/4.

![image 62](<2015-baroni-first-passage-percolation-random_images/imageFile62.png>)

![image 63](<2015-baroni-first-passage-percolation-random_images/imageFile63.png>)

Thus,

- (2.9) P(Bin(D,√p) > k) ≥ c1√pτ−1/(2k)(τ−1) − e−k/4 ≥

![image 64](<2015-baroni-first-passage-percolation-random_images/imageFile64.png>)

![image 65](<2015-baroni-first-passage-percolation-random_images/imageFile65.png>)

c˜′1 kτ−1

![image 66](<2015-baroni-first-passage-percolation-random_images/imageFile66.png>)

,

so that c˜1 is the minimum between c˜1(K) and c˜′1.

![image 67](<2015-baroni-first-passage-percolation-random_images/imageFile67.png>)

![image 68](<2015-baroni-first-passage-percolation-random_images/imageFile68.png>)

![image 69](<2015-baroni-first-passage-percolation-random_images/imageFile69.png>)

![image 70](<2015-baroni-first-passage-percolation-random_images/imageFile70.png>)

A result on the size of the giant component in the conﬁguration model has ﬁrst been proved by Molloy and Reed (see [21]). In the context of percolation on the conﬁguration model, we rely on the following theorem by Janson:

Theorem 2.4 ([17, Proposition 3.1] in the case of i.i.d. degrees). Let CMn(D) have i.i.d. degrees with distribution function satisfying (1.3). Then w.h.p. there is a giant component C1 if and only if ED(D − 2) > 0. In particular, its size v(C1) is given by

- (2.10)


v(C1) n

→P 1 − hD(ξ),

![image 71](<2015-baroni-first-passage-percolation-random_images/imageFile71.png>)

where ξ satisﬁes

- (2.11)

h′D(ξ) E[D]

![image 72](<2015-baroni-first-passage-percolation-random_images/imageFile72.png>)

= ξ,

Further,

- (2.12)

vk(C1) n

![image 73](<2015-baroni-first-passage-percolation-random_images/imageFile73.png>)

−→P P(D = k)(1 − ξk),

where vk(C1) is the number of vertices with degree k in the giant component. Note that

- (2.13)

h′D(s) E[D]

![image 74](<2015-baroni-first-passage-percolation-random_images/imageFile74.png>)

= k

ksk−1P(D = k) E[D]

![image 75](<2015-baroni-first-passage-percolation-random_images/imageFile75.png>)

=

k

sk(k + 1)

P(D = k + 1) E[D]

![image 76](<2015-baroni-first-passage-percolation-random_images/imageFile76.png>)

=

k

skP(D⋆ − 1 = k) = hD⋆−1(s).

Using this, it follows that (2.11) is equivalent to

- (2.14) hD⋆−1(ξ) = ξ.


Note that the solution ξ to hD⋆−1(ξ) = ξ is the extinction probability of a branching process with oﬀspring distribution D⋆ − 1. Further, 1 − hD(ξ) is the survival probability of a BP where the root has oﬀspring D and all other individuals have oﬀspring distributed as D⋆ − 1. Due to Janson [17] (see also the ﬁrst paper on percolation on the conﬁguration model by Fontoulakis [12]), percolation on CMn(D) has the same distribution as a conﬁguration model with percolated degrees, where we keep each half-edge with probability √p, so that the degree of any vertex in the percolated graph is distributed as Bin(D,√p). Hence, the combination of [17], then Lemma 2.2 and Theorem 2.4 yields the following corollary:

![image 77](<2015-baroni-first-passage-percolation-random_images/imageFile77.png>)

![image 78](<2015-baroni-first-passage-percolation-random_images/imageFile78.png>)

Corollary 2.5 (Giant component of percolated conﬁguration model). Fix p ∈ [0,1], and consider percolation with parameter p on the conﬁguration model with i.i.d. degrees having distribution FD satisfying (1.3). Then, in the percolated graph Gp, the new degree distibution satisﬁes

- (1.3) with diﬀerent coeﬃcients, and the giant component has size v(C1) s.t.
- (2.15)


v(C1(Gp)) n

→P 1 − hD(ξ(p)),

![image 79](<2015-baroni-first-passage-percolation-random_images/imageFile79.png>)

where hD is the p.g.f. of D and ξ(p) is the extinction probability of a branching process where the root is present only with probability √p and the oﬀspring distribution is

![image 80](<2015-baroni-first-passage-percolation-random_images/imageFile80.png>)

- (2.16) Bin(D⋆ − 1,√p) := Bp.


![image 81](<2015-baroni-first-passage-percolation-random_images/imageFile81.png>)

If we denote the extinction probability of a BP with oﬀspring distribution Bp by χ(p), then it is easy to prove that ξ(p) = 1 −

√p + √pχ(p). Now that we have gathered all preliminaries, we are ready to prove our main results.

![image 82](<2015-baroni-first-passage-percolation-random_images/imageFile82.png>)

![image 83](<2015-baroni-first-passage-percolation-random_images/imageFile83.png>)

3. Proof of Theorem 1.6. In this section, we use the results of Section 2 to prove Theorem 1.6. We want to prove that given ε arbitrarily small, w.h.p.

- (3.1) Vn(1)ρ + Vn(2)ρ ≤ Wn ≤ Vn(1)ρ + Vn(2)ρ + ε.


To prove the lower bound we have to show that, for a proper choice of ρ, SWGunρ, SWGvnρ are w.h.p. disjoint. Once we know that they are disjoint, Vn(1)ρ and Vn(2)ρ denote the time to reach the nρth individuals in the clusters, hence, the result. That disjointedness is true for a proper choice of nρ follows from the following proposition (see [4, Proposition 4.7]).

Proposition 3.1 (Disjointedness of SWGs). There exists a ρ > 0 such that, w.h.p.

- (3.2) V(SWGunρ) ∩ V(SWGvnρ) = ∅. where V(SWG) is the set of vertices of the shortest-weight graph.


Proof. The proof of the proposition follows directly from [20, Lemma 2.2], which in turn follows from [4, Proposition 4.7].

![image 84](<2015-baroni-first-passage-percolation-random_images/imageFile84.png>)

![image 85](<2015-baroni-first-passage-percolation-random_images/imageFile85.png>)

![image 86](<2015-baroni-first-passage-percolation-random_images/imageFile86.png>)

![image 87](<2015-baroni-first-passage-percolation-random_images/imageFile87.png>)

- Proposition 3.1 immediately proves that Wn(u,v) ≥ Vn(1)ρ + Vn(2)ρ . To prove the corresponding upper bound, we can decompose the shortest-weight path as the union of three components, the ﬁrst lies in SWGunρ, the second in SWGvnρ and the third is the minimal weight path that connects these two clusters. We will show that the upper bound in (3.1) holds w.h.p., where ε bounds the weight of the minimal connecting path from above. The bound in (3.1) is a consequence of the following proposition:
- Proposition 3.2 (Small-weight connection between SWGs). For any ﬁxed ε > 0, w.h.p. there exists a path that connects SWGunρ and SWGvnρ having weight less than ε.


The proof of Proposition 3.2 consists of a combination of the bond percolation methods described in Section 2.3 and a layering decomposition of the percolated graph. This layering decomposition is also useful in the case of the unpercolated graphs, see e.g. [20]. We keep SWGunρ and SWGvnρ and delete every other edge with probability P(X > ε), where Y = 1 + X is the weight of the edge. Then we decompose the percolated graph in the following sets of vertices or layers:

- (3.3) Γpi := {v ∈ Gp: Dvp > ui}, where ui is deﬁned recursively by


- (3.4) ui+1 =


ui C log n

![image 88](<2015-baroni-first-passage-percolation-random_images/imageFile88.png>)

1/(τ−2)

, u0 := nρ0,

where ρ0 < ρ(τ − 2) and ρ is deﬁned in Proposition 3.2. A simple calculation yields that

- (3.5) ui = nρ0((τ−2)−i)(C log n)−ei with ei =

1 3 − τ

![image 89](<2015-baroni-first-passage-percolation-random_images/imageFile89.png>)

1 τ − 2

![image 90](<2015-baroni-first-passage-percolation-random_images/imageFile90.png>)

i

− 1 .

Also, we deﬁne v⋆ as the maximum degree vertex of the graph, if there are more we choose one uniformly at random. By (1.3), a lower bound on the (percolated) degree of v⋆ follows:

- (3.6) lim n→∞


1/(τ−1)

n blog n

Dip <

P max

![image 91](<2015-baroni-first-passage-percolation-random_images/imageFile91.png>)

i∈[n]

= 0

for an appropriate costant b. So, w.h.p., Dvp⋆ > (lognn)1/(τ−1). The following lemma (see [20, Lemma 3.3]) describes how these layering sets are connected in Gp:

![image 92](<2015-baroni-first-passage-percolation-random_images/imageFile92.png>)

Lemma 3.3 (Connectivity lemma). With ui and Γpi deﬁned as in (3.5) and (3.3), for every v ∈ Γpi, w.h.p. there is a vertex w ∈ Γpi+1 such that (v,w) ∈ E(Gp), where E(Gp) is the set of edges in Gp. Furthermore, w.h.p. the previous statement can be applied repeatedly to build a path from Γ0 to Γi as long as

- (3.7) i < −

log((τ − 1)ρ0) |log(τ − 2)|

![image 93](<2015-baroni-first-passage-percolation-random_images/imageFile93.png>)

.

We want to prove the existence of a path between SWGunρ and SWGvnρ of arbitrary small length. By Lemmas 2.2 and 3.3, it follows that the connectivity lemma is still valid for Gp. We still need to check if SWGunρ intersects with Γp0. The next lemma handles this:

Lemma 3.4 (Intersection of SWGunρ and Γp0). With high probability, SWGunρ ∩ Γp0 = ∅ as n → ∞.

Proof. We call VMnρ the vertex having the maximum percolated degree in SWGunρ, that is, the maximal degree vertex after percolation. Then its degree deg VMnρ is given by

- (3.8) deg VMnρ = max 1≤i≤nρ

Bin(Bi,√p),

![image 94](<2015-baroni-first-passage-percolation-random_images/imageFile94.png>)

where Bi is the ith vertex chosen in the growth of SWGunρ, so that by [20, Proposition 2.1] Bi are i.i.d. random variables with distribution from (1.3). By Lemma 2.2 the same is true for the

variables Bin(Bi,√p) with a diﬀerent constant in (1.3). So, elementary calculations yield that for any constant r > 0 and some proper constant c˜p > 0

![image 95](<2015-baroni-first-passage-percolation-random_images/imageFile95.png>)

- (3.9) P deg VMnρ <

nρ r

![image 96](<2015-baroni-first-passage-percolation-random_images/imageFile96.png>)

1/(τ−2)

< e−c˜pr. Choosing r = clog n establishes the claim.

![image 97](<2015-baroni-first-passage-percolation-random_images/imageFile97.png>)

![image 98](<2015-baroni-first-passage-percolation-random_images/imageFile98.png>)

![image 99](<2015-baroni-first-passage-percolation-random_images/imageFile99.png>)

![image 100](<2015-baroni-first-passage-percolation-random_images/imageFile100.png>)

As a result of Lemma 3.4, w.h.p. u is connected to some vertex u˜ in Γp0 ∩ SWGunρ. Then, we use the Connectivity Lemma 3.3 in C1(Gp) to construct a path from u˜ to Γpi∗, where i⋆ is the last index when Γpi is w.h.p. non-empty. Finally, Lemma 3.6 below shows that we can connect this path in less than two steps with the maximum degree vertex v1⋆ in Gp. We next perform the details of this proof. In it, we will use the next lemma, which is [20, Lemma 4.1]:

Lemma 3.5 (Direct connectivity lemma). Consider two sets of vertices A and B. If the number of half-edges HA = o(n) and HB satisfying

- (3.10)

HAHB n

![image 101](<2015-baroni-first-passage-percolation-random_images/imageFile101.png>)

> C(n),

then, conditioning on the event {|Ln| < 2E[D]n}, with N(B) denoting the neighbors of B,

- (3.11) P(A ∩ N(B) = ∅) < exp{−C(n)/(4E[D])}.


Lemma 3.6 (Two-hop connection to maximum degree vertex). Let i⋆ be the last i for which

Γpi∗ = ∅. If v ∈ Γpi⋆, then there exists w ∈ Γpi⋆ s.t. (v,w),(w,v⋆) ∈ E(G), with v⋆ maximum degree vertex in the percolated graph.

τ−2

Proof. We deﬁne Γpε = {u ∈ Gp s.t. Dup > n

τ−1+ε}, we denote the number of half-edges in the graph that are connected to vertices with degree ≥ y by S≥py. Then,

![image 102](<2015-baroni-first-passage-percolation-random_images/imageFile102.png>)

- (3.12) S≥py

=d

n

i=1

Dip {Dp

i ≥y},

where Dip =d Bin(Di,√p), with Di the degree of i ∈ [n]. Therefore,

![image 103](<2015-baroni-first-passage-percolation-random_images/imageFile103.png>)

- (3.13) S≥py ≥ y

n

i=1

{Dip≥y}.

Let R = ni=1 {Dp

i ≥y}, so that R ∼ Bin(n,p˜), where p˜ = P(Dip ≥ y). Then, E[R] = np˜. Thus, using Lemma 2.3, with p˜ ≥ c˜1/yτ−1,

- (3.14) P S≥py <

- 1

![image 104](<2015-baroni-first-passage-percolation-random_images/imageFile104.png>)

- 2


n

c˜1 yτ−1 ≤ P S≥py <

![image 105](<2015-baroni-first-passage-percolation-random_images/imageFile105.png>)

- 1

![image 106](<2015-baroni-first-passage-percolation-random_images/imageFile106.png>)

- 2


E[R] < exp{−E[R]/8}.

Then, w.h.p.

- (3.15) S≥py ≥


- 1

![image 107](<2015-baroni-first-passage-percolation-random_images/imageFile107.png>)

- 2


c1 (τ − 2)

y(2−τ).

n

![image 108](<2015-baroni-first-passage-percolation-random_images/imageFile108.png>)

τ−2

From (3.4) and (3.6), if v ∈ Γpi⋆ then Dvp > ((lognn)α)(

τ−1) w.h.p. for a certain α > 0. We can apply (3.15) with y = n

![image 109](<2015-baroni-first-passage-percolation-random_images/imageFile109.png>)

![image 110](<2015-baroni-first-passage-percolation-random_images/imageFile110.png>)

τ−2

τ−1+ε to see that the number of half-edges in Γpε is w.h.p. at least (nc1/(τ −2))n−(τ−2)(

![image 111](<2015-baroni-first-passage-percolation-random_images/imageFile111.png>)

τ−2

τ−1+ε), where the exponent of n equals 1−(τ −2)(ττ−−12 +ε) > 0 when ε > 0 is suﬃciently small.

![image 112](<2015-baroni-first-passage-percolation-random_images/imageFile112.png>)

![image 113](<2015-baroni-first-passage-percolation-random_images/imageFile113.png>)

ε from (3.15) we see that there exists a vertex w ∈ Γpε such that (v,w) forms an edge. Finally, we apply Lemma 3.5 with H{w} and H{v⋆} to see that w.h.p. there is an edge between w and v⋆.

Applying Lemma 3.5 to H{v} and HΓp

![image 114](<2015-baroni-first-passage-percolation-random_images/imageFile114.png>)

![image 115](<2015-baroni-first-passage-percolation-random_images/imageFile115.png>)

![image 116](<2015-baroni-first-passage-percolation-random_images/imageFile116.png>)

![image 117](<2015-baroni-first-passage-percolation-random_images/imageFile117.png>)

By applying Lemma 3.6 twice, we get that any pair of vertices in the most external layer Γp0 has a path connecting them of length at most 2(i⋆ +2) and weight at most 2(i⋆ +2)ε. Note that i⋆ does not grow with n. This proves (3.1).

4. Proof of Theorem 1.8. In this section, we prove Theorem 1.8, under the assumptions of i.i.d. edge weights Y = 1 + X with inf supp(X) = 0. In Section 1.4 we have reduced it to the proof of Proposition 1.9.

4.1. Proof of Proposition 1.9. We denote by PWn (u,v) and PDn(u,v) the path from u to v with the minimal weight and the one with the minimal number of edges in CMn(D). By deﬁnition (1.7), the hopcount is such that Hn(u,v) = |PWn (u,v)|. When u and v are in the same connected component,

- (4.1) Dn(u,v) ≤ Hn(u,v) ≤ Wn(u,v),


where Dn(u,v) is the graph distance between u and v. We prove Proposition 1.9 by ﬁnding an upper bound on Wn(u,v).

Proof of Proposition 1.10. Let p = p(ε0) be the survival probability of an edge, i.e., P(X ≤ ε0) = p(ε0), where ε0 will be chosen later in the proof. We deﬁne the k-neighborhood of u in a graph G by

- (4.2) Nk(u) = {u˜ ∈ G: Dn(u,u˜) ≤ k}. We prove the following lemma:

Lemma 4.1 (Intersection of ﬁrst layer and giant percolated component). For G = CMn(D), and any p > 0,

- (4.3) lim k→∞

liminf

n→∞

P(Nk(u) ∩ C1(Gp) = ∅) = 1.

We stress here that Nk(u) is the neighborhood in the unpercolated conﬁguration model.

Proof. Let Ak = ∂Nk(u) = {u˜ ∈ G: Dn(u,u˜) = k}. We denote by VMk the vertex with the

maximum percolated degree Dvd in Ak. By Proposition 2.1, |Ak| →P ∞. The number of outgoing edges from vi ∈ Ak can be coupled to i.i.d. random variables Bi ∼ B, with B deﬁned in (1.5), so that

- (4.4) deg VMk = max i∈Ak

Bin(Bi,√p), VMk = arg maxi∈A

![image 118](<2015-baroni-first-passage-percolation-random_images/imageFile118.png>)

k

Bin(Bi,√p).

![image 119](<2015-baroni-first-passage-percolation-random_images/imageFile119.png>)

Using (2.4), an elementary calculation shows that for any constant r > 0 and some constant c˜p > 0

- (4.5) P deg VMk < |Ak| r

![image 120](<2015-baroni-first-passage-percolation-random_images/imageFile120.png>)

1/(τ−2) < e−c˜pr.

Let En,k = {VMk ∈/ C1(Gp)} with G = CMn(D). To prove (4.3) it is enough to show that

- (4.6) lim k→∞

limsup

n→∞

P(En,k) = 0.

By the law of total probability,

- (4.7) P(En,k) = j

P(En,k|deg VMk = j)P(deg VMk = j).

By (2.12),

- (4.8)

vj(Gp) n −

![image 121](<2015-baroni-first-passage-percolation-random_images/imageFile121.png>)

vj(C1(Gp)) n

![image 122](<2015-baroni-first-passage-percolation-random_images/imageFile122.png>)

→P P(Dp = j)ξ(p)j.

Therefore,

lim

k→∞

limsup

n→∞

P(En,k) = lim

k→∞

limsup

n→∞

j

- (4.9) P(En,k | deg VMk = j)P(deg VMk = j)


= lim

k→∞

j

ξ(p)jP(deg VMk = j) = 0,

where, in the last equality we have used (4.5) which implies deg VMk →P ∞ as k → ∞.

![image 123](<2015-baroni-first-passage-percolation-random_images/imageFile123.png>)

![image 124](<2015-baroni-first-passage-percolation-random_images/imageFile124.png>)

![image 125](<2015-baroni-first-passage-percolation-random_images/imageFile125.png>)

![image 126](<2015-baroni-first-passage-percolation-random_images/imageFile126.png>)

By (3.9), there exists ε1 = ε1(k) such that P(deg VMk ≥ j) > 1 − ε1. Notice that k = k(ε0,ε1) does not depend on n. We denote by u1 the vertex of ∂Nk(u) ∩ C1(Gp(ε0)) having the minimal weight distance from u. Such a vertex exists with probability 1 − ε1. Let v1 denote the corresponding vertex for ∂Nk(v)∩C1(Gp(ε0)). In particular, u1 and v1 are in the giant component of a conﬁguration model with the same power-law exponent τ. By [16, Theorem 3.1], for every ε > 0,

- (4.10) lim

n→∞

P Dnp(˜u1,v˜1) ≤

2(1 + ε)log log n) |log(τ − 2)|

![image 127](<2015-baroni-first-passage-percolation-random_images/imageFile127.png>)

Dnp(˜u1,v˜1) < ∞ = 1,

where now u˜1 and v˜1 are two vertices chosen uniformly at random from [n] conditionally on being connected and Dnp(˜u1,v˜1) is the distance between u˜1 and v˜1 in Gp with G = CMn(D). In our case, however, the points u1 and v1 are not chosen uniformly from the giant component, so we prove a more general statement:

Lemma 4.2 (Distances between uniform vertices of ﬁxed degree). For p ∈ (0,1). If C1(Gp) is the giant component of Gp with G = CMn(D) and the degrees (Di)i∈[n] are i.i.d. random variables whose distribution function FD satisﬁes (1.3), then, for every k1,k2,

- (4.11) lim

n→∞

P Dnp(u1,v1) ≤

2(1 + ε)log log n |log(τ − 2)|

![image 128](<2015-baroni-first-passage-percolation-random_images/imageFile128.png>)

| u1,v1 ∈ C1(Gp),Dup1 = k1,Dup2 = k2 = 1,

where Dupi is the degree of ui in Gp. Proof. By (4.10),

- (4.12) lim

n→∞

P Dnp(u1,v1) ≤

2(1 + ε)log log n |log(τ − 2)|

![image 129](<2015-baroni-first-passage-percolation-random_images/imageFile129.png>)

u1,v1 ∈ C1(Gp) = 1,

where u1 and v1 are chosen uniformly at random in C1(Gp). Further,

P Dnp(u1,v1) ≤

2(1 + ε)log log n |log(τ − 2)|

![image 130](<2015-baroni-first-passage-percolation-random_images/imageFile130.png>)

- (4.13) u1,v1 ∈ C1(Gp)

=

k1,k2

P Dnp(u1,v1) ≤

2(1 + ε)log log n |log(τ − 2)|

![image 131](<2015-baroni-first-passage-percolation-random_images/imageFile131.png>)

u1,v1 ∈ C1(Gp),Dup1 = k1,Dvp1 = k2

× P Dup1 = k1,Dup2 = k2|u1,v1 ∈ C1(Gp) . We have a series of the form

- (4.14) a(n) =

k1,k2

ak1,k2(n)bk1,k2(n),

where ak1,k2(n) is the ﬁrst factor on the right-hand side of (4.13), while bk1,k2(n) is the second. By [17, Prop 3.1],

- (4.15) bk(n) = P(deg u1 = k | u1 ∈ C1(Gp)) →

P(Dp = k)(1 − ξ(p)k) 1 − hD(ξ(p))

![image 132](<2015-baroni-first-passage-percolation-random_images/imageFile132.png>)

,

with ξ(p) as in Corollary 2.5. Then, using the independence of coupling for two vertices (see [16, Theorem 1.1]), (2.12) and (2.11), for every k1,k2 ≥ 0

- (4.16) bk1,k2(n) →


P(Dp = k1)(1 − ξ(p)k1)P(Dp = k2)(1 − (ξ(p))k2) (1 − hD(ξ(p)))2 ≡ bk1,k2.

![image 133](<2015-baroni-first-passage-percolation-random_images/imageFile133.png>)

It is straightforward to check that

- (4.17)

k1,k2

bk1,k2(n) =

k1,k2

bk1,k2 = 1.

Further, by (4.10), a(n) → 1. Now we are ready to complete the argument. We would like to show that limn→∞ ak˜

1,k˜2(n) = 1 for any k˜1,k˜2. We argue by contradiction. Suppose instead that there exist k˜1,k˜2 for which

- (4.18) liminf

n→∞

ak˜

1,k˜2(n) = 1 − β < 1. Then,

liminf

n→∞

a(n) ≤ liminf

n→∞

ak˜

1,k˜2(n)bk˜

1,k˜2(n) +

(k1,k2) =(k˜1,k˜2)

bk1,k2(n)

= (1 − β)bk1,k2 + 1 − bk1,k2 = 1 − βbk1,k2,

which leads to a contradiction, since bk1,k2 > 0. We conclude that (4.18) cannot hold, so that liminfn→∞ ak1,k2(n) = 1 for every k1,k2.

![image 134](<2015-baroni-first-passage-percolation-random_images/imageFile134.png>)

![image 135](<2015-baroni-first-passage-percolation-random_images/imageFile135.png>)

![image 136](<2015-baroni-first-passage-percolation-random_images/imageFile136.png>)

![image 137](<2015-baroni-first-passage-percolation-random_images/imageFile137.png>)

We continue with the proof of Proposition 1.9. We want to show that, for u and v uniformly chosen in G, any ﬁxed ε, there exists n(δ1,ε) s.t. for every n > n(δ1,ε)

- (4.19) P

Wn(u,v) 2log log n ≤

![image 138](<2015-baroni-first-passage-percolation-random_images/imageFile138.png>)

1 + ε |log(τ − 2)|

![image 139](<2015-baroni-first-passage-percolation-random_images/imageFile139.png>)

≥ 1 − δ1.

Let En′ = {πp(Nk(u)) ∩ C1(Gp) = ∅,πp(Nk(v)) ∩ C1(Gp) = ∅} where G = CMn(D). Then

- (4.20) P

Wn(u,v) 2log log n ≤

![image 140](<2015-baroni-first-passage-percolation-random_images/imageFile140.png>)

1 + ε |log(τ − 2)|

![image 141](<2015-baroni-first-passage-percolation-random_images/imageFile141.png>)

≥ P

Wn(u,v) 2log log n ≤

![image 142](<2015-baroni-first-passage-percolation-random_images/imageFile142.png>)

1 + ε |log(τ − 2)|

![image 143](<2015-baroni-first-passage-percolation-random_images/imageFile143.png>)

|En′ P(En′ )

Also, by (4.3), if n ≥ n(δ1,ε) is so large that P(En′ ) ≥ 1 − δ1 then

P

Wn(u,v) 2log log n ≤

![image 144](<2015-baroni-first-passage-percolation-random_images/imageFile144.png>)

1 + ε |log(τ − 2)|

![image 145](<2015-baroni-first-passage-percolation-random_images/imageFile145.png>)

≥ P

Wn(u,v) 2log log n ≤

![image 146](<2015-baroni-first-passage-percolation-random_images/imageFile146.png>)

1 + ε |log(τ − 2)|

![image 147](<2015-baroni-first-passage-percolation-random_images/imageFile147.png>)

- (4.21) En′ (1 − δ1).

So, we need to prove that there exists an n(δ2,ε) s.t. for all n > n(δ2,ε)

- (4.22) P

Wn(u,v) 2log log n ≤

![image 148](<2015-baroni-first-passage-percolation-random_images/imageFile148.png>)

1 + ε |log(τ − 2)|

![image 149](<2015-baroni-first-passage-percolation-random_images/imageFile149.png>)

|En′ > 1 − δ2.

By Lemma 4.2, for any ﬁxed ε1 it holds w.h.p. the following

- (4.23) Dnp(u1,v1) ≤

2(1 + ε1)log log n |log(τ − 2)|

![image 150](<2015-baroni-first-passage-percolation-random_images/imageFile150.png>)

,

where u1,v1 are two vertices in C1(Gp) as in (4.10). So, we choose ε1 satisfying

- (4.24) (1 + ε0)(1 + ε1) ≤ (1 + ε),

where ε0 is the threshold length for percolation, i.e., we only keep edges with length 1 + ε0 in Gp. Under the hypothesis that En′ is true, we have:

- (4.25) Dn(u,v) ≤ k + Dnp(u1,v1) + k.


Let Y≤uk be the random variable that describes the weight of the path with the minimal distance PDn(u,u1), Y≤vk be the weight for PDn(v,v1). Also Y≤uk =d Y≤vk

d

≤ ki=1 Yi, where Yi are i.i.d. random variables with law Y and the stochastic dominance is due to the weight-dependent choice of u1 and v1 if there are more elements in the intersections ∂Nk(u) ∩ C1(Gp) and ∂Nk(v) ∩ C1(Gp). Then, for any k, w.h.p.,

- (4.26) Wn(u,v) ≤ Y≤uk +

2(1 + ε0)(1 + ε1)log log n |log(τ − 2)|

![image 151](<2015-baroni-first-passage-percolation-random_images/imageFile151.png>)

+ Y≤vk.

We ﬁx k = k(ε0,δ1) such that

- (4.27) liminf k→∞

liminf

n→∞

P(En′ ) ≥ 1 − δ1.

Thus, for any ﬁxed δ1 > 0, there exists n > n(k,ε0,ε1,δ2) s.t. P(2log logWn(u,v)n ≤ (1+|log(ε0)(1+τ−2)ε|1)|En′ ) > 1 − δ2. So, from (4.21), we have to choose δ1 and δ2 s.t.

![image 152](<2015-baroni-first-passage-percolation-random_images/imageFile152.png>)

![image 153](<2015-baroni-first-passage-percolation-random_images/imageFile153.png>)

- (4.28) (1 − δ1)(1 − δ2) > 1 − δ. This completes the proof of Proposition 1.9.


![image 154](<2015-baroni-first-passage-percolation-random_images/imageFile154.png>)

![image 155](<2015-baroni-first-passage-percolation-random_images/imageFile155.png>)

![image 156](<2015-baroni-first-passage-percolation-random_images/imageFile156.png>)

![image 157](<2015-baroni-first-passage-percolation-random_images/imageFile157.png>)

Acknowledgements.. This work is supported by the Netherlands Organisation for Scientiﬁc Research (NWO) through VICI grant 639.033.806 (EB and RvdH), VENI grant 639.031.447 (JK), the Gravitation Networks grant 024.002.003 (RvdH) and the STAR Cluster (JK).

References.

- [1] R. Albert, I. Albert, and G. L. Nakarado. Structural vulnerability of the North American power grid. Physical Review E, 69(2):025103, Feb. 2004.
- [2] R. Albert and A.-L. Barab´asi. Statistical mechanics of complex networks. Rev. Mod. Phys., 74:47–97, Jan 2002.
- [3] A.-L. Barab´asi, R. Albert, and H. Jeong. Scale-free characteristics of random networks: the topology of the world-wide web. Physica A: Statistical Mechanics and its Applications, 281(14):69 – 77, 2000.
- [4] S. Bhamidi, R. v. d. Hofstad, and G. Hooghiemstra. First passage percolation on random graphs with ﬁnite mean degrees. Ann. Appl. Probab., 20(5):1907–1965, 2010.
- [5] S. Bhamidi, R. v. d. Hofstad, and G. Hooghiemstra. Universality for ﬁrst passage percolation on sparse random graphs. Preprint 2012. Available at arXiv: 1210.6839 [math.PR].
- [6] B. Bollob´s. Random Graphs. Cambridge University Press, 2001.
- [7] S. Bornholdt and H. G. Schuster, editors. Handbook of Graphs and Networks: From the Genome to the Internet. John Wiley & Sons, Inc., New York, NY, USA, 2003.
- [8] P. L. Davies. The simple branching process: a note on convergence when the mean is inﬁnite. J. Appl. Probab., 15(3):466–480, 1978.
- [9] M. Deijfen and R. v. d. Hofstad. The winner takes it all. ArXiv e-prints, June 2013.
- [10] P. Erd˝s and A. Re´nyi. On random graphs i. Publ. Math. Debrecen, 6:290–297, 1959.
- [11] M. Faloutsos, P. Faloutsos, and C. Faloutsos. On power-law relationships of the internet topology. SIGCOMM Comput. Commun. Rev., 29(4):251–262, Aug. 1999.
- [12] N. Fountoulakis. Percolation on sparse random graphs with given degree sequence. Internet Math., 4(4):329– 356, 2007.
- [13] D. R. Grey. Explosiveness of age-dependent branching processes. Z. Wahrscheinlichkeitstheorie und Verw. Gebiete, 28:129–137, 1973/74.
- [14] T. Harris. The theory of branching processes. Die Grundlehren der Mathematischen Wissenschaften, Bd. 119. Springer-Verlag, Berlin, (1963).
- [15] R. v. d. Hofstad. Random graphs and complex networks. Available on http://www. win. tue. nl/∼ rhofstad/NotesRGCN. pdf, In preparation(2015).
- [16] R. v. d. Hofstad, G. Hooghiemstra, and D. Znamenski. Distances in random graphs with ﬁnite mean and inﬁnite variance degrees. Electron. J. Probab., 12:no. 25, 703–766, 2007.


- [17] S. Janson. On percolation in random graphs with given vertex degrees. Electron. J. Probab., 14:no. 5, 86–118, 2009.
- [18] P. Kaluza, A. K¨lzsch, M. T. Gastner, and B. Blasius. The complex network of global cargo ship movements. Journal of The Royal Society Interface, 2010.
- [19] J. Komj´thy and R. v. d. Hofstad. Fixed speed competition on the conﬁguration model with inﬁnite variance degrees: equal speeds. Preprint 2015. Available at arXiv: 1503.09046 [math.PR].
- [20] J. Komj´thy, R. v. d. Hofstad, and E. Baroni. Fixed speed competition on the conﬁguration model with inﬁnite variance degrees: unequal speeds. Preprint 2014. Available at arXiv:1408.0475 [math.PR].
- [21] M. Molloy and B. Reed. A critical point for random graphs with a given degree sequence. Random Structures & Algorithms, 6(2-3):161–180, 1995.
- [22] M. E. J. Newman. The Structure and Function of Complex Networks. SIAM Review, 45:167–256, Jan. 2003.
- [23] F. Radicchi, S. Fortunato, and A. Vespignani. Citation networks. In A. Scharnhorst, K. B¨orner, and P. van den Besselaar, editors, Models of Science Dynamics, Understanding Complex Systems, pages 233–257. Springer Berlin Heidelberg, 2012.
- [24] J. Wu, C. K. Tse, F. C. Lau, and I. W. H. Ho. Analysis of communication network performance from a complex network perspective. Circuits and Systems I: Regular Papers, IEEE Transactions on, 60(12):3303– 3316, 2013.


Eindhoven University of Technology, e.baroni@tue.nl

Eindhoven University of Technology, r.w.v.d.hofstad@TUE.nl

Eindhoven University of Technology, j.komjathy@tue.nl

