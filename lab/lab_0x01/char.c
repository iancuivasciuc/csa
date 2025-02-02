#include <stdio.h>

#include <sys/syscall.h>

int main(void)
{
    char *str1 = "salut";

    // printf("str1: %s\n", str1);

    char str2[] = { 'c', 'e', 'f', 'a', 'c', 'i' };
    char str3[] = { 'b', 'i', 'n', 'e', 't', 'u' };

    printf("str1: %s, str2: %s, str3: %s\n", str1, str2, str3);

    return 0;
}