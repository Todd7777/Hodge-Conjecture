"""Tests for hodge/lifts.py: Proposition L1 and Theorem L2 of docs/fermat/05-lifts.md (lifting xi_q to degree 2q)."""
from collections import Counter

from hodge import formal_module as F
from hodge import lifts as LF
from hodge import two_prime as T


def odd_two_factor(qmax):
    return sorted(p1 * p2 for p1 in range(3, qmax) for p2 in range(p1 + 1, qmax)
                  if T.is_prime(p1) and T.is_prime(p2) and p1 * p2 <= qmax)


def test_pushdown_of_lift_is_xi():
    for q in (15, 35, 65, 77, 221):
        xi = T.shortest_tuple(q)
        assert LF.pushdown(F.lift(xi, q, 2 * q), q) == Counter(xi)


def test_pushdown_kills_pairs():
    q = 35
    for x in range(1, 2 * q):
        if x == q:
            continue
        c = LF.pushdown((x, 2 * q - x), q)
        assert all(n == c[(-a) % q] for a, n in c.items())      # a sum of pairs (a) + (-a)


def test_proposition_L1():
    # pi(S_{2q}) is contained in D_q + S_q (exact lattice check)
    for q in (15, 21, 33, 35, 39, 55, 65, 69):
        assert LF.pushdown_respects_standard(q), q


def test_doubling_bound_values():
    expected = {15: 3, 21: 3, 33: 4, 35: 5, 39: 3, 51: 6, 55: 5, 57: 6, 65: 9, 69: 7, 77: 9, 85: 10, 87: 9, 91: 12,
                93: 10, 95: 10, 111: 10}
    assert {q: LF.doubling_bound(q) for q in expected} == expected
    for q in expected:
        assert LF.doubling_bound(q) >= -(-T.predicted_length(q) // 2)


def test_doubling_never_reaches_six_beyond_57():
    small = [q for q in odd_two_factor(1000) if LF.doubling_bound(q) <= 6]
    assert small == [15, 21, 33, 35, 39, 51, 55, 57]


def test_doubled_representatives():
    for q, rep in LF.DOUBLED.items():
        D = 2 * q
        assert F.is_hodge_tuple(rep, D)
        # in the class of the lift of xi_q: rep - lift(xi_q) lies in D_D + S_D
        S = F.span_folded(F.standard_tuples(D), D)
        diff = [a - b for a, b in zip(F.fold(rep, D), F.fold(F.lift(T.shortest_tuple(q), q, D), D))]
        assert S.contains(diff), q
        assert len(rep) >= LF.doubling_bound(q)
