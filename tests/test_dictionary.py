import pytest

from src.category import Category
from src.dictionary import Dictionary
from src.difficulty import Difficulty
from src.word import Word


class TestDictionary:

    @pytest.fixture
    def dictionary(self) -> Dictionary:
        """Fixture to create a new Dictionary instance for each test"""
        dictionary: Dictionary = Dictionary()
        dictionary.load_words_from_file("src/words.json")
        return dictionary

    def test_without_filtering(self, dictionary: Dictionary):
        random_word: Word = dictionary.get_random_word(None, None)
        assert random_word in dictionary.words

    def test_with_category_filtering(self, dictionary: Dictionary):
        random_word: Word = dictionary.get_random_word(Category.JOBS.value, None)
        assert random_word.category == Category.JOBS.value

    def test_with_difficulty_filtering(self, dictionary: Dictionary):
        random_word: Word = dictionary.get_random_word(None, Difficulty.HARD.value)
        assert random_word.difficulty == Difficulty.HARD.value

    def test_with_an_invalid_category(self, dictionary: Dictionary):
        with pytest.raises(ValueError) as exc_info:
            dictionary.get_random_word("INVALID_CATEGORY", None)

        assert str(exc_info.value) == "No words match the specified criteria"
