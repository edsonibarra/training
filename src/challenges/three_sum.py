class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        nums.sort()
        print(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                if total_sum == 0:
                    t = [nums[i], nums[left], nums[right]]
                    if t not in triplets:
                        triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                elif total_sum < 0:
                    left += 1
                elif total_sum > 0:
                    right -= 1
                # if total_sum > 0:
                #     right -= 1
                # elif total_sum < 0:
                #     left += 1
                # else:
                #     t = [nums[i], nums[left], nums[right]]
                #     if t not in triplets:
                        
                #         triplets.append([nums[i], nums[left], nums[right]])
                #         left += 1
                #         right -= 1

        return triplets