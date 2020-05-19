/******************************************************************************
This is Quick Sort.
*******************************************************************************/

#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <stdbool.h>
void generate_array(int *array, int array_size){
    srand(time(0));
    int i;
    for(i = 0; i < array_size; i++)
        array[i] = rand() % 100;
    return;
}

void print_array(int *array, int array_size){
    for(int i = 0; i < array_size; i++)
        printf("%d ", array[i]);
    printf("\n");
}

void quick_sort(int *array, int array_size){
    
}

int main(void) 
{
    int array_size;
    printf("QUICK SORT\n");
    printf("Enter array size:");
    scanf("%d", &array_size);
    int array[array_size];
    generate_array(&array[0], array_size);
    
    printf("Original array:");
    print_array(&array[0], array_size);
    quick_sort(&array[0], array_size);
    printf("Sorted array:");
    print_array(&array[0], array_size);
    return 0; 
} 