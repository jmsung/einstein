---
type: source
kind: paper
title: A classification of Fourier summation formulas and crystalline measures
authors: Felipe Gonçalves
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2312.11185v3
source_local: ../raw/2023-gonalves-classification-fourier-summation-formulas.pdf
topic: general-knowledge
cites:
---

# arXiv:2312.11185v3[math.CA]26Jan2026

## A CLASSIFICATION OF FOURIER SUMMATION FORMULAS AND CRYSTALLINE MEASURES

FELIPE GONC¸ALVES

Abstract. We completely classify Fourier summation formulas, and in particular, all crystalline measures with quadratic decay. Our classification employs techniques from almost periodic functions, Hermite-Biehler functions, de Branges spaces and Poisson representation. We show how our classification generalizes recent results of Kurasov & Sarnak and Olevskii & Ulanovskii. As an application, we give a new classification result for nonnegative measures with uniformly discrete support that are bounded away from zero on their support. Moreover, we give a new construction using eta-quotients, generalizing an old example of Guinand.

1. Introduction

To understand the atomic structure of a crystal (of some material) one can fire a beam of electrons into the object and observe an electron diffraction pattern on a screen1. In most materials one observes a periodic diffraction pattern, such as a two-dimensional lattice with 6-fold symmetry, as in Tantalum pentoxide Ta2O5. However, this is not the case with Holmium-magnesium-zinc Ho-Mg-Zn, where one observes some 5-fold and 10fold symmetries, hence a non-periodic diffraction pattern (see [46, Figures 1 and 2]). The first to record such phenomena experimentally was materials scientist Dan Shechtman, in 1982, and today these materials are called quasicrystals. He was awarded the Nobel Prize in Chemistry in 2011 for his breakthrough. Mathematically, if µ represents the crystal (so µ ě 0 and supppµq is uniformly discrete) then what we see in the diffraction pattern is effectively |µp|2 (where µp is the Fourier transform of µ). A famous inverse problem is that of reconstructing atomic structure from diffraction data, overcoming the issue that diffraction only determines intensity of spots but loses phase information. Real-world quasicrystals (such as Decagonite Al71Ni24Fe5), although uniformly discrete in physical space, typically have everywhere dense diffraction spectrum2. The diffraction pattern is a super-position of Dirac combs with several intensities (Bragg peaks) however, due to instrument precision and tuning, we only see peaks that have, say, an intensity above 10´4 of the brightest peak. Hence, in real physical experiments, although the diffraction picture visually seems to be locally finite, nevertheless the real measure µp has a dense support. On the other hand, stable 1D quasicrystals with locally finite spectra do exist

Date: January 27, 2026. 1This technique is called high resolution electron microscopy (HRTEM), but another common technique is X-ray microscopy.

- 2We thank Michael Baake for pointed this out, among several other remarks.


in nature, and can be found as projections along pseudo axis’s, see [45, Figure 1] and the references in [19, Ch. 7]. Nowadays there is unified framework to construct measures µ whose spectrum fits the data observed in the diffraction patterns of physical quasicrystals, these are called model sets (or Meyer sets) [8, 19, 28, 36, 37, 39].

From the mathematical standpoint, many mathematicians have wondered about what different types of measures µ with pure point support and spectrum are there, and what kind of geometrical properties of the spectrum are allowed under various conditions on µ? The main classification question from the mathematical perspective is:

Can on one classify all measures µ with pure point support and spectrum? Freeman Dyson addressed this question in 2009 in his famous paper [18], using the word quasicrystals for such measure, suggesting that such classification might be a very difficult mathematical problem, but made the “outrageous suggestion” it could potentially give a proof of the Riemann Hypothesis3. He said: “My suggestion is the following. Let us pretend that we do not know that the Riemann Hypothesis is true. Let us tackle the problem from the other end. Let us try to obtain a complete enumeration and classification of one-dimensional quasicrystals. That is to say, we enumerate and classify all point distributions that have a discrete point spectrum.” Dyson stated this because of Guinand’s prime summation formula (also known as Weyl’s summation formula), which we explain in the Section 8. The notorious paper of Guinand [22], which inspired Dyson, grasps such classification, but it was forgotten awhile. Meyer resurrected Guinand’s paper in [37].

We say a measure µ is crystalline if it has locally finite support and its Fourier transform µp also has locally finite support4. In this scenario, the first geometric classification breakthrough occurred in the work of Lev & Olevskii [30, 31], where they classify classical Poisson summation as the only crystalline measures that have uniformly discrete support and spectrum. Guinand’s example [22, p. 265] shows the theorem is tight (we generalize his construction in Section 8). Recently, the field is very active, and the amazing works of Radchenko & Viazovska [42], Ramos & Sousa [44], Kurasov & Sarnak [26], Olevskii & Ulanovskii [40] and Alon et. al. [2, 1], but also, the not so recent works of Bohr [16], Besicovitch [10], Guinand [22], de Branges [13] and Meyer [35], deeply inspired this paper.

In this paper we completely classify (what we call) Fourier summation formulas, and in particular we classify crystalline measures that have quadratic decay, although our results are more general and can be applied to dense spectra. As far as we know, it is the first time classification results are proven in such generality. Our classification involves heavily the theory of almost periodic analytic functions [10] and de Branges spaces techniques [13]. Almost periodic functions have permeated this are for some time now, for example

- 3We do not share the same belief. 4Such measures are sometimes also called quasicrystals, Fourier quasicrystals, or doubly sparse, depending on the author, area, context, decay conditions, etc. We will stick with Meyer’s denomination of crystalline measure.


in the works of Guinand [22], Meyer [38] and Baake et. al. [4, 8, 9], among others. On the other hand, the connection with de Branges spaces that we make here is totally new.

- A Fourier summation formula should be one where the identity ż


φpptqdµptq “ ÿ

apλnqφpλnq

R

nPN

holds, at the bear minimum, for all functions φ P Cc8pRq, where tλnunPN Ă R is some sequence of real nodes, tapλnqunPN Ă C are some complex coefficients and µ is some complex-valued measure. There is a zoo of formulas of such type which we describe in Section 8. We choose the above form of because: (1) We want a summation formula, so there must be a sum somewhere in the definition and such summation must be singular with respect to Lebesgue measure; (2) Allowing the right hand side above to have a vanishing singular part is boring, as otherwise any L1-function would give rise to a Fourier summation formula.

1.1. Overview. Theorems 1 and 2 are our main general classification results and we later specialize them for measures with locally finite support (in particular, also crystalline measures) in Theorems 3 and 4. Finally, we derive a new characterization Theorem 5 for measures with uniformly discrete support such that µ|supppµq ě ε, but with no geometric assumption on µp, which perhaps makes this result most useful to physics.

2. Main Results

We will have to introduce several things before we can state our first main result. We say that a complex-valued measure µ on R is locally finite if its total variation

ÿ

|µ|pKq “ sup

|µpPjq| ă 8

\jPNPj“K

jPN

is finite on every compact set K Ă R, or equivalently, if there are nonnegative locally finite Borel measures µj such that µ “ µ1´µ2`ipµ3´µ4q. We say that µ is tempered if it is a complex-valued locally finite measure and there exists a tempered distribution u P S1pRq such that upφq “ şR φdµ for all φ P Cc8pRq. Some authors might not concord with this definition, but we are following the setup of [4]. We say µ is strongly tempered if φ P L1p|µ|q for all φ P SpRq. By [4, Prop. 2.5], this is equivalent to the degree of µ

degpµq :“ min"n P Z : ż

ă 8*

d|µ|ptq p1 ` t2qn{2

R

being ă 8. In particular, the functional φ ÞÑ şR φdµ defines a tempered distribution, hence µ is tempered. The implication [tempered] ñ [strongly tempered] is false. Indeed,

the measure µ “ ř

ně0 3n2pδn ´ δn`4´n2q is not strongly tempered but it is tempered, since

ş

2´t2d|µ|ptq ě ř

### ně0 3n22´n2 “ 8 but5 |ř

ně0 3n2pφpnq ´ φpn ` 4´n2qq| ! }φ1}8.

5Whenever it is convenient, we write A ! B to mean that there is C ą 0 such that |A| ď C|B|.

We say that a function a : R Ñ C is locally summable if supppaq :“ tλ P R : apλq ‰ 0u is at most countable and for some enumeration supppaq “ tλnuně1 we have

ÿ

|apλnq| ă 8,

λnPr´T,Ts

for all T ą 0. This is equivalent to say that ν “ ř

ně1 apλnqδλ

is locally finite. In particular, local sums

n

ř

λPK apλq are always well-defined for any bounded set K Ă R.

Definition 1 (Fourier Summation Pairs). We say pµ,aq is a Fourier summation pair pFS-pairq if µ is a strongly tempered measure, a : R Ñ C is locally summable and

ż

φpptqdµptq “ ÿ

apλqφpλq

R

λPR

for every φ P Cc8pRq. Equivalently, µ is a strongly tempered measure and for some locally summable function a : R Ñ C we have µp|Cc8

“ ř

λPR apλqδλ.

We use the following definition for Fourier transform: φppξq “ ż

φpxqe´2πixξdx.

R

Perhaps the two most simple examples of FS-pairs are ż

φpptqdt “ φp0q pFourier Inversionq and ÿ

φppnq “ ÿ

φpnq pPoisson Summationq.

R

nPZ

nPZ

- Remark 1 (Real-Antipodal splitting). In the following we show that any FS-pair can be split into two real-antipodal FS-pairs. We say that a function a : R Ñ C is antipodal if ap´λq “ apλq for every λ P R. We say that an FS-pair pµ,aq if real-antipodal is µ is real-valued and ap¨q is (and must be) antipodal. Indeed, if we are given an arbitrary FS-


pair pµ,aq then we can write a1pλq “ apλq`2ap´λq, a2pλq “ ap´λ2q´i apλq, and so a “ a1 ´ ia2, with each aj antipodal, and we can write µ “ µ1 ´ iµ2, where µ1 “ Reµ and µ2 “ Imµ, and so each µj is real-valued. If φ P Cc8pRq is antipodal then φp is real, and if we further assume that either φ is real-valued or imaginary-valued, then from the identity

pa1pλq ´ ia2pλqqφpλq “ ż

φpptqdµ1ptq ´ iż

ÿ

φpptqdµ2ptq

R

R

λPR

ř

### λPR ajpλqφpλq is real, one deduces that

and the fact that

ajpλqφpλq “ ż

ÿ

φpptqdµjptq

R

λPR

for j “ 1,2. Since for any φ P Cc8pRq we have φ “ φ1 ´ iφ2 where each φj is antipodal, and each φj “ Reφj ´ iImφj, where Reφj is real and even and iImφj is imaginary and odd (hence both are antipodal as well), we deduce by linearity that pµj,ajq is a realantipodal FS-pair for j “ 1,2. As an example, note that

ř

nPZ inφppnq “ ř

### nPZ φpn ` 1{4q

### has the real-antipodal splitting

ÿ

- 1

- 2 ÿ


p´1qnφpp2nq “

pφpn ` 1{4q ` φpn ´ 1{4qq ÿ

nPZ

nPZ

- 1

- 2i ÿ


p´1qnφpp2n ` 1q “

pφppn ` 1{4q ´ φppn ´ 1{4qq.

nPZ

nPZ

### We say that a locally summable function a : R Ñ C has exponential growth if

ÿ

|apλq|e´c|λ| ă 8

λPR

for some c ą 0. We let C` “ tz “ x ` iy : y ą 0u. Following Besicovitch6 [10, Ch. 3], we say a holomorphic function f : C` Ñ C is almost periodic if for every 0 ă α ă β ă 8 and ε ą 0 there is a relatively dense7 set of ε-translations τ Ă R such that

|fpzq ´ fpz ` tq| ď ε

sup

αăIm zăβ

for every t P τ. We write f P APpC`q. If f P APpC`q it can be shown that

ż T`iy

- 1

- 2T


fpzqe´2πiλzdz

Efpλq :“ lim

TÑ8

´T`iy

exists for all λ P R and is independent of y ą 0 (see Section 4). It is straightforward to see that if instead fp¨ ` icq P APpC`q for some c ą 0, then the above limit exists and is independent of y ą c. If f P APpC`q we define the spectrum of f by

specpfq :“ tλ P R : Efpλq ‰ 0u,

and it can be shown that this set is at most countable. We say a holomorphic function g : C` Ñ C is of bounded type8 if there are two bounded holomorphic functions P,Q : C` Ñ C such that g “ P{Q. The following is the first main result of this paper.

- Theorem 1. Let pµ,aq be a real-antipodal FS-pair. Assume that degpµq ď 2 and that ap¨q has exponential growth. Then we have:


- (I) The limit fpzq “

- 1

- 2


ap0q ` lim

TÑ8

ÿ

0ăλăT

apλqp1 ´ λ{Tqe2πiλz (1)

converges uniformly in compact sets of C`;

- (II) There is c1 ą 0 such that fp¨ ` ic1q P APpC`q;


- 6Besicovitch considers the half-plane Rez ą 0 instead of Imz ą 0, so one has to mentally perform a rotation in order to use his results.
- 7A set τ Ă R is relatively dense if there exists l ą 0 such that px,x ` lq X τ ‰ H for every x P R. 8This is the same to say that log |gpzq| has a nonnegative harmonic majorant.


- (III) There are c2,B ą 0, with c2 ě c1, such that for any trigonometric polynomial

ppxq “ řN

n“1 pne2πiθ

nx, with tθnu Ă r0,8q, we have limsup

TÑ8 ˇ

- 1

- 2T


ż T

´T

fpx ` ic2qppxqdxˇ ď B max|pn|;

- (IV) exppfq is of bounded type.


Conversely, suppose f : C` Ñ C is a given holomorphic function such that items pIIq,pIIIq and pIVq hold true. Then there is c ě 0 such that the limit

ż T`iy

- 1

- 2T


fpzqe´2πiλzdz

Efpλq :“ lim

TÑ8

´T`iy

exists for every λ P R and y ą c, is independent of y, vanishes identically for λ ă 0 and defines a locally summable function with exponential growth such that

ÿ

|Efpλq|e´2πy|λ| ă 8

λPR

for every y ą c. Moreover, there is a unique real-valued locally finite measure µ of degree at most 2 satisfying

ż

dµptq pz ´ tqpw ´ tq

fpzq ` fpwq z ´ w “

- 1

- 2πi


### (2) for all w,z P C`. Furthermore, if we let

R

$ ’&

Efpλq if λ ą 0 2ReEfp0q if λ “ 0 Efp´λq if λ ă 0

apλq “

(3)

’%

then pµ,aq is an real-antipodal FS-pair and identity (1) holds.

The proof we give for Theorem 1 in the converse part actually shows a stronger result.

- Theorem 2. Let f : C` Ñ C be a holomorphic function such that properties pIIq and pIVq in Theorem 1 hold true, but also the following weaker version of property pIIIq:


(III˚) There is c2 ě c1, and for every M ą 0 there is BM ą 0, such that for any trigonometric polynomial ppxq “ řN n“1 pne2πiθ

nx, with tθnu Ă r0,Ms, we have limsup

ż T

- 1

- 2T


fpx ` ic2qppxqdxˇ ď BM max|pn|; Then there is c ě 0 such that the limit

TÑ8 ˇ

´T

ż T`iy

- 1

- 2T


fpzqe´2πiλzdz

Efpλq :“ lim

TÑ8

´T`iy

exists for every λ P R and y ą c, is independent of y, vanishes identically for λ ă 0 and defines a locally summable function. Moreover, there is a unique real-valued locally finite

measure µ of degree at most 2 satisfying (2), and if we define ap¨q as in (3) then pµ,aq is an real-antipodal FS-pair and identity (1) holds.

Note that condition (III˚) is equivalent to Efpλq being locally summable only, no growth required.

- Remark 2. We claim that if pµ,aq is an FS-pair such such that µ ě 0 and ap¨q has


exponential growth then degpµq ď 2. Indeed, let φ P Cc8pRq be even, 0 ď φ ď 1,

ş

φ “ φp0q “ 1 and supppφq Ă p´1,1q. Let φεpxq “ φpx{εq{ε and ψεpxq “ φppx{εq{ε for

0 ă ε ă 1. Let gpxq “ e´2πC|x|, with C ą 0 sufficiently large, and note gppξq “ πpC2C`ξ2q. We have ż

pgpφpεq ˚ ψεpt ´ t0qdµptq “ ÿ

apλqg ˚ φεpλqψpεpλqe´2πiλt

,

0

R

λPR

for any t0 P R. It is not hard to show that |g ˚ φεpλqψpεpλq| ď e´2πCp|λ|´1q. Thus, we conclude the right hand side above is uniformly bounded in absolute valued for 0 ă ε ă 1. Since µ ě 0 and pgpφpεq ˚ ψε Ñ gp pointwise, as ε Ñ 0, we can apply Fatou’s Lemma to deduce

ş C2`pdµtp´tqt0q2 ă C0, for some constant C0 ą 0 independent of t0. In particular we obtain that9

µprt0 ´ 1,t0 ` 1sq ď pC2 ` 1qC0.

sup

t0PR

3. Applications

We now apply Theorems 1 and 2 to classify crystalline pairs. Some of the results and proofs presented here would be better understood after reading Sections 4, 5 and 6. We say an entire function E is of Hermite-Biehler class if

|E˚pzq| ă |Epzq| for all z P C`, (4)

where E˚pzq “ Epzq. In this case we always write E “ A ´ iB, where A and B are real entire functions10 defined by A “ pE˚ ` Eq{2 and B “ pE˚ ´ Eq{p2iq, and we always write Θ “ E˚{E. In particular we have the following identity

1 ` Θ 1 ´ Θ

- A

- B “


. (5)

i

Note that both A and B have only real zeros. We denote by φ “ φE a phase function associated to E. This is characterized by the condition eiφpxqEpxq P R for all real x (φ is

unique modulo an integer multiple of π). For instance, one could take φ “ 21i log Θ after branch cutting all zeros and poles of Θ by vertical semi-lines. It is not hard to show that

E1pxq Epxq

φ1pxq “ Rei

“ By log Θpx ` iyq|y“0 ą 0,

9Hence µ is translation-bounded. 10Entire functions which attain only real values on the real line.

for all real x, and so φpxq is an increasing function of real x. We also have that e2iφpxq “

Apxq2 |Epxq|2

Bpxq2 |Epxq|2

ApxqBpxq |Epxq|2

´

` 2i

,

for all real x. As a consequence, the points γ P R such that φpγq ” 0pmod πq coincide with the real zeros of B{E and the points s P R such that φpsq ” π{2pmod πq coincide with the real zeros of A{E and, because φ1 ą 0, these zeros are simple. In particular, A{B has only simple real zeros and simple real poles, which interlace, and

1 φ1jpγq

tγ P R : φjpγq ” 0pmodπqu “ ZerospBj{Ajq and

“ Res

pAj{Bjq ą 0.

z“γ

Moreover, if E has no real zeros then A and B have only real simple zeros which interlace11. The next result characterizes FS-pairs pµ,aq for which µ ě 0 has locally finite support.

- Theorem 3. Let E “ A ´ iB be of Hermite-Biehler class such that A{B P APpC`q and λ P R ÞÑ EpA{Bqpλq is locally summable. Let


ż T`i

Apzq Bpzq

1 T

e´2πiλzdz pfor λ ą 0q,

apλq “ ap´λq “ EpiA{Bqpλq “ lim

i

TÑ8

´T`i

ż T`i

Apzq Bpzq

- 1

- 2


1 T

ap0q “ ReEpiA{Bqp0q “ Re lim

i

dz,

(6)

TÑ8

´T`i

µ “ 2π ÿ

1 φ1Epγq

δγ.

φEpγq”0 pmod πq

Then pµ,aq is a real-antipodal FS-pair such that µ ě 0 and µ has locally finite support12. Conversely, if pµ,aq is a real-antipodal FS-pair such that µ ě 0, supppµq is locally finite and ap¨q has exponential growth, then pµ,aq has to be built from the construction above.

- Remark 3. Observe that by Lemma 12(iii),(iv),(v) and identity (5), A{B P APpC`q if and only if Θ “ E˚{E P APpC`q and A{B has locally finite spectrum if and only if Θ has. Note also that if E,E˚ P APpC`q then Θ P APpC`q. In particular, if E is a trigonometric polynomial of Hermite-Biehler class, then iA{B belongs to APpC`q and has locally finite spectrum, hence Theorem 3 applies and the pair pµ,aq is crystalline.
- Remark 4 (The Kurasov & Sarnak construction). Theorem 3 generalizes a construction of Kurasov & Sarnak [26]. They construct a crystalline FS-pair pµ,aq by letting


µ “ ÿ

mpγqδγ,

Qpγq“0

where Q is any given trigonometric polynomial with only real zeros γ and multiplicities mpγq. Theorem 3 majorates this construction. Indeed, since Q has finite exponential

11For more on this we recommend [13] and the introduction of [21]. 12A set S Ă R is locally finite if #pS X pa,bqq ă 8 for any a ă b.

type, Hadamard’s factorization implies that Qpzq “ znec

ź

1z`c2

p1 ´ z{γqez{γ

γ‰0

for some c1,c2 P C and n ě 0, where the γ1s are the real zeros of Q. In particular e´c

2´izImc1Q is a real entire trigonometric polynomial, so we can assume that Q is real on the real line. If that is the case then c1 P R and

“ ÿ

Q1pzq Qpzq

### y

px ´ γq2 ` y2 ą 0.

Rei

γ

We obtain that E “ Q1 ´ iQ is a trigonometric polynomial of Hermite-Biehler class by a routine calculation. By the previous remark, Theorem 3 applies. It is also easy to see that the zeros of Q coincide with the points γ P R such that φEpγq ” 0pmodπq and φ1Epγq´1 “ Resz“γ pA{Bq “ mpγq. Thus, by Theorem 3 (with ap¨q as in (6)), both µ and ap¨q have locally finite support, and so pµ,aq is crystalline. A simple example is given by the Hermite-Biehler trigonometric polynomial

Epzq “ 12ppπ ` 1qe´πiz ` eiz ` pπ ´ 1qeπizq “ π cospπzq ` 12 cospzq ´ ipsinpπzq ` 12 sinpzqq, which produces the crystalline measure µ “ řsinpπγq`

sinpγq“0 δγ.

1 2

- Remark 5 (The Ulanovskii & Oleveskii result). We now explain how one can prove the main result of Ulanovskii & Oleveskii [40] using Theorem 3, but under milder decay conditions. We claim that if pµ,aq is an FS-pair such µ ě 0 is N-valued, ap¨q has locally finite support and exponential growth then the Hermite-Biehler function E “ A ´ iB given by Theorem 3 is a trigonometric polynomial, and so the construction from Remark


- 4 applies. Indeed, since degpµq ď 2 one can take B to have the same zeros of B, but with multiplicities given by the weights of µ. We can take such B with orderpBq ď 1 by [32, Thm. 6, p. 16]. Using (2) we conclude that ReiB1{B “ ReA{B in C`, and so Poisson representation shows that A{B “ B1{B ` h for some h P R, hence we can assume that A “ B1. Since ap¨q has locally finite support, then B1{B has locally finite spectrum contained in r0,8q. Lemma 13 shows that B P APpC`q and it has locally finite spectrum bounded from below. The class APpC`q is closed under differentiation, and so


- B1 P APpC`q, and therefore, E P APpC`q, both with locally finite spectrum bounded from below. Note that B1 also has order ď 1, and so E has order ď 1. We can then apply Lemma 17 to conclude that E is a trigonometric polynomial.


- Proof of Theorem 3. Let f “ iA{B. Since E “ A ´ iB is Hermite-Biehler, we obtain that Ref ą 0 in C`, and so |e´f| ă 1 in C`, hence ef is of bounded type. Moreover, Efpλq is locally summable by hypothesis. We conclude that Theorem 2 applies. Poisson representation [13, Thm. 4 & Prob. 89] for f implies that µ has the form given by


(6). Conversely, if pµ,aq is a real-antipodal FS-pair such that µ ě 0, supppµq is locally finite and ap¨q has exponential growth, then we can apply Theorem 4 to obtain that

(6) holds for some Hermite-Biehler function E “ A ´ iB such that Apz ` icq{Bpz ` icq belongs to APpC`q for some c ą 0. However, Lemma 12 also shows that Θpz ` icq “ E˚pz ` icq{Epz ` icq belongs to APpC`q, and since |Θ| ă 1 in C`, Lemma 11 shows that Θ P APpC`q and, by Lemma 12 again we obtain that A{B P APpC`q. Since apλq is locally summable and apλq “ Efpλq for λ ą 0, then Efpλq is locally summable. □

The next result classifies FS-pairs pµ,aq for which µ has locally finite support.

- Theorem 4. Let pµ,aq be an FS-pair such that µ has locally finite support, degpµq ď 2 and ap¨q has exponential growth. Then there exists four Hermite-Biehler functions Ej “ Aj ´ iBj and numbers pj P t0,1u, for j “ 1,2,3,4, such that if we let f “ ip1A1{B1 ´ ip2A2{B2 and g “ ip3A3{B3 ´ ip4A4{B4 then fp¨ ` icq and gp¨ ` icq belong to APpC`q for some c ą 0, Efpλq and Egpλq are locally summable, and:


δγ ´ p2 ÿ

µ “ p1 ÿ

- 1

- 2π


1 φ12pγq

1 φ11pγq

## δγ

φ2pγq”0 pmod πq

φ1pγq”0 pmod πq

´ ip3 ÿ

δγ ` ip4 ÿ

1 φ13pγq

1 φ14pγq

δγ;

(7)

φ3pγq”0 pmod πq

φ4pγq”0 pmod πq

apλq “ Efpλq ´ iEgpλq and ap´λq “ Efpλq ` iEgpλq pfor λ ą 0q;

- 1

- 2ap0q “ ReEfp0q ´ iReEgp0q,


where φj is the phase function associated with Ej. Moreover: (i) µ ě 0 if and only if p1 “ 1 and p2 “ p3 “ p4 “ 0; (ii) ap¨q has locally finite support if and only if f and g have locally finite spectrum. Furthermore, if µ is N-valued then we can take A1 “ B11.

- Proof of Theorem 4. By real-antipodal splitting we can assume that µ is real-valued (so p3 “ p4 “ 0). We can then apply Theorem 1 and obtain that


ż

ÿ

1 ` tz t ´ z

ap0q 2 ` lim

dµptq 1 ` t2

- 1

- 2πi


p1 ´ λ{Tqapλqe2πiλz “ ih `

fpzq “

,

TÑ8

R

0ăλăT

for some h P R, where f is holomorphic in C` and fp¨ ` icq P APpC`q for some c ą 0. Let µ “ ř

γPΛ rpγqδγ where Λ Ă R is locally finite and rpγq “ r1pγq ´ r2pγq, with rj ě 0. Let

ż

1 ` tz t ´ z

dµjptq 1 ` t2

- 1

- 2πi


fjpzq “

R

for j “ 1,2, where µj “ ř

γPΛ rjpγqδγ. Observe that each fj is meromorphic in C with only simple poles (possibly) at Λ. Since µj ě 0 we have ifjpC`q Ă C` Y t0u, and we can then apply a classical result [32, p. 308, Thm. 1] to deduce this happens exactly when there are two real entire functions Aj and Bj with only real zeros that interlace and such that ifj “ ´pjAj{Bj, with pj P t0,1u to account for the case when µj “ 0 for some j “ 0,1. Since ReiAj{Bj ą 0, we deduce that Ej “ Aj ´ iBj is of Hermite-Biehler

class, and so, Poisson representation shows that µ “ 2πp1 ÿ

δγ ´ 2πp2 ÿ

1 φ12pγq

1 φ11pγq

δγ.

φ2pγq”0 pmod πq

φ1pγq”0 pmod πq

Noting that f “ f1 ´ f2 ` ih, we obtain f1p¨ ` icq ´ f2p¨ ` icq P APpC`q, and since ap¨q has exponential growth we conclude that apλq “ Epf1 ´ f2qpλq for λ ą 0 and 21ap0q “ ReEpf1´f2qp0q. If µ ě 0 then pp1,p2q “ p1,0q. Also, ap¨q has locally finite support if and only if f1´f2 has locally finite spectrum. Finally, if µ is N valued then, since degpµq ď 2, one might take B to have zeros exactly at support of µ with multiplicity determined by the weights of µ and order at most 1. In particular, Hadamard factorization and logdifferentiation show that ReiB1{B “ ReiA1{B1 and so f1 “ ih ` iB1{B, and E “ B1 ´ iB is now Hermite-Biehler. □

- Remark 6. We note that it follows from Theorems 1 and 2 that Theorem 4 is sharp. That is, if we are given four Hermite-Biehler functions Ej “ Aj ´iBj and numbers pj P t0,1u, for j “ 1,2,3,4, such that f “ ip1A1{B1´ip2A2{B2 and g “ ip3A3{B3´ip4A4{B4 belong to APpC`icq for some c ą 0, then the pair pµ,aq defined by (7) is an FS-pair. A crucial instantiation of Theorem 4 is the difference of two prime summation formula of Guinand, explained of Section 8.5. It can be obtained from our results in the following way. Let


χ1 and χ2 be two primitive and even Dirichlet characters of distinct modulus N1 and N2, and let

Lpχj,sq “ ÿ

χjpnqn´s

ně1

be their associated L-functions for j “ 1,2 and Res ą 1. One can attach to each of them the function

Bjpzq “ χpjp1q´1{2pNj{πq´iz{2Γp1{4 ´ iz{2qLpχj,1{2 ´ izq for complex z, where χpjp1q “ Nj´1{2

řN

n“1 χpjqe2πin{N P t˘1,˘1u. Thanks to their functional equations, it can be shown that Bj is real on the real line, this is, Bjpzq “ Bjpzq, and that each Bj is an entire function of order ď 1. Assuming the Riemann Hypothesis for both L-functions, each Bj have only real zeros and those coincide (with multiplicity) with the ordinates of the nontrivial zeros of each L-function. We now let Ej “ Aj ´ iBj, with Aj “ Bj1. Hadamard’s factorization shows that ReiAj{Bj ě 0 in C` and so each Ej is a Hermite-Biehler function. Now observe that

L1pχ1,1{2 ´ izq Lpχ1,1{2 ´ izq

L1pχ2,1{2 ´ izq Lpχ2,1{2 ´ izq

A1 B1 ´ i

- A2

- B2 “


- 1

- 2


logpN1{N2q `

´

i

logpN1{N2q ` ÿ

Λpnqpχ1pnq ´ χ2pnqq ?n

logpnq 2π

- 1

- 2


z

e2πi

“

ně2

B1 ´iA

when Imz ą 1{2, where Λpnq is the von Mongoldt function. It follows that f “ iA

2 B2

1

is almost periodic in C` ` i{2. The previous results show that the pair µ “ 2πˆ ÿ

˙

1 ´ ÿ

δγ

## δγ

2

Lpχ1,1{2`iγ1q“0

Lpχ2,1{2`iγ2q“0

„pχ1pnq ´ χ2pnqq1logpnq

ȷ

a “ logpN1{N2q10 ` ÿ

Λpnq ?n

` pχ1pnq ´ χ2pnqq1

logpnq 2π

´

ně2

2π

is a FS-pair (above, 1cpλq “ 1 if λ “ c and 1cpλq “ 0 otherwise).

In what follows we say that an entire function E is of P´olya class if E has no zeros in C`, |E˚{E| ď 1 in C` and y ÞÑ |Epx ` iyq| is nondecreasing for y ą 0. A classical result [13, Thm. 7] states that a function E is of Po´lya class if and only if

ź

Epzq “ Eprqp0qpzr{r!qe´dz

2´ibz

p1 ´ z{znqezRe 1{z

,

n

n

where d ě 0, Reb ě 0, tzn “ xn ´ iynu are the nonzero zeros of E (with yn ě 0) and

ÿ

1 ` yn x2n ` yn2 ă 8.

n

The Po´lya class can be also defined as functions that are uniform limits in compact sets of polynomials with no zeros in C` (see [13, Problem 12]). Moreover, any function of Po´lya class has order at most 2 ([13, Problem 10]).

The next result is a brand new classification theorem13 for nonnegative crystalline measures. It generalizes a result of Olevekii & Ulanovskii [40] in the uniformly discrete case, dropping the N-valuedness assumption.

- Theorem 5. Let pµ,aq be an FS-pair. Assume that:


- (1) µ has uniformly discrete support and there is δ ą 0 such that µptxuq ě δ for all x P supppµq;
- (2) There is b ą 0 such that supppaq X p0,bq “ H and ap¨q has exponential growth.


Then there exists an entire function E “ A ´ iB of Hermite-Biehler class and of finite exponential type such that E,E˚ P APpC`q (and so A{B P APpC`q), specpEq is bounded and (6) holds. If in addition supppaq is locally finite, then E is a trigonometric polynomial and Remark 4 applies.

Proof. Step 1. We first apply Theorem 3 to conclude there is an Hermite-Biehler function

- E “ A ´ iB such that A{B P APpC`q and (6) holds. We can assume that E has no real zeros as these can be removed (with a Weierstrass product) without altering A{B or the fact that E is Hermite-Biehler. In particular, supppµq “ tγ P R : φpγq ” 0pmodπqu “ ZerospBq, where φ is the phase function associated with E, and these zeros are all simple. The zeros of A are also simple and interlace those of B. Since µ is bounded from below


- 13In a way, this is the most technically hard result of the paper.


on its support and ap¨q has exponential growth, we can apply Remark 2 to obtain c ă φ1pγq ă 1{c, for some 0 ă c ă 1, whenever Bpγq “ 0. In particular, we have

ř

1`γ2 ă 8 and, since the zeros of A interlace those of B, we also have

1

Bpγq“0

ř

1`s2 ă 8. We claim that we can assume E is has order at most 1. Indeed, define the canonical products

1

Apsq“0

Bpzq “ bzp ź

p1 ´ z{γqez{γ and Apzq “ zq ź

p1 ´ z{sqez{s,

Bpγq“0, γ‰0

Apsq“0, s‰0

for some p,q P t0,1u, where b P R is chosen so that pApzq{Bpzqq{pApzq{Bpzqq “ 1 ` Opzq for z Ñ 0. Hence both A and B have order at most 1 by a classical result of Borel [32, Thm. 6, p. 16]. Since ReiA{B ě 0 in C` and, a straitfoward computation, shows that ReiA{B ě 0 in C`, we conclude that both A{B and A{B are of bounded type and so

- F “ pA{Bq{pA{Bq also is and has no zeros. Since F “ F˚, a classical result of Krein [25] (see also [33, Thm. 1, p. 115]) shows that F is of exponential type, and so Fpzq “ ehz, for some h P R. Since F is of bounded type we have h “ 0. We can then define Er “ A ´ iB to finish the claim.


Step 2. Let tzn “ xn ´ iynu be the zeros of E with yn ą 0. We claim supn yn ă 8 and that E is of Po´yla class. Indeed, since f “ iA{B P APpC`q, by Remark 3 we have Θ “ E˚{E “ p1 ´ fq{p1 ` fq P APpC`q. Since specpfq Ă r0,8q, a simple computation using Lemma 12(i) shows EΘp0q “ 11´`EEffpp00qq. However, 2ReEfp0q “ ap0q ą 0 (because µ ě 0), thus |EΘp0q| ă 1. Assume now EΘp0q ‰ 0. Then Lemma 12(i) shows straightforwardly that Θpx ` iyq has no zeros for large y ą 0. Assume otherwise that EΘp0q “ 0, that is, Efp0q “ 1. Since apλq “ Efpλq for λ ą 0 we deduce that specpfq Ă t0u Y rb,8q where b “ inftλ ą 0 : apλq ‰ 0u ą 0 by assumption. Since f has no zeros in C`, we can then apply Lemma 12(ii) to conclude that b P specpfq. Writing f “ 1 ´ 2g, with specpgq Ă rb,8q and Egpbq ‰ 0, we can apply Lemma 12(i) to conclude that |gpx`iyq| ă 1 for large y ą 0, and so

“ ÿ

gpzq 1 ´ gpzq

gpzqn,

Θpzq “

ně1

hence specpΘq Ă rb,8q and EΘpbq ‰ 0. We can then apply again Lemma 12(i) to conclude that limyÑ8 supx |e´2πibpx`iyqΘpx ` iyq ´ EΘpbq| “ 0, hence Θpzq has no zeros for large Imz. Finally, since E has order at most 1 the following sum is now finite

ÿ

1 ` yn

x2n ` yn2 ă 8. and E has the following factorization

n

Epzq “ Ep0qe´ihz ź

p1 ´ z{znqezRe 1{z

n

n

### for some h ě 0. Hence E is of P´oyla class.

Step 3. We claim now that supxPR φ1pxq ă 8. Since (2) holds true for f “ iA{B, we obtain that

“ ÿ

BpzqBpwq pγ ´ zqpγ ´ wq for all z,w P C. A routine computation shows that

BpzqApwq ´ BpwqApzq πpz ´ wq

1 πφ1pγq

Kpw,zq :“

Bpγq“0

“ ÿ

E1pxq Epxq

sin2 φpxq φ1pγqpγ ´ xq2

πKpx,xq |Epxq|2

φ1pxq “ Rei

“

.

Bpγq“0

Enumerate the ZerospBq “ tγnu and let c ą 0 be so small that γn`1 ´ γn ě c for all n. Let 0 ă ε ă c{10 to be chosen later. Observe first that if distpx,tγnuq “ |x´γ| ě ε (with γ “ γn

) then |x ´ γn

0`k| ě ε ` |k|c{2, and so φ1pxq ď 2 ÿ

0

1 cpε ` kc{2q2

“ Opε´2q.

kě0

On the other hand, if distpx,tγnuq “ |x ´ γ| ď ε, then |γn

0`k ´ x| ě 2c|k|, for k ‰ 0, and φ1pγqφ1pxq ď

sin2 φpxq pγ ´ xq2

` C sin2 φpxq

for some C ą 0, independent of ε and γ. Using the inequality x2 ě sin2 x for all real x, and factoring sin2 φpxq, we obtain

φ1pγqφ1pxq sin2 φpxq

pπ{cq2 sin2rpγ ´ xqπ{cs

` C We conclude that the function

ď

π c

ξpxq “ φ1pγqcotφpxq ´

cotrπpx ´ γq{cs ` Cpx ´ γq,

which is analytic in a complex neighbourhood of the segment I “ rγ ´ ε,γ ` εs, is nondecreasing for x P I and ξpγq “ 0. We conclude that

πpx ´ γq c

px ´ γqφ1pγqcotφpxq ě

cotrπpx ´ γq{cs ´ Cpx ´ γq2

for x P I. Since the function πpxc´γq cotrπpx ´ γq{cs has value 1 for x “ γ, there is ε0 “ ε0pc,Cq ą 0, with 0 ă ε0 ă c{10, such that the right hand side above is bounded

from below by πpx2´cγq cotrπpx ´ γq{cs for x P I0 :“ pγ ´ ε0,γ ` ε0q, and so

πpx ´ γq 2c

px ´ γqφ1pγqcotφpxq ě

cotrπpx ´ γq{cs

for x P I0. We now select ε “ ε0. Observing the right hand side above is positive for x P I0, we can square both sides above, factor out px ´ γq2, lower bound φ1pγq ě c and isolate sin2 φ to obtain

1 1 ` C cot2rπpx ´ γq{cs

sin2 φpxq ď

### for C “ π2{p4c4q. Note also that for x P I0 we have |x ´ γn

0 ´ kc| for any k P Z, hence

0`k| ě |x ´ γn

1 c ÿ

sin2 φpxq sin2rπpx ´ γq{cs ď

sin2 φpxq px ´ γ ` kcq2

π2 c3

φ1pxq ď

“

kPZ

π2 c3

π2 c3

1 sin2rπpx ´ γq{cs ` C cos2rπpx ´ γq{cs

ď

.

for x P I0. This proves the claim.

Step 4. We claim the zeros of E are separated from the real axis, that is, there is c ą 0 such that yn ě c for all n. Indeed, observe that since Epzqeiφpzq “ E˚pzqe´iφpzq whenever φpzq is defined (any neighborhood of R not containing tznunPZ Y tznunPZ) we obtain that

Θ1pzq Θpzq

1 2i

1 2i

φ1pzq “ Bz

log Θpzq “

, with Θ “ E˚{E. Using the factorization of E we obtain

Θpzq “ e2ihz ź

1 ´ z{zn 1 ´ z{zn

,

nPZ

and so

φ1pxq “ h ` ÿ

yn |x ´ zn|2

nPZ

for real x. Hence φ1pxnq ě 1{yn, and since φ1pxq is bounded, the claim follows.

Step 5. We claim that φ1 P APpRq and specpφ1q Ă rb,8q. Let c ą 0 be small enough such that Θ has no zeros or poles in the strip S “ t´c ă Imz ă cu. First we show that Θ is bounded in every horizontal strip contained in S. We only need to show this for z P S with Imz ď 0. Indeed, since

- 1

- 2By log |Θ˚px ` iyq| “ h ` ÿ


ynrpx ´ xnq2 ` yn2 ´ y2s |z ´ zn|2|z ´ zn|2 and yn2 ´ y2 ď 3pyn ´ yq2 for 0 ď y ď c, we deduce that

nPZ

- 1

- 2By log |Θ˚px ` iyq| ď h ` 3 ÿ


yn |x ´ zn|2

ď 3φ1pxq ď C

nPZ

for some C ą 0. Since log |Θ˚pxq| “ 0, integration shows that Θ˚px ` iyq ď e2Cy for 0 ď y ď c. Since Θ P APpC`q, we can now apply Lemma 11 to deduce that Θp¨ ´ icq P APpC`q and Θ1p¨ ´ icq P APpC`q. By Lemma 12(iv), we get that |Θ| is bounded away from zero in every horizontal strip contained in S. We deduce that Θ1{Θ P APpRq, and so14 φ1 P APpRq. Step 1 shows that specpΘq Ă t0u Y rb,8q and EΘpbq ‰ 0, hence specpΘ1{Θq Ă rb,8q and specpφ1q Ă rb,8q.

- 14If we let APpSq be defined in the same way as in APpC`q, but considering only horizontal strips strictly contained in S, we have showed that φ1 P APpSq.


Step 6. Since E is of Po´lya class we have ReiE1{E ě 0 in C`, and Poisson representation guarantees that

ż

iE1pzq Epzq

φ1ptqdt 1 ` t2

1 ` tz t ´ z

1 πi

“ id ´ ipz `

,

R

for some d P R and p ě 0, where degpφ1ptqdtq ď 2. This fact, in conjunction with the factorization of E shows that

ż

px ´ tq2 ` y2 “ h ` ÿ

φ1ptqdt

iE1pzq Epzq

y ` yn px ´ xnq2 ` py ` ynq2

y π

“ py `

.

Re

R

n

ř

1piyq

1`yn

x2n`yn2 ă 8, we conclude that p “ limyÑ8 Re iE

yEpiyq “ 0. We can apply Lemma 16 so deduce that iE1{E P APpC`q and specpiE1{Eq Ă t0uYrb,8q. We can apply Lemma 13 to conclude that E P APpC`q and that specpEq is bounded from below. Since E˚ “ ΘE, we conclude that E˚ P APpC`q also and that specpE˚q is bounded from below. Finally, we can use Lemma 17 to deduce the spectrum of E (and of E˚) is bounded and E is of exponential type. To finish, if in addition supppaq is locally finite, then so is specpA{Bq. Since ap¨q has exponential growth, we obtain that Θ has locally finite spectrum, thus so φ1 has locally finite spectrum. The previous applications of Lemmas 16 and 13 (and their content) show that E has locally finite spectrum as well, and so Lemma 17 shows that E is a trigonometric polynomial. □

Since

n

We believe that Theorem 5 should still hold only assuming that supppµq is locally finite. Note that by Remark 2, supppµq is contained in a finite union of uniformly discrete sets. Also, the uniformly discreteness of supppµq plays a role only in Step 3 above, where we show φ1 is bounded as a stepping stone to show the zeros of E cannot get close to the real axis. Note that if φ1 is bounded then supppµq is uniformly discrete. However, we still think there must be a way to circumvent this issue, and nevertheless conclude that the zeros of E are separated from the real axis. Unfortunately we were not able to come up with such maneuver, despite many efforts.

- Remark 7. We now construct one example of an FS-pair pµ,aq satisfying the conclusion of Theorem 5 for which E is not a trigonometric polynomial. We let E “ B1 ´ iB where


ÿ8

10´n sinpπp1 ´ 2θnqzq,

Bpzq “

n“0

where θ0 “ 0 and tθnuně1 Ă p0,1{2q is a sequence of irrational numbers such that t1,θ1,...,θku is independent over Z for each k ě 0. Assume also that θ1 “ infně1 θn. Note that B is well-defined entire function and almost periodic in C since its series converges uniformly in any horizontal strip. Also note that B is of exponential type at most π. In order to show that E is Hermite-Biehler we only need to verify that B has only real zeros. Consider the box QM “ r´M ´1{2,M `1{2s`ir´M ´1{2,M `1{2s, for M ě 0.

Then function sinpπzq has exactly 2M ` 1 simple real zeros in this box. Since,

|sinpzq|2 “ coshpyq2 sinpxq2 ` sinhpyq2 cospxq2 ď e2|y|,

ř8

n“2 10´n sinpπσnzqˇ on the boundary of QM. Rouche’s Theorem implies that Bpzq has the same number of zeros in QM as sinpπzq for large M, which equals 2M ` 1. However, |Bpn ` 1{2q ´ p´1qn| ď 19 for all n P Z, and so B has only real simple zeros, with exactly one zero in each interval pn ´ 1{2,n ` 1{2q for all n. Also note that

it is not hard to show that |sinpπzq| ą ˇ

specpiB1{Bq “ tk1θ1 ` ... ` klθl ` m1p1 ´ θ1q ` ... ` mlp1 ´ θlq : kj,mj ě 0u,

and so specpiB1{Bq X p0,θ1q “ H. Moreover, by construction, each λ P specpiB1{Bq has a uniquely associated pair of vectors pk1,....,klq and pm1,...,mlq such that λ “ k1θ1 `...` klθl ` m1p1 ´ θ1q ` ... ` mlp1 ´ θlq. We obtain that

EpiB1{Bqpλq “ 10´pk

1`m1`...`kl`mlq ě 10´λ{θ

. Since iB1{B P APpC`q we obtain that

1

ÿ

e4πT ÿ

|EpiB1{Bqpλq| ď 10T{θ

|EpiB1{Bqpλq|2e´4πλ “ 10T{θ

e4πTEr|B1{Bp¨`iq|2s ă 8.

1

1

0ďλăT

λPR

Hence λ ÞÑ EpiB1{Bqpλq is locally summable. We conclude that if we define the FS-pair pµ,aq as in (6) (with A “ B1) then

µ “ 2π ÿ

## δγ

Bpγq“0

has uniformly discrete support and its Fourier transform is supported in ˘specpiB1{Bq. Hence it satisfies the conclusion of Theorem 5, but E is not a trigonometric polynomial. Finally, let K0 “ specpiB1{Bq and Kp “ Kp1´1 for p ě 1, where Kp1´1 is the set of accumulation points of Kp. Assume now that limθn “ 1{2. It is then simple to deduce, by the description of K0, that Kp “ K0 ` 21tp,p ` 1,p ` 2,...u, and so the support of µp is not dense in any interval.

3.1. de Branges spaces - a Hilbert space interpretation of FS-pairs. A de Branges space [13] (see also the introduction of [21]) is a Hilbert space pH,}¨}q of entire functions F : C Ñ C satisfying:

- (H1) If F P H and Fpwq “ 0 for some w P C, then Gpzq “ Fpzqzz´´ww belongs to H and }G} “ }F};

- (H2) The functional F P H ÞÑ Fpwq is continuous for every w P C;
- (H3) If F P H then F˚ P H and }F˚} “ }F}.


Because of (H2), the space H comes equipped with an unique reproducing kernel Kpw,zq, that is, Fpwq “ xF,Kpw,¨qy for any w P C and F P H. De Branges proved [13, Thm. 23] that for any such Hilbert space H there exists an Hermite-Biehler function E such

that H “ HpEq isometrically, where HpEq is the Hilbert space of entire functions F such that15

ż

2

Fpx ` iyq Epx ` i|y|qˇ

}F}2 :“ sup

dx ă 8,

ˇ

yPR

R

in which case the sup above is attained at y “ 0. De Branges also shows [13, Thm. 19] that any such space HpEq is a Hilbert space that satisfies the above axioms. When we identify H “ HpEq for some Hermite-Biehler function E “ A ´ iB we have

EpzqEpwq ´ E˚pzqEpwq 2πipw ´ zq

BpzqApwq ´ BpwqApzq πpz ´ wq

“

Kpw,zq “

(8) and

Fpwq “ ż

FptqKpw,tq |Eptq|2

dt

R

for every w P C and F P H. The function E realizing H “ HpEq is not unique. Indeed, if HpEq “ HpE1q isometrically, one can then apply [13, Problem 69] (for S “ A1 and S “ B1) to obtain

eiβ a1 ´ |p|2

pEpzq ´ pE˚pzqq

E1pzq “

for some β P R and p P C, with |p| ă 1. Conversely, a routine computation shows that any E1 defined in the above way satisfies (8), and since 0 ă Kpz,zq “ p4πyq´1p|E1pzq|2 ´ |E1˚pzq|2q for z P C`, we conclude that E1 is Hermite-Biehler, and so HpEq “ HpE1q isometrically. Moreover, their theta functions are related by the Mo¨bius transformation

Θpzq ´ p 1 ´ Θpzqp

Θ1pzq “ e2iβ

.

A major result [13, Thm. 22] is that, for any α P r0,πq, the set tKpγ,zquφpγq”αpmod πq is orthogonal in HpEq, and its orthogonal complement is one-dimensional and spanned by eiαE ´ e´iαE˚. In particular, if α “ 0 and E has no real zeros, and B R HpEq, then representation of functions in the basis tKpγ,zquBpγq“0 implies the identities

BpzqApwq ´ BpwqApzq z ´ w “ ÿ

BpzqBpwq pγ ´ zqpγ ´ wq and

1 φ1pγq

πKpw,zq :“

Bpγq“0

Fpzq “ ÿ

FpγqBpzq B1pγqpz ´ γq

, for any F P HpEq,

Bpγq“0

with convergence in HpEq and uniformly (and absolutely) in compact sets of C. Letting f “ iA{B, if one divides the expansion of K above by iBpzqBpwq we get

ż

fpzq ` fpwq z ´ w “

dµptq pt ´ zqpt ´ wq

- 1

- 2πi


R

- 15The original definition involves bounded type theory, but this is an equivalent short definition, see [21].


with µ “ ř

φ1pγqδγ. Assume now that f “ iA{B P APpC`q and that Efp¨q is locally summable. Thus, Theorem 3 applies and pµ,aq is a FS-pair (with ap¨q as in (6)). There is no particular reason (other than convenience) to take α “ 0 here. One could select as well any α P r0,πq, but now the FS-pair would be16

2π

Bpγq“0

µ “ ÿ

2π φ1pγq

δγ,

φpγq”α pmod πq

apλq “ ap´λq “ Efpλq pλ ą 0q ap0q “ 2ReEfp0q,

assuming f “ p1 ` e´2iαΘq{p1 ´ e´2iαΘq P APpC`q (note if Eα “ eiαE “ Aα ´ iBα then f “ iAα{Bα).

One could ask the question whether there is another natural axiom, as the ones above, that would force the space H to “produce” an FS-pair. Such axiom indeed exists. Proposition 6. Let pH,} ¨ }q be a Hilbert space of entire functions satisfying (H1), (H2) and (H3), with reproducing kernel Kpw,zq. Assume also that:

(H4) There is α P C` such that the function fpzq “

pα ´ zqKpα,zq ´ pα ´ zqKpα,zq pα ´ zqKpα,zq ` pα ´ zqKpα,zq

belongs to APpC`q and Efp¨q is locally summable. Then there is an Hermite-Biehler function E “ A´iB such that H “ HpEq isometrically, and, if we define µ and ap¨q as in (6), we have that pµ,aq is a FS-pair.

Proof. We can then apply [13, Thm. 23, p. 58] to obtain that the identity pKpw,zq ´ Kpβ,zqKpβ,βq´1Kpw,βqqpz ´ βq

pKpw,zq ´ Kpβ,zqKpβ,βq´1Kpw,βqqpw ´ βq w ´ β holds for all w,z P C and β P C`. Let Lpw,zq “ 2πipw ´ zqKpw,zq and

z ´ β “

E1pzq “ Lpα,αq´1{2Lpα,zq. A routine computation, using the above identity, now shows that

E1pzqE1pwq ´ E1˚pzqE1pwq 2πipw ´ zq

Kpw,zq “

.

Since 0 ă Kpz,zq for z P C`, we conclude that E1 is of Hermite-Biehler class, thus H “ HpE1q isometrically. Letting E1 “ A1 ´ iB1 and noting that Lpα,zq˚ “ ´Lpα,zq, we deduce that

˚

1 ` Lpα,zq

### 1 ` Θ1pzq 1 ´ Θ1pzq

- A1pzq

- B1pzq


Lpα,zq

fpzq “

“

“ i

.

˚

1 ´ Lpα,zq

Lpα,zq

We can then apply Theorem 3 to finish the proof. □

- 16The proof of Theorem 1 implies that peiαE ´ e´iαE˚q R HpEq


4. Almost Periodic Functions in R

We say that a continuous function f : R Ñ C in almost periodic (in the sense of Bohr [16]) if for every ε ą 0 the following set is relatively dense

τεpfq :“ tt P R : sup

|fpxq ´ fpx ` tq| ď εu.

xPR

This set is called the set of ε-translations for f. We denote by APpRq the set of continuous almost period functions f : R Ñ C. It is not hard to show that any f P APpRq is bounded and uniformly continuous, and that τεpfq is also closed with non-empty interior. The following is a very useful criteria for almost periodicity (see [3, p. 7]). In what follows CpRq denotes the usual Banach algebra of bounded continuous functions with the topology induced by the sup-norm }f}8 “ supxPR |fpxq|.

In the remaining part of this section we compile necessary facts about almost periodic functions and we provide some proofs for completeness. Theorem 7 (Bochner’s criterion). Let f : R Ñ C be continuous. Then f P APpRq if and only if the set of functions tfp¨ ` hquhPR is pre-compact in CpRq.

- Remark 8. Bochner’s criterion works also for functions f : R Ñ Cn. In particular, if fj P APpRq for j “ 1,...,N, then XNj“1τεpfjq is nonempty and relatively dense.


It is now straightforward to show that APpRq closed under multiplication, addition and uniform convergence, hence APpRq is a closed subalgebra of CpRq. Moreover, it also follows that for every continuous g : C Ñ C we have g ˝ f P APpRq whenever f P APpRq. Since exponentials e2πixλ, with λ P R, are periodic, we conclude by Bochner’s criterion that any trigonometric polynomial

ÿN

nx pλn P Rq

ane2πiλ

ppxq “

n“1

belongs to APpRq.

- Lemma 8. Given any f P APpRq and ε ą 0, there is a trigonometric polynomial p


such that }f ´ p}8 ă ε. In particular, APpRq is the closure in CpRq of the algebra of trigonometric polynomials.

Proof. We can assume }f}8 ď 1. For a given ε ą 0 let τε be the set of ε-translations for f. First we will need some auxiliary functions. We claim that for every sufficiently

şR φM “ 1, şR |φ1M| “ Oεp1q and ÿ

large M ě 1 there exists φM P Cc8pτε X p´M,Mqq such that 0 ď φM ď 1,

|φppn{p4Mqq|1{2 “ Oεp1q. Assuming this claim is true, we now finish the proof. Let

nPZ

fMpxq “ ż

fpx ` tqφMptqdt

R

and note that }f ´ fM}8 ď ε for any M. Also note that if |x| ď M then

fMpxq “ ż 2M

fptqφMpt ´ xqdt. The function φMpxq can be identified with a 4M-periodic C8-function and so we have φmpxq “ ÿ

´2M

θne2πinx{p4Mq

nPZ

nPZ |θn|2 “ p4Mq´1 ş´2M2M |φMpxq|2dx and

ř

where

θn “ p4Mq´1 ż 2M

φMpxqe´2πinx{p4Mqdx “ φpMpn{p4Mqq{p4Mq. We obtain

´2M

fMpxq “ ÿ

θrne´2πinx{p4Mq for |x| ď M,

nPZ

ş´2M2M fptqe2πint{p4Mqdt. Note this representation converges absolutely since |θrn| ď 4M|θn| “ |φpMpn{p4Mqq| ď 1,

where θrn “ θn

ř

ř

nPZ |θrn| “ Oεp1q. Now enumerate pθrnqnPZ in decreasing order of magnitude and call this new sequence pαM,nqně1. We obtain

nPZ |θrn|1{2 “ Oεp1q, and so,

fMpxq “ ÿ

αM,ne2πiλ

M,nx for |x| ď M,

ně1

for some λM,n P 4M1 Z. Noticing that

ÿn

|αM,n|1{2n ď

|αM,j|1{2 “ Oεp1q,

j“1

we obtain |αM,n| ď n´2. A standard Cantor’s diagonal procedure guarantees the existence of pαnqně1 such that

ř

nPZ |αn| “ Oεp1q and a subsequence Mk Ñ 8 such that limk αM

k,n “ αn for all n ě 1. Let now I Ă N be the n’s such that supk |λM

k,n| ă 8. By further taking a subsequence of the Mk’s we can assume that limk λM

k,n Ñ λn for n P I. Note now that

ż

1 2π|λM

|φ1Mpxq|dx “ Oδp|λM

k,n|´1q. In particular, limk αM

|αM

k,n| ď |φpMp´λM

k,nq| ď

k,n|

R

k,n “ αn “ 0 if n R I. Finally, the uniform bound |αM,n| ď n´2 forces fM

to converge uniformly in compact sets to gpxq “ ÿ

k

αne2πiλ

nx,

ně1

which in particular implies that

}f ´ g}8 ď ε. However, we can now simply truncated g to find a trigonometric polynomial p such that }f ´ p}8 ď 2ε.

It remains to construct the auxiliary functions φM. Since f is also uniformly continuous, it is easy to show that ttnunPZ ` p´δ,δq Ă τε{4 for some small δ “ δε ą 0 and some sequence ttnunPZ satisfying 1{δ ď tn`1 ´tn ď 3{δ for all n. Take h P Cc8p´1,1q even with 0 ď h ď 1 and

şR h “ 1. Let hδpxq “ hpx{δq{δ, ψpxq “ p2N ` 1q´1 řN

n“´N hδpx ´ tnq and φMpxq “ ψ ˚ ψ ˚ ψ ˚ ψ, where N ě 1 is selected to be the largest such that ttnu|n|ďN ` p´δ,δq Ă τε{4Xp´M{4,M{4q. Note we must have N ě δM10 for sufficiently large M. Since τε{4 ` τε{4 ` τε{4 ` τε{4 Ă τε we conclude that φM P Cc8pτε X p´M,Mqq. Also note that şR φM “ pşR ψq4 “ 1 and, since φ1M “ ψ1 ˚ ψ ˚ ψ ˚ ψ, that

ż

|φ1M| ď ż

|ψ1| “ Op1{δq. Finally note that

R

R

|ψppn{p4Mqq|2 “ 4M ż 2M

ÿ

|φpMpn{p4Mqq|1{2 “ ÿ

|ψpxq|2dx

´2M

nPZ

nPZ

ż 1

4M δp2N ` 1q

4M δp2N ` 1q

! δ´2,

|hpxq|2dx ď

“

´1

for M large enough. This finishes the proof. □

We define Ef :“ lim

ż T

ż T

- 1

- 2T


- 1

- 2T


fpxqe´2πiλxdx, whenever these limits exist (so Ef “ Efp0q).

### fpxqdx and Efpλq :“ lim

TÑ8

TÑ8

´T

´T

- Lemma 9. For any f P APpRq we have:


- (1) The average Efpλq exists;
- (2) The set specpfq :“ tλ P R : Efpλq ‰ 0u it at most countable;
- (3) If specpfq “ H then f “ 0;
- (4) If

ř

λPR |Efpλq| ă 8, then the following series converges absolutely and uniformly fpxq “ ÿ

λPR

Efpλqe2πiλx;

- (5) We have E|f|2 “ ř


λ |Efpλq|2 and for every ε ą 0 there is S Ă specpfq finite such that Ex|fpxq ´ ř

λPS Efpλqe2πiλx|2 ă ε.

Proof. For item (1), we can assume λ “ 0. Let ε ą 0 be given and take a trigonometric polynomial p such that }f ´ p}8 ď ε. Let A “ Ep, which exists by direct computation. We have

ż T1

ż T1

ż T

ż T

- 1

- 2T


1 2T1

- 1

- 2T


- 1

- 2T1


fpxqdx ´

fpxqdx “ Op2εq `

ppxqdx ´

ppxqdx

´T1

´T1

´T

´T

“ Op2εq ` A ´ A ` oT,T1p1q.

For item (2), note first that Efpλq exists since fpxqe´2πiλx is also almost periodic (by Bochner’s criterion). Let pn be a trigonometric polynomial such that }f ´ pn}8 ă n1. Assume that |Efpλq| ą 0 and let 1{n ă |Efpλq|. We obtain that |Epnpλq| ě |Efpλq|´ n1 ą 0, hence Epnpλq ‰ 0. We conclude that specpfq Ă Ť

ně1 specppnq. For item (3), let ε ą 0 be given and take a trigonometric polynomial p such that }f¯´ p}8 ď ε. Now, observing that

ż T

ż T

ż T

- 1

- 2T


- 1

- 2T


- 1

- 2T


fpxqpf¯pxq´ppxqqdx “ oTp1q`Opε}f}8q,

|fpxq|2dx “

fpxqppxqdx`

´T

´T

´T

ş´TT |fpxq|2dx “ 0. This is impossible if f is nonzero, because |f|2 is also almost periodic and uniformly continuous, and so if |fpxq|2 ě c for x in some interval I then |fpxq|2 ě c{2 for x P τc{2p|f|2q `I. Since τc{2p|f|2q contains some increasing sequence ttnunPZ satisfying tn`1 ´ tn “ Op1q, it implies that E|f|2 ě Ep1τ

we conclude that limT 21T

c{2p|f|2q`Iq ą 0, which is absurd. We conclude that f “ 0. For item (4), note that

gpxq “ ÿ

Efpλqe2πiλx,

λPR

is well-defined and converges absolutely and uniformly on R. Also note that dominated convergence implies that Egpλq “ Efpλq for all λ P R, and so by item (3) f “ g. For item (5), let Λ1 :“ Ymě1specppmq for some trigonometric polynomials pm such that }f ´ pm}8 ă 1{m and enumerate Λ1 “ tλnuně1. It is enough to show that E|f|2 “ ř

ně1 |Efpλnq|2. Let fNpxq “ řN

n“1 Efpλnqe2πiλ

nx. A straightforward computation shows that E|f|2 ´ E|fN|2 “ E|f ´ fN|2 and so

řN

n“1 |Efpλnq|2 ď E|f|2 for all N. Another routine computation shows

E|f ´ p|2 “ E|f|2 ´ E|fN|2 ` E|fN ´ p|2 ě E|f|2 ´ E|fN|2, for any trigonometric polynomial of the form ppxq “ řN

nx, for some bn P C. Since pm is of such form for some Nm, we conclude that E|f ´ fN

n“1 bne2πiλ

m|2 ă 1{m and that E|fN

m|2 ď E|f|2 ď E|fN

m|2 ` 2{m.

□

The following proposition (see [10, p. 46]) justifies the notation fpxq „ ÿ

Efpλqe2πiλx.

λPR

Proposition 10 (Bochner’s approximation). For any f P APpRq there is an sequence of functions cn : R Ñ r0,1s, cn ď cn`1, each cn with finite support, satisfying

$ &

1 if Efpλq ‰ 0 0 if Efpλq “ 0,

cnpλq “

lim

%

nÑ8

and such that

|fpxq ´ ÿ

cnpλqEfpλqe2πiλx| “ 0.

lim

sup

nÑ8

xPR

λPR

5. Almost Periodic Functions in C`

Recall that we have defined in the introduction the space APpC`q of holomorphic almost periodic functions f : C` Ñ C such that for every ε ą 0 there is a relatively dense set of ε-translations τεpfq Ă R satisfying

|fpzq ´ fpz ` tq| ă ε

sup

εăIm ză1{ε

for every t P τεpfq. We say a function f : C` Ñ C is bounded on strips if sup

|fpzq| ă 8

εăIm ză1{ε

for every ε ą 0. We now give an alternative characterization of almost periodicity.

- Lemma 11. Let f : C` Ñ C be holomorphic. Then following are equivalent:


- (1) f is bounded on strips and for every h ą 0 we have fp¨ ` ihq P APpRq;
- (2) f is bounded on strips and there is h ą 0 such that fp¨ ` ihq P APpRq;
- (3) f P APpC`q;


In this case the quantity

ż T`iy

- 1

- 2T


fpzqe´2πiλzdz exists for every λ P R, is independent of y ą 0, it is nonzero in at most countably many λ’s and ÿ

Efpλq :“ lim

TÑ8

´T`iy

|Efpλq|2e´4πyλ “ Er|fp¨ ` iyq|2s for every y ą 0.

λPR

Proof. The implications p1q ñ p2q and p3q ñ p1q are obvious. We now show p2q ñ p3q. Let τε be the set of ε-translations for fp¨ ` ihq. We claim that τε also works in any horizontal strip containing the line Imz “ h. Indeed, let t P τε and 0 ă y1 “ y2{2 ă y2 ă h. For all y with y2 ă y ă h, we can then apply Hadamard’s there lines lemma (for Imz P ty1,y,hu) to conclude that

log |fpx ` iyq ´ fpx ` iy ` tq|

sup

x

y ´ y1 h ´ y1

h ´ y h ´ y1

ď

log |fpx ` ihq ´ fpx ` ih ` tq| `

log |fpx ` iy1q ´ fpx ` iy1 ` tq|

sup

sup

x

x

y2 ´ y1 h ´ y1

h ´ y2 h ´ y1

ď

log ε `

B1

- for some B1 ą 0. Hence, there is α “ αpy2,hq ą 0 such that


1 α

εα.

|fpzq ´ fpz ` tq| ď

sup

y2ăIm zăh

We can apply the same procedure for h ă Imz ă y3 for any y3 ą h to prove the claim. This shows that f P APpC`q. Now notice that by Lemma 9 the limit Efpλq exists for every y ą 0. To show is independent of y, we can use Cauchy’s formula to deduce that if 0 ă y1 ă y2 then

„

fpzqe´2πiλzdzȷ

ż T`iy

ż T`iy

- 1

- 2T


- 1

- 2T


1

2

fpzqe´2πiλzdz ´

´T`iy1

´T`iy2

“ „

fpzqe´2πiλzdzȷ “ Oppy2 ´ y1qe2π|λ|y

ż ´T`iy

ż T`iy

- 1

- 2T


- 1

- 2T


2

2

fpzqe´2πiλzdz ´

{Tq.

2

´T`iy1

T`iy1

Taking T Ñ 8, we conclude that Efpλq is independent of y. Since e´2πλyEfpλq “ Erfp¨` iyqspλq we deduce that λ P R ÞÑ Efpλq has countable support and

ř

λPR |e´2πλyEfpλq|2 “ E|fp¨ ` iyq|2. This finishes the proof. □

For a function f P APpC`q (or f P APpRq) we define the spectrum of f to be specpfq :“ tλ P R : Efpλq ‰ 0u.

- Lemma 12. The following hold:


- (i) Let f P APpC`q. Then f is bounded in C` ` ic, for some c ą 0, if and only if specpfq Ă r0,8q. In this case f is bounded in C` ` ic for any c ą 0 and limyÑ8 supx |fpx ` iyq ´ Efp0q| “ 0;
- (ii) If f P APpC`q, specpfq is bounded from below and fpzq ‰ 0 for all Imz ą c, for some c ą 0, then inf specpfq P specpfq;
- (iii) If f,g P APpC`q have spectrum bounded from below then so has fg P APpC`q. If in addition f,g have locally finite spectrum, then so has fg.
- (iv) If f P APpC`q and f ‰ 0 in C`, then infεăImză1{ε |fpzq| ą 0 for all ε ą 0 and 1{f P APpC`q. Moreover, if f has spectrum bounded from below then so has 1{f, and if in addition f has locally finite spectrum then so has 1{f.
- (v) If f P APpC`q and |fpzq| ă 1 for all z P C` then for every ε ą 0 there is c ą 0 such that |fpzq| ă 1 ´ c if Imz ą ε.


Proof. Items (i) and (ii): These are direct applications of [10, Thm. p. 162 & p. 152].

- Item (iii): Note that f1pzq “ e´2πiMzfpzq and g1pzq “ e´2πiMzgpzq have spectrum contained in r0,8q for some M ą 0, thus both are bounded for Imz ą 1 and so is h “ f1g1. Thus, specpfgq “ specphq ` 2M Ă r0,8q, hence fg have spectrum bounded from below.

We also have specpfgq Ă specpfq`specpgq “ specpf1q`specpg1q´2M, and since sums of locally finite sets contained in r0,8q is also locally finite and contained in r0,8q, we conclude that the spectrum of fg is locally finite if both f and g have locally finite spectrum.

- Item (iv): By a clever application of Hadamard’s Three-Lines theorem [10, Thm. 11, p.


139 & Thm. 9, p. 144], one can show that if w is an accumulation point of f in an horizontal line, then fpzq “ w has a solution in any horizontal strip containing this line. In particular, if f never vanishes in C` then |f| is bounded away from zero in any horizontal strip, thus 1{f P APpC`q. If f „ ř

λěM Efpλqe2πiλz where M “ inf specpfq, since f has no zeros, M P specpfq, p “ EfpMq ‰ 0 and limyÑ8 supx |fpx ` iyqe´2πiMpx`itq ´ p| “ 0. In particular gpzq “ 1 ´ fpzqe´2πiMz{p is bounded in absolute value by 1{2 for Imz ą c, for some large c ą 0 and specpgq Ă p0,8q. We obtain

e´2πiMz p ÿ

e´2πiMz p

1 fpzq

1 1 ´ gpzq

gpzqn,

“

“

ně0

where the sum converges absolutely and uniformly for Imz ą c. We conclude that Ep1{fqpλq “ ř

ně0 Epgnqpλ ` Mq (with absolute convergence), and so Ep1{fqpλq “ 0 if λ ă ´M. If in addition specpfq is locally finite, then specpgq is locally finite and contained in rδ,8q, for some δ ą 0. Since specp1{fq ` tMu Ă Yně0` ‘n specpgq˘

, we conclude that pspecp1{fq ` tMuq X r0,Ts Ă Y0ďnďT{δ

` ‘n specpgq X r0,Ts˘

, and so specp1{fq is locally finite. Item (v): Since f is bounded we deduce that Efpλq “ 0 for λ ă 0 and, by [10, Thm. 9, p. 144], that supεăImză1{ε |fpzq| ă 1 for every ε ą 0. Hence |Efp0q| ă 1. On the other hand limyÑ8 supx |fpx ` iyq ´ Efp0q| “ 0. □

- Lemma 13. Let f P APpC`q and assume specpfq Ă t0u Y rb,8q for some b ą 0. If F : C` Ñ C is holomorphic and iF1{F “ f, then F P APpC`q and specpFq Ă t´Efp0q{p2πquYr´Efp0q{p2πq`b,8q. Moreover, if in addition specpfq is locally finite, then so it is specpFq.


Proof. Let p “ Efp0q. Since F has no zeros in C` we can write Fpzq “ e´igpzq´ipz for some g : C` Ñ C holomorphic. Since g1pzq ` p “ iF1pzq{Fpzq “ fpzq we conclude that g1 P APpC`q, specpgq Ă rb,8q and Epg1qpλq “ 1λěbEfpλq. We can now apply [10, Thm. 9, p. 152] to conclude that g P APpC`q and that Egpλq “ 1λěbEfpλq{p2πiλq for λ ‰ 0. If Φ : C Ñ C is entire and h P APpC`q then it is easy to conclude that Φ˝h P APpC`q. Indeed, since h is bounded in strips and since Φ1 is bounded in bounded sets, we conclude that for any horizontal strip contained in C` there is C ą 0 such that |Φphpzqq ´ Φphpwqq| ď C|hpzq ´ hpwq| for all z and w in that strip. This shows that Φ ˝ h P APpC`q. This implies that the power series expansion

Φphpzqq “ ÿ

Φpnqp0q n!

hpzqn.

ně0

converges absolutely and uniformly on any horizontal strip. Now assume that specphq Ă rb,8q for some b ą 0. Since specphnq Ă rnb,8q and

ErΦ ˝ hspλq “ ÿ

Φpnqp0q n!

Erhnspλq,

ně0

we conclude that specpΦ ˝ hq Ă t0u Y rb,8q. If in addition specphq is locally finite, since specpΦ ˝ hq X r0,Ts Ă Y0ďnďT{b

` ‘n specphq X r0,Ts˘

,

we conclude that specpΦ ˝ hq is locally finite. Considering Φpzq “ e´iz and hpzq “ gpzq ´ Egp0q, we deduce that Fpzq “ Φphpzqqe´iEgp0q´ipz belongs to APpC`q and that specpFq Ă t´p{p2πqu Y r´p{p2πq ` b,8q. Moreover, specpFq is locally finite if specpfq also is. □

We also have approximation by trigonometric polynomials (see [10, p. 148])

Proposition 14 (Bochner’s approximation). Let f P APpC`q. Then for every b ą 1 there is a sequence of functions cn : R Ñ r0,1s as in Proposition 10 such that

|fpzq ´ ÿ

cnpλqEfpλqe2πiλz| “ 0.

lim

sup

nÑ8

1{băIm zăb

λPR

6. Representations of Analytic Functions

We say a holomorphic function g : C` Ñ C if of bounded type if there are two bounded holomorphic functions P,Q : C` Ñ C such that g “ P{Q. We write g P BTpC`q. If g is of bounded type then the mean type

log |gpiyq| y

ϑpgq :“ limsup

yÑ8

exists and is finite. For more information about these definitions we recommend [13, 20].

- Lemma 15. Let f : C` Ñ C be holomorphic and write g “ exppfq. The following are equivalent:


- (1) There is a real-valued locally finite measure µ with degpµq ď 2 such that fpzq ` fpwq

z ´ w “

1 2πi

ż

R

dµptq pt ´ zqpt ´ wq

(9) holds for every z,w P C`;

- (2) g P BTpC`q and ϑpgq “ 0.


Proof. First we show that p1q ñ p2q. Indeed, note first that Refpx ` iyq “

ż

dµptq pt ´ xq2 ` y2

y π

.

R

Writing µ “ µ1 ´ µ2 where each µj is nonnegative and defining fjpzq “

ż

1 ` tz t ´ z

dµjptq 1 ` t2

1 πi

R

we conclude that Refj ě 0 in C` and that Ref “ Ref1 ´ Ref2, hence f “ f1 ´ f2 ` ih for some constant h P R. However, since each gj “ expp´fjq is bounded in absolute value

### by 1 in C` and g “ eihg2{g1, we deduce that g P BTpC`q. Note also that ϑpgq “ limsup

ż

### Refpiyq y “ limsup

dµptq t2 ` y2 “ 0.

1 π

yÑ8

yÑ8

R

Now we show p2q ñ p3q. Since g has no zeros, Nevalinnas’s factorization for functions of bounded type [13, Theprem 9] implies that there exists a unique real-valued locally finite measure µ, with degpµq ď 2, and some c,h P R such that

efpzq “ gpzq “ e´ihz expˆic `

˙.

ż

dµptq 1 ` t2

1 ` tz t ´ z

1 πi

R

Since h “ ϑpgq “ 0, a simple computation shows that (9) holds. □

- Lemma 16. Let f P APpRq and assume that specpfq X p0,bq “ H for some b ą 0. Then Fpzq “

- 1

- 2πi


ż

R

1 ` tz t ´ z

fptqdt 1 ` t2

belongs to APpC`q and EFpλq “ 1λěbEfpλq for λ ‰ 0. Proof. Since any f P APpRq is bounded, the integral defining F converges absolutely and defines an holomorphic function F. Noticing that pt´z1qp`1tz`t

2q “ t´1z ´ 1`tt2

we obtain that

F1pzq “

- 1

- 2πi


ż

R

fptqdt pt ´ zq2

,

and so |F1px ` iyq| ď 21y maxtPR |fptq| for y ą 0, hence F1 is bounded on strips. Since

F1px ` iq “

1 2πi

ż

R

fpt ` xqdt pt ´ iq2 it is clear that any set of ε-translations for f is also one for F1p¨ ` iq, and so F1p¨ ` iq P APpRq, and Lemma 11 shows that F1 P APpC`q. Dominated Convergence implies that

EF1pλq “ e2πλEfpλq

- 1

- 2πi


ż

R

e2πiλt pt ´ iq2

“ e2πλEfpλq2πi|λ|e´2π|λ|1λą0 “ 2πimaxtλ,0uEfpλq,

and, since specpfqXp0,bq “ H for some b ą 0, we obtain specpF1q Ă rb,8q. We can now apply [10, Thm. 9, p. 152] to conclude that F P APpC`q. □

- Lemma 17. Let f : C Ñ C be entire such that f,f˚ P APpC`q and both have spectrum bounded from below. If f has finite order, that is,


### log` |fpzq| |z|ρ

ă 8u ă 8,

orderpfq :“ inftρ ą 0 : limsup

|z|Ñ8

then f has finite exponential type, that is, τ “ limsup

### log |fpzq| |z|

ă 8.

|z|Ñ8

In this case f and f˚ are of bounded type, f is bounded on the real line and |fpzq| ď Meτ|y| for all z “ x ` iy, where M “ supxPR |fpxq| and τ “ maxtϑpf˚q,ϑpfqu. Moreover,

Efpλq “ Epf˚qp´λq for all λ P R and

specpfq “ ´specpf˚q Ă r´τ{p2πq,τ{p2πqs. If in addition specpfq is locally finite, then f is trigonometric polynomial.

Proof. Observe that since f has spectrum bounded from below, then Lemma 12(i) shows that for m “ mintinf specpfq,inf specpf˚qu we have that |fpzqe´2πimz| ` |f˚pzqe´2πimz| is bounded for Imz ą c, for any c ą 0. This in particular shows that fpzqe´2π|m|z is bounded on the sides of any sector Sc “ tz “ x`iy : x ą |y|{cu. Since f has finite order, one can apply Phranm¨en-Lindel¨of for sectors (with small c ą 0) [33, Thm. 1, p. 37] to conclude that fpzqe´2π|m|z is bounded in Sc. We then apply the same argument replacing fpzq by f˚p´zq to conclude that f˚p´zqe´2π|m|z is bounded in Sc. All these imply that f has finite exponential type, that is,

|fpzq| ! eC|z|

- for some C ą 0. However, since fpz ` iqe´2πimpz`iq is bounded on the real line, another application of Phranm¨en-Lindelo¨f [33, Thm. 3, p. 38] shows that |fpz ` iqe´2πimpz`iq| ! eC1|y| for some C1 ą 0, and so |fpzq| ! eC2|y| for some C2 ą 0. In particular f is bounded on every horizontal strip and, by the same result, we can take C1 “ τ. A straightforward calculation using Cauchy’s integral formula shows that


fpzqe´2πiλzdz˙ “ 0,

ˆż T`i

fpzqe´2πiλzdz ´ ż ´T`i

1 2T

Efpλq ´ Epf˚qp´λq “ lim

TÑ8

´T´i

T´i

since f is now bounded on horizontal strips. In particular, specpfq “ ´specpf˚q. A well-known result of Krein [25] (see also [33, Thm. 1, p. 115]) shows that f,f˚ P BTpC`q and that τ “ maxtϑpf˚q,ϑpfqu. Since gpzq “ fpzqeiτz is bounded in C`, Lemma 12(i) shows that specpfq ` τ{p2πq “ specpgq Ă r0,8q, hence specpfq Ă r´τ{p2πq,8q. The same argument shows that specpf˚q Ă r´τ{p2πq,8q, but since Efpλq “ Epf˚qp´λq, we obtain that specpfq Ă r´τ{p2πq,τ{p2πqs. Finally, if specpfq is locally finite, Proposition

- 14 proves straightforwardly that f is a trigonometric polynomial. □


7. Proof of Theorem 1 We start we some lemmas.

## Lemma 18. For w,z P C` let

e´2πiw|x|1xă0 ` e2πiz|x|1xě0 z ´ w

gpw,z,xq “

. Then

1 2πipξ ´ zqpξ ´ wq

gppw,z,ξq “

.

Proof. Letting fzpxq “ e2πiz|x|1xą0 ` 121x“0 we have fpzpξq “ ż 8

1 2πipξ ´ zq

e2πixpz´ξqdx “

.

0

The lemma follows since gpw,z,xq “ pz ´ wq´1pf´wp´xq ` fzpxqq. □

- Lemma 19. Let pµ,aq be a FS-pair with degpµq ď 2. Then


ż

ÿ

dµptq pt ´ zqpt ´ wq uniformly for w and z in the region

1 2πi

apλqgpw,z,λqp1 ´ |λ|{Tq “

lim

TÑ8

R

|λ|ăT

Rc :“ tz P C` : |Rez| ď 1{c and Imz ě cu, pfor any c ą 0q.

ş

Proof. Let φ P Cc8pRq,

φ “ 1, φ ě 0, suppφ Ă p´1,1q and define φεpxq “ φpx{εq{ε for 0 ă ε ă 1. Let w,z P Rc, T ą 2{c and

gε,Tpxq :“ pgpw,z,¨qp1 ´ T1 | ¨ |q`q ˚ φεpxq, where s` “ maxt0,su. Note that gε,T P Cc8p´ε ´ T,T ` εq and

gpε,Tpξq “ pgppw,z,¨q ˚ STpξqqφppεξq, where STpxq “ sin

2pTπxq

Tpπxq2 . Note that |φppεξq| ď 1. We claim that17

1 ξ2 ` c2

|gppw,z,¨q ˚ STpξq| !c

. (10) We shall prove this claim in the end. Since pµ,aq is a FS-pair, in particular we obtain

apλqgε,Tpλq “ ż

ÿ

gpε,Tptqdµptq.

R

|λ|ăT`ε

Since ap¨q is locally summable, and as ε Ñ 0, gε,Tpxq Ñ gpw,z,xqp1 ´ |x|{Tq` uniformly in x P R and gpε,Tpξq Ñ gppw,z,¨q ˚ STpξq pointwise, Dominated Convergence implies that

apλqgpw,z,λqp1 ´ |λ|{Tq “ ż

ÿ

gppw,z,¨q ˚ STptqdµptq.

R

|λ|ăT

It is now enough to show the right hand side above converges uniformly in the region pw,zq P Rc2. This can be done by noticing that

|ξ1 ´ ξ2| 4πc3

1 2π|z ´ w|ˇ

1 ξ1 ´ z ´

1 ξ1 ´ w ´

1 ξ2 ´ z `

1 ξ2 ´ wˇ ď

|gppw,z,ξ1q ´ gppw,z,ξ2q| “

,

and so gppw,z,¨q ˚ STpξq Ñ gppw,z,ξq uniformly in x P R and pw,zq P Rc, as T Ñ 8. Finally, the uniform bound (10) guarantees the desired uniform convergence. It remains

17We write A !p B if there is a numerical constant K ą 0, depending only in the parameter p, such that A ď KB.

to prove the claim (10). First note that |gppw,z,ξq| !

1

1

1 c2 ` ξ2

pξ ´ Rezq2 ` c2 `

pξ ´ Rewq2 ` c2 !c

, and so we can use a contour change (and that T ą 2{c) to obtain

ż

ż

sin2pπTtq ppξ ´ tq2 ` c2qt2

sin2pπTpt ` i{Tqq ppξ ´ t ´ i{Tq2 ` c2qpt ` i{Tq2

1 T

1 T

|gpw,z,¨q ˚ STpξq| !c

dt “

dt

R

R

ż

πpc ` 1{Tq{c ξ2 ` pc ` 1{Tq2

1 ppξ ´ tq2 ` c2qpt2 ` 1{T2q

1 T

1 c2 ` ξ2

dt “

!

!

.

R

## □ Proof of Theorem 1 (and Theorem 2).

Necessity. Assume that pµ,aq is an real-antipoal FS-pair such that degpµq ď 2 and ap¨q has exponential growth. Since ap´λq “ apλq, we can apply Lemma 19 (multiplying both sides by pz ´ wq) to obtain

ˆ ÿ

apλqe´2πiλwp1 ´ λ{Tq˙

apλqe2πiλzp1 ´ λ{Tq ` ÿ

ap0q ` lim

TÑ8

0ăλăT

0ăλăT

ˆ

˙dµptq “

ż

ż

ż

1 ` tz t ´ z

dµptq 1 ` t2 ´

1 ` tw t ´ w

dµptq 1 ` t2

1 t ´ z ´

1 t ´ w

1 2πi

1 2πi

- 1

- 2πi


“

,

R

R

R

where the limit exists and is uniform for w and z in compact sets of C`. In particular, we conclude there exists h P R such that

ż

ÿ

1 ` tz t ´ z

dµptq 1 ` t2

- 1

- 2


- 1

- 2πi


apλqe2πiλzp1 ´ λ{Tq “ ih `

fpzq “

ap0q ` lim

,

TÑ8

R

0ăλăT

where the limit above exists and is uniform in compact sets. A simple computation shows fpzq ` fpwq z ´ w “

ż

dµptq pt ´ zqpt ´ wq

- 1

- 2πi


. (11)

R

This proves assertion (I). Since ap¨q has exponential growth, we let c “ inftb ą 0 : ř

λPR |apλq|e´2πb|λ| ă 8u. Then we must have fpzq “

ap0q ` ÿ

- 1

- 2


apλqe2πiλz

λą0

for Imz ą c, as the above series converges absolutely and uniformly for Imz ą c ` ε, for any ε ą 0. Thus, after choosing an enumeration for supppaq, we conclude that fp¨ ` ihq is the uniform limit of trigonometric polynomials and we obtain that fp¨ ` ihq P APpRq for every h ą c. By Lemma 11 we obtain fp¨ ` icq P APpC`q. This proves assertion (II). Assertion (III) is direct since if ppxq “ ř

θPS pθe2πiθx, for some finite set S Ă r0,8q, then limsup

ż T

ap0qδSp0q ` ÿ

- 1

- 2T


- 1

- 2


apλqe´4πcλδSpλqpλˇ

fpx ` 2icqppxqdxˇ “ ˇ

TÑ8 ˇ

´T

λą0

! max|pθ| ÿ

|apλq|e´4πc|λ| ! max|pθ|.

λPR

Finally, by Lemma 15, assertion (IV) is implied by representation (11).

Sufficiency. We prove sufficiency replacing property pIIIq by pIII˚q as in Theorem 2, and so also proving Theorem 2. Let c1 “ inftb ą 0 : fp¨`ibq P APpC`qu and f1pzq “ fpz`c1q. By condition pIIq, we can apply Lemma 11 to deduce the limit

ż T`iy

ż T`iy`ic

1 2T

1 2T

1

f1pzqe´2πiλzdz “ e´2πλc

fpzqe´2πiλzdz

Ef1pλq “ lim

### lim

1

TÑ8

TÑ8

´T`iy

´T`iy`ic1

exists, does not depend on y ą 0 and is nonzero only for countable many real λ’s. We also have that

ř

λ |Ef1pλq|2e´4πhλ ă 8 for all h ą 0. This shows that Efpλq “ lim

ż T`iy

1 2T

fpzqe´2πiλzdz

TÑ8

´T`iy

is independent of y ą c1 and is nonzero only for countable many real λ’s. By condition pIII˚q, there is BM ą 0 and c2 ě c1 (with equality only if fp¨ ` ic1q P APpRq) such that

ż T

ÿ

1 2T

Efpλqe´2πc

2λδSpλqpλˇ

BM max|pθ| ě limsup TÑ8 ˇ

fpx ` ic2qppxqdxˇ “ ˇ

´T

0ďλďM

whenever ppxq “ ř

θPS pθe2πiθx for some finite set S Ă r0,Ms. We conclude that specpfq Ă r0,8q and ÿ

|Efpλq| ď BMe2πc

2M

0ďλďM

for every M ą 0, so the function apλq defined in (3) is locally summable. Lemma 12(i) f is bounded for Imz ą 2c1, in particular limyÑ8 Refpiyq{y “ 0. By condition pIVq, we can now apply Lemma 15 to deduce there is a real-valued locally finite measure µ of degree at most 2 such that (11) is true. In particular,

ż

dµptq pt ´ xq2 ` y2

y π

2Refpx ` iyq “

.

R

As in Lemma 15 one can then write f “ f1 ´ f2 such that Refj ě 0 in C` and fjpiq “ şR

dµjptq

2πp1`t2q. We can then apply Harnack’s inequality [10, p. 136], that translates to

fjpzq ´ fjpiq fjpzq ` fjpiqˇ ď ˇ

z ´ i z ` iˇ.

ˇ

Since

|z ` i| ` |z ´ i| |z ` i| ´ |z ´ i|

p1 ` |z|q2

4y pz “ x ` iyq, we conclude that |fjpzq| ď p1`|z|q

ď

4y şR

### 4y fjpiq and so |fpzq| ď p1`|z|q

d|µ|ptq

2

2

2πp1`t2q. We deduce that liminf rÑ8

ż π

1 r

log` |fpreiθq|sinθdθ “ 0,

0

and so one can now apply the Phranme¨n-Lindel¨of principle (as in [13, Thm. 1]) to obtain that fpz ` icq is bounded in C` for every c ą c1. Lemma 12(i) shows that Efpλq “ 0 for λ ă 0. Finally, let us prove that pµ,aq is a FS-pair. For z P C` and t P R let

Pzptq “ πipt2z´z2q. Since identity (11) holds true, a simple computation shows

fpz ` sq ` fp´z¯ ` sq “ Pz ˚ µpsq for all s P R. By Bochner’s approximation on APpRq, for every h ą 0, one can find a sequence of functions dn : R Ñ r0,1q, each with finite support and such that limn dnpλq “ 1specpfqpλq, and that

|fpzq ´ ÿ

Efpλqdnpλqe2πiλz| “ 0.

lim

sup

n

Im z“c1`h

λě0

Let φ P Cc8pp´M,Mqq be antipodal. It is now straightforward (using Bochner’s approximation, Dominated Convergence and local summability) to conclude that

ż

fpz ` sqφppsqds “ ÿ

Efpλqφpλqe2πiλz.

R

0ďλăM

if Imz ą c1. Another routine computation (using that ap0q “ 2ReEfp0q) shows

apλqφpλqe2πi|λ|z “ ż

rfpz ` sq ` fp´z¯ ` sqsφppsqds “ ż

ÿ

Pz ˚ µpsqφppsqds

R

R

|λ|ăM

“ ż

Pz ˚ φpptqdµptq

R

if Imz ą c1. By real-antipodal splitting and linearity, the above formula holds for all φ P Cc8pRq. Now observe that both sides extend analytically to Imz ą 0. Taking z “ iy and noting that Piy is Poisson’s kernel, a routine application of Dominated Convergence and approximate identity arguments (using that ap¨q is locally summable and degpµq ď 2) allows us to take y Ñ 0 and conclude that

apλqφpλq “ ż

ÿ

φpptqdµptq.

R

|λ|ăM

Therefore pµ,aq is an FS-pair. This finishes the proof. □

8. FS-pairs, an account of various examples.

Throughout this section we will define certain families of FS-pairs for which we will try to provide as many examples as possible, old and new. We define these families so that they are closed under scaling, translation, modulation and multiplication by scalar.

- 8.1. Finite Support. Let pµ,aq be a FS-pair such that ap¨q has finite support, that is,


there is tpnuNn“1 Ă C and tλnuNn“1 Ă R such that

ż

ÿN

φpptqdµptq “

pnφpλnq

R

n“1

for all φ P Cc8pRq. It is easy to see that we must have dµptq “ řN

n“1 pne2πiλ

ntdt.

## 8.2. Uniformly Discrete Poisson Summation (UDPS). We denote UDPS the set of

FS-pairs pµ,aq such that there is α ą 0, tθjuNj“1 Ă r0,αq and trig-polynomials tQjuNj“1 where

ÿN

ÿ

µ “

Qjpλqδλ.

j“1

λPαZ`θj

It is easy to see that if pµ,aq P UDPS then ap¨q is also of the above form. The breakthrough of Lev & Olveskii [31] shows that pµ,aq P UDPS if and only if µ and ap¨q have uniformly discrete support (assuming apriori that both are strongly tempered), which justifies the name of this family. We observe that we can always assume that all Q1js are equal since by classical interpolation results (for instance, Lagrange interpolation via Chebyshev polynomials) one can always find trigonometric polynomials Pj, which are α-periodic, and such that Pjpθkq “ δj,k. Thus, if we let Q “ řN

j“1 PjQj then Qpαn ` θjq “ Qjpαn ` θjq for all n P Z, and so

µ “ ÿ

Qpλqδλ.

λPYNj“1pαZ`θjq

### 8.3. Real Rooted Trigonometric Polynomial (RRTP). We let the class RRTP to be the family of FS-pairs pµ,aq such that there are four trigonometric polynomials Ej (j “ 1,2,3,4) of Hermite-Biehler class, that is, |Ejpzq| ą |Ejpzq| for Imz ą 0, and such that

δγ ´ ÿ

µ “ ÿ

Q2pγq φ12pγq

Q1pγq φ11pγq

## δγ

φ2pγq”0 pmod πq

φ1pγq”0 pmod πq

´ i ÿ

δγ ` i ÿ

Q3pγq φ13pγq

Q4pγq φ14pγq

δγ,

φ3pγq”0 pmod πq

φ4pγq”0 pmod πq

where Qj are trigonometric polynomials, φj is the phase function associated with Ej, defined by the condition that Ejpxqeiφ

jpxq is real for all x P R (φj is uniquely defined modulo π, see (4)). We observe that if we write Ej “ Aj ´ iBj, were Aj,Bj are trigonometric polynomials which are real on the real line, then both A and B have only real zeros, A{B have only simple real zeros and simple poles which interlace,

1 φ1jpγq

tγ P R : φjpγq ” 0pmodπqu “ ZerospBj{Ajq and

pAj{Bjq ą 0. By Remark 4, RRTP contains the pairs pµ,µpq where

“ Res

z“γ

µ “ ÿ

mpγqQpγqδγ

Ppγq“0

and Q and P are any given trigonometric polynomials, P with only real roots and mpγq is the multiplicity of the zero γ. These measures were first introduced and studied by Kurasov and Sarnak [26]. Observe that UDPS Ă RRTP since YjαZ ` θj “ Zerospś

j sinpπpz ´ θjq{αqq. Indeed RRTP is a much richer class than UDPS since, for

instance,

Ppzq “ detpU ` diagpe2πil

1z,...,e2πil

nzqq

has only real roots if U is a n ˆ n unitary matrix and l1,....,ln P R. The zeros of such polynomials are generically not contained in a finite union of arithmetic progressions [2]. Trigonometric polynomials with only real zeros have been classified recently in [1] as restrictions of Lee-Yang polynomials. A polynomial R : Cn Ñ C is Lee-Yang if Rpz1,...,znq ‰ 0 whenever mintmaxt|z1|,...,|zn|u,maxt|z1|´1,...,|zn|´1uu ă 1. Indeed, the main result in [1] states that if P is a trigonometric polynomial with only real zeros then there exists a Lee-Yang polynomial Rpz1,...,znq and positive reals l1,...,ln, linear independent over Q, such that

nxq. A simple example is

Ppxq “ Rpeil

1x,...,eil

¨ ˚ ˝Id3 ´

» –

˛ ‹ ‚“ 1 ` z12{3 ´ z2p1{3 ` z12q

fi ffi fldiagpz1,z1,z2q

- 0 ´1{3 4{3
- 1 0 0 0 2{3 1{3


Rpz1,z2q “ det

### and

?

?

?

3i 2

Rpeπip

2´1qz,e2πip1`

2qzq “ sinp2πzq ` 3sinp2π

Ppzq “

2zq. Note the characteristic polynomial of the matrix above is px ´ 1qp3x2 ` 2x ` 3q{3, with roots t1,´1{3 ˘ i

?

8{3u, and so it is an unitary matrix. Hence, the polynomial R above is Lee-Yang and P has only real roots.

- 8.4. Crystalline Measures (CM). We let CM be the class of FS-pairs pµ,aq such that both µ and ap¨q have locally finite support. By Theorem 3 we conclude that RRTP Ă CM. One main theme investigated in [26, 2, 1] is to find pairs pµ,aq P CM such that supppaq and/or supppµq intersects any infinite arithmetic progression at most finitely18. Guinand [22, p. 265], in 1959, was “almost the first” to produce such pair, as we shall explain below. He constructs a (self-dual) FS-pair pµ,µq with


µ “ ÿ

n`1{9 ` δ´?

cnpδ?

n`1{9q,

ně0

where cn are the cofficients of the modular form19

“ q1{9 ˆ1 ´

q6 ` ¨¨¨˙ “ ÿ

ηpzq2{3ηp4zq2{3 ηp2zq1{3

- 2

- 3


4 9

40 81

160 243

268 729

1808 6561

q2 ´

q3 ´

q4 `

q5 `

q ´

cnq1{9`n.

ně0

#### 18So very non-periodic 19Guinand did not realized this nor constructed his example in the way we do here.

### Above

ηpzq “ q1{24 ź

p1 ´ qnq “ ÿ

2{24

χ12pnqqn

ně1

ně1

is the Dedekind eta-function, q “ e2πiz and χ12 is the Dirichlet character of modulus 12 with χ12p1q “ χ12p11q “ ´χ12p5q “ ´χ12p7q “ 1 and zero otherwise. Note that if n “ 9m2 ` 2m then an ` 1{9 “ 3m ` 1{3, and so the support of µ contains an infinite arithmetic progression t3m ` 1{3umě1. We will show below that, with the right point of view, one can embed Guinand’s example and also classical Poisson summation in a real one-parameter family, for which almost all members have the property that their support intersect any infinite arithmetic progression at most four times. For that we need first the following lemma.

Lemma 20. Let F P APpC`q, with locally finite spectrum contained in r0,8q and assume that ÿ

|EFpγnq|p1 ` γnq´k ă 8

ně0

for some k ą 0, where specpFq “ tγnuně0. Assume that Gpzq “ Fp´1{zqai{z also belongs to APpC`q, has locally finite spectrum contained in r0,8q and EG satisfies a similar estimate the one above for EF. Let

µ “ ÿ

EFpγnqpδ?2γn ` δ´?2γnq. Then µ is a strongly tempered measure and

ně0

µp “ ÿ

EGpλnqpδ?

2λn ` δ´?

2λnq

ně0

where specpGq “ tλnuně0. Hence pµ,µpq P CM.

Proof. The proof is inspired by [17, Lemma 2.1]. Consider the gaussian gzptq “ eπizt2 for z P C`. Observe that gpzptq “ ai{zg´1{zptq and that gzp

?

2sq “ e2πizs for s ě 0. Then the identity

Gpzq “ ÿ

EGpλnqgzpa2λnq “ Fp´1{zqai{z “ ÿ

EFpγnqgpzpa2γnq

ně0

ně0

shows that

ÿ

EFpγnqpφppa2γnq ` φpp´a2γnqq “ ÿ

EGpλnqpφpa2λnq ` φp´a2λnqq,

ně0

ně0

for any φ P spanCtgz : z P C`u. An approximation argument similar to the one employed in [17, Lemma 2.1] shows that the above identity actually holds for any φ P SpRq. □

The following constructions were inspired by a similar one partially communicated in 2018 by Danylo Radchenko in a seminar at the University of Bonn.

- 8.4.1. N-Level eta-quotients and self-dual crystalline measures. Let N ě 1 be an integer and r “ trdud|N be a sequence of reals indexed by the divisors of N such that


rd “ rN{d, ÿ

1 24 ÿ

rd “ 1 and

drd “ b,

d|N

d|N

where c ě 0. Consider the eta-quotient ηpr,zq “ ź

“ qb ÿ

αnqn.

ηpdzqr

d

ně0

d|N

The eta-function η : C` Ñ C is an holomorphic function that satisfies the functional identities ηpz ` ℓq “ eπiℓ{12ηpzq, for ℓ P Z, and ηp´1{zq “ az{iηpzq. In particular we obtain that

ηpr,z ` 1q “ e2πibηpr,zq

“ bz{pi

?

ź

“ ź

ηpr,´1{zq “ ź

Nqź

d{2

ηpz{dqr

pz{pdiqqr

ηp´d{zqr

ηpdz{Nqr

N{d

d

d

d|N

d|N

d|N

d|N

“ bz{pi

?

Nqηpr,z{Nq. Above we used that

ś

d{2 “ N´1{4, which follows from the conditions on rd. Etaquotients of this type are known to be weakly holomorphic functions of weight 1{2 on Γ0pNq (see [11, Prop. 1.39]). In particular, we conclude that the function

d|N d´r

?

ÿ

?

?

Nq “ qb{

αnqn{

N

N.

Fpr,zq “ ηpr,z{

něk

satisfies the functional equations Fpr,z `

?

Nq “ e2πibFpr,zq and ai{z Fpr,´1{zq “ Fpr,zq

for all z P C`. Since the function pImzq1{4|ηpr,zq| is Γ0pNq-invariant, one can straightforwardly deduce that |αn| ! nk, for some k ą 0, whenever ηpr,zq grows at most polynomially at all cusps of Γ0pNq (one can even obtain the Hecke-bound |αn| ! n1{4 if ηpr,zq vanishes exponentially at all cusps of Γ0pNq). This condition turns out to be equivalent to the verification of at most dpNq-linear inequalities given by20 [11, Lemma 1.40]. Assuming that such inequalities are satisfied, F satisfies the hypotheses of Lemma 20, and the measure

µ “ ÿ

N ` δ´?

αnpδ?

Nq satisfies µp “ µ.

?

?

2pn`bq{

2pn`bq{

ně0

It is now obvious that one can build infinitely many examples of self-dual crystalline measures µ by making linear combination of these types of eta-quotients.

20We are thankful to D. Radchenko for pointing this out.

For instance, consider now the following family

“ qc ˜1 ´ p24c ´ 2qq ` p288c2 ´ 36cqq2 ` ÿ

αn,cqn¸,

ηpzq24c´2ηp4zq24c´2 ηp2zq48c´5

ně3

which fits the previous discussion for N “ 4, pr1,r2,r4q “ p24c ´ 2,5 ´ 48c,24c ´ 2q and b “ c. We will have to impose c P r0,1{8s, as this range guarantees that the coefficients satisfy that Hecke bound |αn,c| ! n1{4, since it will be holomorphic at the cusps 0, i8 and 1{2 of Γ0p4q (actually, numerically, the coefficients αn,c seem to be bounded). The example above produces a measure µc such that

?

?

c ` nuně0. Note that µ0 is classical Poisson summation and µ1

µc “ µpc and supppµcq Ă t

c ` nuně0 Y t´

is Guinand’s example. Perhaps other interesting constructions may be derived from [29] and the references therein. It is not hard to show that tαn,cuně0 are polynomials in c with integer coefficients and degree n. To finish the discussion, note that if c is irrational then t

9

?c ` nuně0 intersects any infinite arithmetic progression at most 2 times. Indeed, having three hits implies that

?n3 ` c ´

?n1 ` c k1 “

?n2 ` c k2

?n2 ` c ´

is satisfied for some integers n3 ą n2 ą n1 ě 0 and k1,k2 ą 0. Writing A “ n2 ` c, n3 ` c “ A ` k3, n1 ` c “ A ´ k4 and solving for A, shows that A is rational, which is absurd.

Such measures are also connected with new Fourier interpolation formulae produced in [42], which as a byproduct produces crystalline pairs with space and spectral supports contained in t˘

?nuně0 Y tx0u, for any x0 not an integer square root. These nodes can also be perturbed to be t˘

?n ` εnuně0, as long as ε0 “ 0 and |εn| ď δn´5{4 for some small δ ą 0, see [44]. The recent papers [43, 27] also suggest that there should exist a crystalline pair with space and spectral supports contained in t˘p21αnqαuně0 and t˘p2p11´αqnq1´αuně0 respectively, whenever 0 ă α ă 1. Moreover, [27, Cor. 3] proves the striking result that for every (supercritical) pair of unbounded increasing sequences T “ ttjujPZ and S “ tsjujPZ such that

maxˆlimsup

|sj|q´1psj`1 ´ sjq˙ ă

- 1

- 2


### |tj|p´1ptj`1 ´ tjq,limsup

,

jÑ8

jÑ8

for some 1 ă p,q ă 8 with p1 ` 1q “ 1, there is a FS-pair pµ,aq with µ supported in T and ap¨q supported in S. An important simple example is again T “ t˘p2aαnqαuně0 and S “ t˘p2bβnqβuně0 for 0 ă α,β,a,b ă 1 with α ` β ď 1 (the multiplying constants a and b are irrelevant unless α`β “ 1, in which case we must impose ab ă 1, but conjecturally ab “ 1 is possible). In fact, pT ,Sq is both a Fourier uniqueness pair and has an associated reconstruction/interpolation formula (for more info see [27]).

- 8.5. Almost Crystalline Measures. We say pµ,aq is an almost Fourier summation pair (AFS-pair) if µ is strongly tempered, ap¨q is locally summable function and


pµp ´ aq|Cc8pRq “ ν|Cc8pRq, for some absolutely continuous complex-measure ν. In particular, if φ P Cc8pRq we have

apλqφpλq ` ż

φptqdνptq “ ż

ÿ

φpptqdµptq.

R

R

λPR

One way to think about this that ν is the absolutely continuous part of µp, while ap¨q is the (atomic) singular part. We then let the class ACM (Almost Crystalline Measures) denote the AFS-pairs pµ,aq such that both µ and ap¨q have locally finite support. The typical example is Guinand’s prime summation formula (also known as Riemann–Weil explicit formula), which states that for every φ P Cc8pRq we have

ˆφˆ

˙ ` φˆ´log n

˙˙ ´ 2ż

1 2π ÿ

logpπ{Nq 2π

Λpnqχpnq ?n

log n 2π

φp0q `

φptqcoshpπtqdt

2π

R

ně2

ż

“ ´ÿ

- 1

- 2π


φppγq `

φpptqReψp14 ` i2tqdt

R

γ

where ψpzq “ Γ1pzq{Γpzq is the digamma function, Λpnq is the von Mangoldt function, ρ “ 1{2 ` iγ are the zeros of the Dirichlet L-function

Lpχ,sq “ ÿ

χpnqn´s

ně1

on the critical strip 0 ă Reρ ă 1 and χ is a primitive, real and even Dirichlet character of modulus N. Since |ψp1{4`it{2q| ! logp2`|t|q and

ř

1`γ2 ă 8, we conclude, assuming the Riemann Hypothesis for Lpχ,sq, that if we let

1

γ

- 1

- 2π ÿ


logpπ{Nq 2π

Λpnqχpnq

?n p1logn

a “

10 `

` 1´logn

q

2π

2π

ně1

ν “ ´2coshpπtqdt µ “ ´ÿ

- 1

- 2π


δγ `

Reψp14 ` i2tqdt

γ

then pµ,aq P ACM. The difference of any two of such pairs above for two characters χ1 and χ2 real, even and primitive, but different moduli N, produces a pair in CM, this was pointed out first by Guinand [22], and we explain how this construction fits our framework in the end of Remark 6. Such measures are also connected with the remarkable new Fourier interpolation formulae produced in [15]. Assuming all non-trivial zeros of Lpχ,sq have real part 1{2 and are simple, these new formulae produce CM-pairs pµ,aq with supppµq “ tγ P R : Lpχ,1{2 ` iγq “ 0u Y tγ0u and supppaq “ tsgnpnqlog4π|n|uně1, where γ0 is any real such that Lpχ,1{2 ` iγ0q ‰ 0.

Acknowledgments

We thank Oleksiy Klurman and Bryce Kerr for all the conversations we had around this topic during their visit to Rio. Theorems do come out of the smoke. We thank Friedrich Littmann for the fruitful conversations and comments which inspired Theorem

- 5. We also thank Michael Baake and Peter Sarnak for further discussions, references and remarks after the first version of this paper. The author acknowledges support from the following funding agencies: The Office of Naval Research GRANT14201749 (award number N629092412126), The Serrapilheira Institute (Serra-2211-41824), FAPERJ (E26/200.209/2023) and CNPq (309910/2023-4).


References

- [1] L. Alon, A. Cohen and C. Vinzant, Every real-rooted exponential polynomial is the restriction of a Lee-Yang polynomial, arXiv:2303.03201.
- [2] L. Alon and C. Vinzant, Gap distributions of Fourier quasicrystals via Lee-Yang polynomials, arXiv:2307.13498.
- [3] L. Amerio and G. Prouse, Almost-periodic functions and functional equations, Van Nostrand Reinhold Company, New York, 1971.
- [4] M. Baake and N. Strungaru, A note on tempered measures, Colloquium Mathematicum 172 (2023), 15-30.
- [5] A. Baranov. Differentiation in de Branges spaces and embedding theorems. J. Math. Sci. 101 no. 2, (2002), 2881 – 2913.
- [6] A. Baranov. Estimates of the Lp-norms of derivatives in spaces of entire functions. J. Math. Sci. 129 no. 4, (2005). 3927 – 3943.
- [7] M. Baake and U. Grimm (eds), Aperiodic Order Volume 1: A Mathematical Invitation, Cambridge University Press, October 2017.
- [8] M. Baake and U. Grimm (eds), Aperiodic Order Volume 2: Crystallography and Almost Periodicity, Cambridge University Press, October 2017.
- [9] M. Baake, N. Strungaru and V. Terauds, Pure point measures with sparse support and sparse Fourier–Bohr support, Trans. London Math. Soc. 7 (2020), 1-32.
- [10] A. S. Besicovitch, Almost Periodic Functions, Dover Publications, 1954 - Fourier series - 180 pages.
- [11] S. Bhattacharya, Factorization of holomorphic eta quotients, Ph.D thesis, Rheinische FriedrichWilhelms-Universit¨t Bonn, 2014.
- [12] V. Blomer and G. Harcos. Hybrid bounds for twisted L-functions. J. Reine Angew. Math., 621:53–79, 2008.
- [13] L. de Branges. Hilbert spaces of entire functions. Prentice Hall, Englewood Cliffs. NJ, 1968.
- [14] R.P. Boas, Entire Functions, Academic Press, New York, 1954.
- [15] A. Bondarenko, D. Radchenko and K. Seip, Fourier Interpolation with Zeros of Zeta and LFunctions, Constructive Approximation (2023) 57:405-461.
- [16] H. Bohr, Zur Theorie der fastperiodischen Funktionen I, Acta Math. 45 (1925), p. 29-127.
- [17] H. Cohn and F. Gon¸calves, An optimal uncertainty principle in twelve dimensions via modular forms, Inventiones Mathematicae 217 (2019), 799-831.
- [18] F. Dyson, Birds and frogs, Notices Amer. Math. Soc. 56 (2009), no. 2, 212-223.
- [19] S. Deloudi and S. Walter, Crystallography of Quasicrystals: Concepts, Methods and Structures, Springer Series in Materials Science 126 (2012).


- [20] J. B. Garnett, Bounded Analytic Functions, Graduate Texts in Mathematics, Springer New York, NY., 2007.
- [21] F. Gon¸calves and F. Littmann, Interpolation Formulas with Derivatives in De Branges Spaces II. J. Math. Anal. Appl. 458 (2018), issue 2, p. 1091-1114.
- [22] A. P. Guinand, Concordance and the harmonic analysis of sequences, Acta Math. 101(3-4): 235-271

(1959).

- [23] A. E. Ingham. A Note on Fourier Transforms. J. London Math. Soc., 9(1):29–32, 1934.
- [24] K. Jaganathan, Y. C. Eldar and B. Hassibi, Phase Retrieval: An Overview of Recent Developments, Optical Compressive Imaging, pp. 264-292 (2016).
- [25] M.G. Krein, A contribution to the theory of entire functions of exponential type, Bull. Acad. Sci. URSS. S6r. Math. [Izvestiya Akad. Nauk. SSSR] 11 (1947) 309-326.
- [26] P. Kurasov and P. Sarnak, Stable polynomials and crystalline measures, Journal of Mathematical Physics, 61(8):083501, 2020.
- [27] A. Kulikov, F. Nazarov and M. Sodin, Fourier uniqueness and non-uniqueness pairs, arXiv:2306.14013v1.
- [28] J. C. Lagarias, Mathematical quasicrystals and the problem of diffraction. In Directions in Mathematical Quasicrystals, Baake M. and Moody R.V. (eds.), (2000), pp. 161-193 (AMS, Providence, RI).
- [29] R.J. Lemke Oliver, Eta-quotients and theta functions, Advances in Mathematics 241 (2013) 1-17.
- [30] N. Lev and A. Olevskii, Fourier quasicrystals and discreteness of the diffraction spectrum, Adv. Math. 315 (2017), 1-26.
- [31] N. Lev and A. Olevskii, Quasicrystals and Poisson’s summation formula. Invent. math. 200, 585–606

(2015).

- [32] B. Ja. Levin, Distribution of Zeros of Entire Functions, Translations of Mathematical Monographs Vol. 5, American Mathematical Soc., 1964.
- [33] B. Ja. Levin, Lectures on Entire Functions, Translations of Mathematical Monographs 150, American Mathematical Society 1996.
- [34] B.M. Levitan and V.V. Zhikov, Almost periodic functions and differential equations, Cambridge University Press, 1983.
- [35] Y. Meyer, Nombres de Pisot, nombres de Salem et analyse harmonique, Lecture Notes in Mathematics, Vol. 117, Springer-Verlag, Berlin-New York, 1970 (French). Cours Peccot donne au Coll‘ege de France en avril-mai 1969.
- [36] Y. Meyer, Quasicrystals, Diophantine approximation and algebraic numbers Beyond quasicrystals (Les Houches, 1994), Springer, Berlin 1995.
- [37] Y. Meyer, Measures with locally finite support and spectrum, Proc. Natl. Acad. Sci. USA 113

(2016), 3152-3158.

- [38] Y. Meyer, Quasicrystals, Almost Periodic Patterns, Mean-periodicFunctions and Irregular Sampling, Afr. Diaspora J. Math. (N.S.) 13 (1), 1-45, (2012)
- [39] R.V. Moody, Model Sets: A Survey, In: Axel, F., D´enoyer, F., Gazeau, JP. (eds) From Quasicrystals to More Complex Systems. Centre de Physique des Houches, vol 13. Springer, Berlin, Heidelberg.
- [40] A. Olevskii and A. Ulanovskii, Fourier quasicrystals with unit masses, Comptes Rendus, Math´ematique, 358(11-12):1207–1211, 2020.
- [41] A. Olevskii and A. Ulanovskii, A simple crystalline measure, arXiv:2006.12037v2 .
- [42] D. Radchenko and M. Viazovska, Fourier interpolation on the real line, Publ. Math. IHES 129


(2019), 51–81.

- [43] J. Ramos and M. Sousa, Fourier uniqueness pairs of powers of integers, J. Eur. Math. Soc. (JEMS) 24 (2022), no. 12, 4327-4351.
- [44] J. Ramos and M. Sousa, Perturbed interpolation formular and applications, To appear in Analysis & PDE.
- [45] S. Ritsch, O. Radulescu, C. Beeli, D.H. Warrington, R. Luck and K. Hiraga, A stable onedimensional quasicrystal related to decagonal Al-Co-Ni, Philosophical Magazine Letters Volume 80, 2000 - Issue 2, Pages 107-118.
- [46] D. Shechtman, I. Blech, D. Gratias, and J. W. Cahn, Metallic Phase with Long-Range Orientational Order and No Translational Symmetry Phys. Rev. Lett. 53, 1951 (1984).


The University of Texas at Austin, 2515 Speedway, Austin, TX 78712, USA

& IMPA - Instituto de Matematica´ Pura e Aplicada, Rio de Janeiro, 22460-320, Brazil. Email address: felipe.ferreiragoncalves@austin.utexas.edu Email address: goncalves@impa.br

