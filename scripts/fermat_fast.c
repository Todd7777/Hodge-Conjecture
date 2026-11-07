/*
 * fermat_fast.c -- Hodge characters of the Fermat variety X^n_m and Shioda's inductive structure.
 *
 * A compiled re-implementation of hodge/fermat.py (same criterion, same conventions, see
 * docs/04-fermat-computations.md section 4.2):
 *
 *   * Hodge characters B^n_m are enumerated up to permutation as sorted (n+2)-tuples
 *     a_0 <= ... <= a_{n+1} from [1, m-1] with  sum a_i = (n/2+1) m  and
 *     sum_i ((t a_i) mod m) = (n/2+1) m  for every unit t of Z/m.  The enumeration is pruned by
 *     the sum (every visited prefix extends to a tuple with the right sum).
 *   * dim Hdg^{n/2}(X^n_m) = 1 + sum over Hodge characters of their multiplicity
 *     (number of distinct permutations of the tuple).
 *   * A Hodge character alpha (length k = n+2) is DECOMPOSABLE if n in {0,2}, or if for some
 *     subset S of the coordinates with 0 in S and 2 <= |S| <= k-2, writing c = sum_S a_i mod m:
 *       (Z)  c == 0, |S| even:  beta' = alpha_S, gamma' = alpha_{S^c} are Hodge characters
 *                              (of X^{|S|-2}, X^{|S^c|-2}) and both are decomposable;
 *       (N)  c != 0, |S| odd, |S|,|S^c| >= 3:  beta = (alpha_S, -c), gamma = (alpha_{S^c}, c)
 *                              are Hodge characters (of X^{|S|-1}, X^{|S^c|-1}) and both are
 *                              decomposable.
 *     Only beta (resp. beta') is tested for being Hodge: gamma (resp. gamma') then is
 *     automatically Hodge (|t beta| + |t gamma| = |t alpha| + 1, resp. |t alpha|).
 *     Results are memoised on the canonical form (lexicographic minimum over the Galois action
 *     t in (Z/m)^* of the sorted tuple); decomposability is invariant under permutations and
 *     under the Galois action.
 *   * Output: dim Hdg, dim of the decomposable and indecomposable parts, number of orbits, and
 *     one representative (the canonical form) per orbit of indecomposable Hodge characters,
 *     in lexicographic order (exactly `indecomposable_orbits` of hodge.fermat.analyze).
 *
 * Usage:  fermat_fast n m [outfile]        (n even, 0 <= n <= 13, 2 <= m <= 255)
 * Build:  gcc -O2 -o fermat_fast fermat_fast.c
 */

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAXK 15          /* k = n + 2 <= 15 (key packing: 1 length byte + 15 entries = 16 bytes) */
#define MAXM 256

static int n, m, k, targetm;                 /* targetm = (n/2 + 1) * m = (k/2) * m */
static int units[MAXM], nunits;              /* (Z/m)^*, increasing, units[0] == 1 */
static int hunits[MAXM], nhunits;            /* units t with 2 <= t < m/2: enough for the Hodge test */
static unsigned char mul[MAXM][MAXM];        /* mul[t][a] = (t*a) mod m */
static uint64_t fact[MAXK + 1];

/* ------------------------------------------------------------------ statistics */
static uint64_t n_leaves = 0;        /* sorted tuples with the target sum */
static uint64_t n_hodge = 0;         /* sorted Hodge tuples */
static uint64_t hodge_mult = 0;      /* sum of their multiplicities = |B^n_m| */
static uint64_t n_indec = 0;         /* sorted indecomposable Hodge tuples */
static uint64_t indec_mult = 0;      /* sum of their multiplicities */

/* ------------------------------------------------------------------ small helpers */
static int gcd_int(int a, int b) { while (b) { int t = a % b; a = b; b = t; } return a; }

static void isort(unsigned char *a, int len) {
    for (int i = 1; i < len; i++) {
        unsigned char v = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > v) { a[j + 1] = a[j]; j--; }
        a[j + 1] = v;
    }
}

/* Is the tuple a (any order, entries in [1,m-1], length len) a Hodge character of X^{len-2}_m?
 * i.e. sum_i ((t a_i) mod m) == (len/2) m for every unit t.  The test for t = 1 is the plain sum;
 * the test for -t follows from the one for t (the two sums add up to len*m), so only the units
 * 2 <= t < m/2 are needed on top of the sum. */
static int is_hodge_full(const unsigned char *a, int len) {
    int tm = (len / 2) * m;
    int s = 0;
    for (int i = 0; i < len; i++) s += a[i];
    if (s != tm) return 0;
    for (int u = 0; u < nhunits; u++) {
        const unsigned char *row = mul[hunits[u]];
        s = 0;
        for (int i = 0; i < len; i++) s += row[a[i]];
        if (s != tm) return 0;
    }
    return 1;
}

/* multiplicity = number of distinct permutations of the sorted tuple a */
static uint64_t multiplicity(const unsigned char *a, int len) {
    uint64_t r = fact[len];
    int i = 0;
    while (i < len) {
        int j = i;
        while (j < len && a[j] == a[i]) j++;
        r /= fact[j - i];
        i = j;
    }
    return r;
}

/* canonical form: lexicographic minimum over all units t of sorted((t*a_i) mod m) */
static void canon(const unsigned char *a, int len, unsigned char *best) {
    unsigned char cand[MAXK];
    memcpy(best, a, (size_t)len);
    isort(best, len);                                  /* t = 1 */
    for (int u = 1; u < nunits; u++) {
        const unsigned char *row = mul[units[u]];
        int mn = 256;
        for (int i = 0; i < len; i++) { cand[i] = row[a[i]]; if (cand[i] < mn) mn = cand[i]; }
        if (mn > best[0]) continue;                   /* cannot beat the current minimum */
        isort(cand, len);
        if (memcmp(cand, best, (size_t)len) < 0) memcpy(best, cand, (size_t)len);
    }
}

/* ------------------------------------------------------------------ memo table (open addressing) */
typedef struct { uint64_t lo, hi; } hkey;            /* byte 0 = length, bytes 1..len = canonical tuple */

static hkey *tab_keys = NULL;
static unsigned char *tab_val = NULL;
static size_t tab_cap = 0, tab_cnt = 0;

static hkey make_key(const unsigned char *a, int len) {
    unsigned char buf[16];
    hkey key;
    memset(buf, 0, sizeof buf);
    buf[0] = (unsigned char)len;
    memcpy(buf + 1, a, (size_t)len);
    memcpy(&key, buf, sizeof key);
    return key;
}

static inline uint64_t mix64(uint64_t x) {
    x ^= x >> 30; x *= 0xbf58476d1ce4e5b9ULL;
    x ^= x >> 27; x *= 0x94d049bb133111ebULL;
    x ^= x >> 31;
    return x;
}
static inline uint64_t hash_key(hkey key) { return mix64(key.lo ^ mix64(key.hi + 0x9e3779b97f4a7c15ULL)); }
static inline int key_empty(hkey key) { return key.lo == 0 && key.hi == 0; }
static inline int key_eq(hkey a, hkey b) { return a.lo == b.lo && a.hi == b.hi; }

static void tab_init(size_t cap) {
    tab_cap = cap; tab_cnt = 0;
    tab_keys = calloc(cap, sizeof *tab_keys);
    tab_val = calloc(cap, 1);
    if (!tab_keys || !tab_val) { fprintf(stderr, "out of memory\n"); exit(2); }
}

static int tab_find(hkey key, size_t *pos) {
    size_t mask = tab_cap - 1, i = hash_key(key) & mask;
    while (!key_empty(tab_keys[i])) {
        if (key_eq(tab_keys[i], key)) { *pos = i; return 1; }
        i = (i + 1) & mask;
    }
    *pos = i;
    return 0;
}

static void tab_grow(void) {
    hkey *ok = tab_keys; unsigned char *ov = tab_val; size_t oc = tab_cap;
    tab_init(oc * 2);
    for (size_t i = 0; i < oc; i++) {
        if (key_empty(ok[i])) continue;
        size_t pos;
        tab_find(ok[i], &pos);
        tab_keys[pos] = ok[i]; tab_val[pos] = ov[i]; tab_cnt++;
    }
    free(ok); free(ov);
}

static void tab_insert(hkey key, int val) {
    size_t pos;
    if (2 * (tab_cnt + 1) > tab_cap) tab_grow();
    if (tab_find(key, &pos)) { tab_val[pos] = (unsigned char)val; return; }
    tab_keys[pos] = key; tab_val[pos] = (unsigned char)val; tab_cnt++;
}

/* ------------------------------------------------------------------ decomposability */
static int dec(const unsigned char *a, int len);

/* a is a canonical Hodge character of length len >= 6 (n >= 4). */
static int dec_compute(const unsigned char *a, int len) {
    unsigned char aS[MAXK + 1], aT[MAXK + 1];
    unsigned nmask = 1u << (len - 1);
    for (unsigned mask = 1; mask < nmask; mask++) {         /* S = {0} + {i+1 : bit i of mask} */
        int sizeS = 1 + __builtin_popcount(mask), sizeT = len - sizeS;
        if (sizeS < 2 || sizeT < 2) continue;
        int nS = 0, nT = 0, sS = 0;
        aS[nS++] = a[0]; sS += a[0];
        for (int i = 1; i < len; i++) {
            if (mask >> (i - 1) & 1u) { aS[nS++] = a[i]; sS += a[i]; }
            else aT[nT++] = a[i];
        }
        int c = sS % m;
        if (c == 0) {
            /* (Z): beta' = alpha_S in A^{|S|-2}, gamma' = alpha_T in A^{|T|-2}; both dims even */
            if (sizeS & 1) continue;
            if (!is_hodge_full(aS, sizeS)) continue;        /* then gamma' is not Hodge either */
            if (dec(aS, sizeS) && dec(aT, sizeT)) return 1;
        } else {
            /* (N): beta = (alpha_S, -c) in A^{|S|-1}, gamma = (alpha_T, c) in A^{|T|-1}; dims even, >= 2 */
            if (!(sizeS & 1)) continue;
            if (sizeS < 3 || sizeT < 3) continue;
            aS[nS] = (unsigned char)(m - c);
            aT[nT] = (unsigned char)c;
            if (!is_hodge_full(aS, sizeS + 1)) continue;    /* gamma is Hodge iff beta is */
            if (dec(aS, sizeS + 1) && dec(aT, sizeT + 1)) return 1;
        }
    }
    return 0;
}

/* a: a Hodge character (any order) of X^{len-2}_m.  Memoised on its canonical form. */
static int dec(const unsigned char *a, int len) {
    unsigned char c[MAXK];
    size_t pos;
    if (len <= 4) return 1;                          /* n = 0 (points) and n = 2 (Lefschetz (1,1)) */
    canon(a, len, c);
    hkey key = make_key(c, len);
    if (tab_find(key, &pos)) return tab_val[pos];
    int r = dec_compute(c, len);
    tab_insert(key, r);
    return r;
}

/* ------------------------------------------------------------------ enumeration of B^n_m */
static unsigned char cur[MAXK];
static const unsigned char *mul0 = NULL;     /* row of the first half-unit, tracked incrementally */
static double t_start;
static double now_sec(void) {
    struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + 1e-9 * (double)ts.tv_nsec;
}

static void handle_hodge(void) {
    uint64_t mult = multiplicity(cur, k);
    n_hodge++;
    hodge_mult += mult;
    if (!dec(cur, k)) { n_indec++; indec_mult += mult; }
}

/* cur[0..i-1] chosen with sum s, next entry >= minv; p0 = partial sum of mul0 over the prefix */
static void rec(int i, int s, int minv, int p0) {
    int rem = k - i;
    if (rem == 1) {
        int v = targetm - s;                    /* in [minv, m-1] by the pruning one level up */
        cur[i] = (unsigned char)v;
        n_leaves++;
        if (mul0 && p0 + mul0[v] != targetm) return;
        for (int u = 1; u < nhunits; u++) {
            const unsigned char *row = mul[hunits[u]];
            int t = 0;
            for (int j = 0; j < k; j++) t += row[cur[j]];
            if (t != targetm) return;
        }
        handle_hodge();
        return;
    }
    int lo = targetm - s - (rem - 1) * (m - 1);
    if (lo < minv) lo = minv;
    int hi = (targetm - s) / rem;
    for (int v = lo; v <= hi; v++) {
        cur[i] = (unsigned char)v;
        rec(i + 1, s + v, v, mul0 ? p0 + mul0[v] : 0);
        if (i == 0)
            fprintf(stderr, "  a0=%d done: leaves=%llu hodge=%llu indec_tuples=%llu memo=%zu (%.1fs)\n",
                    v, (unsigned long long)n_leaves, (unsigned long long)n_hodge,
                    (unsigned long long)n_indec, tab_cnt, now_sec() - t_start);
    }
}

/* ------------------------------------------------------------------ output */
typedef struct { unsigned char a[MAXK]; } orbit_t;
static int cmp_orbit(const void *x, const void *y) { return memcmp(x, y, (size_t)k); }

static void print_u128(FILE *f, unsigned __int128 v) {
    char buf[64]; int p = 63; buf[p] = 0;
    if (v == 0) buf[--p] = '0';
    while (v) { buf[--p] = (char)('0' + (int)(v % 10)); v /= 10; }
    fputs(buf + p, f);
}

static void report(FILE *f, double secs, orbit_t *orb, size_t norb, size_t hodge_orbits) {
    unsigned __int128 b = 1;
    for (int i = 0; i < k; i++) b *= (unsigned)(m - 1);
    if (k & 1) b -= (unsigned)(m - 1); else b += (unsigned)(m - 1);
    b /= (unsigned)m;
    fprintf(f, "# fermat_fast: Hodge characters of X^%d_%d and the Shioda-Katsura inductive structure\n", n, m);
    fprintf(f, "n %d\nm %d\n", n, m);
    fprintf(f, "b_prim "); print_u128(f, b); fprintf(f, "\n");
    fprintf(f, "phi_m %d\n", nunits);
    fprintf(f, "sorted_tuples_with_target_sum %llu\n", (unsigned long long)n_leaves);
    fprintf(f, "hodge_sorted_tuples %llu\n", (unsigned long long)n_hodge);
    fprintf(f, "hodge_orbits %zu\n", hodge_orbits);
    fprintf(f, "dim_hodge_classes %llu\n", (unsigned long long)(hodge_mult + 1));
    fprintf(f, "dim_decomposable %llu\n", (unsigned long long)(hodge_mult - indec_mult + 1));
    fprintf(f, "dim_indecomposable %llu\n", (unsigned long long)indec_mult);
    fprintf(f, "indecomposable_sorted_tuples %llu\n", (unsigned long long)n_indec);
    fprintf(f, "indecomposable_orbits %zu\n", norb);
    fprintf(f, "hodge_conjecture_verified_by_inductive_structure %s\n", indec_mult == 0 ? "True" : "False");
    fprintf(f, "memo_entries %zu\n", tab_cnt);
    fprintf(f, "seconds %.2f\n", secs);
    fprintf(f, "# indecomposable orbit representatives (canonical form = min over the Galois action of the sorted tuple), lexicographic order\n");
    for (size_t i = 0; i < norb; i++) {
        for (int j = 0; j < k; j++) fprintf(f, "%s%d", j ? " " : "", orb[i].a[j]);
        fprintf(f, "\n");
    }
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s n m [outfile]\n", argv[0]); return 1; }
    n = atoi(argv[1]); m = atoi(argv[2]);
    if (n < 0 || n & 1 || n + 2 > MAXK || m < 2 || m > 255) {
        fprintf(stderr, "need n even with 0 <= n <= %d and 2 <= m <= 255\n", MAXK - 2);
        return 1;
    }
    k = n + 2; targetm = (k / 2) * m;
    for (int t = 1; t < m; t++) if (gcd_int(t, m) == 1) units[nunits++] = t;
    for (int t = 2; 2 * t < m; t++) if (gcd_int(t, m) == 1) hunits[nhunits++] = t;
    for (int t = 0; t < m; t++) for (int a = 0; a < m; a++) mul[t][a] = (unsigned char)((t * a) % m);
    fact[0] = 1;
    for (int i = 1; i <= MAXK; i++) fact[i] = fact[i - 1] * (uint64_t)i;
    mul0 = nhunits ? mul[hunits[0]] : NULL;
    tab_init(1u << 16);

    t_start = now_sec();
    fprintf(stderr, "fermat_fast n=%d m=%d k=%d phi(m)=%d half-units=%d\n", n, m, k, nunits, nhunits);
    rec(0, 0, 1, 0);
    double secs = now_sec() - t_start;

    /* orbit representatives: memo entries of length k with value 0 (every top-level canonical form is in the memo) */
    size_t hodge_orbits = 0, norb = 0, cap = 1024;
    orbit_t *orb = malloc(cap * sizeof *orb);
    for (size_t i = 0; i < tab_cap; i++) {
        if (key_empty(tab_keys[i])) continue;
        unsigned char buf[16];
        memcpy(buf, &tab_keys[i], 16);
        if (buf[0] != (unsigned char)k) continue;
        hodge_orbits++;
        if (tab_val[i]) continue;
        if (norb == cap) { cap *= 2; orb = realloc(orb, cap * sizeof *orb); }
        memset(&orb[norb], 0, sizeof orb[norb]);
        memcpy(orb[norb].a, buf + 1, (size_t)k);
        norb++;
    }
    qsort(orb, norb, sizeof *orb, cmp_orbit);

    report(stdout, secs, orb, norb, hodge_orbits);
    if (argc >= 4) {
        FILE *f = fopen(argv[3], "w");
        if (!f) { perror(argv[3]); return 1; }
        report(f, secs, orb, norb, hodge_orbits);
        fclose(f);
    }
    free(orb);
    return 0;
}
