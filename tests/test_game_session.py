import pytest

from src.category import Category
from src.difficulty import Difficulty
from src.game_session import GameSession
from src.word import Word


class TestGameSession:

    @pytest.fixture
    def game_session(self) -> GameSession:
        """Fixture to create a new GameSession instance for each test"""
        game_session: GameSession = GameSession(
            Word("ABC", Category.JOBS, "HINT", Difficulty.HARD), 7
        )
        return game_session

    def test_make_guess_correct_letter(self, game_session: GameSession):
        current_result = game_session.is_correct_guess("A")
        assert current_result is True
        assert game_session.get_game_data()[0] == ["A", "_", "_"]

    def test_make_guess_incorrect_letter(self, game_session: GameSession):
        current_result = game_session.is_correct_guess("D")
        assert current_result is False
        assert game_session._current_state == ["_", "_", "_"]

    def test_case_insensitivity(self, game_session: GameSession):
        current_result = game_session.is_correct_guess("b")
        assert current_result is True
        assert game_session.is_game_over() is False
        assert game_session._current_state == ["_", "B", "_"]

    def test_game_over_after_max_attempts(self, game_session: GameSession):
        game_session.is_correct_guess("D")
        game_session.is_correct_guess("E")
        game_session.is_correct_guess("F")
        game_session.is_correct_guess("G")
        game_session.is_correct_guess("H")
        game_session.is_correct_guess("T")
        game_session.is_correct_guess("Q")
        assert game_session.is_game_over() is True
        assert game_session._current_state == ["_", "_", "_"]

    def test_state_remains_same_on_invalid_input(self, game_session: GameSession):
        game_session.is_correct_guess("xy")
        assert game_session._current_state == ["_", "_", "_"]
        assert game_session._max_attempts == 7

    def test_get_hint(self, game_session: GameSession):
        hint = game_session.get_hint()
        assert hint.isupper() is True
