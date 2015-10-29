class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        colors = [0, 0, 0]
        flag = 0
        for n in nums:
            colors[n] += 1
        for i in xrange(len(nums)):
            while colors[flag]<=0:
                flag += 1
            nums[i] = flag
            colors[flag] -= 1