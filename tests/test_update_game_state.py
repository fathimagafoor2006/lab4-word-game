import pytest

from main import update_game_state


def test_correct_guess_no_life_lost():
	new_guessed, new_lives = update_game_state("apple", [], "a", 5)
	assert new_guessed == ["a"]
	assert new_lives == 5


def test_incorrect_guess_decrements_life():
	new_guessed, new_lives = update_game_state("apple", [], "z", 5)
	assert new_guessed == ["z"]
	assert new_lives == 4


def test_repeat_guess_no_side_effects():
	orig = ["a"]
	new_guessed, new_lives = update_game_state("apple", orig, "a", 5)
	assert new_guessed == ["a"]
	assert new_lives == 5
	# original list must not be mutated
	assert orig == ["a"]


def test_case_normalization_regression():
	# current desired behavior: guesses should be treated case-insensitively
	orig = ["A"]
	new_guessed, new_lives = update_game_state("Apple", orig, "a", 5)
	# function normalizes guesses to lowercase
	assert new_guessed == ["a"]
	assert new_lives == 5


def test_multi_character_guess_behavior():
	# Define expected policy: function currently accepts any string.
	new_guessed, new_lives = update_game_state("apple", [], "ab", 5)
	assert new_guessed == ["ab"]
	# "ab" is not in "apple" so lives should decrement
	assert new_lives == 4


def test_boundary_lives_zero():
	new_guessed, new_lives = update_game_state("x", [], "z", 1)
	assert new_guessed == ["z"]
	assert new_lives == 0

