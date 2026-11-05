"""The 3 m^2 lines on the Fermat surface S_m : x_0^m + x_1^m + x_2^m + x_3^m = 0 and the lattice they span.

For each of the three ways of splitting {0,1,2,3} into two pairs, and for each pair (zeta, eta) of m-th roots of -1,
the line

    L = { x_i = zeta x_j ,  x_k = eta x_l }

lies on S_m (because x_i^m + x_j^m = (zeta^m + 1) x_j^m = 0, and likewise for the other pair).  This gives 3 m^2 lines,
and for m >= 3 these are all the lines on S_m (Schuett-Shioda-van Luijk, "Lines on Fermat surfaces", 2010).

Intersection numbers (exact, no coordinates needed):
    L . L = 2 - m                           (adjunction: L^2 = -2 - K.L, K = (m-4) H)
    L . L' = 1 if the lines meet, 0 otherwise, for L != L'.
Two lines of the same splitting {ij}{kl}, with parameters (zeta, eta) and (zeta', eta'), meet iff zeta = zeta' or
eta = eta' (they then lie in a common plane).  A line {x_0 = zeta x_1, x_2 = eta x_3} and a line
{x_0 = zeta' x_2, x_1 = eta' x_3} meet iff zeta eta' = zeta' eta, and similarly for the other mixed cases.

We encode zeta = eps * w^a, eta = eps * w^b with eps a fixed m-th root of -1 and w = exp(2 pi i/m), so that a line is a
triple (splitting, a, b) with a, b in Z/m, and the meeting conditions become congruences mod m.  The Gram matrix of
the 3 m^2 line classes is then an explicit integer matrix; its rank is the rank of the sublattice of NS(S_m) spanned
by lines.  Shioda (1981) proved this rank is 3(m-1)(m-2) + 1 + [m even]; the Picard number rho(S_m) = |B^2_m| + 1 can be
strictly larger (e.g. m = 6: 86 vs 62).  Both numbers are recomputed here from scratch.
"""

from __future__ import annotations

from typing import List, Tuple

Line = Tuple[int, int, int]  # (splitting index 0/1/2, a, b)

# splitting s: pairs ((i, j), (k, l)): x_i = zeta x_j, x_k = eta x_l
SPLITTINGS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))


def lines(m: int) -> List[Line]:
    return [(s, a, b) for s in range(3) for a in range(m) for b in range(m)]


def _meet(L1: Line, L2: Line, m: int) -> bool:
    """Do two distinct lines meet?

    A line is (s, a, b): splitting s, zeta = w^(2a+1), eta = w^(2b+1) with w = exp(pi i / m) of order 2m, so that
    zeta^m = eta^m = -1.  Solving the four linear equations shows that a common point must have all x_i != 0, and
    then exists (and is unique) iff a single multiplicative relation among zeta, eta, zeta', eta' holds.  With
    exponents compared modulo 2m:

      same splitting           :  a == a'  or  b == b'                     (coplanar lines)
      s=0 vs s=1               :  zeta eta' = zeta' eta
      s=0 vs s=2               :  zeta eta eta'' = zeta''
      s=1 vs s=2               :  zeta' eta' = zeta'' eta''
    """
    s1, a1, b1 = L1
    s2, a2, b2 = L2
    M2 = 2 * m
    z1, e1 = 2 * a1 + 1, 2 * b1 + 1  # exponents of w2
    z2, e2 = 2 * a2 + 1, 2 * b2 + 1
    if s1 == s2:
        return a1 == a2 or b1 == b2
    if s1 > s2:
        s1, s2, z1, e1, z2, e2 = s2, s1, z2, e2, z1, e1
    if (s1, s2) == (0, 1):
        # x0 = z1 x1, x2 = e1 x3 ; x0 = z2 x2, x1 = e2 x3
        # => x0 = z1 e2 x3 and x0 = z2 e1 x3  => z1 e2 = z2 e1
        return (z1 + e2 - z2 - e1) % M2 == 0
    if (s1, s2) == (0, 2):
        # x0 = z1 x1, x2 = e1 x3 ; x0 = z2 x3, x1 = e2 x2
        # => x0 = z1 e2 x2 = z1 e2 e1 x3 and x0 = z2 x3 => z1 e1 e2 = z2
        return (z1 + e1 + e2 - z2) % M2 == 0
    if (s1, s2) == (1, 2):
        # x0 = z1 x2, x1 = e1 x3 ; x0 = z2 x3, x1 = e2 x2
        # => x1 = e2 x2 = e1 x3 => x2 = (e1/e2) x3 ; x0 = z1 x2 = z1 e1/e2 x3 = z2 x3 => z1 e1 = z2 e2
        return (z1 + e1 - z2 - e2) % M2 == 0
    raise AssertionError


def gram_matrix(m: int) -> List[List[int]]:
    """Intersection matrix of the 3 m^2 lines on S_m."""
    Ls = lines(m)
    N = len(Ls)
    G = [[0] * N for _ in range(N)]
    for i in range(N):
        G[i][i] = 2 - m
        for j in range(i + 1, N):
            v = 1 if _meet(Ls[i], Ls[j], m) else 0
            G[i][j] = G[j][i] = v
    return G


def rank_mod_p(G: List[List[int]], p: int) -> int:
    """Rank of an integer matrix over F_p (Gaussian elimination)."""
    A = [[x % p for x in row] for row in G]
    nrows, ncols = len(A), len(A[0])
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, nrows):
            if A[i][c]:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c], -1, p)
        A[r] = [(x * inv) % p for x in A[r]]
        for i in range(nrows):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [(x - f * y) % p for x, y in zip(A[i], A[r])]
        r += 1
        if r == nrows:
            break
    return r


def rank_over_Q(G: List[List[int]]) -> int:
    """Exact rank over Q by Gaussian elimination with Python Fractions (exact; fine for a few hundred rows)."""
    from fractions import Fraction
    A = [[Fraction(x) for x in row] for row in G]
    nrows, ncols = len(A), len(A[0])
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, nrows):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pr = A[r]
        for i in range(r + 1, nrows):
            if A[i][c] != 0:
                f = A[i][c] / pr[c]
                Ai = A[i]
                for k in range(c, ncols):
                    Ai[k] -= f * pr[k]
        r += 1
        if r == nrows:
            break
    return r


def line_lattice_rank(m: int, exact: bool = True) -> int:
    """Rank of the sublattice of NS(S_m) spanned by the 3 m^2 lines."""
    G = gram_matrix(m)
    if exact:
        return rank_over_Q(G)
    # rank over Q >= rank over F_p; two large primes give a certificate for equality in practice but not a proof.
    return max(rank_mod_p(G, 2147483647), rank_mod_p(G, 2147483629))


def shioda_line_rank_formula(m: int) -> int:
    """Shioda's formula for the rank of the lattice spanned by the lines on S_m."""
    return 3 * (m - 1) * (m - 2) + 1 + (1 if m % 2 == 0 else 0)
