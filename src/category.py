import enum
import random


class Category(enum.StrEnum):
    """
    Enum for the different categories of the data
    """

    JOBS = enum.auto()
    ANIMALS = enum.auto()
    CITIES = enum.auto()


def get_category() -> Category:
    """
    Returns category
    """
    while True:
        print(
            "Please choose a category (JOBS, ANIMALS, CITIES), or type 0 to get random:"
        )
        tuple_of_categories: tuple[Category, ...] = tuple(Category)
        category_input: str = input(">>> ").lower()
        category: Category

        if category_input in tuple_of_categories:
            category = Category(category_input)
            break

        elif category_input == "0":
            category = random.choice(tuple_of_categories)
            break
        else:
            print("Invalid category. Please try again")

    return category
