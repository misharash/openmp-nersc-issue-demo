// Simple program that keeps multiple CPUs busy
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <sched.h>
#include <time.h>

int main(int argc, char* argv[]) {
    assert(argc == 3);
    int n_threads = atoi(argv[1]);
    omp_set_num_threads(n_threads);
    int n_per_thread = atoi(argv[2]);
    printf("Running with %d threads, %d iterations on each\n", n_threads, n_per_thread);
    clock_t clock_time = clock();
    #pragma omp parallel for
    {
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
    printf("Elapsed time: %lf s\n", ((double)(clock() - clock_time)) / CLOCKS_PER_SEC);
}