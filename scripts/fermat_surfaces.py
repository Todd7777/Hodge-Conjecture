"""Picard numbers of Fermat surfaces vs. the rank of the lattice spanned by lines.  Writes results/fermat_surfaces.md."""
import sys
import time

sys.path.insert(0, ".")
from hodge import fermat, fermat_lines

M_EXACT = int(sys.argv[1]) if len(sys.argv) > 1 else 8     # exact rank over Q up to this m
M_MODP = int(sys.argv[2]) if len(sys.argv) > 2 else 12     # rank mod two large primes beyond that
rows = []
for m in range(3, M_MODP + 1):
    t = time.time()
    G = fermat_lines.gram_matrix(m)
    if m <= M_EXACT:
        r, how = fermat_lines.rank_over_Q(G), "exact (Q)"
    else:
        r1 = fermat_lines.rank_mod_p(G, 2147483647)
        r2 = fermat_lines.rank_mod_p(G, 2147483629)
        r, how = max(r1, r2), "mod p (two primes)" + ("" if r1 == r2 else " DISAGREE")
    rho = fermat.picard_number_fermat_surface(m)
    std = fermat_lines.shioda_line_rank_formula(m)
    rows.append((m, 3 * m * m, r, std, rho, rho - r, how, round(time.time() - t, 1)))
    print(rows[-1], flush=True)
with open("results/fermat_surfaces.md", "w") as f:
    f.write("# Fermat surfaces S_m: lines versus the full Picard number\n\n")
    f.write("`rank(lines)` is the rank of the Gram matrix of the 3m^2 lines (hodge.fermat_lines); `Shioda` is "
            "3(m-1)(m-2)+1+[m even]; `rho` = |B^2_m| + 1 is the Picard number computed from Hodge characters "
            "(every Hodge class on a surface is algebraic by Lefschetz (1,1)); `rho - rank` is the dimension of "
            "NS (x) Q not spanned by lines (Aoki-Shioda curves are needed there).\n\n")
    f.write("| m | #lines | rank(lines) | Shioda formula | rho(S_m) | rho - rank | rank method | s |\n|---|---|---|---|---|---|---|---|\n")
    for row in rows:
        f.write("| " + " | ".join(map(str, row)) + " |\n")
print("wrote results/fermat_surfaces.md")
