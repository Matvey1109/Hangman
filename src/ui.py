import os


class UI:
    """
    Class represents a ui for the hangman game.
    It contains methods for displaying the current state of the game
    """

    def __init__(
        self,
        category: str,
        difficulty: str,
        max_attempts: int,
    ) -> None:
        self._category: str = category
        self._difficulty: str = difficulty
        self._max_attempts: int = max_attempts
        self._current_state: list[str]
        self._attempts_made: int
        self._typed_letters: set[str]
        self._word_hint: str = ""

    def update_ui(
        self,
        current_state: list[str],
        attempts_made: int,
        typed_letters: set[str],
    ) -> None:
        self._current_state = current_state
        self._attempts_made = attempts_made
        self._typed_letters = typed_letters

    def set_word_hint(self, word_hint: str) -> None:
        self._word_hint = word_hint

    def get_ui_message(self) -> str:
        text_message: str = (
            "Current state: "
            + " ".join(self._current_state)
            + " | Failed attempts made: "
            + str(self._attempts_made)
            + "/"
            + str(self._max_attempts)
            + " | Category: "
            + self._category
            + " | Difficulty: "
            + self._difficulty
            + " | Typed letters: "
            + ", ".join(self._typed_letters)
        )

        if self._word_hint:
            text_message += "\n | Word hint: " + self._word_hint

        text_message += "\nGame visualization: \n" + self.get_hangman_drawing()

        if "_" not in self._current_state:
            return (
                text_message
                + "\nCongrats! You guessed the word: "
                + "".join(self._current_state)
            )
        elif self._attempts_made >= self._max_attempts:
            return text_message + "\nGame Over! You lose!"
        else:
            return text_message

    def get_hangman_drawing(self) -> str:
        diff_between_max_and_attempt: int = self._max_attempts - self._attempts_made

        part1 = "   _____\n"
        part2: str

        if diff_between_max_and_attempt >= 6:
            part2 = "  |     |\n" * self._attempts_made + "  |     \n" * (
                diff_between_max_and_attempt - 6
            )
        else:
            part2 = "  |     |\n" * (self._max_attempts - 6)

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

    @staticmethod
    def clear_screen():
        """Clears the console screen"""
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def hello_message() -> None:
        """Displays a welcome message for the Hangman Game"""
        print("Welcome to the Hangman Game!")
        print("Guess the word by entering one letter at a time.")
        print("Good luck!\n")

    @staticmethod
    def game_menu() -> None:
        """Displays the game menu options"""
        print("1. Start a new game")
        print("2. Exit")

    @staticmethod
    def is_playing_again() -> bool:
        """Asks the player to play again or exit the game"""
        while True:
            UI.game_menu()
            choice = input(">>> ")
            if choice == "1":
                return True
            elif choice == "2":
                print("Thanks for playing!")
                return False
            else:
                print("Invalid choice. Please try again.")
