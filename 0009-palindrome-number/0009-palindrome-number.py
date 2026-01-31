class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        reversed_x = 0

        strX = str(x)

        p = len(strX) - 1

        num = x

        while x > 0:
            r = x % 10
            reversed_x += r * (10**p)
            x = x // 10
            p -= 1
        
        x = num

        return reversed_x == x
        



        