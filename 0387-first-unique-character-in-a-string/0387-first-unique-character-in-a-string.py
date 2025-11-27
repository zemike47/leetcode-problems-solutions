class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniq_char = {}

        for c in s:
            if c in uniq_char:
                uniq_char[c] += 1
            else:
                uniq_char[c] = 1
        
        for i in range(len(s)):
            if uniq_char[s[i]] == 1:
                return i
        else:
            return -1
