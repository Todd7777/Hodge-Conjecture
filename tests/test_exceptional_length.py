"""Checks for Theorem D of docs/fermat/02-exceptional-lengths.md (exact lengths of xi_q for q = 4p and q = 3p)."""
import pytest

from hodge import exceptional_length as E
from hodge import formal_module as F

FAMILY_SMALL = E.family_degrees(130)

# Miranda-Movasati-Rufino-Villaflor, arXiv:2609.27301v2, Table 1 (upper bounds for l_{2,q}(xi_q)), family entries.
MMRV_TABLE1 = {12: 3, 15: 4, 28: 4, 33: 6, 44: 7, 51: 10, 69: 12, 76: 11, 87: 16, 92: 12, 123: 26, 124: 16, 141: 24,
               159: 28, 172: 25, 177: 30, 188: 24, 213: 36, 236: 31, 249: 42, 267: 46, 268: 35, 284: 36, 303: 52,
               316: 40, 321: 54, 332: 43, 339: 58, 393: 66, 411: 70, 412: 52}


def test_family_membership():
    assert FAMILY_SMALL == [12, 15, 28, 33, 44, 51, 69, 76, 87, 92, 123, 124]
    for q in (20, 21, 35, 39, 52, 57, 65, 68):
        with pytest.raises(ValueError):
            E.family(q)


@pytest.mark.parametrize("q", FAMILY_SMALL)
def test_key_identity_on_B_q(q):
    assert E.check_identity_on_B(q)


@pytest.mark.parametrize("q", FAMILY_SMALL)
def test_lambda_is_even_on_linear_and_standard_tuples(q):
    assert all(v % 2 == 0 for v in E.standard_lambda_values(q))
    m, p = E.family(q)
    assert E.lam((p, (m - 1) * p), q) == 0                  # the pair (a, -a) with a of order m


@pytest.mark.parametrize("q", FAMILY_SMALL)
def test_index_two(q):
    assert E.index_B_over_DS(q) == 2


@pytest.mark.parametrize("q", E.family_degrees(420))
def test_explicit_shortest_tuple(q):
    t = E.minimal_tuple(q)
    assert F.is_hodge_tuple(t, q)
    assert len(t) == E.predicted_length(q)
    assert E.lam(t, q) == -1
    m, p = E.family(q)
    assert (p - 1) * E.lam(t, q) + 2 * E.U(t, q) == 0


@pytest.mark.parametrize("q", [12, 15, 28, 33, 44])
def test_lower_bound_by_exhaustion(q):
    """No Hodge tuple of degree q shorter than the predicted length has odd lambda (independent of the proof)."""
    for L in range(1, E.predicted_length(q)):
        assert all(E.lam(t, q) % 2 == 0 for t in F.hodge_tuples(q, L)), L


def test_formula_reproduces_every_family_entry_of_mmrv_table_1():
    for q, value in MMRV_TABLE1.items():
        assert E.predicted_length(q) == value, q


def test_q33_shortest_tuple_is_mmrv_table_2_representative():
    assert E.minimal_tuple(33) == (1, 4, 16, 22, 25, 31)


# ------------------------------------------------------------------ the class chi_m(p) = +1 (Theorem D, second case)

PLUS_SMALL = [q for q in E.family_degrees(130, both=True) if q not in E.family_degrees(130)]

# MMRV Table 1, entries of the class chi_m(p) = +1 (q = 4p, p = 1 mod 4; q = 3p, p = 1 mod 3), all q <= 417.
MMRV_TABLE1_PLUS = {20: 3, 21: 4, 39: 6, 52: 7, 57: 10, 68: 10, 93: 16, 111: 20, 116: 15, 129: 22, 148: 19, 164: 22,
                    183: 36, 201: 36, 212: 27, 219: 42, 237: 40, 244: 31, 291: 50, 292: 36, 309: 54, 327: 54, 356: 44,
                    381: 64, 388: 50, 404: 51, 417: 70}


def test_plus_class_membership():
    assert PLUS_SMALL == [20, 21, 39, 52, 57, 68, 93, 111, 116, 129]


@pytest.mark.parametrize("q", PLUS_SMALL)
def test_plus_class_identities_parity_and_index(q):
    assert E.check_identity_on_B(q)                       # lambda = 0 and g(x) + g(-x) constant on B_q
    assert all(v % 2 == 0 for v in E.standard_lambda_values(q))
    assert E.index_B_over_DS(q) == 2


@pytest.mark.parametrize("q", E.family_degrees(420, both=True))
def test_explicit_shortest_tuple_both_classes(q):
    t = E.minimal_tuple(q)
    assert F.is_hodge_tuple(t, q)
    assert len(t) == E.predicted_length(q)
    assert E.parity_invariant(t, q) % 2 == 1


@pytest.mark.parametrize("q", [20, 21, 39, 52])
def test_plus_class_lower_bound_by_exhaustion(q):
    for L in range(1, E.predicted_length(q)):
        assert all(E.parity_invariant(t, q) % 2 == 0 for t in F.hodge_tuples(q, L)), L


def test_formula_reproduces_every_plus_class_entry_of_mmrv_table_1():
    for q, value in MMRV_TABLE1_PLUS.items():
        assert E.predicted_length(q) == value, q


def test_lambda_52_is_the_plus_class_invariant():
    from hodge import formal_module as FM
    for t in F.hodge_tuples(52, 6)[:200] + [FM.EXCEPTIONAL[52]]:
        assert E.lam_prime(t, 52) == FM.lam(t, 52)
