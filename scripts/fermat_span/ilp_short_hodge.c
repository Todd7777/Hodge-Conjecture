/* ilp_short_hodge.c -- exhaustive enumeration of all REDUCED Hodge tuples of length L <= Lmax
 * in degree d that contain a divisor g of d, with their classes modulo D_d + S~_d.
 *
 * Reduced: entries in (Z/d) - {0, d/2}, no two entries (counted with multiplicity) summing to 0.
 * Every Hodge tuple is congruent mod D_d to a reduced one of no greater length, and (since the
 * Galois action on B_d/(D_d+S~_d) is trivial, checked exactly in Python) every class reached by
 * a tuple is reached by a Galois conjugate containing a divisor g = gcd(a,d) of d.
 * Hence: min over (length of Hodge tuples in a class) <= Lmax is found EXACTLY.
 *
 * Method: tuple = {g} + left (rl smallest of the rest, enumerated) + right (rr largest, looked up
 * in a table keyed by a 64-bit linear hash of the Hodge signature).  Hash: H(a) = sum_t R_t
 * (2<ta> - d) mod 2^64 over units t < d/2; a Hodge tuple has sum H = 0.  Every hash match is
 * re-checked EXACTLY (sum_i <t a_i> = L d / 2 for all units t).  The hash cannot cause misses:
 * a Hodge tuple has hash sum exactly 0, so it is always looked up and found.  Pruning uses only
 * the exact t = 1 condition (sum of representatives in [1,d-1] equals L d / 2).
 *
 * Input file (codes): d-1 lines "a code" with the 64-bit class code of the symbol a (XOR-linear).
 * Output: lines  "C L code count"  and up to NEX example lines  "E L code a1 a2 ... aL".
 * Usage: ilp_short_hodge d Lmax codes_file [nthreads]
 * Build: gcc -O2 -fopenmp -o ilp_short_hodge ilp_short_hodge.c
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <omp.h>

#define NEX 4
#define MAXL 9
#define MAXCLS 4096

static int d, Lmax;
static int *symv, nsym;               /* symbols (values) in increasing order */
static uint64_t *H, *CODE;            /* indexed by value */
static int *U, nU;                    /* units t, 1 <= t < d/2 */

typedef struct { uint64_t key; uint16_t s[3]; } entry;
static entry *tab; static size_t ntab; static int bbits; static size_t *boff;

typedef struct { int L; uint64_t code; long long count; int nex; uint16_t ex[NEX][MAXL]; } clsrec;
typedef struct { clsrec r[MAXCLS]; int n; } accum;

static uint64_t splitmix(uint64_t *x) {
    uint64_t z = (*x += 0x9E3779B97F4A7C15ULL);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL; z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
    return z ^ (z >> 31);
}
static int gcdi(int a, int b) { while (b) { int t = a % b; a = b; b = t; } return a; }

static int exact_hodge(const int *a, int L) {
    if (((long)L * d) % 2) return 0;
    long target = (long)L * d / 2;
    for (int u = 0; u < nU; u++) {
        long s = 0; int t = U[u];
        for (int i = 0; i < L; i++) s += ((long)t * a[i]) % d;
        if (s != target) return 0;
    }
    return 1;
}
static int reduced_ok(const int *a, int L) {   /* no pair summing to 0 mod d */
    for (int i = 0; i < L; i++) for (int j = i + 1; j < L; j++) if ((a[i] + a[j]) % d == 0) return 0;
    return 1;
}
static int cmpentry(const void *x, const void *y) {
    uint64_t a = ((const entry *)x)->key, b = ((const entry *)y)->key;
    return a < b ? -1 : a > b;
}
static void record(accum *A, const int *a, int L) {
    uint64_t c = 0; for (int i = 0; i < L; i++) c ^= CODE[a[i]];
    int k;
    for (k = 0; k < A->n; k++) if (A->r[k].L == L && A->r[k].code == c) break;
    if (k == A->n) {
        if (A->n == MAXCLS) { fprintf(stderr, "too many classes\n"); exit(2); }
        A->n++; A->r[k].L = L; A->r[k].code = c; A->r[k].count = 0; A->r[k].nex = 0;
    }
    A->r[k].count++;
    if (A->r[k].nex < NEX) {
        int t[MAXL]; memcpy(t, a, sizeof(int) * L);
        for (int i = 1; i < L; i++) { int v = t[i], j = i - 1; while (j >= 0 && t[j] > v) { t[j + 1] = t[j]; j--; } t[j + 1] = v; }
        for (int i = 0; i < L; i++) A->r[k].ex[A->r[k].nex][i] = (uint16_t)t[i];
        A->r[k].nex++;
    }
}

/* build the table of all sorted rr-multisets (rr <= 3) of symbols without internal zero-sum pairs */
static void build_table(int rr) {
    free(tab); free(boff); ntab = 0;
    size_t cap = 1;
    if (rr == 1) cap = nsym; else if (rr == 2) cap = (size_t)nsym * (nsym + 1) / 2;
    else if (rr == 3) cap = (size_t)nsym * (nsym + 1) * (nsym + 2) / 6;
    tab = malloc(sizeof(entry) * (cap + 1));
    if (!tab) { fprintf(stderr, "out of memory for table (%zu)\n", cap); exit(3); }
    if (rr == 0) { tab[0].key = 0; ntab = 1; }
    else if (rr == 1) { for (int i = 0; i < nsym; i++) { tab[ntab].key = H[symv[i]]; tab[ntab].s[0] = symv[i]; ntab++; } }
    else if (rr == 2) {
        for (int i = 0; i < nsym; i++) for (int j = i; j < nsym; j++) {
            int a = symv[i], b = symv[j]; if ((a + b) % d == 0) continue;
            tab[ntab].key = H[a] + H[b]; tab[ntab].s[0] = a; tab[ntab].s[1] = b; ntab++; }
    } else {
        for (int i = 0; i < nsym; i++) for (int j = i; j < nsym; j++) {
            int a = symv[i], b = symv[j]; if ((a + b) % d == 0) continue;
            for (int k = j; k < nsym; k++) { int c = symv[k];
                if ((a + c) % d == 0 || (b + c) % d == 0) continue;
                tab[ntab].key = H[a] + H[b] + H[c]; tab[ntab].s[0] = a; tab[ntab].s[1] = b; tab[ntab].s[2] = c; ntab++; } }
    }
    qsort(tab, ntab, sizeof(entry), cmpentry);
    bbits = 1; while (((size_t)1 << bbits) < ntab && bbits < 30) bbits++;
    boff = calloc(((size_t)1 << bbits) + 1, sizeof(size_t));
    for (size_t i = 0; i < ntab; i++) boff[(tab[i].key >> (64 - bbits)) + 1]++;
    for (size_t b = 0; b < ((size_t)1 << bbits); b++) boff[b + 1] += boff[b];
}

/* enumerate sorted left multisets of size rl (symbols index >= lo), then look up the right part */
static void left_rec(accum *A, int g, int rl, int rr, int depth, int lo, int *a, uint64_t hsum, long psum, long long *nlook) {
    if (depth == rl) {
        uint64_t key = (uint64_t)0 - (H[g] + hsum);
        size_t b = key >> (64 - bbits);
        (*nlook)++;
        for (size_t e = boff[b]; e < boff[b + 1]; e++) {
            if (tab[e].key != key) continue;
            if (rl > 0 && rr > 0 && tab[e].s[0] < a[rl - 1]) continue;  /* split = smallest rl | largest rr */
            int t[MAXL]; int L = 0;
            t[L++] = g; for (int i = 0; i < rl; i++) t[L++] = a[i]; for (int i = 0; i < rr; i++) t[L++] = tab[e].s[i];
            if (!reduced_ok(t, L) || !exact_hodge(t, L)) continue;
            record(A, t, L);
        }
        return;
    }
    int L = 1 + rl + rr;
    long target = (long)L * d / 2;               /* t = 1: sum of representatives = L d / 2 */
    for (int i = lo; i < nsym; i++) {
        int v = symv[i];
        /* sorted: the L-1-depth entries still to come (this one included) are all >= v */
        if (psum + g + (long)(L - 1 - depth) * v > target) break;
        /* and all <= d-1 */
        if (psum + g + v + (long)(L - 2 - depth) * (d - 1) < target) continue;
        if ((v + g) % d == 0) continue;
        int bad = 0; for (int j = 0; j < depth; j++) if ((v + a[j]) % d == 0) { bad = 1; break; }
        if (bad) continue;
        a[depth] = v;
        left_rec(A, g, rl, rr, depth + 1, i, a, hsum + H[v], psum + v, nlook);
    }
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: %s d Lmax codes_file [nthreads]\n", argv[0]); return 1; }
    d = atoi(argv[1]); Lmax = atoi(argv[2]);
    if (Lmax > MAXL - 1) Lmax = MAXL - 1;
    if (argc > 4) omp_set_num_threads(atoi(argv[4]));
    H = calloc(d, sizeof(uint64_t)); CODE = calloc(d, sizeof(uint64_t));
    FILE *f = fopen(argv[3], "r"); if (!f) { perror("codes"); return 1; }
    int a; unsigned long long c;
    while (fscanf(f, "%d %llu", &a, &c) == 2) if (a > 0 && a < d) CODE[a] = c;
    fclose(f);
    symv = malloc(sizeof(int) * d); nsym = 0;
    for (int v = 1; v < d; v++) if (2 * v != d) symv[nsym++] = v;
    U = malloc(sizeof(int) * d); nU = 0;
    for (int t = 1; 2 * t < d; t++) if (gcdi(t, d) == 1) U[nU++] = t;
    uint64_t seed = 0x1234567ULL + (uint64_t)d * 1000003ULL;
    uint64_t *R = malloc(sizeof(uint64_t) * nU);
    for (int u = 0; u < nU; u++) R[u] = splitmix(&seed) | 1ULL;
    for (int v = 1; v < d; v++) {
        uint64_t h = 0;
        for (int u = 0; u < nU; u++) h += R[u] * (uint64_t)(int64_t)(2 * (int)(((long)U[u] * v) % d) - d);
        H[v] = h;
    }
    int *divs = malloc(sizeof(int) * d), ndiv = 0;
    for (int g = 1; g < d; g++) if (d % g == 0 && 2 * g != d) divs[ndiv++] = g;
    for (int L = 1; L <= Lmax; L++) {
        if (((long)L * d) % 2) continue;
        int rr = (L - 1) / 2, rl = L - 1 - rr;
        build_table(rr);
        int nthr = omp_get_max_threads();
        accum *acc = calloc(nthr, sizeof(accum));
        long long *nl = calloc(nthr, sizeof(long long));
        long nwork = (long)ndiv * (rl > 0 ? nsym : 1);
        #pragma omp parallel for schedule(dynamic, 1)
        for (long w = 0; w < nwork; w++) {
            int tid = omp_get_thread_num();
            int g = divs[rl > 0 ? w / nsym : w];
            int left[MAXL];
            if (rl == 0) { left_rec(&acc[tid], g, 0, rr, 0, 0, left, 0, 0, &nl[tid]); continue; }
            int i0 = w % nsym, v = symv[i0];
            if ((v + g) % d == 0) continue;
            if (g + (long)(L - 1) * v > (long)L * d / 2) continue;           /* sum pruning */
            if (g + v + (long)(L - 2) * (d - 1) < (long)L * d / 2) continue;
            left[0] = v;
            left_rec(&acc[tid], g, rl, rr, 1, i0, left, H[v], v, &nl[tid]);
        }
        accum *T = calloc(1, sizeof(accum)); long long looks = 0;
        for (int t = 0; t < nthr; t++) {
            looks += nl[t];
            for (int k = 0; k < acc[t].n; k++) {
                clsrec *r = &acc[t].r[k]; int j;
                for (j = 0; j < T->n; j++) if (T->r[j].L == r->L && T->r[j].code == r->code) break;
                if (j == T->n) { T->r[j] = *r; T->r[j].nex = 0; T->r[j].count = 0; T->n++; }
                T->r[j].count += r->count;
                for (int e = 0; e < r->nex && T->r[j].nex < NEX; e++) memcpy(T->r[j].ex[T->r[j].nex++], r->ex[e], sizeof(r->ex[e]));
            }
        }
        fprintf(stderr, "d=%d L=%d table=%zu lookups=%lld classes=%d\n", d, L, ntab, looks, T->n);
        for (int j = 0; j < T->n; j++) {
            printf("C %d %llu %lld\n", T->r[j].L, (unsigned long long)T->r[j].code, T->r[j].count);
            for (int e = 0; e < T->r[j].nex; e++) {
                printf("E %d %llu", T->r[j].L, (unsigned long long)T->r[j].code);
                for (int i = 0; i < T->r[j].L; i++) printf(" %d", T->r[j].ex[e][i]);
                printf("\n");
            }
        }
        fflush(stdout);
        free(acc); free(nl); free(T);
    }
    return 0;
}
