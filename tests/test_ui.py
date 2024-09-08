import pytest

from src.ui import UI


class TestUI:

    @pytest.fixture
    def ui(self) -> UI:
        """Fixture to create a UI instance for each test"""
        return UI("JOBS", "EASY")

    def test_update_ui(self, ui):
        current_state = ["_", "_", "_", "_"]
        attempts_made = 2
        max_attempts = 6
        typed_letters = {"A", "E", "I"}

        ui.update_ui(current_state, attempts_made, max_attempts, typed_letters)

        assert ui._UI__current_state == current_state
        assert ui._UI__attempts_made == attempts_made
        assert ui._UI__max_attempts == max_attempts
        assert ui._UI__typed_letters == typed_letters

    def test_set_word_hint(self, ui):
        word_hint = "Mammal with a long trunk"

        ui.set_word_hint(word_hint)

        assert ui._UI__word_hint == word_hint

    def test_get_ui_message(self, ui):
        ui.update_ui(["E", "L", "E", "_"], 4, 6, {"E", "L"})
        ui.set_word_hint("Big, grey animal")

        assert isinstance(ui.get_ui_message(), str)

    def test_game_state_display_after_user_input(self, ui):
        ui.update_ui(["_", "_", "_", "_"], 0, 6, set())
        ui.set_word_hint("Test Hint")
        ui_message = ui.get_ui_message()

        expected_message = "Current state: _ _ _ _ "

        assert ui_message.startswith(expected_message)

        # Simulate next user input
        ui.update_ui(["a", "_", "_", "_"], 1, 6, {"a"})
        ui_message = ui.get_ui_message()

        expected_message = "Current state: a _ _ _ "

        assert ui_message.startswith(expected_message)

    def test_lose_game(self, ui):
        ui.update_ui(["_", "_", "_", "_"], 6, 6, set())

        assert ui.get_ui_message().endswith("You lose!")
