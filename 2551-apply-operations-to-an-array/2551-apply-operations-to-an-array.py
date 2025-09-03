class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left = 0 
        right = 1
        size = len(nums)

       
        while right < size:


            if nums[left] == nums[right]:
                nums[left] = nums[left] * 2
                nums[right] = 0

            left += 1
            right += 1

        for i in range(size-1,-1,-1):
            if nums[i] != 0:
                continue

            
            
            temp_idx1 = i
            temp_idx2 = i + 1


           

            while temp_idx2 < size:
                nums[temp_idx1] , nums[temp_idx2] = nums[temp_idx2] , nums[temp_idx1]
                temp_idx1 += 1 
                temp_idx2 += 1

        return nums

