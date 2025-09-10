class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x <  10:
            return True
        
        num = x
        revr_num = ""

        while num >= 10:
            r = num % 10
            num //= 10

            revr_num += str(r)

        revr_num += str(num)

        revr_num = int(revr_num)

        return revr_num == x

        