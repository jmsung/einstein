---
type: source
kind: paper
title: "Tiling by translates of a function: results and open problems"
authors: Mihail N. Kolountzakis, Nir Lev
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2009.09410v2
source_local: ../raw/2020-kolountzakis-tiling-translates-function-results.pdf
topic: general-knowledge
cites:
---

## arXiv:2009.09410v2[math.CA]13Sep2021

DISCRETE ANALYSIS, 2021:12, 24 pp. www.discreteanalysisjournal.com

# Tiling by translates of a function: results and open problems

##### Mihail N. Kolountzakis* Nir Lev†

Received 22 September 2020; Published 13 September 2021

Abstract: We say that a function f ∈ L1(R) tiles at level w by a discrete translation set Λ ⊂ R, if we have ∑λ∈Λ f(x−λ) = w a.e. In this paper we survey the main results, and prove several new ones, on the structure of tilings of R by translates of a function. The phenomena discussed include tilings of bounded and of unbounded density, uniform distribution of the translates, periodic and non-periodic tilings, and tilings at level zero. Fourier analysis plays an important role in the proofs. Some open problems are also given.

Key words and phrases: Tiling, translates, spectral gap, uncertainty principle, quasicrystals.

#### 1 Introduction

Let f be a function in L1(R) and let Λ ⊂ R be a discrete set. We say that f tiles R at level w with the translation set Λ, or that f +Λ is a tiling of R at level w (where w is a constant), if we have

∑

f(x−λ) = w a.e. (1.1)

λ∈Λ

and the series in (1.1) converges absolutely a.e.

In the same way one can deﬁne tiling by translates of an L1 function on Rd, or more generally, on any locally compact abelian group. The ﬁnite abelian groups, and in particular the cyclic ones, are an important class being often considered.

*Supported by the Hellenic Foundation for Research and Innovation, Project HFRI-FM17-1733 and by Grant No. 4725 of the University of Crete.

†Supported by ISF Grant No. 227/17 and ERC Starting Grant No. 713927.

© 2021 Mihail N. Kolountzakis and Nir Lev cb Licensed under a Creative Commons Attribution License (CC-BY) DOI: 10.19086/da.28122

If f = 1Ω is the indicator function of a set Ω, and f +Λ is a tiling at level one, then this means that the translated copies Ω+λ, λ ∈ Λ, ﬁll the whole space without overlaps up to measure zero. To the contrary, for tilings by a general real or complex-valued function f, the translated copies may have overlapping supports and a wider variety of phenomena may (and do) occur.

In dimension one, translational tilings exhibit a stronger structure than in higher dimensions, and there are interesting questions as to how rigid this structure must be, e.g. how close the translation set Λ is to being periodic, or to being constructed out of periodic sets, or, at an even more basic level, to being uniformly distributed in R.

The subject has been studied by several authors, see, in particular, [LM91], [KL96], [Kol04], [KL16], [Liu18], [Lev20]. The aim of this paper is to survey the results obtained in earlier works, as well as to prove several new results. At the end of the paper, some open problems are also given.

In this section we survey the main results on the structure of tilings by translates of a function on R, and we state the new results that will be proved in this paper.

- 1.1 Tiling and density We say that a set Λ ⊂ R has bounded density if

sup

x∈R

#(Λ∩[x,x+1)) < +∞. (1.2)

The set Λ is said to be uniformly distributed if there is a number D(Λ) satisfying

#(Λ∩[x,x+r)) = D(Λ)·r+o(r), r → +∞ (1.3) uniformly with respect to x ∈ R. In this case, D(Λ) is called the uniform density of Λ.

The following result establishes a connection between tiling and density:

- Theorem 1.1 ([KL96]). Let f +Λ be a tiling at some nonzero level w, where f ∈ L1(R) and where Λ ⊂ R is a set of bounded density. Then f has nonzero integral, and Λ has a uniform density given by D(Λ) = w·( f)−1.

This was proved in [KL96, Lemma 2.3] for a weaker notion of density1, but a minor adjustment to the proof in fact yields the stronger statement above for the uniform density. A similar result is true also in Rd.

1.2 Tiling at level zero

It is not known whether Theorem 1.1 has an analog for tilings of bounded density at level zero. It was conjectured in [KL96, p. 660] that if f +Λ is such a tiling, then f must have zero integral. In [KL96,

- Lemma 2.4] this was proved under the extra assumption that f has compact support. Here we will prove that the conclusion is true in the general case:


- Theorem 1.2. Let f +Λ be a tiling at level zero, where f ∈ L1(R) and where Λ ⊂ R is a nonempty set of bounded density. Then f must have zero integral.




1In [KL96] the density d(Λ) of a set Λ ⊂ R is deﬁned by d(Λ) := limr→+∞#(Λ∩(−r,r))/(2r).

Do there exist tilings f +Λ at level zero such that the set Λ has density zero? Theorem 1.1 does not exclude such a possibility. In fact, in dimensions two and higher it is easy to exhibit tilings of this kind. For instance, in R2 one may take f(x,y) = ϕ(x)ψ(y), Λ = Γ×{0}, where ϕ,ψ ∈ L1(R) and ϕ +Γ is a tiling of R at level zero.

We will show, however, that this is not the case in dimension one. To state the result, we recall that a set Λ ⊂ R is said to be relatively dense if there is r > 0 such that any interval [x,x+r) contains at least one point from Λ. We will prove the following:

- Theorem 1.3. Let f +Λ be a tiling at level zero, where f ∈ L1(R) is nonzero and Λ ⊂ R is a nonempty set of bounded density. Then Λ must be a relatively dense set.

In particular this implies that Λ cannot have density zero. Does it follow from the assumptions in Theorem 1.3 that Λ has a uniform (positive) density D(Λ)?

The answer to this question is not known. The problem is nontrivial due to the existence of translation sets Λ that admit only tilings at level zero, so that Theorem 1.1 does not apply to these sets:

- Theorem 1.4 ([Lev20]). There exists a nonempty set Λ ⊂ R of bounded density which admits tilings f +Λ with nonzero f ∈ L1(R), but any such a tiling is necessarily a tiling at level zero.

1.3 Periodic tilings

We say that a set Λ ⊂ R has a periodic structure if it can be represented as a disjoint union of ﬁnitely many arithmetic progressions, namely

Λ =

N

j=1

(ajZ+bj) (1.4)

where aj,bj are real numbers and aj > 0. The sets Λ with this structure constitute the basic examples of translation sets for tilings of R. Indeed, one can check that if

f = 1[0,a1] ∗1[0,a2] ∗···∗1[0,aN] (1.5) and Λ is given by (1.4), then f +Λ is a tiling at some positive level w.

The last example shows that any set Λ of the form (1.4) admits a tiling by a compactly supported function f ∈ L1(R). A result ﬁrst proved in [LM91] and rediscovered in [KL96] asserts that there are no other translation sets Λ with this property:

- Theorem 1.5 ([LM91], [KL96]). Let f ∈ L1(R) be nonzero and have compact support. If f tiles at some level w with a translation set Λ of bounded density, then Λ has a periodic structure, namely, it must be of the form (1.4).


The proof of this result is based on Cohen’s characterization of idempotent measures in locally compact abelian groups. The group on which Cohen’s theorem is used in the proof is the Bohr compactiﬁcation of the real line (see also [Mey70, p. 25]).

A discrete set Λ ⊂ R is said to have ﬁnite local complexity if Λ can be enumerated as a sequence {λn}, n ∈ Z, such that λn < λn+1 and the successive differences λn+1 −λn take only ﬁnitely many different values. The following result establishes that tilings of ﬁnite local complexity must be periodic, even if f does not have compact support:

- Theorem 1.6 ([IK13], [KL16]). Let Λ ⊂ R have ﬁnite local complexity. If f ∈ L1(R) is nonzero and f +Λ is a tiling at some level w, then Λ must be a periodic set, namely, it has the form Λ = aZ+{b1,...,bN}.

1.4 Non-periodic tilings

The papers [LM91], [KL96] leave the following question open: Does there exist any set Λ ⊂ R not of periodic structure, which can tile with some function f ∈ L1(R) of unbounded support? Such a set Λ cannot have ﬁnite local complexity by Theorem 1.6. We settled this question afﬁrmatively in [KL16]:

- Theorem 1.7 ([KL16]). There exists a tiling f +Λ at level one, where f ∈ L1(R) and Λ ⊂ R has bounded density, but such that Λ has no periodic structure, i.e. the set Λ is not of the form (1.4).

The proof was based on the implicit function method due to Kargaev [Kar82], and it yields a set Λ which is a small perturbation of the integers. The proof moreover allows to choose the function f in the Schwartz class. However it yields a function f satisfying supp(f) = R, where supp(f) is the closed support of f (the smallest closed set such that f vanishes a.e. on its complement).

In this paper we will prove a stronger version of Theorem 1.7, which establishes the existence of non-periodic tilings f +Λ of bounded density, such that f has “sparse” support. Precisely, we will show that the support (which must be unbounded, due to Theorem 1.5) can be localized inside any given set Ω ⊂ R which contains arbitrarily long intervals:

- Theorem 1.8. There is a discrete set Λ ⊂ R of bounded density, but which is not of the form (1.4), with the following property: given any scalar w, and any set Ω ⊂ R which contains arbitrarily long intervals, one can ﬁnd a nonzero f ∈ L1(R), supp(f) ⊂ Ω, such that f +Λ is a tiling at level w.


We note that the set Ω in this theorem may be chosen very sparse, for example, one may take Ω = ∞j=1[τj,τj + j], where the numbers τj grow arbitrarily fast.

Theorem 1.8 implies in particular the existence of non-periodic tilings by a function f such that supp(f) ⊂ [0,+∞), i.e. the support is bounded from below (while it cannot be bounded from both above and below, due to Theorem 1.5).

The proof of Theorem 1.8 relies on a recent result due to Kurasov and Sarnak [KS20], who constructed a new type of crystalline measures on R. These are pure point measures with discrete closed support, whose Fourier transform is a measure of the same type.

###### 1.5 Tilings of unbounded density

It seems that very little attention has been paid to tilings which are not of bounded density. In fact, we are not aware of any example of such a tiling in the literature. In [KL96, Example 7.1] some examples are given in a more general context, where the points of the translation set Λ are endowed with nonnegative integer multiplicities (so that Λ is actually not a set, but a multi-set).

We will prove that there exist tilings of unbounded density in the proper sense. Let us say that a set Λ ⊂ R has tempered growth if there is N such that

#(Λ∩(−r,r)) = O(rN), r → +∞. (1.6)

- Theorem 1.9. There is a set Λ ⊂ R which is not of bounded density but has tempered growth, with the following property: given any scalar w one can ﬁnd a nonzero function f in the Schwartz class, such that f +Λ is a tiling at level w.

Moreover, in our example the set Λ is contained in a small neighborhood of the integers. The construction is done using a variant of Kargaev’s implicit function method.

It follows from [KL96, Lemma 2.1] that the function f in Theorem 1.9 must change sign, i.e. f cannot be chosen nonnegative. This indicates that cancellations are playing a decisive role in the tiling. We can even prove a stronger claim:

- Theorem 1.10. Let f +Λ be a tiling at some level w, where the set Λ ⊂ R is not of bounded density but has tempered growth, and where f is a function in the Schwartz class. Then f must have zero integral.


It may seem counter-intuitive at ﬁrst glance that one can tile R at a nonzero level w by translates of a Schwartz function f whose integral is zero.

- 1.6 Organization of the paper The rest of the paper is organized as follows.


- In Section 2 some preliminary background is given, and Fourier analytic conditions for tiling are

discussed.

- In Section 3 we prove that if f +Λ is a tiling at level zero, where f ∈ L1(R) is a nonzero function and

Λ ⊂ R is a nonempty set of bounded density, then f has zero integral (Theorem 1.2) and Λ is relatively dense (Theorem 1.3).

- In Section 4 we establish the existence of non-periodic tilings f +Λ of bounded density, such that the

function f has “sparse” support (Theorem 1.8).

- In Section 5 we construct tilings f +Λ of unbounded density, such that Λ has tempered growth and f


is in the Schwartz class (Theorem 1.9). We also show that in any such a tiling, the function f must have zero integral (Theorem 1.10).

In the last section, Section 6, we pose some open problems.

#### 2 Preliminaries. Fourier analytic conditions for tiling.

It is well-known that in the study of translational tilings, Fourier analysis plays an important role, see e.g. [Kol04]. If f ∈ L1(R) then its Fourier transform is deﬁned by

f(t) =

f(x)e−2πitxdx. (2.1)

R

If α is a tempered distribution on R, then α(ϕ) denotes the action of α on a Schwartz function ϕ. The Fourier transform α is deﬁned by α(ϕ) = α( ϕ).

If α is a tempered distribution on R, and if ϕ is a Schwartz function, then the convolution α ∗ϕ is a tempered distribution whose Fourier transform is α · ϕ.

We use supp(α) to denote the closed support of a tempered distribution α.

If f ∈ L1(R) then supp(f) is the smallest closed set such that f vanishes a.e. on its complement. This set coincides with the support of f in the distributional sense.

For more details on distribution theory we refer the reader to [Rud91].

- 2.1 Necessary conditions for tiling For a discrete set Λ ⊂ R we deﬁne the measure

δΛ := ∑

λ∈Λ

δλ. (2.2)

The tiling condition (1.1) can then be restated as

f ∗δΛ = w a.e. (2.3)

If Λ has bounded density then the measure δΛ is a tempered distribution on R. So, at least formally, taking the Fourier transform of both sides of (2.3) yields

f · δΛ = w·δ0. (2.4) If f is a Schwartz function, then condition (2.4) makes sense and it is equivalent to (2.3). To the

contrary, for an arbitrary function f ∈ L1(R) (not assumed to be in the Schwartz class) the product f · δΛ is not well-deﬁned, and the condition (2.4) can only be interpreted as a heuristic principle.

The following result, inspired by the heuristic condition (2.4), provides a necessary condition for tiling which holds for any f ∈ L1(R).

- Theorem 2.1 ([KL16]). Let f ∈ L1(R), and Λ ⊂ R be a discrete set of bounded density. If f +Λ is a tiling at some level w, then

supp( δΛ)\{0} ⊂ { f = 0}. (2.5)

The proof of this result is based on Wiener’s tauberian theorem. In the earlier works [KL96], [Kol00a], [Kol00b] the result was proved under various extra assumptions.

2.2 Sufﬁcient conditions for tiling

One may ask whether Theorem 2.1 admits a converse, i.e. if the condition (2.5) implies that f +Λ is a tiling at some level w. If the distribution δΛ happens to be a measure on R, then the product f · δΛ is a well-deﬁned measure and the condition (2.4) makes sense. In this case, the two conditions (2.4) and (2.5) are equivalent, and can be shown to imply that f +Λ is a tiling:

- Theorem 2.2. Let Λ ⊂ R have bounded density and suppose that δΛ is a locally ﬁnite measure. If f ∈ L1(R) satisﬁes (2.5) then f +Λ is a tiling at level w = δΛ({0})· f.




A proof of this result is given below. In [KL96] the result was proved under the extra assumption that f is a smooth function.

As an example, Theorem 2.2 applies if the set Λ has a periodic structure, i.e. if it has the form (1.4).

In this case δΛ is a (pure point) measure by Poisson’s summation formula, and the condition (2.5) is both necessary and sufﬁcient for a function f ∈ L1(R) to tile at some level w with the translation set Λ.

Theorem 2.2 leaves open, though, the question as to whether the condition (2.5) is sufﬁcient for tiling in the general case, i.e. for an arbitrary set Λ ⊂ R of bounded density. This question was addressed recently in [Lev20] where it was answered in the negative:

- Theorem 2.3 ([Lev20]). There is a set Λ ⊂ R of bounded density and a function f ∈ L1(R), such that (2.5) is satisﬁed however f +Λ is not a tiling at any level.

The proof of this result is based on the relation of the problem to Malliavin’s non-spectral synthesis example.

Theorem 2.3 implies that a converse to Theorem 2.1 can only be valid under certain extra assumptions. One example of such a converse is given by Theorem 2.2. Another example is the following result:

- Theorem 2.4. Let f ∈ L1(R), and let Λ ⊂ R be a discrete set of bounded density. If the set supp( δΛ)\{0} is closed and is disjoint from supp( f), then f +Λ is a tiling at some level w.

We will not use this result in the paper and we do not include its proof. For other results of similar type see [Kol00a, Theorem 3], [Kol00b, Theorem 5].

2.3 Translation-bounded measures

A measure µ on R satisfying the condition

sup

x∈R

|µ|([x,x+1)) < ∞ (2.6)

is said to be translation-bounded. If a measure µ is translation-bounded, then it is a tempered distribution. If µ is a translation-bounded measure on R, and if ν is a ﬁnite measure on R, then the convolution µ ∗ν is a translation-bounded measure.

- Theorem 2.5. Let µ be a translation-bounded measure on R, and suppose that µ is a locally ﬁnite measure. If ν is a ﬁnite measure on R, then the Fourier transform of the convolution µ ∗ν is the measure µ · ν.


In particular, let Λ ⊂ R be a discrete set of bounded density, and let f ∈ L1(R). Then the measure δΛ is translation-bounded, and the convolution f ∗δΛ is the sum of the series ∑λ∈Λ f(x−λ) which converges absolutely a.e., see [KL96, Lemma 2.2]. If the distribution δΛ is assumed to be a locally ﬁnite measure, then using Theorem 2.5 we obtain that the three conditions (2.3), (2.4) and (2.5) are equivalent. We thus see that Theorem 2.2 is a consequence of Theorem 2.5.

Theorem 2.5 should be known to experts but we could not ﬁnd a proof in the literature, so we include one below for completeness.

Proof of Theorem 2.5. We will use σ to denote the measure µ. The assertion of the theorem means that if ψ is a Schwartz function with compact support then

ψ(x)d(µ ∗ν)(x) =

R

ψ(t) ν(t)dσ(t). (2.7)

R

Let χ be a Schwartz function whose Fourier transform χ is non-negative, has compact support,

χ(t)dt = 1, and for each ε > 0 let χε(x) := χ(εx). Let hε := (ψ · ν) ∗ χε, then hε is an inﬁnitely smooth function with compact support. As ε → 0, the function hε remains supported on a certain interval I = [a,b] that does not depend on ε, and hε converges to ψ · ν uniformly on I. Hence

µ(hε) = lim

hε(t)dσ(t) =

ψ(t) ν(t)dσ(t). (2.8)

lim

ε→0

ε→0 R

R

The function ψ is the Fourier transform of some function ϕ in the Schwartz class. Let gε :=(ϕ∗ν)·χε, then gε is a smooth function in L1(R) and we have gε = hε. Since hε belongs to the Schwartz space, the same is true for gε, and it follows that

µ(hε) = µ( hε) =

gε(−x)dµ(x) =

R

(ϕ ∗ν)(−x)χε(−x)dµ(x). (2.9)

R

We observe that |χε(−x)| 1 and χε(−x) → 1 pointwise as ε → 0. We now wish to apply the dominated convergence theorem to (2.9). Using Fubini’s theorem we obtain

(|ϕ|∗|ν|)(−x)|dµ|(x) =

R

|ϕ(−x)|d(|µ|∗|ν|)(x). (2.10)

R

The function ϕ has fast decay being in the Schwartz class, while |µ|∗|ν| is a translation-bounded measure, hence the integral in (2.10) converges. We may therefore apply to (2.9) the dominated convergence theorem, which yields

µ(hε) =

(ϕ ∗ν)(−x)dµ(x) =

ϕ(−x)d(µ ∗ν)(x). (2.11)

lim

ε→0

R

R

But ϕ(−x) = ψ(x), so we see that (2.7) follows from (2.8) and (2.11) as needed.

| |
|---|


#### 3 Tiling at level zero

In this section we prove that if f +Λ is a tiling at level zero, where f ∈ L1(R) is nonzero and Λ ⊂ R is nonempty and has bounded density, then f has zero integral (Theorem 1.2) and Λ is a relatively dense set (Theorem 1.3).

###### 3.1 The function f has zero integral

We begin with Theorem 1.2, for which we give two proofs. The ﬁrst proof is Fourier analytic, and is based on the following result:

- Theorem 3.1 ([KL16]). Let f ∈ L1(R) have nonzero integral. If Λ ⊂ R is a set of bounded density and


- f +Λ is a tiling at some level w, then there is a > 0 such that δΛ = c·δ0 in (−a,a), where c = w·( f)−1.

This result follows from the proof of [KL16, Theorem 4.1] and it is stated in that paper as a remark on p. 4598. The proof of Theorem 3.1 is based on Wiener’s tauberian theorem.

First proof of Theorem 1.2. Let f +Λ be a tiling at level w = 0, and suppose to the contrary that f has nonzero integral. Then by Theorem 3.1 there is a > 0 such that δΛ = c·δ0 in (−a,a), where c = w·( f)−1. Since w = 0 this means that δΛ vanishes in a neighborhood (−a,a) of the origin. We will show that this cannot happen.

Indeed, choose a Schwartz function ϕ such that supp(ϕ) ⊂ (−a,a) and ϕ > 0. Then we have δΛ(ϕ) = 0 since δΛ vanishes in a neighborhood of supp(ϕ). On the other hand,

δΛ(ϕ)=δΛ( ϕ)= ∑

λ∈Λ

ϕ(λ) > 0,

since Λ is nonempty and ϕ is everywhere positive. We thus arrive at a contradiction. As a remark, we record here the following observation:

| |
|---|


Lemma 3.2. Let Λ ⊂ R be a nonempty set of bounded density, and suppose that there is a > 0 such that δΛ = c·δ0 in (−a,a). Then c > 0, and Λ has a uniform density given by D(Λ) = c.

Proof. Let ϕ be a Schwartz function such that ϕ > 0, ϕ = 1 and supp( ϕ) ⊂ (−a,a). Then we have ϕ · δΛ = c·δ0 and hence ϕ +Λ is a tiling at level c. Since ϕ is a positive function and Λ is nonempty, the tiling level c must also be positive. Finally, we obtain from Theorem 1.1 that the set Λ has a uniform density given by D(Λ) = c.

| |
|---|


Next we give our second proof of Theorem 1.2. This proof, which does not involve Fourier analysis, is based on the following result due to Ruzsa and Székely [RS83].

- Theorem 3.3 ([RS83]). Let f ∈ L1(R) be real-valued with f > 0. Then there is a nonnegative (nonzero)


- g ∈ L1(R) such that the convolution f ∗g is nonnegative a.e.


In fact this is proved in [RS83] not only for functions on R, but on a wider class of locally compact abelian groups, which in particular includes also Rd for every d 1.

Second proof of Theorem 1.2. Let f +Λ be a tiling at level zero, and suppose to the contrary that f is nonzero. By replacing f(x) with the function Re ( f)−1 f(x) , we may assume that f is real-valued and that f > 0. So we can use Theorem 3.3 to ﬁnd a nonnegative, nonzero g ∈ L1(R) such that f ∗g is nonnegative a.e. Notice that also the function f ∗g is nonzero, since we have (f ∗g) = ( f)( g) > 0.

On the other hand we have f ∗δΛ = 0 a.e., and the measure δΛ is translation-bounded since Λ has bounded density. Using Fubini’s theorem this implies that

(f ∗g)∗δΛ = g∗(f ∗δΛ) = g∗0 = 0 a.e.,

hence (f ∗g)+Λ is a tiling at level zero. But this is a contradiction, since f ∗g is a nonnegative, nonzero function in L1(R), and Λ is a nonempty set.

###### 3.2 The set Λ is relatively dense

We now move on to the proof of Theorem 1.3. First we note that this theorem cannot be deduced based on Lemma 3.2 above, since there exist tilings f +Λ at level zero such that δΛ is not a scalar multiple of δ0 in any neighborhood of the origin; see [Lev20, Section 5] for a construction of such tilings.

We ﬁx the following terminology: given a sequence of measures {µn} on R, we say that the sequence is uniformly translation-bounded if there is a constant M > 0 not depending on n, such that supx∈R|µn|([x,x+1)) M for every n.

If {µn} is a uniformly translation-bounded sequence of measures on R, then we say that µn converges vaguely to a measure µ if for every continuous, compactly supported function ϕ we have ϕ dµn →

ϕ dµ (see, for instance, [Fol99, Section 7.3]). In this case, the vague limit µ must also be a translationbounded measure. For a uniformly translation-bounded sequence of measures {µn} to converge vaguely, it is necessary and sufﬁcient that {µn} converge in the space of tempered distributions. From any uniformly translation-bounded sequence of measures {µn} one can extract a vaguely convergent subsequence {µnj}.

Proof of Theorem 1.3. Let f + Λ be a tiling at level zero, and suppose to the contrary that Λ is not relatively dense. Then for each r > 0 one can ﬁnd an open interval I(r) of length r which is disjoint from Λ. By translating the interval I(r) we may assume that one of its endpoints lies in Λ (since the set Λ is nonempty). Then for arbitrarily large values of r the right endpoint of I(r) is in Λ, or for arbitrarily large values of r the left endpoint is in Λ. We will assume that the former is the case (the latter case can be treated similarly). It follows that there exist two sequences rj → +∞ and λj ∈ Λ, such that for each j the interval Ij := (λj −rj,λj) does not intersect Λ.

Deﬁne Λj := Λ − λj. Since Λ has bounded density, the measures δΛj are uniformly translationbounded. By passing to a subsequence if necessary, we may assume that δΛj converges vaguely to some (also translation-bounded) measure µ on R. The vague limit µ is supported on [0,+∞), since δΛj vanishes on (−rj,0). Moreover, each measure δΛj is positive and has a unit mass at the origin, which implies that µ is also positive and has an atom at the origin, of mass at least one. In particular the measure µ is nonzero.

On the other hand, since f +Λ is a tiling (at level zero), then by Theorem 2.1 the support of δΛ is contained in { f = 0}∪{0}. Since f is a nonzero continuous function, it follows that there is an open interval (a,b) on which δΛ vanishes. In turn this implies that δΛj also vanishes on (a,b) for each j. But as the sequence δΛj converges to µ in the distributional sense, we obtain that µ vanishes on (a,b) as well.

We conclude that µ is a nonzero, translation-bounded, positive measure on R, supported on [0,+∞) and whose Fourier transform µ vanishes on some open interval (a,b). But this contradicts classical results on boundary values of functions analytic in the upper half-plane. To be more concrete: choose two Schwartz functions ϕ,ψ such that ϕ > 0, supp( ϕ) ⊂ (−δ,δ), ψ is nonnegative, ψ is supported on [0,+∞) and ψ = 1. Then h := (µ ·ϕ)∗ψ is a nonzero function belonging to L1(R), supp(h) ⊂ [0,+∞), and the Fourier transform h = ( µ ∗ ϕ)· ψ is also in L1(R) and h vanishes on some nonempty open interval provided that δ is small enough. This contradicts the uniqueness theorem for functions in the Hardy space H1, see e.g. [Gar07, Chapter II].

#### 4 Non-periodic tilings by functions with sparse support

In this section we establish the existence of non-periodic tilings f +Λ of bounded density, such that the function f has “sparse” support (Theorem 1.8).

Recall that the ﬁrst example of a tiling f +Λ such that f ∈ L1(R), Λ ⊂ R has bounded density, but the set Λ does not have a periodic structure, was given in [KL16]. The proof was based on the implicit function method due to Kargaev [Kar82], and it yields a set Λ which is a small perturbation of the integers. However, in this example the function f is analytic, which implies that supp(f) = R.

In order to prove Theorem 1.8 we will use a different approach, which is based on two main ingredients. The ﬁrst one is a recent construction from [KS20] of a new type of crystalline measures on

- R. The second main ingredient is a result concerning interpolation of discrete functions by continuous ones with a sparse spectrum.


- 4.1 Crystalline measures A tempered distribution µ on R satisfying


µ = ∑

aλδλ, µ = ∑

bsδs (4.1)

λ∈Λ

s∈S

(i.e. both µ and µ are pure point measures), where Λ and S are discrete, closed sets in R, is called a crystalline measure [Mey16]. This notion plays a role in the mathematical theory of quasicrystals, i.e. atomic arrangements having a discrete diffraction pattern.

The classical example of a crystalline measure is µ = δZ, which satisﬁes µ = µ by Poisson’s summation formula. More generally, the measure δΛ is crystalline for any set Λ of the form (1.4), i.e. any set Λ ⊂ R having a periodic structure.

There exist also examples of crystalline measures on R, whose support is not contained in any set Λ with a periodic structure. Constructions of such examples, using different approaches, were given in the papers [LO16], [Kol16], [Mey16], [Mey17], [RV19].

Recently, new progress was achieved by Kurasov and Sarnak [KS20] who constructed examples of crystalline measures on R enjoying some remarkable properties, answering several questions left open by the above mentioned papers. To state the result, we recall the terminology introduced in Section 1.5 above:

Deﬁnition 4.1. We say that a set S ⊂ R has tempered growth if there is N such that

#(S∩(−r,r)) = O(rN), r → +∞. (4.2)

We note that if a set S ⊂ R has tempered growth then the measure δS is a tempered distribution, and also the converse is true.

- Theorem 4.2 ([KS20]). There exist crystalline measures µ of the form (4.1) with the following properties:


- (i) Λ is a set of bounded density;
- (ii) aλ = 1 for all λ ∈ Λ, i.e. we have µ = δΛ;


- (iii) Λ does not have a periodic structure, i.e. it is not of the form (1.4);
- (iv) S is a set of tempered growth.


Actually, the crystalline measures constructed in [KS20] have even stronger properties than stated above – we only mentioned the properties that will be used in this paper. In the more recent works [Mey20], [OU20], alternative approaches to the construction of crystalline measures with these properties can be found.

###### 4.2 Interpolation by functions with a sparse spectrum

We now turn to the second main ingredient in our proof of Theorem 1.8. It can be described in the context of the classical uncertainty principle, which states that a nonzero function f and its Fourier transform f cannot be “too small” at the same time. This general principle has many concrete versions, see [HJ94].

In particular, using complex analysis one can show that if f ∈ L1(R) has compact support, and if f vanishes on a set S ⊂ R satisfying

#(S∩(−r,r)) r

= +∞, (4.3)

limsup

r→+∞

then f = 0 a.e. This fact was used in [LM91], [KL96] in order to prove that if a nonzero function f ∈ L1(R) has compact support, and if f tiles at some level w by a translation set Λ of bounded density, then Λ must have a periodic structure (Theorem 1.5).

On the other hand, suppose that Ω ⊂ R is a set which contains arbitrarily long intervals (and so Ω must be unbounded, but can be very sparse). Then given any discrete set S ⊂ R of tempered growth, there exists a nonzero function f ∈ L1(R), supp(f) ⊂ Ω, such that f vanishes on S. This is a consequence of the following result:

Theorem 4.3. Let Ω ⊂ R be a set which contains arbitrarily long intervals, and let S ⊂ R be a set of tempered growth. Then given any values {c(s)} ∈ 1(S), one can ﬁnd a smooth function f ∈ L1(R), supp(f) ⊂ Ω, such that f(s) = c(s) for all s ∈ S.

If we call supp(f) the “spectrum” of the function f, then the result means that every discrete function in 1(S) can be interpolated by a continuous function (the Fourier transform of an L1 function) with spectrum in Ω. We refer the reader to [OU16] where the problem of interpolation by functions with a given spectrum is discussed in detail.

The approach that we use to prove Theorem 4.3 is inspired by [OU09, Section 3].

###### 4.3 Proof of Theorem 4.3 We begin with a simple lemma.

- Lemma 4.4. Let S ⊂ R be a discrete set of tempered growth, and let N be a sufﬁciently large number such that (4.2) holds. Then for any t ∈ R\S and any p > N we have


### ∑

###### |s−t|−p < +∞. (4.4)

s∈S

Proof. The condition (4.2) remains valid if we replace S with S−t, so we may assume that t = 0. The function n(r) := #(S∩(−r,r)) is then a step function vanishing near the origin. For each R > 0 which is not a jump discontinuity point of n(r), we have

### ∑

|s|−p =

|s| R

R 0

dn(r) rp

=

n(R) Rp

+ p

R 0

n(r) rp+1

dr (4.5)

which follows from integration by parts. But as n(r) = O(rN) and p > N, the right-hand side of (4.5) remains bounded as R → ∞. The condition (4.4) is thus established.

| |
|---|


Proof of Theorem 4.3. We suppose that Ω ⊂ R is a set which contains arbitrarily long intervals, and that

- S ⊂ R is a discrete set of tempered growth. We also choose and ﬁx some enumeration {sj} of the set S. Let Φ be an inﬁnitely smooth function on R supported on the interval [−1,1], and such that Φ = 1.


For each r > 0 we denote Φr(x) := r−1Φ(r−1x). Deﬁne

fj(x) := Φrj(x−τj)e2πisjx where the numbers rj > 0 and τj ∈ R will be determined later on. Then we have fj(t) = Φ(rj(t −sj))e−2πiτj(t−sj).

In particular, fj(sj) = Φ(0) = 1.

Let N be a sufﬁciently large number such that (4.2) holds, and let p > N. Since Φ is a Schwartz function, there is a constant C = C(Φ, p) > 0 such that | Φ(t)| C|t|−p for every nonzero t. For j ﬁxed, we have

| Φ(rj(sk−sj))| Cr−j p ∑

### ∑

| fj(sk)|= ∑

|sk −sj|−p. (4.6)

k =j

k =j

k =j

If we use Lemma 4.4 with the set {sk : k = j} and t = sj, the lemma yields that the sum on the right-hand side of (4.6) converges. We thus see that given any ε > 0, we can choose rj = rj(S,Φ, p,ε) > 0 large enough such that the right-hand side of (4.6) does not exceed ε. It follows that we can choose the numbers rj in such a way that, no matter how the numbers τj are chosen, we have

M := sup

- j

∑

- k =j


| fj(sk)| ε. (4.7)

To any sequence b = {bj} belonging to 1, we associate a corresponding sequence c = {ck} deﬁned by

ck =∑

fj(sk)bj =bk+∑

fj(sk)bj.

j

j =k

It follows from (4.7) that the mapping b  → c deﬁnes a bounded linear operator A : 1 → 1 such that

A−I = M ε, where I is the identity operator. If we choose ε < 1 then this implies that A is invertible in 1.

Now suppose that we are given a sequence c = {ck} ∈ 1. Let b = {bj} ∈ 1 be the solution of the equation Ab = c, and deﬁne

f(x):=∑

bj fj(x). (4.8)

j

We observe that

fj L1(R) = Φ L1(R), ∑|bj|<∞,

which implies that the series (4.8) converges in L1(R). It follows that

f(t)=∑

bj fj(t), (4.9)

j

where the series (4.9) converges uniformly on R. In particular we have

f(sk)=∑

bj fj(sk) = ck (4.10)

j

for each k.

Finally we observe that fj is supported on the interval Ij := [τj −rj,τj +rj]. Since the rj’s were chosen in a way that does not depend on the values of the τj’s, we can use the assumption that Ω contains arbitrarily long intervals in order to choose each τj such that the interval Ij lies in Ω. Moreover, by choosing these intervals e.g. such that dist(Ij,Ik) 1 (j = k) this implies that supp(f) ⊂ Ω and ensures that f is inﬁnitely smooth. Thus f has all the required properties, and Theorem 4.3 is proved.

| |
|---|


- 4.4 Proof of Theorem 1.8 Now we can ﬁnish the proof of Theorem 1.8 based on the two results above, namely, Theorem 4.2 and


- Theorem 4.3. Let µ = δΛ be the crystalline measure given by Theorem 4.2, that is, Λ ⊂ R is a set of bounded


density but not of a periodic structure, such that δΛ is a pure point measure, δΛ = ∑s∈Sbsδs, where S ⊂ R is a set of tempered growth.

Since the set S is discrete and closed, it follows that there is a > 0 such that we have δΛ = c·δ0 in (−a,a). Moreover, we must have c > 0 due to Lemma 3.2. By rescaling the set Λ if needed, we may assume that δΛ = δ0 in (−a,a). In particular, this means that the set S contains the origin.

Now suppose that we are given a scalar w, and a set Ω ⊂ R which contains arbitrarily long intervals. Let ξ be any real number, ξ ∈/ S, and deﬁne S := S∪{ξ}. Then also the set S has tempered growth. We prescribe the values c(ξ) = 1, c(0) = w, and c(s) = 0 for all s ∈ S\{0}, then these values belong to 1(S ). Hence using Theorem 4.3 we can ﬁnd a smooth function f ∈ L1(R), supp(f) ⊂ Ω, such that f(s) = c(s) for all s ∈ S . This means that we have f(0) = w and f(s) = 0 for all s ∈ S\{0}. It also implies that f(ξ) = 0, which ensures that the function f is nonzero.

We conclude that f vanishes on the set supp( δΛ) \ {0}, i.e. the condition (2.5) is satisﬁed, and moreover we have δΛ({0})· f = w. Due to Theorem 2.2 this implies that f +Λ is a tiling at level w, and the proof is thus complete.

| |
|---|


#### 5 Tilings of unbounded density

In this section we construct examples of tilings f +Λ such that the set Λ does not have bounded density (Theorem 1.9). We are not aware of any previous example of such a tiling in the literature. Moreover, in our example the set Λ has tempered growth (see Deﬁnition 4.1) and the function f is in the Schwartz class. We will also show that in any such a tiling, the function f must have zero integral, no matter what the level w of the tiling is (Theorem 1.10).

- 5.1 Translation sets with unbounded density We will construct tilings f +Λ such that the translation set Λ ⊂ R has the form


Λn, Λn ⊂ (n−ε,n+ε), #Λn = n2 +1, (5.1)

###### Λ =

n∈Z

where ε > 0 is an arbitrarily small number. Then the condition (1.2) is not satisﬁed and Λ does not have bounded density. On the other hand it follows from (5.1) that #(Λ∩(−r,r)) = O(r3) as r → +∞, so the set Λ has tempered growth and δΛ is a tempered distribution on R. We will prove the following theorem:

- Theorem 5.1. Given any ε > 0 there is a set Λ ⊂ R of the form (5.1), such that


δ 0 4π2

in (−21, 12). (5.2)

δΛ = δ0 −

In order to better understand what is behind condition (5.2), consider the measure µ on R which assigns the mass n2 +1 to each point n ∈ Z. Using Poisson’s summation formula one can check that the Fourier transform of µ is given by µ = ∑k∈Z(δk −(4π2)−1δ k ). Theorem 5.1 now says that one can “redistribute” the mass n2 +1 assigned at each point n ∈ Z into equal unit masses at n2 +1 distinct points of a set Λn contained in a small neighborhood of n, in such a way that the Fourier transform of the new measure δΛ thus obtained remains unchanged on the interval (−21, 12).

The role of condition (5.2) in the tiling problem is clariﬁed by the following lemma:

- Lemma 5.2. Let Λ ⊂ R be a set of tempered growth, and suppose that there is a > 0 such that supp( δΛ)∩(−a,a) = {0}. (5.3)


Then given any scalar w one can ﬁnd a nonzero Schwartz function f, such that f +Λ is a tiling at level w. Proof. It is well-known that a distribution supported by the origin is a ﬁnite linear combination of derivatives of δ0 (see [Rud91, Theorem 6.25]). Hence (5.3) implies that

n

### ∑

cjδ0(j) in (−a,a), (5.4)

δΛ =

j=0

and we may assume that the highest order coefﬁcient cn is nonzero. It follows that tn δΛ(t) = cnn!(−1)n ·δ0(t) in (−a,a) (5.5)

(see e.g. [Fol99, Section 9.1, Exercise 3]). Let ϕ be a nonzero Schwartz function, supp( ϕ) ⊂ (−a,a), ϕ(0) = w. Then

ϕ(n)(x) cnn!(−2πi)n

(5.6) is also a nonzero Schwartz function. We claim that f +Λ is a tiling at level w. Indeed,

f(x) :=

ϕ(t)tn

f(t) δΛ(t) =

cnn!(−1)n · δΛ(t) = ϕ(t)δ0(t) = w·δ0(t), (5.7) where in the second equality we used (5.5). This implies that f ∗δΛ = w as needed.

| |
|---|


Since condition (5.2) implies (5.3), we see that Theorem 1.9 is a consequence of Theorem 5.1 and Lemma 5.2. It therefore remains to prove Theorem 5.1.

###### 5.2 Kargaev’s implicit function method

In order to prove Theorem 5.1 we will use a variant of Kargaev’s implicit function method [Kar82]. See also [KL16], [Lev20] for applications of the method in the construction of translational tiling examples.

The proof will be done in several steps.

- 5.2.1 For each k = 1,2,3,... let χk be the function on R deﬁned by


χk(x) = k− j+1, x ∈ 2k((kj+−11)), k(k2+j1) , 1 j k, (5.8) and χk(x) = 0 outside the interval [0, k+21).

Let {αn}, n ∈ Z, be a bounded sequence of real numbers. To such a sequence we associate a function F on the real line, deﬁned by

F(x):= ∑

Fn(x), x ∈ R, (5.9) where we let

n∈Z

Fn(x) := sign(αn)·χn2+1(xα−n

) (5.10)

n

for each n ∈ Z such that αn = 0, while if αn = 0 then we let Fn(x) := 0. (The notation sign(αn) means +1 or −1 depending on whether αn > 0 or αn < 0.) One can verify, using the assumption that the sequence {αn} is bounded, that the series (5.9) converges

in the space of tempered distributions. For instance, this follows from the fact that (1+x2)−1∑|Fn(x)| is a bounded function.

Theorem 5.3. Let 0 < ε < 1. Then for any sufﬁciently small r > 0 one can ﬁnd a real sequence α = {αn}, n ∈ Z, satisfying

(1−ε)r |αn| (1+ε)r, n ∈ Z, (5.11) and such that F = 0 in (−21, 21), where F is the function deﬁned by (5.9).

We will ﬁrst prove Theorem 5.3 and then use it to deduce Theorem 5.1.

- 5.2.2 We will need the following lemma.

- Lemma 5.4. The function χk has the following properties:


- (i) χk(x)dx = 1;
- (ii) xχk(x)dx Ck−1;
- (iii) | χk(−s)−1| C|s|k−1;
- (iv) v χk(−v)−1 −u χk(−u)−1 Ck−1|v−u|·max{|u|,|v|}


for every s,u,v ∈ R, where C > 0 is an absolute constant. Proof. The property (i) can be checked directly. In order to establish (ii) we can estimate the left hand side by k 0 2/(k+1)xdx = 2k/(k+1)2. Together with the estimate

| χk(−s)−1| = χk(x)(e2πisx −1)dx 2π|s| xχk(x)dx (5.12)

this yields (iii). Finally, to establish (iv) consider the function ϕ(x) := x(e2πix −1). We may suppose that u < v, then the left hand side of (iv) is equal to

χk(x)

ϕ(vx)−ϕ(ux) x

dx = χk(x)

v u

ϕ (sx)dsdx (5.13) |v−u|· max

s∈[u,v]

χk(x)|ϕ (sx)|dx. (5.14) If we use the estimate |ϕ (sx)| C|sx|, then (5.14) and (ii) imply (iv).

| |
|---|


- 5.2.3 Let X be the space of all bounded sequences of real numbers α = {αn}, n ∈ Z, endowed with the norm


|αn| that makes X into a real Banach space.

α X := sup n∈Z

Denote I := [−12, 12]. LetY be the space of all continuous functions ψ : I → C satisfying ψ(−t) = ψ(t) for all t ∈ I. If we endow Y with the norm ψ Y = sup|ψ(t)|, t ∈ I, then also Y is a real Banach space.

Let α = {αn}, n ∈ Z, be a sequence in X. Deﬁne

(Rα)(t):= ∑

e2πint ·αn χn2+1(−αnt)−1 . (5.15)

n∈Z

We notice that the terms of the series (5.15) are elements of Y. By Lemma 5.4(iii), the n’th term of the series is bounded by C|αn|2(n2 +1)−1 uniformly on I, where C > 0 does not depend on α or n. Hence the series (5.15) converges uniformly on I to an element of Y, and we have

Rα Y C α 2X, (5.16) where the constant C does not depend on α.

We note that the mapping R : X → Y deﬁned by (5.15) is nonlinear.

- 5.2.4 For each r > 0 let Ur denote the closed ball of radius r around the origin in X:

Ur := {α ∈ X : α X r}. (5.17)

- Lemma 5.5. Given any ρ > 0 there is r > 0 such that Rβ −Rα Y ρ β −α X, α,β ∈ Ur. (5.18)

In particular, if r is small enough then R is a contractive (nonlinear) mapping on Ur. Proof. Let α,β ∈ Ur. Then using (5.15) we have

(Rβ −Rα)(t)= ∑

n∈Z

e2πint · βn χn2+1(−βnt)−1 −αn χn2+1(−αnt)−1 . (5.19)

By Lemma 5.4(iv), the n’th term of the series is bounded by Cr(n2 + 1)−1|βn − αn| uniformly on I, where C > 0 does not depend on r, α, β or n. Hence the series converges uniformly on I and

Rβ −Rα Y Cr β −α X, where C is a constant not depending on r, α or β. It thus sufﬁces to choose r small enough so that Cr ρ.

| |
|---|


5.2.5 For each element ψ ∈ Y we denote by F(ψ) the sequence

ψ(n) =

I

ψ(t)e−2πintdt, n ∈ Z, (5.20)

of Fourier coefﬁcients of ψ. Since the Fourier coefﬁcients ψ(n) are real and bounded, we have a linear mapping F : Y → X satisfying F(ψ) X ψ Y.

- Lemma 5.6. Given any ε > 0 there is δ > 0 with the following property: Let β ∈ X, β X δ. Then one can ﬁnd an element α ∈ X, α −β X ε β X, which solves the equation α +F(Rα) = β. Proof. Fix β ∈ X such that β X δ, and let




B = B(β,ε) := {α ∈ X : α −β X ε β X}. We observe that if α ∈ B then α X (1+ε) β X. Deﬁne a map H : B → X by H(α) := β −F(Rα), α ∈ B,

and notice that an element α ∈ B is a solution to the equation α +F(Rα) = β if and only if α is a ﬁxed point of the map H.

Let us show that if δ is small enough then H(B) ⊂ B. Indeed, if α ∈ B then using (5.16) we have

H(α)−β X = F(Rα) X Rα Y C α 2X C(1+ε)2 β 2X.

Hence if we choose δ such that C(1+ε)2δ ε then we obtain

H(α)−β X ε β X, and it follows that H(B) ⊂ B.

It also follows from Lemma 5.5 that if δ is small enough, then H is a contractive mapping from the closed set B into itself. Indeed, let α ,α ∈ B, then we have

H(α )−H(α ) X = F(Rα −Rα ) X Rα −Rα Y ρ α −α X,

where 0 < ρ < 1. Then the Banach ﬁxed point theorem implies that H has a (unique) ﬁxed point α ∈ B, which yields the desired solution.

| |
|---|


###### 5.2.6 Proof of Theorem 5.3

Let r > 0, and let β = {βn}, n ∈ Z, be a real sequence deﬁned by βn := (−1)nr. Then β X = r. If r = r(ε) > 0 is small enough, then by Lemma 5.6 there is an element α ∈ X, α −β X ε β X, which solves the equation α +F(Rα) = β.

We observe that the estimate α −β X ε β X implies (5.11). The relation α +F(Rα) = β means that β −α is the sequence of Fourier coefﬁcients of the function

Rα. This implies that the series

### ∑

(βn −αn)e2πint converges in L2(I) to Rα.

n∈Z

Since we have βn = (−1)nr, n ∈ Z, the series

### ∑

βne2πint

n∈Z

converges in the distributional sense to the measure r·δZ+1

on R. In particular, this series converges to zero in the open interval (−12, 21).

2

Let F be the function given by (5.9) associated to the sequence α = {αn}. Then F(−t) = lim

### ∑

###### Fn(−t)

N→∞

|n| N

in the sense of distributions, and by (5.10) we have

Fn(−t) = e2πint ·αn χn2+1(−αnt). (5.21) Hence

### ∑

βne2πint− ∑

(βn−αn)e2πint+ ∑

e2πint ·αn χn2+1(−αnt)−1 .

F(−t) = lim

N→∞

|n| N

|n| N

|n| N

The ﬁrst sum converges in the distributional sense to zero in (−21, 12). The second sum converges in L2(I) to Rα. The third sum converges to Rα uniformly on I. It follows that the distribution F vanishes in the

open interval (−12, 21).

| |
|---|


###### 5.3 Proof of Theorem 5.1

Let 0 < ε < 1 be given, and for r = r(ε) > 0 sufﬁciently small let {α(n)}, n ∈ Z, be the sequence given by Theorem 5.3. Deﬁne

2jαn (n2 +1)(n2 +2)

, 1 j n2 +1 (5.22)

Λn = n+

and

Λn. (5.23)

Λ =

n∈Z

We have αn = 0 for every n ∈ Z, due to (5.11). Hence Λn is a set with exactly n2 +1 elements. The set Λn is contained in the interval [n−|αn|,n+|αn|]. This yields (5.1) provided that r > 0 is small enough, again due to (5.11). In particular we may assume that the sets Λn are pairwise disjoint.

Observe that the distributional derivative of the function F in (5.9) is

F = ∑

F n = ∑

((n2 +1)δn −δΛn),

n∈Z

n∈Z

and hence

δΛ = ∑

(n2 +1)δn −F .

n∈Z

The Fourier transform of the measure ∑n∈Z(n2 +1)δn is ∑k∈Z δk −(4π2)−1δ k , which follows from Poisson’s summation formula. This implies that

δ 0 4π2 − F in (−21, 12).

δΛ = δ0 −

But since F vanishes in (−21, 12), then the same is true for F , so (5.2) is established.

| |
|---|


###### 5.4 Proof of Theorem 1.10

Finally we show that if f +Λ is a tiling at some level w, where Λ ⊂ R is any set of tempered growth but not of bounded density, and f is any function in the Schwartz class, then f must have zero integral.

Suppose to the contrary that f = f(0) is nonzero. Then, due to the continuity and smoothness of f, there is a Schwartz function g such that f · g = 1 in some neighborhood (−a,a) of the origin. Let h > 0 be a Schwartz function with supp( h) ⊂ (−a,a), then

h· g· f = h and hence

h∗g∗ f = h. It follows that

h∗δΛ = (h∗g∗ f)∗δΛ = (h∗g)∗(f ∗δΛ) = w· (h∗g),

where in the last equality we used the tiling assumption f ∗δΛ = w (the associativity of the convolution is justiﬁed since δΛ is a tempered distribution and f,g,h are Schwartz functions, see [Rud91, Theorem

- 7.19]). We conclude that h+Λ is a tiling (at a certain level). But it is known, see [KL96, Lemma 2.1], that if


- h is a nonnegative, nonzero function and if h+Λ is a tiling, then the set Λ must have bounded density. We thus arrive at a contradiction.


| |
|---|


- 6 Open problems We conclude the paper by posing some open problems.


###### 6.1 Tiling at level zero

The following problem was already mentioned in Section 1.2 above: Let f +Λ be a tiling at level zero, where the function f ∈ L1(R) is nonzero and the set Λ ⊂ R is nonempty and has bounded density. Does it follow that Λ has a uniform density D(Λ)?

In Fourier analytic terms, the problem can be equivalently stated as follows: Let Λ ⊂ R be nonempty

and have bounded density, and suppose that δΛ vanishes on some open interval (a,b). Does Λ necessarily have a uniform density?

What makes the problem nontrivial is the existence of tilings f +Λ at level zero such that δΛ is not a scalar multiple of δ0 in any neighborhood of the origin, see [Lev20, Section 5]. In particular, Lemma 3.2 does not apply.

We note that by Theorem 1.3 the set Λ must be relatively dense, so if the density D(Λ) exists then it is a strictly positive number.

###### 6.2 Non-periodic tilings

Let f be a nonzero function in L1(R), and suppose that the set {x : f(x) = 0} has ﬁnite measure. If f tiles at some level w by a translation set Λ ⊂ R of bounded density, does it follows that Λ has a periodic structure?

Theorem 1.5 does not apply here, since f is not assumed to have compact support. Does there exist a measurable set Ω ⊂ R, 0 < mes(Ω) < +∞, whose indicator function 1Ω can tile at

level one, or, a weaker requirement, at some other integer level w, with a translation set Λ ⊂ R that does not have a periodic structure?

Notice that such a set Ω (if it exists) must be unbounded, again due to Theorem 1.5.

###### 6.3 Tilings of unbounded density

Let f ∈ L1(R) be nonzero and have compact support, and suppose that f +Λ is a tiling at some level w, where Λ ⊂ R is a discrete set (not a multi-set) of tempered growth. Does it follow that Λ is of the form (1.4), i.e. Λ is a set of bounded density having a periodic structure?

In other words, the question is whether Theorem 1.5 remains valid if the set Λ is not assumed to have bounded density, but only tempered growth.

We note that Theorem 1.9 does not provide a negative answer to this question, since the function f constructed in the proof of this theorem has unbounded support.

###### 6.4 Lattice tilings

Let f ∈ L1(Rd), d 1, and suppose that f tiles at some level w with a translation set Λ ⊂ Rd of bounded density.2 Does there necessarily exist a lattice L ⊂ Rd such that f +L is also a tiling, possibly at a different level w ?

The answer is known to be afﬁrmative in the special case where Λ is assumed to be a disjoint union of ﬁnitely many translated lattices, namely, Λ = Nj=1(Lj +τj) where each Lj is a lattice in Rd and the τj are translation vectors. This was proved in dimension one in [KL96, p. 673], while in several dimensions the result was proved more recently in [Liu18, Theorem 1.6]. In both proofs, number theory plays an essential role: the proof in R uses the classical Skolem–Mahler–Lech theorem, while in Rd the proof relies on a result due to Evertse, Schlickewei and Schmidt [ESS02].

#### References

[ESS02] J.-H. Evertse, H. P. Schlickewei, W. M. Schmidt, Linear equations in variables which lie in a multiplicative group. Ann. of Math. (2) 155 (2002), no. 3, 807–836. 22

[Fol99] G. B. Folland, Real analysis: Modern techniques and their applications. Second edition. John

Wiley & Sons, 1999. 10, 16 [Gar07] J. B. Garnett, Bounded analytic functions. Revised ﬁrst edition. Springer, 2007. 10 [HJ94] V. Havin, B. Jöricke, The uncertainty principle in harmonic analysis. Springer-Verlag, 1994.

12 [IK13] A. Iosevich, M. N. Kolountzakis, Periodicity of the spectrum in dimension one. Anal. PDE 6

(2013), no. 4, 819–827. 4

[Kar82] P. P. Kargaev, The Fourier transform of the characteristic function of a set vanishing on an interval (Russian). Mat. Sb. (N.S.) 117 (1982), 397–411. English translation in Math. USSR-Sb. 45 (1983), 397–410. 4, 11, 16

- [Kol00a] M. N. Kolountzakis, Non-symmetric convex domains have no basis of exponentials. Illinois J. Math. 44 (2000), 542–550. 6, 7
- [Kol00b] M. N. Kolountzakis, Packing, tiling, orthogonality and completeness. Bull. London Math. Soc. 32 (2000), 589–599. 6, 7


[Kol04] M. N. Kolountzakis, The study of translational tiling with Fourier analysis. Fourier analysis and convexity, pp. 131–187, Birkhäuser, 2004. 2, 5

2A set Λ ⊂ Rd is said to have bounded density if there exists M > 0 such that #(Λ∩(x+B)) M for all x ∈ Rd, where B is the open unit ball in Rd.

[Kol16] M. N. Kolountzakis, Fourier pairs of discrete support with little structure. J. Fourier Anal. Appl. 22 (2016), no. 1, 1–5. 11

[KL96] M. N. Kolountzakis, J. C. Lagarias, Structure of tilings of the line by a function. Duke Math. J. 82 (1996), 653–678. 2, 3, 4, 5, 6, 7, 12, 21, 22

[KL16] M. N. Kolountzakis, N. Lev, On non-periodic tilings of the real line by a function. Int. Math. Res. Not. IMRN 2016, no. 15, 4588–4601. 2, 4, 6, 9, 11, 16

[KS20] P. Kurasov, P. Sarnak, Stable polynomials and crystalline measures. J. Math. Phys. 61 (2020), no. 8, 083501, 13 pp. 4, 11, 12

[LM91] H. Leptin, D. Müller, Uniform partitions of unity on locally compact groups. Adv. Math. 90

(1991), 1–14. 2, 3, 4, 12 [Lev20] N. Lev, An example concerning Fourier analytic criteria for translational tiling. Preprint,

###### arXiv:2007.09930. 2, 3, 7, 10, 16, 21

[LO16] N. Lev, A. Olevskii, Quasicrystals with discrete support and spectrum. Rev. Mat. Iberoam. 32

(2016), no. 4, 1341–1352. 11 [Liu18] B. Liu, Periodic structure of translational multi-tilings in the plane. Amer. J. Math., to appear,

###### arXiv:1809.03440. 2, 22

[Mey70] Y. Meyer, Nombres de Pisot, nombres de Salem et analyse harmonique (French). Lecture Notes in Mathematics 117, Springer-Verlag, 1970. 3

- [Mey16] Y. Meyer, Measures with locally ﬁnite support and spectrum. Proc. Natl. Acad. Sci. USA 113

(2016), no. 12, 3152–3158. 11

- [Mey17] Y. Meyer, Measures with locally ﬁnite support and spectrum. Rev. Mat. Iberoam. 33 (2017), no. 3, 1025–1036. 11


[Mey20] Y. Meyer, Curved model sets and crystalline measures. To appear in Applied and Numerical Harmonic Analysis, Springer. 12

[OU09] A. Olevskii, A. Ulanovskii, Interpolation in Bernstein and Paley-Wiener spaces. J. Funct. Anal. 256 (2009), no. 10, 3257–3278. 12

[OU16] A. Olevskii, A. Ulanovskii, Functions with disconnected spectrum: sampling, interpolation, translates. American Mathematical Society, 2016. 12

[OU20] A. Olevskii, A. Ulanovskii, A simple crystalline measure. Preprint, arXiv:2006.12037. 12 [RV19] D. Radchenko, M. Viazovska, Fourier interpolation on the real line. Publ. Math. Inst. Hautes

Études Sci. 129 (2019), 51–81. 11 [Rud91] W. Rudin, Functional analysis, Second edition. McGraw-Hill, New York, 1991. 6, 15, 21

[RS83] I. Z. Ruzsa, G. J. Székely, Convolution quotients of nonnegative functions. Monatsh. Math.

95 (1983), no. 3, 235–239. 9

###### AUTHORS

M. N. Kolountzakis Department of Mathematics and Applied Mathematics University of Crete Voutes Campus, GR-700 13 Heraklion, Crete Greece kolount@uoc.gr http://mk.eigen-space.org/

Nir Lev Department of Mathematics Bar-Ilan University Ramat-Gan 5290002 Israel levnir@math.biu.ac.il https://u.math.biu.ac.il/~levnir/

