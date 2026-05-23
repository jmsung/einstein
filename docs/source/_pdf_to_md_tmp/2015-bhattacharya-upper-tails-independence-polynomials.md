# arXiv:1507.04074v3[math.CO]12Sep2017

## UPPER TAILS AND INDEPENDENCE POLYNOMIALS IN RANDOM GRAPHS

BHASWAR B. BHATTACHARYA, SHIRSHENDU GANGULY, EYAL LUBETZKY, AND YUFEI ZHAO

Abstract. The upper tail problem in the Erdős–Rényi random graph G ∼ Gn,p asks to estimate the probability that the number of copies of a graph H in G exceeds its expectation by a factor 1 + δ. Chatterjee and Dembo showed that in the sparse regime of p → 0 as n → ∞ with p ≥ n−α for an explicit α = αH > 0, this problem reduces to a natural variational problem on weighted graphs, which was thereafter asymptotically solved by two of the authors in the case where H is a clique.

Here we extend the latter work to any ﬁxed graph H and determine a function cH(δ) such that, for p as above and any ﬁxed δ > 0, the upper tail probability is exp[−(cH(δ)+o(1))n2p∆ log(1/p)], where ∆ is the maximum degree of H. As it turns out, the leading order constant in the large deviation rate function, cH(δ), is governed by the independence polynomial of H, deﬁned as PH(x) = iH(k)xk where iH(k) is the number of independent sets of size k in H. For instance, if H is a regular graph on m vertices, then cH(δ) is the minimum between 12δ2/m and the unique positive solution of PH(x) = 1 + δ.

1. Introduction

1.1. The upper tail problem in the random graph. Let Gn,p be the Erdős–Rényi random graph on n vertices with edge probability p, and let XH be the number of copies of a ﬁxed graph H in it. The upper tail problem for XH asks to estimate the large deviation rate function given by

RH(n,p,δ) := −log P(XH ≥ (1 + δ)E[XH]) for ﬁxed δ > 0, a classical and extensively studied problem (cf. [7,13,14,18,19,20,21,27] and [1,17] and the references therein) which already for the seemingly basic case of triangles (H = K3) is highly nontrivial and still not fully understood. It followed from works of Vu [27] and Kim and Vu [21] that1

n2p2 RK3(n,p,δ) n2p2 log(1/p) (the lower bound used the so-called “polynomial concentration” machinery, whereas the upper bound follows, e.g., from the fact that an arbitrary set of s ∼ δ1/3np vertices can form a clique in Gn,p with probability p(2s) = pO(n2p2), thus contributing 3 s ∼ δ n3 p3 = δE[XK3] extra triangles). The correct order of the rate function was settled fairly recently by Chatterjee [7], and independently by DeMarco and Kahn [14], proving that RK3(n,p,δ) n2p2 log(1/p) for p ≥ lognn. This was later extended in [13] to cliques (H = Kk for k ≥ 3), establishing that for p ≥ n−2/(k−1)+ε with ε > 0 ﬁxed2,

RKk(n,p,δ) n2pk−1 log(1/p). The methods of [7,13,14] did not allow recovering the exact asymptotics of this rate function, and in particular, one could ask, e.g., whether RK3(n,p,δ) ∼ c(δ)n2p2 log(1/p) with c(δ) = 12δ2/3, as the aforementioned clique upper bound for it may suggest (recall its probability is p(2s) for s ∼ δ1/3np).

Much progress has since been made in that front, propelled by the seminal work of Chatterjee and Varadhan [11] that introduced a large deviation framework for Gn,p in the dense regime (0 < p < 1

- 1We write f g to denote f = O(g); f g means f = Θ(g); f ∼ g means f = (1 + o(1))g and f g means f = o(g).
- 2More precisely, DeMarco and Kahn [13] showed that RKk min{n2pk−1 log(1/p), nkp(k2)} for p ≥ n−2/(k−1). 1


PH(x)

cH(δ)

15

8

10

6

5

| |
|---|


x

4

-4 -2 2 4

- -10

- -5


2

10 20 30 40 50 60

δ

|0.0 0.2 0.4 0.6 0.8 1.0<br><br>1.0<br><br>1.5<br><br>2.0<br><br>2.5<br><br>3.0<br><br><br>3.5<br><br>4.0<br><br>|
|---|


|0.5 1.0 1.5 2.0 2.5 3.0<br><br>0.2<br><br>0.4<br><br>0.6<br><br>0.8<br><br>1.0<br><br>|
|---|


C3 C4 C5

C6 C7 C8

Figure 1. The leading order constant cH(δ) for the upper tail rate function for k-cycles vs. their independence polynomials PH(x). Zoomed-in regions show PH(cH(δ)) = 1 + δ.

ﬁxed) via the theory of graph limits (cf. [10,11,25] for more on the many questions still open in that regime). See the survey by Chatterjee [8] on recent developments on this topic. In the sparse regime (p → 0), in the absence of graph limit tools, the understanding of large deviations for a ﬁxed graph H (be it even a triangle) remained very limited until a recent breakthrough paper of Chatterjee and Dembo [9] that reduced it to a natural variational problem in a certain range of p (see Deﬁnition 1.3 and Theorem 1.4 below). The third and fourth authors solved this variational problem asymptotically for triangles [26], thereby yielding the following conclusion: for ﬁxed δ > 0, if n−1/42 log n ≤ p = o(1), then

RK3(n,p,δ) ∼ c(δ)n2p2 log(1/p) where c(δ) = min 2 1δ2/3, 31δ , (1.1) and we see that the clique construction from above gives the correct leading order constant if δ ≥ 27/8. More generally, for every k ≥ 3 there is an explicit αk > 0 so that, for ﬁxed δ > 0, if n−αk ≤ p = o(1),

RKk(n,p,δ) ∼ ck(δ)n2pk−1 log(1/p) where ck(δ) = min 12δ2/k, k1δ . (1.2)

- For a general ﬁxed graph H with maximum degree ∆ ≥ 2 (when ∆ = 1 the problem is nothing


but the large deviation in the binomial variable corresponding to the edge-count) the order of the rate function was established up to a multiplicative log(1/p) factor by Janson, Oleszkiewicz, and Ruciński [18]. In the range p ≥ n−1/∆, their estimate (which involves a complicated quantity MH∗ (n,p)) simpliﬁes into

n2p∆ RH(n,p,δ) n2p∆ log(1/p) (with constants depending on H and on δ). As a byproduct of the analysis of cliques in [26], it was shown [26, Corollary 4.5] that there is some explicit αH > 0 so that, for ﬁxed δ > 0, if n−αH ≤ p = o(1),

RH(n,p,δ) n2p∆ log(1/p), yet those bounds were not sharp already for the 4-cycle C4. Here we extend that work and determine the precise asymptotics of RH(n,p,δ) for any ﬁxed graph H in the above mentioned range n−αH ≤ p = o(1) (as currently needed in the framework of [9]). Solving the variational problem

for a general H requires signiﬁcant new ideas atop [26], and turns out to involve the independence polynomial PH(x) (see Fig. 1).

- Deﬁnition 1.1 (Independence polynomial). The independence polynomial of H is deﬁned to be

PH(x) :=

k

iH(k)xk ,

where iH(k) is the number of k-element independent sets in H.

- Deﬁnition 1.2 (Inducing on maximum degrees). For a graph H with maximum degree ∆, let H∗ be the induced subgraph of H on all vertices whose degree in H is ∆. (Note that H∗ = H if H is regular.)

Roots of independence polynomials were studied in various contexts (cf. [5, 6, 12] and their references); here, the unique positive x such that PH∗(x) = 1 + δ will, perhaps surprisingly, give the leading order constant (possibly capped at some maximum value if H happens to be regular) of RH(n,p,δ).

- 1.2. Variational problem. For graphs G and H, denote by hom(H,G) the number of homomorphisms from H to G (a graph homomorphism is a map V (H) → V (G) that carries every edge of H to an edge of G). The homomorphism density of H in G is deﬁned as t(H,G) := hom(H,G)|V (G)|−|V (H)|, that is, the probability that a uniformly random map V (H) → V (G) is a homomorphism from H to G.


Henceforth, we will work with t(H,G) for G ∼ Gn,p instead of XH for convenience (the two quantities are nearly proportional, as the only possible discrepancies—non-injective homomorphisms from H to G—are a negligible fraction of all homomorphisms when G is suﬃciently large and not too sparse).

Chatterjee and Dembo [9] proved a non-linear large deviation principle, and in particular derived the exact asymptotics of the rate function for a general graph H in terms of a variational problem.

- Deﬁnition 1.3 (Discrete variational problem). Let Gn denote the set of weighted undirected graphs on n vertices with edge weights in [0,1], that is, if A(G) is the adjacency matrix of G then


Gn = {Gn : A(Gn) = (aij)1≤i,j≤n, 0 ≤ aij ≤ 1, aij = aji, aii = 0 for all i,j}. Let H be a ﬁxed graph with maximum degree ∆. The variational problem for δ > 0 and 0 < p < 1 is

φ(H,n,p,δ) := inf Ip(Gn) : Gn ∈ Gn with t(H,Gn) ≥ (1 + δ)p|E(H)| (1.3) where

t(H,Gn) := n−|V (H)|

aixiy

1≤i1,··· ,ik≤n (x,y)∈E(H)

is the density of (labeled) copies of H in Gn, and Ip(Gn) is the entropy relative to p, that is, Ip(G) :=

1 − x 1 − p

x p

Ip(aij) and Ip(x) := xlog

+ (1 − x)log

.

1≤i<j≤n

- Theorem 1.4 (Chatterjee and Dembo [9]). Let H be a ﬁxed graph. There is some explicit αH > 0 such that for n−αH ≤ p < 1 and any ﬁxed δ > 0,


P t(H,Gn,p) ≥ (1 + δ)p|E(H)| = exp −(1 + o(1))φ(H,n,p,δ) , where φ(H,n,p,δ) is as deﬁned in (1.3) and the o(1)-term goes to zero as n → ∞. Remark. Recently Eldan [15] improved the range of validity of the above theorem to p ≥ n−1/(6|E(H)|) log n.

s ∼ δ1/|V (H)|p∆/2n

![image 1](<2015-bhattacharya-upper-tails-independence-polynomials_images/imageFile1.png>)

1

p

![image 2](<2015-bhattacharya-upper-tails-independence-polynomials_images/imageFile2.png>)

s ∼ θp∆n

![image 3](<2015-bhattacharya-upper-tails-independence-polynomials_images/imageFile3.png>)

![image 4](<2015-bhattacharya-upper-tails-independence-polynomials_images/imageFile4.png>)

1

p

Figure 2. Solution candidates for discrete variational problem (clique and anti-clique). Thanks to this theorem, solving the variational problem φ(H,n,p,δ) asymptotically would give

the asymptotic rate function for H when n−αH ≤ p = o(1) (as was done for H = Kk in [26], yielding (1.2)).

- 1.3. Main Result. Let H be a graph with maximum degree ∆ = ∆(H); recall that H is regular (or ∆-regular) if all its vertices have degree ∆, and irregular otherwise. Starting with a weighted graph Gn with all edge-weights aij equal to p, we consider the following two ways of modifying Gn so it would satisfy the constraint t(H,Gn) ≥ (1 + δ)p|E(H)| of the variational problem (1.3) (see Figure 2).


- (a) (Planting a clique) Set aij = 1 for all 1 ≤ i,j ≤ s for s ∼ δ1/|V (H)|p∆/2n. This construction is eﬀective only when H is ∆-regular, in which case it gives t(H,Gn) ∼ (1 + δ)p|E(H)|.
- (b) (Planting an anti-clique) Set aij = 1 whenever i ≤ s or j ≤ s for s ∼ θp∆n for θ = θ(H,δ) > 0 such that PH∗(θ) = 1 + δ, in which case t(H,Gn) ∼ (1 + δ)p|E(H)|.


We postpone the short calculation that in each case t(H,Gn) ∼ (1 + δ)p|E(H)| to §2. Our main result (Theorem 1.5 below) says that, for a connected graph H and n−1/∆ p 1, one of these constructions has Ip(Gn) that is within a (1 + o(1))-factor of the optimum achieved by the variational problem (1.3). For example, when H = K3, the clique construction has Ip(Gn) ∼

- 1

- 2s2Ip(1) ∼ 12δ2/3n2p2 log(1/p), while PK3(x) = 1 + 3x so θ = δ/3 and the anti-clique construction


has Ip(Gn) ∼ snIp(1) ∼ 13δn2p2 log(1/p) (thus the clique wins if δ > 27/8), exactly the bounds that were featured in (1.1). The following result extends [26, Theorems 1.1 and 4.1] from cliques to the

case of a general graph H. Recall PH∗(x) from Deﬁnitions 1.1 and 1.2.

- Theorem 1.5. Let H be a ﬁxed connected graph with maximum degree ∆ ≥ 2. For any ﬁxed δ > 0 and n−1/∆ p = o(1), the solution to the discrete variational problem (1.3) satisﬁes


φ(H,n,p,δ) n2p∆ log(1/p)

lim

=

n→∞

min θ , 12δ2/|V (H)| if H is regular, θ if H is irregular,

where θ = θ(H,δ) is the unique positive solution to PH∗(θ) = 1 + δ. When combined with Theorem 1.4, this yields the following conclusion for the upper tail problem.

Corollary 1.6. Let H be a ﬁxed connected graph with maximum degree ∆ ≥ 2. There exists αH > 0 such that for n−αH ≤ p 1 the following holds. For any ﬁxed δ > 0,

−log P t(H,Gn,p) ≥ (1 + δ)p|E(H)| n2p∆ log(1/p)

min θ , 12δ2/|V (H)| if H is regular, θ if H is irregular,

lim

=

n→∞

where θ = θ(H,δ) is the unique positive solution to PH∗(θ) = 1 + δ.

Observe that when H is regular, there exists a unique δ0 = δ0(H) > 0 such that3

θ(H,δ) ≤ 21δ2/|V (H)| if and only if δ ≤ δ0(H). (1.4) That is, the leading order constant of φ(H,n,p,δ) (giving the asymptotic upper tail) is governed by the anti-clique for δ ≤ δ0 and by the clique for δ ≥ δ0 (the above example of H = K3 had δ0 = 27/8).

We remark that our results extend (see Theorem 9.1) to any disconnected graph H. The interplay between diﬀerent connected components can then cause the upper tail to be dominated not by an exclusive appearance of either the clique or the anti-clique constructions (as was the case for any connected graph H, cf. Theorem 1.5), but rather by an interpolation of these. See §9 for more details.

The assumption p n−1/∆ in Theorem 1.5 is essentially tight in the sense that the upper tail rate function undergoes a phase transition at that location [18]: it is of order n2+o(1)p∆ for p ≥ n−1/∆, and below that threshold it becomes a function (denoted MH∗ (n,p) in [18]) depending on all subgraphs of H. In terms of the discrete variational problem (1.3), again this threshold marks a phase transition, as the anti-clique construction ceases to be viable for p n−1/∆ (recall that s ∼ θp∆n in that construction). Still, as in [26, Theorems 1.1 and 4.1], our methods show that if H is regular and n−2/∆ p n−1/∆, the solution to the variational problem is (1 + o(1))12δ2/|V (H)| (i.e., governed by the clique construction).

Several of the tools that were developed here to overcome the obstacles in extending the analysis of [26] to general graphs (arising already for the 4-cycle) may be of independent interest and ﬁnd other applications, e.g., the crucial use of adaptively chosen degree-thresholds (see §5 for details).

One can ask to describe the random graph conditioned on having H-density at least (1+δ)p|E(H)|. Informally, our results suggest that the conditioned graph measure exhibits “localization”, that is, the excess copies of H are located in a microscopic part of the graph. In particular, we expect that it behaves like a typical graph along with a randomly planted clique or a complete bi-partite graph (anti-clique) and the nature of the planted structure undergoes a phase transition in δ, when H is regular. However, unlike the dense setting [11,25] where one can characterize the conditioned random graph with respect to the cut metric on graphs, we do not know of a good way to formalize the notion of being “close to” a planted clique or a planted anti-clique in the sparse setting.

- 1.4. Examples. We now demonstrate the solution of the variational problem (1.3), as provided by Theorem 1.5, for various families of graphs (adding to the previously known [26] case of cliques, cf. (1.2)).


- Example 1.7 (k-cycle: H = Ck). It is easy to verify that PCk(x) satisﬁes the recursion4 PCk(x) = PCk−1(x) + xPCk−2(x), PC2(x) = 2x + 1, PC3(x) = 3x + 1.


For instance, PC4(x) = 2x2 + 4x + 1 and PC5(x) = 5x2 + 5x + 1; by Theorem 1.5, if n−1/2 p 1, φ(C4,n,p,δ) ∼ min θ(C4,δ), 12δ1/2 n2p2 log(1/p) for θ(C4,δ) = −1 + 1 + 12δ , φ(C5,n,p,δ) ∼ min θ(C5,δ), 12δ2/5 n2p2 log(1/p) for θ(C5,δ) = −21 + 12 1 + 54δ .

- 3Indeed, PH(x) is increasing as it is a polynomial with nonnegative coeﬃcients, so θ ≤ 12δ2/|V (H)| if and only if 1 + δ ≤ PH(12δ2/|V (H)|) (as PH(θ) = 1 + δ). Since PH(x) is a polynomial of degree at most |V (H)|/2 (since H is regular) and constant term 1, the function f(δ) := (PH(12δ2/|V (H)|) − 1)/δ is decreasing for δ > 0. We have f(δ) → ∞ as δ → 0 and f(δ) ≤ (2 + o(1))(12δ2/|V (H)|)|V (H)|/2/δ ≤ 21−|V (H)|/2 + o(1) as δ → ∞. So f is decreasing and f(δ0) = 1 for some δ0 > 0, which proves the claim.

- 4By the deﬁnition of the independence polynomial, for any graph H and vertex v in it, PH(x) = PH1(x) + xPH2(x), where H1 is obtained from H by deleting v and H2 is obtained from H by deleting v and all its neighbors.


For general k, with square brackets denoting extraction of coeﬃcients, [x]PCk(x) = k (more generally, [x]PH(x) = |V (H)| for any H), while the closely related recursion for Chebyshev’s polynomials yields

k/2

k 2j

PCk(x) = 21−k

(1 + 4x)j , (1.5)

j=0

and so [x2]PCk(x) = 12k(k − 3); e.g., for any k ≥ 4, the behavior of θ(Ck,δ) for small δ (see Fig. 1) is θ(Ck,δ) = k−13 −1 + 1 + 2δ(k − 3)/k + O(δ3) = k1δ + 32−k2kδ2 + O(δ3). Finally, observe that for even k we can write (1.5) as PCk(x) = 12(√1 + 4x + 1) k+ 12(√1 + 4x − 1) k,

and deduce that the value of PCk(12δ2/k) for δ = 2k is simply PCk(2) = 2k + 1 = 1 + δ. Thus, by the remark following Corollary 1.6, the transition addressed in (1.4) occurs at δ0(Ck) = 2k for even k; e.g.,

= −1 + 1 + 12δ if δ < 16,

φ(C4,n,p,δ) n2p2 log(1/p)

(1.6)

lim

√

δ if δ ≥ 16.

1 2

n→∞

As mentioned above, H = C4 is the simplest graph for which the arguments in [26] did not give sharp bounds on φ(H,n,p,δ), and its treatment is instrumental for the analysis of general graphs (see §5.2).

- Example 1.8 (Binary tree). Letting Th denote the complete binary tree of height h (|V (Th)| = 2h−1), observe that, by counting independent sets excluding/including the root, PTh(x) satisﬁes the recursion

PTh(x) = PTh−1(x)2 + xPTh−2(x)4 , PT0(x) = 1, PT1(x) = x + 1. The polynomial PT∗

h

(x) restricts us to independent sets of Th where all degrees are ∆, and therefore PT∗

h

(x) = PTh−2(x)2 , as the restriction excludes precisely the root and leaves. (More generally, for the b-ary tree (b ≥ 2) one has PTh(x) = PTh−1(x)b + xPTh−2(x)b2, and PT∗

h

(x) = PTh−2(x)b.) For instance, the binary tree on 15 vertices, T4, has

PT∗

4

(x) = PT2(x)2 = x4 + 6x3 + 11x2 + 6x + 1, and solving PT∗

4

(θ) = 1 + δ, we obtain, by Theorem 1.5, that for any n−1/3 p 1,

lim

n→∞

φ(T4,n,p,δ) n2p3 log(1/p)

= −32 + 12 5 + 4

√

1 + δ . (1.7)

For general h, we can for instance deduce from the recurrence above (and the facts [x]PH[x] = |V (H)| and [x]PH∗(x) = #{v : deg(v) = ∆}) that [x]PT∗

h

(x) = 2h−1−2 and [x2]PT∗

h

(x) = 22h−3−7·2h−2+7 for any h ≥ 3, using which it is easy to write θ(Th,δ) explicitly up to an additive O(δ3)-term.

- Example 1.9 (Complete bipartite: H = Kk,  for k ≥ ). In case k > we have PK∗


(x) = (1 + x) as we only count independent sets in the k-regular side (of size ); thus, by Theorem 1.5, for n−1/k p 1,

k, 

φ(Kk, ,n,p,δ) n2pk log(1/p)

= (1 + δ)1/  − 1. (1.8)

lim

n→∞

If k = , the coeﬃcients of xj (j ≥ 1) are doubled, so PKk, (x) = 2(1+x)k−1 and for n−1/k p 1, lim

φ(Kk, ,n,p,δ) n2pk log(1/p)

= min 1 + 12δ 1/k − 1, 21δ1/k . (1.9)

n→∞

2. Clique and anti-clique constructions

We prove the claim at the beginning of §1.3, which gives an upper bound to the discrete variational problem φ(H,n,p,δ). It is obtained by planting a clique of an anti-clique of appropriate size (see Figure 2).

Proposition 2.1. Let H be a graph with maximum degree ∆. Let δ > 0 and θ = θ(H,δ) the unique positive solution to PH∗(θ) = 1 + δ.

- (a) (Clique) If H is connected and ∆-regular and n−2/∆ p 1, then φ(H,n,p,δ) ≤ 12δ2/|V (H)| + o(1) n2p∆ log(1/p).

- (b) (Anti-clique) For any graph H with maximum degree ∆ (not necessarily connected or regular), if n−1/∆ p 1, then


φ(H,n,p,δ) ≤ (θ + o(1))n2p∆ log(1/p).

Proof. (a) Let G be a weighted graph on n vertices with adjacency matrix (aij)1≤i,j≤n. Starting with all weights set to p, modify G by setting aij = 1 whenever i,j ≤ s for some integer s ∼ δ1/|V (H)|p∆/2n to be decided. Then Ip(G) ∼ 12s2Ip(1) ∼ 12δ2/|V (H)|p∆ log(1/p). We will show that s ∼ θp∆n implies that t(H,G) ∼ (1 + δ)p|E(H)|, so that an appropriately chosen s ∼ δ1/|V (H)|p∆/2n would give t(H,G) ≥ (1 + δ)p|E(H)|, thereby showing the claimed upper bound on φ(H,n,p,δ).

By summing over the subset of vertices of H that get mapped to {1,...,s} ⊆ V (G), we ﬁnd t(H,G) ∼

|S|

|V (H)|−|S|

s n

s n

p|E(H)|−|E(H[S])|

1 −

S⊆V (H)

|S|

δ1/|V (H)|p∆/2

p|E(H)|−|E(H[S])| ∼ (1 + δ)p|E(H)|.

∼

S⊆V (H)

Here H[S] denotes the subgraph of H induced by S. The ﬁrst estimate hides a 1 + o(1) factor coming from the negligible fraction of maps V (H) → V (G) that send two adjacent vertices of H to the same vertex in G. For the ﬁnal estimate, note that since H is ∆-regular and connected, we have ∆|S|/2 > |E(H[S])| for all ∅ = S V (H), and in such cases the corresponding term in the summation above is o(p|E(H)|). The only non-negligible terms are S = ∅ and S = V (H), which make up the ﬁnal estimate (1 + δ)p|E(H)|.

(b) Let G be a weighted graph on n vertices with adjacency matrix (aij)1≤i,j≤n. Starting with all weights set to p, modify G by setting aij = 1 whenever i ≤ s or j ≤ s for some integer s ∼ θp∆n. Then Ip(G) ∼ snIp(1) ∼ θn2p∆ log(1/p). As earlier, it remains to show t(H,G) ∼ (1 + δ)p|E(H)|.

In computing t(H,G), by summing over the subset of vertices of H that get mapped to {1,...,s} ⊆ V (G), we ﬁnd

|S|

|V (H)|−|S|

s n

s n

p|E(H[V \S])|

t(H,G) ∼

1 −

S⊆V (H)

θ|S|p∆|S|+|E(H[V \S])|

∼

S⊆V (H)

θ|S|p|E(H)| = PH∗(θ)p|E(H)| = (1 + δ)p|E(H)| ,

∼

S indep. set of H∗

### as any S ⊆ V (H) that is not an independent set of H∗ satisﬁes ∆|S| + |E(H[V \S])| > |E(H)| and hence contributes negligibly to the sum.

3. The graphon formulation of the variational problem

Following [26], we will analyze a continuous version of the discrete variational problem (1.3), which has the advantage of having no dependence on n. Recall that a graphon is a symmetric measurable function W : [0,1]2 → [0,1] (where symmetric means W(x,y) = W(y,x)). In the continuous version of (1.3), W replaces the edge-weighted graph Gn, as the latter can be viewed as a discrete approximation of a graphon (see, e.g., [2,3,23,24] for more on graph limits). We write E[f(W)] :=

[0,1]2 f(W(x,y))dxdy.

´

Deﬁnition 3.1 (Graphon variational problem). For δ > 0 and 0 < p < 1, let

φ(H,p,δ) := inf 12E[Ip(W)] : graphon W with t(H,W) ≥ (1 + δ)p|E(H)| , (3.1) where

t(H,W) := ˆ

W(xi,xj)dx1dx2 ···dx|V (H)| .

[0,1]|V (H)|

(i,j)∈E(H)

For example, for H = K3 we wish to minimize E[Ip(W)] := ˆ

Ip(W(x,y))dxdy over all graphons W whose triangle density

[0,1]2

t(K3,W) = ˆ

W(x,y)W(x,z)W(y,z)dxdydz is at least (1 + δ)p3.

[0,1]3

The solution of the graphon variational problem is given by the following two theorems. Recall Deﬁnitions 1.1 and 1.2 for the independence polynomial PH(x) and the subgraph H∗ of H induced by its maximum degree vertices.

- Theorem 3.2. Let H be a connected ∆-regular graph. Fix δ > 0 and let θ = θ(H,δ) be the unique positive solution to PH(θ) = 1 + δ. Then


min θ , 12δ2/|V (H)| if H is regular, θ if H is irregular.

φ(H,p,δ) p∆ log(1/p)

lim

=

p→0

Let us deduce the continuous version, our main theorem Theorem 1.5, from the discrete analog.

- Lemma 3.3. For any H,p,n,δ, we have φ(H,p,δ) ≤ n−2φ(H,n,p,δ).


Proof. Given weighted graph Gn ∈ Gn with adjacency matrix (aij)1≤i,j≤n, form a graphon WGn as follows: divide [0,1] into n equal-length intervals I1,I2,...,In and set WGn(x,y) = aij if x ∈ Ii,y ∈ Ij and i = j, and WGn(x,y) = p if x,y ∈ Ii for some i. The lemma follows after noting that t(H,Gn) ≤ t(H,WGn) and Ip(WGn) = n−2Ip(Gn) (diagonal entries contribute 0 to Ip(WGn)).

Proof of Theorem 1.5 assuming Theorem 3.2. The upper bound to φ(H,n,p,δ) is given by Proposition 2.1. The lower bound follows by Theorem 3.2 and Lemma 3.3.

It remains to prove Theorem 3.2, which is the goal for the rest of the paper. Note that the upper bound to φ(H,p,δ) follows by Proposition 2.1 and Lemma 3.3. Alternatively, consider the graphon analogs of the clique and anti-clique constructions (see Figure 3):

(a) (Clique graphon) Modify the constant graphon W ≡ p by setting W(x,y) = 1 whenever x,y ∈ [0,a] for a ∼ δ1/|V (H)|. (a) (Anticlique graphon) Modify the constant graphon W ≡ p by setting W(x,y) = 1 whenever min{x,y} ∈ [0,b] for b ∼ θp∆.

(b,1)

- (0,0)
- (0,1) (1,1)


- (0,0) (1,0)
- (0,1) (1,1)


p

p

(0,a)

1

(1,b)

1

(a,0)

(1,0) (a) The clique graphon (b) The anti-clique graphon

Figure 3. Solution candidates for the graphon variational problem (a p∆/2 and b p∆).

By essentially the same calculations as in §2, we have t(H,W) ∼ (1 + δ)p|E(H)| for both graphons above. Calculating their entropies yields the claimed upper bounds to φ(H,p,δ).

4. Preliminaries

In this section, we recall various relevant estimates from [26], used there to solve the continuous variational problem (3.1) for the case of cliques. A key inequality used both in [26] and in its prequel dealing with dense graphs [25] is the following generalization of Hölder’s inequality [16, Theorem 2.1] (closely related to the Brascamp–Lieb inequalities [4]).

- Theorem 4.1 (Generalized Hölder’s inequality). Let µ1,µ2,...µn be probability measures on Ω1,...Ωn resp., and let µ = ni=1 µi. Let A1 ...Am be non-empty subsets of [n] = {1,...n} and for A ⊆ [n] put µA = j∈A µj and ΩA = j∈A Ωj. Let fi ∈ Lpi(ΩAi,µAi) for each i ∈ [m], and


further suppose that i: A

i j(1/pi) ≤ 1 for all j ∈ [n]. Then

ˆ m

m

1/pi

ˆ |fi|pi dµAi

|fi|dµ ≤

.

i=1

i=1

Note that, in particular, if every element of [n] is contained in at most ∆ many sets Aj, then one can take pi = ∆ for all i ∈ [m], giving the inequality

´ |fi|∆ dµAi 1/∆.

f1 ...fmdµ ≤ mi=1

´

We will mostly be applying the generalized Hölder’s inequality with each Ai being a two-element set corresponding to an edge of a graph, and all pi’s set to the maximum degree of the graph. Though there are a few tricky cases where it will be important to use non-uniform pi’s.

Let H be any graph with maximum degree ∆, and let W be a graphon with t(H,W) ≥ (1+δ)p|E(H)|. Since Ip is convex and decreasing from 0 to p and increasing from p to 1, we may assume W ≥ p, i.e.,

U := W − p satisﬁes 0 ≤ U ≤ 1 − p and t(H,p + U) ≥ (1 + δ)p|E(H)| . (4.1)

- For b ∈ (0,1], deﬁne the set Bb of points x with high normalized degree d(x) in U by


Bb = Bb(U) := {x : dU(x) ≥ b}, where d(x) = dU(x) := ˆ 1

U(x,y)dy . (4.2)

0

Hereafter, the dependence on U will be dropped from Bb(U) and dU(x), whenever the graphon U is clear from the context.

By Proposition 2.1, it suﬃces to only consider graphons U satisfying E[Ip(p + U)] p∆Ip(1), where the hidden constant may depend on H and δ. The following consequences of this bound will be frequently used later on.

- Lemma 4.2. Let U be a graphon satisfying5 E[Ip(p + U)] p∆Ip(1). (4.3)


Then

E[U] p(∆+1)/2 log(1/p), (4.4) and

E[U2] p∆ , (4.5) and furthermore Bb = {x : d(x) ≥ b}, with p = o(b), satisﬁes

p∆ b

, (4.6) where λ denotes the Lebesgue measure, and, writing Bb := [0,1]\Bb,

λ(Bb)

ˆ

d(x)2 dx p∆b. (4.7)

Bb

We will prove Lemma 4.2 shortly. The following estimates for Ip(x) were given in [26]. The ∼ notation below is with respect to limits as p → 0.

- Lemma 4.3 ([26, Lemma 3.3]). If 0 ≤ x p, then Ip(p + x) ∼ 21x2/p, whereas when p x ≤ 1 − p we have Ip(p + x) ∼ xlog(x/p).

- Lemma 4.4 ([26, Lemma 3.4]). There is some constant p0 > 0 such that for every 0 < p ≤ p0, Ip(p + x) ≥ (x/b)2Ip(p + b) for any 0 ≤ x ≤ b ≤ 1 − p − log(1 − p).


Corollary 4.5 ([26, Corollary 3.5]). There is some constant p0 > 0 such that for every 0 < p ≤ p0, Ip(p + x) ≥ x2Ip(1 − 1/log(1/p)) ∼ x2Ip(1) for any 0 ≤ x ≤ 1 − p. As a consequence, observe that

x3/2 Ip(p + x)/Ip(1) + o(p2) for any 0 ≤ x ≤ 1 − p. (4.8)

Indeed, this is trivial for x p4/3 due to the o(p2) term; if p2/3 ≤ x ≤ 1 − p then Ip(p + x) xIp(1) by Lemma 4.3; and in between, when p4/3 x ≤ p2/3, we have

Lem 4.3

Lem 4.4

≥ (x/p2/3)2Ip(p + p2/3) x3/2p−2/3Ip(p + p2/3)

x3/2Ip(1).

Ip(p + x)

Proof of Lemma 4.2. From Lemma 4.3 we have Ip p + ap(∆+1)/2 log(1/p) ∼ 12a2p∆Ip(1) for any p ≤ p0 and ﬁxed a ≥ 0 and ∆ ≥ 2. However, Ip(p + E[U]) ≤ E[Ip(p + U)] p∆Ip(1) by the convexity of Ip(·) and (4.3). Therefore, by the monotonicity of Ip(p + x) for x ≥ 0 we obtain the upper bound E[U] p(∆+1)/2 log(1/p), proving (4.4). Finally, using (4.3) and Corollary 4.5 we obtain E[U2] E[Ip(p + U)]/Ip(1) p∆, proving (4.5).

By the convexity of Ip(·), for any b p,

Ip(p + U(x,y))dxdy ≥ ˆ 1

E[Ip(p + U)] = ˆ

Ip(p + dU(x))dx ≥ λ(Bb)Ip(p + b). It follows from Lemma 4.3 (combined with (4.3)) that for any p b ≤ 1 − p,

[0,1]2

0

E[Ip(p + U)] Ip(p + b)

p∆Ip(1) blog(b/p)

p∆ b

λ(Bb) ≤

,

5More precisely, the statement is that for every constant C > 0 there is some constant C > 0 such that if (4.3) holds with constant hidden C, then (4.4)–(4.7) all hold with hidden constant C

- proving (4.6). Furthermore, by the convexity of Ip(x) and Lemma 4.4,

E[Ip(p + U)] ≥ ˆ

Bb

Ip(p + d(x))dx ≥ Ip(p + b)ˆ

Bb

(d(x)/b)2 dx.

Combining these, we get

ˆ

Bb

d(x)2 dx ≤

b2E[Ip(p + U)] Ip(p + b)

p∆b,

- proving (4.7).


5. The triangle and the 4-cycle

In the ﬁrst part of this section, we recall, from [26], a short proof of Theorem 3.2 for the triangle. In the second part, we prove it for the 4-cycle—which already illustrates the diﬃculties in extending the arguments of [26] to general graphs. A key new idea for the 4-cycle is to use an adaptively chosen degree threshold instead of a ﬁxed threshold. This section is not needed for the proof of the general result, but it may be helpful in motivating the general analysis later on.

- 5.1. The variational problem for the triangle. The case of K3 (and larger cliques) was resolved in [26] via a divide-and-conquer approach: roughly put, by setting a certain degree threshold b = b(p) one ﬁnds that, in any graphon whose entropy is of the correct order, the Lebesgue measure of the set Bb of high degree points (deﬁned in (4.2)) asymptotically determines the surplus of K1,2 copies (as


in the anti-clique graphon), whereas the points in Bb are left only with the possibility of contributing extra triangles through “cliques.” We include a (slightly condensed) version of this proof, and explain why a more sophisticated cut-oﬀ b(p) (tailored to each U) is needed for a general H.

- Theorem 5.1 ([26, Theorem 2.2]). Fix δ > 0. As p → 0,


φ(K3,p,δ) ∼ min 12δ2/3 , 13δ p2 log(1/p).

Proof. Let W = p + U with t(K3,W) ≥ (1 + δ)p3. Assume U is nonnegative and satisﬁes (4.3) (or else we are done). Expanding t(K3,W) in terms of U,

t(K3,W) − p3 = t(K3,U) + 3pt(K1,2,U) + 3p2 E[U] ≥ δp3 . (5.1) Now, E[U] = o(p) by (4.4), and so (5.1) reduces to

t(K3,U) + 3pt(K1,2,U) ≥ (δ − o(1))p3 . (5.2) Let Bb = {x : d(x) > b} as in (4.2). By (4.6), for any p b 1 − p we have

ˆ

U(x,y)2 dxdy ≤ λ(Bb)2 p4/b2 p2 . (5.3)

Bb×Bb

Let the degree threshold be some function b = b(p) such that plog(1/p) b 1, and note that

ˆ

U(x,y)U(y,z)U(y,z)11{x ∈ Bb or y ∈ Bb or z ∈ Bb}dxdydz ≤ 3λ(Bb)E[U] p3 , (5.4)

[0,1]3

where the last step uses (4.6) and (4.4). Let

θb := p−2 ˆ

### U(x,y)2 dxdy and ηb := p−2 ˆ

Bb×Bb

Bb×Bb

### U(x,y)2 dxdy . (5.5)

We deduce from (5.4) and generalized Hölder’s inequality (Theorem 4.1) that t(K3,U) = ˆ

U(x,y)U(y,z)U(x,z)dxdydz + o(p3)

Bb×Bb×Bb

3/2

≤ ˆ

### + o(p3) = ηb3/2 + o(1) p3 . Similarly, by (4.7), (5.3), and the Cauchy–Schwarz inequality, we obtain, for any p b 1, t(K1,2,U) = ˆ

U

Bb×Bb

U(x,y)U(x,z)dxdydz + o(p2) ≤ θb + o(1) p2 . (5.6) Combining the above two inequalities with (5.2), we obtain

Bb×Bb×Bb

3θb + ηb3/2 ≥ δ − o(1). By Corollary 4.5,

E[Ip(p + U)] ≥ (1 − o(1)) θb + 12ηb p2 log(1/p) ≥ (1 − o(1)) min

(x + 12y) p2 log(1/p)

x,y≥0 3x+y3/2≥δ

∼ min 12δ3/2, 31δ p2 log(1/p), since the minimum is attained at either x = 0 or y = 0. This together with the clique and anti-clique constructions in §2 (recall that PK3(x) = 3x + 1) completes the proof for the case of triangles.

- 5.2. The variational problem for the 4-cycle. The argument in §5.1 can be applied to other graphs H and rule out certain subgraphs F of H from having a non-negligible contribution to t(H,W) in the expansion analogous to (5.1). However, as we next see, already for H = C4 new ideas are required to tackle all subgraphs of C4 and deduce the correct lower bound on φ(C4,p,δ).


Let W = p + U with t(C4,W) ≥ (1 + δ)p4. As earlier, assume U is nonnegative and satisﬁes (4.3). Expanding t(C4,W) as in (5.1),

δp4 ≤ t(C4,W) − p4 = t(C4,U) + 4p2 t(K1,2,U) + 4pt(P4,U) + 2p2(EU)2 + 4p3 EU , (5.7)

where P4 is the path on 4 vertices and we used that E[U] p from (4.4). By (4.4), E[U] = o(p), we the ﬁnal two terms on the right are negligible.

Let Bb = {x : d(x) > b} as in (4.2). By generalized Hölder’s inequality, embeddings P4  → (w,x,y,z) ∈ [0,1]4 with x ∈ Bb satisfy

ˆ

U(w,x)U(x,y)U(y,z)dwdxdydz

[0,1]×Bb×[0,1]×[0,1]

= ˆ

d(x)U(x,y)U(y,z)dxdydz

Bb×[0,1]×[0,1]

1/2 ˆ 1

√

≤ ˆ

d(x)2 dx

U(x,y)2 dxdy p3

b p3

Bb

0

by (4.7) and (4.5), and using b = o(1) for the last inequality. Hence, embeddings of P4 with a non-negligible contribution to t(P4,U) must place both of the interior (degree 2) vertices in Bb. The contribution from such embeddings is therefore at most λ(Bb)2 p4/b2 p3, provided b √p. Hence, t(P4,U) = o(p3).

We have already encountered the term t(K1,2,U) previously when analyzing H = K3. So let us focus our attention on the term t(C4,U). For convenience, write

U(w,x,y,z) := U(w,x)U(x,y)U(y,z)U(z,w).

Bb Bb

Bb Bb

Bb Bb

| |
|---|


| |
|---|


| |
|---|


Bb Bb

Bb Bb

Bb Bb

(a) (b) (c)

≤ Bb×Bb U2(x,y)dxdy 2 = δ22p4 o(p4) (a) (b) (c)

≤ Bb×Bb U2(x,y)dxdy 2 = δ12p4

Figure 4. Diﬀerent embeddings of the 4-cycle: (a) and (b) are non-negligible. By (4.6) and (4.4),

ˆ

U(w,x,y,z)dwdxdydz ≤ λ(Bb)2E[U] p4 . (5.8)

Bb×Bb×[0,1]×[0,1]

So any embedding placing two consecutive vertices of C4 in Bb is negligible. As in (5.5), set

θb := p−2 ˆ

### U(x,y)2 dxdy and ηb := p−2 ˆ

U(x,y)2 dxdy .

Bb×Bb

Bb×Bb

The three other possible embeddings of C4 (see Fig. 4 for an illustration) are handled via generalized Hölder’s inequality as follows.

- (a) Two nonadjacent vertices in Bb (2 conﬁgurations): ˆ

Bb×Bb×Bb×Bb

U(w,x,y,z)dwdxdydz ≤ ˆ

Bb×Bb

U2

2

≤ θb2 + o(1) p4 . (5.9)

- (b) No vertices in Bb (1 conﬁguration): ˆ

Bb×Bb×Bb×Bb

U(w,x,y,z)dwdxdydz ≤ ˆ

Bb×Bb

U2

2

≤ ηb2 + o(1) p4 . (5.10)

- (c) A single vertex in Bb (4 conﬁgurations): ˆ


### U(w,x,y,z)dwdxdydz ≤ ˆ

### U2 ˆ

U2 ≤ (θbηb + o(1))p4 . (5.11)

Bb×Bb×Bb×Bb

Bb×Bb

Bb×Bb

(As we will see shortly, this ﬁnal estimate is not tight.) Combining (5.8), (5.9)–(5.11) and the estimate (5.6) for t(K1,2,U), the expansion (5.7) gives 2θb2 + ηb2 + 4θbηb + 4θb ≥ δ − o(1), (5.12)

valid for any √p b 1. As in the case of K3, we wish to minimize θb + 12ηb subject to this constraint. Unfortunately, the minimum of θb + 12ηb subject to (5.12) is not attained at θb = 0 or ηb = 0. Thus the lower bound obtained in this way does not match the upper bound from Proposition 2.1.

Recall the clique and anti-clique graphons in §3. The main contribution of the anti-clique to t(C4,U) is through embeddings of type (a), whereas for the clique it is through embeddings of

- type (b). For the correct lower bound, we must show that the contribution from embeddings of
- type (c) is negligible; however, this can no longer be achieved using any arbitrary √p b 1. To conclude the proof, we select the degree threshold b adaptively based on the graphon U.


- Lemma 5.2 (Adaptive degree threshold for C4). Assume that U satisﬁes (4.3). There exists b (possibly depending on U) with √p b 1 such that


ˆ

U(w,x,y,z)dwdxdydz = o(p4). (5.13)

Bb×Bb×Bb×Bb

Proof. It suﬃces to show that for every constant ε > 0, we can ﬁnd b = b(U,p,ε) with √p b 1 such that ˆ

U(w,x,y,z)dwdxdydz ≤ εp4

Bb×Bb×Bb×Bb

provided that p is small enough. By generalized Hölder’s inequality, t(C4,U) ≤ E[U2]2 p4 by (4.5). So we can ﬁx some constant C > 0 such that t(C4,U) ≤ Cp4. Set M = 2C/ε . Further let √p b1 b2 ··· bM 1. As usual, set Bbi = {x : d(x) > bi}, and note that BbM ⊆ ... ⊆ Bb1. For every 2 ≤ i ≤ M, using (4.6) and (4.7) we ﬁnd that

bi−1 bi

ˆ

### U(w,x,y,z)dwdxdydz ≤ λ(Bbi)ˆ

d(x)2 dx

p4 p4 . (5.14)

Bbi×Bbi×Bbi−1×Bbi

Bbi−1

Thus, setting b = bi works provided that

ˆ

U(w,x,y,z)dwdxdydz ≤ 12εp4 . (5.15)

Bbi×Bbi×(Bbi−1\Bbi)×Bbi

We ﬁnish the proof by observing that there is necessarily some 2 ≤ i ≤ M satisfying (5.15), as otherwise—since the sets {Bbi × Bbi × (Bbi−1\Bbi) × Bbi : 2 ≤ i ≤ M} are mutually disjoint—we would get t(C4,U) > (Mε/2)p4 ≥ Cp4, a contradiction to our choice of C.

Remark 5.3. Note the advantage of using multiple thresholds with bi−1 bi in the proof of

- Lemma 5.2: a single threshold function bi ≡ b (as in §5.1) would have given a bound of O(p4) for the left-hand of (5.14) vs. the sought o(p4). This idea will be crucial in our arguments for general graphs.


Combining the above estimates, the expansion (5.7) implies (this is (5.12) with the extraneous 4θbηb term deleted)

2θb2 + 4θb + ηb2 ≥ δ − o(1). By Corollary 4.5,

E[Ip(p + U)] ≥ (1 − o(1)) θb + 12ηb p2 log(1/p) ≥ (1 − o(1)) min

(x + 12y) p2 log(1/p).

x,y≥0 2x2+4x+y2≥δ

This minimum is attained at either x = 0 or y = 0 by the following lemma, thereby giving the bound for φ(C4,p,δ) matching the one from Proposition 2.1 (recall that PC4(x) = 2x2 + 4x + 1).

- Lemma 5.4. Let f,g be convex nondecreasing functions on [0,∞) and let a > 0. The minimum of x + y over the region {x,y ≥ 0 : f(x) + g(y) ≥ a} is attained at either x = 0 or y = 0.


Proof. By convexity, if γ = x+yy then f(x) ≤ γf(0)+(1−γ)f(x+y) and g(y) ≤ (1−γ)g(0)+γg(x+y), so

f(x) + g(y) ≤ γ[f(0) + g(x + y)] + (1 − γ)[f(x + y) + g(0)] ≤ max{f(0) + g(x + y), f(x + y) + g(0)}.

This shows that for a ﬁxed value of x + y, f(x) + g(y) is maximized at x = 0 or y = 0. The claim then follows.

6. General graphs

We begin the analysis for a general graph H. As always, ∆ ≥ 2 denotes the maximum degree of H.

- 6.1. Decomposition. We can expand t(H,W) = t(H,p + U) as


t(H,W) − p|E(H)| =

F

N(F,H)t(F,U)p|E(H)|−|E(F)| , (6.1)

where the sum is taken over non-empty subgraphs F of H (up to isomorphism) and N(F,H) is the number of subgraphs of H isomorphic to F. Assuming U satisﬁes (4.3) (in particular the consequence (4.5) E[U2] p∆), every term on the right-hand side of (6.1) is of order O(p|E(H)|), since by generalized Hölder’s inequality,

t(F,U) ≤ (E[U∆])|E(F)|/∆ ≤ (E[U2])|E(F)|/∆ p|E(F)| . (6.2)

However this bound is often not tight, as many contributions are negligible in that t(F,U) = o(p|E(F)|), as we saw earlier in the case H = K3 and K4. We proceed by identifying and bounding the nonnegligible terms.

- 6.2. Negligible terms. Let τ(F) denote the minimum size of a vertex cover of F, where a vertex cover of F is a subset of vertices that intersects every edge of F.


- Lemma 6.1. Let ∆ ≥ 2 and U be a graphon satisfying (4.3), i.e., E[Ip(p + U)] p∆Ip(1). Let F be a connected graph with maximum degree at most ∆. If τ(F) > |E(F)|/∆ and F is not ∆-regular, there is some constant κ = κ(F) > 0 such that t(F,U) p|E(F)|+κ = o(p|E(F)|).


We will prove this lemma shortly. Note that every subgraph F of H satisﬁes τ(F) ≥ |E(F)|/∆. Due to the above lemma, the set of subgraphs

FH := {F : F is a non-empty subgraph of H with τ(F) = |E(F)|/∆} (6.3)

plays an important role. Let us highlight some basic properties of FH for a connected graph H, all of which are easy to prove.

- • Every F ∈ FH is bipartite and has maximum degree exactly ∆.
- • If S is a minimum size vertex cover of F ∈ FH, then S is an independent set and every vertex of S has degree ∆ in F; furthermore, (S,V (F)\S) forms a vertex bipartition of F. Conversely, any non-empty independent set S of H∗ (i.e., an independent set of H consisting

of degree ∆ vertices in H) gives rise to an F ∈ FH with S as a minimum vertex cover by forming F using the edges of H incident to S.

- • Every F ∈ FH has a unique minimum vertex cover except when H is a regular bipartite graph, in which case H ∈ FH has two diﬀerent minimum vertex covers (corresponding to two sides of the vertex partition; here we use that H is connected).
- • For a regular graph H, we have H ∈ FH if and only if H is bipartite.


- Corollary 6.2. Let H be a connected graph with maximum degree ∆ ≥ 2, and F a non-empty


subgraph of H. Let U be a graphon satisfying (4.3). Then t(F,U) = o(p|E(F)|) unless F ∈ FH or F is ∆-regular (in the latter case necessarily F = H). Consequently,

t(H,W) − p|E(H)| =

N(F,H)t(F,U)p|E(H)|−|E(F)| + o(p|E(H)|). (6.4)

F∈FH∪{H}

If H is irregular, one can replace the “FH ∪ {H}” in the summation by simply “FH”.

Proof. Suppose τ(F) > |E(F)|/∆ and F is not ∆-regular. Let F1,...,Fk be the connected components of F. Since τ(F) = τ(F1)+···+τ(Fk), we see that some Fi, say F1, satisﬁes τ(F1) > |E(F1)|/∆. Furthermore this F1 is not ∆-regular, since H has no ∆-regular subgraphs other than possibly itself due to its connectedness, and we have ruled out the possibility of F = H being ∆-regular in the hypothesis. Therefore t(F1,U) = o(p|F1|) by Lemma 6.1 and t(Fi,U) = O(p|Fi|) for i ≥ 2 by (6.2). Therefore t(F,U) = t(F1,U)···t(Fk,U) = o(p|E(F)|) as claimed. The claim (6.4) is then deduced from (6.1).

From the correspondence between FH and independent sets of H∗, we obtain PH∗(x) = 1 +

N(F,H)x|E(F)|/∆ + 1{H is regular and bipartite}x|E(H)|/∆ . (6.5)

F∈FH

In §7 and §8 we will relate each term t(F,U)p|E(H)|−|E(F)| in the right-hand of (6.4) to θ|E(F)|/∆p|E(H)| where θ is deﬁned analogously to (5.5).

We will prove Lemma 6.1 by using generalized Hölder’s inequality with non-uniform weights. The fractional matching number, denoted ν∗(F), is the maximum value of w(E(F)) := e∈E(F) w(e) over all weight functions w : E(F) → [0,1] such that e v w(e) ≤ 1 for every vertex v ∈ F, i.e., ν∗(F) is the linear relaxation of the matching number ν(F), which corresponds to restricting w(e) to {0,1}-values. Recall that the matching number ν(F) is the size of the largest matching of F, where a matching is a subset of edges with no two edges sharing a vertex.

One has ν(H) ≤ τ(H) for every graph H. König’s theorem tells us that this is always an equality when H is bipartite. König’s theorem. For every bipartite graph H, ν(H) = τ(H).

- Lemma 6.3. Let ∆ ≥ 2 and F a connected graph with maximum degree at most ∆ and not ∆-regular. If τ(F) > |E(F)|/∆, then


ν∗(F) > |E(F)|/∆.

Proof. We have ν(F) ≤ ν∗(F) ≤ τ(F) by linear programming duality. If F is bipartite, then ν(F) = τ(F) by König’s theorem, so ν∗(F) = τ(F) > |E(F)|/∆ by hypothesis.

Now assume that F is not bipartite, and let C be an odd cycle in F. Let u0 ∈ V (F) with degF(u0) < ∆. Let P be a shortest path in F from u0 to C (using that F is connected) and let the vertices of P be u0,u1,...,ur. Write the vertices of C as v0,...,v2k with v0 = ur. We now perturb the constant weights w ≡ 1/∆ into new weights w by, for each 0 ≤ j ≤ r − 1, adding (−1)jε to the weight of edge (uj,uj+1) along the path, and, for each 0 ≤ j ≤ 2k, adding (−1)j+rε/2 to the weight of edge (vj,vj+1) along the cycle (index taken modulo 2k + 1). Since C is an odd cycle,

e v w (e) = e v w(e) for all v = u0. Thus, w is admissible as long as ε is small enough. Finally, if r is even then w (P) = w(P) and w (C) = w(C) + ε/2, and if r is odd then w (P) = w(P) + ε and w (C) = w(C) − ε/2. Either way, ν∗(F) ≥ w (E(F)) = E(F)/∆ + ε/2.

- Lemma 6.4. Let ∆ ≥ 2 and U a graphon satisfying (4.3). Let F be a graph with maximum degree at most ∆. If ν∗(F) > |E(F)|/∆, then there is some constant κ = κ(F) > 0 such that t(F,U) p|E(F)|+κ.


Proof. Since ν∗(F) > |E(F)|/∆, the function w ≡ 1/∆ is not a local maximum of the linear program deﬁning ν∗(F). If ∆ = 2, one can perturb w ≡ 1/2 into w : E(F) → [0,2/3], such that

v e w (e) ≤ 1 and e∈E(F) w (e) ≥ (|E(F)| + κ)/2 for some constant κ > 0. By generalized

Hölder’s inequality with these weights, t(F,U) ≤

E[U1/w (e)]w (e) ≤ E[U3/2](|E(F)|+κ)/2

e∈E(F)

(4.3)

(4.8)

≤ E[Ip(p + U)]/Ip(1) + o(p2) (|E(F)|+κ)/2

p|E(F)|+κ . If ∆ ≥ 3, one can perturb w ≡ 1/∆ into w : E(F) → [0,1/2] such that v e w (e) ≤ 1 and

e∈E(F) w (e) ≥ (|E(F)| + κ)/∆ for some constant κ > 0. By generalized Hölder’s inequality with these weights,

(4.5)

E[U1/w (e)]w (e) ≤ E[U2](|E(F)|+κ)/∆

t(F,U) ≤

e∈E(F)

- Lemma 6.1 follows immediately by combining Lemmas 6.3 and 6.4.


p|E(F)|+κ .

- 6.3. Main terms. We now state upper bounds to the non-negligible terms t(F,U) in (6.4), namely


for F ∈ FH, as well as F = H in the case when H is regular. Recall from (4.2) that we denote the set of high degree vertices in U by

Bb = {x : d(x) ≥ b}, where d(x) = ˆ 1

U(x,y)dy .

0

Deﬁne (compared to (5.5) we have p−∆ here instead of p−2)

θb := p−∆ ˆ

### U(x,y)2dxdy and ηb := p−∆ ˆ

U(x,y)2dxdy . (6.6) For any graph F, we write

Bb×Bb

Bb×Bb

W(x|F) :=

W(xi,xj),

(i,j)∈E(F)

where x = (xv)v∈V (F) is clear from context. If the domain of an integral is omitted, then it is assumed to be [0,1] for every xv.

Proposition 6.5. Let ∆ ≥ 2 and U be a graphon satisfying (4.3).

- (a) Let F be a connected irregular bipartite graph with maximum degree ∆ and τ(F) = |E(F)|/∆. Let A be the unique vertex cover of F with size |E(F)|/∆. Then, for any p1/3 b 1,

t(F,U) = ˆ U(x|F)1 ∀v ∈ A: xv ∈ Bb ∀u ∈/ A: xu ∈ Bb

dx + o(p|E(F)|)

≤ θb|E(F)|/∆p|E(F)| + o(p|E(F)|).

- (b) Let H be a connected ∆-regular non-bipartite graph. Then there exists some constant κ = κ(H) > 0 such that for any pκ ≤ b 1 one has

t(H,U) = ˆ U(x|H)1 ∀v ∈ V (H): xv ∈ Bb dx + o(p|E(H)|)

≤ ηb|E(H)|/∆p|E(H)| + o(p|E(H)|).

- (c) Let H be a connected ∆-regular bipartite graph with vertex bipartition (A,V (H)\A). For any b0 = o(1), there exists some b with b0 ≤ b 1 such that


t(H,U) = Γ1 + Γ2 + Γ3 + o(p|E(H)|)

where

- Γ1 = ˆ U(x|H) ∀v ∈ A: xv ∈ Bb ∀u ∈/ A: xu ∈ Bb

dx + o(p|E(H)|)

≤ θb|E(H)|/∆p|E(H)| + o(p|E(H)|),

- Γ2 = ˆ U(x|H) ∀v ∈ A: xv ∈ Bb ∀u ∈/ A: xu ∈ Bb

dx + o(p|E(H)|)

≤ θb|E(H)|/∆p|E(H)| + o(p|E(H)|),

- Γ3 = ˆ U(x|H) ∀v ∈ V (H): xv ∈ Bb dx + o(p|E(H)|)


≤ ηb|E(H)|/∆p|E(H)| + o(p|E(H)|).

Note that each “≤” in the statement of the proposition above follows from the generalized Hölder’s inequality. For example, in (a), one bounds the integral from above by

|E(F)|/∆

|E(F)|/∆

ˆ

≤ ˆ

= θb|E(F)|/∆p|E(F)| .

U∆

U2

Bb×Bb

Bb×Bb

We will prove part (a) of Proposition 6.5 in §7 and parts (b) and (c) in §8. Now we use the proposition to deduce the main result about the asymptotic solutions to the variational problem. Proof of Theorem 3.2 assuming Proposition 6.5. The upper bound to φ(H,p,δ) has been handled by the clique and anti-clique constructions. It remains to prove the lower bounds.

First we consider the case with H being irregular, which only requires part (a) of Proposition 6.5.

Set b = p1/4. By applying Proposition 6.5(a) to connected components of F ∈ FH (and noting (6.2)), we have, by (6.4),

t(H,W) − p|E(H)| =

N(F,H)t(F,U)p|E(H)|−|E(F)| + o(p|E(H)|).

F∈FH

N(F,H)θb|E(F)|/∆p|E(H)| = p|E(H)| (PH∗(θb) − 1) . (6.7)

≤ p|E(H)|

F∈FH

So t(H,W) ≥ (1 + δ)p|E(H)| implies PH∗(θb) ≥ 1 + δ − o(1). Recall that θ satisﬁes PH∗(θ) = 1 + δ. So θb ≥ θ − o(1). By Corollary 4.5,

E[Ip(p + U)] ≥ (θb − o(1))p∆ log(1/p) ≥ (θ − o(1))p∆ log(1/p). This completes the proof in the case of irregular H.

Now assume that H is regular. Proposition 6.5 implies that there is some b = o(1) such that

t(H,W) ≤ p|E(H)|(PH∗(θb) + ηb|E(H)|/∆ + o(1)). (6.8) Indeed, we bound the terms in the expansion (6.4) of t(H,W) = t(H,p + U) by applying Proposition 6.5 and then match them to the terms of PH∗ in (6.5). As earlier, Proposition 6.5 is applied to the connected components of F; recall that since H is connected, no subgraph other than itself can be ∆-regular. It is also worth noting that if H is bipartite and regular then H ∈ FH contributes twice in both (6.4) and (6.5).

So t(H,W) ≥ (1 + δ)p|E(F)| implies PH∗(θb) + ηb|E(H)/∆ ≥ 1 + δ − o(1), which, by Lemma 5.4, implies that θb + 12ηb ≥ min{θ, 12δ2/|V (H)|} − o(1) as PH∗(θ) = 1 + δ. Thus, by Corollary 4.5,

E[Ip(p + U)] ≥ (θb + 21ηb − o(1))p∆ log(1/p) ≥ (min{θ, 21δ2/|V (H)|} − o(1))p∆ log(1/p).

Thereby completing the proof in the case of regular H.

It remains to prove Proposition 6.5, which will be done in the next two sections. Roughly, the idea is to eliminate negligible contributions from t(F,U) (or t(H,U) in parts (b) and (c)) by taking a certain subgraph M of F with maximum degree 2 (i.e., a disjoint union of cycles and paths), so that U(x|F) ≤ U(x|M). This reduces the problem to paths and cycles. We then extend the analysis of the triangle and the 4-cycle in §5 to handle these cases.

7. Bounding contributions from irregular components In this section we prove Proposition 6.5(a). We ﬁrst need a preparatory lemma.

- 7.1. Existence of a 2-matching. We say that a subset M of edges of F is a 2-matching if M is a union of two matchings of F (equivalently M is a disjoint union of paths and even cycles).6 The following lemma is the main result of this section, and it will be used for proving Proposition 6.5(a). The reader may wish to skip its proof on the ﬁrst reading.


- Lemma 7.1. Let F be a connected irregular bipartite graph with maximum degree ∆ and τ(F) = |E(F)|/∆. For every vertex v of F, there is a 2-matching M of F of size 2|E(F)|/∆ such that the connected component of v in M is a path.


Recall that a proper edge-coloring is a coloring of edges so that edges that share a common vertex receive diﬀerent colors. The following result is classic. See [22, Theorem 1.4.18] for a proof via embedding the graph in a larger ∆-regular graph.

König’s edge-coloring theorem. Every bipartite graph of maximum degree ∆ has a proper edgecoloring with ∆ colors.

- Corollary 7.2. Every bipartite graph has a maximum matching which covers all maximum degree vertices.


Proof. Let G be the bipartite graph and ∆ its maximum degree. By König’s edge-coloring theorem, G has a proper edge-coloring of the graph with ∆ colors. Every degree ∆ vertex is incident to all ∆ colors. Let M denote the edges of an arbitrary color class. Then M is a matching that covers all degree ∆ vertices. If M is not a maximum matching, then we can repeatedly replace M by a larger matching via “augmenting paths” [22, Theorem 1.2.1], while maintaining the property that all degree ∆ vertices are covered by M. The process terminates with a maximum matching M that covers all degree ∆ vertices.

Returning to Lemma 7.1, note that if we apply König’s edge-coloring theorem to F and take M to be the union of two arbitrary color classes, then M is a 2-matching of F of size 2|E(F)|/∆. It remains to modify M so that the connected component of v in M is a path.

Proof of Lemma 7.1. The result is easy when ∆ = 2, in which case we can take M = F. So assume ∆ ≥ 3 from now on.

Let (A,B) be a vertex bipartition of F. Due to F being connected and τ(F) = |E(F)|/∆, either A or B must be unique minimum vertex cover of F. Relabeling if necessary, assume that A is the minimum vertex cover. So τ(F) = |E(F)|/∆ = |A| < |B| as F is irregular, and degF(v) = ∆ for every v ∈ A.

First consider the case v ∈ B. We will show that in fact we can have degM(v) = 1. If degF(v) < ∆, then by König’s edge-coloring theorem, the edges of F can be partitioned into ∆ matchings of size |A|. We obtain the desired M by taking two such matchings, with one matching covering v and the other matching not covering v (we can do this since 1 ≤ degF(v) < ∆).

6This diﬀers slightly from the notion of 2-matchings in the literature (cf. [22]), the deﬁnition here being a special case.

Now suppose v ∈ B and degF(v) = ∆. Since F is connected and irregular, and degF(a) = ∆ for every a ∈ A, we see that every S ⊆ A has at least |S| + 1 neighbors in B (otherwise we would have a ∆-regular component). Let F − v denote F with v removed (along with edges incident to v). Apply Hall’s matching theorem to F − v and we ﬁnd that the maximum matching of F − v has size |A|. Then Corollary 7.2 applied to F − v gives a matching M1 of size |A| in F not covering v but covering every other vertex of degree ∆ in B. Let F denote F with M1 removed. We claim that F has a matching of size |A|, since otherwise König’s theorem would imply that F has a vertex cover of size |A| − 1, which is impossible since F has |A|(∆ − 1) edges, and all its vertices have degree at most ∆ − 1 with the exception of v, which has degree ∆. Thus, by Corollary 7.2 again, we can ﬁnd a matching M2 in F of size |A| that covers v. Taking M = M1 ∪ M2 works.

Finally, suppose v ∈ A. Let u ∈ B be an arbitrary neighbor of u. By above, there is a 2-matching

M of size 2|A| such that degM(u) = 1. If (u,v) ∈ M, then we are done. Otherwise, let w be an arbitrary neighbor of v in M, and modify M by removing (v,w) and adding (u,v). Then v lies on a path component in the modiﬁed M.

- 7.2. Proof of Proposition 6.5(a). The claim follows from the next two lemmas.


- Lemma 7.3. Let ∆ ≥ 2 and U be a graphon satisfying (4.3). Let F be a bipartite graph with maximum degree ∆ and τ(F) = |E(F)|/∆. Let A be its unique vertex cover of size |E(F)|/∆. As long as b p1/3,


ˆ U(x|F)1{∃(i,j) ∈ E(F): xi,xj ∈ Bb}dx = o(p|E(F)|). Proof. Fix an edge (i,j) ∈ E(F). It suﬃces to prove that

ˆ U(x|F)1{xi,xj ∈ Bb}dx = o(p|E(F)|).

By König’s edge-coloring theorem, there is a proper edge-coloring of F with ∆ colors, so that each color class is a matching of size exactly |E(F)|/∆ (since every vertex in A must see all edge-colors). Thus there exists a 2-matching M of F of size 2|E(F)|/∆ such that (i,j) ∈ E(M). Let M be obtained from M by removing the edges incident to either i or j. So 2 ≤ |M\M | ≤ 3 (since one of i and j has degree ∆ in H, and hence degree 2 in M). Hence

ˆ U(x|M)1{xi,xj ∈ Bb}dx ≤ λ(Bb)2 ˆ U(x|M )dx ≤ λ(Bb)2 E[U2]|E(M )|/2

2

p∆ b

∆(|E(M)|−3)

2 b−2p|E(F)|+∆2 p|E(F)| .

p

The second inequality is by generalized Hölder’s inequality. The next is due to (4.6) and (4.5). Finally, since U(x|F) ≤ U(x|M), the claim follows.

- Lemma 7.4. Let ∆ ≥ 2 and U be a graphon satisfying (4.3). Let F be a connected irregular bipartite graph with maximum degree ∆ and τ(F) = |E(F)|/∆. Let A be its unique vertex cover of size |E(F)|/∆. Then, as long as b = o(1), one has


ˆ U(x|F)1{∃v ∈ A: xv ∈ Bb}dx = o(p|E(F)|). Fix v ∈ A. It suﬃces to show that

ˆ U(x|F)1{xv ∈ Bb}dx = o(p|E(F)|).

Let M be a 2-matching of F of size 2|A| such that the connected component of v in M is a path. The existence of this 2-matching is guaranteed by Lemma 7.1. Let M1,M2,...,Mq be the connected

components of M, labeled so that M1 is the connected component of v in M. In particular, M1 is a path. Note that U(x|F) ≤ U(x|M) and

t(Mi,U) ≤ E[U2]|E(Mi)|/2 p∆|E(Mi)|/2 for each 1 ≤ i ≤ q (7.1) by generalized Hölder’s inequality and (4.5). Lemma 7.4 is reduced to proving

ˆ U(x|M1)1{xv ∈ Bb}dx = o(p∆|E(M1)|/2), which follows from the next lemma. Lemma 7.5. Let ∆ ≥ 2 and be positive integers, and U a graphon satisfying (4.3). Let P denote a path on 2 + 1 vertices labeled 1,2,...,2 + 1. Then, for every 1 ≤ k ≤ , as long as b = o(1),

ˆ U(x|P)1{x2k ∈ Bb} = o(p∆ ). (7.2) Proof. Since the left-hand side of (7.2) cannot decrease as b gets larger, we may assume that b p.

We use induction on k. For k = 1, we have, by generalized Hölder’s inequality followed by (4.5) and (4.7),

ˆ U(x|P)1{x2 ∈ Bb}dx = ˆ 1{x2 ∈ Bb}d(x2)U(x2,x3)···U(x2 ,x2 +1)dx

1/2

≤ ˆ

E[U2](2 −1)/2 (p∆b)1/2p∆(2 −1)/2

d(x1)2 dx1

Bb

√

bp∆ = o(p∆ ). Now let us prove claim for k ≥ 2 assuming that

=

ˆ U(x|P)1{x2k−2 ∈ Bb } = o(p∆ ) (7.3)

holds for any b = o(1), and in particular, for b = b1/3. By removing vertex 2k − 2 from P and then applying generalized Hölder’s inequality followed by Lemma 4.2, we have, for any p b ,b 1,

ˆ U(x|P)1{x2(k−1) ∈ Bb ,x2k ∈ Bb}dx

≤ λ(Bb )ˆ U(x1,x2)···U(x2k−4,x2k−3) · 1{x2k ∈ Bb}U(x2k−1,x2k)U(x2k,x2k+1)···U(x2 ,x2 +1)dx

≤ λ(Bb )ˆ U(x1,x2)···U(x2k−4,x2k−3) · 1{x2k ∈ Bb}d(x2k)U(x2k,x2k+1)···U(x2 ,x2 +1)dx

1/2

≤ λ(Bb ) ˆ

E[U2](2 −3)/2 p∆ b

d(x2k)2 dx2k

Bb

√

b b

(p∆b)1/2p∆(2 −3)/2 =

p∆ ,

which is o(p∆ ) if b = b1/3. Combining with (7.3), we obtain (7.2). This completes the induction step.

We have completed the proof of our main result, Theorem 3.2, for irregular graphs H.

8. Bounding contributions from regular graphs

- 8.1. Proof of Proposition 6.5(b). Here H is a connected ∆-regular non-bipartite graph. Fix v ∈ V (H). Let H − v denote H after deleting v (and all edges incident to v). We see that H − v is not ∆-regular and satisﬁes τ(H − v) > |E(H − v)|/∆ (or else putting v back in would give τ(H) = |E(H)|/∆, which is impossible as H is non-bipartite). Thus by Lemma 6.1, there is some constant κ > 0 such that t(H − v,U) p|E(H−v)|+κ = p|E(H)|−∆+κ (here we apply Lemma 6.1 to some connected component H of H − v satisfying τ(H ) > |E(H )|/∆ and use (6.2) to bound the other components; note that H has no ∆-regular subgraphs other than itself due to its connectedness).

Thus ˆ U(x|H)1{xv ∈ Bb}dx ≤ λ(Bb)t(H − v,U)

p∆ b

p|E(H)|−∆+κ = o(p|E(H)|), provided that b pκ. Proposition 6.5(b) then follows after considering all v ∈ V (H).

- 8.2. Proof of Proposition 6.5(c). Here H is a connected ∆-regular bipartite graph. Proposition 6.5(c) is an immediate consequence of Lemma 7.3 and the following lemma.


- Lemma 8.1. Let ∆ ≥ 2 and U be a graphon satisfying (4.3). Let H be a ∆-regular bipartite graph. For any b0 = o(1), there exists some b with b0 ≤ b 1 such that

ˆ U(x|H)1{∃v ∈ V (H),u,w ∈ NH(v): xu ∈ Bb,xw ∈ Bb}dx = o(p|E(H)|), where NH(v) is the neighborhood of the vertex v in H.

To deduce Proposition 6.5(c) for a connected graph H, note that Lemma 8.1 implies that to estimate t(H,U) up to o(p|E(H)|), one only needs to consider embeddings of H where the vertices on the same side of the bipartition of H get mapped to the same choice of Bb versus Bb. Furthermore, the case of both sides getting mapped to Bb is eliminated by Lemma 7.3. The possibilities of Bb versus Bb are captured by Γ1, Γ2, and Γ3 in Proposition 6.5(c).

Now we prove Lemma 8.1. By König’s edge-coloring theorem, H has a proper edge-coloring with exactly ∆ colors, where every color class is a perfect matching. For each path u,v,w, by taking the union of the two color classes that contain edges (u,v) and (v,w), we obtain a 2-matching containing the path u,v,w, which must be a disjoint union of cycles. Note that any cycle C in H satisﬁes

t(C ,U) ≤ E[U2] /2 p ∆/2 (8.1)

by generalized Hölder’s inequality and (4.5). As in Lemma (7.4), by isolating the cycle in the 2-matching that contains the vertices u,v,w, Lemma 8.1 follows from the following claim. Its proof is an extension of the 4-cycle case in §5.2.

- Lemma 8.2. Let ∆ ≥ 2 and L be positive integers, and U a graphon satisfying (4.3). For any b0 = o(1), there exists some b with b0 ≤ b 1 such that


ˆ U(x|C )1{x1 ∈ Bb,x3 ∈ Bb}dx = o(p∆ /2) uniformly for all 3 ≤ ≤ L, where the vertices of the cycle C are labeled 1,2,...,  in cyclic order. Proof. Fix ε ≥ 0 (which can be made arbitrarily small). It suﬃces to show that one can ﬁnd b (depending on ε, L and U) with b0 ≤ b 1 such that

ˆ U(x|C )1{x1 ∈ Bb,x3 ∈ Bb}dx ≤ (1 + o(1))εp∆ /2 (8.2) uniformly for all 3 ≤ ≤ L.

By removing the vertex labeled 1 and then applying generalized Hölder’s inequality followed by Lemma 4.2, we have, for any p b ,b 1,

ˆ U(x|C )1{x1 ∈ Bb ,x3 ∈ Bb }dx

≤ λ(Bb )ˆ 1{x3 ∈ Bb }U(x2,x3)U(x3,x4)···U(x −1,x )dx

≤ λ(Bb )ˆ 1{x3 ∈ Bb }d(x3)U(x3,x4)···U(x −1,x )dx

1/2

≤ λ(Bb ) ˆ

E[U2]( −3)/2 p∆ b

d(x3)2 dx3

Bb

√

b b

(p∆b )1/2p∆( −3)/2

p∆ /2 . (8.3)

Fix some for now. By (8.1), there is some constant C such that t(C ,U) ≤ Cp ∆/2. Let M := C/ε . Since it never hurts to make b0 larger, assume that p b0 1. For any sequence b0 < b1 < ··· < bM = o(1) with bi−1 ≤ b3i for each i ≤ M, there is some 1 ≤ i ≤ M such that

ˆ U(x|C )1{x1 ∈ Bbi,x3 ∈ Bbi−1\Bbi}dx ≤ εp ∆/2

since otherwise the sum of these integrals over 1 ≤ i ≤ M (note that the sets Bbi−1\Bbi, 1 ≤ i ≤ M, are disjoint) would violate t(C ,U) ≤ Cp ∆/2. Combining the above estimate with (8.3) applied with

b = bi and b = bi−1 (so that √

b /b = o(1)), we see that (8.2) holds with b = bi (for this speciﬁc ).

To deduce (8.2) for all 3 ≤ ≤ L, we start with the sequence b0 < b1 < ··· < bML satisfying bi−1 ≤ b3i for each i (e.g., take bi = b30−i). Iteratively, for each 3 ≤ ≤ L, use the above argument to take a subsequence keeping at least 1/M fraction of the terms so that b = bi satisﬁes (8.2) for this

for every bi in the remaining subsequence. At the end of the process, we ﬁnd some b = bi that satisﬁes (8.2) for all 3 ≤ ≤ L. Remark 8.3. As mentioned below Theorem 1.5, when H is regular and n−2/∆ p n−1/∆ (a range in which the anti-clique construction is no longer applicable), it follows from our arguments that

φ(H,n,p,δ) n2p∆ log(1/p)

= 12δ2/|V (H)| .

lim

n→∞

Indeed, the upper bound follows from the clique construction in Proposition 2.1(a), and it remains to verify the lower bound. Since np∆ = o(1), in the above arguments, we can choose our threshold b such that np∆ b 1, and thus λ(Bb) p∆/b n−1 by (4.6). Since nλ(Bb) must be an integer in the discrete setting, we must have λ(Bb) = 0, which rules out the anti-clique construction, thereby proving the claim.

9. Disconnected graphs

The arguments at the end of (6.3) can be easily modiﬁed to handle disconnected graphs by considering the diﬀerent connected components. The solution of the variational problem can be expressed as a two variable constrained optimization problem.

Theorem 9.1. Let H be a graph with maximum degree ∆ ≥ 2. Let H1,H2,...,Hs be the connected components of H. For ﬁxed δ > 0, we have

s

φ(H,p,δ) p∆ log(1/p)

### (θ) + 1{Hi is ∆-regular}η|E(Hi)|/∆ = 1 + δ .

θ + 12η :

lim

= inf

### PH∗

i

p→0

θ,η≥0

i=1

For disconnected graphs the solution of the variational problem might not be attained by the clique or the anti-clique graphons, but by a mixture of these two. Example 9.2. Let H be the disjoint union of a triangle (K3) and a 2-star (K1,2). By Theorem 9.1,

φ(H,p,δ) p2 log(1/p)

θ + 21η : (1 + 3θ + η3/2)(1 + θ) = 1 + δ .

lim

= inf

p→0

θ,η≥0

The pure clique construction corresponds to setting θ = 0, so that η = δ2/3 and θ + 12η = 12δ2/3. The pure anti-clique construction corresponds to setting η = 0, so that θ + 12η = θ ∼ √13δ1/2 for large δ. For large δ, the optimal solution is asymptotically given by a mixture with θ ∼ 3−3/5δ2/5 and η ∼ 32/5δ2/5, giving θ + 12η ∼ 2·353/5δ2/5.

Acknowledgment

This work was initiated when the ﬁrst author was an intern at the Theory Group of Microsoft Research, Redmond. E.L. was supported in part by NSF grant DMS-1513403 and Y.Z. was supported by a Microsoft Research Ph.D. Fellowship. We thank the anonymous referee for helpful comments that greatly improved the exposition of the paper.

References

- [1] B. Bollobás, Random graphs, second ed., Cambridge Studies in Advanced Mathematics, vol. 73, Cambridge University Press, Cambridge, 2001.
- [2] C. Borgs, J. T. Chayes, L. Lovász, V. T. Sós, and K. Vesztergombi, Convergent sequences of dense graphs. I. Subgraph frequencies, metric properties and testing, Adv. Math. 219 (2008), 1801–1851.
- [3] C. Borgs, J. T. Chayes, L. Lovász, V. T. Sós, and K. Vesztergombi, Convergent sequences of dense graphs II. Multiway cuts and statistical physics, Ann. of Math. (2) 176 (2012), 151–219.
- [4] H. J. Brascamp and E. H. Lieb, Best constants in Young’s inequality, its converse, and its generalization to more than three functions, Advances in Math. 20 (1976), 151–173.
- [5] J. I. Brown, C. A. Hickman, and R. J. Nowakowski, The independence fractal of a graph, J. Combin. Theory Ser. B 87 (2003), 209–230.
- [6] J. I. Brown and R. J. Nowakowski, Average independence polynomials, J. Combin. Theory Ser. B 93 (2005), 313–318.
- [7] S. Chatterjee, The missing log in large deviations for triangle counts, Random Structures Algorithms 40 (2012), 437–451.
- [8] S. Chatterjee, An introduction to large deviations for random graphs, Bull. Amer. Math. Soc. (N.S.) 53 (2016), 617–642.
- [9] S. Chatterjee and A. Dembo, Nonlinear large deviations, Adv. Math. 299 (2016), 396–450.
- [10] S. Chatterjee and P. S. Dey, Applications of Stein’s method for concentration inequalities, Ann. Probab. 38 (2010), 2443–2485.
- [11] S. Chatterjee and S. R. S. Varadhan, The large deviation principle for the Erdős-Rényi random graph, European J. Combin. 32 (2011), 1000–1017.
- [12] M. Chudnovsky and P. Seymour, The roots of the independence polynomial of a clawfree graph, J. Combin. Theory Ser. B 97 (2007), 350–357.
- [13] B. Demarco and J. Kahn, Tight upper tail bounds for cliques, Random Structures Algorithms 41 (2012), 469–487.
- [14] B. DeMarco and J. Kahn, Upper tails for triangles, Random Structures Algorithms 40 (2012), 452–459.
- [15] R. Eldan, Gaussian-width gradient complexity, reverse log-Sobolev inequalities and nonlinear large deviations, arXiv:1612.04346.
- [16] H. Finner, A generalization of Hölder’s inequality and some probability inequalities, Ann. Probab. 20 (1992), 1893–1901.
- [17] S. Janson, T. Łuczak, and A. Rucinski, Random graphs, Wiley-Interscience Series in Discrete Mathematics and Optimization, Wiley-Interscience, New York, 2000.
- [18] S. Janson, K. Oleszkiewicz, and A. Ruciński, Upper tails for subgraph counts in random graphs, Israel J. Math. 142 (2004), 61–92.
- [19] S. Janson and A. Ruciński, The infamous upper tail, Random Structures Algorithms 20 (2002), 317–342.
- [20] S. Janson and A. Ruciński, The deletion method for upper tail estimates, Combinatorica 24 (2004), 615–640.


- [21] J. H. Kim and V. H. Vu, Divide and conquer martingales and the number of triangles in a random graph, Random Structures Algorithms 24 (2004), 166–174.
- [22] L. Lovász and M. D. Plummer, Matching theory, North-Holland Mathematics Studies, vol. 121, North-Holland Publishing Co., Amsterdam, 1986, Annals of Discrete Mathematics, 29.
- [23] L. Lovász, Large networks and graph limits, American Mathematical Society Colloquium Publications, vol. 60, American Mathematical Society, Providence, RI, 2012.
- [24] L. Lovász and B. Szegedy, Limits of dense graph sequences, J. Combin. Theory Ser. B 96 (2006), 933–957.
- [25] E. Lubetzky and Y. Zhao, On replica symmetry of large deviations in random graphs, Random Structures Algorithms 47 (2015), 109–146.
- [26] E. Lubetzky and Y. Zhao, On the variational problem for upper tails in sparse random graphs, Random Structures Algorithms 50 (2017), 420–436.
- [27] V. H. Vu, A large deviation result on the number of small subgraphs of a random graph, Combin. Probab. Comput. 10 (2001), 79–94.


B. B. Bhattacharya

Department of Statistics, University of Pennsylvania, Philadelphia, PA 19104, USA. E-mail address: bhaswar@wharton.upenn.edu S. Ganguly

Department of Statistics, UC Berkeley, Berkeley, California, CA 94720, USA. E-mail address: sganguly@berkeley.edu E. Lubetzky

Courant Institute, New York University, 251 Mercer Street, New York, NY 10012, USA. E-mail address: eyal@courant.nyu.edu Y. Zhao

Department of Mathematics, MIT, Cambridge, MA 02139, USA. E-mail address: yufeiz@mit.edu

