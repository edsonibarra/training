def average_value(nums):
    is_divisible_by_3 = []
    for n in nums:
        if n % 3 == 0 and n % 2 == 0:
            is_divisible_by_3.append(n)
    if is_divisible_by_3:
        
        return sum(is_divisible_by_3) // len(is_divisible_by_3)
    return 0
    