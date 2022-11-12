import pytest
from src.challenges.move_zeroes import move_zeroes

a = [n for n in range(1,100)]
b = a.copy()

for _ in range(1,100):
    b.insert(0,0)
for _ in range(1,100):
    a.append(0)

@pytest.mark.parametrize(
    ("nums", "result"),
    (
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        (b, a)
    )
)
def test_move_zeroes(nums, result):
    move_zeroes(nums)
    assert nums == result
