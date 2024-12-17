#include <stdio.h>

int main()
{
    const char *filename = "input.txt";

    FILE *file = fopen("input.txt", "r");

    int number1;
    int number2;

    if (fscanf(file, "%d %d", &number1, &number2) == 2) {
        printf("Number: %d, Word: %s\n", number1, number2);
    }
    else {
        printf("Failed!\n");
    }

    fclose(file);

    return 0;
}