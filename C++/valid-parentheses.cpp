class Solution {
public:
    bool isValid(std::string s) {
        std::stack<char> stk;
        std::unordered_map<char, char> hashmap{{')','('}, {']', '['}, {'}', '{'}};
        for(char c : s) {
            if(hashmap.find(c)==hashmap.end()) {
                stk.push(c);
            }
            else {
                if(!stk.empty() && stk.top()==hashmap[c])
                    stk.pop();
                else
                    return false;
            }
        }
        return stk.empty();
    }
};

