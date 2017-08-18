import cards
import random
import csv

from game import Player, Pot

#Bot that plays games of manillen (https://en.wikipedia.org/wiki/Manille).  Used for machine learning

def new_game():
	deck = cards.make_deck()
	random.shuffle(deck)

	new_players = [Player(deck[i*8: (i+1)*8], "Player" + str(i)) for i in range(4)]
	new_pot = Pot()

	return new_players, new_pot


def ronde(player_list, pot):

	for player in player_list:
		played_card = player.play(pot) #plays the card and returns it
		print("%s played %s" % (player, played_card))

	pot.next_round()


def play_game(player_list, pot_object):


	for round_number in range(1,9):
		print("Round %d" % round_number)
		ronde(player_list, pot_object)
		print("")



if __name__ == "__main__":
	PLAYERS, POT = new_game()
	play_game(PLAYERS, POT)




