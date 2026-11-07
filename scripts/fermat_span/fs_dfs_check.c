/*
 * fs_dfs_check.c -- independent check of a mod-2 dual certificate on ALL Hodge tuples of length 1..6.
 * Written separately from fs_enum.c: plain depth-first search over sorted tuples a_1 <= ... <= a_L in
 * [1, d-1] with sum d L / 2.  Partial sums of (t a_i mod d) are carried along the search for up to KT
 * units t (a quick necessary test); every surviving leaf is tested for EVERY unit t of Z/d, 1 < t < d
 * (no symmetry shortcut).  For each Hodge tuple the number of entries in U is counted; it must be even.
 * Usage: fs_dfs_check d Ufile      (Ufile: whitespace-separated elements of U; may be empty)
 * Output: "count L N" for L = 1..6 (all Hodge tuples), "violations V", the first violating tuples if any.
 * Build:  gcc -O2 -o fs_dfs_check fs_dfs_check.c
 */
#include <stdio.h>
#include <stdlib.h>

#define KT 6
static int d, L, nu, *un, *inU, nk;
static int *mk[KT];                       /* mk[j][x] = (un[j] * x) mod d */
static long long cnt[7], viol = 0;
static int a[6];

static int gcdi(int x, int y) { while (y) { int t = x % y; x = y; y = t; } return x; }

static void leaf(void) {
    for (int k = 0; k < nu; k++) {
        long t = un[k], s = 0;
        for (int i = 0; i < L; i++) s += (t * a[i]) % d;
        if (2 * s != (long)d * L) return;
    }
    cnt[L]++;
    int par = 0;
    for (int i = 0; i < L; i++) par ^= inU[a[i]];
    if (par) {
        if (viol < 10) { printf("violation"); for (int i = 0; i < L; i++) printf(" %d", a[i]); printf("\n"); }
        viol++;
    }
}

/* a[0..i-1] chosen, s = their sum, ps[j] = sum of mk[j][a_l]; next entry >= minv */
static void rec(int i, long s, int minv, const long *ps) {
    long target = (long)d * L / 2;
    int rem = L - i;
    if (rem == 1) {
        long v = target - s;
        if (v < minv || v > d - 1) return;
        for (int j = 0; j < nk; j++) if (ps[j] + mk[j][v] != target) return;
        a[i] = (int)v;
        leaf();
        return;
    }
    long lo = target - s - (long)(rem - 1) * (d - 1);
    if (lo < minv) lo = minv;
    long hi = (target - s) / rem;
    if (hi > d - 1) hi = d - 1;
    if (rem == 2) {                     /* last two entries v <= w = target - s - v: tight loop */
        for (long v = lo; v <= hi; v++) {
            long w = target - s - v;
            int ok = 1;
            for (int j = 0; j < nk; j++) if (ps[j] + mk[j][v] + mk[j][w] != target) { ok = 0; break; }
            if (!ok) continue;
            a[i] = (int)v; a[i + 1] = (int)w;
            leaf();
        }
        return;
    }
    long ps2[KT];
    for (long v = lo; v <= hi; v++) {
        a[i] = (int)v;
        for (int j = 0; j < nk; j++) ps2[j] = ps[j] + mk[j][v];
        rec(i + 1, s + v, (int)v, ps2);
    }
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s d Ufile\n", argv[0]); return 1; }
    d = atoi(argv[1]);
    if (d < 3 || d > 1000000) return 1;
    inU = calloc((size_t)d, sizeof(int));
    FILE *f = fopen(argv[2], "r");
    if (!f) { perror(argv[2]); return 1; }
    int x;
    while (fscanf(f, "%d", &x) == 1) { if (x < 1 || x >= d) { fprintf(stderr, "bad U element %d\n", x); return 1; } inU[x] = 1; }
    fclose(f);
    un = malloc(sizeof(int) * (size_t)d); nu = 0;
    for (int t = 2; t < d; t++) if (gcdi(t, d) == 1) un[nu++] = t;
    nk = nu < KT ? nu : KT;
    for (int j = 0; j < nk; j++) {
        mk[j] = malloc(sizeof(int) * (size_t)d);
        for (int y = 0; y < d; y++) mk[j][y] = (int)(((long)un[j] * y) % d);
    }
    long zero[KT] = {0};
    for (L = 1; L <= 6; L++) {
        if (((long)d * L) % 2) { cnt[L] = 0; continue; }
        rec(0, 0, 1, zero);
        fprintf(stderr, "  L=%d done: %lld Hodge tuples\n", L, cnt[L]);
    }
    for (int k = 1; k <= 6; k++) printf("count %d %lld\n", k, cnt[k]);
    printf("violations %lld\n", viol);
    return viol ? 2 : 0;
}
