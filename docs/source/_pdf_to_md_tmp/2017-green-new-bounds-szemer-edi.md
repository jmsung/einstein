arXiv:1705.01703v3[math.CO]10Aug2017

NEW BOUNDS FOR SZEMEREDI’S´ THEOREM, III: A POLYLOGARITHMIC BOUND FOR r4(N)

BEN GREEN AND TERENCE TAO

Abstract. Deﬁne r4(N) to be the largest cardinality of a set A ⊂ {1, . . . , N} which does not contain four elements in arithmetic progression. In 1998 Gowers proved that

r4(N) ≪ N(log log N)−c for some absolute constant c > 0. In 2005, the authors improved this to

√loglogN. In this paper we further improve this to

![image 1](<2017-green-new-bounds-szemer-edi_images/imageFile1.png>)

r4(N) ≪ Ne−c

r4(N) ≪ N(log N)−c, which appears to be the limit of our methods.

Contents

- 1. Introduction 1
- 2. Notation 3
- 3. High-level overview of argument 5
- 4. Bohr sets 18
- 5. Dilated tori 34
- 6. Constructing the approximants 37
- 7. Bad lower bound implies dimension decrement 40
- 8. Bad approximation implies energy decrement 50
- 9. Local inverse U3 theorem 59 References 93


1. Introduction Let N 100 be a natural number (so that log log N is positive). If k 3

is a natural number we deﬁne rk(N) to be the largest cardinality of a set A ⊂ [N] := {1,... ,N} which does not contain an arithmetic progression of k distinct elements.

Klaus Roth proved in 1953 [34] that r3(N) ≪ N(log log N)−1, and so in particular1 r3(N) = o(N) as N → ∞. Since Szemere´di’s 1969 proof [41] that r4(N) = o(N), and his later proof [42] that rk(N) = ok(N) for k 5

![image 2](<2017-green-new-bounds-szemer-edi_images/imageFile2.png>)

1See Section 2 for the asymptotic notation used in this paper.

1

(answering a question from [10]), it has been natural to ask for similarly eﬀective bounds for these quantities. It is worth noting that the famous conjecture of Erd˝os [9] asserting that every set of natural numbers whose sum

n)

of reciprocals is divergent is equivalent to the claim that ∞n=1 rk(2

2n < ∞ for all k 3 (see [48, Exercise 10.0.6]).

![image 3](<2017-green-new-bounds-szemer-edi_images/imageFile3.png>)

A ﬁrst attempt towards quantitative bounds for higher k was made by Roth in [35], who provided a new proof that r4(N) = o(N). A major breakthrough was made in 1998 by Gowers [12, 13], who obtained the

bound rk(N) ≪k N(log log N)−ǫk for each k 4, where ǫk := 1/22k+9. In the other direction, a classical result of Behrend [3] shows that r3(N) ≫ N exp(−c√log N) for some absolute constant c > 0 (see [8, 29] for a slight reﬁnement of this bound), and in [33] (see also [31]) the argument was generalised to give the bound r1+2k(N) ≫k N exp(−clog1/(k+1) N) for any k 1.

![image 4](<2017-green-new-bounds-szemer-edi_images/imageFile4.png>)

In the meantime, there has been progress on r3(N). Szemere´di (unpublished) obtained the bound r3(N) ≪ Ne−c

√log logN, and shortly thereafter Heath-Brown [30] and Szemere´di [44] independently obtained the bound r3(N) ≪ N(log N)−c for some absolute constant c > 0. The best known value of c has been improved in a series of papers [4, 6, 7, 37, 38]. Sanders [38] was the ﬁrst to show that any c < 1 is admissible, and Bloom [4] improved the factor of log log N in Sanders’s bound.

![image 5](<2017-green-new-bounds-szemer-edi_images/imageFile5.png>)

The only other direct progress on upper bounds for rk(N) is our previous paper [26], obtaining the bound r4(N) ≪ Ne−c

√log logN. The main objective of this paper is to obtain a bound for r4(N) of the same quality as the HeathBrown and Szemere´di bound for r3(N).

![image 6](<2017-green-new-bounds-szemer-edi_images/imageFile6.png>)

Theorem 1.1. We have r4(N) ≪ N(log N)−c for some absolute constant c > 0.

An analogous result in ﬁnite ﬁelds was claimed (and published [22]) by us around twelve years ago, although an error in this paper came to light some years later. This was corrected around 5 years ago in [23]. These papers (like almost all of the previously cited quantitative results on rk(N)) are based on the density increment argument of Roth [34]. However we will use a slightly diﬀerent “energy decrement” and “regularity” approach here, inspired by the Khintchine-type recurrence theorems for length four progressions established by Bergelson-Host-Kra [2] in the ergodic setting, and by the authors [19] in the combinatorial setting.

Acknowledgments. The ﬁrst author is supported by a Simons Investigator grant. The second author is supported by a Simons Investigator grant, the James and Carol Collins Chair, the Mathematical Analysis & Application Research Fund Endowment, and by NSF grant DMS-1266164. Part of this paper was written while the authors were in residence at MSRI in Spring 2017, which is supported by NSF grant DMS-1440140.

We are indebted to the anonymous referee for helpful corrections and suggestions. Finally, we would like to thank any readers interested in the

result of this paper for their patience. Most of the argument was worked out by us in 2005, and the result was claimed in [26], dedicated to Roth’s 80th birthday. Whilst a complete, though not very readable, version has been available on request since around 2012, it has taken us until now to create a potentially publishable manuscript.

2. Notation We use the asymptotic notation X ≪ Y or X = O(Y ) to denote |X| CY for some constant C. Given an asymptotic parameter N going to inﬁnity, we use X = o(Y ) to denote the bound |X| c(N)Y for some function c(N) of N that goes to zero as N goes to inﬁnity. We also write X ≍ Y

for X ≪ Y ≪ X. If we need the implied constant C or decay function c() to depend on an additional parameter, we indicate this by subscripts, e.g. X = ok(Y ) denotes the bound |X| ck(N)Y for a function ck(N) that goes to zero as N → ∞ for any ﬁxed choice of k.

We will frequently use probabilistic notation, and adopt the convention that boldface variables such as a or r represent random variables, whereas non-boldface variables such as a and r represent deterministic variables (or constants). We write P(E) for the probability of a random event E, and EX and Var X for the expectation and variance of a real or complex random

variable X; we also use E(X|E) = EPX(E1E) for the conditional expectation of X relative to an event E of non-zero probability, where of course 1E denotes the indicator variable of E. In this paper, the random variables X of which we will compute expectations of will be discrete, in the sense that they take only ﬁnitely many values, so there will be no issues of measurability. The essential range of a discrete random variable X is the set of all values X for which P(X = X) is non-zero.

![image 7](<2017-green-new-bounds-szemer-edi_images/imageFile7.png>)

By a slight abuse of notation, we also retain the traditional (in additive combinatorics) use for E as an average, thus Ea∈Af(a) := |A1| a∈A f(a) for any ﬁnite non-empty set A and function f : A → C, where we use |A| to denote the cardinality of A. Thus for instance Ea∈Af(a) = Ef(a) if a is drawn uniformly at random from A.

![image 8](<2017-green-new-bounds-szemer-edi_images/imageFile8.png>)

A function f : A → C is said to be 1-bounded if one has |f(a)| 1 for all a ∈ A. We will frequently rely on the following probabilistic form of the Cauchy-Schwarz inequality, the proof of which is an exercise.

- Lemma 2.1 (Cauchy-Schwarz). Let A,B be sets, let f : A → C be a 1bounded function, and let g : A × B → C be another function. Let a,b,b′ be discrete random variables in A,B,B′ respectively, such that b′ is a conditionally independent copy of b relative to a, that is to say that


P(b = b,b′ = b′|a = a) = P(b = b|a = a)P(b = b′|a = a) for all a in the essential range of a and all b,b′ ∈ B. Then we have |Ef(a)g(a,b)|2 Eg(a,b)g(a,b′). (2.1)

![image 9](<2017-green-new-bounds-szemer-edi_images/imageFile9.png>)

We will think of this lemma as allowing one to eliminate a factor f(a) from a lower bound of the form |Ef(a)g(a,b)| η, at the cost of duplicating the factor g, and worsening the lower bound from η to η2.

We also have the following variant of Lemma 2.1:

- Lemma 2.2 (Popularity principle). Let a be a random variable taking values in a set A, and let f : A → [−C,C] be a function for some C > 0. If we have


Ef(a) η for some η > 0 then, with probability at least 2ηC , the random variable a attains a value a ∈ A for which f(a) η2. Proof. If we set Ω := {a ∈ A : f(a) η/2}, then

![image 10](<2017-green-new-bounds-szemer-edi_images/imageFile10.png>)

![image 11](<2017-green-new-bounds-szemer-edi_images/imageFile11.png>)

η 2

+ C1a∈Ω and hence on taking expectations

f(a)

![image 12](<2017-green-new-bounds-szemer-edi_images/imageFile12.png>)

Ef(a)

η 2

+ CP(a ∈ Ω).

![image 13](<2017-green-new-bounds-szemer-edi_images/imageFile13.png>)

This implies that

P(a ∈ Ω) η/2C giving the claim.

If θ ∈ R, we write θ R/Z for the distance from θ to the nearest integer, and e(θ) = e2πiθ. Observe from elementary trigonometry that

|e(θ) − 1| = 2|sin(πθ)| ≍ θ R/Z (2.2) and hence also

1 − cos(2πθ) = 2|sin(πθ)|2 ≍ θ 2R/Z. (2.3) We will also use the triangle inequalities

θ1 + θ2 R/Z θ1 R/Z + θ2 R/Z; kθ R/Z |k| θ R/Z (2.4)

for θ1,θ2 ∈ R/Z and k ∈ Z frequently in the sequel, often without further comment.

For any prime p, we (by slight abuse of notation) let a  → ap be the obvious homomorphism from Z/pZ to R/Z that maps a(mod p) to ap(mod 1) for any integer a. We then deﬁne ep : Z/pZ → C to be the character

![image 14](<2017-green-new-bounds-szemer-edi_images/imageFile14.png>)

![image 15](<2017-green-new-bounds-szemer-edi_images/imageFile15.png>)

a p

= e2πia/p

ep(a) := e

![image 16](<2017-green-new-bounds-szemer-edi_images/imageFile16.png>)

of Z/pZ.

3. High-level overview of argument

We will establish Theorem 1.1 by establishing the following result, related to the Khintchine-type recurrence theorems mentioned earlier. It will be convenient to introduce the notation

Λa,r(f) := Ef(a)f(a + r)f(a + 2r)f(a + 3r) whenever a,r are random variables on Z/pZ and f : Z/pZ → [−1,1] is a random function; of course, the notation can also be applied to deterministic functions f : Z/pZ → [−1,1]. Later on we will also need the conditional variant

Λa,r(f|E) := E(f(a)f(a + r)f(a + 2r)f(a + 3r)|E) (3.1) for some events E of non-zero probability. Informally, this quantity counts the density of arithmetic progressions a,a + r,a + 2r,a + 3r on the event E weighted by f, where a,r need not be drawn uniformly or independently (and f may also be coupled to a,r).

Theorem 3.1. Let p be a prime, let η be a real number with 0 < η

- 1 10, and let f : Z/pZ → [−1,1] be a function. Then there exist random variables a,r ∈ Z/pZ, not necessarily independent, obeying the near-uniform distribution bound


![image 17](<2017-green-new-bounds-szemer-edi_images/imageFile17.png>)

Ef(a) = Ex∈Z/pZf(x) + O(η), (3.2) the recurrence property

Λa,r(f) (Ef(a))4 − O(η), (3.3) and the “thickness” bound

P(r = 0) ≪ exp(−η−O(1))/p. (3.4)

We note that a variant of Theorem 3.1 was established by us in [19] (answering a question in [2]), in which the random variable a was uniformly distributed in Z/pZ, the random variable r was uniformly distributed in a subset of Z/pZ of size ≫η p and was independent of a, and the condition (3.4) (which is crucial to the quantitative bound in Theorem 1.1) was not present. Compared to that result, Theorem 3.1 obtains the much more quantitative bound (3.4), but at the expense of no longer enforcing independence between a and r. The use of non-independent random variables a,r is an innovation of this current paper; it is similar to the technique in previous papers of using “factors” (ﬁnite partitions) to break up the domain Z/pZ into smaller “atoms” such as Bohr sets and analysing each atom separately. However there will be technical advantages from the more general framework of pairs of independent random variables a,r. In particular we will be able to avoid some of the boundary issues arising from irregularity of Bohr sets, by using the smoother device of “regular probability distributions” associated to such sets. Although f is allowed to attain negative values in Theorem 3.1, in our applications we shall only be concerned with the case when f is non-negative.

Let us now see how Theorem 1.1 follows from Theorem 3.1. Clearly we may assume that N 100. Suppose that A is a subset of {1,... ,N} without any non-trivial four-term arithmetic progressions. By Bertrand’s postulate, we may ﬁnd a prime p between (say) 2N and 4N. If we deﬁne f : Z/pZ → [−1,1] to be the indicator function 1A of A (viewed as a subset of Z/pZ), then we have

Ex∈Z/pZf(x) = |A| p

(3.5) and also

![image 18](<2017-green-new-bounds-szemer-edi_images/imageFile18.png>)

f(a)f(a + r)f(a + 2r)f(a + 3r) = 0 (3.6)

whenever a,r ∈ Z/pZ with r non-zero. Now let a,r be as in Theorem 3.1, with η to be chosen later. From (3.2), (3.3), (3.5) we have

Λa,r(f) |A| p

![image 19](<2017-green-new-bounds-szemer-edi_images/imageFile19.png>)

4

− O(η).

But by (3.6), (3.4), the left-hand side is O(exp(−η−O(1))/p). Setting η := clog−c p for a suﬃciently small absolute constant c > 0, we conclude that

|A| p

![image 20](<2017-green-new-bounds-szemer-edi_images/imageFile20.png>)

4

≪ log−c p

and hence A ≪ N log−c/4 N, giving Theorem 1.1.

Remark. As mentioned previously, the arguments in [19] established a bound of the form (3.3) with a and r independent, and also one could ensure that a was uniformly distributed over Z/pZ. As a consequence, one could establish a variant of Theorem 1.1, namely that for any N 1, η > 0, and A ⊂ [N], one had

4

|A| N

|A ∩ (A − r) ∩ (A − 2r) ∩ (A − 3r)| N

− η

![image 21](<2017-green-new-bounds-szemer-edi_images/imageFile21.png>)

![image 22](<2017-green-new-bounds-szemer-edi_images/imageFile22.png>)

for ≫η N choices of 0 r N. Unfortunately our methods do not seem to provide a good bound of this form due to our coupling together of a and r.

It remains to establish Theorem 3.1. As in [2, 19], the lower bound (3.3) will ultimately come from the following consequence of the Cauchy-Schwarz inequality which counts solutions to the equation x − 3y + 3z − w = 0 for x,y,z,w in some subset of a compact abelian group; this inequality is a speciﬁc feature of the theory of length four progressions which is not available for longer progressions2.

![image 23](<2017-green-new-bounds-szemer-edi_images/imageFile23.png>)

- 2For longer progressions, the relevant constraints coming from nilpotent algebra are signiﬁcantly more complicated than a single linear equation; see [53]. In any event, the counterexamples in [2] indicate that no comparable positivity property with polynomial lower bounds will hold for higher length progressions.


Lemma 3.2 (Application of Cauchy-Schwarz). Let G = (G,+) be a compact abelian group, let µ be the probability Haar measure on G, and let F : G → R be a bounded measurable function. Then

F(x)F(y)F(z)F(x − 3y + 3z) dµ(x)dµ(y)dµ(z)

G G G

Fdµ

G

4

.

Proof. Making the change of variables w = x − 3y and using Fubini’s theorem, the left-hand side may be rewritten as

2

dµ(w), which by the Cauchy-Schwarz inequality is at least

F(w + 3y)F(y) dµ(y)

G G

F(w + 3y)F(y) dµ(y)dµ(w)

G G

2

.

But by a further application of Fubini’s theorem, the expression inside the square is ( G F(x) dµ(x))2. The claim follows.

To see the relevance of this lemma to Theorem 3.1, and to motivate the strategy of proof of that theorem, let us ﬁrst test that theorem on some key examples. To simplify the exposition, our discussion will be somewhat nonrigorous in nature; for instance, we will make liberal use of the non-rigorous symbol ≈ without quantifying the nature of the approximation.

Example 1: a well-distributed pure quadratic factor. Let G be the dtorus G = (R/Z)d for some bounded d = O(1), and let F : G → [−1,1] be a smooth function (independent of p); for instance, F could be a ﬁnite linear combination of characters χ : G → S1 of G. Let α1,... ,αd ∈ Z/pZ be “generic” frequencies, in the sense that there are no non-trivial linear relations of the form

k1α1 + ··· + kdαd = 0 (3.7)

with k1,... ,kd = O(1) not all equal to zero. We also introduce some additional frequencies β1,... ,βd ∈ Z/pZ, for which we impose no genericity restrictions. Let f : Z/pZ → [−1,1] be the function

f(a) := F (Q(a)) where Q : Z/pZ → G is the quadratic polynomial

αda2 + βda p

α1a2 + β1a p

Q(a) :=

,... ,

,

![image 24](<2017-green-new-bounds-szemer-edi_images/imageFile24.png>)

![image 25](<2017-green-new-bounds-szemer-edi_images/imageFile25.png>)

and where we use the obvious division by zero map a  → ap from Z/pZ to R/Z. For any tuples k = (k1,... ,kd) ∈ Zd ≡ Gˆ and ξ = (ξ1,... ,ξd) ∈ G, we deﬁne the dot product

![image 26](<2017-green-new-bounds-szemer-edi_images/imageFile26.png>)

k · ξ := k1ξ1 + ··· + kdξd.

Because of our genericity hypothesis on the αi, we see from Gauss sum estimates that

Ea∈Z/pZe(k · Q(a)) ≈ 0 for any bounded tuple k ∈ Zd when p is large. By the Weyl equidistribution criterion, we thus see that when p is large, the quantity αa2p+βa becomes equidistributed in G as a ranges over Z/pZ. In particular, as F was assumed to be smooth, we expect to have

![image 27](<2017-green-new-bounds-szemer-edi_images/imageFile27.png>)

Ef(a) = Ea∈Z/pZf(a) ≈

F(x) dµ(x)

G

if a is drawn uniformly in Z/pZ. Now suppose that r is also drawn uniformly in Z/pZ, independently of a. The tuple

(Q(a),Q(a + r),Q(a + 2r),Q(a + 3r)) (3.8)

will not become equidistributed in G4, because of the elementary algebraic identity

Q(a) − 3Q(a + r) + 3Q(a + 2r) − Q(a + 3r) = 0, (3.9) which is a discrete version of the fact that the third derivative of any quadratic polynomial vanishes. However, this turns out to be the only constraint on this tuple in the limit p → ∞. Indeed, from the genericity hypothesis on the αi, one can verify that the quadratic form

(a,r)  → k0 · Q0(a) + k1 · Q0(a + r) + k2 · Q0(a + 2r) + k3 · Q0(a + 3r)

on (Z/pZ)2 for bounded tuples k0,k1,k2,k3 ∈ Zd vanishes if and only if (k0,k1,k2,k3) is of the form (k,−3k,3k,−k) for some tuple k, where

αda2 p denotes the purely quadratic component of Q(a). Using this and a variant of the Weyl equidistribution criterion, one can eventually compute that

α1a2 p

Q0(a) :=

,... ,

![image 28](<2017-green-new-bounds-szemer-edi_images/imageFile28.png>)

![image 29](<2017-green-new-bounds-szemer-edi_images/imageFile29.png>)

F(x)F(y)F(z)F(x − 3y + 3z) dµ(x)dµ(y)dµ(z).

Λa,r(f) ≈

G G G

Applying Lemma 3.2, we conclude (a heuristic version of) Theorem 3.1 in this case, taking a,r to be independent uniformly distributed variables on Z/pZ.

Example 2. A well-distributed impure quadratic factor. Now we give a “local” version of the ﬁrst example, in which the function f exhibits “locally quadratic” behaviour rather than “globally quadratic” behaviour. Let η > 0 be a small parameter, and suppose that p is very large compared to η. We suppose that the cyclic group Z/pZ is somehow partitioned into a number P1,... ,Pm of arithmetic progressions; the number m of such progressions should be thought of as being moderately large (e.g. m ∼ exp(1/ηO(1)) for some parameter η > 0). Consider one such progression, say Pc = {bc +nsc : 1 n Nc} for some bc,sc ∈ Z/pZ and some Nc > 0; one should think

of Nc as being reasonably large, e.g. Nc ≫ exp(−1/ηO(1))p. To each such progression Pc, we associate a torus Gc = (R/Z)dc for some bounded dc with probability Haar measure µc, a smooth function Fc : Gc → [−1,1], and a collection ξc,1,... ,ξc,dc ∈ R/Z of frequencies which are generic in the sense that there does not exist any non-trivial relations of the form

k1ξc,1 + ··· + kdcξc,dc = O

1 Nc

![image 30](<2017-green-new-bounds-szemer-edi_images/imageFile30.png>)

(mod 1) (3.10)

for bounded k1,... ,kdc ∈ Z. We then deﬁne the function f : Z/pZ → [−1,1] by setting

f(bc + nsc) := Fc(ξc,d1n2,... ,ξc,dcn2) for 1 c m and 1 n Nc. One could also add a lower order linear term to the phases ξc,in2, as in the preceding example, if desired, but we will not do so here to simplify the exposition slightly.

Within each progression Pc, a Weyl equidistribution analysis (using the genericity hypothesis) reveals that the tuple (ξc,d1n2,... ,ξc,dcn2) becomes equidistributed in Gc as p becomes large, so that

Ea∈Pcf(a) ≈

Fc(x) dµc(x). (3.11)

Gc

Now we deﬁne the random variables a,r ∈ Z/pZ as follows. We ﬁrst select a random element c from {1,... ,m} with P(c = c) = |Pj|/p for c = 1,... ,m. Conditioning on the event that c is equal to c, we then select a uniformly at random from Pc, and also select r uniformly at random from an arithmetic progression of the form

{nsc : |n| exp(−1/η−C)Nc}, (3.12)

with a and r independent after conditioning on c = c. Note that a and r are only conditionally independent, relative to the auxiliary variable c; if one does not perform this conditioning, then a and r become coupled to each other through their mutual dependence on c.

Without conditioning on c, the random variable a becomes uniformly distributed on Z/pZ, thus

Ef(a) = Ea∈Z/pZf(a). Also, from (3.11) we have the conditional expectation

E(f(a)|c = c) ≈

Fc(x) dµc(x).

Gc

A modiﬁcation of the equidistribution analysis from the ﬁrst example also gives

Λa,r(f|c = c)

Fc(x)Fc(y)Fc(z)F(x − 3y + 3z) dµc(x)dµc(y)dµc(z),

Gc Gc Gc

where the conditional quartic form Λa,r(f|c = c) was deﬁned in (3.1), and hence by Lemma 3.2 we have

Λa,r(f|c = c) (E(f(a)|c = c))4 . Averaging in c (weighted by P(c = c)) to remove the conditional expectation on the left-hand side, and then applying H¨older’s inequality, we obtain a heuristic version of Theorem 3.1 in this case.

Example 3: A poorly distributed pure quadratic factor. We now return to the situation of the ﬁrst example, except that we no longer impose the genericity hypothesis, that is to say we allow for a non-trivial relation of the form (3.7). Without loss of generality we can take the coeﬃcient kd of this relation to be non-zero. Because of this relation, the quantity Q(a) studied in the ﬁrst example and the tuple (3.8) may not necessarily be as equidistributed as before. However, we can use this irregularity of distribution to modify the representation of f (up to a small error) in such a manner as to reduce the number d of quadratic phases involved. Namely, we can write

γa p where

f(a) := F˜ Q ˜(a),

![image 31](<2017-green-new-bounds-szemer-edi_images/imageFile31.png>)

kd−1αd−1a2 + kd−1βd−1a p γ := βd + k1kd−1β1 + ··· + kd−1kd−1βd−1

kd−1α1a2 + kd−1β1a p

Q˜(a) :=

,... ,

![image 32](<2017-green-new-bounds-szemer-edi_images/imageFile32.png>)

![image 33](<2017-green-new-bounds-szemer-edi_images/imageFile33.png>)

F˜(x1,... ,xd−1,y) := F(kdx1,... ,kdxd−1,−k1x1 − ··· − kd−1xd−1 + y)

and where we take advantage of the ﬁeld structure of Z/pZ to locate an inverse kd−1 of kd in this ﬁeld. For our quantitative analysis we will run into a technical diﬃculty with this representation, in that the Lipschitz constant of F˜ will increase by an undesirable amount compared to that of F when one performs this change of variable, at least if one uses the standard metric on the torus. To ﬁx this, we will eventually have to work with more general tori di=1 R/λiZ than the standard torus (R/Z)d, but we ignore this issue for now to continue with the heuristic discussion.

To remove the dependence on the linear phase γap , we partition Z/pZ into “(shifted) Bohr sets” B1,... ,Bm for some moderately large m (e.g. m ∼ exp(1/η−C) for some constant C > 0), deﬁned by

![image 34](<2017-green-new-bounds-szemer-edi_images/imageFile34.png>)

γa p ∈

c − 1 m

c m

Bc := a ∈ Z/pZ :

,

(mod 1) for c = 1,... ,m. On each Bohr set Bc, we have the approximation f(a) := F˜c(Q˜(a))

![image 35](<2017-green-new-bounds-szemer-edi_images/imageFile35.png>)

![image 36](<2017-green-new-bounds-szemer-edi_images/imageFile36.png>)

![image 37](<2017-green-new-bounds-szemer-edi_images/imageFile37.png>)

where F˜c(x,y) := F˜(x, mc ). Using the heuristic that Bohr sets behave like arithmetic progressions, the situation is now similar to that in the second

![image 38](<2017-green-new-bounds-szemer-edi_images/imageFile38.png>)

example, with the number of quadratic phases involved reduced from d to d − 1, except that there may still be some non-trivial relations amongst the surviving quadratic phases (and one also now has some lower order linear terms in the quadratic phases). To deal with this diﬃculty, we turn now to the consideration of yet another example.

Example 4: A poorly distributed impure quadratic factor. We now consider an example which is in some sense a combination of the second and third examples. Namely, we suppose we are in the same situation as in the second example, except that we allow some of the indices c to have “poor quadratic distribution” in the sense that they admit non-trivial relations of the form (3.10). Again we may assume without loss of generality that kdc is non-zero in such relations. Because of such relations, we no longer expect to have the equidistribution properties that were used in the second example. However, by modifying the calculations in the third example, we can obtain a new representation of f (again allowing for a small error) on each of the progressions Pc with poor quadratic distribution in order to reduce the number dc of quadratic polynomials used in that progression by one. Iterating this process a ﬁnite number of times, one eventually returns to the situation in the second example in which no non-trivial relations occur, at which point one can (heuristically, at least) verify Theorem 3.1 in this case.

The situation becomes slightly more complicated if one adds a lower order linear term ζc,in to the purely quadratic phases ξc,in2 appearing in the second example; this basically is the type of situation one encounters for instance at the conclusion of the third example. In this case, every time one converts a non-trivial relation of the form (3.10) on one of the cells Pc of the partition into a new representation of f on that cell, one must subdivide that cell Pj into smaller pieces, by intersecting Pj with various Bohr sets. However, the resulting sets still behave somewhat like arithmetic progressions, and it turns out that we can still iterate the construction a bounded number of times until no further non-trivial relations between surviving quadratic phases remain on any of the cells of the partition, at which point one can (heuristically, at least) verify Theorem 3.1 in this case (as well as in the case considered in the third example).

Example 5: A pseudorandom perturbation of a pure quadratic factor. In all the preceding examples, the function f : Z/pZ → [−1,1] under consideration was “locally quadratically structured”, in the sense that on local regions such as Pc, the function f could be accurately represented in terms of quadratic phase functions a  → Q(a). This is however not the typical behaviour expected for a general function f : Z/pZ → [−1,1]. A more representative example would be a function of the form

f(a) := f1(a) + f2(a),

where f1 : Z/pZ → R is a function of the type considered in the ﬁrst example, thus

f1(a) = F(Q(a)) for some quadratic function Q : Z/pZ → G into a torus G = (R/Z)d and some smooth F : G → [−1,1], and f2 : Z/pZ → [−1,1] is a function which is globally Gowers uniform in the sense that

E

f2(a + ω1h1 + ω2h2 + ω3h3) ≈ 0, (3.13)

(ω1,ω2,ω3)∈{0,1}3

where a,h1,h2,h3 are drawn independently and uniformly at random from Z/pZ. A typical example to keep in mind is when F (and hence f1) takes values in [0,1], and f = f is a random function with f(a) equal to 1 with probability f1(a) and 0 with probability 1−f1(a), independently as a ∈ Z/pZ varies; then the f2(a) for a ∈ Z/pZ become independent random variables of mean zero, and the global Gowers uniformity can be established with high probability using tools such as the Chernoﬀ inequality.

From the standard theory of the Gowers norms (see e.g. [48, Chapter 11]), one can use the global Gowers uniformity of f2, combined with a number of applications of the Cauchy-Schwarz inequality, to establish a “generalised von Neumann theorem” which, in our current context, implies that f and

- f1 globally count about the same number of length four progressions in the sense that


Λa,r(f) ≈ Λa,r(f1); (3.14) similarly one also has

Ef(a) ≈ Ef1(a). (3.15) As a consequence, Theorem 3.1 for such functions follows (heuristically, at least) from the analysis of the ﬁrst example, at least if one assumes the genericity of the frequencies ξ1,... ,ξd.

Example 6: A pseudorandom perturbation of an impure quadratic factor. We now consider a situation which is to the second example as the ﬁfth example was to the ﬁrst. Namely, we consider a function of the form

f(a) := f1(a) + f2(a),

where f1 : Z/pZ → [−1,1] is a function of the type considered in the second example, thus

f1(bc + nsc) := Fc(ξc,d1n2,... ,ξc,dcn2) for c = 1,... ,m and n = 1,... ,Nc. As for the function f2 : Z/pZ → [−1,1], global Gowers uniformity of f2 will be too weak of a hypothesis for our purposes, because the random variable r appearing in the second example is now localised to a signiﬁcantly smaller region than Z/pZ. Instead, we will require the local Gowers uniformity hypothesis

E

f2(a + ω1h1 + ω2h2 + ω3h3) ≈ 0, (3.16)

(ω1,ω2,ω3)∈{0,1}3

where a is now the random variable from the second example (in particular, a depends on the auxiliary random variable c), and once one conditions on an event c = c for c = 1,... ,m, one draws h1,h2,h3 independently of each other and from a, and each hi drawn uniformly from an arithmetic progression of the form

{nsc : |n| exp(−1/η−Ci)Nc}, (3.17)

for some constant Ci > 0 (for technical reasons, it is convenient to allow these constants C1,C2,C3 to be diﬀerent from each other, and also to be larger than the constant C appearing in (3.12), so that h1,h2,h3 range over a narrower scale than r). As with a and r, the random variables a,h1,h2,h3 are now only conditionally independent relative to the auxiliary variable c, but are not independent of each other without this conditioning, as they are coupled to each other through c.

As it turns out, once one assumes this local Gowers uniformity of f2, one can modify the Cauchy-Schwarz arguments used to establish the global generalised von Neumann theorem to obtain the approximations (3.14), (3.15) for the random variables a,r considered in the second example, at which point Theorem 3.1 for this choice of f follows (heuristically, at least) from the analysis of that example, at least if one assumes that there are no nontrivial relations of the form (3.10).

Example 7: Non-pseudorandom perturbation of a pure quadratic factor. We now modify the ﬁfth example by replacing the hypothesis (3.13) by its negation

E

f2(a + ω1h1 + ω2h2 + ω3h3) ≫ 1 (3.18)

(ω1,ω2,ω3)∈{0,1}3

(it is not diﬃcult to show that the left-hand side is non-negative). In this case, the generalised von Neumann theorem used in that example does not give a good estimate. However, in this situation one can apply the inverse theorem for the Gowers norm established by us in [21]. In order to obtain good quantitative bounds, we will use the version of that theorem that involves local correlation with quadratic objects (as opposed to a somewhat weak global correlation with a single “locally quadratic” object). Namely, if (3.18) holds, then one can partition Z/pZ into a moderately large (e.g.

- O(exp(1/η−O(1)))) number of pieces P1,... ,Pm, such that on each piece Pc, the function f2 correlates with a “quadratically structured” object. The precise statement is somewhat technical to state, but one simple special case


of this conclusion is that the pieces P1,... ,Pm are arithmetic progressions as in the second example, and for a “signiﬁcant number” of the progressions

Pc = {bc + nsc : 1 n Nc} there exists a frequency ξc ∈ R/Z such that

|E1 n Ncf2(bc + nsc)e(−ξcn2)| ≫ 1.

(In general, one would take Pc to be Bohr sets of moderately high rank, rather than arithmetic progressions, and the phase a  → ξca2/p would have to be replaced by a more general locally quadratic phase function on such a Bohr set, but we ignore these technicalities for the current informal discussion.) From this and the cosine rule, it is possible to ﬁnd a function

- g : Z/pZ → [−1,1] that is equal to (the real part of) a scalar multiple of the quadratic phases bc + nsc  → e(ξcn2) on each progression Pc, such that f2 + g has an energy decrement compared to f2 in the sense that


Ea∈Z/pZ(f2(a) + g(a))2 Ea∈Z/pZf2(a)2 − ηC (3.19) for some constant C > 0. In this situation, we can modify the decomposition f = f1 +f2 by adding g to f2 and subtracting it from f1. (Strictly speaking, this may make f1 and f2 range slightly outside of [−1,1], but because f itself ranges in [−1,1], it turns out to be relatively easy to modify f1,f2 further to rectify this problem.) The new function f1 has a similar “quadratic structure” to the previous function f1, except that the quadratic structure is now localised to the cells P1,... ,Pm of the partition of Z/pZ, and the number of quadratic functions has been increased by one. If the new function f2 is now locally Gowers uniform in the sense of (3.16), then we are now essentially in the situation of the sixth example (at least if there are no non-trivial relations of the form (3.10)), and we can (heuristically at least) conclude Theorem 3.1 in this case by the previous analysis. If f2 is locally Gowers uniform but there are additionally some relations of the form (3.10), then one can hope to adapt the analysis of the fourth example to reduce the quadratic complexity of f1 on all the poorly distributed cells, at which point one restarts the analysis. If however f2 remains non-uniform, then we need to argue using the analysis of the next and ﬁnal example.

Example 8: Non-pseudorandom perturbation of an impure quadratic factor. Our ﬁnal and most diﬃcult example will be as to the sixth example as the seventh example was to the ﬁfth. Namely, we modify the sixth example by assuming that the negation of (3.16) holds. Equivalently, one has the lower bound

  ≫ 1 (3.20)

 

E

f2(a + ω1h1 + ω2h2 + ω3h3)|c = c

(ω1,ω2,ω3)∈{0,1}3

on the local Gowers norm for a “signiﬁcant fraction” of the c = 1,... ,m.

At the qualitative level, the inverse theorem in [21] for the global Gowers norm allows one to also deduce a similar conclusion starting from the hypothesis (3.20). However, the quantitative bounds obtained by this approach turn out to be too poor for the purposes of establishing Theorem 3.1 or Theorem 1.1. Instead, one must obtain a quantitative local inverse theorem for the Gowers norm that has reasonably good bounds (of polynomial type) on the amount of correlation that is (locally) attained. Establishing such a theorem is by far the most complicated and lengthy component of this

paper, although broadly speaking it follows the same strategy as previous theorems of this type in [12, 21]. If one takes this local inverse theorem for granted, then roughly speaking what we can then conclude from the hypothesis (3.20) is that for a signiﬁcant number of c = 1,... ,m, one can partition the cell Pc into subcells Pc,1,... ,Pc,mc, and locate a “locally quadratic phase function” φc,i : Pc,i → R/Z on each such subcell (generalising the functions bc + nsc  → e(ξcn2) from the previous example), such that

|Ea∈Pc,if2(bc,i)e(−φc,i(a))| ≫ 1 for a signiﬁcant fraction of the c,i. Using this, one can again obtain an energy decrement of the form (3.19), where now g is (the real part of) a scalar multiple of the functions a  → e(φc,i(a)) on each Pc,i. By arguing as in the sixth example, one can then modify f1 and f2 in such a way that the “energy” Ef2(a)2 decreases signiﬁcantly, while f1 is now locally quadratically structured on a somewhat ﬁner partition of Z/pZ than the original partition P1,... ,Pm, with the number of quadratic phases needed to describe f1 on each partition having increased by one. If the function f2 is now locally Gowers uniform (with respect to a new set of random variables a,r adapted to this ﬁner partition), and there are no non-trivial relations of the form we can now (heuristically) conclude Theorem 3.1 from the analysis of the sixth example, assuming the addition of the new quadratic phase has not introduced relations of the form (3.10). If such relations occur, though, one can hope to adapt the analysis of the fourth example to reduce the quadratic complexity of the poorly distributed cells, perhaps at the cost of further subdivision of the cells. Finally, if the new version of f2 remains nonuniform with respect to the ﬁner partition, then one iterates the analysis of this example to reduce the energy of f2 further. This process cannot continue indeﬁnitely due to the non-negativity of the energy (and also because none of the other steps in the iteration will cause a signiﬁcant increase in energy). Because of this, one can hope to cover all cases of Theorem 3.1 by some complicated iteration of the eight arguments described above.

Having informally discussed the eight key examples for Theorem 3.1, we return now to the task of proving this theorem rigorously.

It will be convenient to work throughout the rest of the paper with a ﬁxed choice

1 < C1 < C2 < ··· < C5 of absolute constants, with each Ci assumed to be suﬃciently large depending on the previous C1,... ,Ci−1. For instance, for sake of concreteness one could choose Ci := 22100i; of course, other choices are possible. The implied constants in the O() notation will not depend on the Ci unless otherwise speciﬁed. These constants will serve as exponents for various scales η−Ci that will appear in our analysis, with the point being that any scale of the form η−Ci for i = 2,... ,5 is extremely tiny with respect to any polynomial combination of the previous scales η−C1,... ,η−Ci−1.

In all of the eight examples considered above, the function f was approximated by some “quadratically structured” function, usually denoted f1, with the approximation being accurate in various senses with respect to some pair (a,r) of random variables. The rigorous argument will similarly approximate f by a quadratically structured object; it will be convenient to make this object a random function f rather than a deterministic one (though as it turns out, this function will become deterministic again once an auxiliary random variable c is ﬁxed). The precise deﬁnition of “quadratically structured” will be rather technical, and will eventually be given in Deﬁnition 6.1. For now, we shall abstract the properties of “quadratic structure” we will need, in the following proposition involving an abstract directed graph G = (V,E) (encoding the “structured local approximants”) which we will construct more explicitly later. We will shortly iterate this proposition to establish Theorem 3.1 and hence Theorem 1.1.

Proposition 3.3 (Main proposition, abstract form). Let η be a real number with 0 < η 10 1 , and let p be a prime with

![image 39](<2017-green-new-bounds-szemer-edi_images/imageFile39.png>)

p exp(η−3C5). (3.21) Let f : Z/pZ → [0,1] be a function. Then there exist the following:

- (a) A (possibly inﬁnite) directed graph G = (V,E), with elements v ∈ V referred to as structured local approximants, and the notation v → v′ used to denote the existence of a directed edge from one structured local approximant v to another v′;
- (b) A triple (av,rv,fv) associated to f and to each structured local approximant v ∈ V , where av,rv are random variables in Z/pZ, and fv : Z/pZ → [−1,1] is a random function (with av,rv,fv not assumed to be independent);
- (c) A quadratic dimension d2(v) ∈ N assigned to each vertex v ∈ V ;
- (d) A poorly distributed quadratic dimension dpoor2 (v) ∈ N assigned to each vertex v ∈ V , with 0 dpoor2 (v) d2(v); and
- (e) An initial approximant v0 ∈ V , with d2(v0) = 0 (and hence dpoor2 (v0)


= 0).

Furthermore, whenever a structured local approximant vk ∈ V can be reached from v0 by a path v0 → v1 → ··· → vk with 0 k 8η−2C2, then the following properties are obeyed:

- (i) One has the “thickness” condition P(rvk = 0) ≪ exp(3η−C5)/p; (3.22)
- (ii) We have the almost uniformity condition |Ef(avk) − Ea∈Z/pZf(a)| η; (3.23)
- (iii) Bad approximation implies energy decrement: if |Efvk(avk) − f(avk)| > η (3.24)


or

k,rvk(f)| > η (3.25)

k,rvk(fvk) − Λav

|Λav

then there exists a structured local approximant vk+1 ∈ V with vk → vk+1 such that

E|f(avk+1) − fvk+1(avk+1)|2 E|f(avk) − fvkk(avk)|2 − ηC2 and

d2(vk+1) d2(vk) + 1.

- (iv) Failure of “Khintchine-type recurrence” implies dimension decrement: if


k,rvk(fvk) (Efvk(avk))4 − η, (3.26) then there exists a structured local approximant vk+1 ∈ V with vk → vk+1 obeying the bounds

Λav

E|f(avk+1) − fvk+1(avk+1)|2 E|f(avk) − fvk(avk)|2 + η3C2, d2(vk+1) d2(vk), dpoor2 (vk+1) dpoor2 (vk) − 1.

The proof of this proposition will occupy the remainder of the paper. For now, let us see how this proposition implies Theorem 3.1. Let p,η,f be as in that theorem, and let C1,... ,C5 be as above. If the largeness criterion (3.21) fails, then we may set r := 0, f := f, and draw a uniformly at random from Z/pZ, and it is easy to see that the conclusions of Theorem 3.1 are obeyed (with (3.3) following from H¨older’s inequality). Thus we may assume without loss of generality that (3.21) holds.

Let G = (V,E), v0, d2(), dpoor2 (), and (av,rv,fv) be as in Proposition 3.3. Suppose ﬁrst that there exists a structured local approximant vk ∈ V that can be reached from v0 by a path of length at most 8η−2C2, and for which none of the inequalities (3.24), (3.25), (3.26) hold, that is to say one has the bounds

|Efvk(avk) − fvk(avk)| η, (3.27) |Λav

k,rvk(fvk)| η (3.28) Λav

k,rvk(fvk) − Λav

k,rvk(fvk) > (Efvk(avk))4 − η. (3.29) From (3.29), (3.28), (3.27) and the triangle inequality (and the boundedness of fvk,f) we conclude that

k,rvk(fvk) > (Ef(avk))4 − O(η);

Λav

combining this with (3.22) and (3.23) we see that the random variables avk,rvk obey the properties required of Theorem 3.1. Thus we may assume for sake of contradiction that this situation never occurs, which by Proposition 3.3 implies that whenever vk ∈ V is a structured local approximant that

can be reached from v0 by a path of length at most 8η−2C2, then the conclusions of at least one of (iii) and (iv) hold. Iterating this we may therefore construct a path

v0 → v1 → ··· → vk0+1 with

k0 := ⌊8η−2C2⌋, (3.30)

such that for every 0 k k0, one either has the energy decrement bounds E|f(avk+1) − fk+1(avk+1)|2 E|f(avk) − fk(avk)|2 − ηC2

d2(vk+1) d2(vk) + 1 or the dimension decrement bounds

E|f(avk+1) − fk+1(avk+1)|2 E|f(avk) − fk(avk)|2 + η3C2 d2(vk+1) d2(vk), dpoor2 (vk+1) dpoor2 (vk) − 1.

Since v0 already has the minimum quadratic dimension dpoor2 (v0) = 0, we see that we must experience an energy decrement at the k = 0 stage. Also, if k is the jth index to experience an energy decrement, we see that dpoor2 (vk+1) d2(vk+1) j, and so one can have at most j consecutive dimension decrements after the kth stage; in other words, we must experience another energy decrement within j + 1 steps. By deﬁnition of k0, we have

0 j 2η−C2(j + 1) < k0 if C2 is large enough. We conclude that at least

2η−C2 energy decrements occur within the path v0 → ··· → vk0+1. This implies that

0+1)|2 E|f(av0)−fk+1(av0)|2−(2η−C2)ηC2 +k0η3C2. But if C2 is suﬃciently large, this implies from (3.30) that

E|f(avk

0+1)−fk0+1(avk

0+1)|2 < E|f(av0) − f0(av0)|2 − 4

E|f(avk

0+1) − fk0+1(avk

(say), which leads to a contradiction because the left-hand side is clearly non-negative, and the right-hand side non-positive. This gives the desired contradiction that establishes Theorem 3.1 and hence Theorem 1.1.

It remains to establish Proposition 3.3. This will occupy the remaining portions of the paper.

4. Bohr sets

In order to deﬁne and manipulate the “structured local approximants” that appear in Proposition 3.3, we will need to develop the theory of two mathematical objects. The ﬁrst is that of a Bohr set, which will be covered in this section; the second is that of a dilated torus, which we will discuss in the next section.

Deﬁnition 4.1 (Bohr set). A subset S of Z/pZ is said to be non-degenerate if it contains at least one non-zero element. In this case we deﬁne the dual S-norm

aξ

a S⊥ := sup ξ∈S

![image 40](<2017-green-new-bounds-szemer-edi_images/imageFile40.png>)

p R/Z for any a ∈ Z/pZ, and then deﬁne the Bohr set B(S,ρ) ⊂ Z/pZ for any ρ > 0 by the formula

B(S,ρ) := {a ∈ Z/pZ : a S⊥ < ρ}

where θ R/Z denotes the distance from θ to the nearest integer. We refer to S as the set of frequencies of the Bohr set, ρ as the radius, and |S| as the rank of the Bohr set. We also deﬁne the shifted Bohr sets

n + B(S,ρ) := {a + n : a ∈ B(S,ρ)} for any n ∈ Z/pZ.

From (2.4) we have the triangle inequalities

a + b S⊥ a S⊥ + b S⊥; ka S⊥ |k| a S⊥ (4.1) for a,b ∈ Z/pZ and k ∈ Z; also we trivially have

a S⊥ a (S′)⊥ if S ⊂ S′ and a ∈ Z/pZ, or equivalently that B(S′,ρ) ⊂ B(S,ρ) for ρ > 0. We will frequently use these inequalities in the sequel, usually without further comment. In Lemma 4.6 below, we will show that S⊥ is “dual” to a certain word norm S on Z/pZ. One could also deﬁne Bohr sets in the case when S is degenerate, but this creates some minor complications in our arguments, so we remove this case from our deﬁnition of a Bohr set.

We have the following standard size bounds for Bohr sets, whose proof may be found in [48, Lemma 4.20]. Lemma 4.2. If B(S,ρ) is a Bohr set, then |B(S,ρ)| ρ|S|p and |B(S,2ρ)| 4|S||B(S,ρ)|.

In previous work on Roth-type theorems, one sometimes restricts attention to regular Bohr sets, as ﬁrst introduced in [6]; see [48, §4.4] for some discussion of this concept. Due to our use of the probabilistic method, we will be able to work with a technically simpler and “smoothed out” version of a regular Bohr set, which we call the regular probability distribution on a Bohr set.

Deﬁnition 4.3. Let B(S,ρ) be a Bohr set. The regular probability distribution pB(S,ρ) : Z/pZ → R associated to B(S,ρ) is the function deﬁned by the formula

1

1B(S,tρ)(a) |B(S,tρ)|

pB(S,ρ)(a) := 2

dt; (4.2)

![image 41](<2017-green-new-bounds-szemer-edi_images/imageFile41.png>)

1/2

it is easy to see (from Fubini’s theorem) that this is indeed a probability distribution on Z/pZ. A random variable a ∈ Z/pZ is said to be drawn regularly from B(S,ρ) if it has probability density function pB(S,ρ), thus

- P(a = a) = pB(S,ρ)(a) for all a ∈ Z/pZ. More generally, for any shifted Bohr set n+B(S,ρ), we deﬁne the regular


probability distribution pn+B(S,ρ) : Z/pZ → R by the formula

pn+B(S,ρ)(a) := pB(S,ρ)(a − n), and say that a is drawn regularly from n + B(S,ρ) if it has probability distribution pn+B(S,ρ).

Informally, to draw a random variable a regularly from n + B(S,ρ), one should draw it uniformly from n + B(S,tρ), where t is itself selected uniformly at random from the interval [1/2,1]. Note that if a is drawn regularly from n + B(S,ρ), then m + a will be drawn regularly from m + n + B(S,ρ) for any m ∈ Z/pZ, and similarly ka will be drawn from kn + B(k−1 · S,ρ) for any non-zero k ∈ Z/pZ, where k−1 · S := {k−1ξ : ξ ∈ S} is the dilate of the frequency set S by k−1.

From Lemma 4.2 we see that if a is drawn regularly from a shifted Bohr set n + B(S,ρ), then

1 (ρ/2)|S|p

P(a = a)

(4.3)

![image 42](<2017-green-new-bounds-szemer-edi_images/imageFile42.png>)

for all a ∈ Z/pZ. In practice, this will mean that the inﬂuence of any given value of a will be negligible.

The presence of the averaging parameter t in (4.2) allows for the following very convenient approximate translation invariance property. Given two random variables a,a′ taking values in a ﬁnite set A, we deﬁne the total variation distance between the two to be the quantity

dTV(a,a′) :=

|P(a = a) − P(a′ = a)|,

a∈A

or equivalently

|Ef(a) − Ef(a′)| where f : A → C ranges over 1-bounded functions.

dTV(a,a′) = sup

f

The next lemma gives some approximate translation-invariance properties of Bohr sets. Its proof is a thinly disguised version of the arguments of Bourgain [6].

Lemma 4.4. Let n + B(S,ρ) be a shifted Bohr set, and let a be drawn regularly from B(S,ρ). Let B(S′,ρ′) be another Bohr set with S′ ⊃ S.

- (i) If h ∈ B(S′,ρ′), then a and a+h diﬀer in total variation by at most O(|S|ρρ′).

![image 43](<2017-green-new-bounds-szemer-edi_images/imageFile43.png>)

- (ii) More generally, if h is a random variable independent of a that takes values in B(S′,ρ′), then a and a + h diﬀer in total variation by at most O(|S|ρρ′).


![image 44](<2017-green-new-bounds-szemer-edi_images/imageFile44.png>)

Proof. To prove (i), it suﬃces to show that

ρ′ ρ

Ef(a + h) = Ef(a) + O |S|

![image 45](<2017-green-new-bounds-szemer-edi_images/imageFile45.png>)

for any 1-bounded function f : Z/pZ → C; the claim (ii) then also follows by conditioning h to a ﬁxed value h ∈ B(S′,ρ′), then multiplying by P(h = h) and summing over h.

By translating f by n, we may assume that n = 0. We may assume that ρ′ 10 ρ|S|, as the claim is trivial otherwise.

![image 46](<2017-green-new-bounds-szemer-edi_images/imageFile46.png>)

From (4.2) we have

1

1B(S,tρ)(a) |B(S,tρ)|

Ef(a) = 2

dt

f(a)

![image 47](<2017-green-new-bounds-szemer-edi_images/imageFile47.png>)

1/2 a∈Z/pZ

and

1

1B(S,tρ)−h(a) |B(S,tρ)|

Ef(a + h) = 2

f(a)

dt

![image 48](<2017-green-new-bounds-szemer-edi_images/imageFile48.png>)

1/2 a∈Z/pZ

so by the triangle inequality it suﬃces to show that

a∈Z/pZ |1B(S,tρ)(a) − 1B(S,tρ)−h(a)| |B(S,tρ)|

1

ρ′ ρ

dt ≪ |S|

. (4.4)

![image 49](<2017-green-new-bounds-szemer-edi_images/imageFile49.png>)

![image 50](<2017-green-new-bounds-szemer-edi_images/imageFile50.png>)

1/2

By the triangle inequality, the integrand here is bounded above by 2. Also, from (4.1), we see that any a for which 1B(S,tρ)−h(a) = 1B(S,tρ)(a) lies in the “annulus” B(S,tρ + ρ′)\B(S,tρ − ρ′). We conclude that the left-hand side of (4.4) is bounded by

1

O min |B(S,tρ + ρ′)| − |B(S,tρ − ρ′)| |B(S,tρ − ρ′)|

,1 dt

![image 51](<2017-green-new-bounds-szemer-edi_images/imageFile51.png>)

1/2

which, using the elementary bound min(x − 1,1) ≪ log x for x 1, can be bounded in turn by

O

The integral telescopes to

1

log |B(S,tρ + ρ′)| |B(S,tρ − ρ′)|

dt .

![image 52](<2017-green-new-bounds-szemer-edi_images/imageFile52.png>)

1/2

1+ρ′/ρ

1/2

log |B(S,tρ)| dt

log |B(S,tρ)| dt −

O

1/2−ρ′/ρ

1

which can be bounded in turn by O

ρ′ ρ

log |B(S,2ρ)| |B(S,ρ/4)|

. The claim now follows from Lemma 4.2.

![image 53](<2017-green-new-bounds-szemer-edi_images/imageFile53.png>)

![image 54](<2017-green-new-bounds-szemer-edi_images/imageFile54.png>)

We will be interested in the Fourier coeﬃcients Eep(λn) = Ee(λpn) of random variables n drawn regularly from Bohr sets B(S,ρ). As was noted by Bourgain [6], these coeﬃcients are controlled by a “word norm” S, deﬁned as follows:

![image 55](<2017-green-new-bounds-szemer-edi_images/imageFile55.png>)

Deﬁnition 4.5 (Word norm). If S ⊂ Z/pZ is non-degenerate, and a is an element of Z/pZ, we deﬁne the word norm a S of a to be the minimum value of s∈S |ns|, where (ns)s∈S ∈ ZS ranges over tuples of integers such that one has a representation a = s∈S nss; note that such a representation always exists because S is non-degenerate.

Similarly to (4.1), we observe the triangle inequalities

a + b S a S + b S; ka S |k| a S (4.5) for a,b ∈ Z/pZ and k ∈ Z, which we will use frequently in the sequel, often without further comment.

We now give a duality relationship between the word norm S and the dual S-norm S⊥:

- Lemma 4.6 (Duality). Let S be a non-degenerate subset of Z/pZ, and let λ ∈ Z/pZ.


- (i) For every n ∈ Z/pZ, one has nλp R/Z n S⊥ λ S.

![image 56](<2017-green-new-bounds-szemer-edi_images/imageFile56.png>)

- (ii) Conversely, if one has the estimate nλp R/Z A n S⊥ for some A 1 and all n ∈ Z/pZ, then λ S ≪ |S|3/2A.


![image 57](<2017-green-new-bounds-szemer-edi_images/imageFile57.png>)

Proof. To prove (i), we simply observe (using (2.4)) that for any n ∈ Z/pZ, one has nλ/p R/Z =

nξ p R/Z ξ∈S |aξ| n S⊥ λ S n S⊥ as desired, where λ = ξ∈S aξξ is a representation of λ that minimises

nξ p

|aξ|

=

aξ

![image 58](<2017-green-new-bounds-szemer-edi_images/imageFile58.png>)

![image 59](<2017-green-new-bounds-szemer-edi_images/imageFile59.png>)

R/Z ξ∈S

ξ∈S

ξ∈S |ξ|. Estimates such as (ii) go back to the work of Bourgain [6]. We will prove

this claim by a Fourier-analytic argument. We may assume that λ S

|S|3/2, as the claim is trivial otherwise. Let ψ : R → R be a non-negative smooth even function (not depending on p or λ) supported on [−1,1] and

non-zero on [−1/2,1/2], whose Fourier transform ψˆ(ξ) := R ψ(x)e(−ξx) dx is also non-negative. Set N := |S|−1 λ S, so in particular N 1. We consider the kernel KN : Z/pZ → C deﬁned by

k N

KN(n) :=

);

ep(kn)ψ(

![image 60](<2017-green-new-bounds-szemer-edi_images/imageFile60.png>)

k∈Z

by the Poisson summation formula we have KN(n(mod p)) = N

Nn p − Nm

ψˆ

![image 61](<2017-green-new-bounds-szemer-edi_images/imageFile61.png>)

m∈Z

for any integer n, so in particular KN is non-negative. By deﬁnition of N, the frequency λ has no representations of the form λ = ξ∈S aξξ with supξ∈S |aξ| < N. Hence the Riesz-type product ξ∈S KN(ξn),

when expanded, contains no terms of the form ep(λn) or ep(−λn), and is therefore orthogonal to cos(2πλnp ). In particular we have the identity

![image 62](<2017-green-new-bounds-szemer-edi_images/imageFile62.png>)

2πλn p ξ∈S

En∈Z/pZ

KN(ξn) = En∈Z/pZ 1 − cos

KN(ξn).

![image 63](<2017-green-new-bounds-szemer-edi_images/imageFile63.png>)

ξ∈S

On the other hand, from two applications of (2.3) we have

2

2πλn p

λn p

A2 n 2S⊥

1 − cos(

) ≪

![image 64](<2017-green-new-bounds-szemer-edi_images/imageFile64.png>)

![image 65](<2017-green-new-bounds-szemer-edi_images/imageFile65.png>)

R/Z

2

ξ0n p

2πξ0n p

A2

A2

1 − cos

![image 66](<2017-green-new-bounds-szemer-edi_images/imageFile66.png>)

![image 67](<2017-green-new-bounds-szemer-edi_images/imageFile67.png>)

R/Z

ξ0∈S

ξ0∈S

As KN is non-negative, we conclude that En∈Z/pZ

KN(ξn)

ξ∈S

En∈Z/pZ 

2πξ0n p



≪ A2

KN(ξn) KN(ξ0n) 1 − cos(

![image 68](<2017-green-new-bounds-szemer-edi_images/imageFile68.png>)

ξ0∈S

ξ∈S\ξ0

.

 .

(4.6)

We can expand KN(ξ0n) 1 − cos 2πξp0n as a Fourier series

![image 69](<2017-green-new-bounds-szemer-edi_images/imageFile69.png>)

ψ kN−1 + ψ kN+1 2

k N −

![image 70](<2017-green-new-bounds-szemer-edi_images/imageFile70.png>)

![image 71](<2017-green-new-bounds-szemer-edi_images/imageFile71.png>)

.

ep(kn) ψ

![image 72](<2017-green-new-bounds-szemer-edi_images/imageFile72.png>)

![image 73](<2017-green-new-bounds-szemer-edi_images/imageFile73.png>)

k∈Z

The expression inside parentheses is only non-vanishing for |k| N +1, and has magnitude O(1/N2). As ψ is non-negative everywhere and non-zero on [−1/2,1/2], we thus have a pointwise estimate of the form

8

ψ kN−1 + ψ kN+1 2 ≪

k N −

k N −

1 N2

j 4

![image 74](<2017-green-new-bounds-szemer-edi_images/imageFile74.png>)

![image 75](<2017-green-new-bounds-szemer-edi_images/imageFile75.png>)

ψ

ψ

![image 76](<2017-green-new-bounds-szemer-edi_images/imageFile76.png>)

![image 77](<2017-green-new-bounds-szemer-edi_images/imageFile77.png>)

![image 78](<2017-green-new-bounds-szemer-edi_images/imageFile78.png>)

![image 79](<2017-green-new-bounds-szemer-edi_images/imageFile79.png>)

![image 80](<2017-green-new-bounds-szemer-edi_images/imageFile80.png>)

j=−8

(say). By using the non-negativity of the Fourier coeﬃcients of KN, this gives the estimate

En∈Z/pZ

 KN(ξ0n) 1 − cos

 

KN(ξn)

ξ∈S\ξ0

1 N2

En∈Z/pZ

≪

![image 81](<2017-green-new-bounds-szemer-edi_images/imageFile81.png>)

ξ∈S

2πξ0n p

![image 82](<2017-green-new-bounds-szemer-edi_images/imageFile82.png>)

KN(ξn).

Comparing this with (4.6), we conclude that 1 ≪ A2|S|/N2, and the claim follows from the deﬁnition of N.

Next, we estimate the Fourier coeﬃcients of a regular distribution on a Bohr set in terms of the word norm.

- Lemma 4.7. Let S be a non-degenerate subset of Z/pZ. Suppose that n is drawn regularly from B(S,ρ). Then we have

Eep(λn) ≪

|S|5/2 ρ λ S

![image 83](<2017-green-new-bounds-szemer-edi_images/imageFile83.png>)

for all λ ∈ Z/pZ, where we adopt the convention that the above estimate is vacuously true if λ S = 0.

Proof. For any h ∈ Z/pZ, one has from Lemma 4.4 that

Eep(λn) = Eep(λ(n + h)) + O |S| h S⊥

![image 84](<2017-green-new-bounds-szemer-edi_images/imageFile84.png>)

ρ which we may rearrange as

(1 − ep(λh)) Eep(λn) ≪

|S| h S⊥ ρ

![image 85](<2017-green-new-bounds-szemer-edi_images/imageFile85.png>)

.

Since |1 − ep(λh)| ≫ λhp R/Z, we conclude that λh p R/Z

![image 86](<2017-green-new-bounds-szemer-edi_images/imageFile86.png>)

![image 87](<2017-green-new-bounds-szemer-edi_images/imageFile87.png>)

Eep(λn) ≪

|S| h S⊥ ρ

![image 88](<2017-green-new-bounds-szemer-edi_images/imageFile88.png>)

.

Taking h so as to minimise the ratio h S⊥/ λh/p R/Z, the claim follows from Lemma 4.6.

We will take advantage of the fact that Bohr sets can be approximately described as generalised arithmetic progressions. A key lemma in this regard is the following.

- Lemma 4.8. Let Γ be a lattice in Rd. Then there exist linearly independent generators v1,... ,vd of Γ and real numbers N1,... ,Nd > 0 such that


d

BRd(0,O(d)−3d/2t) ∩ Γ ⊂ {

i=1

nivi : |ni| < tNi} ⊂ BRd(0,t) ∩ Γ (4.7)

for all t > 0, where BRd(0,r) is the open Euclidean ball of radius r in Rd, and the ni are understood to be integers. Furthermore, the determinant/covolume det(Γ) obeys the bounds

det(Γ) = (2d)O(d)

d

Ni−1. (4.8)

i=1

Proof. Applying [49, Theorem 1.6], we can ﬁnd elements v1,... ,vr of Γ for some r d, linearly independent over the rationals, and real numbers

N1,... ,Nd > 0 such that

r

BRd(0,O(d)−3d/2t) ∩ Γ ⊂ {

nivi : |ni| < tNi} ⊂ BRd(0,t) ∩ Γ (4.9) for all t > 0, and such that

i=1

r

O(d)−7d/2|BRd(0,t) ∩ Γ| |{

nivi : |ni| < tNi}| |BRd(0,t) ∩ Γ|.

i=1

(Strictly speaking, the statement of [49, Theorem 1.6] only claims the latter bound for t = 1, but the same argument gives the bound for all t > 0.) Sending t to inﬁnity, we conclude that the v1,... ,vr generate Γ; since, by virtue of being a lattice, Γ is cocompact, this forces d = r. Also, volume packing arguments show that as t → ∞, the cardinality |BRd(0,t) ∩ Γ| is asymptotic to the measure of BRd(0,t) divided by det(Γ), while the cardinality of |{n1v1 + ··· + ndvd : |ni| tNi}| is asymptotic to di=1(2tNi). We conclude (4.8) as desired.

The following corollary describes how we may pick a “basis” for a Bohr set.

Corollary 4.9. Let S be a non-degenerate subset of Z/pZ, and set d := |S|. Then there exist elements a1,... ,ad of Z/pZ and real numbers N1,... ,Nd >

- 0 such that d


Ni−1 = (2d)O(d)p (4.10) and

i=1

ai S⊥ Ni−1 (4.11) for all i = 1,... ,d. Furthermore, for any a ∈ Z/pZ, there exists a representation

a = n1a1 + ··· + ndad (4.12) with n1,... ,nd integers of size

ni = (2d)O(d)Ni a S⊥ (4.13)

for i = 1,... ,d. Finally, if one imposes the additional condition |ni| < Ni/2 for all i = 1,... ,d, then there is at most one such representation of this form (4.12) for a given a.

Proof. For each s ∈ S, the fraction ps can be viewed as an element of R/Z of order at most p; as S is non-degenerate, we see that the tuple (ps)s∈S is an element of the torus (R/Z)S of order p. Let Γ be the preimage in RS of the group generated by this element, thus Γ is a lattice of RS that contains ZS as a sublattice of index p; in particular, Γ has determinant

![image 89](<2017-green-new-bounds-szemer-edi_images/imageFile89.png>)

![image 90](<2017-green-new-bounds-szemer-edi_images/imageFile90.png>)

p. Applying Lemma 4.8, one can ﬁnd generators v1,... ,vd of Γ and real numbers N1,... ,Nd obeying (4.10) such that

d

BRS(0,O(d)−3d/2t) ∩ Γ ⊂ {

nivi : |ni| < tNi} ⊂ BRS(0,t) ∩ Γ (4.14) for all t > 0.

i=1

By construction of Γ, we can ﬁnd elements a1,... ,ad of Z/pZ such that vi =

ais p s∈S

(mod ZS) (4.15)

![image 91](<2017-green-new-bounds-szemer-edi_images/imageFile91.png>)

for i = 1,... ,d. Applying (4.14) with t slightly larger than Ni−1 for some i = 1,... ,d, we see that vi ∈ BRd(Ni−1), and hence by (4.15) we have (4.11).

Finally, if a ∈ Z/pZ, then by deﬁnition of Γ we can ﬁnd an element x of Γ in the preimage of (asp )s∈S such that each component of x has magnitude less than a S⊥; in particular, x ∈ BRS(0,√d a S⊥). Applying (4.14), we conclude that x = di=1 nivi for some integers n1,... ,nd obeying (4.13), giving the desired representation (4.12).

![image 92](<2017-green-new-bounds-szemer-edi_images/imageFile92.png>)

![image 93](<2017-green-new-bounds-szemer-edi_images/imageFile93.png>)

Finally, we show uniqueness. If there were two representations of the form (4.12) with |ni| < Ni/2 for all i = 1,... ,d, then there exists a tuple (n′1,... ,n′d) ∈ Zd, not identically zero, with |n′i| < Ni for all i = 1,... ,d and di=1 niai = 0, which implies that the vector di=1 nivi lies in ZS. As the v1,... ,vd are linearly independent, this vector must have magnitude at least 1; but this contradicts (4.7) (with t = 1).

Linear and quadratic functions on Bohr sets. We will frequently need to deal with locally linear or quadratic functions on Bohr sets. We review the deﬁnitions of these now.

Deﬁnition 4.10. Let B be a subset of Z/pZ, and let G = (G,+) be an abelian group. A function φ : B → G is said to be locally linear on B if one has

φ(n + h1 + h2) − φ(n + h1) − φ(n + h2) + φ(n) = 0

whenever n,h1,h2 ∈ Z/pZ are such that n,n + h1,n + h2,n + h1 + h2 ∈ B. Similarly, φ is said to be locally quadratic on B if one has

(−1)ω1+ω2+ω3φ(n + ω1h1 + ω2h2 + ω3h3) = 0 (4.16)

(ω1,ω2,ω3)∈{0,1}3

whenever n,h1,h2,h3 ∈ Z/pZ are such that n+ω1h1 +ω2h2 +ω3h3 ∈ B for all (ω1,ω2,ω3) ∈ {0,1}3.

A function ψ : B × B → G is said to be locally bilinear on B if one has ψ(h1 + h′1,h2) = ψ(h1,h2) + ψ(h′1,h2) whenever h1,h′1,h2 ∈ B are such that h1 + h′1 ∈ B, and similarly one has

ψ(h1,h2 + h′2) = ψ(h1,h2) + ψ(h1,h′2) whenever h1,h2,h′2 ∈ B are such that h2 + h′2 ∈ B.

Specialising (4.16) to the case h1 = h2 = h3 = h, we conclude that

φ(n) − 3φ(n + h) + 3φ(n + 2h) − φ(n + 3h) = 0 (4.17) whenever φ : B → G is locally quadratic on B and n,n+h,n+2h,n+3h ∈ B.

It is well known (from the Weyl exponential sum estimates) that quadratic exponential sums such as E1 n Ne(αn2 + βn) can only be large when the quadratic phase αn2 is of “major arc” type in the sense that kαn2 is close to constant on the range {1,... ,N} of the summation variable n, for some bounded positive integer k. The following proposition is an analogue of this phenomenon on Bohr sets.

Proposition 4.11 (Large local quadratic exponential sums). Let B(S,ρ) be a Bohr set, let 0 < δ 1/2, let λ,µ : B(S,10ρ) → R/Z be locally linear maps, and let φ : B(S,10ρ) × B(S,10ρ) → R/Z be a locally bilinear phase such that

|Ee(φ(n,m) + λ(n) + µ(m))| δ (4.18) if n,m are drawn independently and regularly from B(S,ρ). Then there exists a natural number

1 k δ−O(C1|S|2) such that

n S m S ρ2

kφ(n,m) R/Z ≪ δ−O(C1|S|2)

(4.19)

![image 94](<2017-green-new-bounds-szemer-edi_images/imageFile94.png>)

whenever n,m ∈ B S, (C δC1ρ

1|S|)3|S| .

![image 95](<2017-green-new-bounds-szemer-edi_images/imageFile95.png>)

Proof. Let d := |S|, thus d 1. By Corollary 4.9, we can ﬁnd elements a1,... ,ad of Z/pZ and real numbers N1,... ,Nd obeying the conclusions of that corollary.

Suppose that 1 i,j d are such that Ni,Nj δC d

1/2ρ (we allow i and j to be equal). Then by (4.11) we have

![image 96](<2017-green-new-bounds-szemer-edi_images/imageFile96.png>)

ai S⊥, aj S⊥ d−1δC1/2ρ.

We can control the coeﬃcient φ(ai,aj) by the following argument. If we draw bi and bj uniformly from {bi ∈ Z : 1 bi δC1/4Niρ/d} and {bj ∈ Z :

- 1 bj δC1/4Njρ/d} respectively and independently of each other and of n,m, then from two applications of Lemma 4.4 (comparing n with n+biai, and m with m + bjaj) we have


Ee(φ(n + biai,m + bjaj) + λ(n + biai) + µ(m + bjaj))

= Ee(φ(n,m) + λ(n) + µ(m)) + O(δC1/4) and hence from (4.18) (assuming C1 large enough) we have

|Ee(φ(n + biai,m + bjaj) + λ(n + biai) + µ(m + bjaj))| ≫ δ. By the pigeonhole principle, we can therefore ﬁnd n,m ∈ B(S,ρ) such that |Ee(φ(n + biai,m + bjaj) + λ(n + biai) + µ(m + bjaj))| ≫ δ.

Using the local bilinearity of φ, the left-hand side may be written as |Ee(bibjφ(ai,aj) + αbi + βbj + γ)|

for some α,β,γ ∈ R/Z depending on i,j,n,m whose exact values are not of importance to us. Evaluating the expectations and using the triangle inequality, we conclude that

E1 b

i δC1/4Niρ/d|E1 b

j δC1/4Njρ/de(bj(biφ(ai,aj) + β))| ≫ δ and hence (by Lemma 2.2)

|E1 b

j δC1/4Njρ/de(bj(biφ(ai,aj) + β))| ≫ δ

for ≫ δC1/4+1Niρ/d values of bi in the range 1 bi δC1/4Niρ/d. This average is a geometric series that can be explicitly computed, leading to the bound

d δ

biφ(ai,aj) + β R/Z ≪

![image 97](<2017-green-new-bounds-szemer-edi_images/imageFile97.png>)

C1

4 +1Njρ

![image 98](<2017-green-new-bounds-szemer-edi_images/imageFile98.png>)

for ≫ δC1/4+1Niρ/d values of bi in the range 1 bi δC1/4Niρ/d. Applying [24, Lemma A.4] (which is really an observation of Vinogradov, used often in the theory of Weyl sums), we conclude that

d2 δO(C1)NiNjρ2

ki,jφ(ai,aj) R/Z ≪

![image 99](<2017-green-new-bounds-szemer-edi_images/imageFile99.png>)

for some natural number ki,j with 1 ki,j ≪ δ−O(C1). If we then “clear denominators” by deﬁning

k :=

ki,j,

1 i,j d:Ni,Nj d

![image 100](<2017-green-new-bounds-szemer-edi_images/imageFile100.png>)

δC1/2ρ

then 1 k ≪ δ−O(C1d2) and kφ(ai,aj) R/Z ≪

1 δO(C1d2)NiNjρ2

![image 101](<2017-green-new-bounds-szemer-edi_images/imageFile101.png>)

(4.20)

for all 1 i,j d with Ni,Nj δC d

1/2ρ.

![image 102](<2017-green-new-bounds-szemer-edi_images/imageFile102.png>)

For any n ∈ Z/pZ, we see from Corollary 4.9 that we can ﬁnd integers n1,... ,nd with

ni ≪ (2d)O(d)Ni n S⊥ such that

n = n1a1 + ··· + ndad. In particular, if n ∈ B(S, (CδC1ρ

1d)3d), then ni is only non-zero when Ni δC d

1/2ρ. From these bounds, (4.20), and the local bilinearity of φ, we conclude (4.19) as desired.

![image 103](<2017-green-new-bounds-szemer-edi_images/imageFile103.png>)

![image 104](<2017-green-new-bounds-szemer-edi_images/imageFile104.png>)

Local U2-inverse theorem. The global inverse U2 theorem, which is a simple and well-known exercise in discrete Fourier analysis, asserts that if a 1-bounded function f : Z/pZ → C obeys the bound

|Ef(h0 + h1)f(h0 + h′1)f(h′0 + h1)f(h′0 + h′1)| η (4.21)

![image 105](<2017-green-new-bounds-szemer-edi_images/imageFile105.png>)

![image 106](<2017-green-new-bounds-szemer-edi_images/imageFile106.png>)

where h0,h1,h′0,h′1 are drawn uniformly at random from Z/pZ, then there exists ξ ∈ Z/pZ such that

|Ef(h)ep(−ξh)| η1/2 (4.22) where h is also drawn uniformly at random from Z/pZ.

In this section we give a local version of the above claim, in which the random variables h,h0,h1,h′0,h′1 are localised to a small Bohr set. If the rank of the Bohr set is bounded, one can modify the above arguments to obtain a reasonable inverse theorem of this nature, but in our application the rank of the Bohr set will be rather large, and it will be important that this rank does not aﬀect the lower bound in correlations of the form (4.22). Fortunately, such a result is available, and will be crucial in the proofs of the two remaining claims (Corollary 4.13 and Theorem 8.1) needed to prove Theorem 1.1.

Here is a precise version of the claim.

- Theorem 4.12. Let S ⊂ Z/pZ be non-degenerate for some prime p, and


let 0 < η < 1/2. Let ρ0,ρ1 be real parameters with 0 < ρ1 < ρ0 < 1/2 and such that

C|S| η2

ρ1 (4.23)

ρ0 >

![image 107](<2017-green-new-bounds-szemer-edi_images/imageFile107.png>)

for a suﬃciently large absolute constant C. Let f : Z/pZ → C be a 1-bounded function such that

|Ef(h0 + h1)f(h0 + h′1)f(h′0 + h1)f(h′0 + h′1)| η (4.24) where h0,h′0,h1,h′1 are drawn independently and regularly from B(S,ρ0),

![image 108](<2017-green-new-bounds-szemer-edi_images/imageFile108.png>)

![image 109](<2017-green-new-bounds-szemer-edi_images/imageFile109.png>)

- B(S,ρ0), B(S,ρ1), B(S,ρ1) respectively. Then there exists ξ ∈ Z/pZ such that


P(n0 = n0)|Ef(n0 + n1)ep(−ξn1)|2 η/2

n0∈Z/pZ

where n0,n1 are drawn independently and regularly from B(S,ρ0),B(S,ρ1) respectively.

Proof. We thank Fernando Shao for supplying a proof of this result, which was considerably simpler than our original argument.

For this proof, which is Fourier-analytic in nature, it will be convenient to work explicitly with probability densities rather than probabilistic notation. (However, in the lengthier proof of the local inverse U3 theorem given in the next section, the probabilistic notation will be signiﬁcantly cleaner to use.) In this argument, all sums will be over Z/pZ. We abbreviate

pi(h) := pB(S,ρi)(h) = P(hi = h)

for i = 0,1 and h ∈ Z/pZ; clearly we have pi(h) 0 and

h

pi(h) = 1. (4.25)

The hypothesis (4.24) may be written as

p0(h0)p0(h′0)p1(h1)p1(h′1)f(h0 + h1)f(h0 + h′1)×

![image 110](<2017-green-new-bounds-szemer-edi_images/imageFile110.png>)

h0,h′

0,h1,h′

1

× f(h′0 + h1)f(h′0 + h′1) η (4.26) and our goal is to locate ξ ∈ Z/pZ such that

![image 111](<2017-green-new-bounds-szemer-edi_images/imageFile111.png>)

2

n0

p0(n0)

n1

p1(n1)f(n0 + n1)ep(−ξn1)

η/2.

The ﬁrst step is to replace the factor p0(h0) by the slightly diﬀerent factor

p01/2(h0+h1)p01/2(h0+h′1). If we use the elementary inequality |x1/2−y1/2| |x − y|1/2 for x,y 0 and then apply Cauchy-Schwarz, Lemma 4.4, and (4.23), we see that

h0

p01/2(h0 + h1)−p01/2(h0) p10/2(h0)

|p0(h0 + h1) − p0(h0)|1/2p10/2(h0)

h0

1/2

|p0(h0 + h1) − p0(h0)|

h0∈Z/pZ

bh1(h0)p0(h0 + h1) − bh1(h0)p0(h0))1/2

= (

h0∈Z/pZ

1/2

η C1/2

|S|ρ1 ρ0

≪

≪

![image 112](<2017-green-new-bounds-szemer-edi_images/imageFile112.png>)

![image 113](<2017-green-new-bounds-szemer-edi_images/imageFile113.png>)

for any h1 in the support of p1, where the 1-bounded function bh1 is given by bh1(h0) := sgn(p0(h0 + h1) − p0(h0)). Similarly we have

η C1/2

|p01/2(h0 + h′1) − p10/2(h0)|p10/2(h0 + h1) ≪

![image 114](<2017-green-new-bounds-szemer-edi_images/imageFile114.png>)

h0

whenever h′1 is also in the support of p1; by the triangle inequality, we conclude that

η C1/2

|p01/2(h0 + h1)p0(h0 + h′1)1/2 − p0(h0)| ≪

![image 115](<2017-green-new-bounds-szemer-edi_images/imageFile115.png>)

h0

for all h1,h′1 in the support of p1. From the 1-boundedness of f and (4.25), we conclude that

|p01/2(h0 + h1)p10/2(h0 + h′1) − p0(h0)|p0(h′0)p1(h1)p1(h′1)

h0,h′

0,h1,h′

1

η C1/2

f(h0 + h1)f(h0 + h′1)f(h′0 + h1)f(h′0 + h′1) ≪

![image 116](<2017-green-new-bounds-szemer-edi_images/imageFile116.png>)

![image 117](<2017-green-new-bounds-szemer-edi_images/imageFile117.png>)

.

![image 118](<2017-green-new-bounds-szemer-edi_images/imageFile118.png>)

If C is large enough, the left-hand side is thus bounded by 0.1η (say), so by (4.26) and the triangle inequality we conclude that

p01/2(h0 + h1)p10/2(h0 + h′1)p0(h′0)p1(h1)p1(h′1)

h0,h′

0,h1,h′

1

f(h0 + h1)f(h0 + h′1)f(h′0 + h1)f(h′0 + h′1)| 0.9η If we write

![image 119](<2017-green-new-bounds-szemer-edi_images/imageFile119.png>)

![image 120](<2017-green-new-bounds-szemer-edi_images/imageFile120.png>)

f0(n) := f(n)p10/2(n), (4.27) we may rewrite the above estimate as

p0(h′0)p1(h1)p1(h′1)

h0,h′

0,h1,h′

1

f0(h0 + h1)f0(h0 + h′1)f(h′0 + h1)f(h′0 + h′1)| 0.9η.

![image 121](<2017-green-new-bounds-szemer-edi_images/imageFile121.png>)

![image 122](<2017-green-new-bounds-szemer-edi_images/imageFile122.png>)

A similar argument then lets us replace p0(h′0) with p10/2(h′0+h1)p10/2(h′0+h′1), leaving us with

p0(h′0 + h1)1/2p0(h′0 + h′1)1/2p1(h1)p1(h′1)×

h0,h′

0,h1,h′

1

× f0(h0 + h1)f0(h0 + h′1)f(h′0 + h1)f(h′0 + h′1)| 0.8η. which we can simplify using (4.27) to

![image 123](<2017-green-new-bounds-szemer-edi_images/imageFile123.png>)

![image 124](<2017-green-new-bounds-szemer-edi_images/imageFile124.png>)

p1(h1)p1(h′1)f0(h0 + h1)f0(h0 + h′1)f0(h′0 + h1)f0(h′0 + h′1) 0.8η.

![image 125](<2017-green-new-bounds-szemer-edi_images/imageFile125.png>)

![image 126](<2017-green-new-bounds-szemer-edi_images/imageFile126.png>)

h0,h′

0,h1,h′

1

Making the change of variables n := h1 − h′1, we may rewrite the left-hand side as

(p1 ∗ ˜p1)(n)|(f0 ∗ f˜0)(n)|2

n

where f˜0(n) := f0(−n), and similarly for p1, and f ∗ g denotes the discrete convolution

![image 127](<2017-green-new-bounds-szemer-edi_images/imageFile127.png>)

f ∗ g(n) :=

f(m)g(n − m) Using the Fourier transform, we may then rewrite the previous bound as p4

m

|ˆp1(ξ′)|2|fˆ0(ξ)|2|fˆ0(ξ + ξ′)|2 0.8η (4.28)

ξ,ξ′

where

1 p n

fˆ(ξ) :=

f(n)ep(−ξn).

![image 128](<2017-green-new-bounds-szemer-edi_images/imageFile128.png>)

- From (4.25), the 1-boundedness of f, and the Plancherel identity we have


ξ

1 p n |f0(n)|2

|fˆ0(ξ)|2 =

![image 129](<2017-green-new-bounds-szemer-edi_images/imageFile129.png>)

1 p

.

![image 130](<2017-green-new-bounds-szemer-edi_images/imageFile130.png>)

By this, (4.28), and the pigeonhole principle, we may therefore ﬁnd ξ ∈ Z/pZ such that

|pˆ1(ξ′)|2|fˆ0(ξ + ξ′)|2 0.8η.

p3

ξ′∈Z/pZ

By the Plancherel identity again, the left-hand side may be rewritten as

2

n0 n1

f0(n0 − n1)p1(n1)ep(ξn1)

and hence (by replacing n1 with −n1 and using (4.27))

2

f(n0 + n1)p10/2(n0 + n1)p1(n1)ep(−ξn1)

n0 n1

0.8η.

By argument similar to those at the beginning of the proof, we may replace p01/2(n0 + n1) by p01/2(n0) and conclude that

2

f(n0 + n1)p10/2(n0)p1(n1)e(−ξn1)

0.7η,

n0 n1

and the claim follows.

As a corollary of this inverse theorem, we can establish that locally almost linear phases on Bohr sets can be approximated by globally linear phases; this will be needed in Section 7 to deal with poorly distributed quadratic factors.

Here is a precise statement.

Corollary 4.13. Let φ : n0 + B(S,ρ) → R/Z be a function on a shifted Bohr set n0 + B(S,ρ) which is “locally almost linear” in the sense that one has the bound

h S⊥ k S⊥ ρ2

(4.29)

φ(n0 +h+k)−φ(n0 +h)−φ(n0 +k)+φ(n0) R/Z A

![image 131](<2017-green-new-bounds-szemer-edi_images/imageFile131.png>)

for all h,k ∈ B(S,ρ/2) and some A 1. Then there exists ξ ∈ Z/pZ such that

h S⊥ ρ

ξh p R/Z ≪ A1/2|S|4

(4.30) for all h ∈ B(S,ρ).

φ(n0 + h) − φ(n0) −

![image 132](<2017-green-new-bounds-szemer-edi_images/imageFile132.png>)

![image 133](<2017-green-new-bounds-szemer-edi_images/imageFile133.png>)

Proof. By translating in space, we may normalise so that n0 = 0; by shifting φ by a phase, we may also suppose that φ(0) = 0. By replacing ρ with the smaller quantity ρ/A1/2 if necessary, we may normalise A to be 1 (note that (4.30) is trivial for h S⊥ ρ/A1/2). Thus, we now have a function φ : B(S,ρ) → R/Z with φ(0) = 0 such that the quantity

∂2φ(h,k) := φ(h + k) − φ(h) − φ(k) (4.31) obeys the bound

h S⊥ k S⊥ ρ2

∂2φ(h,k) R/Z

(4.32) for all h,k ∈ B(S,ρ/2), and our task is to locate ξ ∈ Z/pZ such that

![image 134](<2017-green-new-bounds-szemer-edi_images/imageFile134.png>)

h S⊥ ρ

ξh p R/Z ≪ |S|4

(4.33) for all h ∈ B(S,ρ).

φ(h) −

![image 135](<2017-green-new-bounds-szemer-edi_images/imageFile135.png>)

![image 136](<2017-green-new-bounds-szemer-edi_images/imageFile136.png>)

Let ρ0 := ρ/100, and set ρ1 := C|ρS|3 for some suﬃciently large absolute constant C. If we let f : Z/pZ → C be the 1-bounded function

![image 137](<2017-green-new-bounds-szemer-edi_images/imageFile137.png>)

f(x) := 1B(S,ρ)e(φ(x)) (4.34) and draw h0,h′0,h1,h′1 independently and regularly from B(S,ρ0), B(S,ρ0),

- B(S,ρ1), B(S,ρ1) respectively, then from (4.31) we have f(h0 + h1)f(h0 + h′1)f(h′0 + h1)f(h′0 + h′1)


![image 138](<2017-green-new-bounds-szemer-edi_images/imageFile138.png>)

![image 139](<2017-green-new-bounds-szemer-edi_images/imageFile139.png>)

= e ∂2φ(h0,h1) − ∂2φ(h′0,h1) − ∂2φ(h0,h′1) + ∂2φ(h′0,h′1) . Applying (4.32) and taking expectations, we conclude that

|Ef(h0 + h1)f(h0 + h′1)f(h′0 + h1)f(h′0 + h′1)| 1/2 (say). Applying Theorem 4.12 (which is applicable for C large enough), we may thus ﬁnd ξ ∈ Z/pZ such that

![image 140](<2017-green-new-bounds-szemer-edi_images/imageFile140.png>)

![image 141](<2017-green-new-bounds-szemer-edi_images/imageFile141.png>)

P(n0 = n0)|Ef(n0 + n1)ep(−ξn1)|2 1/4

n0∈Z/pZ

if n0,n1 are drawn independently and regularly from B(S,ρ0),B(S,ρ1) respectively. In particular, there exists n ∈ B(S,ρ0) such that

|Ef(n + n1)ep(−ξn1)| 1/4. By (4.34), (4.31) we have

f(n + n1) = e φ(n1) + φ(n) + ∂2φ(n,n1) so by (4.32) we conclude that

ξn1

Ee φ(n1) −

p ≫ 1. (4.35) For any h ∈ B(S,ρ1), we have from Lemma 4.4 that

![image 142](<2017-green-new-bounds-szemer-edi_images/imageFile142.png>)

ξ(n1 + h) p − Ee φ(n1) −

ξn1 p | ≪ |S|

h S⊥ ρ1

Ee φ(n1 + h) −

;

![image 143](<2017-green-new-bounds-szemer-edi_images/imageFile143.png>)

![image 144](<2017-green-new-bounds-szemer-edi_images/imageFile144.png>)

![image 145](<2017-green-new-bounds-szemer-edi_images/imageFile145.png>)

on the other hand, from (4.31) we have the identity

ξ(n1 + h) p

Ee φ(n1 + h) −

![image 146](<2017-green-new-bounds-szemer-edi_images/imageFile146.png>)

ξn1 p

ξh p

+ ∂2φ(n1,h) . Combining this with (4.32), (4.35), and (2.2), we conclude that

Ee φ(n1) −

= e φ(h) −

![image 147](<2017-green-new-bounds-szemer-edi_images/imageFile147.png>)

![image 148](<2017-green-new-bounds-szemer-edi_images/imageFile148.png>)

ξh p R/Z ≍ |e(φ(h) −

φ(h) −

![image 149](<2017-green-new-bounds-szemer-edi_images/imageFile149.png>)

ξh p

h S⊥ ρ1

) − 1| ≪ |S|

![image 150](<2017-green-new-bounds-szemer-edi_images/imageFile150.png>)

![image 151](<2017-green-new-bounds-szemer-edi_images/imageFile151.png>)

- for all h ∈ B(S,ρ1). As the claim (4.33) is trivial for h ∈ B(S,ρ)\B(S,ρ1), the claim follows.


5. Dilated tori

As mentioned in Example 3 of Section 3, in order to maintain good quantitative control (and speciﬁcally, Lipschitz norm control) on the functions

- F : G → [−1,1] used to build quadratic approximants, one needs to generalise the underlying domain G to more general tori than the standard tori (R/Z)d with the usual norm structure. It turns out that it will suﬃce to work with dilated tori of the form


d

(R/λiZ)

G =

i=1

where λ1,... ,λd 1 are real numbers. One can view this dilated torus as the quotient of Rd by a dilated lattice Γ := di=1 λiZ. We can place a “norm” on G by declaring x G for x ∈ G to be the Euclidean distance in Rd from x to Γ; this generalises the norm R/Z from Section 2. This in turn deﬁnes a metric dG on G by the formula

dG(x,y) := x − y G. The volume vol(G) of a dilated torus is deﬁned to be the product

d

vol(G) :=

λi = det(Γ).

i=1

It will be important to keep this quantity under control during the iteration process. In particular, when transforming from one dilated torus to another, the volume of the new torus should behave like a linear function of the existing torus; anything worse than this (e.g. quadratic behaviour) will lead to undesirable bounds upon iteration.

We deﬁne the Pontryagin dual Gˆ of a dilated torus G to be the lattice

d

1 λi

Gˆ :=

Z.

![image 152](<2017-green-new-bounds-szemer-edi_images/imageFile152.png>)

i=1

Elements k of this dual will be called dual frequencies of the torus. If k = (k1,... ,kd) is a dual frequency and x = (x1,... ,xd) is an element of G, we deﬁne the dot product k · x ∈ R/Z in the usual fashion as

k · x = k1x1 + ··· + kdxd noting that this gives a well-deﬁned element of R/Z.

A dual frequency k is said to be irreducible if it is non-zero, and not of the form k = nk′ for some other dual frequency k′ and some natural number n > 1. If a dual frequency k is irreducible, then its orthogonal complement

k⊥ := {x ∈ G : k · x = 0} is a (d−1)-dimensional subtorus of G; it inherits a metric dk⊥ from the torus

- G it lies in. We will need to pass to such a complement when dealing with poorly distributed quadratic factors (as in the third or fourth examples in Section 3), however we encounter the technical issue that these complements k⊥ will not quite be of the form of a dilated torus. However, we will be able to transform k⊥ into a dilated torus using a bilipschitz transformation, as the following result shows.


- Theorem 5.1. Let G = di=1(R/λiZ) be a dilated torus, and let k ∈ Gˆ be an irreducible dual frequency of G. Then there exists a dilated torus


G′ = di=1−1(R/λ′iZ) and a Lie group isomorphism ψ : k⊥ → G′ obeying the bilipschitz bounds

ψ Lip, ψ−1 Lip ≪ dO(d) (5.1) and such that one has the volume bound

vol(G′) = dO(d)|k|vol(G) (5.2) where |k| denotes the Euclidean magnitude of k in Rd.

Proof. The case d = 0 is vacuous and the case d = 1 is trivial, so we may assume d > 1. One can identify k⊥ with the quotient V/Γ, where V := {x ∈ Rd : k · x = 0} is the hyperplane in Rd orthogonal to k (now

viewed as an element of Rd), and Γ := V ∩ di=1(λiZ) is the restriction of the lattice di=1(λiZ) to V .

As k is irreducible, there exists a vector e in the lattice di=1(λiZ) with k · e = 1; thus e has distance 1/|k| to V . One can form a fundamental domain of Rd/ di=1(λiZ) by taking any fundamental domain for V/Γ and performing the Minkowski sum of that domain with the interval {te : 0

t 1}. By Fubini’s theorem, the d-dimensional Lebesgue measure of such a sum will equal the (d−1)-dimensional Lebesgue measure of the fundamental

domain of V/Γ and 1/|k|; thus the covolume of di=1(λiZ) in Rd equals 1/|k| times the covolume of Γ in V . As the former covolume (determinant) is

d i=1 λi = vol(G), we conclude that Γ has covolume |k|vol(G) in V .

Applying Lemma 4.8, we can ﬁnd linearly independent elements v1,... , vd−1 generating Γ such that

r

BV (0,O(d)−3d/2t) ∩ Γ ⊂ {

nivi : |ni| tNi} ⊂ BV (0,t) ∩ Γ (5.3)

i=1

for all t > 0, where BV (0,r) is the Euclidean ball of radius r in V , and the ni are understood to be integers, with the bound

d−1

Ni−1 = (2d)O(d)|k|vol(G). (5.4)

i=1

- From (5.3) we conclude in particular that


O(d)−3d/2Ni−1 |vi| Ni−1 (5.5) for all 1 i d.

We now deﬁne the (d − 1)-dimensional dilated torus

d−1

(R/Ni−1Z)

G′ :=

i=1

and the isomorphism φ : V/Γ → G′ by the formula

d−1

tivi(mod Γ)) := (t1N1−1,... ,td−1Nd−−11)(mod

φ(

i=1

d−1

Ni−1Z)

i=1

for real numbers t1,... ,td−1. It is easy to see that this is a Lie group isomorphism, and the bound (5.2) follows from (5.4). It remains to establish the bilipschitz bounds (5.1). It suﬃces to show that the linear isomorphism

d−1

tivi  → (t1N1−1,... ,td−1Nd−−11)

i=1

from V to Rd−1, together with its inverse, have an operator norm of O(dO(d)). For the inverse map, this is clear from (5.5). For the forward map, it suﬃces from Crame´r’s rule to show that

dO(d) λ′

|v1 ∧ ··· ∧ vi−1 ∧ x ∧ vi+1 ∧ ··· ∧ vd−1| |v1 ∧ ··· ∧ vd−1|

≪

![image 153](<2017-green-new-bounds-szemer-edi_images/imageFile153.png>)

![image 154](<2017-green-new-bounds-szemer-edi_images/imageFile154.png>)

i

- for all i = 1,... ,d−1 and all unit vectors x in V . But from (5.5) the numerator is at most 1 i′ d−1:i′ =i Ni−′ 1, while the denominator is the volume of


a fundamental domain in V and is thus equal to dO(d)N1−1 ... Nd−−11 thanks to (5.4). The claim follows.

6. Constructing the approximants

In this section we construct the abstract directed graph G = (V,E) that appears in Proposition 3.3. For the rest of the paper, the prime p, the function f : Z/pZ → [−1,1], and the parameter η with 0 < η 10 1 are ﬁxed, and we assume that (3.21) holds.

![image 155](<2017-green-new-bounds-szemer-edi_images/imageFile155.png>)

We begin with a description of the structured approximants v ∈ V .

- Deﬁnition 6.1 (Structured local approximant). A structured local approximant is a tuple


v = (C,c,(nc + B(Sc,ρc))c∈C,(Gc)c∈C,(Fc)c∈C,(Ξc)c∈C) consisting of the following objects:

- • A ﬁnite non-empty set C;
- • A random variable c, which we call the label variable, taking values in C;
- • A shifted Bohr set nc + B(Sc,ρc) associated to each label c ∈ C;
- • A dilated torus Gc associated to each label c ∈ C;
- • A 1-Lipschitz function Fc : Gc → [−1,1] associated to each label c ∈ C; and
- • A locally quadratic function Ξc : nc + B(Sc,ρc) → Gc associated to each label c ∈ C.


We denote the collection of all structured local approximants (up to isomorphism3) as V . Given any structured local approximant v ∈ V , we deﬁne the random variables (av,rv,fv) associated to v by the following construction.

- 1. First, let c be the random label variable appearing above.
- 2. For each c ∈ C in the essential range of c, if we condition on the event c = c, we draw av,rv independently and regularly from nc + B(Sc,ρc/2) and B(Sc,exp(−η−C4)ρc) respectively, and then we let fv be the function


fv(a) := Fc(Ξc(a)).

Thus fv is deterministic when c is conditioned to be ﬁxed, but random when c is allowed to vary.

We also deﬁne the following additional statistics of the structured local approximant v:

- • The waste waste(v) is the quantity |Ef(a) − Ea∈Z/pZf(a)|;
- • The 1-error Err1(v) is |Ef(a) − Ef(a)|;
- • The 4-error Err4(v) is |Λa,r(f) − Λa,r(f)|;
- • The energy Energy(v) is E|f(a) − f(a)|2;
- • The linear rank d1(v) is maxc∈C |Sc|;
- • The quadratic dimension d2(v) is maxc∈C dim(Gc);
- • The linear scale ρ(v) is minc∈C ρc;


![image 156](<2017-green-new-bounds-szemer-edi_images/imageFile156.png>)

3This caveat is needed for the technical reason that V should be a set and not a proper class.

- • The quadratic volume vol(v) is the quantity maxc∈C vol(Gc);
- • The poorly distributed quadratic dimension dpoor2 (v) is the maximum value of dim(Gc) over all poorly distributed c in the essential range of c, or zero if no such c exists. Here, an element c in the essential range of c is said to be poorly distributed if one has


η 2

Λa,r(f|c = c) < E(f(a)|c = c)4 −

. (6.1)

![image 157](<2017-green-new-bounds-szemer-edi_images/imageFile157.png>)

This gives the set V of structured local approximants for Proposition 3.3; we clearly have 0 dpoor2 (v) d2(v) for all v ∈ V .

We now also deﬁne the initial approximant.

- Deﬁnition 6.2. The initial approximant v0 ∈ V is deﬁned to be the tuple v0 = (C,c,(nc + B(Sc,ρc))c∈C,(Gc)c∈C,(Fc)c∈C,(Ξc)c∈C)

deﬁned as follows:

- • C := Z/pZ, and c is drawn uniformly from C.
- • For each c ∈ C, we have nc := 0, Sc := {1}, and ρc := 1.
- • For each c ∈ C, the group Gc is the standard 0-torus (R/Z)0 (that is to say, a point).
- • For each c ∈ C, the function Fc : Gc → [−1,1] is the zero function Fc(x) := 0.
- • For each c ∈ C, the function Ξc : Z/pZ → Gc is the unique (constant) map from Z/pZ to the point Gc.


By chasing the deﬁnitions, we see that av0 is uniformly distributed in Z/pZ, and we can compute several of the statistics of the initial approximant v0:

waste(v0) = dpoor2 (v0) = d2(v0) = 0;d1(v0) = ρ(v) = vol(v) = 1. (6.2) Now we deﬁne the edges of the graph G(V,E).

- Deﬁnition 6.3. We let E be the set of all directed edges v → v′, where v,v′ ∈ V are structured local approximants such that


d1(v′) d1(v) + η−C2 d2(v′) d2(v) + 1

ρ(v′) exp(−η−C5)ρ(v)

vol(v′) exp(η−C3)vol(v) |waste(v) − waste(v′)| ηC3.

From this deﬁnition and (6.2) we have the following bounds on the various statistics of vertices of V that are not too far from the initial vertex v0, assuming that each constant Ci is chosen suﬃciently large depending on the preceding constants C1,... ,Ci−1.

- Lemma 6.4. Suppose a vertex v = vk ∈ V can be reached from v0 by a path v0 → v1 → ··· → vk with 0 k 8η−2C2. Then we have


d1(v) 8η−3C2 (6.3) d2(v) 8η−2C2 (6.4)

ρ(v) exp(−η−2C5) (6.5) vol(v) exp(η−2C3) (6.6)

waste(v) ηC3/2 (6.7)

From (6.7) we see in particular that the almost uniformity axiom in Proposition 3.3(ii) is obeyed. The thickness axiom in Proposition 3.3(i) is also easy, as the following corollary shows.

Corollary 6.5. Suppose a quadratic approximant v = vk ∈ V can be reached from v0 by a path v0 → v1 → ··· → vk of length k at most 8η−2C2. Then we have P(rv = 0) ≪ exp(η−C52)/p.

Proof. Write

v = (C,c,(nc + B(Sc,ρc))c∈C,(Gc)c∈C,(Fc)c∈C,(Ξc)c∈C) . It suﬃces to show that

P(rv = 0|c = c) ≪ exp(η−C52)/p

for each c in the essential range of c. But once c is ﬁxed to equal c, then rv is drawn regularly from nc + B(Sc,exp(−η−C4)ρc). By Lemma 6.4, Sc has cardinality at most 8η−3C2 and ρc is at least exp(−η−2C5). The claim now follows from Lemma 4.2.

It remains to verify the last two axioms (iii), (iv) of Proposition 3.3. We isolate these statements formally, using Lemma 6.4 and Deﬁnition 6.3.

The ﬁrst of these results, Theorem 6.6, states that “a bad approximation implies an energy decrement”. The second, Theorem 6.7, states that “a bad lower bound implies a dimension increment”.

- Theorem 6.6. Let the notation and hypotheses be as above. Suppose that v ∈ V is a structured local approximant obeying (6.3)-(6.6). If we have


Err1(v) > η (6.8) or

Err4(v) > η (6.9)

then there exists a structured local approximant v′ obeying the bounds

d(v′) d(v) + η−C2 (6.10) d2(v′) d2(v) + 1 (6.11)

ρ(v′) exp(−η−C5)ρ(v) (6.12) vol(v′) exp(η−C3)vol(v) (6.13)

|waste(v′) − waste(v)| ηC3 (6.14) Energy(v′) Energy(v) − ηC2. (6.15)

- Theorem 6.7. Let the notation and hypotheses be as above. Suppose that

v ∈ V is a structured local approximant obeying (6.3)-(6.6), and let av,rv,fv be the random variables associated to v. If we have

Λav,rv(fv) (Efv(av))4 − η, (6.16) then there exists a quadratic approximant v′ ∈ V with

d(v′) d(v) + η−C2 (6.17) d2(v′) d2(v) (6.18)

dpoor2 (v′) dpoor2 (v) − 1 (6.19)

ρ(v′) exp(−η−C5)ρ(v) (6.20) vol(v′) exp(η−C3)vol(v) (6.21)

|waste(v′) − waste(v)| ηC3 (6.22) Energy(v′) Energy(v) + η3C2. (6.23)

It remains to prove Theorem 6.6 and Theorem 6.7. Theorem 6.6 will be proven in Section 8 using a diﬃcult local inverse Gowers theorem, Theorem

- 8.1, that will be proven in later sections. Theorem 6.7, on the other hand, will not rely on the local inverse Gowers theorem; it is proven in Section 7.


7. Bad lower bound implies dimension decrement

In this section we prove Theorem 6.7. Let the notation and hypotheses be as in Theorem 6.7. We abbreviate av,rv,fv as a,r,f respectively. We can write the left-hand side of (6.16) as EA(c), where for any c ∈ C, the quantity A(c) is deﬁned as the conditional expectation

A(c) := Λa,r(f|c = c). Similarly, we can write Ef(a) = EB(c), where B(c) := E(f(a)|c = c). By

- (6.16) and H¨older’s inequality, we thus have EB(c)4 − A(c) η.


- Applying Lemma 2.2, we must therefore have P(B(c)4 − A(c) > η/2) ≫ η.


By (6.1), we conclude that c is poorly distributed with probability ≫ η. In particular, there is at least one poorly distributed value of c.

Most of this section will be devoted to the proof of the following proposition, which roughly speaking asserts that when c is poorly distributed, there is a linear constraint between the quadratic frequencies which will ultimately allow us to decrease the poorly distributed quadratic dimension dpoor2 .

Proposition 7.1. Let c be a poorly distributed element of the essential range of c. Then there exists a natural number mc, a frequency ξc ∈ Z/pZ and an irreducible dual frequency kc′ ∈ Gˆc with

1 mc ≪ exp(η−4C3) (7.1) and

exp(−η−4C3) ≪ |kc′| ≪ exp(η−3C2) (7.2) such that

kc′ · Ξc(a + 2mch) − kc′ · Ξc(a) R/Z ≪ exp(−η−3C4) (7.3) for all a ∈ B(Sc,ρc/2) and h ∈ B(Sc ∪ {ξc},exp(−η−5C4)ρ).

A key technical point here is that the upper bound on |kc′| involves only C2 and not C3 or C4; this is necessary in order to keep the bounds under control during the iteration process. However, we will be able to tolerate the presence of the C3 and C4 constants in the other components of Proposition 7.1.

Proof. We condition on the event c = c. By Deﬁnition 6.1, the random variables a,r are now independent and regularly drawn from nc+B(Sc,ρc/2) and B(Sc,exp(−η−C4)ρc) respectively, while f(n) = Fc(Ξc(a)). We conclude that

E(Fc(Ξc(a))Fc(Ξc(a + r))Fc(Ξc(a + 2r))Fc(Ξc(a + 3r))|c = c) < E(Fc(Ξc(a))|c = c)4 − η/2.

Since Ξc : Z/pZ → Gc is locally quadratic on nc + B(Sc,ρc), which contains the progression a,a + r,a + 2r,a + 3r, we see from (4.17) that

Ξc(a) − 3Ξc(a + r) + 3Ξc(a + 2r) − Ξc(a + 3r) = 0 and so the left-hand side can be written as

E(Fc(3)(Ξc(a),Ξc(a + r),Ξc(a + 2r))|c = c), where Fc(3) : G3c → [−1,1] is the function

Fc(3)(x0,x1,x2) := Fc(x0)Fc(x1)Fc(x2)Fc(x0 − 3x1 + 3x2).

- Applying Lemma 3.2, we have


Fc(3)(x0,x1,x2) dµc(x0)dµc(x1)dµc(x2)

G3c

Fc(x) dµc(x)

Gc

4

where µc is the probability Haar measure on Gc. By the triangle inequality, we conclude that at least one of the assertions

E(Fc(3)(Ξc(a),Ξc(a + r),Ξc(a + 2r))|c = c)

Fc(3)(x0,x1,x2) dµc(x0)dµc(x1)dµc(x2) ≫ η or

−

G3c

E(Fc(Ξc(a))|c = c) −

Fc(x) dµc(x) ≫ η holds. Deﬁning F˜ : G3c → [−1,1] by F˜(x0,x1,x2) =

Gc

1 10

Fc(3)(x0,x1,x2) dµc(x0)dµc(x1)dµc(x2) in the former case and

Fc(3)(x0,x1,x2) −

![image 158](<2017-green-new-bounds-szemer-edi_images/imageFile158.png>)

G3c

1 10

F˜(x0,x1,x2) :=

Fc(x0) dµc(x0) in the latter case, we see that F˜ is 1-Lipschitz and of mean zero, and

Fc(x0) −

![image 159](<2017-green-new-bounds-szemer-edi_images/imageFile159.png>)

Gc

|E(F˜(xc)|c = c)| ≫ η (7.4) where xc ∈ G3c is the random variable

xc := (Ξc(a),Ξc(a + r),Ξc(a + 2r)). The Weyl equidistribution criterion, applied in the contrapositive, then suggests that there should be a non-zero dual frequency k = (k1,k2,k3) ∈ Gˆ3c to G3c such that E(e(k · xc)|c = c) is large. The next lemma makes this intuition precise.

- Lemma 7.2 (Weyl equidistribution). With the notation and hypotheses as


above, there exists a non-zero dual frequency k = (k1,k2,k3) ∈ Gˆ3c to G3c with |k| ≪ exp(O(η−3C2)) such that

|E(k · xc|c = c)| ≫ exp(−O(η−3C2))/vol(Gc).

A key point here is that the bound on |k| does not depend on the volume of the dilated torus Gc, which will typically be much larger than η−2C2−10. Proof. Write Gc = di=1(R/λiZ), thus λ1,... ,λd 1, and by (6.4) one has

d 8η−2C2. (7.5) The bound (7.4) is not possible when d = 0, so we may assume d 1. We can write G3c = 3i=1d (R/λiZ), where we extend λi periodically with period d.

Let ϕ : R → R be a ﬁxed smooth even function supported on [−1,1] that

equals 1 at the origin and whose Fourier transform ϕˆ(ξ) := R φ(x)e(−xξ) dx is non-negative; such a function may be easily constructed by convolving an

L2-normalised smooth function on [0,1] with its reﬂection. Let A 1 be a

parameter to be chosen later, and introduce the kernel K : G3c → R+ by the formula

3d

K(t1,... ,t3d) :=

Ki(ti)

i=1

for ti ∈ R/λiZ, where

ki A

Ki(ti) :=

e(kiti).

ϕ

![image 160](<2017-green-new-bounds-szemer-edi_images/imageFile160.png>)

ki∈λ1

Z

![image 161](<2017-green-new-bounds-szemer-edi_images/imageFile161.png>)

i

By Poisson summation, the Ki and hence K are non-negative. A Fourieranalytic calculation using the smoothness of ϕ gives

dti λi

= 1

Ki(ti)

![image 162](<2017-green-new-bounds-szemer-edi_images/imageFile162.png>)

R/λiZ

and

dti λi ≪

1 A2λ2i (where the implied constant is allowed to depend on ϕ) and hence by (2.2) and Cauchy-Schwarz we have

Ki(ti)sin2(πti/λi)

![image 163](<2017-green-new-bounds-szemer-edi_images/imageFile163.png>)

![image 164](<2017-green-new-bounds-szemer-edi_images/imageFile164.png>)

R/λiZ

Ki(ti) ti R/Z

R/λiZ

dti λi ≪

1 A

,

![image 165](<2017-green-new-bounds-szemer-edi_images/imageFile165.png>)

![image 166](<2017-green-new-bounds-szemer-edi_images/imageFile166.png>)

which on taking tensor products gives

K(x) dµ3c(x) = 1 and

G3c

d A

dµ3c(x) ≪

K(x) x G3

,

![image 167](<2017-green-new-bounds-szemer-edi_images/imageFile167.png>)

c

G3c

where µ3c is the Haar probability measure on G3c. If we then take the convolution

F˜(x − y)K(y) dµ3c(y) then by the 1-Lipschitz nature of F˜ we see that

F˜ ∗ K(x) :=

Gc

d A

F˜ ∗ K(x) = F˜(x) + O

. Thus, if we choose

![image 168](<2017-green-new-bounds-szemer-edi_images/imageFile168.png>)

Cd η

A :=

![image 169](<2017-green-new-bounds-szemer-edi_images/imageFile169.png>)

for a suﬃciently large absolute constant C, we conclude from (7.4) that |E(F˜ ∗ K(xc)|c = c)| ≫ η.

However, by Fourier expansion and the fact that F˜ has mean zero,

3d

ki A

) F ˜(k)Ee(k · x)

F˜ ∗ K(xc) =

ϕ(

![image 170](<2017-green-new-bounds-szemer-edi_images/imageFile170.png>)

i=1

k∈Gˆ3c\{0}

where k = (k1,... ,k3d) with ki ∈ λ1iZ for i = 1,... ,3d, and F ˜(k) :=

![image 171](<2017-green-new-bounds-szemer-edi_images/imageFile171.png>)

F˜(x)e(−k · x) dµ3c(x).

G3c

Using the triangle inequality and crudely bounding |F ˜(k)| by 1, we conclude that

d

ki A |E(e(k · xc)|c = c)| ≫ η.

ϕ

![image 172](<2017-green-new-bounds-szemer-edi_images/imageFile172.png>)

i=1

k∈Gˆ3c\{0}

The summand is only non-vanishing when supi |ki| A, so that |k| dA ≪ exp(O(η−3C2)) (thanks to (7.5) and the choice of A), and the number of such k is

3d

(Aλi) ≪ exp(O(η−3C2))vol(T). Since ϕ is bounded, the claim now follows from the pigeonhole principle.

O

i=1

We return to the proof of Proposition 7.1. Applying Lemma 7.2 and (6.5), we see that there exists a non-zero triplet (kc0,kc1,kc2) ∈ Gˆ3c with

|kc0|,|kc1|,|kc2| ≪ exp(η−3C2) (7.6) and

E e(kc0 · Ξc(a) + kc1 · Ξc(a + r) + kc2 · Ξc(a + 2r))|c = c ≫ exp(−η−3C3).

(7.7) Among other things, the non-zero nature of this triplet forces Gc to be non-trivial, and thus

dpoor2 (v) 1.

We also emphasise that the bound (7.6) involves C2 rather than C3; this will become important when establishing the important upper bound of

- (7.2) later in this proof. We can use the exponential sum bound (7.7) to control the “second de-


rivative” of Ξc. Indeed, for any h1,h2 ∈ B(Sc,ρc/10), deﬁne the quantity ∂2Ξc(h1,h2) ∈ R/Z by

∂2Ξc(h1,h2) := Ξc(a + h1 + h2) − Ξc(a + h1) − Ξc(a + h2) + Ξc(a)

for any a ∈ nc + B(Sc,ρ/2). Since Γc is locally quadratic on nc + B(Sc,ρ), this quantity is well-deﬁned, symmetric in h1,h2, and is also locally bilinear in h1 and h2.

- Lemma 7.3. Let the notation and hypotheses be as above. Then for any i = 0,1,2, we have


E e(2kci · ∂2Ξc(r − r′,h − h′))|c = c ≫ exp(−4η−3C3), where, conditioning on the event c = c, the random variables r,r′,h,h′ are drawn independently and regularly from the Bohr sets B(Sc,exp(−η−C4)ρ), B(Sc,exp(−η−C4)ρ), B(Sc,exp(−η−2C4)ρ), B(Sc,exp(−η−2C4)ρ) respectively,

independently of a.

Proof. To simplify the notation we only consider the i = 2 case, as the i = 0,1 cases are similar. This will be “Weyl diﬀerencing” argument that relies primarily on the Cauchy-Schwarz inequality.

Recall that after conditioning to the event c = c, the random variable a is drawn regularly from B(Sc,ρ/2). Using Lemma 4.4, we see that a and a−h diﬀer in total variation by O(exp(−η−C4/2)), hence from (7.7) we have

E e(kc0 · Ξc(a − h) + kc1 · Ξc(a − h + r) + kc2·Ξc(a − h + 2r))|c = c ≫ exp(−η−3C3). Similarly we may use Lemma 4.4 to compare r and r+h, and conclude that E e(kc0 · Ξc(a − h) + kc1 · Ξc(a + r) + kc2·Ξc(a + h + 2r))|c = c

≫ exp(−η−3C3), By the pigeonhole principle (and independence of a,h,r relative to the event c = c), we may thus ﬁnd ac ∈ nc + B(Sc,ρ/2) such that

E e(kc0 · Ξc(ac − h) + kc1 · Ξc(ac + r) + kc2·Ξc(ac + h + 2r))|c = c

≫ exp(−η−3C3). Using the identity

Ξc(ac + h + 2r) = Ξc(ac + h) + Ξc(ac + 2r) − Ξc(ac) + ∂2Ξc(2r,h) we can rewrite the left-hand side as

E b1(r)b2(h)e(kc2 · ∂2Ξc(2r,h))|c = c ≫ exp(−η−3C3) where b1,b2 : B(Sc,ρ) → C are the 1-bounded functions

b1(r) := e(kc1 · Ξc(ac + r) + kc2 · Ξc(ac + 2r) − kc2 · Ξc(ac)) and

b2(h) := e(kc0 · Ξc(ac − h) + kc2 · Ξc(ac + h)). Applying Lemma 2.1 to eliminate the b1(r) factor, we conclude that

E b2(h)b2(h′)e(kc2 · ∂2Ξc(2r,h − h′))|c = c ≫ exp(−2η−3C3).

![image 173](<2017-green-new-bounds-szemer-edi_images/imageFile173.png>)

![image 174](<2017-green-new-bounds-szemer-edi_images/imageFile174.png>)

- Applying Lemma 2.1 again to eliminate the b2(h)b2(h′) factor, we obtain the claim.


We return to the proof of Proposition 7.1. Let i = ic ∈ {0,1,2} be such

that kci is non-zero. Let r,r′,h,h′ be as in the above lemma, and let h′′ be a further independent copy of h or h′, thus h′′ is also drawn regularly from

B(Sc,exp(−η−2C4)ρ) and independently of r,r′,h,h′ (after conditioning on c = c). Applying Lemma 4.4 to compare r with r + h′′, we have

|E(e(2kci · ∂2Ξc(r − r′ + h′′,h − h′))|c = c)| ≫ exp(−4η−3C3),

so by the pigeonhole principle we can ﬁnd r,r′,h′ ∈ B(Sc,exp(−η−C4)ρc) (depending on c, of course) such that

|E(e(2kci · ∂2Ξc(r − r′ + h′′,h − h′))|c = c)| ≫ exp(−4η−3C3). By the local bilinearity of ∂2Ξc, we may thus have

|E(e(2kci · ∂2Ξc(h′′,h) + ψ(h) + ψ′′(h′′))|c = c)| ≫ exp(−4η−3C3)

for some locally linear functions ψ,ψ′′ : B(Sc,ρ/100) → R/Z (which can depend on c).

Applying Proposition 4.11 (recalling from (6.3) that |Sc| 8exp(−3C2)), we conclude that there exists a non-zero multiple kc ∈ Gˆc of kci with

kc ≪ exp(η−4C3) (7.8) such that

n Sc m Sc ρ2c

kc · ∂2Ξc(n,m) R/Z ≪ exp(η−3C4)

(7.9) for n,m ∈ B(Sc,exp(−η−3C4)ρc).

![image 175](<2017-green-new-bounds-szemer-edi_images/imageFile175.png>)

Applying Corollary 4.13, we may thus ﬁnd ξc ∈ Z/pZ such that kc · Ξc(nc + h) − kc · Ξc(nc) −

ξch p R/Z ≪ exp(η−4C4)

h Sc ρc

(7.10)

![image 176](<2017-green-new-bounds-szemer-edi_images/imageFile176.png>)

![image 177](<2017-green-new-bounds-szemer-edi_images/imageFile177.png>)

for all n ∈ Z/pZ (of course, the bound is only non-trivial when h lies in the Bohr set B(Sc,exp(−η−4C4)ρ)).

The dual frequency kc ∈ Gc is non-zero, but not necessarily irreducible. However, we may write kc = mckc′ where mc is a positive natural number and kc′ ∈ Gc is irreducible, thus by (7.8) we have the bound (7.1). The same argument gives the bound kc′ ≪ exp(η−4C3), but this is not suﬃcient to establish the upper bound in (7.2). However, observe that kci must also be a multiple of the irreducible vector kc′, and now the upper bound in (7.2) follows from (7.6).

We can also obtain a lower bound on kc′ by observing that the slab x ∈ Gc : kc′ · x R/Z

- 1

![image 178](<2017-green-new-bounds-szemer-edi_images/imageFile178.png>)

- 2|kc′|


has measure at most |kc′|vol(Gc), and contains the Euclidean ball of radius 1/2 centred at the origin. This gives the lower bound

1 dim(Gc)O(dim(Gc)) vol(Gc)

|kc′| ≫

![image 179](<2017-green-new-bounds-szemer-edi_images/imageFile179.png>)

- which by (6.4), (6.6) gives the lower bound in (7.2).


Now let a ∈ B(Sc,ρc/2) and h ∈ B(Sc ∪ {ξc},exp(−η−5C4)ρc). Then we have

jh ∈ B(Sc,2mc exp(−η−5C4)ρc) and

jξch p R/Z ≪ exp(−η−5C4)ρc

![image 180](<2017-green-new-bounds-szemer-edi_images/imageFile180.png>)

- for all j, 0 j 2mc. From (7.10) and (7.1), we conclude that


kc · Ξc(nc + jh) − kc · Ξc(nc) R/Z ≪ exp(−η−4C4) (say). On the other hand, from (7.9) we have

kc · (Ξc(a + jh) − Ξc(a) − Ξc(nc + jξch) + Ξc(nc)) R/Z ≪ exp(−η−4C4) and hence by the triangle inequality we have

kc · Ξc(a + jh) − kc · Ξc(a) R/Z ≪ exp(−η−4C4) (7.11) for all j, 0 j 2mc.

This is close to (7.3), but we will need to replace the dual frequency kc here with the irreducible dual frequency kc′. To do this, we ﬁrst observe that as Ξc is locally quadratic on nc + B(Sc,ρc), we may write

Ξc(a + jh) = α + βj + γj2 (7.12)

for all j, 0 j 2mc, and some α,β,γ ∈ Gc depending on c,a,h. Inserting this formula into the preceding estimate, we conclude that

j(kc · β) + j2(kc · γ) R/Z ≪ exp(−η−4C4)

for j, 0 j 2mc. Applying this for j = 1,2 and using the triangle inequality, we have

kc · β , 2(kc · γ) R/Z ≪ exp(−η−4C4)

Since 2mckc′ = 2kc and (2mc)2kc′ = (2mc)2kc, we conclude in particular (using (7.1)) that

2mc(kc′ · β) R/Z, (2mc)2(kc′ · γ) R/Z ≪ exp(−η−3C4) and thus by (7.12) we obtain (7.3) as desired. This ﬁnally completes the proof of Proposition 7.1.

We now return to the proof of Theorem 6.7. We are given a structured local approximant

v = (C,c,(nc + B(Sc,ρc))c∈C,(Gc)c∈C,(Fc)c∈C,(Ξc)c∈C) and need to construct a modiﬁcation

v′ = C′,c′,(n′c′ + B(Sc′′,ρ′c′))c′∈C′,(G′c′)c′∈C′,(Fc′′)c′∈C′,(Ξ′c′)c′∈C′

that somehow incorporates the linear constraint identiﬁed in Proposition 7.1 in order to decrement the poorly distributed quadratic dimension of v′, in the spirit of the third and fourth examples in Section 3. To avoid confusion, we

shall restore the subscripts (av,rv,fv) on the random variables associated to v as per Deﬁnition 6.1, in order to distinguish them from the corresponding

random variables (av′,rv′,fv′) that will be associated to v′. We shall set C′ := (Z/pZ) × C, and let c′ be the random variable

c′ := (av,c). Clearly c′ takes values in the non-empty ﬁnite set C′. Now we need to deﬁne n′c′,Sc′′,ρ′c′,G′c′,Fc′′,Ξ′c′ for any given c′ = (a,c) in C′. In the case where c is not poorly distributed, we simply carry over the corresponding data from v without further modiﬁcation. That is to say, we deﬁne

(n′c′,Sc′′,ρ′c′,G′c′,Fc′′,Ξ′c′ := (nc,Sc,ρc,Gc,Fc,Ξc) whenever c′ = (a,c) with c not poorly distributed. If instead c′ = (a,c) with c poorly distributed, then we introduce the natural number mc, the dual frequency kc′ ∈ Gˆc, and the frequency ξc ∈ Z/pZ from Proposition 7.1; of course we can arrange matters so that mc,kc′,ξc depend only on c and not on a. Because of (7.1) and the hypothesis (3.21), the quantity 2mc is invertible in the ﬁeld Z/pZ, and so we may deﬁne the dilate (2mc)−1 · Sc of Sc inside Z/pZ, and can similarly deﬁne the dilate (2mc)−1ξc of ξc. We will need to do this division here in order to cancel some denominators appearing later in the argument.

In this poorly distributed case, we deﬁne the “linear” data n′c′,Sc′′,ρ′c′ by n′c′ := a Sc′′ := (2mc)−1 · Sc ∪ {(2mc)−1ξc} ρ′c′ := exp(−η−6C4)ρc,

thus the shifted Bohr set n′c′ + B(Sc′′,ρ′c′) will be a small subset of nc + B(Sc,ρc) in which the radius ρc has been reduced and an additional frequency ξc/2mc has been added. As we shall see, this particular choice of this linear data will allow us to utilise the approximate constraint (7.3).

The constraint (7.3) has the eﬀect of approximately restricting Ξc (on a suitable Bohr set) to a coset of the orthogonal complement (kc′)⊥ = {x ∈ Gc : kc′ · x = 0} of kc′ in Gc. Applying Theorem 5.1, (6.4), and the crucial bound (7.2), we may ﬁnd a dilated torus G˜c = i dim(=1 Gc)−1(R/λ˜c,iZ) with volume

vol(G˜c) ≪ exp(η−4C2)vol(Gc) (7.13)

as well as a Lie group isomorphism ψc : (kc′)⊥ → G˜c obeying the bilipschitz bounds

ψ Lip, ψ−1 Lip exp(η−4C2). In particular, if we deﬁne the even more dilated torus

dim(Gc)−1

(R/exp(η−4C2)λ˜c,iZ)

G′c :=

i=1

and let δc : G′c → G˜c be the rescaling map δc : (xi)idim(=1 Gc)−1  → (exp(−η−4C2)xi)idim(=1 Gc)−1

then we see that ψ−1 ◦ δc : G′c → (kc′)⊥ is a 1-Lipschitz Lie group isomorphism.

An element of n′c′ + B(Sc′,ρ′c) can be uniquely represented in the form n′c′+2mch for h ∈ B(Sc∪{ξc},exp(−η−6C4)ρc). From (7.3), we know that the point Ξc(n′c′ +2mch)−Ξc(n′c′) lies within a O(exp(−η−3C4))-neighbourhood of the subtorus (kc′)⊥. Using the lower bound in (7.2), we can ﬁnd a locally linear projection πc from this neighbourhood to the subtorus itself (e.g. by viewing the subtorus locally as a graph in dim(Gc) − 1 of the dim(Gc) coordinates and then projecting in the direction of the remaining coordinate), which moves each point in the neighbourhood by at most O(exp(−η−2C4)). From the 1-Lipschitz nature of Fc, we thus have

Fc(Ξc(n′c′ + 2mch))

= Fc πc Ξc(n′c′ + 2mch) − Ξc(n′c′) + Ξc(n′c′) + O(exp(−η−2C4)). We can rewrite this as

Fc(Ξc(n′c′ + 2mch)) = Fc′′(Ξ′c′(n′c′ + 2mch)) + O(exp(−η−2C4)) (7.14) where Fc′′ : G′c → [−1,1] is the 1-Lipschitz function

Fc′′(x) := Fc(ψc−1(δc(x))) + Ξc(n′c′) and Ξ′c′ : n′c′ + B(Sc′,ρ′c) → G′c takes the form

Ξ′c′(n′c′ + 2mch) := δc−1 ψc πc Ξc(n′c′ + 2mch) − Ξc(n′c′) + Ξc(n′c′) .

The map Ξ′c′ is the composition of a locally quadratic map with three locally linear maps, and is hence also locally quadratic. This concludes the

construction of all the required quadratic data G′c′,Fc′′,Ξ′c′ when c′ arises from a poorly distributed c.

It remains to verify the claims (6.17)-(6.23) of Theorem 6.7. The claim

(6.17) is clear; in fact, the frequency sets Sc′′ are either equal to their original counterparts Sc or have the addition of just one further frequency ξc, so we even obtain the improved bound d(v′) d(v) + 1 in our construction

here. Since the dilated torus G′c′ is either equal to Gc when c is not poorly distributed, or has one lower dimension than Gc if c is poorly distributed, we obtain the bounds (6.18), (6.19). Since ρ′c′ is either equal to ρc when c is not poorly distributed, or exp(−η−6C4)ρc when c is poorly distributed, we obtain(6.20) (with a little room to spare). As for the volume bound, G′c′ clearly has the same volume as Gc when c is not poorly distributed, and when c is poorly distributed we have

vol(G′c′) = exp(−η−4C2 dim(G˜c′))vol(G˜c′)

- which by (7.13), (6.3) is bounded in turn by exp(−η−5C2)vol(Gc), which yields (6.21), again with a little bit of room to spare (because the bounds


here only increased the volume by factors that involved C2 rather than C3). Now we establish (6.22). From the triangle inequality we have |waste(v′) − waste(v)| |Ef(av′) − Ef(av)|

P(c = c)|E(f(av′)|c = c) − E(f(av)|c = c)|

c∈C

so it will suﬃce to show that

|E(f(av′)|c = c) − E(f(av)|c = c)| ηC3 (7.15) for each c in the essential range of c.

The claim is trivial when c is not poorly distributed, since in this case av and av′ have identical distribution after conditioning to c = c. If c is poorly distributed, then (after conditioning to c = c) av is drawn regularly from nc + B(Sc,ρc/2), while av′ has the distribution of av + 2mchc where hc is drawn regularly from B(Sc ∪{ξc},exp(−η−6C4)ρc) independently of av (after conditioning to c = c). The required bound (6.22) now follows from Lemma 4.4 (and (6.3)).

Finally, we prove (6.23). Our task is to show that

E|f(av′) − fv′(av′)|2 E|f(av) − fv(av)|2 + η3C2. By the triangle inequality as before, it suﬃces to show that

E |f(av′) − fv′(av′)|2|c = c E |f(av) − fv(av)|2|c = c + η3C2

for all c in the essential range of c. This is trivial for c not poorly distributed, so assume c is poorly distributed. From (7.14) we then have

fv′(av′) = fv(av′) + O(exp(−η−2C4)) and also

fv(a) = Fc(Ξc(a)) for a ∈ B(Sc,ρc), so by the triangle inequality it suﬃces to show that

E |f(av′) − Fc(Ξc(av′))|2|c = c E |f(av) − Fc(Ξc(av))|2|c = c + η4C2 (say). But this follows by repeating the proof of (7.15), with the function f replaced by |f − Fc ◦ Ξc|2. This completes the proof of Theorem 6.7.

8. Bad approximation implies energy decrement

The remaining task in the paper is to prove Theorem 6.6. In this section we will establish this result contingent on a local inverse Gowers norm theorem (Theorem 8.1) that will be proven in later sections. We begin by stating the (rather technical) precise form of that theorem that we will need.

- Theorem 8.1 (Local inverse U3 theorem). Let p be a prime, and let S be a subset of Z/pZ containing at least one non-zero element. Let η be a real parameter with 0 < η < 21. Let K be the quantity


![image 181](<2017-green-new-bounds-szemer-edi_images/imageFile181.png>)

1 η

K :=

+ |S|, (8.1) and let ρ0,ρ1,ρ2,... ,ρ10 be real numbers satisfying

![image 182](<2017-green-new-bounds-szemer-edi_images/imageFile182.png>)

0 < ρ10 < ··· < ρ0 < 1/2 as well as the separation condition

ρi+1 exp(KC2)ρi (8.2) for all i = 0,... ,9. Assume that the prime p is huge relative to the reciprocal of these parameters, in the sense that

3 2

p ρ−KC

10 . (8.3) Let f : Z/pZ → C be a 1-bounded function such that

|Ef(h0 + h1 + h2)f(h0 + h′1 + h2)f(h′0 + h1 + h2)f(h′0 + h′1 + h2) f(h0 + h1 + h′2)f(h0 + h′1 + h′2)f(h′0 + h1 + h′2)f(h′0 + h′1 + h′2)| η

![image 183](<2017-green-new-bounds-szemer-edi_images/imageFile183.png>)

![image 184](<2017-green-new-bounds-szemer-edi_images/imageFile184.png>)

![image 185](<2017-green-new-bounds-szemer-edi_images/imageFile185.png>)

![image 186](<2017-green-new-bounds-szemer-edi_images/imageFile186.png>)

(8.4)

whenever h0,h′0,h1,h′1,h2,h′2 are drawn independently and regularly from

- B(S,ρ0), B(S,ρ0), B(S,ρ1), B(S,ρ1), B(S,ρ2), and B(S,ρ2) respectively. Then there exists a positive integer k < exp(KO(C1)), a set S′ ⊂ Z/pZ, S′ ⊃ S, with


|S′| |S| + O(η−O(C1)), (8.5)

a locally quadratic phase φ : B(S′,ρ9) → R/Z, and a function β : Z/pZ → Z/pZ such that

β(n)m p ≫ ηO(C1) (8.6)

P(n = n) Ef(n + km)e −φ(m) −

![image 187](<2017-green-new-bounds-szemer-edi_images/imageFile187.png>)

n∈Z/pZ

if n,m are drawn independently and regularly from BS(0,ρ0) and BS′(0,ρ10) respectively.

Remarks. The parameters ρ3,... ,ρ8 do not have any role in the statement of this result, but they appear in the proof. We have retained them to avoid a potentially confusing relabelling.

Informally, this theorem asserts that if f has a large U3 norm on B(S,ρ0),

then f will correlate with a locally quadratic phase n+km  → φ(m)+ β(np)m on translates n + k · BS′(0,ρ10) of k · BS′(0,ρ10), with polynomial bounds on the correlation. Although we will not make crucial use of this fact in our arguments, it may be noted that the homogeneous component φ of this locally quadratic phase does not depend on the translation parameter n. In the bounded rank case |S| = O(1), a theorem very roughly of this form was established in [21]; the key point in Theorem 8.1 is that the inverse theory

![image 188](<2017-green-new-bounds-szemer-edi_images/imageFile188.png>)

of [21] can be localised to a Bohr set without having the lower bound ηO(C1) on the correlation appearing in (8.6) depend on the rank |S| or radius ρ0 of the Bohr set (although these parameters certainly inﬂuence the range of the variables n,m appearing in (8.6)).

The proof of Theorem 8.1 will occupy most of the remainder of this paper. To a large extent, it may be understood separately of our main arguments, requiring little of the notation of Section 3, for example. In this section, we will assume Theorem 8.1 and use it to establish Theorem 6.6.

For the remainder of this section, the notation and hypotheses will be as in Theorem 6.6. Namely, we ﬁx a prime p, a function f : Z/pZ → [−1,1], and a parameter 0 < η 1/10, and assume (3.21). We also suppose that

v = (C,c,(nc + B(Sc,ρc))c∈C,(Gc)c∈C,(Fc)c∈C,(Ξc)c∈C)

is a structured local approximant obeying (6.3)-(6.6), and one of (6.8) or (6.9) holds. Our objective is to construct a structured local approximant

v′ = C′,c′,(n′c′ + B(Sc′′,ρ′c′))c′∈C′,(G′c′)c′∈C′,(Fc′′)c′∈C′,(Ξ′c′)c′∈C′

obeying the bounds (6.10)-(6.15). The situation here is a formalisation of Example 8 from Section 3.

Let a = av,r = rv,f = fv be the random variables associated to v in Deﬁnition 6.1. We can unify the hypotheses (6.8), (6.9) by introducing the quadrilinear form

Λa,r(f0,f1,f2,f3) := Ef0(a)f1(a + r)f2(a + 2r)f3(a + 3r),

deﬁned for arbitrary random (or deterministic) bounded functions f0,f1,f2, f3 : Z/pZ → R. From the deﬁnitions of Err1 and Err4 (just prior to (6.1)), the hypothesis (6.8) may be written as

|Λa,r(f,1,1,1) − Λa,r(f,1,1,1)| > η, while (6.9) can be similarly written as

|Λa,r(f,f,f,f) − Λa,r(f,f,f,f)| > η.

Applying the triangle inequality and the quadrilinearity of Λa,r, we conclude that

|Λa,r(f0,f1,f2,f3)| ≫ η

for some random functions f0,f1,f2,f3, each of which is either equal to 1, f, or f − f, and with at least one of the functions f0,f1,f2,f3 equal to f − f. For sake of concreteness we will assume that it is f3 that is equal to f − f, thus

|Λa,r(f0,f1,f2,f − f)| ≫ η; (8.7) the other cases are treated similarly (with some changes to the numerical constants below) and are left to the interested reader.

We can write the left-hand side of (8.7) as

P(c = c)E(f0(a)f1(a + r)f2(a + 2r)(f − f)(a + 3r)|c = c) .

c∈C

- Applying Lemma 2.2, we conclude that with probability ≫ η, the variable c attains a value c for which we have the lower bound


|E(f0(a)f1(a + r)f2(a + 2r)(f − f)(a + 3r)|c = c)| ≫ η. (8.8)

We now use a local version of the standard “generalised von Neumann theorem” argument (based on several applications of the Cauchy-Schwarz inequality) to obtain some local correlation of f −fc with a quadratic phase. Proposition 8.2. Let the notation and hypotheses be as above. For each (a,c) in the essential range of (a,c), there exists a natural number ka,c with

1 ka,c < η−C3, (8.9) a set S˜a,c ⊂ Z/pZ with S˜a,c ⊃ Sc and

|S˜a,c| |Sc| + η−C2, (8.10)

and a locally quadratic function γn,a,c : B(S˜a,c,exp(−η−11C4)ρc) → R/Z for each n ∈ Z/pZ, such that

P(a = a,c = c)

Re

a,c∈Z/pZ

× E((f − fc)(a + 6n + 6ka,cm)e(−γn,a,c(m))|a = a,c = c) ηC2/10, (8.11)

where, after conditioning to the event a = a,c = c, the random variables n and m are drawn regularly and independently from the Bohr sets B(Sc,exp(−η−2C4)ρ) and B(S˜a,c,exp(−η−12C4)ρc) respectively.

Proof. Suppose for now that c obeys (8.8). From Deﬁnition 6.1, once we condition to the event c = c, the random variables a,r are independent and regularly drawn from B(Sc,ρc/2) and B(Sc,exp(−η−C4)ρc) respectively; from (6.4) we have the bounds

|Sc| 8η−3C2 and ρc exp(−η−2C5). (8.12) Also, the function f is now the deterministic function

fc(a) := Fc(Ξc(a))

on the Bohr set B(Sc,ρc), and f0,f1,f2 become deterministic functions f0,c, f1,c and f2,c taking values in [−2,2]. Thus we have

|E(f0,c(a)f1,c(a + r)f2,c(a + 2r)f3,c(a + 3r)|c = c)| ≫ η where f3,c := f − fc.

We now do a linear change of variable with conveniently chosen numerical coeﬃcients that will facilitate a certain use of the Cauchy-Schwarz

inequality to eliminate the bounded functions f0,c,f1,c,f2,c, leaving only the function f3,c. Continuing to condition on the event that c = c, let n1,n2 and n3 be drawn regularly and independently from the Bohr sets B(Sc,exp(−η−2C4)ρc), B(Sc,exp(−η−3C4)ρc), and B(Sc,exp(−η−4C4)ρc) respectively, independently of the previous random variables. We can use Lemma 4.4 (and (8.12)) to compare a with a − 3n2 − 12n3, and conclude that

|E(f0,c(a − 3n2 − 12n3)f1,c(a + r − 3n2 − 12n3)f2,c(a + 2r − 3n2 − 12n3)× × f3,c(a + 3r − 3n2 − 12n3)|c = c)| ≫ η.

By another application of Lemma 4.4, we may compare r with r + 2n1 + 3n2 + 6n3, and conclude that

|E(f0,c(a − 3n2 − 12n3)f1,c(a + r + 2n1 − 6n3)f2,c(a + 2r + 4n1 + 3n2)×

× f3,c(a + 3r + 6(n1 + n2 + n3))|c = c)| ≫ η. Finally, we use Lemma 4.4 to replace a by a − 3r, so that |E(f0,c(a − 3r − 3n2 − 12n3)f1,c(a − 2r + 2n1 − 6n3)×

× f2,c(a − r + 4n1 + 3n2)f3,c(a + 6(n1 + n2 + n3))|c = c)| ≫ η.

The purpose of this odd-seeming change of variables is that each of the functions f0,c,f1,c,f2,c now has an argument that involves only two of the three random variables n1,n2,n3, whilst the argument of the key function f3,c depends on n1,n2,n3 only through their sum n1 + n2 + n3.

One can achieve a similar eﬀect for the other three choices f0,f1,f2 for key function by suitable adjustment to the constants above; we leave the details to the interested reader.

By Lemma 2.2, we see that with probability ≫ η (conditioning on c = c), the random variable a attains a value a such that

|E(f0,c(a − 3r − 3n2 − 12n3)f1,c(a − 2r + 2n1 − 6n3)× × f2,c(a − r + 4n1 + 3n2)f3,c(a + 6(n1 + n2 + n3))|a = a,c = c)| ≫ η. (8.13)

Let a be such that (8.13) holds. We can then ﬁnd an r ∈ Z/pZ (depending on a,c) such that

|E(f0,c(a − 3r − 3n2 − 12n3)f1,c(a − 2r + 2n1 − 6n3)× × f2,c(a − r + 4n1 + 3n2)f3,c(a + 6(n1 + n2 + n3))|a = a,c = c)| ≫ η.

We now suppress the additive structure on the ﬁrst three arguments by rewriting the above bound as

|E(f0,c,a(n2,n3)f1,c,a(n1,n3)f2,c,a(n1,n2)f3,c(a+6(n1+n2+n3))|c = c)| ≫ η

where f0,c,a,f1,c,a,f2,c,a : Z/pZ × Z/pZ → [−2,2] are bounded functions whose exact form

- f0,c,a(n2,n3) := f0,c(a − 3r − 3n2 − 12n3)
- f1,c,a(n1,n3) := f1,c(a − 2r + 2n1 − 6n3)
- f2,c,a(n1,n2) := f2,c(a − r + 4n1 + 3n2)


will not be relevant in the arguments that follow.

We can eliminate the factor f0,c,a using Lemma 2.1 to conclude that |E(f1,c,a(n1,n3)f1,c,a(n′1,n3)f2,c,a(n1,n2)f2,c,a(n′1,n2)

f3,c(a + 6(n1 + n2 + n3))f3,c(a + 6(n′1 + n2 + n3))|a = a,c = c)| ≫ η2

where n′1 is an independent copy of n1 (and also independent of n2,n3) on the event a = a,c = c. We can similarly apply Lemma 2.1 to eliminate the

f1,c,a(n1,n3)f1,c,a(n′1,n3) variables to conclude that

|E(f2,c,a(n1,n2)f2,c,a(n′1,n2)f2,c,a(n1,n′2)f2,c,a(n′1,n′2) f3,c(a + 6(n1 + n2 + n3))f3,c(a + 6(n′1 + n2 + n3)) f3,c(a + 6(n1 + n′2 + n3))f3,c(a + 6(n′1 + n′2 + n3))|a = a,c = c)| ≫ η4

and ﬁnally apply Lemma 2.1 to eliminate the f2,c,a terms and arrive at |E(f3,c(a + 6(n1 + n2 + n3))f3,c(a + 6(n′1 + n2 + n3))

f3,c(a + 6(n1 + n′2 + n3))f3,c(a + 6(n′1 + n′2 + n3)) f3,c(a + 6(n1 + n2 + n′3))f3,c(a + 6(n′1 + n2 + n′3)) f3,c(a + 6(n1 + n′2 + n′3))f3,c(a + 6(n′1 + n′2 + n′3))|a = a,c = c)| ≫ η8,

where n′2,n′3 are independent copies of n2,n3 respectively on a = a,c = c, with n1,n2,n3,n′1,n′2,n′3 all independent relative to a = a,c = c.

We now apply Theorem 8.1, replacing η by a small multiple of η8, and choosing ρi := exp(−η−(i+2)C4)ρ for i = 0,... ,10, and using the bounds

- (8.12), (3.21) to justify the hypothesis (8.3). We conclude that for c obeying (8.8) and a obeying (8.13), we can ﬁnd a natural number ka,c obeying (8.9), a set S˜a,c with Sc ⊂ S˜a,c ⊂ Z/pZ obeying (8.10), a locally quadratic function


φa,c : B(S˜a,c,exp(−η−11C4)ρ) → R/Z, and a function βa,c : Z/pZ → Z/pZ such that

P(n = n|a = a,c = c)

n∈Z/pZ

|E(f3(a + 6n + 6km)e(−φa,c(m) − βa,c(n)m)|a = a,c = c)| ≫ ηC2/20

if n,m are drawn independently and regularly from B(Sc,exp(−η−2C4)ρc) and B(Sa,c,exp(η−12C4)ρc) respectively on the event a = a,c = c. Taking expectations in a (and choosing Sa,c = Sc, φa,c = 0 and βa,c = 0 if (8.8) or

(8.13) is not satisﬁed), we conclude that

P(n = n,a = a,c = c)

n,a,c∈Z/pZ

|E(f3(a + 6n + 6km)e(−φa,c(m) − βa,c(n)m)|a = a,c = c)| ηC2/10.

In particular, if we set γn,a,c(m) := φa,c(m)+βa,c(n)m+θn,a,c for a suitable phase θn,a,c ∈ R/Z, then γn,a,c is locally quadratic on B(S˜a,c,exp(−η−11C4)ρ) and

P(n = n,a = a,c = c)

Re

n,a,c∈Z/pZ

E(f3(a + 6n + 6km)e(−γn,a,c(m))|a = a,c = c)| ηC2/10, giving the claim.

Let n,m,ka,c,S˜a,c,γn,a,c be as in the above proposition. The conclusion (8.11) of Proposition 8.2 may be rewritten more compactly as

ReE((f − f)(a + 6n + 6ka,cm)e(−γn,a,c(m))) ηC2/10. (8.14)

We now introduce the modiﬁed random function f′ : Z/pZ → [−2,2] by the formula

l − a − 6n 6ka,c

f′(l) := f(l) + ηC2/2 cos 2πγn,a,c

, (8.15)

![image 189](<2017-green-new-bounds-szemer-edi_images/imageFile189.png>)

where we extend γn,a,c arbitrarily outside of B(Sc′,exp(−η−11C4)ρc). Note from (8.9) and (3.21) that we can divide by 6ka,c in Z/pZ without diﬃculty.

We claim that the function f′ is a little closer to f than f is.

- Lemma 8.3. We have E|(f − f′)(a + 6n + 6ka,cm)|2 Energy(v) − ηC2.


Proof. From (8.15) we have

f′(a + 6n + 6ka,cm) = f(a + 6n + 6ka,cm) + ηC2/2 cos(2πγn,a,c(m)), and so

|(f − f′)(a + 6n + 6ka,cm)|2

= |(f − f)(a + 6n + 6ka,cm)|2 − 2ηC2/2E(f − f)(a + 6n + 6ka,cm)cos(2πγn,a,c(m))

+ O(ηC2). (8.16)

On the other hand, for any (a,c) in the essential range of (a,c), we may use Lemma 4.4 to compare n with n + ka,cm, and conclude that

E(|(f − f)(a + 6n+6ka,cm)|2|a = a,c = c)

= E(|(f − f)(a + 6n)|2|a = a,c = c) + O(η2C3)

(say), and hence on taking expectations in a E(|(f − f)(a + 6n+6ka,cm)|2|c = c)

= E(|(f − f)(a + 6n)|2|c = c) + O(η2C3). Applying Lemma 4.4 again to compare a with a + 6n, we conclude that

E(|(f − f)(a + 6n + 6ka,cm)|2|c = c) = E(|(f − f)(a)|2|c = c) + O(η2C3). and hence on taking averages in c

E(|(f − f)(a + 6n + 6ka,cm)|2|c = c) = Energy(v) + O(η2C3). (8.17) Taking expectations in (8.16) and using (8.15), (8.17), we obtain the claim.

There is a very minor technical issue that f′ does not quite take values in [−1,1], which is what is needed in the deﬁnition of an approximant. However, this is easily ﬁxed by truncation, or more precisely by introducing the random function f′′ : Z/pZ → [−1,1] deﬁned by

f′′(l) := min(max(f′(l),−1),1). (8.18)

Since f(l) already lies in [−1,1], we see that f′′(l) is at least as close to f(l) as f′(l) is, thus we have the pointwise bound

|(f − f′′)(l)| |(f − f′)(l)| for any l ∈ Z/pZ. From the above lemma, we thus have

E|(f − f′′)(a + 6n + 6ka,cm)|2 Energy(v) − ηC2. (8.19) We can now construct the new structured approximant

v′ = C′,c′,(n′c′ + B(Sc′′,ρ′c′))c′∈C′,(G′c′)c′∈C′,(Fc′′)c′∈C′,(Ξ′c′)c′∈C′ as follows. We write the dilated torus Gc as Gc = dim(i=1 Gc) R/λi,cZ.

- (i) We set C′ := (Z/pZ) × (Z/pZ) × C and c′ := (n,a,c).
- (ii) If c′ = (n,a,c) is in C′, we set n′c′ := a + 6n Sc′′ := (6ka,c)−1 · S˜a,c ρ′c′ := exp(−η−12C4)ρc

G′c′ :=

dim(Gc)

i=1

(R/100λi,cZ) × (R/Z)

- (iii) If c′ = (n,a,c) is in C′, we deﬁne Fc′′ : G′c′ → [−1,1] to be the function


Fc′′(x,y) := min max Fc

1 100 · x + ηC2/2 cos(2πy),−1 ,1

![image 190](<2017-green-new-bounds-szemer-edi_images/imageFile190.png>)

for x ∈ dim(i=1 Gc)(R/100λi,cZ) and y ∈ R/Z, where x  → 1001 · x is the obvious contraction map from dim(i=1 Gc)(R/100λi,cZ) to

![image 191](<2017-green-new-bounds-szemer-edi_images/imageFile191.png>)

dim(Gc) i=1 (R/λi,cZ).

- (iv) If c′ = (n,a,c) is in C′, we deﬁne Ξ′c′ : n′c′ + B(Sc′′,ρ′c′) → G′c′ by the formula


Ξ′c′(l) := 100 · Ξc(l),γn,a,c

l − a − 6n 6ka,c

![image 192](<2017-green-new-bounds-szemer-edi_images/imageFile192.png>)

for l ∈ n′c′ + B(Sc′′,ρ′c′) (which implies in particular that l−6ak−6n

∈ B(S˜a,c,exp(−η−12C4)ρc)), where x  → 100 · x is the obvious dilation map from dim(i=1 Gc)(R/λi,cZ) to dim(i=1 Gc)(R/100λi,cZ) (the inverse of the map x  → 1001 · x from part (iii)).

![image 193](<2017-green-new-bounds-szemer-edi_images/imageFile193.png>)

a,c

![image 194](<2017-green-new-bounds-szemer-edi_images/imageFile194.png>)

Since Fc is 1-Lipschitz, it is easy to see (thanks to the contraction by 1001 ) that Fc′′ is also 1-Lipschitz; similarly, as Ξc and γn,a,c are locally quadratic on nc + B(Sc,ρc) and B(S˜a,c,exp(η−11C4)ρc) respectively, we see that Ξ′c′ is also locally quadratic on n′c′ + B(Sc′′,ρ′c′). From (8.15), (8.18), Deﬁnition 6.1, and the above constructions we see that

![image 195](<2017-green-new-bounds-szemer-edi_images/imageFile195.png>)

f′′ = fv′ and hence by (8.19)

E|(f − fv′)(a + 6n + 6ka,cm)|2 Energy(v) − ηC2.

From Deﬁnition 6.1 and the above constructions, we also see that av′ has the same distribution as a+6n+6ka,cm (after conditioning to any positive probability event of the form (n,a,c) = (n,a,c)), which gives the required energy decrement (6.15).

The bound (6.10) follows from (8.10), while from construction we clearly

have dim(G′c′) = dim(Gc) + 1, which gives (6.11). Since we have ρ′c′ := exp(−η−12C4)ρc, the bound (6.12) is clear; also, from (6.4) we have

vol(G′c′) = 100dim(G′c′) vol(Gc) exp(O(η−2C2)vol(Gc)

which gives (6.13). It remains to establish (6.14). By the deﬁnition of Err1 (just before (6.1)) and the triangle inequality, it suﬃces to show that

|Ef(av′) − Ef(a)| ηC3.

But as mentioned previously, av′ has the same distribution as a+6n+6ka,cm, and by using Lemma 4.4 as in the proof of Lemma 8.3 we have

Ef(a + 6n + 6ka,cm) = Ef(a) + O(η2C3)

giving the claim. This completes the proof of Theorem 6.6, assuming the local inverse Gowers norm theorem (Theorem 8.1).

9. Local inverse U3 theorem

We now turn to the proof of Theorem 8.1, which is the last component needed in the proof of Theorem 1.1. Let us begin by recalling the setup of this theorem. We let S be a subset of Z/pZ, take a parameter η satisfying

- 0 < η < 12, and deﬁne the quantity K by (8.1), thus 1


![image 196](<2017-green-new-bounds-szemer-edi_images/imageFile196.png>)

,|S| K. (9.1) We suppose that

![image 197](<2017-green-new-bounds-szemer-edi_images/imageFile197.png>)

η

0 < ρ10 < ··· < ρ0 < 1/2 are scales obeying the separation condition (8.2) and the largeness condition

- (8.3), and suppose that f : Z/pZ → C is a 1-bounded function obeying
- (8.4). Our task is to locate a natural number k with k < exp(KO(C1)), a set S′ with S ⊂ S′ ⊂ Z/pZ obeying (8.5), a locally quadratic phase φ : B(S′,ρ9) → R/Z, and a function β : Z/pZ → Z/pZ obeying (8.6). We will initially work at the scale ρ0, but retreat to smaller scales as the argument progresses (mainly in order to ensure that the error terms in Lemma 4.4 are negligible), until we are working at the ﬁnal scales ρ9 and ρ10. Let us comment once more that the intermediate scales ρ3,... ,ρ8 play no role in the actual statement of Theorem 8.1.


In this section, all sums will be over Z/pZ unless otherwise stated.

- 9.1. First step: associate a frequency ξ(n2) to each derivative of f. We now begin the (lengthy) proof of this theorem, which broadly follows the same inverse U3 strategy in previous literature [12, 21], but localised to a Bohr set, the key aim being to reduce the dependence of constants on the rank or radius of this Bohr set as much as possible.


The ﬁrst step is to use the local inverse U2 theorem (Theorem 4.12) to

![image 198](<2017-green-new-bounds-szemer-edi_images/imageFile198.png>)

associate a frequency ξ(n2) ∈ Z/pZ to many “derivatives” x  → f(x+n2)f(x) of f.

- Theorem 9.2. Let the notation and hypotheses be as in Theorem 8.1. Then there exists a set Ω ⊂ B(S,2ρ2) obeying the largeness condition


P(h2 − h′2 ∈ Ω) η/4 (9.2)

when h2,h′2 are drawn independently and regularly from B(S,ρ2), and a function ξ : Z/pZ → Z/pZ such that

η 8

P(n0 = n0) Ef(n0 + n1 + n2)f(n0 + n1)ep(−ξ(n2)n1) 2

![image 199](<2017-green-new-bounds-szemer-edi_images/imageFile199.png>)

1Ω(n2)

![image 200](<2017-green-new-bounds-szemer-edi_images/imageFile200.png>)

n0∈Z/pZ

(9.3) for all n2 ∈ Z/pZ, and n0,n1 are drawn independently and regularly from B(S,ρ0),B(S,ρ1) respectively.

Proof. For each n2 ∈ Z/pZ, let fn2 : Z/pZ → C denote the 1-bounded function

![image 201](<2017-green-new-bounds-szemer-edi_images/imageFile201.png>)

fn2(n) := f(n + n2)f(n).

Then we may rewrite the left-hand side of (8.4) as

(h0 + h2 + h′1)×

![image 202](<2017-green-new-bounds-szemer-edi_images/imageFile202.png>)

Efh2−h′

(h0 + h2 + h1)fh2−h′

2

2

(h′0 + h2 + h1)fh2−h′

(h′0 + h2 + h′1) .

![image 203](<2017-green-new-bounds-szemer-edi_images/imageFile203.png>)

× fh2−h′

2

2

By Lemma 4.4 and (8.2), the random variables h0,h′0 diﬀer in total variation from h0 + h2,h′0 + h2 respectively by at most η/4 (say). We conclude that

(h′0 + h′1)| η/2. By the triangle inequality, the left-hand side is at most

(h′0 + h1)fh2−h′

2,0(h0 + h′1)fh2−h′

![image 204](<2017-green-new-bounds-szemer-edi_images/imageFile204.png>)

![image 205](<2017-green-new-bounds-szemer-edi_images/imageFile205.png>)

|Efh2−h′

(h0 + h1)fh2−h′

2

2

2

h

P(h2 − h′2 = h)|Efh(h0 + h1)fh(h0 + h′1)fh(h′0 + h1)fh(h′0 + h′1)|.

![image 206](<2017-green-new-bounds-szemer-edi_images/imageFile206.png>)

![image 207](<2017-green-new-bounds-szemer-edi_images/imageFile207.png>)

The inner expectation is bounded by 1. Applying Lemma 2.2 (with a = h2 − h′2), we conclude that there is a set Ω ⊂ Z/pZ obeying (9.2) such that |Efn2(h0 + h1)fn2(h0 + h′1)fn2(h′0 + h1)fn2(h′0 + h′1)| η/4

![image 208](<2017-green-new-bounds-szemer-edi_images/imageFile208.png>)

![image 209](<2017-green-new-bounds-szemer-edi_images/imageFile209.png>)

for all n2 ∈ Ω. Applying Theorem 4.12, we see that for each n2 ∈ Ω, there exists ξ(n2) ∈ Z/pZ such that

P(n = n0)|Efn2(n0 + n1)ep(−ξ(n2)n1)|2 η/8.

n0∈Z/pZ

For n2  ∈ Ω, we set ξ(n2) arbitrarily (e.g. to zero). The claim follows.

- 9.3. Second step: ξ is approximately linear 1% of the time. The next step, following Gowers [12], is to obtain some approximate linearity control on the function ξ : Z/pZ → Z/pZ. Deﬁne an additive quadruple to be a quadruplet  a = (a(1),a(2),a(3),a(4)) ∈ (Z/pZ)4 such that


a(1) + a(2) = a(3) + a(4), (9.4) and let Q ⊂ (Z/pZ)4 denote the space of all additive quadruples. We call an additive quadruple (a(1),a(2),a(3),a(4)) ∈ Q bad if

KC1 ρ1

, (9.5)

ξ(a(1)) + ξ(a(2)) − ξ(a(3)) − ξ(a(4)) S >

![image 210](<2017-green-new-bounds-szemer-edi_images/imageFile210.png>)

where the word norm S was deﬁned in Deﬁnition 4.5. Let BQ ⊂ Q denote the space of all bad additive quadruples.

Theorem 9.4. Let the notation and hypotheses be as in Theorem 8.1, and let Ω and ξ : Z/pZ → Z/pZ be as in Theorem 9.2. If h2,h′2,k2,k′2 are drawn independently and regularly from B(S,ρ2), then with probability ≫ ηO(1), one has

(h2 − h′2,k2 − k′2,k2 − h′2,h2 − k′2) ∈ Ω4 ∩ (Q\BQ). (9.6)

Proof. Let n0,n1 be drawn independently and regularly from the Bohr sets

- B(S,ρ0), B(S,ρ1) respectively. From (9.3) we have


n0

![image 211](<2017-green-new-bounds-szemer-edi_images/imageFile211.png>)

P(n0 = n0) Ef(n0 + n1 + n2)f(n0 + n1)ep(−ξ(n2)n1) ≫ η

for any n2 ∈ Ω. Using (9.2), we conclude that

P(n0 = n0,h2 − h′2 = n2) Ef(n0 + n1 + n2)f(n0 + n1)×

![image 212](<2017-green-new-bounds-szemer-edi_images/imageFile212.png>)

n0 n2∈Ω

× ep(−ξ(n2)n1) ≫ η2,

where h2,h′2 are drawn independently and regularly from B(S,ρ2), and are independent of n0,n1. By the pigeonhole principle, one can thus ﬁnd n0 ∈ Z/pZ such that

P(h2 − h′2 = n2) Ef(n0 + n1 + n2)f(n0 + n1)ep(−ξ(n2)n1) ≫ η2.

![image 213](<2017-green-new-bounds-szemer-edi_images/imageFile213.png>)

n2∈Ω

We can rewrite the left-hand side as EFn0(h2 − h′2)f(n0 + n1 + h2 − h′2)f(n0 + n1)ep(−ξ(h2 − h′2)n1)

![image 214](<2017-green-new-bounds-szemer-edi_images/imageFile214.png>)

for some 1-bounded function Fn0 : Z/pZ → C depending on n0. Using Lemma 4.4 to compare n1 with n1 + h′2, we conclude that

|EFn0(h2 − h′2)f(n0 + n1 + h2)f(n0 + n1 + h′2)ep(−ξ(h2 − h′2)(n1 + h′2))|

![image 215](<2017-green-new-bounds-szemer-edi_images/imageFile215.png>)

≫ η2. We rearrange the left-hand side as

n1

P(n1 = n1)Ef(n0 + n1 + h2)f(n0 + n1 + h′2)Gn0,n1(h2,h′2)

![image 216](<2017-green-new-bounds-szemer-edi_images/imageFile216.png>)

where Gn0,n1 : Z/pZ × Z/pZ → C is the 1-bounded function

Gn0,n1(h2,h′2) := Fn0(h2 − h′2)ep(−ξ(h2 − h′2)(n1 + h′2)). (9.7) By H¨older’s inequality, we conclude that

n1

P(n1 = n1)|Ef(n0 + n1 + h2)f(n0 + n1 + h′2)Gn0,n1(h2,h′2)|4 ≫ ηO(1)

![image 217](<2017-green-new-bounds-szemer-edi_images/imageFile217.png>)

From this point onward we cease to keep careful track of powers of η. On the other hand, by using two applications of Lemma 2.1 to eliminate the 1-bounded functions f, we have

|Ef(n0 + n1 + h2)f(n0 + n1 + h′2)Gn0,n1(h2,h′2)|4

![image 218](<2017-green-new-bounds-szemer-edi_images/imageFile218.png>)

EGn0,n1(h2,h′2)Gn0,n1(h2,k′2)Gn0,n1(k2,h′2)Gn0,n1(k2,k′2) where (k2,k′2) is an independent copy of (h2,h′2). We thus have

![image 219](<2017-green-new-bounds-szemer-edi_images/imageFile219.png>)

![image 220](<2017-green-new-bounds-szemer-edi_images/imageFile220.png>)

EGn0,n1(h2,h′2)Gn0,n1(h2,k′2)Gn0,n1(k2,h′2)Gn0,n1(k2,k′2) ≫ ηO(1)

![image 221](<2017-green-new-bounds-szemer-edi_images/imageFile221.png>)

![image 222](<2017-green-new-bounds-szemer-edi_images/imageFile222.png>)

which by the triangle inequality and (9.7) gives

2∈ΩP(h2 = h2;k2 = k2;h′2 = h′2;k′2 = k2′ )

1h2−h′

2,k2−k′

2,k2−h′

2,h2−k′

- h2,k2,h′


2,k′

2

|Eep(−(ξ(h2 − h′2) + ξ(k2 − k2′ ) − ξ(k2 − h′2) − ξ(h2 − k2′ ))n1)| ≫ ηO(1).

By Lemma 2.2, we conclude that with probability ≫ ηO(1), the tuple (h2,k2, h′2,k′2) attains a value (h2,k2,h′2,k2′ ) for which

h2 − h′2,k2 − k2′ ,h2 − k2′ ,k2 − h′2 ∈ Ω

and |Eep(−(ξ(h2−h′2)+ξ(k2−k2′ )−ξ(k2−h′2)−ξ(h2−k2′ ))n1)| ≫ ηO(1) ≫ K−O(1)

(9.8)

thanks to (9.1). Since (h2 − h′2,k2 − k2′ ,h2 − k2′ ,k2 − h′2) is an additive quadruple, the claim now follows from Lemma 4.7, (8.2), and (9.1).

We localise this claim slightly, though for notational reasons we will not move from ρ2 immediately to ρ3 and beyond, but instead ﬁrst work in some intermediate scales between ρ2 and ρ3. For any natural number j, deﬁne

ρ2,j := exp(−C1jK)ρ2, thus

ρ2 = ρ2,0 > ρ2,1 > ··· > ρ2,j ρ3 if (say) j KC12.

It will be necessary to break the symmetry between the four components of an additive quadruple, by restricting the second component to a tiny Bohr set, the third component to a larger Bohr set, and the ﬁrst and fourth components to an even larger Bohr set. More precisely, given an additive

- quadruple  a0 = (a(1),0,a(2),0,a(3),0,a(4),0) ∈ Q, a subset S′ ⊂ Z/pZ, and radii 0 < r2 r3 r4 1/2, we say that a random additive quadruple a = (a(1),a(2),a(3),a(4)) ∈ Q is centred at  a0 with frequencies S′ and scales r2,r3,r4 if a(2),a(3),a(4) are drawn independently and regularly from a(2),0+ B(S′,r2), a(2),0+B(S′,r2), and a(2),0+B(S′,r2) respectively. Note that this property also describes the distribution of a(1), since we have the constraint


a(1) = a(3) + a(4) − a(2). In practice, r4 will be much larger than r2,r3, so (by Lemma 4.4) a(1) will be approximately regularly drawn from a(1),0 + B(S′,r4), but will be highly coupled to the other three components of the quadruple (in particular, it will stay close to a(4)). We thus see that for i = 1,2,3,4, each a(i) is either exactly or approximately drawn regularly from a(i),0 +B(S′,rli), where li ∈ {0,1,2} is the quantity deﬁned by the formulae

l1 := 0; l2 := 2; l3 := 1; l4 := 0. (9.9)

Corollary 9.5. Let the notation and hypotheses be as in Theorem 8.1, and let Ω and ξ be as in Theorem 9.2. Then there exists a random additive quadruple a ∈ Q centred at some quadruple  a0 ∈ Q with frequencies S and scales ρ2,2,ρ2,1,ρ2,0, such that a ∈ Ω4 ∩ (Q\BQ) with probability ≫ ηO(1).

Proof. Let h2,k2,h′2,k′2,n2,1,n2,2 be drawn independently and regularly from B(S,ρ2,0), B(S,ρ2,0), B(S,ρ2,0), B(S,ρ2,0), B(S,ρ2,1) and B(S,ρ2,2) respectively. From Theorem 9.4, we have

(h2 − h′2,k2 − k′2,h2 − k′2,k2 − h′2) ∈ Ω4 ∩ (Q\BQ) with probability ≫ ηO(1). Using Lemma 4.4, we may replace k′

2 by k′

2−n2,2, and similarly replace h2 by h2 + n2,1 − n2,2, to conclude that

(h2 − h′2 + n2,1,k2 − k′2 + n2,2,h2 − k′2 + n2,1,k2 − h′2) ∈ Ω4 ∩ (Q\BQ) with probability ≫ ηO(1). By the pigeonhole principle, we may thus ﬁnd k2,k2′ ,h2 ∈ Z/pZ such that

(h2 − h′2 + n2,1,k2 − k2′ + n2,2,h2 − k2′ + n2,1,k2 − h′2) ∈ Ω4 ∩ (Q\BQ) with probability ≫ ηO(1). The left-hand side is an additive quadruple centred at (h2,k2 − k2′ ,h2 − k2′ ,k2) with frequencies S and scales ρ2,2,ρ2,1,ρ2,0, and the claim follows.

9.6. Third step: ξ is approximately linear 99% of the time on a rough set. The next general step in the standard inverse U3 argument is to upgrade this weak additive structure, which is of a “1 percent” nature, to a more robust “99 percent” additive structure . There are two basic ways to proceed here. The ﬁrst way is to invoke the Balog-Szemere´di-Gowers theorem [1, 12], followed by standard sum set estimates including Freiman’s theorem (see e.g. [48, Chapter 2]). It is likely that this approach will eventually work here, but these results need to be localised eﬃciently to Bohr sets, and also to allow for the fact that ξ(a(1))+ξ(a(2))−ξ(a(3))−ξ(a(4)) no longer vanishes, but instead has controlled word norm. This would require reworking of large portions of the standard additive combinatorics literature. We have thus elected instead to follow the second approach, also due to Gowers [13], in which a certain probabilistic argument is used to “purify” a

- 1 percent additive map to a 99 percent additive map, albeit on a set which has no particular structure itself. To deal with this set we will use a more recent innovation, namely a variant4 of the arithmetic regularity lemma [19], [25] to make the subsets of Z/pZ on which one has good control of ξ suitably “pseudorandom” in the sense of Gowers.


![image 223](<2017-green-new-bounds-szemer-edi_images/imageFile223.png>)

- 4The actual arithmetic regularity lemma, which creates arithmetic regularity on almost all regions of space, has quantitative bounds of tower-exponential type, which are far too poor for our application; however we will only need to create a single neighbourhood in which arithmetic regularity exists, and this can be done with much more eﬃcient quantitative bounds.


We turn to the details. We ﬁrst locate a reasonably large quadruple of sets A(1),A(2),A(3),A(4) on which ξ is “almost a Freiman homomorphism” in the sense that most quadruples falling inside A(1) × A(2) × A(3) × A(4) are somewhat good. We call an additive quadruple (a(1),a(2),a(3),a(4)) ∈ Q very bad if

1 ρ3

, (9.10) and let VBQ ⊂ BQ denote the space of all very bad additive quadruples.

ξ(a(1)) + ξ(a(2)) − ξ(a(3)) − ξ(a(4)) S >

![image 224](<2017-green-new-bounds-szemer-edi_images/imageFile224.png>)

Theorem 9.7. Let the notation and hypotheses be as in Theorem 8.1, and let Ω and ξ be as in Theorem 9.2. Let  a be the random additive quadruple from Corollary 9.5. Then there exist sets A(1),A(2),A(3),A(4) ⊂ Ω such that

EW( a) ≫ ηC1+O(1), (9.11) where W : Q → R is the weight function

W( a) := 1A(1)×A(2)×A(3)×A(4)( a) 1 − η−C1/1001VBQ( a) . (9.12)

The idea here is that W is a weight function that strongly penalises very bad quadruples, and so Theorem 9.7 is asserting that “most” of the quadruples in A(1) × A(2) × A(3) × A(4) are not very bad.

Proof. We will construct the sets A(i) by the probabilistic method, adapting an argument from [13] in which the A(i) are created by applying a number of random linear “ﬁlters” to the graph of ξ to eliminate most of the additive quadruples that are not (almost) preserved by ξ. We turn to the details. Let m be the integer

m :=

log ηC1 3log 100

![image 225](<2017-green-new-bounds-szemer-edi_images/imageFile225.png>)

. (9.13)

We then select jointly independent random variables hj ∈ Z/pZ and λj ∈ Z/pZ for each for j = 1,... ,m, by selecting each hj regularly from B(S,ρ2), and selecting λj uniformly at random from Z/pZ; we also choose these random variables to be independent of a. For j = 1,... ,m, we then let Ξj : Z/pZ → R/Z be the random map

λjn p

Ξj(n) := ξ(n)hj +

(9.14) and then deﬁne the random sets

![image 226](<2017-green-new-bounds-szemer-edi_images/imageFile226.png>)

m

A(i) :=

A(i),j

j=1

for i = 1,2,3,4, where

A(1),j = A(2),j = A(3),j := n ∈ Ω : Ξj(n) R/Z

1 200

![image 227](<2017-green-new-bounds-szemer-edi_images/imageFile227.png>)

and

1 10

A(4),j := n ∈ Ω : Ξj(n) R/Z

. We will show that

![image 228](<2017-green-new-bounds-szemer-edi_images/imageFile228.png>)

E1A(1)×A(2)×A(3)×A(4)( a) ≫ ηO(1)100−3m (9.15) and

E1A(1)×A(2)×A(3)×A(4)( a)1BQ( a) ≪ 2−m × 100−3m (9.16) which will give the claim thanks to (9.13) and (9.12), if C1 is large enough.

We ﬁrst show (9.15). By Corollary 9.5 and linearity of expectation, it suﬃces to show that

P(a(i) ∈ A(i) for i = 1,2,3,4) ≫ 100−3m (9.17)

whenever (a(1),a(2),a(3),a(4)) lies in Ω4 ∩ (Q\BQ). Actually, we will only show the weaker assertion that (9.17) holds for all but at most O(mO(1)p2) of the available additive quadruples (a(1),a(2),a(3),a(4)); this still suﬃces, since by (4.3), (9.1) each exceptional additive quadruple is attained with probability O( 1

), and the additional factor of p will dominate all the losses in m,K,ρ3 thanks to (8.3), (9.13).

![image 229](<2017-green-new-bounds-szemer-edi_images/imageFile229.png>)

ρO3 (K)p3

Fix an additive quadruple  a = (a(1),a(2),a(3),a(4)) in Ω4 ∩ (Q\BQ). The left-hand side of (9.17) factors as

m

P(a(i) ∈ A(i) for i = 1,2,3,4) (9.18)

j=1

so it will suﬃce to show that for each j = 1,... ,m, one has

P(a(i) ∈ A(i),j for i = 1,2,3,4) 100−3 − O

1 m

![image 230](<2017-green-new-bounds-szemer-edi_images/imageFile230.png>)

for all but O(mO(1)p2) quadruples (a(1),a(2),a(3),a(4)) ∈ Q\BQ. Note however that from (9.14) we have

Ξj(a(1)) + Ξj(a(2))−Ξj(a(3)) − Ξj(a(4))

= ξ(a(1)) + ξ(a(2)) − ξ(a(3)) − ξ(a(4)) hj

and hence by the hypothesis (a(1),a(2),a(3),a(4)) ∈ Q\BQ and the range of hj we have

Ξj(a(1)) + Ξj(a(2)) − Ξj(a(3)) − Ξj(a(4)) p R/Z

![image 231](<2017-green-new-bounds-szemer-edi_images/imageFile231.png>)

1 100

![image 232](<2017-green-new-bounds-szemer-edi_images/imageFile232.png>)

(say). In particular, we see from the triangle inequality that the claim a(4) ∈ A(4),j is implied by the claims a(i) ∈ A(i),j for i = 1,2,3. Thus it suﬃces to show that

1 m

P(a(i) ∈ A(i),j for i = 1,2,3) 100−3 − O

![image 233](<2017-green-new-bounds-szemer-edi_images/imageFile233.png>)

for all but O(mO(1)p2) triples (a(1),a(2),a(3)) ∈ (Z/pZ)3, noting that a(4) is determined by a(1),a(2),a(3). We can write the left-hand side as

P

(ξ(a(1)),ξ(a(2)),ξ(a(3)))hj + (a(1),a(2),a(3))λj p ∈ [−1/200,1/200]3 ,

![image 234](<2017-green-new-bounds-szemer-edi_images/imageFile234.png>)

where we view the interval [−1/200,1/200] as a subset of R/Z. Thus it will suﬃce to show the equidistribution property

- inf

x∈(R/Z)3

P

(a(1),a(2),a(3))λj p ∈ x + [−1/200,1/200]3 100−3 − O

![image 235](<2017-green-new-bounds-szemer-edi_images/imageFile235.png>)

1 m

![image 236](<2017-green-new-bounds-szemer-edi_images/imageFile236.png>)

.

Let ψ : (R/Z)3 → [0,1] be a Lipschitz cutoﬀ supported on [−1/20,1/20]3 that equals one on [−1/200+1/m,1/200−1/m]3 and has Lipschitz constant O(m). Then we may lower bound the left-hand side by

inf

x∈(R/Z)3

Eλ∈Z/pZψ

(a(1),a(2),a(3))λ

![image 237](<2017-green-new-bounds-szemer-edi_images/imageFile237.png>)

p − x . (9.19) By standard Fourier expansion (see e.g. [24, Lemma A.9]), we may write

ψ(y) =

k∈Z3:k=O(mO(1))

cke(k · y) + O

1 m

![image 238](<2017-green-new-bounds-szemer-edi_images/imageFile238.png>)

for all y ∈ (R/Z)3 and some bounded Fourier coeﬃcients ck = O(1); integrating in x, we see in particular that c0 = 10−3 + O m 1 . We may thus write (9.19) as

![image 239](<2017-green-new-bounds-szemer-edi_images/imageFile239.png>)

10−3 + O

1 m

![image 240](<2017-green-new-bounds-szemer-edi_images/imageFile240.png>)

+ O

 

k∈Z3\{0}:k=O(mO(1))

Eλ∈Z/pZep(k · (a(1),a(2),a(3))λ)

 

which gives the desired claim as long as there are no relations of the form

k · (a(1),a(2),a(3)) = 0 for some non-zero k ∈ Z3 with k = O(mO(1)). But it is easy to see that the number of (a(1),a(2),a(3)) with such a relation is O(mO(1)p2), thus conclud-

- ing the proof of (9.15). Now we show (9.16). By linearity of expectation as before, it suﬃces to


show that

P(a(i) ∈ A(i) for i = 1,2,3,4) ≪ 2−m × 100−3m

for all but O(mO(1)p2) of the quadruples (a(1),a(2),a(3),a(4)) in VBQ. Using the factorisation (9.18), it suﬃces to show that for each j = 1,... ,m, one has

1 m

P(a(i) ∈ A(i),j for i = 1,2,3,4) 2−1 × 100−3 + O

![image 241](<2017-green-new-bounds-szemer-edi_images/imageFile241.png>)

for all but O(mO(1)p2) of the quadruples (a(1),a(2),a(3),a(4)) in VBQ.

The left-hand side may be written as

(ξ(a(1)),... ,ξ(a(4)))hj p

+ aλj ∈ [−1/200,1/200]3 × [−1/10,1/10] , which we bound above by

P

![image 242](<2017-green-new-bounds-szemer-edi_images/imageFile242.png>)

P (ξ(a(1)),ξ(a(2)),ξ(a(3)))hj + (a(1),a(2),a(3))λj ∈[−1/200,1/200]3, σhj p R/Z

1 8

,

![image 243](<2017-green-new-bounds-szemer-edi_images/imageFile243.png>)

![image 244](<2017-green-new-bounds-szemer-edi_images/imageFile244.png>)

where σ := ξ(a(1)) + ξ(a(2)) − ξ(a(3)) − ξ(a(4)). By arguing as in the proof of (9.15), we see that after deleting O(mO(1)p2) exceptional tuples, one has

1 m

P((a(1),a(2),a(3))λj ∈ x + [−1/200,1/200]3) 100−3 + O

,

sup

![image 245](<2017-green-new-bounds-szemer-edi_images/imageFile245.png>)

x∈(R/Z)3

so by Fubini’s theorem and the independence of hj and λj it will suﬃce to show that

P

σhj p R/Z

![image 246](<2017-green-new-bounds-szemer-edi_images/imageFile246.png>)

1/8 2−1 + O

1 m

![image 247](<2017-green-new-bounds-szemer-edi_images/imageFile247.png>)

.

However, by Lemma 4.6 and the hypothesis (a(1),a(2),a(3),a(4)) ∈ VBQ we may ﬁnd h ∈ Z/pZ such that

σh p R/Z

> K−O(1) h S⊥ρ3.

![image 248](<2017-green-new-bounds-szemer-edi_images/imageFile248.png>)

In particular, h is non-zero. By repeatedly doubling h until ηhp

exceeds 1/4, we may also assume that

![image 249](<2017-green-new-bounds-szemer-edi_images/imageFile249.png>)

R/Z

1/2

ηh p R/Z

> 1/4

![image 250](<2017-green-new-bounds-szemer-edi_images/imageFile250.png>)

and thus

h S⊥ ≪ KO(1)ρ3. From Lemma 4.4 we conclude that

P

η(hj + h) p R/Z

![image 251](<2017-green-new-bounds-szemer-edi_images/imageFile251.png>)

1/8 = P

ηhj p R/Z

![image 252](<2017-green-new-bounds-szemer-edi_images/imageFile252.png>)

1/8 + O

1 m

![image 253](<2017-green-new-bounds-szemer-edi_images/imageFile253.png>)

.

But from the triangle inequality we see that the events η(hjp+h)

![image 254](<2017-green-new-bounds-szemer-edi_images/imageFile254.png>)

ηhj p R/Z

![image 255](<2017-green-new-bounds-szemer-edi_images/imageFile255.png>)

1/8 are disjoint. The claim follows.

R/Z

1/8,

9.8. Fourth step: the rough set is pseudorandom in a Bohr set. The sets A(i) provided by Theorem 9.7 are currently rather arbitrary. In particular we have no control on the pseudorandomness of these sets (as measured by local Gowers U2 norms) in the Bohr sets we are working with. However, it is possible to use an “energy decrement argument” to pass to smaller5 Bohr sets in which the sets A(i) do enjoy good pseudorandomness properties, basically by converting any large Fourier coeﬃcient of any of the A(i) in a Bohr set into a reﬁnement of the Bohr sets (which add the frequency of the large Fourier coeﬃcient to the frequency set S) on which the indicator function 1A(i) has smaller variance. Furthermore, it is possible to shrink the Bohr sets in this fashion without destroying the conclusion (9.11) of Theorem 9.7.

Here is a precise statement.

Theorem 9.9. Let the notation and hypotheses be as in Theorem 8.1, and let Ω and ξ be as in Theorem 9.2. Let A(1),A(2),A(3),A(4),W be as in Theorem 9.7. Then there exists a natural number j, j η−103C1, an additive

- quadruple  a1 = (a(1),1,a(2),1,a(3),1,a(4),1) ∈ Q, and a set S1, S ⊂ S1 ⊂ Z/pZ with |S1| |S| + j, with the following properties:


- (i) (Few very bad quadruples) We have EW( a) ≫ ηC1+O(1), (9.20)

where a is a random additive quadruple centred at  a1 with frequencies S1 and scales ρ2,j+2, ρ2,j+1, and ρ2,j.

- (ii) (Local Fourier pseudorandomness) For each i = 1,2,3,4, we have


|Efi(a(i)+h0+h1)fi(a(i)+h0+h′1)fi(a(i)+h′0+h1)fi(a(i)+h′0+h′1)| η100C1 where fi : Z/pZ → [−1,1] denotes the balanced function

fi(a(i)) := 1A(i)(a(i)) − αi, (9.21) αi denotes the mean

αi := E1A(i)(a(i)), (9.22)

and where a(i) and h0,h′0,h1,h′1 are drawn independently and regularly from the Bohr sets a(i),1 + B(S1,ρ2,j+li) and B(S1,ρ2,j+10), B(S1,ρ2,j+10), B(S1,ρ2,j+11), B(S1,ρ2,j+11) respectively, with the quantity li given by (9.9).

![image 256](<2017-green-new-bounds-szemer-edi_images/imageFile256.png>)

- 5This is somewhat analogous to the variants of the Szemere´di regularity lemma [43] in which one locates a single regular pair inside an arbitrary large random graph. In contrast to the full regularity lemma which strives to ensure that almost all pairs are regular, the “one regular pair” versions of the lemma enjoy signiﬁcantly better quantitative bounds. In our current application, such good quantitative bounds are essential, so we cannot appeal to analogues of the regularity lemma such as the arithmetic regularity lemma of the ﬁrst author [19].


Proof. We will formulate the “energy decrement” argument here as a “score maximisation” argument. Deﬁne a 4-neighbourhood to be a tuple

N = ( a1,j,S1)

where  a1 ∈ Q is an additive quadruple, j is a natural number between 0 and η−103C1, and S1 is a subset of Z/pZ containing S with |S1| |S|+j; we refer to j as the depth of the 4-neighbourhood N. Given such a neighbourhood, we deﬁne the score Score(N) of the 4-neighbourhood to be the quantity

Score(N) := EW( a) − η2C1

4

Ei(N) − η103C1j (9.23)

i=1

where a = (a(1),a(2),a(3),a(4)) is a random additive quadruple centred at  a1 with frequencies S1 and scales ρ2,j+2,ρ2,j+1,ρ2,j, and Ei is the energy-type quantity

Ei(N) := Var 1A(i)(a(i)). (9.24) If we deﬁne N0 to be the 4-neighbourhood

N0 := ( a0,0,S), then Theorem 9.7 tells us that

Score(N0) ≫ ηC1+O(1). (9.25) We choose

N := ( a1,j,S1) to be a 4-neighbourhood that comes within η103C1 (say) of maximising the adjusted score. Then we must have

Score(N) Score(N0) − η103C1 ≫ ηC1+O(1) which from (9.23) implies the bound (9.20), as well as the bound j η−103C1 − 103 (say). It will then suﬃce to show that property (ii) of the theorem holds. It remains to show (ii). Let i = 1,2,3,4, and write

 a1 = (a(1),1,a(2),1,a(3),1,a(4),1). Suppose for contradiction that |Efi(a(i)+h0+h1)fi(a(i)+h0+h′1)fi(a(i)+h′0+h1)fi(a(i)+h′0+h′1)| > η100C1

(9.26) where fi is given by (9.21), and a(i),h0,h′0,h1,h′1 are drawn independently and regularly from the Bohr sets a(i),1 +B(S1,ρ2,j+li), B(S1,ρ2,j+10), B(S1, ρ2,j+10), B(S1,ρ2,j+11), B(S1,ρ2,j+11), with li given by (9.9).

We will use (9.26) to construct a random 4-neighbourhood N of depth j + 20 obeying the estimates

EW(N) = W(N) + O(η103C1) (9.27)

and

EEi′(N) Ei′(N) − η500C11i=i′ + O(η103C1) (9.28) for i′ = 1,2,3,4. If we have the estimates (9.27), (9.28), we conclude from (9.23) and linearity of expectation that

EScore(N) > Score(N) + η600C1, contradicting the near-maximality of Score(N).

It remains to construct N obeying (9.27), (9.28). We begin by noting that for each a(i) ∈ Z/pZ, the Gowers uniformity-type quantity

Efi(a(i) + h0 + h1)fi(a(i) + h0 + h′1)fi(a(i) + h′0 + h1)fi(a(i) + h′0 + h′1) can be factored as

P(h0 = h0,h′0 = h′0) Efi(a(i) + h0 + h1)fi(a(i) + h′0 + h1) 2

h0,h′

0

and thus takes values between 0 and 1. By (9.26) and Lemma 2.2, we may thus ﬁnd a set E ⊂ Z/pZ with

P(a(i) ∈ E) ≫ η100C1 such that

Efi(a(i)+h0+h1)fi(a(i)+h0+h′1)fi(a(i)+h′0+h1)fi(a(i)+h′0+h′1) ≫ η100C1 for all a(i) ∈ E. Applying Theorem 4.12, we may thus ﬁnd, for each a(i) ∈ E, a frequency ξ(a(i)) ∈ Z/pZ such that

P(n0 = n0)E Efi(a(i) + n0 + n1)ep(−ξ(a(i))n1) 2 ≫ η100C1,

n0

where n0,n1 are drawn independently and regularly from B(S1,ρ2,j∗+10) and B(S1,ρ2,j∗+11) respectively, independently of the a(i).

If we deﬁne ξ(a(i)) arbitrarily for a(i)  ∈ E (e.g. setting ξ(a(i)) = 0), we thus have

P(n0 = n0,a(i) = a(i))E E(fi(a(i) + n0 + n1)ep(−ξ(a(i))n1)) 2

n0,a(i)

≫ η200C1.

In particular, there exists a 1-bounded function g : Z/pZ × Z/pZ → C such that

Eg(n0,a(i))fi(a(i) + n0 + n1)ep(−ξ(a(i))n1) ≫ η200C1. (9.29)

We now construct the random 4-neighbourhood N as follows. We ﬁrst construct a random additive quadruple k = (k1,k2,k3,k4) centred at the origin (0,0,0,0) with frequency set S1 and scales ρ2,j+10+l2−li, ρ2,j+10+l3−li, ρ2,j+10+l4−li, and independent of all previous random variables. We then set N := ( a + k,j + 20,S1 ∪ {ξ(a(i))}).

It is easy to verify that N is a (random) 4-neighbourhood.

We now verify (9.27). The left-hand side of (9.27) can be expanded as EW( a + k + h) where, once a and k are chosen, the random additive quadruple h = (h1,h2,

- h3,h4) is selected to be centred at (0,0,0,0) with frequencies S1 ∪ {ξ(a(i))} and scales ρ2,j+22,ρ2,j+21,ρ2,j+20.


From two applications of Lemma 4.4 (and the fact that W = O(η−C1/100)), we have

EW( a + k + h) = EW( a + k) + O(η103C1) = EW( a) + O(η103C1) (say). The claim (9.27) now follows from (9.23).

Now we verify (9.28). By (9.24), we have

Ei′(N) =

2

P( a =  a, k = k)E 1A(i′)(a(i′) + ki′ + hi′) − αi′, a, k

 a, k

where  a = (a(1),... ,a(4)), k = (k1,... ,k4), and αi′, a, k is the quantity

αi′, a, k := E1A(i′)(a(i′) + ki′ + hi′). (9.30) By Pythagoras’ theorem, we thus have

Ei′(N) =

P( a =  a, k = k)E 1A(i′)(a(i′) + ki′ + hi′) − αi′

 a, k

2

−|αi′, a, k−αi′|2

where αi′ is deﬁned in (9.22). We shall shortly establish the bound

|αi′, a, k − αi′|2 ≫ η400C11i′=i. (9.31) Assuming this bound, we conclude that

(a(i′) + ki′ + hi′) − αi′|2

P( a =  a, k = k)E|1A

EEi′(N)

(i′)

 a, k

= E|1A(i′)(a(i′) + ki′ + hi′) − αi′|2 − η500C11i′=i.

By applying Lemma 4.4 twice as in the proof of (9.27) to replace a(i′) + ki′ +hi′ by a(i′) for i′ = 2,3,4 (and by using Lemma 4.4 six times for i′ = 1, after writing a(1) in terms of a(2),a(3),a(4), and similarly for k(1) and h(1)) we thus have

EEi′(N) E|1A(i′)(a(i′)) − αi′|2 − η500C11i′=i + O(η103C1).

This will give (9.28) as soon as we establish (9.31). This is trivial for i′ = i, so suppose that i = i. By (9.30) and (9.21), it suﬃces to show that

P( a =  a, k = k) Efi(a(i) + ki + hi) 2 ≫ η400C1. (9.32)

 a, k

To prove this, we introduce random variables n0,n1 drawn independently and regularly from B(S1,ρ2,j+10) and B(S1,ρ2,j+11) independently of all previous variables. From (9.29) we have

Efi(a(i) + n0 + n1)g(n0,a(i))ep(−ξ(a(i))n1) ≫ η200C1

for some 1-bounded function g. After using Lemma 4.4 to compare n1 and n1 + hi for each ﬁxed choice of n0 and a(i), we conclude that

Efi(a(i) + n0 + n1 + hi)g(n0,a(i))ep(−ξ(a(i))(n1 + hi)) ≫ η200C1. But we have

ξ(a(i))hi p R/Z

hi S1∪{ξ(a(i))} ≪ ρj+li+20 and hence by (2.2)

![image 257](<2017-green-new-bounds-szemer-edi_images/imageFile257.png>)

ep(−ξ(a(i))(n1 + hi)) = ep(−ξ(a(i))n1) + O(η103C1). We conclude that

|E(fi(a(i) + n0 + n1 + hi)g(n0,a(i))ep(−ξ(a(i))n1)| ≫ η200C1.

For ﬁxed choices of a(i),h(i),n1, we see from Lemma 4.4 that ki and n0 +n1 diﬀer in total variation by O(η103C1). Thus we have

|E(fi(a(i) + ki + hi)g(ki − n1,a(i))ep(−ξ(a(i))n1)| ≫ η200C1,

and the claim now follows after using Lemma 2.1 to eliminate the g(ki − n1,a(i))ep(−ξ(a(i))n1) factor.

A useful consequence of the bounds in Theorem 9.9(ii) is the following weak mixing bound, which roughly speaking asserts that the convolution of 1A(i) with a bounded function is essentially constant.

Lemma 9.10. Let the notation and hypotheses be as above, and let Ω and ξ be as in Theorem 9.2. Let A(1),... ,A(4) be as in Theorem 9.7, and let j,a(1),∗,... ,a(4),∗,S1,f1,... ,f4 be as in Theorem 9.9. Then for any i = 1,2,3,4, any li < m 10, and any 1-bounded function g : Z/pZ → C, one has

P(n = n)|Efi(n − k)g(k)|2 ≪ η50C1 (9.33)

n

where n,k are drawn independently and regularly from a(i),∗+B(S1,ρ2,j) and B(S1,ρ2,j+m) respectively. Dually, for any 1-bounded function G : Z/pZ → C, one has

P(k = k)|Efi(n − k)G(n)| ≪ η25C1. (9.34)

k

Proof. In preparation for invoking Theorem 9.9(ii), we introduce random variables h0,h1,h′1 drawn independently and regularly from B(S1,ρ2,j∗+10), B(S1,ρ2,j∗+11), and B(S1,ρ2,j∗+11) respectively, independently of n and k.

Using Lemma 4.4 to compare n,k with n + h0, k − h1 respectively, we may transform (9.33) to the estimate

P(n = n,h0 = h0)|E(fi(n + h0 − k − h1)g(k − h1))|2 ≪ η50C1.

n,h0

By the triangle inequality in L2, it thus suﬃces to show that

P(n = n,h0 = h0)|E(fi(n + h0 − k − h1)g(k − h1))|2 ≪ η50C1 (9.35)

n,h0

for all k ∈ B(S1,ρ2,j∗+m). Fix k. We may expand out the left-hand side of (9.35) as

Efi(n + h0 − h1 − k)g(k − h1)fi(n + h0 − h′1 − k)g(k − h′1).

Using Lemma 4.4 to compare n with n + h0 − h1 − h′1 − k, we can thus rewrite (9.35) as

|Efi(n + h0 + h′1)g(k − h1)fi(n + h0 + h1)g(k − h′1)| ≪ η50C1,

which by the triangle inequality and the 1-boundedness of g would follow from

P(n = n,h1 = h1,h′1 = h1)|Efi(n + h0 + h′1)fi(n + h0 + h1)| ≪ η50C1,

n,h1,h′

1

which by Cauchy-Schwarz will follow in turn from

P(n = n,h1 = h1,h′1 = h1)|Efi(n+h0+h′1)fi(n+h0+h1)|2 ≪ η100C1.

n,h1,h′

1

But this follows from Theorem 9.9(ii) (relabeling n as a(i)).

Finally, we show (9.34). By subtracting EG(n) from G (and dividing by 2 to recover 1-boundedness), we may assume that EG(n) = 0. It then suﬃces to show that

k

P(k = k)g(k)E1A(i)(n − k)G(n) ≪ η25C1.

for any 1-bounded function g. But the left-hand side may be rearranged as

n

P(n = n)G(n)(E1A(i)(n − k)g(k) − αiEg(k)) ≪ η25C1,

and the claim follows from (9.33) and the Cauchy-Schwarz inequality.

9.11. Fifth step: a frequency function ξ′ that is approximately linear 99% of the time on a Bohr neighbourhood. The next step is to obtain additive structure on almost all of a Bohr neighbourhood, rather than just the subsets A(i).

Theorem 9.12. Let the notation and hypotheses be as in Theorem 8.1, and let ξ be as in Theorem 9.2. Let A(1),... ,A(4) be as in Theorem 9.7, and let j,a(1),1,a(2),1,a(3),1,a(4),1,S1,α1,... ,α4 be as in Theorem 9.9. Let a1 ∈ Z/pZ be the quantity

a1 := a(1),1 + a(2),1 = a(3),1 + a(4),1,

and let a and a(2) be drawn regularly and independently from a1+B(S1,ρ2,j) and a(2),1 + B(S1,ρ2,j+2) respectively. Then there is a function ξ′ : Z/pZ → Z/pZ, such that with probability at least 1−O(ηC1/200), the random variable a attains a value a for which we have the estimates

E1A(2)(a(2))1A(1)(a − a(2)) = α1α2 + O(η20C1), (9.36) and

1

P a − a(2) ∈ A(1);a(2) ∈ A(2); ξ′(a) − ξ(a − a(2)) − ξ(a(2)) S >

![image 258](<2017-green-new-bounds-szemer-edi_images/imageFile258.png>)

ρ3 ≪ ηC1/200α1α2.

(9.37)

Proof. Let a be drawn regularly from a1+B(S1,ρ2,j), and let (a(1),a(2),a(3), a(4)) be a random additive quadruple centred at (a(1),1,a(2),1,a(3),1,a(4),1) with frequencies S1 and scales ρ2,j+2,ρ2,j+1,ρ2,j, independently of a. From the deﬁnition of an additive quadruple, we have a(1) = a(3) + a(4) − a(2). From Theorem 9.9(i) we thus have

EW(a(3) + a(4) − a(2),a(2),a(3),a(4)) ≫ ηC1+O(1). (9.38) From Lemma 4.4 we see that once we condition a(2) and a(3) to be ﬁxed, a(4) and a−a(3) diﬀer in total variation by O(η100C1). Thus we may replace a(4) by a − a(3) in (9.38) to conclude that

EW(a − a(2),a(2),a(3),a − a(3)) ≫ ηC1+O(1). If we then deﬁne

σ := E1A(1)(a − a(2))1A(2)(a(2))1A(3)(a(3))1A(4)(a − a(3)) then from (9.12) we see that

σ ≫ ηC1+O(1) (9.39) and

E1A(1)(a − a(2))1A(2)(a(2))1A(3)(a(3))1A(4)(a − a(3)) 1VBQ(a − a(2),a(2),a(3),a − a(3)) ≪ η−C1/100σ.

(9.40)

We can express σ in the form

σ = Eg12(a)g34(a) (9.41) where g12,g34 : Z/p/Z → R are the functions

g12(a) := E1A(1)(a − a(2))1A(2)(a(2)) (9.42)

and

g34(a) := E1A(3)(a(3))1A(4)(a − a(3)). From Lemma 9.10, we have

2

≪ η50C1

P(n = n) Ef1(n − k)1A(2)(a(2),1 + k)

n

if n,k are drawn independently and regularly from a(i),1 + B(S1,ρ2,j) and B(S1,ρ2,j+m) respectively. Note that the pair (n,k) has the same distribution as (a − a(2),1,a(2) − a(2),1), thus

2

≪ η50C1.

P(a = a) Ef1(a − a(2))1A(2)(a(2))

a

From (9.21), (9.22), (9.42) we have

Ef1(a − a(2))1A(2)(a(2)) = g12(a) − α1α2 and thus

P(a = a)|g12(a) − α1α2|2 ≪ η50C1. (9.43) Similarly we have

a

P(a = a)|g34(a) − α3α4|2 ≪ η50C1. (9.44) From Cauchy-Schwarz and the triangle inequality we conclude that

a

P(a = a)|g12(a)g34(a) − α1α2α3α4| ≪ η25C1, and hence by (9.41) and the triangle inequality

a

σ = α1α2α3α4 + O(η25C1). (9.45) In particular, from (9.39) one has

α1α2α3α4 ≫ ηC1+O(1). (9.46) From (9.45), (9.46) and (9.40) we have

Eh(a) ≪ ηC1/100α1α2α3α4 where

h(a) := EW(a − a(2),a(2),a(3),a − a(3)). (9.47) By Markov’s inequality, we conclude that we have

h(a) ≪ ηC1/200α1α2α3α4 (9.48) with probability 1 − O(ηC1/200). Similarly, from (9.43), (9.44) and Chebyshev’s inequality we also have

g12(a) = α1α2 + O(η20C1) (9.49) and

g34(a) = α3α4 + O(η20C1) (9.50) with probability 1 − O(ηC1/200).

Now let a be a value of a be such that (9.48), (9.49), (9.50) hold. From (9.50) we have in particular that

E1A(3)(a(3))1A(4)(a − a(3)) ≫ α3α4;

comparing this with (9.48) and (9.47), we see that we may ﬁnd a(3)(a) ∈ A(3) (depending only on a) with a − a(3)(a) ∈ A(4) such that

E1A(1)(a − a(2))1A(2)(a(2))1VBQ(a − a(2),a(2),a(3)(a),a − a(3)(a)) ≪ ηC1/200α1α2.

If we then set ξ′(a) := ξ(a(3)(a))+ξ(a−a(3)(a)) (and deﬁne ξ′(a) arbitrarily when (9.48), (9.49), or (9.50) fail), then the claims (9.36), (9.37) follow from (9.49) and the deﬁnition (9.10) of VBQ.

The function ξ′ has better additive structure than ξ, in that it respects almost all additive quadruples in a Bohr set, rather than almost all additive quadruples in a rough set. More precisely, we have the following.

Proposition 9.13. Let the notation and hypotheses be as in Theorem 9.12. Suppose that a,a′,h are selected independently and regularly from a1 + B(S1,ρ2,j), a1 +B(S1,ρ2,j), and B(S1,ρ2,j+3) respectively. Then with probability 1 − O(ηC1/200) we have

4 ρ3

ξ′(a) − ξ′(a + h) − ξ′(a′) + ξ′(a′ + h) S

. (9.51)

![image 259](<2017-green-new-bounds-szemer-edi_images/imageFile259.png>)

Proof. Let a(2) be drawn regularly from a(2),1+B(S1,ρ2,j+2), independently of a,a′,h. For each a,a′,h ∈ Z/pZ, let Ia,a′,h denote the random indicator variable

Ia,a′,h := 1A(2)(a(2))1A(2)(a(2) + h)1A(1)(a − a(2))1A(1)(a′ − a(2)).

Suppose that we can show that with probability 1 − O(ηC1/200), the triple (a,a′,h) attains a value (a,a′,h) for which one has the estimates

EIa,a′,h 0.9α21α22 (9.52) EIa,a′,h1 ξ′(a)−ξ(a−a(2))−ξ(a(2)) S>1/ρ3 0.1α21α22 (9.53)

EIa,a′,h1 ξ′(a′)−ξ(a′−a(2))−ξ(a(2)) S>1/ρ3 0.1α21α22 (9.54) EIa,a′,h1 ξ′(a+h)−ξ(a−a(2))−ξ(a(2)+h) S>1/ρ3 0.1α21α22 (9.55)

EIa,a′,h1 ξ′(a′+h)−ξ(a′−a(2))−ξ(a(2)+h) S>1/ρ3 0.1α21α22. (9.56)

Assuming these estimates, we conclude from the union bound that with probability 1 − O(ηC1/200), the random variable (a,a′,h) attains a value (a,a′,h) for which there exists at least one element a(2) of Z/pZ obeying the

constraints

a(2),a(2) + h ∈ A(2) a − a(2),a′ − a(2) ∈ A(1)

1

ξ′(a) − ξ(a − a(2)) − ξ(a(2)) S

![image 260](<2017-green-new-bounds-szemer-edi_images/imageFile260.png>)

ρ3 ξ′(a′) − ξ(a′ − a(2)) − ξ(a(2)) S

1

![image 261](<2017-green-new-bounds-szemer-edi_images/imageFile261.png>)

ρ3 ξ′(a + h) − ξ(a − a(2)) − ξ(a(2) + h) S

1

![image 262](<2017-green-new-bounds-szemer-edi_images/imageFile262.png>)

ρ3 ξ′(a′ + h) − ξ(a′ − a(2)) − ξ(a(2) + h) S

1

![image 263](<2017-green-new-bounds-szemer-edi_images/imageFile263.png>)

ρ3 and (9.51) then follows from the triangle inequality.

It remains to establish (9.52)-(9.56). We ﬁrst prove (9.53). By Markov’s inequality, it suﬃces to show that

EIa,a′,h1 ξ′(a)−ξ(a−a(2))−ξ(a(2)) S>1/ρ3 ≪ ηC1/200α21α22. We rewrite the left-hand side as

Eg1(a(2))g2(a(2))1A(2)(a(2))1A(1)(a − a(2))1 ξ′(a)−ξ(a−a(2))−ξ(a(2)) S>1/ρ3 where

- g1(a(2)) := E1A(1)(a′ − a(2))

and

- g2(a(2)) := E1A(2)(a(2) + h).


But from (9.37) we have

E1A(2)(a(2))1A(1)(a − a(2))1 ξ′(a)−ξ(a−a(2))−ξ(a(2)) S>1/ρ3 ≪ ηC1/200α1α2, from Lemma 4.4 one has

- g1(a(2)) = α1 + O(η10C1)

and from (9.33) one has

- g2(a(2)) = α2 + O(η10C1)


with probability 1 − O(η10C1) (say), with the trivial bound g(a(2)) = O(1) otherwise, and the claim (9.53) then follows from (9.46).

The proofs of (9.54)-(9.56) are similar to (9.53) and are omitted. It thus remains to prove (9.52). From (9.34) and Markov’s inequality, we see that with probability 1−O(ηC1/200), the random variable h attains a value h for which

E1A(2)(a(2))1A(2)(a(2) + h) 0.99α22. For any h obeying this inequality, deﬁne E(h) ⊂ Z/pZ to be the set

E(h) := A(2) ∩ (A(2) − h),

so that

P(a(2) ∈ E(h)) 0.99α22. By (9.33) and the Chebyshev inequality, we conclude that with probability 1 − O(ηC1/200), the random variable (a,h) attains a value (a,h) for which one has

P(a(2) ∈ E(h);a − a(2) ∈ A(1)) 0.98α1α22. For any (a,h) of the above form, deﬁne E′(a,h) ⊂ Z/pZ to be the set

E′(a,h) := E(h) ∩ (a − A(1)), then

P(a(2) ∈ E′(a,h)) 0.98α1α22. By one last application of (9.33) and the Chebyshev inequality, we see that with probability 1−O(ηC1/200), the random variable (a′,a,h) attains a value (a′,a,h) for which one has

P(a(2) ∈ E′(a,h);a′ − a(2) ∈ A(1)) 0.97α21α22 which gives (9.52) as required.

9.14. Sixth step: a frequency function ξ′′ that is approximately linear 100% of the time on a Bohr set. We now use a standard “majority vote” argument to upgrade the “99% linear” structure of ξ′ to a “100% linear” structure of a closely related function ξ′′ (cf. [5]). More precisely, one has

Theorem 9.15. Let the notation and hypotheses be as in Theorem 8.1. Let j,S1 be as in Theorem 9.9, and let a1, ξ′ be as in Theorem 9.12. Then there is a function ξ′′ : B(S1,ρ3) → Z/pZ such that

24 ρ3

ξ′′(n + m) − ξ′′(n) − ξ′′(m) S

(9.57)

![image 264](<2017-green-new-bounds-szemer-edi_images/imageFile264.png>)

for all n,m ∈ B(S1,ρ3/2), and such that for any n ∈ B(S1,ρ3), if a is drawn regularly from a1 + B(S1,ρ2,j), one has

ξ′(a) − ξ′(a − n) − ξ′′(n) S

8 ρ3

![image 265](<2017-green-new-bounds-szemer-edi_images/imageFile265.png>)

(9.58)

with probability 1 − O(ηC1/200).

Proof. Let a,h be drawn independently and regularly from a∗ + B(S1,ρ2,j) and B(S1,ρ2,j+3) respectively. From Proposition 9.13 and the pigeonhole principle, we may ﬁnd a′0 ∈ Z/pZ such that

4 ρ3

1 − O(ηC1/200). (9.59)

P ξ′(a) − ξ′(a + h) − ξ′(a′0) + ξ′(a′0 + h) S

![image 266](<2017-green-new-bounds-szemer-edi_images/imageFile266.png>)

Fix this a′0. Now let n by an arbitrary element of B(S1,ρ3). Then using Lemma 4.4 to compare a with a − n and h with h + n, we obtain

4 ρ3 1 − O(ηC1/200).

P ξ′(a − n) − ξ′(a + h) − ξ′(a′0) + ξ′(a′0 + h + n) S

![image 267](<2017-green-new-bounds-szemer-edi_images/imageFile267.png>)

Combining this with (9.59) and the triangle inequality, we see that

8 ρ3 1 − O(ηC1/200).

P ξ′(a) − ξ′(a − n) + ξ′(a′0 + h) − ξ′(a′0 + h + n) S

![image 268](<2017-green-new-bounds-szemer-edi_images/imageFile268.png>)

Thus, by the pigeonhole principle, we may ﬁnd hn ∈ Z/pZ such that

8 ρ3 1 − O(ηC1/200).

P ξ′(a) − ξ′(a − n) + ξ′(a′0 + hn) − ξ′(a′0 + hn + n) S

![image 269](<2017-green-new-bounds-szemer-edi_images/imageFile269.png>)

If we thus deﬁne

ξ′′(n) := ξ′(a′0 + hn + n) − ξ′(a′0 + n) then we have obtained (9.58).

Now suppose that n,m ∈ B(S1,ρ3/2). From (9.58), we see that with probability at least 1 − O(ηC1/200) we have

8 ρ3

ξ′(a) − ξ′(a − n) − ξ′′(n) S

,

![image 270](<2017-green-new-bounds-szemer-edi_images/imageFile270.png>)

8 ρ3

ξ′(a) − ξ′(a − m) − ξ′′(m) S

, and

![image 271](<2017-green-new-bounds-szemer-edi_images/imageFile271.png>)

ξ′(a) − ξ′(a − n − m) − ξ′′(n + m) S

8 ρ3

.

![image 272](<2017-green-new-bounds-szemer-edi_images/imageFile272.png>)

Using Lemma 4.4 to compare a with a − n in the second inequality, we also conclude

8 ρ3

ξ′(a − n) − ξ′(a − n − m) − ξ′′(m) S

,

![image 273](<2017-green-new-bounds-szemer-edi_images/imageFile273.png>)

with probability 1−O(ηC1/200). Thus there is a positive probability that the ﬁrst, third, and fourth estimates hold simultaneously, and the claim (9.57) follows from the triangle inequality.

The function ξ′′ is still closely related to ξ, and in particular a variant of the correlation estimate (9.3) is obeyed by ξ′′.

Proposition 9.16. Let the notation and hypotheses be as in the preceding theorem. Then there exist a0 ∈ B(S,3ρ2) and ξ0 ∈ Z/pZ such that

P(n0 = n0,n = n)|Ef(n0 + h + a0 − n)f(n0 + h)ep((ξ′′(n) − ξ0)h)|2

![image 274](<2017-green-new-bounds-szemer-edi_images/imageFile274.png>)

n0,n

≫ ηC1+O(1),

where n,n0,h are drawn independently and regularly from the Bohr sets B(S1,ρ3/4), B(S,ρ0), B(S1,ρ4) respectively.

With this proposition and the previous theorem, we may now safely forget about the original function ξ, and work now with ξ′′; the parameters a1,j will also no longer be relevant.

Proof. Let n, a, a(2) be drawn independently and regularly from B(S1,ρ3/4), a1 + B(S1,ρ2,j), and B(S1,ρ2,j+2) respectively. From (9.58) we have

1 ρ3

ξ′(a) − ξ′(a − n) − ξ′′(n) S ≪

![image 275](<2017-green-new-bounds-szemer-edi_images/imageFile275.png>)

with probability 1−O(ηC1/200). Similarly, from (9.36), (9.37), (9.46) we see that with probability 1 − O(ηC1/200), the random variable a attains a value a for which

1

P a − a(2) ∈ A(1);a(2) ∈ A(2); ξ′(a) − ξ(a − a(2))−ξ(a(2)) S

![image 276](<2017-green-new-bounds-szemer-edi_images/imageFile276.png>)

ρ3 ≫ α1α2.

Using Lemma 4.4 to compare a and a − n, we also see that with with probability 1 − O(ηC1/200), the random variable (a,n) attains a value (a,n) for which

P a − n−a(2) ∈ A(1);a(2) ∈ A(2);

1

ξ′(a − n) − ξ(a − n − a(2)) − ξ(a(2)) S

ρ3 ≫ α1α2. From the union bound and Fubini’s theorem, we conclude that with probability ≫ α1α2, we simultaneously have the statements

![image 277](<2017-green-new-bounds-szemer-edi_images/imageFile277.png>)

a − n − a(2) ∈ A(1)

a(2) ∈ A(2) ξ′(a) − ξ′(a − n) − ξ′′(n) S ≪

1

![image 278](<2017-green-new-bounds-szemer-edi_images/imageFile278.png>)

ρ3 ξ′(a − n) − ξ(a − n − a(2)) − ξ(a(2)) S

1

![image 279](<2017-green-new-bounds-szemer-edi_images/imageFile279.png>)

ρ3 and hence by the triangle inequality

1 ρ3

ξ′(a) − ξ(a − n − a(2)) − ξ(a(2)) − ξ′′(n) S ≪

.

![image 280](<2017-green-new-bounds-szemer-edi_images/imageFile280.png>)

By the pigeonhole principle, we may thus ﬁnd a,a(2) ∈ Z/pZ such that the statements

a − n − a(2) ∈ A(1) a(2) ∈ A(2)

1 ρ3

ξ′(a) − ξ(a − n − a(2)) − ξ(a(2)) − ξ′′(n) S ≪

![image 281](<2017-green-new-bounds-szemer-edi_images/imageFile281.png>)

simultaneously hold with probability ≫ α1α2, and thus with probability ≫ ηC1+O(1) thanks to (9.46). Writing a0 := a−a(2) and ξ0 := ξ(a(2))−ξ′(a), and recalling from Theorem 9.7 that A(1) ∈ S, we thus have

P a0 − n ∈ S; ξ′′(n) + ξ(a0 − n) − ξ0 S ≪ 1/ρ3 ≫ ηC1+O(1).

In particular, since n ∈ B(S1,ρ3/4) and S ⊂ B(S,2ρ2), we have a0 ∈ B(S,3ρ2).

Let n0,n1 be drawn independently and regularly from B(S,ρ0),B(S,ρ1) respectively, independently of all previous random variables. From the above estimate and (9.3), we see that with probability ≫ ηC1+O(1), the random variable n attains a value n for which the statements

a0 − n ∈ S (9.60)

ξ′′(n) + ξ(a0 − n) − ξ0 S1 ≪ 1/ρ3 (9.61)

- n0

P(n0 = n0) Ef(n0 + n1 + a0 − n)f(n0 + n1)ep(−ξ(a0 − n)n1) 2 η/8

![image 282](<2017-green-new-bounds-szemer-edi_images/imageFile282.png>)

(9.62) simultaneously hold.

Let n obey the above estimates (9.60), (9.61), (9.62). If we now draw h regularly from B(S1,ρ4), then by using Lemma 4.4 to compare n1 with

- n1 + h in (9.62), we obtain


n0

![image 283](<2017-green-new-bounds-szemer-edi_images/imageFile283.png>)

P(n0 = n0) Ef(n0 + n1 + h + a0 − n)f(n0 + n1 + h)×

× ep(−ξ(a0 − n)(n1 + h))

2

≫ η

and thus by the triangle inequality in L2

![image 284](<2017-green-new-bounds-szemer-edi_images/imageFile284.png>)

P(n0 = n0,n1 = n1) Ef(n0+n1 + h + a0 − n)f(n0 + n1 + h)×

n0,n1

2

× ep(−ξ(a0 − n)(n1 + h))

≫ η.

We may delete the deterministic phase ep(−ξ(a0 − n)n1) to obtain

![image 285](<2017-green-new-bounds-szemer-edi_images/imageFile285.png>)

P(n0 = n0,n1 = n1) Ef(n0 + n1 + h + a0 − n)f(n0 + n1 + h)×

n0,n1

2

≫ η. Since h takes values in B(S1,ρ4), we see from (9.61) that

× ep(−ξ(a0 − n)h)

ep(−ξ(a0 − n)h) = ep((ξ′′(n) − ξ0)h) + O(η100) (say), and so

![image 286](<2017-green-new-bounds-szemer-edi_images/imageFile286.png>)

P(n0 = n0,n1 = n1) Ef(n0 + n1 + h + a0 − n)f(n0 + n1 + h)×

n0,n1

2

× ep((ξ′′(n) − ξ0)h)

≫ η. Using Lemma 4.4 to compare n0 with n0 + n1, we conclude that

2

P(n0 = n0,n1 = n1) Ef(n0 + h + a0 − n)f(n0 + h)ep((ξ′′(n) − ξ0)h)

![image 287](<2017-green-new-bounds-szemer-edi_images/imageFile287.png>)

n0,n1

≫ η. Multiplying by P(n = n) and summing in n, we obtain the claim.

9.17. Seventh step: derivatives of f correlate with a locally bilinear form. We now pass to the “cohomological” phase of the argument, in which we remove the error ξ′′(n + m) − ξ′′(n) − ξ′′(m) in the linearity of ξ′′ that appears in (9.57). This improved linearity of the form (n,h)  → ξ(n)h in the n aspect will come at the expense of the h aspect, which will now merely be locally linear instead of globally linear. However, this is a worthwhile tradeoﬀ for our purposes (and in any event local linearity is more natural in this context than global linearity).

More precisely, the purpose of this subsection is to establish the following result towards the proof of Theorem 8.1.

Theorem 9.18. Let the notation and hypotheses be as in Theorem 8.1. Then there exists a set S1 with S ⊂ S1 ⊂ Z/pZ and |S1| |S|+O(η−O(C1)), a locally bilinear map

Ξ : B(S1,ρ4) × B(S1,ρ4) → R/Z, a shift a1 ∈ B(S,4ρ2), and a frequency ξ1 ∈ Z/pZ such that

P(n0 = n0,n1 = n1)×

n0,n1

ξ1m1 p

![image 288](<2017-green-new-bounds-szemer-edi_images/imageFile288.png>)

Ef(n0 + m1 + a1 − n1)f(n0 + m1)e Ξ(n1,m1) −

![image 289](<2017-green-new-bounds-szemer-edi_images/imageFile289.png>)

2

≫ ηC1+O(1) (9.63)

if n0,m1,n1 are drawn independently and regularly from B(S,ρ0), B(S1,ρ5), and B(S1,ρ6) respectively.

Once the proof of this theorem is completed, the auxiliary data ξ,ξ′,ξ′′,j, Ω,VBQ used in the previous parts of the section are no longer needed and may be discarded.

We now prove Theorem 9.18. Let j∗,S1 be as in Theorem 9.9, let a∗, ξ′ be as in Theorem 9.12, let ξ′′ : B(S1,ρ3) → Z/pZ be as in Theorem 9.15, and let a0,ξ0 be as in Proposition 9.16. We will use a “cohomological” argument to construct the required bilinear map Ξ. Namely, we deﬁne the cocycle µ : B(S1,ρ3/2) × B(S1,ρ3/2) → Z/pZ to be the quantity

µ(n,m) := ξ′′(n + m) − ξ′′(n) − ξ′′(m). (9.64) Clearly (9.57) is symmetric, and we have the cocycle equation

µ(n1,n2 + n3) + µ(n2,n3) = µ(n1,n2) + µ(n1 + n2,n3) (9.65) as well as the auxiliary equations

µ(n1,n2) = µ(n2,n1); µ(n1,0) = 0 whenever n1,n2,n3 ∈ B(S1,ρ3/4). From (9.57) we also have the estimate µ(n,m) S

24 ρ3

(9.66)

![image 290](<2017-green-new-bounds-szemer-edi_images/imageFile290.png>)

- for all n,m ∈ B(S1,ρ3/4). To construct the bilinear map Ξ, we will show that a certain projection


of µ is a “coboundary” is a certain sense. Let φ : ZS → Z/pZ be the homomorphism

φ((ns)s∈S) :=

nss.

s∈S

- From (9.66), we see that for each n,m ∈ B(S1,ρ3/4) we have a representation of the form


µ(n,m) = φ(˜µ(n,m)) (9.67) for some lift µ˜(n,m) ∈ ZS of size

|µ˜(n,m)| 24/ρ3. (9.68) This lift µ˜(n,m) is only deﬁned up to an element of the kernel ker(φ) := {p ∈ ZS : φ(p) = 0} of φ; to eliminate this ambiguity we will apply a projection. Since S contains a non-zero element, φ : ZS → Z/pZ is a surjective homomorphism, and in particular, ker(φ) is a sublattice of ZS of index p. Applying Lemma 4.8, we may ﬁnd generators v1,... ,v|S| of ker(φ) and real numbers N1,... ,N|S| > 0 with

|S|

Ni = O(K)O(K)p (9.69)

i=1

such that BRS(0,O(K)−3K/2t) ∩ ker(φ) ⊂ {n1v1 + ... + n|S|v|S| : |ni| tNi}

⊂ BRS(0,t) ∩ ker(φ) (9.70) for all t > 0.

By relabeling, we may take the Ni to be non-increasing. Let d, 0 d |S| be such that

ρ3 exp(KC1)

N1 ... Nd >

Nd+1 ... N|S|. (9.71)

![image 291](<2017-green-new-bounds-szemer-edi_images/imageFile291.png>)

From (9.69), (8.3) we see that d cannot equal |S|. Let V be the d-dimensional subspace of RS spanned by v1,... ,vd, let V ⊥ be the orthogonal complement of V in RS, and let π : RS → V ⊥ be the orthogonal projection.

We claim that π(˜µ(n,m)) is now uniquely determined by µ(n,m) for n,m ∈ B(S1,ρ3/4). Indeed, if µ˜(n,m) and µ˜′(n,m) both obeyed (9.67), (9.68), then their diﬀerence (call it w) would be of magnitude O(1/ρ3) and lies in the kernel of φ. By (9.70) with t = exp(−KC1)ρ3, we conclude that w lies in V , and hence π(˜µ(n,m)) and π(˜µ′(n,m)) agree.

A variant of the above argument shows that π ◦ µ˜ also continues to obey the cocycle equation. Lemma 9.19 (Projected lift is a cocycle). One has

π(˜µ(n1,n2 + n3)) + π(˜µ(n2,n3)) = π(˜µ(n1,n2)) + π(˜µ(n1 + n2,n3)) and additionally

π(˜µ(n1,n2)) = π(˜µ(n2,n1)); π(˜µ(n1,0)) = 0 for all n1,n2,n3 ∈ B(S1,ρ3/4).

Proof. By (9.68), the quantity w := µ˜(n1,n2 + n3) + µ˜(n2,n3) − µ˜(n1,n2) − µ˜(n1 +n2,n3) has magnitude O(1/ρ3); by (9.67), (9.65), w lies in the kernel of φ. Repeating the previous arguments, we conclude that w ∈ V . Applying the homomorphism π, we obtain the ﬁrst claim. The second claim is proven similarly.

We can in fact make π ◦ µ˜ a coboundary, after shrinking the domain somewhat. Proposition 9.20 (Projected lift is a coboundary). There exists a map F : B(S1,2exp(−KC12)ρ3) → V ⊥ with

KO(C1) ρ3

(9.72)

F(n) ≪

![image 292](<2017-green-new-bounds-szemer-edi_images/imageFile292.png>)

for all n ∈ B(S1,2exp(−KC12)ρ3), such that

π(˜µ(n1,n2)) = F(n1 + n2) − F(n1) − F(n2) for all n1,n2 ∈ B(S1,exp(−KC12)ρ3).

Proof. As a ﬁrst attempt at constructing F, we introduce the average F1(n) := Eπ(˜µ(n,n3))

for n ∈ B(S1,ρ3/4), where n3 is drawn regularly from B(S1,ρ3/4). From (9.68) we have

24 ρ3

|F1(n)|

![image 293](<2017-green-new-bounds-szemer-edi_images/imageFile293.png>)

for all n ∈ B(S1,ρ3/4). Also, since |S1| ≪ KO(C1), if we replace n3 by n3 in Lemma 9.19 and take expectations using Lemma 4.4, we conclude that

KO(C1) n2 S⊥

1

F1(n1) + F1(n2) = π(˜µ(n1,n2)) + F1(n1 + n2) + O

![image 294](<2017-green-new-bounds-szemer-edi_images/imageFile294.png>)

ρ23 for all n1,n2 ∈ B(S1,ρ3/8).

If we now introduce the modiﬁed cocycle

σ1(n1,n2) := π(˜µ(n1,n2)) + F1(n1 + n2) − F1(n1) − F1(n2) for n1,n2 ∈ B(S1,ρ3/8), then we have the cocycle equation

σ1(n1,n2 + n3) + σ1(n2,n3) = σ1(n1,n2) + σ1(n1 + n2,n3), (9.73) the auxiliary equations

σ1(n1,n2) = σ1(n2,n1); σ1(n1,0) = 0 and the bound

KO(C1) n2 S⊥

1

(9.74) for n1,n2 ∈ B(S1,ρ3/16).

σ1(n1,n2) ≪

![image 295](<2017-green-new-bounds-szemer-edi_images/imageFile295.png>)

ρ23

We now make σ1 a coboundary by using a basis for B(S1,ρ3/16). Set d := |S1| KO(C1). By Corollary 4.9, we can ﬁnd a1,... ,ad of Z/pZ and real numbers N1,... ,Nd > 0 such that

Ni−1 (9.75)

ai S⊥

1

for all i = 1,... ,d, and such that for any a ∈ Z/pZ, there exists a representation

a = m1a1 + ··· + mdad (9.76) with m1,... ,md integers of size

mi ≪ exp(O(KO(C1)))Ni a S⊥

(9.77)

1

for i = 1,... ,d, with at most one such representation obeying the bounds |mi| < Ni/2 for i = 1,... ,d.

By relabeling we may assume that Ni 32d′/ρ3 for i = 1,... ,d′ and Ni < 32d′/ρ3 for i = d′ + 1,... ,d for some 0 d′ d. By (9.75) we have ai ∈ B(S1,ρ3/32d′) for all i = 1,... ,d′. In particular, from (9.73) we see that for any n ∈ B(S1,ρ3/32) and 1 i,j d′, we have

σ1(n1,ai + aj) + σ1(ai,aj) = σ1(n1,ai) + σ1(n1 + ai,aj)

and hence by swapping i and j and subtracting σ1(n1 + aj,ai) − σ1(n1,ai) = σ1(n1 + ai,aj) − σ1(n1,aj). Let P ⊂ Zd′ denote the collection of tuples (m1,... ,md′) ∈ Zd′ with |mi|

ρ3

2Ni for i = 1,... ,d′, and for each m ∈ P and i = 1,... ,d, deﬁne the quantity fi(m) := σ1(φ(m),ai) where φ : Zd′ → Z/pZ is the homomorphism

![image 296](<2017-green-new-bounds-szemer-edi_images/imageFile296.png>)

d′

φ(m1,... ,md′) :=

mkak.

k=1

Then from (9.75) we have φ(P) ⊂ B(S1,ρ3/32). The above identity then says that the “1-form” (f1,... ,fd′) is “closed” or “curl-free” in the sense that

fi(m + ej) − fi(m) = fj(m + ei) − fj(m) (9.78) whenever i,j = 1,... ,d′ and m,m + ei,m + ej ∈ P, where e1,... ,ed′ is the standard basis for P. This implies that there exists a function H : P → V ⊥ such that F(0) = 0 and fi(m) = H(m + ei) − H(m) whenever i = 1,... ,d and m,m + ei ∈ P. Indeed, one can deﬁne H to be an “antiderivative” of the (f1,... ,fd′) by setting

L−1

H(m) :=

fil(ml)

l=0

whenever 0 = m0,... ,mL = m is a path in P with ml+1 = ml + eil for l = 0,... ,L − 1; a “homotopy” argument using (9.78) shows that the right-

hand side does not depend on the choice of path. From (9.74), (9.75) we have

KO(C1)

fi(m) ≪

![image 297](<2017-green-new-bounds-szemer-edi_images/imageFile297.png>)

Niρ23 for m ∈ P and i = 1,... ,d′, which on “integrating” (and recalling that d′ d ≪ KO(C1)) implies that

KO(C1) ρ3 for all m ∈ P.

H(m) ≪

![image 298](<2017-green-new-bounds-szemer-edi_images/imageFile298.png>)

Since σ1(0,ei) = 0, we have fi(0) = 0 and hence H(ei) = 0 for all i = 1,... ,d′. Thus we have

σ1(φ(m),φ(ei)) = H(m + ei) − H(m) − H(ei)

whenever m,m + ei ∈ P. An induction (on the magnitude of a vector m′) using (9.73) then shows that

σ1(φ(m),φ(m′)) = H(m + m′) − H(m) − H(m′)

- whenever m,m′,m + m′ ∈ P. Now, if n ∈ B(S1,2exp(−KC12)ρ), then by (9.76), (9.77) we see that n = φ(m) for some m ∈ P. If we then deﬁne


F2 : B(S1,2exp(−KC12)ρ) → V ⊥ by setting F2(n) := H(m), we conclude that

KO(C1)

F2(n) ≪

![image 299](<2017-green-new-bounds-szemer-edi_images/imageFile299.png>)

ρ3 and

σ1(n,n′) = F2(n + n′) − F2(n) − F2(n′)

- for all n,n′ ∈ B(S1,exp(−KC12)ρ). Setting F := F2 − F1, we obtain the claim.


Let F be as in Proposition 9.20. We use F to construct the locally bilinear form Ξ : B(S1,ρ4) × B(S1,ρ4) → R/Z as follows. We ﬁrst deﬁne the locally linear map ι : B(S1,ρ4) → RS by the formula

ms p }

ι(m) := {

,

![image 300](<2017-green-new-bounds-szemer-edi_images/imageFile300.png>)

s∈S

where x  → {x} is the signed fractional map from R/Z to (−1/2,1/2]; note that ι takes values in the box [−ρ4,ρ4]S. We then deﬁne

ξ′′(n)m p − F(n) · ι(m) (9.79)

Ξ(n,m) :=

![image 301](<2017-green-new-bounds-szemer-edi_images/imageFile301.png>)

for n,m ∈ B(S1,ρ4), where · denotes the dot product on RS. It is clear that Ξ is locally linear in m; we also claim that it is locally linear in n, thus

Ξ(n1 + n2,m) − Ξ(n1,m) − Ξ(n2,m) = 0 (9.80)

- whenever n1,n2,n1 + n2 ∈ B(S1,ρ4). By (9.64) and Proposition 9.20, the left-hand side of (9.80) may be written as


µ(n1,n2)m p − π(˜µ(n1,n2)) · ι(m) mod 1.

![image 302](<2017-green-new-bounds-szemer-edi_images/imageFile302.png>)

- From (9.67) we have


µ(n1,n2)m p

= µ˜(n1,n2) · ι(m) mod 1

![image 303](<2017-green-new-bounds-szemer-edi_images/imageFile303.png>)

so to prove (9.80), it suﬃces to show that ι(m) lies in V ⊥. This is equivalent to showing that ι(m) · vi = 0 for i = 1,... ,d. Since vi ∈ ker(φ), we have

ι(m) · vi = 0 mod 1.

On the other hand, we have ι(m) = O(K1/2ρ4), and from (9.70) with t = Ni−1 followed by (9.71), we have

exp(KC1) ρ3 and hence |ι(m) · vi| < 1. The claim follows.

|vi| Ni−1 <

![image 304](<2017-green-new-bounds-szemer-edi_images/imageFile304.png>)

Now we verify (9.63). Let a0,ξ0 be as in Proposition 9.16. Let n,n0,h,n1, m1 be drawn independently and regularly from the Bohr sets B(S1,ρ3/4),

B(S,ρ0), B(S1,ρ4), B(S1,ρ6), B(S1,ρ5) respectively. From Proposition 9.16 we have

P(n0 = n0,n = n)|Ef(n0 + h + a0 − n)f(n0 + h)ep((ξ′′(n) − ξ0)h)|2

![image 305](<2017-green-new-bounds-szemer-edi_images/imageFile305.png>)

n0,n

≫ ηC1+O(1).

Using Lemma 4.4 to replace n by n + n1, and to replace h by h + m1, we have

P(n0 = n0,n = n,n1 = n1) Ef(n0 + h + m1 + a0 − n − n1)×

n0,n,n1

2

× f(n0 + h + m1)ep((ξ′′(n + n1) − ξ0)(h + m1))

≫ ηC1+O(1) and thus by the triangle inequality we have

![image 306](<2017-green-new-bounds-szemer-edi_images/imageFile306.png>)

P(n0 = n0,n = n,n1 = n1,h = h) Ef(n0 + h + m1 + a0 − n − n1)×

n0,n,n1,h

2

≫ ηC1+O(1).

× f(n0 + h + m1)ep((ξ′′(n + n1) − ξ0)(h + m1))

![image 307](<2017-green-new-bounds-szemer-edi_images/imageFile307.png>)

The phase e((ξ′′(n + n1) − ξ0)h) is deterministic and may thus be omitted:

P(n0 = n0,n = n,n1 = n1,h = h) Ef(n0 + h + m1 + a0 − n − n1)×

n0,n,n1,h

2

× f(n0 + h + m1)ep((ξ′′(n + n1) − ξ0)m1)

≫ ηC1+O(1).

![image 308](<2017-green-new-bounds-szemer-edi_images/imageFile308.png>)

As the expectation only depends on the sum n0+h rather than the individual variables n0,h, we thus have

P(n0 + h = n0,n = n,n1 = n1) Ef(n0 + m1 + a0 − n − n1)×

n0,n,n1

2

× f(n0 + m1)ep((ξ′′(n + n1) − ξ0)m1)

≫ ηC1+O(1).

![image 309](<2017-green-new-bounds-szemer-edi_images/imageFile309.png>)

By Lemma 4.4 we may replace n0 + h here by n0. From (9.57) we have

ξ′′(n + n1) − ξ′′(n) − ξ′′(n1))m1 R/Z ≪ η100C1 and so

P(n0 = n0,n = n,n1 = n1) Ef(n0 + a0 + m1 − n − n1)×

n0,n,n1

2

× f(n0 + m1)ep((ξ′′(n) + ξ′′(n1) − ξ0)m1)

≫ ηC1+O(1).

![image 310](<2017-green-new-bounds-szemer-edi_images/imageFile310.png>)

By the pigeonhole principle, there thus exists n ∈ B(S∗,ρ3/4) such that

![image 311](<2017-green-new-bounds-szemer-edi_images/imageFile311.png>)

P(n0 = n0n1 =n1)|Ef(n0 + a0 + m1 − n − n1)f(n0 + m1)×

n0,n1

× ep((ξ′′(n) + ξ′′(n1) − ξ0)m1)|2 ≫ ηC1+O(1), which, if we write a1 := a0 − n and ξ1 := ξ0 − ξ′′(n), simpliﬁes to

![image 312](<2017-green-new-bounds-szemer-edi_images/imageFile312.png>)

P(n0 = n0n1 = n1)|Ef(n0 + m1 + a1 − n1)f(n0 + m1)×

n0,n1

× ep((ξ′′(n1) − ξ1)m1)|2 ≫ ηC1+O(1). Since a0 ∈ B(S,3ρ2) and n ∈ B(S∗,ρ3/4), we have a1 ∈ B(S,4ρ2).

Now, from (9.79) one has ep(ξ′′(n1)m1) = e(Ξ(n1,m1))e(−F(n1) · ι(m1));

but since m1 ∈ B(S∗,ρ5), we have ι(m1) = O(Kρ5), and hence by (9.72) we have

F(n1) · ι(m1) R/Z ≪ η100C1, and so

![image 313](<2017-green-new-bounds-szemer-edi_images/imageFile313.png>)

P(n0 = n0;n1 = n1) Ef(n0 + m1 + a1 − n1)f(n0 + m1)×

n0,n1

2

≫ ηC1+O(1), which gives (9.63). The proof of Theorem 9.18 is now complete.

× e(Ξ(n1,m1) − ξ1m1)

- 9.21. Eighth step: making the frequency function symmetric. The next step is the “symmetry step” from [21, 36], which uses the CauchySchwarz inequality to ensure that Ξ is essentially symmetric.


Theorem 9.22. Let the notation and hypotheses be as in Theorem 9.18. For n,m ∈ B(S1,ρ4), deﬁne

{n,m} := Ξ(n,m) − Ξ(m,n). Then there exists a natural number k with 1 k ≪ exp(KO(C1)) such that

n S⊥

m S1 ρ8

1

k{n,m} R/Z

![image 314](<2017-green-new-bounds-szemer-edi_images/imageFile314.png>)

![image 315](<2017-green-new-bounds-szemer-edi_images/imageFile315.png>)

ρ8

for all n,m ∈ B(S1,ρ9). Proof. Let n0,m1,n1 be as in Theorem 9.18. From (9.63) and the pigeonhole principle, we may ﬁnd n0 ∈ Z/pZ such that

![image 316](<2017-green-new-bounds-szemer-edi_images/imageFile316.png>)

P(n1 = n1) Ef(n0 + m1 + a1−n1)f(n0 + m1)×

n1

2

≫ ηC1+O(1)

× e(Ξ(n1,m1) − ξ1m1)

which by the boundedness of the expectation implies

n1

![image 317](<2017-green-new-bounds-szemer-edi_images/imageFile317.png>)

P(n1 = n1) Ef(n0 + m1 + a1 − n1)f(n0 + m1)×

× e(Ξ(n1,m1) − ξ1m1) ≫ ηC1+O(1) and thus we may ﬁnd a 1-bounded function b1 : Z/pZ → C such that

|Eb1(n1)f(n0 + m1 + a1 − n1)f(n0 + m1)e(Ξ(n1,m1) − ξ1m1)| ≫ ηC1+O(1). Writing b2(n) := f(n0 + a1 + n) and b3(n) := f(n0 + m1)e(−ξ1m1), we may simplify this as

![image 318](<2017-green-new-bounds-szemer-edi_images/imageFile318.png>)

![image 319](<2017-green-new-bounds-szemer-edi_images/imageFile319.png>)

|Eb1(n1)b2(m1 − n1)b3(m1)e(Ξ(n1,m1))| ≫ ηC1+O(1).

Using the Cauchy-Schwarz inequality (Lemma 2.1) to eliminate the b3(m1) factor, we conclude that

|Eb1(n1)b1(n′1)b2(m1−n1)b2(m1−n′1)e(Ξ(n1,m1)−Ξ(n′1,m1)| ≫ η2C1+O(1) where n′1 is an independent copy of n1. Writing k := n1 + n′1 − m1, and noting from the local bilinearity of Ξ that

![image 320](<2017-green-new-bounds-szemer-edi_images/imageFile320.png>)

![image 321](<2017-green-new-bounds-szemer-edi_images/imageFile321.png>)

Ξ(n1,m1) − Ξ(n′1,m1) = Ξ(n1 − n′1,m1)

= Ξ(n1 − n′1,n1 + n′1 − k)

= Ξ(n1,n1) − Ξ(n′1,n′1) + {n1,n′1}

− Ξ(n1,k) + Ξ(n′1,k) we conclude that

|Eb3(n1,k)b4(n′1,k)e({n1,n′1})| ≫ η2C1+O(1), where b3,b4 : Z/pZ × Z/pZ → C are the 1-bounded functions

- b3(n1,k) := b1(n1)b2(k − n1)e(Ξ(n1,n1) − Ξ(n1,k))

![image 322](<2017-green-new-bounds-szemer-edi_images/imageFile322.png>)

and

- b4(n′1,k) := b1(n′1)b2(k − n′1)e(−Ξ(n′1,n′1) + Ξ(n′1,k)).


![image 323](<2017-green-new-bounds-szemer-edi_images/imageFile323.png>)

For ﬁxed n1,n′1, we see from Lemma 4.4 that k diﬀers from m1 in total variation by O(η100C1), and hence

|Eb3(n1,m1)b4(n′1,m1)e({n1,n′1})| ≫ η2C1+O(1). By the pigeonhole principle, we may thus ﬁnd m1 ∈ Z/pZ such that |Eb3(n1,m1)b4(n′1,m1)e({n1,n′1})| ≫ η2C1+O(1).

Using Cauchy-Schwarz (Lemma 2.1) to eliminate b4(n′1,m1), and using the local bilinearity of {,}, we conclude that

|Eb3(n1,m1)b3(l1,m1)e({n1 − l1,n′1})| ≫ η4C1+O(1)

![image 324](<2017-green-new-bounds-szemer-edi_images/imageFile324.png>)

where l1 is an independent copy of n1; using a further application of CauchySchwarz (Lemma 2.1) to eliminate b3(n1,m1)b3(l1,m1), we conclude that

![image 325](<2017-green-new-bounds-szemer-edi_images/imageFile325.png>)

|Ee({n1 − l1,n′1 − l′1})| ≫ η8C1+O(1)

where l′1 is an independent copy of n′1 (thus n1,n′1,l1,l′1 are jointly independent and drawn regularly from B(S1,ρ6)). In particular, by the pigeonhole principle one can ﬁnd l1,l1′ ∈ B(S1,ρ6) such that

|Ee({n1 − l1,n′1 − l1′ })| ≫ η8C1+O(1).

By local bilinearity, one can rewrite {n1−l1,n′1−l1′ } as {n1,n′1} plus locally linear functions of n1 and n′1. The claim now follows from Proposition 4.11.

9.23. Ninth step: integrating the frequency function. We may now ﬁnally prove Theorem 8.1. Let the notation and hypotheses be as in that theorem, let S1 and Ξ be as in Theorem 9.18, and let k be as in Theorem

- 9.22. Thus if we let n0,n1,m1 be drawn independently and regularly from B(S,ρ0), B(S1,ρ6), B(S1,ρ5) respectively, we have


![image 326](<2017-green-new-bounds-szemer-edi_images/imageFile326.png>)

P(n0 = n0,n1 = n1) Ef(n0+m1 + a1 − n1)f(n0 + m1)×

n0,n1

× e(Ξ(n1,m1) − ξ1m1) 2 ≫ ηC1+O(1). (9.81)

Now let n2,m2 be drawn independently and regularly from the Bohr sets B(S1,ρ9),B(S1,ρ10) respectively, independently of all previous random variables. By Lemma 4.4, we may replace n1,m1 by n1 +2kn2 and m1 +2km2 in (9.81), leading to

P(n0 = n0,... ,n2 = n2) Ef(n0 + m1 + 2km2 + a1 − n1 − 2kn2)×

n0,n1,n2

× f(n0 + m1 + 2km2)e(Ξ(n1 + 2kn2,m1 + 2km2) − ξ1(m1 + 2km2)) 2 ≫ ηC1+O(1).

![image 327](<2017-green-new-bounds-szemer-edi_images/imageFile327.png>)

Thus we may ﬁnd n1 ∈ B(S1,ρ6), m1 ∈ B(S1,ρ5) such that

P(n0 = n0,n2 = n2) Ef(n0 + m1 + 2km2 + a1 − n1 − 2kn2)×

n0,n2

f(n0 + m1 + 2km2)e(Ξ(n1 + 2kn2,m1 + 2km2) − ξ1(m1 + 2km2)) 2 ≫ ηC1+O(1),

![image 328](<2017-green-new-bounds-szemer-edi_images/imageFile328.png>)

which we can simplify slightly as

P(n0 = n0,n2 = n2) Ef(n0 + 2km2 + a2 − 2kn2)×

n0,n2

× f(n0 + m1 + 2km2)e(Ξ(n1 + 2kn2,m1 + 2km2) − 2kξ1m2) 2 ≫ ηC1+O(1)

![image 329](<2017-green-new-bounds-szemer-edi_images/imageFile329.png>)

- where a2 := a1 + m1 − n1; since a1 ∈ B(S,4ρ2), m1 ∈ B(S1,ρ5), n1 ∈ B(S1,ρ6), we have a2 ∈ B(S,5ρ2). By the local bilinearity of Ξ, we have


Ξ(n1 + 2kn2,m1 + 2km2)

= Ξ(n1,m1) + 2kΞ(n2,m1) + 2kΞ(n1,m2) + 4k2Ξ(n2,m2)

= Ξ(n1,m1) + 2kΞ(n2,m1) + 2kΞ(n1,m2) + 2k2Ξ(n2 + m2,n2 + m2)

− 2k2Ξ(n2,n2) − 2k2Ξ(m2,m2) + 2k2{n2,m2} and so we have

P(n0 = n0,n2 = n2)|EF(n0,n2 − m2)G(n0,m2)e(2k2{n2,m2})|2

n0,n2

≫ ηC1+O(1) where

F(n,m) := f(n + a2 − 2km)e(−k2Ξ(m,m)) (9.82) and

G(n,m) := f(n + m1 + 2km)e(2kΞ(n1,m) − 2k2Ξ(m,m) − 2kξ1m). By Theorem 9.22, one has k{n2,m2} R/Z ≪ η100C1, and thus

![image 330](<2017-green-new-bounds-szemer-edi_images/imageFile330.png>)

P(n0 = n0,n2 = n2)|EF(n0,n2 − m2)G(n0,m2)|2 ≫ ηC1+O(1).

n0,n2

By boundedness of the expectation, this implies that

P(n0 = n0,n2 = n2)|E(F(n0,n2 − m2)G(n0,m2)| ≫ ηC1+O(1)

n0,n2

and thus

|EF(n0,n2 − m2)G(n0,m2)H(n0,n2)| ≫ ηC1+O(1)

for some 1-bounded function H : Z/pZ × Z/pZ → C. By Cauchy-Schwarz (Lemma 2.1), we thus have

|EF(n0,n2 − m2)G(n0,m2)F(n0,n2 − m′2)G(n0,m2)| ≫ η2C1+O(1)

![image 331](<2017-green-new-bounds-szemer-edi_images/imageFile331.png>)

![image 332](<2017-green-new-bounds-szemer-edi_images/imageFile332.png>)

- where m′2 is an independent copy of m2; by a second application of CauchySchwarz (Lemma 2.1), we then have |EF(n0,n2−m2)F(n0,n2−m′2)F(n0,n′2−m2)F(n0,n′2−m′2)| ≫ η4C1+O(1)


![image 333](<2017-green-new-bounds-szemer-edi_images/imageFile333.png>)

![image 334](<2017-green-new-bounds-szemer-edi_images/imageFile334.png>)

- where n′2 is an independent copy of n2. Since the distributions of m2,m′2 are symmetric, we thus have


|EF(n0,n2+m2)F(n0,n2+m′2)F(n0,n′2+m2)F(n0,n′2+m′2)| ≫ η4C1+O(1). In particular, with probability ≫ η4C1+O(1), the random variable n0 attains a value n0 for which

![image 335](<2017-green-new-bounds-szemer-edi_images/imageFile335.png>)

![image 336](<2017-green-new-bounds-szemer-edi_images/imageFile336.png>)

|EF(n0,n2+m2)F(n0,n2+m′2)F(n0,n′2+m2)F(n0,n′2+m′2)| ≫ η4C1+O(1).

![image 337](<2017-green-new-bounds-szemer-edi_images/imageFile337.png>)

![image 338](<2017-green-new-bounds-szemer-edi_images/imageFile338.png>)

(9.83) If n0 is such that (9.83) holds, then we may apply Theorem 4.12 and conclude that there exists a frequency β(n0) ∈ Z/pZ such that

P(n2 = n2)E(F(n0,n2 + m2)e(−β(n0)m2)| ≫ η2C1+O(1)

|

n2

and thus (deﬁning β(n0) arbitrarily if (9.83) does not hold),

P(n0 = n0,n2 = n2)|EF(n0,n2 + m2)e(−β(n0)m2)| ≫ η6C1+O(1)

n0,n2

and hence there exists n2 ∈ B(S1,ρ9) with

P(n0 = n0)|E(F(n0,n2 + m2)e(−β(n0)m2)| ≫ η6C1+O(1).

n0

Applying (9.82), we conclude that

P(n0 = n0) E(f(n0 + a3 − 2km2)e(−k2Ξ(m2,m2)−β(n0)m2)

n0

≫ η6C1+O(1)

- where a3 := a2 − 2kn2; since a2 ∈ B(S,5ρ2), n2 ∈ B(S1,ρ9), and k = O(exp(KO(C1))), we have a3 ∈ B(S,6ρ2). In particular, by Lemma 4.4, n0 and n0 + a3 diﬀer in total variation by O(η100C1+O(1)), and thus


P(n0 = n0)|Ef(n0 − 2km2)e(−k2Ξ(m2,m2) − β(n0)m2)| ≫ η6C1+O(1).

n0

Theorem 8.1 then follows after a change of variables, noting that the map m2  → Ξ(m2,m2) is locally quadratic on B(S1,ρ9).

References

- [1] A. Balog and E. Szemere´di, A statistical theorem of set addition, Combinatorica 14

(1994), no. 3, 263–268.

- [2] V. Bergelson, B. Host and B. Kra, Multiple recurrence and nilsequences. With an appendix by Imre Ruzsa, Invent. Math. 160 (2005), no. 2, 261–303.
- [3] F. A. Behrend, On sets of integers which contain no three terms in arithmetic progression, Proc. Nat. Acad. Sci. 32 (1946), 331–332.
- [4] T. F. Bloom, A quantitative improvement for Roth’s theorem on arithmetic progressions, J. Lond. Math. Soc. (2) 93 (2016), no. 3, 643–663.
- [5] M. Blum, M. Luby and R. Rubinfeld, Self-testing/correcting with applications to numerical problems, Proceedings of the 22nd Annual ACM Symposium on Theory of Computing (Baltimore, MD, 1990). J. Comput. System Sci. 47 (1993), no. 3, 549–595.


- [6] J. Bourgain, On triples in arithmetic progression, GAFA 9 (1999), no. 5, 968–984.
- [7] , Roth’s theorem on progressions revisited, J. Anal. Math., 104 (2008), 155– 192.

![image 339](<2017-green-new-bounds-szemer-edi_images/imageFile339.png>)

- [8] M. Elkin, An improved construction of progression-free sets, Israel J. Math. 184

(2011), 93-128.

- [9] P. Erd˝s, Problems in number theory and Combinatorics, in Proceedings of the Sixth Manitoba Conference on Numerical Mathematics (Univ. Manitoba, Winnipeg, Man., 1976), Congress. Numer. XVIII, 35–58, Utilitas Math., Winnipeg, Man., 1977
- [10] P. Erd˝s and P. Tur´an, On some sequences of integers, Journal of the London Mathematical Society 11 (1936), 261-264.
- [11] H. Furstenberg, Nonconventional ergodic averages, The legacy of John von Neumann (Hempstead, NY, 1988), 43–56, Proc. Sympos. Pure Math., 50, Amer. Math. Soc., Providence, RI, 1990.
- [12] W. T. Gowers, A new proof of Szemer´edi’s theorem for progressions of length four, GAFA 8 (1998), no. 3, 529–551.
- [13] , A new proof of Szemer´edi’s theorem, GAFA 11 (2001), 465–588.

![image 340](<2017-green-new-bounds-szemer-edi_images/imageFile340.png>)

- [14] W. T. Gowers and J. Wolf, Linear forms and quadratic uniformity for functions on Fnp, Mathematika 57 (2011), no. 2, 215–237.
- [15] B. J. Green, On arithmetic structures in dense sets of integers, Duke Math. J. 114

(2002), no. 2, 215–238.

- [16] , Finite ﬁeld models in additive combinatorics, Surveys in Combinatorics 2005, LMS Lecture Note Series 327,1–29.

![image 341](<2017-green-new-bounds-szemer-edi_images/imageFile341.png>)

- [17] , Generalizing the Hardy-Littlewood method for primes, Proc. Intern. Cong. Math. (Madrid 2006), Vol. 2, 373–399.

![image 342](<2017-green-new-bounds-szemer-edi_images/imageFile342.png>)

- [18] , Montr´eal lecture notes on quadratic Fourier analysis, Additive combinatorics (ed. Granville, Nathanson and Solymosi) , 69–102, CRM Proc. Lecture Notes, 43, Amer. Math. Soc., Providence, RI, 2007.

![image 343](<2017-green-new-bounds-szemer-edi_images/imageFile343.png>)

- [19] , A Szemer´edi-type regularity lemma in abelian groups, with applications, Geom. Funct. Anal. 15 (2005), no. 2, 340–376.

![image 344](<2017-green-new-bounds-szemer-edi_images/imageFile344.png>)

- [20] B. J. Green and T. C. Tao, The primes contain arbitrarily long arithmetic progressions, Ann. of Math. (2) 171 (2010), no. 3, 1753–1850.
- [21] , An inverse theorem for the Gowers U3(G)-norm, Proc. Edinb. Math. Soc.

![image 345](<2017-green-new-bounds-szemer-edi_images/imageFile345.png>)

(2) 51 (2008), no. 1, 73–153.

- [22] , New bounds for Szemer´edi’s theorem, I: Progressions of length 4 in ﬁnite ﬁeld geometries, Proc. Lond. Math. Soc. (3) 98 (2009), no. 2, 365–392.

![image 346](<2017-green-new-bounds-szemer-edi_images/imageFile346.png>)

- [23] , New bounds for Szemer´edi’s theorem, Ia: Progressions of length 4 in ﬁnite ﬁeld geometries revisited, preprint available at https://arxiv.org/abs/1205.1330.

![image 347](<2017-green-new-bounds-szemer-edi_images/imageFile347.png>)

- [24] , Quadratic uniformity of the M¨obius function, Ann. Inst. Fourier (Grenoble) 58 (2008), no. 6, 1863–1935.

![image 348](<2017-green-new-bounds-szemer-edi_images/imageFile348.png>)

- [25] , An arithmetic regularity lemma, an associated counting lemma, and applications, An irregular mind, 261–334, Bolyai Soc. Math. Stud., 21, J´anos Bolyai Math. Soc., Budapest, 2010.

![image 349](<2017-green-new-bounds-szemer-edi_images/imageFile349.png>)

- [26] , New bounds for Szemer´edi’s Theorem, II: A new bound for r4(N), Analytic number theory: essays in honour of Klaus Roth, W. W. L. Chen, W. T. Gowers, H. Halberstam, W. M. Schmidt, R. C. Vaughan, eds, Cambridge University Press,

![image 350](<2017-green-new-bounds-szemer-edi_images/imageFile350.png>)

2009. 180–204.

- [27] , Linear equations in primes, Ann. of Math. 171 (2010), no. 3, 1753–1850.

![image 351](<2017-green-new-bounds-szemer-edi_images/imageFile351.png>)

- [28] B. J. Green, T. C. Tao and T. Ziegler, An inverse theorem for the Gowers U4-norm, Glasg. Math. J. 53 (2011), no. 1, 1–50.
- [29] B. J. Green and J. Wolf, A note on Elkin’s improvement of Behrend’s construction, in Additive Number Theory, 141–144, Springer, New York, 2010.
- [30] D. R. Heath-Brown, Integer sets containing no arithmetic progressions, J. London Math. Soc. 35 (1987), 385–394.


- [31] I.  Laba, M. Lacey, On sets of integers not containing long arithmetic progressions, unpublished.
- [32] H. Montgomery, Ten lectures on the interface between analytic number theory and harmonic analysis, CBMS Regional Conference Series in Mathematics 84, AMS 1994.
- [33] R.A. Rankin, Sets of integers containing not more than a given number of terms in arithmetic progression, Proc. Roy. Soc. Edinburgh Sect. A 65 (1960/1961), 332–344.
- [34] K. F. Roth, On certain sets of integers, J. London Math. Soc. 28 (1953), 245–252.
- [35] , Irregularities of sequences relative to arithmetic progressions, IV. Period. Math. Hungar. 2 (1972), 301–326.

![image 352](<2017-green-new-bounds-szemer-edi_images/imageFile352.png>)

- [36] A. Samorodnitsky, Low degree tests at large distances, In STOC 2007, Proceedings of the thirty-ninth annual ACM symposium on Theory of computing, San Diego, California, USA, 506–515.
- [37] T. Sanders, On certain other sets of integers, J. Anal. Math. 116 (2012), 53–82.
- [38] , On Roth’s theorem on progressions, Ann. of Math. (2) 174 (2011), no. 1, 619–636.

![image 353](<2017-green-new-bounds-szemer-edi_images/imageFile353.png>)

- [39] W. M. Schmidt, Small fractional parts of polynomials, CBMS Regional conference series in math. 32, Amer. Math. Soc. 1977.
- [40] E. M. Stein, Harmonic analysis: real-variable methods, orthogonality, and oscillatory integrals. With the assistance of Timothy S. Murphy. Princeton Mathematical Series,

43. Monographs in Harmonic Analysis, III. Princeton University Press, Princeton, NJ, 1993.

- [41] E. Szemere´di, On sets of integers containing no four elements in arithmetic progression, Acta Math. Acad. Sci. Hungar. 20 (1969), 89–104.
- [42] , On sets of integers containing no k elements in arithmetic progression, Acta Arith. 27 (1975), 299–345.

![image 354](<2017-green-new-bounds-szemer-edi_images/imageFile354.png>)

- [43] , Regular partitions of graphs, Proble´mes combinatoires et the´orie des graphes (Colloq. Internat. CNRS, Univ. Orsay, Orsay, 1976), pp. 399–401, Colloq. Internat. CNRS, 260, CNRS, Paris, 1978.

![image 355](<2017-green-new-bounds-szemer-edi_images/imageFile355.png>)

- [44] , Integer sets containing no arithmetic progressions, Acta Math. Hungar.56

![image 356](<2017-green-new-bounds-szemer-edi_images/imageFile356.png>)

(1990), no. 1-2, 155–158.

- [45] T. C. Tao, Obstructions to uniformity, and arithmetic patterns in the primes, Quarterly J. Pure Appl. Math. 2 (2006), 199–217 [Special issue in honour of John H. Coates, Vol. 1 of 2]
- [46] , Arithmetic progressions in the primes, 2004 El Escorial conference proceedings.

![image 357](<2017-green-new-bounds-szemer-edi_images/imageFile357.png>)

- [47] , The dichotomy between structure and randomness, arithmetic progressions, and the primes, ICM proceedings, Madrid 2006.

![image 358](<2017-green-new-bounds-szemer-edi_images/imageFile358.png>)

- [48] T. C. Tao and V. H. Vu, Additive combinatorics, Cambridge Studies in Advanced Math. 105, Cambridge University Press, 2006.
- [49] , John-type theorems for generalized arithmetic progressions and iterated sumsets, Adv. in Math. 219 (2008), 428–449.

![image 359](<2017-green-new-bounds-szemer-edi_images/imageFile359.png>)

- [50] , Higher order Fourier Analysis, Graduate Studies in Mathematics 142, American Mathematical Society, Providence RI 2012.

![image 360](<2017-green-new-bounds-szemer-edi_images/imageFile360.png>)

- [51] T. C. Tao and T. Ziegler, The primes contain arbitrarily long polynomial progressions, Acta Math. 201 (2008), no. 2, 213–305.
- [52] R. C. Vaughan, The Hardy-Littlewood Method, 2nd Ed., Cambridge Tracts in Mathematics 125, CUP 1997.
- [53] T. Ziegler, A non-conventional ergodic theorem for a nilsystem, Ergodic Theory Dynam. Systems 25 (2005), no. 4, 1357–1370.


Mathematical Institute, Andrew Wiles Building, Radcliffe Observatory

Quarter, Woodstock Rd, Oxford OX2 6GG. E-mail address: ben.green@maths.ox.ac.uk Department of Mathematics, UCLA, Los Angeles CA 90095-1555, USA. E-mail address: tao@math.ucla.edu

