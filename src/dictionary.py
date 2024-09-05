import random

from src.word import Word


class Dictionary:
    words = []

    @staticmethod
    def load_words_from_file(file_path):
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split(",")  # Words are comma-separated
                if len(parts) == 4:
                    word = Word(parts[0], parts[1], parts[2], parts[3])
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
