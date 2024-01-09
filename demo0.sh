#!/bin/bash
#SBATCH --account=desi
#SBATCH --constraint=cpu
#SBATCH --qos=regular
#SBATCH --time=00:05:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --job-name=openmp-issue-demo0

# OpenMP settings
export OMP_PROC_BIND=spread
export OMP_PLACES=threads
export OMP_NUM_THREADS=256
export OMP_DISPLAY_ENV=verbose
export OMP_DISPLAY_AFFINITY=true

./demo $OMP_NUM_THREADS $(python3 -c 'print(10**8)')