class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0
        while math.pow(4,i) <= n:
            if math.pow(4,i) == n:
                return True

            i += 1
        
        return False
        