arXiv:1907.00847v2[math.CO]29Aug2019

# Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture

Hao Huang ∗

Abstract

In this paper, we show that every p2n´1 ` 1q-vertex induced subgraph of the ndimensional cube graph has maximum degree at least ?n. This result is best possible, and improves a logarithmic lower bound shown by Chung, Fu¨redi, Graham and Seymour in 1988. As a direct consequence, we prove that the sensitivity and degree of a boolean function are polynomially related, solving an outstanding foundational problem in theoretical computer science, the Sensitivity Conjecture of Nisan and Szegedy.

![image 1](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile1.png>)

## 1 Introduction

Let Qn be the n-dimensional hypercube graph, whose vertex set consists of vectors in t0,1un, and two vectors are adjacent if they diﬀer in exactly one coordinate. For an undirected graph G, we use the standard graph-theoretic notations ∆pGq for its maximum degree, and λ1pGq for the largest eigenvalue of its adjacency matrix. In 1988, Chung, Fu¨redi, Graham, and Seymour [3] proved that if H is an induced subgraph of more than 2n´1 vertices of Qn, then the maximum degree of H is at least p1{2 ´ op1qqlog2 n. Moreover, they constructed a p2n´1 ` 1q-vertex induced subgraph whose maximum degree is r?ns.

![image 2](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile2.png>)

In this short paper, we prove the following result, establishing a sharp lower bound that matches their construction. Note that the 2n´1 even vertices of Qn induce an empty subgraph. This theorem shows that any subgraph with just one more vertex would have its maximum degree suddenly jump to ?n.

![image 3](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile3.png>)

Theorem 1.1. For every integer n ě 1, let H be an arbitrary p2n´1`1q-vertex induced subgraph of Qn, then

?n. Moreover this inequality is tight when n is a perfect square.

![image 4](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile4.png>)

∆pHq ě

![image 5](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile5.png>)

∗Department of Mathematics, Emory University, Atlanta, USA. Email: hao.huang@emory.edu. Research supported in part by the Collaboration Grants from the Simons Foundation.

The induced subgraph problem is closely related to one of the most important and challenging open problems in theoretical computer science: the Sensitivity vs. Block Sensitivity Problem. In his 1989 paper, Nisan [12] gave right bounds for computing the value of a boolean function in the CREW-PRAM model. These bounds are expressed in terms of two complexity measures of boolean functions. For x P t0,1un and a subset S of indices from rns “ t1,¨¨¨ ,nu, we denote by xS the binary vector obtained from x by ﬂipping all indices in S. For f : t0,1un Ñ t0,1u, the local sensitivity spf,xq on the input x is deﬁned as the number of indices i, such that fpxq ‰ fpxtiuq, and the sensitivity spfq of f is maxx spf,xq. The sensitivity measures the local changing behavior of a boolean function with respect to the Hamming distance. It can be viewed as a discrete analog of the smoothness of continuous functions (see [7] for more in-depth discussions). The local block sensitivity bspf,xq is the maximum number of disjoint blocks B1,¨¨¨ ,Bk of rns, such that for each Bi, fpxq ‰ fpxBiq. Similarly, the block sensitivity bspfq of f is maxx bspf,xq. Obviously bspfq ě spfq. A major open problem in complexity theory was posed by Nisan and Szegedy [13], asking whether they are polynomially related.

Conjecture 1.2. (Sensitivity Conjecture) There exists an absolute constant C ą 0, such that for every boolean function f,

bspfq ď spfqC.

Although seemingly unnatural, the block sensitivity is known to be polynomially related to many other important complexity measures of boolean functions, including the decision tree complexity, the certiﬁcate complexity, the quantum and randomized query complexity, and the degree of the boolean function (as real polynomials), and the approximate degree [10]. It is noteworthy that some of these relationship is quite subtle. For instance, although the degree and approximate degree both concern algebraic properties of boolean functions, the only known proof of their polynomial relationship goes through other more combinatorial notions.

The Sensitivity Conjecture, if true, would place the sensitivity in the same category with the other complexity measures listed above. Computationally, it would imply that “smooth” (low-sensitivity) functions are easy to compute in some of the simplest models like the deterministic decision tree model. Algebraically, it asserts that such functions have low degree as real polynomials. Combinatorially, as observed by Gotsman and Linial [9], it is equivalent to the previous cube problem. We will discuss this connection later.

Despite numerous attempts for almost thirty years, the Sensitivity conjecture still remains wide open, and the best upper bound of bspfq is exponential in terms of spfq. For example, Kenyon and Kutin [11] showed that bspfq “ Opespfq

![image 6](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile6.png>)

a

spfqq. For the lower bound, Rubinstein [14] ﬁrst proposed a boolean function f with bspfq “

- 1

![image 7](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile7.png>)

- 2spfq2, showing a quadratic separation between these two complexity measures. Virza [16], and subsequently Ambainis and Sun [1] obtained better constructions which still provides quadratic separations. For a comprehensive survey with more background and


discussions, in particular the many problems equivalent to the Sensitivity Conjecture, we refer the readers to the surveys of Buhrman and de Wolf [2], Hatami, Kulkarni and Pankratov [10], and some recent works [4, 6, 8, 15].

Recall that Qn denotes the n-dimensional cube graph. For an induced graph H of Qn, let Qn ´ H denote the subgraph of Qn induced on the vertex set V pQnqzV pHq. Let ΓpHq “ maxt∆pHq,∆pQn ´ Hqu. The degree of a boolean function f, denoted by degpfq, is the degree of the unique multilinear real polynomial that represents f. Gotsman and Linial [9] proved the following remarkable equivalence using Fourier analysis.

- Theorem 1.3. (Gotsman and Linial [9]) The following are equivalent for any monotone function h : N Ñ R.

- (a) For any induced subgraph H of Qn with |V pHq| ‰ 2n´1, we have ΓpHq ě hpnq.
- (b) For any boolean function f, we have spfq ě hpdegpfqq.


Note that Theorem 1.1 implies that hpnq can be taken as ?n, since one of H and Qn´H must contain at least 2n´1`1 vertices, and the maximum degree ∆ is monotone. As a corollary, we have

![image 8](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile8.png>)

- Theorem 1.4. For every boolean function f, spfq ě a

![image 9](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile9.png>)

degpfq.

This conﬁrms a conjecture of Gotsman and Linial [9]. This inequality is also tight for the AND-of-ORs boolean function [10, Example 5.2]. Recall that the degree and the block sensitivity are polynomially related. Nisan and Szegedy [13] showed that bspfq ď 2degpfq2 and this bound was later improved by Tal [15] to bspfq ď degpfq2. Combining these results we have conﬁrmed the Sensitivity Conjecture.

- Theorem 1.5. For every boolean function f, bspfq ď spfq4.


## 2 Proof of the main theorem

To establish Theorem 1.1, we prove a series of lemmas. Given a n ˆ n matrix A, a principal submatrix of A is obtained by deleting the same set of rows and columns from A.

- Lemma 2.1. (Cauchy’s Interlace Theorem) Let A be a symmetric n ˆ n matrix, and B be a m ˆ m principal submatrix of A, for some m ă n. If the eigenvalues of A are


λ1 ě λ2 ě ¨¨¨ ě λn, and the eigenvalues of B are µ1 ě µ2 ě ¨¨¨ ě µm, then for all 1 ď i ď m,

λi ě µi ě λi`n´m.

Cauchy’s Interlace Theorem is a direct consequence of the Courant-Fischer-Weyl min-max principle. A direct proof can also be found in [5].

- Lemma 2.2. We deﬁne a sequence of symmetric square matrices iteratively as follows,

A1 “ „

- 0 1
- 1 0


 , An “ „

An´1 I I ´An´1

 .

Then An is a 2n ˆ 2n matrix whose eigenvalues are ?n of multiplicity 2n´1, and ´

![image 10](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile10.png>)

?n of multiplicity 2n´1.

![image 11](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile11.png>)

Proof. We prove by induction that A2n “ nI. For n “ 1, A21 “ I. Suppose the statement holds for n ´ 1, that is A2n´1 “ pn ´ 1qI, then

A2n “ „

A2n´1 ` I 0 0 A2n´1 ` I

 “ nI.

Therefore, the eigenvalues of An are either ?n or ´

![image 12](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile12.png>)

?n. Since TrrAns “ 0, we know that An has exactly half of the eigenvalues being ?n and the rest being ´

![image 13](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile13.png>)

![image 14](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile14.png>)

?n.

![image 15](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile15.png>)

![image 16](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile16.png>)

![image 17](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile17.png>)

![image 18](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile18.png>)

![image 19](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile19.png>)

- Lemma 2.3. Suppose H is an m-vertex undirected graph, and A is a symmetric matrix whose entries are in t´1,0,1u and whose rows and columns are indexed by V pHq, and whenever u and v are non-adjacent in H, Au,v “ 0. Then


∆pHq ě λ1 :“ λ1pAq.

Proof. Suppose  v is the eigenvector corresponding to λ1. Then λ1 v “ A v. Without loss of generality, assume v1 is the coordinate of  v that has the largest absolute value. Then

ÿm

ď ÿ

ÿ

|A1,j||v1| ď ∆pHq|v1|.

“

|λ1v1| “ |pA vq1| “

A1,jvj

A1,jvj

j„1

j„1

j“1

ˇ

ˇ

ˇ

ˇ

Therefore |λ1| ď ∆pHq. With the lemmas above, we are ready to prove the main theorem.

![image 20](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile20.png>)

![image 21](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile21.png>)

![image 22](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile22.png>)

![image 23](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile23.png>)

Proof of Theorem 1.1. Let An be the sequence of matrices deﬁned in Lemma 2.2. Note that the entries of An are in t´1,0,1u. By the iterative construction of An, it is not hard to see that when changing every p´1q-entry of An to 1, we get exactly the adjacency matrix of Qn, and thus An and Qn satisfy the conditions in Lemma 2.3. For example, we may let the upper-left and lower-right blocks of An correspond to the two pn ´ 1q-dimensional subcubes of Qn, and the two identity blocks correspond to the perfect matching connecting these two subcubes. Therefore, a p2n´1 ` 1q-vertex induced subgraph H of Qn and the principal submatrix AH of An naturally induced by H also satisfy the conditions of Lemma 2.3. As a result,

∆pHq ě λ1pAHq.

On the other hand, from Lemma 2.2, the eigenvalues of An are known to be ?n,¨¨¨ ,?n,´

?n,¨¨¨ ,´

?n.

![image 24](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile24.png>)

![image 25](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile25.png>)

![image 26](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile26.png>)

![image 27](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile27.png>)

Note that AH is a p2n´1 ` 1q ˆ p2n´1 ` 1q submatrix of the 2n ˆ 2n matrix An. By Cauchy’s Interlace Theorem,

?n. Combining the two inequalities we just obtained, we have ∆pHq ě

![image 28](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile28.png>)

λ1pAHq ě λ2n´1pAnq “

?n, completing the

![image 29](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile29.png>)

proof of our theorem. Remark. From the proof, one actually has λ1pHq ě λ1pAHq ě

![image 30](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile30.png>)

![image 31](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile31.png>)

![image 32](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile32.png>)

![image 33](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile33.png>)

?n. Since ∆pHq ě λ1pHq, this result strengthens Theorem 1.1. More interestingly, the inequality λ1pHq ě ?n is best possible for all n. This can be seen by taking all the even vertices and one odd vertex of Qn, then the induced subgraph is a copy of the star K1,n, together with many isolated vertices. The largest eigenvalue of this induced subgraph is exactly ?n.

![image 34](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile34.png>)

![image 35](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile35.png>)

![image 36](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile36.png>)

## 3 Concluding Remarks

In this paper we conﬁrm the Sensitivity Conjecture by proving its combinatorial equivalent formulation discovered by Gotsman and Linial. The following problems might be interesting.

- • Given a “nice” graph G with high symmetry, denote by αpGq its independence number. Let fpGq be the minimum of the maximum degree of an induced subgraph of G on αpGq ` 1 vertices. What can we say about fpGq? In particular, for which graphs, the method used in proving Theorem 1.1 would provide a tight bound?
- • Back to the hypercube problem, let gpn,kq be the minimum t, such that every t-vertex induced subgraph H of Qn has maximum degree at least k. In this paper, we show that gpn,?nq “ 2n´1 ` 1. It would be interesting to determine gpn,kq asymptotically for other values of k.

![image 37](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile37.png>)

- • Although we have shown a tight bound between the sensitivity and the degree, at the time of writing this paper, the best separation between the block sensitivity


bspfq and the sensitivity spfq is bspfq “ 23spfq2 ´ 13spfq shown in [1], which is quadratic. Theorem 1.5 only shows a quartic upper bound. Perhaps one could

![image 38](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile38.png>)

![image 39](<2019-huang-induced-subgraphs-hypercubes-proof_images/imageFile39.png>)

close this gap by directly applying the spectral method to boolean functions instead of to the hypercubes.

Acknowledgment. The author would like to thank Benny Sudakov for simplifying the proof of Lemma 2.2, Jacob Fox, Yan Wang and Yao Yao for reading an earlier draft of the paper, Matthew Kwan, Po-Shen Loh and Jie Ma for the inspiring discussions over the years, and the anonymous referee for helpful suggestions on improving the presentation of this paper.

## References

- [1] A. Ambainis, X. Sun, New separation between spfq and bspfq, Electronic Colloquium on Computational Complexity (ECCC), 18, 116, 2011. Available at http://eccc.hpi-web.de/report/2011/11.
- [2] H. Buhrman, R. de Wolf, Complexity measures and decision tree complexity: a survey, Theoretical Computer Science 288 (2002), 21–43.
- [3] F. Chung, Z. Fu¨redi, R. Graham, P. Seymour, On induced subgraphs of the cube, J. Comb. Theory, Ser. A, 49 (1) (1988), 180–187.
- [4] A. Drucker, A note on a communication game, CoRR, abs/1706.07890, 2017.
- [5] S. Fisk, A very short proof of Cauchy’s interlace theorem for eigenvalues of Hermitian matrices, Amer. Math. Monthly 112 (2005), no. 2, 118.
- [6] J. Gilmer, M. Koucky´, M. Saks, A new approach to the sensitivity conjecture, Proceedings of the 2015 Conference on Innovations in Theoretical Computer Science, ACM, 2015, 247–254.
- [7] P. Gopalan, N. Nisan, R. Servedio, K. Talwar, and A. Wigderson, Smooth Boolean functions are easy: eﬃcient algorithms for low-sensitivity functions, 7th Innovations in Theoretical Computer Science Conference (ITCS), 2016.
- [8] P. Gopalan, R. Servedio, A. Tal, A. Wigderson, Degree and sensitivity: tails of two distributions, 31st Conference on Computational Complexity, CCC 2016, Tokyo, Japan, 13:1–13:23.
- [9] C. Gotsman, N. Linial, The equivalence of two problems on the cube. J. Combin. Theory Ser. A, 61 (1) (1992), 142–146.
- [10] P. Hatami, R. Kulkarni, D. Pankratov, Variations on the Sensitivity Conjecture, Theory of Computing Library, Graduate Surveys 4 (2011), 1–27.
- [11] C. Kenyon, S. Kutin, Sensitivity, block sensitivity, and ℓ-block sensitivity of Boolean functions, Information and Computation, 189 (1) (2004), 43–53.
- [12] N. Nisan, CREW PRAMs and decision trees, Proc. 21st STOC, New York, NY, ACM Press (1989) 327–335.
- [13] N. Nisan, M. Szegedy, On the degree of Boolean functions as real polynomials, Comput. Complexity, 4 (1992), 462–467.
- [14] D. Rubinstein, Sensitivity vs. block sensitivity of Boolean functions, Combinatorica, 15 (2) (1995), 297–299.
- [15] A. Tal, Properties and applications of boolean function composition, Proceedings of the 4th conference on Innovations in Theoretical Computer Science, ITCS ’13, 441–454.
- [16] M. Virza, Sensitivity versus block sensitivity of boolean functions, Information Processing Letters, 111 (2011), 433–435.


