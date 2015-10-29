class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        n = len(nums)
        jumps = last = curr = 0
        for i in xrange(n):
            if i>last:
                last = curr
                jumps += 1
            curr = max(curr, nums[i]+i)
        return jumps
