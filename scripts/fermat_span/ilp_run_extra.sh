#!/bin/bash
# ilp_run_extra.sh -- follow-up runs: lifts by p^2 (p = 11, 13, 17: where the order-p parity
# invariant of ilp.md section 5 stops being an invariant), larger composite lifts, and deep
# (length <= 8) exhaustive passes for odd degrees (only even lengths occur there).
cd "$(dirname "$0")"
case "$1" in
  p2)   python3 ilp_main.py --q 44 --d 484 --threads 1
        python3 ilp_main.py --q 52 --d 676 --threads 1
        python3 ilp_main.py --q 51 --d 867 --threads 1
        python3 ilp_main.py --q 68 --d 1156 --threads 1 ;;
  big)  python3 ilp_main.py --q 44 --d 1452,1540,1716 --threads 2 --ilp-time 300
        python3 ilp_main.py --q 52 --d 1404,1820 --threads 2 --ilp-time 300
        python3 ilp_main.py --q 51 --d 1326,1428 --threads 2 --ilp-time 300 ;;
  deep) python3 ilp_main.py --q 51 --d 51,153,255,357,459 --configs none --odd-deep-max 460 \
            --out ../../results/fermat_span/ilp_deep_odd.jsonl --threads 1 ;;
esac
