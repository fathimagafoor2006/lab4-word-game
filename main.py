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

def choose_mode():
    print("\nChoose a mode:")
    print("1. Play manually")
    print("2. Autoplay (computer guesses)")
    choice = input("Enter 1 or 2: ").strip()
    return choice

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

import string
import random

def autoplay_one_game():
    secret = random.choice(WORDS)
    guessed = []
    lives = 6

    remaining_letters = list(string.ascii_lowercase)

    print(f"\nAutoplay started! Secret word has {len(secret)} letters.")

    while not is_game_over(lives, secret, guessed):
        masked = mask_word(secret, guessed)
        show_state(masked, guessed, lives)

        guess = random.choice(remaining_letters)
        remaining_letters.remove(guess)

        print(f"Autoplayer guesses: {guess}")

        guessed, lives = update_game_state(secret, guessed, guess, lives)

    masked = mask_word(secret, guessed)
    show_state(masked, guessed, lives)

    if is_word_guessed(secret, guessed):
        print("Autoplayer won!")
    else:
        print(f"Autoplayer lost! The word was: {secret}")


def main():
    while True:
        choice = choose_mode()

        if choice == "1":
            play_one_game()
        elif choice == "2":
            autoplay_one_game()
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue

        replay = input("\nReturn to menu? (y/n): ").lower()
        if replay != "y":
            break


if __name__ == "__main__":
    main()
