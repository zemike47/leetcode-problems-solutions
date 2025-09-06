class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        left = 0
        right = 1
        result = ""

        while right < len(s):
            sub = s[left:right]
            len_sub = len(sub)
            n = len(s) // len_sub

            for i in range(n):
                result += sub

            if result == s:
                return True
            else:
                result = ""
                right += 1

        return False 

        