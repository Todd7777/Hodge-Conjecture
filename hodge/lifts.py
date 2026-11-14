"""Lifting the exceptional classes: how short can the lift of xi_q be in degree 2q?  See docs/fermat/05-lifts.md.

For q = p1 p2 odd, the push-down map

    pi : R_{2q} -> R_q,   (x) -> (u) + (-u/2)  for x odd, u = x mod q;   (2b) -> (b);   (q) -> 0

sends D_{2q} + S_{2q} into D_q + S_q (Proposition L1) and the lift of xi_q to xi_q.  The coset functionals of
Theorem T (hodge/two_prime.py) are therefore odd on pi(alpha') for every alpha' in lift(xi_q) + D_{2q} + S_{2q}.
An odd entry of alpha' meets two supports, C and 2^{-1}C, and an even entry meets one.  So every cycle of
C -> 2^{-1}C on the supports, of length o, needs at least ceil(o/2) entries (Theorem L2, `doubling_bound`).
"""

from __future__ import annotations

from collections import Counter
from typing import Dict, Iterable, Sequence

from . import formal_module as F
from . import two_prime as T


def pushdown(tup: Iterable[int], q: int) -> Counter:
    """pi(sum (x)) as residue counts in R_q (q odd).  Entries are residues mod 2q."""
    if q % 2 == 0:
        raise ValueError("q must be odd")
    inv2 = pow(2, -1, q)
    out: Counter = Counter()
    for x in tup:
        x %= 2 * q
        if x == 0 or x == q:
            continue
        if x % 2:
            u = x % q
            out[u] += 1
            out[(-u * inv2) % q] += 1
        else:
            out[(x // 2) % q] += 1
    return out


def fold_counts(c: Dict[int, int], q: int):
    v = [0] * ((q - 1) // 2)
    for a, n in c.items():
        for i, x in enumerate(F.fold((a,), q)):
            v[i] += n * x
    return v


def pushdown_respects_standard(q: int) -> bool:
    """Exact check of Proposition L1 for one q: every standard tuple of degree 2q (all degrees dividing 2q, lifted)
    maps into D_q + S_q."""
    S = F.span_folded(F.standard_tuples(q), q)
    return all(S.contains(fold_counts(pushdown(s, q), q)) for s in F.standard_tuples(2 * q))


def doubling_bound(q: int) -> int:
    """Theorem L2: l_{2,2q}(xi_q) >= sum over the cycles of C -> 2^{-1} C on the coset supports of ceil(len/2)."""
    funcs = T.coset_functionals(q)
    owner = {}
    for i, (_, s) in enumerate(funcs):
        for x in s:
            owner[x] = i
    inv2 = pow(2, -1, q)

    def step(i: int) -> int:
        x = next(iter(funcs[i][1]))
        return owner[(-x * inv2) % q]

    seen, total = set(), 0
    for i in range(len(funcs)):
        if i in seen:
            continue
        length, j = 0, i
        while j not in seen:
            seen.add(j)
            length += 1
            j = step(j)
        total += (length + 1) // 2
    return total


# Shortest representatives in degree 2q of the lifted class, found by the MILP of scripts/lift_lengths.py and verified
# exactly (tests/test_lifts.py).  For q = 35, 55, 57 they have length <= 6, which is how MMRV settle these degrees.
DOUBLED: Dict[int, Sequence[int]] = {
    35: (13, 23, 32, 36, 50, 56),
    55: (3, 23, 53, 93, 103),
    57: (6, 41, 47, 53, 83, 112),
    65: (17, 20, 27, 37, 57, 78, 88, 97, 105, 124),
    69: (16, 17, 46, 59, 70, 94, 99, 101, 119),
}
