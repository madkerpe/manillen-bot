import game
import cards
import random
import csv

from cards import Card
from game import Player, Pot

#Bot that plays games of manillen (https://en.wikipedia.org/wiki/Manille).  Used for machine learning

def new_game():
	Deck = cards.make_deck()
	random.shuffle(Deck)
	
	new_players = [Player(Deck[i*8: (i+1)*8], "Player" + str(i)) for i in range(4)]
	new_pot = Pot()

	return new_players, new_pot

def play_card(player_object, pot_object, card_object):
	player_object - card_object
	pot_object + card_object

def ronde(player_list, pot_object):
	for player in player_list:
		card = player.random_card()
		play_card(player, pot_object, card)
		print("%s played %s" % (player.name, card))

	pot_object.next_round()
	

def play_game(player_list, pot_object):


	for round_number in range(1,9):
		print("Round %d" % round_number)
		ronde(player_list, pot_object)
		print("")
		


if __name__ == "__main__":
	PLAYERS, POT = new_game()
	play_game(PLAYERS, POT)




