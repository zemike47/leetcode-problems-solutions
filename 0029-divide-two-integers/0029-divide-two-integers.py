class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Edge case overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1
            # Shift temp until it’s the largest multiple <= dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        return -quotient if negative else quotient
        