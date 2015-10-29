class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        ans = 0
        for i in nums: ans^=i
        return ans
