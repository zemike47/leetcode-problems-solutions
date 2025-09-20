class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        def sumOfdigits(num):
            sum = 0
            while num >= 10:
                r = num % 10
                num //= 10
                sum += r
            
            sum += num
            return sum
        
        while num >= 10:
            num = sumOfdigits(num)

        return num
        