def dissappeared_numbers(nums):
    nums_copy = [n for n in range(1,len(nums) + 1)]
        
    nums_set = set(sorted(nums))
    nums_set_copy = set(nums_copy)
    
    a = nums_set_copy.difference(nums_set)
    ans = []
    for n in a:
        ans.append(n)
    return sorted(ans)