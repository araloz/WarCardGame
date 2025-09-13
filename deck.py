from .card import Card
import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Sxix", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

class Deck():

    def __init__(self):
        self.allCards = []

        for suit in suits:
            for rank in ranks:
                createdCard = Card(suit, rank)
                self.allCards.append(createdCard)

    def shuffle(self):
        random.shuffle(self.allCards)  # shuffles internally : no return

    def deal_one(self):
        return self.allCards.pop()