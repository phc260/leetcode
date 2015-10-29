class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        ans = []
        n = len(candidates)
        candidates.sort()
        
        def DFS(candidates, target, start, partial_sol):
            if target==0 and partial_sol not in ans:
                ans.append(partial_sol)
            for i in xrange(start, n):
                if target<candidates[i]: return
                if i==start or candidates[i-1]!=candidates[i]:
                    DFS(candidates, target-candidates[i], i+1, partial_sol+[candidates[i]])
        
        DFS(candidates, target, 0, [])
        return ans