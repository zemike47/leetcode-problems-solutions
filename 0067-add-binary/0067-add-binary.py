class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        
        i = len(a) - 1
        j = len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            # Append the current bit (0 or 1)
            result.append(str(total % 2))
            # Calculate new carry
            carry = total // 2
        
        # The result is built in reverse order
        return ''.join(reversed(result))