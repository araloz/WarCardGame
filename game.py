from .card import Card
from .deck import Deck
from .player import Player


playerOne = Player("One")
playerTwo = Player("Two")

newDeck = Deck()
newDeck.shuffle()

for x in range(int(len(newDeck.allCards)/2)):
    playerOne.add_cards(newDeck.deal_one())
    playerTwo.add_cards(newDeck.deal_one())

gameOn = True
roundNum = 0
while gameOn:
    roundNum += 1
    print(f"Round {roundNum}")

    playerOneCards = []
    playerOneCards.append(playerOne.remove_one())

    playerTwoCards = []
    playerTwoCards.append(playerTwo.remove_one())


    if len(playerOne.allCards) == 0:
        print(f"{playerOne.name} is out of cards! {playerTwo.name} wins!")
        gameOn = False
        break

    if len(playerTwo.allCards) == 0:
        print(f"{playerTwo.name} is out of cards! {playerOne.name} wins!")
        gameOn = False
        break

    atWar = True

    while atWar:
        
        if playerOneCards[-1].value > playerTwoCards[-1].value:
            playerOne.add_cards(playerOneCards)
            playerOne.add_cards(playerTwoCards)
            atWar = False
        elif playerOneCards[-1].value < playerTwoCards[-1].value:
            playerTwo.add_cards(playerTwoCards)
            playerTwo.add_cards(playerOneCards)
            atWar = False
        else:
            print("WAR!")

            if len(playerOne.allCards) < 5:
                print(f"{playerOne.name} does not have enough cards to play the game")
                print(f"{playerTwo.name} wins!")
                gameOn = False
                break
            elif len(playerTwo.allCards) < 5:
                print(f"{playerTwo.name} does not have enough cards to play the game")
                print(f"{playerOne.name} wins!")
                gameOn = False
                break
            else:
                for num in range(5):
                    playerOneCards.append(playerOne.remove_one())
                    playerTwoCards.append(playerTwo.remove_one())

