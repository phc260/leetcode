class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        def reverse(start, end):
            end -= 1
            while start<end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
                
        n = len(nums)
        k %= n
        
        reverse(0, n)
        reverse(0, k)
        reverse(k, n)