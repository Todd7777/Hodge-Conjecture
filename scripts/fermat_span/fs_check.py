"""fs_check.py -- independent checker for the span-test certificates in results/fermat_span/.

Deliberately self-contained: it does NOT import fs_lattice.py or fs_run.py.  Everything (units, the set Q,
lifts, Galois action, standard tuples of MMRV Definition 3.7, the Hodge condition) is re-implemented
here in a few lines.  The only shared input is the authors' exceptional_tuples.csv.

MEMBER certificate ('type member'): checks every 'gen' line against its label --
    hodge L entries : 1 <= L <= 6, entries in [1,d-1], d*L even, sum_i (t a_i mod d) = d*L/2 for ALL units t
    std p i d'      : p prime, d' | d, d' = p k' with k' >= 3, 1 <= i < d', p !| i, entries of s_{p,i} nonzero
                      mod d', and the tuple is the lift of s_{p,i} from degree d' to degree d
    xi q' t         : q' in Q, q' | d, q' != q, q' listed as known AND itself certified by a valid member
                      certificate cert_q<q'>_d*.txt in the same directory (checked recursively), t a unit,
                      tuple = t . lift(xi_q') with xi_q' from the CSV
    lin a / eps     : (a, d-a) with 1 <= a < d/2 / (d/2) with d even
  and the exact identity  lift(xi_q) = sum coef * tuple  in Z^{d-1}.
NON-MEMBER certificate ('type nonmember', modulus 2, set U): checks U = -U, d/2 not in U, an odd number of
  entries of lift(xi_q) in U, an even number for every lifted standard tuple of every divisor of d and for
  every G_d-conjugate of every known xi_q', and -- through the independent C program fs_dfs_check
  (compiled on the fly) -- for EVERY Hodge tuple of length 1..6 in degree d.  It also reports whether the
  same U is even on the conjugates of ALL other xi_q' (q' in Q, q' | d, q' != q), i.e. whether the
  non-membership persists even if every other exceptional tuple of degree dividing d were algebraic.
Usage: python3 fs_check.py CERT [CERT ...]
"""
import csv
import os
import subprocess
import sys
import tempfile
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = "/home/user/mmiirandaaaa/length-reduction-functions/exceptional_tuples.csv"


def load_csv():
    out = {}
    with open(CSV) as f:
        r = csv.reader(f, delimiter="|")
        next(r)
        for row in r:
            out[int(row[0])] = [int(x) for x in row[1].split(",")]
    return out


def is_prime(n):
    return n >= 2 and all(n % k for k in range(2, int(n ** 0.5) + 1))


def in_Q(q):
    """q = product of an even number (>= 2) of distinct elements of {4} u {odd primes}."""
    m, parts = q, 0
    if m % 2 == 0:
        if m % 4 or (m // 4) % 2 == 0:
            return False          # 2 || q, or 8 | q: not allowed
        m //= 4
        parts += 1
    p = 3
    while m > 1:
        if p * p > m:
            p = m
        if m % p == 0:
            m //= p
            if m % p == 0:
                return False
            parts += 1
        p += 2 if p > 2 else 1
    return parts >= 2 and parts % 2 == 0


def hodge(tup, d):
    L = len(tup)
    if not 1 <= L <= 6 or (d * L) % 2 or any(not 1 <= a <= d - 1 for a in tup):
        return False
    return all(2 * sum((t * a) % d for a in tup) == d * L for t in range(1, d) if gcd(t, d) == 1)


def std_tuple(p, i, dp, d):
    k = dp // p
    if p == 2:
        s = [i, k + i, dp - 2 * i, k]
    else:
        s = [i + j * k for j in range(p)] + [dp - p * i]
    s = [x % dp for x in s]
    if any(x == 0 for x in s):
        return None
    return sorted((d // dp) * x for x in s)


def all_standards(d):
    out = []
    for dp in range(2, d + 1):
        if d % dp:
            continue
        for p in range(2, dp + 1):
            if dp % p or not is_prime(p) or dp // p < 3:
                continue
            for i in range(1, dp):
                if i % p:
                    s = std_tuple(p, i, dp, d)
                    if s is not None:
                        out.append(((p, i, dp), s))
    return out


def xi_conj(X, qp, t, d):
    return sorted((t * (d // qp) * a) % d for a in X[qp])


def parse(path):
    info, gens = {}, []
    for line in open(path):
        if line.startswith("#") or not line.strip():
            continue
        w = line.split()
        if w[0] == "gen":
            gens.append(w[1:])
        elif w[0] == "end":
            break
        else:
            info[w[0]] = w[1:]
    return info, gens


def check_member(path, X, stack=()):
    info, gens = parse(path)
    q, d = int(info["q"][0]), int(info["d"][0])
    assert info["type"] == ["member"]
    assert in_Q(q) and d % q == 0, "q not in Q or q does not divide d"
    assert [int(x) for x in info["xi_q"]] == X[q], "xi_q differs from the CSV"
    known = [] if info["known"] == ["-"] else [int(x) for x in info["known"][0].split(",")]
    total = [0] * (d - 1)
    kinds = {}
    for g in gens:
        coef, kind = int(g[0]), g[1]
        if kind == "hodge":
            tup = [int(x) for x in g[2:]]
            assert hodge(tup, d), f"not a Hodge tuple of length <= 6: {tup}"
        elif kind == "std":
            p, i, dp = int(g[2]), int(g[3]), int(g[4])
            tup = [int(x) for x in g[5:]]
            assert is_prime(p) and d % dp == 0 and dp % p == 0 and dp // p >= 3 and 1 <= i < dp and i % p
            assert std_tuple(p, i, dp, d) == sorted(tup), f"bad standard tuple {g}"
        elif kind == "xi":
            qp, t = int(g[2]), int(g[3])
            tup = [int(x) for x in g[4:]]
            assert qp in known and qp != q and in_Q(qp) and d % qp == 0 and gcd(t, d) == 1
            assert xi_conj(X, qp, t, d) == sorted(tup)
        elif kind == "lin":
            a = int(g[2])
            tup = [int(x) for x in g[3:]]
            assert 1 <= a and 2 * a < d and tup == [a, d - a]
        elif kind == "eps":
            tup = [int(x) for x in g[2:]]
            assert d % 2 == 0 and tup == [d // 2]
        else:
            raise AssertionError(f"unknown generator kind {kind}")
        kinds[kind] = kinds.get(kind, 0) + 1
        for a in tup:
            total[a - 1] += coef
    mult = int(info.get("multiple", ["1"])[0])
    if info.get("scope") == ["DS"]:
        assert all(k in ("std", "lin", "eps") for k in kinds), "scope DS allows only standard and linear generators"
        assert d == q, "the Kubert-Aoki check is in degree q"
    target = [0] * (d - 1)
    for a in xi_conj(X, q, 1, d):
        target[a - 1] += mult
    assert total == target, "identity lift(xi_q) = sum coef*gen FAILS"
    # every known xi_q' must itself be certified (recursively)
    used = sorted({int(g[2]) for g in gens if g[1] == "xi"})
    dirn = os.path.dirname(os.path.abspath(path))
    for qp in used:
        assert qp not in stack, "circular certificate"
        cands = sorted(f for f in os.listdir(dirn) if f.startswith(f"cert_q{qp}_d"))
        assert cands, f"no certificate for known xi_{qp}"
        check_member(os.path.join(dirn, cands[0]), X, stack + (q,))
    return q, d, kinds, used


def check_nonmember(path, X, dfs_bin):
    info, _ = parse(path)
    q, d = int(info["q"][0]), int(info["d"][0])
    assert info["type"] == ["nonmember"] and info["modulus"] == ["2"]
    assert in_Q(q) and d % q == 0 and [int(x) for x in info["xi_q"]] == X[q]
    known = [] if info["known"] == ["-"] else [int(x) for x in info["known"][0].split(",")]
    U = set(int(x) for x in info["U"])
    assert all(1 <= a < d for a in U) and all((d - a) in U for a in U) and (2 * (d // 2) != d or d // 2 not in U)
    chi = lambda tup: sum(1 for a in tup if a in U) % 2
    assert chi(xi_conj(X, q, 1, d)) == 1, "chi(xi_q) is not odd"
    for lab, s in all_standards(d):
        assert chi(s) == 0, f"chi odd on standard {lab}"
    if info.get("scope") == ["DS"]:
        return q, d, None, known, [], None
    units = [t for t in range(1, d) if gcd(t, d) == 1]
    for qp in known:
        assert qp != q and in_Q(qp) and d % qp == 0
        for t in units:
            assert chi(xi_conj(X, qp, t, d)) == 0, f"chi odd on {t}.xi_{qp}"
    others = [qp for qp in range(2, d + 1) if d % qp == 0 and in_Q(qp) and qp != q]
    all_others_even = all(chi(xi_conj(X, qp, t, d)) == 0 for qp in others for t in units)
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
        f.write(" ".join(map(str, sorted(U))) + "\n")
        uf = f.name
    out = subprocess.run([dfs_bin, str(d), uf], capture_output=True, text=True)
    os.unlink(uf)
    counts = {}
    viol = None
    for line in out.stdout.splitlines():
        w = line.split()
        if w[0] == "count":
            counts[int(w[1])] = int(w[2])
        elif w[0] == "violations":
            viol = int(w[1])
    assert viol == 0, f"chi odd on some Hodge tuple: {out.stdout}"
    return q, d, counts, known, others, all_others_even


def main(paths):
    X = load_csv()
    dfs_bin = os.path.join(tempfile.gettempdir(), f"fs_dfs_check_{os.getpid()}")
    subprocess.run(["gcc", "-O2", "-o", dfs_bin, os.path.join(HERE, "fs_dfs_check.c")], check=True)
    bad = 0
    for p in paths:
        try:
            hdr = parse(p)[0]
            if "type" not in hdr:
                print(f"skipped (not a certificate): {os.path.basename(p)}")
                continue
            typ = hdr["type"][0]
            if typ == "member":
                q, d, kinds, used = check_member(p, X)
                if parse(p)[0].get("multiple"):
                    print(f"VALID multiple  q={q} d={d}: {parse(p)[0]['multiple'][0]}*xi_q = explicit Z-combination of {kinds}  [{os.path.basename(p)}]")
                    continue
                print(f"VALID member     q={q} d={d}: lift(xi_q) = explicit Z-combination of {kinds}; known xi used: {used or 'none'}  [{os.path.basename(p)}]")
            else:
                q, d, counts, known, others, aoe = check_nonmember(p, X, dfs_bin)
                if counts is None:
                    print(f"VALID nonmember-of-D+S  q={q} d={d}: chi vanishes on every linear and lifted standard tuple, odd on xi_q  [{os.path.basename(p)}]")
                    continue
                print(f"VALID nonmember  q={q} d={d}: chi even on all {sum(counts.values())} Hodge tuples of length<=6 "
                      f"(by length {counts}), standards, linear, known {known or 'none'}; odd on xi_q; "
                      f"also even on all other xi_q' {others}: {aoe}  [{os.path.basename(p)}]")
        except AssertionError as e:
            bad += 1
            print(f"INVALID {p}: {e}")
    os.unlink(dfs_bin)
    return bad


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1:]) else 0)
