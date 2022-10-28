import pytest
from palindrome_check import is_palindrome


@pytest.mark.parametrize(
    ('string', 'expected'),
    (
        ("aaa", True),
        ("a,b,a", True),
        ("a", True),
        (",a b", False),
    )
)
def test_palindrome_chek(string, expected):

    assert is_palindrome(string) == expected
