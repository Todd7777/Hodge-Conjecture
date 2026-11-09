"""Aoki's formal module of tuples, the Hodge lattice B_d, and the lambda-invariant of the open degrees 44, 51, 52.

This module re-derives, with exact integer arithmetic and no dependencies, the lattice statements that
`docs/attacks/17-fermat-open-cases.md` (Theorem A) obtained with python-flint and PARI.  It shares no code with
`scripts/fermat_formal_module.py` or `scripts/fermat_span/`.

Notation (Aoki 1983; Miranda-Movasati-Rufino-Villaflor, arXiv:2609.27301, section 4)
--------------------------------------------------------------------------------------
* R_d = free Z-module on the symbols (a), a in (Z/d) - {0}.  A tuple (a_1, ..., a_L) is the vector sum_i (a_i);
  join is addition, deletion is subtraction, permutations act trivially.
* A tuple of length L is a *Hodge tuple* of degree d if  sum_i <t a_i>_d = L d / 2  for every unit t of Z/d, where
  <x>_d in [0, d) is the residue.  For even L these are the Hodge characters of the Fermat variety X^{L-2}_d.
* B_d = the Z-span of all Hodge tuples of degree d (all lengths) = the kernel lattice
  {v in R_d : sum_a v_a (<t a>_d - d/2) = 0 for all units t}   (docs/fermat/01-span-test.md, Lemma 1).
* D_d = span of (a) + (-a) and, for d even, eps_d = (d/2): the characters of the d points X^0_d.
* Folding.  pi : R_d -> Z^h, h = floor((d-1)/2), (a) -> e_a for a < d/2, -e_{d-a} for a > d/2, (d/2) -> 0.
  pi is onto and ker(pi) = D_d.  Hence R_d / L = Z^h / pi(L) for every lattice D_d <= L <= R_d; in particular
  L is saturated in R_d iff pi(L) is saturated in Z^h, and indices between such lattices can be computed in Z^h.

The lambda-invariants (`LAMBDA`) are additive functionals R_d -> Z that kill D_d, so they factor through pi:
lambda_44 = n_11 - n_33 = x_11,  lambda_51 = n_17 - n_34 = x_17,  lambda_52 = n_1 + n_25 - n_27 - n_51 = x_1 + x_25.

Everything here is exact.  The lattice code keeps a row-style Hermite basis and is unimodular, so it also
computes integer kernels.
"""

from __future__ import annotations

from itertools import combinations_with_replacement
from math import gcd
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

Tuple_ = Tuple[int, ...]

LAMBDA: Dict[int, Dict[int, int]] = {44: {11: 1, 33: -1}, 51: {17: 1, 34: -1}, 52: {1: 1, 25: 1, 27: -1, 51: -1}}
EXCEPTIONAL: Dict[int, Tuple_] = {44: (1, 5, 13, 22, 24, 33, 37, 41),
                                  51: (1, 4, 7, 19, 24, 34, 37, 40, 43, 46),
                                  52: (1, 4, 17, 21, 29, 41, 45, 50)}


# ------------------------------------------------------------------------------------------- arithmetic helpers

def units(d: int) -> List[int]:
    return [t for t in range(1, d) if gcd(t, d) == 1]


def half_units(d: int) -> List[int]:
    """Units t with t < d/2.  The Hodge conditions for t and d - t are equivalent (<-x> = d - <x> for x != 0)."""
    return [t for t in units(d) if 2 * t < d]


def prime_divisors(n: int) -> List[int]:
    out, p = [], 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def xgcd(a: int, b: int) -> Tuple[int, int, int]:
    """(g, s, t) with s a + t b = g = gcd(a, b) >= 0."""
    s0, s1, t0, t1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    if a < 0:
        a, s0, t0 = -a, -s0, -t0
    return a, s0, t0


# ------------------------------------------------------------------------------------------- tuples

def is_hodge_tuple(tup: Sequence[int], d: int) -> bool:
    """sum_i <t a_i> = L d / 2 for every unit t (entries must be nonzero mod d)."""
    L = len(tup)
    if any(a % d == 0 for a in tup) or (L * d) % 2:
        return False
    target = L * d // 2
    return all(sum((t * a) % d for a in tup) == target for t in half_units(d))


def hodge_tuples(d: int, L: int) -> List[Tuple_]:
    """All sorted Hodge tuples of length L >= 2 and degree d, entries in [1, d-1].

    Meet in the middle: a multiset is Hodge iff the vector (sum_i <t a_i>)_t equals (L d/2, ..., L d/2); split it into
    a sub-multiset of size floor(L/2) and its complement and match the two halves in a dictionary."""
    if (L * d) % 2 or L < 2:
        return []
    us = half_units(d)
    base = L * d + 1
    weight = [base ** j for j in range(len(us))]

    def key(ms: Sequence[int]) -> int:
        return sum(w * sum((t * a) % d for a in ms) for w, t in zip(weight, us))

    target = sum(w * (L * d // 2) for w in weight)
    L1, L2 = L // 2, L - L // 2
    table: Dict[int, List[Tuple_]] = {}
    for ms in combinations_with_replacement(range(1, d), L1):
        table.setdefault(key(ms), []).append(ms)
    out = set()
    for ms in combinations_with_replacement(range(1, d), L2):
        for other in table.get(target - key(ms), ()):
            out.add(tuple(sorted(ms + other)))
    return sorted(out)


def to_vector(tup: Iterable[int], d: int) -> List[int]:
    """The element sum_i (a_i) of R_d as a coefficient vector indexed by a = 1..d-1."""
    v = [0] * (d - 1)
    for a in tup:
        a %= d
        if a == 0:
            raise ValueError("tuple entries must be nonzero mod d")
        v[a - 1] += 1
    return v


def fold(tup: Iterable[int], d: int) -> List[int]:
    """pi(sum_i (a_i)) in Z^h, h = floor((d-1)/2)."""
    h = (d - 1) // 2
    x = [0] * h
    for a in tup:
        a %= d
        if a == 0:
            raise ValueError("tuple entries must be nonzero mod d")
        if 2 * a < d:
            x[a - 1] += 1
        elif 2 * a > d:
            x[d - a - 1] -= 1
    return x


def lam(tup: Iterable[int], d: int) -> int:
    """The lambda-invariant of docs/attacks/17 (defined for d = 44, 51, 52)."""
    coeff = LAMBDA[d]
    return sum(coeff.get(a % d, 0) for a in tup)


def lift(tup: Iterable[int], d0: int, d: int) -> Tuple_:
    """Lift R_{d0} -> R_d, (a) -> (k a), k = d / d0."""
    if d % d0:
        raise ValueError("d0 must divide d")
    k = d // d0
    return tuple(sorted(k * (a % d0) for a in tup))


def act(t: int, tup: Iterable[int], d: int) -> Tuple_:
    return tuple(sorted((t * a) % d for a in tup))


def standard_tuples(d: int, units_only: bool = False) -> List[Tuple_]:
    """Aoki's standard tuples s_{p,i} (MMRV Def. 3.7) of every degree d' = p k dividing d with k >= 3, lifted to
    degree d.  s_{p,i} = (i, i+k, ..., i+(p-1)k, -p i) for odd p and (i, k+i, d'-2i, k) for p = 2.  The index i runs
    over the residues with p not dividing i and all entries nonzero (or over the units of Z/d' if units_only).
    Modulo D_d the two choices span the same lattice."""
    out = set()
    for d1 in range(1, d + 1):
        if d % d1:
            continue
        for p in prime_divisors(d1):
            k = d1 // p
            if k < 3:
                continue
            for i in range(1, d1):
                if units_only and gcd(i, d1) != 1:
                    continue
                if i % p == 0:
                    continue
                if p == 2:
                    s = (i, k + i, d1 - 2 * i, k)
                else:
                    s = tuple(i + j * k for j in range(p)) + (-p * i,)
                s = tuple(a % d1 for a in s)
                if any(a == 0 for a in s):
                    continue
                out.add(lift(s, d1, d))
    return sorted(out)


# ------------------------------------------------------------------------------------------- integer lattices

class Lattice:
    """A sublattice of Z^n, kept as a row-style Hermite basis {pivot column: row}.

    Insertion uses only unimodular row operations, so the basis always spans exactly the Z-span of the inserted
    vectors.  Rows are reduced modulo later pivots to keep the entries small."""

    def __init__(self, n: int, vectors: Iterable[Sequence[int]] = ()):
        self.n = n
        self.rows: Dict[int, List[int]] = {}
        for v in vectors:
            self.add(v)

    # -- construction
    def add(self, v: Sequence[int]) -> None:
        v = list(v)
        if len(v) != self.n:
            raise ValueError("wrong length")
        c = self._lead(v, 0)
        while c is not None:
            b = self.rows.get(c)
            if b is None:
                if v[c] < 0:
                    v = [-x for x in v]
                self.rows[c] = v
                self._reduce_row(c)
                self._reduce_others(c)
                return
            if v[c] % b[c] == 0:
                q = v[c] // b[c]
                v = [x - q * y for x, y in zip(v, b)]
            else:
                g, s, t = xgcd(b[c], v[c])
                vb, bb = v[c] // g, b[c] // g
                new = [s * y + t * x for x, y in zip(v, b)]
                v = [vb * y - bb * x for x, y in zip(v, b)]
                self.rows[c] = new
                self._reduce_row(c)
                self._reduce_others(c)
            c = self._lead(v, c + 1)

    @staticmethod
    def _lead(v: Sequence[int], start: int) -> Optional[int]:
        for i in range(start, len(v)):
            if v[i]:
                return i
        return None

    def _reduce_row(self, c: int) -> None:
        """Reduce the entries of row c modulo the pivots of later rows."""
        r = self.rows[c]
        for c2 in sorted(k for k in self.rows if k > c):
            b = self.rows[c2]
            q = r[c2] // b[c2]
            if q:
                r = [x - q * y for x, y in zip(r, b)]
        self.rows[c] = r

    def _reduce_others(self, c: int) -> None:
        """Reduce the entries in column c of earlier rows modulo the (new) pivot of row c."""
        b = self.rows[c]
        for c0 in sorted(k for k in self.rows if k < c):
            r = self.rows[c0]
            q = r[c] // b[c]
            if q:
                self.rows[c0] = [x - q * y for x, y in zip(r, b)]

    # -- queries
    def rank(self) -> int:
        return len(self.rows)

    def basis(self) -> List[List[int]]:
        return [self.rows[c] for c in sorted(self.rows)]

    def contains(self, v: Sequence[int]) -> bool:
        v = list(v)
        for c in sorted(self.rows):
            b = self.rows[c]
            if v[c] % b[c]:
                return False
            q = v[c] // b[c]
            if q:
                v = [x - q * y for x, y in zip(v, b)]
        return not any(v)

    def contains_lattice(self, other: "Lattice") -> bool:
        return all(self.contains(r) for r in other.basis())

    def elementary_divisors(self) -> List[int]:
        """Smith invariants of the basis matrix (rank many positive integers)."""
        return smith_invariants(self.basis())

    def is_saturated(self) -> bool:
        """Is Z^n / L torsion-free?"""
        return all(e == 1 for e in self.elementary_divisors())


def smith_invariants(rows: List[List[int]]) -> List[int]:
    """Nonzero Smith invariants of an integer matrix (plain elimination; fine for small matrices)."""
    M = [list(r) for r in rows if any(r)]
    out: List[int] = []
    while M:
        ncols = len(M[0])
        # pick the entry of smallest absolute value
        best = None
        for i, r in enumerate(M):
            for j, x in enumerate(r):
                if x and (best is None or abs(x) < abs(M[best[0]][best[1]])):
                    best = (i, j)
        if best is None:
            break
        i, j = best
        M[0], M[i] = M[i], M[0]
        for r in M:
            r[0], r[j] = r[j], r[0]
        p = M[0][0]
        done = True
        # clear column 0
        for i in range(1, len(M)):
            q = M[i][0] // p
            if q:
                M[i] = [x - q * y for x, y in zip(M[i], M[0])]
            if M[i][0]:
                done = False
        # clear row 0
        for j in range(1, ncols):
            q = M[0][j] // p
            if q:
                for r in M:
                    r[j] -= q * r[0]
            if M[0][j]:
                done = False
        if not done:
            continue
        # p must divide every remaining entry
        bad = None
        for i in range(1, len(M)):
            for j in range(1, ncols):
                if M[i][j] % p:
                    bad = i
                    break
            if bad is not None:
                break
        if bad is not None:
            M[0] = [x + y for x, y in zip(M[0], M[bad])]
            continue
        out.append(abs(p))
        M = [r[1:] for r in M[1:] if any(r[1:])]
    return out


def integer_kernel(A: List[List[int]], n: int) -> Lattice:
    """The lattice {x in Z^n : A x = 0} (A given by rows of length n), via the Hermite basis of [A^T | I]."""
    m = len(A)
    big = Lattice(m + n)
    for j in range(n):
        big.add([A[i][j] for i in range(m)] + [1 if k == j else 0 for k in range(n)])
    ker = Lattice(n)
    for c, row in big.rows.items():
        if c >= m:
            assert not any(row[:m])
            ker.add(row[m:])
    return ker


def hodge_lattice_folded(d: int) -> Lattice:
    """pi(B_d) = {x in Z^h : sum_a x_a (2 <t a>_d - d) = 0 for every unit t}."""
    h = (d - 1) // 2
    A = [[2 * ((t * a) % d) - d for a in range(1, h + 1)] for t in half_units(d)]
    return integer_kernel(A, h)


def rank_D(d: int) -> int:
    """rank of D_d = number of pairs {a, -a} plus [d even]."""
    return (d - 1) // 2 + (1 if d % 2 == 0 else 0)


def span_folded(tuples: Iterable[Sequence[int]], d: int) -> Lattice:
    return Lattice((d - 1) // 2, (fold(t, d) for t in tuples))


def index(sup: Lattice, sub: Lattice) -> int:
    """[sup : sub] for sub <= sup of equal rank."""
    if not sup.contains_lattice(sub):
        raise ValueError("not a sublattice")
    if sup.rank() != sub.rank():
        raise ValueError("ranks differ: index is infinite")
    num = 1
    for e in sub.elementary_divisors():
        num *= e
    den = 1
    for e in sup.elementary_divisors():
        den *= e
    assert num % den == 0
    return num // den


def is_multiset_identity(lhs: Sequence[Sequence[int]], rhs: Sequence[Sequence[int]], d: int) -> bool:
    """Do the joins of the tuples on each side agree as multisets of residues mod d?"""
    left = sorted(a % d for t in lhs for a in t)
    right = sorted(a % d for t in rhs for a in t)
    return left == right
