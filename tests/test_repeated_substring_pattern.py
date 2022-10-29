from re import L
import pytest
from src.LEETCODE_repeated_substring_pattern import repeated_substring_pattern


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
        ("ababab", True),
        ("a", False),
        ("abcabc", True),
        ("ccca", False),
    )
)
def test_repeated_substring_pattern(s, expected):
    assert repeated_substring_pattern(s) == expected