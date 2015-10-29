class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        def cmpstr(a, b):
            return -1 if a+b>b+a else 1
            
        num = sorted([str(x) for x in num], cmp = cmpstr)
        
        ans = ''.join(num).lstrip('0')
            
        return ans or '0'