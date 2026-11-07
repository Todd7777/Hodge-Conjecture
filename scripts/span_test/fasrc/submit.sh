#!/bin/bash
# Usage (from this directory, on a FASRC login node): bash submit.sh [degree ...]
# Default degrees: the large ones that the cloud workers do not cover.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p logs out
if [ $# -gt 0 ]; then printf '%s\n' "$@" > degrees.txt; else
  printf '%s\n' 2772 2856 2860 3060 3080 3120 3168 3276 3432 3640 3696 3960 4004 4284 4368 4488 > degrees.txt
fi
n=$(wc -l < degrees.txt)
python3 ../run_degrees.py --validate --outdir out/validate --procs 1
sbatch --array=0-$((n - 1)) span_array.sbatch
echo "submitted $n degrees; watch with: squeue -u \$USER ; results: cat out/d*/results.jsonl"
