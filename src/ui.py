class UI:
    """
    Class represents a ui for the hangman game.
    It contains methods for displaying the current state of the game
    """

    def __init__(
        self,
        current_state: list[str],
        attempts_made: int,
        max_attempts: int,
        typed_letters: set[str],
        category: str,
        difficulty: str,
    ) -> None:
        self.__current_state: list[str] = current_state
        self.__attempts_made: int = attempts_made
        self.__max_attempts: int = max_attempts
        self.__typed_letters: set[str] = typed_letters
        self.__category: str = category
        self.__difficulty: str = difficulty
        self.__word_hint: str = ""

    def update_ui(
        self,
        current_state: list[str],
        attempts_made: int,
        max_attempts: int,
        typed_letters: set[str],
    ) -> None:
        self.__current_state: list[str] = current_state
        self.__attempts_made: int = attempts_made
        self.__max_attempts: int = max_attempts
        self.__typed_letters: set[str] = typed_letters

    def set_word_hint(self, word_hint: str) -> None:
        self.__word_hint: str = word_hint

    # def get_hangman_drawing(self) -> str:
    #     part1 = "   _____\n"

    #     # part2 = "  |     |\n" * attempt + "  |     \n" * (max_input - attempt - 6)

    #     # if max_input - attempt < 6: go to part3 etc...

    #     part3 = """  |
    #     |
    #     |
    #     __|__
    #     """

    #     part4 = """  |     O
    #     |
    #     |
    #     __|__
    #     """

    #     part5 = """  |     O
    #     |     |
    #     |
    #     __|__
    #     """

    #     part6 = """  |     O
    #     |    /|
    #     |
    #     __|__
    #     """

    #     part7 = """  |     O
    #     |    /|\\
    #     |
    #     __|__
    #     """

    #     part8 = """  |     O
    #     |    /|\\
    #     |    /
    #     __|__
    #     """

    #     part9 = """  |     O
    #     |    /|\\
    #     |    / \\
    #     __|__
    #     """

    #     return

    def get_ui_message(self) -> str:
        if "_" not in self.__current_state:
            return "Congrats! You guessed the word: " + "".join(self.__current_state)
        elif self.__attempts_made >= self.__max_attempts:
            return "Game Over! You lose!"
        else:
            text_message: str = (
                "Current state: "
                + " ".join(self.__current_state)
                + " | Failed attempts made: "
                + str(self.__attempts_made)
                + "/"
                + str(self.__max_attempts)
                + " | Category: "
                + self.__category
                + " | Difficulty: "
                + self.__difficulty
                + " | Typed letters: "
                + ", ".join(self.__typed_letters)
            )

            if self.__word_hint:
                text_message += "\n | Word hint: " + self.__word_hint

            # text_message += self.get_hangman_drawing()

            return text_message
