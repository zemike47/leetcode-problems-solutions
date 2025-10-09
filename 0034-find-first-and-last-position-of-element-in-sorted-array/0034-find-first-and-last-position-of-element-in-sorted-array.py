class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]

        output = []

        postion = nums.index(target)
        output.append(postion)

        arr = nums[::-1]
        postion = len(arr) -  arr.index(target) - 1
        output.append(postion)

        return output




        
        