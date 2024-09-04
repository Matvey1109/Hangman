from src.category import Category
from src.dictionary import Dictionary
from src.difficulty import Difficulty


def test_get_random_word():
    # without filtering
    random_word = Dictionary.get_random_word(None, None)
    assert random_word in Dictionary.words

    # with a specific category
    random_word = Dictionary.get_random_word(Category.JOBS.value, None)
    assert random_word.category == Category.JOBS.value

    # with a specific difficulty
    random_word = Dictionary.get_random_word(None, Difficulty.HARD.value)
    assert random_word.difficulty == Difficulty.HARD.value

    # with an invalid category
    try:
        random_word = Dictionary.get_random_word("INVALID_CATEGORY", None)
    except ValueError as e:
        assert str(e) == "No words match the specified criteria"
