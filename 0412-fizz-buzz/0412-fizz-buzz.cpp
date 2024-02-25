class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> strarray;
        for(int i = 1; i <= n ; i++){
            
          if(i % 3 == 0 && i % 5 == 0){
            strarray.push_back("FizzBuzz");
        }
          else if(i % 5 == 0){
              strarray.push_back("Buzz");
    
        }
          else if(i % 3 == 0){
              strarray.push_back("Fizz");
           
        }
            else{
             
               strarray.push_back(to_string(i));  
            }
    }
        
        return strarray;
    }
};