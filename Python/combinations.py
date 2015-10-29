class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        def DFS(n, k, start, ans, partial):
            if len(partial)==k:
                ans.append(partial[:])
                return
            for i in xrange(start, n+1):
                partial.append(i)
                DFS(n, k, i+1, ans, partial)
                partial.pop()

        ans = []
        partial = []
        DFS(n, k, 1, ans, partial)
        
        return ans