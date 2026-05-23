---
type: source
kind: paper
title: Longest common subsequences between words of very unequal length
authors: Boris Bukh, Zichao Dong
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2009.05869v2
source_local: ../raw/2020-bukh-longest-common-subsequences-between.pdf
topic: general-knowledge
cites:
---

arXiv:2009.05869v2[math.PR]19Aug2021

Longest common subsequences between words of very unequal length

Boris Bukh∗ Zichao Dong∗

Abstract

We consider the expected length of the longest common subsequence between two random words of lengths n and (1 − ε)kn over a k-symbol alphabet. It is well-known that this quantity is asymptotic to γk,εn for some constant γk,ε. We show that γk,ε is of the order 1 − cε2 uniformly in k and ε. In addition, for large k, we give evidence that γk,ε approaches 1 − 41ε2, and prove a matching lower bound.

![image 1](<2020-bukh-longest-common-subsequences-between_images/imageFile1.png>)

# 1 Introduction

Background. A word over alphabet Σ is a sequence of elements of Σ, which we call symbols. A subsequence in a word w is any word obtained from w by deleting some, not necessarily contiguous, symbols. By contrast, a subword consists of consecutive symbols from w. For example, abada is a subsequence, but not a subword of abracadabra.

For a pair of words w,w′, a common subsequence is any word that is a subsequence of both w and w′. We denote by LCS(w,w′) the length of the longest common subsequence between w and w′. This quantity is a common way to measure similarity between words. The earliest mathematical studies of LCS and its variants were motivated by biological applications [14], but later it found connections to coding theory, linguistics, and text processing among other ﬁelds (book [33] provides general overview, [17, Ch. 11] discusses computational biology aspects, for recent coding-theoretic applications see [8, 12] and references therein).

A particular problem is to understand LCS(w,w′) for a pair of random words w,w′. Almost all the work on LCS for random words concerned LCS(w,w′) for a pair of random independent equally long words w,w′. Most of the focus has been on the Chv´atal–Sankoﬀ constants, which is the limit

γk def= lim

1 n

Ew,w′∼[k]n LCS(w,w′).

![image 2](<2020-bukh-longest-common-subsequences-between_images/imageFile2.png>)

Here, we write ω ∼ Ω to signify that element ω is chosen uniformly from the set Ω, with the convention that whenever this notation occurs several times in the same expression, then the respective choices are independent. So, w ∼ [k]n signiﬁes that w is a random n-symbol word over [k]. Similarly, we write w ∼ [k]∞ to denote an inﬁnite random word where each symbol is independently sampled from [k].

![image 3](<2020-bukh-longest-common-subsequences-between_images/imageFile3.png>)

∗Department of Mathematical Sciences, Carnegie Mellon University, Pittsburgh, PA 15213, USA. Supported in part by U.S. taxpayers through NSF CAREER grant DMS-1555149.

Much work has been done on estimating γk. For k = 2, Lueker [31] proved that 0.788071 ≤ γ2 ≤ 0.826280. For large k, Kiwi–Loebl–Matousˇek [24] showed that

√

![image 4](<2020-bukh-longest-common-subsequences-between_images/imageFile4.png>)

k as k → ∞. (1)

γk = (2 + o(1) /

For small k ≥ 3, the best bounds on γk can be found in [2] (upper bounds) and in [23] (lower bounds). For simulations that estimate γk, see [2, Table 2], [10, Table 1] and [7, Section 5].

Results. In this paper we consider LCS for words of drastically unequal length. Let us temporarily ﬁx k ∈ N and ε > 0 arbitrarily. It is fairly easy to see that if w ∈ [k]m is any ﬁxed word of length m, and w′ ∼ [k]∞, then the shortest preﬁx of w′ that contains w will be of length about km. So, if w ∼ [k]n and w′ ∼ [k](1−ε)kn are uniform random words of lengths n and (1 − ε)kn respectively, then LCS(w,w′) ≥ 1−ε−o(1) n with high probability. This bound turns out to be far from being sharp, and our results provide asymptotics for LCS(w,w′) in this situation.

Let

1 n

γk,ε def= lim

ELCS(w,w′), for w ∼ [k]n, w′ ∼ [k](1−ε)kn.

![image 5](<2020-bukh-longest-common-subsequences-between_images/imageFile5.png>)

n→∞

A standard argument using Fekete’s lemma and superadditivity of LCS shows that the limit above exists (see e.g. [34, Section 1.1]).

- Theorem 1. For all k ≥ 2 and all 0 < ε < 1/60, 1 − 8ε2 ≤ γk,ε ≤ 1 − ε2/72.

It is likely that, for ﬁxed k and ε → 0, the quantity γk,ε should be asymptotic to 1 − γ′

kε2 for some constant γ′

k depending on k. Similarly to the usual Chv´atal–Sankoﬀ constants, determination of constants γ′

k for speciﬁc values of k appears to be diﬃcult. However, it should be possible to prove an analogue of (1) for γ′

k. In fact, we conjecture that γ′

k → 41 as k → ∞. We are able to prove a half of this conjecture.

![image 6](<2020-bukh-longest-common-subsequences-between_images/imageFile6.png>)

- Theorem 2. There exist absolute constants c,C > 0 such that γk,ε ≥ 1 − 14ε2(1 +Ck−2/13) whenever


![image 7](<2020-bukh-longest-common-subsequences-between_images/imageFile7.png>)

k ≤ 41. To motivate the conjecture, we must explain the ideas in the proofs of Theorems 1 and 2.

k exist, then limsupk→∞ γ′

0 < ε ≤ c/k log k. In particular, if the constants γ′

![image 8](<2020-bukh-longest-common-subsequences-between_images/imageFile8.png>)

Rough proof strategy. Both our lower and our upper bounds on LCS rely on chopping random words w and w′ up into linearly many small subwords. Chopping up is not a new idea, see for example [24, 9], but we do it diﬀerently than previous works. Usually one tries to estimate LCS(u,u′) for a pair of random subwords u,u′ of suitably chosen lengths. In our argument, we chop the longer word w′ into subwords of ﬁxed length, but the partition of the shorter word is into subwords of variable lengths. Namely, for a subword u′ of w′ and a suﬃx u of w, we shall seek the longest preﬁx of u that is almost a subsequence of u′, in the sense that it can be made into a genuine subsequence by removing only a handful of symbols.

Formally, we say that a word u is d-almost contained in a word u′, and write u ≺d u′, if we may remove at most d symbols from u and obtain a subsequence of u′. In particular, u ≺0 u′ means that u is a subsequence of u′. For example, macabre ≺2 abracadabra.

We index symbols in a word from 0, denoting the symbols of a word u by u[0],u[1],... in order. For example, if u = abad, then u[0] = a, u[1] = b, u[2] = a and u[3] = d. For a word u, denote by u<m the preﬁx of u of length m. Consider a pair of random words w,w′, where w ∼ [k]∞ and w′ is a uniform random word of length at least L. Let Pd(L) be the length of the longest preﬁx of w that is d-almost contained in w′

<L, i.e.,

Pd(L) def= max{m : w<m ≺d w<L′ }.

In other words, if we imagine that w is generated symbol-by-symbol, Pd(L) is the waiting time until we obtain a word that is not d-almost contained in w′

<L. In Sections 2 and 3 we shall derive Theorem 1 from the following pair of estimates:

- Theorem 3. We have E[P1(L) − P0(L)] ≥ L/7k, if k ≥ 2 and L ≥ 20k.

![image 9](<2020-bukh-longest-common-subsequences-between_images/imageFile9.png>)

- Theorem 4. We have E[Pd(L) − P0(L)] ≤ d 2L/k + d, for all k and all d.

![image 10](<2020-bukh-longest-common-subsequences-between_images/imageFile10.png>)

It is possible to turn tighter estimates on E[Pd(L) − P0(L)] into tighter estimates on γk,ε. This is precisely how we obtain Theorem 2, by proving the following asymptotics for E[Pd(L) − P0(L)]:

- Theorem 5. We have E[Pd(L)−P0(L)] = 2 dL/k · 1+O d2 1/3 + (L/dklogL)1/2 + kd31//22 + exp(k1/L2d13//22kL−33//22) . Sadly, this asymptotics is not suﬃciently precise to obtain an upper bound on γk,ε that matches


![image 11](<2020-bukh-longest-common-subsequences-between_images/imageFile11.png>)

![image 12](<2020-bukh-longest-common-subsequences-between_images/imageFile12.png>)

![image 13](<2020-bukh-longest-common-subsequences-between_images/imageFile13.png>)

![image 14](<2020-bukh-longest-common-subsequences-between_images/imageFile14.png>)

![image 15](<2020-bukh-longest-common-subsequences-between_images/imageFile15.png>)

the lower bound in Theorem 2. The obstacle is the kd31//22 term; our upper bound arguments require an estimate for E[Pd(L) − P0(L)] be at most linear in d. (On the other hand, the last term involving d3/2 is unproblematic, as it disappears in the limit L → ∞.)

![image 16](<2020-bukh-longest-common-subsequences-between_images/imageFile16.png>)

Connection to the longest non-decreasing subsequences. The advantage of focusing on P0,... ,Pd is that the growth of Pd is controlled by the length of the longest non-decreasing subsequence (LNDS) in a suitably constructed word over (d + 1)-symbol alphabet, for 1 ≪ d ≪ k.

To explain the connection between the LCS and the LNDS, we must examine how P0(L),... ,Pd(L) change as we increase L. Recall that w[i] is the symbol of a word w at position i, with indexing starting from 0. At the start, we have Pi(0) = i, for each i. We then update P’s using the following observation.

- Proposition 6 (Proof is in Appendix A). We may compute the values of P0(L + 1),... ,Pd(L + 1) from P0(L),... ,Pd(L) by doing the following, in order:


- (A) Examine w′[L]. Set A[L] = {i : w[Pi(L)] = w′[L]}.
- (B) For each i = 0,1,... ,d in order, do


- • If i ∈ A[L], then Pi(L + 1) = Pi(L) + 1.
- • If i ∈/ A[L], then Pi(L + 1) = max(Pi(L),Pi−1(L + 1) + 1). (With the convention that P−1(L) = −∞.)


We may describe this process alternatively by imagining that P0,... ,Pd indicate positions of d+1 particles. When we expose the value of w′[L], we check which particles sit atop matching symbols; we denote those by A[L]. We then advance particles in A[L] one step to the right. If two particles collide, the particle on the left ‘bumps’ the particle on the right, causing it to advance one step further to the right.

Below is an example of the ﬁrst three exposure steps for words w = 1323121. .. and w′ = 231. .. . In this example, we write the elements of sets A[0],... ,A[L] in descending order.

P0P1P2P3

P0P1 P2P3

P0 P1 P2P3

P0P1 P2P3

w 1 3 2 3 1 2 1 . . .

A[0]=2 w 1 3 2 3 1 2 1 . . .

A[1]=21 w 1 3 2 3 1 2 1 . . .

A[2]=20 w 1 3 2 3 1 2 1 . . .

w′ ? ? ? ? ? ? ? . . .

w′ 2 ? ? ? ? ? ? . . .

w′ 2 3 ? ? ? ? ? . . .

w′ 2 3 1 ? ? ? ? . . .

L=0

L=3 Figure 1: Evolution of P0,P1,P2,P3 (example).

L=1

L=2

The values of P0(L),... ,Pd(L) depend only on sets A[0],... ,A[L − 1]. We can describe this dependence in terms of non-decreasing subsequences. A word w is non-decreasing if w[i] ≤ w[i + 1] holds for all i. For example, the word 001224 is non-decreasing. For a word w, let LNDS(w) denote the length of the longest non-decreasing subsequence of w. Slightly more generally, let LNDSi(w) = LNDS(w|i), where w|i is the word obtained by deleting symbols greater than i from w. In particular, if w ∈ {0,1,... ,d}L, then LNDSd(w) = LNDS(w).

For a set A ⊆ {0,1,... ,d}, consider the word obtained by writing the elements of A in decreasing order. We denote this word by the same letter A.

- Proposition 7 (Proof is in Appendix A). Let A[0],A[1],... ,A[L − 1] be sets as in Proposition 6. Then the word A[0]A[1]··· A[L − 1] satisﬁes LNDSi(A[0]A[1]··· A[L − 1]) = Pi(L) − i, for every i.


For example in the Figure 1, we have P3(3) = 6 and LNDS(22120) = 3. We also have P1(3) = 2 and LNDS1(22120) = 1 in the same example.

Expectant partitions. Consider the update rule in Proposition 6. Let A[L] consist of all nonempty sets of the form {i : w[Pi(L)] = s} for s ∈ [k]. Note that A[L] is a partition of {0,1,... ,d}. If the word w′ is random, then the set A[L] at Step (A) in Proposition 6 is chosen uniformly from A[L], conditioned on A[L] being non-empty. For that reason, we call A[L] expectant partition at step L. For example, in Figure 1 the expectant partitions are A[0] = {0},{1,3},{2} , A[1] = {0,3},{1,2} , A[2] = {0,2},{1,3} , and A[3] = {0},{1,2},{3} . At the next step, the set A[3] will be chosen to be one of {0}, {1,2}, {3}, each with probability 13.

![image 17](<2020-bukh-longest-common-subsequences-between_images/imageFile17.png>)

We call the partition all of whose sets are singletons trivial partition. Had all expectant partitions been trivial, then A[0]A[1]··· A[L − 1] would have been a uniform random word. The behavior of LNDS on uniform random words is well understood, thanks to the work of Tracy and Widom [35] (see also [21, 26]).

In our proof of Theorem 2, we will ﬁrst show that most expectant partitions are trivial. Then we will show that the remaining handful of non-trivial partitions do not change Pd(L) much.

Adversarial game arguments. Our main technical innovation concerns analysis of Markov chains. The Markov chains that arise in our analysis of Pd(L) have complicated state spaces and complicated transition rules. Instead of trying to describe their behavior directly, we choose to ignore certain details of the chain, and do the worst-case analysis instead.

More formally, we imagine that certain transitions are no longer random, but instead are chosen by a suitably restricted adversary. Every adversary’s strategy leads to a diﬀerent Markov chain, with one of the choices being our original chain. Furthermore, we can reduce the state space of the chain, by ignoring those parts that are under adversary’s control. When this is done carefully, we are able to ensure that the adversary’s optimal strategy leads to a much smaller Markov chain that is easier-to-analyze than the original chain.

We shall formalize these ideas in Theorem 11.

Paper organization. We begin by showing how to turn the estimates on E[Pd − P0] into bounds on γk,ε: In Section 2 we derive the lower bounds in Theorems 1 and 2 from the lower bounds on E[Pd − P0] in Theorems 3 and 5. Similarly, in Section 3 we derive the upper bound in Theorem 1 from the upper bound on E[Pd − P0] in Theorem 4.

The main bulk of paper is then devoted to proving bounds on E[Pd − P0]. Since these bounds all use the adversarial game argument, we start by formalizing the argument in Section 4. We then present the proofs of Theorems 3 and 4, starting with the easier Theorem 4 in Section 5, and following it up with the proof of Theorem 3 in Section 6.

The asymptotic result in Theorem 5 is broken into several parts. In Section 7 we show that most expectant partitions are trivial. We then estimate the eﬀect of non-trivial partitions in Section 8.

Acknowledgments. We are grateful to Greg Kuperberg and Kurt Johansson for answering our queries about longest non-decreasing subsequences. We also beneﬁted from discussions with Chris Cox and Zilin Jiang. We are very thankful to the referee for extensive comments on the manuscript.

# 2 Proof of the lower bounds in Theorems 1 and 2 In this section, we will show the following:

![image 18](<2020-bukh-longest-common-subsequences-between_images/imageFile18.png>)

Lemma 8. Suppose d,k ∈ N and α > 0 are such that E[Pd(L) − P0(L)] ≥ α L/k holds for all L ≥ L0. Then γk,ε ≥ 1 − dε2(1 + 4ε)/α2 for all 0 < ε < min(1/20,α k/2L0).

![image 19](<2020-bukh-longest-common-subsequences-between_images/imageFile19.png>)

Upon applying the lemma with d = 1, α = 1/√7 and L0 = 200k, the lower bound in Theorem 1 instantly follows from Theorem 3. Similarly, to derive Theorem 2 from Theorem 5 we apply the lemma with d = k3/13 and L0 = 36k3 log2 k.

![image 20](<2020-bukh-longest-common-subsequences-between_images/imageFile20.png>)

With hindsight let

L def= (1 − 2ε)2α2kε−2, M def= (1 − ε)kn/L.

We employ the customary abuse of notation: we write our proofs as if the numbers L and M are integers. This can be made formal by rounding L to an integer, and truncating the word of length (1 − ε)kn slightly so that its length is an integral multiple of L. Doing so does not aﬀect the limit

γk,ε, which is the subject of the present lemma. We will use similar abuses of notation later in the paper without any further comment.

Let w ∼ [k]n and w′ ∼ [k](1−ε)kn be random words as in the deﬁnition of γk,ε. Imagine that the word w is a preﬁx of an inﬁnite random word w ∼ [k]∞. Write w′ as a concatenation of M words of length L each, say w′ = w′

![image 21](<2020-bukh-longest-common-subsequences-between_images/imageFile21.png>)

1w′

2 ··· w′

M. We iteratively deﬁne words w1,... ,wM in such a way that w1 ··· wM is a preﬁx of w: Given w1 through wr, write w = w1 ··· wrv for some suﬃx v. We then deﬁne wr+1 to be the longest preﬁx of v that is d-almost contained in wr′+1.

![image 22](<2020-bukh-longest-common-subsequences-between_images/imageFile22.png>)

![image 23](<2020-bukh-longest-common-subsequences-between_images/imageFile23.png>)

![image 24](<2020-bukh-longest-common-subsequences-between_images/imageFile24.png>)

![image 25](<2020-bukh-longest-common-subsequences-between_images/imageFile25.png>)

![image 26](<2020-bukh-longest-common-subsequences-between_images/imageFile26.png>)

![image 27](<2020-bukh-longest-common-subsequences-between_images/imageFile27.png>)

![image 28](<2020-bukh-longest-common-subsequences-between_images/imageFile28.png>)

![image 29](<2020-bukh-longest-common-subsequences-between_images/imageFile29.png>)

![image 30](<2020-bukh-longest-common-subsequences-between_images/imageFile30.png>)

![image 31](<2020-bukh-longest-common-subsequences-between_images/imageFile31.png>)

![image 32](<2020-bukh-longest-common-subsequences-between_images/imageFile32.png>)

Let Yi def= len wi. The random variables Y1,... ,YM are independent. Indeed, we may imagine

![image 33](<2020-bukh-longest-common-subsequences-between_images/imageFile33.png>)

ﬁrst generating w1′ and w1, then generating w2′ and w2, and so forth. In this process, to generate the pair (w′

![image 34](<2020-bukh-longest-common-subsequences-between_images/imageFile34.png>)

![image 35](<2020-bukh-longest-common-subsequences-between_images/imageFile35.png>)

ℓ,wℓ), we ﬁrst generate w′

ℓ, and then we append symbols to wℓ as long as wℓ ≺d w′

ℓ. Hence, after the pair (w′

![image 36](<2020-bukh-longest-common-subsequences-between_images/imageFile36.png>)

![image 37](<2020-bukh-longest-common-subsequences-between_images/imageFile37.png>)

![image 38](<2020-bukh-longest-common-subsequences-between_images/imageFile38.png>)

ℓ,wℓ) has been generated, the symbol following wℓ has also been generated. This symbol will become the ﬁrst symbol of wℓ+1, and so the word wℓ+1 will not be independent from the words w1,... ,wℓ. However, since the ﬁrst symbol of w′

![image 39](<2020-bukh-longest-common-subsequences-between_images/imageFile39.png>)

![image 40](<2020-bukh-longest-common-subsequences-between_images/imageFile40.png>)

![image 41](<2020-bukh-longest-common-subsequences-between_images/imageFile41.png>)

![image 42](<2020-bukh-longest-common-subsequences-between_images/imageFile42.png>)

ℓ+1 is independent from ℓ,w1,... ,wℓ,wℓ+1[0], the event w′

![image 43](<2020-bukh-longest-common-subsequences-between_images/imageFile43.png>)

![image 44](<2020-bukh-longest-common-subsequences-between_images/imageFile44.png>)

- w1′ ,... ,w′


ℓ+1[0] = wℓ+1[0] still has probability 1/k, and so the length of wℓ+1 is independent from the lengths of the preceding words.

![image 45](<2020-bukh-longest-common-subsequences-between_images/imageFile45.png>)

![image 46](<2020-bukh-longest-common-subsequences-between_images/imageFile46.png>)

![image 47](<2020-bukh-longest-common-subsequences-between_images/imageFile47.png>)

![image 48](<2020-bukh-longest-common-subsequences-between_images/imageFile48.png>)

![image 49](<2020-bukh-longest-common-subsequences-between_images/imageFile49.png>)

Let Y def= Y1 + Y2 + ··· + YM. If Y ≥ n, then the word w is a preﬁx of w1 ··· wM, implying that LCS(w,w′) ≥ n − dM.

![image 50](<2020-bukh-longest-common-subsequences-between_images/imageFile50.png>)

![image 51](<2020-bukh-longest-common-subsequences-between_images/imageFile51.png>)

Since the lengths of w1,... ,wM are independent, Y = Y1 + ··· + YM is a sum of independent random variables. Because each Yi is sampled from Pd(L), and E[P0(L)] = L/k, it follows that

![image 52](<2020-bukh-longest-common-subsequences-between_images/imageFile52.png>)

![image 53](<2020-bukh-longest-common-subsequences-between_images/imageFile53.png>)

(1 − ε)2 1 − 2ε

n ≥ (1 + ε2)n.

![image 54](<2020-bukh-longest-common-subsequences-between_images/imageFile54.png>)

E[Y ] ≥ M(L/k + α L/k) =

![image 55](<2020-bukh-longest-common-subsequences-between_images/imageFile55.png>)

Since d ≤ Yi ≤ L + d for each i, the Chernoﬀ bound [1, Theorem A.1.18] implies that

Pr[Y ≤ n] ≤ Pr[Y ≤ EY − ε2n] ≤ exp −2(ε2n)2/ML2 ≤ exp −2ε4n/kL = o(1). Hence,

ε2 α2 − o(1) n.

1 − ε (1 − 2ε)2 ·

ELCS(w,w′) ≥ Pr[Y ≥ n](n − dM) ≥ 1 − d

![image 56](<2020-bukh-longest-common-subsequences-between_images/imageFile56.png>)

![image 57](<2020-bukh-longest-common-subsequences-between_images/imageFile57.png>)

As (1−1−2εε)2 ≤ 1 + 4ε for ε ≤ 1/20, the proof is complete.

![image 58](<2020-bukh-longest-common-subsequences-between_images/imageFile58.png>)

# 3 Proof of the upper bound in Theorem 1 assuming Theorem 4

In the introduction, we deﬁned a subsequence of w as any word obtained from w by removing some of the symbols. Sometimes the same word can be so obtained from w in several ways. To eliminate this ambiguity, we introduce a couple of deﬁnitions.

Recall that w[i] denotes the symbol of a word w at position i, with indexing starting from 0. For a word w and a set of integers I, we deﬁne w[I] def= (w[i] : i ∈ I). For example, if w = abracadabra and

- I = {1,2,4}, then w[I] = brc. A distinguished subsequence of a word w ∈ [k]n is a pair (u,I) such that u = w[I]; note that u is the usual (undistinguished) subsequence of w. Similarly, a distinguished common subsequence of words w and w′ is a triple (u,I,I′) such that u = w[I] = w′[I′]. When there is no chance of confusion, we shall use u to refer to the distinguished (common) subsequence, omitting I and I′ from the notation.


For each pair of words w ∈ [k]n and w′ ∈ [k](1−ε)kn, we shall select a suitable distinguished longest common subsequence, and assign a vector d that describes the “shape” of that common subsequence. We will then show that, for any ﬁxed d, a pair of random words is very unlikely to have a long common subsequence of that shape. The union bound will then complete the argument.

Standard preﬁx. Deﬁne three constants

L def= 432kε−2, M def= (1 − ε)kn/L, D def= 12εn k/3L. For the future use, observe that the choice of L implies that 2L/k + 1 ≤ 3L/k.

![image 59](<2020-bukh-longest-common-subsequences-between_images/imageFile59.png>)

![image 60](<2020-bukh-longest-common-subsequences-between_images/imageFile60.png>)

![image 61](<2020-bukh-longest-common-subsequences-between_images/imageFile61.png>)

![image 62](<2020-bukh-longest-common-subsequences-between_images/imageFile62.png>)

As in the preceding section, whenever we have a word w′ ∈ [k](1−ε)kn of length (1−ε)kn, we write it as a concatenation of M words of length L each, w′ = w1′ ··· w′

M. We use this notation throughout the section.

Suppose d = (d1,... ,dM) is a vector of non-negative integers. Given w ∈ [k]n and w′ ∈ [k](1−ε)kn, we say that w is d-almost contained in w′ and write w ≺d w′ if there is a decomposition of w as w = w1 ··· wM for some words w1,... ,wM such that the word wi is a di-almost contained in w′

i.

Observation 9. If LCS(w,w′) ≥ n − D, then there is a vector d = (d1,... ,dM) ∈ ZM+ satisfying d1 + ··· + dM ≤ D such that w ≺d w′.

Proof. Let u be a distinguished common subsequence between w and w′ of length n − D. Deﬁne w1,... ,wM inductively. Assume that w1,... ,wi−1 have been deﬁned, and w = w1 ··· wi−1v for some word v. Let wi be the longest preﬁx of v that contains no symbol that u matches to w′

i+1. Let di be the number of unmatched symbols in wi. It is then clear that len u + di = n.

![image 63](<2020-bukh-longest-common-subsequences-between_images/imageFile63.png>)

![image 64](<2020-bukh-longest-common-subsequences-between_images/imageFile64.png>)

![image 65](<2020-bukh-longest-common-subsequences-between_images/imageFile65.png>)

![image 66](<2020-bukh-longest-common-subsequences-between_images/imageFile66.png>)

Let a vector d = (d1,... ,dM) and words w ∈ [k]n and w′ ∈ [k](1−ε)kn be given. Deﬁne a sequence of words w1,... ,wM inductively as follows: Assume that w1 through wi−1 have been deﬁned, and write w = w1 ··· wi−1v. Let wi be the longest preﬁx of v that is di-almost contained in w′

i. It might happen that, for some j, the word v is dj-almost contained in w′

j. In that case, wj = v and so all the subsequent words wj+1,wj+2,... ,wM are empty. We call w1 ··· wM the standard preﬁx of w (with respect to w′ and d).

Lemma 10. If w ≺d w′, then the standard preﬁx of w with respect to w′ and d is equal to w. Proof. Let w = wˆ1 ··· wˆM be a decomposition of w satisfying wˆi ≺di w′

i, which exists because w ≺d w′. Let w1 ··· wM be the standard preﬁx of w. By induction on i it follows that wˆ1 ··· wˆi is a preﬁx of w1 ··· wi. In particular, w = wˆ1 ··· wˆM is a preﬁx of w1 ··· wM. So, w = w1 ··· wM follows.

![image 67](<2020-bukh-longest-common-subsequences-between_images/imageFile67.png>)

![image 68](<2020-bukh-longest-common-subsequences-between_images/imageFile68.png>)

![image 69](<2020-bukh-longest-common-subsequences-between_images/imageFile69.png>)

![image 70](<2020-bukh-longest-common-subsequences-between_images/imageFile70.png>)

Any ﬁxed d-vector is unlikely. Let d = (d1,... ,dM) be an arbitrary vector of nonnegative integers satisfying d1 + ··· + dM ≤ D. We shall estimate the probability that w ≺d w′ for random w ∼ [k]n and w′ ∼ [k](1−ε)kn.

We imagine generating symbols of w and w′ gradually in M +1 rounds, numbered 0,1,... ,M. In round 0 we generate only the ﬁrst symbol of w. Before the start of round i we already generated

- • subwords w1′ ,... ,w′


i−1 of w′, and

- • the ﬁrst i − 1 words w1,... ,wi−1 in the standard preﬁx of w, and
- • a single symbol that follows wi−1 in w.


In round i, we ﬁrst generate L symbols that make up w′

i. We then generate symbols of wi (starting with a single already-generated symbol) as long as wi ≺di w′

i. Once wi ≺di w′

i ceases to hold, we backtrack one symbol. That symbol will become the ﬁrst symbol of wi+1 in the next round. (This backtracking is similar to the backtracking in Section 2 in the deﬁnition of Yi.)

We also need a pair of ﬁx-up rules: once we generated n symbols of w, we stop generating symbols of w, and generate all the remaining symbols of w′ in one shot. Similarly, if after the end of the M’th round, the word w still has fewer than n symbols, we generate the remaining symbols of w.

It is clear that this algorithm generates a pair of independent uniformly distributed words w ∼ [k]n and w′ ∼ [k](1−ε)kn. To simplify the analysis, it is convenient to consider the version of this algorithm without the ﬁx-up rules. We call this modiﬁed algorithm tidy, and denote the distribution on pairs of words (w,w′) that it induces by T(d).

Let U denote the uniform distribution on [k]n × [k](1−ε)kn. Since, by Lemma 10, w ≺d w′ implies that len w1 + ··· + len wM = len w, it follows that

[w ≺d w′] = Pr

[len w ≥ n] = Pr

[len w1 + ··· + len wM ≥ n]. (2)

Pr

(w,w′)∼U

(w,w′)∼T(d)

(w,w′)∼T(d)

Because the ﬁrst symbol of wi depends on the ﬁrst i − 1 rounds, the word wi is not independent of w1 through wi−1 and w′

1 through w′

i−1. However, the distribution of len wi is the same for every ﬁxed initial symbol. So, the lengths len w1,... ,len wM are independent.

We shall use Talagrand’s inequality to bound the probability on the right side of (2). Recall that, in the context of Talagrand’s inequality, a random variable W on a product space Ω is called f-certiﬁable if, whenever, W(x) ≥ b, there exists a set of at most f(b) coordinates such that every y ∈ Ω agreeing with x on these coordinates satisﬁes W(y) ≥ b.

Sample w′ ∼ [k](1−ε)kn and M independent inﬁnite words w(1),... ,w(M) ∼ [k]∞. Let wˆi be the longest preﬁx of w(i) satisfying wˆi ≺di w′

i. The vectors (len w1,··· ,len wM) and (len wˆ1,··· ,len wˆM) are identically distributed. Deﬁne a random variable Y def= len wˆ1 + ··· + len wˆM. Since len wˆi is sampled from the distribution Pdi(L), from Theorem 4 it follows that

E[Y ] ≥ ME[P0(L)] = ML/k = (1 − ε)n, (3)

M

![image 71](<2020-bukh-longest-common-subsequences-between_images/imageFile71.png>)

![image 72](<2020-bukh-longest-common-subsequences-between_images/imageFile72.png>)

L/k + di 2L/k + di ≤ ML/k + D( 2L/k + 1)

E[Y ] ≤

i=1

![image 73](<2020-bukh-longest-common-subsequences-between_images/imageFile73.png>)

≤ ML/k + D 3L/k = (1 − ε/2)n. (4)

The random variable Y = len wˆ1 + ··· + len wˆM is 2b-certiﬁable. Indeed, let Ω be the space of all (M + 1)-tuples (w(1),... ,w(M),w′) ∈ ([k]∞)M × [k](1−ε)kn endowed with the uniform measure. We may think of Ω as a product of inﬁnitely many uniform random variables sampled from [k] (one for each symbol of w(1),... ,w(M),w′). If Y (w(1),... ,w(M),w′) ≥ b, then there are b symbols in w′ and a total of b symbols in words w(1),... ,w(M),w′ that make up wˆ1 through wˆM. These 2b symbols certify

that Y ≥ b. Hence, Talagrand’s inequality (see [1, Theorem 7.7.1]) tells us that Pr Y ≤ b − t

√

2b Pr[Y ≥ b] ≤ exp(−t2/4). (5)

![image 74](<2020-bukh-longest-common-subsequences-between_images/imageFile74.png>)

Let m be the median of Y . We apply (5) with b = m and with b = m + t2 + 2t√2m. The ﬁrst choice gives us

![image 75](<2020-bukh-longest-common-subsequences-between_images/imageFile75.png>)

√

2m] ≤ 2exp(−t2/4). (6)

![image 76](<2020-bukh-longest-common-subsequences-between_images/imageFile76.png>)

Pr[Y ≤ m − t

Because of m + t2 + t√2m − t 2(m + t2 + t√2m) ≥ m, the second choice gives us

![image 77](<2020-bukh-longest-common-subsequences-between_images/imageFile77.png>)

![image 78](<2020-bukh-longest-common-subsequences-between_images/imageFile78.png>)

![image 79](<2020-bukh-longest-common-subsequences-between_images/imageFile79.png>)

√

2m] ≤ 2exp(−t2/4). (7) From (6) we deduce that

Pr[Y ≥ m + t2 + t

![image 80](<2020-bukh-longest-common-subsequences-between_images/imageFile80.png>)

√

![image 81](<2020-bukh-longest-common-subsequences-between_images/imageFile81.png>)

E[Y ] ≥ m −

2m

∞

√

Pr[Y ≤ m − t

t=0

√

![image 82](<2020-bukh-longest-common-subsequences-between_images/imageFile82.png>)

![image 83](<2020-bukh-longest-common-subsequences-between_images/imageFile83.png>)

2m] ≥ m − 2

2m

∞

√

exp(−t2/4) ≥ m − 5

t=0

![image 84](<2020-bukh-longest-common-subsequences-between_images/imageFile84.png>)

2m.

Note that this implies that m ≤ 2n, for otherwise E[Y ] > n contradicting (4). So, (7) implies Pr[Y ≥ E[Y ] + t2 + 2(t + 5)√n] ≤ Pr[Y ≥ E[Y ] + t2 + (t + 5)

√

![image 85](<2020-bukh-longest-common-subsequences-between_images/imageFile85.png>)

![image 86](<2020-bukh-longest-common-subsequences-between_images/imageFile86.png>)

2m] ≤ Pr[Y ≥ m + t2 + t

√

![image 87](<2020-bukh-longest-common-subsequences-between_images/imageFile87.png>)

(8)

2m] ≤ 2exp(−t2/4).

We choose t = 6ε√n. With this choice, t2 + 2(t + 5)√n < 3t√n ≤ εn/2, and so from the combination of (2), (4), and (8) we obtain

![image 88](<2020-bukh-longest-common-subsequences-between_images/imageFile88.png>)

![image 89](<2020-bukh-longest-common-subsequences-between_images/imageFile89.png>)

![image 90](<2020-bukh-longest-common-subsequences-between_images/imageFile90.png>)

![image 91](<2020-bukh-longest-common-subsequences-between_images/imageFile91.png>)

[w ≺d w′] ≤ 2exp(−ε2n/144). (9)

Pr

(w,w′)∼U

Putting everything together. The number of nonnegative integer vectors (d1,... ,dM) satisfying d1 + ··· + dM ≤ D is DM+M . Plugging in our choice of constants D and M, and using the bound

m cm ≤ 2H(c)m, we obtain

ε2n(1/72 + 1/432)

D + M M

ε2n/432 ≤ exp(ε2n/150). Observation 9 and inequality (9) then tell us that

=

D + M

M · 2exp(−ε2n/144) = o(1/n). As this implies that ELCS(w,w′) ≤ n − D − 1, the proof is complete.

Pr[LCS(w,w′) ≥ n − D] ≤

# 4 Adversarial game argument

Suppose X0,X1,X2,... is a Markov chain with a complicated transition rule, and that our goal is to estimate Ef(Xn). One approach is to replace some of the randomness in the chain by adversarial choices. We can then bound Ef(Xn) from below by inf Ef(Xn), where the inﬁmum is over all possible strategies for the adversary.

Furthermore, we may do so in stages: we ﬁrst replace some of the randomness by adversarial choices, determine what optimal (or near-optimal) choices are, use that to simplify the chain, and then replace some of the remaining randomness by adversarial choices again.

The aim of this section is to make these ideas precise. The reader might want to ﬁrst glance at the applications in the later sections, and only then continue reading the formalism that underlies them.

Markov games. To make these ideas precise, we need to deﬁne the notion of an ‘adversarial strategy’. Formally, we deﬁne a Markov game as a tuple (I,Ω,P,R), where

- • The set I ⊆ {0,1,... } indexes the times in which the transitions are chosen by the adversary,
- • Ω0,Ω1,Ω2,... is a sequence of at most countable sets, with |Ω0| = 1, where Ωn represents the possible states at the n’th step,
- • R is a tuple of functions R = (Rn)n∈I with Rn: Ωn → 2Ωn+1 \ {∅}, where Rn(xn) ⊆ Ωn+1 represents the set of states to which the adversary can move from the state xn ∈ Ωn,
- • P is a tuple of functions P = (Pn)n/∈I with Pn: Ωn+1 × Ωn → [0,1] that satisﬁes


xn+1∈Ωn+1 Pn(xn+1,xn) = 1 for each xn ∈ Ωn. The value of Pn(xn+1,xn) represents the transition probability to the state xn+1 ∈ Ωn+1 from the state xn ∈ Ωn.

In this language, Markov chain1 is the same as a Markov game with I = ∅. The only element in Ω0 is the initial state of the Markov chain. Since the tuple R is trivial if I = ∅, we abbreviate (∅,Ω,P,R) to (Ω,P) in a case of a Markov chain.

Note that a Markov game is not a probability space, and is not naturally associated with a probability space (unless I = ∅). Instead it models a one-player game in which some of the turns are made by the player (which we call Adversary), and some turns are made at random. When discussing the applications of actual Markov games in the following sections, for ease of reading we shall usually personify the randomness as Fortune. In this section, however, our task is to lay the formal basis for the adversarial game argument, and so we use the formal deﬁnition directly.

The next deﬁnition captures the notion of ‘giving the adversary more choices’. Suppose that G = (I,Ω,P,R) and G′ = (I′,Ω′,P′,R′) are a pair of Markov games. We say that a sequence π = (π0,π1,... ) is a morphism from G to G′ if

(M1) I ⊆ I′,

![image 92](<2020-bukh-longest-common-subsequences-between_images/imageFile92.png>)

1In this paper, Markov chains are not assumed to be time-homogeneous, i.e., we allow the state spaces and the transition probabilities to depend on the time step n.

(M2) πn is a function from Ωn to Ω′n, for each n, (M3) for each n ∈ I, and xn ∈ Ωn, we have πn+1(Rn(xn)) ⊆ Rn′ (πn(xn)), (M4) for each n ∈ I′ \ I, whenever xn ∈ Ωn and xn+1 ∈ Ωn+1 satisfy Pn(xn+1,xn) > 0, the set

Rn′ (πn(xn)) contains πn+1(xn+1), (M5) for each n ∈/ I′, every xn ∈ Ωn and x′n+1 ∈ Ω′n+1 satisfy Pn′ x′n+1,πn(xn) =

Pn(x,xn).

x:πn+1(x)=x′n+1

If Ωn = Ω′n and each πn is the identity function, then this deﬁnition perfectly mirrors the intuitive idea of giving more choices to the adversary. In general, if πn is not injective, say πn(xn) = πn(˜xn), then the morphism π collapses the states xn and x˜n into a single state. The conditions (M4) and (M5) require that, in the Markov game G′, the new state is indistinguishable from its preimages in G.

Strategies. Intuitively, a deterministic strategy for the adversary consists of choosing, for every time step n ∈ I and every state xn ∈ Ωn, a state in Rn(xn) that xn is mapped to. A probabilistic strategy is then identiﬁed with a collection of probability distributions on all Rn(xn), which is quite an unwieldy object to work with.

We adopt a simpler point of view. Any choice of a (possibly probabilistic) strategy turns a Markov game into a Markov chain. In our approach, we identify the strategy with this Markov chain. Formally, we say that a Markov chain S = (Ω,P) is a strategy for G′ = (I′,Ω′,P′,R′) if there is a morphism π: S → G′ such that

- • Ωn = Ω′n, and
- • there is a morphism from S to G′ in which each πn: Ωn → Ω′n is the identity map.


Let Strat0(G′) denote the set of all strategies for G′.

Say that a Markov chain S = (Ω,P) is determined at n if Pn(xn+1,xn) ∈ {0,1} for all xn ∈ Ωn. We say that a strategy for a Markov game G = (I,Ω,P,R) is deterministic if it is determined for every n ∈ I. Let Strat(G′) denote the set of all deterministic strategies for G′.

Statement of the adversarial game argument. A function on a Markov game is any function on n≥0 Ωn. Given a morphism π: G → G′, we may pull back a function f on G′, to a function on G whose value at (x0,x1,... ) ∈ n≥0 Ωn is f(π0(x0),π1(x1),... ). For ease of notation, we shall denote the pull back of f on G by the same letter f.

Though a general Markov game is not a probability space, we may naturally regard a Markov chain as a probability space. So, for a Markov chain M, we write PrM and EM for the probability and expectation on the probability space associated to M. In particular if M = (Ω,P) is a Markov chain, Pn is the transition matrix for the n’th transition step with respect to the probability PrM.

With these deﬁnitions at our disposal, we can formally state the idea at the start of this section.

Theorem 11 (Adversarial game argument). Let M → G be a morphism from a Markov chain M to a Markov game G. Suppose f is any function on G. Then

EM[f] ≥ inf

ES[f].

S∈Strat(G)

The theorem has several uses beside bounding expectations from below:

- • We can get an upper bound on EMf by applying the theorem to −f.
- • We may bound probabilities of suitable events in M by applying the theorem to their characteristic functions.
- • By applying the theorem to the random variable (f − EMf)2, and then using the inequality ES[(f − c)2] ≥ ES[(f − ES[f])2] we also obtain

VarM[f] ≥ inf

S∈Strat(G)

VarS[f].

- • Similarly, by applying the theorem to the function −exp(tf) we may bound the momentgenerating function of f. This gives a way to prove strong tail bounds on f.


Penalties. In applications of the adversarial game argument, we will sometimes have constraints on adversary’s action that are cumbersome to enforce using sets Rn. In this situation, it will be convenient to impose a penalty instead. Formally, a penalty is a function on a Markov game that is equal to some large constant when some condition is violated, and is equal to 0 otherwise. When f is a function that the adversary tries to minimize and Pnlt is a penalty, we instead consider a new function f + Pnlt. Similarly, if the adversary tries to maximize f, then the new function is f − Pnlt.

We shall always denote the penalty by Pnlt.

Compositions of morphisms. The morphisms can be composed, i.e., whenever π: G → G′ and π′: G′ → G′′ are morphisms from G to G′ and from G′ to G′′ respectively, their composition π′ ◦ π is a morphism from G to G′′. We omit the routine proof.

Observation 12. If G → G′ is a morphism of Markov games and f is a function on G′, then infS∈Strat(G) ES[f] ≥ infS′∈Strat(G′) ES′[f].

Hence, for the purposes of the adversarial game argument, we may replace any game by its homomorphic image. Proof of Observation 12. Let S ∈ Strat(G) be arbitrary. Composition of morphisms S → G and

- G → G′ yields a morphism S → G′. By the adversarial game argument ES[f] ≥ infS′∈Strat(G′) ES′[f]. As S is arbitrary, we are done.


![image 93](<2020-bukh-longest-common-subsequences-between_images/imageFile93.png>)

![image 94](<2020-bukh-longest-common-subsequences-between_images/imageFile94.png>)

![image 95](<2020-bukh-longest-common-subsequences-between_images/imageFile95.png>)

![image 96](<2020-bukh-longest-common-subsequences-between_images/imageFile96.png>)

Proof of the adversarial game argument. We shall break the proof of Theorem 11 into two steps. We begin by showing a weaker version of the lemma allowing randomness in adversary’s strategy. Then we use derandomization to obtain the full strength of the lemma.

- Lemma 13 (Adversarial game argument, basic version). Let M → G be a morphism from a Markov chain M to a Markov game G. Suppose f is any function on G. Then


EM[f] ≥ inf

ES[f].

S∈Strat0(G)

Proof. Write M = (Ω,P) and G = (I′,Ω′,P′,R′) and denote by π: M → G the morphism from M to G. To deﬁne strategy S = (Ω′, P) for G, we must specify the transition probabilities Pn. We put, for x′n ∈ Ω′n and x′n+1 ∈ Ω′n+1,

Pn(x′n+1,x′n) def= Pn′(x′n+1,x′n) if n ∈/ I′, Pn(x′n+1,x′n) def= PrM[πn+1(Xn+1) = x′n+1 | πn(Xn) = x′n

Pn(xn+1,xn)PrM Xn = xn | πn(Xn) = x′n if n ∈ I′,

=

xn∈πn−1(x′n) xn+1∈πn−+11 (x′n+1)

where (X0,X1,... ,Xn,Xn+1,... ) is sampled from n≥0 Ωn using the Markov chain M.

S is a Markov chain. We ﬁrst must check that the functions Pn deﬁne a Markov chain on Ω′. To that end we need to verify that x′

n+1,x′n) = 1 for each x′n ∈ Ω′n. If n ∈/ I′, this follows from Pn = Pn′ and the respective property of Pn′. On the other hand, if n ∈ I′, then this follows because the quantity PrM[ · | πn(Xn) = x′n] is a conditional probability on an actual probability space, and so the total probability is 1.

n+1∈Ω′n+1 Pn(x′

S is a valid strategy for G. We must verify that the identity maps on (Ω′n)n induce a morphism from S = (Ω′, P) to the game G = (I′,Ω′,P′,R′). Since the condition (M3) holds vacuously for morphisms from Markov chains (because I = ∅), we need only to check conditions (M4) and (M5).

We ﬁrst check (M4). Suppose n ∈ I′. Assume that the states x′n ∈ Ω′n and x′

n+1 ∈ Ω′

n+1 satisfy Pn(x′n+1,x′n) > 0. From the deﬁnition of Pn in the case n ∈ I′, it follows that there exist xn ∈ π−1

n (x′n) and xn+1 ∈ π−1

n (x′n) such that Pn(xn+1,xn)PrM Xn = xn | πn(xn) = x′n > 0. In particular, Pn(xn+1,xn) > 0. By the condition (M4) applied to the morphism π: M → G, it follows that πn+1(xn+1) ∈ Rn′ (πn(xn)). As πn(xn) = x′n and πn+1(xn+1) = x′

n+1, this implies that n+1 ∈ Rn′ (x′n).

- x′


The condition (M5) is nearly trivial to check. Because the morphism S → G is used by the identity maps on (Ωn)n, the condition (M5) reduces to assertion that Pn = Pn′ for n ∈/ I′.

Checking that EMf = ESf. Use Markov chain M to sample sequence X = (X0,X1,... ) from n≥0 Ωn, and use S to sample X′ = (X0′,X1′,... ) from n≥0 Ω′n. Let x′ ∈ n≥0 Ω′n be arbitrary.

≤n for (x′0,... ,x′n). Deﬁne the notations X≤n and X′

Write x′

≤n similarly. We shall write π(x≤n) for π0(x0),π1(x1),... ,πn(xn) . We will show that, for every n and every choice of x′,

PrM[π(X≤n) = x′≤n] = PrS[X≤′ n = x′≤n]. (10) This will clearly imply EMf = ESf.

We use induction on n. The base case n = 0 holds because both Ω0 and Ω′

0 are single-element sets. Assume that (10) has been shown for all numbers that are at most n. Using the Markov property of

- S we compute


PrM[π(X≤n+1) = x′≤n+1] = PrM[πn+1(Xn+1) = x′n+1 | π(X≤n) = x′≤n]PrM[π(X≤n) = x′≤n]

= PrM[πn+1(Xn+1) = x′n+1 | πn(Xn) = x′n]PrS[X≤′ n = x′≤n].

To complete the proof it suﬃces to show that PrM[πn+1(Xn+1) = x′n+1 | πn(Xn) = x′n] = Pn(x′n+1,x′n), for it would then follow that

PrS[π(X≤n+1) = x′≤n+1] = Pn(x′n+1,x′n)PrS[X≤′ n = x′≤n] by Markov property of S

= Pn(x′n+1,x′n)PrM[X≤′ n = x′≤n] by the induction hypothesis

= PrM[X≤′ n+1 = x′≤n+1].

If n ∈ I′, the requisite formula for PrM[πn+1(Xn+1) = x′n+1 | πn(Xn) = x′n] follows from the deﬁnition of Pn(x′n+1,x′n).

If n ∈/ I′, then we use the condition (M5) for the morphism π: M → G to conclude

PrM[πn+1(Xn+1) = x′n+1 | πn(Xn) = x′n]

PrM[πn+1(Xn+1) = x′n+1 | Xn = xn]PrM[Xn = xn | πn(Xn) = x′n]

=

xn∈πn−1(x′n)

Pn(xn+1,xn)PrM[Xn = xn | πn(Xn) = x′n]

=

xn∈πn−1(x′n) xn+1∈πn−+11 (x′n+1)

Pn′ x′n+1,x′n PrM[Xn = xn | πn(Xn) = x′n] by (M5) for π: M → G

=

xn∈πn−1(x′n)

Pn x′n+1,x′n PrM[Xn = xn | πn(Xn) = x′n] since n ∈/ I′

=

xn∈πn−1(x′n)

= Pn x′n+1,x′n .

![image 97](<2020-bukh-longest-common-subsequences-between_images/imageFile97.png>)

![image 98](<2020-bukh-longest-common-subsequences-between_images/imageFile98.png>)

![image 99](<2020-bukh-longest-common-subsequences-between_images/imageFile99.png>)

![image 100](<2020-bukh-longest-common-subsequences-between_images/imageFile100.png>)

The second ingredient in the proof of Theorem 11 is a derandomization argument that permits us to turn any randomized strategy into a deterministic strategy.

- Lemma 14. Suppose f is any function on a Markov game G, and S is a strategy for G. Then there is a deterministic strategy S∗ for G satisfying ES[f] ≥ ES∗[f].


Proof. Let G = (I,Ω,P,R), and S = (Ω, P). Make a new probability space M consisting of countably many independent random variables {Dn,xn : n ∈ I,xn ∈ Ωn}. The random variable Dn,xn is deﬁned by PrM[Dn,xn = xn+1] def= Pn(xn+1,xn). Let S∗ = (Ω, P∗) be a deterministic strategy with the transition function

1 if Dn,xn = xn+1, 0 otherwise.

Pn∗(xn+1,xn) =

Note that the strategy S∗ is a random variable on the space M.

The S∗ is indeed a strategy for G, for the conditions (M4) and (M5) follow from respective conditions for S. Since

EM ES∗[f] = ES[f], there is a choice of S∗ such that ES[f] ≥ ES∗[f].

![image 101](<2020-bukh-longest-common-subsequences-between_images/imageFile101.png>)

![image 102](<2020-bukh-longest-common-subsequences-between_images/imageFile102.png>)

![image 103](<2020-bukh-longest-common-subsequences-between_images/imageFile103.png>)

![image 104](<2020-bukh-longest-common-subsequences-between_images/imageFile104.png>)

# 5 Crude upper bound on E[Pd − P0]

Markov game strengthening. In this section we will prove a strengthening of Theorem 4. Its two advantages are that it is easier to prove, and that it is in the form that will be useful in the proof of the asymptotics for E[Pd − P0] in Section 8.

The strengthening concerns the following Markov game.

- Game A. Game state: Nonnegative integers P0 < P1 < ... < Pd, which are interpreted as particle positions. Start: Pi = i for all i = 0,1,... ,d. Duration: L turns. Each turn: Adversary chooses a partition A of {0,1,... ,d} into k parts, some of which are possibly


empty. Then Fortune picks a set A ∈ A uniformly among the k sets in A. The particle positions are then updated as in the Step (B) of Proposition 6.

Since this is our ﬁrst example of a Markov game, before stating our result we explain how to translate this description into the formalism of the preceding section.

We use the personiﬁed ‘Fortune’ to denote the times when the transitions are random, and ‘Adversary’ to denote the remaining times. In this game, actions of Adversary and Fortune alternate, with Adversary acting ﬁrst. Hence, I = {0,2,4,6,... } is the set of times when Adversary acts. Since each game turn is made of two actions, and the game lasts L turns, this means that we are interested only in the times 0,1,... ,2L, and can ignore whatever happens afterward. For the same reason, the notation Pi(L) below refers to the value of Pi at the end of the L’th turn, i.e., at the time 2L.

At the beginning of Adversary’s turns, the state space consists of an ordered tuple (P0,P1,... ,Pd) satisfying P0 < P1 < ··· < Pd. After Adversary makes their turn, the state space becomes enriched with the partition A that they choose. Hence, denoting by P(d) the set of of all partitions of {0,1,... ,d} into exactly k (possibly empty) parts, we have

Ω0 = {(0,1,... ,d)} Ωn = {(P0,P1,... ,Pd) ∈ Zd≥0 : P0 < P1 < ... < Pd} if n ∈ I \ {0}, Ωn = {(P0,P1,... ,Pd,A) ∈ Zd≥0 × P(d) : P0 < P1 < ... < Pd} if n ∈/ I.

The functions Rn are simple: Rn(P0,P1,... ,Pd) = {(P0,P1,... ,Pd)} × P(d). The deﬁnition of Pn is more cumbersome: suppose n ∈/ I, and let xn = (P0,P1,... ,Pd,A) ∈ Ωn. For a set A ∈ A, denote by Evolve(xn,A) the particle positions after applying the procedure from the Step (B) of Proposition 6 to particles in positions P0,P1,... ,Pd with the set A in place of A[L]. For a state xn+1 = (P0′,P1′,... ,P′

d) ∈ Ωn+1, let r be the number of sets A ∈ A for which Evolve(xn,A) = xn+1. Then Pn(xn+1,xn) = r/k.

We are now ready to state the main result of this section.

![image 105](<2020-bukh-longest-common-subsequences-between_images/imageFile105.png>)

- Lemma 15. For every adversary’s strategy in Game A, E[Pi+1(L) − Pi(L)] ≤ 2L/k + 1 for all i. In particular, E[Pd(L) − P0(L)] ≤ d 2L/k + d for every strategy.


![image 106](<2020-bukh-longest-common-subsequences-between_images/imageFile106.png>)

The expectation here is taken with respect to the strategy. In particular, the lemma immediately implies Theorem 4. Indeed, let G = (I,Ω,P,R) be the formalization of Game A constructed above, and consider the strategy S = (Ω′,P′) where Ω′n consists of tuples (P0,P1,... ,Pd,w,w′) where P0 < P1 < ··· < Pd are nonnegative integers and w,w′ are words over [k] of lengths Pd + 1 and ⌊n/2⌋ respectively. The transition from Ω′

2ℓ to Ω′

2ℓ+1 is the identity, i.e., the chain remains in the same state. The transition from Ω′

2(ℓ+1) is performed by appending a random symbol to w′ and then executing the algorithm in Proposition 6 with ℓ in place of L. This is indeed a strategy for Game A, with the morphism π given by π2ℓ(P0,P1,... ,Pd,w,w′) = (P0,P1,... ,Pd) for even times and by π2ℓ+1(P0,P1,... ,Pd,w,w′) = (P0,P1,... ,Pd,A[ℓ]) for odd times.

2ℓ+1 to Ω′

We have stated the lemma in terms of d + 1 particles P0,... ,Pd rather than the pair Pi, Pi+1 only because we wanted to point its implication on the quantity E[Pd(L) − P0(L)]. For the purpose of giving a proof, we may however strip away the irrelevant particles, and focus solely on the gap between a ﬁxed pair of consecutive particles. We obtain a much simpler game:

- Game B. Game state: Positive integer ∆ (which we interpret as a gap between two consecutive particles). Start: ∆ = 1. Duration: L turns. Each turn: • First, Adversary chooses a vector v that either is the zero vector 0 ∈ Zk or is a


permutation of the vector (+1,−1,0,0,0,... ,0) ∈ Zk.

- • Second, Adversary decrements one of the coordinates of v, or keeps it intact.
- • Third, Fortune then picks i ∈ [k] uniformly at random, and adds vi to ∆.
- • Finally, if ∆ is 0 or less, then we reset ∆ to 1.


Objective: Adversary aims to maximize ∆.

In the formal language of Section 4, we may say that Game A admits a morphism into Game B. Again, we spell out the details.

We model Game B similarly to how we modeled Game A: it is the Markov game (I′,Ω′,P′,R′), where I′ = {0,2,4,6,... } (same as in Game A), Ω′n = N for positive even n, whereas for odd values

of n the set Ω′n consists of pairs of the form (∆,v) where ∆ ∈ N and v ∈ V with

- V def= U + W, U def= { 0} ∪ {v ∈ Zk : v is a permutation of (+1,−1,0,0,0,... ,0)},
- W def= { 0} ∪ {v ∈ Zk : v is a permutation of (−1,0,0,0,0,... ,0)}.


When n is odd, (∆,v) ∈ Ω′n, ∆′ ∈ Ω′n+1, we set Pn′ ∆′,(∆,v) = r/k where r is the number of coordinates i ∈ [k] such that ∆′ = max(∆ + vi,1). Finally, the Rn′ is deﬁned by Rn′ (∆) = {∆} × V (for even n).

The morphism π from Game A to Game B maps the (d + 1)-tuple (P0,... ,Pd) into the number ∆ = Pi+1−Pi and the partition A into vector v in such a way that choice of i’th part in A corresponds to choice of vi. The decrementation in game B corresponds to the particle Pi−1 bumping into Pi and pushing Pi.

Proof of Lemma 15. Invoking Observation 12, we see that Lemma 15 would follow if we show that E[∆] ≤ 1 + 2L/k for every strategy in Game B. That is precisely what we will do.

![image 107](<2020-bukh-longest-common-subsequences-between_images/imageFile107.png>)

Let ∆′ def= ∆ − 1/2. It suﬃces to show that

E[∆′(L)2] ≤ 41 + 2L/k (11) holds for every Adversary’s strategy. Indeed, Cauchy–Schwarz inequality would then imply that E[∆(L)] ≤ 14 + 2L/k + 12 ≤ 2L/k + 1.

![image 108](<2020-bukh-longest-common-subsequences-between_images/imageFile108.png>)

![image 109](<2020-bukh-longest-common-subsequences-between_images/imageFile109.png>)

![image 110](<2020-bukh-longest-common-subsequences-between_images/imageFile110.png>)

![image 111](<2020-bukh-longest-common-subsequences-between_images/imageFile111.png>)

![image 112](<2020-bukh-longest-common-subsequences-between_images/imageFile112.png>)

We prove (11) by induction on L. The base case L = 0 is immediate, so assume L > 0. Consider the vector v chosen by Adversary at the last (i.e., the L’th) turn of the game. Write it as v = u + w where u is either 0 or a permutation of (+1,−1,0,0,... ,0), and w is either 0 or a permutation of (−1,0,... ,0). Fix any strategy S for Game B, and denote by i ∈ [k] the Fortune’s random choice at turn L. We compute

PrS[∆′(L − 1) = x] k 1(x − 1)2 + k1(x + 1)2 + k−k2x2

ES (∆′(L − 1) + ui)2 ≤

![image 113](<2020-bukh-longest-common-subsequences-between_images/imageFile113.png>)

![image 114](<2020-bukh-longest-common-subsequences-between_images/imageFile114.png>)

![image 115](<2020-bukh-longest-common-subsequences-between_images/imageFile115.png>)

x∈Z+1/2

PrS[∆′(L − 1) = x](x2 + k2)

=

![image 116](<2020-bukh-longest-common-subsequences-between_images/imageFile116.png>)

x∈Z+1/2

= ES ∆′(L − 1)2 + k2. Since ∆′(L) = max(∆′(L − 1) + ui + wi,1/2) ≤ |∆′(L − 1) + ui|, it thus follows that

![image 117](<2020-bukh-longest-common-subsequences-between_images/imageFile117.png>)

ES ∆′(L)2 ≤ ES ∆′(L − 1)2 + k2, concluding the induction step.

![image 118](<2020-bukh-longest-common-subsequences-between_images/imageFile118.png>)

# 6 Crude lower bound on E[P1 − P0]

Similarly to the proof of the upper bound in the preceding section we shall compare the evolution of P1 − P0 to an (adversarial) random walk. The appropriate random walk is lazy, i.e., there is a

non-negligible probability that in a given step nothing happens. To argue that E[P1 −P0] is large, we must show that the random walk is not too lazy. This makes the argument more complex compared to that in the previous section.

The game we use is similar to the two-particle version of Game A, except that we must keep track of whether the symbols w[P0] and w[P1] are same or diﬀerent.

- Game C. Game state: Pair (∆,F) where ∆ ∈ N and F ∈ {same,diff}. Start: ∆ = 1, whereas F = same with probability 1/k and F = diff with probability


1 − 1/k. Duration: L turns. Each turn: What happens depends on the value of F at the turn’s start.

- • If F = same, then with probability 1/k Fortune decides to toss a coin.
- • If F = diff, then

- – with probability 1/k, Fortune decrements ∆ (setting it to 1 afterward should it become 0), and Adversary chooses the new value of F,
- – with probability 1/k, Fortune increments ∆, and decides to toss a coin,
- – with probability 1 − 2/k, nothing happens.


- • The coin, should Fortune decide to toss it, lands on heads with probability 1−1/k. Should it land on heads, the new value of F is set to diff, and should it land on tails, the new value of F is set to same.


Objective: Adversary aims to minimize ∆.

There is a morphism from the Markov chain of Proposition 6 into this game, which can informally be described as setting ∆ = P1 − P0 and setting F = same iﬀ w[P0] = w[P1].

The formal treatment is similar to that of Games A and B in the preceding section: each turn of Game C is represented by two time steps, the ﬁrst step being random, and the second step being adversarial. The exception is the very ﬁrst step in which the initial value of F is chosen. So,

- I = {2,4,6,... }. The state spaces are


Ωn = {(∆,F) : ∆ ∈ N, F ∈ {same,diff}} if n ∈/ I and n ≥ 1, Ωn = {(∆,F,C) : ∆ ∈ N, F ∈ {same,diff}, C ∈ {yes,no}} if n ∈ I,

where the variable C records whether the Adversary has the choice of F at the next step. The functions Rn are deﬁned by

Rn(∆,F,no) = {(∆,F)}, Rn(∆,F,yes) = {(∆,same),(∆,diff)}.

The transition functions Pn are deﬁned by

Pn (∆,diff,no),(∆,same) = k1(1 − k1),

![image 119](<2020-bukh-longest-common-subsequences-between_images/imageFile119.png>)

![image 120](<2020-bukh-longest-common-subsequences-between_images/imageFile120.png>)

Pn (∆,same,no),(∆,same) = 1 − k1 + k12, Pn (max(∆ − 1,1),same,yes),(∆,diff) = k1,

![image 121](<2020-bukh-longest-common-subsequences-between_images/imageFile121.png>)

![image 122](<2020-bukh-longest-common-subsequences-between_images/imageFile122.png>)

![image 123](<2020-bukh-longest-common-subsequences-between_images/imageFile123.png>)

Pn (∆ + 1,diff,no),(∆,diff) = k1(1 − k1), Pn (∆ + 1,same,no),(∆,diff) = k12,

![image 124](<2020-bukh-longest-common-subsequences-between_images/imageFile124.png>)

![image 125](<2020-bukh-longest-common-subsequences-between_images/imageFile125.png>)

![image 126](<2020-bukh-longest-common-subsequences-between_images/imageFile126.png>)

Pn ∆,diff,no),(∆,diff) = 1 − k2.

![image 127](<2020-bukh-longest-common-subsequences-between_images/imageFile127.png>)

Call a turn in which Fortune either decrements or increments ∆ a good turn. Let H be the total number of coin tosses that landed on heads. Let G be the number of good turns. Once a coin lands on heads, at least one good turn must occur before the next coin toss. Hence, G ≥ H − 1.

Because each turn Fortune decides to toss a coin with the same probability 1/k, it follows that

- H ∼ Binom L,(1/k)(1 − 1/k) . Since (1/k)(1 − 1/k) ≥ 1/2k (in view of k ≥ 2), from an asymmetric version of the Chernoﬀ bound (see [1, Theorem A.1.13]) we infer that


(L/4k)2

Pr[G ≤ L/4k − 1] ≤ Pr[H ≤ L/4k] ≤ exp −

2(1/k)(1 − 1/k)L ≤ exp(−L/32k). (12) Because of this estimate, we may simplify the game further:

![image 128](<2020-bukh-longest-common-subsequences-between_images/imageFile128.png>)

- Game D. Game state: Nonnegative integer ∆. Start: ∆ = 1. Duration: L turns. Each turn: Adversary decides if they want this turn to be good. If they decide on the turn being


good, Fortune adds either −1 or +1 to ∆ at random (setting ∆ to 1 afterward should it become 0). If they decide on the turn being bad, nothing happens.

Objective: Adversary aims to minimize ∆. Penalty: Adversary pays penalty of T +1 to the objective function if the total number of good

turns is less than T def= L/4k − 1.

Recall that penalties provide a shorthand for deﬁning objective functions. So, formally the objective is equal to ∆ if the number of good turns is at least L/4k − 1, and is equal to ∆ + T + 1 otherwise. However, as we shall shortly see, separating the penalty is convenient in the analysis.

If Adversary uses an optimal strategy, then the penalty condition is never triggered. Indeed, if S is any strategy that sometimes triggers the penalty, we may modify it so it does not. Namely, when exactly t turns are left and only T − t good turns have been played, not allowing the next turn to be good triggers the penalty. In any such situation, Adversary should make all the remaining turns good. Doing so strictly improves the strategy. So, every optimal strategy always uses at least T good turns.

Because it does not matter which turns are good, we may assume that the ﬁrst T turns are good, whereas the subsequent turns are subject to Adversary’s strategy. We claim that Adversary’s best strategy is to disallow good turns on all of these subsequent turns.

Indeed, ﬁx any strategy and denote by ∆(ℓ) the value of ∆ at the end of the ℓ’th turn. Then ∆(ℓ + 1) = max(∆(ℓ) + vℓ,1) where vℓ is either 0 (if the turn is bad) or a uniform element of {±1}. In either case, E[∆(ℓ + 1)] ≥ E[∆(ℓ)] with equality if the turn is bad. Hence, E[∆(L)] ≥ E[∆(T)] with equality if all but the ﬁrst T turns are bad. So, in particular, Adversary’s optimal strategy is to disallow good turns.

The reﬂection principle tells us that the value of ∆ under the optimal play is the same as 1/2 + |∆′| where ∆′ is the position of a simple random walk on Z + 1/2 starting from 1/2 after

- T steps. Therefore,


 

T T/2

- 1

![image 129](<2020-bukh-longest-common-subsequences-between_images/imageFile129.png>)

- 2


- 1

![image 130](<2020-bukh-longest-common-subsequences-between_images/imageFile130.png>)

- 2


+ 2−T · T +

, if T is even,

E[∆] ≥ E 1/2 + |∆′| =

T − 1 (T − 1)/2

- 1

![image 131](<2020-bukh-longest-common-subsequences-between_images/imageFile131.png>)

- 2




+ 2−T · 2T

, if T is odd,

where the formula for E |∆′| is proved in Appendix B. Both in the case T is even and in the case T is odd, using Stirling’s formula with explicit error term (see [16, Eq. (9.91)]), we may show that

2n n ≥ e−1/6n√4πnn for all n, and use this to deduce that

![image 132](<2020-bukh-longest-common-subsequences-between_images/imageFile132.png>)

![image 133](<2020-bukh-longest-common-subsequences-between_images/imageFile133.png>)

![image 134](<2020-bukh-longest-common-subsequences-between_images/imageFile134.png>)

E[∆] ≥ 12 + 47(T + 1), if L ≥ 200k, in the optimal strategy for Game D.

![image 135](<2020-bukh-longest-common-subsequences-between_images/imageFile135.png>)

![image 136](<2020-bukh-longest-common-subsequences-between_images/imageFile136.png>)

Let Pnlt be the penalty function from Game D. Recall that the pull back of Pnlt from Game D to Game C is a function on Game C, which is also denoted by Pnlt. Using (12) and applying Observation 12 to the morphism from Game C to Game D, we obtain

ES[∆] + (T + 1)exp(−L/32k) ≥ inf

inf

ES[∆ + Pnlt] ≥ inf

S∈Strat(Game C)

S∈Strat(Game C)

ES′[∆ + Pnlt]

S′∈Strat(Game D)

![image 137](<2020-bukh-longest-common-subsequences-between_images/imageFile137.png>)

- 1

![image 138](<2020-bukh-longest-common-subsequences-between_images/imageFile138.png>)

- 2


L 7k

≥

+

.

![image 139](<2020-bukh-longest-common-subsequences-between_images/imageFile139.png>)

Since (T + 1)exp(−L/32k) ≤ 12 when L ≥ 200k, Theorem 3 follows.

![image 140](<2020-bukh-longest-common-subsequences-between_images/imageFile140.png>)

# 7 Most expectant partitions are trivial

As sketched in the introduction, the key to the proof of Theorem 5 is to show that almost all expectant partitions are trivial, which are deﬁned as partitions all of whose non-empty parts are singletons. Let B def= {ℓ < L : A[ℓ] is non-trivial}. This section is devoted to the proof of the following estimate.

- Lemma 16. The number of non-trivial expectant partitions satisﬁes Pr[|B| ≥ 6d2L/k] ≤ 4d2Lexp(−L1/2k−3/2)


for all d,L ≥ 1 and all k ≥ 2.

Bumps and jumps. We shall deﬁne Q0,... ,Qd in such a way that Q0,... ,Qd is a permutation of P0,... ,Pd. In particular, an expectant partition will be non-trivial if and only if w[Qi] = w[Qj] for some pair i = j.

Following the interpretation of P0,... ,Pd as particles, we shall think of Q0,... ,Qd also as particles. Informally, we think of P-particle that tries to move into an already-occupied positions as bumping the particle that is located there. On the other hand, Q-particles will avoid moving into an alreadyoccupied position, jumping over the particles in front of it instead.

Formally, we begin with Qi(0) = i for i = 0,1,... ,d. At time step ℓ, we examine w′[ℓ], and use its value to deﬁne the set I = {i : w[Qi(ℓ)] = w′[ℓ]}. We think of particles {Qi : i ∈ I} as being excited. We then examine excited particles in decreasing order of their positions. We move each excited particle to next vacant position on the right, jumping over non-excited particles if necessary.

The advantage of Q-particles over P-particles is that we may focus on a single pair of particles at a time, without worrying that other particles might bump and displace them.

The ﬁgure below illustrates the diﬀerence between the dynamics of P-particles and Q-particles, during the same time step.

- P0 P1 P2 P3 P4 P5

- Q2 Q4 Q0 Q3 Q1 Q5


- P0 P1 P2 P3 P4 P5

- Q2 Q4 Q0 Q3 Q1 Q5


- P0 P1 P2 P3 P4 P5

- Q2 Q0 Q4 Q3 Q5 Q1


Four particles are excited

Previous state

Next state

Figure 2: Evolution of P- and Q-particles (example).

Two-particle evolution. Fix a pair i = j; and let Bij def= {ℓ : w[Qi(ℓ)] = w[Qj(ℓ)]}. We will show that

Pr[|Bij| ≥ 6L/k] ≤ 2Lexp(−L1/2k−3/2). (13) Since B = i =j Bij and there are d+12 pairs i = j, Lemma 16 will then follow from the union bound.

Throughout the rest of the section, we use notations Qmax def= max(Qi,Qj) and Qmin def= min(Qi,Qj). Since the right side of (13) exceeds 1 if L ≤ k3, we may also assume that L > k3 in what follows.

Since Q-particles move if and only if they are excited, it is tempting to immediately discard all the particles except for Qi and Qj. This requires a little care because Qi and Qj might still jump over the other particles. However, as the next lemma shows, the values of w[Qmax] still behave as if the other particles do not exist.

- Lemma 17. Let ℓ be arbitrary. Then Pr w[Qmax(ℓ)] = s | Qmax(ℓ) > Qmax(ℓ − 1) ∧ Hist(ℓ) = 1/k for all s ∈ [k],


where Hist(ℓ) consists of values of 5-tuples (Qi(t),Qj(t),w[Qi(t)],w[Qj(t)],w′[t]) for all t < ℓ.

In particular, if we consider the times ℓ when Qmax(ℓ) > Qmax(ℓ−1), and write down the sequence of values of w[Qmax(ℓ)] at those times, then we obtain a uniform random word.

Proof of Lemma 17. It suﬃces to prove, for each T, that

Pr w[Qmax(ℓ)] = s | T = Qmax(ℓ) > Qmax(ℓ − 1) ∧ Hist(ℓ) = 1/k for all s ∈ [k].

Consider T-bounded dynamics, which is identical to the Q-particle dynamics except that once the value of Qr, for r = i,j, becomes T or larger, we stop tracking Qr. We imagine uncovering the symbols of w only when a particle lands on it. Under this coupling, if ℓ is the ﬁrst time when Qmax becomes T or larger, the value of w[Qmax(ℓ)] is not revealed before time ℓ, and so is independent of the history before the time ℓ.

![image 141](<2020-bukh-longest-common-subsequences-between_images/imageFile141.png>)

![image 142](<2020-bukh-longest-common-subsequences-between_images/imageFile142.png>)

![image 143](<2020-bukh-longest-common-subsequences-between_images/imageFile143.png>)

![image 144](<2020-bukh-longest-common-subsequences-between_images/imageFile144.png>)

We can delay exposing w[Qmax(ℓ)] for even longer than in the preceding proof: Imagine that for each symbol w[p] of w we generate a random {0,1}-vector of length k having a single 1 and k − 1 many 0’s. We then set w[p] to the position of the single 1 in that vector. In the T-bounded dynamics, when Qmax becomes equal to some value T, we do not expose w[T] completely, but instead only check if w[T] = w[Qmin] by exposing w[Qmin]’th position of the vector associated to w[T]. That is enough to decide if i and j belong to the same part of the expectant partition. Then each time Qmin increases, we similarly check for w[Qmax] = w[Qmin]. This gives us a way to bound the conditional probability

Pr w[Qmax(ℓ)] = w[Qmin(ℓ)] | (Qmin(ℓ) > Qmin(ℓ − 1)) ∧ Hist(ℓ) .

Indeed, if T = Qmax(ℓ) = Qmax(ℓ−1), then the probability is 0 if w[Qmin(ℓ)]’th position of the vector associated to w[T] has been exposed, and otherwise the probability is 1/r where r is the number of yet-unexposed entries in the vector associated to w[Qmax]. If T = Qmax(ℓ) > Qmax(ℓ − 1), then the probability is 1/k. So, in all three cases, we obtain that

Pr w[Qmax(ℓ)] = w[Qmin(ℓ)] | (Qmin(ℓ) > Qmin(ℓ − 1)) ∧ Hist(ℓ) ≤ 1/r.

This suggests the following Markov game, in which we give Adversary the power to choose new values of Qi, Qj and w[Qmin], whenever Qi and Qj change. Furthermore, when Adversary chooses the value of w[Qmin], they have the extra power of overwriting the old value of w[Qmin]. Adversary can also choose the initial values of Qi and Qj. To aid the analysis, the initial set of yet-unexposed positions in w[Qmax] will be arbitrary. By symmetry, only its size will matter.

More speciﬁcally, the game depends on two parameters s0 ∈ {0,1,... ,k} and b0 ∈ {in,out} determining the initial state. In this game, S corresponds to the set of yet-unexposed positions of the {0,1}-vector associated to w[Qmax]. The parameters s0 and b0 indicate the initial size of S, and whether w[Qmin] is an element of S. Though we are interested only in the case (s0,b0) = (k,in), the extra generality will be useful in the analysis.

- Game E.


Game state: Set S ⊆ [k], two non-negative distinct integers Qi,Qj and a symbol w[Qmin] ∈ [k]. Duration: T turns. Start: Set S = [s0] (if s0 = 0, then S = ∅). Adversary chooses the initial values of Qi and

Qj. Adversary also chooses the initial value of w[Qmin], which has to be an element of S if b0 = in, or an element of [k] \ S if b0 = out.

Each turn: (G1) First, if w[Qmin] ∈ S, then

- • with probability 1/|S|, Fortune sets S to ∅,
- • with probability 1 − 1/|S|, Fortune removes w[Qmin] from the set S.


If, on the other hand, w[Qmin] ∈/ S, nothing happens. (G2) Second,

- (a) if S = ∅, then

- • with probability 1/k, Fortune forces Adversary to increase Qi (to a value of Adversary’s choice),
- • with probability 1/k, Fortune forces Adversary to increase Qj (to a value of Adversary’s choice),
- • with probability 1 − 2/k, nothing happens,


- (b) if S = ∅, then

- • with probability 1/k, Fortune forces Adversary to increase both Qi and Qj to values of Adversary’s choice,
- • with probability 1 − 1/k, nothing happens,


- (c) if Qmax is increased as a result of (G2a) or (G2b), then S is reset to [k],
- (d) if Qmin or Qmax is increased as a result of (G2a) or (G2b), then Adversary sets w[Qmin] at will.


![image 145](<2020-bukh-longest-common-subsequences-between_images/imageFile145.png>)

Objective: Let B(s0,b0,T) be the number of those turns for which we have S = ∅ at the start of step (G2). The Adversary’s goal is to maximize f = f B(s0,b0,T) , which is some non-decreasing function of B(s0,b0,T).

![image 146](<2020-bukh-longest-common-subsequences-between_images/imageFile146.png>)

![image 147](<2020-bukh-longest-common-subsequences-between_images/imageFile147.png>)

From the preceding discussion and the adversarial game argument, we know that E[f] ≤ sup

ES[f]. (14)

S∈Strat(Game E)

![image 148](<2020-bukh-longest-common-subsequences-between_images/imageFile148.png>)

In our application of Game E, f will be the characteristic function of the event B(s0,b0,T) ≥ 3pL for a suitable choice of p ∈ [0,1]. For simplicity and generality of the analysis, we shall assume that f is an arbitrary non-decreasing function of B(s0,b0,T). Note that any such function is a function on Game E in the sense of Section 4.

![image 149](<2020-bukh-longest-common-subsequences-between_images/imageFile149.png>)

- Analysis of Game E. Because the function f that Adversary tries to maximize is non-decreasing, Adversary’s optimal strategy must be memoryless, i.e., Adversary’s actions should depend only on


the current set S, integers Qi,Qj and the symbol w[Qmin]. Furthermore, from the symmetry, it is clear that only the size of S matters, not the actual constituent elements. It is not hard to see, by induction on T, that decreasing the size of S is advantageous to Adversary, i.e., decreasing |S| can only increase the value of B(s0,b0,T). From this it follows that Adversary should set w[Qmin] to an element of S whenever they can. Similarly, Adversary should avoid Qmin jumping over Qmax and thus resetting S. They may do so by choosing the initial gap between Qi and Qj to be suﬃciently large.

![image 150](<2020-bukh-longest-common-subsequences-between_images/imageFile150.png>)

Consider the evolution of |S| and of the Boolean value of the statement “w[Qmin] ∈ k” in Adversary’s optimal strategy described above. They form a pair (s,b) undergoing a random walk on the domain {0,1,... ,k} × {out,in} \ {(0,in),(k,out)} with the initial state (s0,b0), and the following transition rule:

- • If the current state is (0,out), then

- – (⋆) with probability 1/k, the next state is (k,in),
- – (⋆) with probability 1 − 1/k, the next state is (0,out).


- • If the current state is (s,out), for s ≥ 1, then

- – with probability 1/k, the next state is (s,in),
- – with probability 1/k, the next state is (k,in),
- – with probability 1 − 2/k, the next state is (s,out).


- • If the current state is (s,in), for s ≥ 1, then


- – (⋆) with probability 1/ks, the next state is (k,in),
- – (⋆) with probability (1/s)(1 − 1/k), the next state is (0,out),
- – with probability (1 − 1/s)(1/k), the next state is (s − 1,in),
- – with probability (1 − 1/s)(1/k), the next state is (k,in),
- – with probability (1 − 1/s)(1 − 2/k), the next state is (s − 1,out).


![image 151](<2020-bukh-longest-common-subsequences-between_images/imageFile151.png>)

Here, (⋆) indicates that the respective turn is counted by B(s0,b0,L). Denote this Markov chain by M. The chain M is aperiodic because for the state (0,out) there

is a positive probability of remaining in the state. The chain is also clearly strongly connected. Denote by π the stationary distribution of M. If we start the chain from the stationary distribu-

![image 152](<2020-bukh-longest-common-subsequences-between_images/imageFile152.png>)

tion, then E(s,b)∼πB(s,b,L) = L · Pr(s,b)∼π[(⋆) encountered on transition from (s,b)]. As chain M is aperiodic, it follows that, for every initial condition (s,b),

![image 153](<2020-bukh-longest-common-subsequences-between_images/imageFile153.png>)

lim

E[B(s,b,L)]/L = Pr

L→∞

(s,b)∼π

[(⋆) encountered]. (15)

It remains to compute the probability on the right hand side, and to bound the rate of convergence. It is routine to verify that the stationary distribution is given by

 

1

k22k−1 · s2s−1 if b = in and s ∈ [k],

![image 154](<2020-bukh-longest-common-subsequences-between_images/imageFile154.png>)

1

k22k−1 · s2s−1(k − 2) if b = out and s ∈ [k − 1],

Pr

[(s,b)] =

![image 155](<2020-bukh-longest-common-subsequences-between_images/imageFile155.png>)

π



1

k22k−1 · (2k − 1)(k − 1) if (s,b) = (0,out). From this we obtain

![image 156](<2020-bukh-longest-common-subsequences-between_images/imageFile156.png>)

1 k22k−1 · (2k − 1)(k − 1) +

p def= Pr

[(⋆) encountered] =

![image 157](<2020-bukh-longest-common-subsequences-between_images/imageFile157.png>)

(s,b)∼π

k

2k − 1 k2k−1

2s−1 =

.

![image 158](<2020-bukh-longest-common-subsequences-between_images/imageFile158.png>)

s=1

Let Xi be the characteristic random variable of the event that we visit (⋆) at the i’th step of the chain. Then B(s,b,L) = X1 + X2 + ··· + XL. To bound the rate of convergence in (15) we require a tail bound for this sum. Though there are a number of such results in the literature [29, 13, 37, 15, 22], the explicit bounds for non-reversible chains are complicated to state. The simple form of M allows

![image 159](<2020-bukh-longest-common-subsequences-between_images/imageFile159.png>)

us to give a short and self-contained argument. The resulting bound is signiﬁcantly weaker, but it is suﬃcient for our application.

We begin by noting that, from every state, the probability of making a transition to the state (k,in) is 1/k. Suppose we have two copies of the chain with diﬀerent starting states. We couple their evolution as follows. At each step we toss a biased coin that lands heads with probability 1/k. If it lands on heads, we transition to (k,in) simultaneously in both chains. If it lands on tails, we make steps in the two chains independently conditioned on not transitioning to (k,in). Since the probability that the two chains are in diﬀerent states after t steps is at most (1 − 1/k)t, this implies, via [28, Theorem 5.2], that the total variation distance to π from M after t steps is at most (1−1/k)t. Let T be a natural number to be chosen later, and partition the sequence X1,... ,XL into T subsequences, each of which is made of samples T steps apart. Let Xi,XT+i,... ,XmT+i be any such subsequence, where m = m(i) = ⌊(L − i)/T⌋ and i ∈ {1,2,... ,T}. Drop the ﬁrst element Xi; the total variation distance between (XT+i,... ,XmT+i) and m independent samples from π is at most m(1 − 1/k)T . Since Xi’s are {0,1}-valued, it follows from the usual Chernoﬀ bound [1, Theorem A.1.4] that

Pr[XT+i + ··· + XmT+i − mp ≥ λ] ≤ e−2λ2/m + m(1 − 1/k)T ≤ e−2Tλ2/L + me−T/k. Setting λ = L/2k, and using the union bound over i we obtain

![image 160](<2020-bukh-longest-common-subsequences-between_images/imageFile160.png>)

![image 161](<2020-bukh-longest-common-subsequences-between_images/imageFile161.png>)

Pr[XT+1+XT+2 + ··· + XL − (L − T)p ≥ T L/2k] ≤

![image 162](<2020-bukh-longest-common-subsequences-between_images/imageFile162.png>)

Pr[XT+i + ··· + Xm(i)T+i − m(i)p ≥ L/2k]

i∈[T]

≤ (T + L)e−T/k. We choose T = (2kL)1/2p. Since X1 + ··· + XT ≤ T and T ≤ pL (as L > k3), we deduce that Pr[B(s,b,L) ≥ 3pL] ≤ 2Le−p(2L/k)1/2.

![image 163](<2020-bukh-longest-common-subsequences-between_images/imageFile163.png>)

Since 1/k ≤ p ≤ 2/k, the desired bound (13) follows from an application of (14) to the characteristic function of the event “B(s0,b0,T) ≥ 3pL”.

![image 164](<2020-bukh-longest-common-subsequences-between_images/imageFile164.png>)

- 8 Asymptotics for E[Pd − P0] In this section we prove Theorem 5, which is the asymptotic


![image 165](<2020-bukh-longest-common-subsequences-between_images/imageFile165.png>)

E[Pd(L) − P0(L)] = 2 dL/k · 1 + O

1 d2/3

+

![image 166](<2020-bukh-longest-common-subsequences-between_images/imageFile166.png>)

d3/2 k1/2

log L (L/dk)1/2

+

![image 167](<2020-bukh-longest-common-subsequences-between_images/imageFile167.png>)

![image 168](<2020-bukh-longest-common-subsequences-between_images/imageFile168.png>)

k1/2d3/2L3/2 exp(L1/2k−3/2)

+

![image 169](<2020-bukh-longest-common-subsequences-between_images/imageFile169.png>)

. (16)

By Theorem 4 we see that E[Pd(L) − P0(L)] ≤ d 2L/k + d = 2 dL/k · O

√

![image 170](<2020-bukh-longest-common-subsequences-between_images/imageFile170.png>)

![image 171](<2020-bukh-longest-common-subsequences-between_images/imageFile171.png>)

![image 172](<2020-bukh-longest-common-subsequences-between_images/imageFile172.png>)

![image 173](<2020-bukh-longest-common-subsequences-between_images/imageFile173.png>)

d + dk/L .

√

d = O exp( k1/L2d13//22kL−33//22) + kd31//22 if L ≤ k3 or d ≥ 1001 k1/2 or k ≤ C. Since dk/L = O (L/dk logL)1/2 , in the proof of (16) we may assume that L ≥ k3, and d ≤ 1001 k1/2, and k ≥ k0.

![image 174](<2020-bukh-longest-common-subsequences-between_images/imageFile174.png>)

Let k0 be a constant to be determined. Note that

![image 175](<2020-bukh-longest-common-subsequences-between_images/imageFile175.png>)

![image 176](<2020-bukh-longest-common-subsequences-between_images/imageFile176.png>)

![image 177](<2020-bukh-longest-common-subsequences-between_images/imageFile177.png>)

![image 178](<2020-bukh-longest-common-subsequences-between_images/imageFile178.png>)

![image 179](<2020-bukh-longest-common-subsequences-between_images/imageFile179.png>)

![image 180](<2020-bukh-longest-common-subsequences-between_images/imageFile180.png>)

Recall that, for a word w, LNDS(w) is the length of the longest nondecreasing subsequence in w. The study of LNDS(w) for a random word began with the case when w is a random permutation. In this case, the asymptotics was obtained in [30] and [36], and then much reﬁned later in [3]. Similar results for LNDS(w) itself was ﬁrst obtained by [35], building on the earlier work [3] for random permutations. The results have been extended and reﬁned in a number of subsequent works, including [21, 26].

The main result of [35] shows that, after suitable normalization, LNDS(w) converges in distribution to the Tracy–Widom distribution F2. For our purposes, convergence in distribution is insuﬃcient, as we need an estimate on E[LNDS(w)]. In Appendix C we combine the existing results into the following estimate.

- Lemma 18.


- (i) For a uniform random word w ∼ [k]n, E[LNDS(w)] − n/k

![image 181](<2020-bukh-longest-common-subsequences-between_images/imageFile181.png>)

2√n

![image 182](<2020-bukh-longest-common-subsequences-between_images/imageFile182.png>)

= 1 + O

1 k2/3

![image 183](<2020-bukh-longest-common-subsequences-between_images/imageFile183.png>)

+

k2 + k log n n1/2

![image 184](<2020-bukh-longest-common-subsequences-between_images/imageFile184.png>)

.

- (ii) There exists an absolute constant C > 0 such that the following holds. Pick m ∼ Binom(n,p), and then choose w ∼ [k]m uniformly. Then


k2 + k log pn (pn)1/2

E[LNDS(w)] − pn/k 2√pn

n log n ≥ C.

1 k2/3

+

whenever p

= 1 + O

![image 185](<2020-bukh-longest-common-subsequences-between_images/imageFile185.png>)

![image 186](<2020-bukh-longest-common-subsequences-between_images/imageFile186.png>)

![image 187](<2020-bukh-longest-common-subsequences-between_images/imageFile187.png>)

![image 188](<2020-bukh-longest-common-subsequences-between_images/imageFile188.png>)

![image 189](<2020-bukh-longest-common-subsequences-between_images/imageFile189.png>)

We shall analyze the concatenation A[0]A[1]··· A[L−1] appearing in Proposition 7 by partitioning the word A[0]A[1]··· A[L − 1] into two parts: those subwords A[ℓ] that come from trivial expectant partitions, and those that come from non-trivial expectant partitions. To analyze the ﬁrst part we will appeal to the known results on LNDS in random words (encapsulated in Lemma 18). We will then argue that even if the remaining partitions A[ℓ] are chosen adversarily, the LNDS is unlikely to change much. The adversarial argument is captured by the following Markov game.

- Game F. Game state: Sequence of sets A[0],... ,A[ℓ − 1] ⊆ {0,1,... ,d}, each of which is marked either as


‘tampered’ or ‘untampered’. Start: The sequence is empty. Duration: L turns. Each turn: • First, Adversary decides whether to intervene this turn. If they decide to intervene, then they choose a partition A of {0,1,... ,d} into k parts, some of which are possibly empty, and also choose a position where to insert the next set into the list A[0],... ,A[ℓ − 1] that must be after the last tampered set (if any). If they decide not to intervene, then A becomes the trivial partition.

• Then Fortune picks a set A ∈ A uniformly among the k sets in A. The set A is then inserted at the chosen position (if Adversary intervened) or at the end of the list (if Adversary abstained this turn). If A was chosen by Adversary, the inserted set is marked as ‘tampered’; otherwise, it is ‘untampered’.

Objective: Adversary aims either to maximize or to minimize E[LNDS(A[0]A[1]... A[L − 1])]. Penalty: Adversary pays penalty of L to the objective function if the total number of interven-

tions exceeded 6d2L/k.

It is not hard to extract from Proposition 6 a Markov chain admitting a morphism to Game F. Indeed, we may think of the state of Markov chain from Proposition 6 at time ℓ as consisting of the word w, the preﬁx w′

<ℓ as well as all partitions A[0],... ,A[ℓ−1] and choices A[0],... ,A[ℓ−1]. We can then break each step into parts: computing A[ℓ] in the ﬁrst step, and examining w′[ℓ] and choosing A[ℓ] in the second step. By giving Adversary the power to choose the partitions in the even-numbered steps, and also the power to insert the partitions not only at the end, but also in the middle of the list, we obtain the game above.

- Analysis of Game F. Since LNDS(A[0]··· A[L − 1]) is always between 0 and L, in the optimal play Adversary must never use more than 6d2L/k interventions. Indeed, any strategy that sometimes uses more than 6d2L/k interventions can be improved by replacing intervention steps that exceed the 6d2L/k threshold by any other steps (similarly to the argument in the analysis of Game D). In addition, since Adversary may insert partitions anywhere in the list, they may as well hold oﬀ the interventions until the very end. Finally, since Adversary is allowed to select trivial partitions, they may as well use all 6d2L/k interventions.


So, under the optimal strategy Adversary ﬁrst waits for Fortune to generate a random word for the ﬁrst L − 6d2L/k turns, and then intervenes for each of the last 6d2L/k turns. Note that because d ≤ 1001 k1/2, it follows that 6d2L/k < L.

![image 190](<2020-bukh-longest-common-subsequences-between_images/imageFile190.png>)

Let wFortune be the word generated by Fortune in the ﬁrst L′ def= L − 6d2L/k turns. Note that the length of wFortune might be strictly less than L′ because the trivial partitions contain only d + 1 non-empty parts among k parts. So, wFortune is a uniform random word over the alphabet {0,1,... ,d} of length Binom(L′,(d + 1)/k). Lemma 18(ii) tells us that

E[LNDS(wFortune)] − L′/k 2 L′(d + 1)/k

= 1 + O

![image 191](<2020-bukh-longest-common-subsequences-between_images/imageFile191.png>)

![image 192](<2020-bukh-longest-common-subsequences-between_images/imageFile192.png>)

1 d2/3

+

![image 193](<2020-bukh-longest-common-subsequences-between_images/imageFile193.png>)

d2 + dlog pL′ (pL′)1/2

![image 194](<2020-bukh-longest-common-subsequences-between_images/imageFile194.png>)

L′ log L′ ≥ C,

d k ·

whenever

![image 195](<2020-bukh-longest-common-subsequences-between_images/imageFile195.png>)

![image 196](<2020-bukh-longest-common-subsequences-between_images/imageFile196.png>)

where p = (d + 1)/k. We may drop the condition kd · logL′L′ ≥ C, as it is satisﬁed when L ≥ k3 and d ≤ 1001 k1/2 and k ≥ k0 if we deﬁne k0 def= C + 10 with the constant C given by Lemma 18(ii).

![image 197](<2020-bukh-longest-common-subsequences-between_images/imageFile197.png>)

![image 198](<2020-bukh-longest-common-subsequences-between_images/imageFile198.png>)

![image 199](<2020-bukh-longest-common-subsequences-between_images/imageFile199.png>)

By changing the variable from L′ to L, we may rewrite this more conveniently as

E[LNDS(wFortune)] − L′/k 2 dL/k

= 1 + O

![image 200](<2020-bukh-longest-common-subsequences-between_images/imageFile200.png>)

![image 201](<2020-bukh-longest-common-subsequences-between_images/imageFile201.png>)

1 d2/3

+

![image 202](<2020-bukh-longest-common-subsequences-between_images/imageFile202.png>)

d2 k

log dL/k (L/dk)1/2

+

![image 203](<2020-bukh-longest-common-subsequences-between_images/imageFile203.png>)

![image 204](<2020-bukh-longest-common-subsequences-between_images/imageFile204.png>)

. (17)

The following lemma implies that Adversary’s intervention cannot decrease E[LNDSd −LNDS0].

- Lemma 19. Let w,w′ be any two words over alphabet {0,1,... ,d}. Then for every partition A of {0,1,... ,d} into k (not necessarily nonempty) parts,


EA∼A LNDS(wAw′) ≥ LNDS(ww′) + 1/k.

Proof. Let uu′ be a non-decreasing subsequence in ww′ of length LNDSd(ww′), where u and u′ are subsequences in w and w′ respectively. Suppose ﬁrst that u is non-empty. Let s ∈ {0,1,... ,d} be the last symbol in u, and note that if s ∈ A, then wAw′ contains subsequence usu′, which is of length LNDSd(ww′) + 1. Hence, E LNDSd(wAw′) ≥ LNDSd(ww′) + 1/k in this case. If u is empty, but u′ is non-empty, then we let s to be the ﬁrst symbol of u′, and use the same argument to reach the same conclusion. The remaining case, when both u and u′ are empty, is trivial as well.

![image 205](<2020-bukh-longest-common-subsequences-between_images/imageFile205.png>)

![image 206](<2020-bukh-longest-common-subsequences-between_images/imageFile206.png>)

![image 207](<2020-bukh-longest-common-subsequences-between_images/imageFile207.png>)

![image 208](<2020-bukh-longest-common-subsequences-between_images/imageFile208.png>)

Let Pnlt be the penalty function from Game F. From Proposition 7 and the adversarial game argument it follows that

E[Pd(L) + Pnlt] ≥ inf

E[LNDS(A[0]A[1]··· A[L − 1]) + Pnlt].

S∈Strat(Game F)

Hence, (17) and Lemma 19 together imply that

6d2L/k k

E[Pd(L) + Pnlt] ≥ E[LNDS(wFortune)] +

![image 209](<2020-bukh-longest-common-subsequences-between_images/imageFile209.png>)

1 d2/3

![image 210](<2020-bukh-longest-common-subsequences-between_images/imageFile210.png>)

= L/k + 2 dL/k · 1 + O

![image 211](<2020-bukh-longest-common-subsequences-between_images/imageFile211.png>)

d2 k

log L (L/dk)1/2

+

+

![image 212](<2020-bukh-longest-common-subsequences-between_images/imageFile212.png>)

![image 213](<2020-bukh-longest-common-subsequences-between_images/imageFile213.png>)

.

We next tackle the upper bound on E[Pd(L)]. We will use the following simple fact.

(18)

- Lemma 20. Suppose a word w (which we view as a sequence of symbols) is partitioned into two subsequences u1 and u2. Then LNDS(w) ≤ LNDS(u1) + LNDS(u2).


Proof. The restrictions of a nondecreasing subsequence in w to I1 and I2 are nondecreasing subsequences in u1 and u2, respectively. So, LNDS(w) ≤ LNDS(u1) + LNDS(u2) follows.

![image 214](<2020-bukh-longest-common-subsequences-between_images/imageFile214.png>)

![image 215](<2020-bukh-longest-common-subsequences-between_images/imageFile215.png>)

![image 216](<2020-bukh-longest-common-subsequences-between_images/imageFile216.png>)

![image 217](<2020-bukh-longest-common-subsequences-between_images/imageFile217.png>)

Because in Game F Adversary can select the insertion position only after the already-tampered sets, this reduces our task to analyzing the following Markov game:

- Game G. Game state: Finite word w over alphabet {0,1,... ,d}. Start: The word w is empty. Duration: L turns. Each turn: Adversary chooses a partition A of {0,1,... ,d} into k parts, some of which are possibly


empty. Then Fortune picks a set A ∈ A uniformly among the k sets in A. The elements of A are then appended in descending order to w.

Objective: Adversary aims to maximize E[LNDS(w)].

Thanks to the connection between LNDS and the evolution of P0,P1,... ,Pd from Proposition 7, we see that this game is in fact equivalent to Game A, for which we already gave an upper bound in

Lemma 15. Combining that bound with the upper bound from Lemma 20 we obtain

E[Pd(L) − Pnlt] ≤ sup

E[LNDS(A[0]A[1]··· A[L − 1]) − Pnlt] + d

S∈Strat(Game F)

E[LNDS(A[0]··· A[6d2L/k − 1])] + d

≤ E[LNDS(wFortune)] + sup

S∈Strat(Game G) for 6d2L/k turns

d2 k

log dL/k (L/dk)1/2

1 d2/3

≤ L′/k + 2 dL/k 1 + O

![image 218](<2020-bukh-longest-common-subsequences-between_images/imageFile218.png>)

+

+

![image 219](<2020-bukh-longest-common-subsequences-between_images/imageFile219.png>)

![image 220](<2020-bukh-longest-common-subsequences-between_images/imageFile220.png>)

![image 221](<2020-bukh-longest-common-subsequences-between_images/imageFile221.png>)

6d2L k2

![image 222](<2020-bukh-longest-common-subsequences-between_images/imageFile222.png>)

+ d 2(6d2L/k)/k + 2d

+

![image 223](<2020-bukh-longest-common-subsequences-between_images/imageFile223.png>)

d3/2 k1/2

L k

1 d2/3

log dL/k (L/dk)1/2

![image 224](<2020-bukh-longest-common-subsequences-between_images/imageFile224.png>)

≤

+ 2 dL/k · 1 + O

+

+

.

![image 225](<2020-bukh-longest-common-subsequences-between_images/imageFile225.png>)

![image 226](<2020-bukh-longest-common-subsequences-between_images/imageFile226.png>)

![image 227](<2020-bukh-longest-common-subsequences-between_images/imageFile227.png>)

![image 228](<2020-bukh-longest-common-subsequences-between_images/imageFile228.png>)

Lemma 16 implies that E[Pnlt] ≤ 4d2L2 exp(−L1/2k−3/2). So, from (18) and the preceding bound we deduce that

E[Pd(L)] =

L k

![image 229](<2020-bukh-longest-common-subsequences-between_images/imageFile229.png>)

+ 2 dL/k · 1 + O

![image 230](<2020-bukh-longest-common-subsequences-between_images/imageFile230.png>)

1 d2/3

+

![image 231](<2020-bukh-longest-common-subsequences-between_images/imageFile231.png>)

log dL/k (L/dk)1/2

+

![image 232](<2020-bukh-longest-common-subsequences-between_images/imageFile232.png>)

d3/2 k1/2

+

![image 233](<2020-bukh-longest-common-subsequences-between_images/imageFile233.png>)

d2L3/2 exp(L1/2k−3/2)

![image 234](<2020-bukh-longest-common-subsequences-between_images/imageFile234.png>)

.

Hence Theorem 5 follows since E[P0(L)] = L/k.

# 9 Remarks and open problems

- • We believe that Lemma 15 should hold with C dL/k + d instead of d 2L/k + d. Any upper

![image 235](<2020-bukh-longest-common-subsequences-between_images/imageFile235.png>)

![image 236](<2020-bukh-longest-common-subsequences-between_images/imageFile236.png>)

bound in Lemma 15 that is sublinear in d would imply that limγ′

k = 41 (assuming that constants γ′

![image 237](<2020-bukh-longest-common-subsequences-between_images/imageFile237.png>)

k exist). That is because we can upper bound E[Pd−P0] by smallest of the bound in Theorem 4 and the bound in such improved Lemma 15. That can then be used in an argument similar to that in Section 3.

- • The formalism of Markov games can be generalized. Most notably instead of giving an adversary, for each state xn, a choice of states Rn(xn) ⊂ Ωn+1 where they can take the chain to, we give them a choice of a probability distributions on Ωn+1. Perhaps the most natural case is when the set of allowable probability distributions is a convex set in the space of probability distributions


on Ωn+1. Doing so would eliminate the need for the set I in the deﬁnition of a Markov game. Since we did not need the extra generality, we opted for less abstract presentation.

# References

- [1] Noga Alon and Joel H. Spencer. The probabilistic method. Wiley Series in Discrete Mathematics and Optimization. John Wiley & Sons, Inc., Hoboken, NJ, fourth edition, 2016.
- [2] R. A. Baeza-Yates, R. Gavalda`, G. Navarro, and R. Scheihing. Bounding the expected length of longest common subsequences and forests. Theory Comput. Syst., 32(4):435–452, 1999. https:// users.dcc.uchile.cl/~gnavarro/ps/tocs99.pdf.


- [3] Jinho Baik, Percy Deift, and Kurt Johansson. On the distribution of the length of the longest increasing subsequence of random permutations. J. Amer. Math. Soc., 12(4):1119–1178, 1999. arXiv:math/9810105.
- [4] A. D. Barbour and Peter Hall. On the rate of Poisson convergence. Math. Proc. Cambridge Philos. Soc., 95(3):473–480, 1984.
- [5] Yu. Baryshnikov. GUEs and queues. Probab. Theory Related Fields, 119(2):256–274, 2001. http://www.math.uiuc.edu/~ymb/ps/GaQ.pdf.
- [6] Jean-Christophe Breton and Christian Houdre´. Asymptotics for random Young diagrams when the word length and alphabet size simultaneously grow to inﬁnity. Bernoulli, 16(2):471–492,

2010. arXiv:0812.3672v3.

- [7] Boris Bukh and Christopher Cox. Periodic words, common subsequences and frogs. arXiv:1912.03510, 2019.
- [8] Boris Bukh, Venkatesan Guruswami, and Johan Ha˚ stad. An improved bound on the fraction of correctable deletions. IEEE Trans. Inform. Theory, 63(1):93–103, 2017. arXiv:1507.01719.
- [9] Boris Bukh and Raymond Hogenson. Length of the Longest Common Subsequence between Overlapping Words. SIAM J. Discrete Math., 34(1):721–729, 2020. arXiv:1803.03238.
- [10] R. Bundschuh. High precision simulations of the longest common subsequence problem. The European Physical Journal B — Condensed Matter and Complex Systems, 22(4):533–541, Aug

2001. arXiv:cond-mat/0106326.

- [11] Cle´ment Cannone. A short note on Poisson tail bounds. http://www.cs.columbia. edu/~ccanonne/files/misc/2017-poissonconcentration.pdf. Archived at https://web. archive.org/web/20200604093220/http://www.cs.columbia.edu/~ccanonne/files/misc/ 2017-poissonconcentration.pdf.
- [12] Kuan Cheng, Bernhard Haeupler, Xin Li, Amirbehshad Shahrasbi, and Ke Wu. Synchronization strings: highly eﬃcient deterministic constructions over small alphabets. In Proceedings of the Thirtieth Annual ACM-SIAM Symposium on Discrete Algorithms, pages 2185–2204. SIAM, Philadelphia, PA, 2019. arXiv:1704.00807.
- [13] Kai-Min Chung, Henry Lam, Zhenming Liu, and Michael Mitzenmacher. Chernoﬀ-Hoeﬀding bounds for Markov chains: generalized and simpliﬁed. In 29th International Symposium on Theoretical Aspects of Computer Science, volume 14 of LIPIcs. Leibniz Int. Proc. Inform., pages 124–135. Schloss Dagstuhl. Leibniz-Zent. Inform., Wadern, 2012. arXiv:1201.0559.
- [14] V´acl´v Chv´atal and David Sankoﬀ. Longest common subsequences of two random sequences. J. Appl. Probability, 12:306–315, 1975.
- [15] I. H. Dinwoodie. A probability inequality for the occupation measure of a reversible Markov chain. Ann. Appl. Probab., 5(1):37–43, 1995.


- [16] Ronald L. Graham, Donald E. Knuth, and Oren Patashnik. Concrete mathematics. AddisonWesley Publishing Company, Reading, MA, second edition, 1994. A foundation for computer science.
- [17] Dan Gusﬁeld. Algorithms on strings, trees, and sequences. Cambridge University Press, Cambridge, 1997. Computer science and computational biology.
- [18] Christian Houdre´ and Trevis J. Litherland. On the longest increasing subsequence for ﬁnite and countable alphabets. In High dimensional probability V: the Luminy volume, volume 5 of Inst. Math. Stat. (IMS) Collect., pages 185–212. Inst. Math. Statist., Beachwood, OH, 2009. arXiv:math/0612364.
- [19] Christian Houdre´ and Hua Xu. On the limiting shape of Young diagrams associated with inhomogeneous random words. In High dimensional probability VI, volume 66 of Progr. Probab., pages 277–302. Birkh¨auser/Springer, Basel, 2013. arXiv:0901.4138.
- [20] Kurt Johansson. The longest increasing subsequence in a random permutation and a unitary random matrix model. Math. Res. Lett., 5(1-2):63–82, 1998.
- [21] Kurt Johansson. Discrete orthogonal polynomial ensembles and the Plancherel measure. Ann. of Math. (2), 153(1):259–296, 2001. arXiv:math/9906120.
- [22] Nabil Kahale. Large deviation bounds for Markov chains. Combin. Probab. Comput., 6(4):465– 474, 1997. http://nkahale.free.fr/papers/large-deviation-bounds-for.pdf.
- [23] M. Kiwi and J. Soto. On a speculated relation between Chv´atal-Sankoﬀ constants of several sequences. Combin. Probab. Comput., 18(4):517–532, 2009. arXiv:0810.1066.
- [24] Marcos Kiwi, Martin Loebl, and Jirˇı´ Matousˇek. Expected length of the longest common subsequence for large alphabets. Adv. Math., 197(2):480–498, 2005. arXiv:math/0308234.
- [25] J. Komlo´s, P. Major, and G. Tusn´ady. An approximation of partial sums of independent RV’s and the sample DF. I. Z. Wahrscheinlichkeitstheorie und Verw. Gebiete, 32:111–131, 1975.
- [26] Greg Kuperberg. Random words, quantum statistics, central limits, random matrices. Methods Appl. Anal., 9(1):99–118, 2002. arXiv:math/9909104.
- [27] Michel Ledoux. Deviation inequalities on largest eigenvalues. Summer school “Connections between Probability and Geometric Functional Analysis”, Jerusalem, June 2005. http://www. math.univ-toulouse.fr/~ledoux/Jerusalem.pdf. Archived at https://web.archive.org/ web/20120720141011/http://www.math.univ-toulouse.fr/~ledoux/Jerusalem.pdf.
- [28] David A. Levin and Yuval Peres. Markov chains and mixing times. American Mathematical Society, Providence, RI, 2017. Second edition of [ MR2466937], With contributions by Elizabeth L. Wilmer, With a chapter on “Coupling from the past” by James G. Propp and David B. Wilson.
- [29] Pascal Lezaud. Chernoﬀ-type bound for ﬁnite Markov chains. Ann. Appl. Probab., 8(3):849–867, 1998.


- [30] B. F. Logan and L. A. Shepp. A variational problem for random Young tableaux. Advances in Math., 26(2):206–222, 1977.
- [31] George S. Lueker. Improved bounds on the average length of longest common subsequences. Journal of the ACM, 56(3):1–38, May 2009.
- [32] Dan Romik. The surprising mathematics of longest increasing subsequences, volume 4 of Institute of Mathematical Statistics Textbooks. Cambridge University Press, New York, 2015. Available at https://www.math.ucdavis.edu/~romik/book/.
- [33] David Sankoﬀ and Joseph B. Kruskal, editors. Time warps, string edits, and macromolecules: the theory and practice of sequence comparison. Addison-Wesley Publishing Company, Advanced Book Program, Reading, MA, 1983.
- [34] J. Michael Steele. Probability theory and combinatorial optimization, volume 69 of CBMS-NSF Regional Conference Series in Applied Mathematics. Society for Industrial and Applied Mathematics (SIAM), Philadelphia, PA, 1997. Videos of the lectures are available at https://sms. cam.ac.uk/collection/1189351.
- [35] Craig A. Tracy and Harold Widom. On the distributions of the lengths of the longest monotone subsequences in random words. Probab. Theory Related Fields, 119(3):350–380, 2001. arXiv:math/9904042.
- [36] A. M. Versˇik and S. V. Kerov. Asymptotic behavior of the Plancherel measure of the symmetric group and the limit form of Young tableaux. Dokl. Akad. Nauk SSSR, 233(6):1024–1027, 1977. http://mi.mathnet.ru/dan40430.
- [37] Roy Wagner. Tail estimates for sums of variables sampled by a random walk. Combin. Probab. Comput., 17(2):307–316, 2008. arXiv:math/0608740.


- A Proofs of Propositions 6 and 7 In this appendix, we supply proofs that were omitted in the introduction.


- Proof of Proposition 6. Case w[Pi(L)] = w′[L]: Let u be a common subsequence of w<Pi(L) and


<L that is obtained from w<Pi(L+1) by removing at most i symbols. By appending w′[L] to u we obtain a subsequence of w′

w′

<L+1 that is a witness to the inequality Pi(L + 1) ≥ Pi(L) + 1. As the reverse inequality Pi(L + 1) ≤ Pi(L) + 1 always holds, this shows that Pi(L + 1) = Pi(L) + 1.

Case w[Pi(L)] = w′[L]: Note that we always have Pi(L + 1) ≥ max Pi(L),Pi−1(L + 1) + 1 . We must show the reverse inequality.

Suppose Pi(L + 1) > Pi(L), and so Pi(L + 1) = Pi(L) + 1. Let u˜ be the common subsequence of w′

<L+1 and w<Pi(L+1) obtained from the latter by omitting i symbols. Since w[Pi(L)] = w′[L], the last symbol in u˜ is either diﬀerent from w[Pi(L)] or from w′[L]. In the former case, Pi(L + 1) ≤ Pi−1(L + 1) + 1 holds, whereas in the latter case Pi(L + 1) ≤ Pi(L) holds.

- Proof of Proposition 7. The proof is by induction on L and i. When L = 0, we have Pi(0) = i for all i and the only non-decreasing subsequence of the empty word is empty. Similarly, if i = 0, the claim is trivially true. Suppose now that we wish to prove the claim for the pair (L + 1,i), and that the claim holds for all smaller pairs.


Suppose i ∈ A[L]. In this case, Pi(L + 1) = Pi(L) + 1 according to Proposition 6. On the other hand, we may append i to any non-decreasing subsequence in A[0]··· A[L − 1] using only symbols from {0,1,... ,i}, and so LNDSi(A[0]··· A[L − 1]A[L]) = LNDSi(A[0]··· A[L − 1]A[L]) + 1.

Suppose i ∈/ A[L]. In this case, consider the longest non-decreasing sequence in A[0]··· A[L] that uses only symbols from {0,1,... ,i}. If the sequence contains no i, then LNDSi(A[0]··· A[L]) = LNDSi−1(A[0]··· A[L]) = (Pi−1(L + 1) − i) + 1. If the sequence contains i, then it does not contain any symbols from A[L], in which case LNDSi(A[0]··· A[L]) = LNDSi−1(A[0]··· A[L−1]) = Pi(L)−i. Both cases match the behavior of Pi(L + 1) from Proposition 6.

# B Expected modulus of a simple random walk

Given T ∈ N. Consider a particle doing a simple random walk starting from 1/2 for T steps. Let ∆′ be the ﬁnal position of this particle.

Proposition 21. We have that

 

T T/2

- 1

![image 238](<2020-bukh-longest-common-subsequences-between_images/imageFile238.png>)

- 2


2−T · T +

, if T is even,

E |∆′| =

T − 1 (T − 1)/2



2−T · 2T

, if T is odd.

Proof. Suppose T is even, and write it as T = 2m. Set p def= 2−2m. The binomial theorem tells us that Pr[∆′ = 1/2] = p · 2mm , and that

Pr[∆′ = 1/2 + 2r] = Pr[∆′ = 1/2 − 2r] = p · m 2m+r = p · m 2m−r for r = 1,... ,m. Then

m

2r · 2 · m 2m+r

p−1E |∆′| = 12 · 2mm +

![image 239](<2020-bukh-longest-common-subsequences-between_images/imageFile239.png>)

r=1

2m m+r

= 21 · 2mm + 4 ·

(m + r) · m 2m+r − 4m ·

![image 240](<2020-bukh-longest-common-subsequences-between_images/imageFile240.png>)

r≥1

r≥1

2m m+r

= 21 · 2mm + 4 ·

2m · m 2+mr−−11 − 4m ·

![image 241](<2020-bukh-longest-common-subsequences-between_images/imageFile241.png>)

r≥1

r≥1

= 21 · 2mm + 8m · 21 · 22m−1 − 4m · 12 · 22m − 2mm

![image 242](<2020-bukh-longest-common-subsequences-between_images/imageFile242.png>)

![image 243](<2020-bukh-longest-common-subsequences-between_images/imageFile243.png>)

![image 244](<2020-bukh-longest-common-subsequences-between_images/imageFile244.png>)

= (2m + 12) · 2mm . Hence E |∆′| = 2−T(T + 12) T/ T2 .

![image 245](<2020-bukh-longest-common-subsequences-between_images/imageFile245.png>)

![image 246](<2020-bukh-longest-common-subsequences-between_images/imageFile246.png>)

Suppose T is odd, and write it as T = 2m + 1. Set p def= 2−(2m+1).

The binomial theorem tells us that

Pr[∆′ = 1/2 + 2r − 1] = Pr[∆′ = 1/2 − 2r + 1] = p · 2mm++1r = p · m 2+1m+1−r for r = 1,... ,m + 1. Then

m

(2r − 1) · 2 · 2mm++1r

p−1E |∆′| =

r=1

2m+1 m+r

(m + r) 2mm++1r − (4m + 2) ·

= 4 ·

r≥1

r≥1

(2m + 1) · m 2+mr−−11 − (4m + 2) ·

2m+1 m+r

= 4 ·

r≥1

r≥1

= (8m + 4) · 12 · 22m + 2mm − (4m + 2) · 21 · 22m+1

![image 247](<2020-bukh-longest-common-subsequences-between_images/imageFile247.png>)

![image 248](<2020-bukh-longest-common-subsequences-between_images/imageFile248.png>)

= (4m + 2) 2mm . Hence E |∆′| = 2−T+1T (T T−−1)1/2 .

![image 249](<2020-bukh-longest-common-subsequences-between_images/imageFile249.png>)

![image 250](<2020-bukh-longest-common-subsequences-between_images/imageFile250.png>)

![image 251](<2020-bukh-longest-common-subsequences-between_images/imageFile251.png>)

![image 252](<2020-bukh-longest-common-subsequences-between_images/imageFile252.png>)

# C Behavior of LNDS for growing alphabet

Here, we prove Lemma 18 describing the behavior of E[LNDS(w)] for a random w ∼ [k]n uniformly in k and n. A closely related work is [6], which asserts, as a special case, convergence of LNDS(w) to the Tracy–Widom distribution as both k → ∞ and n → ∞, subject to appropriate growth conditions on k. Sadly, we are unable to use [6] because it does not claim convergence of moments. Also, the proof in [6] has a minor gap — after the application of the one-dimensional strong approximation result of Sakhanenko to several dependent random variables, the resulting Brownian motions will be dependent, but nothing is proved about their dependency. In a private correspondence, the authors of [6] indicated that this gap can be ﬁxed by appealing to results in [18] and [19]. We take this opportunity to present an alternative argument. An advantage of our argument is that we obtain an explicit error term.

Poissionization and de-Poissonization. Denote the Poisson random variable with mean λ by Pois(λ), and deﬁne random variables

Ln def= LNDS(w) − n/k for w ∼ [k]n, Lλ def= LPois(λ).

The variable Lλ serves a standard purpose: it is substantially easier to analyze than Ln. We shall recover ELn from E Lλ via de-Poissonization argument in the following lemma.

- Lemma 22. Suppose s0,s1,... is an increasing sequence satisfying sm − sm−1 ≤ mA with A ≥ 0. Deﬁne sλ def= sPois(λ).


- (i) We have


E sλ− − 4/nA ≤ sn ≤ E sλ+ + 4/nA, whenever n ≥ n0(A), where λ± = n ± (A + 1)√2nlog n.

![image 253](<2020-bukh-longest-common-subsequences-between_images/imageFile253.png>)

- (ii) We also have


|E[sBinom(n,p) − spn]| ≤ pE[ sλ+ − sλ−] + 13/nA, whenever plognn ≥ n0(A). where λ± = pn ± (2A + 3)√2pnlog n.

![image 254](<2020-bukh-longest-common-subsequences-between_images/imageFile254.png>)

![image 255](<2020-bukh-longest-common-subsequences-between_images/imageFile255.png>)

An often-quoted result that is similar to (i) appears in [20, Lemma 2.5]; a slightly more general and streamlined version is reproduced in [32, Lemma 2.31]. The part (ii), as far as we are aware, is new. Without the factor p, it follows easily from (i) and the Chernoﬀ bounds. The extra factor allows for simpler application, and results in a slightly stronger error term in Theorem 5.

Proof. We shall use the tail bound for the Poisson distribution from [11]: Pr |Pois(λ) − λ| ≥ x ≤ 2e−

x2

2(λ+x), x ≥ 0. (19)

![image 256](<2020-bukh-longest-common-subsequences-between_images/imageFile256.png>)

- Proof of (i). Let λ = λ−. Then

E sλ ≤ sn +

m>n

(sm − sm−1)Pr[Pois(λ) ≥ m] ≤ sn + 2

m>n

mAe−

(m−λ)2

![image 257](<2020-bukh-longest-common-subsequences-between_images/imageFile257.png>)

2m . (20)

The ratio between consecutive terms in the sum is (1+1/m)A·exp(−21 + 2m(λm2+1)), which is decreasing in m. Hence, by our choice of λ and the condition, the ratio is at most exp(−2/n1/2) for large n, and so E sλ ≤ sn + 4nA+1/2e−(n−λ)2/2n ≤ sn + 4/nA.

![image 258](<2020-bukh-longest-common-subsequences-between_images/imageFile258.png>)

![image 259](<2020-bukh-longest-common-subsequences-between_images/imageFile259.png>)

Similarly, we let λ = λ+ and compute

E sλ ≥ sn −

m<n

(sm+1 − sm)Pr[Pois(λ) ≤ m] ≥ sn − 2

m<n

mAe−

(λ−m)2 2λ−m

![image 260](<2020-bukh-longest-common-subsequences-between_images/imageFile260.png>)

≥ sn − 2nA+1e−

(λ−n)2 2λ

![image 261](<2020-bukh-longest-common-subsequences-between_images/imageFile261.png>)

≥ sn − 4/nA.

- Proof of (ii). Deﬁne λ def= pn and consider probability distributions Binom(n,p) and Pois(λ). In [4, Theorem 1] it is shown that the total variation distance between the two distributions satisﬁes dTV def= dTV(Binom(n,p),Pois(λ)) ≤ p(1 − exp(−λ)). Consider the diﬀerence


∆(m) def= Pr[Binom(n,p) = m] − Pr[Pois(λ) = m], and note that

E[sBinom(n,p)] = E[ sλ] +

sm∆(m)

m

Let x def= (A + 2)√pnlog n. When m ≤ λ + x and ∆(m) > 0, we upper bound sm by sλ+x. Similarly, when m ≥ λ − x and ∆(m) < 0, we upper bound −sm by −sλ−x. We thus obtain

![image 262](<2020-bukh-longest-common-subsequences-between_images/imageFile262.png>)

sm∆(m) ≤

(sm − sλ+x)∆(m)

sλ+x∆(m) +

m

m:∆(m)>0

m:∆(m)>0 m>λ+x

sλ−x∆(m) −

(sλ−x − sm)∆(m)

+

m:∆(m)<0

m:∆(m)<0 m<λ−x

≤ dTV(sλ+x − sλ−x) + nA+1 Pr[Binom(n,p) > λ + x] + (λ − x)A+1 Pr[Pois(λ) < λ − x].

Applying the asymmetric Chernoﬀ bound from [1, Theorem A.1.11] and (19), we derive

sm∆(m) ≤ p(sλ+x − sλ−x) + nA+1(e−x2/2λ+x3/2λ2 + 2e−x2/2λ)

m

≤ p(sλ+x − sλ−x) + 3/nA. Similarly, using the asymmetric Chernoﬀ bound from [1, Theorem A.1.13], we obtain −

sm∆(m) ≤ dTV(sλ+x − sλ−x) + nA+1 Pr[Binom(n,p) < λ − x] +

mA+1 Pr[Pois(λ) = m]

m

m>λ+x

mA+1e−(m−λ)2/2m.

≤ dTV(sλ+x − sλ−x) + 1/nA +

m>λ+x

This can be bounded as in (20) to obtain −

sm∆(m) ≤ dTV(sλ+x − sλ−x) + 5/nA.

m

By part (i), sλ+x ≤ E sλ+ + 4/nA and sλ−x ≥ E sλ− − 4/nA. To apply the preceding lemma we will need the following fact.

![image 263](<2020-bukh-longest-common-subsequences-between_images/imageFile263.png>)

![image 264](<2020-bukh-longest-common-subsequences-between_images/imageFile264.png>)

![image 265](<2020-bukh-longest-common-subsequences-between_images/imageFile265.png>)

![image 266](<2020-bukh-longest-common-subsequences-between_images/imageFile266.png>)

- Lemma 23. The expectation E[Ln] is an increasing function of n.

Proof. Think of a random word w ∼ [k]n+1 as consisting of the ﬁrst symbol w[0] and the suﬃx w′ of length n. Let A ∈ [k] be the largest symbol such that w′ contains a non-decreasing subsequence of length LNDS(w′) whose ﬁrst symbol is A. Then E[LNDS(w) − LNDS(w′) | w′] = A/k. Since A ≥ 1, it follows that E[Ln+1 − Ln | w′] = (A − 1)/k ≥ 0.

![image 267](<2020-bukh-longest-common-subsequences-between_images/imageFile267.png>)

![image 268](<2020-bukh-longest-common-subsequences-between_images/imageFile268.png>)

![image 269](<2020-bukh-longest-common-subsequences-between_images/imageFile269.png>)

![image 270](<2020-bukh-longest-common-subsequences-between_images/imageFile270.png>)

Geometric view. We will use a geometric representation for Lλ: Let T def= λ/k and imagine k independent Poisson point processes P(1),... ,P(k) on the interval [0,T], each is of constant intensity 1. For each i ∈ [k], replace points of P(i) with the symbol i, and read the symbols left-to-right to obtain a random word of length Pois(λ). Then Lλ is the normalized length of the LNDS in this word.

It is convenient to normalize the processes P(1),... ,P(k) by subtracting their means. We deﬁne

the processes Q(1),... ,Q(k) by Qt(i) def= Pt(i) − t. Note that these processes still have independent increments. Then

Lλ = −

1 k

![image 271](<2020-bukh-longest-common-subsequences-between_images/imageFile271.png>)

k

i=1

Q(Ti) + max 0=t0≤t1≤t2≤··· ···≤tk−1≤tk=T

k

i=1

Q(ti)

i

− Q(ti)

i−1 .

Strong approximation. We shall approximate the processes Q(1),... ,Q(k) by Brownian motions.

- Lemma 24. Let Q be as above. Then there are independent standard Brownian motions B(1),... ,B(k) such that


|Qt(i) − Bt(i)| > x ≤ k exp(−cx), for x ≥ C log T, where c > 0 is a constant independent of k and T.

Pr max

max

i∈[k]

t∈[0,T]

Proof. Consider the values of Qt(i) at integral values of t. For a ﬁxed value of i, the increments Q(1i) − Q(0i),... ,QT(i) − QT(i)−1 are independent copies of Pois(1) − 1. By the Komlo´s–Major–Tusn´ady strong approximation theorem [25] there are constants c0,C0 > 0 that depend only on the distribution Pois(1) − 1, and Brownian motions B(i) such that

Pr[∆(i) ≥ C0 log T + x] ≤ exp(−c0x),

where ∆(i) def= maxm=0,1,...,T |Qm(i) − Bm(i)|. Note that since Q(1),... ,Q(k) are independent, we may choose B’s to be independent as well.

Since the Poisson point process is monotone, for t ∈ [m,m + 1] we have

Qt(i) − Bt(i) ≤ Q(mi)+1 − Bm(i)+1 + (Bm(i)+1 − Bt(i)).

Because, as a function of t, the diﬀerence Bm(i)+1 − Bt(i) is the standard Brownian motion, it follows that

Pr[∃t ∈ [0,T], i ∈ [k] s.t. Qt(i) − Bt(i) ≥ ∆(i) + x] ≤ kT Pr[ max t∈[0,1]

Bt ≥ x] ≤ kT exp(−x2/2).

Since Q(ti) decreases by at most 1 on any interval of length 1, we similarly derive

Pr[∃t ∈ [0,T], i ∈ [k] s.t. Qt(i) − Bt(i) ≤ −∆(i) − x − 1] ≤ kT Pr[ max t∈[0,1]

Bt ≥ x + 1] ≤ kT exp(−x2/2).

Putting these together we obtain Pr[max

|Qt(i) − Bt(i)| ≥ C0 log T + 2x + 1] ≤ k exp(−c0x) + kT exp(−x2/2),

max

i∈[k]

t∈[0,T]

from which the promised inequality follows by appropriate choice of constants c and C. Let

k

k

1 k

− Bt(i)

Bt(i)

BT(i) + max 0=t0≤t1≤t2≤··· ···≤tk−1≤tk=T

R def= −

i−1 .

![image 272](<2020-bukh-longest-common-subsequences-between_images/imageFile272.png>)

i

i=1

i=1

![image 273](<2020-bukh-longest-common-subsequences-between_images/imageFile273.png>)

![image 274](<2020-bukh-longest-common-subsequences-between_images/imageFile274.png>)

![image 275](<2020-bukh-longest-common-subsequences-between_images/imageFile275.png>)

![image 276](<2020-bukh-longest-common-subsequences-between_images/imageFile276.png>)

From Lemma 24 we see that Pr[|R − Lλ| > (2k + 1)x] ≤ k exp(−cx) for x ≥ C log T. In particular,

∞

Pr |R − Lλ| ≥ (2k + 1)x dx

E[R − Lλ] ≤ E |R − Lλ| = (2k + 1)

0

(21)

∞

k exp(−cx)dx = O(k log T + k2).

≤ (2k + 1) C log T +

C log T

The expectation of the ﬁrst term in the deﬁnition of R vanishes. When it comes to the second term, the scaling invariance of the Brownian motion implies that it suﬃces to consider the case T = 1. In that case, the main result of [5] asserts that the maximum in the deﬁnition of R is equal in the law to λkmax, the largest eigenvalue of a k-by-k Gaussian Unitary Ensemble (GUE). Hence,

√

T · E[λkmax] = λ/k · E[λkmax].

![image 277](<2020-bukh-longest-common-subsequences-between_images/imageFile277.png>)

![image 278](<2020-bukh-longest-common-subsequences-between_images/imageFile278.png>)

E[R] =

We have been unable to ﬁnd asymptotic for E[λkmax] in the literature. The most precise result that we are aware of is in [27]: On the bottom of page 27 in [27] it is asserted that

E[λkmax] 2

1 C′k2/3 ≤

1 Ck2/3

√

1 −

k ≤ 1 −

![image 279](<2020-bukh-longest-common-subsequences-between_images/imageFile279.png>)

![image 280](<2020-bukh-longest-common-subsequences-between_images/imageFile280.png>)

![image 281](<2020-bukh-longest-common-subsequences-between_images/imageFile281.png>)

![image 282](<2020-bukh-longest-common-subsequences-between_images/imageFile282.png>)

(22)

for some C,C′ > 0 and all k ≥ 1 (note that [27] uses a non-standard normalization for GUE, which we accounted for when copying the result). The proof of (22) in [27] relies on the estimate (2.11) therein, which in turn relies on the tail bound in Proposition 2.4, but no proof of the proposition is given2. However, on page 51 of [27] another tail bound is given in (5.16). While it is weaker than Proposition 2.4, it is strong enough to imply (2.11), and hence also (22) above.

Putting (21) and (22) together yields

1 C′k2/3

1 −

+ O

![image 283](<2020-bukh-longest-common-subsequences-between_images/imageFile283.png>)

k2 + k log λ λ1/2 ≤

E[ Lλ] 2

1 Ck2/3

√

λ ≤ 1 −

+ O

![image 284](<2020-bukh-longest-common-subsequences-between_images/imageFile284.png>)

![image 285](<2020-bukh-longest-common-subsequences-between_images/imageFile285.png>)

![image 286](<2020-bukh-longest-common-subsequences-between_images/imageFile286.png>)

![image 287](<2020-bukh-longest-common-subsequences-between_images/imageFile287.png>)

k2 + k log λ λ1/2

![image 288](<2020-bukh-longest-common-subsequences-between_images/imageFile288.png>)

.

Combining Lemma 23 and Lemma 22(i) applied with A = 2 to sn = E[Ln], we obtain

1 C′k2/3

1 −

+ O

![image 289](<2020-bukh-longest-common-subsequences-between_images/imageFile289.png>)

k2 + k log n n1/2 ≤

E[Ln] 2√n ≤ 1 −

1 Ck2/3

+ O

![image 290](<2020-bukh-longest-common-subsequences-between_images/imageFile290.png>)

![image 291](<2020-bukh-longest-common-subsequences-between_images/imageFile291.png>)

![image 292](<2020-bukh-longest-common-subsequences-between_images/imageFile292.png>)

![image 293](<2020-bukh-longest-common-subsequences-between_images/imageFile293.png>)

k2 + k log n n1/2

![image 294](<2020-bukh-longest-common-subsequences-between_images/imageFile294.png>)

,

which proves part (i) of Lemma 18. The part (ii) follows similarly with the help of Lemma 22(ii).

![image 295](<2020-bukh-longest-common-subsequences-between_images/imageFile295.png>)

2Proposition 2.4 in [27] is introduced by “. . . there is no doubt that a similar Riemann–Hilbert analysis might be performed anagously [sic] for these examples, and that the statements corresponding to Proposition 2.3 hold true. We may for example guess the following. . . ”

