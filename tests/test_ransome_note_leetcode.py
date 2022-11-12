import pytest

from src.challenges.ransome_note_leetcode import ransome_note


@pytest.mark.parametrize(
    ("ransome_note_str", "magazine", "result"),
    (
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj", True),
    ),
)
def test_ransome_note(ransome_note_str, magazine, result):
    assert ransome_note(ransome_note_str, magazine) == result
