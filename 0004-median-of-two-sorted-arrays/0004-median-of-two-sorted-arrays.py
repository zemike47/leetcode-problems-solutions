class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        
        nums.sort()

        length = len(nums)

        if length % 2 == 0:
            i = int((length / 2) - 1)
            median = (nums[i] + nums[i+1]) / 2

            return float(median)
        
        else:
            i = int((length // 2))
            median = nums[i]

            return float(median)


        

        