#!/bin/bash
#SBATCH --account=desi
#SBATCH --constraint=cpu
#SBATCH --qos=regular
#SBATCH --time=00:05:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --job-name=openmp-issue-demo1

# load cosmodesi environment
source /global/common/software/desi/users/adematti/cosmodesi_environment.sh main

# OpenMP settings
export OMP_PROC_BIND=spread
export OMP_PLACES=threads
export OMP_NUM_THREADS=256

# Limit OpenBLAS thread usage to avoid another issue
export OPENBLAS_NUM_THREADS=1

python -u demo.py