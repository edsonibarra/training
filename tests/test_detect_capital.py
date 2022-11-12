import pytest

from src.challenges.detect_capital import detect_capital


@pytest.mark.parametrize(
    ("word", "expected"), (("Google", True), ("aaaAaa", False), ("FERF", True))
)
def test_detect_capital(word, expected):
    assert detect_capital(word) == expected
