import json
import random

from word import Word
from category import Category
from difficulty import Difficulty


class Dictionary:
    """
    Class for getting random word
    """

    def __init__(self, file_path: str) -> None:
        self._words: list[Word] = []

        with open(file_path, "r") as file:
            data = json.load(file)
            for item in data:
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

        return random.choice(filtered_words)
