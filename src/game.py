from category import Category
from word import Word
from difficulty import Difficulty


class Game:
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
