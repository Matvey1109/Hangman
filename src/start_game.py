import os

from category import Category, get_category
from dictionary import Dictionary
from difficulty import Difficulty, get_difficulty
from game_session import GameSession
from ui import UI
from word import Word


def setup_game() -> tuple[GameSession, UI]:
    """Sets up the game session and UI for the Hangman Game"""
    max_attempts: int = int(os.environ.get("MAX_ATTEMPTS", "7"))
    words_file_path: str = os.environ.get("WORDS_FILE_PATH", "src/words.json")

    category: Category = get_category()
    difficulty: Difficulty = get_difficulty()

    dictionary: Dictionary = Dictionary(words_file_path)
    hidden_word: Word = dictionary.get_random_word(category, difficulty)

    game_session: GameSession = GameSession(hidden_word, max_attempts)

    ui = UI(
        category=hidden_word.category,
        difficulty=hidden_word.difficulty,
        max_attempts=max_attempts,
    )

    return game_session, ui


def start_game():
    """Starts the Hangman game"""
    while True:
        UI.clear_screen()
        UI.hello_message()

        game_session: GameSession
        ui: UI

        game_session, ui = setup_game()

        UI.clear_screen()
        while True:
            current_state: list[str]
            attempts_made: int
            typed_letters: set[str]

            current_state, attempts_made, typed_letters = game_session.get_game_data()

            ui.update_ui(current_state, attempts_made, typed_letters)
            message: str = ui.get_ui_message()
            print(message)

            if game_session.is_game_over():
                should_play_again: bool = UI.is_playing_again()
                if not should_play_again:
                    return
                if should_play_again:
                    break

            letter: str = input("Enter a letter, or type 0 to get hint: ")
            UI.clear_screen()

            if letter != "0":
                is_guess_correct: bool = game_session.is_correct_guess(letter)
                print("Correct guess!" if is_guess_correct else "Incorrect guess!")
                continue

            hint: str = game_session.get_hint()
            ui.set_word_hint(hint)
