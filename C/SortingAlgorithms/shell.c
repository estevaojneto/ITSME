/******************************************************************************
This is Shell Sort.
Shell Sort is very similar to Insert Sort, the difference being that Insert
uses a gap size of 1 to compare each element and move accordingly, and Shell
uses a dynamic gap size - which can be calculated to an optimal value, but
for simplicity, we'll adopt an initial gap = array_size/2.
*******************************************************************************/

#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <math.h>
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

void shell_sort(int *array, int array_size){
    int gap = floor(array_size/2);
    int i, j, aux;
    while(gap > 0){
        for(i = gap; i < array_size; i++){
            aux = array[i];
            j = i;
            while((j>=gap) && (aux < array[j-gap])){
                array[j] = array[j-gap];
                j -= gap;
            }
            array[j] = aux;
        }
    gap = floor(gap/2);
    }
}

int main(void) 
{
    int array_size;
    printf("SHELL SORT\n");
    printf("Enter array size:");
    scanf("%d", &array_size);
    int array[array_size];
    generate_array(&array[0], array_size);
    
    printf("Original array:\n");
    print_array(&array[0], array_size);
    shell_sort(&array[0], array_size);
    printf("Sorted array:\n");
    print_array(&array[0], array_size);
    return 0; 
} 
/*A person very qualified in computer science once told me
Shell Sort has its name due to its nature of dividing the array 
sort of like a shell. Although this kinda makes sense, interestingly, 
it is actually because of scientist Donald Shell, who invented this method.
Just a bit of nerd history.*/