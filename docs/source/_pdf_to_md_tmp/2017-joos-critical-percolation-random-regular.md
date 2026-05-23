arXiv:1703.03639v3[math.CO]17Jan2018

CRITICAL PERCOLATION ON RANDOM REGULAR GRAPHS

FELIX JOOS AND GUILLEM PERARNAU

Abstract. We show that for all d ∈ {3, . . . , n − 1} the size of the largest component of a random d-regular graph on n vertices around the percolation threshold p = 1/(d−1) is Θ(n2/3), with high probability. This extends known results for ﬁxed d ≥ 3 and for d = n − 1, conﬁrming a prediction of Nachmias and Peres on a question of Benjamini. As a corollary, for the largest component of the percolated random d-regular graph, we also determine the diameter and the mixing time of the lazy random walk. In contrast to previous approaches, our proof is based on a simple application of the switching method.

1. Introduction

For every d ∈ {3,... ,n − 1}, let Gn,d be the set of all simple and vertex-labelled d-regular graphs on n vertices and let Gn,d be a graph chosen uniformly at random from Gn,d. For p ∈ [0,1], let Gn,d,p be a graph obtained from Gn,d by retaining each edge independently with probability p. The goal of this paper is to study the order of the largest component of Gn,d,p, denoted by L1(Gn,d,p), in terms of n,d and p.

Most of the literature in the area focuses either on ﬁxed d ≥ 3 or on d = n − 1. Goerdt [8] showed the existence of a critical probability, pcrit := 1/(d − 1), such that for every ﬁxed d ≥ 3 and every ǫ > 0 the following holds with probability 1 − o(1): if p ≤ (1 − ǫ)pcrit, then L1(Gn,d,p) = O(log n), while if p ≥ (1 + ǫ)pcrit, then L1(Gn,d,p) = Θ(n). Similar results were also obtained in a more general setting by Alon, Benjamini and Stacey [1]. For d = n − 1, the random graph Gn,d,p corresponds to the classic Erd˝os-Re´nyi random graph Gn,p. In their seminal paper [5], Erd˝os and Re´nyi proved that for every ǫ > 0, the following holds with probability 1 − o(1): if p ≤ (1 − ǫ)/n, then the largest component of Gn,p has order O(log n), if p = 1/n (critical probability), then it has order Θ(n2/3), while if p ≥ (1 + ǫ)/n, then it has linear order.

Both for ﬁxed d ≥ 3 and for d = n − 1, the behaviour around the critical probability has attracted a lot of interest. It is well established that the critical window in Gn,p around p = 1/n is of order n−1/3 (see e.g. [21]). More precise estimates can be found in [14]. Benjamini posed the problem of determining the width of the critical window in Gn,d,p around pcrit = 1/(d − 1) (see [20, 22]). Nachmias and Peres [20] and Pittel [22], independently showed that the critical window exhibits mean-ﬁeld behaviour for ﬁxed d ≥ 3, namely, the following holds with probability 1 − o(1): for every ﬁxed λ ∈ R, if p = 1+λnd−−11/3, then L1(Gn,d,p) = Θ(n2/3). See also Riordan [23] for more precise results on L1(Gn,d,p) in the critical window.

![image 1](<2017-joos-critical-percolation-random-regular_images/imageFile1.png>)

The case when d is an arbitrary function of n is much less understood. It follows from existing results in the literature1 that for every d ∈ {3,... ,n−1}, the critical probability for the existence of a linear order component in Gn,d,p is 1/(d − 1). Results inside the critical window for given d-regular graphs have also been obtained in the context of transitive graphs under the ﬁnite triangle condition [4] or under certain expansion conditions [18].

Finally, similar results have been obtained for irregular degree sequences whenever the average degree is bounded by a constant [3, 6, 7, 10].

In view that both the sparse regime (ﬁxed d ≥ 3) and the densest one (d = n − 1) exhibit similar properties, Nachmias and Peres [20] suggested that the mean-ﬁeld behaviour extends to

![image 2](<2017-joos-critical-percolation-random-regular_images/imageFile2.png>)

The ﬁrst author was supported by the EPSRC, grant no. EP/M009408/1.

1The non-existence of a linear order component when p ≤ (1 − ǫ)pcrit follows from Proposition 1 in [20]. The existence of a linear order component when p ≥ (1 + ǫ)pcrit follows from the expansion properties of Gn,d (see Corollary 2.8 in [13]) and the results on (n, d, λ)−graphs in [12].

1

every d ∈ {3,... ,n − 1}. In this paper we conﬁrm this prediction in the critical window and thus answer the question posed by Benjamini for all d ∈ {3,... ,n − 1}.

Theorem 1. Suppose λ ∈ R and d,n ∈ N such that 3 ≤ d ≤ n − 1 and n is suﬃciently large. Let p = 1+λnd−−11/3. Then for every suﬃciently large A = A(λ), we have

![image 3](<2017-joos-critical-percolation-random-regular_images/imageFile3.png>)

P[L1(Gn,d,p) ∈/ [A−1n2/3,An2/3]] ≤ 20A−1/2 .

The upper bound in Theorem 1 directly follows from the upper bound for d-regular graphs in Proposition 1 in [20]. The proof of the lower bound is more intricate and we devote the rest of the paper to it.

Most of the previous work on the component structure of Gn,d,p uses the conﬁguration model introduced by Bollob´s in [2]. The conﬁguration model, denoted by G∗n,d, is a model of random d-regular multigraphs on n vertices. Conditional on G∗n,d being simple, one obtains the uniform distribution on Gn,d. It is well-known (see for example [24]) that

P[G∗n,d simple] = e−Ω(d2) . (1)

While P[G∗n,d simple] is constant for ﬁxed d ≥ 3, it quickly tends to 0 if d grows with n, and new ideas are needed to study Gn,d. A standard tool to estimate probabilities for Gn,d when d grows with n is the switching method, introduced by McKay in [16]. For instance, this method has been used to estimate (1) for d = o(√n) [17] or to determine several combinatorial properties of Gn,d when d grows with n [13].

![image 4](<2017-joos-critical-percolation-random-regular_images/imageFile4.png>)

The proof of the lower bound in Theorem 1 is based on the analysis of an exploration process in Gn,d,p using the switching method. The central quantity that we track through the process is the number of edges between the explored and unexplored parts of the graph, denoted by Xt. Our proof relies on sharp estimations of the ﬁrst and second moments of Xt.

This approach is inspired by recent developments of the switching method for the study of the component structure of random graphs with a given degree sequence [7, 11]. We take this opportunity to illustrate the use of our method with a simple proof that makes no assumptions on d.

The critical window. Theorem 1 shows that the critical window has width Ω(n−1/3). Proposition 1 in [20] implies that, as λ → −∞, the typical order of the largest component is o(n2/3). Following analogous ideas as the ones used in the proof of Theorem 1, one obtains that, as λ → ∞, the typical order of the largest component is ω(n2/3). More precisely, there exist

constants c,C > 0 such that for every 3 ≤ d ≤ n − 1 and λ > 0, if p = 1+λnd−−11/3, then P L1(Gn,d,p) ≤ c · λn2/3 ≤ Cλ−1 .

![image 5](<2017-joos-critical-percolation-random-regular_images/imageFile5.png>)

The proof of this statement is simpler than the proof of our main theorem, since the assumption λ > 0 implies that Xt has positive drift. In particular, the ﬁrst part of the exploration process can be analysed using a ﬁrst moment argument only and for the entire process it suﬃces to control the variance of Xt from above. It follows that the width of the critical window is Θ(n−1/3).

In its current form, our method does not give sharp estimates for L1(Gn,d,p) in the barely subcritical and barely supercritical regimes. However, we believe that similar estimates as the ones in Lemma 6 hold in general and may be used to extend the results of Nachmias and Peres in [20] to all d ∈ {3,... ,n − 1}.

Diameter and Mixing Time. We present a consequence of Theorem 1. For a component C, let diam(C) denote its diameter and let Tmix(C) denote the mixing time of the lazy random walk on C. Theorem 1.2 in [19] implies the following corollary.

Corollary 2. Suppose λ ∈ R and d,n ∈ N such that 3 ≤ d ≤ n − 1 and n is suﬃciently large. Let p = 1+λnd−−11/3. Let C be the largest component of Gn,d,p. Then, for every ǫ > 0, there exists A = A(λ,ǫ) such that

![image 6](<2017-joos-critical-percolation-random-regular_images/imageFile6.png>)

P[diam(C) ∈/ [A−1n1/3,An1/3]] < ǫ .

and

P[Tmix(C) ∈/ [A−1n,An]] < ǫ .

Organisation of the paper. The paper is organized as follows. In Section 2, we describe our exploration process of Gn,d,p and introduce diﬀerent quantities we will track during the process. In Section 3, we present our main combinatorial tool (switching method) and prove two technical lemmas. In Section 4, we use these lemmas to study a single step of the exploration process. Finally, in Section 5, we conclude with the proof of the lower bound in Theorem 1.

2. The exploration process

Before describing the exploration process, we brieﬂy introduce some notation. For a graph G, a subset of vertices X of G, and a vertex u of G, we write dG(u) for the number of neighbours of u in G and dG,X(u) for the number of neighbours of u in G that belong to X. We also write ∆(G) for the maximum degree of G. Finally, for p ∈ [0,1], we write Gp for the graph where each edge in G is independently retained with probability p.

We will use an exploration process to reveal the component structure of Gn,d,p. Let us denote the vertex set by V , which we equip with a linear order (from now on V is always a vertex set of size n). For technical reasons, we perform our exploration process not on Gn,d,p, but on what we call an input. An input is a tuple (G,S), where G ∈ Gn,d and S = {σv}v∈V is a collection of n permutations of length d. For each vertex of G, arbitrarily label the edges incident to it with distinct elements from {1,... ,d}. Thus every edge receives two labels. In fact, we may think about this as a labelling of the semi-edges of G. Let I be the set of all inputs (G,S) where G ∈ Gn,d and S is a collection of n permutations of length d. Observe that every graph in G ∈ Gn,d gives rise to exactly (d!)n inputs. Thus, choosing an input uniformly at random from I and ignoring the edge-labels is equivalent to choosing Gn,d. Let Sn,d be a collection of n permutations of length d each chosen independently and uniformly at random. Hence, if an input is chosen uniformly at random from I, then this input is distributed as (Gn,d,Sn,d).

Next, we describe our exploration process on an input (G,S). First, for every uv ∈ E(G), we denote by I(uv) the indicator random variable that is 1 if uv belongs to Gp (it percolates) and

- 0 otherwise. If I(uv) is revealed, we say that the edge uv has been exposed. For each integer


- t ≥ 0, the set St consists of the vertices explored up to time t (with S0 = ∅); the bipartite graph Ft, with bipartition (St,V \ St), consists of all edges in G between St and V \ St that have been exposed and have failed to percolate; and the graph Ht, with vertex set St, consists of all edges in G within St, that is, Ht := G[St]. Let Ht be the history of all random choices we make until time t (which we will treat as an event).


We now describe how to obtain Ht+1, given Ht. Suppose there exists at least one vertex u ∈ St such that dHt(u) + dFt(u) < d. Among all such vertices u, let vt+1 be the vertex which comes ﬁrst in the linear order of V . Let wt+1 be the vertex w ∈ V \St with vt+1w ∈ E(G)\E(Ft) that minimizes σvt+1(ℓ(w)), where ℓ(w) is the label of the semi-edge incident to vt+1 that corresponds to vt+1w. Thereafter, we expose vt+1wt+1. If I(vt+1wt+1) = 0, then we set St+1 := St, Yt+1 := 0, Zt+1 := 0 and we let Ft+1 be the graph obtained from Ft by adding vt+1wt+1. If I(vt+1wt+1) = 1, then we set

St+1 := St ∪ {wt+1}, Yt+1 := dFt(wt+1), Zt+1 := dG,St(wt+1) − Yt+1 − 1,

and we let Ft+1 be the graph obtained from Ft by deleting all edges incident to wt+1 and moving wt+1 to the other side of the bipartition. Since Ht+1 = G[St+1], we also reveal all the edges between wt+1 and St. Observe that Zt+1 counts the number of neighbours of wt+1 in St \{vt+1} whose corresponding edge has not yet been exposed.

If dHt(u) + dFt(u) = d for all u ∈ St, that is, every edge incident to a vertex in St has been exposed, then we pick a vertex x ∈ V \ St that minimises dFt(x) and set wt+1 := x, St+1 := St ∪ {wt+1}, Yt+1 := dFt(wt+1), Zt+1 := 0 and we let Ft+1 be the graph obtained from Ft by deleting all edges incident to wt+1 and by moving wt+1 to the other side of the bipartition. Observe that, in any of the above-mentioned cases, |E(Ft+1)| ≤ |E(Ft)| + 1 and hence |E(Ft)| ≤ t.

A crucial parameter of our exploration process is the number of edges between St and V \ St which have not yet been exposed:

(d − dHt(u) − dFt(u)) .

Xt :=

u∈St

For the sake of simplicity, we deﬁne ηt+1 := Xt+1 − Xt. If Xt > 0, then

ηt+1 = −(1 − I(vt+1wt+1)) + I(vt+1wt+1)(d − 2 − Yt+1 − 2Zt+1) , (2) and if Xt = 0, then

ηt+1 = d − Yt+1 . (3)

Note that Yt+1 and Zt+1 are measurable random variables given Ht and thus ηt+1 is a predictable sequence with respect to Ht.

3. The switching method and some applications

In this section we explain the switching method and we present two simple applications. In Lemma 3 we use the switching method to bound the probability from above that two vertices are adjacent. In Lemma 4 we provide an upper bound on the expectation of the number of neighbours of a vertex in a speciﬁed set of vertices.

Let G be a graph and let x1,x2,x3,x4 be distinct vertices of G. Suppose x1x2,x3x4 ∈ E(G) and x1x4,x2x3 ∈/ E(G). A switching on the 4-cycle x1x2x3x4 transforms G into a graph G′ by deleting x1x2,x3x4 and adding x1x4,x2x3. Observe that the degree sequence of G is preserved by the switching. In particular, if G is d-regular, then so is G′. Moreover, the switching operation is reversible: if G can be transformed into G′ by a switching, then G can be also obtained from G′ by a switching on the same 4-cycle. Finally, there is a natural way to extend the notion of a switching from graphs to inputs by simply preserving the labels on each semi-edge.

Switchings can be used to obtain bounds on the probability that Gn,d satisﬁes a certain property. Suppose A,B are disjoint subsets of Gn,d. Suppose that for every graph G ∈ A, there are at least a switchings that transform G into a graph in B and for every graph G′ ∈ B, there are at most b switchings that transform G′ into a graph in A. By double-counting the number of switchings between A and B, we obtain a|A| ≤ b|B|. Thus aP[A] ≤ bP[B], where we deﬁne P[S] := |S|/|Gn,d| for every S ⊆ Gn,d.

- Lemma 3. Suppose d,n ∈ N such that 3 ≤ d ≤ n/4 and S ⊆ V such that |S| ≤ n/6. Let H be a graph with vertex set S and let F be a bipartite graph with vertex partition (S,V \ S) with


- ∆(F ∪ H) ≤ d. Let u ∈ S and v ∈ V \ S such that uv ∈/ E(F). Then


6(d − dH(u) − dF(u)) n

P[uv ∈ E(Gn,d) | Gn,d[S] = H, F ⊆ Gn,d] ≤

.

![image 7](<2017-joos-critical-percolation-random-regular_images/imageFile7.png>)

Proof. Let F+ be the set of graphs G ∈ Gn,d such that G[S] = H, F ⊆ G and uv ∈ E(G), and let F− be the set of graphs G ∈ Gn,d such that G[S] = H, F ⊆ G but uv ∈/ E(G). We will only perform switchings that involve edges and non-edges that are not contained in E(H) ∪ E(F). This ensures that the graph G′ obtained from a switching also satisﬁes G′[S] = H and F ⊆ G′.

Suppose G ∈ F+. In order to bound the number of switchings from below it suﬃces to switch on a cycle uvxy that satisﬁes xy ∈ E(G), uy,vx ∈/ E(G), and x,y ∈ V \ S. There are at least dn − 2d|S| ordered edges xy with both endpoints in V \ S. There are at most d2 edges xy such that x is at distance at most 1 from v and at most d2 edges xy such that y is at distance at most

- 1 from u. Thus, there are at least dn − 2d|S| − 2d2 ≥ dn/6 switchings that transform G into a graph in F−. Suppose now G ∈ F−. Then there are clearly at most d · (d − dH(u) − dF(u))


switchings that transform G into a graph in F+. It follows that P[uv ∈ E(Gn,d) | Gn,d[S] = H, F ⊆ Gn,d] ≤

d(d − dH(u) − dF(u))

dn/6 · P[uv ∈/ E(Gn,d) | Gn,d[S] = H, F ⊆ Gn,d] ≤

![image 8](<2017-joos-critical-percolation-random-regular_images/imageFile8.png>)

6(d − dH(u) − dF(u)) n

.

![image 9](<2017-joos-critical-percolation-random-regular_images/imageFile9.png>)

- Lemma 4. Suppose d,n ∈ N such that 3 ≤ d ≤ n/4 and S ⊆ V such that |S| ≤ n/6. Let H be a graph with vertex set S and let F be a bipartite graph with vertex partition (S,V \ S) with

- ∆(F ∪ H) ≤ d. Let v ∈ V \ S. Then E[dG,S(v) − dF(v) | Gn,d[S] = H, F ⊆ Gn,d] ≤ 6d|S|/n.


Proof. For every k ≥ 0, let Fk be the set of graphs G ∈ Gn,d such that G[S] = H, F ⊆ G, and dG,S(v)−dF(v) = k. As in Lemma 3, we will only perform switchings using edges and non-edges that are not contained in E(H) ∪ E(F).

Consider a graph in Fk. There are at most (d − dF(v)) · d|S| ≤ d2|S| switchings that lead to a graph in Fk+1. For every graph in Fk+1, we can use a switching on a cycle uvxy that satisﬁes uv,xy ∈ E(G) \ E(F), uy,vx ∈/ E(G) and u ∈ S, and v,x,y ∈ V \ S. There are k + 1 choices for uv and, for any particular choice of uv, there are at least dn − 2d|S| − 2d2 ≥ dn/6 choices for the (ordered) edge xy. Hence, there are at least (k + 1)dn/6 switchings that lead to a graph in Fk. Thus, for every k ≥ 0, we obtain

P[Fk+1] ≤

6d|S|/n (k + 1) · P[Fk] . (4)

![image 10](<2017-joos-critical-percolation-random-regular_images/imageFile10.png>)

Let X be a Poisson distributed random variable with mean 6d|S|/n. Lemma 3.4 in [15] together with (4) implies that for every m ≥ 0

P[dG,S(v) − dF(v) ≥ m | Gn,d[S] = H, F ⊆ Gn,d] ≤ P[X ≥ m] , which implies the statement of the lemma.

4. Analysis of the exploration process

In this section we show how to control the expectation of ηt and ηt2. We ﬁrst use Lemmas 3 and 4 to bound the expectation of Yt+1 and Zt+1 from above.

- Lemma 5. Suppose d,n ∈ N such that 3 ≤ d ≤ n − 1 and n is suﬃciently large. Fix p ∈ [0,1]. Consider the exploration process described above on (Gn,d,Sn,d) with percolation probability p and suppose t ≤ dn2/3. Conditional on Ht satisfying |St| ≤ 5n2/3, we have


E[Yt+1|Ht] ≤ 20dn−1/3 and E[Zt+1|Ht] ≤ 180dn−1/3 .

Proof. If Ht satisﬁes Xt = 0, then Yt+1 ≤ t/(n − |St|) ≤ 2dn−1/3 by our choice of wt+1 (we always choose the vertex x that minimises dFt(x)) and |E(Ft)| ≤ t. Note that Zt+1 = 0 by deﬁnition. Hence we may assume from now on that Xt > 0.

Note that if d ≥ n/4, then the lemma follows directly from the fact that Yt+1 ≤ |St| ≤ 5n2/3 ≤ 20dn−1/3, and similarly for Zt+1. Thus, in the following we assume that d ≤ n/4.

Given w ∈ V \St such that vt+1w ∈/ E(Ft), we apply Lemma 3 with S = St, F = Ft, H = Ht,

- u = vt+1 and v = w to obtain


6(d − dHt(vt+1) − dFt(vt+1)) n

P[vt+1w ∈ E(Gn,d) | vt+1w ∈/ E(Ft),Ht] ≤

.

![image 11](<2017-joos-critical-percolation-random-regular_images/imageFile11.png>)

Observe that we run our exploration process on inputs. In order to apply Lemma 3, we ﬁx the semi-edge labelings and perform switchings on the graphs.

Since σvt+1 is a random permutation, each edge incident to vt+1 that is not contained in E(Ft) ∪ E(Ht) is chosen with the same probability to continue the exploration process. Hence,

given that vt+1w ∈ E(Gn,d) \ E(Ft), the probability that wt+1 = w is precisely (d − dHt(vt+1) − dFt(vt+1))−1. Therefore,

P[wt+1 = w | vt+1w ∈/ E(Ft),Ht]

6 n

= P[wt+1 = w | vt+1w ∈ E(Gn,d) \ E(Ft),Ht] · P[vt+1w ∈ E(Gn,d) | vt+1w ∈/ E(Ft),Ht] ≤

. Since P[wt+1 = w | vt+1w ∈ E(Ft),Ht] = 0, it follows that for every w ∈ V \ St

![image 12](<2017-joos-critical-percolation-random-regular_images/imageFile12.png>)

6 n

P[wt+1 = w | Ht] ≤

. (5) Using that |E(Ft)| ≤ t, we conclude

![image 13](<2017-joos-critical-percolation-random-regular_images/imageFile13.png>)

(5)

6 n

6 n · t ≤ 6dn−1/3 .

dFt(w)P[wt+1 = w|Ht]

≤

E[Yt+1|Ht] =

dFt(w) ≤

![image 14](<2017-joos-critical-percolation-random-regular_images/imageFile14.png>)

![image 15](<2017-joos-critical-percolation-random-regular_images/imageFile15.png>)

w∈V \St

w∈V \St

We now prove the second statement. Given w ∈ V \ St with P[wt+1 = w | Ht] > 0 (that is, vt+1w ∈/ E(Ft)), we apply Lemma 4 with S = St, F obtained from Ft by adding vt+1w, H = Ht, and v = w, to obtain

E[Zt+1|Ht] =

(5)

≤

E[Zt+1|wt+1 = w,vt+1w ∈/ E(Ft),Ht]P[wt+1 = w | vt+1w ∈/ E(Ft),Ht]

w∈V \St

6d|St| n ·

6 n ≤ 180dn−1/3 .

![image 16](<2017-joos-critical-percolation-random-regular_images/imageFile16.png>)

![image 17](<2017-joos-critical-percolation-random-regular_images/imageFile17.png>)

w∈V \St

- Lemma 6. Suppose µ ≥ 0 and d,n ∈ N such that 3 ≤ d ≤ n − 1 and n is suﬃciently large.


Consider the exploration process described above on (Gn,d,Sn,d) with p = 1−µnd−−11/3 and suppose t ≤ dn2/3. Conditional on |St| ≤ 5n2/3, then

![image 18](<2017-joos-critical-percolation-random-regular_images/imageFile18.png>)

E[ηt+1|Ht] ≥ −(570 + µ)n−1/3 and E[ηt2+1|Ht] ≥ d/4 . Moreover, if Xt > 0, then E[ηt2+1|Ht] ≤ d.

Proof. First assume that Xt > 0. Recall that for any Ht and for any edge uv that has not been exposed yet, we have E[I(uv) | Ht] = p = (1 − µn−1/3)/(d − 1). Recall that Yt+1 and Zt+1 are measurable with respect to Ht. Taking conditional expectations on (2) and using Lemma 5, we obtain

1 − µn−1/3 d − 1

1 − µn−1/3 d − 1

E[ηt+1|Ht] = − 1 −

(d − 2 − E[Yt+1|Ht] − 2E[Zt+1|Ht])

+

![image 19](<2017-joos-critical-percolation-random-regular_images/imageFile19.png>)

![image 20](<2017-joos-critical-percolation-random-regular_images/imageFile20.png>)

E[Yt+1|Ht] + 2E[Zt+1|Ht]

d − 1 − µn−1/3 ≥ −

≥ −

![image 21](<2017-joos-critical-percolation-random-regular_images/imageFile21.png>)

380dn−1/3

d − 1 − µn−1/3 ≥ −(570 + µ)n−1/3 , since d ≥ 3.

![image 22](<2017-joos-critical-percolation-random-regular_images/imageFile22.png>)

Again, by Lemma 5 and (2), we obtain

1 − µn−1/3 d − 1

1 − µn−1/3 d − 1

(−1)2 +

E[(d − 2 − Yt+1 − 2Zt+1)2 | Ht]

E[ηt2+1|Ht] = 1 −

![image 23](<2017-joos-critical-percolation-random-regular_images/imageFile23.png>)

![image 24](<2017-joos-critical-percolation-random-regular_images/imageFile24.png>)

(1 − µn−1/3)(d − 2)2 d − 1 −

2(d − 2)(E[Yt+1|Ht] + 2E[Zt+1|Ht]) d − 1 ≥ (1 − µn−1/3)(d − 2) − 2(E[Yt+1|Ht] + 2E[Zt+1|Ht]) ≥ (1 − µn−1/3)(d − 2) − 760dn−1/3 ≥ d/4 ,

d − 2 d − 1

≥

+

![image 25](<2017-joos-critical-percolation-random-regular_images/imageFile25.png>)

![image 26](<2017-joos-critical-percolation-random-regular_images/imageFile26.png>)

![image 27](<2017-joos-critical-percolation-random-regular_images/imageFile27.png>)

where the last inequality holds since d ≥ 3 and n is suﬃciently large. Observe that E[ηt2+1|Ht] ≤ d follows from a similar argument as (d − 2 − Yt+1 − 2Zt+1)2 ≤ (d − 2)2.

If Xt = 0, then clearly E[ηt+1|Ht] ≥ 0 and, since E[ηt2+1|Ht] = E[(d − Yt+1)2|Ht], similarly as before, one can prove that E[ηt2+1|Ht] ≥ d/4.

- Lemma 7. Suppose µ ≥ 0 and d,n ∈ N such that 3 ≤ d ≤ n − 1 and n is suﬃciently large.


Consider the exploration process described above on (Gn,d,Sn,d) with p = 1−µnd−−11/3. Then, for every ﬁxed δ > 0 and all 0 ≤ t1 ≤ t2 ≤ 5dn2/3, we have

![image 28](<2017-joos-critical-percolation-random-regular_images/imageFile28.png>)

t2 − t1

d − 1 ≥ −δn2/3 = 1 − o(n−2) and P |St2 \ St1| −

P |St2 \ St1| −

![image 29](<2017-joos-critical-percolation-random-regular_images/imageFile29.png>)

t2 − t1 d − 1 −

t2 5d/6 ≤ δn2/3 = 1 − o(n−2) .

![image 30](<2017-joos-critical-percolation-random-regular_images/imageFile30.png>)

![image 31](<2017-joos-critical-percolation-random-regular_images/imageFile31.png>)

Proof. We add a vertex to St either if I(vt+1wt+1) = 1 or if we start exploring a new component of Gn,d,p at time t+1. Thus, |St2 \St1| stochastically dominates a binomial random variable with parameters t2 − t1 and (1 − µn−1/3)/(d − 1). A standard application of Chernoﬀ’s inequality implies the ﬁrst statement.

Let At ⊆ St be the set of vertices that start a new component in Gn,d,p. For every 0 ≤

t ≤ 5dn2/3, let at := |At|, let ct := |St \ At| and let bt := |St \ (St1 ∪ At)|. Observe that ct is stochastically dominated by a binomial random variable with parameters t and 1/(d−1). Using

Chernoﬀ’s inequality, we have ct ≤ 8n2/3 with probability 1 − o(n−2) for any t ≤ 5dn2/3.

We claim that for every 0 ≤ t ≤ 5dn2/3 and conditional on ct ≤ 8n2/3, we have at ≤ ⌈5d/t 6⌉. Indeed, the claim is true for t ∈ {0,1}. Assume that t ≥ 2 and that the claim holds for every t′ ∈ {0,... ,t − 1}. If Xt−1 > 0, then at = at−1 and we are done. Thus, assume that Xt−1 = 0. Let s be the largest integer s′ ∈ {0,... ,t − 2} such that Xs′ = 0 (it exists since X0 = 0 and t ≥ 2). Recall that ws+1 is a vertex x ∈ V \ Ss that minimises dFs(x). It follows that

![image 32](<2017-joos-critical-percolation-random-regular_images/imageFile32.png>)

|E(Fs)| n − (as + cs) ≤

s n − ⌈s/(5d/6)⌉ − 8n2/3 ≤

d 6

dFs(ws+1) ≤

,

![image 33](<2017-joos-critical-percolation-random-regular_images/imageFile33.png>)

![image 34](<2017-joos-critical-percolation-random-regular_images/imageFile34.png>)

![image 35](<2017-joos-critical-percolation-random-regular_images/imageFile35.png>)

provided that n is large enough. Hence, Xs+1 ≥ 5d/6 and the process will not start a new component for the next 5d/6 steps. In particular, s + 5d/6 ≤ t. This implies at = as + 1 ≤ ⌈5d/s 6⌉ + 1 ≤ ⌈5d/t 6⌉.

![image 36](<2017-joos-critical-percolation-random-regular_images/imageFile36.png>)

![image 37](<2017-joos-critical-percolation-random-regular_images/imageFile37.png>)

Since |St2 \ St1| ≤ at2 + bt2, the second part of the lemma now follows from the upper bound

on at2 (which holds as we assume ct ≤ 8n2/3) and an upper bound on bt2 obtained by Chernoﬀ’s inequality.

5. Proof of Theorem 1

As we mentioned in the introduction, due to the result of Nachmias and Peres, we only need to prove a lower bound. Since it suﬃces to prove the lower bound of the statement for λ ≤ 0, we use the deﬁnition µ := −λ. We now present a brief overview of the proof. In the ﬁrst phase, we show that with probability at least 1−A−1/2, the process Xt exceeds A−1/4dn1/3 in the ﬁrst dn2/3 steps. In the second phase and conditional on the success of the ﬁrst phase, we show that Xt stays positive for at least 2A−1dn2/3 steps with probability at least 1 − A−1/2. From standard concentration inequalities, this gives the existence of a component of order at least A−1n2/3, concluding the proof. This proof strategy was introduced by Nachmias and Peres to prove the same statement for ﬁxed d ≥ 3 [20] and for d = n − 1 [21]. We remark that, in comparison to [20], our analysis of the exploration process is simpler, as we do not need to track the number of vertices x ∈ V \St which satisfy dFt(x) = k for k ∈ {0,1,... ,d}. If d ≥ 3 is ﬁxed,

- as in [20], almost every vertex x satisﬁes dFt(x) ∈ {0,1}. However, this is no longer true if d is an arbitrary function of n. We avoid the technicalities involved with this issue by averaging over the values of dFt(x).


First phase: We start with the deﬁnition of a few parameters. Let h := A−1/4dn1/3, T1 := 5dn2/3/6 and T2 := 2A−1dn2/3. In addition, we deﬁne the following stopping times:

τh := min{t : Xt ≥ h} ∧ T1 τS1 := min{t : |St| ≥ 3n2/3} τ1 := τh ∧ τS1 .

Recall that Xt+1 = ηt+1 +Xt. Note also that for every t < τ1, we have Xt ≤ h and |St| ≤ 5n2/3. Hence, Lemma 6 implies that

E[Xt2+1 − Xt2|Ht] ≥ E[ηt2+1|Ht] + 2E[ηt+1Xt|Ht] ≥ d/4 − 2 · (570 + µ)n−1/3h ≥ d/5 ,

provided that A is large enough with respect to µ (and thus, with respect to λ). Hence Xt2∧τ1 − (t ∧ τ1)d/5 is a submartingale. By the Optional Stopping theorem for submartingales (see for

example [9] p.491), E[Xτ21 − d5τ1] ≥ E[X02] = 0, which implies that E[τ1] ≤ d5E[Xτ21]. Since Xτ21 ≤ (h + d)2 ≤ 2h2, we obtain

![image 38](<2017-joos-critical-percolation-random-regular_images/imageFile38.png>)

![image 39](<2017-joos-critical-percolation-random-regular_images/imageFile39.png>)

5E[Xτ21] dT1 ≤

10h2 dT1

E[τ1] T1 ≤

= 12A−1/2 .

P[τ1 = T1] ≤

![image 40](<2017-joos-critical-percolation-random-regular_images/imageFile40.png>)

![image 41](<2017-joos-critical-percolation-random-regular_images/imageFile41.png>)

![image 42](<2017-joos-critical-percolation-random-regular_images/imageFile42.png>)

By Lemma 7 with t1 = 0 and t2 = T1, we have P[τS1 ≤ T1] = o(1). Thus P[{τh = T1} ∪ {τS1 ≤ τh}] ≤ P[τ1 = T1] + P[τS1 ≤ T1] ≤ 12A−1/2 + o(1) ≤ 13A−1/2 . (6)

We conclude that the event E := {τh < T1,τh < τS1} holds with probability at least 1−13A−1/2. In particular, with probability at least 1 − 13A−1/2, the random process Xt exceeds h before time T1.

Second phase: Write P∗ and E∗ for the probability and the expectation conditional on E. We deﬁne

τ0 : = min{t : Xτh+t = 0} ∧ T2 τS2 : = min{t : |Sτh+t \ Sτh| ≥ 2n2/3} τ2 : = τ0 ∧ τS2 .

Consider the random variable

Wt := h − min{h,Xτh+t} . Hence

Wt2+1 − Wt2 ≤ (h − min{h,Xτh+t} − ητh+t+1)2 − (h − min{h,Xτh+t})2

= ητ2

h+t+1 − 2ητh+t+1(h − min{h,Xτh+t}) ≤ ητ2

h+t+1 − 2ητh+t+1h .

If t < τ2 and n is suﬃciently large, we can apply Lemma 6 and this leads to (provided A is suﬃciently large with respect to µ)

E∗[Wt2+1 − Wt2 | Hτh+t] ≤ d + 2 · (570 + µ)n−1/3 · h ≤ 2d .

Thus, Wt2∧τ2 − 2d(t ∧ τ2) is a supermartingale. Similar as before, we use the Optimal Stopping theorem to conclude that

E∗[Wτ22] ≤ 2dE∗[τ2] ≤ 2dT2 . Thus

P∗[τ2 < T2] = P∗[τ0 < T2,τS2 > T2] + P∗[τS2 ≤ T2] ≤ P∗[Wτ2 ≥ h] + P∗[|Sτh+T2 \ Sτh| ≥ 2n2/3] ≤ P∗[Wτ22 ≥ h2] + o(1) ≤

E∗[Wτ22] h2

+ o(1) ≤ 5A−1/2 ,

![image 43](<2017-joos-critical-percolation-random-regular_images/imageFile43.png>)

where we used Lemma 7 with t1 = τh and t2 = τh + T2 for the second inequality. (Observe that we cannot apply Lemma 7 directly, because we assume E holds and τh is a random time. However, as τh ≤ T1, a simple union bound with t1 = k and t2 = k + T2 for all k ≤ T1 together with the fact that P[E] ≥ 1 − 13A−1/2 ≥ 1/2, yields the desired result.) It follows that

P[{τ2 < T2} ∪ {τh = T1} ∪ {τS1 ≤ τh}] ≤ P[{τh = T1} ∪ {τS1 ≤ τh}] + P∗[τ2 < T2]

(6) ≤ 13A−1/2 + 5A−1/2 = 18A−1/2 .

Since all the vertices explored from time τh to τh+τ2 belong to the same component of Gn,d,p, there exists a component of size at least |Sτh+τ2 \Sτh|. As τ2 = T2 = 2A−1dn2/3 with probability

- at least 1 − 18A−1/2, by Lemma 7 with t1 = τh and t2 = τh + T2 (as above, strictly speaking, we apply Lemma 7 with t1 = k and t2 = k + T2 for all k ≤ T1 and use the fact that P[E] ≥ 1/2) with probability at least 1 − 18A−1/2 − o(1) ≥ 1 − 19A−1/2, there exists a component of size at least A−1n2/3.


Acknowledgements: The authors want to thank Nikolaos Fountoulakis, Michael Krivelevich, and Asaf Nachmias for fruitful discussions on the topic and the anonymous referees for their valuable comments.

References

- 1. N. Alon, I. Benjamini, and A. Stacey, Percolation on ﬁnite graphs and isoperimetric inequalities, Ann. Probab.

(2004), 1727–1745.

- 2. B. Bollob´s, A probabilistic proof of an asymptotic formula for the number of labelled regular graphs, Europ. J. Combin. 1 (1980), 311–316.
- 3. B. Bollob´s and O. Riordan, An old approach to the giant component problem, J. Combin. Theory (Series B) 113 (2015), 236–260.
- 4. C. Borgs, J. T. Chayes, R. van der Hofstad, G. Slade, and J. Spencer, Random subgraphs of ﬁnite graphs. I. The scaling window under the triangle condition, Random Structures Algorithms 27 (2005), 137–184.
- 5. P. Erd˝s and A. Re´nyi, On the evolution of random graphs, Magyar Tud. Akad. Mat. Kutato´ Int. K¨zl. 5

(1960), 17–61.

- 6. N. Fountoulakis, Percolation on sparse random graphs with given degree sequence, Internet Math. 4 (2007), 329–356.
- 7. N. Fountoulakis, F. Joos, and G. Perarnau, Percolation on random graphs with a ﬁxed degree sequence, arXiv:1611.08496 (2016).
- 8. A. Goerdt, The giant component threshold for random regular graphs with edge faults, Theoret. Comput. Sci. 259 (2001), 307–321.
- 9. G. Grimmett and D. Stirzaker, Probability and random processes, Oxford University Press, 2001.
- 10. S. Janson, On percolation in random graphs with given vertex degrees, Electron. J. Probab. 14 (2009), 87–118.
- 11. F. Joos, G. Perarnau, D. Rautenbach, and B. Reed, How to determine if a random graph with a ﬁxed degree sequence has a giant component, to appear in Probability Theory and Related Fields (2017).
- 12. M. Krivelevich and B. Sudakov, The phase transition in random graphs: A simple proof, Random Structures Algorithms 43 (2013), 131–138.
- 13. M. Krivelevich, B. Sudakov, V. H. Vu, and N. C. Wormald, Random regular graphs of high degree, Random Structures Algorithms 18 (2001), 346–363.
- 14. T.  Luczak, B. Pittel, and J. C. Wierman, The structure of a random graph at the point of the phase transition, Trans. Amer. Math. Soc. 341 (1994), 721–748.
- 15. C. McDiarmid, Connectivity for random graphs from a weighted bridge-addable class, Electron. J. Combin. 19 (2012), no. 4, Paper 53, 20.
- 16. B. D. McKay, Asymptotics for symmetric 0-1 matrices with prescribed row sums, Ars Combin 19 (1985), 15–25.
- 17. B. D. McKay and N. C. Wormald, Asymptotic enumeration by degree sequence of graphs with degrees o(n1/2), Combinatorica 11 (1991), 369–382.
- 18. A. Nachmias, Mean-ﬁeld conditions for percolation on ﬁnite graphs, Geom. Funct. Anal. 19 (2009), 1171–1194.
- 19. A. Nachmias and Y. Peres, Critical random graphs: diameter and mixing time, Ann. Probab. (2008), 1267– 1286.
- 20. , Critical percolation on random regular graphs, Random Structures Algorithms 36 (2010), 111–148.

![image 44](<2017-joos-critical-percolation-random-regular_images/imageFile44.png>)

- 21. , The critical random graph, with martingales, Israel J. Math. 176 (2010), 29–41.

![image 45](<2017-joos-critical-percolation-random-regular_images/imageFile45.png>)

- 22. B. Pittel, Edge percolation on a random regular graph of low degree, Ann. Probab. 36 (2008), 1359–1389.
- 23. O. Riordan, The phase transition in the conﬁguration model, Comb. Probab. Comput. 21 (2012), 265–299.
- 24. N. C. Wormald, Models of random regular graphs, Surveys in combinatorics, 1999 (Canterbury), London Math. Soc. Lecture Note Ser., vol. 267, Cambridge Univ. Press, Cambridge, 1999, pp. 239–298.


Version November 6, 2018 Felix Joos

- <f.joos@bham.ac.uk> Guillem Perarnau
- <g.perarnau@bham.ac.uk> School of Mathematics, University of Birmingham, Birmingham United Kingdom


