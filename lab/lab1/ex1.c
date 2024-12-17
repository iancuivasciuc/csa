#include<stdio.h>

int main()
{
    int x = 3;
    int y = 5;

    x = x ^ y;
    y = x ^ y;
    x = x ^ y;

    x = x + y;
    y = x - y;
    x = x - y;

    printf("x = %d, y = %d\n", x, y);

    return 0;
}