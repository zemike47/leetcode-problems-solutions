class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if i + 3 <= len(nums):
                    j = i
                    while j < 3 + i:
                        if nums[j] == 0:
                            nums[j] = 1
                        else:
                            nums[j] = 0
                        j += 1
                    
                    count += 1
        
        if 0 in nums:
            return -1
        else:
            return count

                    
                    

                    


                    
                
                

                
            

