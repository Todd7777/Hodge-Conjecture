"""ilp_core.py -- exact core for the (lifted) Aoki-Shioda length reduction of MMRV
(Miranda-Movasati-Rufino-Villaflor, arXiv:2609.27301, sections 4.3-4.4).

Conventions (MMRV section 4.1).  R_d = free Z-module on (Z/d) - {0}; a tuple (a_1,..,a_L)
is the element sum_i (a_i)_d.  Lift: (a)_{d'} -> (k a)_d, k = d/d'.
  D_d  : linear tuples (a, -a), and eps_d = (d/2) for d even          (Remark 4.6)
  S~_d : here the Z-span of the lifts to degree d of the standard tuples s_{p,i} of
         Definition 3.7 of every divisor d' of d (d' = p k', k' >= 3, p prime, p !| i).
FOLDED coordinates: R_d / D_d is free on the classes of (a), 1 <= a < d/2, because
(a) == -(d-a) mod D and (d/2) == 0 mod D.  fold(alpha)[a-1] = n_a - n_{d-a}.  By MMRV
Remark 4.11 the length of the shortest element of alpha + D_d is ||fold(alpha)||_1, and a
shortest representative with non-negative coefficients is unfold(fold(alpha)).
Everything in this file is exact integer arithmetic (Python ints / python-flint / PARI).
"""
import csv
import os
from math import gcd

AUTHORS_DIR = "/home/user/mmiirandaaaa/length-reduction-functions"
EXC_CSV = os.path.join(AUTHORS_DIR, "exceptional_tuples.csv")
RED_CSV = os.path.join(AUTHORS_DIR, "exceptionals_modulo_lineals_and_standard.csv")

# MMRV Tables 2 and 4 (the published representatives), (q, d) -> tuple
MMRV_TABLE2 = {
    12: (1, 8, 9), 15: (1, 7, 10, 12), 20: (3, 8, 19), 21: (1, 10, 15, 16),
    28: (5, 13, 17, 21), 33: (1, 4, 16, 22, 25, 31), 35: (1, 2, 16, 17, 21, 22, 30, 31),
    39: (1, 16, 19, 22, 28, 31), 44: (8, 11, 15, 19, 27, 31, 43)}
MMRV_TABLE4 = {
    (33, 66): (19, 26, 43, 44), (35, 70): (10, 12, 13, 53, 56, 66), (39, 78): (25, 43, 49),
    (44, 132): (3, 37, 39, 75, 84, 99, 125), (51, 102): (7, 19, 25, 60, 68, 87, 91),
    (52, 156): (24, 51, 63, 75, 87, 97, 149), (55, 110): (19, 29, 39, 79, 109),
    (57, 114): (23, 41, 64, 66, 71, 77)}


def read_tuples(path=EXC_CSV):
    out = {}
    with open(path) as f:
        rows = csv.DictReader(f, delimiter="|")
        keys = rows.fieldnames
        for row in rows:
            out[int(row[keys[0]])] = tuple(int(x) for x in row[keys[1]].split(","))
    return out


def divisors(n):
    return [k for k in range(1, n + 1) if n % k == 0]


def prime_divisors(n):
    ps, p, m = [], 2, n
    while p * p <= m:
        if m % p == 0:
            ps.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        ps.append(m)
    return ps


def units(d):
    return [t for t in range(1, d) if gcd(t, d) == 1]


def is_hodge(tup, d):
    """Exact Hodge test (MMRV (16), any length, odd lengths allowed when d is even):
    sum_i <t a_i> = (L/2) d for every unit t of Z/d, and no entry is 0 mod d."""
    L = len(tup)
    if any(a % d == 0 for a in tup) or (L * d) % 2:
        return False
    target = L * d // 2
    return all(sum((t * a) % d for a in tup) == target for t in units(d))


def lift(tup, d0, d):
    assert d % d0 == 0
    c = d // d0
    return tuple(sorted((c * a) % d for a in tup))


def galois(tup, t, d):
    return tuple(sorted((t * a) % d for a in tup))


# ---------------------------------------------------------------- generators of D_d + S~_d
def linear_tuples(d):
    out = [(a, d - a) for a in range(1, (d + 1) // 2)]
    if d % 2 == 0:
        out.append((d // 2,))
    return out


def standard_tuple(p, i, d):
    """s_{p,i} of MMRV Definition 3.7 in degree d = p k."""
    k = d // p
    assert p * k == d
    if p == 2:
        return tuple(sorted([i % d, (k + i) % d, (-2 * i) % d, k % d]))
    return tuple(sorted([(i + j * k) % d for j in range(p)] + [(-p * i) % d]))


def lifted_standard_tuples(d, with_origin=False):
    """All lifts to degree d of the standard tuples s_{p,i} (Definition 3.7: p prime,
    d' = p k' | d, k' >= 3, p does not divide i, all entries non-zero) of every divisor d'.
    Returns a sorted list of distinct tuples (and, if asked, one origin (d', p, i) each)."""
    seen = {}
    for dp in divisors(d):
        for p in prime_divisors(dp):
            kp = dp // p
            if kp < 3:
                continue
            for i in range(1, dp):
                if i % p == 0:
                    continue
                s = standard_tuple(p, i, dp)
                if any(a == 0 for a in s):
                    continue
                t = lift(s, dp, d)
                if t not in seen:
                    seen[t] = (dp, p, i)
    keys = sorted(seen)
    return (keys, [seen[k] for k in keys]) if with_origin else keys


def authors_standard_tuples(d):
    """The generator set of the authors' utils.standards(d) (p | d, k = d/p, all i with
    k >= 3 gcd(i,k), deduplicated), re-implemented for comparison."""
    out = set()
    for p in prime_divisors(d):
        k = d // p
        for i in range(1, d):
            if k < 3 * gcd(i, k):
                continue
            out.add(standard_tuple(p, i, d))
    return sorted(out)


# ---------------------------------------------------------------- folded coordinates
def fdim(d):
    return (d - 1) // 2


def fold(tup_or_counts, d, counts=False):
    """Folded vector (list of ints, length (d-1)//2) of a tuple, or of a count vector
    (index a-1 holds the coefficient of (a)) if counts=True."""
    m = fdim(d)
    y = [0] * m
    items = (enumerate(tup_or_counts, 1) if counts else ((a, 1) for a in tup_or_counts))
    for a, c in items:
        a %= d
        if c == 0 or a == 0 or 2 * a == d:
            continue
        if a < d - a:
            y[a - 1] += c
        else:
            y[d - a - 1] -= c
    return y


def unfold(y, d):
    """Shortest non-negative representative (sorted tuple) of the class of folded y."""
    out = []
    for j, c in enumerate(y):
        a = j + 1
        out += [a] * c if c > 0 else [d - a] * (-c)
    return tuple(sorted(out))


def counts(tup, d):
    v = [0] * (d - 1)
    for a in tup:
        v[a % d - 1] += 1
    return v


def in_D(vec, d):
    """vec: count vector over 1..d-1 (any integers). True iff vec is in D_d, i.e. the
    coefficient of (a) equals that of (-a) for every a (then vec = sum c_a((a)+(-a)) +
    c (d/2))."""
    return all(vec[a - 1] == vec[d - a - 1] for a in range(1, d))


# ---------------------------------------------------------------- exact lattice layer
def generator_tuples(d, extra=()):
    """Standard generators (lifted, Definition 3.7) of S~_d plus extra algebraic tuples of
    degree d (e.g. lifts of already-reduced exceptional tuples and their Galois conjugates).
    The linear generators are implicit in folded coordinates."""
    gens = list(lifted_standard_tuples(d))
    seen = set(gens)
    for t in extra:
        t = tuple(sorted(a % d for a in t))
        if t not in seen:
            seen.add(t)
            gens.append(t)
    return gens


def folded_matrix(d, gens):
    """Columns = folded generators; returned as a list of rows (m x N) of Python ints."""
    m = fdim(d)
    cols = [fold(g, d) for g in gens]
    return [[cols[j][i] for j in range(len(cols))] for i in range(m)]


def hodge_functionals(d):
    """W[t][a-1] = 2<ta> - d for t in units, t < d/2, and 1 <= a < d/2.  A folded vector y is
    the fold of a Hodge element iff W y = 0 (for a non-negative tuple: iff it is Hodge)."""
    m = fdim(d)
    return [[2 * ((t * a) % d) - d for a in range(1, m + 1)] for t in units(d) if 2 * t < d]


class Mod2Classes:
    """Classes modulo L = span_Z(folded gens), for vectors of Lam = span_Q(L) cap Z^m,
    tested modulo 2.  Valid when (i) Lam is saturated with the same rank (automatic) and
    (ii) 2 Lam is inside L.  Then for y in Lam:  y in L  <=>  y mod 2 in (L mod 2).
    [Proof: y = l + 2z, l in L, z in Z^m; 2z = y - l in Lam, so z in Lam (saturation) and
    2z in 2 Lam in L.]  (ii) is checked exactly by `verify` (Smith form of L)."""

    def __init__(self, d, gens):
        self.d, self.m = d, fdim(d)
        self.gens = gens
        self.cols = [fold(g, d) for g in gens]
        self.basis = {}                       # pivot bit -> row bitset (fully reduced)
        for c in self.cols:
            self._insert(self._bits(c))
        self.rank2 = len(self.basis)
        self.sym = {}                         # symbol a -> class bitset of fold((a))

    @staticmethod
    def _bits(y):
        b = 0
        for i, c in enumerate(y):
            if c & 1:
                b |= 1 << i
        return b

    def _reduce(self, b):
        while True:
            x = b
            done = True
            for piv, row in self.basis.items():
                if b >> piv & 1:
                    b ^= row
                    done = False
            if done or b == x:
                return b

    def _insert(self, b):
        b = self._reduce(b)
        if b == 0:
            return False
        piv = b.bit_length() - 1
        for p2 in list(self.basis):
            if self.basis[p2] >> piv & 1:
                self.basis[p2] ^= b
        self.basis[piv] = b
        return True

    def cls(self, y):
        """Canonical class (int bitset) of folded y modulo L (mod 2)."""
        return self._reduce(self._bits(y))

    def cls_tuple(self, tup):
        c = 0
        for a in tup:
            a %= self.d
            if 2 * a == self.d:
                continue
            if a not in self.sym:
                self.sym[a] = self.cls(fold((a,), self.d))
            c ^= self.sym[a]
        return c

    def verify(self):
        """Exact checks (python-flint): rank_Q L = m - rank_Q W (so Lam = Hodge kernel and
        every Hodge tuple folds into Lam) and the Smith invariants of L are all in {1,2}
        (so Lam/L = (Z/2)^s and 2 Lam is in L).  Returns a dict of the numbers."""
        import flint
        m, d = self.m, self.d
        M = flint.fmpz_mat(m, len(self.cols), [self.cols[j][i] for i in range(m)
                                               for j in range(len(self.cols))])
        r = M.rank()
        W = flint.fmpz_mat(hodge_functionals(d))
        rw = W.rank()
        S = M.snf()
        inv = [int(S[i, i]) for i in range(min(S.nrows(), S.ncols())) if S[i, i] != 0]
        bad = sorted(set(abs(x) for x in inv) - {1, 2})
        s = sum(1 for x in inv if abs(x) == 2)
        gens_hodge = all(is_hodge(g, d) for g in self.gens)   # so L is inside the Hodge kernel
        return {"m": m, "rank_L": r, "rank_W": rw, "hodge_kernel_rank": m - rw,
                "rank_L_mod2": self.rank2, "s_twos": s, "bad_invariants": bad,
                "generators_hodge": gens_hodge,
                "ok": gens_hodge and (r == m - rw) and not bad and (s == r - self.rank2)}


def _pari_mem(pari):
    """Small initial PARI stack, allowed to grow (virtual) up to 8 GB on demand."""
    if not getattr(pari, "_ilp_mem_set", False):
        pari.allocatemem(64 * 10**6, 8 * 10**9, silent=True)
        try:
            pari._ilp_mem_set = True
        except Exception:
            pass


def integer_certificate(d, gens, target_folded):
    """Exact integer x with  sum_j x_j fold(gens[j]) = target_folded  (PARI matsolvemod
    over Z), or None.  Returned x is then re-checked in unfolded coordinates by
    check_certificate."""
    import cypari2
    pari = cypari2.Pari()
    _pari_mem(pari)
    m = fdim(d)
    cols = [fold(g, d) for g in gens]
    rows = ";".join(",".join(str(cols[j][i]) for j in range(len(cols))) for i in range(m))
    Mp = pari("[" + rows + "]")
    Y = pari("[" + ",".join(str(v) for v in target_folded) + "]~")
    X = pari.matsolvemod(Mp, 0, Y)
    if X == 0 and any(target_folded):
        return None
    return [int(v) for v in X]


def check_certificate(d, xi_tuple, beta_tuple, gens, x):
    """Exact unfolded check of  xi - beta - sum_j x_j gens[j]  in D_d  (coefficient of (a)
    equal to that of (-a) for all a).  Returns True/False."""
    v = [0] * (d - 1)
    for a in xi_tuple:
        v[a % d - 1] += 1
    for a in beta_tuple:
        v[a % d - 1] -= 1
    for g, c in zip(gens, x):
        if c:
            for a in g:
                v[a % d - 1] -= c
    return in_D(v, d)


def hodge_kernel_basis(d):
    """LLL-reduced Z-basis (list of folded vectors) of {y in Z^m : W y = 0} (PARI matkerint)."""
    import cypari2
    pari = cypari2.Pari()
    _pari_mem(pari)
    W = hodge_functionals(d)
    Wp = pari("[" + ";".join(",".join(str(x) for x in row) for row in W) + "]")
    K = pari.matkerint(Wp)
    ncols = int(pari.matsize(K)[1])
    return [[int(K[i, j]) for i in range(fdim(d))] for j in range(ncols)]


def galois_fold(y, t, d):
    """Folded image of folded y under the Galois element t (exact signs)."""
    m = fdim(d)
    z = [0] * m
    for j, c in enumerate(y):
        if c:
            b = (t * (j + 1)) % d
            if b < d - b:
                z[b - 1] += c
            else:
                z[d - b - 1] -= c
    return z


def unit_group_generators(d):
    """A generating set of (Z/d)^x (greedy: add units not yet in the generated subgroup)."""
    U = units(d)
    H = {1}
    gens = []
    for u in U:
        if u in H:
            continue
        gens.append(u)
        frontier = list(H)
        H2 = set(H)
        while frontier:
            new = []
            for h in frontier:
                x = (h * u) % d
                if x not in H2:
                    H2.add(x)
                    new.append(x)
            frontier = new
            # close under products with all of H2
        changed = True
        while changed:
            changed = False
            for a in list(H2):
                for g in gens:
                    x = (a * g) % d
                    if x not in H2:
                        H2.add(x)
                        changed = True
        H = H2
        if len(H) == len(U):
            break
    return gens


def quotient_structure(d, K, HK=None):
    """Exact description of V_d = Lam/L (Lam = Hodge kernel lattice): returns the classes of
    a Z-basis of Lam (mod 2, modulo L), an F_2-basis of V_d among them, and whether the
    Galois action on V_d is trivial (checked on unit-group generators and a Z-basis of Lam)."""
    if HK is None:
        HK = hodge_kernel_basis(d)
    classes = [K.cls(y) for y in HK]
    basis = {}
    for c in classes:
        b = c
        for piv, row in sorted(basis.items(), reverse=True):
            if b >> piv & 1:
                b ^= row
        if b:
            basis[b.bit_length() - 1] = b
    trivial = True
    for t in unit_group_generators(d):
        for y in HK:
            z = galois_fold(y, t, d)
            if K.cls([a - b for a, b in zip(z, y)]) != 0:
                trivial = False
                break
        if not trivial:
            break
    return {"dim_V": len(basis), "galois_trivial": trivial, "HK": HK, "classes": classes}
