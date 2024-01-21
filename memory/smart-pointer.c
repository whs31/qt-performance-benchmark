#include <stdint.h>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>

struct Data {
    uint64_t a;
    uint64_t b;
};

void initData(struct Data* data, uint64_t a, uint64_t b) {
    data->a = a;
    data->b = b;
}

int main() {
    struct timeval st, et;
    gettimeofday(&st,NULL);
    //
    {
        size_t i;
        struct Data** vec = (struct Data**)malloc(100000 * sizeof(void*));
        for (i = 0; i < 100000; ++i) {
            vec[i] = malloc(sizeof(struct Data));
            initData(vec[i], i, i / 2);
        }
        for (i = 0; i < 100000; ++i)
            free(vec[i]);
        free(vec);
    }
    //
    gettimeofday(&et,NULL);
    int elapsed = ((et.tv_sec - st.tv_sec) * 1000000) + (et.tv_usec - st.tv_usec);
    printf("%llu", elapsed);
    return 0;
}