import io

import pytest

from src.start_game import setup_game


@pytest.mark.parametrize(
    "mock_input, expected_output",
    [
        ("JOBS\nEASY", "jobs"),
        ("ANIMALS\nHARD", "animals"),
    ],
)
def test_setup_game(mock_input, expected_output, monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO(mock_input))

    game_session, ui = setup_game()

    assert game_session._word.category == expected_output
