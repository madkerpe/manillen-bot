import csv


class Pot(object):
	def __init__(self, trump):
		self.trump = trump
		self.strike = []
		self.winner = None

	def __str__(self):
		return str(self.strike)

	def __add__(self, other):
		if len(self.strike) >= 4:
			self.winner = None

		else:
			self.strike.append(other)
	
		return self
		

class GameHistory(object):
	def __init__(self, bestandsnaam):
		self.bestandsnaam = bestandsnaam
		self.history = []

	def update(self, pot):
		if len(self.history >= 8):
			print(pot)

		else
			self.history.append(pot)

		return self

	def next_round(self):
		self.old_strikes.append(list(self.strike))
		self.strike = []
		return self