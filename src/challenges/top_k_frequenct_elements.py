from abc import ABC, abstractmethod


class Solution(ABC):
    @abstractmethod
    def solve(*args):
        pass


class KthFrequentElements(Solution):
    def solve(self, nums, k):
        return self.k_frequent_elements(nums, k)

    def get_frequency(self, nums):
        frequencies = {}
        for n in nums:
            frequencies[n] = frequencies.get(n, 0) + 1
        return frequencies

    def convert_and_sort(self, frequencies):
        value_key_frequencies = []
        for key, value in frequencies.items():
            value_key_frequencies.append((value, key))
        return sorted(value_key_frequencies, reverse=True)

    def k_frequent_elements(self, nums, k):
        frequencies = self.get_frequency(nums)
        sorted_frequencies = self.convert_and_sort(frequencies)
        most_k_frequent = self.get_k_frequent(sorted_frequencies, k)
        return most_k_frequent

    def get_k_frequent(self, freq, k):
        ans = []
        for i in range(k):
            ans.append(freq[i][1])
        return ans


problem = KthFrequentElements()
print(problem.solve([1,1,1,2,2,3],2))
print(problem.solve([1],1))