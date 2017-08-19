from random import choice

class Player(object):
	def __init__(self, hand=None, name=None):
		if hand == None:
			self.hand = []

		else:
			self.hand = hand
		
		self.name = name
		self.possibilities = []

	def __str__(self):
		
		return str([card.name for card in self.hand])
	def __sub__(self, other):
		if other in self.hand:
			self.hand.remove(other)

		else:
			print("Card not in hand!")

		return self

	def possibilities(self, pot):
		
		#player starts off the round
		if len(pot.strike) == 0:
			self.possibilities = self.hand

		#player has to play the same value as the same card
		else:
			possibilities = [card for card in self.hand if card.color == pot.strike[0].color]
			self.possibilities = possibilities

		#if you can buy, you have to buy 
		if len(self.possibilities) == 0:
			trumps = [card for card in self.hand if card.color == pot.trump.color]
			
			if len(trumps) == 0:
				self.possibilities = self.hand

			else:
				self.possibilities = trumps

		return self


class DumbPlayer(Player):
	def __init__(self, hand=None, name="Derp"):
		super(DumbPlayer, self).__init__(hand, name)

	def choose_trump(self, pot):
		return choice(['H', 'R', 'S', 'K'])

	def play_card(self, pot):
		###DEFINE HERE HOW THE CARD GETS CHOSEN###
		chosen_card = choice(self.hand)



		##########################################
		self - chosen_card

		return chosen_card


class SmartPlayer(Player):
	def __init__(self, hand, name):
		super(DumbPlayer, self).__init__(hand, name)
		
	def choose_trump(self, pot):
		pass

	def play_card(self, pot):
		pass
