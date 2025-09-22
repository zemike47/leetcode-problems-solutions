class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        strnum = str(num)
        numOfdivisors = 0
        for i in range(len(strnum)):
            if i + k <= len(strnum) and int(strnum[i:i+k]) != 0:
                n = int(strnum[i:i+k])
                if num % n == 0:
                    numOfdivisors += 1
        
        return numOfdivisors


        