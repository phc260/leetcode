class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        while True:
            try:
                nums.remove(val)
            except:
                break
                    
        return len(nums)
