class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = []
        total_sum = 0

        for i in range(len(nums)):
            total_sum += nums[i]
            prefix_sum.append(total_sum)
        
        return prefix_sum