class Solution {
public:
    int titleToNumber(std::string s) {
        int n = 0;
        for(char c : s) {
            n = n*26+c-'A'+1;
        }
        return n;
    }
};

