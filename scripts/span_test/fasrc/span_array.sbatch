#!/bin/bash
# SLURM array job for the span test on FASRC (Cannon). One array task = one degree.
# Submit with submit.sh (it writes degrees.txt and sets --array). Runs on compute nodes, never on a login node.
#SBATCH -J hodge-span
#SBATCH -p shared,serial_requeue
#SBATCH -c 8
#SBATCH --mem=32G
#SBATCH -t 0-12:00
#SBATCH -o logs/span_%A_%a.out
#SBATCH --requeue
set -euo pipefail
module load python >/dev/null 2>&1 || true
module load gcc >/dev/null 2>&1 || true
cd "$SLURM_SUBMIT_DIR"
DEG=$(sed -n "$((SLURM_ARRAY_TASK_ID + 1))p" degrees.txt)
REPO=$(cd ../../.. && pwd)
python3 -c "import flint, numpy" 2>/dev/null || python3 -m pip install --user --quiet python-flint numpy
echo "host $(hostname) degree $DEG cpus $SLURM_CPUS_PER_TASK start $(date)"
python3 "$REPO/scripts/span_test/run_degrees.py" --degrees "$DEG" --procs "$SLURM_CPUS_PER_TASK" --outdir "out/d$DEG"
echo "done $(date)"
