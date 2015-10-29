class Solution {
private:
    int rob(std::vector<int> &nums, int start, int end) {
        int dp[2] = {0, 0};
        int flag = 0;
        for(int i=start; i<end; ++i) {
            dp[flag] = std::max(dp[1-flag], dp[flag]+nums[i]);
            flag = 1-flag;
        }
        return std::max(dp[0], dp[1]);
    }
public:
    int rob(std::vector<int> &nums) {
        int n = nums.size();
        if(n==0) return 0;
        if(n==1) return nums[0];
        return std::max(rob(nums, 0, n-1), rob(nums, 1, n));
    }
};
