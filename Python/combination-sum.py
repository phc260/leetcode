class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        def DFS(candidates, start, target, partial):
            if target==0:
                ans.append(partial)
            for i in xrange(start, len(candidates)):
                if target < candidates[i]: return
                DFS(candidates, i, target-candidates[i], partial+[candidates[i]])

        candidates.sort()
        ans = []
        DFS(candidates, 0, target, [])
        return ans
