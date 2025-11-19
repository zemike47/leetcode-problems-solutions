class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        arr = nums[:]

        while len(arr) > 1:
            new = []
            for i in range(len(arr) - 1):
                new.append((arr[i] + arr[i+1]) % 10)
            
            arr = new
        
        return arr[-1]