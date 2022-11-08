from typing import List


def first_duplicate_value(array: List[int]) -> int:

    seen = {}

    i = 0
    while i < len(array):

        current = array[i]
        if current in seen:

            if seen[current][-1] < i:
                return current

        else:

            seen[current] = [i]

        i += 1

    return -1


print(first_duplicate_value(array=[2, 1, 5, 2, 3, 3, 4]))
print(first_duplicate_value(array=[2, 1, 5, 3, 3, 2, 4]))