"""Tests for hodge/two_prime.py: Theorem T of docs/fermat/02-exceptional-lengths.md section 6,
f_0(q) = phi(q)/4 + c_{p1}(p2) + c_{p2}(p1) for every q = p1 p2 (two distinct odd primes)."""
import cmath

from hodge import exceptional_length as EL
from hodge import formal_module as F
from hodge import two_prime as T


def two_prime_degrees(qmax, pmin=5):
    return sorted(p1 * p2 for p1 in range(pmin, qmax) for p2 in range(p1 + 1, qmax)
                  if T.is_prime(p1) and T.is_prime(p2) and p1 * p2 <= qmax)


def test_formula_small_values():
    expected = {35: 8, 55: 10, 65: 16, 77: 16, 85: 18, 91: 22, 95: 20}
    assert {q: T.predicted_length(q) for q in expected} == expected


def test_formula_extends_theorem_D_prime():
    # with p1 = 3 the formula is Theorem D' (and Theorem D for chi_3(p) = -1)
    for q in EL.family_degrees(300, both=True):
        if q % 3 == 0 and q % 4 and q != 9:
            assert T.predicted_length(q) == EL.predicted_length(q)


def test_functionals_partition():
    for q in (35, 65, 91, 145):
        p1, p2 = T.factor(q)
        funcs = T.coset_functionals(q)
        assert len(funcs) == T.predicted_length(q)
        supports = [s for _, s in funcs]
        allx = [x for s in supports for x in s]
        assert len(allx) == len(set(allx))                   # disjoint
        for s in supports:
            assert frozenset((-x) % q for x in s) == s       # closed under negation: even on D_q


def test_functionals_kill_standard_tuples():
    # Proposition T1 (checked): every coset functional is even on every standard tuple of every degree dividing q
    for q in two_prime_degrees(300, pmin=3):
        std = F.standard_tuples(q)
        for _, s in T.coset_functionals(q):
            assert all(T.count(s, t, q) % 2 == 0 for t in std), q


def test_exceptional_element():
    # Propositions T2, T3 (checked): the explicit element is a Hodge tuple, odd on every coset functional
    for q in two_prime_degrees(1200, pmin=3):
        xi = T.aoki_xi(q)
        assert F.is_hodge_tuple(xi, q), q
        assert all(T.count(s, xi, q) % 2 == 1 for _, s in T.coset_functionals(q)), q


def test_shortest_tuple_construction():
    # Proposition T4 and Theorem T: adapted half systems give a Hodge tuple of exactly the formula length, with one
    # entry in each coset support and nothing else
    for q in two_prime_degrees(1200, pmin=3):
        t = T.shortest_tuple(q)
        assert F.is_hodge_tuple(t, q), q
        assert len(t) == T.predicted_length(q), q
        assert all(T.count(s, t, q) == 1 for _, s in T.coset_functionals(q)), q


def test_any_half_systems():
    # Propositions T2, T3 hold for every choice of half systems (random choices)
    import random
    rnd = random.Random(7)
    for q in (35, 65, 91, 143, 221, 323):
        p1, p2 = T.factor(q)
        for _ in range(5):
            h1 = sorted(x if rnd.random() < 0.5 else p1 - x for x in range(1, (p1 + 1) // 2))
            h2 = sorted(x if rnd.random() < 0.5 else p2 - x for x in range(1, (p2 + 1) // 2))
            xi = T.xi_from_half_systems(q, h1, h2)
            assert F.is_hodge_tuple(xi, q)
            assert all(T.count(s, xi, q) % 2 == 1 for _, s in T.coset_functionals(q))


def test_shortest_65_matches_mmrv_list():
    assert T.shortest_tuple(65) == (1, 2, 6, 16, 17, 21, 27, 32, 41, 42, 45, 47, 52, 55, 56, 60)


def test_xi_35_matches_mmrv():
    assert T.aoki_xi(35) == (1, 2, 16, 17, 21, 22, 30, 31)     # MMRV Table 2


def test_sign_change_identity():
    """2 * sum_{w in W} chi(w) = (conj(chi)(p) - 1) * sum_{y in hs} chi(y) for odd characters chi mod l, where
    W = {p^{-1} y : y in hs, p^{-1} y not in hs} (the key identity in the proof that xi'_q is Hodge)."""
    for p, l in ((5, 7), (5, 13), (7, 11), (11, 19), (3, 17)):
        g = T.primitive_root(l)
        hs = T.half_system(l)
        inv = pow(p, -1, l)
        W = [inv * y % l for y in hs if inv * y % l not in set(hs)]
        log = {pow(g, k, l): k for k in range(l - 1)}
        for j in range(1, l - 1, 2):                          # odd characters chi(g^k) = exp(2 pi i j k/(l-1))
            chi = lambda x: cmath.exp(2j * cmath.pi * j * log[x % l] / (l - 1))
            lhs = 2 * sum(chi(w) for w in W)
            rhs = (chi(p).conjugate() - 1) * sum(chi(y) for y in hs)
            assert abs(lhs - rhs) < 1e-9


def test_representatives():
    for q in (35, 55, 65, 77, 85, 91, 95, 115, 119, 133, 143, 145, 155):
        rep = T.REPRESENTATIVES[q]
        v = T.verify(q, rep)
        assert v["kills_D"] and v["kills_S"] and v["odd_on_rep"] and v["rep_hodge"] and v["rep_outside"], q
        assert v["length"] == v["bound"] == T.predicted_length(q), q


def test_all_representatives_have_formula_length():
    for q, rep in T.REPRESENTATIVES.items():
        assert len(rep) == T.predicted_length(q)
        assert F.is_hodge_tuple(rep, q)
        # one entry in each coset, nothing else
        funcs = T.coset_functionals(q)
        assert all(T.count(s, rep, q) == 1 for _, s in funcs)
        assert sum(T.count(s, rep, q) for _, s in funcs) == len(rep)
