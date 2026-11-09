"""Lengths of Aoki's exceptional tuples xi_q for q = 4p (p = 3 mod 4) and q = 3p (p = 2 mod 3).

Companion to docs/fermat/02-exceptional-lengths.md, which proves (Theorem D there):

    l_{2,q}(xi_q) = f_0(q) = (p + 1)/2 + c_r(p),   r = 2 if q = 4p,  r = 3 if q = 3p,
    c_r(p) = (p - 1)/ord_p(r) if ord_p(r) is even, and 0 if ord_p(r) is odd.

Here l_{2,q} is the length modulo linear and standard tuples of degree q and f_0(q) = min{l_{2,q}(a) : a in
B_q \\ (D_q + S_q)}, as in Miranda-Movasati-Rufino-Villaflor (arXiv:2609.27301, section 4.3).  The lower bound comes from
the character-sum identity (p - 1) lambda + 2 U = 0 on B_q, where lambda = n_p - n_{(m-1)p} counts the entries of order m
and U = sum of chi_m over the unit entries; the upper bound is the explicit tuple built by `minimal_tuple`.

This module only builds the objects and evaluates the invariants; the proofs are in the note, and the checks are in
tests/test_exceptional_length.py and scripts/exceptional_lengths.py.
"""

from __future__ import annotations

from math import gcd
from typing import List, Tuple

from . import formal_module as F


def is_prime(n: int) -> bool:
    return n > 1 and all(n % k for k in range(2, int(n ** 0.5) + 1))


def mult_order(r: int, p: int) -> int:
    k, x = 1, r % p
    while x != 1:
        x = x * r % p
        k += 1
    return k


def family(q: int) -> Tuple[int, int]:
    """(m, p) if q = m p is in one of the two families (m = 4, p = 3 mod 4 prime; m = 3, p = 2 mod 3 prime, p > 3),
    else raise ValueError."""
    for m in (4, 3):
        if q % m == 0:
            p = q // m
            if is_prime(p) and p != m and p % m == m - 1 and not (m == 3 and p == 2):
                return m, p
    raise ValueError(f"{q} is not of the form 4p (p = 3 mod 4) or 3p (p = 2 mod 3)")


def family_degrees(qmax: int) -> List[int]:
    out = []
    for q in range(3, qmax + 1):
        try:
            family(q)
            out.append(q)
        except ValueError:
            pass
    return out


def chi(m: int, a: int) -> int:
    """The odd quadratic character of conductor m in {3, 4}."""
    a %= m
    if m == 4:
        return {1: 1, 3: -1}.get(a, 0)
    return {1: 1, 2: -1}.get(a, 0)


def lam(tup, q: int) -> int:
    """lambda_q = n_p - n_{(m-1)p}: signed count of the entries of exact order m (for q = 44 this is lambda_44)."""
    m, p = family(q)
    return sum(1 for a in tup if a % q == p) - sum(1 for a in tup if a % q == (m - 1) * p)


def U(tup, q: int) -> int:
    """sum of chi_m over the entries that are units mod q."""
    m, _ = family(q)
    return sum(chi(m, a) for a in tup if gcd(a, q) == 1)


def predicted_length(q: int) -> int:
    m, p = family(q)
    r = 2 if m == 4 else 3
    o = mult_order(r, p)
    return (p + 1) // 2 + (0 if o % 2 else (p - 1) // o)


def minimal_tuple(q: int) -> Tuple[int, ...]:
    """An explicit Hodge tuple of degree q with lambda_q = -1 and length predicted_length(q).

    Units u = 1 mod m whose residues mod p form a set H containing exactly one of x, -x for every x; one entry
    (m-1)p of order m; and, when -1 lies in <r> mod p, one entry (q/p) w of order p for each coset w<r>, with H meeting
    that coset in the 'half cycle' {r w, r^2 w, ..., r^(o/2) w} (o = ord_p(r))."""
    m, p = family(q)
    r = 2 if m == 4 else 3
    o = mult_order(r, p)

    def unit(x: int) -> int:
        return next(u for u in range(x % p, q, p) if u % m == 1)

    out = [(m - 1) * p]
    seen = set()
    for w in range(1, p):
        if w in seen:
            continue
        coset = [w * pow(r, j, p) % p for j in range(o)]
        if o % 2:
            seen.update(coset)
            seen.update((-y) % p for y in coset)
            out += [unit(y) for y in coset]
        else:
            seen.update(coset)
            out += [unit(w * pow(r, j, p) % p) for j in range(1, o // 2 + 1)]
            out.append((q // p) * w % q)
    return tuple(sorted(out))


def check_identity_on_B(q: int) -> bool:
    """(p - 1) lambda + 2 U vanishes on a lattice basis of pi(B_q), hence on B_q (both functionals kill D_q)."""
    m, p = family(q)
    B = F.hodge_lattice_folded(q)
    for x in B.basis():
        # in folded coordinates: lambda = x_p, U = sum_{a < q/2, a unit} chi_m(a) x_a
        lam_x = x[p - 1]
        u_x = sum(chi(m, a) * x[a - 1] for a in range(1, (q - 1) // 2 + 1) if gcd(a, q) == 1)
        if (p - 1) * lam_x + 2 * u_x:
            return False
    return True


def standard_lambda_values(q: int) -> List[int]:
    return sorted({lam(s, q) for s in F.standard_tuples(q)})


def index_B_over_DS(q: int) -> int:
    B = F.hodge_lattice_folded(q)
    S = F.span_folded(F.standard_tuples(q), q)
    return F.index(B, S)
