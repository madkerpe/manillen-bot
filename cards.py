class Card(object):
	def __init__(self, name, owned_by=None, played_by=None):
		self.name = name
		self.color = name[0]
		self.value = name[1]
		self.owned_by = owned_by
		self.played_by = played_by


	def __str__(self):
		if self.owned_by != None:
			return "[Name: %s; Owned_by: %s]" % (self.name, self.owned_by)

		elif self.played_by != None:
			return "[Name: %s; Played_by: %s]" % (self.name, self.played_by)

		else:
			return "[Name: %s]" % (self.name)


	def __eq__(self, other):
		return self.name == other.name


	#Getters & Setters
	def set_owned_by(self, new_owned_by):
		self.owned_by = new_owned_by
		return self

	def set_played_by(self, new_played_by):
		self.played_by = new_played_by
		return self

	def get_owned_by(self):
		return self.owned_by

	def get_played_by(self):
		return self.played_by

def make_deck():
    """Generates a list filled with 32 cards for the game "manillen":
    https://en.wikipedia.org/wiki/Manille. The deck is in ordered."""


    color = ['H', 'R', 'S', 'K']
    value = ['A', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = []
    for i in color:
        for j in value:
            deck.append(Card(i+j))
    return deck
