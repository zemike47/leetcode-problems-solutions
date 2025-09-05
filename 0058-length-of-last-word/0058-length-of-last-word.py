class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        slist = s.split()

        lastword = slist[-1]

        return len(lastword)
