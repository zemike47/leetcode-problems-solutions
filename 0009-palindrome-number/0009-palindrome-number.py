class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_num = 0
        length = 0
        
        num = x

        
        while num > 0:
            num = num // 10
            length += 1

        num = x
        length -= 1

        while num > 0:
            remainder = num % 10
            reverse_num = reverse_num + remainder * pow(10,length)
            num = num // 10
            
            length -= 1

        return reverse_num == x

        

        