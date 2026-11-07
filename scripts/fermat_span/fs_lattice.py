"""fs_lattice.py -- exact lattice core of the 'span test' for the exceptional tuples xi_q of
Miranda-Movasati-Rufino-Villaflor (MMRV), 'Lengths of Hodge characters in Fermat varieties',
arXiv:2609.27301, section 4.

Conventions (MMRV Definition 4.1, Remark 4.1).  R_d is the free Z-module on (Z/d) - {0}; a tuple
(a_1,...,a_L) is identified with sum_i (a_i)_d, stored as a sorted tuple of integers in [1, d-1].
Lift R_{d'} -> R_d:  (a)_{d'} -> (k a)_d, k = d/d'.  G_d = (Z/d)^* acts by t.(a) = (t a).

Generators used (all exact, all labelled):
  linear     (a, d-a) for 1 <= a < d/2, and eps_d = (d/2) for d even           [MMRV Def 3.6, Rem 4.6]
  standard   s_{p,i} of MMRV Definition 3.7 in degree d' | d (d' = p k', k' >= 3, p prime, p !| i,
             all entries nonzero mod d'), lifted to degree d                       [Def 3.7, Def 4.5]
  xi         t.xi_{q'} (lifted to degree d) for q' in Q, q' | d, t in G_d         [Def 4.8, 4.9]
  hodge      Hodge tuples of length <= 6 of degree d (odd lengths for d even)    [Def 3.9, (16)]

Folded coordinates.  pi: R_d -> Z^h, h = floor((d-1)/2), pi((a)) = e_a (a < d/2), -e_{d-a} (a > d/2),
0 (a = d/2).  Its kernel is exactly D_d (the span of (a)+(-a) and eps_d).  The Hodge functionals
h_t(v) = sum_a v_a (<ta>_d - d/2) vanish on D_d and descend to Z^h.  B_d (MMRV Def 4.3) equals the
kernel lattice K_d = {v in R_d : h_t(v) = 0 for all t in G_d} (see docs/fermat/01-span-test.md, Lemma 1),
so pi(B_d) = {x in Z^h : A x = 0}, A_{t,a} = 2<ta>_d - d.

Integer linear algebra: PARI/GP via cypari2 (mathnf, matsnf with transforms, matsolvemod) and plain
Python integers.  Nothing is floating point.
"""
import csv
import os
from math import gcd

import cypari2

pari = cypari2.Pari()
pari.allocatemem(2 * 10**9, silent=True)

AUTHORS_DIR = "/home/user/mmiirandaaaa/length-reduction-functions"
EXC_CSV = os.path.join(AUTHORS_DIR, "exceptional_tuples.csv")
RED_CSV = os.path.join(AUTHORS_DIR, "exceptionals_modulo_lineals_and_standard.csv")


# ----------------------------------------------------------------------------- arithmetic helpers
def divisors(n):
    return [k for k in range(1, n + 1) if n % k == 0]


def prime_divisors(n):
    out, p, m = [], 2, n
    while p * p <= m:
        if m % p == 0:
            out.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        out.append(m)
    return out


def units(d):
    return [t for t in range(1, d) if gcd(t, d) == 1] if d > 1 else []


def half_units(d):
    """units t of Z/d with 1 <= t < d/2 (t and d-t give equivalent Hodge conditions)."""
    return [t for t in range(1, (d + 1) // 2) if gcd(t, d) == 1] if d > 2 else [1]


def P_elements(d):
    """elements of MMRV's P = {4} u {odd primes} dividing d."""
    out = [p for p in prime_divisors(d) if p != 2]
    if d % 4 == 0:
        out = [4] + out
    return out


def Q_divisors(d):
    """q in Q (products of an even number >= 2 of distinct elements of P) with q | d, sorted."""
    P = P_elements(d)
    out = set()
    n = len(P)
    for mask in range(1, 1 << n):
        if bin(mask).count("1") % 2:
            continue
        q = 1
        for j in range(n):
            if mask >> j & 1:
                q *= P[j]
        if d % q == 0:
            out.add(q)
    return sorted(out)


def in_Q(q):
    return q > 1 and q in Q_divisors(q)


# ----------------------------------------------------------------------------- tuples
def read_tuples(path=EXC_CSV):
    out = {}
    with open(path) as f:
        rows = csv.DictReader(f, delimiter="|")
        keys = rows.fieldnames
        for row in rows:
            out[int(row[keys[0]])] = tuple(int(x) for x in row[keys[1]].split(","))
    return out


def lift(tup, d0, d):
    assert d % d0 == 0
    k = d // d0
    return tuple(sorted(k * a for a in tup))


def act(t, tup, d):
    return tuple(sorted((t * a) % d for a in tup))


def hodge_defect(tup, d):
    """max over units t of |2*sum<t a> - d*L| (0 iff the tuple is a Hodge tuple of degree d)."""
    L = len(tup)
    worst = 0
    for t in half_units(d):
        s = sum((t * a) % d for a in tup)
        worst = max(worst, abs(2 * s - d * L))
    return worst


def is_hodge(tup, d):
    if any(a % d == 0 for a in tup):
        return False
    return hodge_defect(tup, d) == 0


def to_vec(tup, d):
    """R_d vector (length d-1, index a-1) of a tuple (formal sum)."""
    v = [0] * (d - 1)
    for a in tup:
        v[a % d - 1] += 1
    return v


def fold(vec, d):
    """pi: R_d (list of length d-1) -> Z^h."""
    h = (d - 1) // 2
    return [vec[a - 1] - vec[d - a - 1] for a in range(1, h + 1)]


def fold_tuple(tup, d):
    h = (d - 1) // 2
    x = [0] * h
    for a in tup:
        a %= d
        if 2 * a < d:
            x[a - 1] += 1
        elif 2 * a > d:
            x[d - a - 1] -= 1
    return x


# ----------------------------------------------------------------------------- generators
def linear_gens(d):
    out = [(("lin", a), (a, d - a)) for a in range(1, (d + 1) // 2)]
    if d % 2 == 0:
        out.append((("eps",), (d // 2,)))
    return out


def standard_tuple(p, i, dp):
    """s_{p,i} of MMRV Definition 3.7 in degree dp = p*k (as an unsorted tuple of residues mod dp)."""
    k = dp // p
    if p == 2:
        return (i % dp, (k + i) % dp, (dp - 2 * i) % dp, k % dp)
    return tuple((j * k + i) % dp for j in range(p)) + ((dp - p * i) % dp,)


def standard_gens(d, mode="div"):
    """Standard tuples, deduplicated, with labels ('std', p, i, d').
    mode 'deg': only d' = d (the generators of S_d of MMRV Definition 4.5);
    mode 'div': every divisor d' of d, lifted to degree d (generators of sum_{d'|d} S_{d'} in S~_d)."""
    seen = {}
    degs = [d] if mode == "deg" else divisors(d)
    for dp in degs:
        for p in prime_divisors(dp):
            k = dp // p
            if k < 3:
                continue
            for i in range(1, dp):
                if i % p == 0:
                    continue
                s = standard_tuple(p, i, dp)
                if any(a == 0 for a in s):
                    continue
                key = lift(s, dp, d)
                if key not in seen:
                    seen[key] = ("std", p, i, dp)
    return [(lab, tup) for tup, lab in seen.items()]


def xi_orbit_gens(qp, xi, d, ts=None):
    """t.xi_{q'} lifted to degree d for t in half_units(d) (t and -t differ by a sign mod D_d)."""
    base = lift(xi, qp, d)
    if ts is None:
        ts = half_units(d)
    return [(("xi", qp, t), act(t, base, d)) for t in ts]


# ----------------------------------------------------------------------------- PARI helpers
def to_pari_cols(cols, h):
    """list of length-h integer lists -> PARI matrix whose columns are those vectors."""
    if not cols:
        return pari.matrix(h, 0)
    rows = [[c[r] for c in cols] for r in range(h)]
    return pari.matrix(h, len(cols), [x for row in rows for x in row])


def pari_mat_to_lists(M):
    """PARI matrix -> list of rows (Python ints)."""
    nr = int(pari.matsize(M)[0])
    nc = int(pari.matsize(M)[1])
    return [[int(M[r, c]) for c in range(nc)] for r in range(nr)]


def hodge_matrix(d):
    """rows: t in half_units(d); columns a = 1..h; entry 2<ta>_d - d."""
    h = (d - 1) // 2
    return [[2 * ((t * a) % d) - d for a in range(1, h + 1)] for t in half_units(d)]


class SNFLattice:
    """Sublattice L of Z^h given by generator columns; stores an exact HNF basis and a Smith form
    U * H * V = D (U in GL_h(Z)).  For x in Z^h the class of x in Z^h / L is determined by the
    vector U x reduced modulo the row moduli (modulus 0 = free row)."""

    def __init__(self, cols, h):
        self.h = h
        X = to_pari_cols(cols, h)
        self.H = pari.mathnf(X)                     # h x r, columns a basis of L
        self.r = int(pari.matsize(self.H)[1])
        if self.r == 0:
            self.U = pari.matid(h)
            self.mod = [0] * h
            return
        U, V, D = pari.matsnf(self.H, 1)
        # verify the Smith decomposition exactly
        assert pari.matdet(U) in (1, -1), "U not unimodular"
        assert pari.matdet(V) in (1, -1), "V not unimodular"
        assert U * self.H * V == D, "SNF identity fails"
        Dl = pari_mat_to_lists(D)
        mod = []
        for row in Dl:
            nz = [x for x in row if x != 0]
            assert len(nz) <= 1
            mod.append(abs(nz[0]) if nz else 0)
        # each column of D has exactly one nonzero entry (rank r)
        for c in range(self.r):
            assert sum(1 for row in Dl if row[c] != 0) == 1
        self.U = U
        self.Ul = pari_mat_to_lists(U)
        self.mod = mod

    def elementary_divisors(self):
        return sorted(m for m in self.mod if m != 0)

    def coords(self, x):
        """U x as a list of Python ints."""
        return [sum(u * xi for u, xi in zip(row, x) if xi) for row in self.Ul]

    def contains(self, x):
        c = self.coords(x)
        for ci, m in zip(c, self.mod):
            if m == 0:
                if ci != 0:
                    return False
            elif ci % m:
                return False
        return True

    def torsion_rows(self, modulus):
        return [j for j, m in enumerate(self.mod) if m == modulus]


def solve_in_lattice(cols, h, target):
    """integer vector c with sum_j c_j cols[j] = target, or None (PARI matsolvemod over Z)."""
    X = to_pari_cols(cols, h)
    B = pari.Col(list(target))
    sol = pari.matsolvemod(X, 0, B)
    if sol == 0:
        return None
    c = [int(sol[j]) for j in range(len(cols))]
    # exact verification
    for r in range(h):
        assert sum(c[j] * cols[j][r] for j in range(len(cols)) if c[j]) == target[r]
    return c
