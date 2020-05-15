//"Make a program that prints numbers from 0 to 1000, prints "fizz" when a number divisible by 3 and "buzz" when a number is divisible by 5"
//Coded by Estevao Neto
#include <stdio.h>
#include <stdlib.h>

void main(){
	int i;
	for(i = 0; i < 1001; i++){
		if(i%(3*5)==0) printf("fizzbuzz\t");
		else if(i%3==0) printf("fizz\t");
		else if(i%5==0) printf("buzz\t");
		else printf("%d\t", i);
	}
}