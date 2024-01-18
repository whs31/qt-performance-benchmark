#include <stdio.h>
#include <stdint.h>

typedef int (*callback_t)(int);

int q = 0;
void iota(callback_t cb)
{
    cb(q++);
}

int cb(int i)
{
    return i;
}

int main()
{
    // find sum of first 1000000 numbers via callback
    unsigned long long sum = 0;
    for(int i = 0; i < 1000000; i++)
    {
        sum += iota(cb);
    }
    return 0;
}