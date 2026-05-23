arXiv:1609.07670v3[math.CO]26Dec2016

Variants of the Erd˝os-Szekeres and Erd˝os-Hajnal Ramsey problems

Dhruv Mubayi∗

October 3, 2018

Abstract

Given integers ℓ,n, the ℓth power of the path Pn is the ordered graph Pnℓ with vertex set v1 < v2 < ··· < vn and all edges of the form vivj where |i − j| ≤ ℓ. The Ramsey number r(Pnℓ,Pnℓ) is the minimum N such that every 2-coloring of [N2] results in a monochromatic copy of Pnℓ. It is well-known that that r(Pn1,Pn1) = (n − 1)2 + 1. For ℓ > 1, Balko-Cibulka-Kr´alKynˇcl proved that r(Pnℓ,Pnℓ) < cℓn128ℓ and asked for the growth rate for ﬁxed ℓ. When ℓ = 2, we improve this upper bound substantially by proving r(Pn2,Pn2) < cn19.5. Using this result, we determine the correct tower growth rate of the k-uniform hypergraph Ramsey number of a (k+1)-clique versus an ordered tight path. Finally, we consider an ordered version of the classical Erdo˝s-Hajnal hypergraph Ramsey problem, improve the tower height given by the trivial upper bound, and conjecture that this tower height is optimal.

# 1 Introduction

Let Kn be the complete graph on n vertices. An ordered path Ps is the graph whose vertices are ordered as v1 < ··· < vs and its edges are v1v2,v2v3,... ,vs−1vs. The Ramsey number r(Ps,Pn) is the minimum N such that every red/blue coloring of [N2] results in a red copy of Ps or a blue copy of Pn. Note that Ps usually stands for the (unordered) path but since we only consider ordered paths in this paper, we have taken the liberty to use Ps for the ordered path (similarly, Kn refers to the ordered or unordered clique). A similar comment applies to the notation r(Ps,Pn) that we have employed here. Usually this stands for unordered Ramsey numbers but since we exclusively consider ordered Ramsey numbers in this paper, we have chosen to keep this notation and hope that there will be no confusion. Further, there is not yet a standard notation for ordered Ramsey numbers in the literature as these numbers have only recently been considered systematically ([1] uses “R”, [4] uses “r<”, [12] uses “OR”, [13] uses “N” and [14] and the current paper use “r”).

![image 1](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile1.png>)

Let f(s,n) be the minimum N such that every sequence of N distinct real numbers contains an increasing subsequence of length s or a decreasing subsequence of length n. The famous Erd˝osSzekeres monotone subsequence theorem [10] states that f(s,n) = (s−1)(n−1)+1. This function is closely related to r(Ps,Pn). Indeed, it is trivial that r(Ps,Pn) ≥ f(s,n) while several proofs for

![image 2](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile2.png>)

∗Department of Mathematics, Statistics, and Computer Science, University of Illinois, Chicago, IL, 60607 USA. Research partially supported by NSF grant DMS-1300138. Email: mubayi@uic.edu

f(s,n) ≤ (s−1)(n−1) also give the same upper bound for r(Ps,Pn) (see [13] for a further discussion about this). Consequently, it is well-known that r(Ps,Pn) = (s − 1)(n − 1) + 1. This implies that for ﬁxed s, the Ramsey number r(Ps,Pn) is a polynomial function in n (in fact a linear function). On the other hand, r(n,n) = r(Kn,Kn) has exponential growth rate. We begin by considering the case of ordered graphs that are denser than paths but sparser than cliques.

Deﬁnition 1. Given ℓ ≥ 1, the ℓth power Psℓ of a path Ps has ordered vertex set v1 < ··· < vs and edge set {vivj : |i −j| ≤ ℓ}. The Ramsey number r(Psℓ,Pnℓ) is the minimum N such that every red/blue coloring of [N2] results in a red copy of Psℓ or a blue copy of Pnℓ.

Note that Ps1 = Ps. Conlon-Fox-Lee-Sudakov [4] asked whether r(Pnℓ,Pnℓ) is polynomial in n for every ﬁxed ℓ ≥ 1. Actually, the problem in [4] is about the Ramsey number of ordered graphs with

bandwidth at most ℓ but Pnℓ contains all such graphs so an upper bound for Pnℓ provides an upper bound for the bandwidth problem. This question was answered by Balko-Cibulka-Kra´l-Kyncˇl [1]

who proved an upper bound cℓn128ℓ and asked (Problem 2 of [1]) for the growth rate of r(Pnℓ,Pnℓ) (subsequently, a diﬀerent proof was also sketched in [4]). The proof of our ﬁrst result gives a slightly

worse polynomial growth rate of r(Pnℓ,Pnℓ) than in [1] for large ℓ but a much better one for small ℓ, in particular for ℓ = 2. Note that the bound in [1] for ℓ = 2 is cn256.

Theorem 2. There is an absolute constant c > 0 such that r(Pn2,Pn2) < cn19.487 for all n > 1.

Our second result is an application of Theorem 2 to a hypergraph Ramsey problem. Indeed, this hypergraph Ramsey problem is what motivated us to consider proving Theorem 2.

Deﬁnition 3. A k-uniform tight path of size s, denoted by Ps, comprises a set of s vertices that are ordered as v1 < ··· < vs, and edges (vj,vj+1,... ,vj+k−1) for j = 1,2,... ,s − k + 1. The length of Ps is the number of edges, s − k + 1. Given (ordered) k-graphs F1,F2, the Ramsey number rk(F1,F2) or r(F1,F2) is the minimum N such that every red/blue coloring of the edges of the complete N-vertex k-graph KNk , whose vertex set is [N], contains a red copy of F1 or a blue copy of F2.

The famous cups-caps theorem of Erd˝os and Szekeres [10] implies that r3(Ps,Pn) = n+s−s−24 +1. The author and Suk [14] considered the closely related problem of determining rk(Ps,n) := rk(Ps,Knk) and showed that determining the tower height of r4(P5,n) is equivalent to the notorious conjecture of Erd˝os-Hajnal and Rado on the tower height of r3(n,n). The results in [14] focused on ﬁxed s and large n and there are no nontrivial results for the opposite case, namely for rk(s,Pn). Given the close connection between this problem and the problem of determining classical Ramsey numbers, it would be of interest to obtain the growth rate in this range as well. Here we settle the ﬁrst open case. Recall that the tower function twri(x) is deﬁned by twr1(x) = x and twri+1(x) = 2twri(x).

Theorem 4. For n large, r3(4,Pn) < n21 and more generally for each k ≥ 3, there exists c > 0 such that for n large,

twrk−2(nc) < rk(k + 1,Pn) < twrk−2(n62).

The main open problem here is to prove that r3(5,Pn) has polynomial growth rate and more generally that r3(s,Pn) has polynomial growth rate for all ﬁxed s ≥ 4. The corresponding results for higher uniformity follow easily from the case k = 3.

Our ﬁnal topic considers a version of the well-known Erd˝os-Hajnal hypergraph Ramsey problem with respect to tight paths. In order to shed more light on classical hypergraph Ramsey numbers, Erd˝os and Hajnal [7] in 1972 considered the following more general parameter.

Deﬁnition 5. (Erdo˝s-Hajnal [7]) For integers 2 ≤ k < s < n and 2 ≤ t ≤ k s , let rk(s,t;n) be the minimum N such that every red/blue coloring of the edges of KNk results in a monochromatic blue copy of Knk or has a set of s vertices which induces at least t red edges.

Note that by deﬁnition rk(s,n) = rk(s, k s ;n) so rk(s,t;n) includes classical Ramsey numbers. The main conjecture of Erd˝os and Hajnal states that as t grows from 1 to k s , there is a well-deﬁned value t1 = h(1k)(s) at which rk(s,t1 − 1;n) is polynomial in n while rk(s,t1;n) is exponential in a power of n, another well-deﬁned value t2 = h(2k)(s) at which it changes from exponential to double exponential in a power of n and so on, and ﬁnally a well-deﬁned value tk−2 = h(kk−)2(s) < k s at which it changes from twrk−2 to twrk−1 in a power of n. They were not able to oﬀer a conjecture as to what h(ik)(s) is in general, except when i = 1 (for which Erd˝os oﬀered $500) and when s = k +1. For the latter, they conjectured that hi(k)(k +1) = i+2. This was solved for all but three i recently by the author and Suk [15] via the following result.

Theorem 6. (Mubayi-Suk [15]) For 4 ≤ t ≤ k −2, there are positive c = c(k,t) and c′ = c′(k,t) such that

twrt−1(c′nk−t+1 log n) ≥ rk(k + 1,t; n) ≥

twrt−1(cnk−t+1) if k − t is even twrt−1(cn(k−t+1)/2) if k − t is odd.

Here we consider the very same problem in the ordered setting by replacing Knk with Pn.

Deﬁnition 7. For integers 2 ≤ k < s < n and 2 ≤ t ≤ k s , let rk(s,t;Pn) be the minimum N such that every red/blue coloring of the k-sets of [N] results in a monochromatic blue copy of Pn or has a set of s vertices which induces at least t red edges.

Of course, rk(s, k s ;Pn) = rk(s,Pn). We will focus our attention on the smallest case s = k + 1. Our main contribution here is the following conjecture which parallels the Erd˝os-Hajnal conjecture

for cliques. Conjecture 8. For 3 ≤ t ≤ k, there are positive c = c(k,t) and c′ = c′(k,t) such that

twrt−2(nc) < rk(k + 1,t;Pn) < twrt−2(nc′).

This conjecture seems more diﬃcult than the original problem of Erd˝os and Hajnal. For over 40 years the gaps in the bounds for the Erd˝os-Hajnal problem were between exponential and tower functions. Theorem 6 shows that the correct growth rate is a tower function. For Conjecture 8 the gap is again between an exponential and a tower function but unfortunately the constructions used for Theorem 6 fail.

Using standard arguments, it is easy to prove an upper bound of the form twrt−1(nc) in Conjecture 8 (see [15] for details). We improve this upper bound to the tower height given by Conjecture 8.

- Theorem 9. For all 3 ≤ t ≤ k there exists c = c(k) such that rk(k + 1,t;Pn) < twrt−2(cn2k).

We make some further modest progress towards Conjecture 8 in the cases t = 3 and (k,t) = (4,4) by proving sharper bounds. Note that Theorem 4 determines the correct tower height of rk(k+1,t;Pn) when t = k + 1; it is k − 2 = t − 3 so the formula diﬀers from that in Conjecture 8.

- Theorem 10. The following bounds hold:


- (a) rk(k + 1,3;Pn) ≤ 16n for n ≥ k ≥ 3
- (b) 2n − 2 ≤ r3(4,3;Pn) ≤ 3n − 4 for n ≥ 3
- (c) r4(5,4;Pn) ≥ 2n−2 + 1 for n ≥ 2.


We are not ready to oﬀer a conjecture about the tower growth rate of rk(s,t;Pn) as t grows from

- 2 to k s for s > k + 1.


In all our results where we ﬁnd either a long (ordered) blue Pn or a small red structure (Theorems 4, 9,10) our proof actually ﬁnds an ordered blue hypergraph that contains Pn. We call this hypergraph a broom (see Deﬁnition 11). Using brooms we can load the induction hypothesis suitably to carry out the induction step. Perhaps this is one of the main new ideas in this work.

# 2 Proof of Theorem 2

We will prove Theorem 2 by using bounds on the Ramsey multiplicity problem introduced by Erd˝os [6]. This problem asks for the largest α = α(ℓ) such that every 2-edge coloring of KN yields at least (α − o(1))Nℓ monochromatic copies of Kℓ. Erd˝os [6] observed that α(ℓ) > 0 for all ℓ ≥ 4. The best known bounds for α(ℓ) for large ℓ are very far apart and can be found in [2, 18]. We will use the speciﬁc result α(4) > 0.0287/4! = 0.00119583 that was recently proved using Flag Algebras in [16] (see also [17]). Note that log2(1/α(4)) < 9.7434. After this paper was written, we learned that the approach of using ramsey multiplicity for ordered Ramsey problems was also used in [4].

![image 3](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile3.png>)

Proof of Theorem 2. Let α = α(4) be the constant from the Ramsey multiplicity problem above. Let ǫ = 10−9 and choose c such that every red/blue coloring of [N2] for N > c results in at least (α − ǫ)N4 monochromatic copies of K4. We will prove that

r(Pa2,Pb2) ≤ c(ab)9.7435 for all a,b ≥ 2. This immediately gives the bounds we seek by letting a = b = n.

We will proceed by induction on a + b. If a = 2 then the trivial upper bound is b < c(2b)9.7435 and the same holds if b = 2. For the induction step, suppose we have a red/blue coloring of [N2] with N = c(ab)9.7435 > c. By the choice of c, we obtain at least (α − ǫ)N4 monochromatic copies of K4. Assume without loss of generality that half of these copies are red. To each such copy with vertex set x0 < x1 < x2 < x3 associate the middle pair of vertices x1,x2. By the pigeonhole principle there exists a set Y = y1 < y2 that is the middle pair for at least ((α−ǫ)/2)N4/ N2−2 > (α−2ǫ)N2 = βN2 red copies of K4. Let L be the set of smallest vertices y0 in these red K4s and let R be the set of largest vertices y3 in these red K4s. Note that all edges between Y and L ∪ R are red and that

|L||R| is the number of the red copies of K4 that we are working with. If |L| = γN < βN, then, since L and R are disjoint, |R| ≤ (1 − γ)N and so

βN2 ≤ |L||R| ≤ γ(1 − γ)N2 < β(1 − β)N2.

Consequently, |L| ≥ βN and similarly |R| ≥ βN. By induction and log2(1/α) < 9.7434, |L| ≥ βN = βc(ab)9.7435 > c(1/2)9.7435(ab)9.7435 ≥ r(P⌊2a/2⌋,Pb2).

Now we apply the induction hypothesis to ﬁnd either a red P⌊2a/2⌋ or a blue Pb2 in L. If the latter occurs we are done so we get the former. The same argument applies to R. Therefore, we obtain

two red copies of P⌊2a/2⌋, one in L and the other in R. Consider these two copies together with Y . Since the distance between vertices in L and vertices in R is at least 3, and Y is connected to all

vertices in L ∪ R by red edges, this yields a red copy of P22⌊a/2⌋+2 which contains a red copy of Pa2 because 2⌊a/2⌋ + 2 ≥ a.

![image 4](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile4.png>)

![image 5](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile5.png>)

![image 6](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile6.png>)

![image 7](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile7.png>)

# 3 Proof of Theorem 4

Deﬁnition 11. The (ordered) broom Ba,mk is the k-graph with vertices v1 < v2 < ··· < va < w1 < ··· < wm such that v1,... ,va is a tight k-graph path and we also have all the edges va−k+2 ··· vawj for all j ∈ [m].

We will omit the superscript k in Ba,mk in all future usage as it will be obvious from the context. For example, in the proof below k = 3.

Theorem 12. r3(4,Pn) < 6nm where m = r(Pn2,Pn2).

Proof. Recall that we are using the notation Pn for a 3-uniform tight path and Pn2 for the square of a 2-uniform (i.e. graph) ordered path. We will prove that every red/blue coloring χ of [N3] , where N = 6nm yields either a red K43, or a blue Pn. Assume that there is no red K43. We will show that there there is a blue Pn or a blue Ba,m for all 2 ≤ a ≤ n within the ﬁrst 6am vertices. Since Pn ⊂ Bn,m this will prove the result. Let us show that there is a blue Pn or a blue Ba,m in [6am] by induction on a. For the base case a = 2, we seek a pair of vertices v1 < v2 and at least m vertices w > v2 within [12m] such that v1v2w is blue. If we cannot ﬁnd these m vertices for any pair v1,v2, then the number of blue edges is at most 122m (m − 2) < 1/4 123m so the number of red edges is more than (3/4) 123m and a simple averaging argument shows that we would have a red K43, contradiction.

Now for the induction step, assume that we have a blue copy of Ba−1,m in [6(a−1)m] and we wish

- to augment this to a blue copy of Ba,m in [6am]. Suppose that the vertex set of the blue Ba−1,m is v1 < v2 < ··· < va−1 < w1 < ··· < wm.


Deﬁne the red/blue coloring φ of the complete graph on {w1,... ,wm} by φ(wiwj) = χ(va−1wiwj). By deﬁnition of m, we get a copy H of a monochromatic Pn2 under φ with vertices z1 < ··· < zn.

Suppose H is red under φ. The four vertices va−1,zi,zi+1,zi+2 have three red edges, so χ(zizi+1zi+2) is blue for all i. We conclude that z1 < ··· < zn is a blue Pn.

Next, suppose H is blue under φ. Fix i and consider the three vertices zi,zi+1,zi+2. If there are at least m edges zizi+1y with y ≤ 6am and χ(zizi+1y) is blue, then we can use these edges to form a blue copy of Ba,m in [6am] with vertices

v2 < ··· < va−1 < zi < zi+1 < Y

where Y is the set of these y. So the number of such y is at most m, and the same is true for the pairs zi+1,zi+2 and zi,zi+2. Since 6am − 6(a − 1)m = 6m > 3m there is a vertex y such that χ(zizi+1y) = χ(zizi+2y) = χ(zi+1zi+2y) and these are all red. Therefore χ(zizi+1zi+2) is blue. Since this argument applies for each i, we obtain a blue Pn under χ with vertices z1 < ··· < zn.

![image 8](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile8.png>)

![image 9](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile9.png>)

![image 10](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile10.png>)

![image 11](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile11.png>)

Proof of Theorem 4. The case k = 3 of Theorem 4 follows immediately from Theorem 2 and

- Theorem 12. The lower bound for general k follows from the lower bound for rk(Pk+1,Pn) in [12, 13] (see also [5]). The upper bound for general k follows from the upper bound when k = 3 (as a base case) and the standard pigeonhole argument for hypergraph Ramsey numbers due to Erd˝os and Rado (see the proof on pages 421-423 in [9] for the original argument, or [11], or Section 2 of [3], or Section 2 of [15]). Applying this argument from k = 3 to k = 4 raises the exponent of n by a factor of 3 (from slightly less than 20.5 to slightly less than 61.5) and subsequent applications do not aﬀect the exponent of n.

![image 12](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile12.png>)

![image 13](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile13.png>)

![image 14](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile14.png>)

![image 15](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile15.png>)

4 Proof of Theorem 9

Let fk(n) be the minimum N such that every red/blue coloring of [Nk] results in a blue Pn or a set S of k + 1 vertices with at least 3 red edges, one of which consists of the smallest k vertices in

S. Let Hk(3) denote the set of ordered k-graphs with three red edges as described above. We will abuse notation by saying a copy of Hk(3) when we mean a copy of some H ∈ Hk(3).

- Theorem 13. fk(n) ≤ 2n2 for all n > k ≥ 3.


Proof. We will prove that every red/blue coloring χ of [Nk] , where N = 2n2 yields either a red Hk(3) or a blue Pn. Assume that there is no red Hk(3). We will show that there is a blue Pn or a blue Bn−1,n. Since Pn ⊂ Bn−1,n this will prove the result. We will prove that there is a blue Bn−1,n by showing that there is a blue Ba,n in [2an] for all 1 ≤ a ≤ n − 1 by induction on a. The base case a = 1 is trivial since B1,n is just a collection of n + 1 vertices (with no edge since k ≥ 3) and 2n > n + 1.

Now for the induction step, assume that we have a blue copy B of Ba−1,n in [2(a−1)n] and we wish

- to augment this to a blue copy of Ba,n in [2an]. Suppose that the vertex set of the blue Ba−1,n is v1 < v2 < ··· < va−1 < w1 < ··· < wn.


Let V = {v1,... ,va−1} and W = {w1,... ,wn}. For each 0 ≤ j ≤ k, let Sj = {va−j,... ,va−1} denote the j largest vertices of V .

Claim. For every i ∈ [k] and P ∈ Wi , χ(Sk−i ∪ P) is blue. Proof of Claim. Let us proceed by induction on i. The base case i = 1 is trivial, due to the deﬁnition of B. Indeed, if a − 1 ≥ k − 1, then all k-sets of the form Sk−1 ∪ {w} for w ∈ W are blue. If a − 1 < k − 1 there is nothing to check. For the induction step, let i ≥ 2 and suppose for contradiction that χ(Sk−i ∪ P) is red for some P ∈ Wi .

Let P1,P2 be two distinct (i − 1)-sets contained in P. Note that i ≥ 2 means that that i− i1 ≥ 2 so such P1,P2 exist. Suppose that there are n vertices w1′ < w2′ < ··· < wn′ ≤ 2an such that

- w1′ > wn and χ(Sk−i ∪ P1 ∪ {wi′}) is blue. Then V ∪ P1 ∪ {w1′ ,... ,wn′ } is a blue Ba+i−2,n which contains a blue Ba,n in [2an] as required. Indeed, it suﬃces to check that χ(Sk−j ∪ Qj) is blue for all j ≤ i − 1, where Qj is the set of j smallest vertices of P1. But Qj ∈ Wj and j < i so this is true by induction on i. We conclude that the number of such vertices wi′ is at most n − 1 and the same assertion holds for P1 replaced by P2. This gives at most 2n − 2 vertices between wn and 2an. Since wn ≤ 2(a − 1)n = 2an − 2n, there exists a w such that wn < w ≤ 2an such that both χ(Sk−i ∪ P1 ∪ {w}) and χ(Sk−i ∪ P2 ∪ {w}) are red. This means that we have a red copy of Hk(3) in Sk−i ∪ P ∪ {w}, contradiction.


Now we simply apply the Claim with i = k to conclude that all k-sets of Wk are blue, and this is a blue clique with n vertices which contains a blue Pn.

![image 16](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile16.png>)

![image 17](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile17.png>)

![image 18](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile18.png>)

![image 19](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile19.png>)

- Proof of Theorem 9. Let fk(k+1,t;Pn) be the minimum N such that every red/blue coloring of [N]

k results in a blue Pn or a set S of k +1 vertices with at least t red edges, one of which consists of the smallest k vertices in S. We observe that fk(k + 1,t;Pn) < 2(fk−1(k,tk−1;Pn−1)). Indeed, this follows from the standard pigeonhole argument for hypergraph Ramsey numbers due to Erd˝os and Rado (see the proof on pages 421-423 in [9] for the original argument, or [11], or Section 2 of [3] or Section 2 of [15]). When applying this argument, we must note that the initial red edge in the (k − 1)-graph gives rise to two red edges in the k-graph, one of which is again an initial edge. We apply this recurrence t − 3 times until we have a (k − t + 3)-graph. As k ≥ t, Theorem 13 now applies to give fk−t+3(k − t + 4,3;Pn) = fk−t+3(n) ≤ 2n2 and this yields the result.

![image 20](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile20.png>)

![image 21](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile21.png>)

![image 22](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile22.png>)

![image 23](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile23.png>)

5 Proof of Theorem 10

Let us ﬁrst prove the t = 3 case of Theorem 10 by improving the quadratic bound in Theorem 13 to a linear bound. Let F(3) be the collection of ordered k-graphs with k + 1 vertices and at least three edges.

- Proof of Theorem 10 (a). We are to show that rk(k + 1,3;Pn) ≤ 16n for all n ≥ k ≥ 3. We


will prove that every red/blue coloring χ of [N3] , where N = 16n yields either a red H ∈ F(3) or a blue Pn. Assume that there is no red H ∈ F(3). We will show that there is a blue Bn−1,6. As Pn ⊂ Bn−1,6 this will prove the result. We will prove that there is a blue Bn−1,6 by showing that there is a blue Ba,6 for all k − 1 ≤ a < n within the ﬁrst 16(a + 1) vertices by induction on a. For the base case a = k − 1, we seek k − 1 vertices v1 < ··· < vk−1 and at least 6 vertices w > vk−1 within [16k] such that v1 ··· vk−1w is blue. If we cannot ﬁnd these 6 vertices for any (k − 1)-set v1 < ··· < vk−1, then the number of blue edges in [16k] is at most 5 k 16−k1 . A short calculation

shows that this is less than ((k − 1)/(k + 1)) 16kk since k ≥ 3. Consequently, the number of red edges is more than (2/(k + 1)) 16kk and an easy averaging argument then implies that there is a red H ∈ F(3), contradiction.

Now for the induction step, assume that we have a blue copy of Ba−1,6 in [16a] and we wish to augment this to a blue copy of Ba,6 in [16(a+1)]. Suppose that the vertex set of the blue Ba−1,6 is

v1 < v2 < ··· < va−1 < w1 < ··· < w6.

For q ∈ {k − 1,k − 2,k − 3}, let Sq = {va−q,... ,va−1} be the greatest q vertices among the vi. Deﬁne the red/blue coloring φ of the complete graph on {w1,... ,w6} by φ(wiwj) = χ(Sk−2wiwj). Since r(3,3) ≤ 6, we obtain a monochromatic triangle T under φ. If T is red, then T ∪ Sk−2 yields a red member of F(3) which is a contradiction, so T is blue. Assume for simplicity that T = w1 <

- w2 < w3. Fix 1 ≤ i < j ≤ 3. If there are at least 6 edges Sk−3wiwjy with w3 < y ≤ 16(a + 1) and χ(Sk−3wiwjy) is blue, then we can use these edges to form a blue copy of Ba,m in [16(a + 1)] with vertices


v2 < ··· < va−1 < wi < wj < Y where Y is the set of these y. So the number of such y is at most 5, and the same is true for all three pairs {i,j}. Since 16(a + 1) − 16a = 16 > 15 there is a vertex y such that χ(Sk−3w1w2y) = χ(Sk−3w1w3y) = χ(Sk−3w2w3y) and these are all red. This gives a red member of F(3), contradiction.

![image 24](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile24.png>)

![image 25](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile25.png>)

![image 26](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile26.png>)

![image 27](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile27.png>)

- Proof of Theorem 10 (b). For the lower bound, consider the ordering of 2n − 3 points v1,v1′ < v2,v2′ < ··· < vn−2,vn′ −2 < vn−1.


For all i < j, color the triples vivi′vj red. Color all other triples blue. No blue path Pq can contain both vi and vi′ unless they appear at the end of Pq. If no such pair is in Pq then clearly q ≤ n − 1. If vi,vi′ are both in Pq, then they lie at the end of the path, and q ≤ (i − 1) + 2 = i + 1 ≤ n − 1. Hence there is no blue Pn. If we have four points with two red edges, then two of these triples must be vivi′a and vivi′b for some vi < a,b. But then there cannot be any other red edge among these points.

For the upper bound, we will prove the following stronger statement by induction on n: r3(4,3;Bn−1,2) ≤ 3n − 3.

Since Pn ⊂ Bn−1,2, this will prove the upper bound. The base case n = 3 is true due to the following simple argument. Suppose we have a red/blue coloring of [6]3 . If there are two edges of the form 12i that are blue then we have a blue B2,2 so there is at most one such edge. This means that there are 2 < i < j < k ≤ 6 such that 12x is red for all x ∈ S = {i,j,k}. If any edge of the form 1xy or 2xy is red for x,y ∈ S, then {1,2,x,y} has three red edges, so all such edges are blue. This means that 1ij and 1ik are both blue, giving a blue B2,2.

Now for the induction step, assume that N = 3n − 3 and we have a red/blue coloring χ of the triples of [N] with no four points containing three red edges. By induction, we obtain a blue Bn−2,2 in [N − 3]. Say the vertices of this Bn−2,2 are

v1 < ··· < vn−2 < vn−1 < vn′ −1.

Let S = {N − 2,N − 1,N}. If there are two blue edges of the form vn−2vn−1x and vn−2vn−1y for x,y ∈ S, then we have obtained a blue copy of Bn−1,2 with x = vn and y = vn′ . So at most one of these edges is blue. The same applies to vn−2vn′ −1x and vn−2vn′ −1y. Since |S| = 3, there is w ∈ S such that both vn−2vn−1w and vn−2vn′ −1w are red. Now consider the four vertices vn−2,vn−1,vn′ −1,w. We have identiﬁed two red edges among them so vn−2vn−1vn′ −1 and vn−1vn′ −1w are blue. If there exists z ∈ S − {w} such that χ(vn−1vn′ −1z) is blue, then we obtain a copy of Bn−1,2 as follows:

v2 < ··· < vn−2 < vn−1 < vn′ −1 < w < z or v2 < ··· < vn−2 < vn−1 < vn′ −1 < z < w.

Therefore χ(vn−1vn′ −1a) = χ(vn−1vn′ −1b) and both are red, where S = {a,b,w} with a < b. If χ(vn−2vn−1x) is blue for some x ∈ {a,b}, then we obtain the blue Bn−1,2

v1 < ··· < vn−2 < vn−1 < vn′ −1 < x.

Hence χ(vn−2vn−1x) is red for both x ∈ {a,b}. The four vertices vn−2,vn−1,vn′ −1,x contain the two red edges vn−2vn−1x and vn−1vn′ −1x so χ(vn−2vn′ −1x) is blue for x ∈ {a,b}. This gives us

v1 < ··· < vn−2 < vn′ −1 < a < b which is a blue Bn−1,2, and the proof of r3(4,3;Bn−1,2) ≤ 3n − 3 is complete. Observe that r3(4,3;Pn) ≤ r3(4,3;Bn−1,2) − 1 by taking an optimal construction for r3(4,3;Pn), adding a new largest vertex v and coloring all triples containing v with blue.

![image 28](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile28.png>)

![image 29](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile29.png>)

![image 30](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile30.png>)

![image 31](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile31.png>)

- Proof of Theorem 10 (c). We are to show that r4(5,4;Pn) ≥ 2n−2 + 1. Let us proceed by induction on n. The case n = 2 is trivial, so assume we have a construction for n − 1 that uses the vertices [2n−3]. To obtain the construction for n, take a copy of the construction for n − 1 among the vertices {2n−3 +1,... ,2n−2}. It remains to color 4-sets that intersect both halves of [2n−2]. We color all the 4-sets that have exactly two points in each half red and all other 4-sets blue. Let us ﬁrst argue that no 5 points contain 4 red edges. If all 5 points lie in one half then we are done by induction. If the distribution of points is 4 + 1 then we again have at most one red edge and if the distribution is 3+2 then we have exactly three red edges. The other cases are of course symmetric. Next we argue that there is no blue Pn. Such a blue Pn cannot have two points in both halves as the 2 + 2 edges are red so all but one point must lie in one half. This gives a blue Pn−1 in one half which cannot exist by induction.


![image 32](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile32.png>)

![image 33](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile33.png>)

![image 34](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile34.png>)

![image 35](<2016-mubayi-variants-erd-s-szekeres-erd_images/imageFile35.png>)

Acknowledgment. I am grateful to Andrew Suk for many helpful discussions on this topic, to David Conlon for informing me about the results in [1, 4], and to both referees who read the paper very carefully and provided many comments that improved the presentation.

# References

- [1] M. Balko, J. Cibulka, K. Kra´l, J. Kyncˇl, Ramsey numbers of ordered graphs, submitted. arXiv:1310.7208. Extended abstract in: Proceedings of The Eight European Conference on Combinatorics, Graph Theory and Applications (EuroComb 2015), Electronic Notes in Discrete Mathematics 49 (2015), 419-424.


- [2] D. Conlon, On the Ramsey multiplicity of complete graphs, Combinatorica 32 (2012), 171-186.
- [3] D. Conlon, J. Fox, and B. Sudakov, Hypergraph Ramsey numbers, J. Amer. Math. Soc. 23

(2010), 247–266.

- [4] D. Conlon, J. Fox, C. Lee, B. Sudakov, Ordered Ramsey numbers, to appear in J. Combin. Theory Ser. B.
- [5] D. Duﬀus, H. Lefmann, V. Ro¨dl, Shift graphs and lower bounds on Ramsey numbers rk(l;r), Discrete Mathematics 137 (1995), 177–187.
- [6] P. Erd˝os, On the number of complete subgraphs contained in certain graphs. Magyar tud. Akad. Mat. Kutato´ Int. Ko¨zl., 7: 459464, 1962.
- [7] P. Erd˝os and A. Hajnal, On Ramsey like theorems, problems and results, Combinatorics (Proc. Conf. Combinatorial Math., Math. Inst., Oxford, 1972), pp. 123–140, Inst. Math. Appl., Southhend-on-Sea, 1972.
- [8] P. Erd˝os, A. Hajnal, and R. Rado, Partition relations for cardinal numbers, Acta Math. Acad. Sci. Hungar. 16 (1965), 93–196.
- [9] P. Erd˝os, R. Rado, Combinatorial theorems on classiﬁcations of subsets of a given set, Proc. London Math. Soc. (3) 2 (1952), 417–439.
- [10] P. Erd˝os and G. Szekeres, A combinatorial problem in geometry, Compos. Math. 2 (1935), 463–470.
- [11] R. Graham, B. Rothschild, and J. Spencer, Ramsey Theory, 2nd ed., Wiley, New York, 1990.
- [12] K.G. Milans, D. Stolee, and D. West, Ordered Ramsey theory and track representations of graphs, to appear in J. Combinatorics.
- [13] G. Moshkovitz and A. Shapira, Ramsey-theory, integer partitions and a new proof of the Erd˝os-Szekeres theorem, Advances in Mathematics 262 (2014), 1107–1129.
- [14] D. Mubayi, A. Suk, Oﬀ-diagonal hypergraph Ramsey numbers, J. Combin. theory Ser. B, accepted.
- [15] D. Mubayi, A. Suk, The Erd˝os-Hajnal hypergraph Ramsey problem, submitted.
- [16] S. Nieß, Counting monochromatic copies of K4: a new lower bound for the Ramsey multiplicity problem, http://arxiv.org/pdf/1207.4714v1.pdf.
- [17] K. Sperfeld, On the minimal monochromatic K4-density, https://arxiv.org/pdf/1106.1030.pdf.
- [18] A. Thomason, A disproof of a conjecture of Erd˝os in Ramsey theory. J. London Math. Soc.


(2), 39(2):246255, 1989.

