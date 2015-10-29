class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        def DFS(start, k, n, partial_sol):
            if n<0: return
            if k==0 and n==0:
                ans.append(partial_sol)
            else:
                for i in xrange(start, 10):
                    DFS(i+1, k-1, n-i, partial_sol+[i])
                    
        ans = []
        DFS(1, k, n, [])
        return ans
