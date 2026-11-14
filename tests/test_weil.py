"""Tests for hodge/weil.py: Theorems W1 and W3 of docs/fermat/04-weil-route.md (degree q, exact) and the explicit
realizations of xi_44, xi_51, xi_52 as Weil classes relative to non-quadratic CM fields."""
from collections import Counter

import pytest

from hodge import formal_module as F
from hodge import galois as GA
from hodge import weil as W

QS = (44, 51, 52)


@pytest.fixture(scope="module")
def factors():
    return {q: W.simple_factors(q) for q in QS}


def test_factor_counts_and_dimensions(factors):
    # (dim A', dim A_beta) multiplicities, docs/fermat/04 Table 1
    expected = {
        44: Counter({(10, 10): 10, (5, 5): 9, (1, 1): 1, (1, 5): 1, (5, 10): 1}),
        51: Counter({(16, 16): 11, (8, 8): 5, (1, 1): 1}),
        52: Counter({(12, 12): 12, (6, 6): 10, (1, 1): 1, (2, 2): 1, (2, 6): 1, (6, 12): 1}),
    }
    for q in QS:
        fac = factors[q]
        assert Counter((f.simple_dim, f.dim) for f in fac) == expected[q]
        # the orbits partition the curve characters (as multisets)
        chars = {tuple(sorted((a, b, (-a - b) % q))) for a in range(1, q) for b in range(1, q) if (a + b) % q}
        orbits = [{W.scale(t, f.beta, q) for t in W.units(q)} for f in fac]
        assert sum(len(o) for o in orbits) == len(chars) == len(set().union(*orbits))
        for f in fac:
            assert f.stab <= f.h
            # the CM type has half the units, and the induced type is stable under H
            assert 2 * len(f.phi) == len(W.units(q))


def test_odd_factors(factors):
    odd = {q: sorted(f.beta for f in factors[q] if any(W.parity(v, q) for v in f.eigencharacters())) for q in QS}
    assert odd[44] == [(1, 10, 33), (1, 11, 32)]
    assert odd[51] == [(1, 16, 34), (1, 17, 33), (17, 17, 17)]
    assert len(odd[52]) == 12 and all(f.simple_dim == 12 for f in factors[52] if f.beta in odd[52])


def test_parity_constant_on_H_cosets(factors):
    # tv and thv differ by a divisor class (a Hodge element of length 6), so their parities agree
    for q in QS:
        for f in factors[q]:
            for t in W.units(q):
                assert len({W.parity(W.scale(t * h % q, f.beta, q), q) for h in f.h}) == 1


def test_imaginary_quadratic_subfields():
    for d, n in ((44, 2), (51, 2), (52, 2), (88, 4), (132, 4)):
        Ns = W.imaginary_quadratic(d)
        assert len(Ns) == n
        for N in Ns:
            assert 2 * len(N) == len(W.units(d)) and d - 1 not in N
            assert W.closure(list(N), d) == N


def test_theorem_W1(factors):
    """Weil generators for every imaginary quadratic K, and Hodge elements on factors of dimension <= 5, are Hodge
    and have even parity, hence lie in D_q + S_q."""
    for q in QS:
        fac = factors[q]
        gens = [g for N in W.imaginary_quadratic(q) for g in W.weil_generators(q, N, fac)]
        assert gens
        for g in gens:
            assert W.is_hodge_counts(g, q)
            assert W.parity(W.counts_to_tuple(g), q) == 0
        for g in W.small_factor_generators(q, 5, fac):
            assert W.is_hodge_counts(g, q)
            assert W.parity(W.counts_to_tuple(g), q) == 0


def test_single_halves_follow_signature(factors):
    # a K-half alone is Hodge exactly when its signature defect vanishes (the Weil-type condition)
    q = 44
    for N in W.imaginary_quadratic(q):
        for f in factors[q]:
            if not f.h <= N:
                continue
            u = next(u for u in W.e_weil_units(q, N, [f]) if 1 in {u.twist * x % q for x in N})
            assert F.is_hodge_tuple(u.element(), q) == (u.defect() == 0)


def test_theorem_W3(factors):
    """For every CM subfield E of Q(mu_q): an odd-parity E-Weil element exists iff [Q(mu_q) : E] is odd."""
    for q in QS:
        for N in W.cm_subgroups(q):
            assert W.odd_e_weil_exists(q, N, factors[q]) == (len(N) % 2 == 1)


@pytest.mark.parametrize("key,dim,deg", [("44/C5", 16, 8), ("44/1", 40, 4), ("51/1", 64, 4), ("52/1", 48, 4),
                                         ("52/C3", 16, 4)])
def test_realizations(key, dim, deg):
    q = W.REALIZATIONS[key][0]
    el, d_, g_ = W.realization(key)
    assert (d_, g_) == (dim, deg)
    assert len(el) == 3 * deg
    assert F.is_hodge_tuple(el, q)
    assert W.parity(el, q) == 1          # so el = xi_q mod D_q + S_q (Theorems D, D')


def test_realization_44_c5_is_e_weil():
    """E = Q(i, sqrt(-11)), B = A_(1,11,32) x E_i^6 with E acting on A through the twist 7 and on each E_i^2 through
    M_2(Q(i)).  For each of the four embeddings s*tau_0 of E (s = 1, 3, 7, 13 represent G/N) the s-part of H^1(B) is
    5 + 3 eigencharacters; all four parts are Hodge (B is of Weil type relative to E, d = 8) and have odd lambda_44."""
    q, N = 44, sorted((1, 5, 9, 25, 37))
    beta_A, beta_E = (1, 11, 32), (11, 11, 22)
    for s in (1, 3, 7, 13):
        part = [W.scale(s * 7 * t % q, beta_A, q) for t in N] + [W.scale(s, beta_E, q)] * 3
        tup = tuple(sorted(x for v in part for x in v))
        assert F.is_hodge_tuple(tup, q)
        assert W.parity(tup, q) == 1


def test_exponent_counts_matches_exact():
    for D in (44, 52):
        pds = [GA.PrimeData(l, D) for l in GA.split_primes(2 * D, 4)]
        for N in W.imaginary_quadratic(D):
            for g in W.weil_generators(D, N)[:5]:
                t = W.counts_to_tuple(g)
                for pd in pds:
                    assert W.exponent_counts(g, pd) == GA.exponent_exact(t, pd)


def test_galois_degree_44():
    """Theorem W2 for D = 44: Weil and small-factor characters do not reach eps(xi_44)."""
    D = 44
    grp = GA.CharacterGroup(D, GA.split_primes(2 * D, 24))
    for t in GA.known_generators(D, 6):
        grp.add(t)
    fac = W.simple_factors(D)
    extra = [g for N in W.imaginary_quadratic(D) for g in W.weil_generators(D, N, fac)]
    extra += W.small_factor_generators(D, 5, fac)
    for g in extra:
        grp.lattice.add([W.exponent_counts(g, pd) for pd in grp.data])
    assert not grp.contains(GA.even_form(F.EXCEPTIONAL[44], D))


def test_other_degrees_dichotomy():
    """docs/fermat/04 Table 4 (fast part): the odd-index criterion fails exactly when xi_q is a divisor class on a
    product of two CM elliptic-curve factors."""
    for q, fails in ((12, True), (15, True), (20, True), (21, True), (28, False), (33, False), (39, True)):
        res = [(len(N), W.odd_e_weil_exists(q, N)) for N in W.cm_subgroups(q)]
        crit = all(odd == (n % 2 == 1) for n, odd in res)
        assert crit == (not fails)
        ell = W.elliptic_divisor_realization(q)
        assert (ell is not None) == fails
        if ell:
            el = tuple(sorted(ell[0] + ell[1]))
            assert F.is_hodge_tuple(el, q) and W.parity(el, q) == 1


def test_generic_parity_matches_lambda():
    for q in QS:
        phi = W.parity_functional(q)
        for key in W.REALIZATIONS:
            if W.REALIZATIONS[key][0] == q:
                el = W.realization(key)[0]
                assert bin(W._mask(F.fold(el, q)) & phi).count("1") % 2 == 1
        assert bin(W._mask(F.fold(F.EXCEPTIONAL[q], q)) & phi).count("1") % 2 == 1
