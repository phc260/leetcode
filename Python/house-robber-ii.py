class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob1(self, num):
        n = len(num)
        even = odd = 0
        for i in xrange(n):
            #dp[i] = max(dp[i-1], dp[i-2]+num[i])
            if i%2==0:
                even = max(odd, even+num[i])
            else:
                odd = max(even, odd+num[i])

        return max(even, odd)
        
    def rob(self, nums):
        n = len(nums)
        if n==0: return 0
        if n==1: return nums[0]
        return max(self.rob1(nums[1:]), self.rob1(nums[:n-1]))
