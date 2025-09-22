class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        count = 0
        for i in range(len(s)):
            sub_str = s[i:i+3]
            uniq_chars = set(sub_str)
            if len(uniq_chars) == 3:
                count += 1
            
        return count