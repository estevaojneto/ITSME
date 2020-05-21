var num_players = 4;
var qty_cards = 5;

var i, j;
var deck = [];
var suits = ["HEARTS", "SPADES", "CLUBS", "DIAMONDS"];

function deal_card(){  
	if(deck.length < 1)
		card_name = "(no more cards)"
	else{
		var min = Math.ceil(0);
		var max = Math.floor(deck.length);
		var card_index = Math.floor(Math.random() * (max - min)) + min;
		var card_no = parseInt(deck[card_index]%13);
		//card 2 is the third card from the first suit; card 40 is the second card from the last suit, etc
		var card_suit_id = parseInt(deck[card_index]/13);
		//cards 0...12: A,2,3...J,Q,K of Hearts; cards 13...25:  1...K of Spades; etc
		deck.pop(card_index);
		var card_name = card_no + ' of ' + suits[card_suit_id];		
	}
	return card_name;
}

for(i = 0; i < 52; i++)
	deck.push(i);

for(i = 0; i < num_players; i++)
	for(j = 0; j < qty_cards; j++)
		console.log("Player " + (i+1) + " gets a " + deal_card());
