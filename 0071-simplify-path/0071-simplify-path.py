class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []

        for p in paths:
            if p == "..":
                if stack:
                    stack.pop()
                else:
                    continue
                    
            elif p == "." or p == "/" or p == '':
                continue
            else:
                stack.append(p)
            
        return "/"+"/".join(stack)
        




       