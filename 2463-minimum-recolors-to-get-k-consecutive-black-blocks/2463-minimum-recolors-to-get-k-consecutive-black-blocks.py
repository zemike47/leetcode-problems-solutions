class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minm = float("inf")
        
        i = 0
        while i + k <= len(blocks):
            substr = Counter(blocks[i:i+k])
            minm = min(minm,substr['W'])
            i += 1
        
        return minm
        