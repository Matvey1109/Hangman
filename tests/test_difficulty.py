from src.difficulty import get_difficulty


class InputSimulator:
    """Custom input for testing"""

    def __init__(self, user_inputs):
        self.user_inputs = iter(user_inputs)

    def __call__(self, prompt):
        return next(self.user_inputs)


def test_valid_difficulty_input():
    user_input = InputSimulator(["EASY"])

    get_difficulty.__globals__["input"] = user_input

    assert get_difficulty() == "easy"
