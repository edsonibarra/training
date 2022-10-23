from two_num_sum import two_number_sum


def test_two_num_sum():
    assert two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10) == [11, -1]
    assert two_number_sum([4, 6], 10) == [4, 6]