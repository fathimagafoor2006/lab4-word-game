```markdown
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

## Rules & Invariants

### Game Rules:
- The player guesses one letter at a time.
- The game ends when the player either:
  - Reveals all letters in the word (win)
  - Uses up all allowed guesses (loss)
- Repeated guesses do not consume a turn.
- Only alphabetic characters are accepted as valid guesses.
- The game is case-insensitive (e.g., "A" and "a" are treated the same).
- Spaces in phrases are always revealed and not guessable.

### Invariants:
- `remaining_turns` is always ≥ 0
- `guessed_letters` contains only unique, lowercase letters
- `masked_word` always matches the length and structure of `secret_word`
- The game state is one of: `start`, `playing`, `won`, `lost`
- `incorrect_guesses` is a subset of `guessed_letters`
 - `incorrect_guesses` is a subset of `guessed_letters`

## Possible Bugs and Mitigations

- **Input validation:** accepts non-letter or multi-character input → sanitize input, allow only single-letter or full-word guesses; add unit tests for invalid inputs.
- **Case-sensitivity:** treats 'A' and 'a' differently → normalize (lowercase) secret and guesses; add mixed-case tests.
- **Repeated-guess handling:** duplicate guesses decrement attempts or double-count → maintain `guessed_letters` set and ignore duplicates; test duplicate sequences.
- **Partial reveal of repeated letters:** reveals only first occurrence → reveal all indices for a guessed letter; test words with repeated letters.
- **Off-by-one attempt counting:** game ends one guess too early/late → define wrong-guess decrement policy and add boundary tests for `remaining_turns`.
- **Win detection errors:** incorrect win before full reveal → compute win from required unique letters vs `guessed_letters`; test with repeated letters.
- **Whole-word guess handling:** mishandled as sequence of letters → treat full-word guesses atomically and apply single penalty on wrong guess; test both outcomes.
- **Empty/invalid word list:** crash or freeze → validate word list on startup and provide a fallback; test empty-list behavior.
- **Unicode/grapheme issues:** accented letters or emoji break indexing → normalize Unicode and handle grapheme clusters; include tests with accented words.
- **Punctuation/spaces handling:** treated as guessable → auto-reveal or exclude from guessing; test multi-word phrases.
- **State-transition bugs:** illegal actions allowed in wrong states → enforce transitions via `game_state` enum and guards; unit-test all transitions.
- **Shared/global state leaks:** multiple games share state → use per-game instances (no globals); simulate concurrent sessions in tests.
- **Save/load mismatches:** deserialized state corrupts game → versioned save format and load validation; round-trip tests.
- **UI sync bugs:** display not matching logic → use single source of truth for state; add UI integration/snapshot tests.
- **Rapid input/race conditions:** duplicate processing on fast input → debounce/disable input during processing; test rapid input.
- **Reset/new-game bugs:** not clearing `guessed_letters` or counters → implement and test `reset()`.
- **Localization/alphabet assumptions:** A–Z only → parameterize valid alphabet per locale; add locale tests.
- **Performance with extreme inputs:** very long words or huge lists → limit word length and add performance tests.
- **Insufficient test coverage:** regressions unnoticed → add unit tests for core logic and integration tests.

## update_game_state (Minimal Core)

- **Purpose:** Provide a minimal, well-tested core implementation of `update_game_state` that applies a single user action (single-letter guess or whole-word guess) to the current game record. It updates `guessed_letters`, `incorrect_guesses`, `remaining_turns`, `masked_word`, and `game_state` (one of `start`, `playing`, `won`, `lost`).

- **Design & simplicity:** The Minimal Core focuses on the smallest, correct behavior needed by tests:
  - Normalizes input to lowercase and handles a single-letter guess or whole-word guess.
  - Assumes inputs provided by tests are valid; performs only light validation.
  - Omits extended features (pause/resume, undo, localization, event hooks).
  - Keeps logic compact and in-place to make behavior easy to reason about and test.

- **Why minimal:** A compact core reduces cognitive overhead for students and isolates the invariants we care about: revealing letters, counting remaining turns, detecting win/loss, and ignoring duplicate guesses.

- **How it differs from `update_game_state_copilot`:**
  - The Copilot variant is more defensive and feature-rich: stricter validation, explicit error states, and more granular state transitions (e.g., pause/resume, event emissions).
  - Copilot's implementation may separate responsibilities (validation, transitions, persistence) into smaller functions or classes; the Minimal Core keeps them together for brevity.
  - Operationally, the Copilot version often implements additional safeguards (Unicode normalization, configurable alphabets, alternative penalty policies) that the Minimal Core intentionally leaves out.

- **When to use each:** Use the Minimal Core for teaching, quick iteration, and focused unit tests. Adopt or refactor the Copilot implementation when you need production-grade validation, extensibility, or integration with a larger application.

``` ## Game State Model

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

## Rules & Invariants

### Game Rules:
- The player guesses one letter at a time.
- The game ends when the player either:
  - Reveals all letters in the word (win)
  - Uses up all allowed guesses (loss)
- Repeated guesses do not consume a turn.
- Only alphabetic characters are accepted as valid guesses.
- The game is case-insensitive (e.g., "A" and "a" are treated the same).
- Spaces in phrases are always revealed and not guessable.

### Invariants:
- `remaining_turns` is always ≥ 0
- `guessed_letters` contains only unique, lowercase letters
- `masked_word` always matches the length and structure of `secret_word`
- The game state is one of: `start`, `playing`, `won`, `lost`
- `incorrect_guesses` is a subset of `guessed_letters`
 - `incorrect_guesses` is a subset of `guessed_letters`

## Possible Bugs and Mitigations

- **Input validation:** accepts non-letter or multi-character input → sanitize input, allow only single-letter or full-word guesses; add unit tests for invalid inputs.
- **Case-sensitivity:** treats 'A' and 'a' differently → normalize (lowercase) secret and guesses; add mixed-case tests.
- **Repeated-guess handling:** duplicate guesses decrement attempts or double-count → maintain `guessed_letters` set and ignore duplicates; test duplicate sequences.
- **Partial reveal of repeated letters:** reveals only first occurrence → reveal all indices for a guessed letter; test words with repeated letters.
- **Off-by-one attempt counting:** game ends one guess too early/late → define wrong-guess decrement policy and add boundary tests for `remaining_turns`.
- **Win detection errors:** incorrect win before full reveal → compute win from required unique letters vs `guessed_letters`; test with repeated letters.
- **Whole-word guess handling:** mishandled as sequence of letters → treat full-word guesses atomically and apply single penalty on wrong guess; test both outcomes.
- **Empty/invalid word list:** crash or freeze → validate word list on startup and provide a fallback; test empty-list behavior.
- **Unicode/grapheme issues:** accented letters or emoji break indexing → normalize Unicode and handle grapheme clusters; include tests with accented words.
- **Punctuation/spaces handling:** treated as guessable → auto-reveal or exclude from guessing; test multi-word phrases.
- **State-transition bugs:** illegal actions allowed in wrong states → enforce transitions via `game_state` enum and guards; unit-test all transitions.
- **Shared/global state leaks:** multiple games share state → use per-game instances (no globals); simulate concurrent sessions in tests.
- **Save/load mismatches:** deserialized state corrupts game → versioned save format and load validation; round-trip tests.
- **UI sync bugs:** display not matching logic → use single source of truth for state; add UI integration/snapshot tests.
- **Rapid input/race conditions:** duplicate processing on fast input → debounce/disable input during processing; test rapid input.
- **Reset/new-game bugs:** not clearing `guessed_letters` or counters → implement and test `reset()`.
- **Localization/alphabet assumptions:** A–Z only → parameterize valid alphabet per locale; add locale tests.
- **Performance with extreme inputs:** very long words or huge lists → limit word length and add performance tests.
- **Insufficient test coverage:** regressions unnoticed → add unit tests for core logic and integration tests.

