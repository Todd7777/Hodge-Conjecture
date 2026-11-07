#!/bin/bash
# ilp_run_main.sh -- the main run (two workers), as executed for results/fermat_span/ilp.md.
# Each line of results/fermat_span/ilp_main.jsonl is one (q, d) record written by ilp_main.py.
cd "$(dirname "$0")"
LOG=${ILP_WORK:-/tmp/claude-0/-home-user/449337f7-e47b-5016-b39e-f1ecd6549c95/scratchpad/ilpwork}
worker_a() {
  python3 ilp_main.py --q 44 --d 44,88,132,176,220,264,308,396,572,660 --threads 1
  python3 ilp_main.py --q 52 --d 52,104,156,208,260,312,364,468,572,780 --threads 1
  python3 ilp_main.py --q 44 --d 748,836,924,1012,1100,1188,1276 --threads 1
  python3 ilp_main.py --q 52 --d 884,988,1092,1196,1300 --threads 1
}
worker_b() {
  python3 ilp_main.py --q 51 --d 51,102,153,204,255,306,357,408,459,510,561,663,714 --threads 1
  python3 ilp_main.py --q 68 --d 68,136,204,272,340,408,476,612 --threads 1
  python3 ilp_main.py --q 51 --d 816,969,1020,1122,1173,1275 --threads 1
  python3 ilp_main.py --q 68 --d 748,884,1020,1292 --threads 1
}
case "$1" in
  a) worker_a ;;
  b) worker_b ;;
esac
