def difference(nums):
    total_nums_sum = sum(nums)
    nums_str = "".join(map(str, nums))
    digits_sum = 0
    for c in nums_str:
        digits_sum += int(c)
    return abs(total_nums_sum - digits_sum)
