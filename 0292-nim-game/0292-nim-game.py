class Solution:
    def canWinNim(self, n: int) -> bool:
        if (n - 1) % 4 == 0:
            return True
        elif (n - 2) % 4 == 0:
            return True
        elif (n - 3) % 4 == 0:
            return True
        else:
            return False
        
        