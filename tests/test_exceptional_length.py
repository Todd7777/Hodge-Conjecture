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
