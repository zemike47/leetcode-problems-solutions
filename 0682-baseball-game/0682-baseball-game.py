class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for ops in operations:
            if ops == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                Sum = n1 + n2
                stack.append(n2)
                stack.append(n1)
                stack.append(Sum)

            elif ops == "D":
                top = stack.pop()
                double = 2 * top
                stack.append(top)
                stack.append(double)
            
            elif ops == "C":
                stack.pop()
                
            else:
                num = int(ops)
                stack.append(num)
            

        return sum(stack)






                

