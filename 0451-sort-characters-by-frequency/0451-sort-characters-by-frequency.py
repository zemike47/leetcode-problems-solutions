class Solution:
    def frequencySort(self, s: str) -> str:
        char_map = {}

        for c in s:
            if  c in char_map:
                char_map[c] += 1
            else:
                char_map[c] = 1
        
        char_map = dict(sorted(char_map.items(),key=lambda item : item[1],reverse = True))

        result = []

        for key , values in char_map.items():
            result.append(key * values)

        result = ''.join(result)

        return result
    





