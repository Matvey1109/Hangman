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
    ) -> None:
        self.__current_state: list[str] = current_state
        self.__attempts_made: int = attempts_made
        self.__max_attempts: int = max_attempts
        self.__typed_letters: set[str] = typed_letters

    def set_word_hint(self, word_hint: str) -> None:
        self.__word_hint: str = word_hint

    def get_result_message(self) -> str:
        if "_" not in self.__current_state:
            return "Congrats! You guessed the word: " + "".join(self.__current_state)
        elif self.__attempts_made >= self.__max_attempts:
            return "Game Over! You lose!"
        else:
            text_message: str = (
                "Current state: "
                + " ".join(self.__current_state)
                + " | Attempts made: "
                + str(self.__attempts_made)
                + "/"
                + str(self.__max_attempts)
                + " | Typed letters: "
                + ", ".join(self.__typed_letters)
            )

            if self.__word_hint:
                text_message += " | Word hint: " + self.__word_hint

            return text_message
