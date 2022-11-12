from typing import List


def move_zeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead
    nums = [0, 1, 0, 3, 12]
            b
            a
    nums = [0, 1, 0, 3, 12]
            b
               a # Swap numbers
    nums = [1, 0, 3, 12]
               b
                   a  # Swap again and so on    
    """

    behind = 0
    ahead = 0

    while ahead < len(nums):
        if nums[behind] == 0 and nums[ahead] != 0:
            nums[behind], nums[ahead] = nums[ahead], nums[behind]

        if nums[behind] != 0:
            behind += 1
        ahead += 1
 