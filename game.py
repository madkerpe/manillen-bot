import csv

class Pot(object):
	"""pot object that keeps track of an ongoing round"""

	def __init__(self):
		self.trump = None
		self.strike = []
		self.last_winner = None
		self.last_strike = []

	def __str__(self):
		
		return str(self.strike)
	def __add__(self, other):
		if len(self.strike) >= 4:
			#figuring out who won
			self.last_winner = self.round_winner()

			#end of a strike
			self.last_strike = self.strike
			self.strike = []

		else:
			self.strike.append(other)
	
		return self
		

	def round_winner(self):
		"""returns the winner of the round"""
		
		trump = self.trump

		#is there a trump played?
		contenders = [card for card in self.strike if card.color == trump ]
		
		#there is no trump played
		if len(contenders) == 0:
			trump = self.strike[0].color
			contenders = [card for card in self.strike  if card.color == trump]
			return highest_value_card(contenders).played_by
		
		#there is a trump played
		else:
			return highest_value_card(contenders).played_by



def highest_value_card(contenders):
	
	contenders_values = [contender.value for contender in contenders]
	return contenders[contenders_values.index(max(contenders_values))]



class GameLog(object):
	"""objects used to log the game and print it to a .csv file"""

	def __init__(self, bestandsnaam):
		self.bestandsnaam = bestandsnaam
		self.history = []

	def update(self, pot):
		if len(self.history >= 8):
			#end of a game
			with open(bestandsnaam, 'w', newline='') as gamelog_file:
				writer =  gamelog_file.writer(gamelog_file)
				
				for round_log in self.history:
					writer.writerow(round_log)

			print(self.history)

		else:
			self.history.append(pot.last_strike)

		return self
