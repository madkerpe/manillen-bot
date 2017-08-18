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

	def random_card(self):

		return choice(self.hand)


	#Getters & Setters
	def get_hand(self):
		
		return self.hand

	def set_hand(self, new_hand):
		self.hand = new_hand
		return self

class Pot(object):
	def __init__(self):
		self.strike = []
		self.old_strikes = []

	def __add__(self, other):
		self.strike.append(other)
		return self
	
	def __sub__(self, other):
		if other in self.strike:
			self.strike.remove(other)

		else:
			print("%s not in strike" % other)

		return self

	def __str__(self):
		
		return self.strike

	def next_round(self):
		self.old_strikes.append(list(self.strike))
		self.strike = []
		return self

	#Getters & Setters
	def set_strike(self, strike):
		self.strike = new_strike
		return self
	def set_old_strikes(self, old_strikes):
		self.old_strikes = old_strikes
		return self
	def get_strike(self):
		
		return self.strike
	def get_old_strike(self):
		
		return self.old_strikes

#For testing...
if __name__ == "__main__":
	pass