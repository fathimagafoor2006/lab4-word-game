### GUESS THE WORD — Hangman Game

A simple Python word‑guessing game where the player (or the computer in autoplay mode) tries to uncover a hidden word one letter at a time.

---

## Features

- **Manual Play** — user inputs one letter per turn  
- **Autoplay Mode** — the computer automatically guesses letters  
- **Pure-function logic** — all game rules live in `logic.py` and are easy to test  
- **UI separated from logic** — clean architecture for assignments and testing  

---

## Prerequisites

- Python **3.8+**  
- Optional: `pytest` for running tests  

---

## Quick Start

1. Open a terminal in the project folder  
2. Run the game:

```
python main.py
```

3. Choose a mode:
- `1` → Manual Play  
- `2` → Autoplay Mode  

---

##  Running Tests

1. Install pytest:

```
python -m pip install pytest
```

2. Run the test suite:

```
python -m pytest tests/test_update_game_state.py
```

---

##  Core Logic

All core game logic lives in **`logic.py`** as small, pure functions:

- `update_game_state()` — apply a guess and update lives/state  
- `mask_word()` — return the masked word with hidden letters  
- `is_word_guessed()` — detect a win  
- `is_game_over()` — detect win/lose conditions  

These functions:

- do **not** mutate inputs  
- do **not** use loops  
- are fully separated from UI code  
- are easy to test  

---

## Project Structure

```
LAB4-WORD-GAME/
├── .github/                     # GitHub configuration (optional)
│
├── agents/                      # Agent-related markdown files
│   ├── journal-logger.agent.md
│   └── copilot-instructions.md
│
├── tests/                       # Unit tests
│   └── test_update_game_state.py
│
├── .gitignore                   # Git ignore rules
├── copilot.usage.png            # Image asset (optional)
│
├── DESIGN.md                    # Design notes and decisions
├── JOURNAL.md                   # Development journal
├── logic.py                     # Core game logic (pure functions)
├── main.py                      # CLI entrypoint, menu, gameplay loop
├── MY_NOTES.md                  # Personal notes and analysis
├── README.md                    # Project documentation
├── REPORT.md                    # Final report / deliverables
└── ui.py                        # Input/output helpers
```

---
