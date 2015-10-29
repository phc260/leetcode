class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        dp = [1, 1]
        flag = 0
        for i in xrange(2, n+1):
            dp[flag] = dp[1-flag] + dp[flag]
            flag = 1- flag
        return dp[1-flag]
