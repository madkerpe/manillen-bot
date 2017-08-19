#Bot that plays games of manillen (https://en.wikipedia.org/wiki/Manille)
#Using it to experiment with machine learning

import cards
import random

from game import Pot
from players import Player, DumbPlayer
from itertools import cycle

#game_log = GameLog("back.txt")

	

def play_one_round(player_list, pot, pole_position=0):
	deal_cards(player_list)
	pot.trump = player_list[pole_position].choose_trump(pot)
	print("chosen trump by %s is: %s" % (player_list[pole_position].name, pot.trump))
	print("-------------------------------------------------------")
	

	for position_number in range(4):
		player = player_list[(pole_position + position_number) % 4]

		played_card = player.play_card(pot)
		played_card.played_by = player ###try to put this in the method when it works (maybe add it to standard player?)
		print("%s played %s" % (player.name, played_card.name))
	

	print("-------------------------------------------------------")
	print("winner is: %s" % pot.last_winner.name)
	print("the round was %s" % pot.last_strike)
	

def deal_cards(player_list):
	deck = cards.make_deck()
	random.shuffle(deck)
	for i, player in enumerate(player_list):
		player.hand = deck[i*8:(i + 1)*8]



if __name__ == "__main__":
	player_0 = DumbPlayer(name="player_0")
	player_1 = DumbPlayer(name="player_1")
	player_2 = DumbPlayer(name="player_2")
	player_3 = DumbPlayer(name="player_3")

	player_list = [player_0, player_1, player_2, player_3]
	pot = Pot()

	play_one_round(player_list, pot, pole_position=1)
