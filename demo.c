// Simple program that keeps multiple CPUs busy
#include <assert.h>
#include <stdio.h>
#include <omp.h>
#include <sched.h>

int main(int argc, char* argv[]) {
    assert(argc == 3);
    int n_threads = atoi(argv[1]);
    omp_set_num_threads(n_threads);
    int n_per_thread = atoi(argv[2]);
    #pragma omp parallel
    if (omp_get_thread_num() == 0) printf("Running with %d threads, %d iterations on each\n", omp_get_num_threads(), n_per_thread);
    #pragma omp for
    for (int t = 0; t < n_threads; t++) {
        int s = 0, x = 0, a = 0, o = 0;
        for (int ii = 0; ii < n_per_thread; ii++) {
            int i = n_per_thread * t + ii;
            s += i;
            x ^= i;
            a &= i;
            o |= i;
        }
    }
}