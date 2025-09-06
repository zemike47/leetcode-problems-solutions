class Solution:
    def reverseVowels(self, s: str) -> str:
        v = "aeiouAEIOU"
        vstr = ""

        for ch in s:
            if ch in v:
                vstr += ch

        vstr = vstr[::-1]
        result = ""
        j = 0

        for i in range(len(s)):
            if s[i] in vstr:
                result += vstr[j]
                j += 1
            else:
                result += s[i]

        return result
            
        
            







        