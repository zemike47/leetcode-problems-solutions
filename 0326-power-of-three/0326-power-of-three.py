class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 0
        while math.pow(3,i) <= n:
            if math.pow(3,i) == n:
                return True
            i += 1

        return False
        