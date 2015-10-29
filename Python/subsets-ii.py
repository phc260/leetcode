class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def make(self, S, idx, ans, sol):
        n = len(S)
        i = idx
        while i<n:
            sol.append(S[i])
            ans.append(sol[:])
            self.make(S, i+1, ans, sol)
            sol.pop()
            while i<n-1 and S[i]==S[i+1]: i+=1
            i += 1
            
            
    def subsetsWithDup(self, S):
        sol = []
        ans = [[]]
        S.sort()
        self.make(S, 0, ans, sol)
        
        return ans