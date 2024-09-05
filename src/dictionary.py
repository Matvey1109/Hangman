import json
import random

from src.word import Word


class Dictionary:
    words: list[Word] = []

    @staticmethod
    def load_words_from_file(file_path: str) -> None:
        with open(file_path, "r") as file:
            data = json.load(file)
            for item in data:
                word = Word(
                    item["name"], item["category"], item["hint"], item["difficulty"]
                )
                Dictionary.words.append(word)

    @staticmethod
    def get_random_word(
        category: str | None = None, difficulty: str | None = None
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
