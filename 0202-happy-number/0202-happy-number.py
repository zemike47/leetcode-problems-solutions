class Solution:
    def isHappy(self, n: int) -> bool:
        s = []
        s.append(n)

        def check(n):

            newnum = 0
            while n > 0:
                r = n % 10
                newnum += r **2
                n = n // 10
            
        
            

            if newnum == 1:
                return True
            
            if newnum in s:
                return False
            else:
                s.append(newnum)
                return check(newnum)
        
        return check(n)
            

            
        
            

      