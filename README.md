# openmp-nersc-issue-demo
Simplified example for a NERSC OpenMP issue.

First of all, one needs to build the `demo` executable (not doing anything meaningful but keeping each CPU core busy for about a second) with `make`, which should work out of the box at NERSC.

## Normal behavior
At NERSC, submit a batch job with `sbatch demo0.sh`, or request an interactive one with `bash demo_interactive.sh 0`.
Either only requests 5 minutes and should finish much faster.
For me, the clock time was almost 256 times larger than the wtime which I think means a pretty good parallelism.

## The issue
At NERSC, submit a batch job with `sbatch demo1.sh`, or request an interactive one with `bash demo_interactive.sh 1`.
Either only requests 5 minutes and should finish a bit faster.
The problem seems to be resolved by compiling the code into a shared library and loading it in Python through `ctypes`.
For me, the clock time is almost 256 times larger than the wtime -- seems like very good parallelism.
The above was on NERSC; on Mac the program hangs unless compiled with `-O1` when it runs too fast.
