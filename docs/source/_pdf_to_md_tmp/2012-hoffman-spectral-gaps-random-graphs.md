arXiv:1201.0425v6[math.CO]14Jul2019

SPECTRAL GAPS OF RANDOM GRAPHS AND APPLICATIONS

CHRISTOPHER HOFFMAN, MATTHEW KAHLE, AND ELLIOT PAQUETTE

Abstract. We study the spectral gap of the Erdős–Rényi random graph through the connectivity threshold. In particular, we show that for any ﬁxed δ > 0 if

(1/2 + δ) log n n

,

p ≥

![image 1](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile1.png>)

then the normalized graph Laplacian of an Erdős–Rényi graph has all of its nonzero eigenvalues tightly concentrated around 1. This is a strong expander property.

We estimate both the decay rate of the spectral gap to 1 and the failure probability, up to a constant factor. We also show that the 1/2 in the above is optimal, and that if p = clogn n for c < 1/2, then there are eigenvalues of the Laplacian restricted to the giant component that are separated from 1.

![image 2](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile2.png>)

We then describe several applications of our spectral gap results to stochastic topology and geometric group theory. These all depend on Garland’s method [24], a kind of spectral geometry for simplicial complexes. The following can all be considered to be higher-dimensional expander properties.

First, we exhibit a sharp threshold for the fundamental group of the Bernoulli

random 2-complex to have Kazhdan’s property (T). We also obtain slightly more information and can describe the large-scale structure of the group just before the (T) threshold. In this regime, the random fundamental group is with high probability the free product of a (T) group with a free group, where the free group has one generator for every isolated edge. The (T) group plays a role analogous to that of a “giant component” in percolation theory.

Next, we give a new, short, self-contained proof of the Linial–Meshulam– Wallach theorem [35, 39], identifying the cohomology-vanishing threshold of Bernoulli random d-complexes. Since we use spectral techniques, it only holds for Q or R coeﬃcients rather than ﬁnite ﬁeld coeﬃcients, as in [35] and [39]. But it is sharp from a probabilistic point of view, providing for example, hitting time type results and limiting Poisson distributions inside the critical window. It is also a new method of proof, circumventing the combinatorial complications of cocycle counting. Similarly, results in an earlier preprint version of this article were already applied in [33] to obtain sharp cohomology-vanishing thresholds in every dimension for the random ﬂag complex model.

1. Introduction

Studying the spectral properties of random matrices has played a central role in probability theory ever since Wigner’s paper establishing the semi-circular law for symmetric matrices with independent entries of equal variance [44]. The theory of

![image 3](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile3.png>)

Date: July 16, 2019.

The ﬁrst author was supported by an AMS Centennial Fellowship and NSF grant DMS0806024. The second author was supported by NSA grant # H98230-10-1-0227, DARPA grant #N66001-12-1-4226, NSF grant #DMS-1352386, and an Alfred P. Sloan research fellowship. The third author was supported by NSF grants DMS-0847661 and DMS-0806024 and NSF postdoctoral fellowship DMS-1304057.

1

these matrices is rich and well-developed, and its techniques and theorems provide great insight into the adjacency matrices of random graphs.

In this paper we study the normalized Laplacian matrix of a Bernoulli (also Erdős–Rényi ) random graph G(n,p), which has n vertices and whose every edge is included independently with probability p = p(n). For a connected graph G, the normalized Laplacian has smallest eigenvalue λ1 = 0, and the remainder of its eigenvalues {λi}ni=2 lie in the interval 0 < λi ≤ 2. The spectral gap, λ2, is the principal quantity of interest in many applications, and it has received much attention in the literature [10, 8, 9, 12].

Our focus is on typical behavior of random graphs for large values of n. So, we will use the terminology with high probability (abbreviated w.h.p.) as a qualiﬁer for a statement holds with probability tending to 1 as n tends to inﬁnity. We will also use the expression with overwhelming probability, meaning the statement holds with failure probability smaller than O(n−C) for all C > 0.

We will make use of the Landau notations O,o,ω,Ω,Θ in the asymptotic sense, so that f = O(g) means f/g is eventually bounded above as n → ∞ and f = o(g) means f/g tends to 0 as n → ∞. Also, f = ω(g) means g = o(f) and f = Ω(g) means g = O(f). Finally, we will use f = Θ(g) to mean f = O(g) and f = Ω(g).

We will also make use of the notion of thresholds. A function f = f(n) is said to be a threshold for a property P if p = ω(f) implies G ∈ P w.h.p. and p = o(f) implies G  ∈ P w.h.p. Such a threshold is only deﬁned up to n–independent scalar multiples. If there is a function g = o(f) so that p ≥ f + g implies G ∈ P w.h.p. and p ≤ f − g implies G  ∈ P w.h.p. the threshold is sharp. If no such g exists, the threshold is coarse.

A fundamental result of random graph theory is that every nontrivial monotone property has a threshold [21], which need not be sharp. For example, the appearance of triangles in G(n,p) has the threshold 1/n, which is coarse. On the other hand, the Erdős–Rényi theorem shows that log n/n is the sharp threshold for connectivity of the graph. Similarily, we will need that 21 log n/n is the sharp threshold for the graph to consist only of one giant component G˜ and isolated vertices, which is an easy extension of the Erdős–Rényi theorem. We will use G˜ to denote the largest connected component of G(n,p), which is well–deﬁned w.h.p. for p = ω(1/n) (see [31] for a detailed discussion or Lemma 5.8).

![image 4](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile4.png>)

For the Erdős–Rényi graph, as we shall show, the eigenvalues {λi}ni=2 tend to cluster around 1, and hence we deﬁne λ(G) = maxi =1 |1−λi|. The quantity 1−λ(G) is sometimes referred to as the absolute gap. The methods in the previous papers are successful in establishing the correct order for λ(G) of C(np)−1/2 when the density of edges is suﬃciently large, but they do not extend to p very near the connectivity threshold log n/n.

Our main result on spectral gaps are contained in the following two theorems.

- Theorem 1.1. Fix δ > 0 and let p ≥ (12 + δ)log n/n. Let d = p(n − 1) denote the expected degree of a vertex. For every ﬁxed ǫ > 0, there is a constant C = C(δ,ǫ), so that


![image 5](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile5.png>)

C √

λ(G˜) <

.

![image 6](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile6.png>)

![image 7](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile7.png>)

d

with probability at least 1 − Cn exp(−(2 − ǫ)d) − C exp(−d1/4 log n).

This result improves on a number of previous results. These earlier results are discussed in more detail in Section 2. In brief, the state of the art is due to Coja– Oghlan [12] who obtains gap 1 − O(d−1/2) for p ≥ C log n/n, where C > 0 is a suﬃciently large constant. We are able to extend this to C = 1, and appropriately modifying the statement for the giant component, we extend this to C = 12.

![image 8](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile8.png>)

We note that Theorem 1.1 is vacuous for p ≤ 21 log n/n. Indeed, the next result shows that for smaller values of p, the gap is no longer 1 − o(1).

![image 9](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile9.png>)

- Theorem 1.2. For p satisfying p = ω(√log n/n) and p ≤ 21 log n/n λ(G˜) ≥ 12,

![image 10](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile10.png>)

![image 11](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile11.png>)

![image 12](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile12.png>)

with high probability.

For p = O(√log n/n), Fountoulakis and Reed [19] show that the mixing time is large, and hence provide a lower bound for λ(G˜) in this regime. So G(n,p) has λ(G˜) bounded away from 0, but at 21 log n/n there is a phase transition, and at this point λ(G˜) = o(1). We in fact prove a slightly stronger result than Theorem 1.2 in Section 5 (c.f. Lemma 4.2).

![image 13](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile13.png>)

![image 14](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile14.png>)

We also consider an Erdős–Rényi process version (see Section 6 for deﬁnitions) of the spectral gap theorem. In particular, we show that if random edges are added one at a time, at the moment of connectivity the random graph already has spectral gap 1 − o(1). More precisely, we have the following.

- Theorem 1.3. Let τc be the connection time for the Erdős–Rényi graph process G(n,m). Then there is a constant C so that with high probability


![image 15](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile15.png>)

λ(G(n,τc)) ≤ C/ log n.

This theorem follows immediately from Theorem 6.1 in the 2–dimensional case: that theorem shows that the largest component of the Erdős–Rényi graph process has gap λ(G˜) ≤ C/√log n for all time after (14 + δ)n log n edges have been added, w.h.p. Hence, at the connection time τc, which occurs when about (12)n log n edges have been added, λ(G) = λ(G˜) ≤ C/√log n.

![image 16](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile16.png>)

![image 17](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile17.png>)

![image 18](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile18.png>)

![image 19](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile19.png>)

Applications to stochastic topology

As we will see, Theorem 1.1 is useful in the study of random topological spaces and random groups. We now provide several examples where this theorem yields sharp results. All of these new results depend on the combination of the spectral gap theorem with “Garland’s method” and its reﬁnements by Ballman and Świątkowski [3], and by Żuk [46, 45].

• Kazhdan’s property (T). Linial and Meshulam [35] introduce an analogous measure Y2(n,p) to the binomial random graph for random 2-dimensional simplicial complexes. This is the probability distribution on all simplicial complexes with vertex set [n] = {1,2,...,n}, with complete 1-skeleton (i.e. with all possible n2

edges), and such that each of the n3 possible 2-dimensional faces are included independently with probability p. We use the notation Y ∼ Y2(n,p) to indicate a complex drawn from this distribution. We will call an edge isolated if no triangle contains it.

We prove here a structure theorem for the random fundamental group, for a certain range of p.

- Theorem 1.4. Suppose δ > 0 is ﬁxed,


(1 + δ)log n n

p ≥

,

![image 20](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile20.png>)

and Y ∼ Y2(n,p). Then w.h.p. π1(Y ) is isomorphic to the free product of a (T) group G, and a free group F, where the free group F has one generator for every isolated edge in Y .

As a corollary, we also show that the threshold for π1(Y ) to have property (T) agrees precisely with the homology-vanishing threshold found by Linial and Meshulam [35]. For the proof, along with further details and explanation, see Section 3.2.

It might be that π1(Y ) is a free product of a (T) group and a free group for smaller p. The most interesting conjecture about the structure of π1(Y ) might be the birth of a giant (T) free factor at p = c/n for some constant c ≈ 2.7538. This is the same point as the homological phase transition studied by Linial and Peled [36].

• Random d-dimensional simplicial complexes. Meshulam and Wallach further generalize the 2-dimensional model to random d-dimensional complexes Yd(n,p) [39]. Their main result is that p = dlog n/n is a sharp threshold for vanishing of cohomology Hd−1(Y,k) where k is a ﬁnite ﬁeld or a ﬁeld of characteristic 0. The proof requires delicate cocycle counting arguments.

The new spectral gap results give a new proof of the Meshulam–Wallach theorem, in the case that k is a ﬁeld of characteristic 0. The Meshulam–Wallach theorem is stronger topologically, since homology vanishing over a ﬁnite ﬁeld implies vanishing over Q. But our new proof is very short (given the spectral gap theorem), and the result is slightly sharper probabilistically. For example, we obtain hitting time results in an accompanying stochastic growth process (see for Corollaries 3.3 and 3.9 for representative examples of “hitting time results”), and also we recover a simple proof of the Poisson distribution of Betti numbers in the critical window (Corollary 3.4).

Gundert and Wagner show that the Laplacian on (d − 1)-forms in a random d-complex has a large spectral gap for p ≥ Cd log n/n for some suﬃciently large Cd [28]. Combining their argument with the results in this paper would yield a hitting time result, and in particular this shows that the gap for these higher Laplacians is already large for p ≥ dlog n/n.

Parzanchevski, Rosenthal, Tessler [14] combine Gundert and Wagner’s argument with earlier work of Pach [40] to show that for p ≥ Cd log n/n, w.h.p. Y has the “geometric overlap” property.1 It also seems possible to use the new spectral gap results to sharpen this result, and show that in the process version of the random complex, random d-complexes already have the geometric overlap property as soon as they are pure d-dimensional.

As far as we can tell, these suggested sharpenings of the main theorems in [28] and [14] are not written down anywhere, and we do not further elaborate on them

![image 21](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile21.png>)

1A sequence of d-dimensional simplicial complexes Sn with Fn d-dimensional faces has the geometric overlap property if there exists a constant λ > 0 so that for every geometric map: Sn → Rd (i.e. aﬃne linear on each face), there exists a point p ∈ Rd that lies in the image of at least λFn d-faces. See for example recent work by Gromov and collaborators in [26], [27], and [20].

in this note. It seems that these sharper results only depend on substituting our Theorem 1.1 for earlier results on spectral gap G(n,p).

- • Triangular random groups. Antoniuk et. al. study the phase transitions that occur in the triangular model of random groups [1]. Similarly, by using our spectral gap results, their results can be strengthened, for example to show a hitting time result.
- • Random ﬂag complexes. Let X(n,p) denote the random clique complex, i.e. the maximal simplicial complex, with respect to inclusion of faces, whose 1–skeleton is given by an Erdős–Rényi graph G(n,p).


Combining the spectral gap theorem from an earlier version of this paper with Garland’s method, similar cohomology vanishing results were recently obtained for X(n,p) by the second author in [33]. Combining with several earlier results [32],

- as a corollary this shows that for every d ≥ 3, there is a wide range of p for which X(n,p) is rationally homotopy equivalent to a bouquet of d-dimensional spheres.2


• Random right-angled Coxeter groups. Group cohomology of random rightangled Coxeter groups were studied in [15]. Applying the same techniques as in the random ﬂag complex paper [33], it is shown that for a certain measure and range of parameter, random right-angled Coxeter groups are rational duality groups with high probability. This is actually a special case of a more general statement that shows that the same holds for random graph products of ﬁnite groups.

Organization

Section 2 contains the background about the spectrum of the normalized Laplacian of Erdős–Rényi random graphs. Section 3 does the same for our applications of our spectral results to random topology. In Section 4 we show how to transfer adjacency matrix estimates to the normalized Laplacian under some assumptions on the structure of the graph. In Section 5 we show that an Erdős–Rényi graph satisﬁes these structural conditions with high probability. In Section 6 we show that the Linial-Meshulam process has large gap in a local spectral sense. In Section 7 we show how to apply the Ballman–Świątkowski criterion to prove the structure theorem for rational cohomology, and in Section 8 we show how to apply Żuk’s criterion to prove the structure theorem for the fundamental group. In Section 9 we apply the Kahn-Szemerérdi machinery to show that the adjacency matrix of the Erdős–Rényi graph has a gap of the correct order for any p with p = Ω(log n/n). Finally, we include one appendix which proves the precise versions of the tail bounds for binomial variables that we use.

2. Background: spectra of random graphs

There are multiple common notions of spectra of a graph. The most elementary deﬁnition is given by the eigenvalues of the adjacency matrix A. The subjects of our main theorems are the eigenvalues of the normalized Laplacian L (see (1) for a precise deﬁnition). When the graph is regular, these two notions of spectra are just shifted rescalings of one another.

![image 22](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile22.png>)

2A simplicial complex is rationally homotopy equivalent to a bouquet of d spheres if it is simply connected and all of its nontrivial reduced, rational, homology is in degree d.

Appropriately, when the graph is nearly regular, as is the case for G(n,p) with p = ω(log n/n), these two spectra behave in nearly the same way. Coarse statements about the spectral gap of G(n,p) in this regime can largely be considered a statement about either spectra, and indeed, the primary method for estimating the gap of L in the setting of Erdős–Rényi graphs is by comparison with A.

We will now give a precise deﬁnition of the normalized Laplacian. A good general introduction to the properties of the normalized Laplacian is available in [10]. Let π+ be the projection map onto the vertices with positive degree, let T be the diagonal matrix of degrees, and let A be the adjacency matrix. The normalized Laplacian is deﬁned as

- (1) L = π+ − T−1/2AT−1/2,


where T−1/2 is taken to be 0 in coordinates where the degree is 0. Note that some authors use an alternate deﬁnition of normalized Laplacian, with π+ replaced by Id. We let 0 = λ1 ≤ λ2 ≤ ... ≤ λn ≤ 2 be the eigenvalues of L.

The principal nontrivial property we will employ about L is that the dimension of the kernel is equal to the number of components of G. An immediate consequence is that for a graph with multiple nontrivial components, λ2 = 0. In particular, when np − log n → −∞ the normalized Laplacian has no spectral gap with high probability. That said, it still makes sense to consider the spectral gap of L restricted to the giant component.

Techniques for estimating eigenvalues. As A has i.i.d. entries above the diagonal, many oﬀ-the-shelf techniques can be applied to it directly. In particular, the original trace method bound of Füredi and Komlós [23] can be extended to show that when p = ω(log6 n/n), the second largest eigenvalue of the adjacency matrix of an Erdős– Rényi graph is of smaller order than the largest eigenvalue. Improvements and corrections to this argument brought the bound to p = ω(log4 n/n), [43] and later to as low as p ≫ log2 n/n [8]. Newer methods have been pursued in [34], [6], [5].

The alternative method of Kahn and Szemerédi [22], ﬁrst developed for bounding the spectral gap of d-regular graphs, has been adapted quite successfully for estimating the spectral gap in the p = Θ(log n/n) regime by Feige and Ofek [18]. In particular, they show that there are constants c > 0 and K > 0 so that for p > c log n/n, all but the ﬁrst eigenvalue are at most K√np.

![image 23](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile23.png>)

One contribution of this paper is a sharpening of this estimate (see Proposition 5.2). Indeed, we show that for any c > 0, there is a K > 0 so that for p > c log n/n, all but the ﬁrst eigenvalue are at most K√np. Conversely, it is easily checked that for p = o(log n/n), there are many eigenvalues greater in magnitude than √np, coming from the existence of high-degree stars in the graph. Thus, in a sense, we sharpen the Kahn-Szemerédi analysis of the full adjacency matrix of G(n,p) to its natural endpoint.

![image 24](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile24.png>)

![image 25](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile25.png>)

However, our main contribution in this paper is a technique for exactly characterizing when and why the extremal eigenvalues of the normalized Laplacian stop tracking the extremal eigenvalues of the adjacency matrix. Throughout the p = Θ(log n/n), the extremal eigenvalues of the adjacency matrix do not undergo a phase transition (see Proposition 5.2).

In contrast, for the Laplacian, there is a transition at p = log n/n, before which point the graph has isolated vertices. Each isolated vertex contributes a 0-eigenvalue to the spectra of the Laplacian, but as a consequence of Theorem 1.1, the remaining

eigenvalues will be 1 + O(1/√np) as anticipated. There is a second transition at p = 21 log n/n below which there are quadruplets of vertices in the giant component on which the induced graph is a path. These quadruplets each contribute an eigenvalue near to 12, but the remainder of the spectra will again be 1+O(1/√np). Continuing in this way, we conjecture that there are a whole family of transitions at

![image 26](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile26.png>)

![image 27](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile27.png>)

![image 28](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile28.png>)

![image 29](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile29.png>)

- 1 k log n/n for any natural number k, where the spectral gap of the giant component is asymptotically the spectral gap of a path on k vertices.

![image 30](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile30.png>)

- 2.1. Comparing spectra and the gap theorem proof approach. While it is relatively straightforward to transfer estimates on the gap of A to the gap of L in the p = ω(log n/n) regime, Coja-Oghlan [12] sharpens this analysis to show that there are c > 0 and K > 0 so that for p ≥ c log n/n, all but the smallest eigenvalue of L are at most K/√np in modulus with high probability.


![image 31](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile31.png>)

There are some similarities between our approach and the method of CojaOghlan [12]. His analysis rests on applying the Kahn-Szemerédi machinery to the adjacency matrix of a suﬃciently regular subgraph of G(n,p) and then arguing this core of the graph determines the eigenvalues of the Laplacian of the whole graph. We make a ﬁner analysis of the structure of G(n,p) in the p = Θ(log n/n) regime in order to show that in fact the spectra of the adjacency matrix and the spectra of the normalized Laplacian only fail to be comparable when small sparse subgraphs appear.

To bound maxi>1 |1 − λi| it suﬃces instead to bound the spectrum of what is essentially I −L. Given the graph G with vertices {1,2,...,n} we deﬁne the matrix

√ 1 deg(u)

√

if u is adjacent to v, 0 otherwise.

![image 32](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile32.png>)

![image 33](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile33.png>)

![image 34](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile34.png>)

deg(v)

Mu,v =

Thus if all degrees are positive we have M = T−1/2AT−1/2,

and it is easily checked that for any vertex set W of a connected component of V , T1/21W is an eigenvector with eigenvalue one.

Set S = {x | xt1 = 0}. The standard Kahn-Szemerérdi machinery applied to the adjacency matrix shows that

√

![image 35](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile35.png>)

|xtAy| ≤ C

d x y , where d = np, for all x ∈ S and all y ∈ Rn, provided p = Ω(log n/n).

When p > (1+ǫ)logn/n, the comparison is relatively straightforward, by virtue of the fact that with high probability all the degrees in the graph are larger than d/M√ for some suﬃciently large M. In particular, this means that T−1/2 ≤

√

![image 36](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile36.png>)

![image 37](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile37.png>)

d. One must additionally show that T−1/21 is nearly parallel to 1, i.e. T−1/2 nearly maps the space S to itself. In sum, these two facts show that for x ∈ S, T−1/2x is still nearly in S and has norm T−1/2x ≤

M/

√

√

![image 38](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile38.png>)

![image 39](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile39.png>)

d. Thus, |xtMx| = |(T−1/2x)A(T−1/2x)| ≈ C

M x /

√

√

![image 40](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile40.png>)

![image 41](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile41.png>)

d T−1/2x 2 ≤ CM x 2/

d, giving the desired result.

1/2+δ log log n n , the minimal degree of the graph is

Likewise, when p > logn+(logn)

![image 42](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile42.png>)

still at least d1/2+δ w.h.p. In this case, the T−1/2 still nearly maps S to S, but now

T−1/2x ≤ d−1/4−δ/2. This allows one to show that max

|1 − λi| < d−δ, which is essentially the approach taken by an earlier version of this paper.

i>1

To get theorems that hold all the way down to below p = log n/n, where the minimum degree drops to 0 an additional argument is needed. This is because it is no longer the case that T−1/2 = O(1/

√

![image 43](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile43.png>)

d). The key structure theorem that allows the comparison to go through is an analysis of the graph structure surrounding lowdegree vertices. Precisely, we show that near the connectivity threshold, there are no edges between low-degree vertices, and low-degree vertices do not even have shared neighbors (see Proposition 5.3). Thus, they are only connected through the large, high-degree core. This is enough to ensure that the desired spectral properties persist all the way down to around p ∼ 1/2 logn/n.

On the other hand, below p ∼ 1/2 logn/n, low-degree vertices in the giant component begin to connect with high probability. Indeed, it is possible to show that there are even two degree 2 vertices that connect to each other and the high-degree core. This is enough to ensure that λ2 of the giant component is at most a little above 12 and λn is at least 23.

![image 44](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile44.png>)

![image 45](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile45.png>)

- 2.2. Further Discussion. For p satisfying np − log n → ∞, we have provided a bound on λ(G) that is sharp up to a constant multiplicative factor. For the adjacency matrix in many regimes, much more is known about the behavior of the second largest eigenvalue.


Recall that a Wigner matrix is a symmetric matrix with independent, centered, variance 1 entries above the diagonal. From Wigner’s celebrated semicircle law, it can be inferred that the largest eigenvalue of such a matrix is around 2√n. In fact a much stronger result is known for a large class of Wigner matrices, for which it is seen that

![image 46](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile46.png>)

n1/6(λ1 − 2√n) ⇒ X where X follows the GOE Tracy-Widom law. When the entry distributions are Bernoulli(p) – i.e. when this is the adjacency matrix of an Erdős–Rényi graph – it was recently shown by Knowles, L. Erdős, Yau and Yin [17] that for p ≫ n−1/3, the analogous results hold for the second largest eigenvalue. One of the limits of comparing the spectra of the adjacency matrix and the Laplacian matrix is that such a ﬁne statement about the spectra does not easily transfer. It is appealing to speculate that at p ∼ log n/n, the smallest nonzero eigenvalue of the normalized Laplacian is exactly 1−(2−o(1))√np, consistent with what would be predicted by the semicircle law of the adjacency matrix.

![image 47](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile47.png>)

![image 48](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile48.png>)

The spectral gap of the normalized Laplacian is strongly related to other probabilistic quantities of the graph, in particular to properties of simple random walk (see [10] for more details) and to the Cheeger constant. Direct analysis of these quantities is also possible, which then implicitly give bounds on the spectral gap. Benjamani et. al. take a combinatorial approach and study the Cheeger constant (also called isoperimetric constant, or conductance) throughout the evolution of the random graph process [7]. Likewise Fountoulakis and Reed study the mixing time of simple random walk on the giant component through the conductance [19] in

√log n

![image 49](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile49.png>)

the strictly supercritical regime 1+nǫ < p <

n . Ding et. al. studied probabilistic aspects of the graph including the mixing time of simple random walk on the giant

![image 50](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile50.png>)

![image 51](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile51.png>)

component as the graph emerges from the critical window [16]. All these works show that the giant component can be partitioned into a well connected expanding core together with small (logarithmic size) graphs attached to the core. We also employ a version of this decomposition to analyze the spectral properties of the graph.

3. Random topology

In [35], Linial and Meshulam introduce an analogous measure Y2(n,p) to the binomial random graph for random 2-dimensional simplicial complexes. This is a probability distribution over all simplicial complexes with vertex set [n] = {1,2,...,n}

with complete 1-skeleton (i.e. with all possible n2 edges). Each of the n3 possible 2-dimensional faces are included independently with probability p. We use the no-

tation Y ∼ Y2(n,p) to indicate a complex drawn from this distribution. Meshulam and Wallach [39] extend this deﬁnition to a d-dimensional complex Yd(n,p), formed by taking the complete (d − 1)-skeleton of the n-vertex simplex, and including ddimensional faces independently with probability p.

The distributions can be made into stochastic growth processes in a natural way. Let Y2(n,m) be the random 2-complex that has the uniform distribution over all simplicial complexes with n vertices, n2 edges, and exactly m two-dimensional faces. In the random complex process {Y2(n,m)}, faces are added one at a time, uniformly randomly from all faces which have not already been chosen. In the same way, we can deﬁne the process {Yd(n,m)} by including d-faces one at a time.

We also deﬁne a time-changed version of this process Ytd(n), more suitable to working with the binomial complex. Instead of including the faces one at a time, create independent Exp(1) clocks for every d-face. When one of the clocks rings, include the corresponding face. If we let p(t) = 1 − e−t, then Ytd(n) has the distribution Yd(n,p(t)).

- 3.1. Cohomology vanishing. The foundational work on the Linial-Meshulam complexes is a cohomological analogue of the Erdős–Rényi connectivity theorem.


Linial–Meshulam–Wallach theorem. Let k be any ﬁnite ﬁeld, d ≥ 2 ﬁxed, f(n) → ∞ be any slowly growing function, and Y ∼ Yd(n,p). If

dlog n + f(n) n

p ≥

, then w.h.p. Hd−1(Y,k) = 0, and if

![image 52](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile52.png>)

dlog n − f(n) n

p ≤

, then w.h.p. Hd−1(Y,k) = 0.

![image 53](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile53.png>)

For the case that d = 2 and k = Z2, this is due to Linial and Meshulam [35], while for the version stated, this is due to Meshulam and Wallach [39]. By the universal coeﬃcient theorem, these results imply the corresponding theorem for the cohomology with Q coeﬃcients. For Z coeﬃcients, it is shown by the authors in [30] that for p ≥ 80dlogn/n, Hd−1(Y,Z) = 0 by other techniques. For d = 2, work of [37] establishes 2 logn/n as the sharp threshold for vanishing Z homology.

The threshold p ∼ dlog n/n is also the threshold for the existence of isolated (d − 1)-faces in the complex, i.e. faces that are not included in any d-face. Indeed, the presence of isolated faces is precisely the reason that the cohomology is nonzero

below this threshold. In fact, a ﬁner statement can be made about the number of isolated (d − 1)-faces.

- Lemma 3.1. Let I denote the number of isolated (d−1) faces in Yd(n,p). Suppose that for ﬁxed c,


dlog n + c + o(1) n

. Then I converges in law to Poisson(e−c/d!).

p =

![image 54](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile54.png>)

The proof of this lemma is standard and can be proved in the same manner as the Poisson convergence of the number of isolated vertices in G(n,p). See Proposition

- 4.13 of [42]. Using spectral techniques, we give a new proof of the Linial–Meshulam–Wallach


theorem, although only with Q or R coeﬃcients. However, for Q coeﬃcients, we also sharpen the theorem by proving a process version. More strikingly, this theorem shows that long before the last isolated (d−1)-faces disappear, the only obstruction to vanishing cohomology are those isolated (d − 1)-faces. Its proof follows almost immediately from spectral arguments and Garland’s method (see Section 7).

Theorem 3.2. Consider the random complex process {Ytd(n)}. Let It denote the number of isolated (d − 1)-faces in the complex at time t. Fix any δ > 0 and deﬁne

t0 so p(t0) = (d − 1 + δ)log n/n. Then w.h.p. for all time t ≥ t0, Hd−1(Ytd(n),Q) ∼= QI

. As w.h.p. It

t

> 0 we immediately get the following hitting time corollary.

0

- Corollary 3.3. Consider the random complex process {Yd(n,m)}. Let M1 = min{m | Yd(n,m) has no isolated (d − 1) − dimensional faces},

and let

M2 = min{m | Hd−1(Yd(n,m),Q) = 0}. Then w.h.p. M1 = M2.

Further, it is standard to show at this point that the Betti numbers are asymptotically Poisson.

- Corollary 3.4. Suppose that for ﬁxed c,


dlog n + c + o(1) n

p =

. Then bd−1(Yd(n,p)) converges in law to Poisson(e−c/d!). Note that this follows immediately from Lemma 3.1 and Theorem 3.2.

![image 55](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile55.png>)

- 3.2. The fundamental group. For the 2-dimensional complex, a fair bit is known


about the fundamental group π1(Y ). Babson and the ﬁrst two authors ﬁnd the threshold for the fundamental group to be trivial [2].

- Theorem 3.5 (Babson–Hoﬀman–Kahle). If p = n−α where α < 1/2 then w.h.p.


π1(Y ) is a nontrivial word hyperbolic group. If p ≥ n−1/2 log(n) then π1(Y ) is trivial.

Cohen et al. [11] show that if p = o(1/n), then w.h.p. π1(Y ) is free. Finally, Costa and Farber describe the cohomological dimension cdπ1(Y ) in various regimes [13, 41].

- Theorem 3.6 (Costa–Farber). Let Y ∼ Y2(n,p), and set p = n−α.


- (1) If α > 1 then w.h.p. cdπ1(Y ) = 1,
- (2) if 1 > α > 3/5 then w.h.p. cdπ1(Y ) = 2, and
- (3) if 3/5 > α > 1/2 then w.h.p. cdπ1(Y ) = ∞.


For the 2-dimensional complex, we combine the new spectral results with Garland’s method to show a threshold theorem for π1(Y ) to have property (T). A group

- G is said to have property (T) if every unitary action of G on a Hilbert space that has almost invariant vectors also has a nonzero invariant vector. The ﬁrst explicit examples of expanders, due to Margulis, were constructed using Cayley graphs on quotients of (T) groups such as SL(3,Z) [38]. Conversely, expansion properties of some graphs associated to the generating set of a group can imply property (T) (see [46]).


Property (T) has found use in many diﬀerent areas of mathematics. For example, groups with property (T) lead to good mixing properties in ergodic theory — a process which mixes slowly must leave some subsets almost invariant. In particular, if a group Γ has property (T), then every ergodic Γ system is also strongly ergodic [25]. See the monograph [4] for a comprehensive overview of property (T).

We recall for convenience the statement of Theorem 1.4: Theorem. Suppose δ > 0 is ﬁxed,

(1 + δ)log n n

p ≥

,

![image 56](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile56.png>)

and Y ∼ Y2(n,p). Then w.h.p. π1(Y ) is isomorphic to the free product of a (T) group G, and a free group F, where the free group F has one generator for every isolated edge in Y .

Theorem 1.4 might be viewed as a group-theoretic analogue of the fact that for p ≥ (1/2 + δ)log n/n, the random graph G ∼ G(n,p) is w.h.p. a giant component, which is an expander, and isolated vertices.

We anticipate that the true threshold for π1(Y ) being the free product of a free group and a nontrivial (T) group is much lower, and that it occurs in the range p = Θ(1/n). The signiﬁcance of the threshold log n/n is that this is the threshold

- at which the free group is generated by isolated edges. For example, if p = δ log n/n with 0 < δ < 1 ﬁxed, then w.h.p. there exists a


triangle abc in Y2(n,p) such that edges ab and ac are not contained in any other triangle. In other words, the edge bc is a connected component in the link of vertex a. In this case, the edge ab and triangle abc can be collapsed by an elementary collapse. This is a homotopy equivalence—after the collapse, the edge ac is a generator of a free Z factor in π(Y ), but before the collapse there is no isolated edge generating this element of the group.

On the other hand, this is also the point our argument in Section 8 ceases to apply. To apply Żuk’s criterion in Section 8, we ﬁrst delete all isolated edges and the resulting complex has connected vertex links with good expansion properties. In the case above, the vertex link a is not connected, even after such deletions.

We have the following corollary of Theorem 1.4, which shows that the threshold for property (T) is the same as the Linial–Meshulam theorem for vanishing of Z/2homology.

Corollary 3.7. Let ω → ∞ as n → ∞, and Y ∼ Y2(n,p). If p ≥

2 logn + ω n then P[π1(Y ) has property (T)] → 1.

![image 57](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile57.png>)

We also describe a process version of this structure theorem that holds below the connectivity threshold.

Theorem 3.8. Consider the random complex process {Ytd(n)}. Let F˜t be a free group with the number of generators equal to the number of isolated edges in the

complex Ytd(n). Fix any δ > 0 and deﬁne t0 so p(t0) = (1+δ)log n/n. Then w.h.p. for all t ≥ t0,

π1(Y2(n,p(t))) ∼= Gt ∗ F˜t where Gt has property (T).

Note that Theorem 1.4 follows immediately from this. As the number of isolated edges at time t0 is positive w.h.p, we get the following hitting time corollary. Corollary 3.9. Consider the random complex process {Y2(n,m)}. Let

M1 = min{m | Y2(n,m) has no isolated edges}, and let

M2 = min{m | π1(Y2(n,m)) is (T)}. Then w.h.p. M1 = M2.

Remark 3.10. We can additionally give an explicit Kazhdan pair for the (T) group. Setting S to be the canonical generating set based at vertex 1, i.e. all loops cycles of the form 1 → x → y → 1 for distinct vertices x and y, then (S,√2(1 − o(1))) is a Kazhdan pair (see Remark 5.5.3 of [4]).

![image 58](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile58.png>)

4. Spectral estimates

In this section we give some conditions on an arbitrary graph G on n vertices which facilitate a large spectral gap. Fix positive constants C1,C2,C3 and M. In this section d can be any function of n with d = d(n) ≥ 1, and this is always satisﬁed by d = (n − 1)p, the convention taken in other sections.

Recall that T is the diagonal matrix of degrees. Let W denote the set of vertices

- x for which deg x > 0 and I be the number of isolated vertices in the graph. For any set of vertices S, let 1S denote the vector that is one in every coordinate corresponding to S and 0 elsewhere. Let 0 = λ1 ≤ λ2 ≤ ··· ≤ λn be the eigenvalues of the normalized Laplacian L[G], so that λ1 = λ2 = ··· = λI+1 = 0. We also deﬁne a set of vertices of small degree. Let


- (2) ℵM = {v ∈ V : deg(v) ≤ d/M}. We now deﬁne four conditions that will ensure a spectral gap.


- (1) Bounded degree condition (b.d.c) Every vertex has degree at most C1d.
- (2) Adjacency matrix


√

![image 59](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile59.png>)

|xtAy| ≤ C2

d.

sup

x =1,xt1=0 y =1

- (3) Fuzz There are no edges between vertices of ℵM, |ℵM| ≤ n2 and

![image 60](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile60.png>)

max

u∈ℵcM

e(u,ℵM) ≤ 1,

where e(U,V ) denotes the number of edges between sets of vertices U and V.

- (4) Parallel eigenspaces


√n d

![image 61](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile61.png>)

|xtT−1/21ℵc

| ≤ C3

sup

.

![image 62](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile62.png>)

M

x =1, xtT1/21W =0

The ﬁnal condition states that a vector x that is orthogonal to the kernel of L will not have such a large component in the direction of the principal eigenvector of T−1/2A. The vector 1ℵc

can be considered as a good approximation to this principal right eigenvector. Otherwise said, the 0–eigenspace of L and the principal right eigenspace of T−1/2A are nearly parallel.

M

With these deﬁnitions we can now state our main result on spectral gaps.

- Lemma 4.1. Let G be a graph on n vertices and let C1,C2,C3 and M be constants. If G satisﬁes the four conditions above then there is a constant C = C(C1,C2,C3,M) so that


C √

|1 − λi| <

max

.

![image 63](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile63.png>)

![image 64](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile64.png>)

d

i>I+1

Proof. Let W be the set of vertices x for which deg x > 0. By the spectral theorem, L admits a basis of orthogonal eigenvectors. Let v be a normalized eigenvector of L corresponding to an eigenvalue λi with i > I + 1. Setting l1,l2,...,lI to be the isolated vertices, a basis for the kernel of L is given by {T1/21,δl

I}, where δa is 1 in the ath coordinate and 0 elsewhere. As v is orthogonal to all of these, it is orthogonal to T1/21W. Hence,

,...,δl

,δl

2

1

|1 − λi| = vtT−1/2AT−1/2v ≤ sup

xtT−1/2AT−1/2x .

x =1, xtT1/21W =0

As this holds for all such i > I + 1, it suﬃces to bound the right hand side.

Orthogonally decompose T−1/2x = u + v, where u is supported on vertices in ℵcM and v is supported on vertices in ℵM. Further decompose u = u0+u1 by letting

- u1 be the projection of u along 1ℵc


. Expanding the quadratic form, we may write

M

- (3) xtT−1/2AT−1/2x ≤ 2|ut0Au| + |ut1Au1| + |vtAv| + 2|vtAu|.

Each of these terms will be seen to have the right order bound, completing the proof.

As u0 ⊥ 1ℵc

M

and is supported only on ℵcM, we have that u0 ⊥ 1. By the deﬁnitions of ℵM and x, we have that

u0 2 ≤ u 2 =

i∈ℵcM

|xi|2 deg i ≤

![image 65](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile65.png>)

M d

![image 66](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile66.png>)

.

Hence by the adjacency matrix condition and the above equation we have that

- (4) |ut0Au| ≤ C2


√

C2M √

![image 67](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile67.png>)

d u0 u ≤

.

![image 68](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile68.png>)

![image 69](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile69.png>)

d

As u1 is the projection of u along 1ℵc

, we have

M

1ℵc

1ℵc

= (xtT−1/21ℵc

u1 = (ut1ℵc

M

M

)

)

.

![image 70](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile70.png>)

![image 71](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile71.png>)

|ℵcM|

|ℵcM|

M

M

Because√ |ℵcM| ≥ n2, the parallel eigenspaces condition implies that we have u1 ≤ 2C3 d . The norm of A is at most the maximum degree of the graph, and by the

![image 72](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile72.png>)

![image 73](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile73.png>)

![image 74](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile74.png>)

bounded degree condition this is at most C1d. Hence, we get that

- (5) |ut1Au1| ≤

2C1C32 d

![image 75](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile75.png>)

For the third term, we note that by the ℵM condition there are no edges between vertices of ℵM, and hence

- (6) vtAv = 0. Finally, we may expand vtAu as

vtAu =

i∈ℵM

xi √deg i j∈ℵ

![image 76](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile76.png>)

![image 77](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile77.png>)

c M,

j∼i

uj.

By Cauchy-Schwarz, this is bounded by

|vtAu|2 ≤

i∈ℵM

1 deg i j∈ℵ

![image 78](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile78.png>)

c M,

j∼i

uj

2

≤

i∈ℵM j∈ℵcM, j∼i

(uj)2 .

Now each j ∈ ℵcM has at most one neighbor in ℵM, and hence we have

- (7) vtAu ≤ u =


√

![image 79](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile79.png>)

M √

. Plugging (4), (5), (6) and (7) into (3) completes the proof. In the remainder of this section we prove a condition on a graph that will imply

![image 80](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile80.png>)

![image 81](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile81.png>)

d

an upper bound on the spectral gap. This lemma shows that our previous argument breaks down when the set ℵM fails to be isolated.

- Lemma 4.2. Suppose that H is a connected graph and that there are vertices u,v,w,x for which the induced graph on u,v,w,x is a path with endpoints u and x. Suppose further that deg v = deg w = 2 and deg u,deg x ≥ m. Let 0 = λ1 ≤ λ2 ≤ ··· ≤ λ|H| be the eigenvalues of the normalized Laplacian L[H], then


λ|H| ≥ 32 and

![image 82](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile82.png>)

λ2 ≤ 21 + O(1/√m) Proof. For each case, we construct an appropriate approximate eigenvector. For the ﬁrst, consider the vector f with f(v) = 1, f(w) = −1 and f(y) = 0 for all other

![image 83](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile83.png>)

![image 84](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile84.png>)

- y. This vector is orthogonal to T1/21, the ﬁrst eigenvector of L. Now T−1/2f is just f/√2 while ftAf = −2. Thus,


![image 85](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile85.png>)

ftT−1/2AT−1/2f f 2

- 1

![image 86](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile86.png>)

- 2


= −

,

![image 87](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile87.png>)

and so λ|S| ≥ 1 − −21 = 32.

![image 88](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile88.png>)

![image 89](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile89.png>)

For the lower bound let f be given by f(v) = f(w) = 1/√2 while f(x) = −1/√deg x and f(u) = −1/√deg u. Then we have f ⊥ T1/21. By direct computation,

![image 90](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile90.png>)

![image 91](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile91.png>)

![image 92](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile92.png>)

- 1

![image 93](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile93.png>)

- 2 −


1 deg x −

1 deg u

ftT−1/2AT−1/2f =

, while

![image 94](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile94.png>)

![image 95](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile95.png>)

1 deg u

1 deg x

f 2 ≤ 1 +

. Thus, combining everything, we have that

+

![image 96](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile96.png>)

![image 97](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile97.png>)

- 1

![image 98](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile98.png>)

- 2 − m2


= 12 + O(1/√m).

![image 99](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile99.png>)

![image 100](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile100.png>)

λ2 ≤ 1 −

![image 101](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile101.png>)

![image 102](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile102.png>)

![image 103](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile103.png>)

1 + m2

![image 104](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile104.png>)

5. Probability bounds

In this section we show various estimates on G(n,p), which when combined with the deterministic lemmas on spectral gaps from the previous section, will complete the proofs of Theorems 1.1 and 1.2. In this section we again use that d = (n − 1)p is the expected degree of a vertex.

- Lemma 5.1. For each δ > 0 and m ≥ 0, there is a constant C = C(δ,m) so that the following conditions hold with probability at least 1 − C exp(−md) and 1 − C exp(−md1/4 log n) respectively in G(n,p) with p ≥ δ log n/n.


- (1) Bounded degree condition (b.d.c) Every vertex has degree at most Cd.
- (2) Discrepancy For every pair of vertex sets A and B, letting e(A,B) denote the number of edges between the sets and µ(A,B) = |A||nB|d, one of


![image 105](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile105.png>)

- (a) µe((A,BA,B)) ≤ C

![image 106](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile106.png>)

- (b) e(A,B)log µe((A,BA,B)) ≤ C(|A| ∨ |B|)log |A|∨|n B|

![image 107](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile107.png>)

![image 108](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile108.png>)

- (c) |A| ≤ d1/4/100,|B| ≤ d1/4/100


occurs.

Both of these bounds are consequences of tail bounds of binomial variables, and they are relatively standard in the literature (see, e.g. [22],[18],[12]). This one diﬀers in that we look for more control over the order of decay of the failure probability.

- Proposition 5.2. For each δ > 0 and m ≥ 0, there is a constant C = C(δ,m) suﬃciently large so that if p ≥ δ log n/n then


√

![image 109](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile109.png>)

|xtAy| ≤ C

sup

d

x =1,xt1=0 y =1

with probability at least 1 − C exp(−md1/4 log n) − C exp(−md).

This follows from the standard Kahn-Szemerérdi argument, and it is essentially proven in both Feige and Ofek [18] and the original Friedman, Kahn and Szemerérdi paper [22]. This version has a sharper estimate on the failure probability than [18], which in turn follows from Lemma 5.1. We will delay the proof of both this and the previous lemma to Section 9.

Additionally, the bounded degree condition is needed to make estimates about low degree vertices. Recall the deﬁnition of ℵM from (2). We show that this set is both small and structurally very simple for suﬃciently large M.

- Proposition 5.3. For each δ > 0 and each ǫ > 0, there is an M = M(δ,ǫ) > 1 such that for p ≥ (12 + δ)log n/n, G(n,p) satisﬁes:


![image 110](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile110.png>)

- (1) |ℵM| < n/(100d)
- (2) ℵM is an independent set,
- (3) and maxu∈ℵc


e(u,ℵM) ≤ 1 with probability at least 1 − Cn exp(−(2 − ǫ)d) − C exp(−cn) for some absolute constant c > 0.

M

Proof. (i) We start by estimating the size of ℵM, which we do by a simple union bound. Namely by symmetry we have

Pr[|ℵM| ≥ k] ≤

n k

Pr[deg ui ≤ d/M,1 ≤ i ≤ k].

Let S be the set of vertices uk+1,...,un, then we have Pr[deg ui ≤ d/M,1 ≤ i ≤ k] ≤ Pr[e(ui,S) ≤ d/M,1 ≤ i ≤ k],

which are now independent Binom(n − k,p) variables. Applying Lemma A.1, we get

log Pr[|ℵM| ≥ k] ≤ k (1 + log

n k

) − (d − kp) +

![image 111](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile111.png>)

d M

(1 + log(M)) .

![image 112](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile112.png>)

Setting k = [n/(100d)], we may make M suﬃciently large that

(1 + log

n k

) − (d − kp) +

![image 113](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile113.png>)

d M

d 2

(1 + log(M)) ≤ −

![image 114](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile114.png>)

![image 115](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile115.png>)

for all n ≥ n0(δ). Hence we have that |ℵM| < n/(100d) with probability at least 1 − O exp(−cn) for some absolute constant c > 0.

(ii) We begin by bounding the probability that there is an edge between any two vertices of ℵM. Note that we may assume that d < n/100, lest ℵM = ∅ by the previous bound.

From the union bound and symmetry, we have that Pr[ℵM is not an independent set] ≤ n2 Pr[v ∈ S,w ∈ S,v ↔ w].

Thus it suﬃces to compute this probability, which we do by conditioning deg v = d1 and deg w = d2. Note that the law of the neighborhood N of {v,w} under this conditioning is not uniform over all such neighborhoods. For a possible neighborhood

- H of {v,w}, let E(H) denote the number of edges in this neighborhood. Then we have that


1 Z

Pr[N = H|deg v = d1,deg w = d2] =

![image 116](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile116.png>)

for a suitable normalization constant Z.

p 1 − p

![image 117](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile117.png>)

E(H)

,

Thus, we have that

Pr[v ↔ w|deg v = d1,deg w = d2] Pr[v  ↔ w|deg v = d1,deg w = d2]

Pr[v ↔ w|deg v = d1,deg w = d2] ≤

![image 118](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile118.png>)

n−2 d1−1

n−2 d2−1 n−2 d1

1 − p p

.

=

![image 119](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile119.png>)

![image 120](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile120.png>)

n−2 d2

As we consider only d1 and d2 that are less than d/M, and as d < n/100, we may bound this as Cd/n for some absolute constant C. It remains to estimate the probability that both v and w are in ℵM. Hence we have

Pr[deg v ≤ d/M,deg w ≤ d/M] ≤ Pr[X ≤ d/M]2 , where X ∼ Binom(n − 2,p). Applying Lemma A.1, we have that

2d M

- (8) Pr[deg v ≤ d/M,deg w ≤ d/M] ≤ exp −2d +


(1 + log M + O(1))

![image 121](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile121.png>)

Thus by adjusting M to be suﬃciently large, we have Pr[ℵM is not an independent set] = O(ndexp(−(2−ǫ/2)d)) = O(n exp(−(2−ǫ)d)).

(iii) This follows in much the same way as the proof of (ii). Here though, we

require that the degrees of ℵcM are not too large. By Lemma 5.1, these degrees can be bounded by some Cd with probability at least 1 − O(exp(−2d)), and so it suﬃces to assume it. From the union bound and symmetry, we have that

Pr[∃u ∈ ℵcM : e(u,ℵM) ≥ 2 ∩ b.d.c.] ≤ n3 Pr[u ∈ ℵcM,v ∈ ℵM,w ∈ ℵM,u ↔ v,u ↔ w ∩ b.d.c.].

Again we condition on the degrees deg u = d1,deg v = d2, and deg w = d3, and bound

Pr[u ↔ v,u ↔ w|deg u = d1,deg v = d2,deg w = d3] ≤

Pr[u ↔ v,u ↔ w|deg u = d1,deg v = d2,deg w = d3] Pr[u  ↔ v,u  ↔ w,v  ↔ w|deg u = d1,deg v = d2,deg w = d3]

![image 122](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile122.png>)

2 n−3 d1−2

n−3 d2−1

n−3 d3−1 + 1−pp d n−3

n−3 d2−2

n−3 d3−2 n−3 d1

1 − p p

![image 123](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile123.png>)

1−2

.

=

![image 124](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile124.png>)

![image 125](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile125.png>)

n−3 d3

n−3 d2

As before, we have d1 and d2 are less than d/M. As we also require the b.d.c. to hold, we may take d1 ≤ c1d and as d < n/100, we may bound this as Cc1d2/n2 for some absolute constant C.

From (8), we have that

Pr[v ∈ ℵM,w ∈ ℵM] = O(exp(−(2 − ǫ/2)d)), and so we conclude that

e(u,ℵM) > 1 = O(n exp(−(2 − ǫ)d)).

Pr max

u∈ℵcM

Our next lemma shows that the variance of the degree distribution is not too much larger than its expectation.

- Lemma 5.4. For each ﬁxed δ > 0 and m ≥ 0, there is a constant C = C(δ,m) suﬃciently large so that if p ≥ δ log n/n then


(deg v − d)2 ≤ Cnd.

v∈V

with probability at least 1 − C exp(−md). Proof. Note that this sum is the square Euclidean norm of the vector (A − dI)1. Further, it is possible to write the norm as

|xt(A − dI)1|.

(A − dI)1 = sup

x =1

For any ﬁxed vector x, we orthogonally decompose it as x = v + c1, where |c| ≤ 1/√n. We have that vt(A − dI)1 = vtA1, and so by Proposition 5.2, for any m there is a constant C so that

![image 126](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile126.png>)

√

![image 127](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile127.png>)

|vtA1| ≤ C

sup

nd

v =1 vt1=0

with probability at least 1−O(exp(−md)). It remains to bound 1t(A−dI)1, which is

1t(A − dI)1 =

deg v − nd.

v∈V

Note that v∈V deg v ∼ 2 Binom( n2 ,p), and so by standard Chernoﬀ bounds, we have that

t2 Cnd

Pr 1t(A − dI)1 ≥ t ≤ C exp(−

) for some absolute constant C and all t ≤ nd. By taking t = mn

![image 128](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile128.png>)

√

![image 129](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile129.png>)

d, we have that |1t(A − dI)1| ≤ mn

√

![image 130](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile130.png>)

d with probability at least 1 − O(exp(−mn)) for suﬃciently large n. Recalling that |c| ≤ 1/√n, we have that

![image 131](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile131.png>)

√

![image 132](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile132.png>)

c1t(A − dI)1 = O(

nd). which completes the proof.

Using the previous lemma, we show that T−1/2 tends to map the orthogonal complement of the ﬁrst eigenvector of M to the approximate orthogonal complement of the ﬁrst eigenvector of A.

- Lemma 5.5. Let W be the set of vertices x for which deg x > 0, and let ℵM be as in Proposition 5.3. For each δ > 0 and m ≥ 0, there is a constant C = C(δ,m) suﬃciently large so that if p ≥ δ log n/n then


√n d

![image 133](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile133.png>)

|xtT−1/21ℵc

| ≤ C

sup

![image 134](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile134.png>)

M

x =1, xtT1/21W =0

with probability at least 1 − C exp(−md). Proof. As we have that |ℵM| < n/(100d) by Proposition 5.3, it follows that

M ≤ d|ℵM| = O √n .

![image 135](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile135.png>)

M| ≤ T1/21ℵ

|xtT1/21ℵ

![image 136](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile136.png>)

= −xtT1/21ℵc

Further, we have that xtT1/21ℵ

, and hence it suﬃces to show that

M

M

√n d

![image 137](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile137.png>)

xt(T−1/2 − T1/2/d)1ℵc

≤ C

.

sup

![image 138](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile138.png>)

M

x =1, xtT1/21=0

Taking norms,

≤ (T−1/2 − T1/2/d)1ℵc

xt(T−1/2 − T1/2/d)1ℵc

. Squaring this norm, we get

M

M

√deg v d

2

![image 139](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile139.png>)

2

1 √deg v −

M d3 v∈ℵ

(deg v − d)2 .

(T−1/2 − T1/2/d)1ℵc

≤

=

![image 140](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile140.png>)

![image 141](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile141.png>)

![image 142](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile142.png>)

![image 143](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile143.png>)

M

v∈ℵcM

c M

- Lemma 5.4 completes the proof.


Proof of Theorem 1.1. We show that we satisfy the conditions in Lemma 4.1. In Lemma 5.1, we show the bounded degree condition. In Proposition 5.2, we show the adjacency matrix condition. In Proposition 5.3, we show the fuzz condition. Finally, in Lemma 5.5, we show the parallel eigenspaces condition. Summing the failure probabilities, the failure probability in Theorem 1.1 is the sum of Cn exp(−(2 − ǫ)d) from Proposition 5.3 and C exp(−md1/4 log n) from Proposition 5.2, with all other errors much smaller in magnitude. Without the condition that p ≥ (21 + δ)log n/n, for some δ > 0, the failure probability in Proposition 5.3 is not in control.

![image 144](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile144.png>)

We wish to now show the lower bounds for λ(G˜). We will use Lemma 4.2, and this requires that we show:

Proposition 5.6. If p = ω(√log n/n) and p ≤ 21 log n/n then with high probability, there are four distinct vertices a,b,c,d in the giant component for which the degrees

![image 145](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile145.png>)

![image 146](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile146.png>)

of a and d are at least np/2, the degrees of b and c are 2, and the induced subgraph on (a,b,c,d) is a path.

We ﬁrst show by the second moment method that such four-tuples (a,b,c,d) exist in the graph with high probability. We then show that with high probability, the small components have maximal degree o(np), and hence these four-tuples must have been part of the giant component.

- Lemma 5.7. Suppose that p = ω(1/n) and that p ≤ 21 log n/n. Then, with high probability, there are four-tuples (a,b,c,d) for which the degrees of a and d are at least np/2, the degrees of b and c are 2, and the induced subgraph on (a,b,c,d) is a path. Proof. Deﬁne the pair of events


![image 147](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile147.png>)

- A(a,b,c,d) = {a ↔ b ↔ c ↔ d,deg b = deg c = 2} and
- B(a,b,c,d) = A(a,b,c,d) ∩ {deg a ≥ np/2,degd ≥ np/2}.


Set S to be the number of occurrences of B, i.e. S =

1 {B(a,b,c,d)} ,

a,b,c,d

with the sum over ordered 4-tuples of distinct vertices (a,b,c,d). We need to show that S > 0 with high probability.

The probability of A can be explicitly calculated as Pr[A(a,b,c,d)] = p3(1 − p)2(n−3).

Meanwhile, conditional on A(a,b,c,d), the probability of B(a,b,c,d) is exactly the probability of having two speciﬁc vertices of degree at least np/2−1 in G(n−2,p). Set Q = Pr[X ≥ np/2] where X ∼ Binom(n,p). Note that as np → ∞, we have that Q = 1 − o(1).

Furthermore, as np → ∞ we have that Pr[B(a,b,c,d) | A(a,b,c,d)] = Q2(1 − o(1)),

simply by conditioning on the edge between a and d. By summing over all possible tuples, it follows that ES = Θ(nQ2(np)3e−2np) = ω(1).

For the variance of S, we need to compute probabilities of the pairs B((ai)4i=1)∩ B((bi)4i=1). Note that if a2 = b2 then the only way both can happen is if ai = bi for all i ∈ [4]. Analogous conclusions hold if a2 = b3 or if a3 ∈ {b2,b3}. Thus, the only nontrivial way for the events B((ai)4i=1) and B((bi)4i=1) to intersect is if

- (1) all ai and bi are distinct,
- (2) a1 = b1 and the rest are distinct,
- (3) a1 = b1, a4 = b4, and the rest are distinct, or
- (4) ai = bi for all i.


Note that there’s no need to consider a1 = b4, as the event B((bi)4i=1) is preserved under reversing the ai. Likewise, there’s no need to consider a4 = b4, as one can reverse both ai and bi. Set Ti to be the pairs of tuples satisfying each of the 4 cases.

If the pair is in T1, then Pr B((ai)4i=1) ∩ B((bi)4i=1) A((ai)4i=1) ∩ A((bi)4i=1) = Q4(1 − o(1))

- as once more, this is the statement that four vertices in G(n − 4,p) have degree at least (np/2 − 1). We also have that


Pr A((ai)4i=1) ∩ A((bi)4i=1) = p6(1 − p)4n−16, so that

Pr B((ai)4i=1) ∩ B((bi)4i=1) = Pr B((ai)4i=1) 2 (1 − o(1)). Thus the contribution of the pairs in T1 to the variance of S is o((ES)2). For terms from T2, the same reasoning as above shows that Pr B((ai)4i=1) ∩ B((bi)4i=1) = Q3p6(1 − p)4n(1 − o(1))

For such pairs, however, we have that |T2| = Θ(n7), and hence the contribution to the variance of S is o((ES)2). In the same way, the contributions of T3 and T4 are smaller still. As each is individually of order o((ES)2), we have that S > 0 with high probability.

- Lemma 5.8. Suppose that p = ω(1/n), then for any ǫ > 0, the number of vertices not in the giant component is at most ne−(1−ǫ)np with high probability.


Proof. Set R to be the number of vertices not in the largest component of G(n,p). If W is the set of these vertices, then W satisﬁes e(W,Wc) = 0. Therefore, if there is no collection W of at least r vertices such that e(W,Wc) = 0, then R < r.

The expected number ENr of such collections W is given by ENr = (1 − p)r(n−r)

n r

.

Set r0 = ne−(1−ǫ)np. We will show that n/r=2r

ENr → 0, which implies the lemma. Subdivide the sum into two pieces S1 and S2, given by S1 = ⌊rǫn/4⌋

0

ENr and S2 = n/⌊ǫn/2 4⌋ ENr. For ⌊ǫn/4⌋ ≤ r ≤ n/2,

0

n r ≤ e−c

ǫn2p2n, for some cǫ > 0, which decays exponentially in n as np → ∞. Hence S2 → 0.

ENr = (1 − p)r(n−r)

As for S1, we claim that for any α > 0 there is an n ≥ n0(α,ǫ) suﬃciently large so that for all r0 < r < ǫn/4, ENr+1 ≤ αENr for all n ≥ n0(α,ǫ). Estimating for these r,

n − r − 1 r + 1 ≤

ENr+1 ENr

= (1 − p)n−2r+1

![image 148](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile148.png>)

![image 149](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile149.png>)

ne−np+2rp r

.

![image 150](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile150.png>)

ne−(1−ǫ/2)np r

≤

. ≤ e−ǫnp/2.

![image 151](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile151.png>)

Hence, as np → ∞, this is eventually less than any positive α. As S1 is dominated by a geometric series, and S1 = O(ENr

). For this leading term, we get that

0

r0

0(n−r0) en r0

≤ exp −ǫn2pe−(1−ǫ)np(1 − o(1)) → 0, completing the proof.

0 ≤ e−pr

ENr

![image 152](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile152.png>)

- Lemma 5.9. If p = ω(√log n/n), then with high probability, the maximum degree of the vertices not in the giant component is at most np/100.


![image 153](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile153.png>)

Proof. Set R to be the number of vertices not in the giant component. By Lemma 5.8,

we have that R ≤ ne−np/2 with high probability. Suppose that W is a ﬁxed collection of vertices of size r. Conditional on there being no edges between W and Wc, the law of the induced graph on W is simply that of G(r,p).

- Let X ∼ Binom(r−1,p). Then by Lemma A.2 there are absolute constants c > 0

and M > 0 so that

Pr[X > np/100] ≤ exp(−cnp log(n/r)) provided r < n/M. Setting EW to be the event that W and Wc are not connected

Pr max

w∈W

deg w > np/100 EW ≤ r exp(−cnp log(n/r)).

- Let Y be the max degree of all vertices not in the largest component As the previous bound holds for all W in consideration, we get that


Pr[Y > np/100 | R = r] ≤ r exp(−cnp log(n/r)). This bound is monotone increasing in r, and so we get that

Pr Y > np/100 R ≤ ne−np/2 ≤ n exp(−c(np)2(1 − o(1)))

for some absolute constant c. Thus by the assumption on np, the desired claim holds.

Proof of Theorem 1.2 and Proposition 5.6 .

For Proposition 5.6, the previous three Lemmas 5.7, 5.8, and 5.9 show the desired claim that w.h.p. there are tuples (a,b,c,d) of vertices in the giant component for which deg a and deg d are at least np/2, vertices b and c have degree 2, and the induced graph on these vertices is a path.

Letting H be the giant component of the graph, then there is a constant C so that the eigenvalues of the Laplacian of H satisfy

λ|H| ≥ 23 and

![image 154](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile154.png>)

λ2 ≤ 12 + C/√np, by Lemma 4.2.

![image 155](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile155.png>)

![image 156](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile156.png>)

6. Gap process theorem

In this section we prove a general process-version theorem for the spectral gap below the connectivity threshold. We recall the deﬁnition of Ytk(n), the continuous time Linial-Meshulam process. Let Fk denote the collection of all possible k–faces on n vertices, and let Fk(S) for simplicial complex S be all k–faces of S. Let {Tσ,σ ∈ Fk} be an i.i.d. family of Exp(1) variables. Deﬁne {Ytk(n),t ≥ 0} to be the continuous time Markov process where Y0k(n) is the complete (k − 1)-skeleton of the n-simplex and its k-faces are given by

Fk(Ytk(n)) = {σ ∈ Fk : Tσ ≤ t}.

Thus Ytk(n) is the complex whose k-faces have been born up to time t, and Y∞k (n) is the complete k-skeleton of the n-simplex. For k = 1, this recovers the standard

continuous time Erdős–Rényi process. For ﬁxed t, Ytk(n) is the Bernoulli complex Yk(n,p(t)) with p(t) = 1 − e−t. Let d(t) = (n − 1)p(t). Fix δ ∈ (0, 21) and deﬁne t0 by the relation that

![image 157](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile157.png>)

(12 + δ)log n/n k = 1, (k − 1 + δ)log n/n k > 1.

![image 158](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile158.png>)

p(t0) =

For any (k − 2)–dimensional face f of a k–dimensional simplicial complex S, we identify its link with a graph, denoted lk(f). We will only consider links of (k −2)– dimensional faces. This graph lk(f) has vertex set given by all (k −1)–dimensional faces containing f. Two of these edges e and g are connected if and only if e ∪ g, which is a k–dimensional face, is contained in S.

For example, when k = 1 and S is a graph, the only (k − 2)–dimensional face is the empty set. Its link has vertex set given by all 0–dimensional faces (all vertices), and vertices are connected if and only if they are contained in an edge. Hence, in this case lk(∅) can be identiﬁed with the original graph S.

In Ytk(n), which has a complete (k − 1)–skeleton, each link is distributed as a G(n − k + 1,p(t)). These links {lk(f)}, where f ranges over all (k − 2)–dimensional faces, are not independent, and in fact are analysis rests in some ways on exploiting their exact dependency structure.

Recall that we refer to a (k −1)–dimensional face f as isolated if and only if it is not contained in any k–dimensional face. Note that a face f is isolated if and only if it is an isolated vertex in lk(g) for all (k − 2)–dimensional g ⊂ f.

Theorem 6.1. Let Y˜tk(n) denote the process derived from Ytk(n) by removing every isolated (k − 1)-face. There is a constant C = C(k,δ) so that with high probability

the normalized Laplacian of lk(f) of every dimension–(k − 2) face f of Y˜tk(n) has max

C d(t)

|1 − λi| <

.

![image 159](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile159.png>)

![image 160](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile160.png>)

i>1

for all t ≥ t0.

An equivalent formulation is that each lk(f) for codimension-2 f ∈ Ytk(n) consists of isolated vertices and a giant component whose gap is 1 − C/ d(t) for all time t ≥ t0. In the higher-dimensional setting, the proof is more complicated than simply studying each link individually and taking the union bound. The key is to study the “fuzz” globally. To this end, for each lk(f) and for any M ≥ 1, let

![image 161](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile161.png>)

- (9) ℵfM(t) = {w ∈ V(lk(f)) : deglk(f)(w) ≤ d(t0)/M}. Note that this makes each ℵfM(t) monotone decreasing in t.


- Lemma 6.2. There is an M = M(k,δ) and an ǫ = ǫ(k,δ) so that


2

ℵfM(t0)

≤ n1−ǫ

f∈Fk−2

with overwhelming probability. Proof. For k = 1, there is only one link to consider, and so it suﬃces to show that

ℵ∅M(t0) ≤ n1/2−ǫ. For k > 1, we proceed by showing that for any ǫ there is an M so that both

k−2 ℵfM(t0) ≤ nǫ

(1) maxf∈F

ℵfM(t0) ≤ n1−2ǫ hold with overwhelming probability.

(2) f∈F

k−2

The ﬁrst condition follows from an identical argument to the ﬁrst part of Proposition 5.3; the k = 1 case follows from an identical argument, and we just sketch the k > 1 case. As before, for any 1 > η > 0, there is an M(δ,η) suﬃciently large so that for a ﬁxed set of vertices w1,w2,...,w⌈nǫ⌉,

Pr deglk(f)(wi) ≤ d(t0)/M, ∀ 1 ≤ i ≤ ⌈nǫ⌉ = O(exp(−nǫd(t0)(1 − η))). This overwhelms the O(exp((1 − ǫ)nǫ log n)) possible choices of vertices as

d(t0)/ log n > (1 + δ)(1 + o(1))

and η may be chosen suﬃciently small. As there are only O(nk−1) many links to consider, this may be taken to hold for all links simultaneously with overwhelming probability.

We now turn to the second condition. For a ﬁxed (k − 1)-dimensional face f, let Xf denote the number of k-faces in Ytk

(n) containing f. If f is a vertex in a (k − 2)-dimensional face of Ytk

0

(n), then Xf is the degree of that vertex in lk(f). Hence

0

1 k f∈F

ℵfM(t0) =

1 {Xf ≤ d(t0)/M} .

![image 162](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile162.png>)

f∈Fk−1

k−2

Thus by adjusting ǫ, it suﬃces to show the claim for the right hand side. Call a collection S of (k − 1)-faces balanced if

|{σ ∈ S : w ⊂ σ}| ≤ nǫ. Observe that we have shown that with overwhelming probability the set S = {f ∈ Fk−1 : Xf ≤ d(t0)/M}

max

w∈Fk−2

is balanced with overwhelming probability. By symmetry we have Pr[∃ f1,f2,...,fr ∈ Fk−1 : Xf

i ≤ d(t0)/M, 1 ≤ i ≤ r, {fi} balanced] ≤

n k

i ≤ d(t0)/M,1 ≤ i ≤ r, {fi} balanced]. Let X denote the number of k-faces that contain some fi. If every Xf

Pr[Xf

r

i ≤ d(t0)/M, it follows that X ≤ rd(t0)/M. Each fi is contained in n − k possible k-faces, but it may be possible that some fi and fj are both contained in a single k-face. If this occurs, however, it must be that |fi ∩ fj| = k − 1. In other words, each contains a common (k − 2)-face. Furthermore, there is at most one k-face that contains both fi and fj.

A ﬁxed face fj contains k distinct (k−2)-faces q1,q2,...,qk. As {fi} is balanced, each ql is contained in at most nǫ distinct fi. Thus there are at most nǫk many kfaces that contain fj and some other fi, and this implies there are at least r(n−k− nǫk) distinct possible k-faces that contain some fi. It follows that X stochastically dominates a Binom r(n − k − nǫk) ,p(t0) variable. Applying Lemma A.1, we get

i ≤ d(t0)/M,1 ≤ i ≤ r, {fi} balanced] ≤ Pr[X ≤ rd(t0)/M] ≤ exp −r(n − k − nǫk)p(t0) + rd(t

Pr[Xf

ǫk))p(t0)

M (1 + log M(1+r(n−k−n

0)

rd(t0) ) . Thus, we get

![image 163](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile163.png>)

![image 164](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile164.png>)

i ≤ d(t0)/M, 1 ≤ i ≤ r] ≤ r (k log n − log r) − d(t0) +

log Pr[∃ f1,f2,...,fr : Xf

d(t0) M

![image 165](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile165.png>)

(1 + log(M)) (1 + o(1)).

Since d(t0) ≥ (k−1+δ)logn−o(1), we can set r = [n1−δ/2] and make M suﬃciently large that

d(t0) M

(1 + log(M)) → −∞. Taking ǫ = δ/4, we have shown the desired claim.

(k log n − log r) − d(t0) +

![image 166](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile166.png>)

With global control on the number of exceptional vertices, the proof now reduces to essentially a union bound over all later times and links.

- Lemma 6.3. There is a constant C = C(k) so that with high probability, every lk(f) where f ∈ Ytk(n) has dimension (k − 2) satisﬁes


- (1) Bounded degree condition (b.d.c) Every vertex has degree at most Cd(t).


- (2) Adjacency matrix The adjacency matrix of the link satisﬁes

sup

x =1,xt1=0 y =1

|xtAy| ≤ C d(t).

![image 167](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile167.png>)

- (3) Parallel eigenspaces Setting ℵM = ℵfM(t) and T to be the diagonal matrix of degrees of the link,


√n d(t)

![image 168](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile168.png>)

|xtT−1/21ℵc

| ≤ C

.

sup

![image 169](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile169.png>)

M

x =1, xtT1/21W =0

for all t ≥ t0. Proof. Let I be the interval [t1,t2], where t0 ≤ t1 ≤ t2. The probability that there are two faces that appear in this interval can be bounded by

1 ∈ I and Tσ

2 ∈ I] ≤

Pr[∃ σ1,σ2 : Tσ

n k

2

(p(t2) − p(t1))2 .

Let r be the smallest integer so that p(t0) + rn−2k−1 ≥ 1. Set pi = p(t0) + in−2k−1 for all 0 ≤ i < r, and set pr = 1. Let ti be such that p(ti) = pi, and set tr = ∞. Note that for t ∈ [ti,ti+1), Ytk(n) = Ytk

(n) and Ytk(n) = Ytk

(n) implies there must be two faces σ1 and σ2 for which Tσ

i+1

i

2 ∈ [ti,ti+1). Hence,

,Tσ

1

r−1

Pr ∃ t ≥ t0 : Ytk(n) = Ytk

2 ∈ I]

Pr[∃ σ1,σ2 : Tσ

(n) ∀ 0 ≤ i ≤ r ≤

,Tσ

1

i

i=0

r−1

n−2k−2 ≤ n−2.

≤

i=0

By applying Lemma 5.1, Proposition 5.2, and Lemma 5.5 with m suﬃciently large, we may thus assure that there is a constant suﬃciently large that these properties occur for all links of all Ytk

(n), for 0 ≤ i ≤ r − 1.

i

- Lemma 6.4. There is an M = M(k,δ) and a constant C = C(M,k) so that with t1


satisfying p(t1) = C log n/n, all ℵfM(t) = ∅ for t ≥ t1 with high probability. Further, for all t1 ≥ t ≥ t0 every lk(f) of Ytk(n) satisﬁes

- (1) |ℵM| ≤ n2,

![image 170](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile170.png>)

- (2) ℵM is an independent set,
- (3) and maxu∈ℵc


e(u,ℵM) ≤ 1

M

with ℵM = ℵfM(t). Proof. There is an M1 so that this holds for Ytk

(n) by Proposition 5.3 and by taking the union bound over all links. Likewise, there is an M2 so that the conclusions of Lemma 6.2 holds. Take M to be the maximum of these, and note that from

0

monotonicity, the conclusions of both the proposition and lemma hold. As ℵfM(t) is monotone in t also, we have that

|ℵfM(t)| ≤ |ℵfM(t0)| ≤ n/2 is satisﬁed for all n suﬃciently large.

From a union bound and Lemma A.1, we may choose C = C(M,k) suﬃciently large so that with probability going to 1,

ℵfM(t1) = ∅ for all f ∈ Fk−2.

Let τi be the times at which the ith face is added to Ytk(n) after time t0, and let τ0 = t0. Likewise, let ∆i denote the ith face, and let F(τi) = σ(Yτk

(n)). Let N denote the largest i so that τi ≤ C log n/n. From Chernoﬀ bounds, there are at most 100C(logn)nk many k-dimensional faces in Ytk

i

(n) with overwhelming probability, and hence N ≤ 100(logn)nk with overwhelming probability.

1

We begin by bounding the probability that a newly added face creates an edge between two vertices of ℵfM(t) for some f ∈ Fk−2.

|ℵfM(τi)|2 |Fk| − |Yτk

Pr ∃ u,v ∈ ℵfM(τi) : u,v ∈ ∆i+1 F(τi) ≤

- (10)


![image 171](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile171.png>)

(n)| ≤

i

|ℵfM(τ0)|2 |Fk| − |Ytk

.

![image 172](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile172.png>)

(n)|

1

Let Ei,f denote the event that

- (1) the number of k–dimensional faces |Ytk

1

(n)| ≤ 100Cnk log n,

- (2) f∈F

k−2

|ℵfM(t0)|2 ≤ n1−ǫ,

- (3) there exists u and v in ℵfM(τi) so that u ∈ ∆i+1 and v ∈ ∆i+1.


By conditioning, we have that

N

|ℵfM(τ0)|21 {Ei,f} |Fk| − |Ytk

Pr[∪i,fEi,f] ≤ E

![image 173](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile173.png>)

(n)|

i=0 f∈Fk−2

1

f∈Fk−2 |ℵfM(τ0)|21 {Ei,f} |Fk| − 100Cnk log n

N

≤ E

![image 174](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile174.png>)

i=0

N

n1−ǫ1 Ytk

(n) ≤ 100Cnk log n |Fk| − 100Cnk log n

≤ E

1

![image 175](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile175.png>)

i=0

(100Cnk log n)n1−ǫ |Fk| − 100Cnk log n

= O(n−ǫ log n).

≤

![image 176](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile176.png>)

Thus with high probability, no face added between t0 and t1 creates an edge between two elements of any ℵfM(t).

We now turn to bounding the probability that a newly added face connects an element of ℵfM(t) to a neighbor of ℵfM(t). Let NMf (t) be the set of neighbors of ℵfM(t), and let D(t) be an upper bound for the degree of a vertex of any link of Ytk(n). Note that |NMf (t)| ≤ D(t)|ℵfM(t)|. Then

D(τi)|ℵfM(τi)|2 |Fk| − |Yτk

Pr ∃ u ∈ ℵfM(τi),v ∈ NMf (t) : u,v ∈ ∆i+1 F(τi) ≤

.

![image 177](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile177.png>)

(n)|

i

With high probability, there is a constant K so that all the degrees can be bounded by K log n for all t ≤ t1. This failure probability is at most a logarithmic factor

more than the failure probability in (10). Hence the same proof shows that with high probability, no added face increases

e(u,ℵfM(t)).

max u∈V(lk(f))\ℵfM(t)

Proof of Theorem 6.1. We are essentially ready to apply Lemma 4.1. The only concern is that in (9), the set ℵfM(t) is deﬁned in terms of d(t0) and not d(t). However, as noted in Lemma 6.4, all these sets disappear once p(t1) = C log n/n,

- at which point d(t) has only risen by a factor of K = p(t


1)

p(t0). Thus, Qf(t) = {w ∈ V(lk(f)) : deglk(f)(w) ≤ d(t)/KM} ⊆ ℵfM(t),

![image 178](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile178.png>)

for all t ≤ t1, and by monotonicity, all the desired properties of ℵfM(t) transfer to Qf(t). Thus Lemmas 6.3 and 6.4 show all the needed properties of Lemma 4.1 hold, completing the proof.

7. Cohomology structure theorem

The structure theorem for cohomology relies on the following theorem of Ballman– Świątkowski [3]. A simplicial complex ∆ is called pure k–dimensional if it is k– dimensional and every face is contained in a k–dimensional one.

Ballman–Świątkowski criterion. If ∆ is a ﬁnite, pure k-dimensional simplicial complex, so that for every (k − 2)-dimensional face σ, the normalized Laplacian L = L[lk(σ)] satisﬁes λ2 > 1 − k1 then Hk−1(∆,Q) = 0.

![image 179](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile179.png>)

Proof of Theorem 3.2. Recall that we deﬁne t0 so that p(t0) = (k − 1 + δ)log n/n. Let Y˜t denote the simplicial complex Ytk(n) with all its isolated (k−1)-faces deleted. By Theorem 6.1, w.h.p. for all t ≥ t0, all links of Y˜t have λ2(L) = 1 − o(1).

We need to check that Y˜t is pure k-dimensional, i.e. that every face is contained in some k-dimensional face. Note that this can only fail if there is some (k − 2)dimensional face of Ytk(n) that is not contained in any k-dimensional face. As this is a monotone property, it suﬃces to check that Ytk

(n) has no such (k − 2)-faces. Put I to be the number of isolated (k − 2)-faces in Ytk

0

(n). Then

0

n k − 1

2/2(1 − o(1)),

(1 − p(t0))n

EI =

which decays exponentially in n. Hence, Y˜t is pure k-dimensional w.h.p. for all t ≥ t0, and so Theorem 7 applies. It follows that Hk−1(Y˜t,Q) = 0, and it remains to compare Hk−1(Y˜t,Q) and Hk−1(Ytk(n),Q).

For what remains, ﬁx t ≥ t0. It will follow from induction that each additional (k − 1)-face we glue to Y˜ increases the dimension of the (k − 1)-cohomology by 1.

- Let Z be the complex formed by including one of the isolated (k−1)-faces of Y back into Y˜. Let B be a neighborhood of the included (k − 1)-face that is homotopic to a single (k − 1)-simplex. Then the Mayer-Vietoris sequence (see Chapter 3 of [29]) for the (k − 1)-dimensional cohomology is ··· → Hk−1(Z,Q) → Hk−1(Y˜,Q) ⊕ Hk−1(B,Q) → Hk−1(Y˜ ∩ B,Q) → Hk(Z,Q).


As Y˜ ∩B is homotopic to a (k −2)-dimensional sphere, Hk−1(Y˜ ∩B,Q) = 0. Also, Hk−1(B,Q) = Q, and so this sequence becomes

0 → Hk−1(Z,Q) → Hk−1(Y˜,Q) ⊕ Q → 0,

or otherwise stated, Hk−1(Z,Q) ∼= Hk−1(Y˜,Q) ⊕ Q. Each additional isolated (k − 1)-faces increases the dimension by one by the very same argument, which completes the proof.

8. Property (T)

The proof here is nearly identical to the proof of the cohomology vanishing structure theorem. To establish our results concerning property (T) of random fundamental groups, we will use the following theorem of Żuk.

Żuk’s criterion. If X is a pure 2-dimensional locally-ﬁnite simplicial complex so that for every vertex v, the vertex link lk(v) is connected and the normalized Laplacian L = L[lk(v)] satisﬁes λ2(L) > 1/2, then π1(X) has property (T).

Proof of Theorem 1.4. Recall that we deﬁne t0 so that p(t0) = (1 + δ)log n/n. Let Y˜t denote the simplicial complex Yt2(n) with all its isolated edges deleted. By Theorem 6.1, w.h.p. for all t ≥ t0, all links of Y˜t have λ2(L) = 1 − o(1). Then by Żuk’s criterion, π1(Y˜t) has property (T) for all t ≥ t0.

Fix t ≥ t0. It only remains to compare the fundamental groups π1(Y˜) and π1(Y ). But attaching a 1-cell to a connected CW complex W adds a free Z-factor to the fundamental group π1(W), by the Seifert–van Kampen theorem (see Theorem 1.20 of [29]). So we only need to check that deleting all the isolated edges in Y does not result in a disconnected complex Y˜.

Removing less than n −1 edges from the complete graph Kn can not disconnect it; indeed, to separate a component of order k form the rest of the graph requires removing at least k(n − k) edges, which is minimized when k = 1. Thus we need only check that the number of isolated edges is fewer than n−1. From monotonicity, it suﬃces to show that at time t0 the number of isolated edges is w.h.p. o(n).

By linearity of expectation, the expected number of edges deleted E[D] is given by

n 2

(1 − p(t0))n−2

E[D] =

- 1

![image 180](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile180.png>)

- 2


n2 exp(−p(t0)(n − 2)) ≤ O n1−c

≤

for some constant c > 0. By the second moment method, for example, D is tightly concentrated around its mean, so w.h.p. Y˜ is connected. The claim follows.

Corollary 3.7 quickly follows.

Proof of Corollary 3.7. Let I denote the number of isolated edges. The expected number of isolated edges E[I] is

n 2

(1 − p)n−2 ≤ n2e−np

E[i] =

Taking p = (2 logn + f(n))/n, where f(n) → ∞, this is seen to go to 0, completing the proof.

9. Kahn-Szemerérdi argument

In this section we give the proof of Proposition 5.2 and Lemma 5.1, which are minor modiﬁcations of the standard Kahn–Szemerérdi argument.

We begin with a proof of the regularity conditions. Proof of Lemma 5.1. For any vertex v, deg(v) is a binomial random variable with mean d > δ log(n). By Lemma A.2, P(deg(v) > c0d) ≤ exp −dc

0 log c0

![image 181](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile181.png>)

3 provided c0 > 4. Thus taking the union bound over all vertices, we get that

Pr[b.d.c. fails] ≤ exp(d(δ1 − c

0 log c0

3 )).

![image 182](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile182.png>)

![image 183](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile183.png>)

By taking c0 suﬃciently large, we may take 1 δ −

c0 log c0

3 ≤ −m, completing the proof of the ﬁrst claim.

![image 184](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile184.png>)

![image 185](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile185.png>)

We will now turn to showing the discrepancy property, for which we need to show there are constants ci = ci(δ,m) so that at least one of

- (1) µe((A,BA,B)) ≤ c1

![image 186](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile186.png>)

- (2) e(A,B)log µe((A,BA,B)) ≤ c2(|A| ∨ |B|)log |A|∨|n B|

![image 187](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile187.png>)

![image 188](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile188.png>)

- (3) |A| ∨ |B| ≤ d1/4/100


Note that these properties are monotone in ci, and so we are free to increase the constants as need be throughout the proof.

Let D be the event that the discrepancy condition fails and let D(A,B) be the event that the discrepancy condition fails for sets A and B. Then by the union bound

P(D) ≤ P(∃A,B with |A| ∧ |B| ≥ n/e) : D(A,B) occurs)

+ P(∃A,B with |A| ∨ |B| ≥ n/e ≥ |A| ∧ |B|) : D(A,B) occurs)

P(D(A,B))

+

A,B: |A|∨|B|<n/e

Taking c1 > e2, then when |A| ∧ |B| ≥ ne , e(A,B) > c1µ(A,B) > c1(n/e)2d/n > nd.

![image 189](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile189.png>)

Thus, there are at least nd edges in the graph. The distribution of the number of edges is binomial with mean n(n − 1)p/2 = nd/2, and so the probability of this is going to zero exponentially in nd, i.e.

- (11) P(∃A,B with |A| ∧ |B| ≥ n/e) : D(A,B) occurs) = O(exp(−cnd)) for some absolute constant c > 0.

If |A| ∨ |B| ≥ ne > |A| ∧ |B|, and if the bounded degree condition holds, then e(A,B) ≤ (|A| ∨ |B|)c0d and

![image 190](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile190.png>)

e(A,B) µ(A,B,n) ≤

![image 191](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile191.png>)

c0nd(|A| ∨ |B|) |A||B|d

![image 192](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile192.png>)

=

c0n |A| ∧ |B|

![image 193](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile193.png>)

≤ c0e. Thus taking c1 > c0e, we have that

P(∃A,B with |A| ∨ |B| ≥ n/e ≥ |A| ∧ |B|) : D(A,B)occurs) ≤ P(b.d.c.fails)

- (12) = O(exp(−md)).


Now we need to deal with the case that both A and B are less than ne , but at least one is greater than d1/4/100. Take c2 > 18 + 1200m. For emphasis, we will write µ(A,B,n) = µ(A,B) = |A||nB|d. Choose r = r(A,B,n) = c1 ∨ r1 where r1 is the solution to

![image 194](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile194.png>)

![image 195](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile195.png>)

µ(A,B,n)r1 log(r1) = c2(|A| ∨ |B|)log |A|∨|n B|.

![image 196](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile196.png>)

For any A, B and n we must have either

- • e(A,B) ≤ rµ(A,B,n) and r = c1
- • e(A,B) ≤ rµ(A,B,n) and r = r1 or
- • e(A,B) > rµ(A,B,n)


Thus if D(A,B) occurs then at least one of the following three events occur.

- • D1 = D1(A,B) = e(A,B) ≤ rµ(A,B,n), r = c1 and

e(A,B) > c1µ(|A|,|B|,n)

- • D2 = D2(A,B) = e(A,B) ≤ rµ(A,B,n),r = r1 and

e(A,B)log µe((A,B,nA,B)) > c2(|A|∨|B|)log |A|∨|n B|

![image 197](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile197.png>)

![image 198](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile198.png>)

- • D3 = D3(A,B) = {e(A,B) > rµ(A,B,n)}


For D1 the conditions are mutually exclusive as e(A,B) can not be simultaneously greater than and less than or equal to c1µ(A,B,n). Thus D1(A,B) is empty. For D2 we get similar contradiction after a little work.

e(A,B)log µe((A,B,nA,B)) > c2(|A| ∨ |B|)log |A|∨|n B| e(A,B)log µe((A,B,nA,B)) > µ(A,B,n)r1 log r1

![image 199](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile199.png>)

![image 200](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile200.png>)

![image 201](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile201.png>)

µ(A,B,n) log µe((A,B,nA,B)) > r1 log r1

e(A,B)

![image 202](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile202.png>)

![image 203](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile203.png>)

e(A,B)

µ(A,B,n) > r1

![image 204](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile204.png>)

e(A,B) > r1µ(A,B,n) e(A,B) > rµ(A,B,n).

This is a contradiction so D2(A,B) is also empty.

Now we bound P(D3(A,B)). As e(A,B) is binomial with mean at most µ(A,B,n), Lemma A.2 implies

for any r ≥ 4.

P(D3(A,B)) ≤ exp −µ(|A|,|B3|,n)rlogr

![image 205](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile205.png>)

For all A,B we have D ⊂ D1 ∪ D2 ∪ D3 and P(D1(A,B)) = P(D2(A,B)) = 0. Combining this with (11) and (12) we get

P(D) ≤ P(∃A,B : D(A,B) occurs) ≤ P(∃A,B : |A|,|B| < n/e and D(A,B) occurs) + O(exp(−md)) ≤ P(∃A,B : |A|,|B| < n/e and D3(A,B) occurs) + O(exp(−md)) ≤

P(D3(A,B)) + O(exp(−md))

|A|,|B|

exp −µrlog3 r + O(exp(−md))

≤

![image 206](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile206.png>)

a,b |A|=a,|B|=b

n a

n b

exp −µ(a,b,n3)rlogr + O(exp(−md)),

≤

![image 207](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile207.png>)

a,b

where the sums are over all pairs (a,b) with d1/4/100 ≤ a ∨ b ≤ n/e. To evaluate the last term we get

µr log r

3 ≥ 6 + 400m (|A| ∨ |B|)log |A|∨|n B| > 2 + 2 + 2 + (400m)) (|A| ∨ |B|)log |A|∨|n B| > 2|A|(log |An|) + 2|B|(log |Bn|) + 2 log n + 4md1/4 log 100d n

![image 208](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile208.png>)

![image 209](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile209.png>)

![image 210](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile210.png>)

![image 211](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile211.png>)

![image 212](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile212.png>)

![image 213](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile213.png>)

1/4

> |A|(1 + log |An|) + |B|(1 + log |Bn|) + 2 log n + 3md1/4 log n.

![image 214](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile214.png>)

![image 215](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile215.png>)

The ﬁrst line is due to the deﬁnitions of r and c2. In the third line we use the monotonicity of xlog nx on [1,n/e] by substituting in |A|, |B|, 1 and d1/4/100 for x. In the fourth line we use that |A| ∨ |B| ≤ ne so log |An|,log |Bn| > 1

![image 216](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile216.png>)

![image 217](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile217.png>)

![image 218](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile218.png>)

![image 219](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile219.png>)

Exponentiating we get exp µrlog3 r ≥ | enA|

n

n

n2 exp(3md1/4(log n)) It follows that

en |B|

![image 220](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile220.png>)

![image 221](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile221.png>)

![image 222](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile222.png>)

n a

n b

n a

n b

−n n−2 exp(−3md1/4 log n) ≤ n−2 exp(−3md1/4 log n).

−n en b

exp −µ(a,b,n3)rlogr ≤

en a

![image 223](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile223.png>)

![image 224](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile224.png>)

![image 225](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile225.png>)

Putting this together we get P(D) ≤

n a

n b

exp −µ(a,b,n3)rlogr + O(exp(−md))

![image 226](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile226.png>)

d/100≤a∨b≤n/e

≤ n2n−2 exp(−3md1/4 log n) + O(exp(−md)). Thus the lemma is satisﬁed.

We ﬁnally give a quick sketch of how Proposition 5.2 follows from Lemma 5.1. This is nearly the same as Theorem 2.5 of [18], and so we will cite heavily. Proof of Proposition 5.2.

We recall that we wish to bound sup

√

![image 227](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile227.png>)

|xtAy| ≤ C

d.

x =1,xt1=0 y =1

For this we will relax the supremum to a ﬁnite, discrete space. Deﬁne U =

z 2√n

: z ∈ Zn, z 2 ≤ 4n and T = {z ∈ U : z ⊥ 1}.

![image 228](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile228.png>)

![image 229](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile229.png>)

As U is 12-net of the sphere, and S = {x : x = 1,xt1 = 0} is in the convex hull of T (by Lemma 2.3 of [18]), we have that

![image 230](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile230.png>)

|xtAy| ≤ 4 sup

|xtAy|.

sup

x =1,xt1=0 y =1

- x∈T
- y∈U


Further, we have that |T | ≤ |U| ≤ Cn for some absolute constant C.

For a ﬁxed pair of vectors (x,y) ∈ T × U, deﬁne the light couples L = L(x,y) to be all those ordered pairs (u,v) ∈ {1,2,...,n}2 so that |xuyv| ≤

√

![image 231](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile231.png>)

d

n , and let the heavy couples H = H(x,y) be all those pairs that are not light. We will use the notation

![image 232](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile232.png>)

xuAuvyv,

light(x,y) =

(u,v)∈L

and the notation

xuAuvyv,

heavy(x,y) =

(u,v)∈H

For the light couples, we recall Bernstein’s inequality, which says that for inde-

pendent, centered random variables {Xi}N1 such that |Xi| ≤ M almost surely for all 1 ≤ i ≤ N and all t ≥ 0,

N

Xi > t ≤ exp −t2 2 Ni=1 EXi2 + 32Mt

Pr

.

![image 233](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile233.png>)

![image 234](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile234.png>)

i=1

To realize light(x,y) as a sum of independent variables, we need to account for the symmetry in A. Let N be the number of undirected edges {u,v} so that either (u,v) or (v,u) appear in L. Enumerate these edges and deﬁne for i with 1 ≤ i ≤ N corresponding to {u,v},

Xi = (Auv − p)xuyv1 {(u,v) ∈ L} + (Auv − p)xvyu1 {(v,u) ∈ L}. For our purposes, it will be enough to use the bound

N

EXi2 ≤

i=1

N

2p (xuyv)2 + (xvyu)2 ≤ 2p

i=1

x2uyv2 ≤ 2p,

(u,v)

where we have used the normalization of the vectors. In summary, by Bernstein’s inequality,

Pr[|light(x,y) − Elight(x,y)| > t] ≤ exp −nt2 4d + 23

√

.

![image 235](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile235.png>)

![image 236](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile236.png>)

dt

![image 237](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile237.png>)

To control the expectation, note that on account of x ∈ T ,

Elight(x,y) + Eheavy(x,y) = 0 However,

√

np √

![image 238](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile238.png>)

d|xuyv|2 ≤

p|xuyv| ≤

|Eheavy(x,y)| ≤

d.

![image 239](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile239.png>)

![image 240](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile240.png>)

(u,v)∈H

(u,v)∈H

As T is only of cardinality eO(N), for each m there is a constant C = C(m) so that

√

![image 241](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile241.png>)

d ≤ Ce−mn.

|light(x,y)| > C

Pr sup

(x,y)∈T ×U

To control the heavy couples, we use the discrepancy property (c.f. Corollary 2.11 of [18] or Section 2.3 of [22]). The proof is nearly identical to either of those two claims, although it is not exactly either one, on account of the slightly altered deﬁnition of discrepancy.

Lemma 9.1. Suppose c1,c2,C1 are constants greater than 1 and d > 0. There is a constant C > 0 depending only on c1,c2,C1 so that for any graph with the property that all degrees are bounded by C1d and for all subsets A and B of vertices

- (1) µe((A,BA,B)) ≤ c1

![image 242](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile242.png>)

- (2) e(A,B)log µe((A,BA,B)) ≤ c2(|A| ∨ |B|)log |A|∨|n B|

![image 243](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile243.png>)

![image 244](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile244.png>)

- (3) |A| ∨ |B| ≤ d1/4/100


then for all x,y ∈ U

√

![image 245](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile245.png>)

|xuAu,vyv| ≤ C

d.

{u,v}∈H

By Lemma 5.1, all these conditions hold with the desired probability, and hence the proof of Proposition 5.2 is complete.

Proof of Lemma 9.1. We will partition the summands into blocks where each term xu or yv has approximately the same magnitude. Let γi = 2i, n∗ = ⌈log2 √n⌉ and put

![image 246](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile246.png>)

Ai = u γ

√i−n1 ≤ |xu| < γ

√in , 0 ≤ i ≤ n∗. Bi = u γ

![image 247](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile247.png>)

![image 248](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile248.png>)

![image 249](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile249.png>)

![image 250](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile250.png>)

√i−n1 ≤ |yu| < γ

√in , 0 ≤ i ≤ n∗. Let Hˆ denote those pairs (i,j) so that γiγj ≥

![image 251](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile251.png>)

![image 252](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile252.png>)

![image 253](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile253.png>)

![image 254](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile254.png>)

√

![image 255](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile255.png>)

d. The contribution of the absolute sum can, in these terms, be bounded by

γiγj n

|xuAu,vyv| ≤

e(Ai,Bj).

![image 256](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile256.png>)

(i,j)∈Hˆ

(u,v)∈H

In what follows, we will bound the contribution of the summands where |Ai| ≥ |Bj|. By symmetry, the contribution of the other summands will have the same bound. The heavy couples will now be partitioned into 6 classes {Hˆi}6i=1 where their contribution is bounded in a diﬀerent way. Let Hˆi ⊆ Hˆ be those pairs (i,j) which satisfy the ith property from the following list but none of the prior properties:

- (1) |Ai| < d1/4/100.
- (2) µe((AAi,Bj)

![image 257](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile257.png>)

i,Bj) ≤ c1γ√iγdj .

![image 258](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile258.png>)

![image 259](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile259.png>)

- (3) γj > 41

![image 260](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile260.png>)

√

![image 261](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile261.png>)

dγi.

- (4) log µe((AAi,Bj)

![image 262](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile262.png>)

i,Bj) > 12 log |An

![image 263](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile263.png>)

![image 264](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile264.png>)

i|.

- (5) |An

![image 265](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile265.png>)

i| > γi4.

- (6) |An


i| ≤ γi4.

![image 266](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile266.png>)

Bounding the contribution of Hˆ1. For these terms, we have that e(Ai,Bj) ≤ |Ai||Bj| ≤

√

![image 267](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile267.png>)

d

10000. Hence

![image 268](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile268.png>)

√

√

n∗

![image 269](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile269.png>)

![image 270](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile270.png>)

γiγj n

d 10000 ≤

d 10000

γiγj n

16

e(Ai,Bj) ≤

,

![image 271](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile271.png>)

![image 272](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile272.png>)

![image 273](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile273.png>)

![image 274](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile274.png>)

i,j=0

(i,j)∈Hˆ1

i=0 2i ≤ 4√n.

∗

where in the last line we have used that n

![image 275](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile275.png>)

Bounding the contribution of Hˆ2. Applying the bound directly to the sum, we have that

√

γi2γj2 n

γi2γj2 n

|Ai||Bj| n

γiγj n

![image 276](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile276.png>)

√

e(Ai,Bj) ≤ c1

d

.

µ(Ai,Bj) = c1

![image 277](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile277.png>)

![image 278](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile278.png>)

![image 279](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile279.png>)

![image 280](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile280.png>)

![image 281](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile281.png>)

d

(i,j)∈Hˆ2

(i,j)∈Hˆ2

(i,j)∈Hˆ2

Further,

n∗

n

γi2|Ai| n ≤ 4

|xu|2 ≤ 4,

![image 282](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile282.png>)

u=1

i=0

and the same bound holds for the sum over |Bj|. Hence

n∗

√

√

γi2γj2 n

|Ai||Bj| n

γiγj n

![image 283](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile283.png>)

![image 284](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile284.png>)

e(Ai,Bj) ≤ c1

= 16c1

d

d.

![image 285](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile285.png>)

![image 286](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile286.png>)

![image 287](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile287.png>)

i,j=0

(i,j)∈Hˆ2

Bounding the contribution of Hˆ3. By the bound on the degrees, we have that e(Ai,Bj) ≤ C1|Bj|d. Hence

γiγj n |Bj|.

γiγj n

e(Ai,Bj) ≤ C1d

![image 288](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile288.png>)

![image 289](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile289.png>)

(i,j)∈Hˆ3

(i,j)∈Hˆ3

√

![image 290](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile290.png>)

Since γi < 4γj/

d, upon summing over all possible i, we get that for ﬁxed j

Therefore,

8γj √

γi ≤

.

![image 291](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile291.png>)

![image 292](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile292.png>)

d

i:(i,j)∈Hˆ3

√

γiγj n

![image 293](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile293.png>)

e(Ai,Bj) ≤ C1

d

![image 294](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile294.png>)

(i,j)∈Hˆ3

n∗

√

8γj2 n |Bj| ≤ 32C1

![image 295](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile295.png>)

d.

![image 296](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile296.png>)

j=0

Bounding the contribution of Hˆ4. As we are not in Hˆ1 or Hˆ2, it must be that (i,j) ∈ Hˆ4 satisfy the second discrepancy condition, that is

i| ≤ e(Ai,Bj)log µe((AAi,Bj)

- 1

![image 297](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile297.png>)

- 2e(Ai,Bj)log |An


i,Bj) ≤ c2|Ai|log |An

i|. Hence, applying this bound and summing over all j so that γj ≤ 41

![image 298](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile298.png>)

![image 299](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile299.png>)

![image 300](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile300.png>)

√

![image 301](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile301.png>)

dγi,

![image 302](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile302.png>)

n∗

√

√

γi2|Ai|

γiγj n

![image 303](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile303.png>)

![image 304](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile304.png>)

e(Ai,Bj) ≤ c2

n ≤ 4c2

d

d.

![image 305](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile305.png>)

![image 306](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile306.png>)

i=0

(i,j)∈Hˆ4

Bounding the contribution of Hˆ5. For (i,j) ∈ Hˆ5 we have e(Ai,Bj) ≤ µ(Ai,Bj) |A n

−1/2

1/2

≤ d|Bj|γi−2 Hence,

= d|Bj| |A n

![image 307](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile307.png>)

![image 308](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile308.png>)

i|

i|

n∗

√

dγj2|Bj| nγiγj ≤

dγj2|Bj| n ≤ 8

γiγj n

2 √

![image 309](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile309.png>)

e(Ai,Bj) ≤

d,

![image 310](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile310.png>)

![image 311](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile311.png>)

![image 312](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile312.png>)

![image 313](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile313.png>)

![image 314](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile314.png>)

d

j=0

(i,j)∈Hˆ5

(i,j)∈Hˆ5

where we have used in the penultimate bound that the sum over i is dominated by the series

2γj √

1 γi ≤

.

![image 315](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile315.png>)

![image 316](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile316.png>)

![image 317](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile317.png>)

d

√

![image 318](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile318.png>)

d≤γjγi

i:

Bounding the contribution of Hˆ6. For (i,j) ∈ Hˆ6, we have that e(Ai,Bj)log c1√γidγj ≤ e(Ai,Bj)log µe((AAi,Bj) i,Bj) ≤ c2|Ai|log |An

i| ≤ 4c2|Ai|logγi This brings us to the bound

![image 319](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile319.png>)

![image 320](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile320.png>)

![image 321](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile321.png>)

![image 322](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile322.png>)

γi|Ai|log γi n

γj log(c1γiγj) − log

γiγj n

√

e(Ai,Bj) ≤ 4c2 ·

.

![image 323](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile323.png>)

![image 324](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile324.png>)

![image 325](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile325.png>)

![image 326](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile326.png>)

d

(i,j)∈Hˆ6

(i,j)∈Hˆ6

√

![image 327](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile327.png>)

dγi and such that γjγi ≥

The sum in j only runs over those terms such that 4γj ≤

√

√

![image 328](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile328.png>)

![image 329](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile329.png>)

d. For j such that γj ≤ γi

d/(1 + log(γi)) we bound the sum over j by

√

![image 330](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile330.png>)

γj log(c1γiγj) − log

2γi

γj log c1 ≤

d (log c1)(1 + log γi)

√

d ≤

.

![image 331](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile331.png>)

![image 332](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile332.png>)

![image 333](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile333.png>)

![image 334](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile334.png>)

j

j

For larger j, we bound the sum by

√

![image 335](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile335.png>)

γi

γj log c1γi2 − log(1 + log γi) ≤

γj log(c1γiγj) − log

d 2(log c1)(log γi)

√

d ≤

,

![image 336](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile336.png>)

![image 337](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile337.png>)

![image 338](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile338.png>)

![image 339](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile339.png>)

j

j

having applied the inequality log(1 + x) ≤ x. Hence, we conclude that

√

√

![image 340](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile340.png>)

![image 341](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile341.png>)

γi2|Ai| n ≤

γiγj n

d log c1 ·

d log c1

10c2

40c2

e(Ai,Bj) ≤

.

![image 342](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile342.png>)

![image 343](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile343.png>)

![image 344](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile344.png>)

![image 345](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile345.png>)

(i,j)∈Hˆ6

(i,j)∈Hˆ6

A. Estimates of Binomial Random Variables

- Lemma A.1. Let X be a binomial random variable with mean µ. Then for any t ≤ µ


P [X ≤ t] ≤ exp −µ + t(1 + log µt ) ,

![image 346](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile346.png>)

- Proof of Lemma A.1. The proof follows from a standard estimate on the Laplace transform combined with Markov’s inequality. For any λ ∈ R, the Laplace transform of X ∼ Binomial(n,p) can be bounded by


EeλX = peλ + (1 − p) n = 1 + p(eλ − 1) n ≤ exp µ(eλ − 1) .

Provided that λ < 0, the tail bound now can be bounded by Markov’s inequality by

P [X ≤ t] = P eλX ≥ eλt ≤ EeλX e−λt ≤ exp µ(eλ − 1) − λt .

Assuming that t < µ, this bound holds with λ = log(t/µ), which upon evaluation gives

P [X ≤ t] ≤ exp µ(elog(t/µ) − 1) − log(t/µ)t = exp −µ + t(1 + log µt ) .

![image 347](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile347.png>)

- Lemma A.2. Let X be a binomial random variable with mean µ. Then for any t > 4


tµlog(t) 3

P [X ≥ tµ] ≤ exp −

,

![image 348](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile348.png>)

- Proof of Lemma A.2. The proof here is identical in approach to the proof of Lemma A.1. As there, it is possible to bound the Laplace transform of X as


EeλX ≤ exp µ(eλ − 1) , for any real λ. For λ > 0, the tail bound follows from Markov’s inequality by

P [X ≥ tµ] = P eλX ≥ eλtµ ≤ EeλX e−λtµ ≤ exp µ(eλ − 1) − λtµ .

For t > 1, it is possible to take λ = log t. This gives the bound on the tail probability P [X ≥ tµ] ≤ exp[µ(t − 1 − tlog t)].

To complete the proof, it remains to show that t − 1 ≤ 32tlog t when t ≥ 4. The function t−t1 log t is monotonically increasing for t > 1, and thus it suﬃces to show that 34 log 4 ≥ 23, or equivalently that log 4 ≥ 98. This follows from log 4 = 1 4 x1dx and bounding the integral from below by a right Riemann sum.

![image 349](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile349.png>)

![image 350](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile350.png>)

![image 351](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile351.png>)

![image 352](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile352.png>)

![image 353](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile353.png>)

![image 354](<2012-hoffman-spectral-gaps-random-graphs_images/imageFile354.png>)

References

- [1] Sylwia Antoniuk, Tomasz Łuczak, and Jacek Światkowski. Random triangular groups at density 1/3. Compositio Mathematica, 151(1):167–178, 2015.
- [2] Eric Babson, Christopher Hoﬀman, and Matthew Kahle. The fundamental group of random 2-complexes. J. Amer. Math. Soc., 24(1):1–28, 2011.
- [3] W. Ballmann and J. Świ ‘

atkowski. On L2-cohomology and property (T) for automorphism groups of polyhedral cell complexes. Geom. Funct. Anal., 7(4):615–645, 1997.

- [4] Bachir Bekka, Pierre de la Harpe, and Alain Valette. Kazhdan’s property (T), volume 11 of New Mathematical Monographs. Cambridge University Press, Cambridge, 2008.
- [5] Florent Benaych-Georges, Charles Bordenave, and Antti Knowles. Largest eigenvalues of sparse inhomogeneous erd\h {o} sr\’enyi graphs. arXiv preprint arXiv:1704.02953, 2017.
- [6] Florent Benaych-Georges, Charles Bordenave, and Antti Knowles. Spectral radii of sparse random matrices. arXiv preprint arXiv:1704.02945, 2017.
- [7] Itai Benjamini, Simi Haber, Michael Krivelevich, and Eyal Lubetzky. The isoperimetric constant of the random graph process. Random Structures Algorithms, 32(1):101–114, 2008.
- [8] Fan Chung, Linyuan Lu, and Van Vu. The spectra of random graphs with given expected degrees. Internet Math., 1(3):257–275, 2004.


- [9] Fan Chung and Mary Radcliﬀe. On the spectra of general random graphs. Electron. J. Combin., 18(1):Paper 215, 14, 2011.
- [10] Fan R. K. Chung. Spectral graph theory, volume 92 of CBMS Regional Conference Series in Mathematics. Published for the Conference Board of the Mathematical Sciences, Washington, DC, 1997.
- [11] D. Cohen, A. Costa, M. Farber, and T. Kappeler. Topology of random 2-complexes. Discrete Comput. Geom., 47(1):117–149, 2012.
- [12] Amin Coja-Oghlan. On the Laplacian eigenvalues of Gn,p. Combin. Probab. Comput., 16(6):923–946, 2007.
- [13] AE Costa and Michael Farber. The asphericity of random 2-dimensional complexes. Random Structures & Algorithms, 46(2):261–273, 2015.
- [14] AE Costa and Michael Farber. Geometry and topology of random 2-complexes. Israel Journal of Mathematics, 209(2):883–927, 2015.
- [15] Michael W. Davis and Matthew Kahle. Random graph products of ﬁnite groups are rational duality groups. J. Topol., 7(2):589–606, 2014.
- [16] Jian Ding, Jeong Han Kim, Eyal Lubetzky, and Yuval Peres. Anatomy of a young giant component in the random graph. Random Structures & Algorithms, 39(2):139–178, 2011.
- [17] László Erdős, Antti Knowles, Horng-Tzer Yau, and Jun Yin. Spectral statistics of Erdős-Rényi Graphs II: Eigenvalue spacing and the extreme eigenvalues. Comm. Math. Phys., 314(3):587– 640, 2012.
- [18] Uriel Feige and Eran Ofek. Spectral techniques applied to sparse random graphs. Random Structures Algorithms, 27(2):251–275, 2005.
- [19] N. Fountoulakis and B.A. Reed. The evolution of the mixing rate of a simple random walk on the giant component of a random graph. Random Structures & Algorithms, 33(1):68–86, 2008.
- [20] Jacob Fox, Mikhail Gromov, Vincent Laﬀorgue, Assaf Naor, and János Pach. Overlap properties of geometric expanders. J. Reine Angew. Math., 671:49–83, 2012.
- [21] Ehud Friedgut and Gil Kalai. Every monotone graph property has a sharp threshold. Proceedings of the American mathematical Society, 124(10):2993–3002, 1996.
- [22] J. Friedman, J. Kahn, and E. Szemerédi. On the second eigenvalue of random regular graphs. In Proceedings of the twenty-ﬁrst annual ACM symposium on Theory of computing, STOC ’89, pages 587–598, New York, NY, USA, 1989. ACM.
- [23] Z. Füredi and J. Komlós. The eigenvalues of random symmetric matrices. Combinatorica, 1(3):233–241, 1981.
- [24] Howard Garland. p-adic curvature and the cohomology of discrete subgroups of p-adic groups. Ann. of Math. (2), 97:375–423, 1973.
- [25] Eli Glasner. Ergodic theory via joinings, volume 101 of Mathematical Surveys and Monographs. American Mathematical Society, Providence, RI, 2003.
- [26] Mikhail Gromov. Singularities, expanders and topology of maps. I. Homology versus volume in the spaces of cycles. Geom. Funct. Anal., 19(3):743–841, 2009.
- [27] Mikhail Gromov. Singularities, expanders and topology of maps. Part 2: From combinatorics to topology via algebraic isoperimetry. Geom. Funct. Anal., 20(2):416–526, 2010.
- [28] Anna Gundert and Uli Wagner. On Laplacians of random complexes. In Computational geometry (SCG’12), pages 151–160. ACM, New York, 2012.
- [29] Allen Hatcher. Algebraic topology. Cambridge University Press, Cambridge, New York, 2002. Autre(s) tirage(s) : 2003,2004,2005,2006.
- [30] Christopher Hoﬀman, Matthew Kahle, and Elliot Paquette. The threshold for integer homology in random d-complexes. Discrete & Computational Geometry, 57(4):810–823, 2017.
- [31] Svante Janson, Donald E Knuth, Tomasz Łuczak, and Boris Pittel. The birth of the giant component. Random Structures & Algorithms, 4(3):233–358, 1993.
- [32] Matthew Kahle. Topology of random clique complexes. Discrete Math., 309(6):1658–1671, 2009.
- [33] Matthew Kahle. Sharp vanishing thresholds for cohomology of random ﬂag complexes. Ann. of Math. (2), 179(3):1085–1107, 2014.
- [34] Can M Le, Elizaveta Levina, and Roman Vershynin. Concentration and regularization of random graphs. Random Structures & Algorithms, 51(3):538–561, 2017.
- [35] Nathan Linial and Roy Meshulam. Homological connectivity of random 2-complexes. Combinatorica, 26(4):475–487, 2006.


- [36] Nathan Linial and Yuval Peled. On the phase transition in random simplicial complexes. Ann. of Math. (2), 184(3):745–773, 2016.
- [37] Tomasz Łuczak and Yuval Peled. Integral homology of random simplicial complexes. Discrete & Computational Geometry, 59(1):131–142, 2018.
- [38] G. A. Margulis. Explicit constructions of expanders. Problemy Peredači Informacii, 9(4):71– 80, 1973.
- [39] R. Meshulam and N. Wallach. Homological connectivity of random k-dimensional complexes. Random Structures Algorithms, 34(3):408–417, 2009.
- [40] János Pach. A Tverberg-type result on multicolored simplices. Comput. Geom., 10(2):71–76, 1998.
- [41] Ori Parzanchevski, Ron Rosenthal, and Ran J Tessler. Isoperimetric inequalities in simplicial complexes. Combinatorica, 36(2):195–227, 2016.
- [42] Nathan Ross. Fundamentals of Stein’s method. Probab. Surv., 8:210–293, 2011.
- [43] Van H. Vu. Spectral norm of random matrices. Combinatorica, 27(6):721–736, 2007.
- [44] Eugene P. Wigner. On the distribution of the roots of certain symmetric matrices. Ann. of Math. (2), 67:325–327, 1958.
- [45] Andrzej Żuk. La propriété (T) de Kazhdan pour les groupes agissant sur les polyèdres. C. R. Acad. Sci. Paris Sér. I Math., 323(5):453–458, 1996.
- [46] Andrzej Żuk. Property (T) and Kazhdan constants for discrete groups. Geom. Funct. Anal., 13(3):643–670, 2003.


Department of Mathematics, University of Washington E-mail address: hoffman@math.washington.edu

Department of Mathematics, The Ohio State University E-mail address: mkahle@math.osu.edu

Department of Mathematics, The Ohio State University E-mail address: paquette.30@osu.edu

