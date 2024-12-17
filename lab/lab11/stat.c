#include <stdio.h>
#include <sys/stat.h>

int main()
{
    printf("Size of struct stat: %zu!\n", sizeof(struct stat));
    return 0;
}