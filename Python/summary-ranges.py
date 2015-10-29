class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        n = len(nums)
        i = 0
        ans = []
        while i<n:
            start = end = i
            while end+1<n and nums[end]+1==nums[end+1]: end += 1
            if start<end: ans.append(str(nums[start])+'->'+str(nums[end]))
            else: ans.append(str(nums[start]))
            i = end+1
        return ans

