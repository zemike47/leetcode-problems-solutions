class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if i == 0 :
                if sum(nums[1:len(nums)]) == 0:
                    return 0
            elif i == len(nums) - 1:
                if sum(nums[:len(nums)-1]) == 0:
                    return i
            else:
                if sum(nums[:i]) == sum(nums[i+1:]):
                    return i           
        else:
            return -1
                
           




        