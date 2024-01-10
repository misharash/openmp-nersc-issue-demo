#!/bin/bash
#SBATCH --account=desi
#SBATCH --constraint=cpu
#SBATCH --qos=regular
#SBATCH --time=00:05:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --job-name=openmp-issue-demo1

module load python

# OpenMP settings
export OMP_PROC_BIND=spread
export OMP_PLACES=threads
export OMP_NUM_THREADS=10

python -u demo.py