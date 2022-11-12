from typing import List


def missing_number(nums: List[int]) -> int:
    """Given an array nums containing n distinct 
    numbers in the range [0, n], return the only number 
    in the range that is missing from the array.

    Args:
        nums (List[int]): numbers list

    Returns:
        int: missing number in nums

    Let's say we are given this List:
    nums = [3, 0, 1]

    Sort the list = [0, 1, 3]
    Genereate another list "copy" in range len of nums + 1.
    Create two pointer for each list respectively.

    While the numbers are the same in both list
    continue increasing the pointers by 1. If the loop
    terminates it means we hit the end of nums but not of copy;
    return copy[at index nums].
    If the numbers are not the same while iterating over the lists
    then return the number in the copy list.
    """

    nums.sort()
    l = [n for n in range(len(nums) + 1)]
    a = 0
    b = 0
    while a < len(nums):
        if nums[a] == l[b]:
            print('cierto')
            a += 1
            b += 1
        else:
            return l[b]
    return l[a]
