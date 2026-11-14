"""Exceptional lengths for q = p1 p2, a product of two odd primes: coset parity invariants and the formula

    f_0(q) = phi(q)/4 + c_{p1}(p2) + c_{p2}(p1),   c_r(p) = (p - 1)/ord_p(r) if ord_p(r) is even, else 0,

proved for all distinct odd primes p1, p2 in docs/fermat/02-exceptional-lengths.md section 6 (Theorem F); with 4 or 3 in
place of p1 it is Theorems D and D'.

The lower bound comes from mod-2 functionals that count the entries in one coset:
  * units in one coset of H = {t : t^2 = 1} (|H| = 4), giving phi(q)/4 cosets;
  * entries p1*y with y in one coset of <p1> in (Z/p2)^x, when ord_{p2}(p1) is even (then -1 is in <p1>), giving
    c_{p1}(p2) cosets; and symmetrically for p2.
They vanish mod 2 on D_q + S_q (Proposition F1) and are odd on Aoki's xi_q, built from any half systems (`aoki_xi`,
`xi_from_half_systems`; Propositions F2, F3).  So every element of the class has a nonzero coefficient sum on every
coset, and its length is at least the number of cosets.  `shortest_tuple` (half systems adapted to the cycles,
Proposition F4) attains it.  `verify` re-checks all of this exactly for a given q and representative.
"""

from __future__ import annotations

from math import gcd
from typing import Dict, FrozenSet, List, Sequence, Tuple

from . import formal_module as F


def is_prime(n: int) -> bool:
    return n >= 2 and all(n % k for k in range(2, int(n ** 0.5) + 1))


def mult_order(r: int, p: int) -> int:
    k, x = 1, r % p
    while x != 1:
        x = x * r % p
        k += 1
    return k


def c_term(r: int, p: int) -> int:
    o = mult_order(r, p)
    return (p - 1) // o if o % 2 == 0 else 0


def factor(q: int) -> Tuple[int, int]:
    """(p1, p2) with q = p1 p2, 3 <= p1 < p2 primes.  (p1 = 3 is the family of Theorem D' and serves as a check.)"""
    for p1 in range(3, int(q ** 0.5) + 1):
        if q % p1 == 0 and is_prime(p1) and is_prime(q // p1) and q // p1 != p1:
            return p1, q // p1
    raise ValueError(f"{q} is not a product of two distinct odd primes")


def predicted_length(q: int) -> int:
    p1, p2 = factor(q)
    return (p1 - 1) * (p2 - 1) // 4 + c_term(p1, p2) + c_term(p2, p1)


def coset_functionals(q: int) -> List[Tuple[str, FrozenSet[int]]]:
    """The supports (sets of residues mod q) of the coset-counting functionals."""
    p1, p2 = factor(q)
    G = [t for t in range(1, q) if gcd(t, q) == 1]
    H = [t for t in G if t * t % q == 1]
    out, seen = [], set()
    for t in G:
        if t in seen:
            continue
        coset = frozenset(t * h % q for h in H)
        seen |= coset
        out.append((f"units {min(coset)}H", coset))
    for a, b in ((p1, p2), (p2, p1)):
        if mult_order(a, b) % 2:
            continue
        sub = {pow(a, k, b) for k in range(mult_order(a, b))}
        seen = set()
        for y in range(1, b):
            if y in seen:
                continue
            coset = {y * s % b for s in sub}
            seen |= coset
            out.append((f"{a}*({min(coset)}<{a}> mod {b})", frozenset(a * z % q for z in coset)))
    return out


def count(support: FrozenSet[int], element: Sequence[int], q: int) -> int:
    return sum(1 for x in element if x % q in support)


def verify(q: int, representative: Sequence[int]) -> Dict[str, object]:
    """Exact check of the lower bound and of the representative.

    Returns a dict with: functionals (number), kills_D (supports closed under negation), kills_S (every standard tuple
    of every degree dividing q has an even count on every support), odd_on_rep, rep_hodge, rep_outside (the
    representative is not in D_q + S_q, an exact lattice check), length (of the representative), bound (number of
    functionals).  When all flags hold and length == bound, l_{2,q}(representative) = bound."""
    funcs = coset_functionals(q)
    supports = [s for _, s in funcs]
    kills_D = all(frozenset((-x) % q for x in s) == s for s in supports)
    std = F.standard_tuples(q)
    kills_S = all(count(s, t, q) % 2 == 0 for s in supports for t in std)
    odd_on_rep = all(count(s, representative, q) % 2 == 1 for s in supports)
    S = F.span_folded(std, q)
    return {
        "functionals": len(funcs),
        "kills_D": kills_D,
        "kills_S": kills_S,
        "odd_on_rep": odd_on_rep,
        "rep_hodge": F.is_hodge_tuple(representative, q),
        "rep_outside": not S.contains(F.fold(representative, q)),
        "length": len(representative),
        "bound": len(funcs),
    }


# Shortest representatives of xi_q for every q = p1 p2 <= 300 (p1 >= 5), found by the MILP of
# scripts/two_prime_lengths.py and verified exactly by `verify` (tests/test_two_prime.py, results/two_prime_lengths.md).
# Each has length phi(q)/4 + c_{p1}(p2) + c_{p2}(p1): one entry in each coset of every coset functional, and nothing else.
REPRESENTATIVES: Dict[int, Tuple[int, ...]] = {
    35: (3, 8, 9, 14, 23, 24, 29, 30),
    55: (4, 9, 12, 14, 27, 34, 37, 42, 47, 49),
    65: (1, 2, 7, 15, 20, 22, 27, 31, 36, 40, 41, 46, 52, 57, 61, 62),
    77: (5, 12, 13, 19, 24, 27, 34, 38, 40, 41, 45, 52, 62, 63, 68, 73),
    85: (1, 3, 11, 18, 21, 26, 28, 38, 41, 43, 46, 58, 63, 66, 68, 71, 80, 83),
    91: (2, 9, 13, 18, 20, 23, 27, 28, 39, 41, 44, 46, 48, 53, 62, 65, 67, 72, 74, 79, 83, 88),
    95: (4, 7, 9, 17, 19, 24, 39, 42, 44, 47, 49, 54, 57, 62, 64, 74, 77, 82, 87, 92),
    115: (7, 9, 12, 19, 22, 29, 32, 42, 44, 49, 52, 55, 59, 64, 67, 69, 72, 82, 84, 87, 99, 104, 107, 114),
    119: (2, 3, 9, 10, 16, 29, 36, 37, 38, 43, 44, 45, 50, 71, 72, 78, 79, 80, 85, 87, 94, 101, 105, 106, 113, 114),
    133: (2, 4, 6, 9, 11, 20, 23, 25, 30, 39, 41, 44, 58, 60, 79, 83, 90, 95, 97, 102, 104, 109, 116, 118, 121,
         123, 125, 128),
    143: (2, 4, 5, 13, 15, 16, 30, 38, 41, 43, 46, 54, 57, 59, 68, 70, 81, 82, 85, 90, 93, 96, 98, 103, 107, 109,
         120, 121, 129, 134, 137, 142),
    145: (1, 2, 6, 16, 17, 21, 22, 31, 32, 35, 46, 47, 51, 60, 61, 67, 76, 87, 92, 96, 97, 102, 112, 116, 117, 121,
         122, 126, 131, 132, 137, 141),
    155: (1, 3, 11, 13, 23, 33, 36, 41, 46, 48, 53, 56, 58, 63, 73, 81, 86, 96, 98, 103, 106, 108, 116, 118, 126,
         141, 143, 146, 148, 151),
    161: (2, 8, 11, 16, 18, 22, 25, 29, 37, 39, 43, 57, 60, 64, 65, 71, 79, 85, 88, 91, 100, 102, 106, 114, 121,
         123, 134, 135, 137, 144, 148, 149, 156, 158),
    185: (1, 3, 8, 11, 16, 18, 31, 33, 38, 46, 48, 51, 53, 61, 68, 81, 83, 88, 91, 98, 101, 105, 116, 118, 126,
         128, 136, 138, 146, 148, 151, 153, 156, 163, 166, 173, 181, 183),
    187: (9, 15, 26, 30, 31, 32, 41, 43, 48, 49, 52, 60, 63, 64, 65, 74, 75, 81, 82, 86, 92, 97, 98, 103, 108, 109,
         114, 115, 119, 120, 125, 126, 131, 137, 142, 148, 151, 159, 162, 176, 184, 185),
    203: (2, 3, 16, 17, 20, 23, 24, 30, 31, 45, 48, 52, 59, 65, 69, 72, 79, 83, 90, 94, 101, 104, 107, 108, 111,
         118, 132, 135, 136, 139, 146, 156, 164, 170, 177, 181, 185, 188, 191, 195, 198, 199),
    205: (1, 3, 6, 13, 23, 33, 43, 46, 51, 53, 56, 58, 61, 66, 68, 71, 83, 86, 88, 91, 101, 105, 116, 126, 128,
         133, 136, 138, 140, 143, 146, 148, 153, 156, 166, 168, 173, 176, 181, 183, 191, 198),
    209: (8, 12, 18, 27, 29, 31, 34, 38, 40, 41, 51, 52, 53, 56, 60, 67, 71, 75, 78, 84, 86, 89, 97, 107, 108, 117,
         122, 126, 128, 129, 141, 148, 151, 155, 162, 166, 170, 173, 174, 181, 183, 184, 185, 192, 203, 205),
    215: (3, 4, 9, 14, 18, 19, 38, 43, 49, 53, 55, 58, 63, 64, 73, 78, 88, 89, 93, 98, 103, 104, 113, 118, 124,
         128, 133, 138, 139, 143, 144, 148, 149, 159, 164, 174, 178, 179, 184, 189, 193, 199, 204, 214),
    217: (3, 6, 13, 17, 23, 24, 27, 30, 31, 34, 37, 44, 48, 52, 55, 58, 65, 73, 79, 83, 86, 104, 108, 114, 115,
         122, 135, 136, 139, 146, 150, 153, 167, 170, 177, 178, 181, 184, 185, 192, 198, 199, 209, 212, 213, 216),
    221: (9, 12, 13, 15, 16, 26, 29, 31, 33, 44, 46, 48, 57, 61, 64, 65, 67, 68, 74, 77, 80, 81, 83, 91, 94, 98,
         100, 111, 116, 129, 132, 133, 135, 142, 145, 146, 148, 150, 152, 159, 163, 165, 168, 176, 184, 185, 187,
         197, 200, 202, 210, 213, 217, 220),
    235: (1, 8, 11, 13, 18, 21, 23, 31, 41, 43, 48, 56, 58, 61, 66, 68, 78, 88, 91, 103, 106, 108, 111, 113, 121,
         126, 131, 138, 146, 150, 153, 158, 166, 168, 173, 178, 181, 186, 188, 193, 196, 201, 206, 211, 213, 228,
         231, 233),
    247: (1, 10, 14, 23, 32, 35, 36, 39, 48, 49, 54, 58, 61, 67, 71, 73, 74, 80, 86, 87, 88, 92, 93, 99, 105, 106,
         112, 118, 125, 126, 127, 131, 144, 145, 149, 153, 162, 164, 165, 166, 175, 183, 184, 188, 191, 201, 203,
         204, 209, 210, 222, 223, 229, 240, 242, 244),
    253: (2, 3, 12, 14, 15, 17, 25, 26, 35, 37, 39, 45, 48, 56, 58, 61, 68, 72, 79, 81, 83, 88, 91, 94, 102, 111,
         114, 125, 127, 133, 134, 155, 156, 157, 160, 171, 177, 178, 179, 180, 199, 200, 201, 202, 210, 221, 222,
         223, 224, 226, 232, 233, 244, 245, 246, 248),
    259: (1, 8, 9, 16, 22, 23, 43, 44, 46, 50, 53, 60, 71, 72, 79, 81, 86, 93, 100, 107, 109, 116, 120, 121, 123,
         127, 128, 130, 134, 137, 144, 149, 155, 156, 158, 165, 170, 183, 186, 190, 191, 193, 197, 198, 204, 207,
         211, 218, 219, 228, 232, 235, 239, 256),
    265: (1, 7, 12, 17, 22, 26, 32, 37, 42, 47, 51, 56, 57, 62, 66, 67, 71, 72, 76, 77, 96, 107, 111, 121, 126,
         131, 132, 151, 157, 162, 166, 171, 172, 176, 177, 181, 182, 191, 196, 201, 202, 206, 212, 216, 217, 221,
         226, 227, 230, 231, 232, 236, 237, 257),
    287: (3, 5, 10, 19, 24, 26, 29, 33, 40, 45, 59, 66, 68, 71, 73, 75, 80, 82, 85, 87, 92, 101, 103, 106, 108,
         110, 112, 115, 117, 122, 127, 141, 148, 150, 152, 155, 157, 162, 164, 169, 183, 185, 190, 192, 194, 197,
         199, 204, 208, 215, 229, 232, 234, 239, 246, 250, 264, 267, 271, 274, 276, 278, 281, 285),
    295: (6, 8, 11, 13, 18, 23, 31, 33, 38, 43, 56, 58, 61, 73, 83, 91, 93, 96, 98, 101, 103, 106, 111, 113, 118,
         126, 128, 131, 136, 141, 148, 151, 156, 158, 161, 168, 173, 176, 183, 188, 191, 201, 208, 211, 216, 221,
         231, 233, 236, 238, 246, 266, 268, 273, 276, 278, 283, 286, 288, 291),
    299: (7, 15, 17, 20, 21, 28, 30, 33, 34, 38, 42, 43, 51, 56, 60, 67, 68, 80, 86, 90, 99, 103, 106, 107, 111,
         112, 120, 125, 129, 132, 134, 137, 138, 145, 155, 158, 159, 160, 168, 171, 172, 176, 181, 189, 194, 198,
         199, 203, 207, 212, 224, 228, 229, 237, 241, 249, 250, 251, 263, 264, 267, 268, 272, 275, 281, 290, 293,
         298),
}


def primitive_root(p: int) -> int:
    for g in range(2, p):
        if all(pow(g, (p - 1) // r, p) != 1 for r in range(2, p) if (p - 1) % r == 0 and is_prime(r)):
            return g
    raise ValueError(p)


def half_system(p: int) -> List[int]:
    """{mu^i : 0 <= i < (p-1)/2} for the least primitive root mu: one element from each pair {x, -x} mod p."""
    g = primitive_root(p)
    return [pow(g, i, p) for i in range((p - 1) // 2)]


def aoki_xi(q: int) -> Tuple[int, ...]:
    """Aoki's exceptional element xi_q (MMRV Definition 4.8) for q = p1 p2, as a tuple representing its class in R_q/D_q.

    Primitive part: the units x with x mod p1 in hs(p1) and x mod p2 in hs(p2) (one unit in each coset of H).
    p1-part: the solution of (p1 - 1) xi_{q,p1} = tau_{p1}(xi_{q,1}) in R_{p2}/D_{p2}.  Modulo D it is the sum of (w)_{p2}
    over the w = p1^{-1} y with y in hs(p2) and w in -hs(p2) (a sign change), lifted to the entries p1 w of R_q.  The
    p2-part is symmetric.  (Read with the opposite sign of tau, the result is not Hodge; this sign makes it Hodge, as
    MMRV Prop. 4.2 requires, and reproduces MMRV's representative of xi_35.  `is_hodge_tuple` checks it.)"""
    p1, p2 = factor(q)
    h1, h2 = half_system(p1), half_system(p2)
    out = []
    for a in h1:
        for b in h2:
            out.append(next(x for x in range(1, q) if x % p1 == a and x % p2 == b))
    for (a, b, hb) in ((p1, p2, h2), (p2, p1, h1)):
        inv = pow(a, -1, b)
        hset = set(hb)
        for y in hb:
            w = inv * y % b
            if w not in hset:                     # p^{-1} y in -hs: a sign change
                out.append(a * w % q)
    return tuple(sorted(out))


def adapted_half_system(p: int, r: int) -> List[int]:
    """A half system mod p adapted to multiplication by r^{-1}: on each cycle of <r> of even length o, the half-cycle
    w_0, w_1, ..., w_{o/2 - 1} (w_k = r^{-k} w_0); for cycles of odd length (then -C != C), all of C and nothing of -C."""
    inv = pow(r, -1, p)
    o = mult_order(r, p)
    chosen, seen = [], set()
    for w0 in range(1, p):
        if w0 in seen:
            continue
        cyc = [w0]
        while len(cyc) < o:
            cyc.append(cyc[-1] * inv % p)
        seen |= set(cyc)
        if o % 2 == 0:
            chosen += cyc[: o // 2]
        else:
            seen |= {(-w) % p for w in cyc}          # the cycle -C is left out entirely
            chosen += cyc
    assert len(chosen) == (p - 1) // 2 and len({x for c in chosen for x in (c, p - c)}) == p - 1
    return sorted(chosen)


def xi_from_half_systems(q: int, h1: Sequence[int], h2: Sequence[int]) -> Tuple[int, ...]:
    """The element xi'_q built from arbitrary half systems h1 mod p1 and h2 mod p2 (section 6: Propositions F2 and F3
    hold for every choice)."""
    p1, p2 = factor(q)
    out = [next(x for x in range(1, q) if x % p1 == a and x % p2 == b) for a in h1 for b in h2]
    for (a, b, hb) in ((p1, p2, h2), (p2, p1, h1)):
        inv = pow(a, -1, b)
        hset = set(hb)
        for y in hb:
            w = inv * y % b
            if w not in hset:
                out.append(a * w % q)
    return tuple(sorted(out))


def shortest_tuple(q: int) -> Tuple[int, ...]:
    """An explicit shortest representative of xi_q (Theorem F): xi'_q with half systems adapted to the cycles."""
    p1, p2 = factor(q)
    return xi_from_half_systems(q, adapted_half_system(p1, p2), adapted_half_system(p2, p1))
