from src.category import get_category


class InputSimulator:
    """Custom input for testing"""

    def __init__(self, user_inputs):
        self.user_inputs = iter(user_inputs)

    def __call__(self, prompt):
        return next(self.user_inputs)


def test_valid_category_input():
    user_input = InputSimulator(["JOBS"])

    get_category.__globals__["input"] = user_input

    assert get_category() == "jobs"
