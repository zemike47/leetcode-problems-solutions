class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.split("-")
        s = ''.join(s)
        s = s.upper()

        len_FG = len(s) % k
        len_Group = len(s) // k

        result = ""

        if len_FG == 0:
            for i in range(0,len(s),k):
                result += s[i:k+i] + "-"
            
            return result[:-1]

        else:
            result += s[0:len_FG] + "-"
            for i in range(len_FG,len(s),k):
                result += s[i:k+i] + "-"
            
            return result[:-1]





        


        