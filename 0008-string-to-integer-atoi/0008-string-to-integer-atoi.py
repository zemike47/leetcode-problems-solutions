class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Step 1: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # If all characters were spaces
        if i == n:
            return 0
        
        # Step 2: Handle optional sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1

        # Step 3: Convert digits to number
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        num *= sign

        # Step 4: Clamp to 32-bit signed integer range
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num
