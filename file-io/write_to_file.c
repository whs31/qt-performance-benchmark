#include <stdio.h>
#include <stdint.h>

int main()
{
    printf("[ C ] Starting 1'000'000 writes to file\n");
    FILE* fp;
    fp = fopen("test.junk", "wb");
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
    printf("[ C ] Done!\n");

    printf("[ C ] Cleaning up...\n");
    int a = remove("test.junk");
    if(a != 0)
        perror("[ C ] Failed to remove file!");
    else
        printf("[ C ] Done!\n");
    return 0;
}