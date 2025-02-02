#include <stdio.h>
#include <stdlib.h>

int *create_static_array(int size)
{
    int arr[size];

    for (int i = 0; i < size; i++) {
        arr[i] = i;
    }

    return arr; // Wrong. The variable is freed after we exit the function.
}

int *create_dynamic_array(int size)
{
    int *arr = malloc(size * sizeof(int));

    for (int i = 0; i < size; i++) {
        arr[i] = i;
    }

    return arr;
}

int main()
{
    int size = 5;
    int *arr1 = create_static_array(size); // This pointer points to invalid memory.
    // int *arr2 = create_dynamic_array(size);

    for (int i = 0; i < size; i++) {
        printf("%d ", arr1[i]);
    }
    puts("");

    // for (int i = 0; i < size; i++) {
    //     printf("%d ", arr2[i]);
    // }
    // puts("");
    
    // free(arr2);

    // printf("%d\n", *p);

    return 0;
}