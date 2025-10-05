class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        maxArea = 0

        while left < right:
            Area = abs(right - left) * min(height[right],height[left])


            maxArea = max(maxArea,Area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea

            









        