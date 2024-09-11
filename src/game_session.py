from word import Word


class GameSession:
    """
    Class represents a game session
    """

    def __init__(self, max_attempts: int) -> None:
        self._max_attempts: int = max_attempts  # 7 is min
        self._attempts_made: int = 0
        self._typed_letters: set[str] = set()

        if self._max_attempts < 7:
            raise ValueError("Max attempts should be at least 7")

    def start_new_game(self, word: Word) -> None:
        self._word_to_guess: str = word.name.upper()
        self._len_of_word: int = len(self._word_to_guess)

        if self._len_of_word == 0:
            raise ValueError("Incorrect length of hidden word")

        self._word_hint: str = word.hint.upper()
        self._current_state: list[str] = ["_"] * self._len_of_word

    def make_guess(self, letter: str) -> bool:
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

        if upper_letter in self._word_to_guess:
            for index, char in enumerate(self._word_to_guess):
                if char == upper_letter:
                    self._current_state[index] = upper_letter
            return True
        else:
            self._attempts_made += 1
            return False

    def get_hint(self) -> str:
        return self._word_hint

    def is_game_over(self) -> bool:
        return (
            self._attempts_made >= self._max_attempts
            or "_" not in self._current_state
        )

    def get_game_data(self) -> tuple[list[str], int, int, set[str]]:
        return (
            self._current_state,
            self._attempts_made,
            self._max_attempts,
            self._typed_letters,
        )
