from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        num_map = Counter(arr1)

        result = []

        for num in arr2:
            result.extend([num]* num_map[num])
        
        for num in arr1:
            if num not in result:
                result.extend([num]* num_map[num])

        return result