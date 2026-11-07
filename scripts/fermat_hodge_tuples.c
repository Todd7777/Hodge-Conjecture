/*
 * fermat_hodge_tuples.c -- list all sorted Hodge characters of a given length and degree.
 *
 * A tuple (a_1 <= ... <= a_L) of integers in [1, d-1] (L even) is a Hodge character of the Fermat
 * variety X^{L-2}_d if  sum_i (t a_i mod d) = (L/2) d  for every unit t mod d  (docs/04, section 4.1).
 * Since |(-t)alpha| = L - |t alpha|, it suffices to test one unit from each pair {t, -t}.
 *
 * Build:  gcc -O2 -o fermat_hodge_tuples scripts/fermat_hodge_tuples.c
 * Run:    ./fermat_hodge_tuples d L > out.txt      (one tuple per line, entries separated by spaces)
 * The last line written to stderr is "count <number of sorted Hodge tuples> leaves <tuples tested>".
 *
 * Part of the attack docs/attacks/17-fermat-open-cases.md (new file; does not modify existing code).
 */
#include <stdio.h>
#include <stdlib.h>

static int d, L, target, nu;
static int us[4096];
static int *mul;           /* mul[t*d + a] = t*a mod d for t in us (indexed by position) */
static int a[64];
static long long count = 0, leaves = 0;

static int gcd(int x, int y) { while (y) { int r = x % y; x = y; y = r; } return x; }

static void test_and_print(void) {
    leaves++;
    for (int k = 0; k < nu; k++) {
        const int *row = mul + (size_t)k * d;
        int s = 0;
        for (int i = 0; i < L; i++) s += row[a[i]];
        if (s != target) return;
    }
    count++;
    for (int i = 0; i < L; i++) printf(i ? " %d" : "%d", a[i]);
    printf("\n");
}

/* fill positions pos..L-1 with nondecreasing entries >= lo, remaining sum rem */
static void rec(int pos, int lo, int rem) {
    int left = L - pos;
    if (left == 1) {
        if (rem >= lo && rem <= d - 1) { a[pos] = rem; test_and_print(); }
        return;
    }
    int amin = lo, amax = rem / left;
    if (rem - (left - 1) * (d - 1) > amin) amin = rem - (left - 1) * (d - 1);
    if (amax > d - 1) amax = d - 1;
    for (int x = amin; x <= amax; x++) { a[pos] = x; rec(pos + 1, x, rem - x); }
}

int main(int argc, char **argv) {
    if (argc != 3) { fprintf(stderr, "usage: %s d L\n", argv[0]); return 1; }
    d = atoi(argv[1]); L = atoi(argv[2]);
    if (d < 2 || L < 2 || L % 2 || L > 64) { fprintf(stderr, "bad arguments\n"); return 1; }
    target = (L / 2) * d;
    nu = 0;
    for (int t = 2; t < d; t++)          /* t = 1 is the sum condition itself */
        if (gcd(t, d) == 1 && t <= d - t) us[nu++] = t;   /* one of each pair {t, -t} */
    mul = malloc(sizeof(int) * (size_t)nu * d);
    for (int k = 0; k < nu; k++) for (int x = 0; x < d; x++) mul[(size_t)k * d + x] = (us[k] * x) % d;
    rec(0, 1, target);
    fprintf(stderr, "count %lld leaves %lld\n", count, leaves);
    return 0;
}
