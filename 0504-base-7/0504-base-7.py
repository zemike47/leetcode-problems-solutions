class Solution:
    def convertToBase7(self, num: int) -> str:
        output = ""
        n = abs(num)

        while n >= 7:
            r = n % 7
            n = n // 7 
            output += str(r)

        output += str(n)
        revoutput = []
        revoutput[:] = output[::-1] 
        revoutput = ''.join(revoutput)

        if num < 0:
            revoutput = "-" + revoutput
            return revoutput
        else:
            return revoutput