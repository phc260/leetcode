class Solution {
public:
    int rob(std::vector<int> &nums) {
        int dp[2] = {0, 0};
        int flag = 0;
        for(int i=0; i<nums.size(); ++i) {
            dp[flag] = std::max(dp[1-flag], dp[flag]+nums[i]);
            flag = 1-flag;
        }
        return std::max(dp[0], dp[1]);
    }
};
