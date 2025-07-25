class Solution:
  def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Reverse iterate from end of strings (least significant digit)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1

                # Add to previous stored result
                sum_ = mul + result[p2]
                result[p2] = sum_ % 10
                result[p1] += sum_ // 10

        # Skip leading zeros
        result_str = ''.join(map(str, result)).lstrip("0")
        return result_str or "0"
        