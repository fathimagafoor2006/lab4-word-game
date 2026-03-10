def show_state(masked_word: str, guessed: list[str], lives: int):
    print(f"\nWord: {masked_word}")
    print(f"Guessed letters: {', '.join(guessed)}")
    print(f"Lives remaining: {lives}")

def ask_for_guess() -> str:
    guess = input("Enter a letter: ").strip()
    return guess[0] if guess else ""
