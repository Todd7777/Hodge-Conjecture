"""Tests for hodge.galois and Theorem G of docs/fermat/03-galois-obstruction.md."""
import random

import pytest

from hodge import formal_module as F
from hodge import galois as G

A44 = (1, 5, 13, 22, 24, 33, 37, 41)
A52 = (1, 4, 17, 21, 29, 41, 45, 50)
A51 = (1, 4, 7, 19, 24, 34, 37, 40, 43, 46)
XI35 = (1, 2, 16, 17, 21, 22, 30, 31)          # MMRV Table 2 representative of xi_35


def dlog(g, b, l):
    x, k = 1, 0
    while x != b % l:
        x, k = x * g % l, k + 1
    return k


@pytest.mark.parametrize("d,tuples", [(12, [(1, 6, 8, 9), (1, 5, 7, 11)]), (44, [A44, (1, 43, 2, 42), (2, 22, 24, 40)])])
def test_exact_and_float_gauss_sums_agree(d, tuples):
    for l in G.split_primes(2 * d, 3):
        pd = G.PrimeData(l, d)
        for t in tuples:
            k, err = G.exponent_float(t, pd)
            assert err < 1e-8
            assert G.exponent_exact(t, pd) == k


def test_non_hodge_tuple_is_rejected():
    grp = G.CharacterGroup(44, G.split_primes(88, 2))
    with pytest.raises(ValueError):
        grp.vector((1, 1, 1, 41))


def test_kummer_descriptions_of_three_characters():
    """linear: trivial at l = 1 mod 88;  s_{11,1}: quartic residue symbol of 11;  alpha_44: 11-part = (2/P)_11."""
    s11 = (1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 33)
    for l in G.split_primes(88, 25):
        pd = G.PrimeData(l, 44)
        assert G.exponent_exact((3, 41, 5, 39), pd) == 0
        assert G.exponent_exact(s11, pd) == (22 * dlog(pd.g, 11, l)) % 88
        assert (G.exponent_exact(A44, pd) - dlog(pd.g, 2, l)) % 11 == 0


def test_alpha44_is_not_defined_over_Q_zeta_88():
    """At l = 89 (a split prime of Q(zeta_88)) the character is a nontrivial 11th root of unity."""
    from math import gcd
    pd = G.PrimeData(89, 44)
    k = G.exponent_exact(A44, pd)
    assert 88 // gcd(k, 88) == 11


@pytest.fixture(scope="module")
def group44():
    grp = G.CharacterGroup(44, G.split_primes(88, 24))
    for t in G.known_generators(44):
        grp.add(t)
    return grp


def test_theorem_G_degree_44(group44):
    assert not group44.contains(A44)


def test_every_lambda_odd_orbit_of_X6_44_is_obstructed_and_lambda_even_ones_are_not(group44):
    T8 = F.hodge_tuples(44, 8)
    random.seed(0)
    odd = [t for t in T8 if F.lam(t, 44) % 2]
    even = [t for t in T8 if F.lam(t, 44) % 2 == 0]
    assert all(not group44.contains(t) for t in random.sample(odd, 40))
    assert all(group44.contains(t) for t in random.sample(even, 40))
    six = [(1, 4, 5, 13, 33, 37, 41, 42), (1, 5, 8, 9, 33, 37, 41, 42), (1, 5, 9, 16, 29, 33, 41, 42),
           (1, 5, 9, 24, 26, 33, 37, 41), (1, 5, 12, 13, 33, 34, 37, 41), A44]
    assert all(not group44.contains(t) for t in six)


def test_twice_alpha44_is_reached(group44):
    """2 alpha_44 lies in D + S (Kubert-Aoki), so the obstruction is a quadratic character."""
    assert group44.contains(A44 + A44)


def test_theorem_G_degrees_51_and_52():
    assert G.galois_obstructed(A52, 52)
    assert G.galois_obstructed(A51, 51)


def test_control_xi35_obstructed_in_degree_35_but_not_70():
    """MMRV prove xi_35 algebraic via a length-6 representative in degree 70; the Galois test must agree."""
    assert G.galois_obstructed(XI35, 35)
    assert not G.galois_obstructed(F.lift(XI35, 35, 70), 70)
