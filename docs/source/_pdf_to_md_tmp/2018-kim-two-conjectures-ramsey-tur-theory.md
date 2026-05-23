arXiv:1803.04721v1[math.CO]13Mar2018

TWO CONJECTURES IN RAMSEY-TURAN´ THEORY

JAEHOON KIM, YOUNJIN KIM AND HONG LIU

Abstract. Given graphs H1, . . . , Hk, a graph G is (H1, . . . , Hk)-free if there is a k-edge-colouring φ : E(G) → [k] with no monochromatic copy of Hi with edges of colour i for each i ∈ [k]. Fix a function f(n), the Ramsey-Tur´an function RT(n, H1, . . . , Hk, f(n)) is the maximum number of edges in an n-vertex (H1, . . . , Hk)-free graph with independence number at most f(n). We determine RT(n, K3, Ks, δn) for s ∈ {3, 4, 5} and suﬃciently small δ, conﬁrming a conjecture of Erd˝s and S´os from 1979. It is known that RT(n, K8, f(n)) has a phase transition at f(n) = Θ(√n log n). However, the values of RT(n, K8, o(√n log n)) was not known. We determined this value by proving

![image 1](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile1.png>)

![image 2](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile2.png>)

RT(n, K8, o(√n log n)) = n42 + o(n2), answering a question of Balogh, Hu and Simonovits. The proofs utilise, among others, dependent random choice and results from graph packings.

![image 3](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile3.png>)

![image 4](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile4.png>)

1. Introduction and results

Tura´n’s theorem [26] states that among all n-vertex Ks+1-free graphs, the balanced complete s-partite graph, now so-called s-partite Tura´n graph Ts(n), has the largest size, where the size of a graph is the number of edges in a graph. Notice that these Tur´an graphs have rigid structures, in particular, there are independent sets of size linear in n. It is then natural to ask for the size of an n-vertex Ks+1-free graph without these rigid structures, i.e. graphs with additional contstraints on their independence number. Such problems, ﬁrst introduced by So´s [11] in 1969, are the substance of the Ramsey-Tura´n theory. Formally, given a graph H and natural numbers m,n ∈ N, the RamseyTura´n number, denoted by RT(n,H,m) is the maximum number of edges in an n-vertex H-free graph G with α(G) ≤ m can have. Motivated by above reasons, the most classical case is when m is sublinear in n, i.e. m = o(n).

Deﬁnition. Given a graph H and δ ∈ (0,1), let

RT(n,H,δn) n2

̺(H,δ). We write

and ̺(H) := lim

- (1.1) ̺(H,δ) := lim n→∞


![image 5](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile5.png>)

δ→0

RT(n,H,o(n)) = ̺(H) · n2 + o(n2).

We call ̺(H) the Ramsey-Tura´n density of H. The Ramsey-Tura´n density of cliques are wellunderstood. For odd cliques, Erd˝os and So´s [11] proved that ̺(K2s+1) = 12(s−s1) for all s ≥ 1. The problem for even cliques is much harder. Szemere´di [25] ﬁrst showed that ̺(K4) ≤ 18. However no lower bound on ̺(K4) was known until Bollob´s and Erd˝os [6] provided a matching lower bound using an ingenious geometric construction, showing that ̺(K4) = 18. Finally, Erd˝os, Hajnal, So´s and Szemere´di [9] determined the Ramsey-Tura´n density for all even cliques, proving that ̺(K2s) = 21(33ss−−25) for all s ≥ 2.

![image 6](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile6.png>)

![image 7](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile7.png>)

![image 8](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile8.png>)

![image 9](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile9.png>)

![image 10](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile10.png>)

![image 11](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile11.png>)

While ̺(H) shows only the limit value, ̺(H,δ) captures the transition behaviours of RamseyTura´n number more accurately when independence number drops to o(n). Capturing this more subtle behaviour, Fox, Loh and Zhao [13] proved that ̺(K4,δ) = 81 + Θ(δ). Building on Fox-LohZhao’s work, Lu¨ders and Reiher [20] have very recently showed that, surprisingly, there is a precise

![image 12](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile12.png>)

![image 13](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile13.png>)

Date: July 7, 2021. J.K. was supported by ERC grant 306349; Y.K. was supported by Basic Science Research Program through the

National Research Foundation of Korea(NRF) funded by the Ministry of Education (2017R1A6A3A04005963); and H.L. was supported by the Leverhulme Trust Early Career Fellowship ECF-2016-523.

1

formula for ̺(H,δ) for all cliques and suﬃciently small δ: for all s ≥ 2, ̺(K2s−1,δ) = 21(ss−−12 + δ), while ̺(K2s,δ) = 21(33ss−−52 +δ−δ2). Inspired by Lu¨ders and Reiher’s work, one of our results concerns the multicolour extension of this result. For more literature on Ramsey-Tura´n theory, we refer the readers to a survey of Simonovits and So´s [23]. See also [2, 3, 4] for more recent results on variants of Ramsey-Tura´n problem.

![image 14](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile14.png>)

![image 15](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile15.png>)

![image 16](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile16.png>)

![image 17](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile17.png>)

- 1.1. Multicolour Ramsey-Tura´n problem. Given graphs H1,... ,Hk, we say that a graph G is (H1,... ,Hk)-free if there exists an edge colouring φ : E(G) → [k] such that for each i ∈ [k], the spanning subgraph with all edges of colour i is Hi-free. Let RT(n,H1,... ,Hk,m) be the maximum size of an n-vertex (H1,... ,Hk)-free graph with independence number at most m, and deﬁne ̺(H1,... ,Hk,δ) and ̺(H1,... ,Hk) analogous to (1.1). Erd˝os, Hajnal, Simonovits, So´s and Szemere´di [10] proved that the multicolour Ramsey-Tura´n density for cliques is determined by certain weighted Ramsey numbers (see Deﬁnition 5 and Theorem 2 in [10] for more details). Determining the actual values of ̺(Ks1,... ,Ksk) turns out to be very diﬃcult. Only sporadic cases are


known [10]: ̺(K3,K3) = 14, ̺(K3,K4) = 31, ̺(K3,K5) = 25 and ̺(K4,K4) = 1128. Even 2-coloured triangle versus a clique case, i.e. determining ̺(K3,Ks), remains open. Recall that the Ramsey number R(s,t) is the minimum integer N such that every blue/red colouring of KN contains either a blue Ks or a red Kt. Erd˝os, Hajnal, Simonovits, So´s and Szemere´di [10] conjectured for all s ≥ 2,

![image 18](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile18.png>)

![image 19](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile19.png>)

![image 20](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile20.png>)

![image 21](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile21.png>)

̺(K3,K2s−1) = 21 1 − R(3,s1)−1 .

![image 22](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile22.png>)

![image 23](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile23.png>)

Capturing more subtle behaviours of multicolour Ramsey-Tura´n number, Erd˝os and So´s [12] proved in 1979 that ̺(K3,K3,δ) = 41 + Θ(δ) and conjectured that for suﬃciently small δ, there exists c > 0 such that ̺(K3,K3,δ) = 41 +cδ. In the following theorem, we determine the exact value of ̺(K3,K3,δ) for all small δ > 0, thus conﬁrming the conjecture of Erd˝os and So´s. Furthermore, we also determine the exact values of ̺(K3,K4,δ) and ̺(K3,K5,δ). We remark that ̺(K3,K4,δ) behaves quite diﬀerently from ̺(K3,Ks,δ) with s ∈ {3,5}. The extremal graph achieving the value of ̺(K3,K3,δ) (resp. ̺(K3,K5,δ)) comes from taking the union of T2(n) (resp. T5(n)) and F∗, certain almost δn-regular K3-free graph with independence number at most δn. It turns out that the natural lower bound from the union of T3(n) and F∗ is not optimal for ̺(K3,K4,δ).

![image 24](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile24.png>)

![image 25](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile25.png>)

- Theorem 1.1. For suﬃciently small δ > 0, we have


- • ̺(K3,K3,δ) = 14 + 2δ;

![image 26](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile26.png>)

![image 27](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile27.png>)

- • ̺(K3,K4,δ) = 31 + 2δ + 32δ2;

![image 28](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile28.png>)

![image 29](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile29.png>)

![image 30](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile30.png>)

- • ̺(K3,K5,δ) = 52 + 2δ;


![image 31](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile31.png>)

![image 32](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile32.png>)

We can see that the 2-colour Ramsey-Tura´n number ̺(K3,Ks,δ) shares some similarity with the single-colour problem ̺(Ks,δ) as they both have an extra quadratic term when s is even. However, the single-colour Ramsey-Tura´n number has the same quadratic term for all even s. This is not the case for the 2-colour Ramsey-Tura´n number due to its relation to Ramsey number R(3,⌈s/2⌉). Indeed, we give a construction showing that

δ 2

5 12

+ 2δ2. We conjecture that the equality above holds (see concluding remark for more details).

̺(K3,K6,δ) ≥

+

![image 33](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile33.png>)

![image 34](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile34.png>)

In the following theorem, we determine Ramsey-Tura´n numbers for (K3,Ks) for all s ≥ 3 when the independence number condition is slightly more strict than sublinear, providing evidence towards the Erd˝os-Hajnal-Simonovits-S´s-Szemere´di conjecture. Let ω(n) be a function growing to inﬁnity arbitrarily slowly as n → ∞. For each integer s ≥ 2, deﬁne

n eω(n)·(logn)1−1/s

- (1.2) gsω(n) :=


.

![image 35](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile35.png>)

We omit ω and write gs(n) whenever the result holds for any function ω(n) growing to inﬁnity. Note that n ≫ gs(n) ≫ n1−ε, for any ε > 0.

- Theorem 1.2. For all s ≥ 2, we have

- • RT(n,K3,K2s−1,gs(n)) = 12 1 − R(3,s1)−1 n2 + o(n2); and

![image 36](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile36.png>)

![image 37](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile37.png>)

- • RT(n,K3,K2s,gs(n)) = 12 1 − R(31,s) n2 + o(n2).


![image 38](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile38.png>)

![image 39](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile39.png>)

1.2. Phase transition. Our next result concerns phase transitions of the single-coloured RamseyTura´n number. A graph H has Ramsey-Tura´n phase transition at f if

lim

n→∞

RT(n,H,f(n)) − RT(n,H,o(f(n))) n2

![image 40](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile40.png>)

> 0,

where RT(n,H,o(f(n)) = limδ→0 RT(n,H,δ·f(n)). In other words, a slightly stronger upper bound on the independence number, o(f(n)) instead of f(n), would result in a drop at the maximum possible edge-density of an H-free graph (see [1] for more details).

From odd cliques, the result of Erd˝os-So´s [11] shows that K2s+1, with s ≥ 1, has its ﬁrst phase transition at f(n) = n, where the density drops from 12(2s2−s1) to 12(s−s1). In fact, RT(n,K2s+1,c√nlog n) =

![image 41](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile41.png>)

![image 42](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile42.png>)

![image 43](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile43.png>)

![image 44](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile44.png>)

![image 45](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile45.png>)

- 1

![image 46](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile46.png>)

- 2(s−s1 + o(1))n2 for c > 2/√s. Balogh, Hu and Simonovits ([1], Theorem 2.7) proved that


![image 47](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile47.png>)

![image 48](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile48.png>)

RT(n,K2s+1,o(√nlog n)) ≤ 21(2s2−s3 + o(1))n2, showing that the second phase transition happens at f(n) = √nlog n (around the inverse function of R(3,n)). Erd˝os and So´s [11] asked whether

![image 49](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile49.png>)

![image 50](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile50.png>)

![image 51](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile51.png>)

![image 52](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile52.png>)

RT(n,K5,o(√n)) = o(n2). Sudakov [24] showed that it is true if a slightly stronger bound is imposed on the independence number: RT(n,K5,g2(√n)) = o(n2). Later, Balogh, Hu, Simonovits [1] answered Erd˝os and So´s’s question in a stronger form, showing that: RT(n,K5,o(√nlog n)) = o(n2).

![image 53](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile53.png>)

![image 54](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile54.png>)

![image 55](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile55.png>)

The situation for even cliques, K2s with s ≥ 2, is again less clear apart from the ﬁrst phase transition at f(n) = n as shown by Erd˝os-Hajnal-Simonovits-S´s-Szemere´di [10], where the density decreases from 21(22ss−−21) to 21(33ss−−52). Extending a result of Sudakov [24], Balogh, Hu, Simonovits ([1],

![image 56](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile56.png>)

![image 57](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile57.png>)

![image 58](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile58.png>)

![image 59](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile59.png>)

- Theorem 3.4) showed that : RT(n,K2s,f(n)) = 21(ss−−21 + o(1))n2 for any c√nlog n < f(n) ≤ gs(n) where c > 2/√s − 1; while Fox, Loh and Zhao [13] showed that RT(n,K2s,g∗(n)) = 12(33ss−−52 +


![image 60](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile60.png>)

![image 61](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile61.png>)

![image 62](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile62.png>)

![image 63](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile63.png>)

![image 64](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile64.png>)

![image 65](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile65.png>)

![image 66](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile66.png>)

log n

o(1))n2, where g∗(n) := ne−o

![image 67](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile67.png>)

loglogn . Thus, the second phase transition for K2s happens somewhere in the small window between g∗(n) and gs(n). The third phase transition for even cliques occurs at f(n) = √nlog n, but not a single extremal density is known except the trivial case of K4. For example, RT(n,K6,o(√nlog n)) ≤ n62 + o(n2) and we do not know whether it is o(n2). For K8, Balogh, Hu and Simonovits [1] showed that

![image 68](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile68.png>)

![image 69](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile69.png>)

![image 70](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile70.png>)

- • RT(n,K8,c√nlog n) = n32 + o(n2) for c > 2/√3;

![image 71](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile71.png>)

![image 72](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile72.png>)

![image 73](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile73.png>)

- • 2n72 + o(n2) ≥ RT(n,K8,o(√nlog n)) ≥ RT(n,K7,o(√nlog n)) = n42 + o(n2);

![image 74](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile74.png>)

![image 75](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile75.png>)

![image 76](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile76.png>)

![image 77](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile77.png>)

- • RT(n,K8,g2(√n)) = n42 + o(n2),


![image 78](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile78.png>)

![image 79](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile79.png>)

and raised the question of whether RT(n,K8,o(√nlog n)) = RT(n,K7,o(√nlog n)). So the RamseyTura´n density for K8 drops from 1/3 to at most 2/7 around √nlog n. It is not clear when in between o(√nlog n) and g2(√n), it drops to 1/4. In the following theorem, we close this gap, proving that RT(n,K8,o(√nlog n)) = n42 +o(n2). This answers Balogh-Hu-Simonovits’s question positively and provides the ﬁrst exact value of nontrivial extremal density for the third phase transition of an even clique.

![image 80](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile80.png>)

![image 81](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile81.png>)

![image 82](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile82.png>)

![image 83](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile83.png>)

![image 84](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile84.png>)

![image 85](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile85.png>)

![image 86](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile86.png>)

- Theorem 1.3. For any γ > 0, there exists δ > 0 such that the following holds. Let G be an n-vertex K8-free graph with α(G) ≤ δ√nlog n. Then e(G) ≤ n42 + γn2.


![image 87](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile87.png>)

![image 88](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile88.png>)

Organisation of the paper. In Section 2, we give preliminaries necessary for the proofs. Then we present the proofs of Theorem 1.3 in Section 3, and the lower bounds in Theorem 1.1 in Section 4. We then prove the upper bounds in Theorem 1.1 in Sections 5 and 6. The proof of Theorem 1.2 will be given in Section 7. Finally in Section 8, we make some concluding remarks.

2. Preliminaries In this section, we introduce some notation, tools and lemmas. Denote [q] := {1,2,... ,q},

[p,q] := {p,p+1,... ,q}, and Xi (resp. ≤ Xi ) denotes the set of all subsets of a set X of size i (resp. at most i). We may abbreviate a singleton {x} (resp. a pair {x,y}) as x (resp. xy). If we claim

that a result holds whenever 0 < b ≪ a ≪ 1, this means that there are a constant a0 ∈ (0,1) and a non-decreasing function f : (0,1) → (0,1) (that may depend on any previously deﬁned constants or functions) such that the result holds for all a,b ∈ (0,1) with a ≤ a0 and b ≤ f(a). We write a = b ± c if b − c ≤ a ≤ b + c. We may omit ﬂoors and ceilings when they are not essential.

![image 89](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile89.png>)

Let G = (V,E) be a graph and A,B,V1,... ,Vp ⊆ V . Denote by A := V \ A the complement of A. Let G[A] := (A,{xy ∈ E : x,y ∈ A}) denote the induced subgraph of G on A, and denote by N(A,B) the common neighbourhood of A in B. Write N(v,B) instead of N({v},B), and d(v,B) = |N(v,B)|. Denote by G[V1,... ,Vp] the p-partite subgraph of G induced by p-partition V1∪···∪Vp. We say that a partition U1∪...∪Up of V is a max-cut p-partition of G if e(G[U1,... ,Up]) is maximised among all p-partition of V . Denote by δcr(G[V1,... ,Vp]) := minij∈([p2]), v∈Vi d(v,Vj) the minimum crossing degree of G with respect to the partition V1 ∪ ... ∪ Vp. For each n,p ∈ [n], Tp(n) denotes the n-vertex Tura´n graph, which is the n-vertex complete p-partite graph such that each partite sets has size either ⌊n/p⌋ or ⌈n/p⌉. For two n-vertex graphs G and H, we deﬁne |G△H| be the minimum number N = N1 + N2 such that we can obtain a graph isomorphic to H after deleting N1 edges from G and adding N2 edges to G.

Given φ : E(G) → [k], throughout the paper, for each i ∈ [k], we will always denote Gi the spanning subgraph of G induced by all edges of colour i. We say that φ, and also G, is (Ks1,... ,Ksk)free if Gi is Ksi-free for each i ∈ [k]. We will write φ(A,B) = i if φ(e) = i for all e ∈ E(G[A,B]), and write φ(v,B) instead of φ({v},B). If φ is also deﬁned on V (G), we write φ(A) = i if φ(v) = i for all v ∈ A. The following result will be useful.

- Theorem 2.1 ([16]). Let G be an n-vertex K4-free graph with e(G) ≥ n2/4 + t. Then G contains at least t edge-disjoint triangles.


Given d,n ∈ N, denote by F(n,d) an n-vertex d-regular triangle-free graph with α(G) = d. Let B ⊆ (0,1) consists of all the rationals δ for which there exists some F(n,d) with d/n = δ. We will use a result of Brandt [7], which states that B is dense in (0,1/3), in the following form.

- Theorem 2.2 ([7]). For any 0 < η,δ < 1/3, there exists n0 > 0 such that the following holds for all n ≥ n0. For some d ∈ [(δ − η)n,δn], there exists a graph F(n,d).

The following is a result of Fu¨redi proving stability of Kp+1-free graphs.

- Theorem 2.3 ([15]). Suppose that t ∈ N and G is an n-vertex Kp+1-free with e(G) ≥ e(Tn,p) − t. Then there exists v1,... ,vp such that e(Kv1,...,vp) ≥ e(Tn,p) − 2t and |G△Kv1,...,vp| ≤ 3t. Consequently, vi = n/p ± 2√t for all i ∈ [p] and |G△Tp(n)| = O(√tn).

![image 90](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile90.png>)

![image 91](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile91.png>)

The following theorem follows from Shearer’s bound on Ramsey number R(3,k) ≤ (1+o(1))k2/log k (see also [5, 8, 21] for more recent development on R(3,k)).

- Theorem 2.4. [22] There exists k0 ∈ N such that for all k ≥ k0, any graph on at least 2k2/log k vertices contains either a triangle or an independent set of size k.


We will make use of the multicolour version of the Szemere´di Regularity Lemma (see, for example, [18, Theorem 1.18]). We introduced the relevant deﬁnitions. Let X,Y ⊆ V (G) be disjoint non-empty sets of vertices in a graph G. The density of (X,Y ) is dG(X,Y ) := e(|GX[X,Y| |Y|]). For ε > 0, the pair (X,Y ) is ε-regular in G if for every pair of subsets X′ ⊆ X and Y ′ ⊆ Y with |X′| ≥ ε|X| and |Y ′| ≥ ε|Y |, we have |dG(X,Y ) − dG(X′,Y ′)| ≤ ε. Additionally, if dG(X,Y ) ≥ γ, for some γ > 0, we say that (X,Y ) is (ε,γ)-regular. A partition V (G) = V1 ∪ ... Vm is an ε-regular partition of a k-edge-coloured graph G if

![image 92](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile92.png>)

- (1) for all ij ∈ [m2] , |Vi| − |Vj| ≤ 1;
- (2) for each i ∈ [m], all but at most εm choices of j ∈ [m] satisﬁes that the pair (Vi,Vj) is ε-regular in Gℓ for each colour ℓ ∈ [k].


- Lemma 2.5 (Multicolour Regularity Lemma [18]). Suppose 0 < 1/M′ ≪ ε,1/M ≪ 1/k ≤ 1 and n ≥ M. Suppose G is an n-vertex k-edge-coloured graph and U1 ∪ U2 is a partition of V (G). Then there exists an ε-regular partition V (G) = V1 ∪ ... ∪ Vm with M ≤ m ≤ M′ such that for each i ∈ [m] we have either Vi ⊆ U1 or Vi ⊆ U2.

Given ε,γ > 0, a graph G, a colouring φ : E(G) → [k] and a partition V (G) = V1 ∪ ··· ∪ Vm, deﬁne the reduced graph R := R(ε,γ,φ,(Vi)mi=1) of order m as follows: V (R) = [m] and ij ∈ E(R) if (Vi,Vj) is (i) ε-regular with respect to Gp for every p ∈ [k] and (ii) d(Gq[Vi,Vj]) ≥ γ for some q ∈ [k]. For brevity, we may omit φ or (Vi)ri=1 in the notation when these are clear. It is easy to see that we have

e(G) ≤ e(R) ·

n m

![image 93](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile93.png>)

2

+

n2 m

![image 94](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile94.png>)

- (2.1) + kγn2.


Given a graph R and s ∈ N, let R(s) be the graph obtained by replacing every vertex of R with an independent set of size s and replacing every edge of R with Ks,s. The following lemmas provide some useful properties related to regular partitions.

- Lemma 2.6 (Counting Lemma, Theorem 2.1 in [18]). Suppose 0 < 1/n ≪ ε ≪ γ,1/h ≤ 1. Suppose that H is an h-vertex graph and R is a graph such that H ⊆ R(h). If G is a graph obtained by replacing every vertex of R with an independent set of size n and replacing every edge of R with an (ε,γ)-regular pair, then G contains at least (γ/2)e(H)N|V (H)| copies of H.
- Lemma 2.7 (Slicing Lemma, Fact 1.5 in [18]). Let ε < α,γ,1/2. Suppose that (A,B) is an (ε,γ)regular pair in a graph G. If A′ ⊆ A and B′ ⊆ B satisﬁes |A′| ≥ α|A| and |B′| ≥ α|B|, then (A′,B′) is an (ε′,γ − ε)-regular pair in G, where ε′ := max{ε/α,2ε}.
- Lemma 2.8 (Claim 7.1 in [1] with p = 2). For a given function gs as in (1.2), suppose 0 < 1/n ≪

- 1/m,ε ≪ γ < 1. Suppose that G is an n-vertex graph with α(G) ≤ gs(n) and V1 ∪ ··· ∪ Vm is an ε-regular partition and R = R(ε,γ) is a corresponding reduced graph. If Ks ⊆ R, then we have K2s ⊆ G.


The following lemma will be useful to guarantee a certain minimum degree condition in a dense graph.

- Lemma 2.9. Suppose 0 < 1/n ≪ ε ≪ d ≤ 1. Suppose that G is an n-vertex graph with e(G) ≥ (d + ε)n2/2. Then G contains an n′-vertex subgraph G′ with n′ ≥ ε1/2n/2 such that e(G′) ≥ (dn′2 + εn2 − d(n − n′))/2 and δ(G′) ≥ dn′.


Proof. Obtain a sequence of graphs Gn := G,Gn−1,... as follows. For each i ≤ n, if there exists a vertex vi ∈ V (Gi) with dGi(vi) ≤ di, then set Gi−1 := Gi \ {vi}. Let Gn′ be the ﬁnal graph. Then we have

n

n′2 ≥ 2e(Gn′) > (d + ε)n2 −

2di = εn2 + dn′2 − dn + dn′.

i=n′+1

This implies n′ ≥ ε1/2n/2, thus proving the lemma.

3. Proof of Theorem 1.3

We need ﬁrst the following variation of dependent random choice lemma. For more on the dependent random choice method, we refer the readers to a survey of Fox and Sudakov [14].

Lemma 3.1. Let 0 < γ < 1 and G be a 3-partite graph with vertex partition Z1 ∪Z2 ∪Z3 such that |Zi| = n for each i ∈ [3]. If d(v,Zi) ≥ γn holds for all v ∈ Z1 and i ∈ {2,3}, then there exists a set S ⊆ Z1 of size 21n2/3 such that every pair of vertices P ∈ S2 satisﬁes |N(P,Zi)| ≥ γ9n for each i ∈ {2,3}.

![image 95](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile95.png>)

Proof. Set q := 6 log(1logn/γ). For each i ∈ {2,3}, pick q vertices in Zi uniformly at random with repetition and denote by Qi the set of chosen vertices. We call a pair P ∈ Z21 bad if there exists

![image 96](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile96.png>)

- i ∈ {2,3} such that |N(P,Zi)| < γ9n. Deﬁne S′ := N(Q2 ∪ Q3,Z1), and deﬁne a random variable X as the number of bad pairs in S′. Note that for each bad pair P ∈ Z21 , we have


3

q

|N(P,Zi)| |Zi|

≤ γ18q.

P[P ⊆ S′] = P[Q2 ∪ Q3 ⊆ N(P)] =

![image 97](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile97.png>)

i=2

Thus, by the linearity of expectation, we have that E[X] ≤ |Z21| · γ18q ≤ n2γ18q. On the other hand,

3

q

d(v,Zi) |Zi|

P[v ∈ S′] =

E|S′| =

≥ nγ2q.

P[Q2 ∪ Q3 ⊆ N(v)] =

![image 98](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile98.png>)

i=2

v∈Z1

v∈Z1

v∈Z1

So, there exists choices of Q2 and Q3 such that E[|S′| − X] ≥ nγ2q − n2γ18q ≥ 21n2/3. Then the set

![image 99](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile99.png>)

- S obtained from deleting one vertex from every bad pair in S′ has the desired properties. Proof of Theorem 1.3. Fix constants δ,M′,ε as follows:


0 < 1/n0 ≪ δ < 1/M′ ≪ ε ≪ γ ≪ 1. Assume that G is an n-vertex graph with n ≥ n0 and α(G) ≤ δ√nlog n. Apply the regularity lemma (Lemma 2.5 with k = 1) with G,V (G),∅,ε,ε−1,1 and M′ playing the roles of G,U1,U2,ε,M,k and M′, respectively to obtain a regularity partition V1 ∪···∪Vm and the reduced graph R = R(ε,γ/2) of order m with ε−1 ≤ m ≤ M′. Note that R is K4-free by Lemma 2.8. We say that a triangle ijk in R is chubby if dG(Vi′,Vj′) ≥ 2/3 + γ for some i′j′ ∈ {i,j,k2 } . We ﬁrst show that there is no chubby triangle in R.

![image 100](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile100.png>)

Claim 3.2. No triangle in R is chubby. Proof. Suppose without loss of generality that {1,2,3} induces a triangle in R with d(V2,V3) ≥

- 2/3+γ. By the deﬁnition of regular pair, it is well-known that for each i ∈ [3], there exists a subset Vi∗ ⊆ Vi such that |Vi∗| = (1 − 2ε)|Vi| and δcr(G[V1∗,V2∗,V3∗]) ≥ γ|Vi∗|/3. Applying Lemma 3.1 to G[V1∗,V2∗,V3∗] with Vi∗s playing the roles of Zis, we obtain a set S ⊆ V1∗ of size at least 13 m n 2/3 such


![image 101](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile101.png>)

![image 102](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile102.png>)

that every pair P ∈ S2 satisﬁes |N(P,Vi∗)| ≥ (γ3)9n/m for each i ∈ {2,3}. As 13 m n 2/3 ≥ α(G), the set S contains an edge uv ∈ E(G) with |N(uv,Vi∗)| ≥ (γ3)9n/m for each i ∈ {2,3}. Using Lemma 2.7 and again deleting low degree vertices, we get Vi′ ⊆ N(uv,Vi∗) for i ∈ {2,3} such that |V2′| = |V3′| ≥ γ10n/m; (V2′,V3′) is (√ε, 32 + γ4)-regular with δ(G[V2′,V3′]) ≥ (32 + γ5)|V3′|. Observe that V2′ must contain a triangle, as otherwise Theorem 2.4 implies that there exists an independent set of size at least

![image 103](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile103.png>)

![image 104](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile104.png>)

![image 105](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile105.png>)

![image 106](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile106.png>)

![image 107](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile107.png>)

![image 108](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile108.png>)

![image 109](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile109.png>)

![image 110](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile110.png>)

![image 111](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile111.png>)

![image 112](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile112.png>)

n m

- 1

![image 113](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile113.png>)

- 2


1 m

- 1

![image 114](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile114.png>)

- 2 |V2′|log |V2′| ≥


n m

![image 115](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile115.png>)

![image 116](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile116.png>)

![image 117](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile117.png>)

γ10

log γ10

nlog n > δ nlog n ≥ α(G),

>

- (3.1)


![image 118](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile118.png>)

![image 119](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile119.png>)

![image 120](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile120.png>)

a contradiction. Let T be a triangle in V2′. Then we have that |N(T,V3′)| ≥ 3δ(G[V2′,V3′]) − 2|V3′| ≥

n m

γ 2|V3′| ≥ γ12

.

![image 121](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile121.png>)

![image 122](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile122.png>)

Almost identical calculation as (3.1) shows that N(T,V3′) contains a triangle, which together with u, v and T forms a copy of K8, a contradiction.

X1

F(n5,d) F(n5,d)

![image 123](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile123.png>)

F2

A B

![image 124](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile124.png>)

F(n2,d) F(n2,d) F(n5,d)

![image 125](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile125.png>)

![image 126](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile126.png>)

![image 127](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile127.png>)

F1

F1

F(n5,d)

![image 128](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile128.png>)

F(n5,d)

![image 129](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile129.png>)

X2

X3

Figure 1: Constructions for s = 3,4,5 in order. Colour 1: dotted blue. Colour 2: red.

We are now ready to prove Theorem 1.3. Let t ∈ R be such that e(R) = m2/4 + t. If t < 0, then (2.1) with the deﬁnition of R = R(ε,γ/2) implies that

e(G) ≤ (m2/4)(n/m)2 + n2/m + γn2/2 ≤ n2/4 + γn2 as 1/m ≪ γ. We may thus assume t ≥ 0.

Recall that R is K4-free, Tura´n’s theorem implies that e(R) ≤ m2/3 and t/m2 ≤ 1/12; and by Lemma 2.1, E(R) can be decomposed into m2/4 − 2t edges and t edge-disjoint triangles. Each triangle in R, by Claim 3.2, corresponds to at most

3 · (2/3 + γ) · (n/m)2 = (2 + 3γ)(n/m)2 edges in G. Hence

m2 4 − 2t + (2 + 3γ)t

n2 m2

n2 4

n2 m

γ 2

+ γn2, as desired.

n2 ≤

e(G) ≤

+

+

![image 130](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile130.png>)

![image 131](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile131.png>)

![image 132](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile132.png>)

![image 133](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile133.png>)

![image 134](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile134.png>)

4. Lower bound constructions for ̺(K3,Ks,δ)

For each s ∈ {3,4,5} and small δ > 0, we will construct an n-vertex (K3,Ks)-free graph G with α(G) ≤ δn and the desired edge-density. This provides a lower bound on ̺(K3,Ks,δ). Throughout this section, we use X1,... ,Xk for the partite sets of Tk(n).

- 4.1. Lower bound for ̺(K3,Ks,δ) when s ∈ {3,5}. If s = 3, let G be a graph obtained from putting a copy of F(n2,d), for some d ∈ [δn − o(n),δn], in both partite sets of T2(n). It is easy


![image 135](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile135.png>)

to see that α(G) ≤ δn and e(G) = n42 + δn22 + o(n2). It is also easy to check that the following edge-colouring φ is a (K3,K3)-free colouring: φ(e) = 1 for all e ∈ ∪i∈[2]G[Xi]; and φ(X1,X2) = 2, see Figure 1.

![image 136](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile136.png>)

![image 137](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile137.png>)

If s = 5, let G be a graph obtained from putting a copy of F(n5,d), for some d ∈ [δn − o(n),δn], in each partite set of T5(n). It is easy to see that α(G) ≤ δn and e(G) = 2n52 + δn22 + o(n2). It is also easy to check that the following edge-colouring φ is a (K3,K5)-free colouring: φ(e) = 2 for all e ∈ ∪i∈[5]G[Xi]; φ(Xi,Xi+1) = 2 for all i ∈ [5] (addition modulo 5); and all other edges are of colour

![image 138](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile138.png>)

![image 139](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile139.png>)

![image 140](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile140.png>)

- 1, see Figure 1.


- 4.2. Lower bound for ̺(K3,K4,δ). We construct an n-vertex (K3,K4)-free graph G with α(G) ≤ δn and (13 + 2δ + 32δ2 − o(1))n2 edges as follows.


![image 141](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile141.png>)

![image 142](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile142.png>)

![image 143](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile143.png>)

- • By Theorem 2.2, there exist F1 := F(n3,d1) and F2 := F(n3 −δn,d2) where di ∈ [δn−o(n),δn] for each i ∈ [2]. So e(F1) = δn62 + o(n2) and e(F2) = δn62 − δ22n2 + o(n2).


![image 144](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile144.png>)

![image 145](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile145.png>)

![image 146](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile146.png>)

![image 147](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile147.png>)

![image 148](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile148.png>)

- • Let B = {b1,b2,... ,bd2} be an independent set of size d2 in F2. Let F be an n/3-vertex graph obtained from F2 by

- – ﬁrst adding a clone set of B, i.e. a set of d2 new vertices A = {a1,a2,... ,ad2} with NF(ai) := NF2(bi) for each i ∈ [d2];
- – adding all [A,B]-edges; and
- – adding an additional set of δn − d2 isolated vertices.


Note that F is not triangle-free, and

e(F) = e(F2) + d22 + d22 =

δn2 6

![image 149](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile149.png>)

+

3δ2n2 2

![image 150](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile150.png>)

+ o(n2).

- • Finally, let G be the graph obtained from T3(n) on partite sets Xi, i ∈ [3], by putting a copy of F in X1 and a copy of F1 in X2 and X3.


It is clear that G has the desired size and easy to check that the following 2-edge-colouring φ of G is (K3,K4)-free, see Figure 1:

- • let φ(A,X2) = φ(B,X3) = φ(X2,X3) = 1;
- • let φ(e) = 1, for all e ∈ E(G[X1] \ [A,B]);
- • all other edges are of colour 2.


5. Upper bound for ̺(K3,K4,δ) For the convenience of the reader, we rephrase the upper bound as follows.

- Lemma 5.1. Suppose 0 < 1/n ≪ δ ≪ 1. Let G be an n-vertex (K3,K4)-free graph with α(G) ≤ δn. Then

e(G) ≤

n2 3

![image 151](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile151.png>)

+

δn2 2

![image 152](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile152.png>)

+

3δ2n2 2

![image 153](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile153.png>)

.

We use the stability approach. A weak stability was proven in [10]1, stating that an n-vertex (K3,K4)-free graph G with α(G) ≤ δn is close to T3(n). For the exact result for ̺(K3,K4,δ), we need a coloured stability, which roughly says that any (K3,K4)-free colouring of an almost extremal graph should look similar to the colouring given in the lower bound construction.

5.1. Coloured stability.

- Lemma 5.2. Suppose 0 < 1/n ≪ δ ≪ γ < 1. Let G be an n-vertex (K3,K4)-free graph with α(G) ≤ δn and δ(G) ≥ 2n/3. Then for any (K3,K4)-free 2-edge colouring φ : E(G) → [2], there exists a partition X1 ∪ X2 ∪ X3 of V (G) such that the following holds.


- (A1) For each i ∈ [3], we have |Xi| = n/3 ± 2γ1/7n.
- (A2) α(G1[X1]) ≤ γ1/4n.
- (A3) For each i ∈ [3], we have ∆(G[Xi]) ≤ γ1/18n.
- (A4) For each v ∈ X1, we have min{dG1(v,X2), dG1(v,X3)} < γ1/9n.
- (A5) δcr(G[X1,X2,X3]) ≥ n/3 − γ1/19n.
- (A6) For all i ∈ {2,3} and v ∈ Xi, we have dG2(v,X1) ≥ |X1| − γ1/20n.


Furthermore, one of the following occurs:

- (P1) For all i ∈ {2,3} and v ∈ Xi, we have α(G2[Xi]) ≤ γ1/4n and dG1(v,X5−i) ≥ |X5−i|−γ1/20n.
- (P2) For all i ∈ {2,3} and v ∈ Xi, we have α(G1[Xi]) ≤ γ1/4n and dG2(v,X5−i) ≥ |X5−i|−γ1/20n. We need an additional deﬁnition for the proof of Lemma 5.2.


Deﬁnition 5.3. Given a weighted graph R with weight d : E(R) → (0,1] and Y ⊆ X ⊆ V (R), a γ-generalised clique of order t := |X| + |Y |, denoted by Zt, on (X,Y ) is a clique on X with

- d(e) > 1/2 + γ for every e ∈ E(R[Y ]). 1Their proof missed a case, which can be easily ﬁxed. We include it in the online arXiv version.


![image 154](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile154.png>)

For brevity, we will write (a1a2 ... as,b1b2 ... bs′) for ({a1,... ,as},{b1,... ,bs′}). Note that, for an n-vertex 2-edge-coloured graph G with α(G) = o(n), both G1,G2 can have Ω(n) independence number. We will use the following lemma combined with regularity lemma to obtain a regular partition such that each part of the partition induces a graph with small independence number in one of the two colours.

- Lemma 5.4 (Lemma 3.1 in [2] with r = 2). Let c > 0, G be an n-vertex graph with α(G) ≤ c2n


and φ : E(G) → [2]. Then there exists a partition V (G) = V1∗ ∪ V2∗2 such that for every i ∈ [2], α(Gi[Vi∗]) ≤ cn.

- Proof of Lemma 5.2. We choose the constants as follows: 0 < 1/n ≪ δ ≪ δ∗ ≪ 1/m ≪ ε ≪ γ ≪ 1.


We apply Lemma 5.4 with c = δ1/2 to obtain a partition V1∗ ∪ V2∗ such that α(Gi[Vi∗]) ≤ δ1/2n. Apply Theorem 2.5 with G,V1∗,V2∗,φ,ε,ε−1 and M′ playing the roles of G,U1,U2,φ,ε,M and M′ to obtain an ε-regular partition V1 ∪··· ∪ Vm with ε−1 ≤ m ≤ M′ which reﬁnes the partition V1∗ ∪ V2∗. Let R := R(ε,γ,φ,(Vi)i∈[m]) be its reduced graph. It was shown in [10] (Theorem 3(b) and (e)) that |G△T3(n)| ≤ δ∗n2. As a consequence, the number of K4 in G is at most δ∗n4. It is well-known that the reduced graph R essentially inherits the structure of G: δ(R) ≥ (2/3 − 3γ)m and R is K4-free. Indeed, if K4 ⊆ R, then by Lemma 2.6, G contains at least (γ/2)6(n/m)4/2 > δn4 copies of K4, a contradiction. Thus, by Theorem 2.3,

- (5.1) |R△T3(m)| ≤ γ1/3m2. We deﬁne a colouring φind : V (R) ∪ E(R) → [2], induced by φ, as follows:

- (i) for each k ∈ [m], we have φind(k) = i if Vk ⊆ Vi∗; and
- (ii) for each pq ∈ E(R), we have φind(pq) = 1 if dG1(Vp,Vq) ≥ γ, and φind(pq) = 2 if dG1(Vp,Vq) < γ and dG2(Vp,Vq) ≥ γ.


We remark that colour 1 has “higher priority” on E(R) in φind, i.e. if (Vi,Vj) is dense in both G1 and G2, then we have φind(ij) = 1. This asymmetry is needed for the embedding later. For each pq, we let d(pq) := dG

φind(pq)

(Vp,Vq) be the weight on E(R), and we consider R as a weighted graph. It is also well-known that for each p ∈ V (R), we have

q∈NR(p)

d(pq) ≥

- m

![image 155](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile155.png>)

- n


2

δ(G)

n m −

![image 156](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile156.png>)

εn2 m −

![image 157](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile157.png>)

2γn2 m −

![image 158](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile158.png>)

n m

![image 159](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile159.png>)

2

- (5.2) ≥ (2/3 − 3γ)m.

Let R′ be the graph obtained from R by deleting all edges of weight at most 1/2 + γ. Then for each p ∈ V (R), we have

(2/3 − 3γ)m ≤

q∈NR(p)

d(pq) ≤ dR′(p) + (1/2 + γ)(dR(p) − dR′(p)),

thus, as δ(R) ≥ (2/3 − 3γ)m, we have

- (5.3) dR′(p) ≥ 4m/3 − dR(p) − 9γm. Moreover, by (5.1), we know e(R) ≤ m32 + γ1/3m2. As δ(G) ≥ 2n/3, similar to (2.1), we have

![image 160](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile160.png>)

n2/3 ≤ e(G) ≤ (e(R) − e(R′))

(1/2 + γ)n2 m2

![image 161](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile161.png>)

+ e(R′)

n2 m2

![image 162](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile162.png>)

+ (2γ + ε + 1/m)n2. This implies

- (5.4) e(R) − e(R′) ≤ γ1/4m2.


![image 163](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile163.png>)

2It could be that some Vi∗ is empty.

We will omit γ in the term ‘γ-generalised clique’. For each i ∈ [2] and Y ⊆ X ⊆ V (R), we say that a generalised clique Zt in R on (X,Y ) is of colour i if φind(k) = φind(pq) = i, for all k ∈ Y

and pq ∈ X2 . We say that R is (Zt1,Zt2)-free if there is no Zti of colour i for any i ∈ [2]. It was implicitly proven in the proof Theorem 1.3 in [2] that a Zt of colour i in R implies Kt ⊆ Gi. This implies the following, since G is (K3,K4)-free:

- (5.5) R is (Z3,Z4)-free.

Let U1 ∪ U2 ∪ U3 be a max-cut 3-partition of R. The desired partition of V (G) will be an adjustment of this partition. By (5.1) and the deﬁnition of max-cut and Theorem 2.3, it is easy to see that we have

- (5.6) i∈[3]

e(R[Ui]) ≤ γ1/3m2, |Ui| = m/3 ± γ1/7m and

- (5.7) δcr(R[U1,U2,U3]) ≥ (δ(R) − max i∈[3]


|Ui|)/2 ≥ m/7.

We will obtain the colour pattern of R in φind. First we show that each vertex set Ui is monochromatic in φind.

- Claim 5.5. For every i ∈ [3], there exist j ∈ [2] such that φind(Ui) = j. In particular, we have


√

![image 164](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile164.png>)

α(Gj[∪k∈UiVk]) ≤

δn. Proof. Suppose the lemma is not true, then by symmetry, we may assume that φ(U1) = j for any

- j ∈ [2]. Let W := {w ∈ U1 : φind(w) = 2}. We shall argue that one of the following two cases must happen and then derive contradictions in each case. Case 1. There exists vertices u,w ∈ U1 v2 ∈ U2, v3 ∈ U3 such that {v2v3,uv2,uv3} ⊆ E(R) and wv2,wv3 ⊆ E(R′) and φind(u) = 1,φind(w) = 2. Case 2. There exists vertices u,w ∈ U1 v2 ∈ U2, v3 ∈ U3 such that R[{u,w,v2,v3}] induces a copy of K4 and φind(u) = 1,φind(w) = 2.


Suppose that |W| ≥ m/100. Fix an arbitrary u ∈ U1 with φind(u) = 1. Then, by (5.4), more than half of the vertices w in W satisfy dR′(w) ≥ dR(w) − γ1/5m, and as i∈[3] e(R[Ui]) ≤ γ1/3m2, more than half of the vertices w in W satisﬁes |NR(w,U1)| ≤ γ1/4m. Hence there exists w ∈ W with |NR′(w,Ui)| ≥ δ(R) − |U5−i| − 2γ1/5m ≥ m/4 for each i ∈ {2,3}. By this and (5.7), for each i ∈ {2,3} we have

|NR(u,Ui) ∩ NR′(w,Ui)| ≥ m/7 + m/4 − |Ui| ≥ m/30. Together with (5.1) and the deﬁnition of max-cut partition, this implies that there exists an edge v2v3 between NR(u,U2) ∩ NR′(w,U2) and NR(u,U3) ∩ NR′(w,U3), yielding Case 1.

We may then assume that |W| ≤ m/100. Fix an arbitrary w ∈ W. If |NR(w,U1)| > m/50, then we have |NR(w,U1 \ W)| ≥ m/100. As i∈[3] e(R[Ui]) ≤ γ1/3m2, more than half of the vertices u in NR(w,U1 \ W) satisfy |NR(u,U1)| ≤ γ1/4m. Hence there exists u ∈ NR(w,U1 \ W) with |NR(u,Ui)| ≥ m/4 for each i ∈ {2,3}. By this and (5.7), for each i ∈ {2,3} we have

|NR(u,Ui) ∩ NR(w,Ui)| ≥ m/7 + m/4 − |Ui| ≥ m/30.

Thus by (5.1) and the deﬁnition of max-cut partition, there exists an edge v2v3 between NR(uw,U2) and NR(uw,U3), yielding Case 2.

Thus we may assume that |NR(w,U1)| ≤ m/50, thus dR(w) ≤ |U2|+|U3|+m/50 ≤ (2/3+1/40)m. Together with (5.3), this implies that

dR′(w) ≥ 4m/3 − (2/3 + 1/40)m − 9γm ≥ (2/3 − 1/30)m. Hence, for each i ∈ {2,3}, we have

|NR′(w,Ui)| ≥ dR′(w) − |NR(w,U1)| − |U5−i| ≥ (1/3 − 1/30 − 1/40)m ≥ m/4.

By (5.7), there exists a vertex u ∈ U1 \ W such that for each i ∈ {2,3}, we have |NR(u,Ui) ∩ NR′(w,Ui)| ≥ m/4 + m/7 − |U2| ≥ m/30.

Thus by (5.1) and the deﬁnition of max-cut partition, there exists an edge v2v3 between NR(u,U2)∩ NR′(w,U2) and NR(u,U3) ∩ NR′(w,U3), yielding again Case 1.

For each i ∈ {2,3} and j ∈ [2], if φind(Ui) = j, then, by the deﬁnition of φind, we have ∪k∈UiVk ⊆ Vj∗, and so α(Gj[∪k∈UiVk]) ≤ α(Gj[Vj∗]) ≤

√

![image 165](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile165.png>)

δn as desired. We shall now derive contradictions in each case to ﬁnish the proof.

Suppose Case 1 happens. By the deﬁnition of R′, for each i ∈ {2,3} we have d(wvi) ≥ 1/2 + γ. As φind(u) = 1, we must have φind(uvi) = 2 for i ∈ {2,3}, otherwise we get a Z3 of colour 1 on (uvi,u), contradicting (5.5). Suppose now that φind(v2v3) = 2. For each i ∈ {2,3}, it must be that φind(vi) = 1, otherwise (uv2v3,vi) is a Z4 of colour 2, which in turn implies that φind(wvi) = 2, otherwise (wvi,vi) is a Z3 of colour 1. But then (wv2v3,w) is a Z4 of colour 2, a contradiction.

Hence, we may assume that φind(v2v3) = 1. For each i ∈ {2,3}, we must have φind(vi) = 2, otherwise we get a Z3 of colour 1 on (v2v3,vi), a contradiction. As d(wvi) ≥ 1/2+γ and φind(w) = 2, we must have φind(wvi) = 1, otherwise we get a Z4 of colour 2 on (wvi,wvi). However, then we have a Z3 of colour 1 on (wv2v3,∅), a contradiction.

Suppose Case 2 happens. As φind(u) = 1, we must have φind(uw) = φind(uvi) = 2 for i ∈ {2,3}, otherwise we get a Z3 of colour 1 on (uvi,u) or (uw,u), contradicting (5.5).

Suppose now that φind(v2v3) = 2. Then for each i ∈ {2,3}, we have φind(vi) = 1, otherwise (uv2v3,vi) is a Z4 of colour 2, which in turn implies that φind(wvi) = 2 for each i ∈ {2,3}. But then (wuv2v3,∅) is a Z4 of colour 2, a contradiction.

Hence, we may assume that φind(v2v3) = 1, Then for each i ∈ {2,3}, we must have φind(vi) =

- 2, otherwise we get Z3 of colour 1 on (v2v3,vi). Moreover, for each i ∈ {2,3}, we must have φind(wvi) = 1, otherwise (viuw,w) is a Z4 of colour 2. But then (wv2v2,∅) forms a Z3 of colour 1, a contradiction.


- Claim 5.6. By permuting indices of U1,U2,U3, we may assume the following. We have φind(U1) = 1 and for each i ∈ {2,3}, we have φind(U1,Ui) = 2 and one of the following holds.

- (B1) φind(U2) = φind(U3) = 2 and φind(U2,U3) = 1; or
- (B2) φind(U2) = φind(U3) = 1 and φind(U2,U3) = 2.


Proof. If φind(Ui) = 2 for all i ∈ [3], then it is easy to see that all crossing edges of R′ are of colour

- 1, otherwise we obtain a generalised clique Z4 of colour 2. However, then we can easily check that R contains a copy of K3 of colour 1, which is again a contradiction.


Hence, by Claim 5.5, we may assume that φind(U1) = 1. Then as R does not have a generalised clique Z3 of colour 1, we have that φind(U1,Ui) = 2 for i ∈ {2,3}. If φind(U2) = 2, then φind(U2,U3) = 1, otherwise we get a generalised clique Z4 of colour 2. But then we must have φind(U3) = 2, giving (B1). Similarly if φind(U2) = 1, we obtain (B2).

Let V (G) = X1′ ∪ X2′ ∪ X3′ be the partition corresponding to V (R) = U1 ∪ U2 ∪ U3, i.e. Xi′ := ∪k∈UiVk, then (5.6) implies that for each i ∈ [3] we have |Xi′| = n3 ± 32γ1/7n. Note that we have (5.8)

![image 166](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile166.png>)

![image 167](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile167.png>)

i∈[3]

e(G[Xi′]) ≤

i∈[3]

e(R[Ui]) ·

n m

![image 168](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile168.png>)

2

+ εn2 +

n2 m

![image 169](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile169.png>)

+ 2γn2

(5.6) ≤ 2γ1/3n2.

Note that (5.7) provides a minimum crossing degree of R with respect to the partition U1 ∪U2 ∪U3. However, in G, some vertex could have low crossing degree with respect to the partition X1′ ∪X2′ ∪X3′. To amend this problem, we will consider the following modiﬁed partition X1 ∪ X2 ∪ X3 of V (G).

- Claim 5.7. There exists a partition X1 ∪ X2 ∪ X3 of V (G) such that the following holds. (X1) For each i ∈ [3], we have |Xi| = n/3 ± 2γ1/7n and |Xi△Xi′| ≤ 20γ1/3n.


(X2) δcr(G[X1,X2,X3]) ≥ n/10.

Proof. For all i ∈ [3] and v ∈ Xi′, if d(v,Xj′) ≤ n/10 for some j = i, then move v to Xj′. We repeat this until no such vertex exists. Let the resulting set be Xi, i ∈ [3]. We ﬁrst show that this process terminates and so Xis are well-deﬁned.

Recall that δ(G) ≥ 2n/3, so if there exist ij ∈ [3]2 and v ∈ Xi′ with d(v,Xj′) ≤ n/10, we see that for each k = j,

|Xi′| ≥ n/5.

d(v,Xk′ ) ≥ δ(G) − n/10 − max i∈[3]

Thus, after moving v from Xi′ to Xj′, the number of inner edges decreases by at least n/5 − n/10 = n/10. Hence, by (5.8), after moving at most 2γ1/3n2/(n/10) = 20γ1/3n vertices, the process stops. Hence, we obtain (X1) proving the ﬁrst part and (X2) holds by deﬁnition.

Note that (A1) holds due to (X1). By Claims 5.5, 5.6 and (X1), we have (A2) as

- (5.9) α(G1[X1]) ≤ α(G1[X1′]) + ||X1′| − |X1|| ≤

√

![image 170](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile170.png>)

δn + 20γ1/3n ≤ γ1/4n.

For what follows, we assume (B1) holds, which then leads to (P1) ((B2) implying (P2) can be proven analogously). Similar to (5.9), (B1) implies that α(G2[Xi]) ≤ γ1/4n for i ∈ {2,3}, proving the ﬁrst part of (P1).

We now bound ∆(G[Xi]) for each i ∈ {2,3}. Without loss of generality, it is enough to bound ∆(G[X2]). Note ﬁrst that, as G1 is K3-free, by (5.9), for each v ∈ V (G), we have

- (5.10) dG1(v,X1) ≤ α(G1[X1]) ≤ γ1/4n. Deﬁne

J :=

i∈[3]

{v ∈ Xi : d(v,Xi) ≤ |Xi| − γ1/8n}

![image 171](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile171.png>)

![image 172](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile172.png>)

to be the set of vertices with large missing crossing degree. By Claim 5.7 and (5.8), we have

i∈[3]

e(G[Xi]) ≤

i∈[3]

(e(G[Xi′]) + ||Xi′| − |Xi||n) ≤ γ1/4n2,

and so, as e(G) ≥ n32 and e(K|X1|,|X2|,|X3|) ≤ n2/3, we have that e(G[X1,X2,X3]) ≤

![image 173](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile173.png>)

![image 174](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile174.png>)

n2 3 − (e(G) −

![image 175](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile175.png>)

i∈[3]

e(G[Xi])) ≤

i∈[3]

e(G[Xi]) ≤ γ1/4n2 and

|J| ≤

2e(G[X1,X2,X3]) γ1/8n

![image 176](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile176.png>)

![image 177](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile177.png>)

- (5.11) = 2γ1/8n. We claim that for each y ∈ X3, we have
- (5.12) dG2(y,X2) ≤ 3γ1/8n and dG1(y,X3) ≤ |J| ≤ 2γ1/8n.


Indeed, suppose that dG2(y,X2) > 3γ1/8n. Then |NG2(y,X2) \ J| ≥ γ1/8n > α(G2[X2]), and so there exists uv ∈ E(G2) with u,v ∈ NG2(y,X2) \ J. By (X2), (5.10) and the deﬁnition of J, we have

|NG2({u,v,y},X1)| ≥ δcr(G[X1,X2,X3]) −

dG1(x,X1) − 2 · γ1/8n ≥ n/20,

x∈{u,v,y}

showing that K4 ⊆ G2, a contradiction, thus the ﬁrst part of (5.12) holds.

Suppose that dG1(y,X3) > |J|. So there exists yy′ ∈ E(G1[X3]) with y′ ∈/ J. But then the ﬁrst part of (5.12) implies that

|NG1({y,y′},X2)| ≥ δcr(G[X1,X2,X3]) −

dG2(x,X2) − γ1/8n ≥ n/20,

x∈{y,y′}

- contradicting K3  ⊆ G1. Thus (5.12) holds. We now show that for each y ∈ X3, we have dG2(y,X3) ≤ 3γ1/17n, which together with (5.12)

implies that ∆(G[X3]) ≤ γ1/18n. Fix an arbitrary y ∈ X3 and let Y := NG2(y,X3). suppose to the contrary that |Y | > 3γ1/17n. For i ∈ [2], deﬁne

Ji := {v ∈ Xi : dGi(v,X3) ≥ γ1/16n}. By (5.10) and (5.12), we get, for each i ∈ [2], that

|Ji| ≤

e(Gi[Xi,X3]) γ1/16n ≤

![image 178](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile178.png>)

|X3| · max{γ1/4n,3γ1/8n} (5.13) γ1/16n ≤ 3γ1/16n. As |NG2(y,X1)| ≥ δcr(G[X1,X2,X3])−dG1(y,X1) > |J|+|J1| due to (5.10) and (5.11), we can pick u ∈ NG2(y,X1) \ (J ∪ J1). By the deﬁnition of J and J1, we have

![image 179](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile179.png>)

dG2(u,Y ) ≥ |Y | − dG(u,X1) − dG1(u,X3) ≥ |Y | − γ1/17n.

![image 180](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile180.png>)

![image 181](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile181.png>)

Similarly, we can pick v ∈ X2 \ (J ∪ J2) with dG1(v,Y ) ≥ |Y | − γ1/17n. Thus, writing Y ′ := NG1(v,Y ) ∩ NG2(u,Y ), we have |Y ′| ≥ |Y | − 2γ1/17n > α(G). So there exists xx′ ∈ E(G[Y ′]). However, if φ(xx′) = 1, then {x,x′,v} induces a K3 in G1; while if φ(xx′) = 2, then {x,x′,u,y} induces a K4 in G2, a contradiction. This shows ∆(G[X3]) ≤ γ1/18n, and ∆(G[X2]) ≤ γ1/18n.

To bound ∆(G[X1]), we need to ﬁrst prove (A4) that no vertex in X1 can have high G1-degree to both X2 and X3. Suppose that v ∈ X1 is such that dG1(v,Xi) ≥ γ1/9n > |J| for both i ∈ {2,3}. Fix an arbitrary u ∈ NG1(v,X3) \ J. Then by (5.12) and the fact that u ∈/ J, we have

|NG1({v,u},X2)| ≥ dG1(v,X2) − dG(u,X3) − dG2(u,X2) ≥ γ1/8n, which contradicts K3  ⊆ G1, proving (A4).

![image 182](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile182.png>)

![image 183](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile183.png>)

Fix an arbitrary w ∈ X1, suppose to the contrary that d(w,X1) ≥ γ1/18n > dG1(w,X1)+|J ∪J1|, due to (5.10) and (5.11) and (5.13). Fix a vertex u ∈ NG2(w,X1) \ (J ∪ J1). By (A4), we may assume that dG1(w,X3) < γ1/9n. Then by (X2) and the fact that u ∈/ J ∪ J1, we have

|NG2({w,u},X3)| ≥ δcr(G[X1,X2,X3]) − dG1(w,X3) − dG(u,X1) − dG1(u,X3) > α(G2[X3]),

![image 184](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile184.png>)

![image 185](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile185.png>)

- contradicting K4  ⊆ G2. Thus, for each i ∈ [3], we have ∆(G[Xi]) ≤ γ1/18n, proving (A3). Consequently,


δcr(G[X1,X2,X3]) ≥ δ(G) − max i∈[3]

(∆(G[Xi]) + |Xi|) ≥ n/3 − γ1/19n,

- proving (A5). Together with (A1), this implies that for all i ∈ {2,3} and v ∈ Xi, we have

dG2(v,X1) ≥ δcr(G[X1,X2,X3]) − dG1(v,X1)

(5.10)

≥ |X1| − γ1/20n, and that

dG1(v,X5−i) ≥ δcr(G[X1,X2,X3]) − dG2(v,X5−i)

(5.12) ≥ |X5−i| − γ1/20n,

- proving (A6) and the second part of (P1) as desired.


- 5.2. Proof of Lemma 5.1. Suppose that e(G) > (13 + 2δ + 32δ2 )n2. By applying Lemma 2.9 with G,2/3,δ + 3δ2 playing the roles of G,d,ε, respectively, to obtain an n′-vertex graph G′ with n′ ≥ δ1/2n/2. Then δ(G′) ≥ 2n′/3. Let δ′ := δn/n′ ∈ [δ,δ1/3]. Since 1 ≤ α(G′) ≤ α(G) = δn = δ′n′, we have


![image 186](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile186.png>)

![image 187](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile187.png>)

![image 188](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile188.png>)

3δ2 2

δ′ 2

3δ′2 2

n′2 3

n − n′ 3 ≥

δ 2

1 3

- (5.14) e(G′) ≥


n2 −

n′2.

+

+

+

+

![image 189](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile189.png>)

![image 190](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile190.png>)

![image 191](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile191.png>)

![image 192](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile192.png>)

![image 193](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile193.png>)

![image 194](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile194.png>)

![image 195](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile195.png>)

Note that φ still induces an edge-colouring of G′ which is (K3,K4)-free. As 1/n ≪ δ ≪ γ and n′ ≥ δ1/2n/2 and δ′ ∈ [δ,δ1/3], we can apply Lemma 5.2 with G′,δ′,γ playing the roles of G,δ,γ

to obtain a partition X1 ∪ X2 ∪ X3 of V (G′) satisfying (A1)–(A6). We assume that (P1) occurs.3. Deﬁne

(v,X3) ≥ n′/5}. Note that (A4) implies that A ∩ B = ∅. Bounding e(G) amounts to show the following claim.

(v,X2) ≥ n′/5} and B := {v ∈ X1 : dG′

A := {v ∈ X1 : dG′

1

1

- Claim 5.8. The following hold:


- (G′1) For each i ∈ {2,3}, the graph G′[Xi] is K3-free.
- (G′2) Both A and B are independent sets and so |A|,|B| ≤ α(G′) ≤ δ′n′.
- (G′3) Both G′[X1 \ A] and G′[X1 \ B] are K3-free.


First, we show how Claim 5.8 implies Lemma 5.1. For each i ∈ {2,3}, (G′1) implies that ∆(G′[Xi]) ≤ α(G′) ≤ δ′n′, and so e(G′[Xi]) ≤ δ′n′|Xi|/2. On the other hand, (G′2) and (G′3) imply that ∆(G′[X1 \ A]),∆(G′[X1 \ B]) ≤ α(G′) ≤ δ′n′, and so e(G′[A,X1 \ (A ∪ B)]) ≤ δ′n′|A|. Therefore,

e(G′[X1]) = e(G′[X1 \ A]) + e(G′[A,B]) + e(G′[A,X1 \ (A ∪ B)])

≤ (|X1| − |A|)δ′n′/2 + |A|δ′n′ + δ′n′|A| ≤ δ′n′|X1|/2 + 3δ′2n′2/2. Thus, we have

e(G′) ≤ e(G′[X1,X2,X3]) +

e(G′[Xi]) ≤ n′2/3 + δ′n′2/2 + 3δ′2n′2/2,

i∈[3]

- contradicting (5.14). Thus we conclude that e(G) ≤ (31 + 2δ + 32δ2)n2. Proof of Claim 5.8. Fix arbitrary i ∈ {2,3}. Suppose that T = {u,v,w} induces a triangle in


![image 196](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile196.png>)

![image 197](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile197.png>)

![image 198](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile198.png>)

G′[Xi]. By (A1) and (P1), we see that |NG′

(T,X5−i)| ≥ n/4. As G′1 is K3-free, this implies that

1

(T,X1)| ≥ n/4. This contradicts K4  ⊆ G′2, proving (G′1).

- T is monochromatic in colour 2. But then, by (A6), we have |NG′


2

Suppose that uv is an edge in G′[A] (the proof for B is similar). By the deﬁnition of A and (A1), we have |NG′

(uv,X2)| ≥ 2n/5 − |X2| ≥ n/20, implying that φ(uv) = 2 as G′1 is K3-free. Also by (A4) and the fact that u,v ∈ A, we see that both dG′

1

(v,X3) are less than γ1/9n. Thus, by (A5), we have that

(u,X3) and dG′

1

1

(uv,X3)| ≥ 2(δcr(G′[X1,X2,X3]) − γ1/9n) − |X3| ≥ n/4 > α(G′2[X3]). Hence, there exists an edge of colour 2 in NG′

|NG′

2

(uv,X3), contradicting K4  ⊆ G′2, proving (G′2).

2

Suppose T = {u,v,w} induces a triangle in X1 \ B (the proof for X1 \ A is similar). Since G′1 is K3-free, we may assume that φ(uw) = 2. To prove (G′3), it suﬃces to show that |NG′

(uw,Xi)| ≥

2

n/30 > α(G′2[Xi]) for some i ∈ {2,3}, since then K4 ⊆ G′2, a contradiction. As A is an independent set due to (G′2), we may further assume that w ∈/ A ∪ B. By the deﬁnition of A and B, we have

(w,Xi) ≥ δcr(G′[X1,X2,X3]) − n/5 ≥ n/10, ∀ i ∈ {2,3}. For each i ∈ {2,3}, let Wi := NG′

- (5.15) dG′


2

(u,X2) ≥ dG′

(u,W2) ≥ n/20, since otherwise |NG′

(w,Xi). Note that dG′

2

1

1

(u,X3) < γ1/9n. Together with (A1), (A5) and (5.15), we have

(uw,X2)| ≥ n/30 as desired. Then (A4) implies that dG′

2

1

(uw,X3)| ≥ δcr(G′[X1,X2,X3]) − dG′

(w,X3) − |X3| ≥ n/30, as desired.

|NG′

(u,X3) + dG′

1

2

2

This completes the proof of Lemma 5.1, providing the second equality of Theorem 1.1.

![image 199](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile199.png>)

3The (P2) case is only easier, we include its proof in the online arXiv version. In fact, graphs satisfying (P2) case can only have at most n′2/3 + δn′2/2 edges, a contradiction

6. Stability for ̺(K3,K3,δ) without regularity

In this section, we present the upper bound on ̺(K3,K3,δ).4 For convenience, we rephrase the upper bound as follows.

- Lemma 6.1. Suppose 0 < 1/n ≪ δ < 10−13. Let G be an n-vertex (K3,K3)-free graph with α(G) ≤ δn. Then


δn2 2

n2 4

e(G) ≤

. We will prove Lemma 6.1 using the following coloured stability.

+

![image 200](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile200.png>)

![image 201](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile201.png>)

Lemma 6.2. Suppose 0 < 1/n ≪ δ < 10−6. Let G be an n-vertex (K3,K3)-free graph with α(G) ≤ δn and δ(G) ≥ n/2. Then for any (K3,K3)-free φ : E(G) → [2], there exists a partition V (G) = A ∪ B with |A|,|B| = n/2 ± δ1/3n and δ(G1[A,B]) ≥ 2n/5.

We will present a proof of Lemma 6.2 without regularity lemma. First, we show how it implies Lemma 6.1.

- Proof of Lemma 6.1. Suppose that e(G) > (14+2δ)n2. By applying Lemma 2.9 with G,1/2,δ playing the roles of G,d,ε, respectively, to obtain an n′-vertex graph G′ with n′ ≥ δ1/2n/2 satisfying the following, where δ′ := δn/n′ ∈ [δ,106):


![image 202](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile202.png>)

![image 203](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile203.png>)

n′2 4

δn2 2 −

n − n′ 4 ≥

δ′ 2

1 4

δ(G′) ≥ n′/2 and e(G′) ≥

n′2. Moreover, α(G′) ≤ α(G) = δn = δ′n′.

+

+

![image 204](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile204.png>)

![image 205](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile205.png>)

![image 206](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile206.png>)

![image 207](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile207.png>)

![image 208](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile208.png>)

As G is (K3,K3)-free, G′ ⊆ G is also (K3,K3)-free and there exists an (K3,K3)-free 2 edgecolouring φ of G′. As 1/n ≪ δ and n′ ≥ δ1/2n/2 and δ′ < 10−6, we apply Lemma 6.2 to obtain a partition A ∪ B of V (G′) with |A|,|B| = n′/2 ± δ′1/3n and δ(G′1[A,B]) ≥ 2n′/5.

We claim that both G′[A] and G′[B] are triangle-free. Suppose that T ∈ A3 induces a triangle in G′[A]. Since G′1 is K3-free and |NG′

(T,B)| ≥ 3δ(G′1[A,B]) − 2|B| > n/6, we see that no edge in T can be of colour 1. But then T is monochromatic in colour 2, contradicting K3  ⊆ G′2. Thus,

1

- e(G′[A]) ≤ ∆(G′[A])|A|/2 ≤ α(G′)|A|/2 ≤ δ′n′|A|/2. Similarly, e(G′[B]) ≤ δ′n′|B|/2. Hence, e(G′) = e(G′[A,B]) + e(G′[A]) + e(G′[B]) ≤ n′2/4 + δ′n′2/2,


a contradiction. Thus we conclude e(G) ≤ (41 + 2δ)n2. Proof of Lemma 6.2. Assume without loss of generality that e(G1) ≥ e(G2), so e(G1) ≥ n2/8. It is easy to see that the following fact follows from G being (K3,K3)-free and that α(G) ≤ δn. Fact 6.3. For all x,y ∈ V (G), we have |NG1(x) ∩ NG2(y)| ≤ α(G) ≤ δn.

![image 209](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile209.png>)

![image 210](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile210.png>)

We will sequentially choose four vertices as follows.

- • Take a vertex x with maximum G1-degree, i.e. dG1(x) = ∆(G1), and set X := NG1(x). Then |X| ≥ 2e(nG1) ≥ n/4.

![image 211](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile211.png>)

- • Choose a vertex y ∈ X with maximum G1-degree and set Y := NG1(y). Note that as G1 is K3-free, X ∩ Y = ∅. Denote Z := V (G) \ (X ∪ Y ) and α := |Z|/n.
- • Pick now x′ ∈ Z with maximum G2-degree in Z. Let X′ := NG2(x′,Z) and β := |X′|/n. By deﬁnition, we have 0 ≤ β ≤ α.
- • Finally, take y′ ∈ X′ with maximum G2-degree in Z and set Y ′ := NG2(y′,Z). Similarly, as G2 is K3-free, X′ ∩ Y ′ = ∅. So |Y ′| ≤ |Z \ X′| = (α − β)n.


- Claim 6.4. We have |X| + |Y | ≥ n/3, consequently, α ≤ 2/3.


![image 212](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile212.png>)

4The upper bound on ̺(K3, K5, δ) can be proved by combining ideas in the proofs of the upper bounds on ̺(K3, K3, δ) and ̺(K3, K4, δ), we include its proof in the online arXiv version.

Proof. We may assume that |X| ≤ n/3 otherwise we are done. By the deﬁnition of x and X, every vertex in X (resp. not in X) has G1-degree at most |Y | (resp. |X|). Thus,

- (6.1)

n2 4 ≤ 2e(G1) ≤

![image 213](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile213.png>)

u/∈X

dG1(u) +

v∈X

dG1(v) ≤ (n − |X|)|X| + |X||Y |,

implying that f(a) := (1 − a)a + ab − 14 ≥ 0, where 1/4 ≤ a := |X|/n ≤ 1/3 and b := |Y |/n. As f′(a) = 1 + b − 2a > 0, we have 0 ≤ f(a) ≤ f(1/3), implying that b ≥ 1/12 and then a + b ≥ 1/3

![image 214](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile214.png>)

as desired. Let us show the following bound on the size of G1:

- (6.2) e(G1) ≤

(1 − β)2n2 4

![image 215](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile215.png>)

+ δn2.

Indeed, the ﬁrst term above bounds e(G1[X′]) as G1 is K3-free; while the second term bounds all G1-edges with at least one endpoints in X′. To see this, for each vertex v ∈ V (G), we have dG2(v,X′) ⊆ NG1(v) ∩ NG2(x′), thus the desired bound follows from Fact 6.3. Similarly, we can bound all G2-edges with at least one endpoints in X ∪ Y by 2δn2. Thus, we have that e(G2) ≤ e(G2[Z]) + 2δn2.

![image 216](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile216.png>)

Claim 6.5. We have that e(G2) ≤ 22δn2. Proof. As we have e(G2) ≤ e(G2[Z]) + 2δn2, it suﬃces to prove e(G2[Z]) ≤ 20δn2. Note ﬁrst that, by the deﬁnition of x′, we have that

- (6.3) e(G2[Z]) ≤

|X′| · |Z| 2

![image 217](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile217.png>)

=

αβn2 2

![image 218](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile218.png>)

. On the other hand, analogous to (6.1), by the deﬁnition of y′, we have

e(G2[Z]) ≤

- 1

![image 219](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile219.png>)

- 2


 

u∈Z\X′

dG2(u,Z) +

v∈X′

dG2(v,Z)

 

≤

1

![image 220](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile220.png>)

- (6.4) 2 |Z \ X′| · βn + |X′| · (α − β)n = (α − β)βn. We now distinguish two cases.

- Case 1 : β ≤ α/2. By (6.2) and (6.3), we have that

(6.5)

n2 4 ≤ e(G) ≤

![image 221](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile221.png>)

n2 4

![image 222](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile222.png>)

((1 − β)2 + 2αβ) + 3δn2 ⇔ (β2 − 2β + 2αβ) + 3δ ≥ 0.

- Let f(β) := β2 − 2β + 2αβ + 3δ ≥ 0, then f′(β) = 2β − 2 + 2α ≤ 3α − 2 ≤ 0 as α ≤ 2/3 due to Claim 6.4. So we have β ≤ 40δ, as otherwise

f(β) ≤ f(40δ) = 40δ(40δ − 2 + 2α) + 3δ < 0, contradicting (6.5). Then by (6.3), we have e(G2[Z]) ≤ βn2/2 ≤ 20δn2 as desired. Case 2 : β ≥ α/2. By (6.2) and (6.4), we have that

(6.6)

n2 4 ≤ e(G) ≤

![image 223](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile223.png>)

n2 4

![image 224](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile224.png>)

((1 − β)2 + 4(α − β)β) + 3δn2 ⇔ (4αβ − 2β − 3β2) + 3δ ≥ 0.

- Let g(β) := 4αβ − 2β − 3β2 + 3δ ≥ 0, then g′(β) = 4α − 2 − 6β ≤ 4α − 2 − 3α < 0. So we have α ≤ 20δ, as otherwise, using that α ≤ 2/3,






α 2

α 6

α 2

4α − 2 − 3 ·

+ 3δ ≤ −

g(β) ≤ g(α/2) =

+ 3δ < 0, contradicting (6.6). Then by (6.3), we have e(G2[Z]) ≤ αn2/2 ≤ 10δn2 as desired.

![image 225](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile225.png>)

![image 226](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile226.png>)

![image 227](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile227.png>)

By Claim 6.5, we have e(G1) ≥ n2/4 − 22δn2. Apply Theorem 2.3 to G1 with t = 22δn2 and let V (G) = V (G1) = A ∪ B be an arbitrary max-cut partition of G1. Then we have

n2

4 − 88δn2, and |A|,|B| = n/2 ± 2√t = n/2 ± 10

- (6.7) e(G[A]) + e(G[B]) ≤ 3t = 66δn2 ⇒ e(G1[A,B]) ≥ e(G1) − 66δn2 ≥


![image 228](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile228.png>)

√

![image 229](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile229.png>)

![image 230](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile230.png>)

δn. Note that there exists a vertex v ∈ B with

√

√

n2/4 − 88δn2 n/2 + 10

n 2 − 10

e(G1[A,B]) |B|

![image 231](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile231.png>)

![image 232](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile232.png>)

√

dG1(v,A) ≥

δn ≥

δn ≥ |A| − 20

≥

δn.

![image 233](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile233.png>)

![image 234](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile234.png>)

![image 235](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile235.png>)

![image 236](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile236.png>)

√ √ δn, as otherwise |NG2(u) ∩ NG1(v)| ≥ δn, contradicting Fact 6.3. Similarly, dG2(u,B) ≤ 21

![image 237](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile237.png>)

Consequently, for any u ∈ V (G), we have dG2(u,A) ≤ 21

√

√

![image 238](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile238.png>)

![image 239](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile239.png>)

![image 240](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile240.png>)

δn. Thus we have ∆(G2) ≤ 42

δn.

We claim that A ∪ B is the desired partition. Suppose dG1(w,B) < 2n/5 for some w ∈ A. Then dG1(w,A) ≥ δ(G) − ∆(G2) − dG1(w,B) ≥ n/20. As A ∪ B is a max-cut, we see that dG1(w,B) ≥ dG1(w,A) − ∆(G2) ≥ n/30. Since G1 is K3-free, there is no edge of G1 in [NG1(w,A),NG1(w,B)], implying that e(G1[A,B]) ≤ n2/4 − (n/20) · (n/30), contradicting (6.7) and that δ < 10−6.

7. Proof of Theorem 1.2

- 7.1. Upper bound. Let s ≥ 2 and ﬁx a function gs(n) satisfying (1.2). Note that a function gs′(n) satisfying gs(n) = (gs′ (n)/n)2n is also a function satisfying (1.2). We choose constants such that 0 < 1/n ≪ 1/M′ ≪ ε ≪ γ ≪ 1. In particular, 1/gs′ (n) ≪ 1/M′.


Let G be an n-vertex graph with α(G) ≤ gs(n) with a 2-edge-colouring φ. We apply Lemma 5.4 with c = (gs′(n)/n)2, to obtain a partition V1∗ ∪ V2∗ such that α(Gi[Vi∗]) ≤ gs′(n). Apply Theorem 2.5 with G,V1∗,V2∗,φ,ε,ε−1 and M′ playing the roles of G,U1,U2,φ,ε,M and M′ to obtain an ε-regular partition V1∪···∪Vm with ε−1 ≤ m ≤ M′ which reﬁnes the partition V1∗ ∪ V2∗. Let R := R(ε,γ,φ,(Vi)i∈[m]) be its reduced graph. Let the colouring φind be as deﬁned in the proof of Lemma 5.2. So if φind(i) = j for some i ∈ V (R) and j ∈ [2], it means the corresponding cluster Vi in G satisﬁes α(Gj[Vi]) ≤ gs′(n).

By Tura´n’s Theorem, it suﬃces to show the following.

- (R1) R is KR(3,s)-free if φ is (K3,K2s−1)-free;
- (R2) R is KR(3,s)+1-free if φ is (K3,K2s)-free.


Indeed, it is easy to see that (R1) implies e(G) ≤ 21 1 − R(3,s1)−1 n2 + 3γn2 and (R2) implies e(G) ≤ 21 1 − R(31,s) n2 + 3γn2 .

![image 241](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile241.png>)

![image 242](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile242.png>)

![image 243](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile243.png>)

![image 244](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile244.png>)

To show (R1) and (R2), without loss of generality, assume that [t] ⊆ V (R) induces a maximum size clique in R. As the case s = 2 is covered in Theorem 1.1, we assume that s ≥ 3.

Suppose that G is (K3,K2s−1)-free (resp. (K3,K2s)-free). Suppose that φind(i) = 2 for all i ∈ [t], then by Lemma 2.8, φind|[t] is (K3,Ks)-free, and so t ≤ R(3,s)−1 as desired. We may then assume that φind(t) = 1. Then φind(it) = 2 for all i ∈ [t − 1], as otherwise it is easy to see that one can embed K3 in G1[Vi ∪ Vt]. Consequently, by Lemma 2.8, we have that φind|[t−1] is (K3,Ks−1)-free (resp. (K3,Ks)-free). Hence, t − 1 ≤ R(3,s − 1) − 1 ≤ R(3,s) − 2 (resp. t − 1 ≤ R(3,s) − 1) as desired.

- 7.2. Lower bound. Let n be a suﬃciently large number, and let H(n) be an n-vertex K3-free graph with independence number O(√nlog n). The celebrated result of Kim [17] shows the existence of such graphs.


![image 245](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile245.png>)

X1

X5

F1

F1

I5 I1

F1

F2

I4

I2

X2

I3

F1

X6

X4 F1 X3

Figure 2: A graph with no blue (dotted) K3 and no red K6. All edges incident to i∈[5] Ii and i∈[5] Xi are omitted in the picture except blue edges between I5 and X5 ∪ X1.

- 7.2.1. Lower bound for RT(n,K3,K2s−1,gs(n)). Let t = R(3,s)−1 and φ : [2t] → [2] be a (K3,Ks)free colouring. Let G be obtained from adding a copy of H(n/t) to each partite set of Tt(n). The following colouring witnesses G being (K3,K2s−1)-free: colour all edges inside each partite set colour


- 2 and colour all crossing edges according to φ, i.e. for any ij ∈ [2t] and h ∈ [2], all edges in [Xi,Xj] are of colour h if φ(ij) = h.


- 7.2.2. Lower bound for RT(n,K3,K2s,gs(n)). Let t = R(3,s) and φ : [t−21] → [2] be a (K3,Ks)free colouring. Let G be obtained from adding a copy of H(n/t) to each partite set of Tt(n). The following colouring witnesses G being (K3,K2s)-free: colour all edges inside Xt colour 1, and edges inside Xi colour 2 for all i ∈ [t − 1]; colour all crossing edges in [X1,... ,Xt−1] according to φ and colour all [Xi,Xt]-edges colour 2 for all i ∈ [t − 1].

8. Concluding remarks

- 8.1. The value of ̺(K3,K6,δ). We conjecture that the following equality holds.


δ 2

5 12

+ 2δ2. The lower bound is given by the construction below, see Figure 2.

+

̺(K3,K6,δ) =

![image 246](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile246.png>)

![image 247](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile247.png>)

- • Let F1 := F(n6,d1) and F2 := F(n6−3δn2 ,d2) where di ∈ [δn−o(n),δn]. So e(F1) = δn122 ±o(n2) and e(F2) = δn122 − 3δ24n2 ± o(n2).

![image 248](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile248.png>)

![image 249](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile249.png>)

![image 250](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile250.png>)

![image 251](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile251.png>)

![image 252](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile252.png>)

![image 253](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile253.png>)

- • Let I = {v1,v2,... ,vd2} be an independent set of size d2 in F2. Let I = I1 ∪ I2 be an equipartition of I. Let F be an n/6-vertex graph obtained from F2 by

- – ﬁrst adding 3 clone sets of I1, say Ii with i ∈ {3,4,5};
- – adding all [Ii,Ii+2]-edges for each i ∈ [5] (addition modulo 5); and
- – adding an additional set of 32(δn − d2) isolated vertices.


![image 254](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile254.png>)

Note that F is not triangle-free, and

e(F) = e(F2) +

3d2 2 · d2 + 5

![image 255](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile255.png>)

d2 2

![image 256](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile256.png>)

2

=

δn2 12

![image 257](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile257.png>)

+ 2δ2n2 ± o(n2).

- • Finally, let G be the graph obtained from T6(n), by putting a copy of F in X6 and a copy of F1 in Xi for each i ∈ [5].


It is clear that G has the desired size and easy to check that the following 2-edge-colouring φ of G is (K3,K6)-free:

- • let φ(Xi,Xi+2) = 1 for each i ∈ [5] (addition modulo 5);
- • let φ(Ii,Xi ∪ Xi+1) = 1 for each i ∈ [5] (addition modulo 5);
- • let φ(e) = 1, for all e ∈ E(G[X6] \ G[∪i∈[5]Ii]);
- • all other edges are of colour 2.


- 8.2. The value of ̺(K3,K2s). Recall that for triangle versus odd cliques, Erd˝os, Hajnal, Simonovits, So´s and Szemere´di [10] conjectured that ̺(K3,K2s−1) is achieved by the (R(3,s) − 1)-


partite Tura´n graph, i.e. ̺(K3,K2s−1) = 12 1 − R(3,s1)−1 . Base on Theorem 1.2, we put forward the following conjecture for triangle versus even cliques.

![image 258](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile258.png>)

![image 259](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile259.png>)

Conjecture 8.1. For all s ≥ 2, ̺(K3,K2s) = 12 1 − R(31,s) .

![image 260](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile260.png>)

![image 261](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile261.png>)

- 8.3. Ramsey-Tura´n number with more than 2 colours. We remark that the multicolour Ramsey-Tura´n number for triangles is related to a version of Ramsey number studied by Liu, Pikhurko and Sharifzadeh [19]. They introduced r∗(Ka1,... ,Kak) as the largest integer N such that there exists a colouring φ : [≤N2] → [k] with the following property:


(∗) for each i ∈ [k], there is no edge-monochromatic Kai in colour i, and there is no edge incident to a vertex with the same colour, i.e. φ(ij) = φ(i) for any j = i.

Note that when an n-vertex graph G is (K3,... ,K3)-free with α(G) = o(n), then the colouring φind on its reduced graph R satisﬁes (∗), hence

- 1

![image 262](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile262.png>)

- 2


1 r∗(K3,... ,K3)

1 −

̺(K3,... ,K3) =

.

![image 263](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile263.png>)

In particular, Theorems 1.8 and 1.9 in [19] imply ̺(K3,K3,K3) = 25 and ̺(K3,K3,K3,K3) = 1532.

![image 264](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile264.png>)

![image 265](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile265.png>)

In general Ramsey-Tura´n numbers for larger cliques are not determined by r∗, for example ̺(K3,K5) = 25 = 12 1 − r∗(K13,K5) = 83 and ̺(K4,K4) = 1128 = 12 1 − r∗(K14,K4) = 31.

![image 266](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile266.png>)

![image 267](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile267.png>)

![image 268](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile268.png>)

![image 269](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile269.png>)

![image 270](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile270.png>)

![image 271](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile271.png>)

![image 272](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile272.png>)

![image 273](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile273.png>)

References

- [1] J. Balogh, P. Hu, M. Simonovits, Phase transitions in the Ramsey-Tur´an theory, J. Combin. Theory Ser. B, 114,

(2015), 148–169.

- [2] J. Balogh, H. Liu, M. Sharifzadeh, On two problems in Ramsey-Tur´an theory, SIAM J. Discrete Math., 31,

(2017), 1848–1866.

- [3] J. Balogh, A. McDowell, T. Molla, R. Mycroft, Triangle-tilings in graphs without large independent sets, Combinatorics, Probability and Computing, to appear.
- [4] J. Balogh, T. Molla, M. Sharifzadeh, Triangle factors of graphs without large independent sets and of weighted graphs, with an Appendix by Christian Reiher and Mathias Schacht, Random Structures and Algorithms, 49,

(2016), 669–693.

- [5] T. Bohman, P. Keevash, Dynamic concentration of the triangle-free process, The Seventh European Conference on Combinatorics, Graph Theory and Applications, CRM Series, 16, (2013), 489–495.
- [6] B. Bollob´s, P. Erd˝s, On a Ramsey-Tur´an type problem, J. Combin. Theory Ser. B, 21, (1976), 166–168.
- [7] S. Brandt, Triangle-free graphs whose independence number equals the degree, Discrete Math., 310, (2010), 662–669.
- [8] E. Davies, M. Jenssen, W. Perkins, B. Roberts, On the average size of independent sets in triangle-free graphs, Proc. Amer. Math. Soc., to appear.
- [9] P. Erd˝s, A. Hajnal, V. T. S´os, E. Szemere´di, More results on Ramsey-Tur´an type problems, Combinatorica, 3,

(1983), 69–81.

- [10] P. Erd˝s, A. Hajnal, M. Simonovits, V. T. S´os, E. Szemere´di, Tur´an-Ramsey theorems and simple asymptotically extremal structures, Combinatorica, 13, (1993), 31–56.
- [11] P. Erd˝s, V.T. S´os, Some remarks on Ramseys and Tur´ans theorem, Combinatorial theory and its applications, II (Proc. Colloq., Balatonfured, 1969), North-Holland, Amsterdam, (1970), 395–404.
- [12] P. Erd˝s, V. .T. S´os, On Tur´an-Ramsey type theorems II, Studia Sci. Math. Hungar., 14, (1979), 27–36.


- [13] J. Fox, P. Loh, Y. Zhao, The critical window for the classical Ramsey-Tur´an problem, Combinatorica, 35, (2015), 435–476.
- [14] J. Fox, B. Sudakov, Dependent Random Choice, Random Structures and Algorithms, 38, (2011), 1–32.
- [15] Z. Fu¨redi, A proof of the stability of extremal graphs, Simonovits’ stability from Szemere´di’s regularity, J. Combin. Theory Ser. B, 115, (2015), 66–71.
- [16] E. Gyo˝ri, B. Keszegh, On the number of edge-disjoint triangles in K4-free graphs, Combinatorica, to appear.
- [17] J. H. Kim, The Ramsey number R(3, t) has order of magnitude t2/ log t Random Structures and Algorithms, 7,

(1995), 173–207.

- [18] J. Koml´os, M. Simonovits, Szemere´di’s regularity lemma and its applications to graph theory, In Combinatorics, Paul Erd˝os is Eighty, J´anos Bolyai Math. Soc., Budapest, 2, (1996), 295–352.
- [19] H. Liu, O. Pikhurko, M. Sharifzadeh, Edges not in any monochromatic copy of a ﬁxed graph, submitted, arXiv:1705.01997.
- [20] C. Lu¨ders, C. Reiher, The Ramsey-Tur´an problem for cliques, submitted, arXiv:1709.03352.
- [21] G. Fiz Pontiveros, S. Griﬃths, R. Morris, The triangle-free process and the Ramsey number R(3, k), Mem. Amer. Math. Soc., to appear.
- [22] J. Shearer, A note on the independence number of triangle-free graphs, Discrete Math., 46, (1983), 83–87.
- [23] M. Simonovits, V.T. S´os, Ramsey-Tur´an theory, Discrete Math., 229, (2001), 293–340.
- [24] B. Sudakov, A few remarks on RamseyTur´an-type problems, J. Combin. Theory Ser. B, 88, (2003), 99–106.
- [25] E. Szemere´di, On graphs containing no complete subgraph with 4 vertices, Mat. Lapok, 23, (1972), 113–116.
- [26] P. Tur´an, Eine Extremalaufgabe aus der Graphentheorie, Mat. Fiz. Lapok, 48, (1941), 436–452.


Jaehoon Kim Younjin Kim Hong Liu School of Mathematics Institute of Mathematical Sciences Mathematics Institute University of Birmingham Ewha Womans University University of Warwick Birmingham Seoul Coventry UK South Korea UK

E-mail addresses: j.kim.3@bham.ac.uk, younjinkim@ewha.ac.kr, h.liu.9@warwick.ac.uk. Appendix A.

- A.1. When (P2) occurs in (K3,K4) stability. We bounded ̺(K3,K4,δ) from above in Section 5.2 assuming that (P1) occurs in the stability. Here we sketch a proof that if G′ satisﬁes (P2), then we have e(G′) ≤ n′2/3 + δ′n′2/2.

Recall that we have a partition X1 ∪ X2 ∪ X3 of V (G′) satisfying (A1)–(A6). Assume that (P2) occurs. It suﬃces to show that for each i ∈ [3], the graph G′[Xi] is triangle-free. Indeed, this would implies that for each i ∈ [3], we have ∆(G′[Xi]) ≤ α(G′) ≤ δ′n′, and then we have

(A.1) e(G′) ≤ e(G′[X1,X2,X3]) +

i∈[3]

e(G′[Xi]) ≤

n′2 3

![image 274](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile274.png>)

+

δ′n′2 2

![image 275](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile275.png>)

,

as desired.

By symmetry, suppose to the contrary that {u,v,w} ∈ X31 induces a copy of K3. As G′1 is K3-free, we may assume that uv is of colour 2. As α(G′1[Xi]) ≤ γ1/4n′ for each i ∈ {2,3} and G′1 is K3-free, neither u nor v can have more than γ1/5n′ neighbours in X2 or X3 in the graph G′1. Then by (A1), (A5) and (P2), for each i ∈ {2,3}, we can easily ﬁnd, a vertex xi ∈ NG′

2

(uv,Xi) such that x2x3 ∈ E(G′2). Then u,v,x2,x3 induces a K4 in G′2, a contradiction.

- A.2. Upper bound for ̺(K3,K5,δ). Let G be an n-vertex (K3,K5)-free graph with α(G) ≤ δn. We ﬁrst prove the following coloured stability using the approach for Lemma 5.2.


Lemma A.1. Suppose 0 < 1/n ≪ δ ≪ γ ≪ η ≪ 1. Let G be an n-vertex (K3,K5)-free graph with α(G) ≤ δn and δ(G) ≥ 4n/5. Then for any (K3,K5)-free φ : E(G) → [2], there exists a partition V (G) = X1 ∪ ... ∪ X5 such that for each i ∈ [5],

- (A′1) |Xi| = n/5 ± ηn;
- (A′2) α(G2[Xi]) ≤ ηn;


- (A′3) for every v ∈ Xi, we have dG1(v,Xi+2) ≥ |Xi+2| − ηn;
- (A′4) for every v ∈ Xi, we havedG2(v,Xi+1) ≥ |Xi+1| − ηn.


Sketch of proof. Let G,φ,R,R′,φind be obtained analogous to that in the proof of Lemma 5.2. Then R is close to T5(|R|) and (Z3,Z5)-free. Let BLUE and RED be colour 1 and colour 2 respectively. Let U1 ∪ ... ∪ U5 be a max-cut 5-partition of V (R). As R is close to T5(|R|), similar to (5.6) and (5.7), we get that i∈[5] e(R[Ui]) = o(m2), |Ui| = m/5 ± o(m), and δcr(R[U1,... ,U5]) ≥ (δ(R) − 3max |Ui|)/2 ≥ m/11.

We now show that each Ui should be monochromatic in φind with RED colour. Suppose this is not the case. As in Claim 5.5, let u ∈ X1 be a BLUE vertex and x2 ∈ X2 be a typical vertex such that for each i ∈ {3,4,5} we have |NR(u,Xi) ∩ NR′(x2,Xi)| ≥ m/20. As R is close to T5(|R|), we can ﬁnd three vertices x3 ∈ X3,x4 ∈ X4,x5 ∈ X5 such that {u,x2,x3,x4,x5} forms a copy of K5 in R. Moreover, all edges incident to x2 is also in R′.

If wi is BLUE for some i ∈ [5]\{1}, then any edges in the K5 incident to u or wi are all RED, as otherwise we obtain a BLUE generalised clique Z3. Let {j,k,ℓ} = [5] \ {1,i}. If all three remaining edges xjxk,xjxℓ,xkxℓ are RED, then we obtain a RED K5 (which is also a generalised clique Z5), a contradiction. If all three edges xjxk,xjxℓ,xkxℓ are BLUE, then we obtain a BLUE K3 (which is also a copy of Z3), a contradiction. Thus we may assume that xjxk is RED while xjxℓ is BLUE. Then xj is RED, as otherwise we obtain a BLUE Z3. However, in such a case (uwxjxk,xj) is a RED Z5, a contradiction.

So, we may assume that x2,x3,x4,x5 are all RED, and any edges in the K5 incident to u are all RED. If any edge incident to x2 but not u, say x2x3 is RED, then as x2x3 ∈ R′, we obtain a (ux2x3,x2x3), a RED generalised clique Z5, a contradiction. Thus x2x3,x2x4,x2x5 are all BLUE. Then all three edges x3x4,x3x5,x4x5 must be all RED, otherwise we obtain a BLUE K3 together with x2. However, then (ux3x4x5,x3) is a RED generalised clique Z5, a contradiction. Thus, all vertices of R are RED.

Since each Ui is monochromatic in RED. By the stability for 2-coloured Tura´n problem, R[U1,... ,U5]

is close to the blow-up (K3,K3)-free 2-edge-colouring of K5. This almost gives all we need, except that the corresponding partition could have low-degree vertices. Let X1′ ∪...∪X5′ be the corresponding partition of V (G), i.e. Xi′ := ∪k∈UiVk. By using argument similar to the proof of Claim 5.7, we can obtain sets X1,... ,X5, such that for each k = j ∈ [5], d(v,Xk) ≥ δ(G) − 3max |Xi| − n/20 ≥ n/10. As R is close to T5(|R|), Xi and Xi′ only diﬀer on o(n) vertices, proving (A′1). Also as each Ui is monochromatic in RED, we see that the RED graph induced on each Xi′, hence also on Xi, has o(n) independence number, proving (A′2). Both (A′3) and (A′4) follow from the fact that that the colour pattern of R[U1,... ,U5] is close to the blow-up (K3,K3)-free 2-edge-colouring of K5.

We now show how Lemma A.1 implies the desired upper bound on ̺(K3,K5,δ). Assume that e(G) > (52 + 2δ)n2. By applying Lemma 2.9 with G,1/2,δ playing the roles of G,d,ε,

![image 276](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile276.png>)

![image 277](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile277.png>)

respectively, to obtain an n′-vertex graph G′ with n′ ≥ δ1/2n/2 satisfying δ(G′) ≥ (25 + δ2′)n′2 and α(G′) ≤ α(G) = δn = δ′n′, where δ′ := δn/n′ ∈ [δ,δ1/3).

![image 278](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile278.png>)

![image 279](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile279.png>)

As G is (K3,K5)-free, G′ ⊆ G is also (K3,K5)-free and there exists an (K3,K5)-free 2 edgecolouring φ of G′. As 1/n ≪ δ and n′ ≥ δ1/2n/2 and δ′ < 10−6, we apply Lemma A.1 to obtain a partition X1 ∪ ... ∪ X5 of V (G′) satisfying (A′1)–(A′4) . We ﬁrst observe that each G′[Xi] is monochromatic in colour 2. Indeed, if there is an edge uv ∈ E(G′1[Xi]), then by (A′3), we get K3 ⊆ G1, a contradiction.

Suppose that T ∈ X3i induces a triangle in Xi. By the observation above, T is monochromatic in colour 2. By (A′1), (A′2) and (A′4), we have |NG′

(T,Xi+1)| ≥ n/6 > α(G′2[Xi+1]), implying a copy of K5 in G′2, a contradiction.

2

Hence for each i ∈ [5], the graph G′[Xi] is triangle-free, which would imply that e(G′) ≤ 2n5′2 +δn2′2 using the calculation similar to (A.1), a contradiction. Therefore, we conclude e(G) ≤ 2n52 + δn22.

![image 280](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile280.png>)

![image 281](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile281.png>)

![image 282](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile282.png>)

![image 283](<2018-kim-two-conjectures-ramsey-tur-theory_images/imageFile283.png>)

- A.3. A missing case in the weak stability in [10]. We will use the notation in [10]. In their proof, they consider a coloured weighted clique Kt(w). They assume that there is a BLUE vertex v in the weighted clique Kt(w) (BLUE=colour 1; while RED=colour 2). However, it could be that all vertices are RED. This missing case can be easily proven as follows. When all vertices are RED,


Kt(w) cannot contain an edge-monochromatic K3, implying that t ≤ 5. Also as all vertices are RED, no RED edge can have weight larger than 1/2. Together with the fact that BLUE edges induces a triangle-free graph, a simple optimisation shows that maximum is achieved when t = 3.

