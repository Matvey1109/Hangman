from src.start_game import game_menu, hello_message, play_again


class InputSimulator:
    """Custom input for testing"""

    def __init__(self, user_inputs):
        self.user_inputs = iter(user_inputs)

    def __call__(self, prompt):
        return next(self.user_inputs)


def test_hello_message(capsys):
    hello_message()
    captured = capsys.readouterr()
    assert "Welcome to the Hangman Game!" in captured.out


def test_game_menu(capsys):
    result = game_menu()
    captured = capsys.readouterr()
    assert "1. Start a new game" in captured.out
    assert result is None


def test_play_again():
    user_input_1 = InputSimulator(["1"])
    play_again.__globals__["input"] = user_input_1

    assert isinstance(play_again(), bool)

    user_input_2 = InputSimulator(["2"])
    play_again.__globals__["input"] = user_input_2

    assert isinstance(play_again(), bool)
