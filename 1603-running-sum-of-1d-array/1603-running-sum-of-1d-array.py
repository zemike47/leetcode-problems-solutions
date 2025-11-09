class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [0] * len(nums)
        runningSum[0] = nums[0]
        accumulater = nums[0]

        for i in range(1,len(nums)):
            accumulater += nums[i]
            runningSum[i] = accumulater

        return runningSum
            
        