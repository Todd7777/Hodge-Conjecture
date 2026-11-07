/*
 * fs_enum.c -- enumerate all Hodge tuples of length 1..6 in R_d (MMRV arXiv:2609.27301, Def. 3.9)
 * and record their classes in an F_2-quotient given by K mod-2 functionals.
 *
 * A Hodge tuple of length L and degree d is a multiset {a_1 <= ... <= a_L} in [1, d-1] with
 *     sum_i <t a_i>_d = d L / 2   for every unit t of Z/d        (L odd only possible for d even).
 * The condition for d - t follows from the one for t, so only units 1 <= t < d/2 are tested.
 *
 * Classes: input file gives, for a = 1..d-1, a K-bit mask Vb[a] (bit j = value at (a) of the j-th
 * functional R_d -> F_2).  The class of a tuple is the XOR of Vb over its entries.
 *
 * Methods: lengths 1..5 by a depth-first search over sorted tuples with the right entry sum
 * (pruned by the sum); length 6 either by the same search (--dfs6) or by a meet-in-the-middle
 * join of the three smallest and the three largest entries, matched on the entry sums for t = 1
 * and for the two smallest units t1, t2 > 1 (default; O(d^3) instead of O(d^5)).
 *
 * --reduced: skip tuples containing d/2 or a pair {x, d-x}; such a tuple is the sum of eps_d or
 * (x)+(d-x) and a shorter Hodge tuple, so the span of all Hodge tuples of length <= 6 is the span
 * of the reduced ones together with D_d.  (Counts in this mode are counts of reduced tuples.)
 *
 * Usage: fs_enum d classfile|- [--reduced] [--dfs6] [--maxlen L] [--dump FILE]
 * Output: per length the number of Hodge tuples, and per (length, class) the count and the first
 * tuple found with that class (the witness).
 * Build: gcc -O2 -march=native -o fs_enum fs_enum.c
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static int d, nh, K = 0, reduced_only = 0, dfs6 = 0, maxlen = 6;
static int *hu;                 /* half units, hu[0] = 1 */
static int **mt;                /* mt[u][a] = (hu[u] * a) % d */
static uint64_t *Vb;            /* class bits of (a) */
static uint64_t cnt[7];
static uint64_t *sigcnt[7];
static int (*sigwit[7])[6];
static FILE *dumpf = NULL;
static int incnt[100000];       /* multiplicity of values in the current DFS prefix */

static int gcd_i(int a, int b) { while (b) { int t = a % b; a = b; b = t; } return a; }
static double now_s(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }

/* full Hodge test for units u >= from (u = 0 is t = 1, i.e. the plain sum) */
static int hodge_from(const int *a, int L, int from) {
    int tg = d * L;                                   /* 2 * sum must equal d L */
    for (int u = from; u < nh; u++) {
        const int *row = mt[u];
        int s = 0;
        for (int i = 0; i < L; i++) s += row[a[i]];
        if (2 * s != tg) return 0;
    }
    return 1;
}

static int reducible(const int *a, int L) {
    for (int i = 0; i < L; i++) {
        if (2 * a[i] == d) return 1;
        for (int j = i + 1; j < L; j++) if (a[i] + a[j] == d) return 1;
    }
    return 0;
}

static void record(const int *a, int L) {
    uint64_t s = 0;
    for (int i = 0; i < L; i++) s ^= Vb[a[i]];
    cnt[L]++;
    if (sigcnt[L][s]++ == 0) memcpy(sigwit[L][s], a, sizeof(int) * (size_t)L);
    if (dumpf) {
        fprintf(dumpf, "%d", L);
        for (int i = 0; i < L; i++) fprintf(dumpf, " %d", a[i]);
        fprintf(dumpf, "\n");
    }
}

/* ------------------------------------------------------------------ DFS over sorted tuples */
static int cur[6];
static void dfs(int i, int L, int s, int minv) {
    int target = d * L / 2, rem = L - i;
    if (rem == 1) {
        int v = target - s;
        if (v < minv || v > d - 1) return;
        if (reduced_only && (2 * v == d || incnt[d - v])) return;
        cur[i] = v;
        if (hodge_from(cur, L, 1)) record(cur, L);
        return;
    }
    int lo = target - s - (rem - 1) * (d - 1);
    if (lo < minv) lo = minv;
    int hi = (target - s) / rem;
    if (hi > d - 1) hi = d - 1;
    for (int v = lo; v <= hi; v++) {
        if (reduced_only && (2 * v == d || incnt[d - v])) continue;
        cur[i] = v;
        incnt[v]++;
        dfs(i + 1, L, s + v, v);
        incnt[v]--;
    }
}

/* ------------------------------------------------------------------ meet in the middle, L = 6 */
/* For a triple T with entry sum sigma_T and a unit t, s_t(T) = sum <t a> = t sigma_T - d N_t(T) with the
 * carry count N_t(T) = sum floor(t a / d).  For L (3 smallest entries) and R (3 largest) with
 * sigma_L + sigma_R = 3d, the Hodge condition s_t(L) + s_t(R) = 3d is N_t(L) + N_t(R) = 3(t - 1).
 * R is hashed on (N_t(R))_{t in KT}, KT = up to 40 half-units > 1; L looks up (3(t-1) - N_t(L))_t.
 * The hash is a fixed function of the carry vector, so no true match is missed; collisions only
 * cost extra (full) Hodge tests. */
#define MAXKT 40
typedef struct { int b[3]; uint64_t key; int next; } rtrip;
static rtrip *R = NULL; static size_t Rcap = 0;
static int *head = NULL; static uint32_t *stamp = NULL; static size_t hcap = 0; static uint32_t curstamp = 0;
static int nkt = 0, **fl = NULL;               /* fl[j][a] = floor(KT_j * a / d) */
static uint64_t kc[MAXKT], kt_off[MAXKT];      /* hash multipliers, 3(t-1) */

static void mitm_init(void) {
    nkt = nh - 1 < MAXKT ? nh - 1 : MAXKT;
    /* For a fixed entry sum each carry count N_t takes only ~3 values (N_t = (t sigma - s_t)/d with
     * 0 < s_t < 3d), i.e. ~1.6 bits per unit, so many units are needed for the hash to discriminate. */
    fl = malloc(sizeof(int *) * (size_t)(nkt > 0 ? nkt : 1));
    uint64_t x = 0x243F6A8885A308D3ULL;
    for (int j = 0; j < nkt; j++) {
        int t = hu[1 + (int)((long)j * (nh - 1) / nkt)];   /* nkt half-units > 1, spread over the list */
        fl[j] = malloc(sizeof(int) * (size_t)d);
        for (int a = 0; a < d; a++) fl[j][a] = (int)(((long)t * a) / d);
        x ^= x << 13; x ^= x >> 7; x ^= x << 17;
        kc[j] = x | 1ULL;
        kt_off[j] = 3ULL * (uint64_t)(t - 1);
    }
}
static inline uint64_t key_right(int b1, int b2, int b3) {
    uint64_t k = 0;
    for (int j = 0; j < nkt; j++) k += kc[j] * (uint64_t)(fl[j][b1] + fl[j][b2] + fl[j][b3]);
    return k;
}
static inline uint64_t key_left_complement(int a1, int a2, int a3) {
    uint64_t k = 0;
    for (int j = 0; j < nkt; j++) k += kc[j] * (kt_off[j] - (uint64_t)(fl[j][a1] + fl[j][a2] + fl[j][a3]));
    return k;
}

static void mitm6(void) {
    int target = 3 * d;
    mitm_init();
    if (hcap == 0) { hcap = 1u << 16; head = malloc(hcap * sizeof *head); stamp = calloc(hcap, sizeof *stamp); }
    int c6[6];
    for (int sigma = 3; 2 * sigma <= target; sigma++) {
        int S = target - sigma;
        int b1min = (sigma + 2) / 3;
        size_t nR = 0;
        /* right triples: b1 <= b2 <= b3 <= d-1, b1 >= ceil(sigma/3) (as b1 >= a3 >= sigma/3), sum S */
        int lo1 = S - 2 * (d - 1); if (lo1 < b1min) lo1 = b1min;
        for (int b1 = lo1; 3 * b1 <= S; b1++) {
            if (reduced_only && 2 * b1 == d) continue;
            int lo2 = S - b1 - (d - 1); if (lo2 < b1) lo2 = b1;
            for (int b2 = lo2; 2 * b2 <= S - b1; b2++) {
                int b3 = S - b1 - b2;
                if (reduced_only && (2 * b2 == d || 2 * b3 == d || b1 + b2 == d || b1 + b3 == d || b2 + b3 == d)) continue;
                if (nR == Rcap) { Rcap = Rcap ? 2 * Rcap : 4096; R = realloc(R, Rcap * sizeof *R); }
                R[nR].b[0] = b1; R[nR].b[1] = b2; R[nR].b[2] = b3; R[nR].key = key_right(b1, b2, b3); nR++;
            }
        }
        if (nR == 0) continue;
        while (hcap < 2 * nR) {
            free(head); free(stamp); hcap *= 2;
            head = malloc(hcap * sizeof *head); stamp = calloc(hcap, sizeof *stamp); curstamp = 0;
        }
        curstamp++;
        if (curstamp == 0) { memset(stamp, 0, hcap * sizeof *stamp); curstamp = 1; }
        size_t mask = hcap - 1;
        for (size_t r = 0; r < nR; r++) {
            size_t hsh = (size_t)((R[r].key * 0x9E3779B97F4A7C15ULL) >> 32) & mask;
            if (stamp[hsh] != curstamp) { stamp[hsh] = curstamp; head[hsh] = -1; }
            R[r].next = head[hsh]; head[hsh] = (int)r;
        }
        /* left triples a1 <= a2 <= a3 <= d-1 with sum sigma */
        for (int a1 = 1; 3 * a1 <= sigma; a1++) {
            if (reduced_only && 2 * a1 == d) continue;
            int lo2 = sigma - a1 - (d - 1); if (lo2 < a1) lo2 = a1;
            for (int a2 = lo2; 2 * a2 <= sigma - a1; a2++) {
                int a3 = sigma - a1 - a2;
                if (reduced_only && (2 * a2 == d || 2 * a3 == d || a1 + a2 == d || a1 + a3 == d || a2 + a3 == d)) continue;
                uint64_t key = key_left_complement(a1, a2, a3);
                size_t hsh = (size_t)((key * 0x9E3779B97F4A7C15ULL) >> 32) & mask;
                if (stamp[hsh] != curstamp) continue;
                for (int r = head[hsh]; r >= 0; r = R[r].next) {
                    if (R[r].key != key || R[r].b[0] < a3) continue;
                    c6[0] = a1; c6[1] = a2; c6[2] = a3; c6[3] = R[r].b[0]; c6[4] = R[r].b[1]; c6[5] = R[r].b[2];
                    if (reduced_only && reducible(c6, 6)) continue;
                    if (hodge_from(c6, 6, 1)) record(c6, 6);
                }
            }
        }
    }
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: %s d classfile|- [--reduced] [--dfs6] [--maxlen L] [--dump FILE]\n", argv[0]); return 1; }
    d = atoi(argv[1]);
    if (d < 3 || d >= 100000) { fprintf(stderr, "need 3 <= d < 100000\n"); return 1; }
    for (int i = 3; i < argc; i++) {
        if (!strcmp(argv[i], "--reduced")) reduced_only = 1;
        else if (!strcmp(argv[i], "--dfs6")) dfs6 = 1;
        else if (!strcmp(argv[i], "--maxlen") && i + 1 < argc) maxlen = atoi(argv[++i]);
        else if (!strcmp(argv[i], "--dump") && i + 1 < argc) { dumpf = fopen(argv[++i], "w"); if (!dumpf) { perror("dump"); return 1; } }
        else { fprintf(stderr, "bad option %s\n", argv[i]); return 1; }
    }
    hu = malloc(sizeof(int) * (size_t)d); nh = 0;
    for (int t = 1; 2 * t < d; t++) if (gcd_i(t, d) == 1) hu[nh++] = t;
    mt = malloc(sizeof(int *) * (size_t)nh);
    for (int u = 0; u < nh; u++) { mt[u] = malloc(sizeof(int) * (size_t)d); for (int a = 0; a < d; a++) mt[u][a] = (int)(((long)hu[u] * a) % d); }
    Vb = calloc((size_t)d, sizeof *Vb);
    if (strcmp(argv[2], "-")) {
        FILE *f = fopen(argv[2], "r");
        if (!f) { perror(argv[2]); return 1; }
        if (fscanf(f, "%d", &K) != 1 || K < 0 || K > 20) { fprintf(stderr, "bad class file header (K <= 20)\n"); return 1; }
        for (int a = 1; a < d; a++) {
            int aa; unsigned long long m;
            if (fscanf(f, "%d %llx", &aa, &m) != 2 || aa != a) { fprintf(stderr, "bad class file line for a=%d\n", a); return 1; }
            Vb[a] = m;
        }
        fclose(f);
    }
    size_t nsig = (size_t)1 << K;
    for (int L = 1; L <= 6; L++) { sigcnt[L] = calloc(nsig, sizeof(uint64_t)); sigwit[L] = calloc(nsig, sizeof(int[6])); }
    double t0 = now_s();
    for (int L = 1; L <= maxlen && L <= 6; L++) {
        if ((d * L) % 2) continue;
        double t1 = now_s();
        if (L == 6 && !dfs6) mitm6();
        else { memset(incnt, 0, sizeof(int) * (size_t)d); dfs(0, L, 0, 1); }
        fprintf(stderr, "  L=%d: %llu tuples (%.2fs)\n", L, (unsigned long long)cnt[L], now_s() - t1);
    }
    printf("d %d\nK %d\nmode %s %s\n", d, K, reduced_only ? "reduced" : "all", dfs6 ? "dfs6" : "mitm6");
    for (int L = 1; L <= 6; L++) printf("count %d %llu\n", L, (unsigned long long)cnt[L]);
    for (int L = 1; L <= 6; L++)
        for (size_t s = 0; s < nsig; s++)
            if (sigcnt[L][s]) {
                printf("sig %d %zx %llu", L, s, (unsigned long long)sigcnt[L][s]);
                for (int i = 0; i < L; i++) printf(" %d", sigwit[L][s][i]);
                printf("\n");
            }
    printf("seconds %.2f\n", now_s() - t0);
    if (dumpf) fclose(dumpf);
    return 0;
}
