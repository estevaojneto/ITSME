//"Create a program that counts from x to y (where x > y) and prints whether each number is odd or even"
//Coded by Estevao Neto
#include <stdio.h>
void main(){
	int current, end;
	printf("Start number:");
	scanf("%d", &current);
	printf("End number:");
	scanf("%d", &end);
	for(current; current<=end; current++){ // we don't need to remember the initial state of the starting number;
	//this allows us to create a code with one less counter (int i) and saves us sizeof(int) bytes of memory
		printf("%d is an ", current);
		(current%2==0)? printf("even ") : printf("odd ");
		printf("number.\n");
	}
}
