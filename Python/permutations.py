class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        n = len(nums)
        if n==0:
            return []
        if n==1:
            return [nums]
        ans = []
        for i in xrange(n):
            for j in self.permute(nums[0:i] + nums[i+1:n]):
                ans.append([nums[i]]+j)
                
        return ans
