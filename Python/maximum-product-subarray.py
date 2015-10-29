class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        
        local_max = nums[0]
        local_min = nums[0]
        global_max = nums[0]
        
        for i in xrange(1, len(nums)):
            t_max = local_max
            t_min = local_min
            local_max = max(nums[i], t_max*nums[i], t_min*nums[i])
            local_min = min(nums[i], t_max*nums[i], t_min*nums[i])
            global_max = max(global_max, local_max)
            
        return global_max
