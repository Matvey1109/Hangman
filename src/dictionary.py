import json
import random

from category import Category
from difficulty import Difficulty
from word import Word


class Dictionary:
    """
    Class for getting random word
    """

    def __init__(self, file_path: str) -> None:
        self._words: list[Word] = []

        with open(file_path, "r") as file:
            data = json.load(file)
            for item in data:
                if len(item["name"]) == 0:
                    raise ValueError("Incorrect length of hidden word")

                word = Word(
                    item["name"], item["category"], item["hint"], item["difficulty"]
                )

                self._words.append(word)

    def get_random_word(self, category: Category, difficulty: Difficulty) -> Word:
        filtered_words = [
            word
            for word in self._words
            if word.category == category and word.difficulty == difficulty
        ]

        if not filtered_words:
            raise ValueError("No words match the specified criteria")

        random_word: Word = random.choice(filtered_words)
        random_word.name = random_word.name.upper()
        random_word.hint = random_word.hint.upper()

        return random_word
