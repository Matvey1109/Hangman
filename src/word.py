from dataclasses import dataclass


@dataclass
class Word:
    """
    Represents a word in the game
    """

    name: str
    category: str
    hint: str
    difficulty: str
