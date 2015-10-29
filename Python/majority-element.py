class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        candidate = 0
        count = 0
        for n in nums:
            if count==0:
                candidate = n
                count = 1
            elif candidate==n:
                count += 1
            else:
                count -= 1
        return candidate
