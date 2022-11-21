def find_all_good_indices(nums, k):
    l = len(nums)
    ans = []
    for i,n in enumerate(nums):
        if i >= k and i < l - k:
            print(f'Found Index {i}')
            next_items = nums[i+1:i + k + 1]
            past_items = nums[i-2:i]
            print(f'before subarr = {past_items}')
            print(f'next subarr = {next_items}')
            non_inc = True
            if past_items and len(past_items) > 1:
                idx = 1
                while idx < len(past_items):
                    if past_items[idx] > past_items[idx-1]:
                        non_inc = False
                        break
                    idx += 1
            #TODO: corner case len == 1
            
            non_dec = True
            if next_items and len(next_items) > 1:
                jdx = 1
                while jdx < len(next_items):
                    if next_items[jdx] < next_items[jdx-1]:
                        non_dec = False
                        break
                    jdx+=1
            if non_dec and non_inc:
                ans.append(i)
    return ans


# print(find_all_good_indices(nums = [2,1,1,1,3,4,1], k = 2))
print(find_all_good_indices(nums = [478184,863008,716977,921182,182844,350527,541165,881224], k = 1))
