class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        arr = [nums[0]]
        for n in nums[1:]:
            if n != arr[-1]:
                arr.append(n)
  

        for i in range(1,len(arr) - 1):
            if arr[i-1] < arr[i] > arr[i+1] or  arr[i-1]  > arr[i] < arr[i+1]:
                count += 1
            

        return count
            
