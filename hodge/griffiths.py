"""Hodge numbers of smooth hypersurfaces via Griffiths' residue calculus.

Let X = {F = 0} be a smooth hypersurface of degree d in P^{n+1}, so dim X = n.  Griffiths (1969) identified the
primitive middle cohomology with graded pieces of the Jacobian ring

    R = C[x_0, ..., x_{n+1}] / (dF/dx_0, ..., dF/dx_{n+1}),

namely

    H^{n-q, q}_prim(X)  ~=  R_{(q+1) d - (n+2)}          (0 <= q <= n).

Since the partials of a smooth F form a regular sequence of n+2 forms of degree d-1, the Hilbert series of R is

    H_R(t) = ( (1 - t^{d-1}) / (1 - t) )^{n+2}  =  (1 + t + ... + t^{d-2})^{n+2},

so every primitive Hodge number is a coefficient of an explicit polynomial.  The total Hodge numbers of X are obtained
by adding the classes of powers of the hyperplane section:  h^{p,p}(X) = h^{p,p}_prim + 1 for 2p = n, and for 2p != n
the degree-2p cohomology is spanned by h^p (Lefschetz hyperplane theorem), so h^{p,p} = 1, h^{p,q} = 0 for p != q.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Dict, List, Tuple


def _poly_mul(a: List[int], b: List[int]) -> List[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


@lru_cache(maxsize=None)
def jacobian_ring_hilbert_series(n: int, d: int) -> Tuple[int, ...]:
    """Coefficients of ((1 - t^{d-1})/(1 - t))^{n+2}, i.e. dim R_k for the Jacobian ring of a smooth
    degree-d hypersurface in P^{n+1}."""
    if d < 1 or n < 0:
        raise ValueError("need d >= 1 and n >= 0")
    base = [1] * (d - 1)  # 1 + t + ... + t^{d-2}
    if d == 1:
        base = [1]  # degenerate: R = C, hypersurface is a hyperplane
    poly = [1]
    for _ in range(n + 2):
        poly = _poly_mul(poly, base)
    return tuple(poly)


def primitive_hodge_numbers(n: int, d: int) -> List[int]:
    """[h^{n,0}_prim, h^{n-1,1}_prim, ..., h^{0,n}_prim] for a smooth degree-d hypersurface of dimension n."""
    hs = jacobian_ring_hilbert_series(n, d)
    out = []
    for q in range(n + 1):
        k = (q + 1) * d - (n + 2)
        out.append(hs[k] if 0 <= k < len(hs) else 0)
    return out


def hodge_diamond(n: int, d: int) -> Dict[Tuple[int, int], int]:
    """Full Hodge numbers h^{p,q}(X) of a smooth degree-d hypersurface X of dimension n, as a dict."""
    prim = primitive_hodge_numbers(n, d)
    h: Dict[Tuple[int, int], int] = {}
    for p in range(n + 1):
        for q in range(n + 1):
            val = 0
            if p + q == n:
                val += prim[q]
            if p == q and p + q <= 2 * n:
                val += 1
            if val:
                h[(p, q)] = val
    return h


def middle_betti_number(n: int, d: int) -> int:
    """b_n(X) for a smooth degree-d hypersurface of dimension n."""
    b = sum(primitive_hodge_numbers(n, d))
    if n % 2 == 0:
        b += 1
    return b


def euler_characteristic(n: int, d: int) -> int:
    """Topological Euler characteristic of a smooth degree-d hypersurface of dimension n, computed from the
    Hodge diamond (as a cross-check it must agree with the closed formula ((1-d)^{n+2} - 1)/d + n + 2)."""
    h = hodge_diamond(n, d)
    return sum((-1) ** (p + q) * v for (p, q), v in h.items())


def euler_characteristic_closed_form(n: int, d: int) -> int:
    """chi_top(X) = ((1-d)^{n+2} - 1)/d + n + 2  (from c(T_X) = (1+h)^{n+2}/(1+dh))."""
    num = (1 - d) ** (n + 2) - 1
    assert num % d == 0
    return num // d + n + 2


def hodge_classes_dimension(n: int, d: int) -> int:
    """dim_Q of the space of rational Hodge classes in the middle cohomology H^n(X, Q) (n even) that the
    Hodge diamond alone predicts as an *upper bound*: it is h^{n/2,n/2}(X).  (Which of these classes are
    actually rational, i.e. the true Hodge number of the Hodge structure, depends on the specific X;
    for Fermat hypersurfaces see hodge.fermat.)"""
    if n % 2:
        return 0
    return hodge_diamond(n, d)[(n // 2, n // 2)]
