from word import Word


class GameSession:
    """
    Class represents a game session
    """

    def __init__(self, word: Word, max_attempts: int) -> None:
        self._max_attempts: int = max_attempts  # 7 is min
        self._attempts_made: int = 0
        self._typed_letters: set[str] = set()
        self._word: Word = word
        self._current_state: list[str] = ["_"] * len(self._word.name)

    def is_correct_guess(self, letter: str) -> bool:
        upper_letter: str = letter.upper()

        if upper_letter in self._typed_letters:
            print(
                f"You've already typed the letter '{upper_letter}'. Try a different letter."
            )
            return False

        if not upper_letter.isalpha():
            print("Invalid input")
            return False

        if len(upper_letter) != 1:
            print("Please, enter a single letter")
            return False

        self._typed_letters.add(upper_letter)

        if upper_letter not in self._word.name:
            self._attempts_made += 1
            return False

        for index, char in enumerate(self._word.name):
            if char == upper_letter:
                self._current_state[index] = upper_letter

        return True

    def get_hint(self) -> str:
        return self._word.hint

    def is_game_over(self) -> bool:
        return (
            self._attempts_made >= self._max_attempts or "_" not in self._current_state
        )

    def get_game_data(self) -> tuple[list[str], int, set[str]]:
        return (
            self._current_state,
            self._attempts_made,
            self._typed_letters,
        )
