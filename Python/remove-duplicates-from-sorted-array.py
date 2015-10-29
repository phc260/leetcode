class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        m = n = len(nums)
        i = 0
        j = 1
        while j<n:
            if nums[i] != nums[j]:
                 i += 1
                 nums[i] = nums[j]
            else:
                m -= 1
            j += 1
        
        return m