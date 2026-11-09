"""Independent re-verification of Theorems A-C of docs/attacks/17-fermat-open-cases.md.

hodge.formal_module shares no code with scripts/fermat_formal_module.py (python-flint) or scripts/fermat_span/ (PARI);
every number below was first obtained there and is recomputed here in pure Python."""
from math import factorial
from collections import Counter

import pytest

from hodge import formal_module as F

RANK_B = {44: 33, 51: 34, 52: 39}
SHORT_COUNTS = {44: (293, 3164), 51: (341, 3341), 52: (399, 4884)}   # sorted Hodge tuples of length 4 and 6


@pytest.fixture(scope="module", params=[44, 51, 52])
def degree_data(request):
    d = request.param
    T = {L: F.hodge_tuples(d, L) for L in range(2, 7)}
    return d, T, F.hodge_lattice_folded(d)


def test_lattice_helpers_on_a_small_example():
    L = F.Lattice(3, [[2, 4, 6], [3, 6, 9]])
    assert L.rank() == 1 and L.contains([1, 2, 3]) and not L.contains([1, 2, 4])
    assert F.smith_invariants([[2, 0], [0, 6]]) == [2, 6]
    K = F.integer_kernel([[1, 1, 1]], 3)
    assert K.rank() == 2 and K.contains([1, -1, 0]) and K.is_saturated()


def test_hodge_tuple_enumeration_matches_brute_force():
    from itertools import combinations_with_replacement
    for d, L in ((12, 4), (15, 4), (20, 3), (9, 6)):
        brute = [t for t in combinations_with_replacement(range(1, d), L) if F.is_hodge_tuple(t, d)]
        assert F.hodge_tuples(d, L) == brute


def test_theorem_A1_rank_and_counts(degree_data):
    d, T, B = degree_data
    assert B.rank() + F.rank_D(d) == RANK_B[d]
    assert (len(T[4]), len(T[6])) == SHORT_COUNTS[d]


def test_theorem_A2_lambda_vanishes_on_short_hodge_tuples(degree_data):
    d, T, _ = degree_data
    for L, tuples in T.items():
        assert all(F.lam(t, d) == 0 for t in tuples), (d, L)


def test_theorem_A3_exceptional_character(degree_data):
    d, _, _ = degree_data
    alpha = F.EXCEPTIONAL[d]
    assert F.is_hodge_tuple(alpha, d)
    assert F.lam(alpha, d) == {44: -1, 51: -1, 52: 1}[d]


def test_theorem_A4_surfaces_and_points_span_the_kernel_of_lambda(degree_data):
    """pi(B^2_d) is saturated of corank 1 in pi(B_d); with lambda(alpha_d) = +-1 this gives
    ker(lambda | B_d) = D_d + B^2_d and B_d = Z alpha_d + D_d + B^2_d."""
    d, T, B = degree_data
    B2 = F.span_folded(T[4], d)
    assert B.contains_lattice(B2)
    assert B2.rank() == B.rank() - 1
    assert B2.is_saturated()
    everything_short = F.span_folded([t for L in T for t in T[L]], d)
    assert B2.contains_lattice(everything_short)                 # in particular B^4_d is inside D_d + B^2_d
    with_alpha = F.Lattice(B.n, B2.basis() + [F.fold(F.EXCEPTIONAL[d], d)])
    assert with_alpha.contains_lattice(B) and B.contains_lattice(with_alpha)


def test_theorem_A5_lambda_52_is_chi4_equivariant():
    d = 52
    B = F.hodge_lattice_folded(d)
    chi4 = {1: 1, 3: -1}
    for x in B.basis():
        # lift the folded vector back to a tuple-like element of R_52: entries a < 26 with multiplicity x_a
        lam_x = x[0] + x[24]                                     # lambda_52 = x_1 + x_25 in folded coordinates
        for t in F.units(d):
            y = [0] * len(x)
            for a, c in enumerate(x, start=1):
                b = (t * a) % d
                if 2 * b < d:
                    y[b - 1] += c
                else:
                    y[d - b - 1] -= c
            assert y[0] + y[24] == chi4[t % 4] * lam_x


def test_theorem_A6_index_two_and_standard_parity(degree_data):
    d, _, B = degree_data
    S = F.span_folded(F.standard_tuples(d), d)
    assert F.index(B, S) == 2
    assert F.index(B, F.span_folded(F.standard_tuples(d, units_only=True), d)) == 2
    assert {F.lam(s, d) for s in F.standard_tuples(d)} == {-2, 0, 2}
    assert all(S.contains([2 * c for c in row]) for row in B.basis())


def test_proposition_3_2_kang_free_certificates():
    certs = {44: ([(1, 12, 23, 26, 34, 36), (4, 20, 21, 43), (8, 18, 22, 40), (10, 22, 24, 32)],
                  [(1, 43), (4, 40), (8, 36), (10, 34), (12, 32), (18, 26), (20, 24), (21, 23), (22, 22)]),
             52: ([(1, 14, 27, 30, 40, 44), (4, 24, 25, 51), (8, 22, 26, 48), (12, 26, 28, 38)],
                  [(1, 51), (4, 48), (8, 44), (12, 40), (14, 38), (22, 30), (24, 28), (25, 27), (26, 26)])}
    for d, (lhs, rhs) in certs.items():
        assert F.is_multiset_identity(lhs, rhs, d)
        assert all(F.is_hodge_tuple(t, d) for t in lhs)
        assert all(len(t) == 2 and (t[0] + t[1]) % d == 0 for t in rhs)


def test_theorem_C1_certificates_for_the_six_open_orbits_of_X6_44():
    a = F.EXCEPTIONAL[44]
    certs = [((1, 4, 5, 13, 33, 37, 41, 42), [(2, 22, 24, 40)], [a, (2, 42), (4, 40)]),
             ((1, 5, 8, 9, 33, 37, 41, 42), [(2, 24, 26, 36), (13, 18, 22, 35)], [a, (2, 42), (8, 36), (9, 35), (18, 26)]),
             ((1, 5, 9, 16, 29, 33, 41, 42), [(2, 22, 24, 40), (4, 13, 35, 36), (8, 15, 28, 37)],
              [a, (2, 42), (4, 40), (8, 36), (9, 35), (15, 29), (16, 28)]),
             ((1, 5, 9, 24, 26, 33, 37, 41), [(13, 18, 22, 35)], [a, (9, 35), (18, 26)]),
             ((1, 5, 12, 13, 33, 34, 37, 41), [(10, 22, 24, 32)], [a, (10, 34), (12, 32)])]
    for orbit, surfaces, rhs in certs:
        assert F.is_hodge_tuple(orbit, 44) and F.lam(orbit, 44) == -1
        assert all(len(s) == 4 and F.is_hodge_tuple(s, 44) for s in surfaces)
        assert F.is_multiset_identity([orbit] + surfaces, rhs, 44)


def test_theorem_C5_open_part_of_Hdg3_of_X6_44():
    def mult(t):
        r = factorial(len(t))
        for c in Counter(t).values():
            r //= factorial(c)
        return r
    T = F.hodge_tuples(44, 8)
    assert 1 + sum(mult(t) for t in T) == 822_935_948              # dim Hdg^3(X^6_44), as in results/fermat_fast.md
    assert sum(mult(t) for t in T if F.lam(t, 44) % 2) == 4_838_400  # = 6 * 20 * 8!
