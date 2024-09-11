from dataclasses import dataclass
from category import Category
from difficulty import Difficulty


@dataclass
class Word:
    """
    Represents a word in the game
    """

    name: str
    category: Category
    hint: str
    difficulty: Difficulty
