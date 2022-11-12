from typing import List


def missing_number(nums: List[int]) -> int:
    """Given an array nums containing n distinct 
    numbers in the range [0, n], return the only number 
    in the range that is missing from the array.

    Args:
        nums (List[int]): numbers list

    Returns:
        int: missing number in nums
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

print(missing_number([0,3,1]))
print(missing_number([3,0,1]))
print(missing_number([9,6,4,2,3,5,7,0,1]))
print(missing_number([0,1]))