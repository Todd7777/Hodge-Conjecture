"""Corollary G4 of docs/fermat/03-galois-obstruction.md: explicit square of the period of xi_q from the Kubert-Aoki certificate 2 xi_q = sum c_g g (g linear/standard/eps).
P(t) := prod_i Gamma(<a_i/d>) / (2 pi i)^{L/2}.  Closed forms:
  lin (a, d-a):            P = 1 / (2 i sin(pi a/d))
  eps (d/2) [length 1]:    Gamma(1/2) = sqrt(pi)    (paired: eps+eps is the linear pair (d/2,d/2) -> 1/(2i))
  std s_{p,i}, deg d'=pk:  P = p^{1/2 - r/k} / (2 sin(pi r/k) i^{(p+1)/2}),  r = i mod k        (p odd)
                           P = -2^{-1-r/k} / sin(pi r/k),                       r = i mod k        (p = 2)
Checks numerically (mpmath, 60 digits) that each closed form equals the Gamma product, and that
P(xi)^2 = prod P(g)^{c_g}."""
import sys
import mpmath as mp
mp.mp.dps = 60

def parse(path):
    gens, xi, d = [], None, None
    for line in open(path):
        w = line.split()
        if not w or line.startswith('#'): continue
        if w[0] == 'd': d = int(w[1])
        if w[0] == 'xi_q': xi = tuple(map(int, w[1:]))
        if w[0] == 'gen':
            c, kind = int(w[1]), w[2]
            if kind == 'std':
                p, i, dp = int(w[3]), int(w[4]), int(w[5]); tup = tuple(map(int, w[6:]))
                gens.append((c, 'std', (p, i, dp), tup))
            elif kind == 'lin':
                a = int(w[3]); tup = tuple(map(int, w[4:]))
                gens.append((c, 'lin', (a,), tup))
            elif kind == 'eps':
                gens.append((c, 'eps', (), (d // 2,)))
    return d, xi, gens

def gamma_prod(tup, d):
    v = mp.mpf(1)
    for a in tup:
        v *= mp.gamma(mp.mpf(a % d) / d)
    return v

def P_num(tup, d):
    return gamma_prod(tup, d) / (2 * mp.pi * 1j) ** (mp.mpf(len(tup)) / 2)

def P_closed(kind, data, d):
    if kind == 'lin':
        a, = data
        return 1 / (2j * mp.sin(mp.pi * a / d))
    if kind == 'std':
        p, i, dp = data
        k = dp // p; r = i % k
        if p == 2:
            return -mp.power(2, -1 - mp.mpf(r) / k) / mp.sin(mp.pi * r / k)
        return mp.power(p, mp.mpf(1) / 2 - mp.mpf(r) / k) / (2 * mp.sin(mp.pi * r / k) * (1j) ** ((p + 1) // 2))
    raise ValueError

def normal_form(path):
    """theta = 2^e2 * p^ep * prod_{a=1}^{D/2} sin(pi a / D)^{n_a}, with D the degree of the certificate."""
    from fractions import Fraction as Fr
    from collections import Counter
    d, xi, gens = parse(path)
    n = Counter(); rad = Counter(); sign = mp.mpc(1)
    def add_sin(num, den, e):
        a = num * (d // den)
        a %= 2 * d
        if a > d: a = 2 * d - a          # sin(pi a/d) up to sign
        if a > d // 2: a = d - a
        n[a] += e
    for c, kind, data, tup in gens:
        if kind == 'lin':
            add_sin(data[0], d, -c); rad[2] += -c                      # 1/(2 i sin)
        elif kind == 'eps':
            rad[2] += Fr(-c, 2)                                        # Gamma(1/2)/(2 pi i)^(1/2) = 1/sqrt(2i)
        elif kind == 'std':
            p, i, dp = data; k = dp // p; r = i % k
            add_sin(r, k, -c)
            if p != 2:
                rad[p] += c * (Fr(1, 2) - Fr(r, k)); rad[2] += -c        # p^(1/2-r/k) / (2 sin)
            else:
                rad[2] += c * (-1 - Fr(r, k))                          # 2^(-1-r/k) / sin
    n = {a: e for a, e in sorted(n.items()) if e}
    val = mp.mpf(1)
    for p, e in rad.items(): val *= mp.power(p, mp.mpf(e.numerator) / e.denominator)
    for a, e in n.items(): val *= mp.sin(mp.pi * a / d) ** e
    return d, dict(rad), n, val

def report(path):
    d, xi, gens = parse(path)
    worst, prod = 0, mp.mpc(1)
    for c, kind, data, tup in gens:
        if kind == 'eps':
            val = mp.sqrt(mp.pi) / mp.sqrt(2 * mp.pi * 1j)
        else:
            val = P_closed(kind, data, d)
            worst = max(worst, abs(val - P_num(tup, d)) / abs(val))
        prod *= val ** c
    Pxi = P_num(xi, d)
    d, rad, n, val = normal_form(path)
    lines = [f"## q = {d}: xi_q = {xi}",
             f"max relative error of the closed forms against the Gamma products: {mp.nstr(worst, 3)}",
             f"Gamma~(xi)^2            = {mp.nstr(Pxi ** 2, 30)}",
             f"product of closed forms = {mp.nstr(prod, 30)}",
             "normal form: theta = " + " * ".join(f"{p}^({e})" for p, e in sorted(rad.items()) if e) + " * "
             + " * ".join(f"s{a}^({e})" for a, e in n.items()) + f",  s_a = sin(pi a/{d});  |value| = {mp.nstr(abs(val), 30)}"]
    return "\n".join(lines)


if __name__ == "__main__":
    import os
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = [report(os.path.join(root, "results", "fermat_span", f"kubert_q{q}.txt")) for q in (44, 51, 52)]
    text = "# Squares of the Gamma-periods of xi_44, xi_51, xi_52 (python3 scripts/gamma_periods.py)\n\n" + "\n\n".join(out) + "\n"
    with open(os.path.join(root, "results", "gamma_periods.txt"), "w") as f:
        f.write(text)
    print(text)
