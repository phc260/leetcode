class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False]*n
        for i in xrange(n-1,-1,-1):
            if s[i:n] in wordDict:
                dp[i] = True
            else:
                for j in xrange(i+1, n):
                    if dp[j] and s[i:j] in wordDict:
                        dp[i] = True
                        break
        return dp[0]