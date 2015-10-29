class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        
        n = len(nums)
        idx1 = idx2 = n-1
        
        for i in xrange(n-2, -1, -1):
            if nums[i]<nums[i+1]:
                idx1 = i
                break
        else:
            nums.reverse()
            return
                
        for i in xrange(n-1, -1, -1):
            if nums[i]>nums[idx1]:
                idx2 = i
                break
        
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
        
        start = idx1+1
        end = n-1
        
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
