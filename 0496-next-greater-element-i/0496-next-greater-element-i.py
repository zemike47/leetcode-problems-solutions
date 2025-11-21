class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        NGE = []
        

        for num in nums1:
            i = nums2.index(num)
            
            for j in range(i+1,len(nums2)):
                if nums2[j] > nums2[i]:
                    NGE.append(nums2[j])
                    break
            else:
                NGE.append(-1)

        
        return NGE



