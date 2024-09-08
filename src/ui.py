class UI:
    """
    Class represents a ui for the hangman game.
    It contains methods for displaying the current state of the game
    """

    def __init__(
        self,
        category: str,
        difficulty: str,
    ) -> None:
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

    def get_ui_message(self) -> str:
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

        text_message += "\nGame visualization: \n" + self.get_hangman_drawing()

        if "_" not in self.__current_state:
            return (
                text_message
                + "\nCongrats! You guessed the word: "
                + "".join(self.__current_state)
            )
        elif self.__attempts_made >= self.__max_attempts:
            return text_message + "\nGame Over! You lose!"
        else:
            return text_message

    def get_hangman_drawing(self) -> str:
        diff_between_max_and_attempt: int = self.__max_attempts - self.__attempts_made

        part1 = "   _____\n"
        part2: str

        if diff_between_max_and_attempt >= 6:
            part2 = "  |     |\n" * self.__attempts_made + "  |     \n" * (
                diff_between_max_and_attempt - 6
            )
        else:
            part2 = "  |     |\n" * (self.__max_attempts - 6)

        part3, part4, part5, part6, part7, part8, part9 = (
            """  |\n  |\n  |\n__|__\n""",
            """  |     O\n  |\n  |\n__|__\n""",
            """  |     O\n  |     |\n  |\n__|__\n        """,
            """  |     O\n  |    /|\n  |\n__|__\n        """,
            """  |     O\n  |    /|\\\n  |\n__|__\n        """,
            """  |     O\n  |    /|\\\n  |    /\n__|__\n        """,
            """  |     O\n  |    /|\\\n  |    / \\\n__|__\n        """,
        )

        parts: list[str] = [part3, part4, part5, part6, part7, part8, part9]
        hangman_part_index = (
            0
            if diff_between_max_and_attempt >= 6
            else -(diff_between_max_and_attempt + 1)
        )

        return part1 + part2 + parts[hangman_part_index]
