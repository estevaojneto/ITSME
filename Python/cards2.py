#Create a program that randomly distributes "X" cards from a deck (non-repeating)
#Coded by Estevao Neto

import sys, random
deck = []
suits = ["HEARTS", "SPADES", "CLUBS", "DIAMONDS"]

def deal_card():
    if len(deck) < 1:
        card_name = "(no more cards)"
    else:
        card_index = random.randrange(0,len(deck))
        card_no = int(deck[card_index]%13)
        #card 2 is the third card from the first suit; card 40 is the second card from the last suit, etc
        card_suit_id = int(deck[card_index]/13)
        #cards 0...12: A,2,3...J,Q,K of Hearts; cards 13...25:  1...K of Spades; etc
        deck.pop(card_index)
        card_name = str(card_no) + ' of ' + str(suits[card_suit_id])
    return card_name

for i in range(0,52):
        deck.append(i)
num_players = 13
if num_players > 13:
    print("Not enough cards for everyone!")
    exit()
for i in range(0,num_players):
    for j in range(0,4):
        print("Player", i+1,"gets a", deal_card())
