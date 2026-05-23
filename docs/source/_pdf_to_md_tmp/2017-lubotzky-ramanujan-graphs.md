arXiv:1711.06558v1[math.HO]15Nov2017

RAMANUJAN GRAPHS

ALEXANDER LUBOTZKY

Let X be a ﬁnite connected k-regular graph, k ≥ 3, with n vertices, and A its adjacency n×n matrix. Being symmetric, all its eigenvalues λ are real and it is easy to see that |λ| ≤ k, k is always an eigenvalue, and −k is an eigenvalue if and only if X is bi-partite. The graph X is called Ramanujan graph if every eigenvalue λ satisﬁes either |λ| = k or |λ| ≤ 2√k − 1. The bound 2√k − 1 is signiﬁcant: by Alon-Boppana Theorem, (cf. [LPS]) this is the best possible bound one can hope for, for an inﬁnite family of k-regular graphs. The real reason behind it is as follows: The universal cover of X (in the sense of algebraic topology) is X˜ = Tk - the inﬁnite k-regular tree. An old result of Kesten asserts that the spectrum of the adjacency operator acting on L2(Tk) is the interval [−2√k − 1, 2√k − 1]. So, being Ramanujan means for X, that all its non-trivial eigenvalues are in the spectrum of its universal cover X˜.

![image 1](<2017-lubotzky-ramanujan-graphs_images/imageFile1.png>)

![image 2](<2017-lubotzky-ramanujan-graphs_images/imageFile2.png>)

![image 3](<2017-lubotzky-ramanujan-graphs_images/imageFile3.png>)

![image 4](<2017-lubotzky-ramanujan-graphs_images/imageFile4.png>)

Ramanujan graphs are optimal expanders from spectral point of view. Recall that a ﬁnite k-regular graph X is called ε-expander if h(X) ≥ ε when h(X) is the Cheeger constant of X, namely

Y ⊆ X, |Y | ≤ |X2|

h(X) = min |E(Y, Y¯)|/|Y |

![image 5](<2017-lubotzky-ramanujan-graphs_images/imageFile5.png>)

when E(Y, Y¯) is the set of edges between Y and its complement. Now if we denote λ1(X) = max{λ | λ = k, λ e.v. of X}, then h2|X| 2k ≤ λ1(X) ≤ 2h(X) (cf. [L1]).

![image 6](<2017-lubotzky-ramanujan-graphs_images/imageFile6.png>)

So, Ramanujan graphs are expanders. Expander graphs are of great importance in combinatorics and computer science (cf. [HLW] and the references therein) and also in pure mathematics (cf. [L2]). Expander graphs serve as basic building blocks in various network constructions, in many algorithms and so on. The bound on their eigenvalues ensures that the random walk on such graphs converges quickly to the uniform distribution and on Ramanujan graphs this happens in the fastest possible way. This is one more reason that makes them so useful.

The existence of Ramanujan graphs is by no means a trivial issue: While it is known that random k-regular graphs are expanders, it is

1

not known if they are Ramanujan. First examples of inﬁnite families of such graphs were given by explicit construction in [LPS] and [M] for k = q + 1, q prime. In [MSV], it is shown, by a non constructive method, that for every k ≥ 3 there exist inﬁnitely many k-regular bi-partite Ramanujan graphs.

Why are Ramanujan graphs named after Ramanujan? As far as we know Ramanujan had no special interest in graph theory. Let us explain the reason for this name which was coined in [LPS].

Let us look at the following power series

△(q) = q

(1 − qn) = Στ(n)qn = q − 24q + 252q3 + . . .

n≥1

The coeﬃcients τ(n) deﬁne the so called Ramanujan tau function. Ramanujan conjectured that τ(p) ≤ 2p

11 2 for every prime p. The importance of △ comes from the fact that if we write q = e2πiz then △(z) is a cusp form of weight 12 on the upper half plane H = {z = x+iy | x, y ∈ R, y > 0} with respect to the modular group Γ = SL2(Z) acting on H by Mobius transformation abcd (z) = czaz++db. Now if Γ0(N) = { abcd ∈ Γ c ≡ 0( mod N)} we denote Sk(N) (or more generally Sk(N, w) for a Dirichlet character w of Z/NZ) the space of cusp forms on H w.r.t. Γ0(N) (and w). The Hecke operators Tp (p prime, (p, N) = 1), act, and commute, on each Sk(N, w), and their common eigenfunctions are the Hecke eigenforms. Now, S12(Γ = Γ0(1)) is one dimensional and so △(z) above is such a Hecke eigenform. Moreover, τ(p) above is equal to the eigenvalue of Tp acting on S12(Γ). A natural and far reaching generalization of the Ramanujan conjecture mentioned above on the size of τ(p) is the so called Ramanujan-Peterson (RP) conjecture: for every Hecke eigenform f in Sk(N, w), the eigenvalues λp of Tp, (p, N) = 1, satisfy |λp| ≤ 2p

![image 7](<2017-lubotzky-ramanujan-graphs_images/imageFile7.png>)

![image 8](<2017-lubotzky-ramanujan-graphs_images/imageFile8.png>)

k−1

2 . The reader is referred to [R] for a concise and clear explanation of all these notions.

![image 9](<2017-lubotzky-ramanujan-graphs_images/imageFile9.png>)

The modern approach to automorphic functions via representation theory brought in another point of view on the Ramanujan-Peterson Conjecture. Satake [S] showed that the RP conjecture is equivalent to the assertion: Let A = AQ be the ring of ade′les of Q, and π an irreducible cuspidal GL2-representation in L2(GL2(A)/GL2(Q)), such that its component at inﬁnity π∞ is square integrable, then for every prime p the local factor at the p-component πp is a tempered representation. See [R] for exact deﬁnitions. Here we only mention that a representation of a (simple) p-adic real Lie group G is tempered if it is weakly contained in L2(G). The RP conjecture was proved by Deligne (for

RAMANUJAN GRAPHS 3

the special representations that are relevant to the Ramanujan graphs, the RP conjecture was actually proven earlier by Eichler). The representation theoretic formulation suggests vast generalizations to other algebraic groups.

Let us look at the simple p-adic group G = PGL2(Qp). The BruhatTits building associated with G is, in this special case, the (p + 1)regular tree T = Tp+1 which can be identiﬁed as T = G/K when K is a maximal compact subgroup of G. If Γ is a discrete cocompact subgroup of G, then X = Γ \ T = Γ \ G/K is a ﬁnite (p + 1)-regular graph. One can show (see [L1]) that X is a Ramanujan graph if and only if every inﬁnite dimensional K-spherical G-sub-representation of L2(Γ \ G) is tempered. Deligne theorem, combined with the so called JacquetLanglands correspondence, enables the construction of such arithmetic subgroups Γ for which the temperedness conditions is satisﬁed and hence Ramanujan graphs are obtained. This was the method of [LPS] and [M]. Let us mention that for every k, if G is the full automorphism group of Tk and Γ a discrete cocompact subgroup of G, then X = Γ\Tk is k-regular Ramanujan graph if and only if the same temperedness condition is satisﬁed: in other words every non-trivial eigenvalue of X = Γ\Tk is coming from the spectrum of Tk if and only if every nontrivial spherical subrepresentation of L2(Γ \ G) is coming from L2(G). This illustrates the connection between the notion of Ramanujan graph and the Ramanujan conjecture.

As mentioned above, the Ramanujan-Peterson conjecture was generalized to other groups, some of its generalizations to GLd (instead of only GL2) led to higher dimensional versions of Ramanujan graphs, the so called Ramanujan complexes.

Finally, another interesting hint to a connection with number theory. Ihara deﬁned the notion of Zeta function of a k-regular graph X and Sunada observed that X is Ramanujan if and only if this Zeta function satisﬁes “the Riemann hypothesis” (see [L1] for details).

References

[HLW] S. Hoory, N. Linial and A. Wigderson, Expander graphs and their applications. Bull. Amer. Math. Soc. (N.S.) 43 (2006), no. 4, 439–561.

- [L1] A. Lubotzky, Discrete groups, expanding graphs and invariant measures. With an appendix by Jonathan D. Rogawski. Progress in Mathematics 125, Birkhuser Verlag, Basel, 1994. xii+195 pp. ISBN: 3-7643-5075-X
- [L2] A. Lubotzky, Expander graphs in pure and applied mathematics. Bull. Amer. Math. Soc. (N.S.) 49 (2012), no. 1, 113–162. [LPS] A. Lubotzky, R. Phillips and P. Sarnak, Ramanujan graphs. Combinatorica 8 (1988), no. 3, 261–277.


[MSV] A.W. Marcus, D.A. Spielman and N. Srivastava, Interlacing families I: Bipartite Ramanujan graphs of all degrees. Ann. of Math (2) 182 (2015), no. 1, 307-325.

[M] G.A. Margulis, Explicit group-theoretic constructions of combinatorial schemes and their applications in the construction of expanders and concentrators. (Russian) Problemy Peredachi Informatsii 24 (1988), no. 1, 51–60.

- [R] J.D. Rogawski, Modular forms, the Ramanujan conjecture and the JacquetLanglands correspondence, An Appendix to [L1].
- [S] I. Satake, Spherical functions and Ramanujan conjecture. 1966 Algebraic Groups and Discontinuous Subgroups (Proc. Sympos. Pure Math., Boulder, Colo., 1965) pp. 258–264. Amer. Math. Soc., Providence, R.I.


