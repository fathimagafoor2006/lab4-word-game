"""Core game-state utilities for the word game.

Provides a minimal, pure update function used by the game loop or tests.
"""

"""
        Update guessed letters and remaining lives for a single guess.

        Behavior:
        - Normalizes `guess` to lowercase.
        - Returns a new list (does not mutate `guessed_letters`).
        - If the normalized guess is already present in the returned list,
            the function returns the list unchanged and `lives`.
        - Appends the normalized guess to the returned list when it is new.
        - Decrements `lives` by 1 when the normalized guess is not present
            in `secret_word` (case-insensitive check).

        Parameters
        - secret_word: target word to guess.
        - guessed_letters: list of previous guesses (caller may supply mixed case).
        - guess: the player's guessed string (expected to be a single letter).
        - lives: current number of remaining wrong guesses allowed.

        Returns
        - (new_guessed_letters, new_lives)

        Notes / Caveats
        - `guessed_letters` elements are not normalized by this function; callers
            should pass a normalized list (lowercase) or the function should be
            extended to normalize them to avoid case-sensitivity bugs.
        - The function does not validate `guess` (it may be multi-character or
            non-alphabetic). Consider validating input upstream or here.
        - To determine whether a guess was correct, compare returned `lives` to
            the input `lives` or check membership of the guess in `secret_word`.

        Suggested improvements: normalize `guessed_letters`, validate `guess`,
        precompute a lowercase `secret = secret_word.lower()`, and optionally
        return a `correct: bool` alongside the current return values.
        """

from logic import update_game_state, mask_word, is_game_over, is_word_guessed
from ui import show_state, ask_for_guess
import random

WORDS = ["apple", "banana", "orange", "grapes", "peach"]

def play_one_game():
    secret = random.choice(WORDS)
    guessed = []
    lives = 6

    while not is_game_over(lives, secret, guessed):
        masked = mask_word(secret, guessed)
        show_state(masked, guessed, lives)

        guess = ask_for_guess()
        guessed, lives = update_game_state(secret, guessed, guess, lives)

   
    masked = mask_word(secret, guessed)
    show_state(masked, guessed, lives)

    if is_word_guessed(secret, guessed):
        print(" You won!")
    else:
        print(" You lost! The word was: {secret}")

def main():
    play_one_game()

    replay = input("\nPlay again? (y/n): ").lower()
    if replay == "y":
        main()  

if __name__ == "__main__":
    main()
