/******************************************************************************
This is Insert Sort.
Putting it simply, Insert Sort will move the array items to accomodate a certain
element; it is good when there are few items to sort and/or the items are
somewhat already sorted. Disadvantage comes up when a list is very entropic and
large, as it must shuffle items almost every time to accomodate a certain item.
*******************************************************************************/

#include <stdio.h>
#include <time.h>
#include <stdlib.h>

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

void insert_sort(int *array, int array_size){
    int i, j, k;
    for(i < 1; i < array_size; i++){
        k = array[i];
        j = i - 1;
        while((j>=0) && (k < array[j])){
            array[j+1] = array[j];
            j = j - 1;
        }
        array[j+1] = k;
    }
}

int main(void) 
{
    int array_size;
    printf("INSERT SORT\n");
    printf("Enter array size:");
    scanf("%d", &array_size);
    int array[array_size];
    generate_array(&array[0], array_size);
    
    printf("Original array:");
    print_array(&array[0], array_size);
    insert_sort(&array[0], array_size);
    printf("Sorted array:");
    print_array(&array[0], array_size);
    return 0; 
}