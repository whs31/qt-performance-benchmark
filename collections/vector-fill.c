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
    struct timeval st, et;
    gettimeofday(&st,NULL);
    //
    {
        size_t i;
        struct Data* vec = (struct Data*)malloc(500000 * sizeof(struct Data));
        for (i = 0; i < 500000; ++i)
            initData(&vec[i], i);
        free(vec);
    }
    //
    gettimeofday(&et,NULL);
    int elapsed = ((et.tv_sec - st.tv_sec) * 1000000) + (et.tv_usec - st.tv_usec);
    printf("%llu", elapsed);
    return 0;
}