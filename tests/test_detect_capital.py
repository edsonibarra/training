from src.detect_capital_leetcode import detect_capital
import pytest


@pytest.mark.parametrize(
    ('word','expected'),
    (
        ('Google',True),
        ('aaaAaa',False),
        ('FERF',True)
    )
)
def test_detect_capital(word, expected):
    assert detect_capital(word) == expected