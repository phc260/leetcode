class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def __init__(self):
        self.ans = []
        
    def is_word_break(self, s, wordDict):
        n = len(s)
        dp = [False]*n
        for i in xrange(n-1,-1,-1):
            if s[i:] in wordDict:
                dp[i] = True
            else:
                for j in xrange(i+1, n):
                    if dp[j] and s[i:j] in wordDict:
                        dp[i] = True
                        break
        return dp[0]
    
    def DFS(self, s, wordDict, partial):
        if len(s)==0:
            self.ans.append(partial[1:])
            return
        if self.is_word_break(s, wordDict):
            for i in xrange(1, len(s)+1):
                if s[:i] in wordDict:
                    self.DFS(s[i:], wordDict, partial+' '+s[:i])
        
    def wordBreak(self, s, wordDict):
        self.DFS(s, wordDict, '')
        return self.ans