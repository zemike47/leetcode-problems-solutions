class Solution {
public:
    bool isValid(string s) {
        char arr[s.size()];
        int top = -1;  
        for (char ch : s) {
    
            if (ch == '(' || ch == '{' || ch == '[') {
                top++;  
                arr[top] = ch;  
            } 
            else {
                if (top < 0 || (ch == ')' && arr[top] != '(') || 
                              (ch == '}' && arr[top] != '{') || 
                              (ch == ']' && arr[top] != '[')) {
                    return false;
                }
                top--;  
            }
        } 
        return top == -1;
    }
};
