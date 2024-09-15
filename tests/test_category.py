import io

import pytest

from src.category import Category, get_category


@pytest.mark.parametrize(
    "mock_input, expected_output",
    [
        ("JOBS", Category.JOBS),
        ("ANIMALS", Category.ANIMALS),
        ("CITIES", Category.CITIES),
    ],
)
def test_valid_category_input(mock_input, expected_output, monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO(mock_input))
    assert get_category() == expected_output


def test_invalid_category_input(monkeypatch):
    with pytest.raises(EOFError) as exc_info:
        monkeypatch.setattr("sys.stdin", io.StringIO("INVALID"))
        get_category()

    assert exc_info.value
