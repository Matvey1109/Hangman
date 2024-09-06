from enum import Enum


class Category(Enum):
    """
    Enum for the different categories of the data
    """

    JOBS = "JOBS"
    ANIMALS = "ANIMALS"
    CITIES = "CITIES"


def get_category() -> str | None:
    """
    Returns category
    """
    while True:
        print(
            "Please choose a category (JOBS, ANIMALS, CITIES), or type 0 to get random:"
        )
        category: str | None = input(">>> ")
        if category in [category.value for category in Category]:
            break
        elif category == "0":
            category = None
            break
        else:
            print("Invalid category. Please try again")

    return category
