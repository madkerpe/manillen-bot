
class Card(object):
	"""card objects initialised from a name consisting of a color + value as one string"""

	def __init__(self, name, played_by=None):
		self.name = name
		self.color = name[0]
		self.value = float(name[1])
		self.played_by = played_by

	def __str__(self):
		if self.played_by != None:
			return "[Name: %s; Played_by: %s]" % (self.name, self.played_by)

		else:
			return "[Name: %s]" % (self.name)
	def __eq__(self, other):
		
		return self.name == other.name



def make_deck():
    """Generates a list filled with 32 cards for the game "manillen":
    https://en.wikipedia.org/wiki/Manille. The deck is in ordered."""


    color = ['A', 'B', 'C', 'D']
    value = ['0.1', '0.2', '0.3', '1', '2', '3', '4', '5']
    deck = []
    for i in color:
        for j in value:
            deck.append(Card(i+j))
    return deck
