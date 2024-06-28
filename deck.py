from card import Card
from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Deck:
    def __init__(self):
        self.cards_in_deck = []

        for suit in suits:
            for rank in ranks:
                mataatu = Card(suit, rank)
                self.cards_in_deck.append(mataatu)

    def __str__(self):
        deck_composition = ''
        for card in self.cards_in_deck:
            deck_composition += '\n' + card.__str__()
        return "The deck has: "+deck_composition

    def shuffle(self):
        shuffle(self.cards_in_deck)

    def deal_one(self):
        return self.cards_in_deck.pop()
