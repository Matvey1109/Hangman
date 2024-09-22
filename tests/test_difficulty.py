import io

import pytest

from src.difficulty import Difficulty, get_difficulty


@pytest.mark.parametrize(
    "mock_input, expected_output",
    [
        ("EASY", Difficulty.EASY),
        ("MEDIUM", Difficulty.MEDIUM),
        ("HARD", Difficulty.HARD),
    ],
)
def test_valid_difficulty_input(mock_input, expected_output, monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO(mock_input))
    assert get_difficulty() == expected_output


def test_invalid_difficulty_input(monkeypatch):
    with pytest.raises(EOFError) as exc_info:
        monkeypatch.setattr("sys.stdin", io.StringIO("INVALID"))
        get_difficulty()

    assert exc_info.value
