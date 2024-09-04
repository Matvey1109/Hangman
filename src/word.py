from dataclasses import dataclass


@dataclass
class Word:
    name: str
    category: str
    hint: str
    difficulty: int
