arXiv:1307.2159v2[math.CO]19Jul2013

A NOTE ON THE DISCREPANCY OF MATRICES WITH BOUNDED ROW AND COLUMN SUMS

NICHOLAS J. A. HARVEY∗

Abstract. A folklore result uses the Lova´sz local lemma to analyze the discrepancy of hypergraphs with bounded degree and edge size. We generalize this result to the context of real matrices with bounded row and column sums.

1. Introduction

In combinatorics, discrepancy theory is the study of red-blue colorings of a hypergraph’s vertices such that every hyperedge contains a roughly equal number of red and blue vertices. A classic survey on this topic is [3].

Many combinatorial discrepancy results have a more general form as a geometric statement about discrepancy of real vectors [3, §4]. Some examples include the Beck-Fiala theorem [2] and Spencer’s “six standard deviations” theorem [6]. One exception is the following folklore result on the discrepancy of hypergraphs of bounded degree and edge size [7, pp. 693] [4, Proposition 12].

- Theorem 1. Let H be a hypergraph of maximum degree ∆ and maximum edge size R. Then there is a red-blue coloring of the vertices such that, for every edge e, the numbers of red and blue vertices in e diﬀer by at most 2 R ln(R∆).

![image 1](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile1.png>)

The proof is a short exercise using the Lov´asz local lemma. We show that this theorem also has a more general form as a geometric statement about discrepancy of real vectors. Theorem 2 recovers Theorem 1 (up to constants) by letting Vi,j ∈ {0,1} indicate whether vertex j is contained in edge i. Let vi denote the ith row of V and vj denote the jth column of V . As usual, let [n] = {1,... ,n} and let  · p denote the ℓp-norm.

- Theorem 2. Let V be an n × m real matrix with |Vi,j| ≤ 1, vi 1 ≤ R, and vj 1 ≤ ∆ for all i ∈ [n],j ∈ [m]. Assume that R ≥ max{∆,4} and ∆ ≥ 2. There exists y ∈ {−1,+1}m with

V y ∞ ≤ O( R log(R∆)).

![image 2](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile2.png>)

2. The Proof

Theorem 2 follows as an easy corollary of the next theorem, by rescaling the vectors and separately considering the positive and negative coordinates. Let lg x denote the base-2 logarithm of x.

- Theorem 3. Let A be a non-negative real matrix of size n×m, and let a1,... ,am ∈ Rn≥0 denote its columns. Assume that β ≤ min {δ/2,1/4} and δ ≤ 1. Suppose that


≤ 1,

• j aj

∞

![image 3](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile3.png>)

∗Department of Computer Science, University of British Columbia. Email: nickhar@cs.ubc.ca. Supported by an NSERC Discovery Grant and a Sloan Foundation Fellowship.

1

- • aj ∞ ≤ β for every j, and
- • aj 1 ≤ δ for every j.


√2. Then there exists a vector y ∈ {−1,+1}m such that

![image 4](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile4.png>)

![image 5](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile5.png>)

Deﬁne α := lg(δ/β2) ≥

![image 6](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile6.png>)

Ay ∞ ≤ 16α β.

We now prove Theorem 3. Suppose we choose the vector y ∈ {−1,+1}m uniformly at random. The discrepancy of row i is the value | j Ai,jyj|. Our goal is to bound Ay ∞ = maxi | j Ai,jyj|, which is the maximum discrepancy of any row.

One annoyance in analyzing Ay ∞ is that the entries of A can have wildly diﬀering magnitudes. The natural approach is to stratify: to partition each row of A into sets whose entries all have roughly the same magnitude. Deﬁne b := ⌊−lg β⌋ ≥ 2, so that every entry of every A is at most 2−b. For k ≥ b, let

Si,k = { j : ⌊−lg Ai,j⌋ = k }

be the locations of the entries in row i that take values in (2−(k+1),2−k]. To bound the discrepancy of row i, we will actually bound the discrepancy of each set Si,k

(i.e., | j∈Si,k Ai,jyj|). By the triangle inequality, the total discrepancy of row i is at most the sum of the discrepancies of each Si,k.

Deﬁne

- (1) ǫ := 8α β > 8 β.

![image 7](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile7.png>)

![image 8](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile8.png>)

Let Ei,k be the event that the discrepancy of Si,k exceeds

- (2) Tk := ǫ j∈Si,k

Ai,j + α2−k/2.

We can analyze the probability of Ei,k by a Hoeﬀding bound: if {Xi}i≤ℓ are independent random variables, each Xi ∈ [−1,+1], and X = X1 + ··· + Xℓ, then Pr[ |X| > a] ≤ 2e−a2/2ℓ. Applying this bound to the discrepancy of Si,k, we get that

Pr [Ei,k ] ≤ 2exp − (Tk2k)2/2|Si,k| < 2exp −

ǫ2 2|Si,k|

![image 9](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile9.png>)

2k j∈S

i,k

Ai,j

2

−

2ǫ 2|Si,k|

![image 10](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile10.png>)

α2k/2 2k j∈S

i,k

Ai,j

≤ 2exp −

ǫ2 8 |Si,k| −

![image 11](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile11.png>)

ǫ 2

![image 12](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile12.png>)

- (3) α2k/2 =: pi,k,,


where the last inequality uses j∈S

i,k

Ai,j ≥ 2−(k+1)|Si,k|.

- 2.1. Discrepancy assuming no events occur. Suppose that none of the events Ei,k happen. Then the total discrepancy of row i is at most

k≥b

Tk = ǫ

k≥b j∈Si,k

Ai,j + α

k≥b

2−k/2

≤ ǫ + α

k≥b

2−k/2 (since we assume mj=1Ai,j ≤ 1)

= ǫ + α

2−b/2 1 − 2−1/2

![image 13](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile13.png>)

≤ ǫ + 4α 2β (since 2−b ≤ 2−(lg(1/β)−1) = 2β)

![image 14](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile14.png>)

(4) ≤ 16α β.

![image 15](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile15.png>)

- 2.2. Avoiding the events. We will use the local lemma to show that, with positive probability, none of the events Ei,k occur. To do so, we must show that these events have limited dependence. Consider Ei,k, which is the event that the elements in row i of value roughly 2−k have large discrepancy. This event depends only on the random values { yj : j ∈ Si,k }. We will bound the total failure probability of the events that depend on those random values.


The local lemma can be stated as follows [1, Theorem 5.1.1]:

- Theorem 4. Let E1,... ,Em be events in a probability space. Let Γ(Ei) be the events (other than Ei itself) which are not independent of Ei. If one can associate a value x(Ei) ∈ (0,1) with each event Ei such that


- (5) Pr [Ei ] ≤ x(Ei) · F∈Γ(Ei)

1 − x(F)

then, with positive probability, no event Ei occurs. The weight that we assign to Ei,k is

- (6) x(Ei,k) := 2exp − ǫ2|Si,k|/16 − ǫα2k/2/2 .


Comparing to (3), we see that this value is closely related to (but slightly larger than) pi,k, which is our upper bound on the probability of Ei,k.

- Claim 5. x(Ei,k) < 1/2 for every i ∈ [n] and k ≥ b. Proof. By (1) we have ǫ > 4√β, so


![image 16](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile16.png>)

√

√

![image 17](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile17.png>)

![image 18](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile18.png>)

ǫ2k/2 ≥ ǫ

![image 19](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile19.png>)

![image 20](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile20.png>)

2b ≥ ǫ 2lg(1/β)−1 ≥ ǫ 1/2β > 2

2. It follows that x(Ei,k) ≤ 2exp(−ǫ2k/2/2) < 2exp(−

√2) < 1/2.

![image 21](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile21.png>)

Our next step is to characterize Γ(Ei,k), the events that are dependent on Ei,k. We let Cj,k be the events corresponding to all entries of value roughly 2−k in the jth column.

Cj,k := { Ei,k : ⌊−lg Ai,j⌋ = k } (for j ∈ [m], k ≥ b)

Next, Yj contains all events corresponding to all entries in the jth column. In other words, Yj is the set of all events that depend on the random variable yj.

Yj :=

Cj,k = Ei,⌊−lgAi,j⌋ : i ∈ [n] (for j ∈ [m])

k≥b

Finally, since Ei,k depends only on the random labels of elements in Si,k, the set Γ(Ei,k) consists of all events that depend on any of those labels.

Γ(Ei,k) =

Yj.

j∈Si,k

- Claim 6. For every event Ei,k, inequality (5) is satisﬁed.


Proof. The main goal of the proof is to give a good lower bound for F∈Γ(E

i,k)(1−x(F)). Claim 5 shows that x(F) ≤ 1/2, so

- (7) F∈Γ(Ei,k)

(1 − x(F)) ≥

F∈Γ(Ei,k)

exp(−2x(F)) = exp − 2

F∈Γ(Ei,k)

x(F) .

So it suﬃces to give a good upper bound for F∈Γ(E

i,k) x(F). First we need to derive an inequality that is rather brutal, but suﬃces for our proof.

ǫ · α2k/2/2 = 8α β · α2k/2/2 (by (1))

![image 22](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile22.png>)

= α2 · 2 β · 21+b/2+(k−b)/2

![image 23](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile23.png>)

= lg(δ/β2) · 2 β2b/2 · 21+(k−b)/2 ≥ b + lg(δ/β) · 21+(k−b)/2 (since lg(1/β) ≥ b and 2b/2 ≥ 1/2β) ≥ b + lg(δ/β) + 21+(k−b)/2 (since xy ≥ x + y if x,y ≥ 2) ≥ b + lg(δ/β) + (k − b) (since 21+i/2 ≥ i for all i ≥ 0)

![image 24](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile24.png>)

![image 25](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile25.png>)

- (8) = k + lg(δ/β)


Next, consider all the events that depend on yj. Then

x(F) =

F∈Yj

≤

≤

x(F)

k≥b F∈Cj,k

exp(−ǫα2k/2/2) (by (6))

k≥b F∈Cj,k

|Cj,k| · e−(k+lg(δ/β)) (by (8))

k≥b

i : Ai,j ∈ (2−k−1,2−k] · 2−(k+lg(δ/β)) ≤ (β/δ) · (2δ) = 2β,

≤

k≥b

since the jth column sums to δ. Therefore

x(F) =

F∈Γ(Ei,k)

x(F) ≤ 2|Si,k|β.

j∈Si,k F∈Yj

Combining this with (7), we obtain the lower bound

x(Ei,k) ·

(1 − x(F)) ≥ x(Ei,k) · exp − 2

x(F)

F∈Γ(Ei,k)

F∈Γ(Ei,k)

≥ 2exp − ǫ2|Si,k|/16 − ǫα2k/2/2 · exp − 4|Si,k|β

= 2exp − |Si,k|(ǫ2/16 + 4β) − ǫα2k/2/2 ≥ 2exp − |Si,k|ǫ2/8 − ǫα2k/2/2

= pi,k ≥ Pr[ Ei,k ]

where the penultimate inequality holds because ǫ2/8 ≥ ǫ2/16 + 4β, which follows because ǫ ≥ 8√β (cf. (1)). This proves (5).

![image 26](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile26.png>)

The previous claim shows that the hypotheses of the local lemma are satisﬁed. So there exists a vector y ∈ {−1,+1}m such that none of the events Ei,k hold. As in (4), this implies that every row has discrepancy at most 16α√β. In other words, Ay ∞ ≤ 16α√β. This completes the proof of Theorem 3.

![image 27](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile27.png>)

![image 28](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile28.png>)

3. Conclusion

Many discrepancy theorems on hypergraphs have a more general statement about the discrepancy of real-valued matrices [3, §4]. We have provided another occurrence of this phenomenon by proving Theorem 2, which generalizes Theorem 1.

We are not aware of any result showing that either Theorem 1 or 2 is optimal. It seems conceivable that the logarithmic factor could be removed. Conjecture 7. Let V be an n × m real matrix with |Vi,j| ≤ 1, vi 1 ≤ R, and vj 1 ≤ ∆ for all i ∈ [n],j ∈ [m]. Assume R ≥ ∆. There exists y ∈ {−1,+1}m with V y ∞ ≤ O(√R).

![image 29](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile29.png>)

Let us mention now the recent discrepancy result of Marcus et al. [5], which implies a solution to the long-standing Kadison-Singer problem. Theorem 8 (Corollary 1.3 of Marcus et al. [5]). Let u1,... ,um ∈ Cn satisfy mi=1 uiu∗i = I and

ui 22 ≤ δ for all i. Then there exists y ∈ {−1,+1}m such that mi=1 yiuiu∗i ≤ O(√δ), where  ·  is the ℓ2-operator norm.

![image 30](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile30.png>)

There is a relationship between Theorems 3 and 8, in the sense that both are implied by the following conjecture. Theorem 8 is the special case where each Ai has rank one, and Theorem 3 implies (ignoring the additional logarithmic factor α) the special case where each Ai is a diagonal matrix.

Conjecture 9. Let A1,... ,Am be Hermitian, positive semi-deﬁnite matrices of the same size satisfying mi=1 Ai = I and trAi ≤ δ for all i. There exists y ∈ {−1,+1}m with mi=1 yiAi ≤ O(√δ).

![image 31](<2013-harvey-note-discrepancy-matrices-bounded_images/imageFile31.png>)

References

- [1] N. Alon and J. Spencer. The Probabilistic Method. Wiley, 2000.
- [2] J´ozsef Beck and Tibor Fiala. “Integer-making” theorems. Discrete Applied Mathematics, 3(1):1–8, 1981.
- [3] J´ozsef Beck and Vera T. S´os. Discrepancy theory. In R. Graham and M. Gr¨tschel and L. Lova´sz, editor, Handbook of Combinatorics, pages 1405–1446. Elsevier Science B.V., 1995.


- [4] Be´la Bollob´s, David Pritchard, Thomas Rothvoss, and Alex Scott. Cover-decomposition and polychromatic numbers. SIAM Journal on Discrete Math. to appear.
- [5] Adam Marcus, Daniel A. Spielman, and Nikhil Srivastava. Interlacing Families II: Mixed Characteristic Polynomials and The Kadison-Singer Problem, June 2013. http://arxiv.org/abs/1306.3969.
- [6] Joel Spencer. Six standard deviations suﬃce. Trans. Amer. Math. Soc., 289:679–706, 1985.
- [7] Aravind Srinivasan. Improving the discrepancy bound for sparse matrices: better approximations for sparse lattice approximation problems. In Proceedings of the 8th Annual ACM-SIAM Symposium on Discrete Algorithms, pages 692–701, 1997.


