from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num_map = Counter(nums)

        num_map = dict(sorted(num_map.items(),key = lambda item : (item[1],-item[0])))

        result = []

        for key , values in num_map.items():
            result.extend([key] * values)

        return result

