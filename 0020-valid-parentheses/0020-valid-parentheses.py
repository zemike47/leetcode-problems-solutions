class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        char_map = {'}':'{',']':'[',')':'('}
        stack = []

        for c in s:
            if c in char_map.values():
                stack.append(c)
            else:
                if stack and stack[-1] == char_map[c]:
                    stack.pop()  
                else:
                    return False
                    

        

        return len(stack) == 0

