import random

from src.category import Category
from src.difficulty import Difficulty
from src.word import Word


class Dictionary:
    words: list[Word] = [
        Word(
            "Doctor",
            Category.JOBS.value,
            "A person trained to treat and cure illnesses",
            Difficulty.EASY.value,
        ),
        Word(
            "President",
            Category.JOBS.value,
            "The person who runs the country",
            Difficulty.MEDIUM.value,
        ),
        Word(
            "Neurosurgeon",
            Category.JOBS.value,
            "A specialist surgeon who operates on the brain and nervous system",
            Difficulty.HARD.value,
        ),
        Word(
            "Dog",
            Category.ANIMALS.value,
            "A domesticated carnivorous mammal",
            Difficulty.EASY.value,
        ),
        Word(
            "Elephant",
            Category.ANIMALS.value,
            "A large mammal with tusks and a trunk",
            Difficulty.MEDIUM.value,
        ),
        Word(
            "Tasmanian Devil",
            Category.ANIMALS.value,
            "A carnivorous marsupial native to Tasmania, known for its aggressive behavior",
            Difficulty.HARD.value,
        ),
        Word(
            "Paris",
            Category.CITIES.value,
            "The capital of France",
            Difficulty.EASY.value,
        ),
        Word(
            "Tokyo",
            Category.CITIES.value,
            "The capital of Japan",
            Difficulty.MEDIUM.value,
        ),
        Word(
            "Istanbul",
            Category.CITIES.value,
            "A major city in Turkey that straddles Europe and Asia",
            Difficulty.HARD.value,
        ),
    ]

    @staticmethod
    def get_random_word(category: str | None, difficulty: int | None) -> Word:
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
