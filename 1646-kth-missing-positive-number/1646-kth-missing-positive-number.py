class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ptr = 0
        for i in range(1,arr[-1]):
            if i != arr[ptr]:
                k -= 1
                if k == 0:
                    return i
            else:
                ptr += 1
        
        return arr[-1] + k
        
    
        
