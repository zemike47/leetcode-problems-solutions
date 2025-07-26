class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        
        for i, jump in enumerate(nums):
            if i > max_reach:
                # Cannot reach current position
                return False
            
            max_reach = max(max_reach, i + jump)
            
            if max_reach >= len(nums) - 1:
                return True
        
        return True