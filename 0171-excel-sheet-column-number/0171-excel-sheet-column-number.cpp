class Solution {
public:
    int titleToNumber(string columnTitle) {
        int result = 0;
        
        for (char ch : columnTitle) {
            // Convert character to its corresponding number: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26
            int value = ch - 'A' + 1;
            result = result * 26 + value;
        }
        
        return result;
    }
};
