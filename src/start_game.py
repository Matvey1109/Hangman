import os

from category import get_category
from dictionary import Dictionary
from difficulty import get_difficulty
from game_session import GameSession
from ui import UI
from word import Word


def clear_screen():
    """Clears the console screen"""
    os.system("cls" if os.name == "nt" else "clear")


def hello_message() -> None:
    """Displays a welcome message for the Hangman Game"""
    print("Welcome to the Hangman Game!")
    print("Guess the word by entering one letter at a time.")
    print("Good luck!\n")


def game_menu() -> None:
    """Displays the game menu options"""
    print("1. Start a new game")
    print("2. Exit")


def setup_game() -> tuple[GameSession, UI]:
    """Sets up the game session and UI for the Hangman Game"""
    max_attempts: int = 7

    category: str | None = get_category()
    difficulty: str | None = get_difficulty()

    words_file_path: str = "src/words.json"
    dictionary: Dictionary = Dictionary()
    dictionary.load_words_from_file(words_file_path)
    hidden_word: Word = dictionary.get_random_word(category, difficulty)

    game_session: GameSession = GameSession(max_attempts)
    game_session.start_new_game(hidden_word)

    ui = UI(
        category=hidden_word.category,
        difficulty=hidden_word.difficulty,
    )

    return game_session, ui


def play_again() -> bool:
    """Asks the player to play again or exit the game"""
    while True:
        game_menu()
        choice = input(">>> ")
        if choice == "1":
            return True
        elif choice == "2":
            print("Thanks for playing!")
            return False
        else:
            print("Invalid choice. Please try again.")


def start_game():
    """Starts the Hangman game"""
    while True:
        clear_screen()
        hello_message()

        game_session: GameSession
        ui: UI

        game_session, ui = setup_game()

        while True:
            current_state: list[str]
            attempts_made: int
            max_attempts: int
            typed_letters: set[str]

            current_state, attempts_made, max_attempts, typed_letters = (
                game_session.get_game_data()
            )

            ui.update_ui(current_state, attempts_made, max_attempts, typed_letters)
            message: str = ui.get_ui_message()
            print(message)

            if game_session.is_game_over():
                should_play_again: bool = play_again()
                if not should_play_again:
                    return
                if should_play_again:
                    break

            letter: str = input("Enter a letter, or type 0 to get hint: ")
            if letter == "0":
                hint: str = game_session.get_hint()
                ui.set_word_hint(hint)

            is_guessed: bool = game_session.make_guess(letter)
            print("Correct guess!" if is_guessed else "Incorrect guess!")
