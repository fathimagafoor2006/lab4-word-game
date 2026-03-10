###### MY ORIGINAL THINKING ######

# For the Hangman game, I first thought about what information the game needs to keep track of. The game should know the secret word, the letters that have been guessed, the current display of the word, and how many wrong guesses the player has made.
# At the start, a secret word is chosen and no letters are guessed yet. Each time the player guesses a letter, the game checks if it is in the word. If it is correct, the letter is shownin the word. If it is wrong, the number of wrong guesses increases.
# The player wins when the full word is revealed and loses when the maximum number of wrong guesses is reached. I also considered cases like repeated guesses, invalid input, different letter cases, and words with repeated letters to avoid possible bugs.

##### COPILOT SUGGESTIONS   #####

## App States
# The notes separate the game state into progress data (secret word, guessed letters, display word, lives) and game status (playing, won, lost). It also highlights that when a correct letter appears multiple times in the word, all occurrences must be revealed. The deeper questions focus on whether some information like the display word should be stored or computed, how to identify incorrect guesses, and how to handle edge cases such as repeated guesses, invalid input, or words containing spaces.

## App Variables
# The minimal information needed to track the Hangman game is **secret_word, guessed_letters, and lives**. From these, other things like the **display word, incorrect guesses, and game status (playing, won, lost)** can be calculated when needed. This keeps the game state simple and avoids storing unnecessary data.

## App rules and Invariants
# The rules define how the game changes: a correct guess adds the letter to `guessed_letters` without reducing lives, an incorrect guess reduces `lives`, and repeated guesses should not change the state. Guesses should also be treated the same regardless of case (e.g., `e` and `E`).The invariants are conditions that must always stay true: `lives` cannot go below 0, `guessed_letters` should only contain unique letters, and the game is won when all letters are guessed or lost when `lives` reaches 0.

## App Bugs
# Several bugs can happen if inputs are not validated properly. The program should reject empty input, numbers, symbols, or multiple letters, and normalize case so guesses like `p` and `P` match the word. It must also prevent duplicate guesses from reducing lives and ensure that all occurrences of a correct letter are revealed. Finally, win detection should check whether all letters in the word have been guessed, and spaces or punctuation in words should usually be revealed automatically.
