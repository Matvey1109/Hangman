class GameSession:
    def __init__(self, max_attempts: int) -> None:
        self.__max_attempts: int = max_attempts
        self.__attempts_made: int = 0
        self.__guessed_letters: set[str] = set()

    def start_new_game(self, word: str) -> None:
        if len(word) == 0:
            raise ValueError("Incorrect length of hidden word")

        self.__word_to_guess: str = word.upper()
        self.__len_of_word: int = len(word)
        self.__current_state: list[str] = ["_"] * self.__len_of_word

    def make_guess(self, letter) -> bool:
        upper_letter: str = letter.upper()

        if upper_letter in self.__guessed_letters:
            print(
                f"You've already typed the letter '{upper_letter}'. Try a different letter."
            )
            return False

        self.__guessed_letters.add(upper_letter)

        if upper_letter in self.__word_to_guess:
            for index, char in enumerate(self.__word_to_guess):
                if char == upper_letter:
                    self.__current_state[index] = upper_letter
            return True
        else:
            self.__attempts_made += 1
            return False

    def is_game_over(self) -> bool:
        return (
            self.__attempts_made >= self.__max_attempts
            or "_" not in self.__current_state
        )

    def get_game_data(self) -> tuple[list[str], int, int]:
        return self.__current_state, self.__attempts_made, self.__max_attempts
