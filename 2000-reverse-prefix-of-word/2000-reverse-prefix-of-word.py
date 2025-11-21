class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        idx = 0
        if ch not in word:
            return word

        # append elements
        for i,c in enumerate(word):
            if c != ch:
                stack.append(c)
            else:
                stack.append(c)
                idx = i
                break
            
        
        reverseWord = ""

        for i in range(len(stack)-1,-1,-1):
            reverseWord += stack[i]

        idx += 1
        while idx < len(word):
            reverseWord += word[idx]
            idx += 1

        
        return reverseWord



        
        

            