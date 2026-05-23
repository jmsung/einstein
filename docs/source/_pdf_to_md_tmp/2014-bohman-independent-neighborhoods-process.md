arXiv:1407.7192v1[math.CO]27Jul2014

The independent neighborhoods process

Tom Bohman∗ Dhruv Mubayi† Michael Picollelli ‡

Abstract

A triangle T(r) in an r-uniform hypergraph is a set of r + 1 edges such that r of them share a common (r − 1)-set of vertices and the last edge contains the remaining vertex from each of the ﬁrst r edges. Our main result is that the random greedy triangle-free process on n points terminates in an r-uniform hypergraph with independence number O((n log n)1/r). As a consequence, using recent results on independent sets in hypergraphs, the Ramsey number r(T(r),Ks(r)) has order of magnitude sr/ logs. This answers questions posed in [4, 10] and generalizes the celebrated results of Ajtai-Komlo´s-Szemer´edi [1] and Kim [9] to hypergraphs.

# 1 Introduction

An r-uniform hypergraph H (r-graph for short) is a collection of r-element subsets of a vertex set V (H). Given r-graphs G and H, the ramsey number r(G,H) is the minimum n such that every red/blue-edge coloring of the complete r-graph Kn(r) := [nr] contains a red copy of G or a blue copy of H (often we will write Kn for Kn(r)). Determining these numbers for graphs (r = 2) is known to be notoriously diﬃcult, indeed the order of magnitude (for ﬁxed t) of r(Kt,Ks) is wide open when t ≥ 4. The case t = 3 is one of the celebrated results in graph Ramsey theory:

r(K3,Ks) = Θ(s2/log s). (1)

The upper bound was proved by Ajtai-Koml´os-Szemere´di [1] as one of the ﬁrst applications of the semi-random method in combinatorics (simpler proofs now exist due to Shearer [12, 13]). The lower bound, due to Kim [9], was also achieved by using the semi-random or nibble method. More recently, the ﬁrst author [3] showed that a lower bound for r(K3,Ks) could also be obtained by the triangle-free process, which is a random greedy algorithm. This settled a question of Spencer on the independence number of the triangle-free process. Still more recently, Bohman-Keevash [6] and Fiz Pontiveros-Griﬃths-Morris [8] have analyzed the triangle-free process more carefully and improved the constants obtained so that the gap between the upper and lower bounds for r(K3,Ks) is now asymptotically a multiplicative factor of 4.

Given the diﬃculty of these basic questions in graph Ramsey theory, one would expect that the corresponding questions for hypergraphs are hopeless. This is not always the case. Hypergraphs

![image 1](<2014-bohman-independent-neighborhoods-process_images/imageFile1.png>)

∗Department of Mathematical Sciences, Carnegie Mellon University, Pittsburgh, PA 15213. Research supported by NSF grant DMS-1100215.

†Department of Mathematics, Statistics, and Computer Science, University of Illinois at Chicago, Chicago, IL

60607. Research supported by NSF grant DMS-1300138. ‡Department of Mathematics, California State University San Marcos, San Marcos, CA 92096.

behave quite diﬀerently for asymmetric Ramsey problems, for example, there exist K4(3)-free 3graphs on n points with independence number of order log n, so r(K4(3),Ks(3)) is exponential in s unlike the graph case. Consequently, to obtain r-graph results parallel to (1), one must consider problems r(G,Ks) where G is much sparser than a complete graph. A recent result in this vein due to Kostochka-Mubayi-Verstrae¨te [10] is that there are positive constants c1,c2 with

c1s3/2 (log s)3/4

< r(C3(3),Ks(3)) < c2s3/2

![image 2](<2014-bohman-independent-neighborhoods-process_images/imageFile2.png>)

where C3(3) is the loose triangle, comprising 3 edges that have pairwise intersections of size one and have no point in common. The authors in [10] conjectured that r(C3(3),Ks(3)) = o(s3/2) and the order of magnitude remains open. Another result of this type for hypergraphs due to Phelps and Ro¨dl [11] is that r(P2(3),Ks(3)) = Θ(s2/log s), where Pt(3) is the tight path with t edges. Recently, the second author and Cooper [7] prove that for ﬁxed t ≥ 4, the behavior of this Ramsey number changes and we have r(Pt(3),Ks(3)) = Θ(s2); the growth rate for t = 3 remains open. These are the only nontrivial hypergraph results of polynomial Ramsey numbers, and in this paper we add to this list with an extension of (1).

- Deﬁnition 1. An r-uniform triangle T(r) is a set of r + 1 edges b1,... ,br,a with bi ∩ bj = R for all i < j where |R| = r − 1 and a = ∪i(bi − R). In other words, r of the edges share a common (r − 1)-set of vertices, and the last edge contains the remaining point in all these previous edges.


When r = 2, then T(2) = K3, so in this sense T(r) is a generalization of a graph triangle. We may view a T(r)-free r-graph as one in which all neighborhoods are independent sets, where the neighborhood of an R ∈ Vr(−H1) is {x : R ∪ {x} ∈ H}. Frieze and the ﬁrst two authors [4] proved that for ﬁxed r ≥ 2, there are positive constants c1 and c2 with

sr (log s)r/(r−1)

< r(T(r),Ks(r)) < c2sr.

c1

![image 3](<2014-bohman-independent-neighborhoods-process_images/imageFile3.png>)

They conjectured that the upper bound could be improved to o(sr) and believed that the log factor in the lower bound could also be improved. Kostochka-Mubayi-Verstrae¨te [10] partially achieved this by improving the upper bound to

r(T(r),Ks(r)) = O(sr/log r) and believed that the log factor was optimal.

In this paper we verify this assertion by analyzing the T(r)-free (hyper)graph process. This process begins with an empty hypergraph G(0) on n vertices. Given G(i−1), the hypergraph G(i) is then formed by adding an edge ei selected uniformly at random from the r-sets of vertices which neither form edges of G(i−1) nor create a copy of T(r) in the hypergraph G(i−1)+ei. The process terminates with a maximal T(r)-free graph G(M) with a random number M of edges. Our main result is the following:

Theorem 1. For r ≥ 3 ﬁxed the T(r)-free process on n points produces an r-graph with independence number O (nlog n)1/r with high probability.

This result together with the aformentioned result of Kostochka-Mubayi-Verstrae¨te give the following generalization of (1) to hypergraphs.

Corollary 2. For ﬁxed r ≥ 3 there are positive constants c1 and c2 with

sr log s

sr log s

< r(T(r),Ks(r)) < c2

.

c1

![image 4](<2014-bohman-independent-neighborhoods-process_images/imageFile4.png>)

![image 5](<2014-bohman-independent-neighborhoods-process_images/imageFile5.png>)

Graph processes that iteratively add edges chosen uniformly at random subject to the condition that some graph property is maintained have been used to generate interesting combinatorial objects in a number of contexts. In addition to the lower bound on the Ramsey number r(K3,Ks) given by the triangle-free graph process (discussed above), the H-free graph process gives the best known lower bound on the Ramsey number r(Kt,Ks) for t ≥ 4 ﬁxed and the best known lower bound on the Tura´n numbers for some bipartite graphs [5]. The process that forms a subset of Zn by iteratively choosing elements to be members of the set uniformly at random subject to the condition that the set does not contains a k-term arithmetic progression produces a set that has interesting properties with respect to the Gowers norm [2].

The T(r)-free (hyper)graph process can be viewed as an instance of the random greedy hypergraph independent set process. Let H be a hypergraph. An independent set in H is a set of vertices that contains no edge of H. The random greedy independent set process forms such a set by starting with an empty set of vertices and iteratively choosing vertices uniformly at random subject to the condition that the set of chosen vertices continues to be an independent set. We study the random greedy independent set process for the hypergraph HT(r) which has vertex set

[n]

r and edge set consisting of all copies of T(r) on vertex set [n]. Note that, since an independent set in HT(r) gives a T(r)-free r-graph on point set [n], the random greedy independent set process on HT(r) is equivalent to the T(r)-free process. Our analysis of the T(r)-free process is based on recent work on the random greedy hypergraph independent set process due to Bennett and Bohman [2].

The remainder of the paper is organized as follows. In the following Section we establish some notation and recall the necessary facts from [2]. The proof of Theorem 1 is given in the Section that follows, modulo the proofs of some technical lemmas. These lemmas are proved in the ﬁnal Section by application of the diﬀerential equations method for proving dynamic concentration.

# 2 Preliminaries

Let H be a hypergraph on vertex set V = V (H). For each set of vertices A ⊆ V , let NH(A) denote the neighborhood of A in H, the family of all sets Y ⊆ V \ A for which A ∪ Y ∈ H. We then deﬁne the degree of A in H to be dH(A) = |NH(A)|. For a nonnegative integer a, we deﬁne ∆a(H) to be the maximum of dH(A) over all A ∈ Va . Next, for a pair of (not necessarily disjoint) sets A,B ⊆ V , we deﬁne the codegree of A and B to be the number of sets X ⊆ V \ (A ∪ B) for which A ∪ X,B ∪ X both lie in H.

Recall that we deﬁne G(i) to be the r-graph produced through i steps of the T(r)-free process. We let Fi denote the natural ﬁltration determined by the process (see [3], for example). We also simplify our notation somewhat and write Ni(A) in place of NG(i)(A), di(A) in place of dG(i)(A), etc., when appropriate.

The r-graph G(i) partitions [nr] into three sets E(i),O(i),C(i). The set E(i) is simply the set of i edges chosen in the ﬁrst i steps of the process. The set O(i) consists of the open r-sets: all

- e ∈ nr \ E(i) for which G(i) + e is T(r)-free. The r-sets in C(i) := [nr] \ (E(i) ∪ O(i)) are closed. Finally, for each open r-set e ∈ O(i), we deﬁne the set Ce(i) to consist of all open r-sets f ∈ O(i) such that the graph G(i) + e + f contains a copy of T(r) using both e and f as edges. (That is, Ce(i) consists of the open r-sets whose selection as the next edge ei+1 would result in e ∈ C(i+1).)


We now introduce some notation in preparation for our application of the results in [2]. Set

N :=

n r

D := (r + 1) ·

n − r r − 1

N D1/r

.

s :=

![image 6](<2014-bohman-independent-neighborhoods-process_images/imageFile6.png>)

Note that N is the size of the vertex set of the hypergraph HT(r) and D is the vertex degree of HT(r) (in other words, every r-set in [n] is in D copies of T(r)). The parameter s is the ‘scaling’ for the

length of the process. This choice is motivated by the heuristic that E(i) should be pseudorandom; that is, E(i) should resemble in some ways a collection of r-sets chosen uniformly at random (without any further condition). If this is indeed the case then the probability that a given r-set is open would be roughly

r D

r

i N

i N

1 −

≈ exp −

D

![image 7](<2014-bohman-independent-neighborhoods-process_images/imageFile7.png>)

![image 8](<2014-bohman-independent-neighborhoods-process_images/imageFile8.png>)

and a substantial number of r-sets are closed when roughly s edges have been added. In order to discuss the evolution in more detail, we pass to a limit by introducing a continuous time variable t where t = t(i) = i/s.

The evolution of key parameters of the process closely follow trajectories given by the functions q(t) := exp {−tr} and c(t) := −q′(t) = rtr−1q(t).

We introduce small constants ζ,γ such that ζ ≪ γ ≪ 1/r. (The notation α ≪ β here means that α is chosen to be suﬃciently small relative to β.) The point where we stop tracking the process is given by

imax := ζ · ND−1/r(log1/r N) and tmax := imax/s = ζ log1/r N. For i∗ ≥ 0, let Ti∗ denote the event that the following estimates hold for all steps 0 ≤ i ≤ i∗:

|O(i)| = q(t) ± N−γ N (2) and for every open r-set e ∈ O(i)

|Ce(i)| = c(t) ± N−γ D1/r. (3) It follows from the results of Bohman and Bennett that Timax holds with high probability.

Proof. This follows from the estimates for the random greedy hypergraph independent set process given in [2] applied to the (r + 1)-uniform hypergraph HT(r). Veriﬁcation of the conditions of Theorem 1.1 in [2] for this hypergraph is routine. (Note that ∆ℓ(HT(r)) = Θ(nr−ℓ) and Γr(HT(r)) = 0.) The estimates (2) and (3) above then follow from those on |V (i)| and d2(v,i) given by (5) and (6) in [2].

![image 9](<2014-bohman-independent-neighborhoods-process_images/imageFile9.png>)

![image 10](<2014-bohman-independent-neighborhoods-process_images/imageFile10.png>)

![image 11](<2014-bohman-independent-neighborhoods-process_images/imageFile11.png>)

![image 12](<2014-bohman-independent-neighborhoods-process_images/imageFile12.png>)

Note that the fact that Timax holds with high probability does not prove that the independence number of G(M) is O (nlog n)1/r with high probability. This is proved below.

We will also make use of the following fact regarding r-graphs that appear as subgraphs of the T(r)-free process.

- Lemma 3 ([2] Lemma 4.2). Fix a constant L and suppose e1,... ,eL ∈ [nr] form a T(r)-free hypergraph. Then for all steps j ≤ imax,


P[{e1,... ,eL} ⊆ E(j)] = (j/N)L · (1 + o(1)).

We conclude this Section by noting that the desired bound on the independence number of G(M) can be viewed as a pseudorandom property of the r-graph G(i). Indeed, if G(i) resembles a collection of r-sets chosen uniformly at random then the expected number of independent sets of size k would be

i

k r n r

kr nr

n k

1 −

= exp Θ(k log n) − Θ i

.

![image 13](<2014-bohman-independent-neighborhoods-process_images/imageFile13.png>)

![image 14](<2014-bohman-independent-neighborhoods-process_images/imageFile14.png>)

If the process lasts through i = Θ(ND−1/r(log1/r N)) = Θ(nr−1+1/r log1/r n) steps then we would anticipate an independence number of O (nlog n)1/r . In the remainder of the paper we make this heuristic calculation rigorous.

# 3 Independence number: Proof of Theorem 1

We expand the list of constants given in the previous section by introducing large constants κ and W, and small constant ǫ such that

1 κ

1 W

≪ ζ ≪

![image 15](<2014-bohman-independent-neighborhoods-process_images/imageFile15.png>)

![image 16](<2014-bohman-independent-neighborhoods-process_images/imageFile16.png>)

≪ ε ≪ γ. (4)

In the course of the argument we introduce dynamic concentration phenomena that will stated in terms of the error function

f(t) := exp {W(tr + t)} . Deﬁne the constant λ := κ−2γ, and then let

![image 17](<2014-bohman-independent-neighborhoods-process_images/imageFile17.png>)

k := κ(nlog n)1/r and ℓ := λ(nlog n)1/r,

noting that as γ is small, k ≈ 2ℓ. Our aim is to show that the independence number of G(imax) is at most k with high probability. To do so, we will show that provided κ is suitably large, w.h.p.

for every step 0 ≤ i ≤ imax, every k-element set of vertices has at least Ω q(t) kr open r-sets. As equation (2) establishes (1+o(1))q(t)N open r-sets in total w.h.p., the probability that Timax holds and a given k-set remains independent over all imax steps is then at most

imax

i=1

1 − Ω

q(t)kr q(t)N

![image 18](<2014-bohman-independent-neighborhoods-process_images/imageFile18.png>)

= 1 − Ω

κr log n nr−1

![image 19](<2014-bohman-independent-neighborhoods-process_images/imageFile19.png>)

imax

= exp −ζκr · Ω(n1/r log1+1/r n) ,

where our O(·),Ω(·),Θ(·) notation does not suppress any constant that appears in (4). Since

nk = exp κ · O(n1/r log1+1/r n) , this suﬃces by the union bound, provided κ is suitably large with respect to r and ζ.

There is a signiﬁcant obstacle to proving that every set of k vertices contains the ‘right’ number of open r-sets. Note that all r-sets within the neighborhood of an (r − 1)-set are closed. (To be precise, if A ∈ r [−n]1 then Nir(A) ⊆ C(i)). So a set of k vertices that has a large intersection with the neighborhood of an (r−1)-set does not have the ‘right’ number of open r-sets. To overcome this obstacle, we extend the argument in [3] for bounding the independence number of the triangle-free process. Our argument has two steps:

- 1. We apply the diﬀerential equations method for establishing dynamic concentration to show that unless a certain ‘bad’ condition occurs, a pair of disjoint ℓ-sets will have the ‘right’ number of open r-sets that are contained in the union of the pair of ℓ-sets and intersect both ℓ-sets, that is about q(t) · [ 2rℓ − 2 r ℓ ] open r-sets. Note that 2rℓ − 2 r ℓ > 13 kr , say, as γ is small.

![image 20](<2014-bohman-independent-neighborhoods-process_images/imageFile20.png>)

- 2. We then argue that w.h.p., every k-set contains a (disjoint) pair of ℓ-sets which is ‘good’, i.e., for which the bad condition does not occur.


We formalize this with the notion of r-sets which are open ‘with respect to’ a pair of disjoint ℓ-sets.

- Deﬁnition 2. Fix a disjoint pair A,B ∈ [nℓ] . The stopping time τA,B is the minimum of imax and the ﬁrst step i for which there exists a (r − 1)-set X such that

Ni(X) ∩ A = ∅, Ni(X) ∩ B = ∅, and |Ni(X) ∩ (A ∪ B)| ≥ k/n2ε.

- Deﬁnition 3. For each step i ≥ 0, we say that an r-set e ⊆ A ∪ B is open with respect to the pair A,B in G(i) if e ∩ A = ∅, e ∩ B = ∅, and either


- • e ∈ O(i) or
- • e ∈ O(i − 1) ∩ C(i) and i = τA,B.


Let QA,B(i) count the number of r-sets which are open with respect to the pair A,B in G(i).

- Lemma 4. With high probability, for every disjoint pair A,B ∈ [nℓ] and all steps 0 ≤ i ≤ τA,B,

QA,B(i) = q(t) ±

f(t) nε

![image 21](<2014-bohman-independent-neighborhoods-process_images/imageFile21.png>)

·

2ℓ r

− 2

ℓ r

. (5)

- Lemma 5. With high probability, for every step 0 ≤ i < imax and every set K ∈ [nk] , there exists a pair of disjoint ℓ-sets A,B contained in K for which τA,B > i.


- Lemmas 4 and 5, respectively, complete steps 1 and 2 of the proof outlined above. The ‘bad’


condition for a pair A,B of disjoint ℓ-sets is the event that we have reached the stopping time τA,B; that is, the bad condition is that there is some (r−1)-set whose neighborhood intersects both A and B and has large intersection with A ∪ B. Note that if i < τA,B then QA,B is equal to the number of open r-sets that are contained in A ∪ B and intersect both A and B. Thus, Lemma 4 says that

if we do not have the ‘bad’ condition then we have the ‘right’ number of such sets. Lemma 5 then says that every k-set contains a pair disjoint pair A,B of ℓ-sets for which the ‘bad’ condition does not hold. Taken together, Lemmas 4 and 5 yield that w.h.p., for every step 0 ≤ i < imax, every k-set contains at least q(t)(1 + o(1))[ 2rℓ − 2 r ℓ ] = Ω q(t) kr open r-sets, as required. We now prove Lemma 5 modulo the proof of Lemma 6 which bounds the maximum degree of an (r−1)-set.

- Lemmas 4 and 6 are proved in the next Section.


Proof of Lemma 5. We require a bound on the maximum degree of (r − 1)-sets of vertices. For each step i ≥ 0 let Di denote the event that ∆r−1(G(i)) ≤ ε(nlog n)1/(r−1).

- Lemma 6. Timax ∧ Dimax holds with high probability. The proof of Lemma 6 is given in the next Section.


Fix a step 0 ≤ i < imax, and a set K ∈ [nk] . Note that, by Lemma 6, we may assume that Di

holds. We also note that the maximum co-degree of a pair of sets A,B ∈ r [−n]1 is at most 5r with high probability. This follows from Lemma 3 and the union bound:

Pr ∃A,B ∈

[n] r − 1

with co-degree 5r ≤

n r − 1

n r − 1

n5r

i N

![image 22](<2014-bohman-independent-neighborhoods-process_images/imageFile22.png>)

10r

= n8−3r+o(1) = o(1). (6)

Given these two facts (i.e. these degree and co-degree bounds for (r − 1)-sets), the remainder of the proof is deterministic.

To begin, deﬁne the set

- Claim 1. |X| < 2n2ε.


X := X ∈

[n] r − 1

: |Ni(X) ∩ K| ≥ k/n2ε .

Proof. Suppose ∃Y ⊆ X with |Y| = 2n2ε. Let N = Y ∈Y(Ni(Y ) ∩ K). By inclusionexclusion,

k ≥ |N| ≥ |Y| · (k/n2ε) − |Y|25r ≥ 2k − 20rn4ε, a contradiction as ε is small and k = n1/r+o(1).

![image 23](<2014-bohman-independent-neighborhoods-process_images/imageFile23.png>)

![image 24](<2014-bohman-independent-neighborhoods-process_images/imageFile24.png>)

![image 25](<2014-bohman-independent-neighborhoods-process_images/imageFile25.png>)

![image 26](<2014-bohman-independent-neighborhoods-process_images/imageFile26.png>)

Next, we ‘discard’ from K the vertices which are common neighbors of (r − 1)-sets in X: let

Kbad := {v ∈ K : ∃X,Y ∈ X with X = Y and v ∈ Ni(X) ∩ Ni(Y )} and Kgood := K \ Kbad. Then

γ 2

|Kbad| ≤ |X|25r ≤ 20rn4ε <

· (nlog n)1/r, say, for large n.

![image 27](<2014-bohman-independent-neighborhoods-process_images/imageFile27.png>)

We ﬁnd disjoint ℓ-subsets A,B of Kgood as follows, noting |Kgood| ≥ 2ℓ + (γ/2)(nlog n)1/r. For each subset Y ⊆ X, let

Ni(Y ) ∩ Kgood.

N(Y) =

Y ∈Y

Now, choose a maximal subset X∗ ⊆ X subject to |N(X∗)| ≤ ℓ. If X∗ = X, then let A,B be ℓ-sets satisfying N(X∗) ⊆ A ⊆ Kgood and B ⊆ Kgood \ A.

Otherwise, pick any set X∗ ∈ X \ X∗, so

ℓ < |N(X∗ ∪ {X∗})| < ℓ + ε(nlog n)1/r; let A ⊆ N(X∗ ∪ {X∗}) and B ⊆ Kgood \ N(X∗ ∪ {X∗}) be ℓ-sets.

Observe now that if X∗ = X, then Ni(X)∩B = ∅ for all X ∈ X. Otherwise, if X ∈ X∗ ∪{X∗}, Ni(X)∩B = ∅, but if X ∈ X \(X∗ ∪{X∗}) then Ni(X)∩A = ∅ as we are working within Kgood. In either case, for every (r−1)-set X for which |Ni(X)∩(A∪B)| ≥ k/n2ε holds, either Ni(X)∩A = ∅ or Ni(X) ∩ B = ∅, and τA,B > i follows.

![image 28](<2014-bohman-independent-neighborhoods-process_images/imageFile28.png>)

![image 29](<2014-bohman-independent-neighborhoods-process_images/imageFile29.png>)

![image 30](<2014-bohman-independent-neighborhoods-process_images/imageFile30.png>)

![image 31](<2014-bohman-independent-neighborhoods-process_images/imageFile31.png>)

# 4 Dynamic Concentration

In this section we prove Lemmas 4 and 6. Both of these statements assert dynamic concentration of key parameters of the T(r)-free process. We apply the diﬀerential equations method for proving dynamic concentration, which we now brieﬂy sketch.

Suppose we have a combinatorial stochastic process based on a ground set of size n that generates a natural ﬁltration F0,F1,... . Suppose further that we have a sequence of random variables A0,A1,... and that we would like to prove a dynamic concentration statment of the form

Ai ≤ Ti + Ei for all 0 ≤ i ≤ m(n) with high probability, (7)

where T0,T1,... is the expected trajectory of the sequence of random variables Ai and E0,E1,... is a sequence of error functions. (One is often interested in proving a lower bound on Ai in conjunction with (7). The argument for proving this is essentially the same as the upper bound argument that we discuss here.) We often make this statement in the context of a limit that we deﬁne in terms of a continuous time t given by t = i/s where s is the time scaling of the process. The limit of the expected trajectory is determined by setting Ti = f(t)S(n) where S = S(n) is the order scaling of the random variable Ai. Given these assumptions we should have

S s

E[Ai+1 − Ai | Fi] = Ti+1 − Ti = [f(t + 1/s) − f(t)]S ≈ f′(t) ·

.

![image 32](<2014-bohman-independent-neighborhoods-process_images/imageFile32.png>)

Thus the trajectory is determined by the expected one-step change in Ai.

We prove (7) by applying facts regarding the probability of large deviations in martingales with bounded diﬀerences. In particular, we consider the sequence

Di = Ai − Ti − Ei.

Note that if we set T0 = A0 (which is often the natural initial condition) then D0 = −E0. If we can establish that the sequence Di is a supermartingale and E0 is suﬃciently large then it should be unlikely that Di is ever positive, and (7) follows. In order to complete such a proof we show that the sequence Di is a supermartingale, a fact that is sometimes called the trend hypothesis (see Wormald [14]). The trend hypothesis will often impose a condition that the sequence of

error functions Ei is growing suﬃciently quickly (i.e. the derivative of the limit of error function is suﬃciently large). We then show that the one-step changes in Di are bounded in some way (this is sometimes called the boundedness hypothesis). This puts us in the position to apply a martingale inequality. In order to get good bounds from the martingale inequality one generally needs to make E0 large.

In this section we appeal to the following pair of martingale inequalities (see [3]). For positive reals b,B, the sequence A0,A1,... is said to be (b,B)-bounded if Ai − b ≤ Ai+1 ≤ Ai + B for all i ≥ 0.

- Lemma 7. Suppose b ≤ B/10 and 0 < a < bm. If A0,A1,... is a (b,B)-bounded submartingale, then P[Am ≤ A0 − a] ≤ exp −a2/3bmB .
- Lemma 8. Suppose b ≤ B/10 and 0 < a < bm. If A0,A1,... is a (b,B)-bounded supermartingale, then P[Am ≥ A0 + a] ≤ exp −a2/3bmB .


Our applications of these Lemmas make use of stopping times. Formally speaking, a stopping time is simply a postive integer-valued random variable τ for which {τ ≤ n} ∈ Fn. In other words, τ is a stopping time if the event τ ≤ n is determined by the ﬁrst n steps of the process. We consider the stopped process (Di∧τ), where x∧y := min{x,y}, in the place of the sequence D0,D1,... . Our stopping time τ is the ﬁrst step in the process when any condition on some short list of conditions fails to hold, where the condition Di ≤ 0 is one of the conditions in the list. Note that, since the variable (Di∧τ) does not change once we reach the stopping time τ, we can assume that all conditions in the list hold when we are proving the trend and boundedness hypotheses. Also note that if the stopping time τ′ is simply the minimum of imax and the ﬁrst step for which Di > 0 then

{Dimax∧τ′ > 0} contains the event {∃i ≤ imax : Di > 0}.

4.1 Proof of Lemma 6. For each set A ∈ r [−n]1 and step i ≥ 0, let OA(i) := {e ∈ O(i) : A ⊆ e}, and QA(i) = |OA(i)|. We deﬁne sequences of random variables

YA+(i) := q(t) · n − QA(i) + f(t) · n1−ε, YA−(i) := q(t) · n − QA(i) − f(t) · n1−ε, ZA(i) := di(A) − t · D−1/rn − f(t)q(t)−1 · n1/r−ε,

Finally, we deﬁne the stopping time τ to be the minimum of nr , the ﬁrst step i where Ti fails, or where any of YA+(i) < 0, YA−(i) > 0, or ZA(i) > 0 holds for some A ∈ r [−n]1 .

To prove Lemma 6, we show that for each A ∈ r [−n]1 ,

P YA+(imax ∧ τ) < 0 = o(n−(r−1)), (8) P YA−(imax ∧ τ) > 0 = o(n−(r−1)), and (9)

P[ZA(imax ∧ τ) > 0] = o(n−(r−1)). (10)

Consider the event τ ≤ imax. This event is the union of the event that Timax fails and the event that there exists A ∈ r [−n]1 such that YA+(imax ∧ τ) < 0 or YA−(imax ∧ τ) > 0 or ZA(imax ∧ τ) > 0. Since Timax holds with high probability, it follows from (8)–(10) and the union bound that w.h.p.

τ > imax. In particular, ZA(i) ≤ 0 for all (r − 1)-sets A and steps 0 ≤ i ≤ imax. It then follows – since ζ ≪ min{1/W,ε} implies that we may bound f(tmax) < nε/2, say – that we have

∆r−1(G(imax)) ≤ tmaxD−1/rn + f(tmax)n1/r−ε/2 = ζ · O((nlog n)1/r) ≤ ε(nlog n)1/r,

for n suﬃciently large. (We remark in passing that the bounds on YA±(i) given when i < τ are necessary for our proof of the bounds on ZA(i).)

For the remainder of this argument, ﬁx a set A ∈ r [−n]1 . We ﬁrst prove (8) and (9).

- Claim 2. For n suﬃciently large, the variables YA+(0),... ,YA+(imax∧τ) form an (O(n/s),O(n1−21r ))-


![image 33](<2014-bohman-independent-neighborhoods-process_images/imageFile33.png>)

bounded submartingale, and the variables YA−(0),... ,YA−(imax ∧ τ) form an (O(n/s),O(n1−21r ))bounded supermartingale.

![image 34](<2014-bohman-independent-neighborhoods-process_images/imageFile34.png>)

Proof. We begin by ﬁxing a step 0 ≤ i ≤ imax, and we assume that i < τ. Throughout we write t = t(i), and note t(i + 1) = t + s−1 and that s−1 = D1/r/N = Θ(n1−1/r−r).

To aid the calculations to follow, we begin by estimating the quantity Ξ := f(t + s−1) − f(t).

Since f(t) = exp(Wtr + Wt), f′(t) and f′′(t) are products of f(t) with polynomials in t. As ζ ≪ max{1/W,ε}, tmax is polylogarithmic in n, and n is large, we have the crude bounds f(t) ≤ nǫ/2 and f′′(t) ≤ no(1)f′(t). Thus, by Taylor’s Theorem,

f′(t) s

Ξ −

![image 35](<2014-bohman-independent-neighborhoods-process_images/imageFile35.png>)

= O

maxt∗≤tmax f′′(t∗) s2

![image 36](<2014-bohman-independent-neighborhoods-process_images/imageFile36.png>)

= o

f′(t) s

![image 37](<2014-bohman-independent-neighborhoods-process_images/imageFile37.png>)

. (11)

Observe now that we may write

YA±(i + 1) − YA±(i) = (q(t + s−1) − q(t)) · n − (QA(i + 1) − QA(i)) ± Ξ · n1−ε.

(Note that this stands for the pair of equations in which each ± is replaced with + or with −, respectively.) We begin by establishing the boundedness claims: it is routine to verify that c(t) and c′(t) are bounded over the reals, implying

|q(t + s−1) − q(t) − c(t) · s−1| = O(s−2), (12) and so

n s

0 ≥ q(t + s−1) − q(t) · n ≥ −O

.

![image 38](<2014-bohman-independent-neighborhoods-process_images/imageFile38.png>)

As we have the bound |f′(t)| = nε/2+o(1) and (11), we have |Ξ| · n1−ε = o(n/s), and the lower bound in the boundedness claims follows. To establish the upper bounds, it remains to bound QA(i) − QA(i + 1). Consider the ‘next’ edge ei+1 ∈ O(i) and observe that

QA(i) − QA(i + 1) = | {ei+1} ∪ Cei+1(i) ∩ OA(i)|. We bound |Cei+1(i) ∩ OA(i)| by considering ﬁve cases depending on |ei+1 ∩ A|:

- Case 1: |ei+1 ∩ A| = 0. Let f ∈ OA(i) ∩ Cei+1(i): then f = A ∪ {v} for some vertex v, and since G(i)+ei+1 +f contains a copy of T(r), v ∈ ei+1 must hold. (Recall that every pair of edges in T(r) either shares exactly one or r − 1 vertices.) In this case, |Cei+1(i) ∩ OA(i)| ≤ |ei+1| = r.
- Case 2: |ei+1 ∩ A| = r − 1. In this case, we may write ei+1 = A ∪ {u1}. Now, let f = A ∪ {v} ∈ OA(i)∩Cei+1(i): since f ∩ei+1 = A and f ∈ Cei+1(i), there must exist vertices u2,... ,ur−1 ∈ Ni(A) so that {u1,... ,ur−1,v} ∈ E(i). As then v ∈ Ni({u1,... ,ur−1}), we may bound the number of such choices of v (and hence of f) in this case above by ∆r−1(G(i))r−1 ≤ ζr−1(nlog n)(r−1)/r. (Note the bound on the maximum degree follows as ZA(i) ≤ 0 since i < τ.)
- Case 3: |ei+1∩A| = 1. Write A = {x1,... ,xr−1}, where we take ei+1∩A = {x1}. Let f = A∪{v} ∈ Cei+1(i) ∩ OA(i), and suppose v ∈/ ei+1 (as there are at most r − 1 such v), so f ∩ ei+1 = {x1}. Consider a copy of T(r) in G(i)+ei+1 +f using both ei+1 and f as edges: without loss of generality, we may assume that one of ei+1,f maps to the edge b1 of T(r), the other to the edge a.

If ei+1 maps to b1, then the (r − 1)-set ei+1 \ {x1} maps to the common intersection B of b1,... ,br. Consequently v ∈ Ni(ei+1 \ {x1}) must hold, and so there are at most ∆r−1(G(i)) such r-sets f ∈ Cei+1(i) ∩ OA(i).

Otherwise, if ei+1 maps to the edge a and f maps to b1, then {x2,... ,xr−1,v} maps to the common intersection B. Thus, for each u ∈ ei+1\{x1} we have {u,x2,... ,xr−1,v} ∈ E(i), implying v ∈ Ni({u,x2,... ,xr−1}) and (as ei+1 is ﬁxed), there are again at most ∆r−1(G(i)) such choices of f. Thus, in this case we have |Cei+1(i) ∩ OA(i)| ≤ 2 + 2∆r−1(G(i)) = n1/r+o(1).

- Case 4: 1 < |ei+1∩A| = r−2. Let f = A∪{v} ∈ OA(i)∩Cei+1(i). Since |f ∩ei+1| ≥ |A∩ei+1| > 1, |f ∩ ei+1| = r − 1 must hold, implying v ∈ ei+1 and so |OA(i) ∩ Cei+1(i)| ≤ r as in Case 1.
- Case 5: 2 ≤ |ei+1 ∩ A| ≤ r − 3. In this case, |Cei+1(i) ∩ OA(i)| = 0, as every f ∈ OA(i) satisﬁes 1 ≤ |f ∩ ei+1| ≤ r − 2.


From the cases above it follows that QA(i) − QA(i + 1) = n(r−1)/r+o(1), and combining the above bounds, it follows that the sequences YA±(0),... ,YA±(imax ∧ τ) are (O(n/s),O(n1−21r ))-bounded.

![image 39](<2014-bohman-independent-neighborhoods-process_images/imageFile39.png>)

We turn now to the sub- and supermartingale claims: all expectation calculations to follow are implicitly conditioned on the history of the process up to step i, and we recall that we assume i < τ. For each open r-set f ∈ OA(i), we have f ∈/ OA(i + 1) if and only if ei+1 ∈ Cf(i) ∪ {f}. Thus,

E YA±((i + 1)) − YA±(i) = (q(t + s−1) − q(t)) · n +

f∈OA(i)

|Cf(i)| + 1 |O(i)|

± Ξ · n1−ε.

![image 40](<2014-bohman-independent-neighborhoods-process_images/imageFile40.png>)

To establish the submartingale claim, consider the following chain of inequalities:

(c(t) − N−γ) · D1/r (q(t) + N−γ) · N

|Cf(i)| + 1 |O(i)|

≥ (q(t) − f(t)n−ε) · n ·

![image 41](<2014-bohman-independent-neighborhoods-process_images/imageFile41.png>)

![image 42](<2014-bohman-independent-neighborhoods-process_images/imageFile42.png>)

f∈OA(i)

N−γ + f(t)n−ε q(t) + N−γ

n s

(c(t) − N−γ) ·

= 1 −

.

![image 43](<2014-bohman-independent-neighborhoods-process_images/imageFile43.png>)

![image 44](<2014-bohman-independent-neighborhoods-process_images/imageFile44.png>)

n s

≥ 1 − 2q(t)−1f(t)n−ε (c(t) − N−γ) ·

![image 45](<2014-bohman-independent-neighborhoods-process_images/imageFile45.png>)

n s

≥ c(t) − 2c(t)q(t)−1f(t)n−ε − N−γ ·

![image 46](<2014-bohman-independent-neighborhoods-process_images/imageFile46.png>)

n s

≥ c(t) − (2c(t)q(t)−1 + 1) · f(t)n−ε ·

.

![image 47](<2014-bohman-independent-neighborhoods-process_images/imageFile47.png>)

The ﬁrst inequality follows from the bounds given by (2) and (3) on the event Ti and as YA−(i) ≤ 0, since i < τ. In the second and fourth inequalities we bounded N−γ < f(t)n−ε, valid as f(t) ≥ 1

and ε ≪ γ. Thus, applying this bound and (12) gives

n1−ε s

1 s2

E YA+(i + 1) − YA+(i) ≥ Ξ · n1−ε − (2c(t)q(t)−1 + 1)f(t)

− O

![image 48](<2014-bohman-independent-neighborhoods-process_images/imageFile48.png>)

![image 49](<2014-bohman-independent-neighborhoods-process_images/imageFile49.png>)

n1−ε s

≥ Ξ · n1−ε − (2c(t)q(t)−1 + 2)f(t)

![image 50](<2014-bohman-independent-neighborhoods-process_images/imageFile50.png>)

n1−ε s by (11). Since f′(t) = (Wrtr−1 + W)f(t) and 2c(t)q(t)−1 = 2rtr−1, this ﬁnal bound is nonnegative for large n as W is large, and so YA+(0),... ,YA+(imax ∧ τ) forms a submartingale.

= (1 + o(1))f′(t) − (2c(t)q(t)−1 + 2)f(t) ·

![image 51](<2014-bohman-independent-neighborhoods-process_images/imageFile51.png>)

We similarly bound E[QA(i) − QA(i + 1)] above to establish the supermartingale claim: as 1 < N−γD1/r for large n, and as Ti holds and YA+(i) ≥ 0,

(c(t) + 2N−γ) · D1/r (q(t) − N−γ) · N

|Cf(i)| + 1 |O(i)|

≤ (q(t) + f(t)n−ε) · n ·

![image 52](<2014-bohman-independent-neighborhoods-process_images/imageFile52.png>)

![image 53](<2014-bohman-independent-neighborhoods-process_images/imageFile53.png>)

f∈OA(i)

N−γ + f(t)n−ε q(t) − N−γ

n s

(c(t) + 2N−γ) ·

= 1 +

![image 54](<2014-bohman-independent-neighborhoods-process_images/imageFile54.png>)

![image 55](<2014-bohman-independent-neighborhoods-process_images/imageFile55.png>)

n s

≤ 1 + 4q(t)−1f(t)n−ε (c(t) + 2N−γ) ·

![image 56](<2014-bohman-independent-neighborhoods-process_images/imageFile56.png>)

n s

≤ c(t) + (4c(t)q(t)−1 + 4)f(t)n−ε ·

.

![image 57](<2014-bohman-independent-neighborhoods-process_images/imageFile57.png>)

In addition to the bound N−γ ≤ f(t)n−ε used above, in the second inequality, we bounded q(t) − N−γ ≥ q(t)/2, and in the ﬁnal we bounded 2N−γ(1 + 4q(t)−1f(t)n−ε) ≤ 4f(t)n−ε as q(t)−1f(t)n−ε ≤ 1 which holds as 2Wζr < ǫ and n is large.

Thus,

n1−ε s

1 s2

E YA−(i + 1) − YA−(i) ≤ −Ξ · n1−ε + (4c(t)q(t)−1 + 4)f(t)

+ O

![image 58](<2014-bohman-independent-neighborhoods-process_images/imageFile58.png>)

![image 59](<2014-bohman-independent-neighborhoods-process_images/imageFile59.png>)

n1−ε s

≤ −Ξ · n1−ε + (4c(t)q(t)−1 + 5)f(t)

![image 60](<2014-bohman-independent-neighborhoods-process_images/imageFile60.png>)

n1−ε s

= −(1 + o(1))f′(t) + (4c(t)q(t)−1 + 5)f(t) ·

,

![image 61](<2014-bohman-independent-neighborhoods-process_images/imageFile61.png>)

and again, as W is large, this is strictly negative for n suﬃciently large. Thus, the sequence YA−(0),... ,YA−(imax ∧ τ) forms a supermartingale, completing the proof.

![image 62](<2014-bohman-independent-neighborhoods-process_images/imageFile62.png>)

![image 63](<2014-bohman-independent-neighborhoods-process_images/imageFile63.png>)

![image 64](<2014-bohman-independent-neighborhoods-process_images/imageFile64.png>)

![image 65](<2014-bohman-independent-neighborhoods-process_images/imageFile65.png>)

Since QA(0) = n − r + 1, YA+(0) = r − 1 + n1−ε and YA−(0) = r − 1 − n1−ε. Applying Lemmas

- 7 and 8, respectively, we have


n2−2ε

P YA+(imax ∧ τ) < 0 ≤ exp −Ω

![image 66](<2014-bohman-independent-neighborhoods-process_images/imageFile66.png>)

n s · ζs log1/r N · n1−21r )

![image 67](<2014-bohman-independent-neighborhoods-process_images/imageFile67.png>)

![image 68](<2014-bohman-independent-neighborhoods-process_images/imageFile68.png>)

= exp −n21r−2ε+o(1) < exp −n41r

![image 69](<2014-bohman-independent-neighborhoods-process_images/imageFile69.png>)

![image 70](<2014-bohman-independent-neighborhoods-process_images/imageFile70.png>)

(valid for large n as ε is small), and an identical calculation yields

P YA−(imax ∧ τ) > 0 ≤ exp −n41r . We have established (8) and (9). It remains to prove (10).

![image 71](<2014-bohman-independent-neighborhoods-process_images/imageFile71.png>)

- Claim 3. The variables ZA(0),... ,ZA(imax ∧ τ) form a (2n/N,2)-bounded supermartingale.


Proof. We begin by ﬁxing a step 0 ≤ i ≤ imax, and we assume that i < τ. Throughout we write t = t(i). Let f1(t) = f(t)q(t)−1 = exp((W+1)tr+Wt), and let Ξ1 := f1(t+s−1)−f1(t). By the same reasoning given in Claim 2, we may bound |f1(t)| < nε/2, say, for large n, and f1′′(t) ≤ no(1)f1′(t), and so

f1′(t) s

maxt∗<tmax f1′′(t∗) s2

f1′(t) s

Ξ1 −

= O

= o

. (13)

![image 72](<2014-bohman-independent-neighborhoods-process_images/imageFile72.png>)

![image 73](<2014-bohman-independent-neighborhoods-process_images/imageFile73.png>)

![image 74](<2014-bohman-independent-neighborhoods-process_images/imageFile74.png>)

Next, we observe that ZA(i + 1) − ZA(i) = di+1(A) − di(A) −

n N

− Ξ1 · n1/r−ε. The boundedness claim then follows for n suﬃciently large as 0 ≤ dA(i + 1) − dA(i) ≤ 1 and as

![image 75](<2014-bohman-independent-neighborhoods-process_images/imageFile75.png>)

|Ξ1| · n1/r−ε ≤ nε/2+o(1) · n1/r−ε · s−1 < n/N as s−1 = D1/r/N = Θ(n1−1/r/N).

Turning to the supermartingale condition, observe that di+1(A) = di(A) + 1 if and only if ei+1 lies in the set of open r-sets counted by QA(i). Conditioned on the history of the process up to step i, it follows that

QA(i) |O(i)|

n N

− Ξ1 · n1/r−ε

E[ZA(i + 1) − ZA(i)] =

−

![image 76](<2014-bohman-independent-neighborhoods-process_images/imageFile76.png>)

![image 77](<2014-bohman-independent-neighborhoods-process_images/imageFile77.png>)

(q(t) + f(t)n−ε) · n (q(t) − N−γ) · N

n N

− Ξ1 · n1/r−ε

−

≤

![image 78](<2014-bohman-independent-neighborhoods-process_images/imageFile78.png>)

![image 79](<2014-bohman-independent-neighborhoods-process_images/imageFile79.png>)

N−γ + f(t)n−ε (q(t) − N−γ)

n N

− Ξ1 · n1/r−ε ≤ (N−γ + f(t)n−ε) · 2q(t)−1 ·

·

=

![image 80](<2014-bohman-independent-neighborhoods-process_images/imageFile80.png>)

![image 81](<2014-bohman-independent-neighborhoods-process_images/imageFile81.png>)

n N

− Ξ1 · n1/r−ε

![image 82](<2014-bohman-independent-neighborhoods-process_images/imageFile82.png>)

n N

− Ξ1 · n1/r−ε

= (2q(t)−1N−γ + 2f1(t)n−ε) ·

![image 83](<2014-bohman-independent-neighborhoods-process_images/imageFile83.png>)

n N

≤ 4f1(t) · n−ε ·

![image 84](<2014-bohman-independent-neighborhoods-process_images/imageFile84.png>)

− Ξ1 · n1/r−ε (14)

Note that the ﬁrst inequality holds as Ti and YA+(i) ≥ 0 since i < τ, the second as q(t) − N−γ ≥ q(t)/2 since ζ ≪ γ, and the ﬁnal as N−γ ≤ f(t) · n−ε, since f(t) ≥ 1 and ε ≪ γ. Noting that for

large n, D ≥ nr−1/rr and so s−1 ≥ n1−1/r/(rN), by (13) we have

f1′(t) s

Ξ1 · n1/r−ε = (1 + o(1)) ·

· n1/r−ε

![image 85](<2014-bohman-independent-neighborhoods-process_images/imageFile85.png>)

Wf1(t) · n1−1/r rN

n1/r−ε >

≥ (1 + o(1)) ·

![image 86](<2014-bohman-independent-neighborhoods-process_images/imageFile86.png>)

n N

W 2r

· f1(t) · n−ε ·

.

![image 87](<2014-bohman-independent-neighborhoods-process_images/imageFile87.png>)

![image 88](<2014-bohman-independent-neighborhoods-process_images/imageFile88.png>)

Thus, since we assume W is large, the supermartingale condition follows now from (14). Finally, to show (10), we apply Lemma 8 to yield

![image 89](<2014-bohman-independent-neighborhoods-process_images/imageFile89.png>)

![image 90](<2014-bohman-independent-neighborhoods-process_images/imageFile90.png>)

![image 91](<2014-bohman-independent-neighborhoods-process_images/imageFile91.png>)

![image 92](<2014-bohman-independent-neighborhoods-process_images/imageFile92.png>)

n2/r−2ε

P[ZA(imax ∧ τ) > 0] ≤ exp −Ω

![image 93](<2014-bohman-independent-neighborhoods-process_images/imageFile93.png>)

n N · ζs log1/r N

![image 94](<2014-bohman-independent-neighborhoods-process_images/imageFile94.png>)

n2/r−2ε n1−(r−1)/r+o(1)

= exp −

![image 95](<2014-bohman-independent-neighborhoods-process_images/imageFile95.png>)

= exp −n1/r−2ε−o(1) which suﬃces as ε is small. This completes the proof of Lemma 6.

- 4.2 Proof of Lemma 4 We begin by letting


S = S(n) =

2ℓ r

− 2

ℓ r

,

and we note that S = Θ(kr).

We ﬁx a pair A,B of disjoint ℓ-element subsets of [n], and deﬁne the following sequences of random variables: for each step i ≥ 0, let

X+(i) = q(t) · S − QA,B(i) + f(t) · Sn−ε, and X−(i) = q(t) · S − QA,B(i) − f(t) · Sn−ε.

We next deﬁne the stopping time τ∗ to be the minimum of τA,B and the ﬁrst step i for which X+(i) ≤ 0, X−(i) ≥ 0, or the event Ti fails to hold.

Claim 4. The sequence X+(0),... ,X+(imax ∧ τ∗) forms a (O(kr/s),O(kr−1/n4ε))-bounded submartingale, and the sequence X−(0),... ,X−(imax ∧ τ∗) forms a (O(kr/s),O(kr−1/n4ε))-bounded supermartingale.

Proof. We ﬁx a step 0 ≤ i ≤ imax, and we suppose that i < τ∗. Throughout we write t = t(i), and note t(i + 1) = t + s−1 and that s−1 = D1/r/N = Θ(n1−1/r−r).

To aid the calculations to follow, we begin by estimating the quantity Ξ := f(t + s−1) − f(t). Recall equation (11):

f′(t) s

Ξ −

![image 96](<2014-bohman-independent-neighborhoods-process_images/imageFile96.png>)

= O

maxt∗≤tmax f′′(t∗) s2

![image 97](<2014-bohman-independent-neighborhoods-process_images/imageFile97.png>)

= o

f′(t) s

![image 98](<2014-bohman-independent-neighborhoods-process_images/imageFile98.png>)

.

Observe that we may write X±(i + 1) − X±(i) = (q(t + s−1) − q(t)) · S − (QA,B(i + 1) − QA,B(i)) ± Ξ · Sn−ε.

(As above, this stands for the pair of equations in which each ± is replaced with + or with −, respectively.) We begin by establishing the boundedness claims: by (12) and as S = Θ(kr), we have

kr s

0 ≥ q(t + s−1) − q(t) · S ≥ −O

.

![image 99](<2014-bohman-independent-neighborhoods-process_images/imageFile99.png>)

Next, bounding |f′(t)| ≤ nε/2+o(1),

kr s

|Ξ| · Sn−ε ≤ n−ε/2+o(1) ·

![image 100](<2014-bohman-independent-neighborhoods-process_images/imageFile100.png>)

In order to establish the boundedness part of the claim, it remains to bound the quantity QA,B(i+ 1) − QA,B(i). Let OA,B(i) denote the set of r-sets that are open with respect to the pair A,B in G(i), and let Oτ denote the set of all open r-sets whose selection as ei+1 would result in τA,B = i+1.

Now, if ei+1 ∈ Oτ, then QA,B(i + 1) − QA,B(i) = 0 by deﬁnition, and, otherwise, we have QA,B(i + 1) − QA,B(i) = −|OA,B(i) ∩ (Cei+1(i) ∪ {ei+1})|.

It suﬃces, then, to bound the quantity |Ce(i) ∩ OA,B(i)| for all e ∈ O(i) \ Oτ: ﬁx such an open r-set e. Now, for any f ∈ Ce(i) ∩ OA,B(i), there is a copy Tr,f of T(r) in the graph G(i) + e + f using both e and f as edges. Up to isomorphism, there are only three possibilities for the pair (e,f) in that copy: (e,f) maps to (b1,b2), or to (b1,a), or to (a,b1). We treat these three cases separately.

- Case 1: (e,f) maps to (b1,b2). In this case, the r − 1 vertices that map to the set R lie entirely in e, and f is the union of those r − 1 vertices along with another vertex lying in A ∪ B. Thus, we may bound the total number of such f above by rk.
- Case 2: (e,f) maps to (b1,a). Let R′ = e − f, the set of r − 1 vertices shared by all edges bj in this copy of T(r). Then f − e ⊆ Ni(R′): since f ∩ A = ∅ and f ∩ B = ∅ (as f ∈ OA,B(i)), and since

- e ∈/ Oτ, it follows that |Ni(R′) ∩ (A ∪ B)| ≤ k/n2ε. Thus, for a ﬁxed such choice of R′ there are fewer than (k/n2ε)r−1 such open r-sets f, yielding a total bound of at most r(k/n2ε)r−1.

Case 3: (e,f) maps to (a,b1). There exists an (r − 1)-set R′ ⊆ A ∪ B and a vertex v ∈ e so that

- f = R′ ∪ {v} and so that e \ {v} ⊆ Ni(R′). To bound the number of such f, it suﬃces to bound the number of (r − 1)-sets R′ ⊆ A ∪ B for which Ni(R′) contains (r − 1) vertices from e.




To that end, ﬁx a vertex v ∈ e and let Hv denote the (r −1)-uniform hypergraph on (A∪B)\e whose edges are the (r − 1)-subsets X for which Ni(X) ⊇ e \ {v}. We claim that

∆r−2(Hv) < 4r.

Suppose to the contrary that this does not hold: then there exist an (r − 2)-set Y ⊆ (A ∪ B) \ e and vertices x1,x2,... ,x4r ∈ (A ∪ B) \ (Y ∪ e) so that for each for each vertex u ∈ e \ {v}, {u} ∪ Y ∪ {xj} ∈ E(i) for 1 ≤ j ≤ 4r. It follows from Lemma 3 that such a conﬁguration does not appear in G(i). Indeed, as this conﬁguration spans 6r − 3 vertices and has 4r(r − 1) edges, the probability that such a conﬁguration appears is at most

n6r−3

i N

![image 101](<2014-bohman-independent-neighborhoods-process_images/imageFile101.png>)

4r(r−1)

= n6r−3−4(r−1)2+o(1) = o(1).

It follows that |Hv| < 4r r− k2 , and thus the total number of such open r-sets f as above is less than 4r2kr−2.

As ε is small and as k = n1/r+o(1), it follows that for large n we have

|Ce(i) ∩ OA,B(i)| ≤ rk + r · (k/n2ε)r−1 + 4r2kr−2 = O(kr−1/n2ε(r−1)), and as r ≥ 3 we conclude that

0 ≥ QA,B(i + 1) − QA,B(i) = −O(kr−1/n4ε).

Thus, it follows that the sequences X±(0),... ,X±(imax ∧ τ∗) are (O(kr/s),O(kr−1/n4ε))-bounded as claimed.

We now turn to the sub- and supermartingale claims, and we remark that all expectation and probability calculations to follow are implicitly conditioned on the history of the process up to step i. We begin by bounding the expected value of QA,B(i+1)−QA,B(i). Recall that we assume i < τA,B and that Oτ ⊆ O(i) consists of the open r-sets whose selection as ei+1 would yield τA,B = i + 1. We claim that

|Oτ| ≤ 4n2ε · k (15) To see this, let

[n] r − 1

: |Ni(X) ∩ (A ∪ B)| ≥ k/(2n2ε) .

R := X ∈

Then |R| < 4n2ε, which can be argued as follows. Suppose by way of contradiction that ∃S ⊆ R with |S| = 4n2ε. Let N = Y∈S(Ni(Y ) ∩ (A ∪ B)). By inclusion-exclusion and the fact that Lemma 3 implies that the co-degree of any pair of (r − 1)-sets is at most 5r (see (6)), we have

k ≥ |N| ≥ |S| · k/(2n2ε) − |S|25r ≥ 2k − 80rn4ε,

a contradiction as ε is small and k = n1/r+o(1). To deduce (15) it suﬃces to observe that each open r-set e ∈ Oτ can be written e = {v} ∪ X for some vertex v ∈ A ∪ B and (r − 1)-set X satisfying |Ni(X) ∩ (A ∪ B)| ≥ k/n2ε − 1 (and thus X ∈ R).

Conditioning on the event ei+1 ∈/ Oτ then yields

E[QA,B(i + 1) − QA,B(i)] = −

e∈OA,B(i)

by linearity of expectation. Consequently,

E X±(i + 1) − X±(i) = (q(t + s−1) − q(t)) · S +

|Ce(i) \ Oτ| |O(i)|

![image 102](<2014-bohman-independent-neighborhoods-process_images/imageFile102.png>)

|Ce(i) \ Oτ| |O(i)|

± Ξ · Sn−ε.

![image 103](<2014-bohman-independent-neighborhoods-process_images/imageFile103.png>)

e∈OA,B(i)

To establish the submartingale claim, we note ﬁrst that as r ≥ 3 and ε ≪ γ ≪ 1/r, from (15) we have |Oτ| = n1/r+2ε+o(1) < N−γ · D1/r. Now, as i < τ∗, Ti and X−(i) ≤ 0 hold, we have

(c(t) − 2N−γ)D1/r (q(t) + N−γ)N

|Ce(i) \ Oτ| |O(i)|

f(t) nε

≥ q(t) −

· S ·

![image 104](<2014-bohman-independent-neighborhoods-process_images/imageFile104.png>)

![image 105](<2014-bohman-independent-neighborhoods-process_images/imageFile105.png>)

![image 106](<2014-bohman-independent-neighborhoods-process_images/imageFile106.png>)

e∈OA,B(i)

N−γ + f(t)n−ε q(t) + N−γ

S s

(c(t) − 2N−γ) ·

= 1 −

![image 107](<2014-bohman-independent-neighborhoods-process_images/imageFile107.png>)

![image 108](<2014-bohman-independent-neighborhoods-process_images/imageFile108.png>)

S s

≥ 1 − 2q(t)−1f(t)n−ε (c(t) − 2N−γ) ·

![image 109](<2014-bohman-independent-neighborhoods-process_images/imageFile109.png>)

S s

≥ c(t) − 2c(t)q(t)−1f(t)n−ε − 2N−γ ·

![image 110](<2014-bohman-independent-neighborhoods-process_images/imageFile110.png>)

S s

≥ c(t) − (2c(t)q(t)−1 + 1)f(t)n−ε ·

.

![image 111](<2014-bohman-independent-neighborhoods-process_images/imageFile111.png>)

Note that these bounds follow for large n since f(t) ≥ 1 and ε ≪ γ imply N−γ ≤ f(t)n−ε/2. Applying this and (12) gives

Sn−ε s

1 s2

E X+(i + 1) − X+(i) ≥ Ξ · Sn−ε − (2c(t)q(t)−1 + 1)f(t)

− O

![image 112](<2014-bohman-independent-neighborhoods-process_images/imageFile112.png>)

![image 113](<2014-bohman-independent-neighborhoods-process_images/imageFile113.png>)

Sn−ε s

≥ Ξ · Sn−ε − (2c(t)q(t)−1 + 2)f(t)

![image 114](<2014-bohman-independent-neighborhoods-process_images/imageFile114.png>)

Sn−ε s

= (1 + o(1))f′(t) − (2c(t)q(t)−1 + 2)f(t) ·

![image 115](<2014-bohman-independent-neighborhoods-process_images/imageFile115.png>)

by (11). Since f′(t) = (Wrtr−1 + W)f(t) and 2c(t)q(t)−1 = 2rtr−1, this ﬁnal bound is nonnegative for large n as W is large, and so X+(0),... ,X+(imax ∧ τ) forms a submartingale.

Turning to the supermartingale claim, we take a similar approach and begin by noting as Ti holds and X+(i) ≥ 0,

(c(t) + N−γ)D1/r (q(t) − N−γ)N

|Ce(i) \ Oτ| |O(i)|

f(t) nε

≤ q(t) +

· S ·

![image 116](<2014-bohman-independent-neighborhoods-process_images/imageFile116.png>)

![image 117](<2014-bohman-independent-neighborhoods-process_images/imageFile117.png>)

![image 118](<2014-bohman-independent-neighborhoods-process_images/imageFile118.png>)

e∈OA,B(i)

N−γ + f(t)n−ε q(t) − N−γ

S s

(c(t) + N−γ) ·

= 1 +

![image 119](<2014-bohman-independent-neighborhoods-process_images/imageFile119.png>)

![image 120](<2014-bohman-independent-neighborhoods-process_images/imageFile120.png>)

S s

≤ 1 + 2q(t)−1f(t)n−ε (c(t) + N−γ) ·

![image 121](<2014-bohman-independent-neighborhoods-process_images/imageFile121.png>)

S s

≤ c(t) + (2c(t)q(t)−1 + 1)f(t)n−ε ·

.

![image 122](<2014-bohman-independent-neighborhoods-process_images/imageFile122.png>)

The supermartingale condition then follows in essentially the same way as the submartingale condition above.

![image 123](<2014-bohman-independent-neighborhoods-process_images/imageFile123.png>)

![image 124](<2014-bohman-independent-neighborhoods-process_images/imageFile124.png>)

![image 125](<2014-bohman-independent-neighborhoods-process_images/imageFile125.png>)

![image 126](<2014-bohman-independent-neighborhoods-process_images/imageFile126.png>)

Now, as X+(0) = Sn−ε, X−(0) = −Sn−ε, S = Θ(kr) and imax = s ·no(1), it follows from Claim

- 4 and Lemmas 7 and 8 that


P X+(imax ∧ τ∗) ≤ 0 ≤ exp −Ω

S2n−2ε kr

![image 127](<2014-bohman-independent-neighborhoods-process_images/imageFile127.png>)

s · knr4−ε1 · sno(1)

![image 128](<2014-bohman-independent-neighborhoods-process_images/imageFile128.png>)

![image 129](<2014-bohman-independent-neighborhoods-process_images/imageFile129.png>)

= exp −k · n2ε−o(1) .

Simillarly, we have

P X−(imax ∧ τ∗) ≥ 0 ≤ exp −k · n2ε−o(1) .

Since there are fewer than n2k = exp{2k log n} choices of the pair of sets A and B, Lemma 4 follows from the union bound.

# References

- [1] M. Ajtai, J. Komlo´s and E. Szemere´di: A Note on Ramsey Numbers. J. Comb. Theory Ser. A, 29 (1980) 354–360.
- [2] P. Bennett and T. Bohman, A note on the random greedy independent set algorithm, submitted, arXiv.1308.3732.
- [3] T. Bohman, The triangle-free process, Advances in Mathematics, 221 (2009) 1653–1677.
- [4] T. Bohman, A. Frieze, D. Mubayi, Coloring H-free hypergraphs, Random Structures and Algorithms, 36 (2010) 11–25.
- [5] T. Bohman and P. Keevash, The early evolution of the H-free process, Inventiones Mathematicae, 181 (2010) 291–336.
- [6] T. Bohman and P. Keevash, Dynamic concentration of the triangle-free process, submitted, arXiv.1302.5963.
- [7] J. Cooper, D. Mubayi, Coloring sparse hypergraphs, submitted, arXiv.1404.2895
- [8] G. Fiz Pontiveros, S. Griﬃths, R. Morris, The triangle-free process and R(3,k), submitted, arXiv.1302.6279.
- [9] J.H. Kim, The Ramsey number R(3,t) has order of magnitude t2/log t, Random Structures & Algorithms, 7 (1995) 173–207.
- [10] A. Kostochka, D. Mubayi, J. Verstrae¨te, On independent sets in hypergraphs, Random Structures & Algorithms, 44 224–239.
- [11] K. T. Phelps, V. Ro¨dl, Steiner triple systems with minimum independence number, Ars Combinatoria, 21 (1986) 167–172
- [12] J.B. Shearer: A note on the independence number of triangle-free graphs. Discrete Math. 46


(1983) 83–87.

- [13] J.B. Shearer: A note on the independence number of triangle-free graphs II. J. Combintorial Theory Series B, 2 300–307.
- [14] N. Wormald, The diﬀerential equation method for random graph processes and greedy algorithms, in Lectures on Approximation and Randomized Algorithms, M. Karonski and H.J. Pr¨omel, editors, 1999, pp. 73-155.


