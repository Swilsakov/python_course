# Deck of Card

# class Deck_of_Card:
#     def __init__(self, rank, suite, card):
#         self.rank = rank
#         self.suite = suite
#         self.card = card
#     def ranks(self):
#         return self.rank
#     def suites(self):
#         return self.suite
#     def cards(self, card):
#         suit_name = ['Червы', 'Трефы', 'Пики', 'Бубны']
        # rank_name = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# a = Deck_of_Card(rank_name, suit_name, cards)
# print(a.cards(suit_name))


#=================================================================================================================================



# import random


# class Card():
#     def __init__(self):
#         self.list = ['Червы', 'Бубны', 'Треф', 'Пики']
#         self.cards = []
#         self.cart = []
#         for card_num in range(0, 52):
#             r = str(card_num % 13)
#             if r == '0':
#                 r = 'K'
#             if r == '1':
#                 r = 'A'
#             if r == '12':
#                 r = 'Q'
#             if r == '11':
#                 r = 'J'
#             index = int((card_num / 13) % 13)
#             self.cards.append((r, self.list[index]))

#     def draw(self):
#         next = self.cards.pop(random.randint(0, len(self.cards) - 1))
#         return next

#     def deck(self):
#         c = Card()
#         for i in range(0, 52):
#             self.cart.append(c.draw())


#         print(self.cart[:])

# c = Card()
# c.deck()




#====================================================================================================
# from random import *
# import random
# from random import shuffle
# class Deck_of_Card:
#     def __init__(self, rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'], suite = ['Червы', 'Трефы', 'Пики', 'Бубны']):
#         self.ranks = rank
#         self.suite = suite

#     def ranks(self):
#         return self.rank

#     def suites(self):
#         return self.suite

#     def value(self):
#         if self.rank == 'J':
#             return 10
        
#         if self.rank == 'Q':
#             return 11

#         if self.rank == 'K':
#             return 12

#         if self.rank == 'A':
#             return 13

#     def shufle(self):
#         random.shuffle(rank)
#         random.shuffle(suite)
# ``


# a = Deck_of_Card()
# print(a.shufle)


#=======================================================================================================



# from random import shuffle
# import random

# class Card:
#     def __init__(self,suit,val):
#         self.suit = suit
#         self.value = val
#     def show(self):
#         print('{}  {}'.format(self.value,self.suit))

# class Deck:
#     def __init__(self):
#         self.cards = []
#         self.build()
#     def build(self):
#         for s in ['Червы','Бубны','Трефы','Пики']:
#             for v in [2,3,4,5,6,7,8,9,10,'J', 'Q', 'K','A']:
#                 self.cards.append(Card(s,v))

#     def show(self):
#         for x in self.cards:
#             x.show()
#     def shuffle(self):
#         for i in range(len(self.cards)-1, 0, -1):
#             r = random.randint(0,i)
#             self.cards[i],self.cards[r] = self.cards[r], self.cards[i]

# deck = Deck()
# deck.shuffle()
# deck.show()