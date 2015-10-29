class Solution:
    # @param s, a string
    # @return a list of lists of string
    def is_palindrome(self, s):
        n = len(s)
        for i in xrange(n/2):
            if s[i]!=s[n-1-i]:
                return False
        return True
        
    def DFS(self, s, sol, ans):
        n = len(s)
        if n<=0:
            ans.append(sol)
        else:
            for i in xrange(1, n+1):
                if self.is_palindrome(s[:i]):
                    self.DFS(s[i:], sol+[s[:i]], ans)
        
        
    def partition(self, s):
        ans = []
        self.DFS(s, [], ans)
        return ans