# coding: utf-8
from random import randint

def raw_input(prompt):
    return input(prompt)
    
class Card:
	suit_strings = ['','D', 'H', 'C', 'S']
	face_strings = ['', 'A', '2', '3', '4', '5', '6', '7', 'J', 'Q', 'K']
	
	def __init__(self, face, suit):
		self.face = face
		self.suit = suit
		
	def to_string(self):
		
		return '{0}{1}'.format(self.get_face_string(), self.get_suit_string())
		
	def get_face_string(self):
		return Card.face_strings[self.face]
		
	def get_suit_string(self):
		return Card.suit_strings[self.suit]
		
class Shoe:
	def __init__(self):
		self.deck = []
		
		for suit in range(1, 5):
			for face in range(1, 11):
				self.deck.append(Card(face, suit))
				
	def to_string(self):
		card_string = ''
		for card in self.deck:
			card_string += '\n{0}'.format(card.to_string())
			
		return card_string
		
	def shuffle(self):
		shoe_size = len(self.deck)
		for i in range(0, shoe_size):
			random_index = randint(1, shoe_size-1)
			temp = self.deck[i]
			self.deck[i] = self.deck[random_index]
			self.deck[random_index] = temp
			
	def deal(self, howmanycards):
		cards = []
		for i in range(0, howmanycards):
			if len(self.deck) > 0:
				cards.append(self.deck.pop())
				
		return cards
		
def print_cards(cards):
	card_string = ''
	print (type(cards))
	for card in cards:
		card_string += '{0}, '.format(card.to_string())
		
	print (card_string)
		
			
		
def test_card():
	ace_diamonds = Card(1, 1)
	print (ace_diamonds.to_string())
	
	two_of_spades = Card(2, 4)
	print (two_of_spades.to_string())
	
	shoe = Shoe()
	print ('*******************')
	print ('shoe ordered')
	print (shoe.to_string())
	
	shoe.shuffle()
	print ('*******************')
	print ('shoe shuffled')
	print (shoe.to_string())
	
	cards = shoe.deal(8)
	print ('*********cards dealt******')
	print_cards(cards)
	print (' shoe size after dealing eight cards')
	print('shoe size {0}'.format(len(shoe.deck)))
	
	
	
shoe = Shoe()
shoe.shuffle()
hand = shoe.deal(8)
print_cards(hand)

while True:
	card_to_throw = raw_input('select 1-8 for which card to throw away')
	card_to_throw = int(card_to_throw)
	if card_to_throw > 0 and card_to_throw < 9:
		break

card_to_throw -= 1

hand.pop(card_to_throw)
hand.append(shoe.deal(1)[0])

print_cards(hand)
		