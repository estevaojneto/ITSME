//"Create a program that randomly distributes "X" cards from a deck
//Coded by Estevao Neto
#include <stdio.h>
#include <stdlib.h>

char cardnumbers[14] = {'A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'};
char suit[4] = {'C', 'P', 'E', 'O'};
main(){
    time_t t;
    srand((unsigned) time(&t));
    int how_many_cards, i;
    printf("How many cards would you like to draw?");
    scanf("%d", &how_many_cards);
    for(i = 0; i < how_many_cards; i++)
        printf("%c %c; ", suit[rand() % 4], cardnumbers[rand() % 14]);
    //there is a gotcha here; there is a chance you'll draw the same card more than once if i > 1
    //this can be corrected by saving which cards were drawn into a hash table,
    //and making the code generate other pair of numbers and cards if a certain entry (e.g "C 7")
    //already exists on the table (i.e this card was already drawn)
    //in practice, it's very likely likelier you'll draw the same cards because rand() isn't too... Random
}
