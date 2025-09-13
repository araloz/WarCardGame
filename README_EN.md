# War Card Game (Python)

## 🎮 About the Project

This project is a simple simulation of the classic **War card game**,
developed in Python using object-oriented programming (OOP).\
The game is played between 2 players, and each player draws cards from
the deck in turns. The values of the cards are compared:\
- The player with the higher card wins the round and collects the
cards.\
- If the cards are equal, a "WAR!" occurs, and each player reveals
additional cards.\
- If one player runs out of cards, the game ends.

------------------------------------------------------------------------

## 📂 Project Structure

    WarCardGame/
    │
    ├── card.py      # Card class: contains rank, suit, and value
    ├── deck.py      # Deck class: creates, shuffles, and deals 52 cards
    ├── player.py    # Player class: manages a player's cards
    └── game.py      # Main game loop: controls the game flow

------------------------------------------------------------------------

## 🛠 Technologies Used

-   Python 3.13\
-   Object-Oriented Programming (OOP)\
-   `random` module (for shuffling the deck)

------------------------------------------------------------------------

## ▶️ How to Run

1.  Navigate to the project folder:

    ``` bash
    cd Projects/Python
    ```

2.  Run the game as a package:

    ``` bash
    python -m WarCardGame.game
    ```

Example output:

    Round 1
    Round 2
    ...
    WAR!
    Player Two does not have enough cards to play the game
    Player One wins!

------------------------------------------------------------------------

## 📖 Game Rules

-   Each player is dealt 26 cards from the deck.\
-   Players draw cards in turns, and the higher card wins the round.\
-   If the cards are equal, **WAR** begins: each player draws 5 more
    cards, and the last cards are compared.\
-   If a player runs out of cards, the other player wins the game.

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Add score tracking\
-   Build a graphical interface (Tkinter / PyGame)\
-   Make the game multiplayer online

------------------------------------------------------------------------

## 👤 Author

This project was created for educational purposes and is shared on
GitHub.
