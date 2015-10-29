class Solution:
    # @param nums, a list of integer
    # @return an integer
    def rob(self, nums):
        n = len(nums)
        dp = [0, 0]
        flag = 0
        for i in xrange(n):
            dp[flag] = max(dp[1-flag], dp[flag]+nums[i])
            flag = 1-flag
        return max(dp)