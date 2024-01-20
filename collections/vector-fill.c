#include <stdint.h>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>

struct Data {
    uint64_t a;
    uint64_t b;
};

void initData(struct Data* data, size_t x) {
    data->a = x / 2;
    data->b = x / (x % 2 + 1);
}

int main() {
    clock_t start_time = clock() / (CLOCKS_PER_SEC / 1000);
    //
    {
        size_t i;
        struct Data* vec = (struct Data*)malloc(5000000 * sizeof(struct Data));
        for (i = 0; i < 5000000; ++i)
            initData(&vec[i], i);
        free(vec);
    }
    //
    clock_t end_time = clock() / (CLOCKS_PER_SEC / 1000);
    double elapsed_time = (double)(end_time - start_time);
    printf("%lf", elapsed_time);
    return 0;
}