#include <stdint.h>
#include <stdlib.h>

struct Data {
    uint64_t a;
    uint64_t b;
};

void initData(struct Data* data, size_t x) {
    data->a = x / 2;
    data->b = x / (x % 2 + 1);
}

int main() {
    size_t i;
    struct Data* vec = (struct Data*)malloc(1000000 * sizeof(struct Data));

    for (i = 0; i < 1000000; ++i) {
        initData(&vec[i], i);
    }

    free(vec);
    return 0;
}