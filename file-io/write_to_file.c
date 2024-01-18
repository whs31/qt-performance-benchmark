#include <stdio.h>
#include <stdint.h>

int main()
{
    printf("Starting 1000000 iterations!\n");
    FILE* fp;
    fp = fopen("test.txt", "wb");
    if(fp == NULL)
    {
        printf("Error!");
        return -1;
    }
    const uint64_t data = 0x123456789ABCDEF0;
    for(size_t i = 0; i < 1000000; i++)
    {
        fwrite(&data, sizeof(uint64_t), 1, fp);
    }
    fclose(fp);
    printf("Done!\n");
    remove("test.txt");
    return 0;
}