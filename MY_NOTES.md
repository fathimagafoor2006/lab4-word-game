###### MY ORIGINAL THINKING ######
## States
The game has three main states: the start state where the secret word is chosen and no guesses have been made, the playing state where the player keeps guessing letters, and the final state where the player either wins by guessing the full word or loses when the lives reach zero.
## Variables
The main variables needed are the secret_word, guessed_letters, the display_word that shows the current progress of the word, and lives which represent how many wrong guesses the player can still make.
## Rules
The player guesses one letter at a time. If the letter exists in the secret word, it is revealed in all positions in the display word. If the letter is not in the word, the number of lives decreases. The player wins when all letters are revealed and loses when lives become zero.
## Invariants
Some conditions must always remain true during the game: lives cannot go below zero, guessed_letters should not contain duplicates, and the display_word must always have the same length as the secret_word.
## App Bugs
Possible bugs include repeated guesses, invalid inputs such as numbers or symbols, case sensitivity issues (uppercase vs lowercase), and words that contain repeated letters. These cases must be handled properly to keep the game working correctly.

##### COPILOT SUGGESTIONS  #####

## App States
 The notes separate the game state into progress data (secret word, guessed letters, display word, lives) and game status (playing, won, lost). It also highlights that when a correct letter appears multiple times in the word, all occurrences must be revealed. The deeper questions focus on whether some information like the display word should be stored or computed, how to identify incorrect guesses, and how to handle edge cases such as repeated guesses, invalid input, or words containing spaces.
## App Variables
The minimal information needed to track the Hangman game is secret_word, guessed_letters, and lives. From these, other things like the display word, incorrect guesses, and game status (playing, won, lost)** can be calculated when needed. This keeps the game state simple and avoids storing unnecessary data.
## App rules and Invariants
The rules define how the game changes: a correct guess adds the letter to `guessed_letters` without reducing lives, an incorrect guess reduces `lives`, and repeated guesses should not change the state. Guesses should also be treated the same regardless of case (e.g., `e` and `E`).The invariants are conditions that must always stay true: `lives` cannot go below 0, `guessed_letters` should only contain unique letters, and the game is won when all letters are guessed or lost when `lives` reaches 0.
## App Bugs
Several bugs can happen if inputs are not validated properly. The program should reject empty input, numbers, symbols, or multiple letters, and normalize case so guesses like `p` and `P` match the word. It must also prevent duplicate guesses from reducing lives and ensure that all occurrences of a correct letter are revealed. Finally, win detection should check whether all letters in the word have been guessed, and spaces or punctuation in words should usually be revealed automatically.

## AUTO PLAY MODE ASSIGNMENT
The game currently only supports manual play. To add autoplay, the computer needs to guess letters instead of the user. The existing logic functions already handle checking guesses, updating lives, and masking the word, so autoplay only needs a way to choose letters automatically. The computer must not guess the same letter twice. After autoplay ends, the game should return to the main menu.
## design decisions -
Add a menu at the start so the user can choose manual play or autoplay
Create a separate function for autoplay instead of changing the manual game
Autoplayer will keep a list of all letters (a–z) and remove letters after guessing them
Use random choice from the remaining letters so no letter is repeated
Reuse the existing logic functions to keep behavior consistent
After autoplay ends, return to the menu instead of quitting
## Questions
Should autoplay stay random or use a smarter guessing strategy?
Should autoplay run instantly or show guesses slowly?
Should the menu support more modes in the future?