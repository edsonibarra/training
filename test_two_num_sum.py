from two_num_sum import two_number_sum


def test_two_num_sum():
    correct1 = [11, -1]
    result1 = two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10)
    for n in result1:
        assert n in correct1
    
    correct2 = [4,6]
    result2 = two_number_sum([4, 6], 10)
    for n in result2:
        assert n in correct2