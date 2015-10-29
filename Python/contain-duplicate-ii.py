class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        first_time = {}
        n = len(nums)
        
        for i in xrange(n):
            if nums[i] in first_time:
                if i-first_time[nums[i]]<=k: return True
            else: first_time[nums[i]] = i
        
        return False
