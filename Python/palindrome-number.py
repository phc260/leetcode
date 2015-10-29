class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        def reverse(x):
        	x = abs(x)
        	y = 0
        	while x:
        		
        		y = y*10 + x%10
        		x /= 10
        		
        	return y
        return x==reverse(x)