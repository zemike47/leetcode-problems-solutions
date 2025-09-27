class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {'(':')',"[":"]","{":"}"}

        for parentheses in s:
            if parentheses in valid:
                stack.append(parentheses)
            else:
                if not stack:
                    return False
                
                top = stack.pop()
                if parentheses != valid[top]:
                    return False
            
        else:
            return not stack
                
        
        