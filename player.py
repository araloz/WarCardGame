class Player():

    def __init__(self, name):
        self.name = name
        self.allCards = []

    def remove_one(self):
        return self.allCards.pop(0)

    def add_cards(self, newCards):
        if type(newCards) == type([]):
            self.allCards.extend(newCards)
        else:
            self.allCards.append(newCards)

    def __str__(self):
        return f"Player {self.name} has {len(self.allCards)} cards."