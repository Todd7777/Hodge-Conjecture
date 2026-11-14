"""Lengths of Aoki's exceptional tuples xi_q for q = 4p (p an odd prime) and q = 3p (p a prime >= 5).

Companion to docs/fermat/02-exceptional-lengths.md, which proves (Theorem D there):

    l_{2,q}(xi_q) = f_0(q) = (p - chi_m(p))/2 + c_r(p),   (m, r) = (4, 2) if q = 4p,  (3, 3) if q = 3p,
    c_r(p) = (p - 1)/ord_p(r) if ord_p(r) is even, and 0 if ord_p(r) is odd,

with chi_m the odd quadratic character of conductor m.  The case chi_m(p) = -1 uses the invariant lambda (signed count
of the entries of order m); the case chi_m(p) = +1 uses lambda' = g(1) + g(-1) (signed count of the unit entries
congruent to +-1 mod p, with signs chi_m).

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


def family(q: int, both: bool = False) -> Tuple[int, int]:
    """(m, p) if q = m p is in the family of Theorem D.  By default only the original class chi_m(p) = -1
    (m = 4, p = 3 mod 4; m = 3, p = 2 mod 3, p > 3); with both=True also chi_m(p) = +1 (any odd prime p != m,
    p != 3).  Raise ValueError otherwise."""
    for m in (4, 3):
        if q % m == 0:
            p = q // m
            if not (is_prime(p) and p % 2 and p != m and p != 3 or (m == 4 and p == 3)):
                continue
            if both or p % m == m - 1:
                return m, p
    raise ValueError(f"{q} is not of the form 4p or 3p required here")


def family_degrees(qmax: int, both: bool = False) -> List[int]:
    out = []
    for q in range(3, qmax + 1):
        try:
            family(q, both)
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
    m, p = family(q, both=True)
    return sum(1 for a in tup if a % q == p) - sum(1 for a in tup if a % q == (m - 1) * p)


def lam_prime(tup, q: int) -> int:
    """lambda'_q = g(1) + g(-1): sum of chi_m over the unit entries congruent to +-1 mod p (for q = 52 this is the
    invariant lambda_52 = n_1 + n_25 - n_27 - n_51 of Attack 17)."""
    m, p = family(q, both=True)
    return sum(chi(m, a) for a in tup if gcd(a, q) == 1 and a % p in (1, p - 1))


def parity_invariant(tup, q: int) -> int:
    """The invariant whose parity detects xi_q: lambda if chi_m(p) = -1, lambda' if chi_m(p) = +1."""
    m, p = family(q, both=True)
    return lam(tup, q) if chi(m, p) == -1 else lam_prime(tup, q)


def U(tup, q: int) -> int:
    """sum of chi_m over the entries that are units mod q."""
    m, _ = family(q, both=True)
    return sum(chi(m, a) for a in tup if gcd(a, q) == 1)


def predicted_length(q: int) -> int:
    m, p = family(q, both=True)
    r = 2 if m == 4 else 3
    o = mult_order(r, p)
    return (p - chi(m, p)) // 2 + (0 if o % 2 else (p - 1) // o)


def minimal_tuple(q: int) -> Tuple[int, ...]:
    """An explicit Hodge tuple of degree q of length predicted_length(q) whose parity invariant is odd.

    Units u = 1 mod m whose residues mod p form a set H containing exactly one of x, -x for every x; when
    chi_m(p) = -1, one entry (m-1)p of order m (then lambda = -1; otherwise lambda' = 1); and, when -1 lies in <r>
    mod p, one entry (q/p) w of order p for each coset w<r>, with H meeting that coset in the 'half cycle'
    {r w, r^2 w, ..., r^(o/2) w} (o = ord_p(r))."""
    m, p = family(q, both=True)
    r = 2 if m == 4 else 3
    o = mult_order(r, p)

    def unit(x: int) -> int:
        return next(u for u in range(x % p, q, p) if u % m == 1)

    out = [(m - 1) * p] if chi(m, p) == -1 else []
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
    """The identities of Propositions 3/4 (chi_m(p) = -1) or 3'/4' (chi_m(p) = +1) on a lattice basis of B_q.
    chi_m(p) = -1: (p - 1) lambda + 2 U = 0.   chi_m(p) = +1: lambda = 0 and g(x) + g(-x) is independent of x."""
    m, p = family(q, both=True)
    B = F.hodge_lattice_folded(q)
    for x in B.basis():
        lam_x = x[p - 1]                                     # folded coordinate of a = p
        if chi(m, p) == -1:
            u_x = sum(chi(m, a) * x[a - 1] for a in range(1, (q - 1) // 2 + 1) if gcd(a, q) == 1)
            if (p - 1) * lam_x + 2 * u_x:
                return False
        else:
            if lam_x:
                return False
            g = [0] * p
            for a, c in enumerate(x, start=1):               # folded: c * ((a) - (q - a))
                if c and gcd(a, q) == 1:
                    g[a % p] += c * chi(m, a)
                    g[(-a) % p] -= c * chi(m, q - a)
            if len({g[t] + g[(-t) % p] for t in range(1, p)}) != 1:
                return False
    return True


def standard_lambda_values(q: int) -> List[int]:
    return sorted({parity_invariant(s, q) for s in F.standard_tuples(q)})


def index_B_over_DS(q: int) -> int:
    B = F.hodge_lattice_folded(q)
    S = F.span_folded(F.standard_tuples(q), q)
    return F.index(B, S)
