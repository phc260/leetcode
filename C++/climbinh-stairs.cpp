class Solution {
public:
    int climbStairs(int n) {
        int dp[2] = {1, 1};
        int flag = 0;
        for(int i=2; i<=n; ++i) {
            dp[flag] = dp[1-flag]+dp[flag];
            flag = 1-flag;
        }
        return dp[1-flag];
    }
};

