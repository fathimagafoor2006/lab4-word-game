## GUESS THE WORD - Hangman Game
This project is a console based Guess the word game similiar to Hangman,created for software engineering course at EPITA
The goal of the assignment is to practice design thinking before coding,pure functions and immutability,seperation of logic and UI,testing with pytest,responsible use of github copilot
The project includes documentation, tests, and a complete playable game.
## How to run the game
Make  sure you are in the projecft folder,then run:
python main.py
The computer randomely selects a secret word,you guess letters one at a time ,the game displays the masked word,your guessed letters ,remaining letters. you win by guessing all letters,you lose when lives reach zero,at the end you can choose to replay without restarting the program
## Running the Tests
This project uses pytest
1. Install pytest:
   python -m pip install pytest
2. Run the tests:
   python -m pytest tests/test_update_game_state.py
## Core logic overview
All game logic is implemented using pure functions inside logic.py
update_game_state
mask_word
is_word_guessed
is_game_over
these functions do not mutate inputs,do not use loops ,easy to test,fully seperated from UI code
