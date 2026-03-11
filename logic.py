def update_game_state(secret_word: str,
                      guessed_letters: list[str],
                      guess: str,
                      lives: int) -> tuple[list[str], int]:
    g = guess.lower()

    normalized = [letter.lower() for letter in guessed_letters]

    if g in normalized:
        return normalized, lives

    normalized.append(g)

    if g not in secret_word.lower():
        lives -= 1

    return normalized, lives


def mask_word(secret_word: str, guessed_letters: list[str]) -> str:
    if secret_word == "":
        return ""

    first = secret_word[0]
    rest = secret_word[1:]

    if first.lower() in guessed_letters:
        return first + mask_word(rest, guessed_letters)
    else:
        return "_" + mask_word(rest, guessed_letters)

def is_word_guessed(secret_word: str, guessed_letters: list[str]) -> bool:
    return all(letter.lower() in guessed_letters for letter in secret_word)

def is_game_over(lives: int, secret_word: str, guessed_letters: list[str]) -> bool:
    return lives <= 0 or is_word_guessed(secret_word, guessed_letters)
