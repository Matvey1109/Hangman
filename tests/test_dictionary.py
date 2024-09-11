import pytest

from src.category import Category
from src.dictionary import Dictionary
from src.difficulty import Difficulty
from src.word import Word


class TestDictionary:

    @pytest.fixture
    def dictionary(self) -> Dictionary:
        """Fixture to create a new Dictionary instance for each test"""
        dictionary: Dictionary = Dictionary("src/words.json")
        return dictionary

    def test_with_category_filtering(self, dictionary: Dictionary):
        random_word: Word = dictionary.get_random_word(Category.JOBS, Difficulty.HARD)
        assert random_word.category == Category.JOBS

    def test_with_difficulty_filtering(self, dictionary: Dictionary):
        random_word: Word = dictionary.get_random_word(Category.JOBS, Difficulty.HARD)
        assert random_word.difficulty == Difficulty.HARD

    def test_with_an_invalid_category(self, dictionary: Dictionary):
        with pytest.raises(ValueError) as exc_info:
            dictionary.get_random_word(Category("INVALID_CATEGORY"), Difficulty.HARD)

        assert exc_info.value
