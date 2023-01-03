class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        seen_averages = {}
        while nums:
            first, last = nums[0], nums[-1]
            cur_average = (first + last) / 2
            if cur_average not in seen_averages:
                seen_averages[cur_average] = True
            nums.pop(0)
            nums.pop(-1)
        return len(list(seen_averages.keys()))
