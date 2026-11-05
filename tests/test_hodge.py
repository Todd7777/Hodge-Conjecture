"""Tests: every number here is either a published value or an internal consistency check between two
independent computations."""
import pytest

from hodge import fermat, fermat_lines, griffiths


# ---------------------------------------------------------------- Griffiths / hypersurfaces

@pytest.mark.parametrize("n,d,expected", [
    (1, 3, [1, 1]),                 # elliptic curve: h^{1,0} = h^{0,1} = 1
    (2, 4, [1, 19, 1]),             # quartic K3: primitive (1, 19, 1)
    (2, 5, [4, 44, 4]),             # quintic surface: p_g = 4, h^{1,1} = 45 = 44 + 1
    (3, 5, [1, 101, 101, 1]),       # quintic threefold
    (4, 3, [0, 1, 20, 1, 0]),       # cubic fourfold: h^{3,1} = 1, h^{2,2} = 21 = 20 + 1
    (3, 3, [0, 5, 5, 0]),           # cubic threefold: h^{2,1} = 5
    (3, 4, [0, 30, 30, 0]),         # quartic threefold: h^{2,1} = 30
])
def test_primitive_hodge_numbers(n, d, expected):
    assert griffiths.primitive_hodge_numbers(n, d) == expected


@pytest.mark.parametrize("n,d", [(1, 3), (2, 4), (2, 6), (3, 5), (4, 3), (4, 5), (5, 4), (6, 3)])
def test_euler_characteristic_two_ways(n, d):
    assert griffiths.euler_characteristic(n, d) == griffiths.euler_characteristic_closed_form(n, d)


@pytest.mark.parametrize("n,m", [(1, 3), (1, 5), (2, 3), (2, 4), (2, 7), (3, 3), (3, 4), (4, 3), (4, 4), (4, 5), (4, 6), (6, 3)])
def test_fermat_characters_reproduce_griffiths(n, m):
    """Counting characters by |alpha| must reproduce the Jacobian-ring Hodge numbers (two independent descriptions
    of H^n_prim of the same variety)."""
    assert fermat.hodge_numbers_by_characters(n, m) == griffiths.primitive_hodge_numbers(n, m)
    assert sum(fermat.hodge_numbers_by_characters(n, m)) == fermat.count_characters(n, m)


# ---------------------------------------------------------------- Fermat surfaces

@pytest.mark.parametrize("m,rho", [(3, 7), (4, 20), (5, 37), (6, 86), (7, 91), (8, 176)])
def test_picard_numbers_of_fermat_surfaces(m, rho):
    """Published Picard numbers (Shioda; Aoki-Shioda): e.g. rho(S_6) = 86, rho(S_8) = 176."""
    assert fermat.picard_number_fermat_surface(m) == rho


@pytest.mark.parametrize("m", [3, 4, 5, 6, 7])
def test_line_lattice_rank_matches_shioda(m):
    G = fermat_lines.gram_matrix(m)
    r = fermat_lines.rank_over_Q(G)
    assert r == fermat_lines.shioda_line_rank_formula(m)
    assert r == fermat_lines.rank_mod_p(G, 2147483647)
    assert r <= fermat.picard_number_fermat_surface(m)


def test_lines_generate_NS_iff_gcd_m_6_is_1_or_m_le_4():
    """Shioda / Schuett-Shioda-van Luijk: the lines span NS(S_m) (x) Q iff m <= 4 or gcd(m, 6) = 1."""
    from math import gcd
    for m in range(3, 9):
        full = fermat_lines.shioda_line_rank_formula(m) == fermat.picard_number_fermat_surface(m)
        assert full == (m <= 4 or gcd(m, 6) == 1), m


def test_gram_matrix_symmetric_and_diagonal():
    m = 5
    G = fermat_lines.gram_matrix(m)
    assert all(G[i][i] == 2 - m for i in range(len(G)))
    assert all(G[i][j] == G[j][i] for i in range(len(G)) for j in range(len(G)))
    # each line meets exactly 3m - 2 others?  Count: same splitting: 2(m-1); each other splitting: m. Total 4m - 2.
    row = sum(G[0]) - G[0][0]
    assert row == 4 * m - 2


# ---------------------------------------------------------------- Hodge characters / decomposability

def test_hodge_character_basics():
    # (1,1,1,1) is the class of the holomorphic 2-form on the Fermat quartic: NOT Hodge.
    assert not fermat.is_hodge((1, 1, 1, 1), 2, 4)
    # (1,3,1,3) = (a,-a,b,-b): standard Hodge class (a line).
    assert fermat.is_hodge((1, 1, 3, 3), 2, 4)
    assert fermat.is_decomposable((1, 1, 3, 3), 4)


def test_surfaces_and_points_are_base_cases():
    for alpha in fermat.hodge_characters(2, 7):
        assert fermat.is_decomposable(alpha, 7)


@pytest.mark.parametrize("n,m", [(4, 3), (4, 5), (4, 7), (4, 11), (4, 13), (6, 5), (6, 7), (8, 5)])
def test_prime_degree_all_decomposable(n, m):
    """Consistent with Shioda (1979) / Ran (1980): Hodge conjecture for Fermat varieties of prime degree."""
    assert fermat.indecomposable_hodge_characters(n, m) == []


@pytest.mark.parametrize("n,m", [(4, 4), (4, 8), (4, 9), (4, 12), (4, 20), (6, 4), (6, 9), (8, 4)])
def test_small_composite_degree_all_decomposable(n, m):
    """Consistent with Shioda's verification of condition (P_m) for m <= 20."""
    assert fermat.indecomposable_hodge_characters(n, m) == []


def test_aoki_type_indecomposable_class_for_m_25():
    """For m = p^2 = 25 the inductive structure alone does not reach every Hodge class (Aoki 1983/1987 constructs
    the missing cycles).  The indecomposable orbit found is (1, 6, 11, 16, 21, 20) = (1, 1+5, 1+10, 1+15, 1+20, -5)."""
    indec = fermat.indecomposable_hodge_characters(4, 25)
    assert indec, "expected an Aoki-type indecomposable Hodge character for m = 25"
    canon = {fermat._canon(a, 25) for a in indec}
    assert (1, 6, 11, 16, 20, 21) in canon
    assert fermat.is_hodge((1, 6, 11, 16, 20, 21), 4, 25)
    # it is pair-free: no two entries sum to 0 mod 25
    a = (1, 6, 11, 16, 20, 21)
    assert not any((a[i] + a[j]) % 25 == 0 for i in range(6) for j in range(i + 1, 6))


def test_condition_P33_false_consistent_with_da_silva():
    assert fermat.indecomposable_hodge_characters(4, 33) != []


def test_dim_hodge_classes_cubic_and_quartic_fourfold():
    # Fermat cubic fourfold: all 21 (2,2)-classes are Hodge (Galois group {+-1}).
    assert fermat.dim_hodge_classes(4, 3) == 21
    assert fermat.dim_hodge_classes(4, 4) == 142
