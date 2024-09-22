import enum
import random


class Difficulty(enum.StrEnum):
    """
    Enum for the different difficulties of the data
    """

    EASY = enum.auto()
    MEDIUM = enum.auto()
    HARD = enum.auto()


def get_difficulty() -> Difficulty:
    """
    Returns difficulty
    """
    while True:
        print("Please choose difficulty (EASY, MEDIUM, HARD), or type 0 to get random:")
        tuple_of_difficulties: tuple[Difficulty, ...] = tuple(Difficulty)
        difficulty_input: str = input(">>> ").lower()
        difficulty: Difficulty

        if difficulty_input in tuple_of_difficulties:
            difficulty = Difficulty(difficulty_input)
            break
        elif difficulty_input == "0":
            difficulty = random.choice(tuple_of_difficulties)
            break
        else:
            print("Invalid difficulty. Please try again")

    return difficulty
