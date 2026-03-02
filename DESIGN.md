## Game State Model

### States:
- `start`: Game setup, word selection
- `playing`: User is guessing letters
- `won`: User has guessed the word
- `lost`: User has used all allowed guesses

### Variables:
- `secret_word`: The word to guess
- `guessed_letters`: List of letters guessed so far
- `remaining_turns`: Number of guesses left
- `incorrect_guesses`: List of incorrect letters
- `masked_word`: Current display of the word (e.g., "_ A _ _ M _ N")
- `game_state`: Current state of the game

## Copilot's Suggested Game States
stateDiagram-v2
    [*] --> NotStarted
    NotStarted --> Setup: new game
    Setup --> Playing: initialize
    Playing --> Won: all letters revealed
    Playing --> Lost: attempts exhausted
    Playing --> Paused: pause
    Paused --> Playing: resume
    Won --> Revealing: show final
    Lost --> Revealing: show final
    Revealing --> NotStarted: restart
    Won --> NotStarted: restart
    Lost --> NotStarted: restart
    Playing --> Error: invalid input
    Error --> Playing: recover
