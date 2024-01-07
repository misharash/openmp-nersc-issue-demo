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
For me, the clock time (same as in previous case) is very close to the wtime which seems to indicate the C++ code is only given one CPU core/hyperthread after `sklearn.cluster.KMeans` usage in `demo.py`.

## Another issue (likely related)
You might wonder why I am setting `OPENBLAS_NUM_THREADS=1` in `demo1.sh`.
That is because otherwise the Python script fails complaining that OpenBlas is using too many threads or allocating too many memory region.
You can see this at NERSC by submitting a batch job with `sbatch demo2.sh`, or request an interactive one with `bash demo_interactive.sh 2`.

## Remarks and warnings
At the moment cases 1 and 2 are using the `cosmodesi` environment that might only be available to DESI members.
Please let me know if you know another common environment or module set that would have `scikit-learn`.
