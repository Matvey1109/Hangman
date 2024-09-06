from enum import Enum


class Difficulty(Enum):
    """
    Enum for the different difficulties of the data
    """

    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"


def get_difficulty() -> str | None:
    """
    Returns difficulty
    """
    while True:
        print("Please choose difficulty (EASY, MEDIUM, HARD), or type 0 to get random:")
        difficulty: str | None = input(">>> ")
        if difficulty in [difficulty.value for difficulty in Difficulty]:
            break
        elif difficulty == "0":
            difficulty = None
            break
        else:
            print("Invalid difficulty. Please try again")

    return difficulty
