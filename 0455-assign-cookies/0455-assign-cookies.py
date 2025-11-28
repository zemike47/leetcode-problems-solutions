class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        j = 0
        i = 0

        count = 0

        while j < len(s) and i < len(g):
            if s[j] >= g[i]:
                count += 1
                j += 1
                i += 1
            else:
                j += 1
        
        return count
                

