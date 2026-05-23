---
type: source
kind: paper
title: The proportion of permutations fixing a $k$-set
authors: Ben Green, Mehtaab Sawhney
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2604.28116v1
source_local: ../raw/2026-green-proportion-permutations-fixing-set.pdf
topic: general-knowledge
cites:
---

# arXiv:2604.28116v1[math.CO]30Apr2026

## THE PROPORTION OF PERMUTATIONS FIXING A k-SET

BEN GREEN AND MEHTAAB SAWHNEY

Abstract. Denote by p(k) the limit, as n → ∞, of the probability that a random permutation on a set of size n has an invariant set of size k. We give an asymptotic formula for p(k), showing

that it is asymptotically f({log2 k})k−δ(log k)−3/2 where δ = 1 − 1+logloglog2 2 ≈ 0.086 and f is a smooth, positive, function on R/Z, which we will describe explicitly. The function f satisfies max f minf < 1 + 2 × 10−7 and we conjecture that it is not constant.

Estimating p(k) is a model for the more well-known question which asks for an estimation of M(n), the number of distinct elements in the n-by-n multiplication table. By elaborating on the techniques in this paper, we will give an asymptotic for M(n) in forthcoming work.

Contents

- Part 1. Introduction and setup 2

- 1. Introduction 2
- 2. Heuristic explanation 7
- 3. Changing measure 11
- 4. Outline of the rest of the paper 14
- 5. Sampling using walks 17
- 6. The random variables τ and τ∗ 20
- 7. The random variables ϱ and ϱ∗ 23

Part 2. Background material 31

- 8. Properties of random walks 31
- 9. Bounds on {0,1}-matrices 44
- 10. The function g 45

Part 3. The Poisson paradigm 47

- 11. Approximate ℓ-wise independence 47
- 12. Inclusion–exclusion 61

Part 4. Putting everything together 72

- 13. Expressing p(k) as an average over walks 72
- 14. Decoupling the walks 78
- 15. Proof of the main theorem 80

Part 5. Description of the measures 88

- 16. Description of µ 89
- 17. Description of µ′ 94




Appendices 100

- Appendix A. Almost positive random walks 100
- Appendix B. On results of Denisov, Tarasov and Wachtel 107


- Appendix C. Fourier estimates 111
- Appendix D. Various real-variable inequalities 112
- Appendix E. Bounded Lipschitz distance 113
- Appendix F. Large deviation bounds 114 References 115


## Part 1. Introduction and setup

1. Introduction

- 1.1. Main result and history. The well-known multiplication table problem of Erdős [16, 17] asks for an asymptotic for M(n), the number of elements in the n-by-n multiplication table. In forthcoming work [27] we offer a solution to this problem.


It is well-known that (at least in certain regimes) both the logs of the prime factors of a random integer and the cycle lengths of a random permutation have Poisson behaviour. A consequence of this is an analogy between certain problems about the divisors of typical integers (which the estimation of M(n) can easily be reduced to) and problems about invariant sets of random permutations. In our forthcoming paper we will go into much greater detail on this connection; the introduction to [15] may also be consulted. The objective of the present work is to fully explore the (limiting version of) the permutation analogue of the multiplication table problem, which we now describe.

Denote by Sn the symmetric group of permutations on n letters. Let i(n,k) denote the probability that π ∈ Sn has an invariant set of size k. Let p(k) = limn→∞ i(n,k); this limit exists, as we will recall below, and we have (for example) p(1) = 1 − 1e and p(2) = 1 − 2e−3/2.

Our main interest in this paper will be the estimation of p(k). We believe this is of interest in its own right, and indeed several previous works such as [14, 15, 31] are devoted to the problem. However, our main rationale is that the methods we develop are relatively clean when it comes to estimating p(k), but will adapt to solve the more well-known (but more technical) question of estimating M(n). Large parts of the present paper can be reused almost verbatim for the latter question.

The following is our main theorem. Let

1 + log log 2 log 2

δ = 1 −

(1.1)

be the “Erdős–Ford–Tenenbaum constant”. In this theorem, and throughout the paper, we write log2 k for log to base 2 (not log log k as one occasionally sees in analytic number theory). We also write {x} for the fractional part of a real number x, that is to say 0 ⩽ {x} < 1 and x − {x} ∈ Z; we have {x} = x − ⌊x⌋ where the ⌊x⌋ is the greatest integer less than or equal to x.

Theorem 1.1. There exists f ∈ C∞(R/Z), nowhere zero, such that

p(k) = (1 + o(1))f({log2 k})k−δ(log k)−3/2. The function f can be expressed as c0g ∗ µ ∗ µ′, where g ∈ C∞(R/Z) is the function defined by

g(x) :=

(log 2)D−x(1 − e−2D−x), (1.2)

D∈Z

1

log2−1), and µ,µ′ are two nonzero, positive Borel measures1 on R/Z which we will define in Propositions 1.3 and 1.4 below. We have

c0 = (π2)1/2(log 2)3/2eγ(

maxf minf

maxg ming

⩽

< 1 + 2 · 10−7.

This may be compared with the main result of [15] where, using the methods of Ford [20], it was shown that k−δ(log k)−3/2 ≪ p(k) ≪ k−δ(log k)−3/2. It is a slightly odd historical quirk of the subject that this was only worked out after Ford proved the strictly more difficult corresponding result for M(n). (That this should be possible was anticipated by Diaconis and Soundararajan, as noted in [36].)

We make some remarks on the theorem.

- (1) We presume that f is not the constant function, but we have not been able to prove this. We will show that g(m) ̸= 0 for all m ∈ Z \ {0}, which means that f is constant if and only if µ ∗ µ′ is the uniform measure. Proving this, or obtaining any numerical simulations of µ,µ′, remains an interesting open problem.
- (2) The most interesting feature of Theorem 1.1 is arguably the appearance of a periodic function

of {log2 k}. This sort of behaviour has been seen in related problems before, notably in the work of Balazard, Nicolas, Pomerance and Tenenbaum [6] where they examine the number of n ⩽ X with τ(n) ⩾ log X, where τ is the divisor function. Citing that paper, Brent, Pomerance, Purdum and Webster [9] speculate that the asymptotic for M(n) may have an oscillatory term. For squarefree n, the condition τ(n) ⩾ log X is the same as ω(n) ⩾ log log X/log 2, where ω denotes the number of prime factors. The asymptotic turns out to be dominated by the contribution of n for which ω(n) = log log X/log 2+O(1). Since ω(n) is constrained to be an integer, the fractional part of log log X/log 2 starts to have a significant effect on the distribution. The same phenomenon is at play in the present paper, with ω(n) replaced by the number of cycles of the permutation π of length ⩽ k, and the important contribution being from π with log2 k + O(1) such cycles.

- (3) The almost constant nature of g seemed extremely surprising and mysterious to us at first sight. One explanation for this, as we shall see below, is that the nonzero Fourier coefficients g(m) are given by values of Γ with imaginary part 2πm/log 2, and so are very small when m ̸= 0. Moreover, it transpires that similar phenomena have been observed on a number of occasions before, with the earliest source we are aware of being formula (2.11.2) in Hardy’s explanation [28] of how Ramanujan failed to prove the prime number theorem. Several further related references are given on [19, p 311]. As pointed out to us by Soundararajan,


the exact same function g appears as ψ1∗ in the work of Granville, Sedunova and Sabuncu [26]; although the contexts are somewhat related, this appears to be at least partially coincidental. Finally, we remark that Sean Eberhard pointed out to us that similar functions can arise in rather basic problems, such as the following question on “binomial thinning”. Suppose we start on day 0 with a population of size k. On day i, each remaining member of the population is eliminated with probability 1/2, these events being independent. What is the probability that there is some day on which precisely one person remains? It is not hard to

see that the answer tends to g0({log2 k}) where g0(t) := D∈Z 2D+te−2D+t as k grows.

An immediate corollary of Theorem 1.1 is the following. Corollary 1.2. There is a positive constant C such that we have the asymptotic p(k) = (C + o(1))k−δ(log k)−3/2 as k → ∞ along powers of two.

Although Corollary 1.2 is an immediate consequence of Theorem 1.1, it is in fact a slightly easier result (we shall see the proof at the end of Section 14).

1Positive means that µ(E) ⩾ 0 for any measurable set E.

- 1.2. The ϱ statistics and the measure µ. We turn now to a description of the measure µ in the statement of our main result.

Let u = (ui)∞i=1 be a sequence of real numbers. In our applications, this will either be the arrival times of a rate 1 Poisson process on [0,∞) or a minor variant of this. Then for each positive integer ℓ we define

ϱu(ℓ) := 2uℓ−ℓ

ε∈{0,1}ℓ

1

ℓ

i=1

εi2−ui ∈ [1 − 2−uℓ,1] , (1.3)

where 1(E) denotes the indicator of the event E. Since we will typically have ui ≈ i, roughly speaking one expects ϱu(ℓ) to have size ≍ 1. One should think of the ϱu(ℓ) as describing some sort of “density” of the set of subset sums i∈I 2−ui near 1.

From now on we fix the upper process u = (ui)∞i=1 to be precisely the sequence of arrival times of a rate 1 Poisson process on [0,∞). The following is our main result concerning the measure µ. Here, and throughout the paper, x+ := max(x,0).

- Proposition 1.3. Let c := −log log 2log 2 . For every Lipschitz function ψ ∈ Lip(R/Z) the measure µ satisfies


R/Z

ψ dµ := (2/π)1/2 lim

ℓ→∞

E(ℓ − uℓ)+ϱu(ℓ)cψ(log2 ϱu(ℓ)), (1.4)

where the expectation E is over the random process u, and x+ := max(x,0). We adopt the convention that the integrand is zero when ϱu(ℓ) = 0.

In particular, the Fourier coefficients of µ are given by µ(r) = (2/π)1/2 lim

ℓ→∞

E(ℓ − uℓ)+ϱu(ℓ)c−

2πir log 2

for r ∈ Z. The existence of these limits is part of the proposition. Moreover, the bounded Lipschitz norm ∥µ∥BL is bounded, and µ is not the zero measure.

Remarks. For the definition of the bounded Lipschitz norm ∥ · ∥BL of a Borel measure on R/Z, see Appendix E.

At first sight, it might appear that the limit as ℓ → ∞ in (1.4) diverges. However, this is not

the case, essentially since if uℓ is significantly smaller than ℓ then ϱu(ℓ) is only nonzero with rather small probability; for rigorous instances of this assertion, see Lemma 7.2.

A remark of a different nature is that, despite the existence of the above formulæ for µ, obtaining any interesting numerical or computational data about µ seems a very difficult task. This is because for any sequence u the determination of ϱu(ℓ) is closely related to the subset sum problem and all known algorithms for this have complexity exponential in ℓ, whilst we expect the rate of convergence in (1.4) to be only polynomial.

- 1.3. The τ statistics and the measure µ′. Now let x = (xi)∞i=1 be a sequence of positive integers. Then for each positive integer ℓ we define


ℓ

τx(ℓ) := 2−ℓ#{

i=1

εixi : ε ∈ {0,1}ℓ}. (1.5)

That is, the number of distinct subset sums ℓi=1 εixi, normalised by the number of such sums. Note in particular that 0 ⩽ τx(ℓ) ⩽ 1 for all ℓ. It is also not hard to see that τx(ℓ) is a non-increasing function of ℓ.

Typically we will have xi ≍ 2i and so roughly speaking one expects τx(ℓ) to have size ≍ 1 (that

is, the subset sums ℓi=1 εixi have a good chance of being mostly distinct; for comparison, when xi = 2i exactly, these sums are genuinely distinct).

Define the lower process x = (xi)∞i=1 by ordering the elements of a random (multi-)set of positive integers, where the multiplicity of i is a Pois(1/(ilog 2)) random variable, with these variables being independent. Here is our main result concerning the measure µ′.

- Proposition 1.4. Let c = −log log 2log 2 . For every Lipschitz function ψ ∈ Lip(R/Z), the measure µ′ satisfies


ψ dµ′ := (2/π)1/2 lim

E(log2 xℓ − ℓ)+τx(ℓ)cψ(log2 τx(ℓ)). In particular the Fourier coefficients of µ′ are given by

ℓ→∞

R/Z

2πir

E(log2 xℓ − ℓ)+τx(ℓ)c−

µ′(r) = (2/π)1/2 lim

log2.

ℓ→∞

The existence of these limits is part of the proposition. Moreover, the bounded Lipschitz norm ∥µ′∥BL is bounded, and µ′ is not the zero measure.

- 1.4. Acknowledgments. MS thanks Ivan Corwin, Milind Hegde, Yang Liu, Ashwin Sah, Dominik Schmid and Mark Sellke for helpful and motivating conversations. BG thanks Sean Eberhard, Kevin Ford and Dimitris Koukoulopoulos for discussions on related matters over a number of years prior to this work. Both authors thank Kannan Soundararajan for his immediate and somewhat remarkable observation that the function g appears in [26]. Finally, we are both very grateful to Kevin Ford for numerous comments on a draft of this paper.

BG is supported by Simons Investigator Award 376201. For the purpose of Open Access, the firstnamed author has applied a CC BY public copyright licence to any Author Accepted Manuscript (AAM) version arising from this submission. This research was conducted during the period MS served as a Clay Research Fellow.

- 1.5. Notation. The following pieces of notation will be in force throughout the paper. The letter k will always be as in Theorem 1.1 (that is, we want to compute p(k)). We always write


k = 2n+ξ (1.6) where n ∈ Z and ξ ∈ [0,1). That is, ξ = {log2 k}.

Bold font. There are many random variables in the paper. We have tried to consistently use bold font to denote these, which hopefully helps avoid some confusion, particularly when various conditionings are in place. To avoid conflict we have used blackboard bold for N,Z,R (the naturals, integers and reals) and for P,E (probability and expectation).

Asymptotic notation. We will use the asymptotic notations ≫,≪ and O(·) in the standard manner for analytic number theorists. That is, X = O(Y ) and X ≪ Y both mean that |X| ⩽ CY for some absolute constant C (which may change from line to line). If X,Y are positive quantities then we write X ≍ Y to mean Y ≪ X ≪ Y . We will sometimes use Ω(X) to mean a quantity which is bounded below by cX for some absolute constant c > 0 (which may change from line to line). We will use the o(·) notation only sparingly; o(1) means a quantity which tends to 0 as k → ∞. The notations ≫ and ≪ are informal and mean ‘much greater than’ and ‘much less than’ respectively.

Further notation. We will use the following conventions and further pieces of notation.

- • Write HX = j⩽X 1/j; here X need not necessarily be an integer.
- • 1S(x) and 1x∈S both mean 1 if x ∈ S and 0 otherwise.
- • If N is a positive integer, [N] = {1,...,N}.
- • If f : [N] → R is a function (for some N) then arg min(f) denotes the first q for which f(q) = min1⩽i⩽N f(i).


- • If E1,E2 are two events, P(E1,E2) denotes the probability that both E1 and E2 occur. Occasionally in more complicated expressions we will write P(E1 ∩ E2) for the same thing. We sometimes write ¬E for the complement of the event E.
- • |S| denotes the cardinality of the set S. This notation will also be used for multisets, in which case elements are counted with multiplicity. The notation #{x : conditions on x} denotes the cardinality of the set of x satisfying the specified conditions.
- • Supp(f) denotes the support of the function f, that is to say {x : f(x) ̸= 0}.
- • x+ denotes max(x,0).
- • X =d Pois(λ) means that X is a random variable with the Pois(λ) distribution, that is to say P(X = i) = e−λλi/i! for nonnegative integers i. Occasionally we will abuse notation by writing Pois(λ) to mean a random variable with the Pois(λ) distribution. Most particularly, we will talk about random walks with Pois(1) − 1 steps, which means the increments ξ are distributed as X − 1 with X =d Pois(1). Similarly a walk with 1 − Pois(1) steps has increments ξ′ distributed as 1 − X with X =d Pois(1).


Index of Key Notation. For convenience we collect an index of the most frequently used notation in the paper.

## Notation Brief Description Defined in

k,n,ξ global parameters k = 2n+ξ (1.6) κ small parameter (= 1001 say) in definition of bounded random walk

Definition 4.1

η small parameter (= 1001 say) in definition of positive random walk

Definition 4.2

ε0,ε1 small positive constants, power savings in random walk estimates

Proposition 8.8, Lemma 8.9

W W(x) = xe−x2/21x⩾0 (density of the Rayleigh distribution)

(8.17)

δ Erdős–Ford–Tenenbaum constant (1.1) γ Euler’s constant g (except Sections 11 and 12) specific function

(1.2)

in C∞(R/Z)

g (Sections 11 and 12) Gaussian density function

(11.10)

ϕ specific map from [0,∞) → N with ϕ(x) ≍ 2x

Definition 5.1

ϕ˜ technical variant of ϕ Definition 5.1

Pois(λ) Poisson random variable parameter λ Section 1.3 β random walk with Pois(1) − 1 steps ξi β′ random walk with 1 − Pois(1) steps ξi′ A random multiset with dyadic rate (3.1) u upper process (rate 1 Poisson process) Definition 2.2 x lower process (random lacunary sequence of

Definition 2.2

integers)

## Notation Brief Description Defined in

s auxiliary rate 1 Poisson process Section 5 τx|β′,τx∗|β′ variants of τ functional Section 6 ϱu|β,ϱ∗u|β variants of ϱ functional Section 7

h(m),h′(m) almost positivity probabilities for random walks

(8.1) and (8.2)

Σ(S) set of subset sums of S Definition 2.1

2. Heuristic explanation

The form of our main result is complicated. We offer here a heuristic explanation for the result, which also serves as a rather rough overview of the actual argument. This heuristic makes certain simplifications and should not be taken too literally; a more technical overview may be found in Section 4 below.

Let us first recall from [15] that we can immediately pass from the language of permutations to a formulation in terms of a so-called Poisson random multiset. A multiset S ⊂ N has the usual definition; rS(i) denotes the multiplicity of i in S.

- Definition 2.1. If S is a multiset (finite or infinite), let s1,s2,... be some listing of its elements

(with multiplicity). We define the set Σ(S) of subset sums to consist of all sums i εisi with εi ∈ {0,1} and all but finitely many εi equal to 0.

Remark. Note carefully that we always regard Σ(S) as a set and not a multiset.

Now let A0 ⊂ N denote the random multiset with rA0(i) =d Pois(1/i) for all i ∈ N, with these variables being independent. We then have

p(k) = P(k ∈ Σ(A0)). (2.1) This follows from the fact that a permutation π has an invariant set of size k if and only if it has disjoint cycles of lengths summing to k, together with the theorem [5] that the distribution of the number of cycles of length i, i = 1,...,k, of a random π ∈ SN tends to that of independent Pois(1/i) random variables in the large n limit. We will not mention permutations again, and from now on our focus will be on (2.1).

An observation which in some form goes back to Erdős [17] is that the most important contribution to p(k) comes from instances of A0 with |A0∩[k]| ≈ log2 k, that is to say from sets which are bigger by a factor log 21 than the expected size. We will explain why this is so in Section 3 below.

It is tempting to model the relevant sets A0 by ‘changing measure’ and using Pois(1/(ilog 2)) variables to define a random multiset A1. However, to better capture the large-scale behaviour we use the following variant of this. First we recall the definitions of the upper and lower processes u,x from the introduction.

- Definition 2.2. Define the upper process u = (ui)∞i=1 to be simply the sequence of arrival times of


a rate 1 Poisson process on [0,∞). Define the lower process x = (xi)∞i=1 by ordering the elements of a random (multi-)set of positive integers, where the multiplicity of i is a Pois(1/(ilog 2)) random

variable, with these variables being independent.

Now we define our random multiset A1. Pick some k0 with 1 ≪ k0 ≪ k. For definiteness one could take k0 :=

√

k, although the precise choice is unimportant (k0 does not need to be an integer). The ‘small’ elements of A1 are simply the elements xi of the lower process which are less than or equal to k0, which we write x1 ⩽ x2 ⩽ ··· ⩽ xL′ in order (where L′ is the number of such elements, which

is itself a random variable). The ‘large’ elements of A1 are ⌊k2−ui⌋, where u1 ⩽ u2 ⩽ ... ⩽ uL are the elements of the upper process which are less than log2(k/k0). Again, L is a random variable. We remark that the probability that some i ⩾ k0 lies in this upper portion of A1 equals the probability that some element of u lies in the interval (log 2)−1 log(k/i) − log(1 + 1i ),log(k/i) , which is ilog 21 + O(i−2).

One may compute that this change of measure affects probabilities as follows. If |A| = n + D then we have

1

log2−1)k−δ(log 2)D−ξP(A1 = A), (2.2) where γ is Euler’s constant. (An essentially identical computation to this one is done carefully at the end of Section 3.) Thus we see that the desired quantity p(k) can be understood with a sufficiently accurate understanding of the probabilities P(k ∈ Σ(A1), |A1| = n + D).

P(A0 ∩ [k] = A) ≈ eγ(

The next observation is (in slightly different language) the key advance of Kevin Ford [20], which is to establish that the main contribution is from sets A1 for which roughly speaking we have

log2 xi ⩾ i − O(1) (2.3) and

ui ⩽ i + O(1) (2.4) for all i. Let us briefly explain in rather heuristic terms where this comes from. In what follows we condition to |A1| = n + D with D = O(1); thus

L + L′ = n + D.

For the discussion, we will otherwise ignore the effect of this conditioning on the distribution of the xi and ui variables.

Suppose first that (2.3) is violated, say log2 xq ⩽ q − m for some m (which we think of as “not O(1)”) and some q ⩽ L′. Then, since the xi grow roughly dyadically, one expects Σ(x1,...,xq) to be contained in [0,O(2q−m)], and hence to have size ⪅ 2q−m. It then follows that

|Σ(A1)| ⩽ |Σ(x1,...,xq)| · |Σ(xq+1,...,xL′)| · |Σ(u1,...,uL)| ⪅ 2q−m · 2n+D−q ∼ k2−m. This leads us to expect that

P(k ∈ Σ(A1)) ⪅ 2−m, (2.5) or in other words the contribution from those x for which (2.3) is violated is quite small.

Now suppose that (2.4) is violated in the sense that uq ⩾ q + m for some q ⩽ L. First observe that k ∈ Σ(A1) requires that

L′

L

ε′ixi ⪅ k0 (2.6)

εi⌊k2−ui⌋ =

k −

i=1

i=1

for some εi,ε′i ∈ {0,1}, where the second inequality is what we typically expect since the xi grow dyadically and the largest is xL′ ⩽ k0. Now one expects i⩾q⌊k2−ui⌋ ⪅ k2−q−m, and so (2.6) requires

q−1

εi2−ui ⪅ 2−q−m (2.7)

1 −

i=1

for some ε1,...,εq−1 ∈ {0,1}. There are 2q−1 choices for ε = (εi)qi=1−1, and for each the inequality (2.7) can typically only happen if εi ̸= 0 for some i = O(1), since ui ≈ i. For any such ε, by revealing all variables except ui one sees that the probability of (2.7) is ⪅ 2−q−m. Summing over ε again yields a bound like (2.5).

This concludes our discussion of why the important contributions come from (2.3) and (2.4); as previously remarked, a rigorous version of this analysis and its implications was one of the key advances of Ford [20].

Now we come to the new part of the analysis. The point of departure is that random A1 satisfying the properties (2.3) and (2.4) will in fact (with high probability) robustly satisfy them in the sense that

log2 xi ⩾ i + i1/2−η (2.8) and

ui ⩽ i − i1/2−η (2.9)

for large i. (Here η is a small constant, say η = 1001 .) These statements are closely analogous to the fact that (under mild hypotheses on the increments) a mean zero random walk β(1),β(2),...,β(N)

of length N, conditioned to stay positive, will almost surely have β(i) ⩾ i1/2−η for all large i. (In fact we will make extensive use of the detailed theory of random walks conditioned to stay almost positive in our arguments.)

The conditions (2.8) and (2.9) (or closely related ones) have two important ramifications for us. First, they imply a stability property for the ϱ and τ statistics defined in (1.3) and (1.5); roughly speaking we have

τx(ℓ) ≈ τx(ℓ′) (2.10) for ℓ,ℓ′ ≫ 1 and similarly

ϱu(ℓ) ≈ ϱu(ℓ′). (2.11) Heuristically, the explanation for (2.10) is that the slightly faster-than-2i growth of the xi means that new coincidences ℓi=1 εixi = ℓi=1 ε′ixi become unlikely as ℓ increases. A similar heuristic can be provided for (2.11). We caution that (2.10) and (2.11) should be considered only as heuristics; the actual statements, established in Sections 6 and 7, are more technical.

The second important ramification of (2.8) and (2.9), and in some sense the heart of the paper, is that with conditions such as these in place we are able to make the following heuristic rigorous.

Consider the portion of Σ(A1) coming from the xi, that is to say

L′

ε′ixi : ε′i ∈ {0,1}}. Observe that by definition (1.5) we have

Σsmall(A1) := {

i=1

|Σsmall(A1)| = 2L′τx(L′). (2.12) The event k ∈ Σ(A1) is then precisely the event that there is some ε = (εi)Li=1 such that

L

εi⌊k2−ui⌋ ∈ Σsmall(A1). (2.13)

k −

i=1

Let ψ(k) be some very slowly-growing function. Then almost surely we have max(Σsmall(A1)) ⩽ ψ(k)k0 ⩽ ψ(k)k2−uL, since xL′ ⩽ k0 ⩽ k2−uL and the xi grow roughly as powers of two. That is, the condition (2.13) is contained in the condition

L

εi⌊k2−ui⌋ ∈ [0,ψ(k)k2−uL]. (2.14)

k −

i=1

By the definition (1.3) of ϱ, we expect the number of ε satisfying this weaker condition to be roughly r := ψ(k)2L−uLϱu(L). (Here we are assuming, for the purpose of the heuristic, that (1.3) does not change much if we replace the interval [1 − 2−uℓ,1] with [1 − (j + 1)2−uℓ,1 − j2−uℓ] for j = 1,...,ψ(k) − 1.)

We now adopt the most naïve heuristic, namely that the probability that a given ε satisfying (2.14) also satisfies (2.13) should be

≈ λ := |Σsmall(A1)| ψ(k)k2−uL .

Assuming suitable independence, the natural guess for the probability that (2.13) holds for at least one of the r choices of ε for which (2.14) holds is 1 − (1 − λ)r ≈ 1 − e−λr, that is to say

P(k ∈ Σ(A1)) ≈ 1 − e−λr. (2.15) Note that using (2.12) we have

λr = |Σsmall(A1)|

- 1 k

- 2L+L′τx(L′)ϱu(L).


ψ(k)k2−uL ψ(k)2L−uLϱu(L) = Since L + L′ = n + D and k = 2n+ξ, it follows that

λr = 2D−ξτx(L′)ϱu(L).

Finally, using the invariance properties (2.10) and (2.11), it follows from the above that (heuristically!)

P k ∈ Σ(A1) | |A1| = n + D ≈ 1 − exp −2D−ξτx(ℓ)ϱu(ℓ) , (2.16) where here 1 ≪ ℓ ≪ L,L′ (one should think of ℓ as being ‘fixed but large’ while if k0 =

√

k then we expect L,L′ ∼ 12 log2 k to grow with k).

Now that we have written the key relation (2.16), for the rest of this heuristic discussion we are no longer conditioning on |A1| = n + D.

Now condition to x1 = x1,...,xℓ = xℓ and u1 = u1,...,uℓ = uℓ for fixed choices of x1 ⩽ ... ⩽ xℓ and u1 ⩽ ... ⩽ uℓ. We wish to calculate the probability that |A1| = n + D, or in other words that L + L′ = n + D. In order to do this we will use the following two facts. Here, W(t) := te−t2/21t⩾0 denotes the density function of the Rayleigh distribution.

- Fact 1. Conditioned on u1 = u1,...,uℓ = uℓ with 0 ⩽ u1 ⩽ ··· ⩽ uℓ < ℓ, the probability that

uℓ′ ⩽ ℓ′ for all ℓ′ with ℓ ⩽ ℓ′ ⩽ L and a given value of L is ≈ (2/π)1/2(ℓ − uℓ)N−1W(L√−NN ), where N = ⌊log2(k/k0)⌋.

- Fact 2. Conditioned on x1 = x1,...,xℓ = xℓ with 0 ⩽ x1 ⩽ ··· ⩽ xℓ and log2 xℓ > ℓ, the


probability that log2 xℓ′ ⩾ ℓ′ for all ℓ′ with ℓ ⩽ ℓ′ ⩽ L′ and a given L′ is ≈ (2/π)1/2(log2 xℓ − ℓ)(N′)−1W(N√′−NL′′) where N′ = ⌊log2 k0⌋.

Both of these facts come from the same source, which is the behaviour of random walks conditioned to stay (almost) positive. For Fact 1, there is a natural random walk whose ith step is the number of elements of u in the interval [uℓ + i − 1,uℓ + i], minus 1; the increments of this walk are i.i.d. Pois(1) − 1 variables, and its length T is ≈ log2(k/k0) − uℓ. The conditions uℓ′ ⩽ ℓ′ are then essentially that this random walk stays above −(ℓ − uℓ), and the event that we are interested in is essentially that the walk ends at L − ℓ − T. We use the approximations T ∼ N and L − ℓ − T ∼ L − N. Fact 1 is then a consequence of known results about the distribution of the endpoint of random walk of length N, conditioned to stay above −m. (For precise statements of the relevant statements, which are consequences of work of Denisov, Tarasov and Wachtel [11], see Section 8 and in particular Propositions 8.1 and 8.8). The explanation of Fact 2 is analogous and we omit a detailed discussion.

We wish to sum the probabilities in Facts 1 and 2 over L,L′ such that L + L′ = n + D (where here D = O(1)). Since the W(·) terms vary on a scale of √

N or √

N′, which we assume ≫ 1, this

sum does not essentially depend on D; ignoring minor issues of integer parts, we may thus assume L = N + t and L′ = N′ − t (so L + L′ = N + N′ = log2 k = n + O(1)). The sum is then

2 π

t √

t √

N−1(N′)−1W

(ℓ − uℓ)(log2 xℓ − ℓ)

W

N′ .

N

t

Writing M := N NN+N′′ 1/2 and approximating the sum by an integral, the sum over t is (NN′)−3/2

3/2 ∞ 0

### M2 (NN′)3/2 t∈Z

M2 NN′

t M

t2e−12t2(N1 +N1′) =

2e−21(t/M)2 ≈

x2e−x2/2dx

t∈Z⩾0

⩾0

= (π/2)1/2(N + N′)−3/2 ≈ (π/2)1/2(log2 k)−3/2. (2.17) In summary, conditioned on x1 = x1,...,xℓ = xℓ and u1 = u1,...,uℓ = uℓ we have

P |A1| = n + D ≈ (2/π)1/2(log2 k)−3/2(ℓ − uℓ)(log2 xℓ − ℓ).

We now combine this with (2.16) and undo the conditioning to x1 = x1,...,xℓ = xℓ and u1 = u1,...,uℓ = uℓ. This gives that P k ∈ Σ(A1), |A1| = n + D is approximately

2 π

1/2(log2 k)−3/2Ex,u(log2 xℓ − ℓ)+(ℓ − uℓ)+ 1 − exp −2D−ξτx(ℓ)ϱu(ℓ) . Finally, summing over D using (2.2) gives

≈

p(k) = P(k ∈ Σ(A0)) ≈ f(ξ)k−δ(log k)−3/2, where

π 2

1

log2−1)Ex,u(log2 xℓ − ℓ)+(ℓ − uℓ)+gτx(ℓ)ϱu(ℓ)(ξ), with

)1/2(log 2)3/2eγ(

f(ξ) = (

(log 2)D−ξ(1 − e−λ2D−ξ).

gλ(ξ) :=

D∈Z

Note that gλ(ξ) =

(log 2)D−ξ(1 − e−2D−ξ+log2λ) (2.18)

D∈Z

log log 2

(log 2)D−ξ+log2 λ(1 − e−2D−ξ+log2λ) = λ−

= (log 2)−log2 λ

log2 g(ξ − log2 λ) (2.19)

D∈Z

with g the function in Theorem 1.1 and so we indeed see that f = c0g ∗ µ ∗ µ′ with µ,µ′ defined as in Propositions 1.3 and 1.4 and c0 = (π2)1/2(log 2)3/2eγ(

1

log2−1).

Remark. Properties of uniform order statistics analogous to (2.8) and (2.9) (so-called “strong barrier conditions”) have been exploited in a related context by Schlitt in recent work [35]; see in particular [35, page 5] for some further references.

3. Changing measure

We will give a detailed outline of the rest of the paper in Section 4 below. However, it is expedient to first give a proper treatment of the ‘change of measure’ step (that is, the move from A0 to A1) described at the start of Section 2, since this sits slightly to one side of the rest of the paper.

Rather than working with exactly the random mulitset A1 as described in Section 2, we will instead consider the random multiset A in which

n iHk

rA(i) =d Pois

(3.1)

for i ∈ [k], where Hk = i⩽k 1/i is the harmonic sum. Note here that n/Hk ≈ 1/log 2, so A is very closely related to A1. Observe that

n Hk i⩽k

1 i

A = d Pois

= Pois(n).

The fact that n is an integer is the reason for this particular rescaling; this will enable us to make effective use of embedded random walks, where we can bring into play the existing literature on the distribution of almost positive walks.

In this short section, we accomplish two things. First, we show that only the contribution to

- (2.1) from sets with |A0 ∩ [k]| ≈ log2 k is important. Second, for sets of roughly this critical size, we analyse the change in passing from the random multiset A0 to the reweighted random multiset A. The following is the key result of the section, and the only one we will need in the rest of the paper. Recall that γ is Euler’s constant and δ the Erdős-Ford-Tenenbaum constant (1.1). Proposition 3.1. Write k = 2n+ξ. We have


p(k) = 1 + O

log log k log k

1

log2−1)k−δ

eγ(

(log 2)D−ξP k ∈ Σ(A), |A| = n + D

|D|⩽20 log n

+ O k−δ(log k)−2 .

Proof. The starting point is of course (2.1). We first eliminate the contribution from sets with size not close to log2 k. The key claim is that

P k ∈ Σ(A0) and |A0 ∩ [k]| − n ⩾ 20log n ≪ k−δ(log k)−2. (3.2) A short computation with Stirling’s formula using the fact that |A0 ∩ [k]| =d Pois(Hk) shows that

P |A0 ∩ [k]| − n ⩾ 20log n ≪ k−δ(log k)−2, so it is enough to show

P k ∈ Σ(A0) and |A0 ∩ [k]| ⩽ m ≪ k−δ(log k)−2, (3.3)

where, for brevity, we have written m := n−20log n. Define Asmall0 := A0 ∩[1, 2 logk k) and Alarge0 := A0 ∩ [2 logk k,k]. Then the LHS of (3.3) is bounded above by

P k ∈ Σ(A0) | |Alarge0 | = r, |Asmall0 | = m′ − r · P |Alarge0 | = r, |Asmall0 | = m′ − r ; (3.4)

m′⩽m 1⩽r⩽m′

the key point here is that we do not need to include r = 0 since, if Alarge0 is empty and |A0∩[k]| ⩽ m then max Σ(A0) ∩ [k] ⩽ 2 logmkk < 3k/4, so in particular k ∈/ Σ(A0).

Conditioned on |Alarge0 | = r, we can write Alarge0 = {a1,...,ar}, where the aj are independent

samples from Z ∩ [2 logk k,k] with P(aj = x) proportional to 1/x. (This is the standard relation between the conditioned Poisson and multinomial distributions.) Further conditioning on a fixed

choice Asmall0 of Asmall0 of size m′ − r, we have

r

εjaj + s}. (3.5)

{k ∈ Σ(A0)} =

{k =

ε∈{0,1}r\{0r} s∈Σ(Asmall0 )

j=1

For each ε, select the minimum i with εi ̸= 0, and reveal all aj except for j = i; since the probability mass function of ai is pointwise bounded by O(logkk), we see that P k = rj=1 εjaj + s ≪ logkk.

Therefore, from (3.5) we have

log k k and so, summing over all Asmall0 weighted by P(Asmall0 = Asmall0 ),

P k ∈ Σ(A0) | |Alarge0 | = r, Asmall0 = Asmall0 ≪ 2m′

log k k

P k ∈ Σ(A0) | |Alarge0 | = r, |Asmall0 | = m′ − r ≪ 2m′

. Substituting into (3.4) gives

log k k

2m′P |Alarge0 | = r, |Asmall0 | = m′ − r

P k ∈ Σ(A0) and |A0 ∩ [k]| ⩽ m ≪

m′⩽m 1⩽r⩽m′

e−Hk(2Hk)m′ (m′)!

log k k m′⩽m

log k k m′⩽m

2m′P |A0 ∩ [k]| = m′ =

⩽

.

Using the bounds e−Hk ≪ 1/k and (m′)! ⩾ (m′/e)m′, one may see that this is bounded above by ≪ logk2k m′⩽m(2eHk/m′)m′. Since (C/x)x is increasing on [0,C/e], and since m = (1 + o(1))loglog 2k, this is ≪ (logk)

2

k2 (2eHk/m)m. Noting that (2elog k/m0)m0 = k2−δ, where m0 := log k/log 2, we can rewrite this bound as

(log k)2k−δ ·

m0 m

mem−m0 ·

Hk log k

m · (2log 2)m−m0.

Using (m0/m)mem−m0 ⩽ 1 and (Hk/log k)m = (1 + O(1/log k))m ≪ 1, we see that this is ≪ (log k)2k−δ(2log 2)−20 log logk < k−δ(log k)−2. This completes the proof of the claim (3.2).

From this and (2.1) we evidently have p(k) = P k ∈ Σ(A0) and |A0 ∩ [k]| − n ⩽ 20log n + O k−δ(log k)−2 . Now we change measure and express the probabilities using A as given by the law (3.1). If A is a fixed multiset of elements from [k] (with the multiplicity of i in A being rA(i)) then P(A0 ∩ [k] = A) =

e−1/i(1/i)rA(i) rA(i)!

e−n/Hki(n/(Hki))rA(i) rA(i)!

, P(A = A) =

,

i∈[k]

i∈[k]

and so if |A| = n + D then

Hk n

n+DP(A = A). Using that

P(A0 ∩ [k] = A) = en−Hk

log k log 2 − ξ,

Hk n

1 log k

1 log2 k

n =

= 1 +

(γ + ξ log 2) + O

log 2, it follows that we have the key relation

P(A0 ∩ [k] = A) = 1 + O

1 + |D| log k

1

log2−1)(log 2)D−ξk−δP(A = A).

eγ(

Summing over all sets A with cardinality in the interval [n − 20log n,n + 20log n] (and thus |D| ≪ log log k) and with k ∈ Σ(A), and applying (3.2), the proof of Proposition 3.1 is complete. □

4. Outline of the rest of the paper

We now give an outline of the rest of the paper. Proposition 3.1 has reduced our main task of proving Theorem 1.1 to that of estimating P(k ∈ Σ(A)) (and that |A| has a certain fixed size close to log k log 2), where the random (multi-)set A is defined using (3.1). An important tool for understanding A – and indeed the reason for the particular definition (3.1) – will be the use of random walks.

Roughly, the idea is that an equivalent way to sample A is via the use of two random walks β,β′. The random walk β = (β(i))i∈N is a random walk with Pois(1)−1 steps ξi = β(i)−β(i−1), where we adopt the convention that β(0) = 0 deterministically. Similarly β′ has 1 − Pois(1) steps ξi′.

Only the ξi with i ⩽ ⌈n/2⌉ and the ξi′ with i ⩽ ⌊n/2⌋ will be relevant. The choice of n/2 here is somewhat arbitrary; any pair of cutoffs summing to n and both tending to infinity would do, and our particular choice corresponds to taking k0 ∼

√

k in the heuristic of Section 2.

The precise manner in which this sampling of A is done is a little technical and is described carefully in Section 5 below. Roughly, one should think of 1 + ξi being the number of elements of A of size ∼ k2−i, and 1 − ξi′ the number of elements of A of size ∼ 2i. The precise meaning of ∼ will be clarified in Section 5 but the definitions will be such that we have

|A| =

(1 + ξi) +

i⩽⌈n/2⌉

(1 − ξi′) = n + β(⌈n/2⌉) − β′(⌊n/2⌋). (4.1)

i⩽⌊n/2⌋

Note that 1+ξi,1−ξi′ =d Pois(1), which makes this modelling of A natural. The reason for using two ‘opposite’ random walks (rather than simply Pois(1) random variables) is completely analogous to the modelling of A1 using the upper and lower processes u,x as described in Section 2, and has to do with the fact that we will exploit positivity properties of these walks.

Throughout many of our arguments we will condition to a fixed choice (β,β′) of (the initial segments of) (β,β′). We use the term upper walk to describe any possible instance β of β; this is simply a sequence (β(i))i∈N whose increments ξi := β(i) − β(i − 1) are bounded below by −1. Similarly a lower walk is any sequence (β′(i))i∈N whose increments ξi′ = β′(i)−β′(i−1) are bounded above by 1.

Write (A | β,β′) for the corresponding (random) choice of A. The definition of this object is described carefully in Section 5.3 below, but this outline can be followed without detailed knowledge of that section. By (4.1) we have

#(A | β,β′) = n + β(⌈n/2⌉) − β′(⌊n/2⌋). We therefore have from Proposition 3.1 that

log log k log k

1

log2−1)k−δ

eγ(

(log 2)D−ξ×

p(k) = 1 + O

|D|⩽20 log n

P (β,β′) = (β,β′) P k ∈ Σ(A | β,β′) + O(k−δ(log k)−2). (4.2)

×

β,β′ β(⌈n/2⌉)−β′(⌊n/2⌋)=D

This formula will be the basis for much of our analysis, and in particular the bulk of our paper will be devoted to trying to understand the quantity

P(k ∈ Σ(A | β,β′)). (4.3)

Broadly, our strategy for doing this will follow the initial steps of the heuristic laid out in Section 2. However, by conditioning to fixed β,β′ the actual details look somewhat different.

The analogue of (2.3) and (2.4) is that the main contribution will come from β,β′ which are almost positive in the sense that

β′(i) ⩾ −O(1). (4.4)

min min

β(i), min

i⩽⌈n/2⌉

i⩽⌊n/2⌋

The main point of departure of the paper will then be the fact that most such walks satisfy β(i),β′(i) ⩾ i1/2−1001 for large i, which is the appropriate analogue of (2.8) and (2.9), as well as some weak boundedness properties on their increments. We give the appropriate technical definitions now, since they will feature throughout the paper. In the following definitions κ and η are fixed small positive constants, global to the paper. We can take κ = η = 1001 , but it makes the exposition clearer to keep these constants unspecified (and separate).

- Definition 4.1. Let R ⩾ 1 be a parameter and let L ∈ N. Let β be a walk (upper or lower) with increments ξi = β(i) − β(i − 1). Then we say that β is R-bounded to length L if |ξi| ⩽ Riκ for

- i = 1,...,L.


- Definition 4.2. Let T ⩾ 0 be a parameter and let L ∈ N. Let β be a walk (upper or lower) with


increments ξi = β(i) − β(i − 1). Then we say that β is T-positive to length L if −T + ℓ1/2−η ⩽ β(ℓ) ⩽ T + ℓ1/2+η for ℓ = 1,...,L.

Continuing to follow the heuristic in Section 2, the next task is to define appropriate analogues of the τ and ϱ statistics. These will be called τx∗|β′(ℓ) and ϱ∗u|β(ℓ) respectively, where ℓ is a positive integer parameter. They are defined, and their key properties explored, in Section 6 and Section 7 respectively. In particular, we will show that if β,β′ are appropriately bounded and positive then these statistics have good convergence properties as ℓ → ∞, statements which correspond to the heuristic assertions (2.10) and (2.11). The precise statements here are Lemma 6.4 and Lemma 7.3.

Part 2 of the paper is an interlude consisting of three sections, whose purpose is to develop various background material. These three sections may be read independently of each other and the rest of the paper.

- Section 8 contains material on almost positive random walks, in particular concerning bound-

edness and positivity properties of such walks. Rigorous statements to the effect that most almost positive walks are appropriately bounded (resp. positive) may be found in Lemma 8.12 and Lemma 8.15 respectively. Section 8 also introduces the technical concept of a jump step. This is a single time t at which the walk β has a large increment, followed by suitable boundedness and positivity properties; the definition is Definition 8.17. Almost positive walks generically have a jump step in appropriate ranges (see Lemma 8.19).

- Section 9 assembles various bounds for {0,1}-matrices satisfying linear-algebraic conditions, and


finally Section 10 gives the basic properties of the function g featuring in our main result (see (1.2)).

Part 3 of the paper, consisting of two sections Sections 11 and 12, is the beating heart of the paper. This is the portion of the paper where the analysis corresponding to (2.12) to (2.16) in our heuristic overview is carried out rigorously. In particular, the phrase ‘assuming suitable independence’ leading up to (2.15) is justified in Section 11 by a (lengthy) local limit theorem analysis; the main result is Lemma 11.2. Here, the existence of a jump step t is used crucially in order to characterise the relevant distributions as Gaussians.

The analysis is continued in Section 12, where the heuristic (2.15) (suitably rephrased in the random walk formalism) is justified via an inclusion–exclusion argument. The apparent dependence on the location of the jump step t is shown to be illusory, and the main result of the section is Proposition 12.1, which is a rigorous version of (2.16). Roughly speaking it provides the desired

expression for (4.3), namely that under suitable conditions we have

P k ∈ Σ(A | β,β′) ≈ 1 − Eexp − 2D−ξϱ∗u|β(L)τx∗|β′(L) , (4.5)

where here ξ = {log2 k}, D = β(⌈n/2⌉) − β′(⌊n/2⌋) and L is an appropriate large parameter. This should be compared with (2.16).

Part 4 of the paper contains the main synthesis, substituting (4.5) (or rather the more technical Proposition 12.1) into Proposition 3.1 in order to prove the weak form of Theorem 1.1 in which the measures µ,µ′ are shown to exist, but are not yet described explicitly. The first task here, accomplished in Section 13, is to reduce to the case where (essentially) D = O(1) and (4.4) holds. Here, with an eye to applying the main results from Part 3, one must additionally restrict to walks which are suitably bounded, positive, and have a jump step.

Section 14 then contains the main analysis, which is parallel to the leveraging of Facts 1 and 2 in our heuristic discussion. The point here is to evaluate the probability that two walks β,β′ of lengths ⌈n/2⌉,⌊n/2⌋ are almost positive and satisfy β(⌈n/2⌉) − β′(⌊n/2⌋) = D. This is done by using a suitable local limit theorem, which states that the endpoints of the two almost positive walks, appropriately scaled, each have a Rayleigh distribution. The result we apply follows from work of Denisov, Tarasov and Wachtel [11], though we will give our own self-contained treatment. The endpoints of the two walks may then be coupled via a fairly straightforward analysis very similar to (2.17).

Throughout the above argument, the walks β,β′ under consideration are bounded below by −M, for some parameter M. By the end of Section 14 we have established an approximate form of Theorem 1.1 in which “f” is of the form g ∗µM ∗µ′M +O(e−cM) for certain Borel measures µM,µ′M on R/Z. To conclude the proof of Theorem 1.1 (and, in particular, to show that f actually exists) we must show appropriate convergence of µM,µ′M to nonzero limit measures µ,µ′ as M → ∞. This task, which is rather delicate, is accomplished in Section 15. It makes considerable further use of the results from Sections 6 to 8.

The final part of the main paper, Part 5, gives the explicit characterisations of the measures µ,µ′ as detailed in Proposition 1.3 and Proposition 1.4 respectively. The proofs occupy Sections 16 and 17 respectively. These involve a translation from the formalism of random walks β,β′ to the language of sequences u,x as in the statements of Propositions 1.3 and 1.4 (and the heuristic sketch). A surprising amount of care is required to carry this out correctly. A key technical issue is that when defining the measures µ and µ′ we have not specified that the corresponding walks are “almost positive” and one needs to prove that the contribution from remaining paths is essentially negligible.

There are six appendices. Appendix A collects various facts about random walks and a basic estimate from renewal theory. Appendix B then gives a self-contained account of a version of the local limit theorem of Denisov, Tarasov and Wachtel which is sufficient for our purposes. Appendix C pulls together some Fourier estimates of fairly standard type. Appendix D gives assorted realvariable inequalities whose proofs would have diverted attention to too great an extent if given in the main text. Appendix E gives the basic properties of the so-called bounded Lipschitz norm on Borel measures, which we use in Section 15 to study the convergence of the measures µM,µ′M, and again in Sections 16 and 17 when characterising µ,µ′. Finally, Appendix F collects some standard large deviation estimates.

### 5. Sampling using walks In this section we give the details of how the random (multi-)set A defined by rA(i) =d Pois iH n

k

(that is, as in (3.1)) may be sampled via a pair of random walks β,β′.

- As in the previous section, and for the rest of the paper, β denotes a random walk with Pois(1)−1

steps ξi = β(i) − β(i − 1), and β′ has 1 − Pois(1) steps ξi′ = β′(i) − β′(i − 1). By convention, β(0) = β′(0) = 0. The walks β,β′ are independent.

- At the same time we will show how to sample the upper and lower processes (see Definition 2.2)


u,x in a similar manner. More precisely we will explain how to couple them to β,β′ respectively.

- 5.1. The upper and lower processes. To couple the upper process u to β, we first sample β

and then, for each i, sample 1 + ξi uniform random elements from (i − 1,i] and order them to create u ∩ (i − 1,i]. It is a standard fact that u is indeed a rate 1 Poisson process. Observe that β(i) = #(u ∩ [0,i]) − i.

Handling the lower process is a little more involved. We begin by associating to β′ an auxiliary

rate 1 Poisson process s by first sampling β′, then for each i sampling 1 − ξi′ uniform random elements from (i−1,i] and ordering them to create s∩(i−1,i]. Again, s is a rate 1 Poisson process,

and now β′(i) = i − #(s ∩ [0,i]).

We then introduce the following pair of closely related maps. Here, HN denotes the harmonic sum and by convention H0 = 0.

- Definition 5.1. Define maps ϕ,ϕ˜ : [0,∞) → N as follows. ϕ(0) = ϕ˜(0) = 1, and if x > 0 then ϕ˜


is the unique map so that x ∈ (Hn

k

Hϕ˜(x)−1, Hn

k

Hϕ˜(x)]. ϕ : [0,∞) → N is the unique map defined by x ∈ (log 21 Hϕ(x)−1, log 21 Hϕ(x)].

We will use ϕ now, and ϕ˜ will be used later when discussing how to sample A. For orientation, we note that ϕ(x),ϕ˜(x) ≍ 2x, and also that ϕ˜ depends on k, but ϕ is ‘universal’. For a detailed proof, see Lemma 5.3 below.

We now couple the lower process x (Definition 2.2) to β′ as follows. First sample β′, then associate the auxiliary process s. Define x = ϕ(s). We observe that, unravelling the definitions,

rx(i) = s ∩

1 log 2

(Hi−1,Hi] = d Pois(1/(ilog 2)).

Thus x indeed has the required distribution of the lower process.

- 5.2. Sampling A. We now turn to the discussion of sampling A (the random multiset defined by


- (3.1)) via the random walks β,β′. Let u be the upper process coupled to β as above, and let s be the auxiliary rate 1 Poisson process coupled to β′, again as described above. Now set


A = ϕ˜ s ∩ [0,⌊n/2⌋] ∪ ϕ˜ n − (u ∩ [0,⌈n/2⌉]) .

That is, we use (β(i))i⩽⌈n/2⌉ to describe the large elements of A, and (β′(i))i⩽⌊n/2⌋ to describe the small elements. Observe that [0,⌊n/2⌋] ∪ (n − [0,⌈n/2⌉]) = [0,n] and so the distribution of A is exactly that of ϕ˜(p ∩ [0,n]), where p is a Poisson process of rate 1. Therefore we have

n Hk

n Hki

(Hi−1,Hi] = d Pois

rA(i) = rϕ˜(p∩[0,n])(i) = p ∩

for i = 1,...,k, and so this A indeed coincides with the random multiset defined by (3.1).

### 5.3. Conditioning to fixed walks. We recall in a formal definition the notions of upper and lower walk.

- Definition 5.2. An upper walk of length N is simply a sequence (β(i))Ni=1 where the increments ξi := β(i)−β(i−1) are integers satisfying ξi ⩾ −1 for all i. A lower walk of length N′ is a sequence


(β′(i))Ni=1′ where the increments ξi′ := β′(i) − β′(i − 1) are integers satisfing ξi′ ⩽ 1 for all i. By convention we set β(0) = β′(0) = 0.

For much of the analysis we will condition to the event that (β(i))i⩽⌈n/2⌉ = (β(i))i⩽⌈n/2⌉ and that (β′(i))i⩽⌊n/2⌋ = (β′(i))i⩽⌊n/2⌋ for some pair of upper- and lower walks β,β′, which we will always take to have lengths ⌈n/2⌉, ⌊n/2⌋ respectively. It is convenient to write (β,β′) = (β,β′) for this event.

We now consider the upper and lower processes u,x and random multiset A conditioned to fixed walks. We take the opportunity to spell out these definitions and at the same time specify notation for listing their elements.

Conditioned upper process. The conditioned upper process (u | β = β), which we write (u | β) for brevity, is obtained by sampling, for each i ⩽ ⌈n/2⌉, 1 + ξi uniform random elements from (i−1,i], and ordering them. (We remark that we will never need to discuss any values of u outside the interval [0,⌈n/2⌉], so we happily ignore the slight inconsistency of notation here.) We write the elements of (u | β) as (ui,j)i⩽⌈n/2⌉;j∈[1+ξi], but leave these randomly ordered on each (i − 1,i]. When this notation is used, the underlying β will be clear from context and so we do not indicate an explicit dependence. Thus ui,j is uniform on (i − 1,i], and these variables are independent for j = 1,2,...,1 + ξi.

Conditioned lower process. To describe (x | β′) = (x | β′ = β′) we first consider the conditioned

auxiliary Poisson process (s | β′). This is obtained by sampling 1 − ξi′ uniform random elements from (i − 1,i], i ⩽ ⌊n/2⌋. We write its elements as (si,j)i⩽⌊n/2⌋,j∈[1−ξ′

i], again randomly ordered on (i−1,i]. Thus si,j is uniform on (i−1,i], and these variables are independent for j = 1,2,...,1−ξi′. We have, by definition, (x | β′) = ϕ(s | β′). We write xi,j = ϕ(si,j), i ⩽ ⌊n/2⌋ and j ∈ [1 − ξi′] for the elements of (x | β′).

Conditioned random multiset. Now we define (A | β,β′) for A conditioned to (β,β′) = (β,β′). First of all we introduce notation which unifies the ⌈n/2⌉ steps of β and the ⌊n/2⌋ steps of β′ which are relevant to the construction. Thus we define non-negative integers b1,...,bn by

bi := 1 − ξi′ (i = 1,...,⌊n/2⌋) and bn+1−i := 1 + ξi (i = 1,...,⌈n/2⌉). (5.1)

bi should be thought of as roughly the number of elements of (A | β,β′) which are of size ≍ 2i, as we will see in Lemma 5.5 below.

The elements of (A | β,β′) may be listed as (ai,j)i∈[n],j∈[bi] with

ϕ ˜(si,j) 1 ⩽ i ⩽ ⌊n/2⌋; ϕ˜(n − un+1−i,j) ⌊n/2⌋ < i ⩽ n.

(5.2)

ai,j =

Note in particular that we have

n

#(A | β,β′) =

bi. (5.3)

i=1

### 5.4. Size and anticoncentration estimates. We will make extensive use of Lemma 5.5 which gives the approximate distribution of the ai,j. In the proof of this we will require some simple properties of the function ϕ˜. We give these, together with essentially identical properties of ϕ, in the following lemma.

- Lemma 5.3. Uniformly for x ∈ [0,n] we have

log2 ϕ(x),log2 ϕ˜(x) = x + O(1). (5.4)

Thus ϕ(x),ϕ˜(x) ≍ 2x. Proof. We give the proofs for ϕ˜. Recall throughout that n = ⌊log2 k⌋. We have Hn

k

= log 21 +O(n1) and Hϕ˜(x) = log ϕ˜(x) + O(1). Thus from x ⩽ Hn

k

Hϕ˜(x) we obtain x ⩽ (log 21 + O(n1))(log ϕ˜(x) + O(1)) = log2 ϕ˜(x)+O(1), or in other words the RHS of (5.4) is at most the LHS. Here, we used that ϕ˜(x) ⩽ k for x ⩽ n in order to bound the cross term O(n1)log ϕ˜(x) by an absolute constant.

In a very similar manner one may obtain an inequality in the opposite direction as well, and putting these together gives (5.4).

The proof for ϕ is extremely similar (and slightly simpler). This estimate in fact holds for all x. □

Before turning to Lemma 5.5 itself, we first give distributional estimates for the components xi,j of the conditioned lower process (x | β′ = β′).

- Lemma 5.4. We have xi,j ≍ 2i (5.5)

deterministically and

sup

t∈Z

P(xi,j = t) ≪ 2−i. (5.6)

Proof. For both parts we use that xi,j = ϕ(si,j). Item (5.5) is immediate from Lemma 5.3 and the fact that si,j ∈ (i − 1,i]. For (5.6), observe that P(ϕ(si,j) = t) is the probability that a uniform random variable on (i−1,i] lies in (log 21 Ht−1, log 21 Ht], which is an interval of length 1/tlog 2. For this interval to intersect (i−1,i] we must (since ϕ is nondecreasing) have t ⩾ ϕ(i−1), and so the desired probability is at most 1/ϕ(i − 1)log 2. The stated bound (5.6) then follows using Lemma 5.3. □

Now we give the key estimate on the ai,j, the elements of the conditioned set (A | β,β′).

- Lemma 5.5. Deterministically we have ai,j ≍ 2i. (5.7)


We also have the anticoncentration estimate sup

P(ai,j = x) ≪ 2−i. (5.8) Here, the implied constants are absolute (and, in particular, do not depend on k). Proof. Item (5.7) is immediate from Lemma 5.3 and (5.2) and the fact that si,j,ui,j = i + O(1).

x∈Z

For (5.8), suppose first that ⌊n/2⌋ < i ⩽ n. Observe that

P(ai,j = x) = P(ϕ˜(n − un+1−i,j) = x) = P(n − un+1−i,j ∈ I) where I := (Hn

Hx]. Now un+1−i,j is uniformly distributed on (n−i,n+1−i], so it follows that

Hx−1, Hn

k

k

n Hkx ≪

1 x

P(ai,j = x) ⩽ |I| =

.

Since ai,j is deterministically ≍ 2i, the result follows. To proof in the case i ⩽ ⌊n/2⌋ is very similar and left to the reader. □

- 5.5. Coupling top and bottom to universals. The material in the following subsection will not be required until the end of Section 12. The idea is to couple A, whose definition is quite heavily dependent on k, to the ‘universal’ upper and lower processes u,x. Essentially this consists


of relating A to the set A1 which featured in our heuristic discussion. We first handle the large elements of A.

- Lemma 5.6. Let β,β′ be upper and lower walks, and consider the conditioned upper process (u | β) and the conditioned random multiset (A | β,β′). Let i satisfy ⌊n/2⌋ < i ⩽ n. Then |k1ai,j − 2−un+1−i,j| ≪ 2i−n(n + 1 − i)/n deterministically.

Proof. By (5.2) we have ai,j = ϕ˜(n−un+1−i,j). From Definition 5.1, this implies that n−un+1−i,j ∈ (Hn

k

Hai,j−1, Hn

k

Hai,j]. Since Ht,Ht−1 = log t + γ + O(1t) uniformly for t ⩾ 2, it follows that n − un+1−i,j =

n Hk

log ai,j + γ + O(2−i) .

Multiplying by Hnk and using Hk = log k + γ + O(k1), Hnk = log 2 + O(n1) and un+1−i,j ⩽ n + 1 − i, this implies that

log k − un+1−i,j log 2 = log ai,j + O

n + 1 − i n

.

That is, writing x := k1ai,j and y := 2−un+i−1,j, we have |log x − log y| ≪ n+1n−i. The desired result then follows using the inequality |x − y| ⩽ max(x,y)|log x − log y| (valid for all real x,y ∈ (0,1])

and the fact that x,y ≍ 2i−n. □ Now we turn to the small elements of A.

- Lemma 5.7. Let β,β′ be upper and lower walks, and consider the conditioned lower process (x | β), with elements xi,j, and the conditioned random multiset (A | β,β′), with elements ai,j. Then, uniformly for i ⩽ ⌊n/2⌋, we have P(xi,j ̸= ai,j) ≪ i/n.


i] be the auxiliary process introduced above. Thus xi,j = ϕ(si,j) and ai,j = ϕ˜(si,j). Thus we must bound P(ϕ(si,j) ̸= ϕ˜(si,j)); that is, it suffices to prove that

Proof. Let (s | β′) = (si,j)i⩽⌊n/2⌋,j∈[1−ξ′

P(ϕ˜(si,j) = x) − P(ϕ(si,j) = x) ≪ i/n.

x

From the definitions (Definition 5.1) of ϕ,ϕ˜, the task is to show

1 log 2

1 log 2

n Hk

n Hk

P si,j ∈ (

Hx] − P si,j ∈ (

Hx] ≪ i/n.

Hx−1,

Hx−1,

x

Recall that here si,j is uniform on (i − 1,i]. In particular, both probabilities vanish unless x ≍ 2i. For each x, the difference in probabilities is the length of the symmetric difference between the two intervals, and therefore the above expression is bounded by

1 n

n Hk −

1 log 2

i n

Hx−1 + Hx ≪

Hx−1 + Hx ≪

,

x≍2i

x≍2i

as required. □ 6. The random variables τ and τ∗

In this section we develop the basic properties of the τ-statistics as defined in (1.5), which feature prominently in the measure µ′ (see Proposition 1.4).

Let β′ be a lower walk with increments ξi′ = β′(i) − β′(i − 1). In this section we suppose that β′ is infinite (rather than of length ⌊n/2⌋) although we will only be dealing with finite segments of β′.

Recall the definition of the conditioned lower process (x | β′) and its elements xi,j, j ∈ [1 − ξi′], as described in Section 5.3. We define two statistics related to τ, as defined in (1.5).

- Definition 6.1. Let ℓ ∈ N. We define


τx∗|β′(ℓ) := 2β′(ℓ)−ℓ#

εi,jxi,j : εi,j ∈ {0,1} . (6.1)

i⩽ℓ;j∈[1−ξi′]

By convention we set τx|β′(0) = τx∗|β′(0) := 1. Suppose that lim

(j − β′(j)) = ∞. (6.2) Then we also define

j→∞

τx|β′(ℓ) := 2−ℓ#

εi,jxi,j : εi,j ∈ {0,1} , (6.3)

i,j

where the (i,j)-sum is taken over the ℓ smallest xi,js.

Remarks. The assumption (6.2) guarantees that τx|β′(ℓ) is defined for all ℓ. We note that the definition of τx|β′ is compatible with the definition (1.5), being the τ statistic defined there applied to the conditioned sequence (x | β′). We think of τx∗|β′(ℓ) as rather analogous to τx|β′(ℓ), but ‘adapted to the random walk’; instead of working with the first ℓ elements of (x | β′), we work with the elements up to ℓ.

i] are precisely the initial ℓ − β′(ℓ) elements of the conditioned lower process (x | β′). Therefore we have

Observe that the ℓ − β′(ℓ) elements (xi,j)i⩽ℓ;j∈[1−ξ′

τx∗|β′(ℓ) = τx|β′(ℓ − β′(ℓ)). (6.4) It is straightforward to check the monotonicity properties

1 = τx|β′(0) ⩾ ... ⩾ τx|β′(ℓ) ⩾ τx|β′(ℓ + 1) ⩾ ... ⩾ 0 (6.5) and

1 = τx∗|β′(0) ⩾ ... ⩾ τx∗|β′(ℓ) ⩾ τx∗|β′(ℓ + 1) ⩾ ... ⩾ 0. (6.6)

The main aim in this section is to develop some basic properties of the variables τx|β′(ℓ) and τx∗|β′(ℓ), particularly the latter. The first statement says that, under reasonable conditions, τx∗|β′(ℓ) ⪅ 2−m if β′ attains the value −m. This should be considered a rigorous version of the heuristics just before (2.5).

Recall from Definition 4.1 the notion of a walk being R-bounded to some length L.

- Lemma 6.2. Let m ⩾ 0 be an integer. Suppose that β′ is a lower walk and that β′(q) = −m for some q with 0 ⩽ q ⩽ ℓ. Suppose that β′ is R-bounded to length ℓ. Then


τx∗|β′(ℓ) ≪ R(1 + q)κ2−m. (6.7)

Proof. If q = 0 then m = 0 and the result is trivial from (6.6). Suppose, then, that q ⩾ 1. By the monotonicity property (6.6) it suffices to handle the case ℓ = q. By (5.5) we have

2i|1 − ξi′| ≪ R2ℓℓκ,

### εi,jxi,j ≪

i⩽ℓ

i⩽ℓ;j∈[1−ξi′]

where in the last step we used the R-boundedness of β′. In particular the number of distinct elements

i⩽ℓ;j∈[1−ξi′] εi,jxi,j is ≪ R2ℓℓκ. From the definition (6.1), it follows that τx∗|β′(ℓ) ⩽ 2β′(ℓ)Rℓκ = 2−mRℓκ, which implies (6.7). □

We will also require the following variant for the unstarred τx|β′ quantities.

- Corollary 6.3. Let m ⩾ 0 and ℓ ⩾ 1 be integers. Suppose that (6.2) holds, and denote by ℓ′ the smallest integer such that ℓ′ − β′(ℓ′) ⩾ ℓ. Suppose that β′(q) = −m for some q with 0 ⩽ q ⩽ ℓ′ − 1, and that β′ is R-bounded to length ℓ′ − 1. Then


τx|β′(ℓ) ≪ R(1 + q)κ2−m. Proof. By the monotonicity of the τx|β′(ℓ) in ℓ, the definition of ℓ′, and (6.4), we have

τx|β′(ℓ) ⩽ τx|β′(ℓ′ − 1 − β′(ℓ′ − 1)) = τx∗|β′(ℓ′ − 1). The result now follows immediately from Lemma 6.2, replacing ℓ by ℓ′ − 1 in that lemma. □

The next fact is more difficult. It allows us to establish rapid convergence of τx∗|β′(ℓ) to the limit as ℓ → ∞ under a suitable condition on the lower walk β′ (that β′ is suitably positive in the sense of Definition 4.2).

- Lemma 6.4. Let β′ be a lower walk. Then uniformly for non-negative integers ℓ we have E τx∗|β′(ℓ) − τx∗|β′(ℓ + 1) ≪ 2−β′(ℓ+1). (6.8)


Here, the expectation is over random choices of (x | β′) = (xi,j)i;j∈[1−ξ′

i]. Proof. For an integer ℓ ⩾ 1, denote ε⩽ℓ = (εi,j)i⩽ℓ,j∈[1−ξ′

i] and for t ∈ Z write rx,ℓ(t) :=

1

εi,jxi,j = t .

i⩽ℓ,j∈[1−ξi′]

ε⩽ℓ

(Thus rx,ℓ(t) is a random variable.) Define also rx,0(t) = 1t=0. Thus by (6.1) we have, for all ℓ ⩾ 0, that

τx∗|β′(ℓ) = 2β′(ℓ)−ℓ Supp(rx,ℓ) , (6.9) where Supp denotes support. Define

1−ξℓ′+1

1Supp(rx,ℓ) t −

fx,ℓ(t) :=

εℓ+1,jxℓ+1,j ,

εℓ+1

j=1

where εℓ+1 denotes (εℓ+1,j)j∈[1−ξ′

ℓ+1]. Since

1−ξℓ′+1

rx,ℓ t −

rx,ℓ+1(t) =

εℓ+1,jxℓ+1,j ,

εℓ+1

j=1

we see that

fx,ℓ(t) = 21−ξℓ′+1 Supp(rx,ℓ) . (6.10) By expansion and a substitution, we have

Supp(fx,ℓ) = Supp(rx,ℓ+1) and

t

1−ξℓ′+1

(εℓ+1,j − ε′ℓ+1,j)xℓ+1,j ,

fx,ℓ(t)2 =

1Supp(rx,ℓ)(t)1Supp(rx,ℓ) t −

εℓ+1,ε′ℓ+1 t

t

j=1

### whence

fx,ℓ(t)2 − 21−ξℓ′+1 Supp(rx,ℓ) =

t

1−ξℓ′+1

(εℓ+1,j − ε′ℓ+1,j)xℓ+1,j .

1Supp(rx,ℓ)(t)1Supp(rx,ℓ) t −

=

εℓ+1̸=ε′ℓ+1 t

j=1

Denote the two equal expressions here by E(x). We may write

1−ξℓ′+1

1Supp(rx,ℓ)(t)1Supp(rx,ℓ)(t′)1 t − t′ =

(εℓ+1,j − ε′ℓ+1,j)xℓ+1,j . (6.11)

E(x) =

εℓ+1̸=ε′ℓ+1 t,t′

j=1

By Cauchy-Schwarz we have Supp(fx,ℓ) ⩾ t fx,ℓ(t) 2/ t fx,ℓ(t)2, and using this, (6.10) and the definition of E(x), it follows that

22(1−ξℓ′+1)|Supp(rx,ℓ)|2 21−ξℓ′+1 Supp(rx,ℓ) + E(x)

Supp(rx,ℓ+1) ⩾

,

and hence from (6.9) (and using ℓ + 1 − β′(ℓ + 1) = ℓ − β′(ℓ) + (1 − ξℓ′+1)) that τx∗|β′(ℓ) ⩽ τx∗|β′(ℓ + 1) 1 +

E(x) 21−ξℓ′+1

.

|Supp(rx,ℓ)|

Taking expectations over the random choice of (x | β′) and using the trivial bound τx∗|β′(ℓ + 1) ⩽ 1 on the second term gives

E(x) 21−ξℓ′+1

Eτx∗|β′(ℓ) ⩽ Eτx∗|β′(ℓ + 1) + E

. (6.12)

|Supp(rx,ℓ)|

The remaining task is to bound the final average here. Consider again the definition (6.11) of E(x). Condition to xi,j = xi,j for i ⩽ ℓ and j ∈ [1 − ξi′]. From (6.11) and the anticoncentration estimate

- (5.6) it follows that

E E(x) | xi,j = xi,j for i ⩽ ℓ and j ∈ [1 − ξi′] ≪ 22(1−ξℓ′+1)−ℓ Supp(rx,ℓ) 2; note here that we have written rx,ℓ rather than rx,ℓ since this quantity depends only on the fixed variables xi,j with i ⩽ ℓ and j ∈ [1 − ξi′]. Consequently

E

E(x) 21−ξℓ′+1

|Supp(rx,ℓ)|

| xi,j = xi,j for i ⩽ ℓ, j ∈ [1 − ξi′] ≪ 21−ξℓ′+1−ℓ Supp(rx,ℓ) ≪ 2−β′(ℓ+1),

where here we used the trivial bound Supp(rx,ℓ) ⩽ 2ℓ−β′(ℓ). Undoing the conditioning and recalling

- (6.12), the estimate (6.8) follows.


□

7. The random variables ϱ and ϱ∗

In this section we develop the basic properties of the ϱ-statistics as defined in Section 1.2, which feature prominently in the measure µ (see Proposition 1.3).

Let β be an upper walk with increments ξi = β(i) − β(i − 1). In this section we suppose that β is infinite (rather than of length ⌈n/2⌉) although we will only be dealing with finite segments of β. Recall the definition of the conditioned upper process (u | β) and its elements ui,j, j ∈ [1 + ξi], as described in Section 5.3.

- Definition 7.1. Let β be an upper walk and let ℓ ⩾ 1 be an integer. Then we define the random variable ϱ∗u|β(ℓ) by


ϱ∗u|β(ℓ) := 2−β(ℓ)

εi,j2−ui,j ∈ [1 − 2−ℓ,1] . (7.1)

1

i⩽ℓ;j∈[1+ξi]

ε

Here, ε ranges over all ε = (εi,j)i⩽ℓ;j∈[1+ξi] with εi,j ∈ {0,1}. By convention we set ϱ∗u|β(0) := 1.

A very closely-related definition is that of ϱu|β(ℓ), which is defined as in (1.3), with u being the sequence (u | β). It is slightly annoying to express this using the ui,j notation for the elements of (u | β); we do this now. Fix the upper walk β. In order for the quantities ϱu|β(ℓ) to be well-defined, we will need to assume that

(j + β(j)) = ∞. (7.2)

lim

j→∞

Given ℓ ⩾ 1, let ℓ′ be minimal so that ℓ′ +β(ℓ′) ⩾ ℓ. (Note carefully that the definition of ℓ′ here, in the context of an upper walk β, differs from the definition in the previous section, but there should be no danger of confusion.) Define an integer r ⩾ 1 by

ℓ′ − 1 + β(ℓ′ − 1) = ℓ − r. (7.3)

We have r ⩽ max(ξℓ′ + 1,ℓ). Define u∗ℓ′,1,...,u∗ℓ′,r to be the r smallest elements among the uℓ′,j, j ∈ [1+ξℓ′], listed in ascending order so that u∗ℓ′,r is the largest of these elements, and therefore the ℓth element of (u | β) when these are listed in ascending order. Then from the definition (1.3) we have

r

∗ ℓ′,r−ℓ

∗

∗

εℓ′,j2−u

ℓ′,j ∈ [1 − 2−u

ϱu|β(ℓ) = 2u

εi,j2−ui,j +

ℓ′,r,1] . (7.4)

1

i<ℓ′;j

j=1

ε∈{0,1}ℓ

We now provide a lemma giving upper bounds for the ϱ and ϱ∗ statistics. The gist of this is that these variables are bounded in expectation (assuming weak boundedness properties of the walk β) and that both have only a small (∼ 2−m) probability of being nonzero if β assumes the value −m. This last point corresponds to a rigorous version of the heuristic around (2.6) and (2.7).

The proofs for ϱ,ϱ∗ are slightly different in minor details but are best given together.

- Lemma 7.2. Let m ⩾ 0 and ℓ ⩾ 1 be integers and let R ⩾ 1 be a parameter. Suppose that β is an upper walk which is R-bounded to length ℓ. Then


Eϱ∗u|β(ℓ) ≪ R2, (7.5) where the expectation is over random choices of (u | β). Suppose in addition that β(q) = −m for some q with 0 ⩽ q ⩽ ℓ. Then

P ϱ∗u|β(ℓ) ̸= 0 ≪ R3(1 + q)κ2−m. (7.6) Now suppose that β satisfies (6.2), and that β is R-bounded to length ℓ′, where ℓ′ is minimal so that ℓ′ + β(ℓ′) ⩾ ℓ. Then

Eϱu|β(ℓ) ≪ R2. (7.7) Suppose in addition that β(q) = −m for some q with 0 ⩽ q ⩽ ℓ′. Then

P ϱu|β(ℓ) ̸= 0 ≪ max(ℓ,ℓ′)32−m. (7.8) Proof. An important tool in the proof will be the anticoncentration estimate

P(2−ui,j ∈ I) ≪ 2i|I| (7.9)

uniformly for all intervals I and all i. This follows quickly from the fact that ui,j is uniformly distributed on (i − 1,i]. An important technical point is that when r is small there may not be a

similar concentration estimate for the u∗ℓ,j, which are likely to be concentrated at one end of the interval. Throughout the proof we may assume without loss of generality that R is sufficiently large.

Proof of (7.5). We observe that using the R-boundedness property we have (deterministically)

εi,j2−ui,j ⩽

(1 + ξi)21−i ⩽

i>2 log2 R

i>2 log2 R;j∈[1+ξi]

(1 + Riκ)21−i < 21. (7.10)

i>2 log2 R

To see the second inequality, one can bound the sum by ≪ R−1/2, then use the assumption that R is sufficiently large. Now suppose that ε counts towards (7.1), that is to say i⩽ℓ;j∈[1+ξ

i] εi,j2−ui,j ∈ i] εi,j2−ui,j ⩾ 12. It follows from this and (7.10) that some εa,b

- [1 − 2−ℓ,1]. In particular, i⩽ℓ;j∈[1+ξ


is nonzero with a ⩽ min(2log2 R,ℓ). We then have P

εi,j2−ui,j ∈ [1 − 2−ℓ,1] ≪ 2a−ℓ ≪ R22−ℓ;

i⩽ℓ;j∈[1+ξi]

this follows by revealing all ui,j with (i,j) ̸= (a,b) then using (7.9). Therefore P

εi,j2−ui,j ∈ [1 − 2−ℓ,1] ≪ R22−ℓ,

i⩽ℓ;j∈[1+ξi]

uniformly for all ε. Summing over the 2 i⩽ℓ(1+ξi) = 2ℓ+β(ℓ) choices of (εi,j)i⩽ℓ,j∈[1+ξi], and multiplying by the normalising factor 2−β(ℓ) in the definition (7.1), we obtain (7.5).

Proof of (7.7). This is similar but slightly more technical due to the failure of (7.9) for the u∗ variables. First note the trivial bound

∗

ℓ′,r ⩽ 2ℓ′. (7.11)

ϱu|β(ℓ) ⩽ 2u

If ℓ′ ⩽ 3, this immediately implies the required bound (since we are assuming R ⩾ 1), so suppose in what follows that ℓ′ ⩾ 4. Suppose that ε counts towards (7.4). Since u∗ℓ′,r ⩾ ℓ′ − 1 ⩾ 3, we have

r

∗

εℓ′,j2−u

ℓ′,j ⩾ 34. (7.12)

εi,j2−ui,j +

i<ℓ′;j∈[1+ξi]

j=1

We divide into two cases: Case 1 is that there is some nonzero εa,b with a ⩽ min(2log2 R,ℓ′ −1), and Case 2 is that this fails to be the case. In Case 1, we may argue as before using (7.9). If we are in Case 2 then, arguing as in the proof of (7.5), we have i<ℓ′;j∈[1+ξi] εi,j2−ui,j ⩽ 12, and hence from (7.12) it follows that rj=1 εℓ′,j2−u

∗

ℓ′,j ⩾ 41. Then, since u∗ℓ′,j ⩾ ℓ′ − 1, we have r ⩾ 2ℓ′−3. By R-boundedness we have r ⩽ 1 + ξℓ′ ⩽ 1 + R(ℓ′)κ. Since r ⩾ 2ℓ′−3 ⩾ 2, this implies that R ≫ 2ℓ′/2, and then (7.7) follows using (7.11).

Proof of (7.6). Suppose first that q ⩽ 2log2 R. Since all steps of β are at least −1, we have q ⩾ m, and so R22−m ⩾ 1. The stated bound is therefore trivial in this case, so we assume from now on that q > 2log2 R.

Suppose that ϱ∗u|β(ℓ) ̸= 0. Then there is some ε such that i⩽ℓ εi,j2−ui,j ∈ [1 − 2−ℓ,1]. As before, this implies that εa,b ̸= 0 for some a ⩽ min(2log2 R,ℓ). In particular, a ⩽ q. Moreover, since ui,j ⩾ i − 1, i⩽q εi,j2−ui,j lies in the interval I := [1 − i⩾q+1(1 + ξi)21−i − 2−ℓ,1]. By revealing all ui,j except ua,b, it follows (since q ⩾ a) that P i⩽q εi,j2−ui,j ∈ I ≪ R2|I|. Summing over all possibilities for (εi,j)i⩽q,j∈[1+ξi], of which there are 2 qi=1(1+ξi) = 2q+β(q) = 2q−m, it follows that

P(ϱ∗u|β(ℓ) ̸= 0) ≪ R22q−m|I| = R22−m

(1 + ξi)2q−i + 2q−ℓ . (7.13)

i⩾q+1

Note that 2q−ℓ ⩽ 1. Moreover, the R-boundedness assumption implies that

1 + R(j + q)κ qκ ≪ Rqκ (7.14)

(1 + ξi)2q−i ⩽ qκ

2−j

i⩾q+1

j⩾1

The desired bound (7.6) therefore follows from (7.13).

Proof of (7.8). Since the steps of β are bounded below by −1, we have ℓ′ ⩾ q ⩾ m. Since (7.8) is vacuous for m ⩽ 3, we may assume ℓ′ ⩾ 3. From the definition of ℓ′ we have that β(ℓ′) ⩾ β(ℓ′ − 1), so the smallest q′ for which β(q′) ⩽ −m has q′ ⩽ ℓ′ − 1. Replacing q by q′ and m by m′ = −β(q′), we may assume that q ⩽ ℓ′ − 1. Write R˜ for the smallest quantity such that β is R˜ bounded to length ℓ′ − 1. Since i⩽ℓ′−1(ξi + 1) = (ℓ′ − 1) + β(ℓ′ − 1) < ℓ, we certainly have ξi ⩽ ℓ for all

- i ⩽ ℓ′ − 1 and so (crudely) R˜ ⩽ ℓ. Suppose that ϱu|β(ℓ) ̸= 0. Then there is some ε such that


r

∗

εℓ′,j2−u

ℓ′,j ∈ [1 − 21−ℓ′,1]. (7.15)

εi,j2−ui,j +

i<ℓ′;j∈[1+ξi]

j=1

Since ℓ′ ⩾ 3, we must again be in at least one of the two cases, Case 1 and Case 2, as described following (7.12).

We first treat Case 1. Using (7.10) (with R˜ replacing R) we see that in this case there is some

nonzero εa,b with a ⩽ min(2log2 R,ℓ˜ ′ − 1). Suppose that q < a. Then q ⩽ 2log2 R˜. Since q ⩾ m, R˜22−m ⩾ 1 and hence ℓ22−m ⩾ 1. The bound (7.8) is therefore trivial in this case, so we assume from now on that q ⩾ a.

By (7.15), i⩽q εi,j2−ui,j lies in the interval I˜ := [1 − q+1⩽i⩽ℓ′−1(1 + ξi)21−i − (r + 1)21−ℓ′,1]. Here, it is important to note that q ⩽ ℓ′ − 1. Arguing as in (7.13) (using here that q ⩾ a, and also that R˜ ⩽ ℓ) we obtain

(1 + ξi)2q−i + (r + 1)2q−ℓ′ .

P ϱu|β(ℓ) ̸= 0 ≪ ℓ22−m

q+1⩽i⩽ℓ′−1

We have (r+1)2q−ℓ′ < r+1 ≪ ℓ, so the contribution from this term is acceptable. The contribution from the sum over i may be bounded exactly as in (7.14) (with R˜ replacing R), and this term is also acceptable. This concludes the analysis of Case 1.

Finally, we consider Case 2. As before, r > 2ℓ′−3. We also have r ⩽ ℓ. Furthermore, since β is

an upper walk we have min0⩽i⩽ℓ′ β(i) ⩾ −ℓ′, and so m ⩽ ℓ′. Combining these facts gives 2m ⩽ 8ℓ, and so (7.8) is trivial in this case. □

Now we come to the second main result of the section, which asserts that ϱ∗u|β(ℓ) has good convergence properties as ℓ → ∞, under the assumption that β is appropriately T-positive in the sense of Definition 4.2. We will also need a related statement involving the ϱu|β(ℓ) and, as with

- Lemma 7.2, it makes sense to prove this at the same time.


- Lemma 7.3. Let ℓ ⩾ 1 be an integer and let T ⩾ 1 be a parameter. Then there is some absolute


constant c ∈ (0, 21) such that the following are true. Suppose that β is an upper walk which is T-positive up to ℓ. Then we have

E ϱ∗u|β(ℓ − 1) − ϱ∗u|β(ℓ) 2 ≪ 23T−cℓ1/4. (7.16) Now suppose that (7.2) holds. Given ℓ and β, we again define ℓ′ to be minimal such that ℓ′+β(ℓ′) ⩾

ℓ. Suppose that β is T-positive up to ℓ′. Then we have

E ϱ∗u|β(ℓ′ − 1) − ϱu|β(ℓ) 2 ≪ 23T−cℓ′1/4. (7.17) Proof. We begin by observing that in both situations, the positivity of β implies some weak boundedness properties. Starting with (7.16), from the definition (7.1) we have the trivial bound ϱ∗u|β(ℓ) ⩽ 2ℓ, and so (7.16) is vacuous unless T ⩽ ℓ. Thus we may assume T ⩽ ℓ throughout. But then, using the

T-positive nature of β, we have ξi = β(i) − β(i − 1) ⩽ 2T + ℓ1/2+η ⩽ 3ℓ for all i ⩽ ℓ. This implies that β is R-bounded up to ℓ for R := 3ℓ.

An essentially identical remark applies regarding (7.17), here using the trivial bound (7.11); in this case we may assume that β is R′ := 3ℓ′-bounded up to ℓ′.

We now begin the proof proper, starting with (7.17), indicating as we go the (minor) modifications required to prove (7.16). From this point on in the proof it is convenient to adopt the following shorthand for intervals: a+b[η] denotes the interval [a,a+bη] ⊂ R. Here, b is allowed to be negative (in which case we mean the interval [a + bη,a]).

Let λ ∈ [0,∞), x ∈ R and L ∈ N (we will have L ∈ {ℓ′,ℓ} later on). Set ε<L = (εi,j)i<L;j∈[1+ξi] ∈ {0,1}L−1+β(L−1). Denote by E(u,ε<L,λ,x) the event (for random (u | β) = (ui,j)i,j) that

εi,j2−ui,j ∈ 1 − x − 2−λ[21−L]. (7.18)

i<L;j∈[1+ξi]

Denote εℓ′ = (εℓ′,j)rj=1 ∈ {0,1}r. By mild rearrangement of (7.4) using (7.3), we have ϱu|β(ℓ) = 2−β(ℓ′−1)

Avεℓ′ 2λ0(u∗ℓ′)1 E(u,ε<ℓ′,λ0(u∗ℓ′),x0(εℓ′,u∗ℓ′) (7.19)

ε<ℓ′

∗

where here λ0(u∗ℓ′) := u∗ℓ′,r − (ℓ′ − 1) ∈ [0,1] and x0(εℓ′,u∗ℓ′) := rj=1 εℓ′,j2−u

ℓ′,j, and Avεℓ′ denotes the average over all tuples in εℓ′ ∈ {0,1}r. On the other hand from the definition (7.1) we have

Avεℓ′ 2λ1(u∗ℓ′)1 E(u,ε<ℓ′,λ1(u∗ℓ′),x1(εℓ′,u∗ℓ′) (7.20)

ϱ∗u|β(ℓ′ − 1) = 2−β(ℓ′−1)

ε<ℓ′

with λ1(u∗ℓ′) = x1(εℓ′,u∗ℓ′) := 0. Subtracting (7.20) from (7.19) gives ϱu|β(ℓ) − ϱ∗u|β(ℓ′ − 1)

Avεℓ′ 2λδ(u∗ℓ′)1 E(u,ε<ℓ′,λδ(u∗ℓ′),xδ(εℓ′,u∗ℓ′) . (7.21)

= 2−β(ℓ′−1)

(−1)δ

ε<ℓ′

δ∈{0,1}

Squaring and taking expectations over the random choice of (u | β) gives E ϱu|β(ℓ) − ϱ∗u|β(ℓ′ − 1) 2 = 2−2β(ℓ′−1)

(−1)δ+δ′×

δ,δ′∈{0,1}

<ℓ′,ε′<ℓ′ xδ(εℓ′,u∗ℓ′),xδ′(ε′ℓ′,u∗ℓ′),λδ(u∗ℓ′ ,λδ′(u∗ℓ′) ,

×

Avε

ℓ′,ε′ℓ′ pε

ε<ℓ′,ε′<ℓ′

where

(x,x′,λ,λ′) := 2λ+λ′P E(u,ε<L,λ,x) ∩ E(u,ε′<L,λ′,x′) . (7.22) Since δ,δ′(−1)δ+δ′ = 0 we have

pε<L,ε′

<L

E ϱu|β(ℓ) − ϱ∗u|β(ℓ′ − 1) 2 ≪ ≪ 2−2β(ℓ′−1)

<ℓ′,ε′<ℓ′(x,x′,λ,λ′) − pε

<ℓ′,ε′<ℓ′(0,0,0,0) . (7.23)

max

pε

0⩽x,x′⩽2Rℓ′2−ℓ′ λ,λ′∈[0,1]

ε<ℓ′,ε′<ℓ′

Here, the constraints on x,x′ come from the definition of x0( , ); we have |x0(εℓ′,u∗ℓ′)| ⩽ r21−ℓ′ ⩽ 2R(ℓ′)κ2−ℓ′.

To complete the proof of (7.17), it therefore suffices to show that the RHS of (7.23) is ≪ 23T−Ω(ℓ′1/4). At this point, ℓ′ can be thought of as simply a dummy variable (rather than specifically

the smallest ℓ′ such that ℓ′ + β(ℓ′) ⩾ ℓ). Replacing it by L (in both (7.22) and (7.23)), the task is therefore to show that if β is R-bounded and T-positive up to L, where R := 3L and T ⩽ L, then

(0,0,0,0) ≪ 23T−Ω(L1/4). (7.24)

2−2β(L−1)

(x,x′,λ,λ′) − pε<L,ε′

max

pε<L,ε′

<L

<L

0⩽x,x′⩽2RL2−L λ,λ′∈[0,1]

ε<L,ε′<L

Before turning to the proof of this, we claim that (7.16) also follows from it in the case L = ℓ. For this, first recall (7.20) (with the dashes dropped from the ℓs):

εi,j2−ui,j ∈ 1 − x1(εℓ,uℓ) − 2−λ1(uℓ)[21−ℓ] ,

ϱ∗u|β(ℓ − 1) = 2−β(ℓ−1)

Avεℓ 2λ1(uℓ)1

ε<ℓ

i<ℓ;j∈[1+ξi]

- where λ1(uℓ) = x1(εℓ,uℓ) = 0. On the other hand,

ϱ∗u|β(ℓ) = 2−β(ℓ−1)

ε<ℓ

Avεℓ 2λ2(uℓ)1

i<ℓ;j∈[1+ξi]

εi,j2−ui,j ∈ 1 − x2(εℓ,uℓ) − 2−λ2(uℓ)[21−ℓ]

- where λ2(uℓ) = 1 and x2(εℓ,uℓ) := ξjℓ=1+1 εℓ,j2−uℓ,j. That (7.16) is a consequence of (7.24) then follows almost verbatim as in the argument from (7.21) to (7.23) above.


To complete the proof of Lemma 7.3, then, the remaining task is to prove (7.24). The bound is trivial for L = O(1), so we may assume L sufficiently large. To ease notation, we write ε = ε<L and ε′ = ε′<L for the rest of the proof.

For any of the pε,ε′(···) terms in (7.24) to be nonzero (for a given fixed ε,ε′) we must have that some event E(u,ε<L,λ,x) with 0 ⩽ x ⩽ 2RL2−L and λ ∈ [0,1] is nontrivial, which implies

- i<L;j∈[1+ξi] εi,j21−i ⩾ 1 − 4RL2−L > 12, using here that R = 3L and that L is sufficiently large.


By (7.10), it follows that there is some (i0,j0) with i0 ⩽ 2log2 R (< L) such that εi0,j0 ̸= 0. Say that ε is good if it has this property. Thus we may restrict the sum in (7.24) to ε good, and similarly also to ε′ good.

We first consider the contribution to (7.24) from the diagonal terms with ε = ε′ (with both being good). The number of such pairs is < 2L+β(L−1). For fixed ε = ε′, pick some (i0,j0) with εi0,j0 ̸= 0 and i0 ⩽ 2log2 R. Revealing all ui,j except ui0,j0, it follows from (7.9) that

pε,ε′(x,x′,λ,λ′) ≪ P

εi,j2−ui,j ∈ 1 − x − 2−λ[21−L] ≪ 2i0−L ≪ R22−L.

i<L;j∈[1+ξi]

Thus the contribution of these terms to (7.24) is ≪ R22−β(L−1), which is ≪ R22T−Ω(L1/4) by the fact that β is a T-positive walk. Thus the contribution of the diagonal terms to (7.24) is acceptable.

Now consider the non-diagonal terms with ε ̸= ε′ and both ε,ε′ good. Order the pairs (i,j) with

- i < L and j ∈ [1 + ξi] lexicographically. Let (a,ja) be the first pair in this ordering for which at


least one of εa,ja,ε′a,j

### is not zero. Let (b,jb) be the first pair for which at least one of εb,jb,ε′b,j

a

b

### is not zero, and for which (εa,ja,ε′a,j

). These pairs must exist since ε,ε′ are distinct and neither is the zero tuple (since they are both good).

### ) ̸= (εb,jb,ε′b,j

a

b

For future reference we count the number of pairs ε,ε′ corresponding to a given (a,b). For such pairs we have εi,j = ε′i,j = 0 for i ⩽ a − 1, whilst (εi,j,ε′i,j) ∈ {(0,0),(εa,ja,ε′a,j

)} for a ⩽ i ⩽ b − 1, so the number of such choices is bounded by

a

2(b+β(b−1))−(a+β(a−1))22(L+β(L−1))−2(b+β(b−1)). (7.25) Expanding out the definitions (that is, (7.22) and the definition (7.18) of the event E(···)), one

sees that

pε,ε′(x,x′,λ,λ′) = 2λ+λ′P Zε,ε′(x,x′,λ,λ′)

where Zε,ε′(x,x′,λ,λ′) is the event that

εa,ja2−ua,ja + εb,jb2−ub,jb + t(u) ∈ 1 − x − 2−λ[21−L] and

2−ub,jb + t′(u) ∈ 1 − x′ − 2−λ′[21−L], where

ε′a,ja2−ua,ja + ε′b,j

b

ε′i,j2−ui,j.

εi,j2−ui,j, t′(u) :=

t(u) :=

(i,j)̸=(a,ja),(b,jb)

(i,j)̸=(a,ja),(b,jb)

εa,ja εb,jb ε′a,ja ε′b,j

Write M = M(ε,ε′) for the (nonsingular) 2×2 matrix

### . Then we can recast the definition of Zε,ε′(x,x′,λ,λ′) as the event that

b

- 2−ua,ja
- 2−ub,jb


∈ Dλ,λ′ − M−1 x x′++tt(′(uu)) , (7.26)

where Dλ,λ′ := M−1 (1 − 2−λ[21−L]) × (1 − 2−λ′[21−L]) ⊂ R2. To continue the computation we condition on the values of t = t(u) and t′ = t′(u), thus we write

pε,ε′(x,x′,λ,λ′) = 2λ+λ′ f(t,t′)P Zε,ε′(x,x′,λ,λ′) | t(u) = t,t′(u) = t′ dtdt′, (7.27)

where f is the probability density function of the variable (t(u),t′(u)). We divide into two cases for the pair (t,t′) via the following definition.

- Definition 7.4. We say that a pair (t,t′) is an edge pair if at least one of the sets Sλ,λ′,x,x′ := Dλ,λ′−M−1 x x′++tt′ , λ,λ′ ∈ [0,1], 0 ⩽ x,x′ ⩽ 2RL2−L, has a point outside the rectangle [2−a,21−a]×


- [2−b,21−b] ⊂ R2, and also one of the Sλ,˜ λ˜′,x,˜ x˜′ has a point inside this rectangle.


Using this definition and (7.27) we may decompose pε,ε′ = pedgeε,ε′ + pnonedgeε,ε′ in the obvious way. By the triangle inequality, it is sufficient to show the bound (7.24) with pε,ε′ replaced by each of pedgeε,ε′ and pnonedgeε,ε′ separately.

The edge case. We begin by handling the contribution of pedgeε,ε′ . One may compute that the distance between any point in Sλ,λ′,x,x′ and any point in Sλ,˜ λ˜′,x,˜ x˜′ is ≪ RL2−L. Therefore if (t,t′) is an edge pair, M−1 1 1−−tt′ (which lies in S0,0,0,0) lies in one of the four thin rectangles [2−a − O(RL2−L),2−a] × [2−b,21−b], [21−a,21−a + O(RL2−L)] × [2−b,21−b], [2−a,21−a] × [2−b − O(RL2−L),2−b] or [2−a,21−a] × [21−b,21−b + O(RL2−L)]. Since the possible rows of M−1 are ±(0,1), ±(1,0) and ±(1,−1), we see that one of t,t′,t − t′ is constrained to some interval of length O(RL2−L). We call these Cases 1,2 and 3 respectively.

- Case 1. Observe that εi1,j1 ̸= 0 for some (i1,j1) with i1 ⩽ b + 2log2 R: this is a consequence of

the restriction to ε,ε′ being good. Revealing all ui,j except ui1,j1, ua,ja, ub,jb, it follows that the probability of M−1(t(u),t′(u)) lying in one of the four thin rectangles is ≪ R3L2b−L.

- Case 2. The analysis is identical to Case 1 except now we use a non-zero value of ε′i

1,j1.

- Case 3. Note that εi1,j1 − ε′i


1,j1 ̸= 0 for some (i1,j1) with i1 ⩽ b + 2log2 R, using the definition of b. The rest of the analysis is as in Case 1.

By the above discussion,

P (t(u),t′(u)) is an edge pair ≪ R3L2b−L. (7.28) Now note that uniformly we have

P Zε,ε′(x,x′,λ,λ′) | t(u) = t, t′(u) = t′ ≪ 2a+b−2L.

This follows by observing that any translate of Dλ,λ′ is contained in some I1 × I2, where I1,I2 are intervals of length 22−L, and so by (7.9) we have

P Zε,ε′(x,x′,λ,λ′) | t(u) = t,t′(u) = t′ ⩽ P(2−ua,ja ∈ I1)P(2−ub,jb ∈ I2) ≪ 2a−L · 2b−L. (7.29) Putting (7.28) and (7.29) together, for a given ε,ε′ corresponding to (a,b), uniformly in x,x′,λ,λ′

we have

pedgeε,ε′ (x,x′,λ,λ) ≪ R3L2a+2b−3L. In particular this holds with x = x′ = λ = λ′ = 0.

We now bound the total contribution to (7.24) from the pedgeε,ε′ terms by summing the above bound over ε,ε′ corresponding to a given pair (a,b), then finally summing over (a,b). Using (7.25), the contribution to (7.24) for a fixed (a,b) is bounded by

≪ R3L · 2−2β(L−1) · 2(b+β(b−1))−(a+β(a−1)) · 22(L+β(L−1))−2(b+β(b−1)) · 2a+2b−3L, which simplifies to R3L2b−β(a−1)−β(b−1)−L. Finally, we sum over all (a,b) with a ⩽ b ⩽ L. The contribution from b < L/2 is negligible (using the T-positive nature of β to bound −β(a − 1) − β(b − 1) ⩽ 2T). For the contribution from b ⩾ L/2, we use b − L ⩽ 0 and −β(a − 1) − β(b − 1) ⩽ 2T − (L/2 − 1)1/2−η, which again follows from the T-positive nature of β. Using these estimates we obtain our sum over all (a,b), that is to say the total contribution from the edge cases, is ≪ R322T−Ω(L1/4). Since R = 3L, the R3 factor can be absorbed by reducing the Ω constant, and this is acceptable towards (7.24).

The non-edge case. In this case, using (7.26) we see that 2λ+λ′P Zε,ε′(x,x′,λ,λ′) | t(u) = t, t(u′) = t′ − P Zε,ε′(0,0,0,0) | t(u) = t, t(u′) = t′

dydy′ yy′ −

dydy′ yy′ , (7.30)

1 (log 2)2

2λ+λ′

=

R′

R

where R := D0,0 − M−1 t t′ , R′ := Dλ,λ′ − M−1 x x′++tt′ , and both regions of integration are contained in [2−a,21−a] × [2−b,21−b]. Set (uu′ ) := M−1 1 1−−tt′ ∈ R; thus (uu′ ) ∈ [2−a,21−a] × [2−b,21−b]. If y y′ ∈ R ∪ R′ then |u − y|,|u′ − y′| ≪ RL2−L. Now since a ⩽ b, both first partial derivatives of 1/yy′ on [2−a,21−a] × [2−b,21−b] are bounded by ≪ 2a+2b, and therefore on R ∪ R′ we have

1 yy′ =

1 uu′ + O(RL2−L2a+2b).

Substituting into (7.30), the contributions from the two uu1′ terms cancel since µ(R) = 2λ+λ′µ(R′) (here µ is Lebesgue measure on R2). The contribution from the O(RL2−L2a+2b) error is ≪ RL2a+2b−3L, since µ(R),µ(R′) ≪ 2−2L. Combining these observations gives

2λ+λ′P Zε,ε′(x,x′,λ,λ′) | t(u) = t, t(u′) = t′ − P Zε,ε′(0,0,0,0) | t(u) = t, t(u′) = t′

≪ RL2a+2b−3L. Integrating over all non-edge (t,t′) and using f(t,t′)dtdt′ = 1, we have

pnonedgeε,ε′ (x,x′,λ,λ) − pnonedgeε,ε′ (0,0,0,0) ≪ RL2a+2b−3L.

Exactly as before, we may sum this over all ε,ε′ corresponding to a given (a,b), and then over all (a,b), obtaining the same bound 22T−Ω(L1/4) for the contribution of the pnonedgeε,ε′ terms to (7.24). This concludes the proof of (7.24) and hence of Lemma 7.3. □

A corollary of Lemma 7.3 is a square mean bound for ϱ∗u|β(ℓ), which we will need in Section 15.

- Corollary 7.5. Let ℓ be sufficiently large and let T ⩾ 1 be a parameter. Suppose that β is an upper walk which is T-positive up to ℓ. Then we have


Eϱ∗u|β(ℓ)2 ≪ 23T. Proof. We use the inequalities

N

N

N

|Xi − Xi−1| 2 ⩽

E|XN − X0|2 ⩽ E

i−2

i2E|Xi − Xi−1|2

i=1

i=1

i=1

and E|XN|2 ⩽ 2E|XN − X0|2 + 2E|X0|2, valid for any sequence (Xi)Ni=0 of real-valued random variables. Applying these with N = ℓ and Xi = ϱ∗u|β(i), the result follows from Lemma 7.3. □

Remark. A somewhat shorter, direct, proof of Corollary 7.5 is possible, along the lines of Lemma 7.3 but without the careful analysis of ‘edge’ cases. We leave the details to the interested reader.

## Part 2. Background material

Each section of this part of the paper may be read independently of the rest of the paper. Our aim here is to assemble various background ingredients for the remaining parts of the argument.

8. Properties of random walks

In this section we collect the results we need on random walks constrained to be almost positive. Throughout the section β will be a random walk with increments ξi =d Pois(1)−1, and β′ a random walk with increments ξi′ =d 1−Pois(1), though much of the discussion would apply to rather general random walks.

For integers m, we write

β(i) ⩾ −m (8.1) and

N1/2P min

h(m) = lim

1⩽i⩽N

N→∞

β′(i) ⩾ −m . (8.2) The following proposition assembles the basic properties of these quantities. Proposition 8.1. We have the following statements.

h′(m) = lim

N1/2P min

1⩽i⩽N

N→∞

- (1) h(m), h′(m) exist for all m ⩾ 0 (that is, the limits in (8.1) and (8.2) exist for m ⩾ 0).
- (2) For m ⩾ 0 we have h(m) = (2/π)1/2(m + 1) and h′(m) = (2/π)1/2(m + O(1)).
- (3) Let 0 ⩽ m ⩽ √


N. Then, uniformly, N1/2P min

β(i) ⩾ −m ≍ m + 1, (8.3) and similarly for β′. Moreover we have the upper bound

1⩽i⩽N

β(i) ⩾ −m ≪ m + 1 (8.4) with no restriction on m.

N1/2P min

1⩽i⩽N

Proof. These may mostly be regarded as classical results from the fluctuation theory of random walks. However, it is not easy to locate appropriate references. See Appendix A for further details and proofs. We remark that (8.4) is a trivial consequence of (8.3). □

Once it is established that h(m) exists for all m ⩾ 0, it follows by conditioning on the first step of the walk that h(m) exists for all m ∈ Z and that we have the recurrence relation

P(Pois(1) − 1 = r)h(m + r) (8.5)

h(m) =

r⩾−m

(and similarly for h′). h(−1) is a convenient shorthand for limN→∞ N1/2P min1⩽i⩽N β(i) > 0 , and similarly for h′(−1). We remark that h′(m) = 0 for m ⩽ −2, since β′(1) ⩽ 1.

- 8.1. Spaces of almost positive paths. In this subsection we describe how, associated to random walks such as β,β′, there are certain measures on ZN supported on sequences which are bounded below. One should heuristically think of this as allowing us to sample ‘a random β which is bounded below’, though some care should be taken with this interpretation since these are not probability measures. The construction is mostly standard and is an example of Doob conditioning; we give brief details for the convenience of the reader.


Let m ⩾ −1. Denote by ZN⩾−m the space of sequences β = (β(i))∞i=1 with β(i) ∈ Z and β(i) ⩾ −m for all i. Consider the σ-algebra on ZN⩾−m generated by ‘cylinder’ sets of the form Γ(c1,...,cℓ) := {β ∈ ZN⩾−m : β(i) = ci for 1 ⩽ i ⩽ ℓ} for some ℓ ∈ N, where here we may restrict to min1⩽i⩽ℓ ci ⩾ −m.

Now consider the upper random walk β, that is to say the random walk with Pois(1) − 1 increments. Define ωm(ZN⩾−m) = h(m) and

ωm Γ(c1,...,cℓ) := h(m + cℓ)P β(i) = ci for 1 ⩽ i ⩽ ℓ . (8.6)

- Lemma 8.2. ωm is well-defined and extends to a measure on ZN⩾−m (with the σ-algebra described above). ωm is supported on sequences β for which β(i + 1) ⩾ β(i) − 1 for all i.


Proof. By the Daniell-Kolmogorov extension theorem it is enough to check the compatibility condition

### ωm Γ(c1,...,cℓ,cℓ+1) = ωm Γ(c1,...,cℓ) . We have

cℓ+1

h(m + cℓ+1)P β(i) = ci for 1 ⩽ i ⩽ ℓ + 1

### ωm Γ(c1,...,cℓ,cℓ+1) =

cℓ+1

cℓ+1

P ξℓ+1 = cℓ+1 − cℓ h(m + cℓ+1)P β(i) = ci for 1 ⩽ i ⩽ ℓ

=

cℓ+1

= h(m + cℓ)P β(i) = ci for 1 ⩽ i ⩽ ℓ = ωm Γ(c1,...,cℓ) ,

where the ξi are the increments of β and in the penultimate step we used (8.5) with m replaced by m+cℓ and the dummy variable r equal to cℓ+1 −cℓ. The key point to note is that this is valid since m + cℓ+1 ⩾ 0 by assumption. □

In an essentially identical manner we define measures ωm′ associated to the lower walk β′ (in fact a similar construction holds for any random walk γ with identical increments satisfying suitable assumptions, but we only need ωm and ωm′ in the present paper).

The following lemma provides a reasonably intuitive way to think about these measures.

- Lemma 8.3. Let m ⩾ −1 and L ⩾ 1 be integers, and suppose that S ⊂ [−m,∞)L ⊂ ZL. Denote by E the set of walks β with (β(1),...,β(L)) ∈ S. Then


β(i) ⩾ −m . (8.7)

N1/2P β ∈ E, min

ωm{β ∈ E} = lim

1⩽i⩽N

N→∞

Suppose moreover that L ⩽ N/2 and that m ⩽ √

N. Then P β ∈ E, min

β(i) ⩾ −m ≪ N−1/2ωm{β ∈ E}. (8.8)

1⩽i⩽N

Analogous results hold for β′ and ωm′ {β′ ∈ E}. Proof. We first establish (8.7). First of all, fix (c1,...,cL) ∈ S, and let N be much larger than L. Considering the translated walk γ(i) := β(i + L) − β(L), we see that

β(i) ⩾ −m

P β(1) =c1,...,β(L) = cL, min

1⩽i⩽N

γ(i) ⩾ −m − cL . By the definitions of h(m + cL) and of ωm, this is

= P β(1) = c1,...,β(L) = cL P min

1⩽i⩽N−L

P β(1) = c1,...,β(L) = cL · (1 + oN→∞(1))(N − L)−1/2h(m + cL)

= P β(1) = c1,...,β(L) = cL · (1 + oN→∞(1))N−1/2h(m + cL)

= (1 + oN→∞(1))N−1/2ωm(Γ(c1,...,cL)).

Summing over all (c1,...,cL) ∈ E gives (8.7). The proof of (8.8) is almost identical, but now using the second statement of Proposition 8.1 (2) and (3) in place of the definition of h(·), and applying the bound N ≪ N − L, which is valid in the range L ⩽ N/2. □

Path spaces. We recall that, associated to β, there is the standard notion of the path space ZN together with its associated measure which, with a slight abuse of notation, we denote by P. Here the σ-algebra is generated by cylinder sets Γ(c1,...,cℓ) (but now in ZN) and 1Γ(c1,...,cℓ)(β)dP(β) := P β(1) = c1,...,β(ℓ) = cℓ). It follows from the definitions that if F is a function supported on paths β with β(i) ⩾ −m for all i, but otherwise depending only on β(1),...,β(ℓ), then

F(β)dωm = F(β)h(m + β(ℓ))dP(β). (8.9)

There is a similar construction with respect to β′, and we will use P′ to denote the corresponding path measure.

- 8.2. Crude bounds for endpoints of almost positive walks. The following lemma may be found in various places, for instance [40, Lemma 20] and [2]. A very succinct argument is presented as Theorem 1 in the unpublished note [1]; we sketch this in Appendix A.3.


- Lemma 8.4. Uniformly for integers N ⩾ 1 and x ⩾ 0 we have

P β(N) = x, min

1⩽i⩽N

β(i) ⩾ 0 ≪ min N−1,(1 + x)N−3/2 ,

and similarly for β′. Proof. See the references above or Appendix A.3. □ We will need the following generalisation in which the condition on min1⩽i⩽N β(i) is relaxed.

- Lemma 8.5. Uniformly for integers N ⩾ 1, m ⩾ 0 and x ⩾ 0 we have


β(i) ⩾ −m ≪ (1 + m)2(1 + x + m)N−3/2. (8.10) and

P β(N) = x, min

1⩽i⩽N

β(i) ⩾ −m ≪ (1 + m)2N−1. (8.11) Similar estimates hold for β′.

P β(N) = x, min

1⩽i⩽N

Proof. In both cases we may assume that min1⩽i⩽N β(i) = −s for some s with 0 ⩽ s ⩽ m since the contribution from walks for which this is not the case can be bounded using Lemma 8.4. For

- j ∈ [N] define the probability


p(j,s,x) := P β(N) = x, β(j) = min

β(i) = −s . Thus it suffices to obtain upper bounds on

1⩽i⩽N

p(j,s,x). (8.12)

0⩽s⩽m 1⩽j⩽N

To bound p(j,s,x) we employ a reversal principle, running a walk with ξ′ increments backwards from

- j and a walk with ξ increments forwards. (Specifically, these walks are given by γ′(i) := β(j −i)+s and γ(i) := β(j + i) + s respectively.) From this we see that


γ′(i) ⩾ 0 P γ(N − j) = x + s, min

γ(i) ⩾ 0 , (8.13)

p(j,s,x) = P γ′(j) = s, min 1⩽i⩽j

1⩽i⩽N−j

where the second term is absent (equal to 1) when j = N, and for the first term to be valid we needed s ⩾ 0.

The second probability term in (8.13) is ≪ (N + 1 − j)−1 by Lemma 8.4 (considering the cases

- j < N and j = N separately). The first probability term in (8.13) is ≪ (1 + s)j−3/2, again using Lemma 8.4. Inputting these bounds into (8.13) gives the estimate


p(j,s,x) ≪ (1 + s)j−3/2(N + 1 − j)−1. (8.14) It then follows easily that the sum in (8.12) is ≪ (1 + m)2N−1, which gives (8.11).

Alternatively, one can use the second estimate in Lemma 8.4 on the second probability term in (8.13), obtaining

p(j,s,x) ≪ (1 + s)(1 + x + s)j−3/2(N + 1 − j)−3/2. From this it follows that the sum in (8.12) is ≪ (1 + m)2(1 + x + m)N−3/2, which gives (8.10). □ Remarks. The statements (8.10) and (8.11) are provided as natural generalisations of Lemma 8.4. In certain applications below one could save occasional powers of 1 + m by slightly more efficient use of the same underlying ideas. However, these powers of 1 + m are not important to us in this paper. The bound (8.14) will be used a few times later on in its own right. Finally, we note that a similar statement with a similar proof may be found as [21, Theorem 2].

As an application, we have the following bounds for measures of certain sets of walks.

- Lemma 8.6. Uniformly for m ⩾ 0, i ⩾ 1 and j ⩾ −m we have ωm{β: β(i) = j} ≪ (1 + m)2(1 + j + m)2i−3/2, (8.15)

and similar bounds hold for ωm′ . In particular for all q ⩾ 0 we have ωm{β: β(q) = −m} ≪ (1 + m)2(1 + q)−3/2. (8.16)

Proof. For (8.15), the value is h(m + j)P β(i) = j, min1⩽i′⩽i β(i′) ⩾ −m). We have h(m + j) ≪ 1+m+j by Proposition 8.1 (2), and the probability term may be bounded using (8.10). This gives (8.15). The bound (8.16) follows from (8.15) by taking i = q and j = −m. □

We also have the following statement about the position of the minimum.

- Lemma 8.7. Uniformly for integers N ⩾ 1, 0 ⩽ q ⩽ N, and m ⩾ 0, we have


β(i) ⩾ −m ≪ (1 + m)(1 + q)−3/2(N + 1 − q)−1/2.

P β(q) = −m, min

1⩽i⩽N

Proof. When q = 0 we must have m = 0, and the result is immediate from the existence of h(0). Suppose that q ⩾ 1. Then by (8.10) we have P β(q) = −m, min1⩽i⩽q β(i) = −m ≪ (1+m)2q−3/2. When q = N this gives the result immediately. Suppose that q < N. The shifted walk γ(i) := β(q + i) − β(q) of length N − q must have min1⩽i⩽N−q γ(i) ⩾ 0 which, by the existence of h(0), occurs with probability ≪ (N − q)−1/2 ≪ (N + 1 − q)−1/2. Since this walk is independent of (β(i))1⩽i⩽q, the stated bound follows. □

- 8.3. Local limit theorems for almost positive walks and applications. The main result of this subsection is a quantitative version of the local limit theorem for random walks constrained to be almost positive. Here is the statement we need. In this result


W(x) = xe−x2/21x⩾0 (8.17) denotes the density of the Rayleigh distribution. Proposition 8.8. There is an absolute constant ε0 > 0 such that the following holds. Uniformly for integers m,x,N with m,x ⩾ 0 and N ⩾ 1 we have

x √

β(i) ⩾ −m = N−1h(m)W

+ O (1 + m)O(1)N−1−ε0 (8.18) and

P β(N) = x, min

1⩽i⩽N

N

x √

β′(i) ⩾ −m = N−1h′(m)W

+ O (1 + m)O(1)N−1−ε0 . (8.19)

P β′(N) = x, min

1⩽i⩽N

N

Remarks. For the proof, see Appendix A.4 and Appendix B. We give some brief bibliographical remarks here. The result also holds in the case m = −1 (with (1+m)O(1) replaced by 1) and this is a result of Denisov, Tarasov and Wachtel [11, Theorem 1]; however, this is a very precise asymptotic with a correspondingly lengthy proof, and moreover depends on [13]. For these reasons, we give an essentially self-contained account in our appendices. Other relevant references are Caravenna [10] (who was seemingly the first to prove a local limit theorem for random walks conditioned to stay positive, but with no quantitative dependencies) and Grama and Xiao [25, Theorem 6.1], which (with a little work) would imply Proposition 8.8. Let us be clear that we claim no originality for this result.

For the remainder of the paper ε0 will denote a fixed constant for which Proposition 8.8 holds true.

- 8.4. Coupling results. We now derive some results about coupling β,β′ together to have nearby endpoints. These will be critical inputs in our argument.


- Lemma 8.9. Let ε1 > 0 be a sufficiently small constant. Let m,m′ be non-negative integers. Let L,N,N′ be positive integers with |N′ − N| ⩽ 1. Let c1,...,cL and c′1,...,c′L ∈ Z with ci ⩾ −m and c′i ⩾ −m′ for all i, 1 ⩽ i ⩽ L. If m > 0 suppose that min1⩽i⩽L ci = −m, and if m′ > 0 that min1⩽i⩽L c′i = −m′. Assume that


c′i ⩽ Nε1 and that L,|d|,m,m′ ⩽ Nε1. Then

max

ci, max

1⩽i⩽L

1⩽i⩽L

P min

β(i) = −m, min

0⩽i⩽N

0⩽i⩽N′

β′(i) = −m′, β(N) − β′(N′) = d | β(i) = ci, β′(i) = c′i, i = 1...,L

√π 4

N−3/2h(m + cL)h′(m′ + c′L) + O(N−3/2−ε1).

=

Proof. The result is vacuous for N = O(1) so we assume N sufficiently large throughout. Let γ be the random walk of length N −L defined by γ(i) := β(L+i)−cL, thus γ has Pois(1)−1 increments. Define γ′ similarly. The condition that min0⩽i⩽N β(i) = −m is then precisely the condition that min1⩽i⩽N−L γ(i) ⩾ −m − cL, and similarly for β′. Therefore the probability we are interested in equals

γ(i) ⩾ −m−cL ·P γ(N′ −L) = x′, min

γ′(i) ⩾ −m′ −c′L .

P γ(N −L) = x, min

1⩽i⩽N−L

1⩽i⩽N′−L

x−x′=d

We can localise the sum to x,x′ ⩽ N1/2+ε1 with simple large deviation estimates on P(γ(N − L) ⩾ N1/2+ε) and the corresponding estimate with γ′ (see Lemma F.3). By Proposition 8.8, the remaining sum is

h(m′ + c′L) N′ − L

x′ √N′ − L

x √N − L

h(m + cL) N − L

+O NCε1−ε0−1

+O NCε1−ε0−1

W

W

x−x′=d x,x′⩽N1/2+ε1

for some absolute constant C. By the assumptions and Proposition 8.1 (2) we have h(m+cL),h′(m′+ c′L) ≪ Nε1 and so one may see that the contribution from all terms involving one of the O(·) errors is acceptable, provided ε1 is sufficiently small in terms of ε0. We are then left with the sum

h(m + cL)h′(m′ + c′L) (N − L)(N′ − L)

x′ √N′ − L

x √N − L

W

W

.

x−x′=d x,x′⩽N1/2+ε1

Now one may check that √Nx′′−L, √Nx−L = √xN + O(Nε1−1/2) in the range of summation, and so the above is

L N

x √

2 + O(Nε1−1/2) .

N−2h(m + cL)h′(m′ + c′L) 1 + O(

W

)

N

x,x−d⩽N1/2+ε1

The contributions from both the O(L/N) and the O(Nε1−1/2) terms are easily seen to be acceptable, so we are left with

x √

N−2h(m + cL)h′(m′ + c′L)

)2.

W(

N

x,x−d⩽N1/2+ε1

Comparing the sum to an integral we see that N−1/2

√π 4

∞

x √

2 =

W(t)2 dt + O(N−1/2) =

+ O(N−1/2).

W

N

0

x,x−d⩽N1/2+ε1

This concludes the proof. □ The next result allows us to dispense with ‘rare’ events in coupled situations like the above.

- Lemma 8.10. Let M,N,N′ be positive integers with |N′ − N| ⩽ 1. Suppose that E is an event on the sample space of walks β of lengths ⩽ N. Then uniformly for nonnegative integers m,m′ ⩽ M and d ∈ Z we have


β′(i) = −m′, β(N) − β′(N′) = d ≪ M2N−1P β ∈ E, min

P β ∈ E, min

β(i) = −m, min

0⩽i⩽N

0⩽i⩽N′

β(i) ⩾ −m . There is a symmetric estimate with the roles of β,β′ reversed.

β(i) = −m ≪ M3N−3/2P β ∈ E | min

0⩽i⩽N

1⩽i⩽N

### Proof. We can write the probability as

β′(i) = −m′, β′(N′) = x − d .

P β ∈ E, min

β(i) = −m, β(N) = x P min

0⩽i⩽N

0⩽i⩽N′

x

Applying (8.11) to the second factor gives the first estimate. To get the second estimate we relax the min0⩽i⩽N β(i) = −m condition to min1⩽i⩽N β(i) ⩾ −m and apply (8.4). □

- 8.5. Boundedness estimates. In this section we bound the probability of an almost positive walk having an unusually large increment. We start with a definition which is closely related to Definition 4.1. Recall that κ = 1001 is a globally defined small constant.


- Definition 8.11. Let β be a walk. Then we define R(β) to be the minimal positive integer R for


which |ξi| ⩽ Riκ for all i. Set R(β) := ∞ if no such R exists. More generally denote by R⩽L(β) the minimal positive integer for which this holds for all i ⩽ L, that is to say the minimal positive integer R for which β is R-bounded to length L.

Remark. The restriction of the values of R to a discrete set (the integers) is a technical convenience. Lemma 8.12. Uniformly in integers L,N with 1 ⩽ L ⩽ N and non-negative integers m,r we have

β(i) ⩾ −m ≪ (m + r + 1)e−rN−1/2. A similar estimate holds for β′.

P R⩽L(β) > r, min

1⩽i⩽N

Proof. We may assume r ⩾ 1, since for r = 0 the result is immediate from (8.4). If R⩽L(β) > r then there is some (minimal) index ℓ, 1 ⩽ ℓ ⩽ L, such that |ξℓ| ⩾ rℓκ. Suppose that |ξℓ| = i. Then, by the minimality of ℓ, we have β(ℓ) ⩽ |ξ1|+···+|ξℓ| ⩽ rℓ2+i. The shifted walk γ(j) := β(ℓ+j)−β(ℓ) of length N − ℓ must therefore stay above −(m + rℓ2 + i), and so the contribution of a given pair (ℓ,i) to our probability is, by (8.4),

1 (i + 1)!

(m + rℓ2 + i)(N + 1 − ℓ)−1/2.

≪ P |ξℓ| = i · (m + rℓ2 + i)(N + 1 − ℓ)−1/2 ≪

(Note that this estimate does hold when ℓ = N, which is why we included the +1 term.) To complete the proof, we must show that the sum of the RHS over all (ℓ,i) is bounded by ≪ (m+r+1)e−rN−1/2.

The contribution from ℓ ⩽ N/2 is ≪ N−1/2

1 (i + 1)!

1 (i + 1)!

(m + rℓ2 + i) ⩽ N−1/2

(m + r + 1)ℓ2i.

ℓ⩾1 i⩾rℓκ

ℓ⩾1 i⩾rℓκ

Using the bounds i⩾X i1! ≪ e−X and ℓ⩾1 ℓ2e−rℓκ ≪ e−r, this is seen to be acceptable.

To estimate the contribution from N/2 < ℓ ⩽ N we can use very crude bounds. We may bound this by

1 (i + 1)!

1 i!

(m + rN2 + i) ⩽ (m + r + 1)N3

≪ N

i⩾r(N/2)κ

i⩾r(N/2)κ

≪ (m + r + 1)N3e−r(N/2)κ ≪ (m + r + 1)e−rN−10.

This is (amply) acceptable and the proof is complete. The proof for β′ is identical since |ξℓ| and |ξℓ′| have the same distribution. □

A consequence of this is the following bound on the ω-measure of walks which are not r-bounded. Corollary 8.13. Suppose that m,r ⩾ 0 are integers. Then uniformly in L ∈ N we have

ωm{R⩽L(β) > r}, ωm′ {R⩽L(β′) > r} ≪ (m + r + 1)e−r. Similar estimates hold for ωm{R(β) > r} and ωm′ {R(β′) > r}.

Proof. The required bounds are immediate from (8.7) and Lemma 8.12. □

- 8.6. Positivity estimates. In this section we show that an almost positive random walk almost surely has a parabolic shape. The following definition is very closely related to the definition of T-positive walk, which is Definition 4.2. Recall that η = 1001 is a globally-defined small parameter. Definition 8.14. Denote by T(β) the smallest integer T for which −T +ℓ1/2−η ⩽ β(ℓ) ⩽ T +ℓ1/2+η


for all ℓ, and set T(β) := ∞ if no such integer exists. More generally, define T⩽L(β) to be the smallest integer T for which this holds for all ℓ ⩽ L, that is to say for which β is T-positive to length L.

Lemma 8.15. Suppose that m ⩾ 0 and T,N > 0 are integers. Then We have

β(i) ⩾ −m ≪ (1 + m)O(1)T−η/2N−1/2. A similar statement holds for β′.

P T⩽N(β) > T, min

1⩽i⩽N

Proof. When T < 2m, the result follows immediately from Proposition 8.1 by simply ignoring the condition T⩽N(β) > T on the LHS. Thus we assume that T ⩾ 2m in what follows. Once again the same proof applies to both the dashed and undashed statements, so we prove only the former. We first consider the ‘upper’ failure of positivity in which there is some ℓ ⩽ N such that β(ℓ) ⩾ T +ℓ1/2+η. In fact we will handle the event β(ℓ) ⩾ T +ℓ1/2 log ℓ. By Proposition 8.1 applied to the shifted walk γ(·) := β(ℓ + ·) − β(ℓ) of length N − ℓ, and by Lemma F.3, we have

P β(ℓ) ⩾ T + ℓ1/2 log ℓ, min

β(i) ⩾ −m ≪

(N + 1 − ℓ)−1/2

(m + i)P(β(ℓ) = i)

1⩽i⩽N

ℓ⩽N

ℓ⩽N

i⩾T+ℓ1/2 log ℓ

(m + i)e−i2/4ℓ.

(N + 1 − ℓ)−1/2

≪

ℓ⩽N

i⩾T+ℓ1/2 log ℓ

To bound this, set i := T +⌈ℓ1/2 log ℓ⌉+j and note that i2 ⩾ T2 +j2 +ℓlog2 ℓ; the sum is therefore bounded by

m + T + ℓ1/2 log ℓ + j e−T2/4ℓe−j2/4ℓ

(N + 1 − ℓ)−1/2ℓ−10

j⩾0

ℓ⩽N

(N + 1 − ℓ)−1/2ℓ−9e−T2/4ℓ

(j + 1)e−j2/4ℓ,

≪ (1 + m)T

j⩾0

ℓ⩽N

using here that m + T + ℓ1/2 log ℓ + j ⩽ (1 + m)Tℓ(j + 1). Since j je−j2/4ℓ ≪ ℓ, this is bounded by

(N + 1 − ℓ)−1/2ℓ−8e−T2/4ℓ.

≪ (1 + m)T

ℓ⩽N

For ℓ ⩽ T we use e−T2/4ℓ ⩽ e−T/4 and ℓ⩽N(N + 1 − ℓ)−1/2ℓ−8 ≪ N−1/2, and for ℓ ⩾ T we use e−T2/4ℓ ⩽ 1 and T⩽ℓ⩽N(N + 1 − ℓ)−1/2ℓ−8 ≪ T−7N−1/2. Thus the probability of this ‘upper failure’ is ≪ (m + 1)T−6N−1/2, which is substantially smaller than the stated bound.

We turn now to bounds for the more subtle ‘lower’ failure of positivity. This fact, namely that almost positive walks almost surely have nearly squareroot growth, is critical for the whole paper. Our argument is closely related to that of Ritter [34]. Suppose that for some ℓ, 1 ⩽ ℓ ⩽ N, we have β(ℓ) ⩽ −T + ℓ1/2−η. Since β(ℓ) ⩾ min1⩽i⩽N β(i) ⩾ −m, we have ℓ ⩾ (T − m)2 ⩾ T2/4, so T ⩽ 2N1/2, and (obviously) β(ℓ) ⩽ ℓ1/2−η. We will bound the measure of walks for which there is an ℓ with these last two properties. The argument will be slightly different according to whether ℓ ⩽ N/8 (say) or not.

The case ℓ ⩽ N/8. Suppose that k ⩽ N/4 is a power of two (here k is just a dummy variable, not the global variable k from the main paper). Let j be an integer with j ∈ [k/2,2k]. Denote

by Zj,k(β) the indicator of the event that β(j) ⩽ 2k1/2−η. Using Proposition 8.1 (applied to the shifted walk γ(·) := β(j + ·) − β(j), which has length N − j ⩾ N/2 and minimum ⩾ −u − m) and then (8.10) we have

β(i) ⩾ −m ≪ N−1/2

β(i) ⩾ −m

P Zj,k(β) = 1, min

(1 + m + u)P β(j) = u, min

1⩽i⩽j

1⩽i⩽N

−m⩽u⩽2k1/2−η

≪ (1 + m)2N−1/2

(m + u + 1)2j−3/2 ≪ (1 + m)5N−1/2k−3η.

−m⩽u⩽2k1/2−η

Denote

Zj,k(β).

Zk(β) :=

j∈[k/2,2k]

It follows that for any δ ∈ (0,1) we have P Zk(β) ⩾ δk, min

β(i) ⩾ −m ≪ (1 + m)5δ−1N−1/2k−3η. (8.20)

1⩽i⩽N

We say that β is reasonable at scale k if β(j2) − β(j1) ⩽ k1/2−η and β(j1) ⩽ k whenever j1,j2 satisfy k/2 ⩽ j1 < j2 ⩽ 2k and j2 − j1 ⩽ k1−2η(log k)−2. We claim the following estimate:

β(i) ⩾ −m ≪ (1 + m)2k−10N−1/2. (8.21)

P β unreasonable at scale k, min

1⩽i⩽N

To see this we use a union bound over the ≪ k2 choices of j1,j2. For each choice, we need to bound

β(i) ⩾ −m +

β(i) ⩾ −m .

P β(j1) = i1,β(j2) = i2, min

P β(j1) = i1, min

1⩽i⩽N

1⩽i⩽N

−m⩽i1⩽k i2−i1>k1/2−η

i1>k

For this we apply Proposition 8.1 to the walk shifted by j2 (for the first term) or j1 (for the second term). Since N − j1,N − j2 ≫ N we see that this is

≪ N−1/2

(m+1+i2)P β(j1) = i1,β(j2) = i2 +N−1/2

(m+1+i1)P β(j1) = i1 . (8.22)

−m⩽i1⩽k i2−i1>k1/2−η

i1>k

By Lemma F.5 we have P(β(j1) = i1) ≪ e−i1/10 uniformly for j1 ∈ [k/2,2k] and i1 > k, and so (after summing over the O(k2) choices of j1,j2) the contribution of the second term here is bounded as claimed in (8.21). To bound the first term in (8.22) we set i = i2−i1 and sum out the i1 variable, obtaining a bound

≪ N−1/2(k + m)

(m + k + i)P(β(j2 − j1) = i).

i>k1/2−η

By a standard large deviation estimate (see Lemma F.3) this is ≪ N−1/2(k + m)

(m + k + i)e−i2/4(j2−j1),

i>k1/2−η

which in turn is bounded by ≪ N−1/2(k + m)2

ie−i2(logk)2/4k1−2η < N−1/2(1 + m)2k−100.

i>k1/2−η

Summing over the O(k2) choices for j1,j2, this completes the proof of (8.21).

Now suppose that β(ℓ) ⩽ ℓ1/2−η (with ℓ ⩽ N/8) and let k be the unique power of two such that ℓ ∈ (k/2,k]. Thus k ⩽ N/4, and β(ℓ) ⩽ k1/2−η. Suppose that β is reasonable at scale k. Then

β(j) ⩽ 2k1/2−η for all j with 0 ⩽ j − ℓ ⩽ k1−2η(log k)−2, and so Zk(β) ⩾ k1−2η(log k)−2. By (8.20) with δ := k−2η(log k)−2, it follows that

β(i) ⩾ −m, β(ℓ) ⩽ ℓ1/2−η for some ℓ ∈ (k/2,k], β reasonable at scale k

P min

1⩽i⩽N

≪ (1 + m)5N−1/2k−η(log k)2 for all (powers of two) k ⩽ N/4. Putting this together with (8.21) gives

β(i) ⩾ −m, β(ℓ) ⩽ ℓ1/2−η for some ℓ ∈ (k/2,k] ≪ (1 + m)5N−1/2k−η(log k)2. Summing k over powers of two with k ⩾ (T − m)2 yields

P min

1⩽i⩽N

β(i) ⩾ −m, β(ℓ) ⩽ ℓ1/2−η for some ℓ, N/8 ⩾ ℓ ⩾ (T − m)2 ≪ (1 + m)5N−1/2T−η/2. This is the desired bound in the case ℓ ⩽ N/8.

P min

1⩽i⩽N

The case N/8 < ℓ ⩽ N. The proof in this case is somewhat similar. In this case, we say that β

is reasonable if |β(j2) − β(j1)| ⩽ N1/2−η whenever j1,j2 ∈ [N/8,N] and |j2 − j1| ⩽ N1−5η/2. By another large deviation estimate (see Corollary F.4), β is reasonable with probability ⩾ 1 − N−10.

If β is reasonable, and if β(ℓ) ⩽ ℓ1/2−η for some ℓ ∈ [N/8,N], then by appropriate rounding there is some j = λ⌊N1−5η/2⌋, λ ∈ Z⩾0, N − j ∈ [N/8,N], with β(N − j) ⩽ 2N1/2−η.

Now for a fixed such j we have P β(N − j) ⩽ 2N1/2−η, min

β(i) ⩾ −m =

β(i) ⩾ −m

P β(N − j) = u, min

1⩽i⩽N

1⩽i⩽N

−m⩽u⩽2N1/2−η

β(i) ⩾ −m · (m + u + 1)(1 + j)−1/2

P β(N − j) = u, min

≪

1⩽i⩽N−j

−m⩽u⩽2N1/2−η

by applying Proposition 8.1 to the walk of length j starting after N − j. (Here we used (1 + j)−1/2 so that the result is true for j = 0). By (8.10), and since N − j ≫ N, this is

(1 + u + m)2N−3/2(1 + j)−1/2 ≪ (1 + m)5N−3η(1 + j)−1/2.

≪ (1 + m)2

−m⩽u⩽2N1/2−η

Summing over j = λ⌊N1−5η/2⌋ with λ ∈ Z⩾0 such that N − j ∈ [N/8,N] (thus λ ≪ N5η/2) gives ≪ (1 + m)5N−1/2−η/2. Since T ⩽ 2N1/2, this is ≪ (1 + m)5N−1/2T−η, which implies the desired bound in this case. □

Corollary 8.16. Let m ⩾ 0 and T ⩾ 1 be integers. We have

ωm{T(β) > T}, ωm′ {T(β′) > T} ≪ (1 + m)O(1)T−η/2. Proof. Once again the proofs of the two statements are the same so we handle only the first one. It follows immediately from Lemma 8.15 that if L ⩽ N then

β(i) ⩾ −m ≪ (1 + m)O(1)T−η/2.

N1/2P T⩽L(β) > T, min

1⩽i⩽N

The result now follows from (8.7) by letting N → ∞, and then letting L → ∞. □

- 8.7. Constructing a jump step. We now come to the most technical part of the section. We start with a definition. Here, η = κ = 1001 are the global constants involved in Definitions 4.1 and 4.2.


Definition 8.17. Let V ∈ N. Let β be a walk of length N with increments ξi = β(i) − β(i − 1). Then we say that an index t is a V -jump step if 1 + ξt = V and if, for all ℓ with 0 ⩽ ℓ ⩽ N − t, we have

β(t + ℓ) − β(t) ⩾ ℓ1/2−2η, (8.23)

and if 1 ⩽ ℓ ⩽ N − t we have

ξt+ℓ ⩽ ℓ2κ. (8.24) We will show that a random β almost surely has a jump step in a suitable range. This will be

done by recursive application of the following result.

- Lemma 8.18. Suppose that N,V are sufficiently large integers and let β be a random walk of length N with Pois(1) − 1 increments. Then we have


β(i) ⩾ 0 ⩾ V −V . Proof. Choose absolute constants R,T such that

P index 1 is a V -jump step for β | min

1⩽i⩽N

β(i) ⩾ 0, β is R-bounded and T-positive up to N ≫ N−1/2, (8.25)

P min

1⩽i⩽N

uniformly for N sufficiently large. That such R,T exist follows from Lemma 8.12 and Lemma 8.15 with m = 0, together with the existence of h(0), which implies that P min1⩽i⩽N β(i) ⩾ 0 ≫ N−1/2. Set L := ⌈max(10,2T,R1/κ)⌉ (thus L is still an absolute constant).

The walk with β(i) = V − 2 + i for i = 1,...,N satisfies (8.23) and (8.24) for t = 1. This walk occurs with probability P(Pois(1) = V ) · P(Pois(1) = 2)N−1 which, if V is sufficiently large, is ⩾ V −V for any N ⩽ 2L. Therefore we may assume N > 2L in what follows.

Now by the existence of h(0) we have P min1⩽i⩽N β(i) ⩾ 0 ⩽ CN−1/2 for some absolute C, so it suffices to show that

P index 1 is a V -jump step for β, min

1⩽i⩽N

β(i) ⩾ 0 ⩾ CV −V N−1/2. (8.26)

Consider the shifted walk γ(i) := β(L + i) − β(L) and let its increments be ξ˜i := ξL+i. We claim that the event on the left in (8.26) contains the event E defined by

γ(i) ⩾ 0, γ is R-bounded and T-positive up to N − L}. This is enough to complete the proof, since (using (8.25) applied to γ) we have

{ξ1 = V − 1,ξ2 = ···ξL = 1} ∩ { min

1⩽i⩽N−L

P(E) ≫ P(Pois(1) = V ) · P(Pois(1) = 2)L−1(N − L)−1/2, so P(E) ⩾ CV −V N−1/2 provided V is sufficiently large.

To prove the claim, suppose that β ∈ E. First note that we clearly have 1 + ξ1 = V . Now for ℓ with 1 ⩽ ℓ ⩽ L−1, we have β(1+ℓ)−β(1) = ℓ ⩾ ℓ1/2−2η. Thus (8.23) holds for ℓ ⩽ L−1. Moreover for i = 0,...,N − L we have, using the T-positive nature of γ and the fact that L ⩾ max(10,2T), that

β(L + i) − β(1) = γ(i) + (β(L) − β(1)) ⩾ −T + i1/2−η + (L − 1)

⩾ L1/2−η + i1/2−η ⩾ (L + i)1/2−η. Thus (8.23) holds for L ⩽ ℓ ⩽ N − 1 as well.

The inequality (8.24) certainly holds for 1 ⩽ ℓ ⩽ L − 1. For i = 0,...,N − L we have

ξ1+L+i = ξ˜1+i ⩽ R(1 + i)κ < (L + i)2κ, and so (8.24) also holds for L ⩽ ℓ ⩽ N − 1. This completes the proof of the claim, and hence of

- Lemma 8.18. □ Now we turn to the main result of this subsection.


- Lemma 8.19. There exists an absolute constant C such that the following holds. Let N,V be


sufficiently large integer parameters. Let m ⩾ 0 be an integer, and suppose that δ ∈ (0, 101 ). Let tmin,tmax be two integer thresholds, and suppose that

8(m + 2)CV V δ

4/η

N > tmax > tmin ⩾

(8.27) and

log log tmax − log log tmin ⩾ 20V V log(1/δ). (8.28) Then

β(i) ⩾ −m ≪ δ.

P β does not have a V -jump step in [tmin,tmax] | min

1⩽i⩽N

Proof. For brevity in what follows set ε := V −V . Define thresholds T1 := tmin and Tj+1 := Tj4, j = 1,2,.... We assume in what follows that any such threshold under discussion is ⩽ tmax; this will ultimately turn out to be the case by use of (8.28), as we shall show later. Set Ij := [Tj,Tj+1). We say that β has a local jump step in Ij if there is some t ∈ [Tj,Tj2] such that 1+ξt = V and such that (8.23) and (8.24) are satisfied for all ℓ with 1 ⩽ ℓ < Tj+1 − t. (Note the case ℓ = 0 of (8.23) is trivial.)

Denote by Jj the event that β has a local jump step in the interval Ij. Set τj := P ¬J1 ∩ ··· ∩ ¬Jj | min

β(i) ⩾ −m . Observe that τ1 ⩾ τ2 ⩾ ... and that for j ⩾ 2 we have

1⩽i⩽N

β(i) ⩾ −m

τj−1 − τj = P Jj ∩ ¬J1 ∩ ··· ∩ ¬Jj−1 | min

1⩽i⩽N

β(i) ⩾ −m . (8.29)

P Jj ∩ ¬J1 ∩ ··· ∩ ¬Jj−1 ∩ arg min

β(i) = s | min

=

1⩽i⩽N

Tj⩽i⩽N

Tj⩽s⩽N

(That is, s is the first s ∈ [Tj,N] for which β attains its minimum on that interval.) To estimate (8.29) from below, we first consider the sum over s ⩾ Tj2. For this, we simply ignore the J events, bounding the sum by

β(i) ⩾ −m . (8.30)

β(i) ∈ [Tj2,N] | min

P arg min

1⩽i⩽N

Tj⩽i⩽N

Suppose that β is t1min/2 -positive up to N (see Definition 4.2). Then β(Tj) ⩽ Tj1/2+η + t1min/2 and β(s) ⩾ (Tj2)1/2−η − t1min/2 for all s with Tj2 ⩽ s ⩽ N. Since Tj ⩾ tmin > 28 and η ⩽ 81, we have Tj1/2+η + t1min/2 < (Tj2)1/2−η − t1min/2 , and so in this case we do not have arg minTj⩽i⩽N β(i) ∈ [Tj2,N]. Thus we can bound (8.30) by

P β is not t1min/2 -positive up to N | min

β(i) ⩾ −m .

1⩽i⩽N

Using Proposition 8.1 (3) and Lemma 8.15, we see that the probability in (8.30) is ⩽ (m+2)Ct−minη/4 for some absolute C. Thus we have shown that

β(i) ⩾ −m ⩽ (m + 2)Ct−minη/4. (8.31)

P Jj ∩ ¬J1 ∩ ··· ∩ ¬Jj−1 ∩ arg min

β(i) = s | min

1⩽i⩽N

Tj⩽i⩽N

Tj2⩽s⩽N

Consider now the portion of the sum in (8.29) over the range Tj ⩽ s < Tj2. We bound this below by

P Jj(s) ∩ ¬J1 ∩ ··· ∩ ¬Jj−1 ∩ arg min

β(i) ⩾ −m , (8.32)

β(i) = s | min

1⩽i⩽N

Tj⩽i⩽N

Tj⩽s<Tj2

where Jj(s) is the event that t = s + 1 is a local jump step; this event is obviously contained in Jj.

We the apply the chain rule for conditional probability P(A ∩ B ∩ Es | M) = P(B | M) · P(Es | B ∩ M) · P(A | B ∩ Es ∩ M),

where A = Jj(s), B = ¬J1∩···∩¬Jj−1, Es = (arg minTj⩽i⩽N β(i) = s) and M = (min1⩽i⩽N β(i) ⩾ −m). Observe that P(B | M) = τj−1. Denote P(Es | B ∩ M) := p(s). Then (8.32) is

p(s)P Jj(s) | ¬J1 ∩ ··· ∩ ¬Jj−1, arg min

β(i) ⩾ −m . (8.33)

β(i) = s, min

τj−1

1⩽i⩽N

Tj⩽i⩽N

Tj⩽s<Tj2

The event we are conditioning on here has the form Es(β(1),...,β(s)) ∩ min1⩽i⩽N−s γ(i) ⩾ 0), where γs(i) := β(s + i) − β(s) is the shifted walk starting at s and

β(i) ⩾ −m) ∩ β(i) > β(s) for Tj ⩽ i < s ;

Es := ¬J1 ∩ ··· ∩ ¬Jj−1 ∩ ( min

1⩽i⩽s

note carefully that, by the definition of local jump step, Es really does depend only on the values β(i) for i ⩽ s. The event Jj(s) depends only on γs (the portion of β after s), and so (8.33) is

p(s)P Jj(s) | min

γ(i) ⩾ 0 ⩾ ετj−1

p(s),

τj−1

1⩽i⩽N−s

Tj⩽s<Tj2

Tj⩽s<Tj2

where the second step follows from Lemma 8.18 applied to γ (recalling here that ε = V −V ). Combining the upper bound (8.31) with the lower bound we have just obtained for (8.32) via

- (8.33), and substituting in to (8.29), we have shown that

τj−1 − τj ⩾ ετj−1

Tj⩽s<Tj2

p(s) − (m + 2)Ctmin−η/4. (8.34)

We must now give a lower bound for the sum over p(s). Note first of all that

Tj⩽s⩽N

p(s) = 1, (8.35)

since precisely one of the events Es occurs for any β. Now for each s we have p(s) = P(Es | B ∩ M) =

P(Es ∩ B ∩ M) P(B ∩ M)

⩽

P(Es ∩ M) P(B ∩ M)

=

P(Es | M) P(B | M)

=

1 τj−1

P(Es | M). (8.36) Furthermore, T2

j ⩽s⩽N P(Es | M) is precisely the probability in (8.30), which we have already shown (in the analysis leading up to (8.31)) to be at most (m + 2)Ct−minη/4. Combining this with

- (8.34) to (8.36) gives


δε 4

τj−1 − τj ⩾ ετj−1 − 2(m + 2)C+1t−minη/4 ⩾ ετj−1 −

,

where this last inequality follows from (8.27). By induction, τj ⩽ 4δ + (1 − 4δ)(1 − ε)j−1, and so τj ⩽ δ/2 for all j ⩾ 10ε−1 log(1/δ), that is to say

P β has no local jump step in any Ij, j ⩽ 10ε−1 log(1/δ) | min

β(i) ⩾ −m ⩽ δ/2. (8.37)

1⩽i⩽N

Suppose now that β has a local jump step in Ij, but does not have an actual jump step in Ij. This means that either (8.23) or (8.24) fails for some ℓ with Tj+1 − t ⩽ ℓ ⩽ N − t and for some t ∈ [Tj,Tj2]. That is, either

β(t + ℓ) ⩽ β(t) + ℓ1/2−2η or ξt+ℓ > ℓ2κ (8.38) for some such ℓ. We additionally observe that ℓ is much larger than t; certainly ℓ ⩾ t since

- t ⩽ Tj2 ⩽ 12Tj+1.


Suppose the first of the alternatives in (8.38) holds. We claim that either β(t+ℓ) ⩽ (t+ℓ)1/2−η −

tmin or β(t) ⩾ t2/3 + tmin. To see this, first note that 1 4(t + ℓ)1/2−η ⩾ max t2/3,ℓ1/2−2η,2tmin . (8.39) The first inequality here follows using t + ℓ ⩾ Tj+1 and t ⩽ Tj2 and the fact that Tj+1 := Tj4. The second inequality follows from 41(t + ℓ)1/2−η > 14ℓ1/2−2η and the fact that ℓ is sufficiently large. The third inequality following using t + ℓ ⩾ Tj+1 and tmin = T1. Adding the inequalities in (8.39) gives (t + ℓ)1/2−η − tmin ⩾ t2/3 + tmin + ℓ1/2−2η, which implies the claim. The claim implies that β fails to be tmin-positive in the sense of Definition 4.2. By another application of Proposition 8.1 and Lemma 8.15, the probability of this event conditional on min1⩽i⩽N β(i) ⩾ −m is ⩽ (m + 2)Ct−minη/2 ⩽ δ/4.

Now suppose the second option in (8.38) holds. Then β fails to be tκ/min2-bounded in the sense

of Definition 4.1; this is because ℓ2κ > tκ/min2(t + ℓ)κ, since ℓ2/3 ⩾ (Tj+1/2)2/3 > T11/2 = t1min/2 and ℓ4/3 > 2ℓ ⩾ t + ℓ. By Proposition 8.1 (3) and Lemma 8.12, the probability of this conditional on

min1⩽i⩽N β(i) ⩾ −m is certainly ⩽ δ/4; the key point here is that the assumption (8.27) implies that the term e−t

κ/2

min arising from the application of Lemma 8.12 is massively smaller than δ, and also that N is massively larger than m and 1/δ. The conclusion of the above analysis is that

β(i) ⩾ −m ⩽ δ/2.

P β has a local but not a global jump step in some Ij | min

1⩽i⩽N

Combining with (8.37) proves that, conditioned on min1⩽i⩽N β(i) ⩾ −m, the probability that β has no (global) jump step in any Ij with j ⩽ 10ε−1 log(1/δ) is at most δ. The proof is concluded by noting that, under condition (8.28), all such intervals Ij are contained in [tmin,tmax]. □

9. Bounds on {0,1}-matrices

This section assembles various ingredients that will be used in Part 3 of the paper, having to do with bounds on the number of {0,1}-matrices satisfying various linear-algebraic conditions.

Let M be an ℓ × N matrix. Write r for its rank (thus r ⩽ ℓ), and for d with 1 ⩽ d ⩽ r denote by qd the least index such that the first qd columns of M span a subspace of Qℓ of dimension d. Set qr+1 := N + 1. We call (r;q1,...,qr) the rank profile of M and denote it by rp(M).

- Lemma 9.1. We have the following statements. Suppose that ℓ ∈ N.


- (i) The number of ℓ-by-N matrices M with {0,1}-entries and rp(M) = (r;q1,...,qr) is bounded above by 2ℓ22rN− rd=1 qd.
- (ii) Suppose that N ⩾ 10ℓ and that 1 ⩽ r < ℓ. The number of ℓ-by-N matrices M with {0,1}entries and rank r, and at least r+1 different nonzero rows, is ≪ 2ℓ22(r−101 )N. (By different rows we mean distinct as elements of QN.)


Proof. (i) We uncover the columns of M one-by-one. Consider the qth column. If q is one of the qd then we bound the number of choices trivially by 2ℓ. Otherwise, suppose that qd < q < qd+1; then the qth column lies in the linear span of the previous columns, which has dimension d. It is a folklore fact (see, for instance, [22, Lemma 5.1]) that any subspace of Qℓ of dimension d intersects the cube {0,1}ℓ in at most 2d points, and so there are at most 2d choices for the qth column. Therefore the quantity we seek is bounded above by

2 rd=1 d(qd+1−qd−1)+ℓr = 2rN− rd=1 qd− rd=1 d+ℓr ⩽ 2ℓ22rN− rd=1 qd as claimed.

(ii) There is some set of r rows which span the row space of M; this can be selected in r ℓ ways. Fix such a set of rows. Consider the induced r-by-N submatrix M′.

Say that an r-by-N matrix is typical if the intersection of the Q-linear span of its rows with {0,1}N consists of only the rows themselves and zero. We claim that a random r-by-N matrix with {0,1}-entries is typical with probability ⩾ 1 − 2−N/10.

Given the claim, we may conclude the proof of (ii) as follows. If M′ is typical, then M can only have r different nonzero rows, since all rows of M are in the Q-linear span of M′. If M′ is not typical, then by the claim there are ⩽ 2(r−101 )N choices for M′. Each of the remaining ℓ − r rows of

- M is drawn from the intersection of {0,1}N with the row space of M′, which has size at most 2r

by the folklore fact above. This gives ⩽ (2r)ℓ−r ways to complete M′ to M. Since r ℓ (2r)ℓ−r ⩽ 2ℓ2, the result follows.

It remains to prove the claim. Let Q be a random r-by-N matrix with {0,1}-entries. Let N′ be an integer with N/3 ⩽ N′ ⩽ N/2. We first reveal the r-by-N′ submatrix Q′ formed from the first

- N′ columns. The probability that Q′ does not have full rank is bounded above by 2r−N′, even over


F2: each of the 2r − 1 possible annihilators of the column space occurs with probability 2−N′.

Suppose now that Q′ has been revealed and that it does have full rank. Fix a set S of r columns which span. We now reveal the remaining elements of Q \ Q′. Consider a hypothetical element of {0,1}N in the row span of Q, not zero or one of rows. Suppose that it is ri=1 λivi where v1,...,vr are the rows of Q and at least two of the λi are not zero. Restricting to the columns in S, we see that there are at most 2r choices for (λ1,...,λr). Fix such a choice. We now proceed to reveal the N − N′ columns in Q \ Q′. Each of these is a vector ε = (ε1,...,εr) ∈ {0,1}r such that

r i=1 λiεi ∈ {0,1} ⩽ 43 since, if λu,λv ̸= 0,

r i=1 λiεi ∈ {0,1}. Observe that we have Pε∈{0,1}r

then the set {0,λu,λv,λu + λv} has size at least 3, hence for every x = i̸=u,v λiεi at least one of

- x,x+λu,x+λv,x+λu+λv is not in {0,1}. It follows that the probability that ri=1 λivi ∈ {0,1}N is ⩽ (3/4)N−N′. Summing over the possible choices of (λ1,...,λr) gives that the probability of Q failing to be typical (for fixed Q′ of full rank) is ⩽ 2r(3/4)N−N′.


Combining the above estimates, we see that the probability that Q is not typical is ⩽ 2r−N′ + 2r(3/4)N−N′. Using the bounds r ⩽ N/10 and the choice of N′, the result follows. □

10. The function g

In this section we give the basic properties of the function g ∈ C∞(R/Z) featuring in our main theorem, and defined as in (1.2). We have already noted the transformation law (2.19). The other key properties we need are contained in the following lemma.

- Lemma 10.1. The Fourier coefficients g(m) := R/Z g(x)e−2πimxdx are given by


1 log 2

log log 2 log 2

2πm log 2

i . (10.1) In particular, g(m) ̸= 0 for all m ∈ Z. We have the bounds

g(m) = −

Γ

+

6 log 2

e−π2|m|/log 2. (10.2) We have

| g(m)| <

maxg ming

⩽ 1 + 2 × 10−7. (10.3)

Remark. Note that since the Fourier coefficients | g(m)| decay quicker than any fixed power of m, the function g is indeed smooth with g(j)(θ) = m∈Z(2πim)j g(m)e2πiθm (see for instance [24, Proposition 3.3.12]).

Proof. From the definition (1.2) and unfolding the R/Z and D∈Z into an integral over the real line, it follows that for m ∈ Z we have

∞

∞

log log 2

log2 +2logπim2 −1(1 − e−u)du. To investigate this, it makes sense to consider more generally the integral

(log 2)x(1 − e−2x)e2πimx dx = (log 2)−1

u

g(m) =

−∞

0

∞

us−1(1 − e−u)du (10.4)

Is :=

0

for Res ∈ (−1,0). It turns out that this can be explicitly evaluated in terms of the Γ-function, namely Is = −Γ(s) for −1 < Res < 0, and from this (10.1) follows immediately.

The evaluation of Is can be justified2as follows:

∞

∞

∞

∞

u

us−1 dudt

e−t

e−t dtdu =

us−1

us−1(1 − e−u)du =

t

0

0

0

0

∞

ts s

1 s

e−t −

dt = −

Γ(s + 1) = −Γ(s).

=

0

Turning to (10.2), presumably one can look up precise numerical asymptotics for Γ in the relevant strip −1 < Res < 0. However, the integral representation (10.4) allows us to derive an appropriate bound from first principles with minimal effort via a contour integration argument, which we give now.

Write s = σ + it and assume t > 0 (the case t < 0 can be handled symmetrically or by taking complex conjugates). One may note that the integral here indeed converges for σ ∈ (−1,0); as

- u → ∞, the condition σ < 0 guarantees convergence, whilst as u → 0 we have 1 − e−u ≪ u and the condition σ > −1 guarantees it. To estimate Iσ+it we perform a contour integration in the upper right quadrant. Denote by Cr = {reiθ : 0 ⩽ θ ⩽ π/2} the quarter circle of radius r. Let 0 < r < 1 < R. Then applying Cauchy’s theorem around the contour formed by Cr,CR and the portions of the real and imaginary axes between r and R, we see that


R

uσ−1+it(1 − e−u)du

r

R

(ui)σ−1+it(1 − e−ui)du −

uσ−1+it(1 − e−u)du +

uσ−1+it(1 − e−u)du.

= i

CR

Cr

r

We first estimate the integral over CR. Using that |1 − e−z| ⩽ 2 for Rez ⩾ 0, we see that on this contour we have |1 − e−u| ⩽ 2, and at u = Reiθ we have |uσ−1+it| = Rσ−1e−θt ⩽ Rσ−1 for t ⩾ 0. The length of the contour is πR/2, and so the total contribution is ≪ Rσ−1 · R which tends to zero as R → ∞, since σ < 0.

Next we estimate the integral over Cr. Now we use |1 − e−u| ≪ |u| = r and |uσ−1+it| ≪ rσ−1. The length of the contour is πr/2, so the total contribution is ≪ r · rσ−1 · r = rσ+1, which tends to zero as r → 0 since σ > −1.

It follows that Iσ+it = i

∞

∞

(ui)σ−1+it(1 − e−ui)du =

uσ−1+iteσiπ/2−πt/2(1 − e−ui)du.

0

0

2As an aside for the reader, the authors originally discovered that g was almost constant via the use of GPT

- o4-mini. Upon being asked to prove this fact, the model suggested the broad strategy but miscomputed this integral (instead replacing it by the computation of the integral 0 ∞ exxs−−11 dx = ζ(s)Γ(s)); this embarrassingly tricked the second author until clarification by the first author. Upon prompting the model with the relevant Wikipedia page

- on Mellin transforms, the model was able to complete the proof and give the counter integral argument to bound the Γ(·) (which is of course completely standard).


Taking absolute values, |Iσ+it| ⩽ e−πt/2

∞

∞

uσ−1|1 − e−iu|du ⩽ e−πt/2

uσ−1(min(u,2))du

0

0

1 σ + 1 −

1 σ

e−πt/2.

= 2σ+1

In the case of interest to us, where σ = log log 2log 2 , we get a numerical value of less than 6, so |Γ(σ + it)| = |Iσ+it| ⩽ 6e−πt/2 in this case. Since g(m) = −log 21 Iloglog2

log2 +2logπim2 , the bound (10.2) follows immediately.

Finally we establish (10.3). Using (10.2) and simple numerics we have

∞

12 log 2

e−π2m/log 2 < 7.5 × 10−12.

| g(m)| ⩽

|m|⩾2

m=2

By further numerical evaluations (using Wolfram Alpha) we have that g(0) = −

1 log 2

log log 2

log 2 ≈ 5.1278218186 and

Γ

1 log 2

log log 2 + 2πi

log 2 ≈ 2.4479026947 × 10−7. Thus we conclude that

| g(1)| = | g(−1)| =

Γ

g(0) + m̸=0 | g(m)| g(0) − m̸=0 | g(m)|

maxg ming

⩽ 1 + 2 · 10−7, which is the desired bound (10.3). □

⩽

## Part 3. The Poisson paradigm

11. Approximate ℓ-wise independence

The main result of this section is Lemma 11.2. We will describe it informally below, but in order to do so we set up some notation.

We will consider a random multiset (A | β,β′) sampled conditioned on (β,β′) = (β,β′) for some fixed pair of upper and lower walks β,β′. The general setup under discussion here is outlined in Section 5 and the reader may wish to review that now. We recall in particular from (5.1) to (5.3) that A = (ai,j)i∈[n],j∈[bi], where

bi := 1 − ξi′ (i = 1,...,⌊n/2⌋) and bn+1−i := 1 + ξi (i = 1,...,⌈n/2⌉). (11.1) Throughout the section we will write

n

D = D(β,β′) := β(⌈n/2⌉) − β′(⌊n/2⌋) =

bi − n. (11.2)

i=1

We occasionally refer to this quantity as the discrepancy of (β,β′). From now on we fix a truncation parameter M; the walks under consideration will have

β′(i) ⩾ −M,

min

β(i), min

1⩽i⩽⌈n/2⌉

1⩽i⩽⌊n/2⌋

and later we will let M → ∞ as n → ∞. Associated to M we will also associate the following key truncation thresholds.

## Definition 11.1. Given M we define

- • R(M) := 20M is a threshold for the R-boundedness of walks;
- • T(M) := e40M/η is a threshold for the T-positivity of walks;
- • L(M) is an extremely large function of M. (How large it needs to be is reliant on the bounds in Lemma 8.19, the result on the existence of jump steps; the point at which we need L(M) to be very large is in the proof of Lemma 13.4.)


These thresholds will be in place for the next several sections. We will also require some more technical parameters namely ℓ∗(M),V (M),tmin(M),tmax(M). The parameter hierarchy will be

T(M) ≪ ℓ∗(M) ≪ V (M) ≪ tmin(M) ≪ tmax(M) ≪ L(M) < n/2. (11.3) and V (M) will be an integer. For the rest of this section we will drop the explicit mention of M when referring to R, T, ℓ∗, V , tmin, tmax and L for notational brevity. We briefly discuss the purpose of the rest of these parameters.

The ℓ∗ parameter will control the depth to which we manage to run a crucial inclusion-exclusion principle during the argument.

The V,tmin,tmax parameters are connected with the (rather technical) notion of jump step (Definition 8.17). Throughout the next two sections we will assume that β has a V -jump step at some index t = t(β) which satisfies tmin ⩽ t ⩽ tmax; for definiteness we take t minimal subject to these constraints. We informally remark that by Lemma 8.19 this will be a generic property of β for appropriate choices of parameters. Note also that bn+1−t = 1 + ξt = V . The jump step t is associated with the random elements an+1−t,j, j ∈ [V ], of A, all of which have size ≍ 2n−t; these will play a special role in what follows.

For technical reasons to do with calculations in the local limit theorem we also need to condition on the approximate distribution of these elements an+1−t,j. To set this up let us briefly recall from (5.2) that an+1−t,j = ϕ˜(n−ut,j), where the ut,j, j ∈ [V ], are independent uniform random variables on (t − 1,t]. The definition of ϕ˜ may be found at Definition 5.1; recall in particular that ϕ˜(x) ≍ 2x, so that indeed an+1−t ≍ 2n−t.

For the rest of the section we abuse notation by writing V 1/3 for ⌊V 1/3⌋ for brevity. Partition

V 1/3

m − 1 V 1/3

m V 1/3

. (11.4)

Im, Im := t − 1 +

(t − 1,t] =

,t − 1 +

m=1

For each u we record the ‘jump distribution’ which is the random tuple f = (f1,...,fV 1/3) where fm is the number (frequency) of the ut,j in the interval Im. Thus, in particular we have m fm = V deterministically. The conditioned variables (ut,j | f = f) consist of fm independent uniform

samples from Im for m = 1,...,V 1/3.

For the remainder of this section and much of the next, we will condition not just to fixed choices β = β, β′ = β′, but also to a fixed choice f = f. The precise point at which the additional conditioning on f will be removed is after (12.36) below. For notational brevity, until that point we write A rather than (A | β = β,β′ = β′,f = f). The key result of the section is Lemma 11.2 below. The main aim of this result (cf. (4.3)) is to understand the quantity P(k ∈ Σ(A)) (with A conditioned to β = β,β′ = β′,f = f as discussed above).

The statement of Lemma 11.2 is a little technical, and the proof lengthy, so we start by offering some motivation. We set

Asmall := (ai,j)1⩽i⩽L,j∈[bi], Amed := (ai,j)L+1⩽i⩽n+1−t,j∈[bi], (11.5) and

Alarge := (ai,j)n+1−t<i⩽n,j∈[bi].

Note in particular that the elements associated to the jump step of β are the elements of Amed with the highest index i = n + 1 − t. We remind the reader that Σ(A) is the set of sums

{ 1⩽i⩽n,j∈[bi] εi,jai,j : εi,j ∈ {0,1}}, and (for example) Σ(Amed) is defined analogously. We consider the event (k ∈ Σ(A)) as the union of the events Xε = (k− n+1−t<i⩽n,j∈[bi] εi,jai,j ∈

Σ(Amed)+Σ(Asmall)), over all choices of εlarge := (εi,j)n+1−t<i⩽n,j∈[bi]. The idea will be to compute P(k ∈ Σ(A)) by using inclusion-exclusion on these events. To enable this, we need to show that

they are approximately ℓ-wise independent for ℓ → ∞.

We relabel the elements of A associated to the jump step t as (an+1−t,j)j∈[V ] to be consistent with the conditioning to f = f. Thus we write an+1−t,j = ϕ˜(n−Um) where m = m(j) is the unique value of m ∈ {1,...V 1/3} for which f1 + ···fm−1 < j ⩽ f1 + ··· + fm, Um is uniform on Im and ϕ˜ is defined in Definition 5.1. Unravelling the definitions, we thus have

n Hk

n Hk

P(an+1−t,j = x) = V 1/3 (n − Im) ∩

Hx−1,

Hx .

Thus, if we set α := V 1/3n/Hk ≈ V 1/3/log 2 then the distribution of an+1−t,j is as follows. There are integers x0,x1 ≍ 2n−t and α0,α1 with 0 ⩽ α0,α1 ⩽ α (all potentially depending on j) such that:

 

0 x < x0 or x > x1;

- α0/x0 x = x0; α/x x0 < x < x1;
- α1/x1 x = x1.


(11.6)

P(an+1−t,j = x) =



Thus, an+1−t,j takes values in an interval of length ≍ V −1/32n−t. A particular point to note is that we must replace the anticoncentration bound (5.8) for i = n + 1 − t by the weaker bound

P(an+1−t,j = x) ≪ V 1/32t−n (11.7) (which follows immediately from (11.6)); for other values of i it is unchanged.

sup

x

Define µj = Ean+1−t,j and write

V

V

1 4

- 1

- 2


µj and σ2 =

Ea2n+1−t,j. (11.8)

µ =

j=1

j=1

In various places in the analysis we will use that (deterministically, and uniformly in f)

an+1−t,j,µj ≍ 2n−t, |an+1−t,j − µj| ≪ V −1/32n−t, σ ≍ V 1/22n−t, (11.9) all of which are clear from the definitions. Finally let g be the Gaussian density with mean µ and variance σ2,

2

1 σ√2π

x−µ σ

- 1

- 2


e−

, (11.10) noting that once again this depends on f.

g(x) :=

Finally we come to the statement of Lemma 11.2. Recall Definitions 4.1 and 4.2.

- Lemma 11.2. Let β,β′ be upper and lower walks that are each R-bounded and T-positive up to lengths ⌈n/2⌉,⌊n/2⌋ respectively. Set L := L(M) < n/2. Suppose that min1⩽i⩽⌈n/2⌉ β(i), min1⩽i⩽⌊n/2⌋ β′(i) ⩾ −M, and that |D| ⩽ M/10, where the discrepancy D is given by (11.2). Suppose that β has a V -jump step. Let n′ be an integer satisfying L ⩽ n′ ⩽ n − L. Suppose that


′

S ⊂ N is a set of size τ2 n

i=1 bi with max(S) ⩽ 2n−L/2 and where V −1 ⩽ τ ⩽ 1. Let ℓ ⩽ ℓ∗, and let

- xi, i = 1,...,ℓ, be positive integers such that |xi − µ| ⩽ (log V )1/4σ. (11.11)


Furthermore suppose that we have the separation condition

|xi − xi′| > 2n−L/2 (11.12) for i ̸= i′. Write A>nmed′ := (ai,j)n′+1⩽i⩽n+1−t,j∈[bi]. Then we have that

ℓ

ℓ

P x1,...,xℓ ∈ S + Σ(A>nmed′ ) = 1 + O(V −1/4) τ2 i n=1+1−t bi

g(xi). (11.13)

i=1

Remarks. Note that A>Lmed = Amed. Note that by (11.8), (11.9), and (11.11) we have x1,...,xℓ ≍ V 2n−t, (11.14)

and so one typically expects the separation condition to be comfortably satisfied; see Lemma 12.4 for more details on this.

The following simple lemma will feature a few times in the proof.

- Lemma 11.3. Suppose that β,β′ are upper and lower walks. Suppose that β is T-positive up to length ⌈n/2⌉, and that the discrepancy D = D(β,β′) satisfies |D| ⩽ M/10. Let notation be as in (11.1). Then


n+1−t

bi − (n − t) ⩽ −21t1/2−η, (11.15) and

−2tmax ⩽

i=1

n−L

bi < n − L. (11.16)

i=1

Proof. From (11.1) and (11.2) we have that if m < ⌈n/2⌉ then

n−m

bi = n + D − (m + β(m)). (11.17)

i=1

We first prove (11.15). We certainly have t ⩽ tmax ≪ n/2, and so by (11.17) we have ni=1+1−t bi − (n − t) = D + 1 − β(t − 1).

For the lower bound, by the T-positive nature of the walk β it follows that D − β(t − 1) ⩾ D−T −(t−1)1/2+η, and the result follows from the parameter hierarchy (11.3), noting in particular that t ⩽ tmax.

For the upper bound, by the T-positive nature of β it follows that D−β(t−1) ⩽ D+T−(t−1)1/2−η, and the result again follows from the parameter hierarchy, specifically that t ⩾ tmin ≫ T, and all these parameters are sufficiently large in terms of M. For (11.16), an analogous proof works since L ≫ T. □

For the proof of Lemma 11.2 (which is rather lengthy), the plan is to first establish a weighted

version of (11.13) in which the number of representations in S +Σ(A⩾medn′ ) is counted. This is stated as Lemma 11.4 below. However, in practice the number of representations is essentially always

either 0 or 1, so we can later remove the weights. To do this rigorously a related technical result (Lemma 11.5 below) is required. The deduction of Lemma 11.2 from the weighted version is quite short and is given at the end of the section.

Fix S and n′ and define RA(x) to be the number of representations of x in S + Σ(A>nmed′ ), that is to say as a sum of a {0,1}-combination of the ai,j, n′ + 1 ⩽ i ⩽ n + 1 − t,j ∈ [bi], and an element of S.

- Lemma 11.4. With the notation and assumptions of Lemma 11.2, and with RA as just defined, we have


ℓ

ERA(x1)···RA(xℓ) = 1 + O(V −1/4) τ2 i n=1+1−t bi

g(x1)···g(xℓ). (11.18) Proof. Denote by Ξ the set of pairs (i,j) with n′ + 1 ⩽ i ⩽ n + 1 − t and j ∈ [bi]. Thus

n+1−t

bi. (11.19)

|Ξ| =

i=n′+1

Note for future reference that, since n′ ⩽ n − L and bi ⩾ 0 for all i,

n+1−t

|Ξ| ⩾

bi = (L + β(L)) − (t − 1) + β(t − 1) > L/2 (11.20)

i=n+1−L

by the T-positive property Definition 4.2 and the parameter hierarchy (11.3), and similarly, using the parameter hierarchy and that n′ ⩾ L, L < n/2 and |D| < M,

n+1−t

|Ξ| ⩽

bi = n + D − (t − 1) + β(t − 1) − (L − β′(L)) < n − L/2. (11.21)

i=L+1

Recall that by definition RA(x) is the number of pairs (ε,s) ∈ {0,1}Ξ × S with

εi,jai,j + s = x.

(i,j)∈Ξ

Thus

ε(i,ju)ai,j = xu − su,u ∈ [ℓ] . (11.22)

ERA(x1)···RA(xℓ) =

### P

ε(1),...,ε(ℓ)∈{0,1}Ξ s1,...,sℓ∈S

(i,j)∈Ξ

For each choice of ε(1),...,ε(ℓ) consider the ℓ-by-|Ξ| matrix M(ε) := (ε(i,ju))u∈[ℓ],(i,j)∈Ξ formed with the ε(u) as rows. We will consider the columns (ε(i,ju))u∈[ℓ] to be ordered by decreasing i and increasing j; thus the first V columns of M(ε) correspond to (i,j) = (n + 1 − t,j), j ∈ [bn+1−t] = [V ], these being the ones associated to the jump step.

To estimate the inner probability in (11.22), we will need to pay attention to the linear-algebraic structure of this matrix M(ε). To this end, recall the definition of rank profile from Section 9 and split the sum according to the rank profile. Write E(r;q1,...,qr) for the contribution of the terms with rp(ε(1),...,ε(ℓ)) = (r;q1,...,qr) to (11.22).

Our first main task (which is already somewhat lengthy) will be to show that only terms with r = ℓ and qℓ ⩽ V contribute importantly; to this end will show that

E(r;q1,...,qr) ≪ 2−Ω(V )2ℓ

(r;q1,...,qr) r<ℓ or r=ℓ and qℓ>V

n+1−t

i=1 bi−(n−t) . (11.23)

To see that this is indeed negligible compared to the stated bound in Lemma 11.2 we use the assumption that τ ⩾ V −1, the fact that g(xi) ≫ σ−1e−C(logV )1/2 (here we use the assumption (11.11)) and finally that σ ≍ V 1/22n−t (see (11.9)) and that V ≫ ℓ (from (11.3)).

The proof of the claim (11.23) will occupy the next few pages. Consider to begin with a fixed choice of ε(1),...,ε(ℓ) with rp(ε(1),...,ε(ℓ)) = (r;q1,...,qr). To bound the inner sum in (11.22),

### first note that

ε(i,ju)ai,j = x′u,u ∈ [ℓ] , (11.24)

ε(i,ju)ai,j = xu − su,u ∈ [ℓ] ⩽ |S|r sup

### P

### P

x′u

s1,...,sℓ∈S

(i,j)∈Ξ

(i,j)∈Ξ

since (due to the rank of M(ε) being r) for fixed xu the probability on the left can only be nonzero for at most |S|r choices of (s1,...,sℓ), since all sus are determined by some subset of r of them.

Consider the columns (ε(i,ju))u∈[ℓ] of M(ε) for (i,j) ∈ Ξ. We remind the reader that we order these first by decreasing i and then by increasing j. Let the columns corresponding to increments in the rank be (n + 1 − i1,j1),...,(n + 1 − ir,jr) where t ⩽ i1 ⩽ i2 ⩽ ··· ⩽ ir (note that these are completely determined by the rank profile). In particular observe that

n+1−t

- n+1−t
- n+2−id


bi < qd ⩽

bi, (11.25)

n+1−id

a relation we will use several times. We claim that P

r

ε(i,ju)ai,j = x′u,u ∈ [ℓ] ≪ V O(ℓ)

2id−n. (11.26)

d=1

(i,j)∈Ξ

To see this, first reveal all ai,j with (i,j) not one of the (n + 1 − id,jd), d ∈ [r]. The remaining elements an+1−i1,j1,...,an+1−ir,jr are then determined (with the ε and x′u fixed). The claim (11.26) then follows from the anticoncentration bound (5.8), unless n + 1 − id = t in which case we must instead use (11.7), which potentially gives rise to the V O(ℓ) factors.

Combining (11.24) and (11.26) gives

r

ε(i,ju)ai,j = xu − su,u ∈ [ℓ] ⩽ V O(ℓ)|S|r

2id−n. (11.27)

### P

s1,...,sℓ∈S

d=1

(i,j)∈Ξ

From this, Lemma 9.1 (i) and the definition of E(r;q1,...,qr) (just after (11.22)) we have

r

E(r;q1,...,qr) ≪ 2ℓ22r|Ξ|− rd=1 qd|S|rV O(ℓ)

2id−n

d=1

n+1−t

i=1 bi−(n−t) − rd=1(qd−id+t). (11.28) (Here, the 2ℓ2 has been absorbed into the V O(ℓ) term due to the assumption (11.3) on parameters, and for the final step we used (11.19) and the crude bound |S| ⩽ 2 n

≪ V O(ℓ)2r

′

i=1 bi, which follows from the assumption that τ ⩽ 1.) The bound (11.28) will be our key tool in the following analysis, the aim of which is to establish (11.23). Below we will use it examine the contributions to (11.23) from various rank profiles.

Suppose that d ∈ {1,...,r}. Using (11.25) we have

- n+1−t
- n+2−id


n

n

qd ⩾

bi − (t − 1 + β(t − 1)) ⩾

bi − 2tmax, (11.29)

bi =

n+2−id

n+2−id

using the T-positive nature of β (see Definition 4.2) and that t ⩽ tmax, T ≪ tmax.

Suppose first that id ⩽ 1 + ⌈n/2⌉. Then (11.29) gives qd ⩾ (id − 1) + β(id − 1) − 2tmax. By the T-positive nature of β (and since T ≪ tmax) it follows that qd ⩾ id + i1d/2−η − 3tmax, and therefore by Lemma D.2 we have qd ⩾ id + 12qd1/2−η − 3tmax.

Alternatively, suppose that id > 1 + ⌈n/2⌉. Then (11.29), the T-positive nature of β′ and the assumption that |D| ⩽ M/10 ≪ tmax give qd ⩾ D−1+id+β′(n−id)−2tmax ⩾ id+(n−id)1/2−η −

3tmax and so (n−qd) ⩽ (n−id)−(n−id)1/2−η+3tmax. Note that by (11.21) and since n+1−id ⩾ n′+1, we have n−qd,n−id > 0. By Lemma D.3 it follows that (n−qd) ⩽ (n−id)− 21(n−qd)1/2−η +6tmax.

In both cases we have

- 1

- 2


qd − id ⩾

min(qd,n − qd)1/2−η − O(tmax). (11.30) We now turn to the promised analysis of the contributions to (11.23) from various rank profiles. Step 1: the contribution from qr ⩾ t10max. Using the parameter hierarchy (11.3) it follows from

(11.28) and (11.30) that

n+1−t

r

E(r;q1,...,qr) ≪ 2O(ℓtmax)−21

d=1 min(qd,n−qd)1/2−η2r

i=1 bi−(n−t) . By (11.15) we may replace the preceding with

n+1−t

r

E(r;q1,...,qr) ≪ 2O(ℓtmax)−21

d=1 min(qd,n−qd)1/2−η2ℓ

i=1 bi−(n−t) .

We sum this over all rank profiles (r;q1,...,qr) with r ⩽ ℓ and maxd min(qd,n − qd) = q, i.e. all qd are either ⩽ q or ⩾ n−q, with at least one equality. The number of choices for these is ⩽ ℓ(2q)ℓ, so the contribution of them to (11.23) is

n+1−t

≪ ℓ(2q)ℓ2O(ℓtmax)−21q1/2−η2ℓ

i=1 bi−(n−t) . Taking into account the parameter hierarchy (11.3), the sum of this over q ⩾ t10max is ≪ 2−t4max2ℓ

n+1−t

i=1 bi−(n−t) ,

which is completely negligible in comparison to the desired bound (11.23) since tmax is much bigger than V .

To complete the analysis of Step 1, it suffices to show that if q < t10max then qr < t10max. By the definition of q, it suffices to show that qr < n − t10max. This follows immediately from (11.21) and the parameter hierarchy, since qr ⩽ |Ξ| ⩽ n − L/2 < n − t10max.

Step 2: The contribution to (11.23) from r < ℓ and qr ⩽ t10max. We consider further the structure of the ε(u). Suppose first that there are only r distinct ε(u). Then in order for the system of equations (i,j)∈Ξ ε(i,ju)ai,j = xu − su, u ∈ [ℓ] to have any solutions in the ai,j at all, we must have xu − su = xu′ − su′ for some u ̸= u′, and therefore |xu − xu′| ⩽ diam(S) ⩽ max(S) ⩽ 2n−L/2 by assumption. This is contrary to the separation assumption (11.12). Thus the contribution of these (ε(1),...,ε(ℓ)) to (11.22) is zero.

Therefore there are at least r +1 different ε(u). Suppose first that one of these is the zero vector. Then we have xu = su and so xu ⩽ max(S) ⩽ 2n−L/2. However, as noted in (11.14), we have xu ≍ V 2n−t, so there is a contradiction since L ≫ t.

Suppose, then, that there are at least r + 1 different nonzero ε(u). However, we showed in Lemma 9.1 (ii) that such matrices are relatively rare; there are at most 2ℓ22(r−101 )|Ξ| of them, noting that the condition |Ξ| ⩾ 10ℓ required in Lemma 9.1 (ii) is satisfied by (11.20) and the parameter hierarchy.

Using (11.27) (and recalling (11.22)), we see that the contribution of this case to the LHS of (11.23) is

r

n+1−t

i=1 bi−(n−t) 2−rt+ rd=1 id, (11.31)

≪ V O(ℓ)2(r−101 )|Ξ||S|r

2id−n ≪ 2−|Ξ|/10V O(ℓ)2r

d=1

′

where in the last step we used (11.19) and the crude bound |S| ⩽ 2 n

i=1 bi.

To bound this we use (11.30), which certainly implies that id ⩽ qd + O(tmax) ⩽ 2t10max, as well as n+1−t i=1 bi − (n − t) ⩾ −2tmax, which is the left-hand inequality in (11.15). This gives that (11.31)

is at most

≪ 2−|Ξ|/10V O(ℓ)2O(ℓt10max)2ℓ i⩽n+1−t bi−(n−t) . This is bounded by the RHS of (11.23) due to the fact that |Ξ| > L/2 (which is (11.20)) and the parameter hierachy, which has L vastly larger than V,ℓ and tmax, and so the analysis of Step 2 is complete.

Step 3: The contribution to (11.23) from r = ℓ and V < qℓ ⩽ t10max. Here we use that t is a V -jump step (Definition 8.17), which has not previously come in to the analysis. From (11.28) we see that it suffices to show that

2−ℓt+ ℓd=1(id−qd) ≪ 2−V . (11.32)

q1,...,qs⩽V V <qs+1,...,qℓ⩽t10max

for every s < ℓ (and then sum over the ℓ choices for s and the V O(ℓ) choices for q1,...,qs ⩽ V , always bearing in mind that ℓ is much smaller than V so that these factors contribute only 2o(V )). Now for d ⩽ s we have qd ⩽ V = bn+1−t and so id = t and hence −t + (id − qd) ⩽ 0, and so it suffices to show

2−t+(id−qd) ≪ 2−V (11.33)

V <qd⩽t10max

for all d = s + 1,...,ℓ, whereupon the desired bound (11.32) follows by taking the product over d (since by the assumption of Step 3 there is at least one d in the range). Fix such a d ∈ {s+1,...,ℓ}. We have id > t. By (11.30) we also have (comfortably) id < n/2, and so by (11.25) and (8.23) we have

- n+1−t
- n+2−id


n−t

bi = V + (id − 1) + β(id − 1) − t − β(t)

qd >

bi = V +

n+2−id

⩾ V + (id − 1 − t) + (id − 1 − t)1/2−2η. The LHS of (11.33) is therefore bounded above by

2−(id−1−t)1/2−2η ≪ 2−V

2−(id−t)1/2−2η. (11.34)

≪ 2−V

V <qd⩽t10max

V <qd⩽t10max

To bound this we additionally use (8.24) (and (11.25) again). This gives that

id−t

n+1−t

bi ⩽ V + O

qd ⩽

u2κ ⩽ V + O (id − t)1+2κ ,

n+1−id

u=1

and so

(id − t)1/2−2η ≫ (qd − V )(1/2−2η)/(1+2κ) ⩾ (qd − V )1/3 (since η = κ = 1001 ). Therefore (11.34) is bounded by

2−Ω((qd−V )1/3) ≪ 2−V

2−V

qd>V

and so the required bound (11.33) holds.

Steps 1,2 and 3 cover all cases in (11.23) and so the proof of that statement is now complete. The remaining argument required for the proof of Lemma 11.2 concerns the contribution to (11.22) from rp(ε(1),...,ε(ℓ)) = (ℓ;q1,...,qℓ) with qℓ ⩽ V . Equivalently, the matrix (ε(nu+1) −t,j)u∈[ℓ],j∈[V ] formed

from the first V columns of M(ε) has full rank ℓ. Beyond this point we will use only this property; the notion of rank profile will have no further role.

Before turning to the heart of the argument, we make one further reduction, which is to the case

where at least 4−ℓV of the V columns (ε(nu+1) −t,j)u∈[ℓ], j = 1,...,V are the basis vector ei ∈ Qℓ, for every i = 1,...,ℓ. In this situation we say that (ε(1),...,ε(ℓ)) is good. We claim that (with the ε sampled independently at random)

Pε((ε(1),...,ε(ℓ)) bad) ⩽ e−Ω(2−ℓV ). (11.35)

For fixed i ∈ {1,...,ℓ} denote by Xj the event that (ε(nu+1) −t,j)u∈[ℓ] = ei ∈ Qℓ, thus Xj is a Bernoulli random variable with mean p := 2−ℓ and X := Vj=1 Xj has the binomial Bi(V,p) distribution with mean pV . By Lemma F.1 (and since p ⩽ 21) we have P(X ⩽ p2V ) ⩽ P(|X − EX| ⩾ 12EX) ⩽ 2e−pV/12. Summing over i = 1,...,ℓ gives

Pε((ε(1),...,ε(ℓ)) bad) ⩽ 2ℓe−pV/12 ⩽ e−Ω(2−ℓV ), which is the desired claim (11.35).

Thus the number of (ε(1),...,ε(ℓ)) which are bad is ⩽ e−Ω(2−ℓV )2ℓ|Ξ|. For each such bad matrix, we bound the inner sum in (11.22) using (11.27), as before. Now we have r = ℓ and i1 = ··· = iℓ = t since all the rank jumps of M(ε) occur in the first V columns (with the ordering of columns described above, that is to say these first V columns are the ones indexed by (n+1−t,1),...,(n+1−t,V )). Thus we see that the contribution of these terms to (11.22) is

≪ e−Ω(2−ℓV )2ℓ|Ξ| · |S|ℓV O(ℓ)2ℓ(t−n). (11.36) By the parameter hierarchy we have e−Ω(2−ℓV )V O(ℓ) < e−V 1/2. Using the trivial bound |S| ⩽ 2 n

′

i=1 bi

and (11.19), we see that (11.36) is

n+1−t

≪ e−V 1/22ℓ

i=1 bi−(n−t) .

This is negligible compared to the stated bound in Lemma 11.2 by the discussion immediately following (11.23).

It remains to analyse the contribution to (11.22) from good tuples (ε(1),...,ε(ℓ)). To spell it out, we wish to show that

ℓ

ℓ

ε(i,ju)ai,j = xu − su,u ∈ [ℓ] = 1 + O(V −1/4) τ2 ni=1+1−t bi

g(xi). (11.37)

### P

i=1

(i,j)∈Ξ

(ε(1),...,ε(ℓ)) good s1,...,sℓ∈S

We now reduce to handling only the indices with i = n + 1 − t, that is to say ‘at the jump step’. To this end write

ε(i,ju)ai,j.

h(A,ε(u)) =

(i,j)∈Ξ i<n+1−t

Observe that using (5.7) and (8.24) that we have (for all choices of the ε(u), and deterministically in A)

|h(A,ε(u))| ≪ 2n−t

bn+1−t−u2−u ≪ 2n−t

u2κ2−u ≪ 2n−t. (11.38)

u⩾1

u⩾1

Write ε(jumpu) = (ε(nu+1) −t,j)j∈[V ] ∈ {0,1}V and also ajump,j := an+1−t,j. In the light of (11.38), and since |S| = τ2 n

′

### i=1 bi and |Ξ| = ni=+1n′−+1t bi = V + i n=−nt′+1 bi, in order to establish (11.37) it suffices

### to show

P

(ε(1)jump,...,ε(jumpℓ) ) good

V

ε(jumpu) ,jajump,j = x′u,u ∈ [ℓ] = 1 + O(V −1/4) 2V ℓ

j=1

ℓ

g(xi) (11.39)

i=1

uniformly for |x′u − xu| ≪ 2n−t, applying this bound with the choice x′u = xu − su − h(A,ε(u)) then summing over all su, all ε(i,ju), i < n+1−t,j ∈ [bi], and revealing the remaining elements (ai,j)i<n+1−t of (ai,j)(i,j)∈Ξ. (Here there is a slight abuse of notation in talking about (ε(1)jump,...,ε(jumpℓ) ) being good, a notion which was originally defined with reference to the full vectors ε(u) but in fact only depends on the ε(jumpu) .)

Now we observe that

ℓ

ℓ

g(xi) = (1 + O(V −1/4))

g(x′i). (11.40)

i=1

i=1

This follows fairly simply from the analytic properties of g(·). Indeed, using |x′i−xi| ≪ 2n−t and that σ ≍ V 1/22n−t, we have |σ−1(xi − µ) − σ−1(x′i − µ)| ≪ V −1/2, and so from the uniformly Lipschitz nature of e−x2/2 we have |g(xi) − g(x′i)| ≪ V −1/2σ−1. Therefore | ℓi=1 g(xi) − ℓi=1 g(x′i)| ≪ 2ℓσ−ℓV −1/2 ≪ V −1/3σ−ℓ. Finally, using that σ−1|x′i − µ| ⩽ σ−1|xi − µ| + O(V −1/2) ⩽ 2(log V )1/4 we have g(x′i) ⩾ (2π)−1/2σ−1e−2(logV )1/2, and so V −1/3σ−ℓ ≪ V −1/4 ℓi=1 g(x′i). This completes the proof of (11.40). Thus (11.39) follows from

P

(ε(1)jump,...,ε(jumpℓ) ) good

V

ε(jumpu) ,jajump,j = x′u,u ∈ [ℓ] = (1 + O(V −1/4))2V ℓ

j=1

ℓ

g(x′i), (11.41)

i=1

where we may assume σ−1|x′i − µ| ⩽ 2(log V )1/4. We phrase this task probabilistically, thus (11.41) is the statement that

V

ℓ

ε(jumpu) ,jajump,j = x′u,u ∈ [ℓ] = 1 + O(V −1/4)

g(x′i), (11.42)

P

j=1

i=1

where the tuple (ε(1)jump,··· ,ε(jumpℓ) ) is sampled uniformly from all good tuples, and the probability is taken over the random choices of the ε and the a. Here, we have noted that by our earlier estimate (11.35) on the number of bad tuples, and the parameter hierarchy (11.3), the sample space of ε tuples has size 1 − O(e−Ω(2−ℓV )) ℓ2V ℓ = (1 + O(V −1/2))2V ℓ.

As before we have g(x′i) ⩾ (2π)−1/2σ−1e−2(logV )1/2 and so in order to establish (11.42) it is enough to prove

V

ℓ

ε(jumpu) ,jajump,j = x′u,u ∈ [ℓ] =

g(x′i) + O(V −1/4σ−ℓ). (11.43)

P

j=1

i=1

We will prove this for all (x′u)u∈[ℓ] ∈ Rℓ. For notational brevity, until the end of the proof (of

- Lemma 11.4) we drop the jump subscripts; thus we write simply εj := εjump,j, aj := ajump,j. Define the random Rℓ-valued random variable


V

1 σ

ε(ju)aj − µ u∈[ℓ]. (11.44) Let

X :=

j=1

γ(x) := σ−ℓ(2π)−ℓ/2e−∥x∥22/2.

Then (dropping the dashes on the x′i) the desired bound (11.43) can be rephrased as the following local limit bound:

P(X = x) − γ(x) ≪ V −1/4σ−ℓ. (11.45)

sup

x∈((Z−µ)/σ)ℓ

As usual with statements of local limit type, we approach this task with a Fourier argument. By orthogonality of characters we have that

e−iθ·xE(eiθ·X)dθ.

P(X = x) = (2πσ)−ℓ

[−πσ,πσ]ℓ

Also, by direct calculation we have γ(x) = (2πσ)−ℓ

e−iθ·xe−∥θ∥22/2 dθ. Therefore the required bound (11.45) follows from

Rℓ

e−iθ·xe−∥θ∥22/2 dθ −

e−iθ·xE(eiθ·X)dθ ≪ V −1/4. (11.46)

Rℓ

[−πσ,πσ]ℓ

We prove this by establishing the following three estimates: sup

E(eiθ·X) − e−∥θ∥22/2 ≪ V −2/7; (11.47)

θ∈[− log V,log V ]ℓ

e−∥θ∥22/2 dθ ≪ V −10; (11.48) and

Rℓ\[− log V,log V ]ℓ

|E(eiθ·X)|dθ ≪ V −10. (11.49)

[−πσ,πσ]ℓ\[− log V,log V ]ℓ

These three estimates are easily seen to imply (11.46), using here that (2log V )ℓ = V o(1) to handle the contribution from ∥θ∥∞ ⩽ log V .

Proof of (11.47). This is essentially a standard computation associated with proving a multivariate

central limit theorem. Since the proportion (ε(1)jump,...,ε(jumpℓ) ) of tuples in ({0,1}V )ℓ that are bad is exponentially small in V (see (11.35)), in this range we may for the purposes of proving (11.47) drop the ‘good’ condition; that is to say it suffices to prove (11.47) with X replaced by the variable

X˜, defined as in (11.44) but with the ε(ju) sampled independently at random from {0,1}. Let θ = (θ1,...,θℓ) and for notational convenience in the rest of the proof write e(ξ) := eiξ. Assume (as in the estimate (11.47) we are trying to prove) that |θu| ⩽ log V for all u.

From this definition and (11.8) we have

E(eiX˜·θ) = Eε,ae

ℓ

1 σ

u=1

V

ℓ

= Ea

u=1

j=1

V

(ε(ju)aj − 12µj)θu

j=1

e

V

ℓ

- 1

- 2σ


(aj − µj)θu Eε

e

u=1

j=1

1 σ

(ε(ju) − 12)ajθu . (11.50)

To estimate the inner average over the ε(ju) we use that e(ξ) + e(−ξ) = e−ξ2/2(1 + O(|ξ|3)) (11.51)

- 1

- 2


for |ξ| ⩽ 1. We apply this with ξ = ajθu/2σ. Note (see (11.9)) that aj ≍ 2n−t, |θu| ⩽ log V and σ ≍ V 1/22n−t, so |ξ| ≪ V −1/2 log V . Therefore substituting (11.51) into (11.50) gives

V

ℓ

V

ℓ

a2jθu2 8σ2

- 1

- 2σ


Ea(eiX˜·θ) = E(1 + η(a))

(aj − µj)θu · exp −

e

u=1

u=1

j=1

j=1

where ∥η∥∞ ≪ ℓV (V −1/2 log V )3 ≪ V −1/2+o(1). Now from (11.8) and (11.9) we have a2j = (1 + O(V −1/3))µ2j = (1 + O(V −1/3))Ea2j and so Vj=1 a2j = 4σ2(1 + O(V −1/3)); since ℓu=1 θu2 = ∥θ∥22, this gives

V

ℓ

1 2σ

E(eiX˜·θ) = e−∥θ∥22/2Ea(1 + η′(a))

(aj − µj)θu

e

u=1

j=1

where ∥η′∥∞ ≪ ℓV −1/3 log V ≪ V −2/7. Consequently

V

ℓ

- 1

- 2σ


E(eiX˜·θ) = O(V −2/7) + e−∥θ∥22/2Ea

(aj − µj)θu .

e

u=1

j=1

Hence, in order to prove the desired result (11.47) it suffices to prove that

V

ℓ

- 1

- 2σ


(aj − µj)θu = 1 + O(V −1/2). (11.52)

E

e

u=1

j=1

Note that the LHS here is

V

Eaje λ(aj − µj) ,

j=1

where λ := 21σ ℓu=1 θu. By (11.9) and the fact that |θu| ⩽ log V we have |λ(aj − µj)| ≪ (ℓlog V )V −5/6 ≪ V −3/4 ≪ 1 and so

e λ(aj − µj) = 1 + iλ(aj − µj) + O(λ2(aj − µj)2); taking expectations gives

Eaje λ(aj − µj) = 1 + O(λ2(aj − µj)2) = 1 + O(V −3/2), and (11.52) follows by taking the product over j = 1,...,V .

- Proof of (11.48). This is a straightforward exercise using t>r e−t2/2dt ⩽ r−1 t>r te−t2/2dt =

r−1e−r2/2.

- Proof of (11.49). We split into dyadic ranges K ⩽ ∥θ∥∞ < 2K, K ∈ {2i log V : i = 0,1,...}.


The region of integration in (11.49) corresponding to such a range has volume ⩽ (4K)ℓ and so it suffices to show the pointwise bound

|E(eiX·θ)| ≪ (8K)−ℓV −10 (11.53) uniformly for K ⩽ ∥θ∥∞ < 2K.

We first consider the smaller ranges log V ⩽ K ≪ V 1/2/log V (say). As in the analysis of (11.47) it suffices to prove (11.53) with X replaced by X˜, defined as in (11.44) but without the ‘good’ condition, that is to say with the ε(ju) sampled independently from {0,1}. From the definition (11.44) and the triangle inequality we have

E(eiX˜·θ) ⩽ Ea Eεe

ℓ

1 σ

u=1

V

ℓ

V

ε(ju)ajθu = Ea

u=1

j=1

j=1

1 + e(θuaj/σ) 2

.

Note that, since aj ≍ 2n−t, σ ≍ V 1/22n−t and |θu| = o(V 1/2), the arguments of the exponentials here are o(1) and we may use the inequality 12|1+e(ξ)| ⩽ e−|ξ|2/8 to give |E(eiX˜·θ)| ⩽ e−Ω(K2). This is bounded as in (11.53) for K ⩾ log V , using here that ℓ is much smaller than V by the parameter hierarchy.

Now we turn to the larger values K ⩾ V 1/2/log V . Here, we apply the triangle inequality the other way around, obtaining

V

ℓ

1 σ

ε(ju)ajθu .

E(eiX·θ) ⩽ E(ε(1),...,ε(ℓ)) good Eae

u=1

j=1

For j ∈ [V ] denote by ϕj the characteristic function ϕj(ξ) := Ee(ξaj). Then the preceding may be rewritten as

ℓ

V

1 σ

ε(ju)θu . Consequently,

E(eiX·θ) ⩽ E(ε(1),...,ε(ℓ)) good

ϕj

u=1

j=1

ℓ

−ℓV ⩽ sup

−ℓV : (11.54)

ϕj(θi/σ) 4

ϕj(∥θ∥∞/σ) 4

E(eiX·θ) ⩽

sup

j

j

i=1

this follows by picking out just those indices j for which (ε(ju))u∈[ℓ] = ei ∈ Qℓ, for i = 1,...,ℓ; by the definition of ‘good’ there are at least 4−ℓV such j for each value of i. We may use the trivial bound |ϕj(θu/σ)| ⩽ 1 everywhere else.

To obtain estimates for the quantities ϕj(∥θ∥∞/σ), first recall from (11.6) how aj is distributed. With the notation used there (recalling that aj = ajump,j = an+1−t,j), it follows that

α1 x1

α0 x0 −

α1 x1

α0 x0

E(eiξX),

e(ξx1) + 1 −

e(ξx0) +

ϕj(ξ) =

where X is the random variable taking values in (x0,x1) ⊂ Z, with P(X = x) ∝ 1/x. In our context α0/x0, α1/x1 are minuscule and so we certainly have

|ϕj(ξ)| ⩽ 21 1 + |E(eiξX)| . We can estimate |E(eiξX)| using Lemma C.1, which is designed for this purpose. We take N = x0, R = x1 − x0 + 1 and ξ = ∥θ∥∞/σ. One may easily check that N ≍ 2n−t and R ≍ V −1/32n−t. Since σ ≍ V 1/22n−t, we have ξR ≍ ∥θ∥∞V −5/6 ≍ KV −5/6. Lemma C.1 then gives

1 − cK2V −5/3 K ⩽ CV 5/6;

ϕj(∥θ∥∞/σ) ⩽

(11.55)

3 4 K ⩾ CV 5/6.

Here, c,C are absolute constants with 0 < c < 1 < C (independent of j, and c may be smaller than the constant in Lemma C.1).

For V 1/2/log V ⩽ K ⩽ CV 5/6 we use the first bound in (11.55), obtaining from (11.54) that |E(eiX·θ)| ≪ (1 − cVlog−22/V3)4−ℓV ≪ e−V 1/4 which is certainly a bound of strength (11.53). For K ⩾ CV 5/6 we instead use the second bound in (11.55) getting |E(eiX·θ)| ≪ (34)4−ℓV , which is again (massively) of strength (11.53).

We have now completed the proof of the three statements (11.47) to (11.49), and hence (11.46). Tracing back through the successive reductions (11.45), (11.41), (11.39) and (11.37), we see that the contribution to (11.22) from the good tuples (ε(1),...,ε(ℓ)) provides the main term in (11.18), and the proof of Lemma 11.4 is (at last) complete. □

As previously stated, we will also require the following technical estimate, which will be used to deduce the unweighted Lemma 11.2 from the version Lemma 11.4 with weights.

- Lemma 11.5. Let the notation and setup be as in Lemma 11.2 and, as in Lemma 11.4, let RA(x) be the number of representations of x in S + Σ(A>nmed′ ). Then we have


ERA(x1)RA(x2)···RA(xℓ)(RA(xℓ) − 1) ⩽ V O(ℓ)

2 i n=1+1−t bi σ

ℓ+1

.

Proof. The proof goes along similar lines to (part of) the proof of Lemma 11.4. In particular, define Ξ in the same way. We have the following modification of (11.22):

ERA(x1)···RA(xℓ)(RA(xℓ) − 1)

ε(i,ju)ai,j = xu − su,u ∈ [ℓ + 1] , (11.56)

### P

=

s1,...,sℓ+1∈S

(i,j)∈Ξ

ε(1),...,ε(ℓ+1)∈{0,1}Ξ ε(ℓ)̸=ε(ℓ+1)

where xℓ+1 := xℓ. This follows by observing that RA(xℓ)(RA(xℓ) − 1) counts pairs of distinct representations of xℓ in S + Σ(A>nmed′ ).

We now proceed completely analogously to the initial steps in the proof of Lemma 11.4, simply changing ℓ to ℓ + 1 in many places. In particular the first main task is to show

E(r;q1,...,qr) ≪ 2−Ω(V )2(ℓ+1)

(r;q1,...,qr) r<ℓ+1 or r=ℓ+1 and qℓ+1>V

n+1−t

i=1 bi−(n−t) . (11.57)

which is (11.23) with ℓ replaced by ℓ+1. Key tools for doing this will be (11.28) and (11.30), which hold verbatim.

The analysis of Steps 1 and 3 proceeds essentially identically, changing ℓ to ℓ + 1 a few times. The initial part of Step 2 requires a very small modification, in that if r < ℓ+1 and there are only r distinct ε(u), then we must have ε(u) = ε(u′) for some pair (u,u′) with u < u′, and moreover we cannot have (u,u′) = (ℓ,ℓ + 1) due to the stipulation that ε(ℓ) ̸= ε(ℓ+1) in the range of summation in (11.56). The rest of that argument proceeds as before, once again switching some instances of ℓ to ℓ + 1.

This concludes the proof of (11.57). Recalling that σ ≍ V 1/22n−t, to conclude the proof of

- Lemma 11.5 we need only show that


E(ℓ+1;q1,...,qℓ+1) ≪ V O(ℓ)2(ℓ+1)

q1,...,qℓ+1⩽V

n+1−t

i=1 bi−(n−t) .

Since the number of possibilities for q1,...,qℓ+1 is V O(ℓ), it suffices to prove the same bound for each E(ℓ+1;q1,...,qℓ+1) individually. For this we use (11.28), where we can take all id to be equal to t since q1,...,qℓ+1 ⩽ V . This gives exactly the desired bound (in fact with an extra factor 2− ℓd+1=1 qd ⩽ 1). This concludes the proof of Lemma 11.5. □

The final task of this section is to establish the key result Lemma 11.2.

med) ⩽ RA(x) pointwise. For the lower bound, we use that 1x∈S+Σ(A>n′

Proof of Lemma 11.2. The upper bound is immediate from Lemma 11.4 since 1x∈S+Σ(A>n′

med) ⩾ RA(x)1RA(x)∈{0,1}, and so

ℓ

P x1,...,xℓ ∈ S + Σ(A>nmed′ ) ⩾ ERA(x1)···RA(xℓ) − ERA(x1)···RA(xℓ) 1 −

1RA(xi)∈{0,1} .

i=1

However

ERA(x1)···RA(xℓ) 1 −

ℓ

ℓ

1RA(xi)∈{0,1} ⩽ ERA(x1)···RA(xℓ)

1RA(xi)>1

i=1

i=1

ℓ

⩽

ERA(x1)···RA(xℓ)(RA(xi) − 1).

i=1

Using Lemma 11.5, and noting that g(xi) ⩾ V −o(1)/σ due to the hypotheses on the xi, comparison with Lemma 11.4 shows that it is enough to prove that

2 i n=1+1−t bi σ ≪ V −1/4.

V O(ℓ)

This follows using σ ≍ V 1/22n−t and the upper bound in (11.15), together with the parameter hierarchy (in particular, that t ⩾ tmin ≫ V ). □

12. Inclusion–exclusion

In this section we carry out the inclusion-exclusion analysis hinted at in the introduction to Section 11, using Lemma 11.2 as our main tool. The following is the main result of the section.

As in the previous section, we have a main truncation parameter M, key further thresholds R(M), T(M) and L(M) as described in Definition 11.1, and technical auxiliary thresholds ℓ∗(M), V (M), tmin(M), tmax(M) as in the hierarchy (11.3).

The reader may also wish to recall the definitions of the random variables ϱ∗u|β(ℓ), τx∗|β′(ℓ), which may be found in Definitions 6.1 and 7.1. Here is the main result of the section.

Proposition 12.1. Fix upper and lower walks β,β′ which are R-bounded and T-positive up to lengths ⌈n/2⌉, ⌊n/2⌋, and which have min1⩽i⩽⌈n/2⌉ β(i),min1⩽i⩽⌊n/2⌋ β′(i) ⩾ −M. Write D = D(β,β′) := β(⌈n/2⌉) − β′(⌊n/2⌋) and suppose that |D| ⩽ M/10. Suppose that β has a V (M)-jump step at some t ∈ [tmin(M),tmax(M)]. Then

P k ∈ Σ(A | β,β′) = 1 − Eexp − 2D−ξϱ∗u|β(L(M))τx∗|β′(L(M)) + O(ℓ∗(M)−1). Remark. Note that the final expression is independent of the location of the jump step t.

To avoid excessively cumbersome notation, we drop the explicit mention of M from the parameters T,tmin,tmax,V,L,ℓ∗, as we did in the last section. For the rest of the section we will assume that β,β′ satisfy the hypotheses of Proposition 12.1 without further comment; this applies in particular to the subsidiary Lemma 12.2.

For the initial analysis notation will be as in Section 11. Specifically, the reader should recall (11.1), the parameter hierarchy (11.3) and the fact that we are conditioning to β = β,β′ = β′ and also to a fixed choice of the jump distribution f = f. In particular, from this point onwards in the section we write A as shorthand for (A | β = β,β′ = β′,f = f).

Associated to this data are the parameters µ,σ2 defined in (11.8), and the Gaussian density g(x) with mean µ and variance σ2 as in (11.10).

As in (11.5) we will divide A as Asmall∪Amed∪Alarge. For much of the section we will additionally condition to fixed choices of Asmall = (ai,j)1⩽i⩽L;j∈[bi] and Alarge = (ai,j)n+1−t<i⩽n;j∈[bi] and sample only Amed at random, with the randomly selected object being denoted by bold font as usual. Since (5.7) holds deterministically, we always assume

ai,j ≍ 2i.

- 12.1. Consequences of Section 11. In the proof of Proposition 12.1 we will make crucial use of the main result of the last section, Lemma 11.2. We record the consequences we need here. For notational clarity in what follows we will write E ≈ E′ as shorthand for E′ = (1 + O(V −Ω(1)))E. Recall that Ω(1) denotes a small positive constant, which may change from line to line.


First (in Lemma 11.2) take n′ = L and S := Σ(Asmall). As remarked after the statement of

- Lemma 11.2, in this case we have A>nmed′ = Amed. The condition max(S) ⩽ 2n−L/2 is satisfied by a large margin. Write τ(Asmall) for the parameter τ in this application of Lemma 11.2, that is to say


τ(Asmall) = 2− Li=1 bi|Σ(Asmall)|. (12.1)

Here the notation Σ(S) is as defined in Definition 2.1. Assume in what follows that τ(Asmall) ⩾ V −1. Suppose that ℓ ⩽ ℓ∗ and that x1,...,xℓ satisfy (11.11) and the separation condition (11.12). Then all the hypotheses of Lemma 11.2 hold and the conclusion (11.13) is that

ℓ

P x1,...,xℓ ∈ Σ(Amed) + Σ(Asmall) ≈ τ(Asmall)2 ni=1+1−t bi ℓ

g(xi) (12.2)

i=1

(where g is a Gaussian density with mean µ and variance σ2 as in (11.10).) Comparing this with the case ℓ = 1, we immediately obtain the key almost-independence statement

P x1,...,xℓ ∈ Σ(Amed) + Σ(Asmall) ≈

ℓ

P xi ∈ Σ(Amed) + Σ(Asmall) , (12.3)

i=1

where here we used the fact that (1+V −Ω(1))ℓ = 1+O(V −Ω(1)) due to the hierarchy of parameters. This will be the first key consequence of Lemma 11.2 that we will use later.

The second important consequence will be an alternative expression for the probabilities on the right in (12.3). For this, note first that the case ℓ = 1 of (12.2) gives that

P x ∈ Σ(Amed) + Σ(Asmall) ≈ τ(Asmall)2 ni=1+1−t big(x), (12.4) still under the assumption that τ(Asmall) ⩾ V −1 and also that

|x − µ| ⩽ (log V )1/4σ. (12.5) (The separation condition (11.12) is redundant.) Leaving this aside temporarily, we now use

- Lemma 11.2 differently in order to obtain an alternative expression for the right-hand side of (12.4).


′

Now take n′ = n − L and S to be any subset of [2−Lk] of size 2 n

i=1 bi. That such a set exists follows from (11.16) (recalling that k ⩾ 2n). The condition max(S) ⩽ 2n−L/2 is again satisfied quite comfortably (noting that k ≍ 2n), and in this case τ = 1. Take ℓ = 1 in (11.13), obtaining (for any S)

P(x ∈ S + Σ(A>nmed−L)) ≈ 2 i n=1+1−t big(x). Comparing with (12.4) gives

P x ∈ Σ(Amed) + Σ(Asmall) ≈ τ(Asmall)P(x ∈ S + Σ(A>nmed−L)). (12.6) We claim that

P(x ∈ S + Σ(A>nmed−L)) ≈ ERA(x). (12.7) where RA denotes the number of representations of x in S + Σ(A>nmed−L) (as defined just prior to Lemma 11.4). First note that the LHS of (12.7) is simply E1RA(x)⩾1, so clearly P(x ∈ S + Σ(A>nmed−L)) ⩽ ERA(x). Obtaining a bound in the other direction is only slightly more involved. By employing the inequality R − R(R − 1) ⩽ 1R⩾1, it suffices to show that

ERA(x)(RA(x) − 1) ≪ V −Ω(1)ERA(x). (12.8)

To see that this is so, we note that Lemma 11.4 (together with the lower bound τ(Asmall) ⩾ V −1, (11.9) and (12.5)) tells us that ERA(x) ≫ V −12 i n=1+1−t big(x) ≫ V −O(1)2 ni=1+1−t bi−(n−t), whilst

- Lemma 11.5 gives ERA(x)(RA(x) − 1) ≪ V O(1)22

n+1−t

i=1 bi−(n−t) . The bound (12.8) then follows using (11.15) and the parameter hierarchy, and this concludes the proof of the claim (12.7).

Combining (12.6) and (12.7) evidently gives

P x ∈ Σ(Amed) + Σ(Asmall) ≈ τ(Asmall)ERA(x). Expanding out the expectation term on the RHS we obtain

P x ∈ Σ(Amed) + Σ(Asmall) ≈ τ(Asmall)

ε′

P x ∈ S +

n−L<i⩽n+1−t j∈[bi]

ε′i,jai,j , (12.9)

where ε′ = (ε′i,j)n−L<i⩽n+1−t,j∈[bi] ranges over all tuples with ε′i,j ∈ {0,1}, and the use of ε′ as a dummy variable is to avoid conflict later. Recall that S is an arbitrary subset of [2−Lk] of size

2 ni=1−L bi. Noting that the LHS of (12.9) is independent of S, we average over all such S and thereby obtain (assuming τ(Asmall) ⩾ 1/V and (12.5)) that

P x ∈ Σ(Amed) + Σ(Asmall) ≈ τ(Asmall)2 i⩽n−L bi(2−Lk)−1

ε′

P(x ∈ [2−Lk] +

n−L<i⩽n+1−t j∈[bi]

ε′i,jai,j). (12.10)

This is the second key result that we will require in the proof of Proposition 12.1.

12.2. The Poisson paradigm. In this section we establish the key ingredient in the proof of Proposition 12.1, which we state as Lemma 12.2 below. We retain the notation in force so far, in particular that we are conditioning to fixed choices of Asmall,Alarge. In what follows we write ε := (εi,j)n+1−t<i⩽n;j∈[bi] and denote

E = E(Alarge) := ε : k −

n+1−t<i⩽n;j∈[bi]

εi,jai,j − µ ⩽ (log V )1/4σ (12.11)

and

Σ′(Alarge) := {

n+1−t<i⩽n;j∈[bi]

εi,jai,j : ε ∈ E(Alarge)}.

Here, µ,σ are defined in (11.8). In particular, it is important to note that the definition of E depends on the jump distribution vector f that we conditioned to at the beginning of the last section, and not just on the walks β,β′.

- Lemma 12.2. Let β,β′ be as in the statement of Proposition 12.1. Let Asmall = (ai,j)1⩽i⩽L;j∈[bi] and Alarge = (ai,j)n+1−t<i⩽n;j∈[bi] be multisets. Define E = E(Alarge) as in (12.11). Suppose that τ(Asmall) ⩾ 1/V and that Alarge satisfies the following separation condition: as ε ranges


over {0,1} n+1−t<i⩽n bi, the numbers n+1−t<i⩽n;j∈[b

i] εi,jai,j are 2n−L/2-separated. Then, writing Amed := (ai,j)L+1⩽i⩽n+1−t;j∈[bi] (chosen at random), we have

P(k ∈ Σ′(Alarge) + Σ(Amed) + Σ(Asmall)) = 1 − e−S(Asmall,Alarge) + O(ℓ−∗ 1), where

P(Xε), (12.12)

S(Asmall,Alarge) :=

ε∈E

with Xε the event that

εi,jai,j ∈ Σ(Amed) + Σ(Asmall). (12.13)

k −

n+1−t<i⩽n;j∈[bi]

Proof. In this proof all instances of P are probabilities with respect to the random choice of Amed. We retain the convention that E ≈ E′ is shorthand for E′ = (1 + O(V −Ω(1)))E. Write S :=

S(Asmall,Alarge) for brevity. We have P k ∈ Σ′(Alarge) + Σ(Amed) + Σ(Asmall) = P

Xε . (12.14)

ε∈E

Let ε(1),...,ε(ℓ) ∈ E be distinct. We claim that (12.3) holds with the xu being the quantities k − n+1−t<i⩽n;j∈[bi] ε(i,ju)ai,j. Indeed, the latter statement was proven assuming that the xu satisfy

- (11.11) and the separation condition (11.12). In the present context the first of these conditions is a consequence of the restriction to ε ∈ E, and the separation condition is one of the assumptions of


- Lemma 12.2. The claim follows. This instance of (12.3) gives the key almost-independence statement


ℓ

ℓ

P(Xε(u)), (12.15)

P

Xε(u) ≈

u=1

u=1

provided that ℓ ⩽ ℓ∗.

We pause to show that the P(Xε) are individually rather small. To do this we first note by the definition (12.13) of Xε and (12.10) we have

n+1−t

P(Xε) ≈ τ(Asmall)2 ni=1−L bi(2−Lk)−1

ε′i,jai,j ∈ [2−Lk] , (12.16)

P k −

εi,jai,j −

ε′

i>n+1−t j∈[bi]

i=n+1−L j∈[bi]

where (as before) ε′ = (ε′i,j)n+1−L⩽i⩽n+1−t;j∈[bi]. Now if ε ∈ E and if, for some ε′, the inner probability is not zero then for some instance (ai,j)n+1−L⩽i⩽n+1−t;j∈[bi] of (ai,j)n+1−L⩽i⩽n+1−t;j∈[bi] we have

n+1−t

ε′i,jai,j ⩾ µ − 2−Lk − (log V )1/4σ. (12.17)

i=n+1−L j∈[bi]

We claim that this forces at least one of the ε′n+1−t,u (that is, associated to the jump step) to not be zero. To see this claim, we may use (5.7) and (8.24) to bound

n−t

n−t

L

bi2i ≪ 2n−t

(1 + i2κ)2−i ≪ 2n−t. (12.18)

ε′i,jai,j ≪

i=n+1−L j∈[bi]

i=n+1−L

i=1

However, recalling that µ ≍ V 2n−t, k ≍ 2n, σ ≍ V 1/22n−t and L ≫ t, the RHS of (12.17) is ≫ V 2n−t, which is much larger than (12.18); this establishes the claim.

Using the anticoncentration estimate (11.7) (revealing all ai,j other than an+1−t,u), we have that

n+1−t

ε′i,jai,j = x ≪ V 1/32t−n,

P k −

εi,jai,j −

i>n+1−t j∈[bi]

i=n+1−L j∈[bi]

uniformly for x ∈ [2−Lk], ε′, and ε ∈ E.

n+1−t

i=n+1−L bi choices of ε′ and using the trivial bound τ(Asmall) ⩽ 1 and the upper bound in (11.15) we obtain

Applying this to (12.16), summing over the 2

i=n+1−L bi · V 1/32t−n ≪ V 1/32−21t1/4 ⩽ 2−13t1min/4 . (12.19) We set this aside for later use, and resume the main line of argument. We divide into two cases according to the value of S = S(Asmall,Alarge).

n+1−t

P(Xε) ≪ 2 ni=1−L bi · 2

Case 1: S ⩽ ℓ∗/100. This is the main case. To estimate the RHS of (12.14) we use the inclusionexclusion principle (“Poisson paradigm”). Let ℓ0 ∈ [ℓ∗/2,ℓ∗] be even. Then by the Bonferroni inequalities we have

1 − P

By (12.15) it follows that

ℓ

Xε ⩽

(−1)ℓP(

0⩽ℓ⩽ℓ0 ε(1)<···<ε(ℓ) ε(1),...,ε(ℓ)∈E

u=1

ε∈E

Xε(u)).

ℓ

Xε ⩽

(1 + O(V −Ω(1)))

(−1)ℓ

1−P

P(Xε(u))

0⩽ℓ⩽ℓ0

u=1

ε∈E

ε(1)<···<ε(ℓ) ε(1),...,ε(ℓ)∈E

ℓ

ℓ

⩽

P(Xε(u)) + O(V −Ω(1))

(−1)ℓ

P(Xε(u)). (12.20)

0⩽ℓ⩽ℓ0

0⩽ℓ⩽ℓ0 ε(1)<···<ε(ℓ) ε(1),...,ε(ℓ)∈E

u=1

u=1

ε(1)<···<ε(ℓ) ε(1),...,ε(ℓ)∈E

- 0
- 1 ℓ! ε P(Xε) ℓ < V −Ω(1)eS < e−ℓ∗ (pro-


The error term here is bounded by ≪ V −Ω(1) 0⩽ℓ⩽ℓ vided ℓ∗ is small enough in terms of V ), and so (12.20) implies that

ℓ

Xε ⩽

P(Xε(u)) + O(e−ℓ∗). (12.21)

(−1)ℓ

### 1 − P

0⩽ℓ⩽ℓ0

u=1

ε∈E

ε(1)<···<ε(ℓ) ε(1),...,ε(ℓ)∈E

We also have

ℓ0

1 ℓ!

1 ℓ!

eS ℓ0

e 50 Also, (12.19) and Lemma D.1 give that

- 1

- 2ℓ∗ ≪ e−ℓ∗. (12.22)


ℓ0 ≪

Sℓ ⩽

e−S −

(−1)ℓ

Sℓ ≪

ℓ=0

ℓ>ℓ0

ℓ

P(Xε(u)) ⩽ ℓ(ℓ − 1)2−13t1min/4 Sℓ−1 < 2−14t1min/4 < e−10ℓ∗. (12.23)

Sℓ − ℓ!

u=1

ε(1)<···<ε(ℓ) ε(1),...,ε(ℓ)∈E

Combining (12.21) to (12.23) with (12.14) gives P k ∈ Σ′(Alarge) + Σ(Amed) + Σ(Asmall) ⩾ 1 − e−S(Asmall,Alarge) + O(e−ℓ∗).

A corresponding upper bound follows using the lower bound Bonferroni inequalities (taking ℓ0 odd) in an entirely analogous manner. This completes the proof of Lemma 12.2 in Case 1.

Case 2: S > ℓ∗/100. For this we use a second moment method. We have E

(1Xε − P(Xε)) 2 =

P(Xε ∩ Xε′) − S2. (12.24)

ε,ε′∈E

ε∈E

Now by (12.15) with ℓ = 2 we have when ε ̸= ε′ that

P(Xε ∩ Xε′) = 1 + O(V −Ω(1)) P(Xε)P(Xε′). Summing over ε,ε′ gives

P(Xε ∩ Xε′) = 1 + O(V −Ω(1)) S2 −

P(Xε)2 + S.

ε,ε′∈E

ε∈E

Therefore from (12.24) we have E

(1Xε − P(Xε)) 2 ≪ S + V −Ω(1)S2.

ε∈E

It follows by Markov’s inequality that the complement of ε Xε, that is to say the event ε 1Xε = 0, has probability ≪ S−1 + V −Ω(1) ≪ ℓ−∗ 1.

This concludes the analysis of Case 2 and hence the proof of Lemma 12.2. □

- 12.3. Proof of the main result. We now turn to the task of proving the main result of the section, Proposition 12.1. To do this, we will use Lemma 12.2 and undo the conditioning to Asmall = Asmall, Alarge = Alarge. We first need to establish that the application of Lemma 12.2 is generically valid. That this is so is the content of Lemmas 12.3 and 12.4 below.


- Lemma 12.3. Define τ(Asmall) as in (12.1). Then, with the setup as in Proposition 12.1, the probability that τ(Asmall) ⩽ 1/V is at most 2T/V .


Proof. Writing rA(x) for the multiplicity of x in Σ(Asmall), we have τ(Asmall) = 2− Li=1 bi Supp(rA). By Cauchy–Schwarz it follows that if |τ(Asmall)| ⩽ 1/V then

rA(x)2 ⩾ 2 Li=1 biV. (12.25) On the other hand, we have

x

ε′i,jai,j ,

rA(x)2 =

E

### P

### εi,jai,j =

1⩽i⩽L;j∈[bi]

1⩽i⩽L;j∈[bi]

ε,ε′

x

where now ε = (εi,j)1⩽i⩽L;j∈[bi], ε′ = (ε′i,j)1⩽i⩽L;j∈[bi]. For each pair (ε,ε′) in the above sum, consider the largest ℓ for which there is some m (which we take minimal) such that εℓ,m ̸= ε′ℓ,m. Then by revealing all ai,j except aℓ,m, we see from (5.8) that the inner probability is ≪ 2−ℓ.

The number of pairs (ε,ε′) corresponding to a given (ℓ,m) is 22 Li=1 bi− Li=ℓ+1 bi−(m−1). Thus we have

L

22 Li=1 bi− Li=ℓ+1 bi−(m−1)

2−ℓ

rA(x)2 ≪

E

x

ℓ=1

m∈[bℓ]

L

L

2−ℓ+2 Li=1 bi− Li=ℓ+1 bi = 2 Li=1 bi

2−β′(ℓ).

≪

ℓ=1

ℓ=1

Since β′ is a T-positive walk, β′(ℓ) ⩾ −T + ℓ1/4 and so it follows that E

rA(x)2 ≪ 2T+ Li=1 bi. By Markov,

x

rA(x)2 ⩾ 2 Li=1 biV ≪ 2T/V, and so the lemma follows from the remarks leading to (12.25). □

P

x

The next lemma controls the separation property required in Lemma 12.2. Here, very crude estimates suffice.

- Lemma 12.4. With the setup in Proposition 12.1, the probability that there exist distinct ε =


(εi,j)n+1−t<i⩽n;j∈[bi] and ε′ = (ε′i,j)n+1−t<i⩽n;j∈[bi] for which i,j(εi,j − ε′i,j)ai,j ⩽ 2n−L/2 is ⩽ 2−L/8.

Proof. The number of pairs ε,ε′ is < 22 ni=n+2−t bi < 2L/4, using the R-boundedness of β and the parameter hierarchy for the second bound. For each pair, choose some index with εu,v ̸= ε′u,v, and reveal all ai,j except for au,v. By (5.8), P n+1−t<i⩽n;j∈[b

i](εi,j − ε′i,j)ai,j ⩽ 2n−L/2 ≪ 2t−n · 2n−L/2. Summing over all pairs ε,ε′ and using the parameter hierarchy again gives the result. □

Now we begin the proof of Proposition 12.1 in earnest. From Lemma 12.2 we have P k ∈ Σ′(Alarge) + Σ(Amed) + Σ(Asmall) = (1 − e−S(Asmall,Alarge))1τ(Asmall)⩾1/V, Alarge∈S

+ O 1τ(Asmall)⩽1/V + 1Alarge∈/S + ℓ−∗ 1 , (12.26) where S denotes the separation condition in the statement of Lemma 12.2. Now from the definition

- (12.12) of S(Asmall,Alarge) and (12.13) we have


P k −

εi,jai,j ∈ Σ(Amed) + Σ(Asmall) .

S(Asmall,Alarge) =

n+1−t<i⩽n j∈[bi]

ε∈E

If τ(Asmall) ⩾ 1/V we now apply (12.10) with x = k − n+1−t<i⩽n,j∈[bi] εi,jai,j, ε ∈ E; the relevant condition (12.5) holds precisely because ε ∈ E(Alarge) (recall the definition (12.11)). This gives that if τ(Asmall) ⩾ 1/V then

S(Asmall,Alarge) = (1 + O(V −Ω(1)))S′(Asmall,Alarge) where S′(Asmall,Alarge) equals

n+1−t

τ(Asmall)2 ni=1−L bi(2−Lk)−1

ε′i,jai,j ∈ [2−Lk] . (12.27)

P k −

εi,jai,j −

i>n+1−t j∈[bi]

i=n+1−L j∈[bi]

ε∈E(Alarge) ε′

where ε = (εi,j)n+1−t<i⩽n;j∈[bi] and ε′ = (ε′i,j)n+1−L⩽i⩽n+1−t;j∈[bi] range over all tuples of elements from {0,1} (subject to the restriction ε ∈ E(Alarge)). Substituting into (12.26), removing the conditioning on Alarge,Asmall and applying Lemmas 12.3 and 12.4 (noting that all error probabilities, as well as the V −Ω(1) term, are much less than ℓ−∗ 1 by the parameter hierarchy) we obtain

P k ∈ Σ′(Alarge) + Σ(Amed) + Σ(Asmall) = 1 − Ee−S′(Asmall,Alarge) + O(ℓ−∗ 1). (12.28) Our next task is to relate the LHS here to P(k ∈ Σ(A)). We pause to recall here that A still

means that we are conditioning to β = β,β′ = β′ and f = f. In carrying out the analysis (and also later on) we will use the following lemma.

- Lemma 12.5. Suppose that s is an integer with 0 ⩽ s ⩽ n+1−L. Write ε = (εi,j)s⩽i⩽n;j∈[bi], and εlarge := (εi,j)n+1−t<i⩽n;j∈[bi]. Then


εi,jai,j ∈ [2s−n−1k], εlarge ∈/ E(Alarge) ≪ R22 ni=s bi−(n−s)e−Ω((logV )1/2).

P k −

s⩽i⩽n;j∈[bi]

ε

Proof. Suppose k ∈ s⩽i⩽n;j∈[bi] εi,jai,j + [2s−n−1k] with εlarge ∈/ E(Alarge), that is to say k −

εi,jai,j − µ ⩾ (log V )1/4σ.

n+1−t<i⩽n;j∈[bi]

Then

εi,jai,j − µ ⩾ (log V )1/4σ − 2s−n−1k > 21(log V )1/4σ,

s⩽i⩽n+1−t;j∈[bi]

where the last step follows using that σ ≍ V 1/22n−t whilst 2s−nk ≪ 2s ⩽ 2n−L ≪ 2n−t.

By (12.18) (truncated to i = s at the lower end of the summation) it follows that the contribution from i < n + 1 − t is negligible and hence that

V

V

εn+1−t,jan+1−t,j − µ ⩾ 14(log V )1/4σ,

εjump,jajump,j − µ =

j=1

j=1

where here and henceforth we write εjump,j := εn+1−t,j and ajump,j := an+1−t,j for j ∈ [V ].

Next we observe that if some ε contributes nontrivially to the LHS in the lemma then it must lie in the set E0 consisting of those ε for which at least one εi,j, i ⩾ n−2log2 R, is not zero. This follows immediately from the R-boundedness of β and (7.10), and the fact that ai,j ≪ 2i deterministically (see (5.7)).

Putting these observations together, the LHS in the lemma is bounded above by

V

εjump,jajump,j − µ ⩾ 14(log V )1/4σ .

εi,jai,j ∈ [2s−n−1k],

P k −

s⩽i⩽n;j∈[bi]

ε∈E0

j=1

Denoting ε˜ := (εi,j)s⩽i⩽n,i̸=n+1−t;j∈[bi] (that is, all the εi,j other than the εjump,j), this is

V

εjump,jajump,j − µ ⩾ 14(log V )1/4σ .

≪ 2s−nk

### P

P

### εi,jai,j = x ·

sup

x

s⩽i⩽n i̸=n+1−t j∈[bi]

εjump

ε ˜:˜ε∈E0

j=1

Here, ε˜ ranges over the set {0,1} s⩽i⩽n,i̸=n+1−t bi, and εjump = (εjump,j)j∈[V ] ranges over {0,1}V = {0,1}bn+1−t. Additionally, we have implicitly used that the parameter hierarchy (11.3) implies that t ≫ 2log2 R, so the conditions ε ∈ E0 and ε˜ ∈ E0 are the same. By revealing all ai,j except for one corresponding to an index (i,j) with i ⩾ n − 2log2 R for which ε˜i,j ̸= 0, we see from (5.8) that the supx P( εi,jai,j = x) term is ≪ R22−n.

Thus, writing εjump,j, j = 1,...,V , for i.i.d. random {0,1} variables (independent of the a variables) and using that k ≍ 2n, the LHS in the lemma is bounded above by

V

2s−nk·2 s⩽i⩽n,i̸=n+1−t biR22−n · 2V P

εjump,jajump,j − µ > 41σ(log V )1/4

j=1

= R22 ni=s bi−(n−s)P

V

Xj − µ > 41(log V )1/4σ , (12.29)

j=1

where Xj := εjump,jajump,j. Now recall that by definition (11.8), µ = 12 Vj=1 Eajump,j, and so V j=1 EXj = µ. Now by Hoeffding’s inequality (see Lemma F.2), if H is an upper bound for

maxj |Xj| we have

V

Xj − µ ⩾ 41(log V )1/4σ ⩽ 2exp − σ2(log V )1/2/(32V H2) ≪ e−Ω((logV )1/2),

P

j=1

where in the last step we used the fact that we can take H ≍ 2n−t, and that σ ≍ V 1/22n−t. The proof of Lemma 12.5 is complete. □

Finally we complete the proof of Proposition 12.1. Proof of Proposition 12.1. From the case s = 1 of Lemma 12.5, noting that in this case we have

s⩽i⩽n bi − n = D, we see that the probability that k ∈ Σ(A), but k ∈/ Σ′(Alarge) + Σ(Amed) + Σ(Asmall), is ≪ R22De−Ω((logV )1/2) ≪ ℓ−∗ 1. By this and (12.28) we have

P(k ∈ Σ(A)) = 1 − Ee−S′(Asmall,Alarge) + O(ℓ−∗ 1). (12.30) Recall that S′(Asmall,Alarge) is defined in (12.27). Define S′′(Asmall,Alarge) as for S′(Asmall,Alarge), but without the constraint (εi,j)n+1−t<i⩽n;j∈[bi] ∈ E(Alarge). That is,

S′′(Asmall,Alarge) := τ(Asmall)2 ni=1−L bi(2−Lk)−1× ×

n+1−t

εi,jai,j ∈ [2−Lk] . (12.31)

P k −

εi,jai,j −

n+1−t<i⩽n j∈[bi]

i=n+1−L j∈[bi]

(εi,j)n+1−L⩽i⩽n;j∈[bi]

Using the trivial bound τ(Asmall) ⩽ 1, we have that E S′′(Asmall,Alarge) − S′(Asmall,Alarge) is bounded by

≪ 2 ni=1−L bi−(n−L)

εi,jai,j ∈ [2−Lk], (εi,j)n+1−t<i⩽n;j∈[bi] ∈/ E(Alarge)

P k −

n+1−L⩽i⩽n j∈[bi]

εi,j

where the first sum is over all (εi,j)n+1−L⩽i⩽n;j∈[bi] with components in {0,1}.

Applying Lemma 12.5 with s = n − L + 1, and using that ni=1 bi = n + D, it follows using the parameter hierarchy (11.3) that

E S′′(Asmall,Alarge) − S′(Asmall,Alarge) ≪ R22De−Ω((logV )1/2) ≪ ℓ−∗ 1. (12.32)

Since x  → e−x is Lipschitz with constant 1 on [0,∞), it follows from (12.30) and (12.32) that we have

P(k ∈ Σ(A)) = 1 − Ee−S′′(Asmall,Alarge) + O(ℓ−∗ 1). (12.33) Recall once more that, throughout the preceeding analysis, A means (A | β = β,β′ = β′,f = f). From the definition (12.31), using again that ni=1 bi = n+D, recalling that i>n−L bi = L+β(L)

and k = 2n+ξ, and rescaling the a-variables by dividing by k, we have that S′′(Asmall,Alarge) equals

n+1−t

ai,j k −

2D−ξτ(Asmall)2−β(L)

### P 1 −

εi,j

i>n+1−t j∈[bi]

i=n+1−L j∈[bi]

ε=(εi,j)i⩾n+1−L;j

Therefore

n

S′′(Asmall,Alarge) = 2D−ξτ(Asmall)2−β(L)

PAmed 1 −

i=n+1−L j∈[bi]

ε=(εi,j)i⩾n+1−L;j

ai,j

k ∈ [2−L] .

εi,j

ai,j

k ∈ [2−L] .

εi,j

In this expression, note carefully that the probability is taken only over random choices of Amed = (ai,j)L+1⩽i⩽n+1−t;j∈[bi], which means that S′′(Asmall,Alarge) still depends nontrivially on the random variables Alarge = (ai,j)n+1−t<i⩽n;j∈[bi]. Recalling Definition 7.1, this may be written

S′′(Asmall,Alarge) = 2D−ξτ(Asmall)EAmedϱ∗u˜|β(L), where u˜ = (u˜i,j)1⩽i⩽L,j∈[1+ξi] is defined by

1 k

2−u˜i,j =

an+1−i,j (12.34)

for 1 ⩽ i ⩽ L and j ∈ [1 + ξi]. Recall here that bn+1−i = 1 + ξi for i ⩽ ⌈n/2⌉, where the ξi are the increments of β, and note that u˜ depends on Amed and Alarge. Set

S′′′(Asmall,Alarge) := 2D−ξτ(Asmall)ϱ∗u˜|β(t − 1); (12.35)

note that ϱ∗u˜|β(t − 1) depends only on Alarge and not on Amed, so this is well-defined. By the Lipschitz nature of e−x and the triangle inequality, and since |D| ⩽ M/10, we have

EAlarge e−S′′(Asmall,Alarge) − e−S′′′(Asmall,Alarge) ≪ EAlarge S′′(Asmall,Alarge) − S′′′(Asmall,Alarge)

### ≪ 2M/10EAlarge ϱ∗u˜|β(t − 1) − EAmedϱ∗u˜|β(L) ⩽ 2M/10EAlarge,Amed ϱ∗u˜|β(t − 1) − ϱ∗u˜|β(L) , and so

E e−S′′(Asmall,Alarge) − e−S′′′(Asmall,Alarge) ≪ 2M/10E ϱ∗u˜|β(t − 1) − ϱ∗u˜|β(L) ,

where here averages are taken over the whole random choice of A = Asmall ∪ Amed ∪ Alarge, conditioned to β = β, β′ = β′ and f = f. Therefore by (12.33) we have

P(k ∈ Σ(A)) = 1 − Ee−S′′′(Asmall,Alarge) + O(ℓ−∗ 1) + O 2M/10 E ϱ∗u˜|β(t − 1) − ϱ∗u˜|β(L) . (12.36) Recall that f is the ‘jump distribution’ from the previous section; specifically, fm is the number of the ut,j in the interval Im (see (11.4)). However, the term S′′′(Asmall,Alarge) is independent of f, using (5.2) and that the jump indices with an+1−t,j are part of Amed. Thus it is tempting to remove the conditioning on f at this juncture. To this end we note the simple comparison estimate

E ϱ∗u˜|β(t − 1) − ϱ∗u˜|β(L) ⩽ P(f = f)−1E˜ ϱ∗u˜|β(t − 1) − ϱ∗u˜|β(L) ⩽ V V/3E˜ ϱ∗u˜|β(t − 1) − ϱ∗u˜|β(L)

where (as above) E denotes averaging with the conditioning to f = f in place, and E˜ is the average with no condition on f (but still conditioning to β = β and β′ = β′). The second computation here comes from

V ! f1!···fV 1/3!

V −V/3 ⩾ V −V/3.

P(f = (f1,...,fV 1/3)) =

Thus, at the expense of a slightly worse error term, we can remove the conditioning on f in (12.36) to conclude that

P(k ∈ Σ(A)) = 1 − Ee−S′′′(Asmall,Alarge) + O(ℓ−∗ 1) + O 2M/10V V/3 E ϱ∗u˜|β(t − 1) − ϱ∗u˜|β(L) . (12.37) Here, and from now on in this section, we are conditioning only to β = β,β′ = β′, thus A denotes (A | β,β′) and the averages on the right are with no conditioning on f (we called this averaging E˜ above), with the u˜i,j still defined as in (12.34).

From the definition (12.35) we have

Ee−S′′′(Asmall,Alarge) = Eexp −2D−ξτ(Asmall)ϱ∗u˜|β(t − 1) . Since e−2Dx is Lipschitz on [0,∞) with constant at most 2D ⩽ 2M/10, we have

Ee−S′′′(Asmall,Alarge) − Eexp − 2D−ξτx∗|β′(L)ϱ∗u|β(L) ≪ 2M/10E τx∗|β′(L)ϱ∗u|β(L) − τ(Asmall)ϱ∗u˜|β(t − 1) . (12.38)

Applying the inequality |x1x2 − x3x4| ⩽ x3|x4 − x5| + x3|x5 − x2| + x2|x3 − x1| (trivially valid for non-negative reals x1,...,x5) with x1 := τx∗|β′(L), x2 := ϱ∗u|β(L), x3 := τ(Asmall), x4 := ϱ∗u˜|β(t − 1) and x5 := ϱ∗u|β(t − 1), we may bound the RHS of (12.38) by 2M/10(E1 + E2 + E3), where

E1 := Eτ(Asmall) · E ϱ∗u˜|β(t − 1) − ϱ∗u|β(t − 1) , E2 := Eτ(Asmall) · E ϱ∗u|β(t − 1) − ϱ∗u|β(L) , and

E3 := Eϱ∗u|β(L) · E|τ(Asmall) − τx∗|β′(L)|. We also introduce

E4 := E ϱ∗u˜|β(t − 1) − ϱ∗u˜|β(L) (which appears in (12.37)). We now proceed to bound E1,...,E4 in turn. Bounding E1. To bound E1, we first use that τ(Asmall) ⩽ 1 deterministically, and so E1 ⩽ E ϱ∗u˜|β(t − 1) − ϱ∗u|β(t − 1) . (12.39)

To bound this we use Lemma 5.6 and (12.34), which give that |2−ui,j − 2−u˜i,j| ≪ 2−ii/n ≪ n1 deterministically for 1 ⩽ i ⩽ L and j ∈ [1 + ξi]. Given ε = (εi,j)1⩽i⩽t−1,j∈[1+ξi], set σε :=

1⩽i⩽t−1,j∈[1+ξi] εi,j2−ui,j and σ˜ε := 1⩽i⩽t−1,j∈[1+ξ

i] εi,j2−u˜i,j. Then we have

t−1

1 n

(1 + ξi) ≪ n−1/2, (12.40)

σε − σ˜ε ≪

i=1

with the final bound following very comfortably from the parameter hierarchy and since β is Rbounded. Now we have by definition

ϱ∗u|β(t − 1) = 2−β(t−1)

1 σε ∈ [1 − 21−t,1]), ϱ∗u˜|β(t − 1) = 2−β(t−1)

1 σ ˜ε ∈ [1 − 21−t,1]),

ε

ε

and so using (12.39) and (12.40) we obtain E1 ⩽ 2−β(t−1)

P(σε ∈ [1−O(n−1/2),1+O(n−1/2)]∪[1−21−t −O(n−1/2),1−21−t +O(n−1/2)] .

ε

As in the proof of Lemma 7.2, using the R-boundedness of β we see that if σε > 21 then εa,b ̸= 0 for some a ⩽ 2log2 R. In particular, the probability term above is zero unless this is the case. Revealing all ui,j except ua,b, it follows that, for each ε, the probability term above is bounded by P(σε ∈ ··· ≪ 2an−1/2. Since the number of ε is 2 ti=1−1(1+ξi) < 2Rt2max < n1/10 and since 2a < n1/10, we have the bound

E1 ≪ n−1/4. (12.41)

- Bounding E2. We again use that τ(Asmall) ⩽ 1, and for the second term we use (7.16) and a

telescoping sum. This gives a bound of

E2 ≪ 23T−Ω(t

1/4

min). (12.42)

- Bounding E3. By (7.5) we have Eϱ∗u|β(L) ≪ R2. To bound the E|τ(Asmall) − τx∗|β′(L)| term,


define x˜ by x˜i,j := ai,j for i ∈ [L] and j ∈ [1 − ξi′]. Thus by the definitions of the various quantities (see (12.1) and Definition 6.1) we have

τ(Asmall) = τx˜∗|β′(L). (12.43)

We showed in Lemma 5.7 that P(xi,j ̸= x˜i,j) ≪ L/n, uniformly for i ∈ [L] and j ∈ [1 − ξi′]; thus with probability 1 − O(L3/n) we have xi,j = x˜i,j for all i ∈ [L] and j ∈ [1 − ξi′], using here the

crude bound Li=1(1 − ξi′) ≪ L2, which follows from the R-boundedness of β′ and the parameter hierarchy.

In the event that xi,j = x˜i,j for all i ∈ [L] and j ∈ [1−ξi′], it follows from (12.43) that τ(Asmall) = τx∗|β′(L). Since all τ∗ quantities are ⩽ 1 deterministically, we obtain from this analysis that

L3 n

E3 ≪ R2

. (12.44) Bounding E4. Finally, to bound E4, we use

E4 ⩽ E ϱ∗u˜|β(t − 1) − ϱ∗u|β(t − 1) + E ϱ∗u|β(t − 1) − ϱ∗u|β(L) + E ϱ∗u˜|β(L) − ϱ∗u|β(L) . The first term we already bounded during the analysis of E1. The third term may be bounded analogously, replacing t − 1 by L throughout. Due to the parameter hierarchy we have the bound n−1/4 for both of these terms. Finally, as we already saw during the analysis of E2, the second term may be bounded by ≪ 23T−Ω(t

1/4

min) by use of (7.16). Thus E4 ≪ 23T−Ω(t

1/4

min). (12.45) Putting the bounds (12.41), (12.42), (12.44), and (12.45) together with (12.36) and (12.38) (re-

calling that the RHS of (12.38) is bounded by 2M/10(E1 + E2 + E3)) and using the parameter hierarchy (11.3) concludes the proof of Proposition 12.1. □

## Part 4. Putting everything together

13. Expressing p(k) as an average over walks

We turn now to the proof of our main results. At this point we drop the convention (in force for the preceding two sections) that A is shorthand for either (A | β = β, β′ = β′, f = f) or (A | β,β′). From now on, A will denote the unconditioned multiset as defined in (3.1), and we will explicitly write (A | β,β′) for the conditioned sets as described in Section 5.3. There should be little danger of confusion since the only result we will need from the preceding two sections is Proposition 12.1, which is stated with the longhand notation. Our starting point will be the expression (4.2) for p(k).

As in the previous two sections, we have a main truncation parameter M and various further key further thresholds R(M), T(M), L(M) as described in Definition 11.1, as well as technical auxiliary thresholds ℓ∗(M), V (M), tmin(M), tmax(M) as in the hierarchy (11.3). We will always assume that L(M) is much less than n = ⌊log2 k⌋; later we will let M → ∞ as k → ∞ sufficiently slowly so that this holds.

To shorten some expressions it is convenient to set N := ⌈n/2⌉ and N′ := ⌊n/2⌋ througout this section.

- 13.1. Reducing to walks with large minima and small discrepancy. As before the discrepancy of a pair of walks (β,β′), which we denote by D(β,β′), is β(N) − β′(N′). For D ∈ Z and m,m′ ∈ Z⩾0 denote


BD,m,m′ := {(β,β′) ∈ ZN × ZN : D(β,β′) = D, min

β′(i) = −m′}, (13.1)

β(i) = −m, min

0⩽i⩽N

0⩽i⩽N′

where we declare β(0) = β′(0) = 0. It follows from Lemma 8.10 with E being the trivial (always satisfied) event that

P (β,β′) ∈ BD,m,m′ ≪ (1 + m + m′)3(log k)−3/2. (13.2) Write

P (β,β′) = (β,β′) P k ∈ Σ(A | β,β′) . (13.3)

ED,m,m′ :=

(β,β′)∈BD,m,m′

Then (4.2) gives

1

log2−1)k−δ

p(k) = (1 + o(1))eγ(

(log 2)D−ξ

ED,m,m′ + O(k−δ(log k)−2). (13.4)

m,m′⩾0

|D|⩽20 log n

We now wish to show that the most important contribution to this sum comes from |D|,m,m′ =

- O(1). In this direction, our first result shows that the contribution from large max(m,m′) is negligible.


## Lemma 13.1. We have

ED,m,m′ ≪ (log k)−100.

(log 2)D

|D|⩽20 log n

max(m,m′)⩾(log n)2

Proof. We first bound the contribution from the (extremely rare) pairs of walks for which maxi⩽n bi is greater than or equal to n. Since bi =d Pois(1), the probability that (β,β′) have this property is ≪ nP(Pois(1) ⩾ n) < e−n. Bounding P(k ∈ Σ(A | β,β′)) trivially by 1, and (log 2)D by (log 2)−20 logn ≪ nO(1), we see that the contribution from these walks is negligible.

Henceforth, we restrict to pairs of walks with maxi⩽n bi ⩽ n. Fix a pair of walks (β,β′) ∈ BD,m,m′, where |D| ⩽ 20log n. We consider the contributions from m ⩾ (log n)2 and from m′ ⩾ (log n)2 separately.

Suppose first that m ⩾ (log n)2. Let q, 0 ⩽ q ⩽ N, be the smallest value such that β(q) = −m. Since ξi ⩾ −1 for all i, we have β(q) ⩾ −q, and so q ⩾ m ⩾ (log n)2. Writing ai,j for the elements of (A | β,β′) as usual (see (5.2)), it follows using (5.8) that

εi,jai,j : εi,j ∈ {0,1}} ≪ n2n−q.

max{

i⩽n−q;j∈[bi]

Since q ⩾ (log n)2, this is certainly o(k). Therefore the event (k ∈ Σ(A | β,β′)) is contained in the union of the events ( n−q<i⩽n;j∈[b

i] εi,jai,j = k − x), over all x ≪ n2n−q = o(k) and all 2q+β(q) choices of (εi,j)n−q<i⩽n;j∈[bi]. Note moreover that for such an event to be nontrivial, we must have εi,j ̸= 0 for some i ⩾ n − 2log2 n; otherwise,

εi,jai,j ⩽

εi,jai,j ≪ n2n−2 log2 n < k/2 < k − x.

n−q<i⩽n;j∈[bi]

i⩽n−2 log2 n;j∈[bi]

By revealing all ai,j except for such a pair of indices, we see that P( n−q<i⩽n;j∈[b

i] εi,jai,j = k−x) ≪ 22 log2 n−n = n22−n for each choice of x and the εi,j. Summing over these choices gives

P(k ∈ Σ(A | β,β′)) ≪ n2n−q · 2q+β(q) · n22−n ≪ n32−(logn)2,

and so (log 2)DP(k ∈ Σ(A | β,β′)) ≪ nO(1)2−(logn)2 ≪ (log k)−100. Summing over all (β,β′) lying in some BD,m,m′ with |D| ⩽ 20log n and m ⩾ (log n)2, weighted by P (β,β′) = (β,β′) , gives a bound of the strength claimed in Lemma 13.1.

Now we consider the possibility that m′ ⩾ (log n)2; the analysis here is very similar. Let q′, 0 ⩽ q′ ⩽ N′, be the smallest value such that β′(q′) = −m′. Similarly to before, it follows using (5.8) that

εi,jai,j : εi,j ∈ {0,1}} ≪ n2q′.

max{

i⩽q′;j∈[bi]

Since q′ ⩽ N′, this is vastly smaller than k. The event (k ∈ Σ(A | β,β′)) is contained in the union of the events q′<i⩽n;j∈[bi] εi,jai,j = k − x , over all x ≪ n2q′ and all 2n+D−q′+β′(q′) choices of (εi,j)q′<i⩽n;j∈[bi], noting here that q′<i⩽n bi = ni=1 bi− qi=1′ bi = n+D−(q′−β′(q′)). As before,

- P( q′<i⩽n;j∈[bi] εi,jai,j = k − x) ≪ n22−n for each choice of x and the εi,j. Summing over these choices gives


P(k ∈ Σ(A | β,β′)) ≪ n2q′ · 2n+D−q′+β′(q′) · n22−n ≪ nO(1)2−(logn)2,

using here that |D| ⩽ 20log n. Summing over all (β,β′) lying in some BD,m,m′ with |D| ⩽ 20log n and m′ ⩾ (log n)2, weighted by P (β,β′) = (β,β′) , again gives a bound of the strength claimed in

- Lemma 13.1. This completes the proof. □


To prepare for our study of the more modest values of m, m′, we establish the following lemma, which should be thought of as very roughly suggesting that P(k ∈ Σ(A | β,β′)) behaves like min(2−m,2−m′) when (β,β′) ∈ BD,m,m′.

- Lemma 13.2. Suppose that D ∈ Z and that m,m′ ∈ Z⩾0. Let β,β′ be walks such that (β,β′) ∈ BD,m,m′. Let q, 0 ⩽ q ⩽ N, be minimal such that β(q) = −m, and q′ be minimal such that β′(q′) = −m′. Let r be the least positive integer such that β is r-bounded to length N (see Definition 8.11), and let r′ be defined similarly for β′. Then we have


P(k ∈ Σ(A | β,β′)) ≪ rO(1)(1 + q)κ2−m, (13.5) and

P(k ∈ Σ(A | β,β′)) ≪ (r′)O(1)(1 + q′)κ2D−m′. (13.6) Proof. By replacing r by max(100,r) if necessary (and similarly for r′) we may assume r,r′ ⩾ 100. We begin with the first bound (13.5). If m ⩽ 2log2 r, the bound is trivial, so assume henceforth that m ⩾ 2log2 r. We may also assume that m is sufficiently large. In particular q ⩾ 1. The argument is very similar to that in the previous lemma. Since β is r-bounded, we have |bn+1−i| ⩽ riκ + 1 and so using (5.7) we have

εi,jai,j : εi,j ∈ {0,1}} ≪ rqκ2n−q. (13.7)

max{

i⩽n−q;j∈[bi]

As in the previous lemma, we have q ⩾ m, and so q ⩾ 2log2 m; therefore (since also q is sufficiently large) the bound in (13.7) is ⩽ k/2. Now we proceed as in the previous lemma, writing the

i] εi,jai,j = k − x), over all x ≪ rqκ2n−q < k/2 and all 2q+β(q) choices of (εi,j)n−q<i⩽n;j∈[bi].

event (k ∈ Σ(A | β,β′)) as the union of the events ( n−q<i⩽n;j∈[b

For such an event to be nontrivial, we must have εi,j ̸= 0 for some i ⩾ n − 2log2 r; otherwise,

εi,jai,j ⩽

(riκ + 1)2i < k/2 < k − x.

εi,jai,j ≪

i⩽n−2 log2 r

n−q<i⩽n;j∈[bi]

i⩽n−2 log2 r;j∈[bi]

By revealing all ai,j except for such a pair of indices, we see that P( n−q<i⩽n;j∈[b

i] εi,jai,j = k−x) ≪ 22 log2 r−n ≪ rO(1)2−n for each choice of x and the εi,j. Summing over these choices gives

P(k ∈ Σ(A | β,β′)) ≪ rqκ2n−q · 2q+β(q) · rO(1)2−n ≪ rO(1)qκ2−m, which is the required result.

Now we turn to the second bound, whose proof is again very similar. The r′-boundedness of β′ gives |bi| ⩽ 1 + r′iκ, and so using (5.8) we have

εi,jai,j : εi,j ∈ {0,1}} ≪ r′(q′)κ2q′.

max{

i⩽q′;j∈[bi]

The rest of the argument proceeds as before; as in the proof of Lemma 13.1 the number of choices for (εi,j)q′<i⩽n;j∈[bi] is 2n+D−q′+β′(q′). We obtain

P(k ∈ Σ(A | β,β′)) ≪ r′(q′)κ2q′ · 2n+D−q′+β′(q′) · (r′)O(1)2−n = (r′)O(1)(q′)κ2D−m′,

which is the required result. □ It follows from (13.5) and the definition (13.3) that ED,m,m′ ≪ 2−m

P (β,β′) = (β,β′) rβO(1)(1 + qβ)κ

(β,β′)∈BD,m,m′

= 2−m

β′(i) = −m′, D(β,β′) = D,

rO(1)(1 + q)κP( min

β(i) = −m, min

0⩽i⩽N

0⩽i⩽N

0⩽q⩽N r⩾1

R⩽N(β) = r, Qm(β) = q),

where qβ,rβ are the q,r associated to β as in the statement of Lemma 13.2, R⩽N(β) is the least positive integer r such that β is r-bounded to length N, and Qm(β) is the least non-negative integer such that β(q) = −m. To estimate this, we apply the first estimate in Lemma 8.10 with the event E being that R⩽N(β) = r and that Qm(β) = q. This gives (recalling that n ∼ log2 k)

ED,m,m′ ≪ (1 + m + m′)22−m(log k)−1

rO(1)(1 + q)κP R⩽N(β) = r,

0⩽q⩽N r⩾1

β(i) = −m .

Qm(β) = q, min

0⩽i⩽N

Applying the AM-GM inequality rO(1)(1 + q)κ ⩽ rO(1) + (1 + q)2κ and summing out the redundant variables gives

ED,m,m′ ≪ (1 + m + m′)22−m(log k)−1

(1 + q)2κP Qm(β) = q, min

β(i) = −m

0⩽i⩽N

0⩽q⩽N

+ (1 + m + m′)22−m(log k)−1

rO(1)P R⩽N(β) = r, min

β(i) = −m . (13.8)

0⩽i⩽N

r⩾1

By Lemma 8.7 (relaxing the condition Qm(β) = q to β(q) = −m, and the condition min0⩽i⩽N β(i) = −m to min1⩽i⩽N β(i) ⩾ −m), we have

(1 + q)2κ−3/2(N + 1 − q)−1/2

(1 + q)2κP Qm(β) = q, min

β(i) = −m ≪ (1 + m)

0⩽i⩽N

0⩽q⩽N

0⩽q⩽N

≪ (1 + m)N−1/2 ≪ (1 + m)(log k)−1/2. (13.9) By Lemma 8.12 (relaxing the condition R⩽N(β) = r to R⩽N(β) > r − 1) we have

β(i) = −m ≪ N−1/2

rO(1)(m + r)e−r

rO(1)P R⩽N(β) = r, min

0⩽i⩽N

r⩾1

r⩾1

≪ (1 + m)N−1/2 ≪ (1 + m)(log k)−1/2. (13.10) It follows from (13.8) to (13.10) that

ED,m,m′ ≪ (1 + m + m′)32−m(log k)−3/2. (13.11) An essentially identical analysis starting from (13.6) yields

ED,m,m′ ≪ (1 + m + m′)32D−m′(log k)−3/2. (13.12)

From this we deduce the following estimate concerning the contribution to (13.4) from walks with small minima or large discrepancy.

- Lemma 13.3. The sum of (log 2)DED,m,m′ over all D,m,m′ with |D| ⩽ 20log n, 0 ⩽ m,m′ ⩽ (log n)2 and either |D| ⩾ M/10 or max(m,m′) ⩾ M is bounded by ≪ e−Ω(M)(log k)−3/2.


### Proof. Given the estimates (13.11) and (13.12), the task is to show that

(log 2)D(1 + m + m′)3 min(2−m,2D−m′) ≪ e−Ω(M), (13.13)

D,m,m′

where the sum is over triples D,m,m′, D ∈ Z, m,m′ ∈ Z⩾0, satisfying one of (1) |D| ⩾ M/10, (2) |D| ⩽ M/10 but max(m,m′) ⩾ M.

Contribution from (1). First we consider the contribution from D ⩾ M/10. For this we use the estimate m,m′⩾0(1 + m + m′)3 min(2−m,2D−m′) ≪ D4. (To verify this, first note that the contribution from m′ ⩽ 2D is ≪ D m⩾0(D + m)32−m, which is acceptable; for m′ ⩾ 2D we have min(2−m,2D−m′) ⩽ min(2−m/2,2−m′/2), so by symmetry the sum is ≪ m⩾m′(1+m+m′)32−m/2 ≪

m(1 + m)42−m/2, which is again acceptable.) Including the factor (log 2)D and summing this estimate over D ⩾ M/10 gives D⩾M/10(log 2)DD4 ≪ (M/10)4(log 2)M/10, which is acceptable.

Next we consider the contribution from D ⩽ −M/10. For this we use the estimate m,m′⩾0(1 + m + m′)3 min(2−m,2D−m′) ≪ |D|42−|D|. (To verify this, first note that the contribution from m ⩽ 2|D| is ≪ |D| m′⩾0(|D| + m′)32−|D|−m′, which is acceptable; for m ⩾ 2|D| we have min(2−m,2D−m′) ⩽ 2−|D| min(2−m/2,2−m′/2), and we can conclude as before.) Including the factor (log 2)D and summing this estimate over D ⩽ −M/10 gives ≪ D⩽−M/10 |D|4(log 2)−|D|2−|D| ≪ (M/10)4(2log 2)−M/10, so this contribution is also acceptable.

Contribution from (2). The contribution to (13.13) from |D| ⩽ M/10 and max(m,m′) ⩾ M is ≪ M(2/log 2)M/10

(1 + m + m′)3 min(2−m,2−m′).

max(m,m′)⩾M

By symmetry it is enough to sum this over m ⩾ max(m′,M). We then note, in turn, that

(1 + m + m′)3 min(2−m,2−m′) ≪ (1 + m)42−m,

m′⩽m

then that m⩾M(1 + m)42−m ≪ M42−M. The result follows. □ It follows, substituting into (13.4), that p(k) = (1 + o(1))eγ(

1

log2−1)k−δ

(log 2)D−ξ

ED,m,m′+

m,m′⩽M

|D|⩽M/10

+ O e−Ω(M)k−δ(log k)−3/2 . (13.14)

This is the desired reduction to the consideration of walks with large minimum and small discrepancy.

13.2. Passing to ‘good’ walks. We now continue with the analysis, the next aim being to refine (13.14) so that ED,m,m′ (see (13.3)) only sums over walks which are R(M)-bounded, T(M)-positive and for which β has a jump step, at which point we will be able to apply Proposition 12.1.

Recall the definition (13.1) of BD,m,m′. We now define two slightly different subsets of BD,m,m′. Let C0 be a (sufficiently large) constant to be specified later. Set

BD,m,m(1) ′ := {(β,β′) ∈ BD,m,m′ : β,β′ are R(M)-bounded and T(M)-positive to length L(M) and

there are q,q′ ⩽ eC0M with β(q) = −m, β′(q′) = −m′}. (13.15) By a jump step at scale M we mean a V (M)-jump step in the sense of Definition 8.17 which lies in the interval [tmin(M),tmax(M)], with the parameters V (M),tmin(M),tmax(M) as in the hierarchy

(11.3). Define BD,m,m(2) ′ to be the set of all (β,β′) ∈ BD,m,m′ such that β,β′ are R(M)-bounded and T(M)-positive to lengths N, N′ respectively, there are q,q′ ⩽ eC0M with β(q) = −m, β′(q′) = −m′, and such that β has a jump step at scale M. We clearly have

BD,m,m(2) ′ ⊆ BD,m,m(1) ′ ⊆ BD,m,m′. (13.16) We claim that both these sets are ‘generic’ in the following sense.

- Lemma 13.4. Suppose that m,m′ ⩽ M and that |D| ⩽ M/10. We have for i = 1,2 that P (β,β′) ∈ BD,m,m′ \ BD,m,m(i) ′ ≪ e−10M(log k)−3/2.


Proof. By (13.16) it is enough to handle the case i = 2. We use Lemma 8.10 with E = 4i=1 E(i) being the event that at least one of the following occurs: (1) β is not R(M)-bounded to length N;

(2) β is not T(M)-positive to length N; (3) there is q with eC0M ⩽ q ⩽ N such β(q) = −m and (4) β has no jump step at scale M. There are also (except for (4)) symmetric events involving β′ to be considered, which may be handled in exactly the same way and about which we shall make no further comment. Applying Lemma 8.10, we see that it is enough to show that

β(i) ⩾ −m ≪ e−10MN−1/2. (13.17) We handle the case i = 1,2,3,4 in turn.

P β ∈ E(i), min

1⩽i⩽N

- Case i = 1. By Lemma 8.12 it follows that (13.17) is ≪ R(M)e−R(M)N−1/2. Recalling from

Definition 11.1 that R(M) = 20M, this is acceptable.

- Case i = 2. By Lemma 8.15 it follows that (13.17) is ≪ MO(1)T(M)−η/2N−1/2. Recalling from

Definition 11.1 that T(M) = e40M/η, this is acceptable.

- Case i = 3. By Lemma 8.7, (13.17) is


q−3/2(N + 1 − q)−1/2 ≪ Me−C0M/2N−1/2,

≪ M

eC0M⩽q⩽N

which is acceptable if C0 > 20.

Case i = 4. In this case the bound follows from Lemma 8.19 with δ = e−10M and (8.4), provided parameters are chosen appropriately. Note here that for any choice of V (M) there are appropriate choices of tmin(M) and tmax(M) for which (8.27) and (8.28) both hold. □

For i = 1,2 define ED,m,m(i) ′ analogously to ED,m,m′ (cf. (13.3)), that is to say write ED,m,m(i) ′ :=

P (β,β′) = (β,β′) P(k ∈ Σ(A | β,β′)).

(β,β′)∈BD,m,m(i) ′

If we replace ED,m,m′ by ED,m,m(i) ′ in (13.14), the error is bounded by ≪ k−δ

P((β,β′) ∈ BD,m,m′ \ BD,m,m(i) ′) ≪ e−5Mk−δ(log k)−3/2 (13.18)

(log 2)D

m,m′⩽M

|D|⩽M/10

by Lemma 13.4. Thus we may replace ED,m,m′ by ED,m,m(i) ′ in (13.14) with changes only in the implied constant in the error term.

Define also E˜D,m,m(i) ′ :=

### P (β,β′) = (β,β′) 1 − Eexp −2D−ξϱ∗u|β(L(M))τx∗|β′(L(M)) .

(β,β′)∈BD,m,m(i) ′

The purpose of this definition is that we have replaced P(k ∈ Σ(A | β,β′)) by the main term in the formula obtained in Proposition 12.1. Indeed, by Proposition 12.1 it follows that

ED,m,m(2) ′ = E˜D,m,m(2) ′ + O(ℓ∗(M)−1P((β,β′) ∈ BD,m,m′)).

Thus, using (13.2), we see that the error if we further replace ED,m,m(2) ′ by E˜D,m,m(2) ′ in (13.14) is bounded by

(log 2)DP (β,β′) ∈ BD,m,m′

≪ ℓ∗(M)−1k−δ

|D|⩽M/10,m,m′⩽M

(log 2)D(1 + m + m′)3(log k)−3/2 ≪ e−10Mk−δ(log k)−3/2

≪ ℓ∗(M)−1k−δ

|D|⩽M/10,m,m′⩽M

if an appropriate choice of ℓ∗(M) is made in the parameter hierarchy (11.3). Finally, we replace E˜D,m,m(2) ′ by E˜D,m,m(1) ′ in (13.14). The error in doing this is again bounded as in (13.18) by a very similar argument using Lemma 13.4.

Let us state the final conclusion of the above analysis, and the only one we will need subsequently,

which is that with negligible error we can replace ED,m,m′ by E˜D,m,m(1) ′ in (13.14), and therefore we have

p(k) = (c0 + o(1))k−δ(log k)−3/2 fM,n(ξ) + O(e−Ω(M)) , (13.19) where c0 is the constant in Theorem 1.1, and for 0 ⩽ θ ⩽ 1 we define fM,n(θ) to be

2 π

1/2n3/2

(log 2)D−θP (β,β′) = (β,β′) 1 − Eexp −2D−θϱ∗u|β(L)τx∗|β′(L) , (13.20)

|D|⩽M/10 m,m′⩽M

(β,β′)∈BD,m,m(1) ′

with L = L(M) and BD,m,m(1) ′ defined in (13.15). (Here we have used that (log k)3/2 = (1 + o(1))(log 2)3/2n3/2, but it is natural to write things in terms of log k in (13.19) and in terms of n in (13.20).)

14. Decoupling the walks

The notation in this section follows that of the previous three sections and in particular we continue to write L = L(M) and N = ⌈n/2⌉, N′ = ⌊n/2⌋ for brevity. It is also convenient to write β⩽L for (β(i))1⩽i⩽L, and similarly for β′. We always have β(0) = β′(0) = 0. Our aim now is to show that the function fM,n in (13.20) essentially does not depend on n. The average in (13.20) is over pairs of walks (β,β′) satisfying the conditions

D(β,β′) := β(N) − β′(N′) = D, min

0⩽i⩽N

β(i) = −m, and min

0⩽i⩽N′

β′(i) = −m′. (14.1)

Note that membership of (β,β′) in BD,m,m(1) ′ is defined by the conditions (14.1) and the following four conditions which depend only on each of β,β′ individually and in fact only on the values β⩽L,β⩽′ L, namely

- (1) β is R(M)-bounded to length L;
- (2) β is T(M)-positive to length L;
- (3) min0⩽i⩽L β(i) = −m;
- (4) There is some q ⩽ eC0M such that β(q) = −m,


and similar conditions on β′. Note that the redundant condition (3) is deliberately retained here as it will be relevant to a later definition. It is also the case that the random variables ϱ∗u|β(L), τx∗|β′(L) depend only β⩽L and β⩽′ L respectively.

Define Cm,M to be the set of all tuples ⃗c = (c1,...,cL) ∈ ZL such that β satisfies (1) to (4) above iff β⩽L ∈ Cm,M. Define Wm,M to be the set of all walks β satisfying (1) to (4) above; thus β ∈ Wm,M if and only if β⩽L ∈ Cm,M.

We may then write (13.20) as

2 π

1/2n3/2

(log 2)D−θE 1 − exp −2D−θϱ∗u|⃗c(L)τx∗|⃗c′(L) ×

fM,n(θ) =

|D|⩽M/10 m,m′⩽M

⃗c∈Cm,M ⃗c′∈Cm′,M

β′(i) = −m′, β(N) − β′(N′) = D, β⩽L = ⃗c, β⩽′ L = ⃗c′ . Applying Lemma 8.9, we obtain

× P min

β(i) = −m, min

0⩽i⩽N

0⩽i⩽N′

(log 2)D−θE 1 − exp −2D−θϱ∗u|⃗c(L)τx∗|⃗c′(L) × × h(m + cL)h′(m′ + c′L) + O(n−ε1) P β⩽L = ⃗c, β⩽′ L = ⃗c′

fM,n(θ) =

|D|⩽M/10 m,m′⩽M

⃗c∈Cm,M ⃗c′∈Cm′,M

= fM(θ) + O(n−ε1/2), (14.2) where ε1 is the (positive) exponent in Lemma 8.9 and

(log 2)D−θ h(m+β(L))h′(m′+β′(L))Ψm,m′,M,D,θ(β,β′)dP(β)dP′(β′) (14.3)

fM(θ) :=

|D|⩽M/10 m,m′⩽M

with

Ψm,m′,M,D,θ(β,β′) := E 1 − exp −2D−θϱ∗u|β(L)τx∗|β′(L) 1Wm,M(β)1W

(β′), (14.4)

m′,M

and the integrations being with respect to the path measures of β, β′ respectively. We comment briefly on the application of Lemma 8.9. The required condition maxci,maxc′i ⩽ Nε1 is comfortably implied by the definition of Wm,M, in particular by the fact that ⃗c must be the initial segment of an R(M)-bounded walk. We also note that the O(n−ε1/2) error term in (14.2) follows using the fact that (log 2)−D is much smaller than nε1/2 (and that the Wm,M are disjoint as m varies).

The crucial point to note is that fM(θ) no longer depends on n; in other words fM(θ) is a ‘universal’ object which does not see k,n,ξ.

Combining (13.19), (13.20), and (14.2) gives p(k) = (c0 + o(1))k−δ(log k)−3/2 fM(ξ) + O(e−Ω(M)) , (14.5)

where ξ = {log2 k} as usual, the o(1) denotes a quantity tending to zero as k → ∞, and M is any quantity satisfying M ⩽ M0(k) for some fixed function M0 with limk→∞ M0(k) = ∞. The function M0 is specified by the requirement that it must be possible to choose parameters as in (11.3).

Let us pause to remark on how Corollary 1.2 already follows from this and the existing literature.

Proof of Corollary 1.2. If k is a power of two then ξ = {log2 k} = 0. By applying (14.5) for fixed M and k → ∞, we see that |fM(0)−fM+1(0)| ≪ e−Ω(M), and therefore we have fM(0) = c1+O(e−Ω(M)) for some c1. Substituting in to (14.5), the corollary follows (with C = c0c1) except we have not shown that C > 0. This does not follow directly from this argument, but is a consequence of [15] and will also be shown in a self-contained fashion in Sections 15.4 and 15.5 below. □

15. Proof of the main theorem

In this section we prove Theorem 1.1. The main task is to show that the measures µ,µ′ exist and are not zero. The more detailed characterisations described in Propositions 1.3 and 1.4 must wait until later.

Recall that Wm,M denotes the set of walks β satisfying conditions (1) – (4) at the start of Section 14. Throughout the section c := −log log 2log 2 .

- 15.1. Approximating fM by a convolution. The starting point for this section is (14.5), with fM defined in (14.3). Our aim is to show convergence of fM to a function f, which we will ultimately describe as a convolution g∗µ∗µ′. As a stepping stone to this result, our main goal in this subsection


is to approximate fM by a convolution; in particular, the function g (defined in (1.2)) will enter the picture for the first time. Specifically, we will prove the following.

- Lemma 15.1. Let M be a sufficiently large positive integer. There is a function f˜M ∈ C∞(R/Z) with


∥fM − f˜M∥∞ ≪ e−Ω(M) (15.1) and such that f˜M may be written as

f˜M = g ∗ µM ∗ µ′M, (15.2) g ∈ C∞(R/Z) the function in (1.2), µM is the Borel measure on R/Z given by

Eϱ∗u|β(L(M))cψ log2 ϱ∗u|β(L(M)) 1Wm,M(β)dωm(β) (15.3)

ψ dµM =

m⩽M ZN⩾−m

for test functions ψ ∈ C(R/Z), and µ′M is defined by ψ dµ′M =

Eτu∗|β′(L(M))cψ log2 τu∗|β′(L(M)) 1Wm,M(β′)dωm′ (β′). (15.4)

m⩽M ZN⩾−m

Here, the convention is that xcψ(log2 x) = 0 if x = 0. Proof. We again write L = L(M) for brevity. With (14.3) in mind, consider first any expression of the form

h(β(L) + m)h′(β′(L) + m′)Ψ(β,β′)dP(β)dP′(β′)

where Ψ : ZN⩾−m × ZN⩾−m′ → R is such that Ψ(β,β′) depends only on the initial segments β⩽L,β⩽′ L. (Note that the functions Ψm,m′,M,D,θ in (14.4) are of this type due to the nature of the 1Wm,M cutoffs.) By (8.9) this expression can be written

Ψ(β,β′)dωm(β)dωm′ ′(β′).

ZN⩾−m ZN⩾−m′

Returning to (14.3), we therefore have

Ψm,m′,M,D,θ(β,β′)dωm(β)dωm′ ′(β′). (15.5)

(log 2)D−θ

fM(θ) =

m,m′⩽M ZN⩾−m ZN⩾−m′

|D|⩽M/10

Suppose in all that follows that θ ∈ [0,1]. The next part of our analysis is to show that we can extend the sum over D in (15.5) to all of Z with small error. First note that, immediately from the definition (14.4), we have Ψm,m′,M,D,θ(β,β′) ⩽ 1 always and so by Proposition 8.1 the integral in (15.5) is ≪ ωm(ZN⩾−m)ωm′ ′(ZN⩾−m′) = h(m)h(m′) ≪ M2.

We immediately see that the error incurred by adding in the terms D > M/10 to (15.5) is ≪ e−Ω(M).

When D is very negative we need an alternative argument. By the inequality 1 − e−x ⩽ x we have 1−exp −2D−θϱ∗u|β(L)τx∗|β′(L) ≪ 2Dϱ∗u|β(L)τx∗|β′(L). Thus, since τx∗|β′(L) ⩽ 1, it follows from Lemma 7.2 and the definition (14.4) that we additionally have Ψm,m′,M,D,θ(β,β′) ≪ 2Dr2 if β is r-bounded up to L, and hence certainly if β is r-bounded. Thus, defining R(β) to be the minimal integer r for which β is r-bounded (as in Definition 8.11), we have using Corollary 8.13 that

Ψm,m′,M,D,θ dωm dωm′ ′ ≪ 2Dωm′ ′(ZN⩾−m′)

r2ωm(R(β) = r)

ZN⩾−m ZN⩾−m′

r

(M + r + 1)e−r ≪ M22D.

≪ 2DM

r∈Z⩾0

From this (and since 2log 2 > 1) we see that the error from adding the terms D < −M/10 to (15.5) is also ≪ e−Ω(M).

Thus, up to error e−Ω(M), we can replace fM(θ) by the completed sum f˜M(θ) =

(log 2)D−θ

Ψm,m′,M,D,θ(β,β′)dωm dωm′ ′.

m,m′⩽M ZN⩾−m×ZN⩾−m′

D∈Z

Recalling the definition (14.4), and temporarily writing ϱ∗u|β = ϱ∗u|β(L), τx∗|β′ = τx∗|β′(L) for brevity, it follows that f˜M(θ) equals

D−θϱ∗u|βτx∗|β′ 1Wm,M(β)1W

E 1 − e−2

(β′)dωm(β)dωm′ ′(β′).

(log 2)D−θ

m′,M

m,m′⩽M ZN⩾−m ZN⩾−m′

D∈Z

Taking the sum over D on the inside and using (2.19) with ξ = θ and λ = ϱ∗u|βτx∗|β′, we see that f˜M(θ) equals

cg θ − log2(ϱ∗u|βτx∗|β′) 1Wm,M(β)1W

(β′)dωm(β)dωm′ ′(β′).

E ϱ∗u|βτx∗|β′

m′,M

m,m′⩽M ZN⩾−m ZN⩾−m′

Recalling the definitions (15.3) and (15.4), we see that (15.2) indeed holds, and this concludes the proof. □

- 15.2. Convergence of the measures µM. The remaining task is to examine the convergence of


the sequences of measures (µM)∞M=1 and (µ′M)∞M=1. In this section we handle the first of these sequences in detail. Recall that µM is defined in (15.3), which we can write as

Eϱ∗u|β(L(M))cψ log2 ϱ∗u|β(L(M)) 1m⩽M1Wm,M(β)dωm(β). Set

ψ dµM =

m⩾0 ZN⩾−m

Eϱ∗u|β(L(M))cψ log2 ϱ∗u|β(L(M)) 1minβ=−m1arg minβ⩽L(M)dωm(β), (15.6)

ψ d˜µM =

m⩾0 ZN⩾−m

where minβ = mini∈{0}∪N β(i) and arg minβ denotes the smallest index q ⩾ 0 for which β(q) = minβ. Our main result is the following. Here, dBL[µ;ν] denotes the bounded Lipschitz distance between two measures; for a full discussion of this concept, see Appendix E.

- Lemma 15.2. We have dBL[µM;µ˜M] ≪ e−Ω(M). In the proof of this lemma we will use the following auxiliary bounds.


### Lemma 15.3. Uniformly for m ∈ Z⩾0, ℓ ∈ N, and N ∈ [ℓ,∞)∪{∞} we have the following bounds:

Eϱ∗u|β(ℓ)c dωm(β) ≪ 2−m/4; (15.7)

min β=−m arg min β⩽ℓ

Eϱ∗u|β(ℓ)c dωm(β) ≪ r2(m + r + 1)e−r; (15.8)

min β=−m R⩽N(β)=r

Eϱ∗u|β(ℓ)c dωm(β) ≪ r3(1 + q)κ−3/2 (15.9)

min β=−m R⩽N(β)=r arg min β=q

for q ⩽ ℓ, and

Eϱ∗u|β(ℓ)c dωm(β) ≪ r2(1 + m)O(1)T−η/2. (15.10)

min β=−m R⩽N(β)=r T(β)>T

Here we define R⩽∞(β) := R(β), the smallest integer r for which β is r-bounded. Proof. The key estimate will be Lemma 7.2. From this, Hölder’s inequality and AM-GM we have that, if minβ = −m and arg minβ ⩽ ℓ,

Eϱ∗u|β(ℓ)c ⩽ Eϱ∗u|β(ℓ) cP(ϱ∗u|β(ℓ) ̸= 0)1−c ≪ R⩽ℓ(β)3(1 + arg minβ)κ2−m/3

⩽ (R⩽ℓ(β)6 + (1 + arg minβ)2κ)2−m/3. Therefore

Eϱ∗u|β(ℓ)c dωm(β)

min β=−m arg min β⩽ℓ

≪ 2−m/3

(1 + q)2κωm{arg minβ = q} + 2−m/3

r6ωm{R⩽ℓ(β) = r}.

q⩾0

r

To estimate the two terms on the right we use (8.16) and Corollary 8.13 respectively, obtaining that the above is

≪ (1 + m)2−m/3

(1 + q)2κ−3/2 +

r6(r + 1)e−r ≪ (1 + m)2−m/3 ≪ 2−m/4,

q

r

which gives (15.7). For (15.8) we use Hölder as above, but now using the trivial bound P(ϱ∗u|β(ℓ) ̸=

0) ⩽ 1. This gives Eϱ∗u|β(ℓ)c ≪ R⩽ℓ(β)2 ⩽ R⩽N(β)2, and so

Eϱ∗u|β(ℓ)c dωm(β) ≪ r2ωm{R⩽N(β) = r}.

min β=−m R⩽N(β)=r

The bound (15.8) follows using Corollary 8.13.

For (15.9) we proceed as for (15.7), except we replace R⩽ℓ(β) by R⩽N(β) and avoid the temptation to apply AM-GM. We then have

Eϱ∗u|β(ℓ)c dωm(β) ≪ r3(1 + q)κ2−m/3ωm{arg minβ = q},

min β=−m R⩽N(β)=r arg min β=q

and the result follows from Lemma 8.6 and the crude estimate (1 + m)2−m/3 ≪ 1. Finally, for (15.10) we proceed as for (15.8), obtaining

Eϱ∗u|β(ℓ)c dωm(β) ≪ r2ω{R⩽N(β) = r,T(β) > T} ⩽ r2ωm{T(β) > T},

min β=−m R⩽N(β)=r T(β)>T

which gives the required bound using Corollary 8.16. □ Proof of Lemma 15.2. Let ψ be a function on R/Z with ∥ψ∥Lip ⩽ 1. In particular, ∥ψ∥∞ ⩽ 1 and so we have

ψ dµM − ψ d˜µM

⩽

Eϱ∗u|β(L(M))c 1minβ=−m,arg minβ⩽L(M) − 1m⩽M1Wm,M(β) dωm(β). (15.11)

m⩾0 ZN⩾−m

Recall that Wm,M is the set of walks β satisfying items (1) – (4) in Section 14, and so we may write 1Wm,M(β) = 1R⩽L(M)(β)⩽R(M)1T⩽L(M)(β)⩽T(M)1min0⩽i⩽L(M) β(i)=−m1minβ−1(−m)⩽eC0M. Restricted to walks β in ZN⩾−m, for some m ⩾ 0, we have

1m⩽M1Wm,M(β) = 1m⩽M1R⩽L(M)(β)⩽R(M)1T⩽L(M)(β)⩽T(M)1minβ=−m1arg minβ⩽eC0M.

Note that, when written this way, it is clear that 1m⩽M1Wm,M(β) ⩽ 1minβ=−m1arg minβ⩽L(M) pointwise for β ∈ ZN⩾−m (and so the absolute value signs in (15.11) are unnecessary). Writing L = L(M) for brevity, by a telescoping sum we may bound (15.11) as a sum of four terms

Eϱ∗u|β(L)c1m>M1minβ=−m1arg minβ⩽L dωm(β), (15.12)

m⩾0 ZN⩾−m

Eϱ∗u|β(L)c1m⩽M1minβ=−m1arg minβ⩽L1R⩽L(β)>R(M) dωm(β), (15.13)

m⩾0 ZN⩾−m

Eϱ∗u|β(L)c1m⩽M1minβ=−m1eC0M<arg minβ⩽L1R⩽L(β)⩽R(M) dωm(β), (15.14) and

m⩾0 ZN⩾−m

Eϱ∗u|β(L)c1m⩽M1minβ=−m1arg minβ⩽eC0M1R⩽L(β)⩽R(M)1T⩽L(β)>T(M) dωm(β). (15.15)

m⩾0 ZN⩾−m

We bound the contributions from these pieces using Lemma 15.3, showing that in each case we get a bound ≪ e−Ω(M). In what follows, recall from Definition 11.1 that R(M) := 20M and that T(M) := e40M/η.

- To bound (15.12) we use (15.7) and sum over m > M. This clearly gives a bound ≪ e−Ω(M).
- To bound (15.13) we use (15.8). Summing over m ⩽ M and r > R(M), this gives a bound

≪

m⩽M r>R(M)

r2(m + r + 1)e−r ≪ e−Ω(M).

- To bound (15.14) we use (15.9). Summing this over m ⩽ M, r ⩽ R(M), and eC0M < q ⩽ L gives


r3(1 + q)κ−3/2 ≪ M5(eC0M)κ−1/2 ≪ e−Ω(M).

≪ M

r⩽R(M) eC0M<q⩽L

Finally, to bound (15.15) we use (15.10), noting that T(β) ⩾ T⩽L(β). Summing this over m ⩽ M and r ⩽ R(M) gives a bound of MO(1)T(M)−η/2 ≪ e−Ω(M). This completes the proof of

- Lemma 15.2. □


We now define measures µ(ℓ) by ψ dµ(ℓ) :=

min β=−m arg min β⩽ℓ

m⩾0

Thus from the definition (15.6) we see that

Eϱ∗u|β(ℓ)cψ(log2 ϱ∗u|β(ℓ))dωm(β). (15.16)

µ˜M = µ(L(M)). (15.17) We now claim the following.

- Proposition 15.4. There is a Borel measure µ on R/Z with ∥µ∥BL = dBL[µ;0] < ∞ such that dBL[µ(ℓ);µ] → 0 as ℓ → ∞.


Proof. Since the space of measures is complete with respect to the bounded Lipschitz metric (Lemma E.1) it is enough to show that the µ(ℓ) are a Cauchy sequence in the bounded Lipschitz norm. For the rest of the section suppose that ψ ∈ C(R/Z) is a test function with ∥ψ∥Lip ⩽ 1. We first observe the inequality

xcψ(log2 x) − ycψ(log2 y) ≪ |x − y|c (15.18)

for x,y ∈ [0,∞). To prove this, suppose wlog that y ⩾ x and write y = x + h. If x = O(h) then the result is trivial. Otherwise, we have

h x

h x ≪ hc

xc ψ(log2 x) − ψ(log2(x + h)) = xc ψ(log2 x) − ψ(log2 x + O(

)) ≪ xc

by the Lipschitz property. Also

h x

h x

1−c ≪ hc, and together these statements give (15.18). We note also that

(x + h)c − xc ψ(log2(x + h)) ⩽ (x + h)c − xc ≪ xc 1 + O(

) − 1 ≪ hc

|x − y|c ⩽ xc + yc. (15.19) Let ℓ < ℓ′. Then by the definition (15.16) and from (15.18) we have

ψ dµ(ℓ) − ψ dµ(ℓ′)

⩽

m

min β=−m arg min β⩽ℓ

Eϱ∗u|β(ℓ)cψ(log2 ϱ∗u|β(ℓ)) − Eϱ∗u|β(ℓ′)cψ(log2 ϱ∗u|β(ℓ′)) dωm(β)

Eϱ∗u|β(ℓ′)c dωm(β)

+

min β=−m ℓ<arg min β⩽ℓ′

m

E ϱ∗u|β(ℓ) − ϱ∗u|β(ℓ′) c dωm(β) +

Eϱ∗u|β(ℓ′)c dωm(β). (15.20)

≪

min β=−m ℓ<arg min β⩽ℓ′

min β=−m arg min β⩽ℓ

m

m

To bound the first term we split into two parts. As usual, R(β) denotes the least integer so that β is R(β)-bounded, and T(β) the least integer such that β is T(β)-bounded. The ‘main’ region of integration is over m ⩽ ℓη0 and β for which R(β) ⩽ ℓη0 and T(β) ⩽ ℓ1/8, where here η0 ∈ (0,η) is an absolute constant to be specified. On this region, it follows from (7.16) with a telescoping sum that E|ϱ∗u|β(ℓ) − ϱ∗u|β(ℓ′)| ≪ e−Ω(ℓ1/4), and hence E|ϱ∗u|β(ℓ) − ϱ∗u|β(ℓ′)|c ≪ e−Ω(ℓ1/4) by Hölder’s inequality. Since ωm(ZN⩾−m) ≪ m, the contribution of the main region of integration to the first term in (15.20) is ≪ e−Ω(ℓ1/4).

### To estimate the contribution to the first term from the remaining portions, we first apply (15.19), thereby reducing matters to estimating

Eϱ∗u|β(ℓ˜)c dωm(β), (15.21)

Eϱ∗u|β(ℓ˜)c dωm(β),

min β=−m R(β)>ℓη0

min β=−m arg min β⩽ℓ

m⩽ℓη0

m>ℓη0

and

Eϱ∗u|β(ℓ˜)c1minβ=−m dωm(β) (15.22)

R(β)⩽ℓη0 T(β)>ℓ1/8

m⩽ℓη0

for ℓ˜∈ {ℓ,ℓ′}. (We dropped the arg min conditions in the second estimate in (15.21) and in (15.22) since we will not need these in the estimations.)

The contribution from the first integral in (15.21) is ≪ e−Ω(ℓη0) < ℓ−10 by (15.7). The contribution from the second integral in (15.21) can be estimated using (15.8) with N = ∞,

which gives a bound of

r2(m + r + 1)e−r ≪ e−Ω(ℓη0/2) < ℓ−10. (15.23)

≪

m⩽ℓη0 r>ℓη0

Finally, the contribution from (15.22) can be estimated using (15.10), which gives a bound of ≪ ℓ−η/16

(r(1 + m))O(1) ≪ ℓ−η/32,

m⩽ℓη0 r⩽ℓη0

provided that η0 is chosen appropriately. This will be the weakest of the various estimates we obtain.

We also need to estimate the second term in (15.20). Using (15.7), the contribution from m > ℓη0 is < ℓ−10 similarly to before.

The contribution from m ⩽ ℓη0 and r ⩾ ℓη0 is < ℓ−10 as in the previous estimation of the second integral in (15.21).

The final remaining contribution is at most

Eϱ∗u|β(ℓ′)c dωm(β).

min β=−m ℓ<arg min β⩽ℓ′

m⩽ℓη0 r⩽ℓη0

By (15.9) with N = ∞ this is ≪ ℓ5η0

(1 + q)κ−3/2 ≪ ℓ5η0+κ−1/2 < ℓ−1/10.

q>ℓ

Putting everything together, it follows that ψ dµ(ℓ) − ψ dµ(ℓ′) ≪ ℓ−η/32.

Since ψ was an arbitrary Lipschitz test function, it follows that dBL[µ(ℓ);µ(ℓ′)] ≪ ℓ−η/32, which establishes that the µ(ℓ) are indeed a Cauchy sequence. □

The following proposition summarises what we have shown.

- Proposition 15.5. Let measures µM be defined as in (15.3). Then there is a Borel measure µ on R/Z with ∥µ∥BL = dBL[µ;0] < ∞ such that dBL[µM;µ] → 0 as M → ∞. Moreover, dBL[µ(ℓ);µ] → 0 as ℓ → ∞, where the measures µ(ℓ) are defined as in (15.16). Proof. This follows by combining Lemma 15.2, (15.17) and Proposition 15.4. □


- 15.3. Convergence of the measures µ′M. In this section we examine the convergence of the

sequence of measures (µ′M)∞M=1, where the µ′M are defined in (15.4). The analysis is very similar to that in the previous section, so we restrict ourselves to stating the main results and indicating the

points at which the arguments differ in minor details. Analogously to Proposition 15.5, the main statement is the following.

- Proposition 15.6. Let measures µ′M be defined as in (15.4). Then there is a Borel measure µ′ on


R/Z such that ∥µ′∥BL = dBL[µ′;0] < ∞ and dBL[µ′M;µ′] → 0 as M → ∞. Moreover, dBL[µ′(ℓ);µ′] → 0 as ℓ → ∞, where the measures µ′(ℓ) are defined by

ψdµ′(ℓ) :=

m⩾0

min β′=−m arg min β′⩽ℓ

Eτx∗|β′(ℓ)cψ(log2 τx∗|β′(ℓ))dωm′ (β′), (15.24)

where c = −log log 2log 2 .

Proof. (Sketch.) For the most part the argument is the same as the one in the previous section, replacing β by β′, ϱ∗u|β by τx∗|β′, and ωm by ωm′ throughout. In place of the estimates (7.5) and

- (7.6) from Lemma 7.2, we instead use (respectively) the trivial bound τx|β′(ℓ) ⩽ 1 and (6.7). With very minor modifications this allows us to recover analogues of all the statements in Lemma 15.3. Later on in the proof, at the point where we applied a telescoping sum to (7.16), we instead apply Lemma 6.4, the T-positivity of β′, and a telescoping sum, which gives a similar bound E|τx∗|β′(ℓ) − τx∗|β′(ℓ′)| ≪ e−Ω(ℓ1/4) at the appropriate point. □


- 15.4. µ is not zero. In this section we prove that the measure µ is not zero. Whilst this follows from Theorem 1.1 and the main result of Ford [20], it does not take long to provide a direct proof using the machinery we have set up.


Our starting point is (15.16). We take ψ = 1 and we restrict attention to walks β which satisfy ξ1 = C, ξ2 = ··· = ξC+1 = −1, and which are R-bounded and T-positive, where R := C2 and T := eC2. Here C is a sufficiently large constant to be specified later. Denote by BC the collection of such walks which additionally satisfy minβ = 0 (and hence arg minβ = 0). Ignoring all terms in (15.16) with m > 0, it suffices to prove that there is some choice of C (independent of ℓ) such that

ω0(BC) > 0 (15.25) and that

Eϱ∗u|β(ℓ)c ≫ 1 (15.26) uniformly for β ∈ BC and all ℓ (the implied constant may depend on C).

We begin with the first statement (15.25). Denote by BC∗ the event BC without the R-bounded and T-positive conditions. By Lemma 8.3 we have, for all sufficiently large N,

β(i) ⩾ 0 .

ω0(BC∗ ) ≫ N1/2P β ∈ BC∗ , min

1⩽i⩽N

The event that β ∈ BC∗ and that min1⩽i⩽N β(i) ⩾ 0 has probability (eC−+1)!C−1 P(min1⩽i⩽N−C−1 γ(i) ⩾

- 0), where γ is another Pois(1) − 1 walk. This is ∼ (eC−+1)!C−1 h(0)(N − C − 1)−1/2 ≫ C−C−3/2N−1/2.


It follows that ω0(BC∗ ) ≫ C−C−3/2. The desired result (15.25) is immediate from this and Corollary 8.13 and Lemma 8.15 and the choice of R and T.

- For (15.26), it suffices by Hölder’s inequality and Corollary 7.5 to show that Eϱ∗u|β(ℓ) ≫ 1 (15.27)


and that uniformly for β ∈ BC and all ℓ sufficiently large. Again the implied constant can depend on C. Let us recall the definition (7.1), which is

εi,j2−ui,j ∈ [1 − 2−ℓ,1] .

ϱ∗u|β(ℓ) = 2−β(ℓ)

1

i⩽ℓ;j∈[1+ξi]

ε⩽ℓ

We can now prove (15.27). We restrict to ε⩽ℓ satisfying ε1,1 = 1, ε1,2 = ··· = ε1,C+1 = 0, (15.28)

and the other εi,j can be arbitrary. Note there are no εi,j for 2 ⩽ i ⩽ C + 1 since 1 + ξi = 0 for these i. Deterministically, we have that

0 ⩽

εi,j2−ui,j ⩽

(1 + ξi)21−i < 101

i⩾C+2

i⩾C+2

for C large enough, using here the fact that β is C2-bounded and so |ξi| ⩽ C2iκ. Therefore for any such ε we have

εi,j2−ui,j ∈ [1 − 2−ℓ,1] ⩾ inf

P(2−u1,1 ∈ 1 − x − [2−ℓ] ≫ 2−ℓ. (15.29)

P

x∈[0,101 ]

i⩽ℓ;j∈[1+ξi]

(To justify this last step observe that if f(x) is the density function of 2−u1,1 (where, recall, u1,1 is uniform on [0,1]) and g(x) is the density function of a uniform U[21,1] variable, then a short calculation gives that f(x)/g(x) ⩾ 1/2log 2 > 21.) The number of choices for ε⩽ℓ satisfying (15.28) is 2−C−12 i⩽ℓ(1+ξi) = 2−C−12ℓ+β(ℓ). Summing (15.29) over these choices immediately gives (15.27).

- 15.5. µ′ is not zero. In this subsection we show that µ′ is not zero. Our starting point is (15.24). We take ψ to be the constant function 1, and we remove all terms


from the sum except m = 0, noting that they are all non-negative. It thus suffices to prove that

Eτx∗|β′(ℓ)c dω0′ (β′) ≫ 1 (15.30) uniformly in ℓ. Note that both the minβ′ = 0 condition and the arg min condition are trivial here since ω0′ is supported on ZN⩾0 and the minimum of β′ occurs at 0. In order to prove this we introduce the representation function

rx|β′,ℓ(t) := #{ε = (εi,j)i⩽ℓ;j∈[1−ξ′

εi,jxi,j = t}.

i] :

i⩽ℓ;j∈[1−ξi′]

Thus by definition (6.1) we have

τx∗|β′(ℓ) = 2β′(ℓ)−ℓ|Supp(rx|β′,ℓ)|. (15.31) Note also that

rx|β′,ℓ(t) = 2ℓ−β′(ℓ). (15.32)

t

We proceed via a second moment argument essentially identical to the one in the proof of Lemma 12.3 (which is unsurprising since our task here is closely analogous to the one there). By opening up the second moment we have

(εi,j − ε′i,j)xi,j = 0 . (15.33)

rx|β′,ℓ(t)2 =

### P

E

i⩽ℓ;j∈[1−ξi′]

ε,ε′

t

We foliate the sum over ε,ε′ according to the largest index r for which there is some s such that εr,s ̸= ε′r,s. For any such pair ε,ε′, the inner probability is ≪ 2−r; this follows by revealing all xi,j

except xr,s and applying the anti-concentration estimate (5.6). The number of pairs ε,ε′ with a given value r is ⩽ 22 i⩽r(1−ξi′)+ r<i⩽ℓ(1−ξi′) = 2ℓ−β′(ℓ)+r−β′(r). Therefore from (15.33) we obtain

rx|β′,ℓ(t)2 ≪ 2ℓ−β′(ℓ)

2−β′(r).

E

r⩽ℓ

t

If we assume that β′ is T-positive (for some T) then β′(r) ⩾ −T + r1/4 and so E

rx|β′,ℓ(t)2 ≪ 2ℓ−β′(ℓ)+T.

t

In particular, with probability at least 21 in (x | β′) we have

rx|β′,ℓ(t)2 ≪ 2ℓ−β′(ℓ)+T.

t

For any such (x | β′) it follows from this, (15.31) and (15.32) that τx∗|β′(ℓ) ≫ 2−T, and so

Eτx∗|β′(ℓ)c ≫ 2−cT. The desired result (15.30) now follows from the fact that

ω0′ {β′ : β′ is T-positive} > 0 for sufficiently large T, which is an immediate consequence of Corollary 8.16.

- 15.6. Conclusion of the proof of Theorem 1.1. It is now a fairly straightforward matter to complete the proof of Theorem 1.1. We begin with (14.5), which we repeat here:


p(k) = (c0 + o(1))k−δ(log k)−3/2 fM(ξ) + O(e−Ω(M)) . (15.34) This was established under the assumption that M ⩽ M0(k) for some fixed function M0 with limk→∞ M0(k) = ∞. We showed in (15.1) and (15.2) that

∥fM − f˜M∥∞ ≪ e−Ω(M) (15.35) where

f˜M = g ∗ µM ∗ µ′M (15.36)

with g ∈ C∞(R/Z) being the function in (1.2). We have also shown that µM → µ and µ′M → µ′ in bounded Lipschitz norm. To complete the proof we set f := c0g ∗ µ ∗ µ′. Then f ∈ C∞(R/Z) by two applications of Lemma E.3. By (15.34) to (15.36), it suffices to show that

∥g ∗ µM ∗ µ′M − g ∗ µ ∗ µ′∥∞ → 0. To show this, we use the triangle inequality and Lemma E.2 to bound

∥g ∗ µM ∗ µ′M − g ∗ µ ∗ µ′∥∞ ⩽ ∥g ∗ µM ∗ (µ′M − µ′)∥∞ + ∥g ∗ (µ − µM) ∗ µ′∥∞ ⩽ dBL[µ′M;µ′]∥g ∗ µM∥Lip + dBL[µM;µ]∥g ∗ µ′∥Lip.

We have dBL[µ′M;µ′],dBL[µM;µ] → 0, whilst ∥g ∗ µM∥Lip and ∥g ∗ µ′∥Lip are bounded uniformly in M by Lemma E.3. This concludes the proof of Theorem 1.1.

## Part 5. Description of the measures

We have completed the proof of Theorem 1.1, but the measures µ,µ′ have only been described as rather complicated limits over random walks satisfying certain technical conditions. Our task in this, the final part of the main paper, is to remove these conditions (and the random walks!) and prove the characterisations of these measures in Propositions 1.3 and 1.4.

16. Description of µ

The proof of Proposition 1.3 is the somewhat more difficult of these two tasks. At the moment, we have characterised µ as the (bounded Lipschitz) limit of measures µ(ℓ), defined as in (15.16). Once again, in this section η0 ∈ (0,η) denotes a sufficiently small absolute constant.

- 16.1. From walks to sequences. Recall the definition (8.1) of h(m) and that (see Proposition 8.1


(2)) h(m) = (2/π)1/2(m + 1) for m ⩾ 0. By a slight abuse of notation we now write h(x) := (2/π)1/2(x + 1)+ for all x ∈ R. (That is, h(x) = (2/π)1/2(x + 1) for x > −1, and 0 otherwise.) We observe the relation

s+1

e−ah(s − a) =

e−uh(s + 1 − u)du (16.1)

a

for a ⩽ s + 1. Definition 16.1. Denote by Ωm the space of all sequences x = (xi)∞i=1 of real numbers with limi→∞ xi = ∞ and satisfying xi ⩽ i + m for all i.

We consider the σ-algebra on Ωm generated by sets of the form {x ∈ Ωm : (x1,...,xr) ∈ B} for some r and for some Borel measurable B ⊂ Rr, which we can and do assume is contained in {(x1,...,xr) : xi ⩽ i + m for i = 1,...,r}. We define

νm{x : (x1,...,xr) ∈ B} :=

h(m + r − xr)e−xr10<x1<···<xr dx1 ···dxr (16.2)

B

We remark that without the factor h(m+r −xr), this would be the usual density functional for the Poisson process. It turns out that νm extends to give a well-defined measure on Ωm with the stated σ-algebra. This is a continuous variant of the Doob conditioning construction given in Lemma 8.2.

- Lemma 16.2. The measure νm is well-defined and νm(Ωm) := h(m).


Proof. The essential point is to check compatibility of (16.2) across different values of r, that is to say we must show that the measures of {x : (x1,...,xr−1) ∈ B} and {x : (x1,...,xr) ∈ B × [0,r + m]} coincide whenever B ⊂ ri=1−1[0,i + m] ⊂ Rr−1. To this end, if r ⩾ 2 we have

νm{x :(x1,...,xr) ∈ B × [0,r + m]}

r+m

h(m + r − xr)e−xr dxr dx1 ...dxr−1

=

1B(x1,...,xr−1)

Rr−1

xr−1

1B(x1,...,xr−1)h(m + r − 1 − xr−1)e−xr−1 dx1 ...dxr−1

=

Rr−1

= νm{x : (x1,...,xr−1) ∈ B},

where the middle step follows from (16.1) with a = 0 and s = m + r − 1 − xr−1 upon making the substitution u = xr − xr−1. If r = 1 we instead take the lower limit of the inner integral down to 0; this confirms that νm(Ωm) = νm{x : x1 ∈ [0,m + 1]} = h(m). □

Given x = (xi)∞i=1 ∈ Ωm, we may define the walk βx by βx(j) = #{i : xi ⩽ j} − j. Thus, the number of elements of x in (j − 1,j] is β(j) − β(j − 1) + 1. Observe that the condition that an increasing sequence x lies in Ωm is equivalent to minβx ⩾ −m. Indeed, if x ∈ Ωm then xi ⩽ i + m for all i, and so xj−m ⩽ j for j > m, which means that #{i : xi ⩽ j} ⩾ j − m and so βx(j) ⩾ −m. Conversely if x ∈/ Ωm then xj > j + m for some j, which means that #{i : xi ⩽ j + m} ⩽ j − 1 and so βx(j + m) ⩽ −m − 1.

### Lemma 16.3. Let F : Ωm → C be an integrable function. Then

EF(u | β)dωm(β).

### F(x)dνm(x) =

ZN⩾−m

Ωm

Here, (u | β) is the upper Poisson process u conditioned to β = β as described in Section 5.3.

Proof. By a limiting argument we may assume that F depends only on the elements of x in [0,L] for some L (the functions we consider will in any case have this property). We evaluate the LHS by splitting up according to the values of βx(j), j = 1,...,L. Note that βx(j) = cj for j = 1,...,L is the condition that xi ∈ (j − 1,j] for j − 1 + cj−1 < i ⩽ j + cj, j ⩽ L, and also that xL+cL+1 > L. Therefore, writing r := cL + L for brevity, we have

L

F(x)

1βx(j)=cj dνm(x)

Ωm

j=1

F(x1,...,xr)h(m + r + 1 − xr+1)1x1<···<xre−xr+1 dx1 ...dxr+1

= xi∈(j−1,j] for

j−1+cj−1<i⩽j+cj, L<xr+1⩽m+r+1

= e−Lh(m + cL) x

F(x1,...,xr)1x1<···<xr dx1 ...dxr

i∈(j−1,j] for j−1+cj−1<i⩽j+cj

L

1 (cj − cj−1 + 1)!

= e−Lh(m + cL)

EF(u | β),

j=1

where β is any walk with β(j) = cj for j ⩽ L (it does not matter which). Here, to get the middle step we integrated out the xr+1 variable and applied (16.1). This is exactly

ωm{β : β(j) = cj for j = 1,...,L}EF(u | β), where here we used the definition (8.6), recalling that the increments of β are Pois(1)−1. Summing over all choices of c1,...,cL gives the result. □

- 16.2. Description of the measure µ. We turn now to the main analysis and proof of Proposition 1.3. The argument will proceed as follows. In Proposition 15.5, we have already characterised µ as the BL-limit of the measures µ(ℓ) defined in (15.16). We have


Eϱ∗u|β(ℓ)cψ(log2 ϱ∗u|β(ℓ))dωm(β). (16.3)

ψ dµ(ℓ) :=

m⩾0 min0⩽i⩽ℓ β(i)=−m

Here, and for the rest of the section, c = −log log 2log 2 . Note that (16.3) differs slightly in appearance from (15.16); we have replaced the condition (minβ = −m) ∩ (arg minβ ⩽ ℓ) by min0⩽i⩽ℓ β(i) = −m, which is a seemingly weaker condition. However there is no contribution to (16.3) from any walks with minβ < −m, since ωm is supported on walks with minβ ⩾ −m, so the two definitions are equivalent.

Define µ(∗ℓ) by

2 π

1/2E(ℓ − uℓ)+ϱu(ℓ)cψ(log2 ϱu(ℓ)), (16.4)

ψ dµ(∗ℓ) :=

where ϱu(ℓ) is defined as in (1.3). To prove Proposition 1.3, it is enough to show that dBL[µ(ℓ);µ(∗ℓ)] = oℓ→∞(1). We will do this in steps, specifying intermediate measures µ(iℓ), i = 0,1,...,5, with µ(0ℓ) := µ(ℓ) and µ(5ℓ) := µ(∗ℓ), and show that dBL[µ(iℓ);µ(i−ℓ)1] = oℓ→∞(1) for i = 1,...,5; an application

of the triangle inequality then concludes the argument. For the remainder of the analysis, ψ denotes an arbitrary function on R/Z with ∥ψ∥Lip ⩽ 1. Then our task is to prove that

ψ dµ(iℓ) − ψ dµ(i−ℓ)1 = oℓ→∞(1), (16.5) uniformly in i ∈ {1,...,5} and ψ.

Step 1. First we compare µ(ℓ) to the measure µ(1ℓ) in which we restrict the integral in (16.3) to walks β which are suitably bounded, positive and for which m ⩽ ℓη0. More precisely, define µ1(ℓ) by

ψ dµ(1ℓ) :=

Eϱ∗u|β(ℓ)cψ(log2 ϱ∗u|β(ℓ))dωm(β).

min0⩽i⩽ℓ β(i)=−m R(β)⩽ℓη0 T(β)⩽ℓ1/8

m⩽ℓη0

We claim that (16.5) holds for i = 1, with a bound of ≪ ℓ−η/32 on the RHS. To prove this claim, we first restrict (16.3) to m ⩽ ℓη0. The error in doing this has already been handled via the first estimate in (15.21). The rest of the error comes from the contribution of β with minβ = −m, m ⩽ ℓη0, and arg minβ ⩽ ℓ but either R(β) > ℓη0 or T(β) > ℓ1/8; that these contributions are appropriately small follows in exactly the same way we bounded the second sum in (15.21) and the sum in (15.22).

Step 2. To obtain µ(2ℓ) from µ(1ℓ) we replace the two copies of ϱ∗u|β(ℓ) by ϱu|β(ℓ) (which is defined in (7.4)). Note that for ϱu|β(ℓ) to be defined we need (7.2) to be satisfied, that is to say limi→∞(i+ β(i)) = ∞. This will be the case for all walks under consideration here, which (since we can restrict

to the support of ωm) have minβ = −m. Moreover, by the definition of T-positive walk and the fact that T(β) ⩽ ℓ1/8, we have −ℓ1/8 + i1/4 ⩽ β(i) ⩽ ℓ1/8 + i3/4. Therefore the quantity ℓ′, defined to be minimal such that ℓ′ + β(ℓ′) ⩾ ℓ, will satisfy

ℓ′ ≍ ℓ. (16.6) We thus define µ(2ℓ) by

ψ dµ(2ℓ) :=

Eϱu|β(ℓ)cψ(log2 ϱu|β(ℓ))dωm(β).

min0⩽i⩽ℓ β(i)=−m R(β)⩽ℓη0 T(β)⩽ℓ1/8

m⩽ℓη0

By (15.18), and since ωm(ZN⩾−m) = h(m) ≪ 1 + m, in order to establish (16.5) with i = 2 it is sufficient to show

E ϱu|β(ℓ) − ϱ∗u|β(ℓ) c ≪ ℓ−10, (16.7) uniformly for β with T(β) ⩽ ℓ1/8. However from (7.16) and (7.17), Cauchy-Schwarz, and the triangle inequality, for such walks β we have

E ϱu|β(ℓ) − ϱ∗u|β(ℓ) ≪ e−Ω(ℓ1/4). Here we used (16.6) in the application of (7.17). The required statement (16.7) then follows using Hölder’s inequality.

Step 3. To obtain µ(3ℓ) from µ(2ℓ) we remove the constraints R(β) ⩽ ℓη0 and T(β) ⩽ ℓ1/8 again. However we retain the constraint β(ℓ) ⩾ 0 (which is implied by T(β) ⩽ ℓ1/8, since β(ℓ) ⩾ −ℓ1/8 + ℓ1/2−η > 0). Thus we define

ψ dµ(3ℓ) :=

m⩽ℓη0

Eϱu|β(ℓ)cψ(log2 ϱu|β(ℓ))dωm(β). (16.8)

min0⩽i⩽ℓ β(i)=−m β(ℓ)⩾0

To establish (16.5) with i = 3, the argument is similar to the case i = 1. Bounding ψ pointwise by

- 1, it suffices to bound


and

m⩽ℓη0

Eϱu|β(ℓ)c dωm(β) (16.9)

min0⩽i⩽ℓ β(i)=−m R(β)>ℓη0

m⩽ℓη0

Eϱu|β(ℓ)c dωm(β). (16.10)

min0⩽i⩽ℓ β(i)=−m R(β)⩽ℓη0 T(β)>ℓ1/8

- For (16.9) we use (7.7) and Corollary 8.13; (16.9) may then be bounded exactly as in (15.23), and


is seen to be ≪ ℓ−10. For (16.10), we note that we have an exact analogue of (15.10) for ϱu|β(ℓ), namely

Eϱu|β(ℓ)c dωm(β) ≪ rO(1)(1 + m)O(1)T−η/2.

min β=−m R(β)=r T(β)>T

The proof is the same, using the other estimates in Lemma 7.2. We can then proceed exactly as in the estimation of (15.22). This concludes the proof that (16.5) holds for i = 3.

Using Lemma 16.3, we can rewrite the definition (16.8) of µ(3ℓ). For a sequence x, denote by Sm the condition that #(x ∩ [0,i]) ⩾ i − m for i ⩽ ℓ, or equivalently xi−m ⩽ i for all m < i ⩽ ℓ, and S˜ the condition that #(x ∩ [0,ℓ]) ⩾ ℓ, or equivalently xℓ ⩽ ℓ. (These definitions also depend on ℓ, but this is fixed through the argument so we suppress this.) We include S−1 in the definition, with S−1 being the empty set.

Now (deterministically in u conditioned to β = β) we have that min1⩽i⩽ℓ β(i) ⩾ −m iff #((u | β) ∩ [0,i]) ⩾ i − m for i ⩽ ℓ, which is so if and only if (u | β) ∈ Sm. Therefore we have (deterministically)

1Sm\Sm−1(u | β) = 1min0⩽i⩽ℓ β(i)=−m. (16.11) Also (again deterministically) we have that β(ℓ) ⩾ 0 iff #((u | β) ∩ [0,ℓ]) ⩾ ℓ, which is so if and only if (u | β) ∈ S˜. Therefore

1S˜(u | β) = 1β(ℓ)⩾0. (16.12) Thus, if for m ⩾ 0 we define

Fm(x) := ϱx(ℓ)cψ(log2 ϱx(ℓ))1Sm\Sm−1(x)1S˜(x) (16.13)

(with ϱx(ℓ) defined as in (1.3)) and apply Lemma 16.3, then it follows using (16.8) and (16.11) and (16.12) that we have

ψ dµ(3ℓ) =

Fm(x)dνm(x).

m⩽ℓη0

Since Fm depends only on x1,...,xℓ we can write in the definition (16.2) of νm, obtaining

ψ dµ(3ℓ) =

=

Fm(x)h(m + ℓ − xℓ)e−xℓ10<x1<···<xℓ dx1 ···dxℓ

m⩽ℓη0

EFm(u)h(m + ℓ − uℓ). (16.14)

m⩽ℓη0

Here, as usual, u is the upper process (a rate 1 Poisson process on [0,∞)).

Step 4. For this step, we replace h(m + ℓ − uℓ) in (16.14) by (π2)1/2(ℓ − uℓ)+, that is we define ψ dµ(4ℓ) =

2 π

1/2

E(ℓ − uℓ)+Fm(u). (16.15)

m⩽ℓη0

For this we recall that h(x) = (2/π)1/2(x + 1)+, which implies that h(m + ℓ − uℓ) = O(m + 1) +

2 π

1/2(ℓ − uℓ)+.

(Here consider the cases ℓ − uℓ ⩾ 0 and ℓ − uℓ < 0 separately; in the latter case, the LHS is zero unless m + ℓ − uℓ ∈ (−1,m]).

Thus, to show (16.5) with i = 4, it is enough to show that the contribution from the O(m + 1) term is small. Since η0 ≪ 101 , it therefore suffices to show

E|Fm(u)| ≪ (1 + m)2ℓ−1/2 (16.16) for all m ⩽ ℓη0. We prove this by conditioning on the embedded walk β of u. The average on the LHS of (16.16) is

E|Fm(u | β)|dP(β),

where P denotes measure on the path space of β. By the definition (16.13) of Fm and (16.11) and (16.12) (and since |ψ| ⩽ 1), this is

Eϱu|β(ℓ)c dP(β). By (7.7) (noting here that β(ℓ) ⩾ 0 gives ℓ′ ⩽ ℓ), this is

≪

min0⩽i⩽ℓ β(i)=−m,β(ℓ)⩾0

R⩽ℓ(β)2 dP(β) =

≪

min0⩽i⩽ℓ β(i)=−m

By Lemma 8.12, this is

r

r2P(R⩽ℓ(β) = r, min

β(i) = −m).

0⩽i⩽ℓ

r2(m + r + 1)e−r ≪ (1 + m)2ℓ−1/2,

≪ ℓ−1/2

r

which is exactly (16.16). This completes the analysis of the case i = 4. Step 5. For the final step, we begin with the claim that if we extend the sum over m in (16.15)

to all m ⩾ 0 then we obtain ψ dµ(5ℓ) = ψ dµ(∗ℓ), where µ(∗ℓ) is defined in (16.4). Indeed, from the definition (16.13) of Fm and a telescoping sum we have

E(ℓ − uℓ)+Fm(u) = E(ℓ − uℓ)+ϱu(ℓ)cψ(log2 ϱu(ℓ))1S˜(u).

m⩾0

However, the cutoff 1S˜(u) is equivalent to 1uℓ⩽ℓ and so is redundant, and this establishes the claim. Therefore to prove (16.5) when i = 5, it is enough to show that

E(ℓ − uℓ)+Fm(u) = oℓ→∞(1).

m>ℓη0

Once again we sample using the embedded walk. By the definition (16.13) of Fm and (16.11) and (16.12), it is enough to bound

m>ℓη0

E(ℓ − (u | β)ℓ)+ϱu|β(ℓ)c dP(β). (16.17)

min0⩽i⩽ℓ β(i)=−m β(ℓ)⩾0

Here, for clarity we note that (u | β)ℓ is the ℓth element of (u | β) when listed in increasing order. Recall that, in the context of Lemma 7.2, ℓ′ is defined to be minimal so that ℓ′ + β(ℓ′) ⩾ ℓ. Since β(ℓ) ⩾ 0, we have ℓ′ ⩽ ℓ. Since all steps of β are ⩾ −1, for any s ⩾ 0 we have β(ℓ′ + s) ⩾ ℓ − ℓ′ − s, and so in particular minℓ′⩽i⩽ℓ β(i) ⩾ 0, and hence min0⩽i⩽ℓ β(i) = min0⩽i⩽ℓ′ β(i).

Denote by R⩽ℓ(β) the least integer R for which β is R-bounded to length ℓ. We use the bounds

- (7.7) and (7.8). Since ℓ′ ⩽ ℓ, these give Eϱu|β(ℓ) ≪ R⩽ℓ(β)2 and P(ϱu|β(ℓ) ̸= 0) ≪ ℓ32−m respectively. By Hölder’s inequality,


Eϱu|β(ℓ)c ⩽ R⩽ℓ(β)2cP(ϱu|β(ℓ) ̸= 0)1−c ⩽ R⩽ℓ(β)2ℓ22−m/3. Using the trivial bound (ℓ − (u | β)ℓ)+ ⩽ ℓ, (16.17) is bounded by

2−m/3

ℓ3

r2P R⩽ℓ(β) = r, min

β(i) = −m .

0⩽i⩽ℓ

m>ℓη0

r

By Lemma 8.12, this is bounded by ≪ ℓ3

r2(m + r + 1)e−r ≪ e−Ω(ℓη0).

2−m/3

m⩾ℓη0

r

This completes the proof of (16.5) for i = 5, and thus the whole proof of Proposition 1.3.

17. Description of µ′

In this section we establish Proposition 1.4, which is a description of the measure µ′. Recall that we have currently identified µ′ as the bounded Lipschitz limit of the measures µ′(ℓ), defined in (15.24), as ℓ → ∞. Throughout this section, ℓ will denote a large integer parameter. The reader may also want to recall the definition of the lower process x, defined just before Proposition 1.4, and the conditioned lower process (x | β′), which is described in Section 5.3. Throughout the section we will assume that β′ is a walk with increments ξi′ bounded above by 1 for which (6.2) holds. Given ℓ and β′, we denote by ℓ′ the least integer such that ℓ′ − β′(ℓ′) ⩾ ℓ, as in the statement of Corollary 6.3. In some cases where β′ is not clear from context, we will write this as ℓ′(β′) (which of course still depends on ℓ).

- 17.1. The first ℓ arrivals. In this subsection we assemble some ingredients for the main argument, having to do with the distribution of the first ℓ arrivals of (x | β′).


- Lemma 17.1. We have the following statements.


- (1) β′(ℓ) > 0 if and only if ℓ′ > ℓ;
- (2) The distribution of τx∗|β′(ℓ) depends only on the values of β′(1),...,β′(ℓ′);
- (3) We have log2(x | β′)ℓ = ℓ + β′(ℓ′) + O(1 + |ξℓ′′|).


Proof. (1) Indeed if β′(ℓ) > 0 then ℓ − β′(ℓ) < ℓ and so, since i − β′(i) is a non-decreasing function of i, we have ℓ′ > ℓ. Conversely if ℓ′ > ℓ then ℓ does not satisfy ℓ−β′(ℓ) ⩾ ℓ, which means β′(ℓ) > 0.

To prepare for (2) and (3) we begin by reviewing the coupling of the lower process x to the lower walk β′, as described in Section 5.3. The key features of the coupling are as follows. There is an auxiliary rate 1 Poisson process s such that β′(i) = i − #(s ∩ [0,i]), and the conditioned process (s | β′) := (s | β′ = β′) consists of sampling 1 − ξi′ uniform random elements from (i − 1,i], which are then ordered. We then define x = ϕ(s), where ϕ : [0,∞) → N is defined in Definition 5.1. In particular to establish (2) it is enough to show that the distribution of the first ℓ elements (s | β′)i, i = 1,...,ℓ, depends only on the values β′(1),...,β′(ℓ′). This statement is essentially the purpose of ℓ′. Indeed, since #((s | β′) ∩ [0,i]) = i − β′(i), we see that (deterministically)

ℓ′ − 1 < (s | β′)ℓ ⩽ ℓ′, (17.1) and (2) then follows.

Finally we turn to (3). Recall that by (5.4) we have log2 x = s + O(1). Thus to prove (3) it suffices to show that

(s | β′)ℓ = ℓ + β′(ℓ′) + O(1 + |ξℓ′′|). (17.2) From the definition of ℓ′ we have

(ℓ′ − 1) − β′(ℓ′ − 1) ⩽ ℓ − 1. (17.3) Using (17.1) and (17.3) (and ℓ′ − β′(ℓ′) ⩾ ℓ) one may check that

β(ℓ′) − 1 ⩽ (s | β′)ℓ − ℓ ⩽ β′(ℓ′ − 1), and so (since β′(ℓ) = β(ℓ′ − 1) + ξℓ′′) the desired statement (17.2) follows immediately. □

Recall that the embedded walk β′ has 1−Pois(1) steps. The following lemma records that ℓ′(β′) is usually O(ℓ).

- Lemma 17.2. Suppose that j ⩾ 1 is an integer. Then we have P(2jℓ ⩽ ℓ′(β′) < 2j+1ℓ) ≪ 2jℓe−2j−4ℓ.


Proof. Suppose that β′(ℓ′ − 1) < ℓ′/2. Then, since ℓ − 1 ⩾ (ℓ′ − 1) − β′(ℓ′ − 1) > ℓ′/2 − 1, we have ℓ′ < 2ℓ. Thus if ℓ′(β′) ⩾ 2jℓ then β′(ℓ′ − 1) ⩾ ℓ′/2 > (ℓ′ − 1)/2.

Now for any fixed t we have P(β′(t) ⩾ t/2) = P(Pois(t) ⩽ t/2) ⩽ e−t/8 by the first estimate in [4, Theorem A.1.15]. Thus if j ⩾ 1 then

P(β′(t) ⩾ t/2) ≪ 2jℓe−2j−4ℓ. □

P(2jℓ ⩽ ℓ′(β′) < 2j+1ℓ) ⩽

2jℓ−1⩽t<2j+1ℓ−1

17.2. The main argument. Recall from Proposition 15.6 that µ′ is the bounded Lipschitz limit of the measures µ′(ℓ) defined by

ψ dµ′(ℓ) :=

Eτx∗|β′(ℓ)cψ(log2 τx∗|β′(ℓ))dωm′ (β′). (17.4)

m⩾0 min0⩽i⩽ℓ β′(i)=−m

Here, ωm′ is defined as in Section 8.1, and c = −log log 2log 2 as usual. Note that walks β′ in the support of ωm′ are lower, that is to say they have steps bounded above by 1 rather than below by −1.

Define a measure µ′∗(ℓ) by ψ dµ′∗(ℓ) := (

2 π

)1/2E(log2 xℓ − ℓ)+τx(ℓ)cψ(log2 τx(ℓ)). (17.5)

Proposition 1.4 is equivalent to the statement that µ′∗(ℓ) → µ′ in bounded Lipschitz norm.

As in the last section, we will prove this by specifying intermediate measures µ′i(ℓ), i = 0,1,...,5, with µ′0(ℓ) := µ′(ℓ) and µ′5(ℓ) := µ′∗(ℓ), and show that

dBL[µ′i(ℓ);µ′i(−ℓ)1] = oℓ→∞(1) (17.6) for i = 1,...,5, and this is enough to complete the proof.

Step 1. In what follows we let ψ be an arbitrary function with ∥ψ∥Lip ⩽ 1. First we replace µ′(ℓ) by µ′1(ℓ) in which we restrict the integral in (17.4) to walks β′ which are suitably bounded, positive and for which m ⩽ ℓη0. More precisely, define µ′1(ℓ) by

ψ dµ′1(ℓ) :=

0⩽m⩽ℓη0

Eτx∗|β′(ℓ)cψ(log2 τx∗|β′(ℓ))dωm′ (β′).

min0⩽i⩽ℓ β′(i)=−m R(β′)⩽ℓη0 T(β′)⩽ℓ1/8

That (17.6) holds for i = 1 follows in essentially the same way as before.

Step 2. To obtain µ′2(ℓ) from µ′1(ℓ) we replace the two copies of τx∗|β′(ℓ) by τx|β′(ℓ), where here the relevant definitions are (6.1) and (6.3). Thus we define µ′2(ℓ) by

ψ dµ′2(ℓ) :=

Eτx|β′(ℓ)cψ(log2 τx|β′(ℓ))dωm′ (β′). (17.7)

min0⩽i⩽ℓ β′(i)=−m R(β′)⩽ℓη0 T(β′)⩽ℓ1/8

m⩽ℓη0

By (15.18), and since ωm′ (ZN⩾−m) = h′(m) ≪ 1 + m, it is sufficient to show E τx|β′(ℓ) − τx∗|β′(ℓ) c ≪ ℓ−10. (17.8)

Now since β′ is ℓ1/8-positive, we have β′(ℓ) ⩾ ℓ1/2−η − ℓ1/8 > 0. Therefore by (6.4) and the monotonicity property (6.5) we have τx∗|β′(ℓ) = τx|β′(ℓ − β′(ℓ)) ⩾ τx|β′(ℓ). We also have β′(2ℓ) ⩽ (2ℓ)1/8 + (2ℓ)1/2+η < ℓ, and so by further applications of (6.4) and (6.5) we have τx∗|β′(2ℓ) = τx|β′(2ℓ−β′(2ℓ)) ⩽ τx|β′(ℓ). Combining these facts and then applying Lemma 6.4 and a telescoping sum, we have

E|τx|β′(ℓ) − τx∗|β′(ℓ)| ⩽ E|τx∗|β′(2ℓ) − τx∗|β′(ℓ)| ≪ e−Ω(ℓ1/4). The required bound (17.8) then follows from Hölder’s inequality.

Step 3. To obtain µ′3(ℓ) from µ′2(ℓ) we remove the constraints R(β′) ⩽ ℓη0 and T(β′) ⩽ ℓ1/8 again. However we retain the constraint β′(ℓ) > 0 (which is implied by T(β′) ⩽ ℓ1/8 as noted above).

Thus we define ψ dµ′3(ℓ) :=

Eτx|β′(ℓ)cψ(log2 τx|β′(ℓ))dωm′ (β′). (17.9)

min0⩽i⩽ℓ β′(i)=−m β′(ℓ)>0

0⩽m⩽ℓη0

The proof that (17.6) holds with i = 3 is very similar to, but easier than, the handling of Step 3 in the last section. Bounding ψ and τx|β′(ℓ)c pointwise by 1, it suffices to bound

ωm′ {β′ : R(β′) > ℓη0} and

ωm′ {β′ : T(β′) > ℓ1/8}

m⩽ℓη0

m⩽ℓη0

That these are bounded by oℓ→∞(1) follows using Corollary 8.13 and Corollary 8.16 respectively, assuming that η0 is sufficiently small.

Now, as explained at the start of the proof of Lemma 17.1, the constraint β′(ℓ) > 0 is equivalent to ℓ′ > ℓ. Thus we may replace (17.9) by

ψ dµ′3(ℓ) :=

Eτx|β′(ℓ)cψ(log2 τx|β′(ℓ))dωm′ (β′).

min0⩽i⩽ℓ β′(i)=−m ℓ′(β′)=t

m⩽ℓη0 t>ℓ

Here, recall that we have written ℓ′(β′) for ℓ′ to emphasise that this quantity depends on β′. Observe that the conditions min0⩽i⩽ℓ β′(i) = −m and ℓ′(β′) = t depend only on β′(1),...,β′(t) (since t ⩾ ℓ), and so too does the integrand (since τx|β′(ℓ) is involves only the first ℓ elements of x, and the number of elements of x up to t is t − β′(t) ⩾ ℓ). Recalling the definition (see Section 8.1) of ωm′ , and in particular (8.9), it follows that

ψ dµ3′(ℓ) =

m⩽ℓη0 t>ℓ

h′(m + β′(t))Eτx|β′(ℓ)cψ(log2 τx|β′(ℓ))dP′(β′), (17.10)

min0⩽i⩽ℓ β′(i)=−m min0⩽i⩽t β′(i)⩾−m

where here P′ denotes measure on the path space of β′. Note that from (17.3) we have β′(t−1) ⩾ t−ℓ. Since all steps of β′ are bounded above by 1, it follows that β′(t − i) ⩾ t − ℓ − (i − 1) for all i ⩾ 1, and in particular minℓ⩽i⩽t−1 β′(i) ⩾ 1. Therefore we may replace (17.10) by

ψ dµ′3(ℓ) =

1t>ℓ1β′(t)⩾−mh′(m + β′(t))Eτx|β′(ℓ)cψ(log2 τx|β′(ℓ))dP′(β′).

min0⩽i⩽ℓ β′(i)=−m ℓ′(β′)=t

m⩽ℓη0 t

(17.11) Step 4. We use the fact that

2 π

h′(r) = (

)1/2r + O(1) (17.12)

for r ⩾ 0, which is Proposition 8.1 (2). Suppose that ℓ′(β′) = t and β′(t) ⩾ −m. Then from (17.12) and Lemma 17.1 (3) we have

2 π

h′(m + β′(t)) = (

)1/2 log2(x | β′)ℓ − ℓ + O(m + 1 + |ξt′|). (17.13)

Suppose that log2(x | β′)ℓ < ℓ. Then from Lemma 17.1 we have β′(t) ⩽ O(1+|ξt′|) and so by (17.12) h′(m + β′(t)) = O(1 + m + |ξt′|). Thus we may replace (17.13) by

2 π

)1/2(log2(x | β′)ℓ − ℓ)+ + O(1 + m + |ξt′|).

h′(m + β′(t)) = (

Next we multiply by the cutoff 1t>ℓ1β′(t)⩾−m appearing in (17.11); we claim that (still assuming ℓ′(β′) = t)

2 π

)1/2(log2(x | β′)ℓ − ℓ)+ + O(1 + m + |ξt′|). (17.14)

1t>ℓ1β′(t)⩾−mh′(m + β′(t)) = (

This is trivial if t > ℓ and β′(t) ⩾ −m, so suppose that either t ⩽ ℓ, or that β′(t) < −m. In either case, the LHS is zero. In both cases, β′(t) ⩽ 0 (in the first case this is since ℓ′(β′) = t and so t − β′(t) ⩾ ℓ by the definition of ℓ′). It follows from Lemma 17.1 (3) that ((log2 x | β′)ℓ − ℓ)+ = O(1 + |ξt′|), so the claim follows in this case also.

Now we define µ′4(ℓ) itself. We set

2 π

ψ dµ′4(ℓ) = (

E(log2(x | β′)ℓ − ℓ)+τx|β′(ℓ)cψ(log2 τx|β′(ℓ))dP′(β′). (17.15)

)1/2

m⩽ℓη0 min0⩽i⩽ℓ β′(i)=−m

This is the same as (17.11) except that we have replaced 1t>ℓ1β′(t)⩾−mh′(m + β′(t)) by the main term in (17.14); note that we have removed the sum over t, since nothing on the right in (17.15) references this variable.

To prove (17.6) in the case i = 4, we must handle the contribution from the error term in (17.14). We split this error term into two parts: the contribution from O(1 + m) and the contribution from

- O(|ξt′|). These terms are, by definition,


and

≪

(1 + m)

m⩽ℓη0

t

Eτx|β′(ℓ)cψ(log2 τx|β′(ℓ))dP′(β′) (17.16)

min0⩽i⩽ℓ β′(i)=−m ℓ′(β′)=t

≪

m⩽ℓη0 t

|ξt′|Eτx|β′(ℓ)cψ(log2 τx|β′(ℓ))dP′(β′). (17.17)

min0⩽i⩽ℓ β′(i)=−m

Bounding (17.16). We bound the τ and ψ terms trivially by 1; thus this contribution is ≪

β′(i) ⩾ −m)

dP′(β′) ≪

(1 + m)P( min

(1 + m)

min0⩽i⩽ℓ β′(i)=−m ℓ′(β′)=t

1⩽i⩽ℓ

m⩽ℓη0

m⩽ℓη0

t

From the definition (8.2) and the fact that h′(m) ≪ 1 + m, this is ≪ ℓ3η0−1/2, which is acceptable. Bounding (17.17). Again we bound the τ and ψ terms trivially by 1, so the contribution is

∞

|ξt′|dP′(β′) ≪

β′(i) = −m, ℓ′(β′) = t, |ξt′| > s .

P min

≪

min0⩽i⩽ℓ β′(i)=−m ℓ′(β′)=t

0⩽i⩽ℓ

m⩽ℓη0 t

m⩽ℓη0 t

s=0

(17.18) We divide our sum over t dyadically. For the sum over t ⩽ 2ℓ we have the upper bound

∞

β′(i) = −m, sup i⩽2ℓ

|ξi′| > s).

P min

≪

0⩽i⩽ℓ

m⩽ℓη0

s=0

The contribution from s ⩽ ℓη0 is ≪ ℓη0 m⩽ℓη0 P min0⩽i⩽ℓ β′(i) = −m) ≪ ℓ3η0−1/2, as before. The contribution from s > ℓη0 is ≪ ℓO(1) s>ℓη0 P(|1 − Pois(1)| > s) < ℓ−10.

Turning now to the higher dyadic ranges of t in (17.18), we drop the min condition completely and bound this above by

∞

P ℓ′(β′) = t,|ξt′| > s .

m⩽ℓη0 j⩾1 2jℓ⩽t<2j+1ℓ

s=0

The contribution from s > 2jℓ is bounded by ≪ ℓO(1)

2j

P(|1 − Pois(1)| > s),

j⩾1

s>2jℓ

which is negligible. The contribution from s ⩽ 2jℓ is ≪ ℓO(1)

2jP(2jℓ ⩽ ℓ′(β′) ⩽ 2j+1ℓ),

j⩾1

which is negligible by Lemma 17.2. Putting these estimates together completes the proof of (17.6) in the case i = 4.

Step 5. Note that to obtain µ′5(ℓ) = µ′∗(ℓ) from µ′4(ℓ) we just need to drop the restriction m ⩽ ℓη0 in (17.15). Indeed, this then gives an unrestricted integral

2 π

)1/2 E(log2(x | β′)ℓ − ℓ)+τx|β′(ℓ)cψ(log2 τx|β′(ℓ))dP′(β′),

(

which is equal to R/Z ψ dµ′∗(ℓ) as defined in (17.5) by removing the conditioning on β′. To estimate the difference between R/Z ψ dµ′4(ℓ) and R/Z ψ dµ′5(ℓ), by bounding the ψ term trivially by 1 it is sufficient to bound

E(log2(x | β′)ℓ − ℓ)+τx|β′(ℓ)c dP′(β′). (17.19)

m>ℓη0 min0⩽i⩽ℓ β′(i)=−m

Clearly, we may restrict the integral to those β′ for which log2(x | β′)ℓ ⩾ ℓ for some instance of x. By Lemma 17.1 (3) this implies that β′(ℓ′) ⩾ −O(1 + |ξℓ′′|). From the definition of ℓ′ it follows that

ℓ′ ⩾ ℓ + β′(ℓ′) ⩾ ℓ − O(1 + |ξℓ′′|). (17.20)

We now distinguish two cases: Case 1 (the typical case) is that mini⩽ℓ′−1 β′(i) ⩽ −m/2. Case 2 (the exceptional case) is that mini⩽ℓ′−1 β′(i) > −m/2 (but still mini⩽ℓ β′(i) = −m).

Case 1. For τx|β′(ℓ) we use the bound ≪ R · (ℓ′)κ2−m/2, which follows from Corollary 6.3. Here R is a (minimal) positive integer parameter for which |ξi′| ⩽ Riκ for all i ⩽ ℓ′ − 1, where (as usual) ℓ′ is minimal so that ℓ′ − β′(ℓ′) ⩾ ℓ. Suppose that mini⩽ℓ′−1 ξi′ = −t. Then, since all ξi′ are ⩽ 1, we have β′(ℓ′ − 1) ⩽ ℓ′ − 2 − t. By (17.3), it follows that t ⩽ ℓ − 2, and so we can take R := ℓ. We thus have the bound

τx|β′(ℓ) ≪ ℓℓ′2−m/2. (17.21)

For the (log2(x | β′)ℓ − ℓ)+ term we can use crude bounds. By Lemma 17.1 (3) and the fact that the steps of β′ are bounded above by 1 we have

(log2(x | β′)ℓ − ℓ)+ ≪ ℓ′ + |ξℓ′′|. (17.22) Combining (17.21) and (17.22) (crudely) gives

(log2(x | β′))ℓ − ℓ)+τx|β′(ℓ)c ≪ ℓ2−cm/2((ℓ′)2 + ℓ′|ξℓ′′|) ≪ ℓ2−cm/2((ℓ′)2 + |ξℓ′′|2). It follows that the contribution of Case 1 to (17.19) is bounded by

≪ e−Ω(ℓη0) ℓ′(β′)2 + |ξℓ′′(β′)|2 dP′(β′). (17.23)

We have ℓ′(β′)2 dP′(β′) ≪ ℓ2; to prove this we partition into dyadic ranges according to the value of ℓ′(β′), using the trivial bound ≪ ℓ2 for the range ℓ′ ⩽ 2ℓ, and Lemma 17.2 to show that the contribution from the higher dyadic ranges 2jℓ ⩽ ℓ′ < 2j+1ℓ, j ⩾ 1, is negligible.

For the second term in (17.23), we have |ξℓ′′(β′)|2 dP′(β′) ⩽ ℓ +

sP(ℓ′(β′) = t,|ξt′| > s),

j⩾1 2jℓ⩽t<2j+1ℓ s

where the first term is the contribution from ℓ′(β′) ⩽ 2ℓ, which is bounded above by i⩽2ℓ E|ξi′|2 ≪ ℓ. Consider the contribution to the sum from some fixed j ⩾ 1. The contribution from s > 2jℓ is

sP(|1 − Pois(1)| > s) ≪ 2jℓe−2jℓ.

≪ 2jℓ

s>2jℓ

The contribution from s ⩽ 2jℓ is ≪ (2jℓ)2P(2jℓ ⩽ ℓ′(β′) < 2j+1ℓ) ≪ ℓ323je−2j−4ℓ, by Lemma 17.2. Summed over j, we get a tiny contribution of ≪ e−Ω(ℓ) in both cases.

It follows from this analysis that (17.23) is bounded by ≪ e−Ω(ℓη0), and hence that the contribution of Case 1 to (17.19) is similarly bounded.

Case 2. We remind the reader that this is the case that mini⩽ℓ′−1 β′(i) > −m/2 and mini⩽ℓ β′(i) = −m. This implies that ℓ′ ⩽ ℓ and that ℓi=ℓ′(1 + |ξi′|) > m/2. Therefore either (i) ℓ − ℓ′ ≫

√m, or (ii) there is some i, ℓ′ ⩽ i ⩽ ℓ, with |ξi′| ≫

√m. If (i) holds then, by (17.20), we have |ξℓ′′| ≫

√m, and so in both cases we have maxℓ′⩽i⩽ℓ |ξi′| ≫

√m. Since the sum in (17.19) is restricted to m > ℓη0, this implies maxi⩽ℓ |ξi′| ≫ ℓη0/2.

To bound the contribution of Case 2 to (17.19), we use (17.22), the fact that ℓ′ ⩽ ℓ in Case 2, and the trivial bound τx|β′(ℓ) ⩽ 1, to bound the contribution by

|ξi′| = u ⩽ ℓ

(ℓ + u)P(Pois(1) = u + 1) < ℓ−10.

(ℓ + u)P max

≪

i⩽ℓ

u≫ℓη0/2

u≫ℓη0/2

Thus, the contribution to (17.19) from Case 2 is minuscule.

Cases 1 and 2 together establish (17.6) in the case i = 5, and this completes the proof of Proposition 1.4.

## Appendices

Appendix A. Almost positive random walks

In this appendix we give the proofs of some results in Section 8. The main references for this material are various parts of Feller [18]. We also benefitted from consulting [3, Section 2].

As in the main part of the paper, we consider a random walk β(N) = ξ1 + ··· + ξN and a

complementary random walk β′(N) = ξ1′ + ··· + ξN′ , where ξi =d Pois(1) − 1 and ξi′ =d 1 − Pois(1). Much of the material under discussion here is, however, valid much more generally.

- A.1. Positive random walks. In this subsection n is a dummy variable. The first task is to understand h(m) and h′(m) for m ∈ {−1,0}. Important ingredients in the analysis are the following identities of Sparre Andersen [37] (subsequently generalised by Spitzer [38]). Denote pn := P(min1⩽i⩽n β(i) > 0) and p˜n := P(min1⩽i⩽n β(i) ⩾ 0). Then


∞

∞

zn n

pnzn = exp

P(β(n) > 0) (A.1)

f(z) := 1 +

n=1

n=1

and

∞

∞

zn n

f˜(z) := 1 +

P(β(n) ⩾ 0) . (A.2)

p˜nzn = exp

n=1

n=1

A good source for the proof is [18, XII. 7]. Since the ξi have mean zero it makes sense to work with the following consequences of (A.1) and (A.2):

∞

∞

αnzn and f˜(z)(1 − z)1/2 = exp

α˜nzn , where here

f(z)(1 − z)1/2 = exp

n=1

n=1

1 n

- 1

- 2


1 n

- 1

- 2


P(β(n) ⩾ 0) − Applying a Tauberian theorem [18, XII. 8, Theorem 1a] we obtain

and α˜n :=

P(β(n) > 0) −

αn :=

pn ∼ eα(πn)−1/2 and p˜n ∼ eα˜(πn)−1/2. (A.3) where ∼ means ‘asymptotic to’ and

∞

∞

1 n

1 n

- 1

- 2


- 1

- 2


P(β(n) ⩾ 0) −

and α˜ :=

(A.4)

P(β(n) > 0) −

α :=

n=1

n=1

In particular, from (A.3) we see that h(−1) and h(0) exist and that

h(−1) = eαπ−1/2, h(0) = eα˜π−1/2. (A.5) Similar statements hold for β′ and the associated probabilities p′n,p˜′n. In particular

h′(−1) = eα′π−1/2, h′(0) = eα˜′π−1/2, (A.6) where α′,α˜′ are defined analogously with reference to β′. Observe that

α = −α˜′, α˜ = −α′. (A.7) We now recall a result of Spitzer [39, Theorem 3.4] (see also [18, XVIII.5, Theorem 1]). This

states the following. Let Z+ be the first strict ascending ladder height of β, that is to say β(τ+)

where τ+ := inf{i ⩾ 1 : β(i) > 0} is the first strict ascending ladder epoch of β. (The use of the letter τ here is unrelated to that in Section 6.) Define Z+′ analogously with reference to β′. Define also τ˜+ := inf{i ⩾ 1 : β(i) ⩾ 0} and Z˜+ := β(˜τ+), and similarly for Z˜+′ .

Then Spitzer’s result is that

EZ+ =

1 √2

e−α, EZ˜+′ =

1 √2

eα, EZ+′ =

1 √2

e−α′, EZ˜+ =

1 √2

eα′. (A.8)

Since the steps of β′ are 1−Pois(1) variables bounded above by 1, we have Z+′ = 1 deterministically and therefore

α′ = −12 log 2. (A.9) One may also observe the identity

∞

α˜ − α =

n=1

1 n

P(β(n) = 0) =

∞

nn−1e−n n!

### = 1, (A.10)

n=1

which goes back to Borel [7] and is equivalent to the fact that the Borel distribution with parameter 1 is well-defined.

Relations (A.5) to (A.10) allow for a complete evaluation of all the constants above, and one may easily check that

α = 12 log 2 − 1, α˜ = 12 log 2, α′ = −12 log 2, α˜′ = 1 − 12 log 2 and thus that EZ+ = e/2 and

√

√

h(−1) = (2/π)1/2e−1, h(0) = (2/π)1/2, h′(−1) = 1/

2π, h′(0) = e/

2π. (A.11)

Remarks. Most of the above discussion holds with minor modification for arbitrary random walks with i.i.d. steps with mean zero and variance 1. The identities (A.1) and (A.2) make critical use of the i.i.d. assumption. From (A.9) onwards we made critical use of the fact that β′ is ‘skip-free’, that is to say has increments bounded above by 1. In the general skip-free case the analogue of (A.10) is that the RHS is −log P(ξ′ = 1) (we omit the proof of this fact, which is not needed in the paper).

- A.2. Renewal theorem. In the proof of Proposition 8.1 we will also require some basic renewal theory. In particular we will need Proposition A.2 below, which is a quantitative version of the renewal theorem in a particular setting. The result is essentially due to Gel’fond [23] but we give a self-contained proof (closely related to that of Gel’fond) in our setting.


Consider a random variable X with the following properties:

- (1) X takes values in {1,2,...};
- (2) P(X = 1) > 0;
- (3) We have E(1 + δ0)X < ∞ for some δ0 > 0.


The key example for us will be when X is the strict ascending ladder height Z+ of the walk β, as defined above. With this example, (1) above is obvious. Item (2) is also obvious; P(X = 1) ⩾

- P(ξ1 = 1). Finally, P(X = j) ⩽ P(ξ ⩾ j) which decays faster than exponential, so in this case we have (3) for all δ0.


Write pj = P(X = j) for brevity in what follows. Consider the moment generating function f(z) := EzX; this will be holomorphic in |z| < 1 + δ0.

- Lemma A.1. There is some 0 ⩽ δ1 < δ0 such that the only zero of f(z) − 1 in |z| ⩽ 1 + δ1 is a simple zero at z = 1.


Proof. If |z| < 1 we have |f(z)| < 1 and so there are no zeros of f(z) − 1 with |z| < 1. By a compactness argument it suffices to check that the only zero of f(z) − 1 with |z| = 1 is at z = 1, and that it is simple. Suppose that z = eiθ. Then

pj cos(jθ) ⩽

pj + p1 cosθ = 1 + p1(cosθ − 1).

Ref(z) =

j

j̸=1

Since p1 > 0, this is < 1 unless cosθ = 1, that is to say θ is a multiple of 2π. Thus the only zero of f(z) − 1 on |z| = 1 is at z = 1. We have f′(1) = EX > 0 and so the zero at z = 1 is simple. □

Remark. The use of a compactness argument means that δ1 is ineffective. In the particular case corresponding to the walk β, an effective δ1 could be obtained without undue difficulty if required.

- Proposition A.2. Suppose that X satisfies (1), (2) and (3) above for some δ0. Let δ1 be as in the conclusion of Lemma A.1, and set λ := EX. Then uniformly for integers m > 0 we have


∞

1 λ

+ O (1 + δ1)−m .

P(X1 + ··· + Xr = m) =

r=1

Proof. We have

- 1

- 2πi |z|=1/2


f(z)rz−m−1dz.

P(X1 + ··· + Xr = m) =

Note that for uniformly for |z| = 12 we have |f(z)| ⩽ P(X = 0) + 12P(X > 0) < 1. Summing over r gives

∞

- 1

- 2πi |z|=1/2


f(z) 1 − f(z)

z−m−1dz.

P(X1 + ··· + Xr = m) =

r=1

Now move the contour to |z| = 1 + δ1. In doing this we pick up a contribution of 1/λ from the pole of the integrand at z = 1. There are no other poles by Lemma A.1. It follows that

∞

1 2πi |z|=1+δ1

f(z) 1 − f(z)

1 λ

z−m−1dz.

P(X1 + ··· + Xr = m) =

+

r=1

The result follows since 1−f(fz()z) is uniformly bounded on |z| = 1 + δ1, and |z|−m = (1 + δ1)−m. □

- A.3. Proof of Proposition 8.1 and Lemma 8.4. We are now ready to prove the main statements needed in the paper concerning the existence of h(m),h′(m) and the asymptotic behaviour of these quantities. We mostly consider the (harder) case of h′, indicating how the analysis simplifices in the much simpler case of h as we go along.


We first give a reference for the proof of Proposition 8.1 (3), or more precisely of (8.3), since (8.4) follows immediately from it. This is the statement that

β(i) ⩾ −m , N1/2P min

β′(i) ⩾ −m ≍ m + 1, (A.12)

N1/2P min

1⩽i⩽N

1⩽i⩽N

uniformly for 0 ⩽ m ⩽ √

N. For m = 0 this is immediate from the existence of h(0) and h′(0). For 1 ⩽ m ⩽ √

N, items (i) (upper bound) and (iii) (lower bound) of [32, Lemma 3.3] give the result.

Remark. As noted in [32], the upper bound is due to Kozlov [30, Theorem A, equation (13)]; however the proof in [32] is different and easier. The lower bound is due to Zhang [41, Lemma 1]. Finally we observe that the upper bound in (A.12) (that is, the LHS is ≪ m+1) holds without any restriction on m for trivial reasons.

We now sketch the proof of Lemma 8.4 following [1].

Proof of Lemma 8.4 (sketch). Recall that this is the statement that P(β(N) = x, min1⩽i⩽N β(i) ⩾ 0) ≪ min N−1,(1 + x)N−3/2 . The argument in [1] goes essentially as follows: consider the first, last and middle thirds of the walk up to N, with the last third of the walk reversed. The first third must be nonnegative to time ⌊N/3⌋, an event with probability ≪ N−1/2 by the existence of h(0). The final third (reversed) must be bounded below by −x, an event with probability ≪ min 1,(1 + x)N−1/2 by (A.12). Conditioned on the first and last thirds, the middle third of the walk sums to some fixed value, and the probability of this is ≪ N−1/2 by a result of Kesten (which in our particular case is an easy computation, see (B.5) below). □

Before turning to the proof of items (1) and (2) of Proposition 8.1, we prove the following (standard) auxiliary estimate on strict ascending ladder times.

- Lemma A.3. Let τ+ := inf{i ⩾ 1 : β(i) > 0} be the first strict ascending ladder epoch of β. We have P(τ+ = t) ≪ t−3/2 uniformly in t. An analgous estimate holds for β′.


Proof. We may assume t ⩾ 2. Couple β to a copy of β′ via β(i) = −β′(i). Then τ+ = t is precisely the event that min1⩽i⩽t−1 β′(i) ⩾ 0 and β(t) > 0, the probability of which is

β′(i) ⩾ 0 P(ξt > x).

P β′(t − 1) = x, min

1⩽i⩽t−1

x⩾0

By Lemma 8.4, the first probability is ≪ (1 + x)t−3/2. Since P(ξt > x) ≪ (1 + x)−3, the result follows. □

Proof of Proposition 8.1 (1) and (2). We have already established the cases m = −1,0 in Appendix A.1, so we assume m ⩾ 1 in what follows. We first give the proof for β′ and h′, which is harder. Couple β′ to a copy of β via β = −β′. Let N be a large positive integer (N > m20 will do).

Associated to β are the strict ascending ladder epochs T1,T2,..., defined by Tj = inf{i : β(i) > β(Tj−1)}, and the strict ascending ladder heights Hj := β(Tj). The variable Tj is distributed as τ1 + ··· + τj where the τi are i.i.d. copies of the first strict ascending ladder epoch τ+ and Hj is distributed as X1 + ··· + Xj where the Xi are i.i.d. copies of the first strict ascending ladder height Z+ = β(τ+). Then, foliating according to r, the number of ladder epochs up to time N, we have

m

N

β′(i) ⩾ −m = P max

β(i) ⩽ m =

P(Tr = t,Hr ⩽ m)P(τ+ > N − t). (A.13)

P min

1⩽i⩽N

1⩽i⩽N

r=0

t=0

Here we adopt the convention that T0 = H0 = 0 deterministically. Note also that the number of ladder epochs is bounded above by m.

We assemble various facts. First, by the existence of h′(0) we have for any ℓ ∈ N that

β′(i) ⩾ 0 = (h′(0) + o(1))ℓ−1/2. (A.14) Next note that uniformly for 1 ⩽ r ⩽ m and t ⩾ 1 we have

β(i) ⩽ 0 = P min

P(τ+ > ℓ) = P max 1⩽i⩽ℓ

1⩽i⩽ℓ

P(Tr = t) ⩽ r sup

P(τ+ = x) ≪ r5/2t−3/2 ≪ m5/2t−3/2, (A.15) where here we used Lemma A.3.

x⩾t/r

We first estimate the contribution to (A.13) from t ⩾ √

N. For this we use P(τ+ > N − t) ≪ (N + 1 − t)−1/2 (a consequence of (A.14)) and (A.15), and we ignore the Hr ⩽ m condition. This gives a bound of

≪ m7/2

t−3/2(N + 1 − t)−1/2 ≪ m7/2N−3/4 = o(N1/2).

√

N<t⩽N

In the remaining range t ⩽ √

N in (A.13), we have P(τ+ > N −t) = (h′(0)+o(1))N−1/2 by (A.14). Putting these facts together we obtain

m

P(Tr = t,Hr ⩽ m) + o(N−1/2).

β′(i) ⩾ −m = (h′(0) + o(1))N−1/2

P min

1⩽i⩽N

r=0 t⩽√

N

√

We can add back in the sum over t >

N, at a cost of a further error of o(N−1/2), by further use of (A.15). The sum over t then becomes redundant and we have

m

β′(i) ⩾ −m = (h′(0) + o(1))N−1/2

P(Hr ⩽ m) + o(N−1/2)

P min

1⩽i⩽N

r=0

m

P(X1 + ··· + Xr ⩽ m) + o(N−1/2).

= (h′(0) + o(1))N−1/2 1 +

r=1

By Proposition A.2 it now follows that h′(m) exists and that h′(m) = h′(0)

m EZ+

+ O(1) . (A.16)

By (A.6) to (A.8) we have h′(0)/EZ+ = (2/π)1/2. Together with (A.16), this completes the proof of Proposition 8.1 (1) and (2) in the case of h′.

The analysis of h(m) is much easier. By exactly the same argument with the roles of β,β′ switched, we obtain

β(i) ⩾ −m = (h(0) + o(1))N−1/2 1 +

P min

1⩽i⩽N

m

P(X1′ + ··· + Xr′ ⩽ m) + o(N−1/2).

r=1

Here, Xi′ are i.i.d. copies of Z+′ , the first strict ascending ladder height of β′. However Z+′ = 1 deterministically, and so we obtain h(m) = h(0)(m + 1). By (A.11) we have h(0) = (2/π)1/2 and this completes the proof of Proposition 8.1 (1) and (2) in the case of h. □

- A.4. Local limit theorems. In this subsection we give the proof of Proposition 8.8. The main ingredient of the proof will be (a weakening of) a result of Denisov, Tarasov and Wachtel [11], which we quote as Theorem A.5 below; we will give a self-contained proof of that in Appendix B. The proofs of (8.18) and (8.19) are identical (we will not use the fact that h(m) is exactly (2/π)1/2(m+1) for m ⩾ 0, which does not hold for h′(m)), so we establish only (8.18).


Recall that

β(i) ⩾ 1 = lim

N1/2P min

N1/2P min

h(−1) := lim

β(i) > 0 .

1⩽i⩽N

1⩽i⩽N

N→∞

N→∞

We showed in (A.11) that h˜(−1) exists and

h˜(−1) = eαπ−1/2 = (2/π)1/2e−1, (A.17) with α defined as in (A.4). We need the following auxiliary lemma.

- Lemma A.4. Let m ⩾ 0 be an integer. We have


∞

P min

h(m) − h(m − 1) = h(−1)

q=1

β(i) = −m, β(q) = −m .

1⩽i⩽q

Proof. Let N be some very large positive integer. By summing over the position q of the last visit to −m up to time N we have

N

γ(i) ⩾ 1 (A.18)

P min

P min

β(i) = −m, β(q) = −m · P min

β(i) = −m =

1⩽i⩽q

1⩽i⩽N

1⩽i⩽N−q

q=1

where γ is the shifted walk γ(i) := β(q + i) + m, and the second probability term on the right is absent when q = N. The contribution to the sum from q ⩾ N1/2 is, using (8.14) and the existence of h(−1),

q−3/2(N + 1 − q)−1/2 ≪ (1 + m)N−3/4.

≪ (1 + m)

q>N1/2

By the existence of h(−1) again, uniformly for q ⩽ N1/2 we have P min1⩽i⩽N−q γ(i) ⩾ 1 = (h(−1) + o(1))N−1/2. Thus (A.18) gives

N1/2

β(i) = −m = (h(−1) + o(1))N−1/2

P min

P min

β(i) = −m, β(q) = −m

1⩽i⩽q

1⩽i⩽N

q=1

+ O (1 + m)N−3/4 . Since

β(i) ⩾ −m − P min

β(i) ⩾ −(m − 1) ,

P min

β(i) = −m = P min

1⩽i⩽N

1⩽i⩽N

1⩽i⩽N

multiplying by N1/2 and sending N to infinity gives the result. □

Now we quote the main external input to the proof of Proposition 8.8 (which is essentially the case m = −1 of the result). As previously mentioned, it is a weak version of a result of Denisov, Tarasov and Wachtel [11, Theorem 1].

Theorem A.5. There is a constant ε > 0 such that the following holds. Uniformly for positive integers N,x we have

x √

+ O(N−1−ε). (A.19) Proof. See Appendix B. □ Proof of Proposition 8.8. We prove (8.18); the proof of (8.19) is identical. Theorem A.5 is the case

β(i) > 0 = N−1h(−1)W

P β(N) = x, min

1⩽i⩽N

N

- m = −1, so we assume that m ⩾ 0 in what follows. We may assume N sufficiently large throughout.


Set ε0 := min(2ε, 101 ), where ε is as in Theorem A.5. We remind the reader of the desired statement, which, replacing the dummy variable m by M, is that uniformly for M,x ∈ Z⩾0 we have

x √

β(i) ⩾ −M = N−1h(M)W

+ O (1 + M)O(1)N−1−ε0 .

P β(N) = x, min

1⩽i⩽N

N

We may assume throughout that M ⩽ Nε0, since otherwise the result has no content by choosing a suitably large O(1) exponent. By a telescoping sum argument, it suffices to show

x √

+ O (1 + m)N−1−ε0 (A.20) uniformly for 0 ⩽ m ⩽ Nε0; to see this, sum (A.20) over m = 0,1,2...,M together with (A.19).

β(i) = −m = N−1(h(m) − h(m − 1))W

- P β(N) = x, min 1⩽i⩽N


N

Henceforth we focus on (A.20). If x > N1/2+ε0 then both the LHS and the first term on the RHS

of (A.20) are ≪ N−10; for the LHS this follows by dropping the min1⩽i⩽N β(i) = −m condition and using the large deviation bound Lemma F.3 to bound P(β(N) = x), while for the first term on the RHS we use the bound h(m) − h(m − 1) = O(1), which follows from Proposition 8.1 (2).

Suppose from now on that x ⩽ N1/2+ε0. We foliate the event on the LHS of (A.20) according to the largest value of q, 1 ⩽ q ⩽ N, such that β(q) = −m. Set Q := ⌊N2ε0⌋. The contribution from

- Q < q ⩽ N is, using (8.14), bounded above by


q−3/2(N + 1 − q)−1

P β(N) = x, min

β(i) = −m, β(q) = −m ≪ (1 + m)

1⩽i⩽N

Q<q⩽N

Q<q⩽N

1 Q1/2N

log N N3/2

≪ (1 + m)

.

+

This may be absorbed into the error term in (A.20) due to the choice of Q. The remaining contribution to the LHS of (A.20) may be written as Qq=1 p1(q)p2(q) where

p1(q) := P γ(N − q) = x + m, min

γ(i) > 0 , p2(q) := P min

β(i) = −m, β(q) = −m ,

1⩽i⩽q

1⩽i⩽N−q

and where γ(i) = β(q+i) is the shifted walk, which is a Pois(1)−1 walk independent of (β(i))1⩽i⩽q. Thus to complete the proof of (A.20) our task is to show, assuming x ⩽ N1/2+ε0, that

Q

p1(q)p2(q) = N−1(h(m) − h(m − 1))W

q=1

x √

N

+ O (1 + m)N−1−ε0 . (A.21)

We first dispense with the case x < N1/2−ε0. By Lemma 8.4, p1(q) ≪ (1+x+m)N−3/2 ≪ N−1−ε0, and by (8.10), independent of any assumption on x we have

p2(q) ≪ (1 + m)q−3/2. (A.22) Thus Qq=1 p1(q)p2(q) ≪ (1 + m)N−1−ε0, which is the size of the error term in (A.21). Using Proposition 8.1 (2), the term N−1(h(m) − h(m − 1))W √ xN ) is bounded by ≪ N−1−ε0, which may also be absorbed into the error term in (A.21). Thus (A.21) holds in this regime.

For the remainder of the proof we assume N1/2−ε0 ⩽ x ⩽ N1/2+ε0. We apply Theorem A.5 with x˜ := x + m and N˜ := N − q. This application of Theorem A.5 implies that if 1 ⩽ q ⩽ Q, then

x + m √N − q

+ O(N−1−ε).

p1(q) = (N − q)−1h(−1)W

We have √xN+m−q = √xN +O(Nε0−1/2) and so, since W′ is uniformly bounded, W √ xN+m−q = W √ xN + O(Nε0−1/2). Also (N − q)−1 = N−1 + O(QN−2) = N−1 + O(N2ε0−2). Since ε0 ⩽ 101 , we see that

x √

+ O(N−1−ε). (A.23) Using Lemma A.4, it follows that

p1(q) = N−1h(−1)W

N

∞

∞

x √

p1(q)p2(q) = N−1(h(m) − h(m − 1))W

+ O(N−1−ε)

p2(q),

N

q=1

q=1

and hence that

Q

∞

x √

+ O(N−1−ε)

p1(q)p2(q) = N−1(h(m) − h(m − 1))W

p2(q) + O

p1(q)p2(q) .

N

q=1

q=1

q>Q

- By (A.22) the second term here is ≪ (1 + m)N−1−ε, which may be absorbed into the error term in (A.21). Finally, by Lemma 8.4 (or (A.23)) we have p1(q) ≪ N−1, and from this and (A.22) we


see that q>Q p1(q)p2(q) ≪ (1 + m)N−1Q−1/2, which may again be absorbed into the error term in (A.21) since Q = ⌊N2ε0⌋. □

Appendix B. On results of Denisov, Tarasov and Wachtel

In this appendix we give a more-or-less self-contained proof of Theorem A.5. This result (and in fact a stronger statement) follows essentially immediately from [11, Theorem 1] in the case r = 1, specialised to our situation. However, that reference is rather lengthy and technical (as befits the authors’ aims of great precision and generality) and moreover depends on the earlier paper [13], which has similar properties.

The argument we give here is much shorter and is in part very closely based on [12]. Our need for less precision, as well as the fact that our random walks have specific rather nicely-behaved increments, is what allows for a much more compact treatment.

Throughout this appendix, we work with the walk β with Pois(1) − 1 steps, but we write the argument such that it would also work for β′ with only trivial changes. In particular we never rely on the fact that the steps of β are bounded below by −1.

## B.1. Berry-Esséen Theorem for positive random walks. The main result of this section,

- Proposition B.1, as well as the proof, are exactly that of [12] except we can remove a technical smoothing device (as we have a discrete random variable) and we do not need to carefully track explicit constants. Additionally, we remark on how one could, if desired, replace appeals to some of the literature on general random walks with computations using Stirling’s formula.


Denote

τ := inf{i ⩾ 1 : β(i) ⩽ 0}. (B.1) Observe that, with the notation of the previous appendix, τ = τ˜+′ , and so in particular

|β(τ)| = Z˜+′ . (B.2)

Here is the main result of this subsection. Proposition B.1. Uniformly for integers N ⩾ 1 and x > 0 we have

P β(N) ⩾ x, τ > N = h˜(0)N−1/2e−x2/2N + O(N−1). Before giving the proof, we begin by assembling some preliminaries. Define p(N,x) := P(β(N) = x) = P(Pois(N) = N + x). (B.3)

- Lemma B.2. Uniformly for integers N ⩾ 1 and x, we have


- 1

√

- 2πN


e−x2/2N + O(N−1). (B.4) In particular

p(N,x) =

p(N,x) ≪ N−1/2 (B.5) uniformly. We have

p(N,x) − p(N,x + ℓ) ≪ |ℓ|N−1/2, (B.6) uniformly in ℓ ∈ N. Uniformly for 0 ⩽ k ⩽ N/2 and all x we have

x

p(N − k,x) − p(N,x) ≪ kN−3/2 + N−1. (B.7) Finally, for −N ⩽ x ⩽ N we have

p(N,x) ⩽ e−x2/4N. (B.8)

Proof. (B.4) is an instance of the local limit theorem for which the standard general reference is the book of Petrov [33]. In our specific case we can compute explicitly. In the range |x| ⩽ N2/3 this can be handled by Stirling’s formula in the form m! = (m/e)m(2πm)1/2(1 + O(1/m)) and a

computation. The tails |x| ⩾ N2/3 follow from the large deviation estimate Lemma F.3. (B.5) follows immediately from (B.4).

For (B.6), by telescoping it suffices to handle the case ℓ = 1. We compute that p(N,x + 1) =

p(N,x)N+Nx+1, so in particular p(N,x) is monotonic decreasing for x = 0,1,2,... and also for x = −1,−2,..., with p(N,0) = p(N,−1). By telescoping, the LHS in (B.6) (with ℓ = 1) is simply 2p(N,0) − p(N,−N), and the stated bound follows from (B.4).

The inequality (B.7) follows from (B.4), the inequality supx e−x2/2n − e−x2/2(n−1) ≪ n−1 (for

- n ⩾ 2) and a telescoping sum; for details see [12, Equation (32)]. Finally, the large deviation estimate (B.8) follows from Lemma F.3, where a reference is given. □


Corollary B.3. Let N ⩾ 1 and let x,y be integers with y ⩾ 0. Let k, 0 ⩽ k ⩽ N/2, be an integer. Uniformly in these parameters we have

y2 N

2 π

1/2 y √

ky N3/2

e−x2/2N + O

P β(N − k) ∈ (x,x + y] ∪ (−x,−x + y] =

.

+

N

Proof. The result is trivial when y = 0, so assume y ⩾ 1. Using (B.7) one may reduce to handling the case k = 0. This in turn follows from (B.4) using the mean value estimate e−x2/2N −e(x+i)2/2N ≪ iN−1/2. □

Recall the definition (B.1) of τ.

- Lemma B.4. Uniformly for N ⩾ 1 and y ⩾ 0 we have the bound P β(N) = −y, τ = N ≪ N−3/2(1 + y)−10. (B.9)

In particular

P(τ = N) ≪ N−3/2. (B.10) Proof. (B.10) is an immediate consequence of (B.9). The result is clear when N = 1, so suppose N ⩾ 2. To prove (B.9) we use Lemma 8.4 (and the fact that {τ = N} is contained in the event {min1⩽i⩽N−1 β(i) > 0}), which gives P(β(N − 1) = z, τ = N) ≪ zN−3/2, uniformly for z > 0. This gives

P β(N) = −y, τ = N ≪ N−3/2

z>0

zP(ξ′ = y + z) ≪ N−3/2(1 + y)−10. □

We record one more preliminary lemma. Let x ⩾ 0 and N ⩾ 1 be integers. Denote FN(x) := P(β(N) ⩾ x) − P(β(N) ⩽ −x).

- Lemma B.5. We have the following bounds:


- (1) FN(x) ≪ N−1/2 uniformly;
- (2) |FN(x) − FN−k(x)| ≪ kN−3/2 uniformly for integer k with 0 ⩽ k < N/2.


Proof. (1) follows from the Berry-Esséen theorem. (2) By telescoping it suffices to check this for k = 1. This is done using characteristic functions in [12, Lemma 10]. Both parts could also be done directly using Stirling’s formula. □

We are now ready for the proof of the main result.

Proof of Proposition B.1. Let x > 0. By considering the time k ⩾ 1 at which the walk is first non-positive, we have

N−1

P β(N) ⩾ x, τ > N = P(β(N) ⩾ x) −

k=1

∞

P β(k) = −y, τ = k P(β(N − k) ⩾ x + y).

y=0

(Note that since x > 0, we cannot have τ = N.) Similarly we have 0 = P β(N) ⩽ −x, τ > N) = P(β(N) ⩽ −x)

N−1

∞

P β(k) = −y, τ = k P(β(N − k) ⩽ −x + y) − P β(N) ⩽ −x, τ = N .

−

y=0

k=1

Subtracting the above two expressions and rearranging gives the identity

P β(N) ⩾ x, τ > N = E1 − E2 + E3 − E4, (B.11) where

N−1

E1 = FN(x)P(τ ⩾ N), E2 =

P(τ = k) FN−k(x) − FN(x) ,

k=1

N−1

∞

P(β(k) = −y,τ = k)P β(N − k) ∈ [x,x + y) ∪ (−x,−x + y] ,

E3 =

y=0

k=1

and E4 = P β(N) ⩽ −x, τ = N . We have E1 ≪ N−1 by Lemma B.5 (1) and (B.10). To estimate E2, we split into 1 ⩽ k < N/2 and N/2 ⩽ k ⩽ N − 1. In the first range we use Lemma B.5 (2) and (B.10), obtaining a bound ≪ N−3/2 1⩽k<N/2 k−1/2 ≪ N−1. In the second range we use

- Lemma B.5 (1), (B.10) and the triangle inequality, obtaining a bound ≪ N/2⩽k⩽N−1 k−3/2(N −


k)−1/2 ≪ N−1. Immediately from (B.10) we have the bound E4 ≪ N−3/2. From this discussion and (B.11) we have

P β(N) ⩾ x, τ > N = E3 + O(N−1).

The analysis of E3, which provides the main term in the asymptotic, is the remaining task. We first bound the contribution from N/2 < k ⩽ N − 1. Using (B.5) and (B.9), this contribution is

∞

(N − k)−1/2

(N − k)−1/2k−3/2 ≪ N−1.

yP β(k) = −y, τ = k ≪

≪

N/2<k⩽N−1

N/2<k⩽N−1

y=0

For the remaining terms (with k ⩽ N/2) in E3 we use Corollary B.3. We first bound the contribution of the error terms there. Using (B.9), this is

∞

∞

y2 N

y2 N

ky N3/2 ≪

ky

N3/2 ≪ N−1. Finally we come to the contribution from the main terms in Corollary B.3, which is

(1 + y)−10

k−3/2

P(β(k) = −y,τ = k)

≪

+

+

k⩽N/2

k⩽N/2

y=0

y=0

2 π

∞

1/2 1 √

e−x2/2N

N

k⩽N/2

y=0

yP β(k) = −y, τ = k .

- By (B.9) we can complete the sum over k back out to k = ∞ at a cost of O(N−1). The remaining expression is then


2 π

1/2 1 √

e−x2/2NE|β(τ)|.

N

To conclude the proof of Proposition B.1 we need the fact that (π2)1/2E|β(τ)| = h(−1). This follows from (A.8), (A.17), and (B.2). □

- B.2. Local limit from global. We will now show that Proposition B.1 implies Theorem A.5, the crucial local limit theorem for random walks conditioned to stay positive. Note that Proposition B.1 and the fact that the derivative of f(x) = e−x2/2N is ≪ N−1/2 pointwise already gives the crude bound


P β(N) = x, τ > N) = P β(N) ⩾ x, τ > N) − P β(N) ⩾ x + 1, τ > N) ≪ N−1 (B.12) uniformly in x; we will use this in the arguments.

Proof of Theorem A.5. Set ε := 401 . We may assume N sufficiently large throughout. We first restrict to the case

N1/2−ε ⩽ x ⩽ N1/2+ε. (B.13)

If x > N1/2+ε then Theorem A.5 is essentially immediate from the large deviation estimate Lemma F.3. If x < N1/2−ε then Theorem A.5 follows from Lemma 8.4.

Henceforth, we assume that (B.13) holds. Set L′ := ⌊N1/4⌋ and L := ⌊N3/4⌋ (there is scope for flexibility in these parameters). First observe that

P β(N) = x, τ > N = P β(N) = x, τ > N − L) + O(N−10).

Indeed if τ ∈ (N − L,N] then infi∈(N−L,N] β(i) ⩽ 0 and so if β(N) = x then | Ni=N−L+1 ξi| ⩾ |x| ⩾ N1/2−ε > L3/5, and the probability of this can be seen to be tiny using Lemma F.3.

We have (with p(·,·) defined as in (B.3)) P β(N) = x, τ > N − L) =

P β(N − L) = x − h, τ > N − L p(L,h).

h

We first replace the RHS here with

h

P β(N − L) = x − h, τ > N − L

1 L′

The error involved in doing this is, using (B.6) and (B.12),

p(L,h + h′). (B.14)

h′∈[L′]

L′ NL1/2 ≪ N−9/8.

|p(L,h) − p(L,h + h′)| · sup

P β(n − L) = x′, τ > N − L ≪

≪ sup

x′

h′∈[L′] h

This is an acceptable error and so henceforth we may work with (B.14). Substituting u = h + h′ and retaining the variables u,h′ gives the equivalent expression

1 L′

u

p(L,u)P β(n) ∈ x − u + [L′], τ > N − L .

Now we replace the right-hand probability term by the asymptotic from Proposition B.1. The contribution of the O(N−1) error is

1 L′

≪ N−1 ·

u

1 NL′ ≪ N−5/4,

p(L,u) ≪

which is acceptable. It remains to show that the contribution from the main term is given by the claimed asymptotic in Theorem A.5, that is to say that

h(−1) (n − L)3/2L′

u

p(L,u)

x−u+L′

te−t2/2(n−L) dt = N−1h(−1)W

x−u

x √

N

+ O(N−1−ε). (B.15)

The contribution from |u| ⩽ L3/5 is negligible using (B.8). For |u| ⩽ L3/5 ≈ N9/20, since x ⩾ N1/2−ε we have x − u,x − u + L′ ≍ x. The derivative of te−t2/(N−L) with respect to t in the range [x − u,x − u + L′] is therefore ≪ 1 + |x|2/N ≪ N2ε, and thus

x−u+L′

1 L′

te−t2/(N−L) dt = (x − u)e−(x−u)2/2(N−L) + O(N2εL′).

x−u

When substituted into the LHS of (B.15), the contribution of the error term is ≪ N−3/2+2εL′ ≪ N−9/8. Thus we are left with a main contribution to the LHS of (B.15) of

h(−1) (N − L)3/2

p(L,u)(x − u)e−(x−u)2/2(N−L). (B.16)

|u|⩽L3/5

We replace the first x − u with x. The error in doing this is ≪ N−3/2

p(L,u)u ≪ L3/5N−3/2 ≪ N−1−1/20,

|u|⩽L3/5

which is acceptable. Thus we may replace (B.16) by

h(−1)x (N − L)3/2

p(L,u)e−(x−u)2/2(N−L). (B.17)

|u|⩽L3/5

Now

x2 2

N−L−N1 +Nxu−L−2(Nu−2L) (1 + O(L/N))

N N − L

1

3/2e−(x−u)2/2(N−L) = e−x2/2N e−

= e−x2/2N 1 + O |x|2L N2

+ |x|L3/5 N

L6/5 N

= e−x2/2N 1 + O(N−1/40) .

+

Since |xe−x2/2N| ≪ N1/2, the total contribution of the O(N−1/40) error term to (B.17) is ≪ N−1−1/40, which is acceptable. Thus we may replace (B.17) in turn by

x √

p(L,u) · h(−1)N−1W

.

N

|u|⩽L3/5

To complete the proof, all that remains is to extend the sum back over all u, which can be done at negligible cost by (B.8). □

Appendix C. Fourier estimates

- Lemma C.1. Let R,N be integer parameters with R ⩽ N, and R sufficiently large. Let X be sampled from (N,N +R], with P(X = j) being proportional to 1/j for all j. Consider the characteristic function ϕX(ξ) := EeiξX for ξ ∈ [−π,π]. Then we have the following estimates:


- (1) for |ξ| ⩽ 16/R we have |ϕX(ξ)| ⩽ 1 − cξ2R2 for some absolute c > 0;
- (2) for 16/R ⩽ |ξ| ⩽ π we have |ϕX(ξ)| ⩽ 12.


Proof. (1) The following argument, given by ChatGPT Pro 5.4 (but shortened, rewritten and checked by us) is cleaner than the one we originally wrote. For 1 ⩽ r ⩽ R, write pr := P(X = N+r). Thus pr = (N+1r)L where L := Rr=1 N1+r. We have L ⩽ NR+1, thus pr ⩾ RN(N+1+r) ⩾ 21R, using that r ⩽ R ⩽ N in the second inequality. We have |ϕX(ξ)| = Rr=1 preiξr . Since |ϕX(ξ)| ⩽ 1 we have (after a short calculation)

- 1

- 2


1 − |ϕX(ξ)| ⩾

1 − |ϕX(ξ)|2 = 2

prps sin2

1⩽r<s⩽R

(s − r)ξ 2

R

sin2

= 2

h=1

hξ 2 1⩽r⩽R−h

prpr+h.

### For h ⩽ R/2 we have

R − h 4R2

1 8R

prpr+h ⩾

⩾

. Therefore

1⩽r⩽R−h

⌊R/2⌋

1 4R

hξ 2

1 − |ϕX(ξ)| ⩾

sin2

.

h=1

To bound this below, we use only the terms with h ⩽ πR/16. For these, using the fact that sinx ⩾ π2x for 0 ⩽ x ⩽ π2, we have sin2(hξ/2) ≫ h2|ξ|2. The result follows.

(2) For this we use partial summation, noting that

t

N+R

N+R

dt t2

1 N + R

eiξj .

eiξj +

LϕX(ξ) =

N+1

j=N+1

j=N+1

From this and the geometric series bound | j∈I eiξj| ⩽ π|ξ|−1 (for any interval I) we obtain |ϕX(ξ)| ⩽ π/(NL|ξ|) and so, since L ⩾ R/(N + R) ⩾ R/2N, |ϕX(ξ)| ⩽ 2π/R|ξ|. The result follows. □

Appendix D. Various real-variable inequalities

- Lemma D.1. Let x1,...,xn ⩾ 0 be real. Let ℓ ∈ N. Then n


n

xi ℓ−1.

xi ℓ − ℓ!

xi1 ···xiℓ ⩽ ℓ(ℓ − 1)(max

xi)

i

1⩽i1<···<iℓ⩽n

i=1

i=1

Proof. By expanding out, we have

n

xi ℓ − ℓ!

xi1 ···xiℓ

1⩽i1<···<iℓ⩽n

i=1

is the sum i

1,...,iℓ xi1 ···xiℓ in which there is at least one repeated index. The contribution from (for example) iℓ−1 = iℓ is

n

xi ℓ−1.

⩽ (maxxi)

xi1 ···xiℓ−1 = (maxxi)

i1,...,iℓ−1

i=1

Summing over all possibilities for the position of the repeated indices gives the result. □

- Lemma D.2. Let c ∈ (0,1]. Suppose that x,y ⩾ 1 and M ⩾ 0 are real numbers with y ⩾ x+xc−M. Then y ⩾ x + 12yc − M. Proof. First suppose that x < M; in this case y ⩾ yc ⩾ x + yc − M trivially. Now suppose that x ⩾ M. We have 21/cx ⩾ 2x > x+xc −M. The RHS is non-negative, so we may raise to the power c giving xc ⩾ 21(x + xc − M)c and hence (x + xc − M) − 12(x + xc − M)c ⩾ x − M. The result now follows from the assumption and the fact that y − 12yc is an increasing function of y for y ⩾ 1. □

- Lemma D.3. Let c ∈ (0,1]. Suppose that x,y ⩾ 1 and M ⩾ 0 are real numbers with y ⩽ x−xc+M. Then y ⩽ x − 21yc + 2M.


Proof. Suppose first that x ⩽ M. Then y+ 12yc ⩽ 23y ⩽ 32(x+M) ⩽ x+2M. Alternatively, suppose x ⩾ M. Then

y + 12yc ⩽ (x − xc + M) + 12(x − xc + M)c ⩽ (x − xc + M) + 12(x + M)c ⩽ (x − xc + M) + xc = x + M,

where we used 21/c ⩾ 2 and x ⩾ M in the penultimate step. □ Appendix E. Bounded Lipschitz distance If ψ ∈ C(R/Z) is a function, define

|ψ(x) − ψ(y)| ∥x − y∥R/Z

Lip(ψ) := sup

.

x̸=y

If this supremum is finite, we say that ψ is Lipschitz. In this case we define the Lipschitz norm of ψ by

∥ψ∥Lip := ∥ψ∥∞ + Lip(ψ), where ∥t∥R/Z denotes distance to the nearest integer. This norm is clearly translation-invariant.

Suppose that µ is a Borel measure on R/Z. In our paper µ will always be positive (meaning µ(E) ⩾ 0 for any measurable set E). Given two such measures µ,ν we define

ψ dµ − ψ dν .

dBL[µ;ν] := sup

∥ψ∥Lip⩽1

This is the bounded Lipschitz distance on the space M+(R/Z) of positive Borel measures. That is satisfies symmetry and the triangle inequality is clear. That dBL[µ;ν] = 0 only when µ = ν follows from the fact that the characteristic function 1A of any closed set A ⊂ R/Z may be approximated monotonically by Lipschitz functions fn(x) := max(1 − ndist(x,A),0), so by the monotone convergence theorem we have, if dBL[µ;ν] = 0, that µ(A) = ν(A) for all A.

- Lemma E.1. P(R/Z) is complete with respect to the bounded Lipschitz distance.


Proof. We use the Riesz representation theorem, namely that P(R/Z) may be identified with the positive linear functionals on Λ : C(R/Z) → R with Λ(1) = 1. Suppose that (µn)∞n=1 is a sequence of probability measures which is Cauchy in the bounded Lipschitz distance. By the Riesz theorem and Alaoglu’s theorem that the unit ball of C(R/Z)∗ is sequentially compact, there is some probability measure µ such that f dµn → f dµ along a subsequence of the µn, for all f ∈ C(R/Z). By the Cauchy property it then follows that f dµn → f dµ for all Lipschitz f. We need this convergence to hold uniformly for all f in the unit ball ∥f∥Lip ⩽ 1. This follows from the compactness of the latter in the uniform topology, which is an instance of the Arzelà-Ascoli theorem. □

Now we prove that the space of positive (but not necessarily probability-) measures is complete in the bounded Lipschitz metric. Suppose that (µn)∞n=1 is a Cauchy sequence. The sequence

1dµn = µn(R/Z) is then Cauchy and so tends to some limit ℓ. If ℓ = 0, the result is trivial; we have µn → 0. Set ℓn := µn(R/Z). Consider (after discarding any small values of n for which ℓn = 0) the probability measures µ′n := ℓ1

µn. If ∥f∥Lip ⩽ 1 then

n

1 ℓn −

1 ℓn

1 ℓm

f dµ′n − f dµ′m ⩽

f dµn − f dµm +

f dµm ⩽

1 ℓn

1 ℓn −

1 ℓm

ℓm → 0

dBL[µn;µm] +

as m,n → ∞. Thus the µ′n are a Cauchy sequence and so by Lemma E.1 there is a probability measure µ′ such that dBL[µ′n;µ′] → 0. We claim that dBL[µn;ℓµ′] → 0. This is from the fact that if ∥f∥Lip ⩽ 1 then

f dµn − ℓ f dµ′ ⩽ ℓn f dµ′n − f dµ′ + |ℓn − ℓ| f dµ′ ⩽ ℓndBL[µ′n;µ′] + |ℓn − ℓ| → 0.

This completes the proof. Convolutions. Recall that if f ∈ C(R/Z) and µ is a measure then f ∗ µ(x) := f(x − y)dµ(y).

- Lemma E.2. Let f be a Lipschitz function on R/Z. Then ∥f ∗ (µ − ν)∥∞ ⩽ dBL[µ;ν]∥f∥Lip.

Proof. This is essentially immediate from the definition and the fact that f ∗(µ−ν)(x) = fx dµ− fx dν where fx(y) := f(x − y) has the same Lipschitz norm as f. □

We conclude with the following lemma. Here, ∥µ∥BL := dBL[µ;0].

- Lemma E.3. Suppose that f ∈ C∞(R/Z) and that µ is a positive Borel measure with ∥µ∥BL < ∞. Then f ∗ µ ∈ C∞(R/Z) and


∥f ∗ µ∥Lip ⩽ ∥f∥∞ + ∥f′∥∞ ∥µ∥BL. (E.1) Proof. We have

µ(R/Z) = 1dµ ⩽ ∥µ∥BL < ∞. (E.2) One may check that f ∗ µ is differentiable with derivative (f ∗ µ)′ = f′ ∗ µ by using

f(x − y + h) − f(x − y) − hf′(x − y) dµ(y) ≪ |h|2∥f′′∥∞µ(R/Z). The fact that f ∗ µ ∈ C∞(R/Z) then follows by induction.

For (E.1) we first observe that using (E.2) we have ∥f ∗ µ∥∞ ⩽ ∥f∥∞∥µ∥BL. Furthermore, we have

Lip(f ∗ µ) ⩽ ∥(f ∗ µ)′∥∞ = ∥f′ ∗ µ∥∞ ⩽ ∥f′∥∞∥µ∥BL. Putting these bounds together gives the result. □

Appendix F. Large deviation bounds In this appendix we collect various large deviation bounds of a standard type.

- Lemma F.1. Let X =d Bi(n,p) be a binomial random variable, and let ε ⩽ 32. Then P |X − EX| ⩾ εEX ⩽ 2e−31ε2EX.


Proof. This is [29, (2.9)]. □

- Lemma F.2. Let X1,...,Xn be independent random variables such that |Xi| ⩽ H for all i and some H ∈ (0,∞). Set X := X1 + ··· + Xn. Then for all λ ∈ (0,∞) we have

P |X − EX| ⩾ λ ⩽ 2e−λ2/(2H2n). Proof. This is Hoeffding’s inequality; see for instance [8, Theorem 2.8]. □

Now let β,β′ be random walks with Pois(1) − 1 and 1 − Pois(1) increments respectively.

- Lemma F.3. For n sufficiently large and 0 ⩽ i ⩽ n we have P(β(n) ⩾ i) ≪ e−i2/4n and similarly for β′.


Proof. This is a very standard type of large deviation bound. The second estimate in [4, Theorem A.1.15] gives that

P(β(n) ⩾ i) ⩽ e−nϕ(i/n) (F.1) where ϕ(x) := (1 + x)log(1 + x) − x. The particular statement given here then follows using ϕ(x) ⩾ x2/4, valid for x ∈ (0,1).

For β′ we have a similar statement to (F.1) but with ϕ˜(x) := x2/2, so in this case the result follows straight away. □ Corollary F.4. With probability ⩾ 1 − N−10, |β(j2) − β(j1)| ⩽ N1/2−η whenever j1,j2 ∈ [N/8,N] and |j2 − j1| ⩽ N1−5η/2, and similarly for β′. Proof. Without loss of generality, j2 > j1. By Lemma F.3 applied with n = j2 − j1, for each fixed j1,j2 we have

P |β(j2) − β(j1)| ⩾ N1/2−η ≪ e−Nη/2/4 ≪ N−20. Summing over the O(N2) choices of j1,j2 gives the result. □

The following slight variant of the large deviation bound was required in the proof of Lemma 8.15. Lemma F.5. We have P(β(n) = i) ⩽ e−i/10 uniformly for i > n/2, and similarly for β′.

Proof. We can again use P(β(n) ⩾ i) ⩽ e−nϕ(i/n), but now use the inequality ϕ(x) ⩾ x/6, valid for x ⩾ 1/2. The inequality holds by a massive margin. A similar proof works for β′. □

References

- [1] Louigi Addario-Berry and Bruce Reed, Ballot theorems for random walks with finite variance, https://problab. ca/louigi/papers/ballot.pdf. 33, 102, 103
- [2] Louigi Addario-Berry and Bruce Reed, Ballot theorems, old and new, Horizons of combinatorics, Bolyai Soc. Math. Stud., vol. 17, Springer, Berlin, 2008, pp. 9–35. 33
- [3] Elie Aidekon and Zhan Shi, The Seneta-Heyde scaling for the branching random walk, Ann. Probab. 42 (2014), 959–993. 100
- [4] Noga Alon and Joel Spencer, The probabilistic method, third ed., Wiley-Interscience Series in Discrete Mathematics and Optimization, John Wiley & Sons, Inc., Hoboken, NJ, 2008, With an appendix on the life and work of Paul Erdős. 95, 114
- [5] Richard Arratia and Simon Tavaré, The cycle structure of random permutations, Ann. Probab. 20 (1992), 1567–

1591. 7

- [6] Michel Balazard, Jean-Louis Nicolas, Carl Pomerance, and Gérald Tenenbaum, Grandes déviations pour certaines fonctions arithmétiques, J. Number Theory 40 (1992), 146–164. 3
- [7] Émile Borel, Sur l’emploi du théorème de Bernoulli pour faciliter le calcul d’un infinité de coefficients. application au problème de l’attente à un guichet, Comptes Rendus de l’Académie des Sciences 214 (1942), 452–456. 101
- [8] Stéphane Boucheron, Gábor Lugosi, and Pascal Massart, Concentration inequalities: A nonasymptotic theory of independence, Oxford University Press, 2013. 114
- [9] Richard Brent, Carl Pomerance, David Purdum, and Jonathan Webster, Algorithms for the multiplication table problem, Integers 21 (2021), Paper No. A92, 19. 3
- [10] Francesco Caravenna, A local limit theorem for random walks conditioned to stay positive, Probab. Theory Related Fields 133 (2005), 508–530. 35
- [11] Denis Denisov, Alexander Tarasov, and Vitali Wachtel, Asymptotic expansions for normal deviations of random walks conditioned to stay positive, arXiv:2412.09145. 10, 16, 35, 104, 105, 107
- [12] Denis Denisov, Alexander Tarasov, and Vitali Wachtel, Berry-Esseén inequality for random walks conditioned to stay positive, arXiv:2412.08502. 107, 108
- [13] Denis Denisov, Alexander Tarasov, and Vitali Wachtel, Expansions for random walks conditioned to stay positive, arXiv:2401.09929. 35, 107
- [14] Persi Diaconis, Jason Fulman, and Robert Guralnick, On fixed points of permutations, J. Algebraic Combin. 28

(2008), 189–218. 2

- [15] Sean Eberhard, Kevin Ford, and Ben Green, Permutations fixing a k-set, Int. Math. Res. Not. IMRN (2016), 6713–6731. 2, 3, 7, 79
- [16] Paul Erdős, Some remarks on number theory (Hebrew with English summary), https://users.renyi.hu/~p_ erdos/1955-13.pdf. 2
- [17] Paul Erdős, An asymptotic inequality in the theory of numbers (Russian), Vestnik Leningrad. Univ. 15 (1960), 41–49. 2, 7
- [18] William Feller, An introduction to probability theory and its applications. Vol. II, second ed., John Wiley & Sons, Inc., New York-London-Sydney, 1971. 100


- [19] Philippe Flajolet and Robert Sedgewick, Analytic combinatorics, Cambridge University Press, Cambridge, 2009. 3
- [20] Kevin Ford, The distribution of integers with a divisor in a given interval, Ann. of Math. (2) 168 (2008), 367–433. 3, 8, 9, 86
- [21] Kevin Ford, Sharp probability estimates for random walks with barriers, Probab. Theory Related Fields 145

(2009), 269–283. 34

- [22] Kevin Ford, Ben Green, and Dimitris Koukoulopoulos, Equal sums in random sets and the concentration of divisors, Invent. Math. 232 (2023), 1027–1160. 44
- [23] Aleksandr Osipovich Gel’fond, An estimate for the remainder term in a limit theorem for recurrent events, Theory of Probability & Its Applications 9 (1964), 299–303. 101
- [24] Loukas Grafakos, Classical Fourier analysis, second ed., Graduate Texts in Mathematics, vol. 249, Springer, New York, 2008. 45
- [25] Ion Grama and Hui Xiao, Local limit theorems for conditioned random walks by the heat kernel approximation, https://arxiv.org/abs/2509.14009. 35
- [26] Andrew Granville, Alisa Sedunova, and Cihan Sabuncu, The multiplication table constant and sums of two squares, Acta Arith. 214 (2024), 499–522. 3, 5
- [27] Ben Green and Mehtaab Sawhney, The multiplication table problem, forthcoming. 2
- [28] G. H. Hardy, Ramanujan. Twelve lectures on subjects suggested by his life and work, Cambridge University Press, Cambridge; The Macmillan Company, New York, 1940. 3
- [29] Svante Janson, Tomasz Łuczak, and Andrzej Rucinski, Random graphs, Wiley-Interscience Series in Discrete Mathematics and Optimization, Wiley-Interscience, New York, 2000. 114
- [30] M. V. Kozlov, The asymptotic behavior of the probability of non-extinction of critical branching processes in a random environment, Teor. Verojatnost. i Primenen. 21 (1976), 813–825, (English translation in Theory of Probability and Its Applications 21 (1976), 791–804.). 102
- [31] Tomasz Łuczak and László Pyber, On random generation of the symmetric group, Combin. Probab. Comput. 2

(1993), 505–512. 2

- [32] Robin Pemantle and Yuval Peres, Critical random walk in random environment on trees, Ann. Probab. 23 (1995), 105–140. 102
- [33] Valentin Vladimirovich Petrov, Sums of independent random variables, Ergebnisse der Mathematik und ihrer Grenzgebiete [Results in Mathematics and Related Areas], vol. Band 82, Springer-Verlag, New York-Heidelberg, 1975, Translated from the Russian by A. A. Brown. 107
- [34] Grant Ritter, Growth of random walks conditioned to stay positive, Ann. Probab. 9 (1981), 699–704. 38
- [35] Jeremy Schlitt, Multiplication tables for integers with restricted prime factors, https://arxiv.org/abs/2603.

19212. 11

- [36] K. Soundararajan, Ramanujan and the anatomy of integers, in Srinivasa Ramanujan: Going Strong at 125, Part II, Notices AMS 60 (2013), no. 1, 10–22. 3
- [37] Erik Sparre Andersen, On the fluctuations of sums of random variables. II, Math. Scand. 2 (1954), 195–223. 100
- [38] Frank Spitzer, A combinatorial lemma and its application to probability theory, Trans. Amer. Math. Soc. 82

(1956), 323–339. 100

- [39] Frank Spitzer, A Tauberian theorem and its probability interpretation, Trans. Amer. Math. Soc. 94 (1960), 150–169. 100
- [40] Vladimir Vatutin and Vitaly Wachtel, Local probabilities for random walks conditioned to stay positive, Probability Theory and Related Fields 143 (2009), 177–217. 33
- [41] Yu Zhang, A power law for connectedness of some random graphs at the critical point, Random Structures Algorithms 2 (1991), 101–119. 102


Mathematical Institute, Andrew Wiles Building, Radcliffe Observatory Quarter, Woodstock

Rd, Oxford OX2 6QW, UK Email address: ben.green@maths.ox.ac.uk Department of Mathematics, Columbia University and OpenAI Email address: m.sawhney@columbia.edu

