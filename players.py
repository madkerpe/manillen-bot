from random import choice

class Player(object):
    def __init__(self, hand, name=None):
		self.hand = hand
		self.name = name

	def __str__(self):
		return str([card.name for card in self.hand])

	def __sub__(self, other):
		if other in self.hand:
			self.hand.remove(other)

		else:
			print("Card not in hand!")

		return self

class DumbPlayer(Player):
	def __init__(self, hand, name):
		super(DumbPlayer, self).__init__(hand, name)

	def choose_trump():
		return choice(['H', 'R', 'S', 'K'])

	def play_card():
		chosen_card = choice(self.hand)
        self - chosen_card
        pot + chosen_card
        
        return chosen_card


class SmartPlayer(Player):
	def __init__(self, hand, name):
		super(DumbPlayer, self).__init__(hand, name)
		
	def choose_trump():
		pass

	def play_card():
		pass