import pytest

from src.game_session import GameSession
from src.word import Word


class TestGameSession:

    @pytest.fixture
    def game_session(self) -> GameSession:
        """Fixture to create a new GameSession instance for each test"""
        game_session: GameSession = GameSession(7)
        game_session.start_new_game(Word("abc", "JOBS", "Hint", "HARD"))
        return game_session

    def test_make_guess_correct_letter(self, game_session: GameSession):
        current_result = game_session.make_guess("A")
        assert current_result is True
        assert game_session.get_game_data()[0] == ["A", "_", "_"]

    def test_make_guess_incorrect_letter(self, game_session: GameSession):
        current_result = game_session.make_guess("D")
        assert current_result is False
        assert game_session.get_game_data()[0] == ["_", "_", "_"]

    def test_case_insensitivity(self, game_session: GameSession):
        current_result = game_session.make_guess("b")
        assert current_result is True
        assert game_session.is_game_over() is False
        assert game_session.get_game_data()[0] == ["_", "B", "_"]

    def test_game_over_after_max_attempts(self, game_session: GameSession):
        game_session.make_guess("D")
        game_session.make_guess("E")
        game_session.make_guess("F")
        game_session.make_guess("G")
        game_session.make_guess("H")
        game_session.make_guess("T")
        game_session.make_guess("Q")
        assert game_session.is_game_over() is True
        assert game_session.get_game_data()[0] == ["_", "_", "_"]

    def test_start_new_game_with_empty_word(self, game_session: GameSession):
        with pytest.raises(ValueError) as exc_info:
            game_session.start_new_game(Word("", "JOBS", "Hint", "HARD"))

        assert str(exc_info.value) == "Incorrect length of hidden word"

    def test_state_remains_same_on_invalid_input(self, game_session: GameSession):
        game_session.make_guess("xy")
        assert game_session.get_game_data()[0] == ["_", "_", "_"]
        assert game_session.get_game_data()[2] == 7

    def test_get_hint(self, game_session: GameSession):
        hint = game_session.get_hint()
        assert hint.isupper() is True
