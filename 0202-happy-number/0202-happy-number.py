class Solution:
    def isHappy(self, n: int) -> bool:
        def totalsumcal(num:int) -> int:
            totalSum = 0
            while num > 0:
                r = num % 10
                num = num // 10
                totalSum += r ** 2

           
            return totalSum
        
        numbers = set()
      
        while n != 1:
            if n in numbers:
                return False
            
            numbers.add(n)
            n = totalsumcal(n)
                  
        return n == 1
        
        

     
        
  


    


        



        
        