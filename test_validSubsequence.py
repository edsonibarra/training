import pytest
from valid_subsequence import valid_subsequence


@pytest.mark.parametrize(
    ('array', 'subsequence', 'expected'),
    (
        ([1,2,3,4,5,6,7,8,9], [7,8,9], True),
        ([1,2,3,4,5,6,7,8,9], [7,8], True),
        ([1,2,3,4,5,6,7,8,9], [7], True),
        ([1,2,3,4,5,6,7,8,9], [], False),
        ([1,2,3,4,5,6,7,8,9], [10,11,12], False),
        ([1], [1], True),
        ([], [7,8,9], False),
    )
)
def test_valid_subsequence(array, subsequence, expected):

    assert valid_subsequence(array, subsequence) == expected