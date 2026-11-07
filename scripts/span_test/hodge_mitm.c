/*
 * hodge_mitm.c -- enumerate the Hodge tuples of length L (4 or 6) in degree d by meet-in-the-middle,
 * and output their DISTINCT classes modulo the linear module D_d.
 *
 * A tuple (a_1..a_L), 1 <= a_i <= d-1, is Hodge iff sum_i (t a_i mod d) = L d / 2 for every unit t
 * (it suffices to check 1 <= t < d/2).  Split a sorted tuple into its first and last L/2 entries;
 * with h(a) = sum_t c_t (t a mod d) (random 64-bit c_t, wrapping arithmetic) a Hodge tuple satisfies
 * h(first half) + h(second half) = (L d/2) sum_t c_t.  Half-tuples with exact sums s and Ld/2 - s are
 * paired through a hash table on h, and EVERY candidate is then verified exactly for every unit, so
 * the output is exact: no Hodge tuple is missed (the hash identity holds exactly for them) and no
 * non-Hodge tuple is accepted.
 *
 * Reduction modulo D_d: (a) + (-a) and (d/2) lie in D_d, so a tuple's class is the multiset of signed
 * representatives a (if a < d/2) or -(d-a) (if a > d/2), entries d/2 dropped, opposite pairs cancelled.
 *
 * Usage: hodge_mitm d L outfile [rank nprocs [count_full]]
 *   rank/nprocs split the work over the first-half sum s (s % nprocs == rank).
 *   count_full = 1 also counts distinct sorted Hodge tuples (for validation against brute force).
 * Output: one line per distinct nonzero class: its sorted signed entries.  Summary on stderr.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int d, L, m, S, H, nu;
static int *units;
static uint16_t *tab;          /* tab[u*d + a] = units[u]*a mod d */
static uint64_t *h, K;

static int gcd(int a, int b) { while (b) { int r = a % b; a = b; b = r; } return a; }
static uint64_t sm_state = 0x9E3779B97F4A7C15ULL;
static uint64_t splitmix(void) { uint64_t z = (sm_state += 0x9E3779B97F4A7C15ULL); z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL; z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL; return z ^ (z >> 31); }

/* ---------- generic 128-bit-key hash set ---------- */
typedef struct { uint64_t *k1, *k2; size_t cap, n; } set128;
static void set_init(set128 *s, size_t cap) { s->cap = cap; s->n = 0; s->k1 = calloc(cap, 8); s->k2 = calloc(cap, 8); if (!s->k1 || !s->k2) { fprintf(stderr, "oom\n"); exit(2); } }
static size_t mix(uint64_t a, uint64_t b) { uint64_t z = a * 0x9E3779B97F4A7C15ULL ^ (b + 0x632BE59BD9B4E019ULL) * 0xC2B2AE3D27D4EB4FULL; z ^= z >> 29; return (size_t)z; }
static int set_add(set128 *s, uint64_t a, uint64_t b);
static void set_grow(set128 *s) {
    set128 t; set_init(&t, s->cap * 2);
    for (size_t i = 0; i < s->cap; i++) if (s->k1[i] | s->k2[i]) set_add(&t, s->k1[i], s->k2[i]);
    free(s->k1); free(s->k2); *s = t;
}
static int set_add(set128 *s, uint64_t a, uint64_t b) {   /* keys are never (0,0) */
    if (2 * (s->n + 1) > s->cap) set_grow(s);
    size_t i = mix(a, b) & (s->cap - 1);
    while (s->k1[i] | s->k2[i]) { if (s->k1[i] == a && s->k2[i] == b) return 0; i = (i + 1) & (s->cap - 1); }
    s->k1[i] = a; s->k2[i] = b; s->n++; return 1;
}

/* ---------- multimap from uint64 hash to half-tuples ---------- */
static uint64_t *mk; static int32_t *mv; static size_t mcap; static uint16_t *half; static size_t nhalf, halfcap;
static void mm_reset(size_t need) {
    size_t cap = 1024; while (cap < 2 * need + 16) cap <<= 1;
    if (cap > mcap) { free(mk); free(mv); mk = malloc(cap * 8); mv = malloc(cap * 4); mcap = cap; }
    for (size_t i = 0; i < cap; i++) mv[i] = -1;
    mcap = cap; nhalf = 0;
    if (need > halfcap) { halfcap = need + 16; free(half); half = malloc(halfcap * m * sizeof(uint16_t)); }
}
static void mm_add(uint64_t key, const int *a) {
    size_t i = (size_t)(key ^ (key >> 31)) & (mcap - 1);
    while (mv[i] >= 0) i = (i + 1) & (mcap - 1);
    mk[i] = key; mv[i] = (int32_t)nhalf;
    for (int j = 0; j < m; j++) half[nhalf * m + j] = (uint16_t)a[j];
    nhalf++;
}

static set128 classes, full;
static long long nverified = 0, ncand = 0;
static int count_full = 0;

static void emit(const int *a, const uint16_t *b) {
    int x[8], n = 0;
    for (int j = 0; j < m; j++) x[n++] = a[j];
    for (int j = 0; j < m; j++) x[n++] = b[j];
    /* exact verification for every unit t >= 2 (t = 1 holds by the sum) */
    ncand++;
    for (int u = 0; u < nu; u++) {
        const uint16_t *row = tab + (size_t)u * d; int s = 0;
        for (int j = 0; j < L; j++) s += row[x[j]];
        if (s != S) return;
    }
    nverified++;
    if (count_full) {            /* distinct sorted tuples */
        int y[8]; memcpy(y, x, sizeof(int) * L);
        for (int i = 1; i < L; i++) { int v = y[i], k = i - 1; while (k >= 0 && y[k] > v) { y[k + 1] = y[k]; k--; } y[k + 1] = v; }
        uint64_t k1 = 0, k2 = 0;
        for (int j = 0; j < 4 && j < L; j++) k1 |= (uint64_t)y[j] << (16 * j);
        for (int j = 4; j < L; j++) k2 |= (uint64_t)y[j] << (16 * (j - 4));
        set_add(&full, k1 | 1ULL << 63, k2);
    }
    /* reduce modulo D */
    int sg[8], ns = 0;
    for (int j = 0; j < L; j++) { int v = x[j]; if (2 * v == d) continue; sg[ns++] = (v <= H) ? v : -(d - v); }
    /* cancel opposite pairs */
    for (int i = 0; i < ns; i++) for (int k = i + 1; k < ns; k++) if (sg[i] != 0 && sg[i] == -sg[k]) { sg[i] = 0; sg[k] = 0; break; }
    int z[8], nz = 0; for (int i = 0; i < ns; i++) if (sg[i]) z[nz++] = sg[i];
    if (nz == 0) return;
    for (int i = 1; i < nz; i++) { int v = z[i], k = i - 1; while (k >= 0 && z[k] > v) { z[k + 1] = z[k]; k--; } z[k + 1] = v; }
    uint64_t k1 = (uint64_t)nz, k2 = 0;
    for (int j = 0; j < nz; j++) { uint64_t e = (uint64_t)(z[j] + 8192) & 0x3FFF; if (j < 4) k1 |= e << (4 + 14 * j); else k2 |= e << (14 * (j - 4)); }
    set_add(&classes, k1, k2);
}

/* enumerate sorted half-tuples (length m) with sum s, entries in [1, d-1] */
static void halves(int s, void (*cb)(const int *)) {
    int a[3];
    if (m == 2) {
        for (a[0] = s - (d - 1) > 1 ? s - (d - 1) : 1; 2 * a[0] <= s; a[0]++) { a[1] = s - a[0]; if (a[1] <= d - 1) cb(a); }
    } else {
        int lo0 = s - 2 * (d - 1); if (lo0 < 1) lo0 = 1;
        for (a[0] = lo0; 3 * a[0] <= s; a[0]++) {
            int r = s - a[0], lo1 = r - (d - 1); if (lo1 < a[0]) lo1 = a[0];
            for (a[1] = lo1; 2 * a[1] <= r; a[1]++) { a[2] = r - a[1]; cb(a); }
        }
    }
}
static uint64_t hh(const int *a) { uint64_t v = 0; for (int j = 0; j < m; j++) v += h[a[j]]; return v; }
static size_t cnt_halves; static void cnt_cb(const int *a) { (void)a; cnt_halves++; }
static void add_cb(const int *a) { mm_add(hh(a), a); }
static void probe_cb(const int *a) {
    uint64_t want = K - hh(a);
    size_t i = (size_t)(want ^ (want >> 31)) & (mcap - 1);
    while (mv[i] >= 0) { if (mk[i] == want) emit(a, half + (size_t)mv[i] * m); i = (i + 1) & (mcap - 1); }
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: %s d L outfile [rank nprocs [count_full]]\n", argv[0]); return 1; }
    d = atoi(argv[1]); L = atoi(argv[2]); const char *out = argv[3];
    int rank = argc > 5 ? atoi(argv[4]) : 0, np = argc > 5 ? atoi(argv[5]) : 1;
    count_full = argc > 6 ? atoi(argv[6]) : 0;
    if ((L != 4 && L != 6) || d < 3 || d > 8000) { fprintf(stderr, "need L in {4,6}, 3 <= d <= 8000\n"); return 1; }
    m = L / 2; S = L * d / 2; H = (d - 1) / 2;
    units = malloc(sizeof(int) * d); nu = 0;
    for (int t = 2; 2 * t < d; t++) if (gcd(t, d) == 1) units[nu++] = t;
    tab = malloc((size_t)nu * d * sizeof(uint16_t));
    for (int u = 0; u < nu; u++) for (int a = 0; a < d; a++) tab[(size_t)u * d + a] = (uint16_t)(((long)units[u] * a) % d);
    h = calloc(d, 8); K = 0;
    for (int u = 0; u < nu; u++) { uint64_t c = splitmix(); K += c * (uint64_t)S; for (int a = 1; a < d; a++) h[a] += c * (uint64_t)tab[(size_t)u * d + a]; }
    set_init(&classes, 1 << 16); if (count_full) set_init(&full, 1 << 16);
    for (int s = m; 2 * s <= S; s++) {
        if (s % np != rank) continue;
        int s2 = S - s;
        cnt_halves = 0; halves(s2, cnt_cb);
        if (cnt_halves == 0) continue;
        mm_reset(cnt_halves); halves(s2, add_cb);
        halves(s, probe_cb);
    }
    FILE *f = fopen(out, "w"); if (!f) { perror(out); return 1; }
    for (size_t i = 0; i < classes.cap; i++) {
        if (!(classes.k1[i] | classes.k2[i])) continue;
        uint64_t k1 = classes.k1[i], k2 = classes.k2[i]; int nz = (int)(k1 & 15);
        for (int j = 0; j < nz; j++) { uint64_t e = j < 4 ? (k1 >> (4 + 14 * j)) & 0x3FFF : (k2 >> (14 * (j - 4))) & 0x3FFF; fprintf(f, j ? " %d" : "%d", (int)e - 8192); }
        fprintf(f, "\n");
    }
    fclose(f);
    fprintf(stderr, "d=%d L=%d rank=%d/%d candidates=%lld verified=%lld classes=%zu", d, L, rank, np, ncand, nverified, classes.n);
    if (count_full) fprintf(stderr, " distinct_sorted_tuples=%zu", full.n);
    fprintf(stderr, "\n");
    return 0;
}
