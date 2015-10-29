class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        n = len(s)
        dp = [0]*(n+1)
        max_len = 0
        for i in xrange(n):
            j = i-1-dp[i]
            if s[i]=='(' or j<0 or s[j]==')':
                dp[i+1] = 0
            else:
                dp[i+1] = dp[i]+dp[j]+2
                max_len = max(max_len, dp[i+1])
        return max_len
