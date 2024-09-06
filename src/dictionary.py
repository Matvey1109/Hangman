import json
import random

from word import Word


class Dictionary:
    """
    Class to getting random word
    """

    words: list[Word] = []

    def load_words_from_file(self, file_path: str) -> None:
        with open(file_path, "r") as file:
            data = json.load(file)
            for item in data:
                word = Word(
                    item["name"], item["category"], item["hint"], item["difficulty"]
                )
                Dictionary.words.append(word)

    def get_random_word(
        self, category: str | None = None, difficulty: str | None = None
    ) -> Word:
        filtered_words = Dictionary.words

        if category:
            filtered_words = [
                word for word in filtered_words if word.category == category
            ]

        if difficulty:
            filtered_words = [
                word for word in filtered_words if word.difficulty == difficulty
            ]

        if not filtered_words:
            raise ValueError("No words match the specified criteria")

        return random.choice(filtered_words)
