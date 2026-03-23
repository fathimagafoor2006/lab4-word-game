## GUESS THE WORD - Hangman Game
A simple Python word‑guessing game where the player tries to uncover a hidden word one letter at a time.
This project now includes two versions of gameplay:
Manual Play — the user guesses letters
Autoplay Mode — the computer guesses letters automatically
Both versions use the same core logic and rules.
### Game Modes
1. Manual Play (Original Version)
The user enters one letter per turn.
The game shows:the masked word,letters already guessed, remaining lives.
The game ends when:the word is fully guessed, or the player runs out of lives.This is the classic version of the game.
2. Autoplay Mode (New Version)
The computer plays against itself. It automatically guesses letters.It never repeats a letter it has already guessed. Uses a simple strategy:Start with all letters a–z, Randomly choose from remaining,letters,Remove each letter after guessing,After autoplay finishes, the game returns to the main menu.This mode is useful for testing and demonstrating the game logic.
### How the Game Works
Both modes use the same core functions:
update_game_state() — checks guesses and updates lives
mask_word() — hides unguessed letters
is_game_over() — checks win/lose
is_word_guessed() — checks if the word is complete
show_state() — displays the current game state
The only difference is who provides the guesses:
Manual mode → the user
Autoplay mode → the computer
## How to run the game
Open a terminal in the project folder.
Run:
Code
python main.py
Choose a mode:
1 → Manual Play
2 → Autoplay Mode
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
## Project Structure
LAB4-WORD-GAME/
│
├── .github/                      # GitHub configuration (optional)
│
├── agents/                      # Agent-related markdown files
│   ├── journal-logger.agent.md
│   └── copilot-instructions.md
│
├── tests/                       # Test suite for logic functions
│   └── test_update_game_state.py
│
├── .gitignore                   # Git ignore rules
├── copilot.usage.png            # Screenshot or image asset
├── DESIGN.md                    # Design documentation
├── JOURNAL.md                   # Journal entries for development
├── logic.py                     # Core game logic (pure functions)
├── main.py                      # Main game loop, menu, autoplay
├── MY_NOTES.md                  # Assignment notes (analysis, design, questions)
├── README.md                    # Project overview and instructions
├── REPORT.md                    # Final report or summary
└── ui.py                        # User interface functions (input/output)
