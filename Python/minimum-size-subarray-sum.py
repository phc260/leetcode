INT_MAX = 2147483647
class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    
    def minSubArrayLen(self, s, nums):
        if not nums: return 0
        
        n = len(nums)
        for i in xrange(1, n): nums[i]+=nums[i-1]
        if nums[n-1]<s: return 0
        
        i = j = 0
        min_len = INT_MAX
        while i<n and nums[i]<s:
            i += 1
        
        while i<n:
            while j<i and nums[i]-nums[j]>=s:
                j += 1
            min_len = min(min_len, i-j+1)
            i += 1
            
        return min_len
