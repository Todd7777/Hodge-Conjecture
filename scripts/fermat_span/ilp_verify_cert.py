"""ilp_verify_cert.py -- INDEPENDENT checker for congruence certificates (does not import ilp_core).

A certificate for (q, d, beta) is a list of terms [origin, c] with origin either
   ["std", dp, p, i]  : the standard tuple s_{p,i} of MMRV Definition 3.7 in degree dp = p*k
                        (k >= 3, p prime, p does not divide i), lifted to degree d, or
   ["xi", qq]         : the exceptional tuple xi_qq of the authors' CSV (only for qq proven algebraic
                        by MMRV, Theorem 4.4: 12,15,20,21,28,33,35,39,55,57), lifted to degree d.
It certifies  xi_q - beta - sum c * origin  in  D_d,  i.e. that the integer vector
   v(a) = #a in xi_q - #a in beta - sum_terms c * #a in tuple
satisfies v(a) = v(d - a) for all a (then it is sum v(a)((a)+(-a)) + v(d/2)(d/2) in D_d).
The checker also tests the Hodge condition for beta and xi_q with every unit of Z/d.
"""
import csv
import json
import sys
from math import gcd

ALGEBRAIC = {12, 15, 20, 21, 28, 33, 35, 39, 55, 57}


def is_prime(n):
    return n > 1 and all(n % k for k in range(2, int(n ** 0.5) + 1))


def csv_tuples(path):
    out = {}
    with open(path) as f:
        r = csv.reader(f, delimiter="|")
        next(r)
        for row in r:
            out[int(row[0])] = [int(x) for x in row[1].split(",")]
    return out


def std(dp, p, i):
    assert is_prime(p) and dp % p == 0 and dp // p >= 3 and i % p != 0, (dp, p, i)
    k = dp // p
    if p == 2:
        t = [i, k + i, -2 * i, k]
    else:
        t = [i + j * k for j in range(p)] + [-p * i]
    t = [x % dp for x in t]
    assert all(x != 0 for x in t)
    return t


def hodge(t, d):
    L = len(t)
    if L * d % 2 or any(x % d == 0 for x in t):
        return False
    return all(sum((u * x) % d for x in t) == L * d // 2 for u in range(1, d) if gcd(u, d) == 1)


def check(q, d, beta, terms, csvpath):
    X = csv_tuples(csvpath)
    v = [0] * d
    for x in X[q]:
        v[(x * (d // q)) % d] += 1
    for x in beta:
        v[x % d] -= 1
    for origin, c in terms:
        if origin[0] == "std":
            _, dp, p, i = origin
            assert d % dp == 0
            t = [(x * (d // dp)) % d for x in std(dp, p, i)]
        elif origin[0] == "xi":
            qq = origin[1]
            assert qq in ALGEBRAIC and qq != q and d % qq == 0, origin
            t = [(x * (d // qq)) % d for x in X[qq]]
        else:
            raise ValueError(origin)
        for x in t:
            v[x] -= c
    congruent = all(v[a] == v[d - a] for a in range(1, d))
    return {"congruent_mod_D": congruent, "beta_hodge": hodge(beta, d),
            "xi_hodge": hodge([(x * (d // q)) % d for x in X[q]], d), "length": len(beta),
            "nterms": len(terms)}


if __name__ == "__main__":
    # usage: ilp_verify_cert.py certificates.json [csv]
    path = sys.argv[1]
    csvp = sys.argv[2] if len(sys.argv) > 2 else \
        "/home/user/mmiirandaaaa/length-reduction-functions/exceptional_tuples.csv"
    allok = True
    for c in json.load(open(path)):
        r = check(c["q"], c["d"], c["beta"], c["terms"], csvp)
        ok = r["congruent_mod_D"] and r["beta_hodge"] and r["xi_hodge"]
        allok &= ok
        print(c["q"], c["d"], c["beta"], r, "OK" if ok else "FAIL")
    print("ALL OK" if allok else "SOME FAILED")
