"""Hodge classes on Fermat varieties and Shioda's inductive structure.

Setting
-------
X = X^n_m :  x_0^m + x_1^m + ... + x_{n+1}^m = 0   in  P^{n+1},   a smooth hypersurface of dimension n and degree m.

The group G = mu_m^{n+2} / (diagonal) acts on X, and the primitive middle cohomology decomposes into one-dimensional
eigenspaces (Weil, Shioda-Katsura):

    H^n_prim(X, C) = (+)_{alpha in A^n_m}  V(alpha),

    A^n_m = { alpha = (a_0, ..., a_{n+1}) in (Z/m)^{n+2} :  a_i != 0 for all i,  sum a_i = 0 }.

Writing <x> in (0,1) for the fractional part of a representative x/m with 1 <= x <= m-1 and

    |alpha| = sum_i <a_i>         (an integer, 1 <= |alpha| <= n+1),

one has V(alpha) in H^{n-q, q}(X) with q = |alpha| - 1  (this is Griffiths' residue of the monomial x^{alpha - 1}).

Rational structure.  The Galois group (Z/m)^* acts on characters by alpha -> t.alpha, and the Q-span of a class in
V(alpha) involves all the conjugates V(t.alpha).  Hence for n = 2p the space of rational Hodge classes in
H^n_prim(X, Q) has dimension |B^n_m|, where

    B^n_m = { alpha in A^n_m :  |t.alpha| = n/2 + 1  for every t in (Z/m)^* }      ("Hodge characters").

Together with the class h^p of a linear section, dim Hdg^p(X) = |B^n_m| + 1.

Shioda-Katsura inductive structure (Tohoku Math. J. 31 (1979)).  There is an explicit correspondence between
X^r_m x X^s_m and X^{r+s}_m (blow up along X^{r-1} x X^{s-1}, quotient by mu_m, blow down) under which

    H^{r+s}_prim(X^{r+s})  =  [ H^r_prim(X^r) (x) H^s_prim(X^s) ]^{mu_m}   (+)   H^{r-1}_prim(X^{r-1}) (x) H^{s-1}_prim(X^{s-1}) (-1)

compatibly with Hodge structures and with algebraic cycle classes.  On characters:

  (N)  beta = (b_0..b_r, c) in A^r,  gamma = (g_0..g_s, -c) in A^s,  c != 0   |-->   beta # gamma = (b_0..b_r, g_0..g_s) in A^{r+s};
  (Z)  beta' in A^{r-1},  gamma' in A^{s-1}                                  |-->   (beta', gamma')  in A^{r+s}   (concatenation).

Consequently, if V(beta) and V(gamma) are spanned by algebraic cycles (on X^r and X^s), then so is V(beta # gamma); and
if V(beta'), V(gamma') are algebraic then so is V((beta', gamma')).  Shioda (Math. Ann. 245 (1979)) used this to prove
the Hodge conjecture for X^n_m in many cases, by showing that every Hodge character is *decomposable*, i.e. can be
built from lower-dimensional Hodge characters by (N) and (Z), down to the base cases

    n = 0  (X^0_m is m points: every class is algebraic),
    n = 2  (every Hodge class on a surface is algebraic by the Lefschetz (1,1) theorem).

What this module computes
-------------------------
* A^n_m, B^n_m, Hodge numbers of X^n_m by characters (cross-checked against hodge.griffiths),
* the restricted "decomposable" predicate defined above (only (N) and (Z) with *both* factors Hodge characters,
  recursively decomposable), and
* the set of Hodge characters that are NOT decomposable in this sense.  For these the Hodge conjecture is not
  settled by the inductive structure alone (Aoki, Math. Ann. 266 (1983); J. Math. Soc. Japan 39 (1987) constructs
  further explicit cycles for some of them).

A character with no indecomposable element in B^n_m is a computer-verified instance of the Hodge conjecture for X^n_m
(given the theorems quoted above).  A character that is indecomposable is *not* a counterexample: it is a Hodge class
whose algebraicity needs a different construction.

Conventions: characters are stored as sorted tuples of integers in [1, m-1] (the problem is symmetric under
permutations of the coordinates and under the Galois action, both of which preserve decomposability).
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations_with_replacement
from math import gcd
from typing import Dict, FrozenSet, Iterator, List, Sequence, Tuple

Character = Tuple[int, ...]


# ----------------------------------------------------------------------------------------------------------------
# Enumeration of characters
# ----------------------------------------------------------------------------------------------------------------

def units(m: int) -> List[int]:
    """(Z/m)^*."""
    return [t for t in range(1, m) if gcd(t, m) == 1]


def norm(alpha: Sequence[int], m: int) -> int:
    """|alpha| = sum of fractional parts, as an integer (sum of representatives in [1, m-1]) divided by m."""
    s = sum(a % m for a in alpha)
    if s % m:
        raise ValueError(f"{alpha} does not sum to 0 mod {m}")
    return s // m


def scaled(alpha: Sequence[int], t: int, m: int) -> Character:
    return tuple(sorted((t * a) % m for a in alpha))


def is_hodge(alpha: Sequence[int], n: int, m: int) -> bool:
    """alpha in B^n_m ?  (n must be even and alpha in A^n_m.)"""
    if n % 2:
        return False
    target = n // 2 + 1
    for t in units(m):
        if sum((t * a) % m for a in alpha) != target * m:
            return False
    return True


def characters(n: int, m: int) -> Iterator[Character]:
    """All of A^n_m up to permutation: sorted (n+2)-tuples from [1, m-1] with sum = 0 mod m."""
    if n < 0 or m < 2:
        return
    for alpha in combinations_with_replacement(range(1, m), n + 2):
        if sum(alpha) % m == 0:
            yield alpha


def hodge_characters(n: int, m: int) -> Iterator[Character]:
    """B^n_m up to permutation."""
    if n % 2:
        return
    target = (n // 2 + 1) * m
    us = units(m)
    for alpha in characters(n, m):
        if all(sum((t * a) % m for a in alpha) == target for t in us):
            yield alpha


def multiplicity(alpha: Sequence[int]) -> int:
    """Number of distinct permutations of alpha (so that sums over sorted tuples recover sums over A^n_m)."""
    from collections import Counter
    from math import factorial
    r = factorial(len(alpha))
    for c in Counter(alpha).values():
        r //= factorial(c)
    return r


def count_characters(n: int, m: int) -> int:
    """|A^n_m| = ((m-1)^{n+2} + (-1)^{n+2} (m-1)) / m, the primitive middle Betti number of X^n_m."""
    num = (m - 1) ** (n + 2) + (-1) ** (n + 2) * (m - 1)
    assert num % m == 0
    return num // m


def hodge_numbers_by_characters(n: int, m: int) -> List[int]:
    """[h^{n,0}_prim, ..., h^{0,n}_prim] of X^n_m computed by counting characters with |alpha| = q + 1."""
    out = [0] * (n + 1)
    for alpha in characters(n, m):
        q = sum(alpha) // m - 1
        out[q] += multiplicity(alpha)
    return out


def dim_hodge_classes(n: int, m: int) -> int:
    """dim_Q Hdg^{n/2}(X^n_m) = |B^n_m| + 1  (n even)."""
    if n % 2:
        return 0
    return 1 + sum(multiplicity(a) for a in hodge_characters(n, m))


def picard_number_fermat_surface(m: int) -> int:
    """rho(X^2_m) = dim Hdg^1 = |B^2_m| + 1 (all of these classes are algebraic by Lefschetz (1,1))."""
    return dim_hodge_classes(2, m)


# ----------------------------------------------------------------------------------------------------------------
# Shioda's inductive structure: decomposability
# ----------------------------------------------------------------------------------------------------------------

def _canon(seq: Sequence[int], m: int) -> Character:
    """Canonical representative of a character up to permutation and Galois action (the decomposability predicate
    is invariant under both, which lets the memo table stay small)."""
    best = None
    for t in units(m):
        cand = tuple(sorted((t * a) % m for a in seq))
        if best is None or cand < best:
            best = cand
    return best  # type: ignore[return-value]


@lru_cache(maxsize=None)
def is_decomposable(alpha: Character, m: int) -> bool:
    """Is the Hodge character alpha in B^n_m (n = len(alpha) - 2) decomposable via (N)/(Z) down to n in {0, 2}?

    alpha must be a Hodge character (checked).  Uses memoisation on the canonical form.
    """
    n = len(alpha) - 2
    if n % 2:
        raise ValueError("odd-dimensional Fermat varieties have no Hodge characters")
    if not is_hodge(alpha, n, m):
        raise ValueError(f"{alpha} is not a Hodge character for n={n}, m={m}")
    if n <= 2:
        return True
    canon = _canon(alpha, m)
    if canon != alpha:
        return is_decomposable(canon, m)

    k = n + 2
    idx = list(range(k))
    # Enumerate subsets S containing index 0 (S and its complement give the same decomposition).
    for mask in range(1, 1 << (k - 1)):
        S = [0] + [i + 1 for i in range(k - 1) if mask >> i & 1]
        sizeS = len(S)
        sizeT = k - sizeS
        if sizeS < 2 or sizeT < 2:
            continue
        T = [i for i in idx if i not in S]
        aS = [alpha[i] for i in S]
        aT = [alpha[i] for i in T]
        c = sum(aS) % m
        if c == 0:
            # (Z): alpha = (beta', gamma') with beta' in A^{|S|-2}, gamma' in A^{|T|-2}.
            r1, s1 = sizeS - 2, sizeT - 2
            if r1 % 2 or s1 % 2:
                continue
            beta = tuple(sorted(aS))
            gamma = tuple(sorted(aT))
            if not is_hodge(beta, r1, m):
                continue  # then gamma is not Hodge either; the product class is not a product of Hodge classes
            if is_decomposable(beta, m) and is_decomposable(gamma, m):
                return True
        else:
            # (N): alpha = beta # gamma with beta = (aS, -c) in A^{|S|-1}, gamma = (aT, c) in A^{|T|-1}.
            r, s = sizeS - 1, sizeT - 1
            if r % 2 or s % 2 or r < 2 or s < 2:
                continue
            beta = tuple(sorted(aS + [(-c) % m]))
            gamma = tuple(sorted(aT + [c]))
            if not is_hodge(beta, r, m):
                continue
            if is_decomposable(beta, m) and is_decomposable(gamma, m):
                return True
    return False


def indecomposable_hodge_characters(n: int, m: int) -> List[Character]:
    """Hodge characters of X^n_m (up to permutation) that are not decomposable."""
    return [a for a in hodge_characters(n, m) if not is_decomposable(a, m)]


def analyze(n: int, m: int) -> Dict[str, object]:
    """Summary statistics for X^n_m: Hodge numbers, number of Hodge classes, number (with multiplicity) of
    decomposable ones, and the indecomposable orbits."""
    hodge = list(hodge_characters(n, m))
    indec = [a for a in hodge if not is_decomposable(a, m)]
    n_hodge = sum(multiplicity(a) for a in hodge)
    n_indec = sum(multiplicity(a) for a in indec)
    # Galois orbits of indecomposables (canonical forms)
    orbits = sorted({_canon(a, m) for a in indec})
    return {
        "n": n,
        "m": m,
        "b_prim": count_characters(n, m),
        "hodge_numbers_prim": hodge_numbers_by_characters(n, m),
        "dim_hodge_classes": n_hodge + 1,
        "dim_decomposable": n_hodge - n_indec + 1,
        "dim_indecomposable": n_indec,
        "indecomposable_orbits": orbits,
        "hodge_conjecture_verified_by_inductive_structure": n_indec == 0,
    }
