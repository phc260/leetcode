class Solution {
public:
    bool wordBreak(std::string s, unordered_set<std::string>& wordDict) {
        int n = s.size();
        bool dp[n] = {false};
        for(int i=n-1; i>-1; --i) {
            if(wordDict.find(s.substr(i, n))!=wordDict.end()) {
                dp[i] = true;
            }
            else {
                for(int j=1; j<n; ++j) {
                    if(dp[j] && wordDict.find(s.substr(i, j-i))!=wordDict.end()) {
                        dp[i] = true;
                        break;
                    }
                }
            }
        }
        return dp[0];
    }
};

