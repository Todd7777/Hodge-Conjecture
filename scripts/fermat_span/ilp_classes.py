"""ilp_classes.py -- exact class structure of V_d = B_d/(D_d + S~_d (+ extra algebraic)) and the
exhaustive search for short Hodge representatives (driver for ilp_short_hodge.c).

V_d is described through the mod-2 class map of ilp_core.Mod2Classes (validity checked exactly
by Mod2Classes.verify: Smith invariants in {1,2}, rank = Hodge-kernel rank).  A class is labelled
by the set of exceptional tuples xi_{q'} (q' | d, from the authors' CSV) whose sum it is; if the
xi's do not span V_d, the missing basis vectors are named eta1, eta2, ... (e.g. xi_660 at d=660,
which is not in the CSV because the CSV only lists products of two elements of P).
"""
import itertools
import os
import subprocess

import ilp_core as C

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.environ.get("ILP_WORK", "/tmp/claude-0/-home-user/449337f7-e47b-5016-b39e-f1ecd6549c95/scratchpad/ilpwork")
ENUM_BIN = os.path.join(WORK, "ilp_short_hodge")


def build_enum():
    src = os.path.join(HERE, "ilp_short_hodge.c")
    if not os.path.exists(ENUM_BIN) or os.path.getmtime(ENUM_BIN) < os.path.getmtime(src):
        subprocess.check_call(["gcc", "-O2", "-fopenmp", "-o", ENUM_BIN, src])


def _reduce_against(b, basis):
    for piv, row in sorted(basis.items(), reverse=True):
        if b >> piv & 1:
            b ^= row
    return b


class ClassSpace:
    """Exact F_2 description of V_d with labelled basis and 64-bit codes."""

    def __init__(self, d, extra=(), xi=None, check=True):
        self.d = d
        self.gens = C.generator_tuples(d, extra)
        self.K = C.Mod2Classes(d, self.gens)
        self.verify = self.K.verify() if check else None
        if check and not self.verify["ok"]:
            raise RuntimeError("mod-2 class test not valid at d=%d: %r" % (d, self.verify))
        st = C.quotient_structure(d, self.K)
        self.galois_trivial = st["galois_trivial"]
        self.dimV = st["dim_V"]
        X = C.read_tuples(C.EXC_CSV) if xi is None else xi
        self.qdivs = sorted(q for q in X if d % q == 0)
        self.xi = {q: C.lift(X[q], q, d) for q in self.qdivs}
        # labelled basis: xi's first (in increasing q), then Hodge-kernel classes as eta's
        self.labels, basis_cls = [], []
        ech = {}
        for q in self.qdivs:
            c = self.K.cls_tuple(self.xi[q])
            r = _reduce_against(c, ech)
            if r:
                ech[r.bit_length() - 1] = r
                self.labels.append("xi%d" % q)
                basis_cls.append(c)
        k = 0
        for c in st["classes"]:
            r = _reduce_against(c, ech)
            if r:
                ech[r.bit_length() - 1] = r
                k += 1
                self.labels.append("eta%d" % k)
                basis_cls.append(c)
        assert len(basis_cls) == self.dimV
        self.basis_cls = basis_cls
        # coordinates: choose dimV bit positions where the basis classes are independent
        rows = list(basis_cls)
        self.pos = []
        tmp = []
        for c in rows:
            for p0, r0 in tmp:
                if c >> p0 & 1:
                    c ^= r0
            if c:
                p0 = c.bit_length() - 1
                tmp.append((p0, c))
                self.pos.append(p0)
        assert len(self.pos) == self.dimV
        # table: code (bits at self.pos) -> label set, over all 2^dimV classes
        self.decode = {}
        for mask in range(1 << self.dimV):
            c = 0
            for i in range(self.dimV):
                if mask >> i & 1:
                    c ^= basis_cls[i]
            code = self.code_of_cls(c)
            assert code not in self.decode
            self.decode[code] = tuple(self.labels[i] for i in range(self.dimV) if mask >> i & 1)

    def code_of_cls(self, c):
        return sum(1 << i for i, p0 in enumerate(self.pos) if c >> p0 & 1)

    def code_of_tuple(self, tup):
        return self.code_of_cls(self.K.cls_tuple(tup))

    def label_of_tuple(self, tup):
        """Exact label (tuple of basis names) of a Hodge tuple's class."""
        assert C.is_hodge(tup, self.d), tup
        return self.decode[self.code_of_tuple(tup)]

    def write_codes(self, path):
        with open(path, "w") as f:
            for a in range(1, self.d):
                if 2 * a == self.d:
                    continue
                f.write("%d %d\n" % (a, self.code_of_cls(self.K.cls(C.fold((a,), self.d)))))

    def short_search(self, Lmax, nthreads=3, tag=None):
        """Run the exhaustive enumerator; returns {label: {L: (count, [examples])}}."""
        build_enum()
        tag = tag or "d%d" % self.d
        cpath = os.path.join(WORK, "codes_%s.txt" % tag)
        self.write_codes(cpath)
        out = subprocess.run([ENUM_BIN, str(self.d), str(Lmax), cpath, str(nthreads)],
                             capture_output=True, text=True, check=True)
        res = {}
        for line in out.stdout.splitlines():
            w = line.split()
            if w[0] == "C":
                L, code, cnt = int(w[1]), int(w[2]), int(w[3])
                lab = self.decode[code]
                res.setdefault(lab, {}).setdefault(L, [0, []])[0] += cnt
            elif w[0] == "E":
                L, code = int(w[1]), int(w[2])
                lab = self.decode[code]
                ex = tuple(int(x) for x in w[3:])
                # exact re-check of every reported example
                assert C.is_hodge(ex, self.d) and self.label_of_tuple(ex) == lab, ex
                res.setdefault(lab, {}).setdefault(L, [0, []])[1].append(ex)
        return res, out.stderr
