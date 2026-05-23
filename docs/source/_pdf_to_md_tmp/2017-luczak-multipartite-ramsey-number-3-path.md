arXiv:1706.08937v1[math.CO]27Jun2017

THE MULTIPARTITE RAMSEY NUMBER FOR THE 3-PATH OF LENGTH THREE

TOMASZ  LUCZAK AND JOANNA POLCYN

Abstract. We study the Ramsey number for the 3-path of length three and n colors and show that R(P33;n) ≤ λ0n + 7√n, for some explicit constant λ0 = 1.97466 ....

![image 1](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile1.png>)

1. Introduction

Let P33 be the 3-uniform hypergraph with the set of vertices {a, b, c, d, e, f, g} and the set of edges {{a, b, c}, {c, d, e}, {e, f, g}}. The Ramsey number R(P33; n) is the smallest integer N such that any coloring of the edges of the complete 3-uniform hypergraph KN3 on N vertices with n colors leads to a monochromatic copy of P33. It is easy to see that R(P33; n) ≥ n + 6 (see [2, 4]) and it is believed that this lower bound is sharp, i.e. that R(P33; n) = n + 6. However, so far this conjecture has been conﬁrmed only for n ≤ 10 (see [4, 6, 9, 10]). On the other hand, from the fact that for N ≥ 8 each P33-free 3-uniform hypergraph H on N vertices satisﬁes

- (1) |H| ≤

N − 1 2

, (see [1] and [5]), it follows that

R(n; P33) ≤ 3n. In [7] the authors of this note improved the above upper bound to

- (2) R(n; P33) ≤ 2n + √18n + 1 + 2.


![image 2](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile2.png>)

Our argument relied on the fact that for 2-graphs the analogous multicolored Ramsey number for a ‘usual’ 2-path of length three is know to be 2n + O(1), where the small hidden constant O(1) depends only on divisibility of n by 3 (see [3]). Thus, it seemed the method we used

![image 3](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile3.png>)

2010 Mathematics Subject Classiﬁcation. Primary: 05D10, secondary: 05C38,

05C55, 05C65. Key words and phrases. Ramsey number, hypergraphs, paths. The ﬁrst author partially supported by NCN grant 2012/06/A/ST1/00261.

1

- in [7] could not be applied directly to get an upper bound better than (λ + o(1))n, for λ < 2.

The main result of this note is to match our previous approach with later results from [8] and get the following estimate for R(P33; n). Theorem 1. Let

f(γ) = (γ3 − 3γ2 + 6γ − 6)2 − 72γ(2 − γ)(γ − 1)2.

and let λ0 = 1.97466 . . . be the solution to the equation f(γ) = 0, such that f(γ) > 0 whenever γ ∈ (λ0, 2). Then

R(P33; n) ≤ λ0n + 7√n.

![image 4](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile4.png>)

2. Proof of Theorem 1 Our argument is based on the following decomposition lemma proved

- in [8]. Before we state it we need some deﬁnitions. We call a 3-graph H quasi-bipartite if one can partition its set of vertices into three sets: X = {x1, x2, . . ., xs}, Y = {y1, y2, . . ., ys}, and Z = {z1, z2, . . ., zt} in such a way that all the edges of H can be written as {xi, yi, zj} for some i = 1, 2, . . ., s, and j = 1, 2, . . ., t. By a star with center v we mean any 3-graph in which each edge contains v. Then the following holds.


- Lemma 2. For any P33-free 3-graph H there exists a partition of its set of vertices V = VR ∪VT ∪VS, such that subhypergraphs of H deﬁned as HR = {h ∈ H : h ∩ VR = ∅}, HT = H[VT] and HS = H \ (HR ∩ HT) = {h ∈ H[V \ VR] : h ∩ VS = ∅} satisfy the following three conditions:

- (i) |HR| ≤ 6|VR|,
- (ii) HT is quasi-bipartite and |HT| ≤ |VT|2/8,
- (iii) HS is a family of disjoint stars such that centers of these stars


are in VT whereas all other vertices are in VS, and |HS| ≤ |V

S|

2 . The following lemma is a direct consequence of the above result.

- Lemma 3. Let H be a P33-free 3-graph H on N ≥ 95 such that for some s, (N + 3)/2 ≤ s ≤ N − 46, we have


N − s 2

s − 1 2

|H| ≥

,

+

and let H = HR ∪ HT ∪ HS be a decomposition of H as described in Lemma 2. Then HS contains a star on at least s vertices.

Proof. Let V = VR ∪ VT ∪ VS be a partition of the set of vertices H given by Lemma 2. Note that |VS| ≥ s − 1, since otherwise

(N − |VS|)2 8 ≤

|H| ≤ 6|VR| + |VT|2 8

|VS| 2

+ |VS| 2 ≤

+

![image 5](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile5.png>)

![image 6](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile6.png>)

(N − s + 2)2 8

N − s 2

s − 1 2

s − 2 2

.

+

<

+

![image 7](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile7.png>)

Recall that HS is a collection of disjoint stars. Suppose that the largest of these stars consists of at most s − 1 > N/2 vertices. Then one

can easily verify that the number of edges in HS is maximised if HS consists of two stars on s−1 and |VS|−(s−1)+2 vertices respectively. Consequently

|H| ≤ 6|VR| + |VT|2 8

+ |VS| − s + 2

s − 2 2

+

![image 8](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile8.png>)

2 ≤

N − s 2

s − 1 2

N − s + 1 2

s − 2 2

+

<

+

,

again contradicting the fact that |H| ≥ s−21 + N2−s . Thus, HS contains a star on at least s vertices.

Proof of Theorem 1. We show that if for given integers N and n one can ﬁnd a coloring of edges of KN3 by n colors without monochromatic copies of P33, then γ = (N − 7√n)/n < λ0 where λ0 is deﬁned in Theorem 1. Some parts of our argument are quite technical and, since we aim to prove the statement for every n, we start with few remarks which makes our future computations a bit easier.

![image 9](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile9.png>)

Note that since λ0 > 1.97, we may assume that γ > 1.9. Moreover,

due to (2), it is enough to consider γ < 2. Finally, since R(n; P33) ≤ 3n we can restrict to the case n ≥ 41 (and hence N > 122) because otherwise 3n < 1.9n + 7√n.

![image 10](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile10.png>)

Thus, for n ≥ 41 and 1.9 < γ < 2, let us consider a coloring of edges of KN3 , N = γn + 7√n, by n colors without monochromatic copies of P33, and let Hi denote the P33-free hypergraph generated by the i-th color.

![image 11](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile11.png>)

We say that the ith color is rich if

n + 6√n − 1 2

N − n − 6√n 2

![image 12](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile12.png>)

![image 13](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile13.png>)

- (3) |Hi| ≥


+

.

- Claim 4. At least βn colors are rich, where


γ3 − 3γ2 + 6γ − 6 6(γ − 1)

.

β =

![image 14](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile14.png>)

Proof. Due to technical calculations it will be convenient to show the statement by contradiction. Denote the number of rich colors by βn and assume that

- (4) β <

γ3 − 3γ2 + 6γ − 6 6(γ − 1)

![image 15](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile15.png>)

<

1 3

![image 16](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile16.png>)

Since by (1), for each i ∈ [n] we have |Hi| ≤ N2−1 ,

N 3

< βn

N − 1 2

+n(1−β)

n + 6√n − 1 2

![image 17](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile17.png>)

+

N − n − 6√n 2

![image 18](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile18.png>)

.

Now substituting N = γn + 7√n and putting all leading terms on the left hand side of the equation we arrive at

![image 19](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile19.png>)

[(γ3 − 3γ2 + 6γ − 6) − β(6γ − 6)]n3 < [β(36γ − 30) − (21γ2 − 6γ − 30)]n5/2

+ [(β(42 − 6γ) − (150γ − 3γ2 − 105)]n2 − [6β + 400 − 42γ]n3/2 − [2γ − 153]n − 14√n.

![image 20](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile20.png>)

But for 1.9 < γ < 2 and 0 ≤ β < 1/3 the right hand side of the above equation is smaller than −19n5/2 − 157n2 − 316n3/2 + 150n − 14√n which, in turn, is negative for all natural n. Consequently,

![image 21](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile21.png>)

[(γ3 − 3γ2 + 6γ − 6) − β(6γ − 6)]n3 < 0, and thus

β >

γ3 − 3γ2 + 6γ − 6 6(γ − 1)

![image 22](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile22.png>)

, contradicting (4).

Recall that each Hi is P33-free and so one can apply to it Lemma 2 to get a decomposition of Hi into three graphs, HRi ∪ HTi ∪ HSi . For all i ∈ [n] let us ‘uncolor’ all the triples in HRi and mark them ‘blank’, and set Hˆi = HTi ∪ HSi . Let Gi be the graph whose edges are pairs which belong to at least two hyperedges of Hˆi and fewer than 6√n blank triples. Note that, because of the structure of Hˆi, Gi is a forest consisting of stars.

![image 23](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile23.png>)

We say that an edge of Gi is private if it is not an edge of any other graph Gj, j = i, and public otherwise. By ei and e′i we denote the number of private and public edges of Gi, respectively. The weight w(Gi) of Gi is deﬁned as

w(Gi) = ei + e′i/2. Since Gi is a forest we have also

- (5) w(Gi) ≤ ei + e′i < N.


Note that at most 3 ni=1 |HRi |

3 ni=1 6N 6√n

= 3√nN = 3√n(γn + 7√n) < 6n3/2 + 21n

6√n ≤

![image 24](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile24.png>)

![image 25](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile25.png>)

![image 26](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile26.png>)

![image 27](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile27.png>)

![image 28](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile28.png>)

![image 29](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile29.png>)

![image 30](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile30.png>)

pairs of KN2 belong to at least 6√n blank triples. Since by the pigeonhole principle all pairs which are contained in fewer than 6√n blank

![image 31](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile31.png>)

![image 32](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile32.png>)

triples are edges of at least one Gi, we have N 2 − 6n3/2 − 21n ≤

w(Gi).

- (6)


i∈[n]

Let us make the following easy yet crucial observation.

- Claim 5. If a color i is rich, then Gi contains more than 2w(Gi) − N private edges. All of them form a star. Proof. Since Gi is a forest we have ei + e′i < N. Thus,


w(Gi) = ei + e′i/2 < ei + N/2 − ei/2 = (ei + N)/2,

and so Gi contains more than 2w(Gi) − N private edges. Note also that, by Lemma 3, HSi contains the unique largest star F on at least n + 6√n vertices. Let us denote the center of this star by w. Then each edge of Gi which does not contain w is clearly contained in fewer than N −n−6√n hyperedges of Hˆi and so belongs to at least n triples of j =i Hˆj. Thus, by the pigeonhole principle, each such edge must be public. Consequently, all private edges must contain w and form in Gi a large star.

![image 33](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile33.png>)

![image 34](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile34.png>)

Let I denote the set of all rich colors. As an immediate corollary of Claim 5, we get the following inequality

(2w(Gi) − N) <

i∈I

ei ≤

i∈I

|I| 2

+ |I|(N − |I|))

which leads to

w(Gi) ≤ N|I| − |I|2/4 − |I|/4 .

i∈I

Thus, using (5) and (6) we get N 2 − 6n3/2 − 21n ≤

i∈[n]

w(Gi) =

w(Gi)

w(Gi) +

i∈I

i/∈I

< N|I| − |I|2/4 − |I|/4 +

N

i/∈I

= N|I| − |I|2/4 − |I|/4 + (n − |I|)N ≤ nN − |I|2/4.

Hence, using the estimate for the size of I given by Claim 4 we arrive at

2 n2 2 ≤

γ3 − 3γ2 + 6γ − 6 6(γ − 1)

|I|2 2

N 2

+ 12n3/2 + 42n.

< 2nN − 2

![image 35](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile35.png>)

![image 36](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile36.png>)

![image 37](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile37.png>)

Now substituting N = γn + 7√n and putting all leading terms on the left hand side of the inequality results in the following formula

![image 38](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile38.png>)

72(γ − 1)2 − γ(2 − γ) n2 < (26−14γ)n3/2+(γ−7)n+7√n. But for 1.9 < γ < 2 and n ≥ 2 we have

(γ3 − 3γ2 + 6γ − 6)2

![image 39](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile39.png>)

![image 40](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile40.png>)

(26 − 14γ)n3/2 + (γ − 7)n + 7√n < 0, and so

![image 41](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile41.png>)

(γ3 − 3γ2 + 6γ − 6)2

72(γ − 1)2 − γ(2 − γ) n2 < 0. Consequently,

![image 42](<2017-luczak-multipartite-ramsey-number-3-path_images/imageFile42.png>)

(γ3 − 3γ2 + 6γ − 6)2 < 72γ(2 − γ)(γ − 1)2, which implies that γ is smaller than λ0 deﬁned in Theorem 1. References

- [1] Z. F¨uredi, T. Jiang, R. Seiver, Exact solution of the hypergraph Tur´an problem for k-uniform linear paths, Combinatorica 34(3) (2014) 299–322.
- [2] A. Gy´arf´s, G. Raeisi, The Ramsey number of loose triangles and quadrangles in hypergraphs, Electron. J. Combin. 19(2) (2012), # R30.
- [3] R.W. Irving, Generalised Ramsey numbers for small graphs, Discrete Math. 9

(1974) 251–264.

- [4] E. Jackowska, The 3-color Ramsey number for a 3-uniform loose path of length 3, Australas. J. Combin. 63(2) (2015) 314–320.
- [5] E. Jackowska, J. Polcyn, A. Ruci´nski, Tur´an numbers for 3-uniform linear paths of length 3, Electron. J. Combin. 23(2) (2016), #P2.30
- [6] E. Jackowska, J. Polcyn, A. Ruci´nski, Multicolor Ramsey numbers and restricted Tur´an numbers for the loose 3-uniform path of length three, arXiv:1506.03759v1.


- [7] T.  Luczak, J. Polcyn, On the multicolor Ramsey number for 3-paths of length three, Electron. J. Combin. 24(1) (2017), #P1.27.
- [8] T.  Luczak, J. Polcyn, Paths in hypergraphs: a rescaling phenomenon, arXiv:1706.08465.
- [9] J. Polcyn, One more Tur´an number and Ramsey number for the loose 3-uniform path of length three, Discuss. Math. Graph Theory 37 (2017) 443–464.
- [10] J. Polcyn, A. Ruci´nski, Reﬁned Tur´an numbers and Ramsey numbers for the loose 3-uniform path of length three, Discrete Math. 340 (2017) 107–118.


Adam Mickiewicz University, Faculty of Mathematics and Computer

Science, Umultowska 87, 61-614 Poznan,´ Poland E-mail address: tomasz@amu.edu.pl Adam Mickiewicz University, Faculty of Mathematics and Computer

Science, Umultowska 87, 61-614 Poznan,´ Poland E-mail address: joaska@amu.edu.pl

