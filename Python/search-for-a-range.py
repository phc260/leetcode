class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        def binary_search(start, end):
            if start<end:
                mid = (start+end)/2
                if nums[mid]==target: return mid
                elif target<nums[mid]: return binary_search(start, mid)
                else: return binary_search(mid+1, end)
            return -1
        
        n = len(nums)
        idx = binary_search(0, n)
        
        if idx==-1:
            return [-1, -1]
        else:
            i = idx-1
            j = idx+1
            
            while i>=0 and nums[i]==nums[idx]:
                i -= 1
                
            while j<n and nums[j]==nums[idx]:
                j += 1
                
            return [i+1, j-1]
