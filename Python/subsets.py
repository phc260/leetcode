class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        partial = []
        ans = [[]]
        def DFS(start):
            for i in xrange(start, len(nums)):
                partial.append(nums[i])
                ans.append(partial[:])
                DFS(i+1)
                partial.pop()
        nums.sort()
        DFS(0)
        return ans
